# T181 Results: Branch-Failure Threshold Theorem

## Theorem Candidate

For a valid-provenance fixed-accounting record family whose future task is survival after any unnamed set of at most k branch failures, capability factors through the threshold predicate branch_support >= k + 1. Exact branch count is unnecessary for each fixed k. Exact count becomes load-bearing for the variable margin task max_tolerated_branch_failures, and branch identity becomes load-bearing for named or correlated outage tasks.

## Threshold Audits

| Task | Projection | Factors | Projection values | Capability values | Witness |
| --- | --- | --- | --- | --- | --- |
| `survive_0_branch_failures` | `support_threshold_ge_1` | `True` | `1` | `1` | None |
| `survive_1_branch_failures` | `support_threshold_ge_2` | `True` | `2` | `2` | None |
| `survive_2_branch_failures` | `support_threshold_ge_3` | `True` | `2` | `2` | None |
| `survive_3_branch_failures` | `support_threshold_ge_4` | `True` | `2` | `2` | None |

## Boundary Audits

| Task | Projection | Factors | Projection values | Capability values | Witness |
| --- | --- | --- | --- | --- | --- |
| `survive_one_branch_failure` | `exact_branch_support_count` | `True` | `4` | `2` | None |
| `max_tolerated_branch_failures` | `support_threshold_ge_2` | `False` | `2` | `4` | `support_AB / support_ABC` |
| `max_tolerated_branch_failures` | `exact_branch_support_count` | `True` | `4` | `4` | None |
| `survive_named_outage_A_C` | `exact_branch_support_count` | `False` | `4` | `2` | `support_A / support_B` |
| `survive_named_outage_A_C` | `support_branch_identity_set` | `True` | `15` | `2` | None |

## Strongest Claim

The T179/T180 topology residue is narrower than exact branch multiplicity. For fixed unnamed k-failure survival, the earned coordinate is the threshold branch_support >= k + 1. Richer topology is justified only when the future task asks for a failure margin or names which branches can fail.

## What Improved

T181 turns the open T180 blocker into a finite theorem screen and adds the first boundary case. It separates threshold sufficiency, count-valued margin capability, and support-identity capability instead of treating all topology as one coordinate.

## What Weakened

This further weakens any claim that exact branch multiplicity is the generic fixed-accounting residue for branch-failure survival. Exact count is over-specified for every fixed unnamed k tested here, and branch identity, not count, is the next richer datum for named hazards.

## Falsification Condition

The threshold theorem fails if a valid-provenance fixed-accounting profile pair has the same branch_support >= k + 1 value but different survival under the declared unnamed k-failure task. The boundary classification fails if named or correlated hazards can be reduced to count thresholds under the same admissible family and task semantics.

## Claim Ledger Update

Add T181 after T180: for unnamed branch-failure tasks, branch_support >= k + 1 is sufficient for each fixed k and exact branch count is nonminimal. Exact count is needed for a margin capability, while support identity is needed for named/correlated hazard tasks. This remains fixed-accounting capability residue, not H7 physical-arrow evidence.

## Open Blocker

No physically grounded hazard model yet tells which branch identities are substrate-natural rather than labels, or how these finite support predicates should be transported into a smooth or quantum record setting without smuggling in the capability object.

## Suggested Next

Either attach the branch-identity boundary to a real detector or memory architecture, or prove a minimal-enrichment statement for hazard partitions: count thresholds for exchangeable hazards, support intersections for named hazards, and no H7 upgrade unless deletion remains constructor-impossible after full accounting.
