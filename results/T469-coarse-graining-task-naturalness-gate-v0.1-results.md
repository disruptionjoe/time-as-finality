# T469 - Coarse-Graining Task-Naturalness Gate - v0.1 results

> Fixture repair and admission gate only. No claim status, roadmap, README, North Star, public-posture, hard-policy, or cross-repo movement.

- Spec: `tests/T469-coarse-graining-task-naturalness-gate.md`
- Model: `models/coarse_graining_task_naturalness_gate.py`
- Tests: `tests/test_coarse_graining_task_naturalness_gate.py`
- Artifact JSON: `results/T469-coarse-graining-task-naturalness-gate-v0.1.json`
- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`
- Prior audits: T467, T468

## Overall verdict: TASK_NATURALNESS_GATE_BUILT_FIXTURE_REPAIRED_NO_PROMOTION

The repaired three-holder packet clears review admission with independent finality-band and support-count positives, while the legacy two-holder packet fails positive-control independence. The cheap accessible xor control still passes the old mechanical gate if a task label is asserted, but T469 blocks it because no certified record object or natural finality task is supplied.

## Packet Decisions

| packet | decision | route | positives independent? | hostile controls blocked? | blockers |
| --- | --- | --- | --- | --- | --- |
| repaired_three_holder_packet | admitted_for_review | REPAIRED_TASK_NATURALNESS_PACKET_ADMITTED | True | True | none |
| legacy_two_holder_packet | not_admitted | POSITIVE_CONTROL_INDEPENDENCE_NOT_MET | False | True | positive_controls_not_independent |

## Candidate Decisions

| candidate | role | decision | route | base route | blockers |
| --- | --- | --- | --- | --- | --- |
| three_holder_finality_band | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| three_holder_support_count | positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| two_holder_finality_band | legacy_positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| two_holder_support_count | legacy_positive_control | admitted_for_review | TASK_NATURALNESS_PACKET_CLEARED | BOUNDED_OBSERVER_CERTIFIABLE | none |
| cheap_accessible_xor_with_task_label | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | certified_record_object_not_named, record_value_or_support_not_preserved, task_semantics_restates_label |
| label_restatement_lookup | hostile_control | not_admitted | TASK_NATURALNESS_NOT_MET | BOUNDED_OBSERVER_CERTIFIABLE | record_value_or_support_not_preserved, task_semantics_restates_label |
| hidden_fourth_field_task | hostile_control | not_admitted | BASE_CERTIFICATION_GATE_NOT_MET | INACCESSIBLE_RECORD_FIELD | base_gate:INACCESSIBLE_RECORD_FIELD |
| observer_creates_truth_overread | forbidden_control | blocked | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | base_gate:FORBIDDEN_POSTURE_OR_CREATION_OVERREAD, observer_creates_truth_overread |

## Future Packet Minimum

- use independent positive controls when claiming constructive support
- include cheap accessible non-finality hostile controls
- name a certified record object before selecting the relation
- show the task preserves record value, support, or finality status
- include a demotion condition for label-restatement or observer-creates-truth overread

## What This Does Not Earn

- D1 promotion
- T10 superselection result
- T29 projection-obstruction promotion
- observer-theory equivalence theorem
- physics or consciousness claim
- claim-ledger movement
- public-posture movement
