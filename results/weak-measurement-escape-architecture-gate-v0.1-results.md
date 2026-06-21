# T146 Results: Weak-Measurement Escape Architecture Gate

| Proposal class | Classification | Active route | Required next |
| --- | --- | --- | --- |
| `coarse_record_only` | `null_coarse_standard_record` | `False` | Condition on the full event-level ordinary monitored transcript. |
| `screened_off_by_full_record` | `null_screened_off_by_full_record` | `False` | Show an auxiliary axis that survives full-record conditioning. |
| `proxy_or_postselected` | `null_proxy_or_postselection` | `False` | Replace the proxy with a calibrated pre-analysis auxiliary channel. |
| `same_instrument_default_null` | `null_same_instrument_default` | `False` | Either tie the auxiliary channel to extra environment structure or declare an explicit instrument enlargement. |
| `extra_environment_candidate` | `candidate_extra_environment_escape` | `True` | Tie the extra environment structure to a named monitored-qubit platform. |
| `enlarged_instrument_candidate` | `candidate_enlarged_instrument_escape` | `True` | Write the enlarged-instrument protocol and audit the preserved comparison. |
| `current_frontier` | `null_same_instrument_default` | `False` | Either tie the auxiliary channel to extra environment structure or declare an explicit instrument enlargement. |

## Strongest claim

After T139 and T143, only two live Q1C architecture classes remain: an
auxiliary channel tied to extra environment structure that survives
full-record conditioning, or an openly enlarged instrument with a
pre-declared preserved comparison target. Same-instrument auxiliary hardware
is null by default.

## What this improved

T146 converts the post-T143 prose into an executable architecture gate.
Future weak-measurement proposals can now be rejected before any literature
or toy-model effort if they do not fit one of the two live escape classes.

## What this weakened

This weakens the generic "second meter" route further. Hardware distinctness,
unscreened rhetoric, and undeclared instrument changes no longer count as
progress.

## Falsification condition

T146 fails if a same-declared-instrument auxiliary channel with no extra
environment handle and no explicit instrument enlargement still yields a
pre-registered verdict-changing axis that survives the full-record gate.

## Q1C update

Q1C remains dormant. Filter future proposals by architecture first: only
extra-environment channels or explicitly enlarged instruments with a declared
preserved comparison target remain live.

## Claim ledger update

Add T146 to Q1C: same-instrument auxiliary hardware is null by default after
the full-record gate unless it captures extra environment structure or openly
enlarges the monitored instrument with a declared preserved comparison target.

## Open blocker

The repo still has no named monitored-qubit platform in either live escape
class.

## Recommended next

Stop generic second-meter searches. Search only for a platform with an
unscreened extra-environment channel or for an explicit enlarged-instrument
protocol that states its preserved comparison target.
