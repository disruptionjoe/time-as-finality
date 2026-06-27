# T341 Results: Soft Cover S Count

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 2^(T252 deletion pass count) with a low-cover multiplier.` |
| `total_weight` | `426940` |
| `tail_weight` | `20480` |
| `tail_probability` | `{'fraction': '1024/21347', 'float': 0.047969269686607016}` |
| `parentcap_probability` | `{'fraction': '11712/106735', 'float': 0.10972970440811355}` |
| `selected_probability` | `{'fraction': '512/106735', 'float': 0.004796926968660702}` |
| `lift_vs_uniform` | `{'fraction': '37158912/21347', 'float': 1740.7088583875955}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `True` |

- Verdict: `soft_cover_s_count_tail_probability_recorded`

## Strongest Claim

The `soft_cover_s_count` candidate assigns the 10-case tail probability 1024/21347.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T341 fails if the `soft_cover_s_count` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T341 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
