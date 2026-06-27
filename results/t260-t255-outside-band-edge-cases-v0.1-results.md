# T260 Results: T255 Outside-Band Edge Cases

## Aggregate Checks

- Outside-band neighbors: 2
- Outside-band swaps: `[[0, 4], [0, 8]]`
- Ordering-fraction distribution: `[{'value': {'fraction': '13/36', 'float': 0.3611111111111111}, 'count': 2}]`
- Cover-count distribution: `[{'value': 6, 'count': 2}]`
- Verdict: `outside_band_neighbors_are_two_low_fraction_edge_cases`

## Strongest Claim

Only two T255 neighbors pass T126 while missing the declared ordering band, and both miss low at ordering fraction 13/36.

## What This Improved

T260 records the small outside-band tail so that the positive count is not mistaken for all T126-passing mutations.

## What This Weakened Or Falsified

This weakens a uniform-neighborhood reading: even T126-passing one-transposition neighbors can fall below the target band.

## Falsification Condition

T260 fails if outside-band status is computed from a different target band, or if swaps outside the T255 transposition list are included.

## S1 Update

S1 remains guarded; two low-fraction edge cases are controls only.

## Claim Ledger Update

Do not update the claim ledger from T260 alone. Safe wording: two T126-passing T255 neighbors fall below the declared ordering band.

## Open Blocker

No principle currently explains the boundary between low-fraction T126 passes and in-band positives.

## Suggested Next

Use exact counting or a stricter local shape gate before adding more selected examples.

## Not Claimed

These diagnostics do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, or settle S1.
