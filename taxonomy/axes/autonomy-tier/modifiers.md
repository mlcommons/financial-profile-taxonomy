# Cross-Cutting Modifiers

## Overview

**Axis:** Autonomy tier (T)

**Definition:** Six risk dimensions stated on the Profile alongside the tier. They are material at any tier and record risk the tier alone leaves unexpressed.

**Value on a Profile:** a stated value for each modifier.

---

## `MOD.data-authority` · Data authority

Sensitivity of what the agent may access, **independent of action capability**. Data authority can raise the risk of a read-only (A1) deployment materially.

*Editorial note (not in the source documents):* the ODD's [data-sensitivity factor](../operational-design-domain/multiplying-factors.md) (public, internal, confidential, PII/NPI, PCI, MNPI) is a candidate shared scale.

## `MOD.reversibility-profile` · Reversibility profile

Whether agent action can be undone without a heavy penalty. Complements the [action-class](../action-class/README.md) ordering, which grades each class by reversibility.

## `MOD.customer-market-impact` · Customer & market impact

Who is affected (**internal · customer · market · regulator · counterparty**) and how badly. The affected parties are enumerated; a severity scale ("how badly") is not yet defined.

## `MOD.stack-composability` · Stack composability

Whether the tool surface is **predefined in advance** or **dynamically assembled at runtime**. For platform-instantiated agents, tools are resolved per session from a closed registry, and stack composability is stated on the Profile.

## `MOD.integrated-stack-accountability` · Integrated-stack accountability

Who stands behind the model, harness, and infrastructure as a whole.

## `MOD.population-scope` · Population scope

Range of parties the agentic system can affect.

---

## Open Questions

The modifiers are named but do not yet have fixed value scales. Stack composability has two stated poles (predefined vs. dynamically assembled); customer & market impact enumerates affected parties but not severity. Proposals for value scales are welcome through the [taxonomy structure contribution](../../../CONTRIBUTING.md#6-taxonomy-structure-contributions) process.

## See Also

- [Autonomy Tier axis](README.md)
- [Tiers](tiers.md)
