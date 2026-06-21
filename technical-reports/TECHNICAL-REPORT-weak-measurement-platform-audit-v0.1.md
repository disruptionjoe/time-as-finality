# Technical Report: Weak-Measurement Platform Audit v0.1

## Claim Under Test

T90 left two concrete target families for T12: superconducting-qubit homodyne
trajectories and undo-style weak-measurement platforms. The highest-value move
now is to stop treating those names as implicit support and ask a narrower
question: do any of these platforms already furnish the independent D1 axis
that T90 requires?

## Result

No audited platform currently passes the gate.

The homodyne trajectory route, the partial-measurement uncollapse route, and
the mid-flight quantum-jump reversal route all fail for one of two reasons:

1. the proposed TaF axis is reconstructed from the same monitoring stream that
   already defines the standard quantum trajectory; or
2. the proposed TaF axis depends on success-conditioned postselection rather
   than an independently metered pre-registered observable.

The strongest supported statement is therefore negative:

```text
Known superconducting weak-measurement platforms validate quantum trajectory
control, but they do not yet instantiate an independent D1 branch-support or
reversal-cost observable.
```

## Audited Platforms

| Platform | Candidate TaF axis | Verdict | Reason |
| --- | --- | --- | --- |
| superconducting homodyne trajectory | branch-live witness from homodyne current plus Bayesian trajectory estimate | `null_same_record_derivation` | the same current record already fixes the standard trajectory |
| superconducting partial-measurement uncollapse | reversal-cost witness from reversal success | `null_postselected_axis` | success is conditioned on a later null/success outcome after the designed pulse sequence |
| three-level quantum-jump reversal | mid-flight warning and feedback reversal as branch-live or reversal witness | `null_same_record_derivation` | the no-click warning is part of the same monitoring stream and the feedback is a fixed policy triggered by it |

## Why Each Route Fails

### 1. Homodyne trajectory platforms

Continuous homodyne monitoring of a superconducting qubit yields a stochastic
current record from which the conditional state trajectory is reconstructed.
If the candidate TaF branch-live witness is just "which branch remains live"
as inferred from that same record, then TaF has not added a new observable. It
has only renamed a statistic or functional of the standard measurement stream.

This is a stronger negative result than T90's generic obstruction because it
eliminates the most obvious real-platform candidate.

### 2. Partial-measurement uncollapse platforms

Undo/uncollapse experiments show that a weak measurement can be conditionally
reversed. That looks superficially close to D1 reversal cost. But the present
platform does not meter reversal cost independently. What it meters is whether
the prescribed reversal sequence succeeded, and success is conditioned on a
later outcome. That makes the candidate axis postselected rather than a
pre-registered observable available before analysis.

So the route is not useless, but it is not yet a TaF discriminator.

### 3. Mid-flight quantum-jump reversal

The no-click warning signal and feedback reversal demonstrate real-time
intervention on a monitored quantum trajectory. But the warning signal is still
the same measurement stream that standard trajectory theory already uses. The
feedback policy is designed from that stream; it does not define an additional
branch-support or reversal-cost observable that can differ while the monitored
record is held fixed.

This route therefore validates controllability, not independent TaF content.

## What This Improved

This report closes a live ambiguity in the repo. Before T91, the roadmap could
still sound as if existing superconducting weak-measurement platforms were only
one small modeling step away from an earned TaF discriminator. That is too
optimistic.

After T91, the repo can state explicitly that the currently named platforms are
blocked examples, not merely unfinished positive ones.

## What This Weakened

This weakens the experimental-sounding part of Q1 again. The repository should
not imply that standard homodyne trajectory experiments, weak-measurement
uncollapse experiments, or quantum-jump reversal experiments already contain a
TaF-specific branch-support or reversal-cost observable waiting to be extracted.

It also weakens the temptation to identify "ability to reverse a monitored
state" with D1 reversal cost by default. Conditional reversal success is not
the same thing as an independently metered reversal-cost axis.

## Falsification Condition

This report fails if a named weak-measurement platform supplies a
pre-registered branch/provenance/reversal observable that:

1. is not reconstructible from the same standard monitoring record;
2. does not rely on success-conditioned postselection; and
3. changes the TaF verdict while the standard monitored record is held fixed.

If such a platform exists, T12 becomes a concrete modeling target again rather
than an operational blocker.

## Claim Ledger Update

Q1 should remain `partially_supported`, but the weak-measurement branch should
now be stated more narrowly:

```text
T12 is not merely obstruction-gated in the abstract. The currently named
superconducting homodyne, uncollapse, and quantum-jump-reversal platform
families do not instantiate the required independent D1 axis.
```

## Open Blocker

The missing object is still a pre-registered observable that is operationally
distinct from the monitored trajectory record itself. The best candidates now
look less like standard single-stream weak measurement and more like:

- duplicated-record provenance during monitoring; or
- a physically metered undo cost fixed before analysis and not conditioned on
  reversal success.

## Next Work

Stop spending effort on standard homodyne/jump-reversal platform dressing.
Search for a route with one of these properties instead:

1. two trajectories with identical monitored current/no-click statistics but
   different raw provenance structure for copied versus independent records; or
2. a hardware-defined undo-cost meter whose value is fixed by actuation budget,
   not by success-conditioned readout.

If neither can be stated concretely, demote T12 below the detector-provenance
branch in the active roadmap.
