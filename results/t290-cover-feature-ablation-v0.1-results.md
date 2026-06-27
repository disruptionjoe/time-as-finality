# T290 Results: Cover Feature Ablation

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `low_cover_parent_count` | `185` |
| `tail_count_inside_low_cover` | `10` |
| `tail_probability_after_low_cover` | `{'fraction': '2/37', 'float': 0.05405405405405406}` |

- Verdict: `cover_feature_is_strong_but_not_sufficient`

## Strongest Claim

The low-cover parent feature leaves 185 cases and is the strongest single hard gate, but it still contains many non-tail cases.

## What This Improved

T290 identifies cover sparsity as the main non-tautological selection signal.

## What This Weakened Or Falsified

It weakens pure ordering-fraction or interval-only routes.

## Falsification Condition

T290 fails if the cover threshold differs from T257's cap.

## S1 Update

S1 is unchanged; cover sparsity is not a physical law.

## Claim Ledger Update

Do not update the claim ledger from T290 alone.

## Open Blocker

Cover sparsity needs a reason, not just a threshold.

## Suggested Next

Combine cover with interval and deletion gates.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
