# T48 Results: FinaliEvent Structure

**Date:** 2026-06-18
**Model:** `models/finali_event_structure.py`
**Runner:** `models/run_t48.py`
**Output:** `results/finali-event-structure-v0.1.json`

---

## Events

| Event | Source | Target | PO1 | causal_magnitude | info_magnitude |
|-------|--------|--------|-----|-----------------|----------------|
| e1_A_locking | U1_source_A | O1_locked_A | True | 2 | 2 |
| e2_B_locking | U2_source_B | O2_locked_B | True | 1 | 3 |
| e3_composite_locking | U3_composite_source | O3_locked_composite | True | 3 | 4 |

All three events are PO1-admissible (all AC1-AC7 conditions satisfied).

Magnitudes are properties of the post-finality target system:
- `causal_magnitude` = `reversal_cost` (how irreversible the locked record is)
- `info_magnitude` = `holder_redundancy` (how redundantly the locked record is stored)

The composite event (e3) has the highest values on both axes: it is the most
irreversible and the most redundantly stored, consistent with it aggregating
the outputs of both e1 and e2.

---

## Record Bases

| System | Records |
|--------|---------|
| U1_source_A | r_A_coherent, r_A_raw |
| U2_source_B | r_B_coherent, r_B_raw |
| U3_composite_source | r_A_locked, r_B_locked, r_composite_raw |
| O1_locked_A | r_A_locked |
| O2_locked_B | r_B_locked |
| O3_locked_composite | r_A_locked, r_B_locked, r_composite_locked |

U3's record basis contains `r_A_locked` and `r_B_locked`: it has absorbed
the finality-crossing outputs of e1 (O1) and e2 (O2). This justifies both
direct dependencies (e1 ≤ e3 and e2 ≤ e3) by subset containment.

---

## Partial Order

**Direct dependencies (record containment):**
- e1 ≤ e3: O1.records = {r_A_locked} ⊆ U3.records = {r_A_locked, r_B_locked, r_composite_raw}
- e2 ≤ e3: O2.records = {r_B_locked} ⊆ U3.records = {r_A_locked, r_B_locked, r_composite_raw}

**No dependency between e1 and e2:**
- O1.records = {r_A_locked} ⊄ U2.records = {r_B_raw, r_B_coherent}
- O2.records = {r_B_locked} ⊄ U1.records = {r_A_raw, r_A_coherent}

**Reflexive-transitive closure (5 pairs):**

| e_j | e_i | e_j ≤ e_i |
|-----|-----|-----------|
| e1 | e1 | True (reflexive) |
| e2 | e2 | True (reflexive) |
| e3 | e3 | True (reflexive) |
| e1 | e3 | True (direct dependency) |
| e2 | e3 | True (direct dependency) |

All other ordered pairs (e3≤e1, e3≤e2, e1≤e2, e2≤e1) are False.

**Axiom verification:**
- Reflexive: True
- Antisymmetric: True (no pair (e_j,e_i) and (e_i,e_j) with e_j ≠ e_i)
- Transitive: True (no transitivity violation in the 3-event closure)
- **Is partial order: True**

---

## Hasse Diagram

```
e1 (U1->O1, causal=2, info=2)    e2 (U2->O2, causal=1, info=3)
                             \   /
                       e3 (U3->O3, causal=3, info=4)
```

**Incomparable pair:** (e1, e2) — neither precedes the other.

**Root events:** e1 and e2 — no predecessors, independent finality crossings.
Both roots are PO1-admissible. Their independence captures the structural
content of "spacelike separation": e1 and e2 can occur in any order (or
simultaneously) because neither's locked records are required by the other's
source system.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
|------------|-------|--------|
| H_PARTIAL_ORDER | Record-dependency relation is a partial order | **supported** |
| H_INCOMPARABLE | Some events are incomparable (partial, not total, order) | **supported** |
| H_ROOT_EVENTS | Root events exist and are PO1-admissible independent crossings | **supported** |
| H_NPW_COMPATIBLE | FinaliEvent Structure is compatible with NPW event structure theory | **supported** |

**Best supported:** all four hypotheses hold.

---

## Connections to Prior Results

**T47 (PO1 DAG Theorem):** FinaliEvents are exactly the PO1-admissible edges of
D1Cat (T47's bipartite DAG). T47's acyclicity theorem directly implies
antisymmetry of the record-dependency partial order: if e_j ≤ e_i and e_i ≤ e_j,
then there is a directed PO1-admissible cycle A_j → A_i → A_j in D1Cat,
contradicting T47. Antisymmetry here is not an independent fact — it is T47's
theorem applied to the record-dependency structure.

**T45 (Measurement Asymmetry):** The forward measurement morphism (Y→X, quantum
to classical) is a FinaliEvent with root-event status: its source system (Y)
contains no locked records from prior events. Later events whose source systems
contain the classical record X's locked output would be successors of e_measurement
in the FinaliEvent Structure.

**H1 (Record Reconstruction):** The FinaliEvent Structure is the formal object
H1 requires: a record-based causal structure from which a temporal ordering can
be derived without background time. Any topological sort of the partial order
is a valid temporal ordering consistent with all record dependencies. T49 will
attempt to prove uniqueness (when is the topological sort total?) and
reconstruction (can the partial order be recovered from record content alone?).

---

## NPW Event Structure Compatibility

The triple (E, ≤, #) with:
- E = {e1, e2, e3}
- ≤ = the record-dependency partial order (5 pairs)
- # = empty (all events are mutually compatible)

satisfies the Nielsen-Plotkin-Winskel (1981) event structure axioms:
1. ≤ is a partial order — verified.
2. For each event e, the set {e' | e' ≤ e} is finite — trivially, since E is finite.
3. Conflict is irreflexive and symmetric — trivially, since # = empty.
4. Conflict is inherited upward — trivially, since # = empty.

The FinaliEvent Structure is the restriction of NPW event structures to
finality-crossing morphisms of D1Cat, where the causality relation arises
from record containment rather than being postulated.

---

## Boundary

- Three events are tested. The partial order axioms are verified for this
  finite witness. The definitions are general (any PO1-admissible morphisms
  with associated record bases), but the general claim that record containment
  always yields a partial order depends on properties of the record-basis
  assignment not proven in T48.

- The record basis is a T48-layer annotation, not part of the formal
  D1RestrictionSystem. T48 claims record containment is structurally
  motivated; a future result (T49 or T50) should characterize when a
  record-basis assignment is canonical.

- Conflict (#) is not modeled: all three events are mutually compatible in
  this witness. Events encoding mutually exclusive finality crossings would
  require a conflict relation; this is deferred to future work.

- Only causal_magnitude (reversal_cost) and info_magnitude (holder_redundancy)
  are encoded as FinaliEvent axis magnitudes. The full 6-axis basis
  (causal, information, observer-access, dependency, branch, scale) is a
  direction for T49-T50; T48 stays at the minimal two-axis level.
