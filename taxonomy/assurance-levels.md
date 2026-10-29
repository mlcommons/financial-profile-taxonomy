# Assurance Levels and the Benchmark Comparability Flag

Not every agent needs the same assurance. The Profile keeps the **same shape at every level**: the axes, components, and definitions are standardized, while the rigor and independence of the evidence adjust. Machine-readable source: [`profile.yaml`](profile.yaml).

Three **production assurance levels** form a single ordered scale of evidence and independence about the deployment in its own environment. A separate **benchmark comparability flag** is a different measurement, trading production fidelity for cross-institution comparability.

## The Ladder

| | **Level 1** · Asserted Profile | **Level 2** · Validated Profile | **Level 3** · Verified Profile | **Flag** · Benchmarked Profile |
|---|---|---|---|---|
| **Tool** | Profile Builder | Profile Validator | Profile Validator, operated by an independent assessor | Profile Benchmarker |
| **What happens** | The institution's own documents and settings are read and compiled into a Profile | The institution runs tests against its own agent | A qualified independent assessor runs the tests | An independent assessor runs the agent in a shared environment |
| **Who stands behind it** | The institution | The institution | An independent assurance firm | An independent assessor |
| **Where it runs** | Nothing is executed | The institution's own environment | The institution's own environment | A shared reference environment with a hidden, rotating scenario set |
| **What the Profile says** | Self-reported | Self-reported, self-tested | Self-reported, independently tested | In addition to its production level: independently benchmarked |
| **Minimum bar** | Inputs attested by a named owner | Reproducible generation, a content hash, signed inputs | The Level 2 bar, plus a qualified independent assessor and its own signed report | Accredited assessor, named environment version, named hidden-set version |
| **May claim** | This is what we believe we have deployed | No critical control failure under the conditions we tested | The same, tested by someone other than us | A result comparable with other institutions under the reference conditions |
| **May not claim** | Anything tested | Independence | Comparability with any other system | Additional assurance about production behavior |
| **Data leaves the institution** | No | No | Either the evidence travels or the assessor works on site | Sometimes, depending on the benchmarking infrastructure and the benchmarked components |

## Mixed-Axis Assurance and the Headline Level

Assurance can differ by axis. The Profile records a production assurance vector with one value per axis, and a headline level equal to the minimum:

```
L(P)            = (L_T, L_O, L_A, L_C)        each in  Level 1 < Level 2 < Level 3
L_headline(P)   = min{ L_T, L_O, L_A, L_C }
```

The rule prevents strong evidence on one axis from raising the apparent assurance of a weaker axis, while the full vector remains visible. The benchmark comparability flag does **not** enter the minimum; it is recorded as a separate field.

The autonomy axis is the one on which the institution's own operational evidence remains indispensable even at the highest levels, because distinguishing substantive from reflexive approval requires the approval logs of the actual deployment.

## Cost and Fit

Levels 1 and 2 should be inexpensive to produce and suit lower-risk agents and estate-wide inventory. Level 3 costs more and suits higher-risk agents. Benchmarking is the costliest and buys comparability. For platform-instantiated systems, Level 3 verification obtained once for the Platform Baseline Profile covers the substrate for every anchored agent.

## Terminology

| Verb | Who | Meaning |
|---|---|---|
| *assess* | Institution | Evaluate an agent |
| *compile* | Institution | Produce its Profile |
| *issue* | Named owner | Sign and issue the Profile |
| *validate* | Institution | Level 2 evidence generation |
| *verify* | Qualified independent assessor | Level 3 evidence generation |
| *benchmark* | Independent assessor | Sets the comparability flag |
| *examine* | Supervisor | Review any Profile |

## See Also

- [The Profile artifact](profile-artifact.md)
- [Glossary](glossary.md)
