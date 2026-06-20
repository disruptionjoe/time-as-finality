# Technical Report: Ambiguous-Tag Channel Independence v0.1

## Claim Under Test

T85 narrowed the measured detector branch: in the existing witness family,
perturbation response and DAG observability were not independently decisive
once trust, pre-registration, and authenticated tags remained strong.

T86 tests the next proposed repair. Make timing and authenticated tags
ambiguous on purpose, then ask whether perturbation response or signed
ancestry can carry the copied-versus-independent partition by itself in the
same T74/T76 audit.

## Artifact

T86 builds five raw-log-count fixtures:

- all timing/tag/provenance channels ambiguous;
- clean perturbation response only;
- perturbation response contaminated by back-action;
- clean signed ancestry DAG only;
- signed ancestry contaminated by truncation and false shared edges.

Trust boundaries and pre-registration remain at the signed T76 values. The
runner converts each fixture through the T76 measured-posterior adapter and
reruns the T74 Monte Carlo audit with 400 samples per fixture.

## Result

The detector branch is not forced to delete perturbation and DAG channels, but
it does not get an empirical upgrade.

| Fixture | Verdict | Robust rate | Withhold rate | D1 computable |
| --- | --- | ---: | ---: | ---: |
| All channels ambiguous | `measured_conservative_withhold` | 0.0 | 1.0 | 0.0 |
| Clean perturbation only | `robust_measured_recovery` | 1.0 | 0.0 | 1.0 |
| Back-action contaminated perturbation | `measured_conservative_withhold` | 0.0 | 1.0 | 0.0 |
| Clean signed DAG only | `robust_measured_recovery` | 1.0 | 0.0 | 1.0 |
| Truncated/false-edge DAG | `measured_conservative_withhold` | 0.0 | 1.0 | 0.0 |

## Current Strongest Claim

Inside the current executable protocol, perturbation response and signed
ancestry can be independently decisive when timing and authenticated tags are
deliberately ambiguous. They should not be removed from the detector schema
yet.

The narrower earned statement is:

```text
Perturbation and DAG channels may stay in Q1 only as isolated,
pre-registered raw-log tests under ambiguous timing/tag controls.
```

## What This Improved

T86 answers the T85 next-work item directly. It constructs the hostile family
that T85 said was needed: tags are ambiguous, timing is non-identifying, and
one non-tag channel is made uniquely clean.

This turns "perturbation/DAG are auxiliary in the current witness" into a more
precise boundary:

```text
auxiliary under strong tags;
independently decisive under ambiguous tags only if clean isolated controls
are present;
withheld under back-action, truncation, or false shared-edge contamination.
```

## What This Weakened Or Falsified

T86 weakens the T85-pessimistic possibility that no honest perturbation-only
or DAG-only fixture exists inside the present scorer.

It also weakens any broad Q1 detector claim. The positive cases are constructed
fixture counts, not measured deployment logs. The contaminated controls
withhold completely, so the branch remains a fragile provenance-admissibility
protocol rather than a detector-dynamics theory.

## Falsification Condition

T86 fails if any of the following occur under the same T74/T76 scoring rule:

1. the all-ambiguous negative control robustly recovers D1;
2. clean perturbation-only or clean DAG-only fixtures stop recovering both
   canonical witness classes;
3. contaminated perturbation or DAG controls recover despite back-action,
   truncation, or false shared-edge risk.

## Claim Ledger Update

Q1 should remain `partially_supported`, with no upgrade to measurement
dynamics. The detector branch should now be stated as:

```text
an admissibility protocol over detector records. Perturbation response and
signed ancestry are retained only as independently isolated, pre-registered
raw-log channels that must be tested under ambiguous timing/tag controls.
They are not empirical support without a real T78-style deployment.
```

## Open Blocker

The positive T86 fixtures are constructed counts. They rely on predefined
copied and independent controls to decide whether recovery is correct. A real
deployment must define those controls before data collection and publish the
event-level logs.

## Next Work

Draft the real-run table needed to instantiate T86 under T78:

- copied-control and independent-control pair definitions;
- perturbation trial outcomes;
- signed ancestry exports and truncation counts;
- tag ambiguity, spoof, and retention rates;
- timing uncertainty and batching windows;
- trust-boundary checks;
- pre-registered demotion rules for back-action and false shared edges.

If such a table cannot be tied to a feasible detector deployment, Q1 should
still demote the detector branch to a narrow record-audit discipline.

## Reproduction

```bash
python -m unittest tests.test_ambiguous_tag_channel_independence -v
python -m models.run_t86
```
