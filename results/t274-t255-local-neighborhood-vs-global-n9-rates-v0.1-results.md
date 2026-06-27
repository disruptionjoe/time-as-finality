# T274 Results: T255 Local Neighborhood Vs Global n=9 Rates

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t255_t126_band_neighbor_rate` | `{'fraction': '7/12', 'float': 0.5833333333333334}` |
| `global_t126_band_rate` | `{'fraction': '28687/72576', 'float': 0.39526840828924165}` |
| `t255_t252_style_neighbor_count` | `0` |
| `global_t252_parent_cap_count` | `66` |
| `global_t252_deletion_stable_count` | `10` |
| `global_t252_parent_rate` | `{'fraction': '11/60480', 'float': 0.00018187830687830687}` |
| `global_t252_deletion_stable_rate` | `{'fraction': '1/36288', 'float': 2.755731922398589e-05}` |

- Verdict: `t255_neighborhood_enriched_for_band_but_not_t252_style_cap`

## Strongest Claim

The T255 one-swap neighborhood is enriched for T126+band passes, but none of the 36 neighbors match the stricter T252-style cap.

## What This Improved

This explains the mixed T255 result: local band positives do not preserve the full T252 interval/cover shape.

## What This Weakened Or Falsified

It weakens the idea that one-swap abundance is enough to support the selected witness.

## Falsification Condition

T274 fails if the local T255 rates are compared against a different n=9 ensemble.

## S1 Update

S1 is unchanged; local enrichment is not a global measure.

## Claim Ledger Update

Do not update the claim ledger from T274 alone.

## Open Blocker

The selected shape is locally fragile under one-swap mutations.

## Suggested Next

Use shape distributions to see what the broader band-positive set looks like.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
