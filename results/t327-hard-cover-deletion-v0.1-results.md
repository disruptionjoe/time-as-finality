# T327 Results: Hard Cover Deletion

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Hard gate: low cover and deletion-band stability.` |
| `total_weight` | `16` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '5/8', 'float': 0.625}` |
| `parentcap_probability` | `{'fraction': '5/8', 'float': 0.625}` |
| `selected_probability` | `{'fraction': '1/16', 'float': 0.0625}` |
| `lift_vs_uniform` | `{'fraction': '22680/1', 'float': 22680.0}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `hard_cover_deletion_tail_probability_recorded`

## Strongest Claim

The `hard_cover_deletion` candidate assigns the 10-case tail probability 5/8.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T327 fails if the `hard_cover_deletion` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T327 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
