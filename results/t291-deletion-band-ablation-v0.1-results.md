# T291 Results: Deletion-Band Ablation

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t253_deletion_band_stable_count` | `8339` |
| `tail_probability_after_t253` | `{'fraction': '10/8339', 'float': 0.001199184554502938}` |

- Verdict: `deletion_band_stability_is_broad`

## Strongest Claim

T253-style deletion-band stability leaves 8339 cases, so deletion-band stability alone does not recover the T252-style shape.

## What This Improved

T291 locates T253 as a robustness filter, not a locality selector.

## What This Weakened Or Falsified

It weakens deletion-stability-only optimism.

## Falsification Condition

T291 fails if deletion suborders are not rank-normalized restrictions.

## S1 Update

S1 remains guarded.

## Claim Ledger Update

Do not update the claim ledger from T291 alone.

## Open Blocker

Deletion-band stability needs shape constraints to become selective.

## Suggested Next

Add interval and cover features.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
