# T340 Results: Soft S Count Cubed

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 8^(number of deletion T252-style passes).` |
| `total_weight` | `1705336003` |
| `tail_weight` | `1342177280` |
| `tail_probability` | `{'fraction': '1342177280/1705336003', 'float': 0.7870456482704071}` |
| `parentcap_probability` | `{'fraction': '1694613504/1705336003', 'float': 0.9937123833771543}` |
| `selected_probability` | `{'fraction': '134217728/1705336003', 'float': 0.07870456482704072}` |
| `lift_vs_uniform` | `{'fraction': '6957847019520/243619429', 'float': 28560.312484436534}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `True` |

- Verdict: `soft_s_count_cubed_tail_probability_recorded`

## Strongest Claim

The `soft_s_count_cubed` candidate assigns the 10-case tail probability 1342177280/1705336003.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T340 fails if the `soft_s_count_cubed` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T340 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
