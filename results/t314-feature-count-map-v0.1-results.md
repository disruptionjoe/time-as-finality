# T314 Results: Feature Count Map

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `feature_counts` | `[{'value': 'band', 'count': 143435}, {'value': 'interval3', 'count': 91350}, {'value': 'lowcover', 'count': 185}, {'value': 'parentcap', 'count': 66}, {'value': 'relaxed_interval3_stable', 'count': 9176}, {'value': 't253_stable', 'count': 8339}, {'value': 'tail', 'count': 10}, {'value': 'total', 'count': 362880}]` |

- Verdict: `feature_count_map_recorded`

## Strongest Claim

The core finite features are recorded for the exact n=9 ensemble.

## What This Improved

T314 exposes the bottlenecks before measure weighting.

## What This Weakened Or Falsified

It weakens qualitative discussion detached from exact feature counts.

## Falsification Condition

T314 fails if feature names are reused with different definitions.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T314 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
