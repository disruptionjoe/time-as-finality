# T349 Results: Best Non-Target Hard Gate

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `best_non_target_hard_gate` | `{'name': 'hard_cover_deletion', 'description': 'Hard gate: low cover and deletion-band stability.', 'total_weight': 16, 'tail_weight': 10, 'parentcap_weight': 10, 'selected_weight': 1, 'tail_probability': {'fraction': '5/8', 'float': 0.625}, 'parentcap_probability': {'fraction': '5/8', 'float': 0.625}, 'selected_probability': {'fraction': '1/16', 'float': 0.0625}, 'lift_vs_uniform': {'fraction': '22680/1', 'float': 22680.0}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': False}` |

- Verdict: `cover_deletion_hard_gate_puts_five_eighths_mass_on_tail`

## Strongest Claim

The best non-target hard gate is low-cover plus deletion-band stability, with tail probability 5/8.

## What This Improved

T349 identifies a genuinely strong finite selection candidate.

## What This Weakened Or Falsified

It weakens the T311 result that obvious finite reweighting was insufficient.

## Falsification Condition

T349 fails if the gate uses the tail label.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T349 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
