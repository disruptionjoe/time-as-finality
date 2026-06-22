# T167 Results: T54 Ordinal Scaling Stress Test

## Exact Comparison Target

- Target: `exact_ordinal_1p1_rank_permutation_scaling_n5_to_n7`
- Basis: For n generic points in a flat 1+1 causal diamond with no light-cone coordinate ties, sorting by one coordinate leaves the other coordinate's rank as a uniform element of S_n. T167 uses that exact finite ordinal ensemble for n=5, n=6, and n=7.

## Size Summary

| n | Cases | T126 pass | T156 pass | Parent pass | Stable survivors | Stable fraction | Oriented classes | Dual classes | Largest class probability |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 120 | 0 | 0 | 0 | 0 | 0/1 (0.000) | 0 | 0 | 0/1 (0.000) |
| 6 | 720 | 578 | 305 | 156 | 26 | 13/360 (0.036) | 15 | 9 | 1/360 (0.003) |
| 7 | 5040 | 4456 | 2051 | 561 | 174 | 29/840 (0.035) | 86 | 45 | 1/1260 (0.001) |

## T126 Classifications

### n = 5

| Classification | Count |
| --- | ---: |
| `insufficient_scale` | 120 |

### n = 6

| Classification | Count |
| --- | ---: |
| `hub_nonlocality_obstruction` | 110 |
| `interval_profile_obstruction` | 20 |
| `order_dimension_obstruction` | 10 |
| `passes_filter_only` | 578 |
| `rank_width_obstruction` | 2 |

### n = 7

| Classification | Count |
| --- | ---: |
| `hub_nonlocality_obstruction` | 182 |
| `interval_profile_obstruction` | 118 |
| `order_dimension_obstruction` | 282 |
| `passes_filter_only` | 4456 |
| `rank_width_obstruction` | 2 |

## Deletion Stability After Parent-Interval Pass

### n = 5

| Deletion pass count | Case count |
| ---: | ---: |
| 0 | 0 |

### n = 6

| Deletion pass count | Case count |
| ---: | ---: |
| 3 | 8 |
| 4 | 34 |
| 5 | 88 |
| 6 | 26 |

### n = 7

| Deletion pass count | Case count |
| ---: | ---: |
| 4 | 4 |
| 5 | 79 |
| 6 | 304 |
| 7 | 174 |

## Stable Strict-Pair Distributions

### n = 5

| Strict pairs | Stable labeled cases |
| ---: | ---: |
| 0 | 0 |

### n = 6

| Strict pairs | Stable labeled cases |
| ---: | ---: |
| 6 | 1 |
| 7 | 12 |
| 8 | 13 |

### n = 7

| Strict pairs | Stable labeled cases |
| ---: | ---: |
| 9 | 10 |
| 10 | 88 |
| 11 | 66 |
| 12 | 10 |

## One-Step Comparison

- n=6 stable fraction: 13/360 (0.036)
- n=7 stable fraction: 29/840 (0.035)
- Delta n=7 minus n=6: -1/630 (-0.002)
- n=7 largest oriented class probability: 1/1260 (0.001)

## Strongest Claim

The T165 rare-tail boundary survives one exact ordinal scaling step. At n=5 every case is blocked by the T126 scale floor. At n=6, 26/720 cases survive all current screens. At n=7, 174/5040 survive, a reduced fraction of 29/840, and those labels collapse to 86 oriented finite-poset classes or 45 order-dual classes.

## What This Improved

T167 replaces the open 'try n=7' suggestion with an exact bounded scaling audit. It checks the same T126, T156, parent-interval, single-deletion, and finite-poset isomorphism stages at n=5, n=6, and n=7, so the six-event result is no longer a one-size-only comparison.

## What This Weakened Or Falsified

This weakens two premature readings at once. The stable T54 tail does not vanish at n=7, so T165 was not merely a six-event accident. But it also does not become typical: the stable fraction slightly decreases from 13/360 to 29/840, and the largest n=7 oriented class has probability only 1/1260.

## Falsification Condition

T167 fails if the ordinal S_n ensemble is not the intended exact finite model for no-tie 1+1 interval samples, if the n=6 result does not reproduce T165, if the n=7 audit changes any screen relative to T126/T156/T159, or if one-step scaling is described as a continuum-limit or generative-law result.

## S1 Update

S1 remains open_formal_target. The T54 survivor tail persists from n=6 to n=7 under the declared exact ordinal comparison, but only as a rare finite tail requiring a generative mechanism, larger-n scaling law, embedding theorem, or continuum bridge.

## Claim Ledger Update

Add T167 to S1: exact ordinal scaling gives n=5 scale-blocked, n=6 stable fraction 13/360, and n=7 stable fraction 29/840 with 86 oriented survivor classes and largest class probability 1/1260. Treat this as one-step persistence of a rare finite tail, not as spacetime evidence.

## Open Blocker

No T54 generative law, asymptotic scaling theorem, natural measure over finality colimits, faithful embedding theorem, Lorentzian metric reconstruction, covariance result, or continuum bridge explains why the rare tail should be physically selected.

## Suggested Next

Do not repeat small-n counting alone. Either derive a T54 generative measure that predicts the rare tail, add an efficient sampling/asymptotic argument for n>=8, or switch to a different S1 bridge such as embedding/covariance/metric reconstruction.

## Not Claimed

T167 does not establish a continuum limit, random sprinkling law, faithful embedding, Lorentzian metric reconstruction, covariance, GR, QFT, or a generative spacetime mechanism. It only runs exact finite ordinal rank-permutation ensembles through the existing T54/T126/T156/T159 screens at n=5, n=6, and n=7.
