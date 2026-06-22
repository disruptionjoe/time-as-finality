# T180: Branch-Support Threshold Minimality

## Route

Thermodynamic arrow of time, with mathematical-machinery pressure.

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [T179: Fixed-Accounting Capability Topology](T179-fixed-accounting-capability-topology.md)

## Question

T179 preserved a fixed-accounting branch-topology survivor and suggested that
`branch_support` might be the minimal topology coordinate for the task
`survive_one_branch_failure`.

Is that actually true, or does the current task already factor through a
weaker threshold predicate?

## Motivation

The highest-value move is to break the stronger conjecture before it hardens.
If the capability only depends on whether at least one backup branch remains,
then exact `branch_support` is an overstatement of the earned residue.

## Setup

Hold the T145/T179 absorber vector fixed and audit a small admissible family of
valid-provenance topology profiles with varying:

- holder count;
- causal-chain count; and
- branch support.

Test the declared future task:

```text
survive_one_branch_failure
```

Audit these projections:

1. exact `branch_support`
2. `backup_branch_threshold := [branch_support >= 2]`
3. `holder_count`
4. `causal_chain_count`
5. `provenance_valid`
6. the non-support signature `(holder_count, causal_chain_count, provenance)`

## Success Criteria

- The one-failure capability factors through `backup_branch_threshold`.
- Exact `branch_support` is shown to be sufficient but nonminimal.
- Non-support signatures fail on explicit witness pairs.
- The result refines T179 downward rather than reopening H7 upward.

## Failure Criteria

- Exact `branch_support` is asserted minimal without testing coarser
  threshold projections.
- Non-support coordinates are treated as sufficient without a factorization
  check.
- The result is promoted into thermodynamic-arrow evidence.

## Claim Impact

H7 remains `weakened_conditional`.

Add this sharpening:

```text
For the current fixed-accounting branch-failure survivor, the earned object is
task-relative backup-branch availability, not exact branch multiplicity.
```

## Reproduction

```bash
python -m unittest tests.test_branch_support_threshold_minimality -v
python -m models.run_t180
```
