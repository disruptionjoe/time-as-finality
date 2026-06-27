# T316 Results: Deletion T252-Pass Distribution

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `deletion_t252_pass_distribution` | `[{'value': 0, 'count': 140470}, {'value': 1, 'count': 2171}, {'value': 2, 'count': 588}, {'value': 3, 'count': 68}, {'value': 4, 'count': 40}, {'value': 5, 'count': 24}, {'value': 6, 'count': 36}, {'value': 7, 'count': 8}, {'value': 8, 'count': 20}, {'value': 9, 'count': 10}]` |
| `parentcap_deletion_t252_pass_distribution` | `[{'value': 4, 'count': 28}, {'value': 7, 'count': 8}, {'value': 8, 'count': 20}, {'value': 9, 'count': 10}]` |

- Verdict: `deletion_t252_pass_distribution_recorded`

## Strongest Claim

Among band-positive cases, the number of deletion T252-style passes is highly concentrated near zero, while parent-cap cases split across 4, 7, 8, and 9 passes.

## What This Improved

T316 motivates deletion-count soft actions.

## What This Weakened Or Falsified

It weakens parent-cap-only explanations.

## Falsification Condition

T316 fails if deletion counts are not rank-normalized suborders.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T316 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
