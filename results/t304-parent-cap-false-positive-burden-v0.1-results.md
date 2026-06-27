# T304 Results: Parent-Cap False Positive Burden

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `parent_cap_count` | `66` |
| `tail_count` | `10` |
| `false_positive_count` | `56` |
| `t252_parent_deletion_pass_distribution` | `[{'value': 4, 'count': 28}, {'value': 7, 'count': 8}, {'value': 8, 'count': 20}, {'value': 9, 'count': 10}]` |

- Verdict: `parent_cap_has_fifty_six_false_positives`

## Strongest Claim

The 66-case parent cap contains 56 cases that fail full T252-style deletion stability.

## What This Improved

T304 shows the parent gate is not enough; deletion behavior is decisive.

## What This Weakened Or Falsified

It weakens parent-shape-only selection proposals.

## Falsification Condition

T304 fails if deletion pass counts are not computed for every parent-cap case.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T304 alone.

## Open Blocker

The false positives need either a principled exclusion or a broader target.

## Suggested Next

Rank hard gates and soft measures.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
