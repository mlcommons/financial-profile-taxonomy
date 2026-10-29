# Glossary

Adapted from Appendix D of the preprint. Two entries are harmonized with the body of the preprint: the ODD definition includes jurisdiction (Section 4.2), and the provenance map lists all five source types (Section 5.2). Operating boundary, Unprofiled, and Modifier are added for this repository.

| Term | Meaning |
|---|---|
| **Agent Reliability Profile** | The single artifact recording the four axis values, the floors, the out-of-scope and validity statements, the provenance map, and pointers to the underlying evidence. Each agent deployment has its own Profile. |
| **Bounded claim** | The scoped, falsifiable assertion produced by fixing the four axes: reliable at this autonomy tier, in this operational design domain, for these action classes, under this control envelope, and nothing else. |
| **Operating boundary** | The combination of the four axis values: autonomy tier, operational design domain, action classes, and control envelope. |
| **Autonomy tier** | How much the agent decides and acts without a person, and who provides the fallback when it cannot continue. The tier determines what counts as a failure and how failures are weighted in evaluation. |
| **Unprofiled (U)** | A status, not a tier: no reliability claim is available because the envelope, the fallback, or the action boundaries are unspecified. |
| **Modifier** | A cross-cutting risk dimension stated alongside the tier: data authority, reversibility profile, customer and market impact, stack composability, integrated-stack accountability, population scope. |
| **Operational design domain (ODD)** | The defined operating context (use case, data, tool surface, customer population, jurisdiction, cost of failure) that specifies the test environment. Follows its use in automated-driving standards. |
| **Boundary detection** | Whether the agent recognises that it has left its tested domain and stops. A defined test at Level 2 and above, distinct from following an escalation rule the agent was given. |
| **Action class** | The type and reversibility of actions the agent may take, from read and draft through submit, transact, and move funds. Recorded as a permitted set (A+) and a prohibited set (A-). |
| **Control envelope** | The containment around the agent (approval gates, least-privilege access, rollback, logging, tested safe state) that makes a given autonomy tier acceptable within a given domain. |
| **Floor** | A pass-or-fail condition that cannot be offset by good results elsewhere. Floors are evaluated before any graded result is computed. |
| **Provenance map** | A field-by-field record of whether each entry on a Profile was measured, checked against configuration, extracted from a signed document, attested by a person, or is absent. |
| **Invalidation list** | The machine-readable statement of which changes void a Profile, which require partial retesting, and which are cosmetic. |
| **Platform Baseline Profile** | The Profile carried by an agent platform itself. Its claim is an enforcement claim (the ceilings and invariants the substrate guarantees for every session it hosts), not an attestation of any hosted agent's performance. |
| **Platform anchor** | The machine-readable record, on an agent's Profile, of the parent Platform Baseline Profile and version whose substrate controls form part of the agent's control envelope. An anchored Profile is void if the parent claim is void. |
| **Autonomy ceiling** | The maximum autonomy tier a platform can grant to any agent it hosts, enforced in software and recorded on the platform's Profile in place of a tier. |
| **Resolved manifest** | The per-session record of the skills, tools, data contexts, and permissions actually granted to a platform-instantiated agent, resolved from a closed registry and preserved as evidence. |
| **Profile Package** | The Profile plus the signed inputs, evidence, and trace it was compiled from. The Profile is the light, scannable summary; the Package is its full backing. |
| **Asserted Profile (Level 1)** | Self-reported: compiled by the Profile Builder from the institution's own documents and settings; nothing executed; signed by a named owner. |
| **Validated Profile (Level 2)** | Self-reported and self-tested: produced by the Profile Validator run in-house, with reproducible, hashed, signed inputs. |
| **Verified Profile (Level 3)** | Self-reported and independently tested: the Profile Validator operated and signed by a qualified independent assessor. |
| **Benchmarked Profile** | A Profile carrying the benchmark comparability flag: run by the Profile Benchmarker in a shared environment with a hidden, rotating scenario set; comparable across institutions under the reference conditions. A separate field, not an assurance level; it does not raise the Profile's production assurance level. |
