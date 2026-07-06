# T467 - Valid Coarse-Graining Admissibility Gate - v0.1 results

> Admission gate only. No claim status, roadmap, README, North Star, public-posture, hard-policy, or cross-repo movement.

- Spec: `tests/T467-valid-coarse-graining-admissibility-gate.md`
- Model: `models/valid_coarse_graining_admissibility_gate.py`
- Tests: `tests/test_valid_coarse_graining_admissibility_gate.py`
- Artifact JSON: `results/T467-valid-coarse-graining-admissibility-gate-v0.1.json`
- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`

## Overall verdict: VALID_COARSE_GRAINING_ADMISSIBILITY_GATE_BUILT_NO_PROMOTION

In this finite fixture, the bounded-observer certification filter admits only the declared finality-record band and local count controls. Microstate identity, trivial collapse, hidden fields, ornate lookup, posthoc partitions, projection-only shadows, one-holder dashboards, and observer-creates-truth overreads all fail before claim movement.

## Budget

- accessible fields: `[0, 1, 2]`
- max fields read: `2`
- max predicate cost: `3`
- min holder redundancy: `2`
- max reversal cost: `2`

## Gate Table

| candidate | decision | route | class count | blockers |
| --- | --- | --- | --- | --- |
| two_holder_finality_band | admitted_for_review | BOUNDED_OBSERVER_CERTIFIABLE | 3 | none |
| bounded_local_count | admitted_for_review | BOUNDED_OBSERVER_CERTIFIABLE | 3 | none |
| microstate_identity | not_admitted | TOO_FINE_MICROSTATE_TRACKING | 16 | uses_inaccessible_record_fields, field_budget_exceeded, predicate_cost_ornate, reversal_cost_over_budget, too_fine_microstate_identity |
| constant_all_states | not_admitted | TOO_COARSE_NO_TASK_SEPARATION | 1 | holder_redundancy_below_d1_floor, too_coarse_no_task_separation |
| hidden_fourth_field | not_admitted | INACCESSIBLE_RECORD_FIELD | 4 | uses_inaccessible_record_fields |
| ornate_table_lookup | not_admitted | COMPUTATION_COST_ORNATE_OR_OVER_BUDGET | 3 | predicate_cost_ornate |
| posthoc_exception_partition | not_admitted | POSTHOC_EQUIVALENCE_NOT_VALID | 2 | posthoc_equivalence_relation |
| projection_only_shadow | not_admitted | PROJECTION_IS_NOT_FINALITY | 2 | projection_without_certified_record |
| single_holder_dashboard | not_admitted | D1_CERTIFICATION_BUDGET_NOT_MET | 2 | holder_redundancy_below_d1_floor |
| observer_creates_truth_overread | blocked | FORBIDDEN_POSTURE_OR_CREATION_OVERREAD | 2 | observer_creates_truth_overread |

## Future Packet Minimum

- finite state universe and candidate equivalence relation declared
- record fields needed to classify each state named before selection
- all fields inside the observer access boundary
- recognition predicate within the declared computation budget
- D1-style holder redundancy and reversal-cost floors satisfied
- nontrivial coarse-graining: neither all states nor microstate identity
- certified record available, not projection alone
- finality-native task declared without observer-creates-truth overread
- positive and hostile controls included before any claim movement

## What This Does Not Earn

- D1 promotion
- T10 superselection result
- T29 projection-obstruction promotion
- observer-theory equivalence theorem
- physics or consciousness claim
- claim-ledger movement
- public-posture movement
