# T525 Results: Repaired S1 Manifoldlikeness Suite

## Verdict

- Verdict: `repaired_s1_suite_no_current_finite_colimit_survivor`
- Random controls pass repaired suite: `True`
- Hard negative controls rejected: `True`
- Current finite colimit survivors: 0

## Calibration Bands

| n | samples | ordering min | ordering max | height | width | largest interval | order-dim count |
| ---: | ---: | ---: | ---: | --- | --- | --- | ---: |
| 7 | 8 | 2/7 (0.2857) | 16/21 (0.7619) | 3..5 | 3..4 | 1..4 | 1 |
| 8 | 8 | 1/4 (0.2500) | 5/7 (0.7143) | 3..6 | 3..5 | 1..5 | 1 |
| 9 | 8 | 1/4 (0.2500) | 3/4 (0.7500) | 3..6 | 3..6 | 1..6 | 1 |
| 12 | 8 | 7/22 (0.3182) | 43/66 (0.6515) | 3..6 | 4..7 | 2..8 | 4 |
| 16 | 8 | 17/60 (0.2833) | 79/120 (0.6583) | 4..7 | 4..9 | 3..12 | 8 |
| 20 | 8 | 53/190 (0.2789) | 21/38 (0.5526) | 4..9 | 5..10 | 5..15 | 8 |

## Candidate Audits

| candidate | group | n | T126 class | orderdim quarantined | frac | height | width | max interval | repaired verdict | reason |
| --- | --- | ---: | --- | :---: | ---: | ---: | ---: | ---: | --- | --- |
| `random_1p1_sprinkle_n8_seed0` | `random_sprinkle_control` | 8 | `order_dimension_obstruction` | True | 17/28 (0.6071) | 4 | 3 | 4 | `passes_repaired_suite` | profile-spread/order-dimension leg quarantined; calibrated statistics pass |
| `random_1p1_sprinkle_n12_seed0` | `random_sprinkle_control` | 12 | `order_dimension_obstruction` | True | 19/33 (0.5758) | 5 | 4 | 6 | `passes_repaired_suite` | profile-spread/order-dimension leg quarantined; calibrated statistics pass |
| `random_1p1_sprinkle_n16_seed0` | `random_sprinkle_control` | 16 | `order_dimension_obstruction` | True | 61/120 (0.5083) | 6 | 5 | 8 | `passes_repaired_suite` | profile-spread/order-dimension leg quarantined; calibrated statistics pass |
| `random_1p1_sprinkle_n20_seed0` | `random_sprinkle_control` | 20 | `order_dimension_obstruction` | True | 97/190 (0.5105) | 6 | 6 | 11 | `passes_repaired_suite` | profile-spread/order-dimension leg quarantined; calibrated statistics pass |
| `t249_grid_colimit` | `current_finite_colimit` | 9 | `passes_filter_only` | False | 3/4 (0.7500) | 5 | 3 | 7 | `fails_repaired_suite` | largest_interval_outside_random_band |
| `t252_ordinal_band_control` | `current_finite_colimit` | 9 | `passes_filter_only` | False | 5/9 (0.5556) | 5 | 2 | 3 | `fails_repaired_suite` | width_outside_random_band |
| `hub_order_control` | `hard_negative_control` | 8 | `hub_nonlocality_obstruction` | False | 1/4 (0.2500) | 2 | 7 | 0 | `fails_repaired_suite` | hard T126 gate rejected: hub_nonlocality_obstruction |
| `complete_bipartite_layer_control` | `hard_negative_control` | 8 | `interval_profile_obstruction` | False | 4/7 (0.5714) | 2 | 4 | 0 | `fails_repaired_suite` | hard T126 gate rejected: interval_profile_obstruction |
| `degenerate_chain_control` | `hard_negative_control` | 7 | `rank_width_obstruction` | False | 1/1 (1.0000) | 7 | 1 | 5 | `fails_repaired_suite` | hard T126 gate rejected: rank_width_obstruction |
| `synthetic_3x3_grid_control` | `current_finite_colimit` | 9 | `passes_filter_only` | False | 3/4 (0.7500) | 5 | 3 | 7 | `fails_repaired_suite` | largest_interval_outside_random_band |

## Strongest Claim

A repaired finite S1 suite can pass true random 1+1 controls while rejecting the current finite colimit witnesses. T249's grid is outside the calibrated interval-abundance envelope, and T252's selected ordinal witness is outside the calibrated width envelope.

## What This Improved

T525 removes the known T126 profile-spread artifact from the wall set and replaces it with explicit random-control calibration. This keeps the S1 closure honest: current witnesses still fail, but not because genuine random sprinkles are punished for fluctuating.

## What This Rescoped

This rescopes T223/T126 language away from the bad `order_dimension_obstruction` leg while preserving the practical S1 conclusion: no current finite finality colimit survives a repaired finite manifoldlikeness screen.

## Falsification Condition

T525 fails if seeded random controls do not pass the repaired suite, if hard negative controls pass, if the T249/T252 verdicts are not computed against event-count-matched calibration bands, or if the finite repaired screen is promoted into a continuum theorem.

## S1 Update

S1 remains `requires_added_assumption`. T525 strengthens the diagnostic basis for that status after T524: the known bad leg is quarantined, but no current finite colimit survives the repaired suite. The live paths remain an independent measure law, a separate formal entry point, or a continuum/embedding bridge.

## Claim Ledger Update

Record T525 as S1 claim-history only: repaired finite diagnostic suite, no current finite colimit survivor, no S1 promotion, and no T223 reversal. Add T525 to the S1 test list and sync the S1 claim file.

## Open Blocker

No finality-native measure, locality law, abundance theorem, embedding theorem, covariance result, Lorentzian metric reconstruction, or continuum bridge selects a repaired-suite survivor.

## Suggested Next

Either build an independent generative measure that produces repaired-suite survivors without tail tuning, or leave the finite S1 colimit route closed and move to a separate formal entry point.

## Not Claimed

T525 does not derive spacetime, prove manifoldlikeness, estimate continuum dimension, establish a random-sprinkling law, reconstruct a Lorentzian metric, prove locality/covariance, derive GR/QFT, or promote S1. It is a finite repaired diagnostic suite calibrated on seeded controls.
