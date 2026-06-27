# T339 Results: Soft Parent S Squared

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `description` | `Soft score 4^(T252 deletion pass count) with a parent-cap multiplier.` |
| `total_weight` | `16839063` |
| `tail_weight` | `10485760` |
| `tail_probability` | `{'fraction': '10485760/16839063', 'float': 0.6227044818348859}` |
| `parentcap_probability` | `{'fraction': '5427200/5613021', 'float': 0.9668946544115905}` |
| `selected_probability` | `{'fraction': '1048576/16839063', 'float': 0.06227044818348859}` |
| `lift_vs_uniform` | `{'fraction': '14092861440/623669', 'float': 22596.70023682434}` |
| `uses_tail_label` | `False` |
| `empirical_target_equivalent` | `False` |
| `uses_deletion_t252_count` | `True` |

- Verdict: `soft_parent_s_squared_tail_probability_recorded`

## Strongest Claim

The `soft_parent_s_squared` candidate assigns the 10-case tail probability 10485760/16839063.

## What This Improved

This records an exact finite probability for a declared candidate weighting rule.

## What This Weakened Or Falsified

The candidate is weakened as an S1-relevant measure unless it is both non-tautological and independently derivable.

## Falsification Condition

T339 fails if the `soft_parent_s_squared` weights are changed without renaming the measure.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T339 alone.

## Open Blocker

A finite weighting rule is not a physical measure until derived from finality-domain dynamics.

## Suggested Next

Compare this probability against the hard-gate and soft-score rankings, then derive or reject the leading candidate.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
