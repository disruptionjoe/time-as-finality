# Technical Report: Weak-Measurement Undo-Cost Independence v0.1

## Claim Under Test

T91 left two possible weak-measurement escape hatches: duplicated-record
provenance during monitoring, or a physically metered undo-cost observable.
T93 tests the second route. The question is not whether undo experiments are
real. The question is whether an undo-cost axis can add TaF-specific content
rather than repackage the monitored record, a pulse schedule, or a postselected
success event.

## Result

The undo-cost route is not yet an earned discriminator. It has a strict
candidate shape:

```text
hold coherence, redundancy, access, and reversal-success statistics fixed;
then a calibrated, pre-registered, non-postselected undo-cost meter must change
the TaF verdict.
```

Control-pulse energy, trajectory-derived cost, and success-conditioned recovery
are null. They do not supply the independent D1 axis required by T90.

## Executable Witnesses

| Case | Classification | Meaning |
| --- | --- | --- |
| `control_energy_proxy` | `null_proxy_cost` | cost is just schedule/control bookkeeping |
| `postselected_reversal_success` | `null_postselected_cost` | cost depends on success-conditioned recovery |
| `independent_meter_candidate` | `candidate_non_null_undo_cost_axis` | the minimum positive witness shape |
| `independent_meter_nondecisive` | `independent_but_not_decisive` | a meter can vary and still fail to matter |

The positive case is not empirical support. It is an admission criterion for a
future platform.

## Current Strongest Claim

Q1 has no weak-measurement prediction yet. The surviving T12 path is only:

```text
a real platform with a calibrated pre-registered undo-cost meter, operationally
distinct from the monitored record and not conditioned on reversal success.
```

Without that meter, the weak-measurement branch remains an obstruction and
admissibility filter rather than a discriminator.

## What This Improved

T93 removes ambiguity from the phrase "undo cost." A reversal protocol is not
enough. A feedback pulse sequence is not enough. A success-conditioned recovery
event is not enough. The repo now has an executable gate for any future
hardware proposal.

## What This Weakened Or Falsified

This weakens the remaining weak-measurement route. It blocks the move from
"we can undo or reverse a weak measurement in selected runs" to "TaF has an
independent reversal-cost observable."

It also falsifies a weaker attempted repair: an independent meter is not
sufficient unless it changes the TaF verdict while standard monitored
statistics are fixed.

## Falsification Criterion

T93 fails if either condition holds:

1. control-schedule energy or success-conditioned reversal can legitimately act
   as an independent D1 coordinate while standard monitored statistics are
   fixed;
2. a calibrated independent undo-cost meter changes no TaF verdict but still
   counts as a weak-measurement discriminator.

The intended escape is narrower: name a real calibrated meter, pre-register it,
and show the verdict separation on raw logs.

## Claim Ledger Update

Q1 should remain `partially_supported`, but the T12 branch should be stated as:

```text
weak measurement is blocked except for a future platform with a calibrated,
pre-registered undo-cost or provenance meter independent of the monitored
record and not postselected.
```

## Open Blocker

No real platform in the repo currently supplies the calibrated independent
undo-cost meter instantiated by T93's candidate witness.

## Next Work

Either name an actual hardware meter and raw-log schema satisfying T93, or
demote weak measurement below detector provenance in the active roadmap.
