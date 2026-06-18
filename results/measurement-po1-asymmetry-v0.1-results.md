# T45 Results: Measurement PO1 Asymmetry

**Date:** 2026-06-18
**Model:** `models/measurement_po1_asymmetry.py`
**Runner:** `models/run_t45.py`
**Output:** `results/measurement-po1-asymmetry-v0.1.json`

---

## System Properties

| System | Sites | Obstruction | Global Witnesses |
|--------|-------|-------------|-----------------|
| quantum_layer_Y | q1, q2, q3 | False | 2 |
| classical_layer_X | c1, c2, c3 | True | 0 |

Y has 2 global witnesses: the all-same assignments (a=b=c=1) and (a=b=c=-1)
both satisfy the three coherence patches. X has 0 global witnesses: the
parity-conflict patches (same-same-different over a triangle) are individually
satisfiable but have no joint global assignment.

---

## Forward Morphism f: Y -> X (Measurement)

| Condition | Result |
|-----------|--------|
| AC1 richer_valid | True |
| AC2 restricted_valid | True |
| AC3 projection_definable | True |
| AC4 local_compat | True |
| AC5 structure_forgotten | True |
| AC6 restricted_obstructed | True |
| AC7 richer_unobstructed | True |
| **Verdict** | **fully_admissible** |
| **PO1 evidence** | **True** |

Measurement Y -> X is a fully admissible PO1 instance. All seven conditions
hold. The forgotten structure (quantum coherence, superposition, phase
information, entanglement) is non-empty and the projection genuinely loses
local profile data (quantum reversal_cost=3, classical reversal_cost=1).

---

## Inverse Morphism g: X -> Y (Attempted Unmeasurement)

| Condition | Result |
|-----------|--------|
| AC1 richer_valid | True |
| AC2 restricted_valid | True |
| AC3 projection_definable | True |
| AC4 local_compat | True |
| AC5 structure_forgotten | True |
| AC6 restricted_obstructed | False |
| AC7 richer_unobstructed | False |
| **Verdict** | **non_admissible_shared_obstruction** |
| **PO1 evidence** | **False** |

The inverse fails at AC6 and AC7 simultaneously:
- AC7 fails: X (the source/richer system for g) is obstructed. PO1 requires the
  richer system to be unobstructed.
- AC6 fails: Y (the target/restricted system for g) is unobstructed. PO1
  requires the restricted system to be obstructed.

Both failures are structural, not incidental. They follow from the definition
of X and Y: AC7 fails because X is obstructed (it has no global section);
AC6 fails because Y is not obstructed (it has 2 global sections).

---

## General Asymmetry Tests

| Test | Target | AC7 | Verdict | Asymmetry |
|------|--------|-----|---------|-----------|
| X -> trivial_unobstructed_Z | trivial 2-site system, no patches | False | boundary_non_definable | CONFIRMED |
| X -> another_obstructed_Z2 | 3-site parity-conflict system | False | non_admissible_shared_obstruction | CONFIRMED |

Both tests confirm AC7=False. When X is the source (richer system), AC7 fails
regardless of the target because X is obstructed.

Note on the trivial_Z case: AC3 also fails (the site map is partial -- X has
3 sites, Z has 2, so the site_map covers only 2 of 3 source sites). The verdict
is "boundary_non_definable" (AC3 priority) rather than "shared_obstruction" (AC7
priority). AC7 is still False -- the asymmetry theorem is confirmed independently
of the AC3 failure. The partial site map is a separate structural issue; the
theorem does not depend on it.

---

## Asymmetry Theorem

**Measurement Asymmetry Theorem (T45):**

For any D1RestrictionSystem S with obstruction_detected = True, there is no
PO1-admissible morphism g: S -> Z for any D1RestrictionSystem Z.

**Proof sketch:**
AC7 requires the richer system (= source of g = S) to be unobstructed.
S is obstructed by hypothesis. Therefore AC7 fails for any target Z.
The failure is independent of Z: it depends only on S being obstructed.
Verified by finite witness: all tested targets Z fail AC7 in this model.

**Corollary (Measurement Irreversibility):**
If f: Y -> X is fully PO1-admissible, then X is obstructed (by AC6 of f).
No PO1-admissible morphism can originate from X.
Measurement is irreversible in the PO1 structural sense.

The irreversibility is not an assumption. It is a consequence of:
1. PO1 requiring AC6 (target obstructed) for any forward morphism, and
2. The same obstruction then failing AC7 (source must be unobstructed) for
   any reverse morphism.

---

## Measurement Interpretation

The classical layer X is globally obstructed: its local records cannot be
jointly assigned in a globally consistent way. This is the measurement problem
expressed as a gluing obstruction. The obstruction is created by the projection
f: Y -> X -- it is not present in Y.

The PO1 structural result says: once this obstruction exists in X, no PO1
morphism can carry the structure back to any other system. The arrow of
measurement is one-directional not by physical assumption but by the
admissibility conditions of PO1.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
|------------|-------|--------|
| H_FWD | f: Y -> X is fully PO1-admissible | **supported** |
| H_INV | g: X -> Y is PO1-admissible | **refuted** |
| H_ASYM | No PO1-admissible g: X -> Z exists for any Z | **supported** |

**Best supported:** H_FWD and H_ASYM.

---

## Boundary

- The model constructs specific finite systems Y and X. The theorem is proved
  by AC7-failure logic, which is general; the finite witness confirms the logic
  but does not extend it to infinite or continuous systems.

- The gluing obstruction in X is the parity-conflict pattern from T27/T29.
  This is structurally clean but is one instance of obstruction, not a
  characterization of all obstructions that could model classical measurement.

- The measurement interpretation (Y = quantum layer, X = classical layer)
  is an analogy. T45 establishes a structural result about PO1 morphisms; the
  claim that physical measurement instantiates this structure is a separate
  question not addressed by this model.

- The dimensionality of Y or X is not derived. The model uses 3 sites for both.
  Whether a physically realistic quantum layer requires higher-dimensional
  structure is outside the scope of T45.
