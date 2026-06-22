# T181: Branch-Failure Threshold Theorem

## Route

Quantum measurement / classical records, with thermodynamic-arrow and
mathematical-machinery pressure.

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [T179: Fixed-Accounting Capability Topology](T179-fixed-accounting-capability-topology.md)
- [T180: Branch-Support Threshold Minimality](T180-branch-support-threshold-minimality.md)

## Question

T180 showed that exact `branch_support` is not minimal for
`survive_one_branch_failure`.

Does the general unnamed branch-failure family factor through thresholds
`branch_support >= k + 1`, and where does that threshold account first fail?

## Motivation

The useful survivor after H7 demotion is not "branch topology matters" in the
abstract. The value is knowing exactly which topology coordinate is forced by a
declared future task after thermodynamic and control accounting are matched.

## Setup

Use a valid-provenance fixed-accounting record family over branch supports of
`A, B, C, D`. Hold the T145/T179 absorber vector fixed.

Audit:

1. unnamed `survive_k_branch_failures` for each fixed `k`;
2. whether exact support count is over-specified for fixed `k`;
3. whether exact support count is needed for the variable margin task
   `max_tolerated_branch_failures`;
4. whether branch identity is needed for a named outage task.

## Success Criteria

- Every unnamed fixed-`k` survival task factors through
  `branch_support >= k + 1`.
- Exact support count is shown nonminimal for fixed one-failure survival.
- Exact support count is shown load-bearing for a margin capability.
- Support identity is shown load-bearing for named/correlated hazard tasks.
- H7 remains demoted: this is capability residue, not arrow evidence.

## Failure Criteria

- The threshold theorem is stated without checking hostile boundary tasks.
- Named hazards are reduced to count thresholds without a witness test.
- Fixed-accounting capability residue is promoted into thermodynamic-arrow or
  physical-arrow evidence.

## Claim Impact

H7 remains `weakened_conditional`.

The sharpened residue is:

```text
For unnamed branch-failure tasks, branch_support >= k + 1 is the fixed-k
capability coordinate. Exact count is a margin coordinate. Branch identity is a
hazard-coordinate only after the task names or correlates failure regions.
```

## Reproduction

```bash
python -m unittest tests.test_branch_failure_threshold_theorem -v
python -m models.run_t181
```
