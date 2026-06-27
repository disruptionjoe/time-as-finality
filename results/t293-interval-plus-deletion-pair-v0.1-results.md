# T293 Results: Interval Plus Deletion Pair

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `interval_and_t253_count` | `7901` |
| `target_tail_count` | `10` |

- Verdict: `interval_deletion_pair_remains_broad`

## Strongest Claim

Interval<=3 plus T253 deletion-band stability leaves 7901 cases.

## What This Improved

T293 shows that deletion stability mostly tracks the interval-relaxed population, not the tiny T252 tail.

## What This Weakened Or Falsified

It weakens interval+deletion selection stories without cover sparsity.

## Falsification Condition

T293 fails if the pair uses the wrong deletion target.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T293 alone.

## Open Blocker

The cover feature is still required.

## Suggested Next

Compare cover+deletion next.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
