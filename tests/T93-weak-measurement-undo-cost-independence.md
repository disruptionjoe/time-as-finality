# T93: Weak-Measurement Undo-Cost Independence

## Route

Quantum measurement / classical records.

## Question

Can the remaining T91 weak-measurement escape hatch, a physically metered
undo-cost observable, avoid collapsing into standard monitored-record
statistics, control-pulse bookkeeping, or postselected reversal success?

## Motivation

T90 requires an independent D1 axis that changes a TaF verdict while standard
monitored statistics are fixed. T91 shows the named superconducting weak
measurement platforms do not yet supply such an axis. T93 isolates the
undo-cost version of the requirement before another platform is named.

## Success Criteria

- The undo-cost rule is fixed before analysis.
- The cost coordinate is calibrated by a meter distinct from the monitored
  trajectory record and control schedule.
- The coordinate does not depend on success-conditioned or null-outcome
  postselection.
- Two witness trajectories with identical coherence, redundancy, access, and
  reversal-success timelines get different TaF verdicts only because the meter
  differs.

## Failure Criteria

- Cost is just a control-pulse or schedule-energy proxy.
- Cost is reconstructed from the same monitored record used by quantum
  trajectory theory.
- Cost is a later success/failure label from a reversal attempt.
- A calibrated independent meter varies but does not change the verdict.

## Claim Impact

Q1 remains `partially_supported`, but T12 stays blocked unless a real platform
can name the calibrated independent meter represented by the positive witness
shape. T93 does not claim that such a meter exists.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_undo_cost_independence -v
python -m models.run_t93
```
