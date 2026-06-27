# T294 Results: Cover Plus Deletion Pair

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `cover_and_t253_count` | `16` |
| `target_tail_count` | `10` |

- Verdict: `cover_deletion_pair_nearly_isolates_tail`

## Strongest Claim

Low-cover plus T253 deletion-band stability leaves 16 cases, much closer to the 10-case tail.

## What This Improved

T294 identifies cover+deletion as the strongest non-parent pair.

## What This Weakened Or Falsified

It weakens interval-first narratives: cover plus deletion does most of the work.

## Falsification Condition

T294 fails if cover and deletion are not evaluated on the same parent/deletion relations.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T294 alone.

## Open Blocker

Six false positives remain without the interval cap.

## Suggested Next

Use the full interval+cover+deletion gate as the target boundary.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
