# T342 Results: Soft Interval Cover S Count

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 2^(T252 deletion pass count) with an interval+cover multiplier.` |
| `total_weight` | `417265` |
| `tail_weight` | `20480` |
| `tail_probability` | `{'fraction': '4096/83453', 'float': 0.04908151893880388}` |
| `parentcap_probability` | `{'fraction': '46848/417265', 'float': 0.11227397457251387}` |
| `selected_probability` | `{'fraction': '2048/417265', 'float': 0.004908151893880388}` |
| `lift_vs_uniform` | `{'fraction': '148635648/83453', 'float': 1781.070159251315}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `True` |

- Verdict: `soft_interval_cover_s_count_tail_probability_recorded`

## Strongest Claim

The `soft_interval_cover_s_count` candidate assigns the 10-case tail probability 4096/83453.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T342 fails if the `soft_interval_cover_s_count` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T342 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
