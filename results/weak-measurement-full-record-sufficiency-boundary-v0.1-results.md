# T139 Results: Weak-Measurement Full-Record Sufficiency Boundary

| Scenario | Classification | Screened by full record | Screened by coarse summary | Coarse-summary split | Full-record split | Witness summary | Witness full record |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `coarse_summary_refinement_only` | `null_coarse_summary_loophole` | `True` | `False` | `True` | `False` | `mid` | `none` |
| `full_record_downstream_meter` | `null_full_record_downstream` | `True` | `True` | `False` | `False` | `none` | `none` |
| `branch_sensitive_extra_meter` | `candidate_full_record_escape` | `False` | `False` | `True` | `True` | `mid` | `x0` |

## Strongest claim

Q1C must hold fixed the full event-level ordinary monitored record, not a coarsened summary of it. A second meter that only refines an underspecified standard log is null even if it appears branch-sensitive at the summary level.

## What this improved

T139 closes a remaining loophole between T132 and T137: future weak-measurement proposals must now show independence from the full standard trajectory record, not merely from a plotted average, dashboard summary, or thresholded export.

## What this weakened

This weakens any rescue that keeps 'ordinary monitored statistics fixed' only at a coarse level. A same-summary split is not enough if the full event-level log already screens off the auxiliary meter.

## Falsification condition

T139 fails if a second meter that is conditionally determined by the full event-level ordinary monitored record can still produce a pre-registered fixed-full-record TaF verdict split.

## Q1C update

Q1C remains dormant. Strengthen the gate again: the ordinary monitored statistics held fixed must be the full pre-registered event-level standard record, not a coarsened summary that an auxiliary meter merely refines.

## Open blocker

No named monitored-qubit platform in the repo currently supplies an auxiliary meter that provably escapes screening-off by the full event-level standard trajectory record.

## Recommended next

Search only for a dual-meter protocol whose auxiliary channel remains verdict-changing after conditioning on the complete ordinary monitored transcript.
