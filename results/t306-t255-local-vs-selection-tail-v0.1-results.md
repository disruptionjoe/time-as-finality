# T306 Results: T255 Local Vs Selection Tail

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t255_t252_style_neighbor_count` | `0` |
| `global_t252_parent_cap_count` | `66` |
| `global_t252_style_tail_count` | `10` |

- Verdict: `t255_neighbors_do_not_preserve_t252_style_cap`

## Strongest Claim

None of the 36 one-swap T255 neighbors satisfy the T252-style parent cap, even though the global ensemble has 66 parent-cap cases.

## What This Improved

T306 explains why local mutation abundance did not become a selection measure.

## What This Weakened Or Falsified

It weakens local-neighborhood optimism.

## Falsification Condition

T306 fails if the T255 neighborhood is not the one-transposition neighborhood of T252.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T306 alone.

## Open Blocker

The target tail is locally fragile under one-swap moves.

## Suggested Next

Rank the hard and soft candidates.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
