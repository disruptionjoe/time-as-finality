# T223: T54 Ordinal Scaling Decisive Verdict

## Route

Spacetime reconstruction.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T159: T54 Interval-Jackknife Screen](T159-t54-interval-jackknife-screen.md)
- [T164: T54 Survivor Isomorphism And Locality Audit](T164-t54-survivor-isomorphism-locality.md)
- [T165: T54 Survivor Sprinkling Stress Test](T165-t54-survivor-sprinkling-stress.md)
- [T167: T54 Ordinal Scaling Stress Test](T167-t54-ordinal-scaling-stress.md)

## Question

Decisive advance-or-kill: when the exact 1+1 ordinal rank-permutation ensemble
is extended one more full step to `n=8`, does the band-and-deletion-stable T54
finality-colimit survivor family stop being a thin decaying rare tail (an
advance for S1), or does the rare tail strictly continue to decay while every
survivor stays a thin height-bounded poset and the typical ensemble member is
rejected (a finite no-go: manifoldlikeness is unreachable from the finite
finality-colimit ensemble without an added assumption)?

## Motivation

T165 and T167 left S1 in a stable but unresolved position. The band survivors
persist from `n=6` to `n=7` but do not grow: `26/720` then `174/5040`, with the
survivor family always thin height-3 posets whose largest Alexandrov interval
has at most one interior event. Each prior step (T156, T157, T159, T163, T164,
T165, T167) added one more rare-tail control without issuing a verdict.

T223 is the decisive scale-up demanded by the S1 open problem. It does not
accrete another control. It runs the identical T126/T156/T159/isomorphism
pipeline used by T167 on the exact `n=8` ordinal ensemble (`40320` cases) and
applies a fixed advance-or-kill rubric to the full `n=6, 7, 8` trajectory.

## Setup

For `n` generic points in a flat 1+1 causal diamond with no light-cone
coordinate ties, sorting by one coordinate leaves the other coordinate's rank as
a uniform element of `S_n`. T223 uses that exact finite ordinal ensemble at
`n=5, 6, 7, 8`, identically to T167's `n=5..7` model.

Each case is completed through the T54 quotient-union pipeline and screened with:

```text
T126 finite causal-set filter
T156 flat 1+1 ordering-fraction band
T159 parent-interval support (largest Alexandrov interval interior <= 1)
T159 all single-deletion stability
finite-poset isomorphism quotient (T164 canonical key) for stable survivors
```

Two additional structural descriptors are recorded per size for the verdict:
the survivor height distribution (does the family grow taller?) and the modal
(typical) ensemble member's T126 classification (is the typical member a stable
band survivor or is it rejected?).

### Decision rubric

```text
ADVANCE  := (stable fraction NOT monotone non-increasing from n=6)
            AND (survivor family does NOT stay thin + height-bounded)

FINITE NO-GO := (stable fraction monotone non-increasing from n=6)
            AND (every survivor stays thin: max Alexandrov interval interior <= 1)
            AND (survivor height does not grow with n)
            AND (the modal/typical ensemble member is rejected as a stable band
                 survivor)
```

The no-go is a statement about the declared finite ordinal ensemble and the
declared finite screens. It is not a continuum theorem.

## Cases

1. `n=5` reproduces the T126 scale block (`0` survivors).
2. `n=6` reproduces T165/T167 exactly: `26/720` stable labels, `15` oriented
   classes, `9` order-dual classes, all height-3, thin intervals.
3. `n=7` reproduces T167 exactly: `174/5040` stable labels, `86` oriented
   classes, `45` order-dual classes, all height-3, thin intervals.
4. `n=8` is the decisive new step: fully enumerated (`40320` cases, not Monte
   Carlo), screened identically. Result: `361/40320` stable labels, `174`
   oriented classes, `90` order-dual classes, largest-class probability
   `1/10080`, all `361` survivors height-3 with thin (interior `<= 1`)
   intervals.

## Success Criteria

- `n=6` and `n=7` reproduce the established T165/T167 counts (regression guard
  that the decisive model reuses the same screens).
- `n=8` is fully enumerated through the identical pipeline.
- The advance-or-kill rubric returns a single named verdict, not a deferral.
- The verdict states explicitly what is and is not earned in spacetime
  language.
- S1 status is updated to match the verdict.

## Failure Criteria

T223 fails if:

