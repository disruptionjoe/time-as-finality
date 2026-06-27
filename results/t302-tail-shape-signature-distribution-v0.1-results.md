# T302 Results: Tail Shape Signature Distribution

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `tail_signature_distribution` | `[{'value': [16, 7, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [17, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [18, 9, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [20, 8, 5, 2, [1, 2, 2, 2, 2], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}, {'value': [20, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}]` |
| `parent_signature_distribution` | `[{'value': [15, 8, 4, 3, [2, 3, 2, 2], 2, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [15, 8, 4, 3, [2, 3, 3, 1], 2, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [15, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 10}, {'value': [15, 8, 5, 3, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 10}, {'value': [15, 8, 5, 3, [3, 3, 1, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [15, 8, 5, 4, [2, 4, 1, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [15, 8, 5, 4, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [16, 7, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [16, 7, 5, 3, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [16, 7, 5, 3, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [16, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 6}, {'value': [17, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [17, 8, 5, 3, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [17, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [18, 9, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [20, 8, 5, 2, [1, 2, 2, 2, 2], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}, {'value': [20, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}]` |

- Verdict: `tail_has_five_shape_signatures`

## Strongest Claim

The 10-case tail occupies five parent shape signatures, so it is narrow but not a single shape.

## What This Improved

T302 prevents treating the tail as one rigid poset.

## What This Weakened Or Falsified

It weakens both singleton and broad-family readings.

## Falsification Condition

T302 fails if signatures do not include strict pairs, covers, height, width, rank profile, interval cap, and cover hub.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T302 alone.

## Open Blocker

The shape signatures still lack a generative explanation.

## Suggested Next

Record representatives for future measure proposals.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
