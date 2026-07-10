# T524 Results: T126 Random-Sprinkle Diagnostic Repair

## Verdict

- Verdict: `t126_order_dimension_leg_confirmed_finite_regular_screen`
- Artifact confirmed: `True`
- Calibration control: `passes_filter_only` (passed=True, ordering_fraction=7/15 (0.4667))

## Comparison Target

- Target: `seeded_random_flat_1p1_lightcone_sprinkles_n8_to_n20`
- Basis: In flat 1+1 light-cone coordinates, a finite causal diamond sample orders p<q exactly when u_p<u_q and v_p<v_q. Its ordering fraction approaches the Myrheim-Meyer 1+1 target 1/2 in expectation; finite interval profiles naturally fluctuate.

## Size Summary

| n | samples | T126 pass | order_dimension reject | other reject | T156 band pass | mean ordering fraction | mean gap from 1/2 | order-dim reject rate |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | 8 | 7 | 1 | 0 | 2 | 9/16 (0.5625) | 15/112 (0.1339) | 1/8 (0.1250) |
| 12 | 8 | 4 | 4 | 0 | 5 | 93/176 (0.5284) | 17/176 (0.0966) | 1/2 (0.5000) |
| 16 | 8 | 0 | 8 | 0 | 6 | 239/480 (0.4979) | 29/480 (0.0604) | 1/1 (1.0000) |
| 20 | 8 | 0 | 8 | 0 | 7 | 75/152 (0.4934) | 39/760 (0.0513) | 1/1 (1.0000) |

## Repair Checks

| Check | Result |
| --- | :---: |
| Mean ordering-fraction gap decreases with size | True |
| Order-dimension rejection rate increases with size | True |
| All N>=16 samples rejected by order-dimension leg | True |

## Per-Sample Audit

| n | seed | ordering fraction | gap | T156 band | T126 classification | height | width |
| ---: | ---: | ---: | ---: | :---: | --- | ---: | ---: |
| 8 | 0 | 17/28 (0.6071) | 3/28 (0.1071) | False | `order_dimension_obstruction` | 4 | 3 |
| 8 | 1 | 1/2 (0.5000) | 0/1 (0.0000) | True | `passes_filter_only` | 4 | 4 |
| 8 | 2 | 9/14 (0.6429) | 1/7 (0.1429) | False | `passes_filter_only` | 4 | 4 |
| 8 | 3 | 1/4 (0.2500) | 1/4 (0.2500) | False | `passes_filter_only` | 3 | 5 |
| 8 | 4 | 19/28 (0.6786) | 5/28 (0.1786) | False | `passes_filter_only` | 6 | 3 |
| 8 | 5 | 5/7 (0.7143) | 3/14 (0.2143) | False | `passes_filter_only` | 5 | 3 |
| 8 | 6 | 13/28 (0.4643) | 1/28 (0.0357) | True | `passes_filter_only` | 3 | 4 |
| 8 | 7 | 9/14 (0.6429) | 1/7 (0.1429) | False | `passes_filter_only` | 3 | 3 |
| 12 | 0 | 19/33 (0.5758) | 5/66 (0.0758) | True | `order_dimension_obstruction` | 5 | 4 |
| 12 | 1 | 9/22 (0.4091) | 1/11 (0.0909) | True | `order_dimension_obstruction` | 5 | 5 |
| 12 | 2 | 7/11 (0.6364) | 3/22 (0.1364) | False | `order_dimension_obstruction` | 6 | 4 |
| 12 | 3 | 7/22 (0.3182) | 2/11 (0.1818) | False | `passes_filter_only` | 3 | 7 |
| 12 | 4 | 43/66 (0.6515) | 5/33 (0.1515) | False | `passes_filter_only` | 6 | 4 |
| 12 | 5 | 35/66 (0.5303) | 1/33 (0.0303) | True | `passes_filter_only` | 5 | 4 |
| 12 | 6 | 17/33 (0.5152) | 1/66 (0.0152) | True | `order_dimension_obstruction` | 6 | 5 |
| 12 | 7 | 13/22 (0.5909) | 1/11 (0.0909) | True | `passes_filter_only` | 5 | 5 |
| 16 | 0 | 61/120 (0.5083) | 1/120 (0.0083) | True | `order_dimension_obstruction` | 6 | 5 |
| 16 | 1 | 7/15 (0.4667) | 1/30 (0.0333) | True | `order_dimension_obstruction` | 6 | 5 |
| 16 | 2 | 79/120 (0.6583) | 19/120 (0.1583) | False | `order_dimension_obstruction` | 7 | 4 |
| 16 | 3 | 17/60 (0.2833) | 13/60 (0.2167) | False | `order_dimension_obstruction` | 4 | 9 |
| 16 | 4 | 11/20 (0.5500) | 1/20 (0.0500) | True | `order_dimension_obstruction` | 7 | 6 |
| 16 | 5 | 61/120 (0.5083) | 1/120 (0.0083) | True | `order_dimension_obstruction` | 7 | 5 |
| 16 | 6 | 1/2 (0.5000) | 0/1 (0.0000) | True | `order_dimension_obstruction` | 6 | 6 |
| 16 | 7 | 61/120 (0.5083) | 1/120 (0.0083) | True | `order_dimension_obstruction` | 5 | 6 |
| 20 | 0 | 97/190 (0.5105) | 1/95 (0.0105) | True | `order_dimension_obstruction` | 6 | 6 |
| 20 | 1 | 1/2 (0.5000) | 0/1 (0.0000) | True | `order_dimension_obstruction` | 8 | 5 |
| 20 | 2 | 52/95 (0.5474) | 9/190 (0.0474) | True | `order_dimension_obstruction` | 7 | 6 |
| 20 | 3 | 53/190 (0.2789) | 21/95 (0.2211) | False | `order_dimension_obstruction` | 4 | 10 |
| 20 | 4 | 21/38 (0.5526) | 1/19 (0.0526) | True | `order_dimension_obstruction` | 8 | 8 |
| 20 | 5 | 21/38 (0.5526) | 1/19 (0.0526) | True | `order_dimension_obstruction` | 9 | 6 |
| 20 | 6 | 49/95 (0.5158) | 3/190 (0.0158) | True | `order_dimension_obstruction` | 8 | 6 |
| 20 | 7 | 93/190 (0.4895) | 1/95 (0.0105) | True | `order_dimension_obstruction` | 5 | 7 |

