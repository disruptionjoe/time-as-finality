# T271 Results: n=9 T252-Style Parent Cap

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t252_parent_cap_count` | `66` |
| `t252_parent_cap_fraction` | `{'fraction': '11/60480', 'float': 0.00018187830687830687}` |
| `t252_parent_signature_distribution` | `[{'value': [15, 8, 4, 3, [2, 3, 2, 2], 2, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [15, 8, 4, 3, [2, 3, 3, 1], 2, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [15, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 10}, {'value': [15, 8, 5, 3, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 10}, {'value': [15, 8, 5, 3, [3, 3, 1, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [15, 8, 5, 4, [2, 4, 1, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [15, 8, 5, 4, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [16, 7, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [16, 7, 5, 3, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [16, 7, 5, 3, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [16, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 6}, {'value': [17, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [17, 8, 5, 3, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [17, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [18, 9, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [20, 8, 5, 2, [1, 2, 2, 2, 2], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}, {'value': [20, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}]` |

- Verdict: `n9_t252_style_parent_cap_is_rare`

## Strongest Claim

Only 66 n=9 permutations match the T252-style parent cap: T126+band, largest interval <=3, and cover hub <=2/7.

## What This Improved

This makes T252's parent shape a genuinely rare global feature, not just another band-positive case.

## What This Weakened Or Falsified

It weakens the local-neighborhood optimism from T255: the stricter T252-style parent cap is globally tiny.

## Falsification Condition

T271 fails if the cover cap differs from the T257 deletion-stable cap.

## S1 Update

S1 is unchanged; rarity under one finite ensemble is not a physical selection law.

## Claim Ledger Update

Do not update the claim ledger from T271 alone.

## Open Blocker

The 66 parents still need deletion stability and a selection explanation.

## Suggested Next

Apply the same cap to every single-event deletion.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
