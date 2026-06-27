# T336 Results: Soft Non Tail Local

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 2^(band + interval3 + lowcover + min(T252 deletion pass count,4)).` |
| `total_weight` | `716601` |
| `tail_weight` | `1280` |
| `tail_probability` | `{'fraction': '1280/716601', 'float': 0.0017862101783279677}` |
| `parentcap_probability` | `{'fraction': '2816/238867', 'float': 0.011788987176964588}` |
| `selected_probability` | `{'fraction': '128/716601', 'float': 0.00017862101783279677}` |
| `lift_vs_uniform` | `{'fraction': '15482880/238867', 'float': 64.81799495116529}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `True` |

- Verdict: `soft_non_tail_local_tail_probability_recorded`

## Strongest Claim

The `soft_non_tail_local` candidate assigns the 10-case tail probability 1280/716601.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T336 fails if the `soft_non_tail_local` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T336 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
