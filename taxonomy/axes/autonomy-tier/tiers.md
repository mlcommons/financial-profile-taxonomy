# Autonomy Tiers

## Overview

**Axis:** Autonomy tier (T)

**Splitting rule:** What the agent does, and who or what provides the fallback when the system cannot continue.

**Values:** T0, T1, T2, T3, T4, and the residual status U. Tier names and definitions are those of the Profile Kit, drawn from Table 1 of the preprint.

---

## T0 · No action capability

**What the agent does:** Read-only or suggestion-only. A person performs the operative task.

**Fallback:** Inapplicable: the person is the operator.

**Example:** A research tool drafts an earnings-call summary; the analyst publishes under their own name.

---

## T1 · Assists individual actions

**What the agent does:** A person invokes each action explicitly. No chaining across a multi-step task.

**Fallback:** The person, continuously and by construction.

**Example:** A relationship manager asks the tool to draft one client email explaining a fee change, edits it, and sends it themselves.

---

## T2 · Bounded multi-step execution with approval

**What the agent does:** Executes a multi-step task inside a strictly bounded envelope. A person approves every material action and is shown the specific resource affected.

**Fallback:** The person, continuously.

**Example:** A loan-origination agent pulls credit, verifies income, location, and credit history, and populates the application, but pauses before each system write.

**Evidence for a T2 claim:**

- Approval latency (time-to-approval distributions)
- Edit rate
- Rejection rate
- Resource display: the specific resource affected is shown to the approver
- Consequence display
- Sampled review quality
- **Habituation testing:** benign, materially incorrect proposed actions are periodically injected and intercepted, with test actions blocked before consequence, to measure reviewer catch rates

**Boundary rule:** Where logs show consistently reflexive acceptance, a configured T2 deployment is classified **T3**.

---

## T3 · Whole task with escalation

> **High scrutiny.** The handoff is where the risk resides.

**What the agent does:** Handles the whole task inside its envelope. Requests help on uncertainty or defined hazard triggers.

**Fallback:** The person, on the system's request, after a handoff. The handoff is where the risk resides.

**Example:** A trade-surveillance agent closes low-scoring alerts with documented rationale, and escalates any alert involving a restricted security or an unknown pattern.

**Evidence for a T3 claim (handoff performance, measured directly):**

- Trigger accuracy
- Time to acknowledgment
- Time to competent control
- Information transferred at handoff
- State preservation
- Actions taken during the delay

---

## T4 · No contemporaneous approval

**What the agent does:** Operates inside a bounded envelope with no contemporaneous approval. Out-of-envelope actions are blocked in software.

**Fallback:** The system, into a defined and tested safe state, to the extent possible. A person is notified afterwards.

**Example:** Real-time card-fraud decisioning: the model declines or approves within milliseconds, but can only act within pre-set rules.

**Evidence for a T4 claim (comprehensive failure management):**

- Halting dangerous actions
- Limiting damage
- Preserving crucial data
- Rolling back changes
- Full recovery

---

## U · Unprofiled (a status, not a tier)

**Description:** No reliability claim is available: envelope, fallback or action boundaries are unspecified.

**Fallback:** Undefined.

**Consequence:** U is a finding requiring remediation, suspension of agent workflows, or documented high risk acceptance.

**Rule:** Unevidenced tier claims are treated as unprofiled.

---

## Open Questions

From the research agenda (preprint, Section 11):

- How consistently can different reviewers classify an agent's autonomy tier?
- Which patterns in approval logs show that a person carefully reviewed a decision, and how should the minimum standard differ by field?
- Do tests of reviewer complacency predict how people respond to unusual cases in real operations?

The mapping from indicator thresholds to tier classification needs field validation, and approval-log indicators and habituation testing require calibration, labor protections, and safeguards against punitive misuse.

## See Also

- [Autonomy Tier axis](README.md)
- [Modifiers](modifiers.md)
