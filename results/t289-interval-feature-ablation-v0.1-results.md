# T289 Results: Interval Feature Ablation

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `interval3_parent_count` | `91350` |
| `tail_count_inside_interval3` | `10` |
| `tail_probability_after_interval3` | `{'fraction': '1/9135', 'float': 0.00010946907498631637}` |

- Verdict: `interval_feature_alone_is_too_permissive`

## Strongest Claim

The interval<=3 parent feature admits 91350 cases, so it cannot explain the 10-case tail by itself.

## What This Improved

T289 separates T252's interval behavior from its cover and deletion behavior.

## What This Weakened Or Falsified

It weakens interval-only selection stories.

## Falsification Condition

T289 fails if interval<=3 is not evaluated after T126+T156.

## S1 Update

S1 is unchanged; interval caps are finite screens.

## Claim Ledger Update

Do not update the claim ledger from T289 alone.

## Open Blocker

Interval caps alone are far from a natural measure.

## Suggested Next

Pair interval caps with cover and deletion features.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
