# T265 Results: Exact n=9 T126 Census

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `total_cases` | `362880` |
| `t126_pass_count` | `263047` |
| `t126_classification_counts` | `[{'value': 'hub_nonlocality_obstruction', 'count': 7341}, {'value': 'interval_profile_obstruction', 'count': 2050}, {'value': 'order_dimension_obstruction', 'count': 90440}, {'value': 'passes_filter_only', 'count': 263047}, {'value': 'rank_width_obstruction', 'count': 2}]` |

- Verdict: `n9_t126_census_complete`

## Strongest Claim

At n=9, 263047 of 362880 ordinal permutations pass T126; the rest are rejected by named finite obstructions.

## What This Improved

This gives the first exact n=9 T126 denominator for the ordinal ensemble.

## What This Weakened Or Falsified

It weakens any reading that T126 alone is highly selective at n=9; most cases still pass that filter.

## Falsification Condition

T265 fails if the sweep does not exhaust all 9! ordinal permutations.

## S1 Update

S1 is unchanged; T126 passing remains filter-only.

## Claim Ledger Update

Do not update the claim ledger from T265 alone.

## Open Blocker

T126 alone does not identify the rare stable tail or a continuum-facing family.

## Suggested Next

Apply the declared ordering band and shape/deletion gates.

## Not Claimed

These exact counts do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
