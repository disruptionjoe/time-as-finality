# T48: FinaliEvent Structure

## Target Claims

- [PO1: Projection-Obstruction Schema](../claims/PO1-projection-obstruction-schema.md)
- [H1: Record Reconstruction](../HYPOTHESES.md)
- [T47: PO1 DAG Theorem](T47-po1-dag-theorem.md)

## Central Question

Can a record-dependency partial order be defined on a set of PO1-admissible
D1RestrictionMorphisms — without presupposing temporal order — such that the
resulting structure is a well-formed partial order compatible with
Nielsen-Plotkin-Winskel event structure theory?

## Object Being Defined

**FinaliEvent**: A PO1-admissible D1RestrictionMorphism (a finality-crossing
event) annotated with two finality axis magnitudes:
  - `causal_magnitude`: reversal_cost of the post-finality target system
  - `info_magnitude`: holder_redundancy of the post-finality target system

**Record-dependency relation**: e_j directly precedes e_i iff the record basis
of e_j's post-finality (target) system is a non-empty subset of the record
basis of e_i's pre-finality (source) system.

**FinaliEvent Structure**: An unordered set of FinaliEvents equipped with the
reflexive-transitive closure of the record-dependency relation.

## Key Constraint

The partial order must be derived from record containment, NOT from a
presupposed temporal order. The word "sequence" is explicitly avoided.
The object is an unordered set plus a dependency relation; temporal
order is a projection from that structure, not an input to it.

## Setup

**Pre-finality systems (unobstructed):**
- U1: source for e1, record basis = {r_A_raw, r_A_coherent}
- U2: source for e2, record basis = {r_B_raw, r_B_coherent}
- U3: source for e3, record basis = {r_A_locked, r_B_locked, r_composite_raw}
  (U3 has absorbed the locked outputs of O1 and O2)

**Post-finality systems (obstructed):**
- O1: target for e1, record basis = {r_A_locked}
- O2: target for e2, record basis = {r_B_locked}
- O3: target for e3, record basis = {r_A_locked, r_B_locked, r_composite_locked}

**Events:**
- e1: U1 -> O1 (A-locking event)
- e2: U2 -> O2 (B-locking event)
- e3: U3 -> O3 (composite-locking event)

**Direct dependencies from record containment:**
- e1 < e3: O1.records = {r_A_locked} ⊆ U3.records
- e2 < e3: O2.records = {r_B_locked} ⊆ U3.records
- e1 || e2: O1.records ⊄ U2.records; O2.records ⊄ U1.records

**Expected partial order (5 pairs including reflexive):**
- {(e1,e1), (e2,e2), (e3,e3), (e1,e3), (e2,e3)}

**Expected Hasse diagram:**
```
e1    e2
  \  /
   e3
```

## Hypotheses Evaluated

- H_PARTIAL_ORDER: The record-dependency relation is a partial order
  (reflexive, antisymmetric, transitive).
- H_INCOMPARABLE: Some events are incomparable under the partial order
  (not all events are ordered — the structure is a partial, not total, order).
- H_ROOT_EVENTS: Root events (events with no predecessors) exist and are
  PO1-admissible independent finality crossings.
- H_NPW_COMPATIBLE: The FinaliEvent Structure satisfies the axioms of
  a Nielsen-Plotkin-Winskel (1981) event structure with empty conflict relation.

## Success Criteria

1. All three events (e1, e2, e3) are PO1-admissible.
2. Record containment identifies exactly the expected direct dependencies
   (e1<e3, e2<e3; no dependency between e1 and e2).
3. The partial order axioms hold: reflexive, antisymmetric, transitive.
4. At least one incomparable pair exists (e1 and e2 are incomparable).
5. Root events are identified (e1 and e2 have no predecessors).
6. The partial order has exactly 5 pairs: {(e1,e1), (e2,e2), (e3,e3), (e1,e3), (e2,e3)}.
7. No temporal variable appears in any definition.

## Failure Criteria

1. Any event fails PO1 admissibility.
   (Would mean the event is not a legitimate finality-crossing morphism.)

2. The record containment relation fails to be a partial order.
   (Would mean the T48 definition is not well-formed without additional constraints.)

3. Record containment produces a total order.
   (Would mean the structure is not genuinely partial — no incomparable events.
   Incomparability is required for the structure to encode spacelike separation.)

4. The order contains a cycle.
   (Would contradict T47's acyclicity theorem — a structural conflict.)

5. e1 and e2 are comparable (one precedes the other).
   (Would contradict the record containment computation: neither O1.records
   nor O2.records is a subset of the other's source.)

## Known Constraints

- Three events are tested. The definitions are general; the three events are a
  finite witness, not a complete characterization.
- The record basis is a T48 annotation, not part of the formal D1RestrictionSystem.
  T48 claims that record containment is a structural property derivable from the
  pre/post-finality systems; the finite witness confirms one instantiation.
- Conflict (#) is not modeled: all three events are mutually compatible.
  A complete NPW event structure for T48 would require a conflict relation
  to handle mutually exclusive finality crossings.
- The causal and information finality axes (causal_magnitude, info_magnitude) are
  the minimal two axes from the Mathematical Minimalist constraint. Additional axes
  (observer-access, dependency, branch, scale) are tracked separately and not
  encoded in T48's FinaliEvent magnitudes.

## Connection to Prior Results

- T47 (PO1 DAG Theorem): FinaliEvents are exactly the PO1-admissible edges of
  D1Cat (T47's DAG). T47's acyclicity theorem implies antisymmetry of the
  record-dependency order here.
- T45 (Measurement Asymmetry): The forward measurement morphism (Y->X) is a
  FinaliEvent. Its record-dependency predecessors are unobstructed preparation
  events; its successors are later measurement-dependent events.
- H1 (Record Reconstruction): The FinaliEvent Structure is the formal object
  whose topological sort would give a valid temporal ordering. T49 will attempt
  to prove that this topological sort is uniquely determined by record content
  without a background time variable.
