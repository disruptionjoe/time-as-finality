# T335 Results: Soft S Count

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 2^(number of deletion T252-style passes).` |
| `total_weight` | `382129` |
| `tail_weight` | `5120` |
| `tail_probability` | `{'fraction': '5120/382129', 'float': 0.013398616697502676}` |
| `parentcap_probability` | `{'fraction': '11712/382129', 'float': 0.03064933569553737}` |
| `selected_probability` | `{'fraction': '512/382129', 'float': 0.0013398616697502675}` |
| `lift_vs_uniform` | `{'fraction': '185794560/382129', 'float': 486.2090027189771}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `True` |

- Verdict: `soft_s_count_tail_probability_recorded`

## Strongest Claim

The `soft_s_count` candidate assigns the 10-case tail probability 5120/382129.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T335 fails if the `soft_s_count` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T335 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
