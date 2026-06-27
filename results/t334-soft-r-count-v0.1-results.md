# T334 Results: Soft R Count

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 2^(number of deletion interval<=3 passes).` |
| `total_weight` | `16995514` |
| `tail_weight` | `5120` |
| `tail_probability` | `{'fraction': '2560/8497757', 'float': 0.00030125596672157134}` |
| `parentcap_probability` | `{'fraction': '5856/8497757', 'float': 0.0006891230238755945}` |
| `selected_probability` | `{'fraction': '256/8497757', 'float': 3.0125596672157135e-05}` |
| `lift_vs_uniform` | `{'fraction': '92897280/8497757', 'float': 10.93197652039238}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `soft_r_count_tail_probability_recorded`

## Strongest Claim

The `soft_r_count` candidate assigns the 10-case tail probability 2560/8497757.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T334 fails if the `soft_r_count` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T334 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
