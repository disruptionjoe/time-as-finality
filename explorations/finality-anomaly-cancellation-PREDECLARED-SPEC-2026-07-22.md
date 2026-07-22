---
title: "PREDECLARED SPEC: finite reflection-anomaly gate for finality"
status: frozen_before_implementation
doc_type: predeclared_specification
created: 2026-07-22
lane: "1"
track: "TaF-2 prediction, with family F6 available to the bounded TaF-1 reflector check"
claim_effect: none
compute_effect: none
---

# PREDECLARED SPEC: finite reflection-anomaly gate for finality

## Decision this specification freezes

This is the TaF-2 specification-only swing requested by the 2026-07-22
strategic reprioritization. It asks whether a finite 1+1-dimensional lattice
fixture can distinguish a genuine reflection-carried obstruction from a
renamed distinct-holder threshold.

No anomaly is computed here. No Geometric Unity identification is assumed.
Implementation must return one of the declared outcomes without changing the
fixture, coefficient group, controls, or thresholds after seeing results.

## Construction fork

The load-bearing object has two constructions:

1. `record construction`: T111-style distinct-holder redundancy and its
   relabeling/access-boundary transformation law;
2. `field-theory construction`: a reflection/Pin+ background coupled to a
   finite U(1) lattice fermion operator and tested by a Nielsen-Ninomiya-style
   obstruction.

They are not identified by name or analogy. The experiment passes only if an
explicit bridge maps the record construction into the field-theory
coefficient before scoring. If that bridge cannot be stated without using the
desired finality verdict, the result is
`blocked_missing_non_circular_charge_bridge`.

## Frozen finite fixture

- spacetime: a periodic 1+1-dimensional square lattice with spatial sizes
  `L in {4, 6, 8}` and equal Euclidean time extent;
- gauge data: U(1) link variables restricted to the two fixed-data sectors
  `flux = 0` and `flux = 1`;
- reflection data: one declared spatial reflection with background
  `a in Z2`, evaluated for `a = 0` and the single reflection-twisted sector
  `a = 1`;
- record data: one record orbit per spatial site and a holder-incidence matrix
  with independent-holder counts `h in {1, 2, 3}`;
- access profile: fixed across the primary comparison; access-boundary changes
  are a separate covariance control, never gauge transformations;
- coefficient group: `Z2` only. No alternative modulus may be introduced in
  this experiment.

The implementation must freeze a source-backed finite lattice operator before
evaluating any record sector. It must state whether it uses a naive, Wilson,
overlap/Ginsparg-Wilson, or another construction and why. If no construction
supports the declared reflection/Pin+ transformation and a computable finite
obstruction, the result is `blocked_missing_anomaly_operator`. A convenient
operator may not be chosen because it produces the desired split.

## Frozen record charge and bridge burden

The record-side candidate is the Z2 parity of the T111-invariant
distinct-holder count,

```text
q_F(r) = h(r) mod 2.
```

This choice is deliberately exposed to a threshold-restatement kill: D1's
under-finalized/finalized split is `h < 2` versus `h >= 2`, so the `h = 3`
sector prevents parity from automatically copying that threshold.

The implementation must define, before scoring, an explicit map from `q_F`
and the reflection background `a` to one finite obstruction coefficient
`A_F in Z2`. It must show that `A_F` is invariant under pure holder and record
relabeling and state its covariant behavior under access-boundary change. T111
is only the entry check; it is not the coefficient.

## Frozen comparison table

The primary cells are the Cartesian product

```text
L in {4, 6, 8}
flux in {0, 1}
a in {0, 1}
h in {1, 2, 3}
```

Each cell records the operator construction, zero-mode or spectral-flow data
used by that construction, `q_F`, `A_F`, the D1 threshold verdict, and whether
the bridge was defined without target labels.

## Required hostile controls

1. Pure relabeling: permute holder and record names. `A_F` must not change.
2. Access covariance: change the accessible holder boundary while preserving
   the underlying incidence data. Report covariance; do not quotient it as
   gauge.
3. Fixed-data separation: hold all U(1), reflection, and lattice data fixed
   while comparing `h = 1, 2, 3`.
4. Threshold-restatement: compare `h = 1` with `h = 3`. They share odd parity
   but lie on opposite sides of the D1 threshold. A coefficient that merely
   copies threshold labels fails.
5. Reflection removal: set `a = 0`. A claimed reflection-carried obstruction
   must disappear or have its surviving non-reflection source identified.
6. Flux removal: set `flux = 0`. Any mixed U(1)/reflection reading must respond
   according to the frozen operator construction.
7. Broken incidence: supply a holder map that is not an admissible record
   bundle map. The coefficient must be undefined, not favorable.
8. Degeneracy: duplicate a decoupled record/holder pair. A result driven only
   by raw multiplicity is classified as absorbed.

## Predeclared outcomes

- `finite_reflection_coefficient_nontrivial`: a nonzero `A_F` is defined
  without target labels, survives relabeling, has the declared access
  covariance, responds to reflection removal, and is not a D1 threshold
  restatement.
- `threshold_restatement_only`: the coefficient is determined by the declared
  D1 threshold or fails the `h = 1` versus `h = 3` control.
- `fixed_data_absorbs_effect`: holder-sector changes do not alter the
  obstruction after U(1), reflection, and lattice data are fixed.
- `not_reflection_carried`: the effect survives `a = 0` without a separately
  declared source.
- `not_gauge_well_typed`: pure relabeling changes the coefficient or broken
  incidence is scored as valid.
- `blocked_missing_non_circular_charge_bridge`: no target-independent map from
  record charge to the field-theory coefficient is available.
- `blocked_missing_anomaly_operator`: no source-backed finite operator supports
  the declared computation.
- `inconclusive_finite_size`: `L = 4, 6, 8` do not agree and no other verdict
  fires.

## Acceptance and kill rules

A positive finite result requires the first outcome in all three lattice
sizes. Any earlier kill outcome ends the experiment without retuning. The
implementation may correct a coding defect, but it may not alter `Z2`, the
fixture grid, `q_F`, or the controls after results exist.

Even a positive result is finite-fixture evidence only. It does not establish
a QFT anomaly, anomaly matching theorem, Pin+ classification, IR spectrum
theorem, classical-objectivity protection, universal arrow of time, or the GU
Y14 identification. The GU sigma/w1 receptacle is an external proposal-grade
input and is not a dependency or validation source.

## Next implementation boundary

The next run may create a bounded test/model/results triplet only after it
freezes the source-backed operator construction in the test document. No heavy
computation is authorized by this specification. TaF-1 may use the resulting
coefficient family as reflector family F6 only after the experiment produces a
non-killed result; F4 remains the independent knob-free anchor.
