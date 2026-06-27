# T305 Results: Low-Cover Bottleneck

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `low_cover_parent_count` | `185` |
| `parent_cap_count` | `66` |
| `tail_count` | `10` |

- Verdict: `low_cover_is_the_main_bottleneck_before_deletion`

## Strongest Claim

Low cover reduces the band-positive set to 185 cases; interval then reduces it to 66, and deletion to 10.

## What This Improved

T305 identifies the sequence of bottlenecks in the finite target.

## What This Weakened Or Falsified

It weakens stories centered only on ordering fraction or interval size.

## Falsification Condition

T305 fails if the bottleneck counts use different parent filters.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T305 alone.

## Open Blocker

The bottleneck still needs a non-ad hoc source.

## Suggested Next

Compare local T255 behavior against the global bottleneck.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
