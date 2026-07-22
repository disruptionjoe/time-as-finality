---
title: "PREDECLARED SPEC: F4-first reversal-self-dual reflector enumeration"
status: frozen_before_results
doc_type: predeclared_specification
created: 2026-07-22
lane: "1"
track: "bounded TaF-1 own-absorber check"
claim_effect: none
compute_effect: none
---

# PREDECLARED SPEC: F4-first reversal-self-dual reflector enumeration

## Decision this freezes

Test whether order-reversal self-duality, with no free continuous coordinate knob, selects finite
orders with a 1+1-dimensional manifold-like signature or merely reproduces ordinary random-poset
structure. This is a bounded own-absorber check feeding TaF's supplier leg; it is not an open-ended
source-law search and does not assemble Dynamic Unity.

`F4` here names the Wave-1 reflector family, not Theorem F4 in
`explorations/reconstruction-failure-h0-h1-cover-structure.md`.

## Construction fork

- Native construction: labeled finite posets sampled only when an order-reversing involutive
  anti-automorphism is supplied as part of the object.
- Standard comparator: unconstrained labeled random posets at matched cardinality and relation
  density, including a Kleitman-Rothschild three-layer control.

No metric, embedding coordinate, fitted order fraction, or post-result manifold label may enter
the native construction. A result in one construction does not transfer silently to the other.

## Frozen finite panel

- Cardinalities: `n in {6, 8, 10}`.
- Primary family F4: reversal-self-dual labeled posets with fixed-point-free reversal for even `n`.
- Controls: matched unconstrained posets; matched three-layer KR posets; chains; antichains; and
  two-dimensional-order planted positives.
- Sampling: exhaustive is permitted only where tractable; otherwise use the first 256 accepted
  objects from seed `20260722`, with rejection counts reported. The sample cap may not be expanded
  after results.
- Order fraction is measured, not tuned. Report its distribution; do not condition on `OF≈1/2`.

## Frozen observables

Run the existing repaired-S1 manifold-likeness suite and Myrheim-Meyer dimension estimator without
changing thresholds. Record dimension estimate, interval abundance residuals, ordering fraction,
height/width, three-layer score, and reversal-orbit diagnostics. A missing executable definition
returns `blocked_missing_registered_observable`; it is not filled by a new favorable proxy.

## Hostile controls

1. Relabeling must preserve every isomorphism-invariant score.
2. Removing the reversal map while holding the poset fixed must remove only reversal-dependent
   quantities, not improve manifold scores by definition.
3. KR controls test under-selection by generic three-layer concentration.
4. Planted 2D orders must be recoverable by the registered suite or the panel is invalid.
5. Chains and antichains bound degenerate low-information positives.
6. Matching relation density prevents order fraction from acting as a hidden coordinate knob.

## Predeclared outcomes

- `generator_found_finite_panel`: F4 separates from both matched random and KR controls toward the
  planted-2D region at every `n`, with the registered observables agreeing.
- `self_duality_underselects`: F4 is statistically indistinguishable from, or closer to, the KR or
  unconstrained controls than the planted positives on any load-bearing observable.
- `representation_result_only`: reversal self-duality forces a finite structural identity but not
  the registered manifold-like signature.
- `blocked_missing_registered_observable`: repaired-S1/MM definitions or thresholds cannot be
  frozen from existing repository truth.
- `inconclusive_finite_panel`: controls pass but the three sizes disagree and no earlier outcome
  fires.

## Kill and non-claim boundary

Any hidden density/coordinate tuning, failed planted-positive recovery, or favorable threshold
chosen after results kills the panel. Even `generator_found_finite_panel` is finite-fixture evidence,
not a continuum theorem, physical source law, universal arrow of time, or cross-repository identity.
F2/F3 remain challengers only after F4 closes. TaF-2 may enter as F6 only after its independent gate
survives; it is not supporting evidence for this specification.

## Next boundary

The next run may locate and freeze the exact repaired-S1 and MM executable references, then either
run this finite panel without retuning or return `blocked_missing_registered_observable`. No heavy
enumeration is authorized by this specification.

