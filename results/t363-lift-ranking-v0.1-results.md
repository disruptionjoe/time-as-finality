# T363 Results: Lift Ranking

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `lift_ranking` | `[{'name': 'hard_interval_cover_deletion', 'description': 'Hard gate: interval<=3, low cover, and deletion-band stability.', 'total_weight': 10, 'tail_weight': 10, 'parentcap_weight': 10, 'selected_weight': 1, 'tail_probability': {'fraction': '1/1', 'float': 1.0}, 'parentcap_probability': {'fraction': '1/1', 'float': 1.0}, 'selected_probability': {'fraction': '1/10', 'float': 0.1}, 'lift_vs_uniform': {'fraction': '36288/1', 'float': 36288.0}, 'uses_tail_label': False, 'empirical_target_equivalent': True, 'uses_deletion_t252_count': False}, {'name': 'soft_s_count_cubed', 'description': 'Soft score 8^(number of deletion T252-style passes).', 'total_weight': 1705336003, 'tail_weight': 1342177280, 'parentcap_weight': 1694613504, 'selected_weight': 134217728, 'tail_probability': {'fraction': '1342177280/1705336003', 'float': 0.7870456482704071}, 'parentcap_probability': {'fraction': '1694613504/1705336003', 'float': 0.9937123833771543}, 'selected_probability': {'fraction': '134217728/1705336003', 'float': 0.07870456482704072}, 'lift_vs_uniform': {'fraction': '6957847019520/243619429', 'float': 28560.312484436534}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': True}, {'name': 'hard_cover_deletion', 'description': 'Hard gate: low cover and deletion-band stability.', 'total_weight': 16, 'tail_weight': 10, 'parentcap_weight': 10, 'selected_weight': 1, 'tail_probability': {'fraction': '5/8', 'float': 0.625}, 'parentcap_probability': {'fraction': '5/8', 'float': 0.625}, 'selected_probability': {'fraction': '1/16', 'float': 0.0625}, 'lift_vs_uniform': {'fraction': '22680/1', 'float': 22680.0}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': False}, {'name': 'soft_parent_s_squared', 'description': 'Soft score 4^(T252 deletion pass count) with a parent-cap multiplier.', 'total_weight': 16839063, 'tail_weight': 10485760, 'parentcap_weight': 16281600, 'selected_weight': 1048576, 'tail_probability': {'fraction': '10485760/16839063', 'float': 0.6227044818348859}, 'parentcap_probability': {'fraction': '5427200/5613021', 'float': 0.9668946544115905}, 'selected_probability': {'fraction': '1048576/16839063', 'float': 0.06227044818348859}, 'lift_vs_uniform': {'fraction': '14092861440/623669', 'float': 22596.70023682434}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': True}, {'name': 'soft_s_count_squared', 'description': 'Soft score 4^(number of deletion T252-style passes).', 'total_weight': 4627863, 'tail_weight': 2621440, 'parentcap_weight': 4070400, 'selected_weight': 262144, 'tail_probability': {'fraction': '2621440/4627863', 'float': 0.5664471917167816}, 'parentcap_probability': {'fraction': '1356800/1542621', 'float': 0.8795420262008621}, 'selected_probability': {'fraction': '262144/4627863', 'float': 0.05664471917167816}, 'lift_vs_uniform': {'fraction': '10569646080/514207', 'float': 20555.23569301857}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': True}, {'name': 'hard_parentcap', 'description': 'Hard gate: T252-style parent interval+cover cap.', 'total_weight': 66, 'tail_weight': 10, 'parentcap_weight': 66, 'selected_weight': 1, 'tail_probability': {'fraction': '5/33', 'float': 0.15151515151515152}, 'parentcap_probability': {'fraction': '1/1', 'float': 1.0}, 'selected_probability': {'fraction': '1/66', 'float': 0.015151515151515152}, 'lift_vs_uniform': {'fraction': '60480/11', 'float': 5498.181818181818}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': False}, {'name': 'hard_lowcover', 'description': 'Hard gate: T126+band and parent cover hub <= 2/7.', 'total_weight': 185, 'tail_weight': 10, 'parentcap_weight': 66, 'selected_weight': 1, 'tail_probability': {'fraction': '2/37', 'float': 0.05405405405405406}, 'parentcap_probability': {'fraction': '66/185', 'float': 0.3567567567567568}, 'selected_probability': {'fraction': '1/185', 'float': 0.005405405405405406}, 'lift_vs_uniform': {'fraction': '72576/37', 'float': 1961.5135135135135}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': False}, {'name': 'soft_interval_cover_s_count', 'description': 'Soft score 2^(T252 deletion pass count) with an interval+cover multiplier.', 'total_weight': 417265, 'tail_weight': 20480, 'parentcap_weight': 46848, 'selected_weight': 2048, 'tail_probability': {'fraction': '4096/83453', 'float': 0.04908151893880388}, 'parentcap_probability': {'fraction': '46848/417265', 'float': 0.11227397457251387}, 'selected_probability': {'fraction': '2048/417265', 'float': 0.004908151893880388}, 'lift_vs_uniform': {'fraction': '148635648/83453', 'float': 1781.070159251315}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': True}, {'name': 'soft_cover_s_count', 'description': 'Soft score 2^(T252 deletion pass count) with a low-cover multiplier.', 'total_weight': 426940, 'tail_weight': 20480, 'parentcap_weight': 46848, 'selected_weight': 2048, 'tail_probability': {'fraction': '1024/21347', 'float': 0.047969269686607016}, 'parentcap_probability': {'fraction': '11712/106735', 'float': 0.10972970440811355}, 'selected_probability': {'fraction': '512/106735', 'float': 0.004796926968660702}, 'lift_vs_uniform': {'fraction': '37158912/21347', 'float': 1740.7088583875955}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': True}, {'name': 'soft_s_count', 'description': 'Soft score 2^(number of deletion T252-style passes).', 'total_weight': 382129, 'tail_weight': 5120, 'parentcap_weight': 11712, 'selected_weight': 512, 'tail_probability': {'fraction': '5120/382129', 'float': 0.013398616697502676}, 'parentcap_probability': {'fraction': '11712/382129', 'float': 0.03064933569553737}, 'selected_probability': {'fraction': '512/382129', 'float': 0.0013398616697502675}, 'lift_vs_uniform': {'fraction': '185794560/382129', 'float': 486.2090027189771}, 'uses_tail_label': False, 'empirical_target_equivalent': False, 'uses_deletion_t252_count': True}]` |

- Verdict: `lift_ranking_recorded`

## Strongest Claim

The highest non-tail lift comes from high-temperature deletion-count and cover-deletion candidates.

## What This Improved

T363 records exact finite lifts relative to uniform.

## What This Weakened Or Falsified

It weakens qualitative ranking by intuition.

## Falsification Condition

T363 fails if tautological tail conditioning is not marked.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T363 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
