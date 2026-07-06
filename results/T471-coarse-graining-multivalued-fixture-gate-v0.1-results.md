# T471 - Coarse-Graining Multivalued Fixture Gate - v0.1 results

> Alphabet-stress gate only. No claim status, roadmap, README, North Star, public-posture, hard-policy, or cross-repo movement.

- Spec: `tests/T471-coarse-graining-multivalued-fixture-gate.md`
- Model: `models/coarse_graining_multivalued_fixture_gate.py`
- Tests: `tests/test_coarse_graining_multivalued_fixture_gate.py`
- Artifact JSON: `results/T471-coarse-graining-multivalued-fixture-gate-v0.1.json`
- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`
- Prior gates: T467, T468, T469

## Overall verdict: MULTIVALUED_FIXTURE_GATE_BUILT_NO_PROMOTION

The T469 packet shape survives the ternary holder alphabet: finality band and support count remain independent positive controls, while cheap modular sum, label restatement, hidden field, microstate identity, and observer-creates-truth controls are blocked. This is an alphabet-stress gate only, not an Observer Theory equivalence theorem or claim promotion.

## Positive-Control Partition Comparison

| alphabet size | holder width | state count | finality-band classes | support-count classes | identical? |
| --- | --- | --- | --- | --- | --- |
| 2 | 3 | 8 | 3 | 4 | False |
| 3 | 3 | 27 | 4 | 4 | False |

## Packet Decisions

| packet | decision | route | positives independent? | hostile controls blocked? | blockers |
| --- | --- | --- | --- | --- | --- |
| binary_three_holder_packet | admitted_for_review | REPAIRED_TASK_NATURALNESS_PACKET_ADMITTED | True | True | none |
| ternary_three_holder_packet | admitted_for_review | REPAIRED_TASK_NATURALNESS_PACKET_ADMITTED | True | True | none |

## Candidate Decisions

| candidate | role | decision | route | base route | blockers |
| --- | --- | --- | --- | --- | --- |
| binary_finality_band | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| binary_support_count | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| binary_mod_sum_with_task_label | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | certified_record_object_not_named, record_value_or_support_not_preserved, task_semantics_restates_label |
| binary_label_restatement_lookup | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | record_value_or_support_not_preserved, task_semantics_restates_label |
| binary_hidden_fourth_field_task | hostile_control | not_admitted | BASE_CERTIFICATION_GATE_NOT_MET | INACCESSIBLE_RECORD_FIELD | base_gate:INACCESSIBLE_RECORD_FIELD |
| binary_microstate_identity | hostile_control | not_admitted | BASE_CERTIFICATION_GATE_NOT_MET | TOO_FINE_MICROSTATE_TRACKING | base_gate:TOO_FINE_MICROSTATE_TRACKING |
| binary_observer_creates_truth_overread | forbidden_control | blocked | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | base_gate:FORBIDDEN_POSTURE_OR_CREATION_OVERREAD, observer_creates_truth_overread |
| ternary_finality_band | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| ternary_support_count | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| ternary_mod_sum_with_task_label | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | certified_record_object_not_named, record_value_or_support_not_preserved, task_semantics_restates_label |
| ternary_label_restatement_lookup | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | record_value_or_support_not_preserved, task_semantics_restates_label |
| ternary_hidden_fourth_field_task | hostile_control | not_admitted | BASE_CERTIFICATION_GATE_NOT_MET | INACCESSIBLE_RECORD_FIELD | base_gate:INACCESSIBLE_RECORD_FIELD |
| ternary_microstate_identity | hostile_control | not_admitted | BASE_CERTIFICATION_GATE_NOT_MET | TOO_FINE_MICROSTATE_TRACKING | base_gate:TOO_FINE_MICROSTATE_TRACKING |
| ternary_observer_creates_truth_overread | forbidden_control | blocked | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | base_gate:FORBIDDEN_POSTURE_OR_CREATION_OVERREAD, observer_creates_truth_overread |

## Future Packet Minimum

- stress constructive packets across at least one non-binary alphabet
- keep independent positive controls under alphabet transport
- include cheap accessible arithmetic partitions as hostile controls
- block label restatement and microstate identity before claim movement
- keep certified-record and observer-creates-truth guardrails active

## What This Does Not Earn

- D1 promotion
- T10 superselection result
- T29 projection-obstruction promotion
- observer-theory equivalence theorem
- physics or consciousness claim
- claim-ledger movement
- public-posture movement
