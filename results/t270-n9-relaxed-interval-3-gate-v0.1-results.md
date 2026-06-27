# T270 Results: n=9 Relaxed Interval-3 Gate

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `parent_interval_cap3_count` | `91350` |
| `relaxed_interval3_deletion_stable_count` | `9176` |
| `parent_interval_cap3_fraction` | `{'fraction': '145/576', 'float': 0.2517361111111111}` |

- Verdict: `n9_relaxed_interval3_gate_complete`

## Strongest Claim

Relaxing the parent interval cap from 1 to 3 admits 91350 parents and 9176 deletion-stable cases.

## What This Improved

This quantifies how much of T252's interval behavior is excluded by the older thin gate.

## What This Weakened Or Falsified

It weakens a binary reading of interval size: cap 3 is much less rare than T252's full cover-local shape.

## Falsification Condition

T270 fails if the relaxed cap is mixed with the older T159 thin cap.

## S1 Update

S1 is unchanged; relaxing a finite cap does not establish locality.

## Claim Ledger Update

Do not update the claim ledger from T270 alone.

## Open Blocker

Interval cap 3 alone is too permissive to explain T252's selected shape.

## Suggested Next

Add the cover-hub cap from T257.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
