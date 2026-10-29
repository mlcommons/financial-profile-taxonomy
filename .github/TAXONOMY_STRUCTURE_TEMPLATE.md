# Taxonomy Structure Proposal Template

Use this template for proposals that change the structure of an axis. Attach it to a [taxonomy contribution](ISSUE_TEMPLATE/taxonomy-contribution.md) issue or include it in the pull request description.

---

## Proposal Type

- [ ] New value on a closed axis (tier, action class, layer, modifier)
- [ ] Split of an existing value
- [ ] Merge of existing values
- [ ] Reordering or re-bounding (e.g., moving the T2/T3 boundary, reordering action classes)
- [ ] New group (line of business, multiplying factor)
- [ ] Change to the Profile artifact or assurance vocabulary

**Axis:**

**Affected IDs:**

## Definition

**Name:**

**Definition** (one paragraph, in the style of the existing entries):

**Splitting rule** (how it is distinguished from its siblings, using the parent's single axis):

## Identification Criteria

**Inclusion cues** (what a deployment looks like that should receive this value):

- 

**Exclusion cues** (near neighbors that should *not* receive it, and where they belong instead):

- 

## Test Implications

**What test does this value determine that can fail?**

**What evidence would support it at Level 1? At Level 2/3?**

## Evidence and Examples

**Illustrative deployments** (describe structurally; no confidential configurations):

1. 
2. 

**Inter-rater check:** Would two institutions describing the same deployment assign the same value? Describe any classification exercise you ran.

## Effect on Existing Profiles

**Which existing Profiles would change classification?**

**Migration note** (canonical IDs are never renumbered or reused; describe deprecation if needed):

## References

- 

## Checklist

- [ ] The proposal preserves the parent's splitting rule, or explicitly proposes changing it
- [ ] Inclusion and exclusion cues are given
- [ ] At least one failing test is identified
- [ ] No confidential institutional configuration included
