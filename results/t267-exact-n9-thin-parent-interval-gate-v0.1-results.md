# T267 Results: Exact n=9 Thin Parent-Interval Gate

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `parent_interval_cap1_count` | `7813` |
| `parent_interval_cap1_fraction` | `{'fraction': '7813/362880', 'float': 0.021530533509700175}` |
| `t156_largest_interval_distribution` | `[{'value': 1, 'count': 7813}, {'value': 2, 'count': 35404}, {'value': 3, 'count': 48133}, {'value': 4, 'count': 34339}, {'value': 5, 'count': 13921}, {'value': 6, 'count': 3392}, {'value': 7, 'count': 433}]` |

- Verdict: `n9_thin_parent_interval_gate_complete`

## Strongest Claim

Only 7813 n=9 T126+T156 cases have largest parent interval size at most 1.

## What This Improved

This extends the T159/T223 thin-parent gate to the n=9 denominator.

## What This Weakened Or Falsified

It weakens the selected T252 route under the older thin gate: T252 has largest interval size 3, not 1.

## Falsification Condition

T267 fails if largest interval sizes are not computed from the audited strict relation.

## S1 Update

S1 is unchanged; thin parent intervals are finite diagnostics only.

## Claim Ledger Update

Do not update the claim ledger from T267 alone.

## Open Blocker

Thinness is still a hostile finite screen, not a continuum theorem.

## Suggested Next

Check deletion stability for the thin-parent cases.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
