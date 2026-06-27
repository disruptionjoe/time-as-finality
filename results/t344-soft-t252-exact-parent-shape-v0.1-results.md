# T344 Results: Soft T252 Exact Parent Shape

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score for exact selected-parent shape labels.` |
| `total_weight` | `766449` |
| `tail_weight` | `320` |
| `tail_probability` | `{'fraction': '320/766449', 'float': 0.00041750984083742035}` |
| `parentcap_probability` | `{'fraction': '760/766449', 'float': 0.0009915858719888734}` |
| `selected_probability` | `{'fraction': '64/766449', 'float': 8.350196816748408e-05}` |
| `lift_vs_uniform` | `{'fraction': '430080/28387', 'float': 15.15059710430831}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `soft_t252_exact_parent_shape_tail_probability_recorded`

## Strongest Claim

The `soft_t252_exact_parent_shape` candidate assigns the 10-case tail probability 320/766449.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T344 fails if the `soft_t252_exact_parent_shape` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T344 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
