# T331 Results: Soft Parent V2

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 3^(band + interval3 + lowcover).` |
| `total_weight` | `1199752` |
| `tail_weight` | `270` |
| `tail_probability` | `{'fraction': '135/599876', 'float': 0.00022504650961198647}` |
| `parentcap_probability` | `{'fraction': '891/599876', 'float': 0.0014853069634391106}` |
| `selected_probability` | `{'fraction': '27/1199752', 'float': 2.2504650961198648e-05}` |
| `lift_vs_uniform` | `{'fraction': '1224720/149969', 'float': 8.166487740799765}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `soft_parent_v2_tail_probability_recorded`

## Strongest Claim

The `soft_parent_v2` candidate assigns the 10-case tail probability 135/599876.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T331 fails if the `soft_parent_v2` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T331 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
