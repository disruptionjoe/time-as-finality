# T96: Detector Feasibility Checklist

## Route

Quantum measurement / classical records.

## Question

After T87 fixed the raw-log contract and T95 mapped one named detector stack
to it, what still carries the route in practice: native detector exports,
ordinary provenance middleware, or custom pre-data control/governance
commitments that can kill detector-side Q1 before any D1 scoring?

## Motivation

The roadmap explicitly asked for an instrument-facing feasibility checklist.
That is higher value than another synthetic witness because the remaining
ambiguity is operational, not conceptual: does the detector route still look
like measurement physics, or has it narrowed into a dry-run record-governance
protocol?

## Success Criteria

- Every T87 table is classified as native hardware, provenance middleware,
  custom control middleware, or governance lock.
- The named T75/T95 route is shown to have exactly which blocker tables are
  non-native and required before the first event.
- The result states clearly whether the route still survives as detector
  physics or only as a governance-heavy dry-run admission program.

## Failure Criteria

- Timing export is treated as if it carries the copied/independent control
  burden.
- Signed provenance logging is treated as enough without ambiguity,
  perturbation, and demotion controls.
- The result overstates dry-run feasibility as empirical support.

## Claim Impact

If T96 passes, Q1 remains `partially_supported`, but the detector branch is
read more narrowly: one native timing table survives, while the decisive
burden shifts to control manifests, ambiguity challenges, perturbation trials,
trust audits, and pre-data demotion rules.

If a lab cannot instantiate that locked packet before data collection, the
detector branch should be demoted below even dry-run status.

## Reproduction

```bash
python -m unittest tests.test_detector_feasibility_checklist -v
python -m models.run_t96
```
