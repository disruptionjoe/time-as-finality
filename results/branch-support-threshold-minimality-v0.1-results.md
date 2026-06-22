# T180 Results: Branch-Support Threshold Minimality

## Audit Table

| Projection | Factors through task | Distinct values | Witness pair | Verdict |
| --- | --- | --- | --- | --- |
| `exact_branch_support` | `True` | `3` | None | `factors_through_capability` |
| `backup_branch_threshold` | `True` | `2` | None | `factors_through_capability` |
| `holder_count_only` | `False` | `2` | `single_branch_triplicate / dual_branch_triplicate` | `does_not_factor_through_capability` |
| `causal_chain_count_only` | `False` | `2` | `single_branch_triplicate / dual_branch_triplicate` | `does_not_factor_through_capability` |
| `provenance_only` | `False` | `1` | `single_branch_triplicate / dual_branch_triplicate` | `does_not_factor_through_capability` |
| `nonsupport_topology_signature` | `False` | `2` | `single_branch_triplicate / dual_branch_triplicate` | `does_not_factor_through_capability` |

## Strongest Claim

For the current fixed-accounting branch-failure family, exact branch_support is not the minimal topology coordinate for the task survive_one_branch_failure. Capability already factors through the weaker threshold predicate backup_branch_threshold := [branch_support >= 2].

## What Improved

T180 sharpens T179's positive residue instead of inflating it. The surviving object is now task-relative and smaller: one-backup branch availability, not exact branch count.

## What Weakened

This weakens the stronger T179 guess that exact numeric branch_support is the minimal coordinate for the current branch-failure task. Profiles with branch_support 2 and 3 remain capability-equivalent in the tested family.

## Falsification Condition

The threshold claim fails if an admissible fixed-accounting profile pair with the same backup-branch threshold but different survive_one_branch_failure capability is found, or if the task is changed so that exact branch multiplicity beyond the threshold becomes operationally relevant.

## Claim Ledger Update

Add T180 to H7/T179: for the current fixed-accounting branch-failure survivor, exact branch_support is not the minimal future-capability coordinate. The current task factors through the coarser threshold backup_branch_threshold = [branch_support >= 2], while non-support topology signatures fail.

## Open Blocker

No theorem yet characterizes the full task family where threshold predicates branch_support >= k+1 are necessary and sufficient, or when richer topology data beyond thresholds becomes genuinely load-bearing under matched accounting.

## Suggested Next

Generalize or kill the pattern: test whether survive_k_branch_failures factors through branch_support >= k+1, and identify the first natural task that needs richer topology than a threshold.