- the `n=6` or `n=7` counts do not reproduce T165/T167;
- the `n=8` enumeration changes any screen relative to T126/T156/T159;
- the no-go is restated as a continuum no-go theorem rather than a finite,
  exact, ensemble-level result;
- a no-go or advance is described as positive or negative spacetime,
  manifoldlikeness, dimension, sprinkling, locality, embedding, covariance,
  metric, or continuum evidence beyond exactly what the screens support;
- the survivor posets are described as 1+1 causal sets rather than as members of
  a declared finite ordering-fraction band.

## Result

Status: implemented and run.

Verdict: `finite_no_go_manifoldlikeness_unreachable_without_added_assumption`.

The exact `n=8` step keeps the band-and-deletion-stable survivor a strictly
decaying rare tail. The unconditional stable-survivor fraction is monotone
non-increasing and drops sharply at the decisive size:

```text
n=6: 26/720    = 13/360    ~= 0.0361
n=7: 174/5040  = 29/840    ~= 0.0345
n=8: 361/40320 = 361/40320 ~= 0.0090   (a ~3.8x drop from n=7)
```

Every stable survivor at every size stays a thin height-3 poset whose largest
Alexandrov interval has at most one interior event (`361/361` survivors at `n=8`
are height-3 with parent interval interior `<= 1`). The typical ensemble member
is rejected as a stable band survivor: the modal `n=8` T126 classification is
`passes_filter_only` (`2837/3360 ~= 0.844` of the ensemble), i.e. over-ordered
relative to the declared 1+1 band rather than a stable survivor. The `361`
stable labels reduce to `174` oriented finite-poset classes (`90` order-dual
classes), and the largest oriented survivor class has probability `1/10080` at
`n=8`, down from `1/1260` at `n=7`.

(The conditional-after-parent survival rate is `1/6`, `58/187`, `361/2057` at
`n=6,7,8`; it is reported for transparency but is not a rarity measure and does
not gate the verdict, since it is normalized by the parent-interval filter.)

The finite finality-colimit ensemble therefore does not concentrate on
manifoldlike causal sets through `n=8`: the share of band-and-deletion-stable
survivors decreases at every step, dropping nearly four-fold at the decisive
size, and the survivors stay structurally thin. On this finite ensemble and
these finite screens, manifoldlikeness is not reached without an added
continuum, sprinkling, or selection assumption.

### What is earned

An exact finite enumeration result and a finite, ensemble-level no-go: the
uniform 1+1 ordinal finality-colimit ensemble does not yield a robust
manifoldlike survivor family through `n=8`; the band survivors are a thin
decaying rare tail.

### What is NOT earned (either direction)

No spacetime derivation. No manifoldlikeness, dimension, or Myrheim-Meyer
dimension estimate (the ordering-fraction band is an audit setting, not a
dimension measurement). No sprinkling, locality, embedding, covariance,
Lorentzian metric, GR, QFT, or continuum-limit claim, positive or negative. The
no-go is about the finite ensemble and the finite screens only; it does not
assert that no continuum construction with added structure could ever produce
spacetime. The survivor posets are not asserted to be 1+1 causal sets; they only
lie inside a declared finite ordering-fraction band.

## Known Physics Constraints

This test derives no spacetime, Lorentzian geometry, metric structure, GR, QFT,
dimension, or continuum limit, and refutes none of those either. It exactly
enumerates a declared finite ordinal ensemble through declared finite screens
and reports whether band survivors concentrate or decay.

## Claim Impact

S1 is downgraded for the finite finality-colimit route from
`open_formal_target` to `requires_added_assumption`. The colimit-of-finality-
domains program is not killed, but it can no longer be advanced by enumerating
finite finality colimits and hoping manifoldlikeness emerges. Any S1 promotion
now requires an explicitly added measure, selection rule, sprinkling, or
continuum bridge.

## Reproduction

```bash
python -m unittest tests.test_t54_ordinal_scaling_decisive -v
TAF_RUN_T223_N8=1 python -m unittest \
  tests.test_t54_ordinal_scaling_decisive.DecisiveVerdictTests -v
python -m models.run_t223
```

## Most Important Follow-On

Is there any natural non-uniform measure on finality colimits under which the
thin band survivors carry non-vanishing weight? If no such measure is exhibited,
the finite-colimit S1 route stays at `requires_added_assumption`, because
manifoldlikeness provably does not arise from the uniform finite
finality-colimit ensemble on its own.
