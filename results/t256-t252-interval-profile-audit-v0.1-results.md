# T256 Results: T252 Interval Profile Audit

## Aggregate Checks

- Parent largest interval size: 3
- Parent interval counts: `[{'size': 0, 'count': 8}, {'size': 1, 'count': 6}, {'size': 2, 'count': 4}, {'size': 3, 'count': 2}]`
- Deletion largest-interval distribution: `[{'value': 2, 'count': 1}, {'value': 3, 'count': 8}]`
- Verdict: `ordinal_interval_profiles_bounded_under_deletion`

## Strongest Claim

The T252 parent has largest finite interval size 3, and all nine single-event deletions keep largest intervals at size 2 or 3.

## What This Improved

T256 records interval shape rather than relying only on the ordering-fraction pass from T252/T253.

## What This Weakened Or Falsified

This weakens the concern that the selected witness hides a deep finite interval like the T249 grid's size-7 interval.

## Falsification Condition

T256 fails if interval counts are not computed from the same T252 strict relation, if deletion suborders are not restrictions, or if the bounded finite profile is promoted into a continuum locality claim.

## S1 Update

S1 remains guarded; bounded finite intervals are diagnostic only.

## Claim Ledger Update

Do not update the claim ledger from T256 alone. Safe wording: the selected T252 witness has small interval profiles under all single deletions.

## Open Blocker

No distributional abundance result or Lorentzian interval-volume comparison has been attached to these finite counts.

## Suggested Next

Pair interval profiles with cover/locality summaries and then ask whether the pattern is common across the n=9 search space.

## Not Claimed

These diagnostics do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, or settle S1.
