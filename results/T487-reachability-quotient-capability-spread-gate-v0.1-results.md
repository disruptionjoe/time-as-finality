# T487 - Reachability Quotient Capability Spread Gate - v0.1 results

> Downstream capability-spread gate only. This consumes the committed T485 artifact and does not rerun T485 or change claim status, roadmap, README, North Star, public posture, hard policy, physics posture, scale, clock, duration, finality, or cross-repo truth.

- Spec: `tests/T487-reachability-quotient-capability-spread-gate.md`
- Model: `models/reachability_quotient_capability_spread_gate.py`
- Tests: `tests/test_reachability_quotient_capability_spread_gate.py`
- Artifact JSON: `results/T487-reachability-quotient-capability-spread-gate-v0.1.json`
- Anchor artifact: `results/T485-transport-topology-invariant-quotient-gate-v0.1.json`

## Overall verdict: REACHABILITY_QUOTIENT_CAPABILITY_SPREAD_BUILT_TASK_ONLY

The T485 quotient signature is sufficient for the declared reachability task and quotient role-profile task. It is not sufficient for path-latency, relay-budget, or component-size capabilities, whose spreads are non-singleton over the same visible quotient class. Finality, scale, physics, and promotion readings remain blocked overreads.

## T485 Anchor

| field | value |
| --- | --- |
| artifact_id | T485-transport-topology-invariant-quotient-gate-v0.1 |
| verdict | TRANSPORT_TOPOLOGY_INVARIANT_QUOTIENT_BUILT_REACHABILITY_ONLY |
| gate_passed | True |
| reachability_quotient_admitted | True |
| component_size_scale_blocked | True |
| hop_band_scale_blocked | True |
| record_finality_change_earned | False |

## Fixture Rows

| fixture | quotient signature | reachable | hop band | relays | max component size |
| --- | --- | --- | --- | --- | --- |
| connected_original | (('source_target_component', 4),) | True | short | 0 | 4 |
| connected_subdivided_once | (('source_target_component', 4),) | True | middle | 3 | 7 |
| connected_subdivided_twice | (('source_target_component', 4),) | True | long | 9 | 13 |
| partitioned_original | (('source_side_component', 2), ('target_side_component', 2)) | False | unreachable | 0 | 2 |
| partitioned_subdivided_once | (('source_side_component', 2), ('target_side_component', 2)) | False | unreachable | 2 | 3 |
| partitioned_subdivided_twice | (('source_side_component', 2), ('target_side_component', 2)) | False | unreachable | 6 | 5 |
| connected_relabel | (('source_target_component', 4),) | True | short | 0 | 4 |

## Capability Spreads

| capability field | singleton on visible fibers | visible-class spreads |
| --- | --- | --- |
| source_target_reachable | True | {"(('source_side_component', 2), ('target_side_component', 2))": ['False'], "(('source_target_component', 4),)": ['True']} |
| quotient_role_profile | True | {"(('source_side_component', 2), ('target_side_component', 2))": ["(('source_side_component', 2), ('target_side_component', 2))"], "(('source_target_component', 4),)": ["(('source_target_component', 4),)"]} |
| source_target_hop_band | False | {"(('source_side_component', 2), ('target_side_component', 2))": ["'unreachable'"], "(('source_target_component', 4),)": ["'long'", "'middle'", "'short'"]} |
| relay_site_count | False | {"(('source_side_component', 2), ('target_side_component', 2))": ['0', '2', '6'], "(('source_target_component', 4),)": ['0', '3', '9']} |
| max_component_size | False | {"(('source_side_component', 2), ('target_side_component', 2))": ['2', '3', '5'], "(('source_target_component', 4),)": ['13', '4', '7']} |
| record_finality_status | True | {"(('source_side_component', 2), ('target_side_component', 2))": ["'unchanged'"], "(('source_target_component', 4),)": ["'unchanged'"]} |
| claim_or_public_posture_status | True | {"(('source_side_component', 2), ('target_side_component', 2))": ["'none'"], "(('source_target_component', 4),)": ["'none'"]} |

## Candidate Evaluations

| candidate | role | decision | route | blockers |
| --- | --- | --- | --- | --- |
| source_target_reachability_task | positive_review_control | admit_declared_reachability_task_only | REACHABILITY_CAPABILITY_SPREAD_SINGLETON | none |
| quotient_role_profile_task | positive_review_control | admit_declared_reachability_task_only | REACHABILITY_CAPABILITY_SPREAD_SINGLETON | none |
| path_latency_band_task | hostile_control | reject_non_singleton_spread | CAPABILITY_UNDERDETERMINED_BY_QUOTIENT | capability_not_task_natural_under_t485, non_singleton_capability_spread, path_or_hop_band_refinement_variant, clock_duration_or_arrow_overread |
| relay_budget_task | hostile_control | reject_non_singleton_spread | CAPABILITY_UNDERDETERMINED_BY_QUOTIENT | capability_not_task_natural_under_t485, non_singleton_capability_spread, relay_count_refinement_artifact, clock_duration_or_arrow_overread |
| component_size_capacity_task | hostile_control | reject_non_singleton_spread | CAPABILITY_UNDERDETERMINED_BY_QUOTIENT | capability_not_task_natural_under_t485, non_singleton_capability_spread, component_size_refinement_variant, reachability_quotient_not_internal_scale_structure |
| reachability_finality_task | hostile_control | reject_or_block | CAPABILITY_READING_BLOCKED | capability_not_task_natural_under_t485, record_finality_change_overread |
| quotient_promotion_task | hostile_control | reject_or_block | CAPABILITY_READING_BLOCKED | capability_not_task_natural_under_t485, reachability_quotient_not_internal_scale_structure, scale_genesis_or_physics_claim_overread, claim_or_public_posture_promotion_shortcut |

## Future Packet Minimum

- state the capability object before reading the reachability quotient as sufficient
- compute capability spread over quotient-visible fibers
- treat non-singleton path, relay, and component-size spreads as underdetermination
- do not convert reachability sufficiency into scale, clock, duration, finality, physics, or promotion evidence

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
