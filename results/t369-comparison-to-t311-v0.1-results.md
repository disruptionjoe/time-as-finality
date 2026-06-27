# T369 Results: Comparison To T311

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t311_best_non_tautological_probability` | `{'fraction': '5/33', 'float': 0.15151515151515152}` |
| `t312_t375_best_simple_hard_probability` | `{'fraction': '5/8', 'float': 0.625}` |
| `t312_t375_best_soft_probability` | `{'fraction': '1342177280/1705336003', 'float': 0.7870456482704071}` |

- Verdict: `expanded_measure_family_strengthens_tail_concentration`

## Strongest Claim

The expanded family improves the best non-tail concentration from 5/33 to 5/8 for a hard gate and above 3/4 for a soft score.

## What This Improved

T369 updates the previous round with a stronger candidate family.

## What This Weakened Or Falsified

It weakens the conclusion that all obvious finite weights are insufficient.

## Falsification Condition

T369 fails if the prior and current candidates are not compared on the same target tail.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T369 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
