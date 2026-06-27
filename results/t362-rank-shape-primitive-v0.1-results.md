# T362 Results: Rank Shape Primitive

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `rank_shape_tail_probability` | `{'fraction': '640/987721', 'float': 0.0006479562548533443}` |
| `exact_parent_shape_tail_probability` | `{'fraction': '320/766449', 'float': 0.00041750984083742035}` |

- Verdict: `rank_shape_soft_scores_do_not_concentrate_tail`

## Strongest Claim

T252-like rank and parent-shape bonuses enrich the tail only weakly.

## What This Improved

T362 keeps shape-label scores from being overread.

## What This Weakened Or Falsified

It weakens parent-shape-only soft actions.

## Falsification Condition

T362 fails if shape scores include tail membership.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T362 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
