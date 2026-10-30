# Contributing to the Agent Reliability Profile Taxonomy

Thank you for helping build a shared vocabulary for agent reliability in financial services. This taxonomy only becomes a standard if it is used repeatedly, has predictive utility, and is revised in response to failures. Contributions from practitioners are how that happens.

## Why Contribute

- **Shape the vocabulary your institution, vendors, and supervisors will use.** Phase 1 of the program succeeds when two institutions describe the same deployment in the same words.
- **Close gaps you have already found.** Use cases you deploy but cannot place, controls you run that the catalogue does not name, boundary cases you have had to adjudicate internally.
- **We are most interested in divergent perspectives**, including arguments that an axis, tier, or class is wrong.

## Who Can Contribute

- Financial institutions deploying or governing agents (first, second, and third lines)
- Supervisors and regulatory observers
- Assurance and audit firms
- Agent platform, tooling, and security vendors
- Researchers in AI evaluation, human factors, and safety engineering
- Standards bodies

## Types of Contributions

### 1. Get Involved

Join the MLCommons Financial Services Working Group to take part in review, pilots, and inter-rater classification exercises. See [governance/maintainers.md](governance/maintainers.md) for contacts.

### 2. Documentation Improvements

Clarifications, typo fixes, broken links, better examples, and resolved action-class boundary cases. Open a pull request directly, or file a [bug report](.github/ISSUE_TEMPLATE/bug-report.md).

### 3. Use-Case Submission

Propose a new operational design domain use case. The ODD is an open set and this is the most common expected contribution. Use the [use-case submission](.github/ISSUE_TEMPLATE/use-case-submission.md) issue template. A good submission:

- names the line of business it belongs to (or argues for a new one)
- explains why it is distinct from existing use cases
- describes the typical systems, data, decisions, and cost of failure involved
- notes which action classes and autonomy tiers are typical for it today

### 4. Control Submission

Propose a new control, a per-control definition, or a crosswalk mapping (OWASP, NIST, CRI, jurisdiction-specific). Use the [control submission](.github/ISSUE_TEMPLATE/control-submission.md) issue template. A good submission:

- names the layer and explains why the control belongs there and not in another layer
- states what the control does and what it does not do
- describes what a Profile must record about its configuration
- describes evidence that would support a Level 1 assertion and a Level 2/3 test

### 5. Worked Example Submission

Contribute an illustrative bounded claim to [`taxonomy/examples.yaml`](taxonomy/examples.yaml), following the structure of the existing entries. Examples must be illustrative: **never submit a real institution's confidential configuration.** Pull requests must pass `python scripts/generate_tables.py --check`.

### 6. Taxonomy Structure Contributions

Structural changes include: a new or redefined autonomy tier; a new, split, merged, or reordered action class; a new modifier or modifier value scale; a new line of business or multiplying factor; a new control layer; or changes to the platform case. These are reviewed by the full working group and usually trigger a minor or major version change. Open an issue with the [taxonomy contribution](.github/ISSUE_TEMPLATE/taxonomy-contribution.md) template, and attach a completed [taxonomy structure template](.github/TAXONOMY_STRUCTURE_TEMPLATE.md).

## Editing the YAML and Regenerating Tables

`taxonomy/taxonomy.yaml` and `taxonomy/examples.yaml` are the single source of truth. Tables in the Markdown pages are generated from them. After editing either YAML file:

```bash
pip install pyyaml
python scripts/generate_tables.py          # validate and regenerate Markdown tables
python scripts/export_vocab.py             # regenerate vocab/ (Profile Kit format)
python scripts/generate_tables.py --check && python scripts/export_vocab.py --check   # what CI runs
```

The script validates that IDs are unique and contiguous, that counts match the expected option universe, and that every ID used in an example exists. **IDs are stable**: once published, a use case, class, or control ID is never renumbered or reused. Retired values are marked deprecated in a future version rather than deleted. If you change the size of an axis, update `EXPECTED` in the script in the same pull request.

## What NOT to Submit

- Confidential institutional configurations, architecture details, or deployment identities
- Customer data, credentials, secrets, or internal system names
- Vendor marketing claims presented as evidence
- Prescriptive requirements on which envelope an institution must choose (on the control axis the taxonomy is descriptive)
- Changes to the Profile rules (sections, evidence classes, assurance levels, conformance): propose these to the Profile Kit's specification
- Changes to scope outside operational reliability (fairness, explainability, consumer compliance, cybersecurity adequacy), which are governed by their own frameworks

## How to Submit

### Option 1: GitHub Issues

Open an issue using the relevant template. Issues are the right place for proposals that need discussion before anyone edits files.

### Option 2: Pull Requests

1. Fork the repository and create a branch.
2. Edit the YAML source and/or Markdown pages.
3. Run `python scripts/generate_tables.py`.
4. Complete the pull request template.
5. Sign the MLCommons CLA when the CLA bot prompts you.

### Option 3: Direct Contact

For contributions that involve sensitive context, contact the maintainers listed in [governance/maintainers.md](governance/maintainers.md).

## Review Process

All submissions are reviewed by the MLCommons Financial Services Working Group against the criteria in [governance/review-process.md](governance/review-process.md).

### Possible Outcomes

1. **New value**: added to the taxonomy (minor version)
2. **Refinement**: an existing value's definition, examples, or crosswalk is enriched
3. **Structural revision**: proceeds through the working group (minor or major version)
4. **Iteration requested**: feedback on how to strengthen the submission

## Community Standards

### Code of Conduct

All contributors and reviewers adhere to the [MLCommons Code of Conduct](https://mlcommons.org/policies/).

## License

By contributing, you agree that your contribution is licensed under [CC-BY-4.0](LICENSE).
