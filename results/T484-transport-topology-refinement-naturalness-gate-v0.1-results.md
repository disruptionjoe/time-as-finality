# T484 - Transport Topology Refinement Naturalness Gate - v0.1 results

> Review gate only. No claim status, roadmap, README, North Star, public-posture, hard-policy, physics, scale-genesis, clock, duration, finality, or cross-repo movement.

- Spec: `tests/T484-transport-topology-refinement-naturalness-gate.md`
- Model: `models/transport_topology_refinement_naturalness_gate.py`
- Tests: `tests/test_transport_topology_refinement_naturalness_gate.py`
- Artifact JSON: `results/T484-transport-topology-refinement-naturalness-gate-v0.1.json`
- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- Local anchors: T24, T38, T480, T481, T482, and T483

## Overall verdict: TRANSPORT_TOPOLOGY_REFINEMENT_GATE_BUILT_REACHABILITY_BOOKKEEPING_ONLY

T484 narrows the T483 transport-topology review target. Source/target reachability roles for the original T24/T38 observer sites are stable under edge subdivision and observer-label relabeling, so they remain admitted as review-grade reachability bookkeeping. Component size and shortest-path length change under the same benign refinement, so they are rejected as internal-scale, clock, duration, finality, or scale-genesis evidence.

## Local Anchor Checks

| check | value |
| --- | --- |
| t483_gate_passed | True |
| t483_transport_topology_review_target_admitted | True |
| t483_fixed_d1_control_passed | True |
| t483_no_internal_scale_structure_earned | True |
| t483_no_clock_or_duration_earned | True |
| t483_future_packet_requires_fixed_d1_control | True |

## Refinement Controls

| check | value |
| --- | --- |
| original_d1_vectors_fixed | True |
| reachability_separates_fixed_d1_pair | True |
| connected_refinement_preserves_original_roles | True |
| partitioned_refinement_preserves_original_roles | True |
| reachability_relabel_invariant | True |
| component_size_changes_under_refinement | True |
| path_length_changes_under_refinement | True |
| partitioned_source_target_remain_unreachable | True |
| uses_clock_duration_or_finality_status | False |
| imports_rg_or_conformal_mechanism | False |

## Connected Original Assignments

| observer | D1 profile tuple | topology role | component size | distance from source |
| --- | --- | --- | --- | --- |
| family | [2, 2, 1, 1] | source_target_component | 4 | 1 |
| individual | [2, 2, 1, 1] | source_target_component | 4 | 0 |
| institution | [2, 2, 1, 1] | source_target_component | 4 | 3 |
| lab | [2, 2, 1, 1] | source_target_component | 4 | 2 |

## Connected Refined Original Assignments

| observer | D1 profile tuple | topology role | component size | distance from source |
| --- | --- | --- | --- | --- |
| family | [2, 2, 1, 1] | source_target_component | 7 | 2 |
| individual | [2, 2, 1, 1] | source_target_component | 7 | 0 |
| institution | [2, 2, 1, 1] | source_target_component | 7 | 6 |
| lab | [2, 2, 1, 1] | source_target_component | 7 | 4 |

## Partitioned Original Assignments

| observer | D1 profile tuple | topology role | component size | distance from source |
| --- | --- | --- | --- | --- |
| family | [2, 2, 1, 1] | source_side_component | 2 | 1 |
| individual | [2, 2, 1, 1] | source_side_component | 2 | 0 |
| institution | [2, 2, 1, 1] | target_side_component | 2 | None |
| lab | [2, 2, 1, 1] | target_side_component | 2 | None |

## Partitioned Refined Original Assignments

| observer | D1 profile tuple | topology role | component size | distance from source |
| --- | --- | --- | --- | --- |
| family | [2, 2, 1, 1] | source_side_component | 3 | 2 |
| individual | [2, 2, 1, 1] | source_side_component | 3 | 0 |
| institution | [2, 2, 1, 1] | target_side_component | 3 | None |
| lab | [2, 2, 1, 1] | target_side_component | 3 | None |

## Candidate Evaluations

| candidate | role | decision | route | blockers |
| --- | --- | --- | --- | --- |
| source_target_reachability_packet | positive_review_control | admit_reachability_bookkeeping_no_scale_structure | REACHABILITY_BOOKKEEPING_ADMITTED_NO_SCALE_STRUCTURE | none |
| component_size_as_scale | hostile_control | reject_refinement_variant | REFINEMENT_VARIANT_SCALE_READING_BLOCKED | component_size_refinement_variant |
| shortest_path_length_as_scale | hostile_control | reject_refinement_variant | REFINEMENT_VARIANT_SCALE_READING_BLOCKED | path_length_refinement_variant |
| label_word_topology_scale | hostile_control | reject_or_block | TRANSPORT_TOPOLOGY_PACKET_BLOCKED | generator_not_predeclared, refinement_invariance_check_missing, relabel_invariance_check_missing, label_word_without_generator |
| observer_id_component_order | hostile_control | reject_or_block | TRANSPORT_TOPOLOGY_PACKET_BLOCKED | observer_label_order_not_relabel_invariant |
| relay_count_as_clock | hostile_control | reject_or_block | TRANSPORT_TOPOLOGY_PACKET_BLOCKED | hidden_calendar_or_time_order, clock_duration_or_arrow_overread |
| record_finality_by_reachability | hostile_control | reject_or_block | TRANSPORT_TOPOLOGY_PACKET_BLOCKED | record_finality_change_overread |
| rg_fixed_point_topology_source | hostile_control | reject_or_block | TRANSPORT_TOPOLOGY_PACKET_BLOCKED | fixed_d1_counterfactual_control_missing, refinement_invariance_check_missing, relabel_invariance_check_missing, rg_or_conformal_mechanism_imported, scale_genesis_or_physics_claim_overread, no_local_taf_anchor |
| promotion_shortcut_topology | hostile_control | reject_or_block | TRANSPORT_TOPOLOGY_PACKET_BLOCKED | scale_genesis_or_physics_claim_overread, claim_or_public_posture_promotion_shortcut |

## Future Packet Minimum

- treat fixed-D1 topology separation as reachability bookkeeping unless a separate theorem earns more
- include transport-refinement controls before using topology as a generator
- reject component-size and path-length scale readings unless an invariant morphism class is declared
- preserve observer-label relabel invariance
- separate reachability topology from scale, clock, duration, finality, RG/conformal, physics, and promotion language

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
