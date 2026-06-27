# T258 Results: T255 Positive Neighbor Shape Catalog

## Aggregate Checks

- Positive neighbors: 21
- Ordering-fraction distribution: `[{'value': {'fraction': '17/36', 'float': 0.4722222222222222}, 'count': 4}, {'value': {'fraction': '19/36', 'float': 0.5277777777777778}, 'count': 4}, {'value': {'fraction': '5/12', 'float': 0.4166666666666667}, 'count': 4}, {'value': {'fraction': '7/12', 'float': 0.5833333333333334}, 'count': 9}]`
- Width distribution: `[{'value': 2, 'count': 4}, {'value': 3, 'count': 13}, {'value': 4, 'count': 4}]`
- Cover-count distribution: `[{'value': 10, 'count': 1}, {'value': 11, 'count': 2}, {'value': 12, 'count': 3}, {'value': 8, 'count': 13}, {'value': 9, 'count': 2}]`
- Largest-interval distribution: `[{'value': 3, 'count': 13}, {'value': 4, 'count': 4}, {'value': 5, 'count': 1}, {'value': 6, 'count': 2}, {'value': 7, 'count': 1}]`
- Verdict: `positive_mutation_neighbors_keep_band_but_shape_varies`

## Strongest Claim

The 21 mutation-positive neighbors are not all copies of T252: they span multiple ordering fractions, widths, cover counts, and largest interval sizes.

## What This Improved

T258 turns the T255 positive count into a structural catalog rather than a bare tally.

## What This Weakened Or Falsified

This weakens the idea that one rigid shape explains every nearby positive case; the local positive region is heterogeneous.

## Falsification Condition

T258 fails if the positives are not exactly T255 one-transposition neighbors that pass both T126 and the T156 band.

## S1 Update

S1 remains guarded; local positive heterogeneity is not typicality.

## Claim Ledger Update

Do not update the claim ledger from T258 alone. Safe wording: 21 one-transposition neighbors pass the finite screens, with varied finite shape summaries.

## Open Blocker

The positive-neighbor catalog has not been converted into an exact global abundance count or a generative law.

## Suggested Next

Compare positive neighbors against the inside-band cases that fail T126 to identify the active obstruction.

## Not Claimed

These diagnostics do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, or settle S1.
