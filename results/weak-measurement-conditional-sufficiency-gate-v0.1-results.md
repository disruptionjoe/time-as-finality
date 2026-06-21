# T149 Results: Weak-Measurement Conditional-Sufficiency Gate

## Aggregate checks

- Null controls rejected: True
- Live cases have positive lift: True
- Current frontier active: False

## Conditional decision audits

| Case | Classification | Active route | Risk with R | Risk with (R,A) | Conditional lift | Required next |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `screened_copy_meter` | `null_conditionally_sufficient_record` | `False` | 0/1 (0.000) | 0/1 (0.000) | 0/1 (0.000) | Show a positive predeclared decision-risk lift at fixed full record. |
| `independent_noise_meter` | `null_conditionally_sufficient_record` | `False` | 1/2 (0.500) | 1/2 (0.500) | 0/1 (0.000) | Show a positive predeclared decision-risk lift at fixed full record. |
| `coarse_record_refinement_only` | `null_coarse_standard_record` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | Define the full ordinary monitored transcript before testing lift. |
| `postselected_positive_lift` | `null_proxy_or_postselection` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | Replace the proxy with a calibrated event-level auxiliary meter. |
| `same_instrument_positive_lift` | `underdeclared_same_instrument_lift` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | Name the extra structure or admit an instrument enlargement. |
| `extra_environment_candidate` | `candidate_extra_environment_conditional_lift` | `True` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | Bind this finite lift to a named monitored-qubit platform. |
| `underdeclared_enlarged_instrument` | `underdeclared_instrument_enlargement` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | Declare the enlarged instrument and preserved comparison target. |
| `enlarged_instrument_candidate` | `candidate_enlarged_instrument_conditional_lift` | `True` | 1/2 (0.500) | 0/1 (0.000) | 1/2 (0.500) | Audit whether the preserved comparison target is physically honest. |
| `current_frontier` | `null_conditionally_sufficient_record` | `False` | 0/1 (0.000) | 0/1 (0.000) | 0/1 (0.000) | Show a positive predeclared decision-risk lift at fixed full record. |

## Strongest claim

Q1C's remaining weak-measurement gate should be stated as a conditional decision-sufficiency test. With the full ordinary event-level record R fixed, an auxiliary channel A is non-null only if adding A strictly lowers a predeclared verdict risk for V, and the source of that lift is physically typed as extra environment structure or an explicit instrument enlargement with a preserved comparison target.

## What this improved

T149 turns 'not screened off by the full record' into an executable finite risk comparison. A platform proposal now needs R, A, V, a loss rule, and an architecture declaration before it can be called a Q1C candidate.

## What this weakened

This further weakens Q1C: a physically distinct meter, a better coarse summary, or a positive lift with no typed physical source does not count. Current Q1C remains a reinstatement gate, not a measurement-dynamics claim.

## Falsification condition

T149 fails if a calibrated platform produces a pre-registered positive decision lift at fixed full ordinary record while neither extra environment structure nor instrument enlargement is needed, or if a zero-lift auxiliary channel can still force a legitimate verdict split under the declared loss.

## Q1C update

Q1C remains dormant. Reopen it only with a named monitored-qubit platform that supplies a positive conditional decision lift at fixed full ordinary record and clears either the extra-environment or enlarged-instrument architecture gate.

## Claim ledger update

Add T149 to Q1C: 'survives full-record conditioning' now means positive predeclared decision-risk lift from adding the auxiliary channel to the full ordinary transcript, plus a physically typed source for that lift. Zero-lift, coarse-record, postselected, and underdeclared same-instrument routes are null.

## Open blocker

The repo still has no named monitored-qubit platform with R, A, V, loss function, event-level data schema, and architecture declaration sufficient to run this gate.

## Recommended next

Do not add more Q1C toy proposals unless they instantiate the T149 input tuple on a real platform. If no platform can supply the tuple, leave Q1C dormant and work another route.
