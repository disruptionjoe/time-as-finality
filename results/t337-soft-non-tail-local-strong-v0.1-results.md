# T337 Results: Soft Non Tail Local Strong

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 2^(band + interval3 + lowcover + min(T252 deletion pass count,6)).` |
| `total_weight` | `739641` |
| `tail_weight` | `5120` |
| `tail_probability` | `{'fraction': '5120/739641', 'float': 0.006922277158783788}` |
| `parentcap_probability` | `{'fraction': '7680/246547', 'float': 0.031150247214527048}` |
| `selected_probability` | `{'fraction': '512/739641', 'float': 0.0006922277158783788}` |
| `lift_vs_uniform` | `{'fraction': '8847360/35221', 'float': 251.1955935379461}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `True` |

- Verdict: `soft_non_tail_local_strong_tail_probability_recorded`

## Strongest Claim

The `soft_non_tail_local_strong` candidate assigns the 10-case tail probability 5120/739641.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T337 fails if the `soft_non_tail_local_strong` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T337 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
