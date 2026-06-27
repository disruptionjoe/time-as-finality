# T253 Results: Nine-Event Ordinal Deletion Stability

## Aggregate Checks

- Parent ordering fraction: 5/9 (0.556)
- Parent band passed: `True`
- Deletion cases: 9
- Deletions passing T126: 9
- Deletions passing band: 9
- Deletion band pass rate: 1/1 (1.000)
- Verdict: `nine_event_ordinal_deletion_stable_band_control`

## Deletion Table

| Removed | T126 | Strict pairs | Ordering fraction | Band passed | Height | Width | Verdict |
| --- | --- | ---: | ---: | --- | ---: | ---: | --- |
| `e0` | `passes_filter_only` | 12 | 3/7 (0.429) | `True` | 4 | 2 | `t126_pass_and_ordering_fraction_pass` |
| `e1` | `passes_filter_only` | 16 | 4/7 (0.571) | `True` | 5 | 2 | `t126_pass_and_ordering_fraction_pass` |
| `e2` | `passes_filter_only` | 16 | 4/7 (0.571) | `True` | 5 | 2 | `t126_pass_and_ordering_fraction_pass` |
| `e3` | `passes_filter_only` | 16 | 4/7 (0.571) | `True` | 5 | 2 | `t126_pass_and_ordering_fraction_pass` |
| `e4` | `passes_filter_only` | 16 | 4/7 (0.571) | `True` | 5 | 2 | `t126_pass_and_ordering_fraction_pass` |
| `e5` | `passes_filter_only` | 16 | 4/7 (0.571) | `True` | 5 | 2 | `t126_pass_and_ordering_fraction_pass` |
| `e6` | `passes_filter_only` | 16 | 4/7 (0.571) | `True` | 5 | 2 | `t126_pass_and_ordering_fraction_pass` |
| `e7` | `passes_filter_only` | 16 | 4/7 (0.571) | `True` | 5 | 2 | `t126_pass_and_ordering_fraction_pass` |
| `e8` | `passes_filter_only` | 16 | 4/7 (0.571) | `True` | 5 | 2 | `t126_pass_and_ordering_fraction_pass` |

## Strongest Claim

The selected T252 nine-event ordinal witness is stable under every single-event deletion for the current finite screens: all nine deletions pass T126 and stay inside the declared ordering band.

## What This Improved

T253 supplies the deletion-stability contrast missing from T252 and separates it from the T249 grid, whose deletions all failed the same band.

## What This Weakened Or Falsified

This weakens only the specific T249-style over-ordering concern. It does not show that such witnesses are common, natural, local, sprinkling-like, or continuum-relevant.

## Falsification Condition

T253 fails if deletion suborders are not restrictions of the T252 quotient-union relation, if any deletion leaves the declared band without being reported, or if finite deletion stability is promoted into a continuum claim.

## S1 Update

S1 remains guarded. The selected witness is deletion-stable under the declared finite screens only.

## Claim Ledger Update

Do not update the claim ledger from T253 alone. Safe future wording: the selected T252 witness is single-deletion stable for T126 and T156.

## Open Blocker

Deletion stability has not been connected to a selection measure, locality law, random sprinkling ensemble, or Lorentzian data.

## Suggested Next

Compare the T252 witness against the T249 grid and run a small mutation screen to estimate finite sensitivity.

## Not Claimed

These controls do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, or settle S1.
