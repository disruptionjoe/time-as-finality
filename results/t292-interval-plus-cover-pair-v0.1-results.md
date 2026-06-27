# T292 Results: Interval Plus Cover Pair

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `interval_and_cover_count` | `66` |
| `tail_probability_after_interval_cover` | `{'fraction': '5/33', 'float': 0.15151515151515152}` |

- Verdict: `interval_cover_pair_is_the_best_parent_gate`

## Strongest Claim

The interval<=3 plus low-cover pair is exactly the 66-case T252 parent cap.

## What This Improved

T292 shows that T252's parent rarity is a two-feature effect.

## What This Weakened Or Falsified

It weakens any single-feature account of the selected witness.

## Falsification Condition

T292 fails if the pair count differs from the T271 parent cap.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T292 alone.

## Open Blocker

The parent gate still has 56 false positives before deletion stability.

## Suggested Next

Apply deletion stability to the parent gate.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
