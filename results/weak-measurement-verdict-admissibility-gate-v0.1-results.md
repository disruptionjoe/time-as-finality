# T150 Results: Weak-Measurement Verdict-Admissibility Gate

## Aggregate checks

- Null controls rejected: True
- Live cases clear target gate: True
- Current frontier active: False

## Verdict audits

| Case | Classification | Active route | Risk with R | Risk with (R,A) | Conditional lift | Smallest verdict support | Required next |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `typed_extra_environment_candidate` | `candidate_typed_verdict_route` | `True` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | 1/2 (0.500) | Bind the typed verdict target to a named monitored-qubit platform. |
| `typed_enlarged_instrument_candidate` | `candidate_typed_verdict_route` | `True` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | 1/2 (0.500) | Bind the typed verdict target to a named monitored-qubit platform. |
| `auxiliary_echo_gerrymander` | `null_auxiliary_defined_verdict` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | 1/2 (0.500) | Define the verdict as a fixed map from the declared TaF axis. |
| `rare_target_gerrymander` | `null_rare_verdict_gerrymander` | `False` | 1/10 (0.100) | 0/1 (0.000) | 1/10 (0.100) | 1/10 (0.100) | Use a verdict partition whose smallest class clears the support floor. |
| `posthoc_target_choice` | `null_posthoc_verdict_target` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | 1/2 (0.500) | Predeclare the verdict class before auxiliary data are scored. |
| `same_instrument_positive_lift` | `null_t149_architecture_not_cleared` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | 1/2 (0.500) | Name the extra structure or admit an instrument enlargement. |
| `current_frontier` | `null_t149_architecture_not_cleared` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | 1/2 (0.500) | Name the extra structure or admit an instrument enlargement. |

## Strongest claim

Positive conditional lift is still not enough for Q1C. The verdict must be a predeclared map from an independently typed TaF axis, not an auxiliary-defined label or a vanishingly rare event class.

## What this improved

T150 closes the verdict-gerrymandering loophole left by T149. Future Q1C proposals must declare the target axis, verdict map, and support floor before auxiliary data are allowed to matter.

## What this weakened

This weakens Q1C again: auxiliary-echo labels, post hoc target choice, and rare-event verdict partitions no longer count as positive weak-measurement evidence even if they show decision lift.

## Falsification condition

T150 fails if a serious Q1C platform needs neither an independently typed TaF axis nor a non-gerrymandered verdict partition to produce its positive lift, or if an auxiliary-defined verdict is still judged an honest Q1C target.

## Q1C update

Q1C remains dormant. Reopen it only with a named monitored-qubit platform that clears T149 and uses a predeclared verdict class induced from an independently typed TaF axis with nontrivial support.

## Claim ledger update

Add T150 to Q1C: positive lift must target a predeclared TaF verdict map rather than an auxiliary-defined or rare-event label. Verdict gerrymanders are null.

## Open blocker

The repo still has no named monitored-qubit platform that supplies a T149-cleared architecture together with an independently typed TaF target axis and non-gerrymandered verdict partition.

## Recommended next

Only consider future Q1C proposals that specify a concrete physical axis H and a fixed verdict map V=g(H) before scoring auxiliary data.
