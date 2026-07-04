# T444 - E2 Changed-Transition Regime Gate - v0.1 results

> Recorded-tier routing/admission gate. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, no claim promotion, no public posture.

- Spec: `tests/T444-e2-changed-transition-regime-gate.md`
- Model: `models/e2_changed_transition_regime_gate.py`
- Tests: `tests/test_e2_changed_transition_regime_gate.py`
- Artifact JSON: `results/T444-e2-changed-transition-regime-gate-v0.1.json`
- Sources: T438, D2 open problem, and adopted taxonomy reference

## Overall verdict: E2_CHANGED_TRANSITION_REGIME_GATE_BUILT_NO_D2_DECISION

T444 admits only predeclared changed-transition or open/nonpermutation packets for separate-spec review. It rejects post-hoc/hidden transition policies, thermodynamic/E1 packets, Brown-Susskind symmetric-complexity packets, pure epistemic ignorance, unfrozen transition evidence, missing open-dynamics law, and resource/environment completion. Closed public-permutation packets route back to T438.

## Imported T438 Guardrail

- T438 verdict: `E2_PERIOD_HARDNESS_ADMISSION_GATE_BUILT_NO_D2_DECISION`
- T438 routed packet ids: `['changed_public_transition_packet', 'open_nonpermutation_packet']`

## Admission Requirements

- family-level packet with security parameter
- not a closed public-permutation packet already governed by T438
- agent/access boundary declared for changed-transition packets
- transition evidence, transcript, or trace frozen before evaluation
- predeclared transition-update law, publication schedule, or open-dynamics law
- public verification or independent audit trail
- explicit distinction between capability boundary and mere ignorance
- named hardness, unpredictability, or theorem burden
- predeclared reduction or theorem target
- no post-hoc policy, hidden oracle, thermodynamic cost, symmetric complexity growth, or resource-completion absorber

## Packet Classification

| packet | label | route | admitted? |
| --- | --- | --- | --- |
| closed_public_permutation_period_packet | ROUTE_BACK_TO_T438_CLOSED_PUBLIC_PERMUTATION | route_back_to_t438 | no |
| post_hoc_transition_swap_packet | BLOCKED_POST_HOC_OR_HIDDEN_TRANSITION_POLICY | rejected | no |
| hidden_oracle_transition_packet | BLOCKED_POST_HOC_OR_HIDDEN_TRANSITION_POLICY | rejected | no |
| thermodynamic_transition_cost_packet | NOT_E2_THERMODYNAMIC_OR_ERASURE_E1 | rejected | no |
| brown_susskind_complexity_packet | NOT_E2_SYMMETRIC_COMPLEXITY_GROWTH | rejected | no |
| pure_unknown_transition_packet | REJECTED_EPISTEMIC_IGNORANCE_NOT_CAPABILITY_BOUNDARY | rejected | no |
| unfrozen_transition_evidence_packet | REJECTED_UNFROZEN_TRANSITION_EVIDENCE | rejected | no |
| predeclared_changed_transition_packet | ADMITTED_CHANGED_TRANSITION_SEPARATE_SPEC_NO_D2_DECISION | admitted_as_separate_spec_target | yes |
| open_nonpermutation_no_law_packet | REJECTED_NO_OPEN_DYNAMICS_LAW | rejected | no |
| resource_completion_absorbed_open_packet | REJECTED_RESOURCE_OR_ENVIRONMENT_COMPLETION_ABSORBS | rejected | no |
| predeclared_open_nonpermutation_packet | ADMITTED_OPEN_NONPERMUTATION_SEPARATE_SPEC_NO_D2_DECISION | admitted_as_separate_spec_target | yes |

## What this earns / does not earn

Earns: a reusable routing/admission classifier for the D2 packets T438 explicitly routed to a separate spec.

Does not earn: a D2 redesign, D2 abandonment, a computational arrow, a crypto theorem, a physics claim, claim-ledger movement, or public posture.

Honest ceiling: Recorded-tier routing/admission gate only. T444 does not redesign or abandon D2, does not promote a claim, does not prove cryptographic hardness, does not turn epistemic ignorance into finality, and does not authorize public posture.

## Recommended Next

- Use T438 for closed public-permutation period-hardness packets.
- Use T444 before any changed-transition or open/nonpermutation D2 attempt.
- Do not treat T444 admission as D2 redesign, D2 success, or claim support.
