# T477 - Coarse-Graining Budget-Index Gate - v0.1 results

> Budget-index stress gate only. No claim status, roadmap, README, North Star, public-posture, hard-policy, or cross-repo movement.

- Spec: `tests/T477-coarse-graining-budget-index-gate.md`
- Model: `models/coarse_graining_budget_index_gate.py`
- Tests: `tests/test_coarse_graining_budget_index_gate.py`
- Artifact JSON: `results/T477-coarse-graining-budget-index-gate-v0.1.json`
- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`
- Prior gates: T467, T468, T469, and T471

## Overall verdict: BUDGET_INDEX_GATE_BUILT_OBSERVER_INDEXED_NO_PROMOTION

The repaired valid-coarse-graining packet is observer-budget indexed. Three-holder positives persist when the observer budget expands; the boundary-pair record is rejected as inaccessible under the three-holder budget and admitted only after the fourth holder enters the declared access boundary. Cheap arithmetic, label restatement, microstate identity, and observer-creates-truth controls remain blocked under expanded access. This is a budget-index guardrail only, not an Observer Theory equivalence theorem or claim promotion.

## Budget Transitions

| candidate | three-holder route | four-holder route | transition |
| --- | --- | --- | --- |
| three_holder_finality_band | TASK_NATURALNESS_PACKET_CLEARED | TASK_NATURALNESS_PACKET_CLEARED | persists_admitted |
| three_holder_support_count | TASK_NATURALNESS_PACKET_CLEARED | TASK_NATURALNESS_PACKET_CLEARED | persists_admitted |
| boundary_pair_status | BASE_CERTIFICATION_GATE_NOT_MET | TASK_NATURALNESS_PACKET_CLEARED | observer_budget_reveals_new_admission |
| cheap_accessible_parity_with_task_label | TASK_NATURALNESS_NOT_MET | TASK_NATURALNESS_NOT_MET | stays_blocked |
| label_restatement_lookup | TASK_NATURALNESS_NOT_MET | TASK_NATURALNESS_NOT_MET | stays_blocked |
| microstate_identity | BASE_CERTIFICATION_GATE_NOT_MET | BASE_CERTIFICATION_GATE_NOT_MET | stays_blocked |
| observer_creates_truth_overread | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | stays_blocked |

## Budget: three_holder_budget

- accessible fields: `[0, 1, 2]`
- packet decision: `admitted_for_review`
- packet route: `REPAIRED_TASK_NATURALNESS_PACKET_ADMITTED`
- packet blockers: `none`

| candidate | role | decision | route | base route | blockers |
| --- | --- | --- | --- | --- | --- |
| three_holder_finality_band | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| three_holder_support_count | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| boundary_pair_status | observer_index_positive_control | not_admitted | BASE_CERTIFICATION_GATE_NOT_MET | INACCESSIBLE_RECORD_FIELD | base_gate:INACCESSIBLE_RECORD_FIELD |
| cheap_accessible_parity_with_task_label | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | certified_record_object_not_named, record_value_or_support_not_preserved, task_semantics_restates_label |
| label_restatement_lookup | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | record_value_or_support_not_preserved, task_semantics_restates_label |
| microstate_identity | hostile_control | not_admitted | BASE_CERTIFICATION_GATE_NOT_MET | TOO_FINE_MICROSTATE_TRACKING | base_gate:TOO_FINE_MICROSTATE_TRACKING |
| observer_creates_truth_overread | forbidden_control | blocked | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | base_gate:FORBIDDEN_POSTURE_OR_CREATION_OVERREAD, observer_creates_truth_overread |

## Budget: four_holder_budget

- accessible fields: `[0, 1, 2, 3]`
- packet decision: `admitted_for_review`
- packet route: `REPAIRED_TASK_NATURALNESS_PACKET_ADMITTED`
- packet blockers: `none`

| candidate | role | decision | route | base route | blockers |
| --- | --- | --- | --- | --- | --- |
| three_holder_finality_band | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| three_holder_support_count | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| boundary_pair_status | observer_index_positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| cheap_accessible_parity_with_task_label | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | certified_record_object_not_named, record_value_or_support_not_preserved, task_semantics_restates_label |
| label_restatement_lookup | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | record_value_or_support_not_preserved, task_semantics_restates_label |
| microstate_identity | hostile_control | not_admitted | BASE_CERTIFICATION_GATE_NOT_MET | TOO_FINE_MICROSTATE_TRACKING | base_gate:TOO_FINE_MICROSTATE_TRACKING |
| observer_creates_truth_overread | forbidden_control | blocked | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | base_gate:FORBIDDEN_POSTURE_OR_CREATION_OVERREAD, observer_creates_truth_overread |

## Future Packet Minimum

- declare the observer budget before selecting the relation
- report budget transitions for every candidate relation
- treat newly accessible record tasks as observer-indexed admissions, not global criteria
- show that cheap arithmetic and label-restatement controls remain blocked under expanded budgets
- keep microstate identity and observer-creates-truth overreads blocked before claim movement

## What This Does Not Earn

- D1 promotion
- T10 superselection result
- T29 projection-obstruction promotion
- observer-theory equivalence theorem
- global valid-coarse-graining criterion
- physics or consciousness claim
- claim-ledger movement
- roadmap movement
- public-posture movement
