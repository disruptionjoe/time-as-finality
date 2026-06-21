# T94: Weak-Measurement Priority Demotion

## Route

Quantum measurement / classical records.

## Question

Given T83, T85, T86, T91, and T93, should the active Q1 frontier still treat
weak measurement as the lead discriminator route, or should detector
provenance remain ahead until weak measurement names a real independent axis?

## Motivation

The repo has repeatedly weakened T12. A durable decision rule is now more
valuable than another speculative platform sketch. If weak measurement stays
high priority without a real independent axis, future work risks dressing null
routes rather than increasing publishability or falsifiability.

## Success Criteria

- Detector provenance has at least one source-anchored, pre-registered,
  event-level raw-log route that survives the current null criteria.
- Weak measurement lacks any named platform with a pre-registered branch,
  provenance, or undo-cost observable independent of the standard monitored
  record.
- The audit states the exact reinstatement condition for T12.

## Failure Criteria

- Weak measurement is kept at equal or higher priority merely because it sounds
  like a cleaner experimental discriminator.
- A candidate weak-measurement axis is allowed even though it is derived from
  the same monitoring stream, is postselected, or changes no verdict.
- Detector provenance is treated as empirically upgraded without a T78-style
  raw deployment.

## Claim Impact

Q1 remains `partially_supported`, but T12 is demoted below detector provenance
in the active roadmap until a concrete monitored platform names a pre-registered
independent branch/provenance/undo-cost axis and shows a verdict change with
standard monitored statistics held fixed.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_priority_demotion -v
python -m models.run_t94
```
