# T165 Results: T54 Survivor Sprinkling Stress Test

## Exact Comparison Target

- Target: `exact_six_point_ordinal_1p1_sprinkling`
- Basis: For a flat 1+1 causal diamond in light-cone coordinates, six generic sampled points have no coordinate ties. After sorting by one coordinate, the other coordinate's rank is a uniform element of S_6, giving exactly the 720 T163 rank-pair cases.

## Aggregate Checks

- Total rank-permutation cases: 720
- T126 pass count: 578
- T156 pass count: 305
- Parent-interval pass count: 156
- Stable labeled survivors: 26
- Stable labeled survivor fraction: 13/360 (0.036)
- Oriented survivor classes: 15
- Order-dual survivor classes: 9
- Largest oriented class probability: 1/360 (0.003)
- All oriented classes below one percent: True

## Conditioning Stages

| Stage | Pass count | Unconditional fraction | Conditional fraction | Interpretation |
| --- | ---: | ---: | ---: | --- |
| T126 finite causal-set filter | 578 | 289/360 (0.803) | 289/360 (0.803) | Most ordinal 1+1 samples clear the coarse T126 filter. |
| T156 ordering-fraction band | 305 | 61/144 (0.424) | 305/578 (0.528) | The declared 1+1 ordering band removes almost half of the T126 passers. |
| T159 parent-interval support | 156 | 13/60 (0.217) | 156/305 (0.511) | Parent interval-thinness is a further strong finite conditioning step. |
| T159 all single deletions stable | 26 | 13/360 (0.036) | 1/6 (0.167) | Only a small tail remains after every single-event deletion must also pass. |

## Strict-Pair Distributions

### Full 720-Case Ensemble

| Strict pairs | Count |
| ---: | ---: |
| 0 | 1 |
| 1 | 5 |
| 2 | 14 |
| 3 | 29 |
| 4 | 49 |
| 5 | 71 |
| 6 | 90 |
| 7 | 101 |
| 8 | 101 |
| 9 | 90 |
| 10 | 71 |
| 11 | 49 |
| 12 | 29 |
| 13 | 14 |
| 14 | 5 |
| 15 | 1 |

### Stable Labeled Survivors

| Strict pairs | Count |
| ---: | ---: |
| 6 | 1 |
| 7 | 12 |
| 8 | 13 |

## Parent-Pass Deletion Stability

| Deletion pass count | Parent-pass cases |
| ---: | ---: |
| 3 | 8 |
| 4 | 34 |
| 5 | 88 |
| 6 | 26 |

## Stable Oriented Class Profiles

| Rank profile | Class count |
| --- | ---: |
| `[2, 2, 2]` | 7 |
| `[2, 3, 1]` | 3 |
| `[3, 1, 2]` | 1 |
| `[3, 2, 1]` | 4 |

| Width | Class count |
| ---: | ---: |
| 2 | 5 |
| 3 | 10 |

## Strongest Claim

The T164 survivor classes are compatible with the exact six-point ordinal 1+1 sprinkling comparison, but only as a heavily conditioned rare tail: 26 of 720 labeled rank-permutation cases survive all current screens, a fraction of 13/360. Each oriented survivor class has uniform-ensemble probability at most 1/360.

## What This Improved

T165 replaces loose 'random sprinkling' language with an exact finite comparison ensemble. It reports the unconditional and conditional narrowing caused by T126, T156, parent-interval, and single-deletion screens, plus the abundance of each T164 class.

## What This Weakened Or Falsified

This weakens any optimistic reading that the 15 T164 classes are typical small sprinkling outputs or evidence of a generative spacetime law. They are a selected 3.6 percent tail of the exact six-point ordinal ensemble, not a broad or natural continuum family by themselves.

## Falsification Condition

T165 fails if the T163 rank-pair family is not the correct exact ordinal model for six no-tie 1+1 interval samples, if the T163 and T164 pipelines disagree about stable survivors, or if rare finite abundance is described as continuum evidence rather than a new generative-law burden.

## S1 Update

S1 remains open_formal_target. The current six-event boundary is finite-compatible with an ordinal 1+1 comparison, but only after strong conditioning; it is not yet a sprinkling law or spacetime reconstruction.

## Claim Ledger Update

Add T165 to S1: the 15 oriented T164 survivor classes occupy only 26/720 labeled cases in the exact six-point ordinal 1+1 sprinkling ensemble, and no oriented class has probability above 1/360. Treat them as a rare finite tail needing a generative explanation, not as spacetime evidence.

## Open Blocker

No T54 generative law, larger-n scaling result, faithful embedding theorem, Lorentzian metric reconstruction, covariance result, or continuum bridge explains why these rare finite classes should be selected physically.

## Suggested Next

Either derive a T54 generative mechanism that predicts the rare survivor tail under a declared measure, or run the same exact ordinal comparison at n=7 with bounded computational scope.

## Not Claimed

T165 does not validate a random sprinkling law, faithful embedding, Lorentzian metric reconstruction, covariance, GR, QFT, or a continuum limit. It only compares the six-event T54 survivors against the exact finite ordinal 1+1 permutation ensemble.
