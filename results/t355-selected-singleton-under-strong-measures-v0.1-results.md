# T355 Results: Selected Singleton Under Strong Measures

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `selected_under_cover_deletion` | `{'fraction': '1/16', 'float': 0.0625}` |
| `selected_under_s_squared` | `{'fraction': '262144/4627863', 'float': 0.05664471917167816}` |
| `selected_under_s_cubed` | `{'fraction': '134217728/1705336003', 'float': 0.07870456482704072}` |

- Verdict: `selected_singleton_still_not_explained`

## Strongest Claim

Even strong tail measures do not uniquely select the original T252 permutation.

## What This Improved

T355 separates tail selection from singleton selection.

## What This Weakened Or Falsified

It weakens overreading of the specific selected witness.

## Falsification Condition

T355 fails if singleton probability is confused with tail probability.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T355 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
