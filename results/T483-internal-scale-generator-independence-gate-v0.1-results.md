# T483 - Internal Scale Generator Independence Gate - v0.1 results

> Review gate only. No claim status, roadmap, README, North Star, public-posture, hard-policy, physics, scale-genesis, clock, duration, finality, or cross-repo movement.

- Spec: `tests/T483-internal-scale-generator-independence-gate.md`
- Model: `models/internal_scale_generator_independence_gate.py`
- Tests: `tests/test_internal_scale_generator_independence_gate.py`
- Artifact JSON: `results/T483-internal-scale-generator-independence-gate-v0.1.json`
- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- Local anchors: T24, T38, T480, T481, and T482

## Overall verdict: INTERNAL_SCALE_INDEPENDENCE_GATE_BUILT_REVIEW_TARGET_ONLY_NO_PROMOTION

T483 rejects T482-style support-gradient generators as D1 completion. A synthetic transport-topology generator separates T24/T38 connected vs partitioned fixtures while their D1 vectors are fixed and survives observer-label relabeling. This is admitted only as a future review target and transport-topology bookkeeping; it earns no internal scale structure, clock, duration, finality change, scale-genesis theorem, physics support, claim movement, or public-posture movement.

## Local Anchor Checks

| check | value |
| --- | --- |
| t482_gate_passed | True |
| t482_support_gradient_admitted_as_bookkeeping | True |
| t482_support_gradient_factors_through_d1 | True |
| t482_no_internal_scale_structure_earned | True |
| t482_no_clock_or_duration_earned | True |
| t482_future_packet_requires_independent_generator | True |

## Fixed-D1 Independence Controls

| check | value |
| --- | --- |
| fixed_d1_vectors_match | True |
| transport_topology_separates | True |
| transport_topology_relabel_invariant | True |
| connected_source_target_reachable | True |
| partitioned_source_target_reachable | False |
| d1_profile_completion_insufficient | True |
| uses_clock_duration_or_finality_status | False |
| imports_rg_or_conformal_mechanism | False |

## Connected Transport Assignments

| observer | D1 profile tuple | topology band | component size |
| --- | --- | --- | --- |
| family | [2, 2, 1, 1] | source_target_component | 4 |
| individual | [2, 2, 1, 1] | source_target_component | 4 |
| institution | [2, 2, 1, 1] | source_target_component | 4 |
| lab | [2, 2, 1, 1] | source_target_component | 4 |

## Partitioned Transport Assignments

| observer | D1 profile tuple | topology band | component size |
| --- | --- | --- | --- |
| family | [2, 2, 1, 1] | source_side_component | 2 |
| individual | [2, 2, 1, 1] | source_side_component | 2 |
| institution | [2, 2, 1, 1] | target_side_component | 2 |
| lab | [2, 2, 1, 1] | target_side_component | 2 |

## Candidate Evaluations

| candidate | role | decision | route | blockers |
| --- | --- | --- | --- | --- |
| t482_d1_support_gradient | absorbed_control | reject_d1_completion_absorbed | D1_COMPLETION_ABSORBED_GENERATOR | d1_profile_completion_absorbs_generator |
| transport_topology_review_target | positive_review_control | admit_review_target_no_scale_structure | TRANSPORT_TOPOLOGY_REVIEW_TARGET_ADMITTED_NO_SCALE_STRUCTURE | none |
| label_word_independence | hostile_control | reject_or_block | INDEPENDENCE_PACKET_BLOCKED | generator_not_predeclared, comparison_domain_not_predeclared, fixed_d1_counterfactual_control_missing, relabel_invariance_check_missing, label_word_without_generator |
| posthoc_counterfactual_selector | hostile_control | reject_or_block | INDEPENDENCE_PACKET_BLOCKED | generator_not_predeclared, comparison_domain_not_predeclared, posthoc_counterfactual_selection |
| observer_id_rank_independence | hostile_control | reject_or_block | INDEPENDENCE_PACKET_BLOCKED | observer_label_order_not_relabel_invariant |
| hidden_time_order_independence | hostile_control | reject_or_block | INDEPENDENCE_PACKET_BLOCKED | fixed_d1_counterfactual_control_missing, hidden_calendar_or_time_order, clock_duration_or_arrow_overread |
| finality_by_transport_component | hostile_control | reject_or_block | INDEPENDENCE_PACKET_BLOCKED | record_finality_change_overread |
| rg_fixed_point_independence_source | hostile_control | reject_or_block | INDEPENDENCE_PACKET_BLOCKED | fixed_d1_counterfactual_control_missing, relabel_invariance_check_missing, rg_or_conformal_mechanism_imported, scale_genesis_or_physics_claim_overread, no_local_taf_anchor |
| promotion_shortcut_independence | hostile_control | reject_or_block | INDEPENDENCE_PACKET_BLOCKED | scale_genesis_or_physics_claim_overread, claim_or_public_posture_promotion_shortcut |

## Future Packet Minimum

- prove the generator is not recoverable from the existing D1 profile tuple
- include a fixed-D1 counterfactual pair before claiming independence
- separate transport topology from scale, clock, duration, and finality language
- preserve relabel-invariance under observer ID permutation
- block label-only, posthoc, hidden-time, finality, RG/conformal, physics, and promotion shortcuts
- treat fixed-D1 transport-topology separation as review metadata unless a separate theorem earns more

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
