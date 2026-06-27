# T315 Results: Intersection Count Map

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `intersection_counts` | `[{'value': 'cover_deletion', 'count': 16}, {'value': 'interval_cover', 'count': 66}, {'value': 'interval_cover_deletion', 'count': 10}, {'value': 'interval_deletion', 'count': 7901}]` |

- Verdict: `intersection_count_map_recorded`

## Strongest Claim

The key intersections show that low-cover plus deletion-band stability leaves 16 cases, while interval+cover+deletion leaves exactly 10.

## What This Improved

T315 identifies which feature combinations are doing the selection work.

## What This Weakened Or Falsified

It weakens single-feature explanations.

## Falsification Condition

T315 fails if intersections are not computed from the same case flags.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T315 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
