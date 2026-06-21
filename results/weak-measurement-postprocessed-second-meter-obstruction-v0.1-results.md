# T137 Results: Weak-Measurement Postprocessed Second-Meter Obstruction

| Scenario | Classification | Postprocessed | Fixed-record split | Witness record | Hot-probability gap |
| --- | --- | --- | --- | --- | ---: |
| `exact_duplicate_meter` | `null_downstream_transform` | `True` | `False` | `none` | 0.0 |
| `noisy_downstream_meter` | `null_downstream_transform` | `True` | `False` | `none` | 0.0 |
| `branch_sensitive_independent_meter` | `candidate_branch_sensitive_second_meter` | `False` | `True` | `low` | 0.8 |

## Strongest claim

A simultaneous second meter does not reopen Q1C when it is only a downstream classical transform of the standard monitored record. Conditioned on the ordinary record, such a meter cannot produce the branch-sensitive split that Q1C requires.

## What this improved

T137 upgrades the vague phrase 'independent second meter' into a conditional-independence test. The repo can now reject physically distinct but downstream-equivalent meters without another literature loop.

## What this weakened

This weakens the softer rescue story that any simultaneous thermal, calorimetric, or auxiliary channel would help merely by being a second piece of hardware. If it is screened off by the standard record, it is null.

## Falsification condition

T137 fails if a second meter that is demonstrably only a downstream kernel of the standard monitored record still yields a pre-registered fixed-record TaF verdict split.

## Q1C update

Q1C remains dormant. Add a stronger gate: a proposed simultaneous second meter is null whenever its statistics are conditionally determined by the ordinary monitored record.

## Open blocker

The missing object is now sharper than 'any second meter': the repo needs a branch-sensitive meter that is not screened off by the ordinary monitoring record and is fixed before analysis.

## Recommended next

Search only for monitored-qubit protocols where the auxiliary meter couples to hidden branch-relevant structure not recoverable from the ordinary trajectory record or its downstream transforms.
