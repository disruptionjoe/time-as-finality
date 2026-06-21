# T93 Results: Weak-Measurement Undo-Cost Independence

## Audits

| Case | Standard timelines equal | Undo cost differs | TaF verdict changes | Classification | Blocker |
| --- | --- | --- | --- | --- | --- |
| `control_energy_proxy` | True | False | False | `null_proxy_cost` | cost coordinate is a proxy for the monitored record or control schedule |
| `postselected_reversal_success` | True | True | True | `null_postselected_cost` | cost coordinate depends on success-conditioned recovery |
| `independent_meter_candidate` | True | True | True | `candidate_non_null_undo_cost_axis` | independent meter changes the TaF verdict with standard statistics fixed |
| `independent_meter_nondecisive` | True | True | False | `independent_but_not_decisive` | meter varies but does not change the TaF verdict |

## Strongest claim

A hardware undo-cost axis is non-null only if a calibrated, pre-registered meter changes the TaF verdict while coherence, redundancy, access, and reversal-success statistics are fixed. Control-pulse energy, trajectory-derived cost, and success-conditioned recovery are null.

## What this improved

T93 turns T91's remaining undo-cost escape hatch into a concrete admission test with a positive witness shape and three failure modes.

## What this weakened

The weak-measurement route is weakened again: naming an undo operation, feedback sequence, or reversal success event is not enough to make T12 non-null.

## Falsification condition

T93 fails if control-schedule energy or success-conditioned reversal can be used as an independent D1 coordinate while standard monitored statistics are held fixed, or if a calibrated independent cost meter changes no TaF verdict yet still counts as a discriminator.

## Q1 update

Keep Q1 partially supported, but treat T12 as blocked except for a future platform with a calibrated pre-registered undo-cost meter that is independent of the monitored record and not postselected.

## Blocker

No real platform in the repo currently supplies the calibrated independent undo-cost meter instantiated by the candidate witness.

## Recommended next

Either name an actual hardware meter and raw-log schema satisfying T93, or demote weak measurement below detector provenance in the active roadmap.
