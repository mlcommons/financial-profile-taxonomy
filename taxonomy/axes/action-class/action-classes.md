# Action Classes

## Overview

**Axis:** Action class (A+ / A-)

**Splitting rule:** Reversibility, graded with consequence, from no side effects (A1) to amplifying (A12).

**Values:** A1 through A12.

---

## A1 · Read / retrieve

**Examples:** Query transactions, read case files, search policy.

**Reversibility:** n/a (no side effects). Ignores data-leakage risk from cyber vulnerabilities, which is out of scope; see the data-authority modifier.

## A2 · Analyse / compute

**Examples:** Score, simulate, reconcile in memory.

**Reversibility:** n/a (no side effects).

## A3 · Draft for a person

**Examples:** Narratives, code, emails, memos, draft filings.

**Reversibility:** Fully reversible.

## A4 · Recommend / route

**Examples:** Disposition recommendations, escalations, prioritisation.

**Reversibility:** Fully reversible.

## A5 · Write internal

**Examples:** Case notes, tickets, opening a pull request, CRM updates.

**Reversibility:** Reversible.

## A6 · Submit / commit internal

**Examples:** Merge code, close a case.

**Reversibility:** Semi-reversible.

## A7 · External communication

**Examples:** Notify a customer, contact a third party, publish.

**Reversibility:** Hard to reverse.

## A8 · Transact (bounded)

**Examples:** Place a hold, block a card, trade within a cancel window.

**Reversibility:** Partially reversible.

## A9 · Move funds

**Examples:** Wire release, payment execution, settlement.

**Reversibility:** Irreversible.

## A10 · Regulatory filing

**Examples:** File a suspicious-activity or currency report, submit returns, attest.

**Reversibility:** Irreversible, with legal effect.

## A11 · Access & infrastructure change

**Examples:** Alter permissions, deploy to production, change branch protection.

**Reversibility:** Irreversible and risk-amplifying.

## A12 · Delegate / spawn

**Examples:** Create sub-agents, grant credentials to another agent.

**Reversibility:** Amplifying.

---

## Boundary Cases

Action-class boundary cases are expected to consume committee time. Examples worth settling early:

- **A5 vs. A6:** where "write" ends and "commit" begins in a given workflow system (e.g., a draft case note vs. a case note that closes a case).
- **A7 vs. A5:** when sharing data with another internal team or system counts as external communication.
- **A8 vs. A9:** when a bounded transaction's cancel window is long enough, or narrow enough, to change its class.
- **Prohibitions that are not action classes:** some stated prohibitions (e.g., "access secrets", "share customer data outside the case context") are data-authority restrictions. The worked examples record them as unmapped.

Submit resolved boundary cases as [documentation improvements](../../../CONTRIBUTING.md#2-documentation-improvements) or, where they require a new or split class, as [taxonomy structure contributions](../../../CONTRIBUTING.md#6-taxonomy-structure-contributions).

## See Also

- [Action Class axis](README.md)
