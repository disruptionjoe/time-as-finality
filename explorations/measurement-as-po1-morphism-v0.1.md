# Measurement as PO1 Morphism

**Status:** Exploration note. No claim update.
**Date:** 2026-06-18
**Prompted by:** Open question from prior conceptual discussions: what would make
the X^4 / Y^n geometric picture a proper repo artifact?

---

## The Geometric Picture

Two layers of the universe are accessible to the formalism:

**X** (classical layer): the space of finalized, stable records. Standard Model
behavior describes how records interact within this layer. D1 finality is
well-defined here. Classical spacetime structure lives here.

**Y** (quantum layer): the space of pre-finality states. Superposition,
entanglement, and phase coherence are present. No stable D1 records yet exist.
Y is richer in structure than X but does not contain finalized records.

**Measurement** is the event that maps Y -> X. Information is lost in the
projection: quantum coherence, phase relationships, and entanglement do not
survive the mapping to a classical record. The forgotten structure is named and
non-trivial.

---

## The PO1 Mapping

If measurement is modeled as a D1RestrictionMorphism f: Y -> X, the PO1
admissibility conditions (AC1-AC7) have natural interpretations:

| Condition | PO1 Requirement | Measurement Interpretation |
|-----------|-----------------|---------------------------|
| AC1 | Y valid D1RestrictionSystem | quantum state is a well-formed object |
| AC2 | X valid D1RestrictionSystem | classical record is a well-formed object |
| AC3 | site map is total | every quantum degree of freedom maps to some classical site |
| AC4 | X locally satisfiable | each local measurement outcome is individually possible |
| AC5 | f forgets named structure | coherence, phase, entanglement are genuinely lost |
| AC6 | X is globally obstructed | no global classical section consistent with all measurement outcomes simultaneously |
| AC7 | Y is globally unobstructed | the quantum state has a global section (is a coherent whole) |

AC6 is the most structurally significant: the classical record system X is
globally obstructed. This is not a defect of the model -- it is the measurement
problem stated in PO1 terms. Measurement creates a globally obstructed classical
layer out of a globally satisfiable quantum layer.

---

## The Structural Claim

**Measurement Asymmetry (candidate Theorem T45):**

For any D1RestrictionSystem S with obstruction_detected = True, there is no
PO1-admissible morphism g: S -> Z for any D1RestrictionSystem Z.

Proof sketch: A PO1-admissible g: S -> Z requires AC7 (richer system S is
unobstructed). But S is obstructed. AC7 fails for any Z.

Corollary: If f: Y -> X is fully PO1-admissible (so AC6 holds: X is obstructed),
then no PO1-admissible morphism can originate from X. Measurement is irreversible
in the PO1 structural sense -- not by assumption, but as a consequence of the
admissibility conditions.

---

## What This Explains

- **Why measurement is irreversible**: once the classical layer X is reached,
  AC7 fails for any reverse morphism. The asymmetry is structural, not postulated.

- **Why faster-than-light signaling is impossible in this picture**: any signal
  must be carried by a finalized record in X. Records propagate at finite rates
  within X. Quantum correlations live in Y and cannot be extracted as signals
  without a measurement morphism f: Y -> X.

- **Why the Standard Model is complete at its layer**: Standard Model degrees
  of freedom live in X. The forgotten structure (coherence, phase) is genuinely
  absent from X, not hidden. It was forgotten in the projection.

---

## What This Leaves Open

- Why Y is any particular dimensionality. The repo makes no claim about this.
  The dimension count is an empirical matter that lies outside the formalism.

- What structures inside Y are preserved by f. AC5 names the forgotten
  structure. The preserved structure (e.g., reversal_cost, distinguishable
  outcomes) is whatever the morphism declares. The formalism does not derive
  which dimensions survive.

- Whether Y itself is obstructed in some other sense. The model treats Y as
  globally satisfiable (AC7). Whether this is accurate for all quantum states
  is left open.

- Whether X^4 (4D classical spacetime) is derivable from X as a D1 structure.
  H5 (Spacetime Aggregation) addresses this separately; it is not claimed here.

---

## Falsification Conditions

This picture fails if:

1. The forward morphism f: Y -> X cannot be constructed as a fully PO1-admissible
   case. (T45 tests this directly.)

2. A PO1-admissible inverse morphism g: X -> Y can be constructed. (T45 tests
   this directly; if it succeeds, measurement irreversibility is not structural.)

3. The obstruction in X can be shown to be trivially constructable from any
   pair of systems, with no structural content. (Would undermine the
   measurement-problem reading of AC6.)

---

## Connection to Existing Results

- **T27/T28/T29**: established that PO1 morphisms exist with non-trivial
  gluing obstructions in the restricted system.

- **T31**: confirmed that the quantum-layer mapping would satisfy AC1-AC7
  provided the constructions are valid -- the structural conditions are not
  new, only the interpretation is.

- **T34 (PO1 Chain Theorem)**: endpoint admissibility is independent of
  intermediate admissibility. The chain structure of measurement events
  follows from T34: multiple measurement steps can compose without each
  being PO1-admissible individually.

- **T41 (D1Cat Theorem)**: PO1 is not a functor on D1Cat. The non-functor
  result means PO1 admissibility is a property of specific endpoint morphisms,
  not a preserved invariant. This supports the view that measurement events
  are discrete events, not continuous flows.

---

## Next Step

T45: build the finite model and run the asymmetry check. The test either
confirms the claim (forward admissible, inverse not) or produces a
counterexample (inverse admissible, asymmetry fails).

See [T45](../tests/T45-measurement-po1-asymmetry.md).
