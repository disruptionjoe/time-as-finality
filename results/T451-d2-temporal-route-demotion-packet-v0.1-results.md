# T451 - D2 Temporal Route Demotion Packet - v0.1 results

> Route-demotion packet. `CLAIM-LEDGER.md`, `ROADMAP.md`, `TESTS.md`, README, and North Star files are untouched. No claim promotion, no crypto theorem, no physics claim, no public posture.

- Spec: `tests/T451-d2-temporal-route-demotion-packet.md`
- Model: `models/d2_temporal_route_demotion_packet.py`
- Tests: `tests/test_d2_temporal_route_demotion_packet.py`
- Artifact JSON: `results/T451-d2-temporal-route-demotion-packet-v0.1.json`
- Sources: T417, T438, T444, T448, T449, T450, and the D2 open problem

## Overall verdict: CURRENT_D2_TEMPORAL_ROUTE_DEMOTED_TO_T417_STATIC_E2_BOUNDARY

The current D2 temporal computational-arrow route has exhausted its tested continuations. Finite public cycles are absorbed by public period traversal, the tested open chain factors through per-step Rabin/T417 inversion, and the closed public-squaring period route collapses to Rabin/factoring trapdoor equivalence. The route is therefore demoted to T417's static E2 boundary, with future D2 work reserved for a genuinely changed assumption or scope.

## Route Matrix

| route | source | status | decision effect |
| --- | --- | --- | --- |
| finite_public_cycle_or_bounded_nonrecovery | T420/T438 | absorbed | cannot carry D2 temporal-arrow novelty |
| open_rabin_lift_chain | T446/T448 | absorbed | collapses to chained T417/Rabin inversion |
| closed_public_squaring_period_oracle | T449/T450 | absorbed | no independent finite-witness temporal residue |
| changed_transition_or_open_nonpermutation | T444 plus T448 tested packet | future_exception_only | future work must supply a different packet, not reuse the T446 chain shape |
| nonstandard_period_assumption | T449/T450 | future_exception_only | only remaining admissible D2 continuation shape |

## Decision Screen

| check | status | passed? |
| --- | --- | --- |
| finite_cycle_route_closed | closed_by_t420_t438 | yes |
| open_chain_route_closed | closed_by_t448 | yes |
| closed_period_route_closed | closed_by_t450 | yes |
| future_exception_preserved | future_changed_assumption_only | yes |
| protected_surfaces_unchanged | no_claim_or_public_posture_move | yes |

## What this earns / does not earn

Earns: closure of the current temporal D2 route as a route-level decision. T417 remains as the static E2 computational-finality boundary.

Does not earn: claim promotion, claim-ledger movement, a computational-arrow theorem, a crypto theorem, a physics claim, North Star movement, or public posture.

Honest ceiling: Route-demotion packet only. T451 closes the current temporal D2 route back to T417's static E2 boundary; it does not demote the whole D2 definition, does not promote a claim, does not prove or refute factoring hardness, does not make a physics claim, and does not authorize public posture.

## Recommended Next

- Stop rebuilding the current public-squaring temporal D2 route.
- Keep T417 as the static E2 computational-finality boundary.
- Only reopen temporal D2 with a changed assumption or packet that clears T438/T444 and avoids T448/T450 absorbers.
