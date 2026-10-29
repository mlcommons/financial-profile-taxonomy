# Cross-Axis Case: Agent-Building Platforms

## Overview

**Applies to:** All four axes.

**Artifacts:** Platform Baseline Profile + anchored Profiles.

A growing share of agents is assembled on shared platforms: substrates on which domain teams build and govern their own agents through a control plane. Examples in financial services include first-party platforms connecting a single agent service to more than a thousand skills and tools, and platforms on which some 20,000 employees build agents under a dedicated release-approval regime.

**A platform is not a deployment.** Its ODD is open by construction, tools are resolved per session rather than enumerated in advance, and its agent population turns over continuously. One Profile for the whole platform would be too broad to bind anything.

## Why Platform-Derived Agents Need Distinct Treatment

1. They are created far faster and modified more easily and frequently.
2. Reachable actions are set by the control plane, so a per-agent Profile alone carries little risk information.
3. Correlated faults (a compromised catalogue entry, an over-broad credential template) appear in every agent at once and in none of their Profiles.

## Platform Baseline Profile

The platform carries its own Profile, whose bounded claim is a **ceiling** on what hosted sessions can do. For every session:

- effective autonomy cannot exceed a stated ceiling without a stated gate;
- out-of-set action classes are unavailable **in software, not by policy**;
- no session reaches data outside its authorised context;
- each effective envelope is immutably recorded.

A single counterexample falsifies the claim; **adversarial session-level testing** is the falsification method. Assurance therefore rests on the design and construction of the platform's control plane, not on configuration discipline. The Baseline Profile attests containment only. It says nothing about whether any agent's work is good.

## Profile Inheritance: The Platform Anchor

A hosted agent carries an ordinary Profile that also records a **platform anchor**: the parent Platform Baseline Profile and version, incorporated by reference, whose controls form part of its control envelope. Its own claim is otherwise unchanged.

An anchored Profile is **void if the parent claim is void**. Because the control plane already records each configuration, Level 1 anchored Profiles can be generated largely automatically.

## Six Properties Required to Carry a Baseline Profile

Each property doubles as a test target.

| ID | Property |
|---|---|
| P1 | Autonomy ceiling enforced in software, with defined gating for escalation |
| P2 | Closed, versioned registry of skills and tools with admission standards |
| P3 | Per-session resolution and immutable recording of the effective envelope |
| P4 | Technically enforced data-context isolation |
| P5 | Version control over the Profile's technical components |
| P6 | Change-impact mapping, so updates invalidate only directly dependent Profiles |

## Where Platforms Touch the Four Axes

| Axis | Platform treatment |
|---|---|
| **T** · Autonomy tier | The platform records an **autonomy ceiling** (the maximum tier grantable to any hosted agent) in place of a tier. |
| **O** · Operational design domain | Open by construction at the platform; each hosted agent states its own bounded domain. |
| **A** · Action class | Tools resolved per session from a closed registry; [stack composability](../axes/autonomy-tier/modifiers.md) is stated on the Profile. |
| **C** · Control envelope | Adds the [control-plane layer](../axes/control-envelope/control-plane.md); substrate controls are held by reference via the anchor. |

## Invalidation, Assurance, and Open Risk

**Invalidation.** A material change to the substrate voids the Baseline Profile and every anchored Profile; a skill update voids only the Profiles that depend on it.

**Assurance composes.** Level 3 verification, obtained once for the Baseline Profile, covers the substrate for every anchored agent; those can remain Level 1, upgraded selectively where a deployment's risk warrants it.

**Open risk: concentration.** A defective platform claim undermines every anchored Profile at once; adversarial testing at scale is an open problem.

## See Also

- [Taxonomy Overview](../taxonomy-overview.md)
- [Assurance levels](../assurance-levels.md)
