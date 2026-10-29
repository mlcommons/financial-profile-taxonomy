# Review Process

All submissions to the taxonomy are reviewed by the MLCommons Financial Services Working Group.

## Pipeline

Submission → Triage → Technical Review → Placement Decision → Merge or Iterate

Structural changes (see [CONTRIBUTING.md](../CONTRIBUTING.md#6-taxonomy-structure-contributions)) additionally require discussion at a working-group meeting before a placement decision.

## Technical Review Criteria

| Criterion | Question |
|---|---|
| Distinctness | Does this represent a distinct value, or a variant or refinement of an existing one? |
| Placement | Is it placed on the right axis and in the right group (line of business, layer), consistent with that group's splitting rule? |
| Axis consistency | Does it preserve the axis's organizing principle (fallback for tiers; reversibility and consequence for action classes; layer of operation for controls)? |
| Falsifiability | Does the value determine at least one test that can fail? |
| Comparability | Would two institutions describing the same deployment assign the same value? |
| Evidence | Is the need grounded in observed deployments, supervisory experience, or established frameworks? |
| Confidentiality | Is the submission free of confidential institutional configuration, customer data, and credentials? |
| Stability | Does it preserve existing canonical IDs? |

The methodological basis for these criteria is the preprint (Hsu et al., 2026), in particular its design requirements (Section 2.3), the four axes (Section 4), and the implementation program (Section 11).

## Placement Decision

A submission is resolved as one of:

1. **New value**: added as a new use case, control, modifier value, or factor value.
2. **Refinement**: enriches an existing value's definition, examples, evidence expectations, or crosswalk.
3. **Structural revision**: motivates a change to an axis's structure, which proceeds through the working group.
4. **Iteration requested**: feedback is provided on how to strengthen the submission.

## Release Cadence

Accepted changes accumulate under `[Unreleased]` in the [CHANGELOG](../CHANGELOG.md). Releases produce a tagged snapshot in `releases/`. During the pilot phase, pilot feedback is batched into releases; publishing the post-pilot taxonomy marks the end of the pilot phase.
