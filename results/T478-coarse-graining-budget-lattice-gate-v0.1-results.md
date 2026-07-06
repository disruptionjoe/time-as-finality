# T478 - Coarse-Graining Budget-Lattice Gate - v0.1 results

> Budget-lattice stress gate only. No claim status, roadmap, README, North Star, public-posture, hard-policy, or cross-repo movement.

- Spec: `tests/T478-coarse-graining-budget-lattice-gate.md`
- Model: `models/coarse_graining_budget_lattice_gate.py`
- Tests: `tests/test_coarse_graining_budget_lattice_gate.py`
- Artifact JSON: `results/T478-coarse-graining-budget-lattice-gate-v0.1.json`
- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`
- Prior gates: T467, T468, T469, T471, and T477

## Overall verdict: BUDGET_LATTICE_GATE_BUILT_PATH_INDEPENDENT_NO_PROMOTION

The repaired coarse-graining packet is coherent across this finite observer-budget lattice: admitted finality-natural relations do not disappear under access expansion, joins preserve prior admissions and admit only relations whose certified fields become available, and top-budget verdicts are independent of the access expansion path. Cheap arithmetic, label restatement, microstate identity, and observer-creates-truth controls remain blocked when they become accessible. This is an observer-indexed intake guardrail only, not a global valid-coarse-graining criterion.

## Budget Lattice

| budget | accessible fields | admitted candidates |
| --- | --- | --- |
| budget_01 | [0, 1] | pair_01_finality_band |
| budget_02 | [0, 2] | pair_02_finality_band |
| budget_03 | [0, 3] | boundary_pair_status |
| budget_012 | [0, 1, 2] | pair_01_finality_band, pair_02_finality_band, three_holder_finality_band, three_holder_support_count |
| budget_013 | [0, 1, 3] | boundary_pair_status, pair_01_finality_band |
| budget_023 | [0, 2, 3] | boundary_pair_status, pair_02_finality_band |
| budget_0123 | [0, 1, 2, 3] | boundary_pair_status, pair_01_finality_band, pair_02_finality_band, three_holder_finality_band, three_holder_support_count |

## Edge Monotonicity

| from | to | lost admissions | monotone? |
| --- | --- | --- | --- |
| budget_01 | budget_012 | none | True |
| budget_01 | budget_013 | none | True |
| budget_02 | budget_012 | none | True |
| budget_02 | budget_023 | none | True |
| budget_03 | budget_013 | none | True |
| budget_03 | budget_023 | none | True |
| budget_012 | budget_0123 | none | True |
| budget_013 | budget_0123 | none | True |
| budget_023 | budget_0123 | none | True |

## Join Checks

| left | right | join | newly admitted at join | path independent and explained? |
| --- | --- | --- | --- | --- |
| budget_01 | budget_02 | budget_012 | three_holder_finality_band, three_holder_support_count | True |
| budget_01 | budget_03 | budget_013 | none | True |
| budget_01 | budget_023 | budget_0123 | three_holder_finality_band, three_holder_support_count | True |
| budget_02 | budget_03 | budget_023 | none | True |
| budget_02 | budget_013 | budget_0123 | three_holder_finality_band, three_holder_support_count | True |
| budget_03 | budget_012 | budget_0123 | none | True |
| budget_012 | budget_013 | budget_0123 | none | True |
| budget_012 | budget_023 | budget_0123 | none | True |
| budget_013 | budget_023 | budget_0123 | three_holder_finality_band, three_holder_support_count | True |

## Candidate Transitions

| candidate | role | required fields | admitted budgets | first admitted budgets |
| --- | --- | --- | --- | --- |
| pair_01_finality_band | positive_control | [0, 1] | budget_01, budget_012, budget_013, budget_0123 | budget_01 |
| pair_02_finality_band | positive_control | [0, 2] | budget_02, budget_012, budget_023, budget_0123 | budget_02 |
| boundary_pair_status | observer_index_positive_control | [0, 3] | budget_03, budget_013, budget_023, budget_0123 | budget_03 |
| three_holder_finality_band | join_positive_control | [0, 1, 2] | budget_012, budget_0123 | budget_012 |
| three_holder_support_count | join_positive_control | [0, 1, 2] | budget_012, budget_0123 | budget_012 |
| cheap_pair01_parity_with_task_label | hostile_control | [0, 1] | none | none |
| cheap_triple_parity_with_task_label | hostile_control | [0, 1, 2] | none | none |
| label_restatement_lookup | hostile_control | [0, 1, 2] | none | none |
| microstate_identity | hostile_control | [0, 1, 2, 3] | none | none |
| observer_creates_truth_overread | forbidden_control | [0, 1] | none | none |

## Future Packet Minimum

- declare a finite observer-budget poset, not only one chain
- report edge monotonicity for admitted finality-natural relations
- report join/path checks for incomparable budget expansions
- explain every new admission by newly accessible certified record fields
- keep cheap arithmetic, label-restatement, microstate, and observer-creates-truth controls blocked at every accessible budget
- treat budget-indexed admissions as local review targets, not global valid-coarse-graining criteria

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
