# T223 Results: T54 Ordinal Scaling Decisive Verdict

## Verdict

- Verdict: `finite_no_go_manifoldlikeness_unreachable_without_added_assumption`
- Basis: Stable-survivor fraction trajectory (n=5:0/1, n=6:13/360, n=7:29/840, n=8:361/40320) is monotone non-increasing from n=6. Every stable survivor at every size stays thin and height-bounded (decisive size n=8 max survivor height 3, all parent intervals interior<=1: True). At the decisive size the modal ensemble member is classified 'passes_filter_only', so the typical member is rejected by the screens.

## Exact Comparison Target

- Target: `exact_ordinal_1p1_rank_permutation_scaling_n5_to_n8`
- Basis: For n generic points in a flat 1+1 causal diamond with no light-cone coordinate ties, sorting by one coordinate leaves the other coordinate's rank as a uniform element of S_n. T223 uses that exact finite ordinal ensemble for n=5, n=6, n=7, and the decisive new step n=8, identically to T167's n=5..7 pipeline.
- Reproduces prior T165/T167 counts: True

## Size Summary

| n | Cases | T126 pass | T156 pass | Parent pass | Stable survivors | Stable fraction | Oriented classes | Dual classes | Largest class prob | Max survivor height | All thin |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :---: |
| 5 | 120 | 0 | 0 | 0 | 0 | 0/1 (0.0000) | 0 | 0 | 0/1 (0.0000) | 0 | True |
| 6 | 720 | 578 | 305 | 156 | 26 | 13/360 (0.0361) | 15 | 9 | 1/360 (0.0028) | 3 | True |
| 7 | 5040 | 4456 | 2051 | 561 | 174 | 29/840 (0.0345) | 86 | 45 | 1/1260 (0.0008) | 3 | True |
| 8 | 40320 | 34044 | 16261 | 2057 | 361 | 361/40320 (0.0090) | 174 | 90 | 1/10080 (0.0001) | 3 | True |

## Stable-Survivor Trajectory

| n | Stable fraction | Conditional-after-parent | Largest class prob |
| ---: | ---: | ---: | ---: |
| 5 | 0/1 (0.0000) | 0/1 (0.0000) | 0/1 (0.0000) |
| 6 | 13/360 (0.0361) | 1/6 (0.1667) | 1/360 (0.0028) |
| 7 | 29/840 (0.0345) | 58/187 (0.3102) | 1/1260 (0.0008) |
| 8 | 361/40320 (0.0090) | 361/2057 (0.1755) | 1/10080 (0.0001) |

## Monotone-Decay And Structure Tests

| Test | Result |
| --- | :---: |
| Stable fraction monotone non-increasing from n=6 | True |
| Conditional survival monotone non-increasing from n=6 | False |
| Survivor family stays thin + height-bounded | True |
| Typical ensemble member rejected as stable band survivor | True |

## Survivor Height Distributions

### n = 5

| Survivor height | Count |
| ---: | ---: |
| n/a | 0 |

### n = 6

| Survivor height | Count |
| ---: | ---: |
| 3 | 26 |

### n = 7

| Survivor height | Count |
| ---: | ---: |
| 3 | 174 |

### n = 8

| Survivor height | Count |
| ---: | ---: |
| 3 | 361 |


## Earned

Earned: an exact finite enumeration result. At n=8 the declared 1+1 ordinal ensemble has 361/40320 band-and-deletion-stable labeled survivors, reducing to 174 oriented finite-poset classes (90 order-dual classes), with largest oriented-class probability 1/10080. Every stable survivor is a thin height-bounded poset. Earned conclusion: on this finite ensemble and these finite screens, manifoldlikeness is not reached without an added assumption (a finite, ensemble-level no-go).

## Not Earned (Either Direction)

NOT earned, in any direction: no spacetime derivation; no manifoldlikeness, dimension, or Myrheim-Meyer dimension estimate (the ordering-fraction band is an audit setting, not a dimension measurement); no sprinkling, locality, embedding, covariance, Lorentzian metric, GR, QFT, or continuum-limit claim, positive or negative. The no-go is about the finite ensemble and the finite screens only; it does not assert that no continuum construction with added structure could ever produce spacetime. The survivor posets are not asserted to be 1+1 causal sets; they only lie inside a declared finite ordering-fraction band.

