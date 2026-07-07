# T482 - Internal Scale Generator Invariance Probe - v0.1 results

> Review probe only. No claim status, roadmap, README, North Star, public-posture, hard-policy, physics, scale-genesis, clock, duration, finality, or cross-repo movement.

- Spec: `tests/T482-internal-scale-generator-invariance-probe.md`
- Model: `models/internal_scale_generator_invariance_probe.py`
- Tests: `tests/test_internal_scale_generator_invariance_probe.py`
- Artifact JSON: `results/T482-internal-scale-generator-invariance-probe-v0.1.json`
- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- Local anchors: T24, T38, T480, and T481

## Overall verdict: D1_SUPPORT_GRADIENT_PROBE_BUILT_BOOKKEEPING_ONLY_NO_SCALE_STRUCTURE

T482 makes T481's review target concrete with a D1-support gradient generator. The packet is predeclared, uses the T24 field-valued D1 profile and T38/T480 comparison edges, passes positive/null controls, and is invariant under observer-label relabeling. It is still only D1-support bookkeeping because the bands factor entirely through the existing D1 profile tuple; no independent internal scale structure is earned.

## Local Anchor Checks

| check | value |
| --- | --- |
| t481_gate_passed | True |
| t481_synthetic_review_target_admitted | True |
| t481_external_bookkeeping_still_admitted | True |
| t481_no_internal_scale_structure_earned | True |
| t481_no_clock_or_duration_earned | True |
| t481_future_packet_requires_relabel_invariance | True |

## Support-Gradient Controls

| check | value |
| --- | --- |
| stratified_packet_nontrivial | True |
| uniform_packet_collapses_to_single_band | True |
| support_gradient_relabel_invariant | True |
| comparison_domain_predeclared_as_transport_edges | True |
| generator_factors_through_d1_profile | True |
| uses_clock_duration_or_finality_status | False |
| imports_rg_or_conformal_mechanism | False |

## Stratified Assignments

| observer | D1 profile tuple | support depth | band |
| --- | --- | --- | --- |
| civilization | [0, 0, 0, 0] | 0 | low_support |
| family | [2, 2, 1, 1] | 6 | middle_support |
| individual | [1, 1, 1, 1] | 4 | low_support |
| institution | [0, 0, 0, 0] | 0 | low_support |
| lab | [4, 3, 2, 2] | 11 | high_support |
| science | [2, 2, 1, 1] | 6 | middle_support |

## Candidate Evaluations

| candidate | role | decision | route | blockers |
| --- | --- | --- | --- | --- |
| d1_support_gradient_review_packet | positive_review_control | admit_review_packet_no_scale_structure | D1_SUPPORT_GRADIENT_REVIEW_ADMITTED_BOOKKEEPING_ONLY | none |
| label_word_internal_scale | hostile_control | reject_or_block | INTERNAL_SCALE_GENERATOR_PACKET_BLOCKED | generator_not_predeclared, comparison_domain_not_predeclared, positive_negative_controls_missing, relabel_invariance_check_missing, label_word_without_generator |
| posthoc_support_thresholds | hostile_control | reject_or_block | INTERNAL_SCALE_GENERATOR_PACKET_BLOCKED | generator_not_predeclared, comparison_domain_not_predeclared, posthoc_thresholds |
| observer_id_rank_generator | hostile_control | reject_or_block | INTERNAL_SCALE_GENERATOR_PACKET_BLOCKED | observer_label_order_not_relabel_invariant |
| hidden_time_step_generator | hostile_control | reject_or_block | INTERNAL_SCALE_GENERATOR_PACKET_BLOCKED | positive_negative_controls_missing, hidden_calendar_or_time_order, clock_duration_or_arrow_overread |
| finality_by_support_band | hostile_control | reject_or_block | INTERNAL_SCALE_GENERATOR_PACKET_BLOCKED | record_finality_change_overread |
| rg_fixed_point_scale_generator | hostile_control | reject_or_block | INTERNAL_SCALE_GENERATOR_PACKET_BLOCKED | positive_negative_controls_missing, relabel_invariance_check_missing, rg_or_conformal_mechanism_imported, scale_genesis_or_physics_claim_overread, no_local_taf_anchor |
| promotion_shortcut_generator | hostile_control | reject_or_block | INTERNAL_SCALE_GENERATOR_PACKET_BLOCKED | scale_genesis_or_physics_claim_overread, claim_or_public_posture_promotion_shortcut |

## Future Packet Minimum

- keep support-gradient packets labeled as D1 bookkeeping unless an independent generator is supplied
- predeclare bands, comparison domain, controls, and relabel-invariance checks before witness construction
- include a null control where uniform D1 support collapses to one band
- include hostile controls for label order, posthoc thresholds, hidden time, finality changes, RG imports, and promotion shortcuts
- block clock, duration, temporal-arrow, finality, scale-genesis, physics, and claim movement unless separately earned

## What This Does Not Earn

- independent internal scale structure
- record clock
- duration or temporal arrow
- record-finality change
- scale-genesis theorem
- physics or conformal-gravity claim
- D1 promotion
- RG/TaF equivalence theorem
- claim-ledger movement
- roadmap movement
- North Star movement
- public-posture movement
