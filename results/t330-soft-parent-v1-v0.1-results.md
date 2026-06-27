# T330 Results: Soft Parent V1

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 2^(band + interval3 + lowcover).` |
| `total_weight` | `689517` |
| `tail_weight` | `80` |
| `tail_probability` | `{'fraction': '80/689517', 'float': 0.00011602324525718728}` |
| `parentcap_probability` | `{'fraction': '176/229839', 'float': 0.0007657534186974361}` |
| `selected_probability` | `{'fraction': '8/689517', 'float': 1.1602324525718728e-05}` |
| `lift_vs_uniform` | `{'fraction': '322560/76613', 'float': 4.210251523892812}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `soft_parent_v1_tail_probability_recorded`

## Strongest Claim

The `soft_parent_v1` candidate assigns the 10-case tail probability 80/689517.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T330 fails if the `soft_parent_v1` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T330 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
