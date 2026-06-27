# T322 Results: Hard Interval3

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Hard gate: T126+band and parent largest interval <= 3.` |
| `total_weight` | `91350` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '1/9135', 'float': 0.00010946907498631637}` |
| `parentcap_probability` | `{'fraction': '11/15225', 'float': 0.000722495894909688}` |
| `selected_probability` | `{'fraction': '1/91350', 'float': 1.0946907498631636e-05}` |
| `lift_vs_uniform` | `{'fraction': '576/145', 'float': 3.972413793103448}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `hard_interval3_tail_probability_recorded`

## Strongest Claim

The `hard_interval3` candidate assigns the 10-case tail probability 1/9135.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T322 fails if the `hard_interval3` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T322 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
