# T318 Results: Tail Symmetry Check

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `tail_symmetry_counts` | `[{'value': 'reverse', 'count': 0}, {'value': 'complement', 'count': 0}, {'value': 'reverse_complement', 'count': 10}, {'value': 'inverse', 'count': 10}]` |

- Verdict: `tail_symmetry_reproduced`

## Strongest Claim

The tail remains closed under inverse and reverse-complement transforms, not under reverse or complement alone.

## What This Improved

T318 confirms the structural symmetry result from T301.

## What This Weakened Or Falsified

It weakens accidental-list readings of the target tail.

## Falsification Condition

T318 fails if transform definitions change after seeing the tail.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T318 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
