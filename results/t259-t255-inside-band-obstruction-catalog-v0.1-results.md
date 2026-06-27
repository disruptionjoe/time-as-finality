# T259 Results: T255 Inside-Band Obstruction Catalog

## Aggregate Checks

- Blocked inside-band neighbors: 13
- Classification distribution: `[{'value': 'order_dimension_obstruction', 'count': 13}]`
- Profile-spread obstruction count: 13
- Rank-profile distribution: `[{'value': [1, 2, 2, 3, 1], 'count': 2}, {'value': [1, 2, 3, 2, 1], 'count': 4}, {'value': [1, 3, 2, 2, 1], 'count': 4}, {'value': [1, 3, 3, 2], 'count': 1}, {'value': [1, 4, 2, 1, 1], 'count': 2}]`
- Verdict: `inside_band_neighbors_blocked_by_profile_spread`

## Strongest Claim

All 13 inside-band neighbors blocked by T126 are classified as order-dimension obstructions, and all 13 trip the profile-spread diagnostic.

## What This Improved

T259 explains why the T156 band alone is too weak in the local neighborhood: it admits cases with unstable interval profiles.

## What This Weakened Or Falsified

This weakens any plan to use the Myrheim-Meyer ordering-fraction band by itself as the next S1-facing filter.

## Falsification Condition

T259 fails if any inside-band T255 blocked neighbor has a different T126 classification or lacks profile-spread obstruction.

## S1 Update

S1 remains guarded; the obstruction confirms the need for multiple finite screens.

## Claim Ledger Update

Do not update the claim ledger from T259 alone. Safe wording: in the T255 neighborhood, every inside-band T126 failure is a profile-spread/order-dimension obstruction.

## Open Blocker

The obstruction is diagnostic, not a theorem identifying the right continuum dimension or a selection measure.

## Suggested Next

Keep the T126 profile-spread gate active in any exact n=9 count.

## Not Claimed

These diagnostics do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, or settle S1.
