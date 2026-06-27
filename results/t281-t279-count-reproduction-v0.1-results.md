# T281 Results: T279 Count Reproduction

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t126_band_count` | `143435` |
| `t253_deletion_band_stable_count` | `8339` |
| `t252_parent_cap_count` | `66` |
| `t252_style_tail_count` | `10` |

- Verdict: `selection_audit_reproduces_t279_tail_counts`

## Strongest Claim

The selection audit reproduces the T279 spine: 143435 band positives, 8339 T253-style stable cases, 66 T252-style parents, and 10 T252-style stable cases.

## What This Improved

This validates that the measure audit is using the same exact n=9 denominator.

## What This Weakened Or Falsified

It weakens concern that selection results come from a shifted target.

## Falsification Condition

T281 fails if any count disagrees with T264-T279 under the same gates.

## S1 Update

S1 is unchanged; this is a regression guard.

## Claim Ledger Update

Do not update the claim ledger from T281 alone.

## Open Blocker

Matching prior counts still does not define a physical measure.

## Suggested Next

Use the reproduced counts as the baseline for measure lift.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
