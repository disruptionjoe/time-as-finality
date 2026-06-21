# T132: Weak-Measurement Non-Null Criterion

## Route

Quantum measurement / classical records.

## Question

What would make the open weak-measurement route a genuine Time as Finality
discriminator rather than a re-parameterization of decoherence, redundancy,
and observer access thresholds?

## Motivation

The detector-provenance branch has been narrowed repeatedly by T83-T87. It is
now an admissibility protocol over already formed records, not a detector
dynamics theory. The remaining high-value path inside Q1 is T12: a continuous
monitoring or weak-measurement setup where TaF predicts a distinct effective
record-finalization time.

That route is also at high risk of collapsing into standard decoherence plus
declared thresholds. T132 makes that collapse condition explicit before more
simulation work is spent on it.

## Non-Null Criterion

A T12-style weak-measurement protocol is non-null only if all of the following
hold:

1. the TaF finalization time is fixed before analysis by a pre-registered rule;
2. at least one D1 coordinate is operationalized by a measured quantity not
   reducible to pointer-coherence decay, fragment mutual information, or a
   declared access window alone;
3. the distinguishing observable changes the TaF verdict while the standard
   decoherence/redundancy verdict stays fixed;
4. the extra observable can be read from event-level trajectory data or an
   intervention protocol rather than from post hoc semantic labeling.

## Null Conditions

Treat the weak-measurement route as null whenever any of the following holds:

1. `t_finality` is only `t_decoherence` with a different threshold;
2. D1 holder redundancy is only a relabeled fragment count with no independently
   justified provenance partition;
3. branch support is constant or fixed by construction in the witness family;
4. reversal cost is only an arbitrary monotone proxy of accessible support or
   coherence loss;
5. the finality verdict changes only because thresholds, access windows, or
   partitions were tuned after inspecting the trajectory.

## Minimal Operational Requirements

To escape those nulls, a continuous-monitoring protocol must supply at least
one independently measured or intervention-defined quantity for each of the
currently weak D1 axes:

- holder redundancy: copied-versus-independent record classes justified by
  measured provenance or isolated channel interventions;
- branch support: a pre-registered criterion for whether multiple candidate
  record branches remain live for the observer;
- reversal cost: an experimentally grounded erasure/undo proxy, not just a
  record count.

Without those inputs, only accessible support is clearly operational, and the
result reduces to access-boundary bookkeeping over standard monitored records.

## Success Criteria

- The repo gains a falsifiable gate for whether T12 is worth implementing.
- The criterion blocks threshold-tuned or post hoc "prediction" claims.
- The next model, if built, must name the extra measured observable that makes
  TaF non-null.

## Failure Criteria

- The criterion still allows a pure decoherence-timescale comparison to count
  as a TaF discriminator.
- The criterion treats semantic provenance labels as measured observables.
- The artifact implies that T12 is already executable with the current D1
  proxies.

## Claim Impact

Q1 remains a demoted umbrella, and Q1C remains dormant. The weak-measurement
branch should now be stated conditionally:

```text
T12 is a valid route only if branch support, holder redundancy, or reversal
cost acquires an independent operational definition inside a pre-registered
monitoring protocol. Otherwise the branch collapses to thresholded decoherence
/ redundancy bookkeeping and should not be presented as a discriminating
prediction.
```

## Contribution Needed

Pick one monitored-qubit platform and specify the first non-reducible D1
observable. If no such observable can be defined before modeling, demote T12
from "discriminating prediction" to "open operationalization blocker."
