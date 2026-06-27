# T264 Results: Optimized Ordinal Counter Validation

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `n6_t126_t156_stable` | `[578, 305, 26]` |
| `n7_t126_t156_stable` | `[4456, 2051, 174]` |
| `n8_t126_t156_stable` | `[34044, 16261, 361]` |
| `reproduces_t223_counts` | `True` |

- Verdict: `optimized_counter_reproduces_t223_n6_to_n8_counts`

## Strongest Claim

The optimized relation-level ordinal counter reproduces the published T223 n=6, n=7, and n=8 counts.

## What This Improved

This makes the n=9 count feasible without rerunning T54 completion for every permutation.

## What This Weakened Or Falsified

It weakens concern that the n=9 sweep is a new, incompatible pipeline.

## Falsification Condition

T264 fails if any reproduced T223 count differs from the published values.

## S1 Update

S1 is unchanged; this is validation of a finite counting implementation.

## Claim Ledger Update

Do not update the claim ledger from T264 alone.

## Open Blocker

The validation says the counter matches prior finite counts; it does not pick a physical measure.

## Suggested Next

Use the optimized counter for the exact n=9 sweep.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
