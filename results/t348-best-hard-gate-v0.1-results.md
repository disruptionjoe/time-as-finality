# T348 Results: Best Hard Gate

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `best_hard_gate` | `{'name': 'hard_interval_cover_deletion', 'description': 'Hard gate: interval<=3, low cover, and deletion-band stability.', 'total_weight': 10, 'tail_weight': 10, 'parentcap_weight': 10, 'selected_weight': 1, 'tail_probability': {'fraction': '1/1', 'float': 1.0}, 'parentcap_probability': {'fraction': '1/1', 'float': 1.0}, 'selected_probability': {'fraction': '1/10', 'float': 0.1}, 'lift_vs_uniform': {'fraction': '36288/1', 'float': 36288.0}, 'uses_tail_label': False, 'empirical_target_equivalent': True, 'uses_deletion_t252_count': False}` |

- Verdict: `best_hard_gate_is_interval_cover_deletion_but_target_equivalent`

## Strongest Claim

The best hard gate is interval+cover+deletion, but it is empirically target-equivalent at n=9.

## What This Improved

T348 separates explanatory gates from target-equivalent gates.

## What This Weakened Or Falsified

It weakens any claim that a perfect hard gate is automatically a physical measure.

## Falsification Condition

T348 fails if target-equivalent gates are not flagged.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T348 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
