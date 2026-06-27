# T273 Results: Selected T252 Global Placement

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `selected_t252_rank_permutation` | `[1, 6, 7, 8, 9, 2, 3, 4, 5]` |
| `selected_t252_strict_pairs` | `20` |
| `selected_t252_largest_interval` | `3` |
| `selected_t252_cover_hub` | `{'fraction': '1/4', 'float': 0.25}` |
| `selected_t252_deletion_summary` | `{'deletion_count': 9, 't159_thin_deletion_pass_count': 0, 'relaxed_interval3_deletion_pass_count': 9, 't253_t126_band_deletion_pass_count': 9, 't252_style_deletion_pass_count': 9}` |
| `selected_is_t252_style_deletion_stable` | `True` |

- Verdict: `selected_t252_is_one_of_the_ten_t252_style_stable_cases`

## Strongest Claim

The selected T252 permutation is one of the 10 exact n=9 T252-style deletion-stable cases.

## What This Improved

This anchors the selected witness inside the global count instead of leaving it as a hand-picked orphan.

## What This Weakened Or Falsified

It weakens overclaiming: T252 fails the older thin cap, so its support depends on the relaxed interval/cover gate.

## Falsification Condition

T273 fails if the selected permutation is not audited as the same rank order used in T252.

## S1 Update

S1 remains guarded; global placement is not physical selection.

## Claim Ledger Update

Do not update the claim ledger from T273 alone.

## Open Blocker

Being one of ten finite cases does not explain why nature would select that tail.

## Suggested Next

Compare the local T255 neighborhood against global rates.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
