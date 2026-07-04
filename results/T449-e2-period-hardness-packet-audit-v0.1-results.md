# T449 - E2 Period-Hardness Packet Audit - v0.1 results

> Recorded-tier period-hardness packet audit. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, no claim promotion, no public posture.

- Spec: `tests/T449-e2-period-hardness-packet-audit.md`
- Model: `models/e2_period_hardness_packet_audit.py`
- Tests: `tests/test_e2_period_hardness_packet_audit.py`
- Artifact JSON: `results/T449-e2-period-hardness-packet-audit-v0.1.json`
- Sources: T420, T438, T448, and the D2 open problem

## Overall verdict: E2_PERIOD_HARDNESS_PACKET_SHARPENED_TO_HIDDEN_ORDER_THEOREM_TARGET_NO_D2_DECISION

The best remaining D2 route is now sharply typed: a closed public squaring family where the missing capability object is the orbit period. If the period is known, reversal is public; if group-order trapdoor data is admitted, the toy family is completed. What is not earned is the hardness theorem. Future progress needs a real hidden-order/cycle-length reduction or lower-bound target, plus seed-distribution controls.

## Packet

- Transition: `F_N(x) = x^2 mod N on QR_N`
- Period problem: Given public N, seed x in QR_N, and y = F_N(x), recover x by determining the orbit period L and computing F_N^(L-1)(y).
- Named burden: hidden-order/cycle-length hardness for public squaring in RSA/Blum groups; theorem target only in this repo artifact
- T438 route: `admitted_as_future_target` / `ADMITTED_E2_PERIOD_HARDNESS_REDESIGN_PACKET_NO_D2_DECISION`

## Family Period Audit

| modulus | N | selected seed | ord_N(seed) | period | period reverses? | QR order gives factors? |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| N0_T419_control | 77 | 4 | 15 | 4 | yes | yes |
| N1_hidden_order_control | 209 | 4 | 45 | 12 | yes | yes |
| N2_hidden_order_control | 713 | 9 | 165 | 20 | yes | yes |
| N3_hidden_order_control | 8549 | 4 | 2091 | 40 | yes | yes |
| N4_hidden_order_control | 23449 | 3 | 5785 | 132 | yes | yes |

## Small-Period Controls

| modulus | N | period | admitted as evidence? |
| --- | ---: | ---: | --- |
| N0_T419_control | 77 | 1 | no |
| N1_hidden_order_control | 209 | 1 | no |
| N2_hidden_order_control | 713 | 1 | no |
| N3_hidden_order_control | 8549 | 1 | no |
| N4_hidden_order_control | 23449 | 1 | no |

## Absorber Screen

| check | status | passed? |
| --- | --- | --- |
| t438_admission | admitted_as_theorem_target | yes |
| period_formula_matches_public_cycle | toy_formula_verified | yes |
| known_period_publicly_reverses | period_is_missing_capability_object | yes |
| group_order_completion_absorbs | trapdoor_completion_recorded | yes |
| small_period_seed_controls | seed_distribution_required | yes |
| hardness_theorem_gap | open_theorem_obligation | yes |

## What this earns / does not earn

Earns: a sharper D2 target. The live closed-regime packet is not point inversion or open-chain coupling; it is hidden-order cycle-length hardness for public squaring, with seed-distribution controls.

Does not earn: D2 redesign, D2 abandonment, a computational-arrow theorem, a period-hardness theorem, a crypto theorem, a physics claim, claim-ledger movement, or public posture.

Honest ceiling: Recorded-tier period-hardness packet audit only. T449 does not redesign or abandon D2, does not prove period hardness, does not prove factoring hardness, does not promote a claim, does not make a physics claim, and does not authorize public posture.

## Recommended Next

- Do not build another finite D2 toy unless it changes the theorem obligation.
- If D2 continues, write a theorem-target note for hidden-order cycle length: exact assumption, seed distribution, and reduction/lower-bound burden.
- If no such theorem target is acceptable, demote the temporal route back to T417's static E2 boundary.
