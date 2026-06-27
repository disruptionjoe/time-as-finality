# T346 Results: Soft Interval Inverse

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score giving an 8x bonus to interval<=3 inside the band.` |
| `total_weight` | `1002330` |
| `tail_weight` | `80` |
| `tail_probability` | `{'fraction': '8/100233', 'float': 7.98140333024054e-05}` |
| `parentcap_probability` | `{'fraction': '88/167055', 'float': 0.0005267726197958757}` |
| `selected_probability` | `{'fraction': '4/501165', 'float': 7.981403330240539e-06}` |
| `lift_vs_uniform` | `{'fraction': '4608/1591', 'float': 2.896291640477687}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `soft_interval_inverse_tail_probability_recorded`

## Strongest Claim

The `soft_interval_inverse` candidate assigns the 10-case tail probability 8/100233.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T346 fails if the `soft_interval_inverse` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T346 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
