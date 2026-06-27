# T317 Results: Selected T252 Placement

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `selected_t252_diagnostics` | `{'classification': 'passes_filter_only', 'strict_pair_count': 20, 'cover_relation_count': 8, 'height': 5, 'width': 2, 'rank_profile': [1, 2, 2, 2, 2], 'largest_interval_size': 3, 'largest_cover_hub_fraction': {'fraction': '1/4', 'float': 0.25}}` |
| `selected_t252_deletion_summary` | `{'deletion_count': 9, 't159_thin_deletion_pass_count': 0, 'relaxed_interval3_deletion_pass_count': 9, 't253_t126_band_deletion_pass_count': 9, 't252_style_deletion_pass_count': 9}` |

- Verdict: `selected_t252_has_full_deletion_t252_count`

## Strongest Claim

The selected T252 witness has all nine deletion suborders passing the T252-style deletion gate.

## What This Improved

T317 anchors the selected witness inside the expanded deletion-count audit.

## What This Weakened Or Falsified

It weakens any account that ignores deletion substructure.

## Falsification Condition

T317 fails if the selected permutation is not the T252 rank order.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T317 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
