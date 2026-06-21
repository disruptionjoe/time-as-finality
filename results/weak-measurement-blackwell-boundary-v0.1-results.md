# T155 Results: Weak-Measurement Blackwell Boundary

## Aggregate checks

- Null controls hold: True
- Positive control improves: True

## Audits

| Case | Classification | Screened off by record | 0-1 risk with R | 0-1 risk with (R,A) | Asymmetric risk with R | Asymmetric risk with (R,A) | Required next |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `garbled_same_instrument_meter` | `null_blackwell_screened_off` | `True` | 1/2 (0.500) | 1/2 (0.500) | 1/4 (0.250) | 1/4 (0.250) | Name extra environment structure or enlarge the instrument. |
| `independent_noise_meter` | `null_blackwell_screened_off` | `True` | 1/2 (0.500) | 1/2 (0.500) | 1/4 (0.250) | 1/4 (0.250) | Name extra environment structure or enlarge the instrument. |
| `record_already_sufficient` | `null_blackwell_screened_off` | `True` | 0/1 (0.000) | 0/1 (0.000) | 0/1 (0.000) | 0/1 (0.000) | Name extra environment structure or enlarge the instrument. |
| `extra_environment_candidate` | `candidate_extra_structure_or_enlargement` | `False` | 1/2 (0.500) | 0/1 (0.000) | 1/4 (0.250) | 0/1 (0.000) | Show whether the gain comes from extra environment structure or an explicit instrument enlargement. |

## Strongest claim

T155 adds the absorber underneath T149: if an auxiliary channel is screened off by the full ordinary monitored transcript, then adding that channel cannot improve any predeclared finite decision problem about an independently typed hidden axis.

## What this improved

This makes the Q1C null class more general and easier to evaluate. A same-instrument auxiliary channel is not merely zero-lift for one chosen verdict map; if it is screened off by the full transcript, it is decision-theoretically redundant across the tested loss family.

## What this weakened

This weakens weak-measurement rescue language again. A second channel that is only a garbling, refinement, or noise decoration of the ordinary transcript does not just fail one toy criterion; it fails the whole predeclared finite decision family tested here.

## Falsification condition

T155 fails if a genuinely screened-off auxiliary channel improves a predeclared finite decision problem at fixed full ordinary record, or if the extra-environment positive control does not improve any tested loss despite changing the hidden-axis posterior.

## Q1C update

Q1C remains dormant. Any future same-instrument auxiliary proposal must first show that its event-level content is not screened off by the full ordinary transcript; otherwise no predeclared verdict lift can count.

## Claim ledger update

Add T155 to Q1C: once the full ordinary transcript screens off the auxiliary channel, that channel is null across the tested finite decision family, not just for one chosen verdict map.

## Open blocker

The repo still lacks a named monitored-qubit platform where the auxiliary channel provably changes the hidden-axis posterior at fixed full ordinary record and can be typed as extra environment structure or honest instrument enlargement.

## Recommended next

Do not search for more same-instrument meters. Search only for a platform that can exhibit non-screened-off event-level content before any verdict or loss rule is optimized.
