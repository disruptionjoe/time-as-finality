# T139: Weak-Measurement Full-Record Sufficiency Boundary

## Route

Quantum measurement / classical records.

## Question

When does a proposed weak-measurement second meter only look non-null because
the "ordinary monitored record" was fixed at an overly coarse summary rather
than at the full pre-registered event-level trajectory?

## Motivation

T132 required an independent axis. T137 showed that a simultaneous second meter
is null when it is screened off by the ordinary monitored record. One loophole
still remained: the repo could silently weaken "ordinary monitored record" to a
dashboard, average, thresholded export, or otherwise coarsened view of the
trajectory, then mistake an auxiliary refinement for a new physical axis.

T139 closes that loophole.

## Setup

T139 adds three finite witness families:

1. `coarse_summary_refinement_only`
   The second meter only refines a coarsened ordinary log. It looks
   branch-sensitive at the coarse-summary level, but not once the full
   event-level monitored record is fixed.
2. `full_record_downstream_meter`
   The second meter is screened off even by the full standard record.
3. `branch_sensitive_extra_meter`
   Logical escape witness: the second meter remains branch-sensitive after the
   full standard record is fixed.

The audit compares screening-off and witness splits at two conditioning levels:

- coarse summary of the ordinary monitored record;
- full pre-registered event-level ordinary monitored record.

## Success Criteria

- A second meter that only refines a coarsened standard log is classified as
  null for Q1C.
- The artifact distinguishes coarse-summary loopholes from true full-record
  escape cases.
- The gate is sharpened without claiming that all dual-meter routes are
  impossible.

## Failure Criteria

- A same-summary split is allowed to count when it disappears after conditioning
  on the full event-level standard record.
- The result treats any physically distinct auxiliary hardware as non-null.
- The artifact claims a new dynamical law rather than an admissibility
  boundary.

## Claim Impact

Q1C remains dormant. Strengthen the route definition:

```text
"ordinary monitored statistics held fixed" must mean the full pre-registered
event-level standard record, not a coarsened summary that an auxiliary meter
merely refines.
```

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_full_record_sufficiency_boundary -v
python -m models.run_t139
```