## Strongest Claim

Finite no-go (exact, ensemble-level). Extending the exact 1+1 ordinal ensemble to n=8 keeps the band-and-deletion-stable T54 survivor a strictly decaying rare tail (n=6=13/360, n=7=29/840, n=8=361/40320) of thin height-bounded posets whose largest Alexandrov interval has at most one interior event, while the typical ensemble member is rejected. The finite finality-colimit ensemble therefore does not concentrate on manifoldlike causal sets; manifoldlikeness is unreachable from this finite ensemble plus these finite screens without an added continuum, sprinkling, or selection assumption.

## What This Improved

T223 replaces the open 'one more size' suggestion with a decisive exact scaling step to n=8 and a fixed advance-or-kill rubric. The rare tail is no longer evaluated one control at a time; the monotone-decay decision and the thin-survivor structural test are computed and reported together, so the S1 lane gets a verdict rather than another deferral.

## What This Weakened Or Falsified

This closes the 'maybe it grows at the next size' escape that kept S1 at open_formal_target. The rare tail does not become typical at n=8; it decays further and stays structurally thin. The honest consequence is that the uniform finite finality-colimit ensemble is the wrong object to expect spacetime from: any S1 promotion now requires an explicitly added measure, selection, or continuum step, not more small-n counting.

## Falsification Condition

T223's no-go is falsified if at any enumerated size the band-and-deletion-stable survivor fraction increases, if a stable survivor appears whose largest Alexandrov interval has more than one interior event, if the survivor height grows with n, if the n=6 or n=7 counts fail to reproduce T165/T167 (26 and 174), or if the verdict is restated as a continuum no-go or as positive spacetime evidence rather than a finite-ensemble decision.

## S1 Update

S1 should be downgraded from open_formal_target to requires_added_assumption for the finite finality-colimit route. T223 supplies a finite, exact, ensemble-level no-go: the uniform 1+1 ordinal ensemble does not concentrate on manifoldlike causal sets through n=8, and the survivors stay a thin decaying rare tail. The colimit-of-finality-domains program is not killed, but it can no longer be advanced by enumerating finite finality colimits and hoping manifoldlikeness emerges; an explicit added measure, selection rule, sprinkling, or continuum bridge is now mandatory.

## Claim Ledger Update

Add T223 to S1 and change status. Exact ordinal scaling (n=5=0/1, n=6=13/360, n=7=29/840, n=8=361/40320) shows the band-and-deletion-stable tail strictly decays through n=8 and every survivor stays a thin height-bounded poset, while the typical member is rejected. This is a finite ensemble-level no-go: manifoldlikeness is unreachable from the finite finality-colimit ensemble without an added assumption. Downgrade S1 (finite-colimit route) to requires_added_assumption.

## Open Blocker

No natural non-uniform measure on finality colimits is known under which the thin band survivors carry non-vanishing weight, and no added selection/sprinkling/continuum bridge has been exhibited. Until one is, the finite finality-colimit ensemble cannot supply manifoldlikeness, dimension, or any spacetime-facing residue.

## Most Important Follow-On Question

Is there any natural measure on finality colimits (not the uniform ordinal ensemble) under which the thin band survivors carry non-vanishing weight? If no such measure is exhibited, S1 should be downgraded from open_formal_target to requires_added_assumption, because manifoldlikeness provably does not arise from the finite finality-colimit ensemble on its own.

## Not Claimed

T223 establishes no continuum limit, random-sprinkling law, faithful embedding, Lorentzian metric, dimension estimate, covariance, locality law, GR, or QFT result, and no positive spacetime or manifoldlikeness claim. It exactly enumerates the declared finite 1+1 ordinal rank-permutation ensemble at n=5,6,7,8 through the existing T126/T156/T159 screens and the T164 poset-isomorphism quotient, and issues an advance-or-kill verdict on the declared finite rubric only.
