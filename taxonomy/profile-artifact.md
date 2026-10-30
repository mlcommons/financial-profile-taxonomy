# The Profile Artifact

The four axes define the option universe. The **Agent Reliability Profile** is the single artifact that records one deployment's values on those axes, with the evidence and conditions that back them.

> **Explanatory summary.** This page summarizes the preprint for readers of the taxonomy. The normative rules for a Profile are in the Agent Reliability Profile Specification in the Profile Kit (`arp/1.0-rc2`); where the two differ, the specification governs.

## Formal Structure

```
S(D) = (T, O, A+, A-, C)          scope of deployment D
P(D) = { S(D), E, F, V, I }       the issued Profile
```

| Symbol | Component |
|---|---|
| **S(D)** | Scope tuple: autonomy tier, ODD instance, permitted and prohibited action-class sets, control envelope |
| **E** | Evidence record with its provenance map |
| **F** | Set of floors with their status |
| **V** | Validity function: a validity window together with the criteria or triggers that would deprecate the Profile's trust status |
| **I** | Issuer, subject, method, schema version, and signatures |

A Profile is a structured claim with evidence and conditions, **not a scalar score**.

## Minimum Content of a Conforming Profile

| Section | Required content | Purpose |
|---|---|---|
| Identity and issuance | Profile identifier; deployment identity; accountable owner; issuer; issue time; validity interval; schema and versions; owner and issuer signatures; parent Platform Baseline Profile and version, where applicable | Binds the claim to a deployment, owner, issuer, and method |
| Claim boundaries | Autonomy tier; ODD; permitted and prohibited action-class sets; control envelope | States the assessed scope |
| Assurance statement | Production assurance level per axis and the headline level; benchmark comparability flag, with environment-fidelity statement where set; assessor role; test environment | Identifies the basis and independence of the evidence |
| Floors | Required pass-or-fail conditions; status; finding references | Prevents aggregate performance from masking critical failure |
| Results | Evaluator-level results at Level 2 or 3; benchmark result where the flag is set | Reports supported findings without implying additional assurance |
| Provenance map | Field-level source type: measured, configuration-derived, document-derived, owner-attested, or absent | Makes evidence quality visible |
| Out-of-scope statement | Domains, actions, controls, and users / adopters excluded from the claim | Defines the external boundary of the claim |
| Invalidation list | Changes that void the Profile or might require partial retesting | Supports change-sensitive validity |
| Evidence pointers | Content hashes and stable identifiers for inputs, evaluator outputs, action traces, and assessor reports | Connects the summary to the Profile Package |
| Status and limitations | Open findings, exceptions, risk acceptances, and interpretation limits | Preserves decision context |

Organizational policies and requirements may add further components. A Profile states only the conclusions its assurance level supports. Comparative grades appear only on Benchmarked Profiles; every other Profile states plainly that its results are specific to its own environment.

## Floors

A floor is a **pass-or-fail condition that cannot be offset by good results elsewhere**. Floors are set before runs and evaluated before any graded result is computed. A failed safety floor blocks issuance of a Profile even when average task performance is high.

## Provenance

Every material field carries provenance:

| Type | Meaning |
|---|---|
| `measured` | Measured in testing |
| `configuration-derived` | Checked against deployed configuration |
| `document-derived` | Extracted from a signed institutional document |
| `owner-attested` | Attested by a named owner |
| `absent` | No source |

Conflicts are made visible. If a policy specifies read-only access but the deployed credential holds write permissions, the Level 1 Profile records the conflict; the Level 2 Profile tests the effective boundary.

## Validity and Change Control

A Profile has a **validity interval** and a machine-readable **invalidation list**. Changes that ordinarily void a Profile:

- expansion to a new ODD
- addition of a higher-consequence action class
- removal of a critical control
- new access, such as a revised owner
- a changed multi-agent topology with new delegation paths
- a model or harness change that can alter tested behavior
- for platform-instantiated agents, a material change to the platform substrate (voids the Platform Baseline Profile and every anchored Profile)

Post-deployment monitoring determines whether the issued conditions continue to hold; the Profile carries a monitoring plan and reissuance requirements, and a point-in-time evaluation is treated as exactly that.

The invalidation list distinguishes changes that **void** the Profile, changes that require **partial retesting**, and changes with **no effect** on the claim.

## The Profile Package

The Profile is the light, scannable summary; the **Profile Package** is its full backing. As applicable: the signed source manifest and inputs; deployment bill of materials and environment manifest; tool catalog, permission map, and control configuration; domain specification and scenario manifest; evaluator definitions, versions, and thresholds; the immutable execution trace; floor findings and evaluator outputs; replay material (where disclosure is safe); the independent assessor's report; benchmark environment and hidden-set version identifiers; and the cryptographic hashes and signatures connecting each component.

## See Also

- [Assurance levels](assurance-levels.md)
- [Worked examples](examples-overview.md)
