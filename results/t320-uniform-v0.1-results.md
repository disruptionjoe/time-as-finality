# T320 Results: Uniform

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Uniform ordinal ensemble over all 9! permutations.` |
| `total_weight` | `362880` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '1/36288', 'float': 2.755731922398589e-05}` |
| `parentcap_probability` | `{'fraction': '11/60480', 'float': 0.00018187830687830687}` |
| `selected_probability` | `{'fraction': '1/362880', 'float': 2.7557319223985893e-06}` |
| `lift_vs_uniform` | `{'fraction': '1/1', 'float': 1.0}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `uniform_tail_probability_recorded`

## Strongest Claim

The `uniform` candidate assigns the 10-case tail probability 1/36288.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T320 fails if the `uniform` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T320 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
