# T359 Results: Anti-Parent Control

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `anti_parent_tail_probability` | `{'fraction': '5/414813', 'float': 1.2053624163177143e-05}` |
| `uniform_tail_probability` | `{'fraction': '1/36288', 'float': 2.755731922398589e-05}` |

- Verdict: `anti_parent_control_suppresses_tail`

## Strongest Claim

The anti-parent control suppresses the target tail below useful concentration.

## What This Improved

T359 checks that the scoring direction matters.

## What This Weakened Or Falsified

It weakens claims that any reweighting will make the tail look good.

## Falsification Condition

T359 fails if control scores are omitted.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T359 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
