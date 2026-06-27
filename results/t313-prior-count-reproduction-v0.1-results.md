# T313 Results: Prior Count Reproduction

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `band_count` | `143435` |
| `t253_stable_count` | `8339` |
| `parentcap_count` | `66` |
| `tail_count` | `10` |

- Verdict: `measure_stress_reproduces_prior_counts`

## Strongest Claim

The stress audit reproduces the prior n=9 counts: 143435 band cases, 8339 deletion-band stable cases, 66 parent-cap cases, and 10 tail cases.

## What This Improved

T313 validates that the expanded measure audit uses the same denominator.

## What This Weakened Or Falsified

It weakens concern that the stronger measures are computed over a shifted ensemble.

## Falsification Condition

T313 fails if any reproduced count changes under the same definitions.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T313 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
