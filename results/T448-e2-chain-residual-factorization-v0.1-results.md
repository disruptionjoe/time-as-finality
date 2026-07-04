# T448 - E2 Chain Residual Factorization - v0.1 results

> Recorded-tier residual audit. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, no claim promotion, no public posture.

- Spec: `tests/T448-e2-chain-residual-factorization.md`
- Model: `models/e2_chain_residual_factorization.py`
- Tests: `tests/test_e2_chain_residual_factorization.py`
- Artifact JSON: `results/T448-e2-chain-residual-factorization-v0.1.json`
- Sources: T417, T438, T444, T446, and the D2 open problem

## Overall verdict: T446_CHAIN_RESIDUAL_FACTORS_THROUGH_PER_STEP_RABIN_NO_NEW_D2_THEOREM

For the current T446 packet, coupled open iteration adds no new theorem beyond per-step Rabin inversion. Full-chain recovery factors through public lift unwraps and independent step oracles, and the length-one chain is already a Rabin inversion challenge. This kills the T446 residual as a positive D2 route, without abandoning the broader D2 open problem.

## Factorization

ChainInverse = public_lift_unwraps + product of independent RabinStepInverse(N_t) calls.

- Expected states: `[4, 256, 32410249]`
- Recovered states: `[4, 256, 32410249]`
- Step oracle calls equal transition count: `True`

| reverse order | step | modulus N | Rabin image | recovered predecessor |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 8549 | 5693 | 256 |
| 1 | 0 | 77 | 16 | 4 |

## Absorber Screen

| check | status | passed? |
| --- | --- | --- |
| full_chain_inversion_factors_through_step_oracles | residual_killed_for_current_packet | yes |
| length_one_embedding_is_rabin_step_problem | no_new_chain_problem | yes |
| next_domain_coupling_control | no_coupling_detected | yes |
| missing_step_oracle_dependency | product_dependency_recorded | yes |
| growth_debt_not_lock | growth_debt_remains | yes |

## Dependency Audit

| omitted step modulus | available step oracles | product decomposition runs? |
| --- | --- | --- |
| 77 | [8549] | no |
| 8549 | [77] | no |
| none | [77, 8549] | yes |

## What this earns / does not earn

Earns: a runnable resolution of the T446 residual for the current open Rabin-lift packet. The chain is product-decomposable into public lift unwraps plus independent per-step Rabin inversions.

Does not earn: D2 redesign, D2 abandonment, a computational-arrow theorem, a crypto theorem, a physics claim, claim-ledger movement, or public posture.

Honest ceiling: Recorded-tier residual audit only. T448 clarifies the current T446 packet; it does not redesign or abandon D2, does not prove or refute factoring hardness, does not promote a claim, does not make a physics claim, and does not authorize public posture.

## Recommended Next

- Treat the current T446 open Rabin-lift chain as absorbed by chained T417/Rabin inversion.
- If D2 continues, require a packet whose chain inversion is not product-decomposable into public unwraps plus independent step inversions.
- Alternatively return to T438 and pursue a true family-level period-hardness packet.
