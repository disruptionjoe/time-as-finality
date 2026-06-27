# T255 Results: Nine-Event Ordinal Mutation Sensitivity

## Aggregate Checks

- Mutation count: 36
- T126 pass and band pass: 21
- T126 pass outside band: 2
- T126 blocked inside band: 13
- Band total: 34
- Verdict: `mutation_neighborhood_mixed_but_band_common`

## Mutation Table

| Swap | T126 | Ordering fraction | Band passed | Height | Width |
| --- | --- | ---: | --- | ---: | ---: |
| `[0, 1]` | `passes_filter_only` | 19/36 (0.528) | `True` | 5 | 2 |
| `[0, 2]` | `passes_filter_only` | 17/36 (0.472) | `True` | 5 | 3 |
| `[0, 3]` | `passes_filter_only` | 5/12 (0.417) | `True` | 5 | 3 |
| `[0, 4]` | `passes_filter_only` | 13/36 (0.361) | `False` | 5 | 3 |
| `[0, 5]` | `passes_filter_only` | 19/36 (0.528) | `True` | 5 | 2 |
| `[0, 6]` | `passes_filter_only` | 17/36 (0.472) | `True` | 5 | 3 |
| `[0, 7]` | `passes_filter_only` | 5/12 (0.417) | `True` | 5 | 3 |
| `[0, 8]` | `passes_filter_only` | 13/36 (0.361) | `False` | 5 | 3 |
| `[1, 2]` | `order_dimension_obstruction` | 19/36 (0.528) | `True` | 5 | 3 |
| `[1, 3]` | `order_dimension_obstruction` | 17/36 (0.472) | `True` | 5 | 4 |
| `[1, 4]` | `passes_filter_only` | 5/12 (0.417) | `True` | 5 | 4 |
| `[1, 5]` | `passes_filter_only` | 7/12 (0.583) | `True` | 5 | 3 |
| `[1, 6]` | `order_dimension_obstruction` | 7/12 (0.583) | `True` | 5 | 3 |
| `[1, 7]` | `order_dimension_obstruction` | 7/12 (0.583) | `True` | 5 | 3 |
| `[1, 8]` | `passes_filter_only` | 7/12 (0.583) | `True` | 5 | 2 |
| `[2, 3]` | `order_dimension_obstruction` | 19/36 (0.528) | `True` | 5 | 3 |
| `[2, 4]` | `passes_filter_only` | 17/36 (0.472) | `True` | 5 | 4 |
| `[2, 5]` | `order_dimension_obstruction` | 7/12 (0.583) | `True` | 5 | 3 |
| `[2, 6]` | `order_dimension_obstruction` | 7/12 (0.583) | `True` | 4 | 3 |
| `[2, 7]` | `passes_filter_only` | 7/12 (0.583) | `True` | 4 | 3 |
| `[2, 8]` | `order_dimension_obstruction` | 7/12 (0.583) | `True` | 5 | 3 |
| `[3, 4]` | `passes_filter_only` | 19/36 (0.528) | `True` | 5 | 3 |
| `[3, 5]` | `order_dimension_obstruction` | 7/12 (0.583) | `True` | 5 | 3 |
| `[3, 6]` | `passes_filter_only` | 7/12 (0.583) | `True` | 4 | 3 |
| `[3, 7]` | `passes_filter_only` | 7/12 (0.583) | `True` | 4 | 3 |
| `[3, 8]` | `passes_filter_only` | 7/12 (0.583) | `True` | 5 | 3 |
| `[4, 5]` | `passes_filter_only` | 7/12 (0.583) | `True` | 5 | 2 |
| `[4, 6]` | `order_dimension_obstruction` | 7/12 (0.583) | `True` | 5 | 3 |
| `[4, 7]` | `passes_filter_only` | 7/12 (0.583) | `True` | 5 | 3 |
| `[4, 8]` | `passes_filter_only` | 7/12 (0.583) | `True` | 5 | 3 |
| `[5, 6]` | `order_dimension_obstruction` | 19/36 (0.528) | `True` | 5 | 3 |
| `[5, 7]` | `order_dimension_obstruction` | 17/36 (0.472) | `True` | 5 | 4 |
| `[5, 8]` | `passes_filter_only` | 5/12 (0.417) | `True` | 5 | 4 |
| `[6, 7]` | `order_dimension_obstruction` | 19/36 (0.528) | `True` | 5 | 3 |
| `[6, 8]` | `passes_filter_only` | 17/36 (0.472) | `True` | 5 | 4 |
| `[7, 8]` | `passes_filter_only` | 19/36 (0.528) | `True` | 5 | 3 |

## Strongest Claim

In the 36 one-transposition neighbors of the T252 permutation, 21 still pass both T126 and the ordering band, 13 remain inside the band but are blocked by T126, and 2 pass T126 outside the band.

## What This Improved

T255 shows the T252 witness is not a single isolated permutation, but the T126 shape filter still matters inside its local mutation neighborhood.

## What This Weakened Or Falsified

The result weakens both extremes: T252 is not unique, but its neighborhood is not uniformly good enough to support an S1 upgrade.

## Falsification Condition

T255 fails if mutations are not single transpositions of the declared permutation, if T126/T156 targets differ from T252, or if local mutation abundance is treated as a global ensemble result.

## S1 Update

S1 remains guarded. Mutation-local abundance is a search hint, not a selection law or continuum bridge.

## Claim Ledger Update

Do not update the claim ledger from T255 alone. Safe future wording: the selected ordinal witness has nearby finite controls, but the local neighborhood is mixed under T126.

## Open Blocker

No global abundance, measure, locality, sprinkling, or Lorentzian selection principle has been derived for the positive neighborhood.

## Suggested Next

If continuing, run a bounded exact n=9 class count or a stricter locality diagnostic, rather than adding more hand-picked examples.

## Not Claimed

These controls do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, or settle S1.
