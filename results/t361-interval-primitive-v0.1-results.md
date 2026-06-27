# T361 Results: Interval Primitive

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `interval3_tail_probability` | `{'fraction': '1/9135', 'float': 0.00010946907498631637}` |
| `interval_deletion_tail_probability` | `{'fraction': '10/7901', 'float': 0.0012656625743576763}` |

- Verdict: `interval_primitive_is_weak_without_cover`

## Strongest Claim

Interval<=3 is weak alone and remains broad even with deletion-band stability.

## What This Improved

T361 demotes interval depth as the primary selection driver.

## What This Weakened Or Falsified

It weakens interval-first interpretations.

## Falsification Condition

T361 fails if interval<=3 is evaluated before the band gate.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T361 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
