# T332 Results: Soft Deletion Binary

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 2^(band + interval3 + lowcover + t253 + relaxed deletion interval3).` |
| `total_weight` | `790437` |
| `tail_weight` | `320` |
| `tail_probability` | `{'fraction': '320/790437', 'float': 0.0004048393483604639}` |
| `parentcap_probability` | `{'fraction': '256/263479', 'float': 0.0009716144360651134}` |
| `selected_probability` | `{'fraction': '32/790437', 'float': 4.048393483604639e-05}` |
| `lift_vs_uniform` | `{'fraction': '3870720/263479', 'float': 14.690810273304514}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `soft_deletion_binary_tail_probability_recorded`

## Strongest Claim

The `soft_deletion_binary` candidate assigns the 10-case tail probability 320/790437.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T332 fails if the `soft_deletion_binary` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T332 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
