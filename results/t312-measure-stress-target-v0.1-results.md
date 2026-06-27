# T312 Results: Measure Stress Target

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `total_cases` | `362880` |
| `target_tail_count` | `10` |
| `uniform_tail_probability` | `{'fraction': '1/36288', 'float': 2.755731922398589e-05}` |

- Verdict: `measure_stress_target_declared`

## Strongest Claim

The finite measure stress target is the same 10-case T252-style tail, with uniform probability 1/36288.

## What This Improved

T312 fixes the target before evaluating a larger candidate-measure family.

## What This Weakened Or Falsified

It weakens hidden-target risk in this round.

## Falsification Condition

T312 fails if the target is not the T272/T311 tail.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T312 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
