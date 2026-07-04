# T446 - E2 Family/Open-Regime Big Swing - v0.1 results

> Recorded-tier packet swing. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, no claim promotion, no public posture.

- Spec: `tests/T446-e2-family-open-regime-big-swing.md`
- Model: `models/e2_family_open_regime_big_swing.py`
- Tests: `tests/test_e2_family_open_regime_big_swing.py`
- Artifact JSON: `results/T446-e2-family-open-regime-big-swing-v0.1.json`
- Sources: T417, T438, T444, and the D2 open problem

## Overall verdict: E2_OPEN_RABIN_LIFT_PACKET_SURVIVES_SCREEN_WITH_T417_CHAIN_RESIDUAL_NO_D2_DECISION

The open Rabin-lift packet is the strongest safe candidate found in this swing. It clears the literal gate and absorber checks as a recorded-tier candidate packet: public transition, injective open dynamics, information-theoretic reversal, named Rabin hardness, and no reliance on E1 cost or symmetric complexity growth. It still carries a serious residual: the hard part is per-step Rabin/T417 inversion, so the packet may be a chained static boundary rather than a new D2 arrow theorem.

Toy status: toy arithmetic is crackable and used only to check algebra, not to evidence hardness

## Packet

Given x_t in QR(N_t), compute r_t = x_t^2 mod N_t, then lift x_{t+1} = r_t^2 as an integer QR element in N_{t+1}, with N_{t+1} > N_t^2.

Hardness assumption: Rabin square-root/factoring hardness for the current Blum modulus at each backward step.

## Gate Routes

- T438 route: `separate_spec_required` / `ROUTE_TO_DIFFERENT_REGIME_SPEC`
- T444 route: `admitted_as_separate_spec_target` / `ADMITTED_OPEN_NONPERMUTATION_SEPARATE_SPEC_NO_D2_DECISION`

## Schedule Audit

| label | N | QR_N size | Blum pair? | next N > N^2? |
| --- | ---: | ---: | --- | --- |
| N0_T417_T419 | 77 | 15 | yes | yes |
| N1_lift_domain | 8549 | 2091 | yes | yes |
| N2_lift_domain | 81162077 | 20286015 | yes | n/a |

## Chain Trace

| step | current N | next N | x_t | Rabin image | x_next | trapdoor reverses? | toy cycle cracks? |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0 | 77 | 8549 | 4 | 16 | 256 | yes | yes |
| 1 | 8549 | 81162077 | 256 | 5693 | 32410249 | yes | yes |

## Absorber Screen

| check | status | passed? |
| --- | --- | --- |
| t438_t444_route | survives | yes |
| information_present_reversal_exists | survives | yes |
| finite_cycle_toy_absorber | survives_with_toy_caveat | yes |
| static_t417_relabel_absorber | partial_residual | yes |
| pure_ignorance_absorber | survives | yes |
| e1_thermodynamic_cost_absorber | survives | yes |
| symmetric_complexity_growth_absorber | survives_with_growth_debt | yes |
| named_hardness_reduction | survives_conditionally | yes |

## What this earns / does not earn

Earns: a runnable candidate packet that clears T438/T444 routing, leaves the closed finite-cycle regime, keeps transition evidence public, and tests the main E2 absorbers directly.

Does not earn: a D2 redesign, D2 abandonment, computational-arrow theorem, crypto theorem, physics claim, claim-ledger movement, or public posture.

Honest ceiling: Recorded-tier packet swing only. T446 does not redesign or abandon D2, does not promote a claim, does not prove factoring hardness, does not make a physics claim, and does not authorize public posture. The strongest residual absorber is that the packet may be only a chained T417/Rabin static boundary with an open lift.

## Recommended Next

- Try to prove or kill the T417-chain residual: does coupled open iteration add any theorem beyond per-step Rabin inversion?
- Try to replace the size-growing lift with a bounded-growth open family, or record growth as a resource-completion absorber.
- Keep any future result recorded-tier until it earns a separate theorem or separation.
