# T303 Results: Tail Representative List

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t252_tail_permutations` | `[[1, 6, 7, 8, 9, 2, 3, 4, 5], [4, 6, 7, 8, 1, 9, 2, 3, 5], [4, 6, 7, 8, 9, 1, 2, 3, 5], [5, 6, 7, 8, 1, 2, 3, 4, 9], [5, 6, 7, 8, 1, 9, 2, 3, 4], [5, 6, 7, 8, 9, 1, 2, 3, 4], [5, 7, 8, 1, 9, 2, 3, 4, 6], [5, 7, 8, 9, 1, 2, 3, 4, 6], [6, 7, 8, 1, 9, 2, 3, 4, 5], [6, 7, 8, 9, 1, 2, 3, 4, 5]]` |
| `selected_t252_rank_permutation` | `[1, 6, 7, 8, 9, 2, 3, 4, 5]` |

- Verdict: `tail_representatives_recorded`

## Strongest Claim

All 10 T252-style stable permutations are recorded for future selection-measure work.

## What This Improved

T303 makes the target tail inspectable rather than just counted.

## What This Weakened Or Falsified

It weakens ambiguity about which cases a later measure must support.

## Falsification Condition

T303 fails if the representative list length differs from 10.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T303 alone.

## Open Blocker

A list of finite representatives is not a measure.

## Suggested Next

Analyze false positives at the parent cap.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
