# T319 Results: Tail Shape Signature Check

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `tail_signature_distribution` | `[{'value': [16, 7, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [17, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [18, 9, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [20, 8, 5, 2, [1, 2, 2, 2, 2], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}, {'value': [20, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}]` |
| `parentcap_signature_distribution` | `[{'value': [15, 8, 4, 3, [2, 3, 2, 2], 2, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [15, 8, 4, 3, [2, 3, 3, 1], 2, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [15, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 10}, {'value': [15, 8, 5, 3, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 10}, {'value': [15, 8, 5, 3, [3, 3, 1, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [15, 8, 5, 4, [2, 4, 1, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [15, 8, 5, 4, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [16, 7, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [16, 7, 5, 3, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [16, 7, 5, 3, [3, 2, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [16, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 6}, {'value': [17, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [17, 8, 5, 3, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [17, 8, 5, 3, [2, 3, 2, 1, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 4}, {'value': [18, 9, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 2}, {'value': [20, 8, 5, 2, [1, 2, 2, 2, 2], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}, {'value': [20, 8, 5, 2, [2, 2, 2, 2, 1], 3, {'fraction': '1/4', 'float': 0.25}], 'count': 1}]` |

- Verdict: `tail_shape_signatures_reproduced`

## Strongest Claim

The 10-case tail remains narrow but not shape-singleton: it occupies multiple parent signatures.

## What This Improved

T319 keeps selection-measure work from collapsing the target into one hand-picked shape.

## What This Weakened Or Falsified

It weakens singleton-shape explanations.

## Falsification Condition

T319 fails if signatures omit the rank profile or cover/interval data.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T319 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
