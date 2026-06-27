# T343 Results: Soft Rank Shape

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score for T252-like parent shape labels.` |
| `total_weight` | `987721` |
| `tail_weight` | `640` |
| `tail_probability` | `{'fraction': '640/987721', 'float': 0.0006479562548533443}` |
| `parentcap_probability` | `{'fraction': '2208/987721', 'float': 0.0022354490792440376}` |
| `selected_probability` | `{'fraction': '128/987721', 'float': 0.00012959125097066883}` |
| `lift_vs_uniform` | `{'fraction': '3317760/141103', 'float': 23.513036576118154}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `soft_rank_shape_tail_probability_recorded`

## Strongest Claim

The `soft_rank_shape` candidate assigns the 10-case tail probability 640/987721.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T343 fails if the `soft_rank_shape` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T343 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
