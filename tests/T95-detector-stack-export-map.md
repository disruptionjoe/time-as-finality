# T95: Detector Stack Export Map

## Route

Quantum measurement / classical records.

## Question

Can the named T75 photon time-tagging stack be mapped to the T87 real-run
raw-log contract before data collection, or is detector-side Q1 still blocked
on custom provenance/control middleware and real event rows?

## Motivation

T94 demoted weak measurement below detector provenance because detector
provenance still has an executable raw-log path. The next valuable step is not
another synthetic detector fixture. It is to ask whether the named instrument
stack can actually export the T87 tables that would make a future run
auditable.

## Success Criteria

- Native HydraHarp/White Rabbit timing export is rejected as insufficient by
  itself.
- A signed archive without copied/independent controls, perturbation trials,
  and demotion logs is rejected before D1 scoring.
- A full augmented pre-registered deployment map covers every T87 table and
  column, but only as a deployment plan while real rows are absent.
- Post hoc and dashboard-summary controls are rejected.

## Failure Criteria

- High-resolution timing is treated as enough for detector finality.
- A signed archive is treated as enough without control-pair, perturbation,
  ancestry, trust, and demotion tables.
- A plan-only export map is reported as empirical support.

## Claim Impact

Q1 remains `partially_supported`, but the detector route narrows again: the
T75 stack is admissible only as an augmented T87 deployment plan, not as native
detector evidence. Most required exports are provenance/control middleware, not
detector physics.

## Reproduction

```bash
python -m unittest tests.test_detector_stack_export_map -v
python -m models.run_t95
```
