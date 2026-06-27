# T352 Results: Hard Cover-Deletion False Positives

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `hard_cover_deletion_count` | `16` |
| `tail_count_inside_gate` | `10` |
| `false_positive_count` | `6` |

- Verdict: `cover_deletion_gate_has_six_false_positives`

## Strongest Claim

The strongest non-target hard gate has 6 false positives outside the 10-case target tail.

## What This Improved

T352 makes the remaining burden explicit.

## What This Weakened Or Falsified

It weakens treating cover+deletion as already identical to the target.

## Falsification Condition

T352 fails if false positives are not counted inside the hard gate.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T352 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
