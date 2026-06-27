# T350 Results: Best Soft Score

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `best_soft_score` | `{'name': 'soft_s_count_cubed', 'description': 'Soft score 8^(number of deletion T252-style passes).', 'total_weight': 1705336003, 'tail_weight': 1342177280, 'parentcap_weight': 1694613504, 'selected_weight': 134217728, 'tail_probability': {'fraction': '1342177280/1705336003', 'float': 0.7870456482704071}, 'parentcap_probability': {'fraction': '1694613504/1705336003', 'float': 0.9937123833771543}, 'selected_probability': {'fraction': '134217728/1705336003', 'float': 0.07870456482704072}, 'lift_vs_uniform': {'fraction': '6957847019520/243619429', 'float': 28560.312484436534}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': True}` |

- Verdict: `best_soft_score_is_cubic_deletion_t252_count`

## Strongest Claim

The best tested soft score is 8^(T252-style deletion pass count), with tail probability above three quarters.

## What This Improved

T350 shows deletion-count temperature can concentrate on the tail without an explicit tail indicator.

## What This Weakened Or Falsified

It weakens low-temperature soft-score pessimism.

## Falsification Condition

T350 fails if the soft score uses parent tail membership directly.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T350 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
