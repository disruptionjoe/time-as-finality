# T329 Results: Hard Tail

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Hard gate: condition directly on the T252-style tail.` |
| `total_weight` | `10` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '1/1', 'float': 1.0}` |
| `parentcap_probability` | `{'fraction': '1/1', 'float': 1.0}` |
| `selected_probability` | `{'fraction': '1/10', 'float': 0.1}` |
| `lift_vs_uniform` | `{'fraction': '36288/1', 'float': 36288.0}` |
| `uses_tail_label` | `True` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `tail_label_conditioning_recorded_as_tautology`

## Strongest Claim

The `hard_tail` candidate assigns the 10-case tail probability 1.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T329 fails if the `hard_tail` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T329 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
