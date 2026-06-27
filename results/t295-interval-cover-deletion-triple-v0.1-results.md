# T295 Results: Interval Cover Deletion Triple

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `interval_cover_t253_count` | `10` |
| `t252_style_tail_count` | `10` |

- Verdict: `interval_cover_deletion_triple_matches_t252_tail`

## Strongest Claim

The interval+cover+deletion triple leaves exactly the 10 T252-style stable cases.

## What This Improved

T295 shows which finite ingredients isolate the selected tail.

## What This Weakened Or Falsified

It weakens broader finite-gate optimism: isolating the tail requires all three ingredients.

## Falsification Condition

T295 fails if the triple no longer equals the T272 tail.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T295 alone.

## Open Blocker

The triple is still a target definition, not a derived measure.

## Suggested Next

Test soft weights that use these features without hard-targeting the tail.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