## Strongest Claim

The seeded random 1+1 controls confirm that T126's `order_dimension_obstruction` is not a reliable manifoldlikeness falsifier. The repo's six-event flat control passes, but random 1+1 sprinkles are increasingly rejected by that leg as their mean ordering-fraction gap from 1/2 decreases.

## What This Improved

T524 upgrades the earlier deterministic calibration note into an executable RNG-ensemble repair audit. It separates the T126 causal-set gate and other obstruction legs from the profile-spread leg that mistakes random interval fluctuation for non-manifoldness.

## What This Rescoped

This rescopes any S1/T223 language that treats the T126 order-dimension leg as a genuine manifoldlikeness wall. It does not weaken the independent T223 rare-tail counting result, and it does not make current finite finality colimits manifoldlike.

## Falsification Condition

T524 fails if the seeded random controls stop approaching the declared 1+1 ordering-fraction target, if larger random sprinkles are not rejected by `order_dimension_obstruction`, if the flat six-event control no longer passes, or if the result is used to promote S1 rather than repair one diagnostic leg.

## S1 Update

S1 remains `requires_added_assumption`. T524 only says the T126 profile-spread leg must be treated as a finite-regularity screen, not as a continuum manifoldlikeness wall. Future S1 work still needs an added measure, selection rule, sprinkling law, dimension estimator, or continuum bridge.

## Claim Ledger Update

Record T524 as an S1 claim-history repair: the T126 `order_dimension_obstruction` leg is quarantined as diagnostic regularity, while T223 remains a finite-screen/finite-ensemble no-go. No S1 status movement and no claim promotion.

## Open Blocker

No repaired manifoldlikeness suite has replaced the profile-spread leg, and no current finality-colimit family has been shown to survive a robust causal-set dimension, abundance, locality, sprinkling, or continuum-limit diagnostic.

## Suggested Next

Replace the T126 profile-spread leg with a declared statistical dimension/locality diagnostic calibrated on random sprinkles, then rerun the S1 finite-colimit route only on that repaired suite.

## Not Claimed

T524 is not a manifoldlikeness proof, dimension estimate, faithful embedding theorem, random-sprinkling law, continuum limit, Lorentzian metric reconstruction, GR, QFT, or S1 promotion. It audits one T126 diagnostic leg against seeded finite random 1+1 controls.
