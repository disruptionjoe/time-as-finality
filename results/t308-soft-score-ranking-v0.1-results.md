# T308 Results: Soft Score Ranking

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `soft_score_ranking` | `[{'name': 'shape_soft', 'description': 'Soft score for T252-like parent shape labels without using the tail label.', 'total_weight': 987721, 'tail_weight': 640, 'parent_cap_weight': 2208, 'selected_t252_weight': 128, 'tail_probability': {'fraction': '640/987721', 'float': 0.0006479562548533443}, 'parent_cap_probability': {'fraction': '2208/987721', 'float': 0.0022354490792440376}, 'selected_t252_probability': {'fraction': '128/987721', 'float': 0.00012959125097066883}, 'tail_lift_vs_uniform': {'fraction': '3317760/141103', 'float': 23.513036576118154}, 'tautological': False}, {'name': 'deletion_soft', 'description': 'Soft integer score 2^(band + interval3 + lowcover + t253 + relaxed deletion interval3).', 'total_weight': 790437, 'tail_weight': 320, 'parent_cap_weight': 768, 'selected_t252_weight': 32, 'tail_probability': {'fraction': '320/790437', 'float': 0.0004048393483604639}, 'parent_cap_probability': {'fraction': '256/263479', 'float': 0.0009716144360651134}, 'selected_t252_probability': {'fraction': '32/790437', 'float': 4.048393483604639e-05}, 'tail_lift_vs_uniform': {'fraction': '3870720/263479', 'float': 14.690810273304514}, 'tautological': False}, {'name': 'parent_soft', 'description': 'Soft integer score 2^(band + interval3 + lowcover).', 'total_weight': 689517, 'tail_weight': 80, 'parent_cap_weight': 528, 'selected_t252_weight': 8, 'tail_probability': {'fraction': '80/689517', 'float': 0.00011602324525718728}, 'parent_cap_probability': {'fraction': '176/229839', 'float': 0.0007657534186974361}, 'selected_t252_probability': {'fraction': '8/689517', 'float': 1.1602324525718728e-05}, 'tail_lift_vs_uniform': {'fraction': '322560/76613', 'float': 4.210251523892812}, 'tautological': False}, {'name': 'anti_parent', 'description': 'Control score 2^(band + not-interval3 + not-lowcover).', 'total_weight': 1659252, 'tail_weight': 20, 'parent_cap_weight': 132, 'selected_t252_weight': 2, 'tail_probability': {'fraction': '5/414813', 'float': 1.2053624163177143e-05}, 'parent_cap_probability': {'fraction': '11/138271', 'float': 7.955391947696913e-05}, 'selected_t252_probability': {'fraction': '1/829626', 'float': 1.2053624163177142e-06}, 'tail_lift_vs_uniform': {'fraction': '8640/19753', 'float': 0.43740191363337216}, 'tautological': False}]` |

- Verdict: `soft_scores_enrich_but_do_not_concentrate_tail`

## Strongest Claim

The tested soft integer scores enrich the target tail but stay far below the parent-cap hard gate.

## What This Improved

T308 separates smooth enrichment from actual concentration.

## What This Weakened Or Falsified

It weakens soft-score optimism without a sharper derivation.

## Falsification Condition

T308 fails if soft scores include the target label while being reported as non-tautological.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T308 alone.

## Open Blocker

No tested soft score supplies a convincing added measure.

## Suggested Next

Set a concentration threshold.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
