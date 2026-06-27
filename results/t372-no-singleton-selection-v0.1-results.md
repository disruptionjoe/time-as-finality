# T372 Results: No Singleton Selection

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `selected_under_best_soft` | `{'fraction': '134217728/1705336003', 'float': 0.07870456482704072}` |
| `selected_under_best_hard` | `{'fraction': '1/16', 'float': 0.0625}` |

- Verdict: `best_measures_select_tail_not_singleton`

## Strongest Claim

The best measures select the tail, not the single chosen T252 permutation.

## What This Improved

T372 keeps singleton claims out of the result.

## What This Weakened Or Falsified

It weakens hand-picked-witness interpretations.

## Falsification Condition

T372 fails if singleton selection is inferred from tail concentration.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T372 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
