# T272 Results: n=9 T252-Style Deletion Stability

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t252_parent_cap_count` | `66` |
| `t252_deletion_stable_count` | `10` |
| `t252_deletion_stable_fraction` | `{'fraction': '1/36288', 'float': 2.755731922398589e-05}` |
| `t252_deletion_stable_signature_distribution` | `[{'value': [16, 7, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [17, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [18, 9, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [20, 8, 5, 2, [1, 2, 2, 2, 2], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}, {'value': [20, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}]` |
| `representative_t252_deletion_stable_permutations` | `[[1, 6, 7, 8, 9, 2, 3, 4, 5], [4, 6, 7, 8, 1, 9, 2, 3, 5], [4, 6, 7, 8, 9, 1, 2, 3, 5], [5, 6, 7, 8, 1, 2, 3, 4, 9], [5, 6, 7, 8, 1, 9, 2, 3, 4], [5, 6, 7, 8, 9, 1, 2, 3, 4], [5, 7, 8, 1, 9, 2, 3, 4, 6], [5, 7, 8, 9, 1, 2, 3, 4, 6], [6, 7, 8, 1, 9, 2, 3, 4, 5], [6, 7, 8, 9, 1, 2, 3, 4, 5]]` |

- Verdict: `n9_t252_style_deletion_stable_tail_has_ten_cases`

## Strongest Claim

Only 10 n=9 permutations pass the T252-style parent cap and keep every deletion inside the same T126/band/interval/cover gate.

## What This Improved

This gives a precise global answer to the T252/T253/T257 route: it exists, but it is a very small tail.

## What This Weakened Or Falsified

It weakens both extremes: T252 is not unique, but T252-style deletion stability is far from typical.

## Falsification Condition

T272 fails if deletions are not rank-normalized suborders of the same parent permutation.

## S1 Update

S1 remains guarded; ten finite cases are not a continuum mechanism.

## Claim Ledger Update

Do not update the claim ledger from T272 alone.

## Open Blocker

The ten-case tail has no natural measure or generative law attached.

## Suggested Next

Inspect where the selected T252 witness sits inside this tail.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
