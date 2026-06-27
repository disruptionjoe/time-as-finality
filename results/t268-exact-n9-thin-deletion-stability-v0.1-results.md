# T268 Results: Exact n=9 Thin Deletion Stability

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `thin_parent_count` | `7813` |
| `thin_deletion_stable_count` | `1583` |
| `thin_stable_fraction` | `{'fraction': '1583/362880', 'float': 0.0043623236331569665}` |
| `thin_stable_strict_pair_distribution` | `[{'value': 16, 'count': 26}, {'value': 17, 'count': 718}, {'value': 18, 'count': 601}, {'value': 19, 'count': 220}, {'value': 20, 'count': 18}]` |

- Verdict: `n9_t159_thin_stable_survivor_count_complete`

## Strongest Claim

At n=9, the T159/T223 thin deletion-stable tail has 1583 labeled survivors.

## What This Improved

This gives the exact next-size count that T223 deliberately left as follow-on work.

## What This Weakened Or Falsified

It weakens any hope that the thin tail becomes common at n=9; the count rises but the fraction continues to fall.

## Falsification Condition

T268 fails if deletion suborders are not rank-normalized restrictions of the parent permutation.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T268 alone; combine with the trajectory result.

## Open Blocker

Thin deletion stability still gives a rare finite tail, not spacetime evidence.

## Suggested Next

Compare the n=9 stable fraction to n=6..8.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
