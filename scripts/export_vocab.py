#!/usr/bin/env python3
"""Export the taxonomy as Agent Reliability Profile Kit vocabulary files.

The taxonomy repository is the source of truth for the four axes. The Profile
Kit consumes them as JSON vocabularies (spec/vocab/*.json). This script writes
the taxonomy-owned vocabularies in the Kit's format to vocab/, and can compare
them with a Kit release.

Exported (taxonomy-owned fields only):
  autonomy-tiers.json     tiers T0-T4, status U, six modifiers
  business-lines.json     nine business lines
  use-cases.json          ODD.1-ODD.52 with business line
  action-classes.json     A1-A12 with reversibility code
  control-catalogue.json  55 controls with layer and ordinal

Kit-owned vocabularies (provenance classes, invalidation triggers,
dispositions, conflict kinds, peer-control sets) and Kit-only fields (e.g.
evidence_requirement, candidates_v1_1) are not exported; they stay in the Kit.

Usage:
  python scripts/export_vocab.py                       # write vocab/
  python scripts/export_vocab.py --check               # exit 1 if vocab/ is stale (CI)
  python scripts/export_vocab.py --compare <kit>/spec/vocab
      Exit 1 if any ID or structural assignment differs from the Kit;
      label and definition differences are listed for information.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "vocab"


def norm(s: str) -> str:
    return " ".join(str(s).split())


def build() -> dict[str, dict]:
    tax = yaml.safe_load((ROOT / "taxonomy" / "taxonomy.yaml").read_text(encoding="utf-8"))
    ver = tax["taxonomy_version"]
    ax = {a["id"]: a for a in tax["axes"]}
    at, odd, ac, ce = (ax[k] for k in ("autonomy-tier", "operational-design-domain", "action-class", "control-envelope"))

    def head(name: str) -> dict:
        return {"vocabulary": f"arp-taxonomy/{ver}/{name}", "version": ver,
                "source": "mlcommons/financial-profile-taxonomy, taxonomy/taxonomy.yaml (generated)"}

    u = at["residual_status"]
    tiers = [{"id": t["id"], "label": t["name"], "agent": norm(t["does"]), "fallback": norm(t["fallback"])}
             for t in at["tiers"]]
    tiers.append({"id": u["id"], "label": f"{u['name']} (status, not a tier)", "agent": norm(u["description"]),
                  "fallback": norm(f"{u['fallback']} {u['consequence']}")})
    mods = []
    for m in at["modifiers"]["values"]:
        d = {"id": m["id"], "label": m["name"], "definition": norm(m["description"])}
        if "values" in m:
            d["values"] = m["values"]
        mods.append(d)

    bls = odd["business_lines"]
    out = {
        "autonomy-tiers.json": {**head("autonomy-tiers"), "terms": tiers, "modifiers": mods},
        "business-lines.json": {**head("business-lines"),
                                "note": "The ODD is an open set; only its schema and top-level business lines are standardised.",
                                "terms": [b["id"] for b in bls], "labels": {b["id"]: b["name"] for b in bls}},
        "use-cases.json": {**head("use-cases"),
                           "note": "An open set: ODD.x_<name> marks an extension.",
                           "terms": sorted(({"id": c["id"], "business_line": b["id"], "label": c["name"]}
                                            for b in bls for c in b["use_cases"]),
                                           key=lambda t: int(t["id"].split(".")[1]))},
        "action-classes.json": {**head("action-classes"),
                                "terms": [{"id": c["id"], "label": c["name"], "reversibility": c["reversibility_code"]}
                                          for c in ac["classes"]]},
        "control-catalogue.json": {**head("control-catalogue"),
                                   "layers": [l["id"] for l in ce["layers"]],
                                   "terms": [{"id": c["id"], "layer": l["id"], "ordinal": i, "label": c["name"]}
                                             for l in ce["layers"] for i, c in enumerate(l["controls"], start=1)]},
    }
    return out


def dump(d: dict) -> str:
    return json.dumps(d, indent=2, ensure_ascii=False) + "\n"


STRUCTURAL = {  # fields whose mismatch is an error, per file
    "autonomy-tiers.json": [],
    "business-lines.json": [],
    "use-cases.json": ["business_line"],
    "action-classes.json": ["reversibility"],
    "control-catalogue.json": ["layer", "ordinal"],
}


def compare(mine: dict[str, dict], kit_dir: Path) -> int:
    errors, notes = [], []
    for fname, ours in mine.items():
        path = kit_dir / fname
        if not path.exists():
            errors.append(f"{fname}: missing from Kit")
            continue
        theirs = json.loads(path.read_text(encoding="utf-8"))
        if fname == "business-lines.json":
            if ours["terms"] != theirs["terms"]:
                errors.append(f"{fname}: business-line IDs or order differ: {ours['terms']} vs {theirs['terms']}")
            for k, v in ours["labels"].items():
                if theirs.get("labels", {}).get(k) != v:
                    notes.append(f"{fname} {k}: label '{v}' (taxonomy) vs '{theirs.get('labels', {}).get(k)}' (Kit)")
            continue
        groups = [("terms", ours["terms"], theirs.get("terms", []))]
        if fname == "autonomy-tiers.json":
            groups.append(("modifiers", ours["modifiers"], theirs.get("modifiers", [])))
        for gname, a, b in groups:
            ia, ib = [t["id"] for t in a], [t["id"] for t in b]
            if ia != ib:
                only_a, only_b = sorted(set(ia) - set(ib)), sorted(set(ib) - set(ia))
                errors.append(f"{fname} {gname}: IDs differ" + (f"; only in taxonomy: {only_a}" if only_a else "")
                              + (f"; only in Kit: {only_b}" if only_b else "")
                              + ("; order differs" if not only_a and not only_b else ""))
            bmap = {t["id"]: t for t in b}
            for t in a:
                o = bmap.get(t["id"])
                if not o:
                    continue
                for f in STRUCTURAL[fname]:
                    if t.get(f) != o.get(f):
                        errors.append(f"{fname} {t['id']}: {f} '{t.get(f)}' (taxonomy) vs '{o.get(f)}' (Kit)")
                for f, v in t.items():
                    if f in ("id",) or f in STRUCTURAL[fname]:
                        continue
                    if norm(json.dumps(v)) != norm(json.dumps(o.get(f))):
                        notes.append(f"{fname} {t['id']}.{f}: taxonomy {json.dumps(v, ensure_ascii=False)} | Kit {json.dumps(o.get(f), ensure_ascii=False)}")
    for e in errors:
        print(f"MISMATCH  {e}")
    for n in notes:
        print(f"label     {n}")
    print(f"\n{len(errors)} ID/structure mismatch(es); {len(notes)} label/definition difference(s).")
    return 1 if errors else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if vocab/ is out of date")
    ap.add_argument("--compare", metavar="KIT_VOCAB_DIR", help="compare with a Kit's spec/vocab directory")
    args = ap.parse_args()
    mine = build()
    if args.compare:
        return compare(mine, Path(args.compare))
    stale = [f for f, d in mine.items() if not (OUT / f).exists() or (OUT / f).read_text(encoding="utf-8") != dump(d)]
    if args.check:
        if stale:
            print(f"vocab/ out of date: {stale}. Run: python scripts/export_vocab.py", file=sys.stderr)
            return 1
        print("vocab/ is up to date.")
        return 0
    OUT.mkdir(exist_ok=True)
    for f, d in mine.items():
        (OUT / f).write_text(dump(d), encoding="utf-8")
    print(f"Wrote {len(mine)} vocabulary files to vocab/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
