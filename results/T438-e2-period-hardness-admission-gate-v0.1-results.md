# T438 - E2 Period-Hardness Admission Gate - v0.1 results

> Recorded-tier admission gate. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, no claim promotion, no public posture.

- Spec (frozen first): `tests/T438-e2-period-hardness-admission-gate.md`
- Model: `models/e2_period_hardness_admission_gate.py`
- Tests: `tests/test_e2_period_hardness_admission_gate.py`
- Artifact JSON: `results/T438-e2-period-hardness-admission-gate-v0.1.json`
- Sources: T417, T419, T420, D2 open problem, and the adopted taxonomy reference

## Overall verdict: E2_PERIOD_HARDNESS_ADMISSION_GATE_BUILT_NO_D2_DECISION

T438 admits only a predeclared family-level period-hardness packet as a future E2 redesign target. It rejects finite public cycles, bounded non-recovery, point-inversion-only static relabels, E1 thermodynamic packets, Brown-Susskind complexity-growth packets, single-instance claims, and post-hoc selectors. Packets that leave the closed public-permutation regime require a separate spec.

## Imported T420 Guardrail

- T419 seed orbit: `[4, 16, 25, 9]`
- Public predecessor label: `9`
- Max public forward steps to predecessor: `3`

## Admission Requirements

- family-level packet, not a single fixed finite instance
- security parameter declared
- closed public-permutation regime declared, or else routed to a separate spec
- public transition knowledge fixed
- period/reversal problem stated, not only point inversion
- named period-hardness assumption or theorem target
- predeclared reduction or proof obligation
- bounded non-recovery is not treated as evidence
- no post-hoc policy, hidden label, thermodynamic cost, or symmetric complexity-growth basis

## Packet Classification

| packet | label | route | admitted? |
| --- | --- | --- | --- |
| t419_qr77_finite_public_cycle | REJECTED_T420_PUBLIC_CYCLE_ABSORBS_ARROW | rejected | no |
| long_cycle_bounded_nonrecovery_only | REJECTED_BOUNDED_NONRECOVERY_NOT_EVIDENCE | rejected | no |
| point_sqrt_hardness_static_relabel | REJECTED_STATIC_T417_RELABEL | rejected | no |
| single_instance_hard_theorem_claim | REJECTED_SINGLE_INSTANCE_FINITE_CRACKABLE | rejected | no |
| thermodynamic_reversal_cost_packet | NOT_E2_THERMODYNAMIC_OR_ERASURE_E1 | rejected | no |
| brown_susskind_complexity_growth_packet | NOT_E2_SYMMETRIC_COMPLEXITY_GROWTH | rejected | no |
| post_hoc_period_policy_packet | BLOCKED_POST_HOC_OR_HIDDEN_SELECTOR | rejected | no |
| changed_public_transition_packet | ROUTE_TO_DIFFERENT_REGIME_SPEC | separate_spec_required | no |
| open_nonpermutation_packet | ROUTE_TO_DIFFERENT_REGIME_SPEC | separate_spec_required | no |
| predeclared_period_hardness_family_packet | ADMITTED_E2_PERIOD_HARDNESS_REDESIGN_PACKET_NO_D2_DECISION | admitted_as_future_target | yes |

## What this earns / does not earn

Earns: a reusable admission classifier for future E2 computational-finality packets after T419/T420.

Does not earn: a D2 redesign, D2 abandonment, a computational arrow, a crypto theorem, a physics claim, claim-ledger movement, or public posture.

Honest ceiling: Recorded-tier admission gate only. T438 does not redesign or abandon D2, does not promote a claim, does not prove cryptographic hardness, does not make a physics claim, and does not authorize public posture.

## Recommended Next

- Any D2 continuation should first supply the admitted period-hardness packet fields.
- If that packet cannot be supplied, demote the temporal story to T417's static E2 boundary.
- Changed-transition or open-regime ideas need their own spec before execution.
