# T275 Results: n=9 Band-Positive Shape Distributions

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t156_height_distribution` | `[{'value': 3, 'count': 32499}, {'value': 4, 'count': 86133}, {'value': 5, 'count': 23374}, {'value': 6, 'count': 1426}, {'value': 7, 'count': 3}]` |
| `t156_width_distribution` | `[{'value': 2, 'count': 126}, {'value': 3, 'count': 21217}, {'value': 4, 'count': 88535}, {'value': 5, 'count': 32653}, {'value': 6, 'count': 904}]` |
| `t156_largest_interval_distribution` | `[{'value': 1, 'count': 7813}, {'value': 2, 'count': 35404}, {'value': 3, 'count': 48133}, {'value': 4, 'count': 34339}, {'value': 5, 'count': 13921}, {'value': 6, 'count': 3392}, {'value': 7, 'count': 433}]` |
| `t156_cover_count_distribution` | `[{'value': 5, 'count': 4}, {'value': 6, 'count': 300}, {'value': 7, 'count': 2574}, {'value': 8, 'count': 10498}, {'value': 9, 'count': 21558}, {'value': 10, 'count': 31892}, {'value': 11, 'count': 31830}, {'value': 12, 'count': 23649}, {'value': 13, 'count': 12890}, {'value': 14, 'count': 5629}, {'value': 15, 'count': 1860}, {'value': 16, 'count': 547}, {'value': 17, 'count': 180}, {'value': 18, 'count': 24}]` |
| `t156_cover_hub_distribution` | `[{'value': {'fraction': '1/4', 'float': 0.25}, 'count': 185}, {'value': {'fraction': '3/8', 'float': 0.375}, 'count': 31580}, {'value': {'fraction': '1/2', 'float': 0.5}, 'count': 83441}, {'value': {'fraction': '5/8', 'float': 0.625}, 'count': 28229}]` |
| `t156_rank_profile_top` | `[{'value': [3, 3, 2, 1], 'count': 11824}, {'value': [2, 3, 3, 1], 'count': 7395}, {'value': [3, 2, 3, 1], 'count': 7030}, {'value': [4, 2, 2, 1], 'count': 6673}, {'value': [2, 4, 2, 1], 'count': 6390}, {'value': [3, 3, 3], 'count': 5791}, {'value': [4, 3, 2], 'count': 5422}, {'value': [3, 4, 2], 'count': 5300}, {'value': [2, 3, 2, 2], 'count': 4600}, {'value': [3, 2, 2, 2], 'count': 4545}]` |

- Verdict: `n9_band_positive_shapes_are_broad`

## Strongest Claim

The 143435 band-positive n=9 cases span broad height, width, interval, cover-count, and cover-hub profiles.

## What This Improved

This turns the band-positive set into a structural distribution rather than a single count.

## What This Weakened Or Falsified

It weakens ordering-fraction-only interpretations: equal band status hides very different finite shapes.

## Falsification Condition

T275 fails if shape labels are computed before applying the T126+T156 filters.

## S1 Update

S1 is unchanged; distributions are finite audit data.

## Claim Ledger Update

Do not update the claim ledger from T275 alone.

## Open Blocker

The broad distribution still needs a principled selection rule.

## Suggested Next

Separate deletion-stable band cases from the broad parent band.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
