# Changelog

All notable changes to the MLCommons Agent Reliability Profile Taxonomy are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-10-29

### Added
- Initial draft-for-comment release of the four-axis Agent Reliability Profile taxonomy for financial services
- Axis 1, Autonomy Tier: five tiers (T0–T4), residual status U, six cross-cutting modifiers, T2/T3 and T3/T4 watchpoints, and evidence indicators for T2, T3, and T4
- Axis 2, Operational Design Domain: open set of 52 candidate use cases across 8 lines of business, with 4 multiplying factors (customer population, data sensitivity, cost of failure, jurisdiction)
- Axis 3, Action Class: 12 classes (A1–A12) graded by reversibility and consequence, recorded as a permitted set A+ and prohibited set A-
- Axis 4, Control Envelope: 55 named controls across 6 layers (model, tool, harness, environment, inter-agent, control plane)
- Cross-axis case for agent-building platforms: Platform Baseline Profile, platform anchor, and six required properties (P1–P6)
- `taxonomy/profile.yaml`: Profile sections, provenance types, floors, assurance Levels 1–3, benchmark comparability flag, headline-level rule, invalidation triggers, and Profile Package contents
- `taxonomy/examples.yaml`: two worked bounded claims (coding agent; financial-crime alert-triage agent) with proposed action-class and control mappings
- Canonical IDs: `T0`–`T4`, `U`, `MOD.*`, `ODD.1`–`ODD.52`, `A1`–`A12`, `CE.<LAYER>.<n>`
- `scripts/generate_tables.py` validates the YAML and regenerates Markdown tables; `.github/workflows/check-tables.yml` enforces drift-free tables
- Crosswalk to NIST AI RMF, EU AI Act, CRI Profile, and ISO/IEC 42001; glossary
- Contribution guidelines, issue and pull request templates, governance documentation, datasheet

### Notes on sources
- Lines of business follow the companion one-pager (8 groups, with insurance and treasury combined). The preprint's Section 4.2 describes 9 business lines (treasury and insurance listed separately); Appendix B of the preprint matches the one-pager.
- The preprint's contributions list (Section 1.2) names a "Profile Verifier"; Section 6.1 describes Level 3 as the Profile Validator operated by a qualified independent assessor. This repository follows Section 6.1.
- Modifier name: Section 4.1 says "accountability"; Appendix B.1 and the one-pager say "integrated-stack accountability". This repository uses the latter.
- ODD definition: Section 4.2 lists jurisdiction; the Appendix D glossary lists tool surface and omits jurisdiction. The glossary here includes both.
- Provenance types: Table 3 and Section 5.2 give five (including document-derived); the Appendix D glossary gives four. This repository uses five.
- Platform invalidation: Section 2.5 (P6) says substrate or skill updates invalidate only directly dependent Profiles; Section 5.3 and the one-pager say a *material* substrate change voids every anchored Profile. This repository follows the one-pager; the two readings reconcile only through "material".
- Worked examples (Appendix A): A.1 prohibits merge and deployment yet lists "human approval to merge" in the envelope; A.2 prohibits disposition yet lists "analyst approval before any disposition". Read as: the agent cannot perform these actions; a person approves them. Both examples set a one-month window although the appendix says validity is keyed to change rather than to the calendar; A.2 also omits "whichever comes first". Recorded as stated; flagged for the authors.

### References
- Hsu, Bankhwal, Moissinac, Werbach, Szpruch, Hillenbrand, "Agent Reliability Profiles in Financial Services," preprint, September 2026
- MLCommons Financial Services Working Group, "The Agent Reliability Profile Taxonomy," companion one-pager, October 2026

---

## Versioning Policy

- **MAJOR** version changes: an axis added, removed, or fundamentally restructured; breaking changes to canonical IDs or the YAML schema
- **MINOR** version changes: new values (use cases, controls, modifiers, factor values), new worked examples, substantive refinements to definitions
- **PATCH** version changes: clarifications, documentation corrections, metadata updates

## Contribution and Review

To propose changes, open a GitHub issue using the relevant template or submit a pull request. All contributions are reviewed by the MLCommons Financial Services Working Group.
