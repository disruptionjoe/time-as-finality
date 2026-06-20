# Technical Report: Weak-Measurement Reparameterization Obstruction v0.1

## Claim Under Test

T88 states that the weak-measurement route is non-null only if at least one D1
coordinate is tied to a pre-registered observable not reducible to coherence
decay, fragment redundancy, access windows, or post hoc threshold choice. T90
turns that gate into an executable obstruction.

## Result

The current weak-measurement route remains blocked. A finalization time built
only from standard monitored-record statistics is a null result even when
`t_finality` numerically differs from `t_decohere`.

The executable criterion is stricter:

```text
A T12-style protocol is an isolated non-null candidate only if two trajectories
with identical coherence, redundancy, and access timelines receive different
TaF finalization verdicts because of a pre-registered independent D1
observable.
```

If the separating observable is post hoc, semantic, or threshold-tuned after
seeing the data, the route remains null.

## Executable Witnesses

T90 implements three cases.

| Case | Standard timelines | TaF verdict | Classification |
| --- | --- | --- | --- |
| standard-only D1 axes | one trajectory | fixed by coherence/redundancy/access thresholds | `null_reparameterization` |
| independent branch witness | identical across pair | changes from `t=3.0` to `t=4.0` | `candidate_non_null_witness` |
| post hoc branch label | identical across pair | changes from `t=3.0` to `t=4.0` | `null_post_hoc` |

The second case is not empirical support. It is the minimum shape a real
weak-measurement discriminator must instantiate.

## Current Strongest Claim

Q1 does not yet contain a weak-measurement prediction. It contains a
separation test for future proposals:

```text
hold standard monitored-record statistics fixed, then show that a
pre-registered branch, provenance, or reversal-cost observable changes the TaF
verdict.
```

Until that happens, the weak-measurement route is a thresholded record-audit
language, not a new physics discriminator.

## What This Improved

T90 converts T88 from a prose gate into a reproducible obstruction test. A
future monitored-qubit model can now be rejected for using only standard
coherence/redundancy/access data, or admitted as a candidate only by naming the
independent D1 axis before analysis.

It also clarifies a common false positive: `t_finality != t_decohere` is not
enough. Different threshold times are still null when both are functions of the
same sufficient statistics.

## What This Weakened Or Falsified

This weakens the T12 experimental-discriminator route. Nothing in the repo yet
supplies the required independent branch-live, provenance, or reversal-cost
observable.

It also falsifies the move from "TaF chooses a later or earlier threshold on a
weak-measurement trajectory" to "TaF predicts a distinct measurement event."

## Falsification Condition

T90 fails if either occurs:

1. a protocol using only standard coherence/redundancy/access statistics yields
   a TaF verdict that cannot be expressed as a thresholded standard-statistic
   rule; or
2. a post hoc branch/provenance/reversal label is legitimately usable as an
   independent observable.

The intended positive escape is different: a concrete platform supplies a
pre-registered independent axis and changes the TaF verdict while standard
statistics stay fixed.

## Claim Ledger Update

Q1 should remain `partially_supported`, but its weak-measurement branch should
be stated as:

```text
T12 is an obstruction-gated route, not an earned prediction. It becomes non-null
only when a pre-registered branch, provenance, or reversal-cost observable
changes the TaF verdict between trajectories with identical standard
monitored-record statistics.
```

## Open Blocker

No concrete platform currently supplies a pre-registered branch-live or
reversal-cost observable that is independent of coherence decay, fragment
redundancy, and access thresholds.

## Next Work

Instantiate the independent-axis test on one real platform:

- superconducting-qubit homodyne trajectories with a pre-registered
  branch-live witness; or
- trapped-ion/cavity-QED undo protocols with a nontrivial reversal-cost
  observable.

If neither can name an independent axis before data analysis, demote T12 from
experimental discriminator to open operationalization blocker.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_reparameterization_obstruction -v
python -m models.run_t90
```
