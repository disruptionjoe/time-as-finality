# T163 Results: T54 Rank-Pair Family Census

## Aggregate Checks

- Total labeled six-event rank-pair cases: 720
- T156 failures after T126 pass: 273
- Parent-interval failures after T156 pass: 149
- Jackknife-fragile cases after parent-interval pass: 130
- Stable survivors after all current screens: 26
- Stable-survivor fraction of full family: 13/360 (0.036)
- T157 baseline permutation: `[1, 6, 4, 5, 2, 3]`
- T157 baseline bucket: `t159_fragile_jackknife`
- T157 baseline stable: `False`

## T126 Classification Counts

| Classification | Count |
| --- | ---: |
| `hub_nonlocality_obstruction` | 110 |
| `interval_profile_obstruction` | 20 |
| `order_dimension_obstruction` | 10 |
| `passes_filter_only` | 578 |
| `rank_width_obstruction` | 2 |

## Representative Cases

- Stable survivor permutations: `[[2, 4, 6, 1, 5, 3], [2, 5, 1, 6, 4, 3], [2, 5, 6, 1, 3, 4], [3, 1, 6, 5, 2, 4], [3, 4, 6, 1, 2, 5]]`
- Fragile survivor permutations: `[[1, 4, 6, 5, 2, 3], [1, 4, 6, 5, 3, 2], [1, 5, 6, 2, 4, 3], [1, 5, 6, 3, 4, 2], [1, 5, 6, 4, 2, 3]]`

## Strongest Claim

The T157 witness is not an isolated accident, but it is also not representative of the whole six-event rank-pair family. Across all 720 labeled T54 rank-pair completions, 26 survive T126, T156, parent-interval, and single-deletion stability screens, while 130 more are jackknife-fragile and 694 remain below robust finite survivor status.

## What This Improved

T163 upgrades S1 from single-example reading to family-level audit. It quantifies how often six-event T54 rank-pair completions are blocked at T126, miss the T156 target, fail parent-interval support, fail jackknife stability, or survive all current finite screens.

## What This Weakened Or Falsified

This weakens the simple demotion story left by T159. The original T157 construction is fragile, but finite deletion-stable survivors do exist in the same six-event T54 rank-pair family. At the same time it weakens any broad optimism: only 26 of 720 labeled cases clear the current screens, so the family is still highly selective.

## Falsification Condition

T163 fails if the census does not actually exhaust the 6! rank-pair family up to the declared fixing of causal ranks, if any case is audited through a different T54/T126/T156/T159 pipeline than the published controls, or if labeled-case counts are misread as a continuum or generic-family theorem.

## S1 Update

S1 remains open_formal_target. The current finite boundary is now slightly stronger than T159 allowed: six-event deletion-stable T54 rank-pair survivors exist. But they remain tiny finite controls, not spacetime evidence, and still lack sprinkling, locality, embedding, covariance, and continuum diagnostics.

## Claim Ledger Update

Add T163 to S1: an exhaustive six-event T54 rank-pair census finds 26 labeled completions that survive T126, T156, parent-interval, and single-deletion screens, while the original T157 witness stays fragile. The S1 finite boundary is therefore family-level but still strictly calibration/control-level.

## Open Blocker

No isomorphism-class reduction, random-sprinkling comparison, neighborhood-growth rule, locality diagnostic, faithful embedding theorem, covariance result, or continuum bridge exists for the 26 survivors.

## Suggested Next

Quotient the 26 survivors by isomorphism and compare those classes against a declared random-sprinkling or locality diagnostic, rather than adding more hand-picked finite examples.

## Not Claimed

T163 does not show a random sprinkling law, faithful embedding, metric or Lorentzian reconstruction, covariance, or a continuum limit. It is a finite family census over one small T54 rank-pair class only.
