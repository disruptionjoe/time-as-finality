# T278 Results: Post-n=9 Route Selection

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `thin_stable_count` | `1583` |
| `t252_style_stable_count` | `10` |
| `selected_next_route` | `non_uniform_selection_measure_for_t252_style_tail` |
| `rejected_route` | `more_uniform_ordinal_counting_without_new_measure` |

- Verdict: `post_n9_route_requires_non_uniform_selection_or_new_bridge`

## Strongest Claim

After exact n=9 counting, the meaningful next route is a non-uniform selection measure or a different bridge, not more uniform ordinal counting alone.

## What This Improved

T278 converts the 16-task data into an actionable research decision.

## What This Weakened Or Falsified

It weakens further hand-picked or uniform-count-only rounds: the exact count already says the relevant tails are rare.

## Falsification Condition

T278 fails if the n=9 count is incomplete or if route selection ignores the tiny T252-style tail.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Safe future wording: exact n=9 counting strengthens the need for an added selection assumption.

## Open Blocker

The actual added measure or continuum bridge remains unbuilt.

## Suggested Next

Next, define and test a non-uniform finality-colimit measure against the 10 T252-style cases.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
