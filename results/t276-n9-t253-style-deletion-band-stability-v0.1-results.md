# T276 Results: n=9 T253-Style Deletion-Band Stability

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `t253_all_deletions_t126_band_stable_count` | `8339` |
| `t253_all_deletions_t126_band_stable_fraction` | `{'fraction': '8339/362880', 'float': 0.022980048500881835}` |
| `t253_stable_parent_max_interval_distribution` | `[{'value': 1, 'count': 970}, {'value': 2, 'count': 4682}, {'value': 3, 'count': 2249}, {'value': 4, 'count': 386}, {'value': 5, 'count': 52}]` |
| `t253_stable_parent_cover_hub_distribution` | `[{'value': {'fraction': '1/4', 'float': 0.25}, 'count': 16}, {'value': {'fraction': '3/8', 'float': 0.375}, 'count': 1512}, {'value': {'fraction': '1/2', 'float': 0.5}, 'count': 5395}, {'value': {'fraction': '5/8', 'float': 0.625}, 'count': 1416}]` |

- Verdict: `n9_t253_style_deletion_band_stability_has_8339_cases`

## Strongest Claim

8339 n=9 permutations pass T126+band and keep every deletion inside T126+band, but most do not satisfy the stricter T252 cover shape.

## What This Improved

This locates T253-style stability between the broad band-positive set and the tiny T252-style tail.

## What This Weakened Or Falsified

It weakens any assumption that deletion-band stability alone recovers T252-like locality.

## Falsification Condition

T276 fails if deletion T126+band checks use a different target from the parent.

## S1 Update

S1 remains guarded; deletion-band stability is still finite control evidence.

## Claim Ledger Update

Do not update the claim ledger from T276 alone.

## Open Blocker

Many deletion-stable band cases have larger cover hubs or intervals.

## Suggested Next

Use obstruction anatomy and route selection to decide what to do next.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
