# T354 Results: Deletion Temperature Ladder

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `soft_s_count` | `{'fraction': '5120/382129', 'float': 0.013398616697502676}` |
| `soft_s_count_squared` | `{'fraction': '2621440/4627863', 'float': 0.5664471917167816}` |
| `soft_s_count_cubed` | `{'fraction': '1342177280/1705336003', 'float': 0.7870456482704071}` |

- Verdict: `deletion_temperature_has_threshold_behavior`

## Strongest Claim

Tail probability rises from about 1.3 percent to 56.6 percent to 78.7 percent as the T252-deletion-count temperature increases.

## What This Improved

T354 shows that concentration depends strongly on temperature.

## What This Weakened Or Falsified

It weakens treating one arbitrary temperature as principled.

## Falsification Condition

T354 fails if the temperature ladder changes after seeing probabilities.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T354 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
