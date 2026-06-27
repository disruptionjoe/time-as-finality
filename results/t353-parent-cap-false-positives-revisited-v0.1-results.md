# T353 Results: Parent Cap False Positives Revisited

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `parentcap_count` | `66` |
| `tail_inside_parentcap` | `10` |
| `false_positive_count` | `56` |

- Verdict: `parentcap_false_positive_burden_stays_large`

## Strongest Claim

The parent cap still has 56 false positives before deletion stability.

## What This Improved

T353 confirms that parent shape alone is not the measure.

## What This Weakened Or Falsified

It weakens parentcap-only selection proposals.

## Falsification Condition

T353 fails if it omits the deletion-stability requirement.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T353 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
