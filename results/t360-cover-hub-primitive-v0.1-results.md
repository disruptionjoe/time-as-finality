# T360 Results: Cover Hub Primitive

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `lowcover_tail_probability` | `{'fraction': '2/37', 'float': 0.05405405405405406}` |
| `cover_deletion_tail_probability` | `{'fraction': '5/8', 'float': 0.625}` |

- Verdict: `cover_hub_needs_deletion_stability`

## Strongest Claim

Low cover alone gives probability 2/37, but low cover plus deletion-band stability gives 5/8.

## What This Improved

T360 identifies deletion stability as the multiplier on cover sparsity.

## What This Weakened Or Falsified

It weakens cover-only accounts.

## Falsification Condition

T360 fails if the cover threshold differs from T257.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T360 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
