# T450 - E2 Period-Oracle Trapdoor Equivalence - v0.1 results

> Recorded-tier trapdoor-equivalence audit. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, no claim promotion, no public posture.

- Spec: `tests/T450-e2-period-oracle-trapdoor-equivalence.md`
- Model: `models/e2_period_oracle_trapdoor_equivalence.py`
- Tests: `tests/test_e2_period_oracle_trapdoor_equivalence.py`
- Artifact JSON: `results/T450-e2-period-oracle-trapdoor-equivalence-v0.1.json`
- Sources: T417, T438, T449, and the D2 open problem

## Overall verdict: PERIOD_ORACLE_COLLAPSES_TO_RABIN_TRAPDOOR_NO_INDEPENDENT_D2_ROUTE

For the current closed public-squaring route, an all-target period oracle is trapdoor-strength: it gives unique predecessors, and Rabin's reduction factors N from such a predecessor oracle. Conversely, group-order/factorization completion computes periods. The remaining D2 route therefore has no independent finite-witness residue beyond the standard Rabin/factoring boundary unless a future theorem target changes the oracle scope or assumption.

## Period Oracle To Predecessor

| modulus | N | target | period | predecessor | verifies? |
| --- | ---: | ---: | ---: | ---: | --- |
| N0_T419_control | 77 | 16 | 4 | 4 | yes |
| N1_hidden_order_control | 209 | 16 | 12 | 4 | yes |
| N2_hidden_order_control | 713 | 81 | 20 | 9 | yes |
| N3_hidden_order_control | 8549 | 16 | 40 | 4 | yes |
| N4_hidden_order_control | 23449 | 9 | 132 | 3 | yes |

## Period Oracle To Factorization

| modulus | N | factor | cofactor | factors? |
| --- | ---: | ---: | ---: | --- |
| N0_T419_control | 77 | 7 | 11 | yes |
| N1_hidden_order_control | 209 | 11 | 19 | yes |
| N2_hidden_order_control | 713 | 23 | 31 | yes |
| N3_hidden_order_control | 8549 | 103 | 83 | yes |
| N4_hidden_order_control | 23449 | 131 | 179 | yes |

## Oracle Scope Classifier

| scope | reverses arbitrary target? | factors by Rabin? | status |
| --- | --- | --- | --- |
| single_seed_period_value | no | no | insufficient_for_d2_packet |
| challenge_target_period_value | no | no | single_challenge_predecessor_only |
| all_qr_targets_period_oracle | yes | yes | trapdoor_strength |
| group_order_or_factorization_completion | yes | yes | native_trapdoor_completion |

## Absorber Screen

| check | status | passed? |
| --- | --- | --- |
| period_oracle_gives_predecessor | temporal_capability_reduced_to_period_value | yes |
| predecessor_oracle_factors_n | rabin_trapdoor_equivalence_exhibited | yes |
| trapdoor_completion_computes_periods | completion_absorbs_period_object | yes |
| oracle_scope_controls | scope_guardrail_recorded | yes |
| independent_d2_residue | not_found_for_current_route | yes |

## What this earns / does not earn

Earns: a runnable collapse audit for the current closed public-squaring period route. The all-target period oracle is trapdoor-strength, and trapdoor completion computes periods.

Does not earn: D2 redesign, D2 abandonment, a computational-arrow theorem, a period-hardness theorem, a crypto theorem, a physics claim, claim-ledger movement, or public posture.

Honest ceiling: Recorded-tier trapdoor-equivalence audit only. T450 does not redesign or abandon D2, does not prove period hardness, does not prove factoring hardness, does not promote a claim, does not make a physics claim, and does not authorize public posture.

## Recommended Next

- Treat the current closed public-squaring period route as absorbed by Rabin/factoring trapdoor equivalence.
- Only continue D2 if a nonstandard period assumption is specified with scope that avoids both single-seed weakness and all-target trapdoor equivalence.
- Otherwise demote the temporal D2 route to T417's static E2 boundary in a separate governed decision packet.
