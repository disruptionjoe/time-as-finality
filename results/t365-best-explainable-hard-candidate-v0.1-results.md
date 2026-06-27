# T365 Results: Best Explainable Hard Candidate

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `candidate` | `{'name': 'hard_cover_deletion', 'description': 'Hard gate: low cover and deletion-band stability.', 'total_weight': 16, 'tail_weight': 10, 'parentcap_weight': 10, 'selected_weight': 1, 'tail_probability': {'fraction': '5/8', 'float': 0.625}, 'parentcap_probability': {'fraction': '5/8', 'float': 0.625}, 'selected_probability': {'fraction': '1/16', 'float': 0.0625}, 'lift_vs_uniform': {'fraction': '22680/1', 'float': 22680.0}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': False}` |

- Verdict: `cover_deletion_is_best_simple_hard_candidate`

## Strongest Claim

The best simple hard candidate is low-cover plus deletion-band stability.

## What This Improved

T365 separates an interpretable gate from high-temperature soft tuning.

## What This Weakened Or Falsified

It weakens purely temperature-based optimism.

## Falsification Condition

T365 fails if target-equivalent gates are allowed to win.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T365 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
