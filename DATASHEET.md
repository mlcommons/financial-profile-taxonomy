# Datasheet: MLCommons Agent Reliability Profile Taxonomy

Documentation following the "Datasheets for Datasets" framework (Gebru et al., 2021), adapted for a taxonomy.

## Motivation

**For what purpose was the taxonomy created?** To give financial institutions, vendors, independent assessors, and regulators a shared, standardized vocabulary for stating what a deployed AI agent is permitted to do, how autonomously, in what context, and with what containment, in a form that can be tested, independently validated, and compared.

**What gap does it fill?** No published standard specifies how to state the operating boundary of a deployed agent. Each deployer defines bounds idiosyncratically, governance and security tools each use their own schemas, and supervisors have limited ability to compare deployments or identify outliers across firms.

**Who created it?** The MLCommons Financial Services Working Group. The underlying architecture is described in Hsu, Bankhwal, Moissinac, Werbach, Szpruch, and Hillenbrand, "Agent Reliability Profiles in Financial Services" (preprint, September 2026).

## Composition

**What does the taxonomy contain?**

| Component | Count | Source file |
|---|---|---|
| Autonomy tiers | 5 (T0–T4) + residual status U | `taxonomy/taxonomy.yaml` |
| Cross-cutting modifiers | 6 | `taxonomy/taxonomy.yaml` |
| ODD lines of business | 8 | `taxonomy/taxonomy.yaml` |
| ODD candidate use cases | 52 (open set) | `taxonomy/taxonomy.yaml` |
| ODD multiplying factors | 4 (25 values) | `taxonomy/taxonomy.yaml` |
| Action classes | 12 | `taxonomy/taxonomy.yaml` |
| Control layers | 6 | `taxonomy/taxonomy.yaml` |
| Named controls | 55 | `taxonomy/taxonomy.yaml` |
| Platform properties | 6 | `taxonomy/taxonomy.yaml` |
| Profile sections | 10 | `taxonomy/profile.yaml` |
| Assurance levels | 3 + benchmark comparability flag | `taxonomy/profile.yaml` |
| Worked examples | 2 | `taxonomy/examples.yaml` |

**Does it contain data about real deployments or individuals?** No. The taxonomy is an option universe. Worked examples are illustrative. Use-case names describe categories of activity, not specific institutions.

**Is anything missing?** Per-control definitions, configuration parameters, and control-level crosswalk mappings; value scales for four of the six modifiers; and jurisdiction-specific mappings. These are documented as open work.

## Collection Process

The axes and their values were developed by the working group from safety-engineering precedents (SAE J3016, the EASA AI Concept Paper, ISO 10218, ASTM F3269), existing AI risk frameworks (NIST AI RMF, EU AI Act, CRI Profile, ISO/IEC 42001, OWASP), the human-factors literature on automation, and practitioner input from working-group members. The fifty-two use cases were identified by the working group and are preliminary.

## Preprocessing

The YAML sources were transcribed from the preprint and the companion one-pager ("The Agent Reliability Profile Taxonomy," October 2026). Canonical IDs were assigned for this repository. Where the two sources differ, the companion one-pager's grouping of lines of business was followed (see CHANGELOG).

## Uses

**Intended uses:**

- Describing agent deployments consistently across business units and institutions
- Compiling Level 1 Asserted Profiles for agent inventories
- Structuring Level 2/3 test plans (the four axes jointly fix the test environment, evaluator suite, failure thresholds, and wording of the claim)
- Supervisory comparison and outlier identification
- Building conforming tools against canonical IDs

**Uses to avoid:**

- Treating a Profile described in these terms as a certification; the taxonomy does not assess anything
- Converting axis values into a composite score; the Profile keeps metrics disaggregated and floors are pass/fail
- Treating the control catalogue as a mandatory checklist; on the control axis the Profile is descriptive
- Applying the ODD catalogue outside financial services without domain-expert adaptation
- Relying on the Profile for fairness, explainability, data governance, consumer compliance, or cybersecurity adequacy

## Distribution

Distributed via GitHub under CC-BY-4.0, with a documentation site built by MkDocs. Machine-readable YAML is the authoritative form; Markdown tables are generated from it.

## Maintenance

Maintained by the MLCommons Financial Services Working Group under semantic versioning, with tagged snapshots in `releases/`. Pilot feedback is expected to revise the axes and their values; publishing the updated taxonomy marks the end of the pilot phase. See [CONTRIBUTING.md](CONTRIBUTING.md) and [governance/review-process.md](governance/review-process.md).
