# T347 Results: Soft Anti Parent

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Control score favoring band cases that fail interval and cover caps.` |
| `total_weight` | `1659252` |
| `tail_weight` | `20` |
| `tail_probability` | `{'fraction': '5/414813', 'float': 1.2053624163177143e-05}` |
| `parentcap_probability` | `{'fraction': '11/138271', 'float': 7.955391947696913e-05}` |
| `selected_probability` | `{'fraction': '1/829626', 'float': 1.2053624163177142e-06}` |
| `lift_vs_uniform` | `{'fraction': '8640/19753', 'float': 0.43740191363337216}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `soft_anti_parent_tail_probability_recorded`

## Strongest Claim

The `soft_anti_parent` candidate assigns the 10-case tail probability 5/414813.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T347 fails if the `soft_anti_parent` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T347 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
