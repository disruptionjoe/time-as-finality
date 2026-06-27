# T307 Results: Hard Gate Ranking

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `hard_gate_ranking` | `[{'name': 'parentcap', 'description': 'Hard conditioning on the T252-style parent interval and cover cap.', 'total_weight': 66, 'tail_weight': 10, 'parent_cap_weight': 66, 'selected_t252_weight': 1, 'tail_probability': {'fraction': '5/33', 'float': 0.15151515151515152}, 'parent_cap_probability': {'fraction': '1/1', 'float': 1.0}, 'selected_t252_probability': {'fraction': '1/66', 'float': 0.015151515151515152}, 'tail_lift_vs_uniform': {'fraction': '60480/11', 'float': 5498.181818181818}, 'tautological': False}, {'name': 'lowcover', 'description': 'Hard conditioning on T126+band and parent cover hub <= 2/7.', 'total_weight': 185, 'tail_weight': 10, 'parent_cap_weight': 66, 'selected_t252_weight': 1, 'tail_probability': {'fraction': '2/37', 'float': 0.05405405405405406}, 'parent_cap_probability': {'fraction': '66/185', 'float': 0.3567567567567568}, 'selected_t252_probability': {'fraction': '1/185', 'float': 0.005405405405405406}, 'tail_lift_vs_uniform': {'fraction': '72576/37', 'float': 1961.5135135135135}, 'tautological': False}, {'name': 't253', 'description': 'Hard conditioning on T253-style deletion-band stability.', 'total_weight': 8339, 'tail_weight': 10, 'parent_cap_weight': 10, 'selected_t252_weight': 1, 'tail_probability': {'fraction': '10/8339', 'float': 0.001199184554502938}, 'parent_cap_probability': {'fraction': '10/8339', 'float': 0.001199184554502938}, 'selected_t252_probability': {'fraction': '1/8339', 'float': 0.0001199184554502938}, 'tail_lift_vs_uniform': {'fraction': '362880/8339', 'float': 43.51600911380262}, 'tautological': False}, {'name': 'interval3', 'description': 'Hard conditioning on T126+band and parent largest interval <= 3.', 'total_weight': 91350, 'tail_weight': 10, 'parent_cap_weight': 66, 'selected_t252_weight': 1, 'tail_probability': {'fraction': '1/9135', 'float': 0.00010946907498631637}, 'parent_cap_probability': {'fraction': '11/15225', 'float': 0.000722495894909688}, 'selected_t252_probability': {'fraction': '1/91350', 'float': 1.0946907498631636e-05}, 'tail_lift_vs_uniform': {'fraction': '576/145', 'float': 3.972413793103448}, 'tautological': False}, {'name': 'band', 'description': 'Hard conditioning on T126 plus the declared T156 ordering band.', 'total_weight': 143435, 'tail_weight': 10, 'parent_cap_weight': 66, 'selected_t252_weight': 1, 'tail_probability': {'fraction': '2/28687', 'float': 6.971799072750723e-05}, 'parent_cap_probability': {'fraction': '66/143435', 'float': 0.00046013873880154774}, 'selected_t252_probability': {'fraction': '1/143435', 'float': 6.9717990727507235e-06}, 'tail_lift_vs_uniform': {'fraction': '72576/28687', 'float': 2.5299264475197827}, 'tautological': False}, {'name': 'uniform', 'description': 'Uniform ordinal ensemble over all 9! permutations.', 'total_weight': 362880, 'tail_weight': 10, 'parent_cap_weight': 66, 'selected_t252_weight': 1, 'tail_probability': {'fraction': '1/36288', 'float': 2.755731922398589e-05}, 'parent_cap_probability': {'fraction': '11/60480', 'float': 0.00018187830687830687}, 'selected_t252_probability': {'fraction': '1/362880', 'float': 2.7557319223985893e-06}, 'tail_lift_vs_uniform': {'fraction': '1/1', 'float': 1.0}, 'tautological': False}]` |

- Verdict: `best_non_tautological_hard_gate_is_parent_cap`

## Strongest Claim

Among non-tautological hard gates, the T252 parent cap is best, raising tail probability to 5/33.

## What This Improved

T307 makes the finite hard-gate tradeoff explicit.

## What This Weakened Or Falsified

It weakens weaker hard gates as serious selection candidates.

## Falsification Condition

T307 fails if tautological tail conditioning is ranked as acceptable.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T307 alone.

## Open Blocker

The best non-tautological hard gate still leaves 56 false positives.

## Suggested Next

Compare soft scores.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
