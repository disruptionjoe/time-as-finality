# T325 Results: Hard Parentcap

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Hard gate: T252-style parent interval+cover cap.` |
| `total_weight` | `66` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '5/33', 'float': 0.15151515151515152}` |
| `parentcap_probability` | `{'fraction': '1/1', 'float': 1.0}` |
| `selected_probability` | `{'fraction': '1/66', 'float': 0.015151515151515152}` |
| `lift_vs_uniform` | `{'fraction': '60480/11', 'float': 5498.181818181818}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `False` |

- Verdict: `hard_parentcap_tail_probability_recorded`

## Strongest Claim

The `hard_parentcap` candidate assigns the 10-case tail probability 5/33.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T325 fails if the `hard_parentcap` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T325 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
