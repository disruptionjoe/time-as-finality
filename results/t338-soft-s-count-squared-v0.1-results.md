# T338 Results: Soft S Count Squared

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 4^(number of deletion T252-style passes).` |
| `total_weight` | `4627863` |
| `tail_weight` | `2621440` |
| `tail_probability` | `{'fraction': '2621440/4627863', 'float': 0.5664471917167816}` |
| `parentcap_probability` | `{'fraction': '1356800/1542621', 'float': 0.8795420262008621}` |
| `selected_probability` | `{'fraction': '262144/4627863', 'float': 0.05664471917167816}` |
| `lift_vs_uniform` | `{'fraction': '10569646080/514207', 'float': 20555.23569301857}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `True` |

- Verdict: `soft_s_count_squared_tail_probability_recorded`

## Strongest Claim

The `soft_s_count_squared` candidate assigns the 10-case tail probability 2621440/4627863.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T338 fails if the `soft_s_count_squared` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T338 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
