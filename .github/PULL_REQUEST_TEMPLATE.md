## Contribution type

- [ ] New ODD use case
- [ ] New control, control definition, or crosswalk mapping
- [ ] Worked example
- [ ] Documentation fix
- [ ] Taxonomy structure change (tier, modifier, action class, layer, line of business, platform case, profile vocabulary)

## Description

What changed and why?

## Related issue

Closes # (or "None" for small fixes)

## What files were changed?

For YAML changes, confirm you ran `python scripts/generate_tables.py` and committed the regenerated Markdown.

## Evidence

Link to supporting deployments, supervisory experience, frameworks, or discussion. For taxonomy structure changes, include a completed [taxonomy structure template](TAXONOMY_STRUCTURE_TEMPLATE.md).

## Checklist

- [ ] `python scripts/generate_tables.py --check` and `python scripts/export_vocab.py --check` pass
- [ ] No existing canonical IDs were renumbered or reused
- [ ] No confidential institutional configuration, customer data, or credentials included
- [ ] I have reviewed existing entries to avoid duplicates
- [ ] I understand this taxonomy is CC-BY-4.0 licensed and my contribution will be openly available
