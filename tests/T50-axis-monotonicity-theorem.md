# T50: Axis Monotonicity Theorem

## Target Claims

- [H1: Record Reconstruction](../HYPOTHESES.md)
- [T48: FinaliEvent Structure](T48-finali-event-structure.md)
- [T49: Reconstruction Without Background Time](T49-reconstruction-without-background-time.md)

## Central Question

Under what conditions does finality-axis dominance (componentwise ordering
on axis magnitudes) exactly match the record-dependency order of a
FinaliEvent Structure?

## The Theorem

**Axis Monotonicity (AM):** A FinaliEvent Structure (E, ≤_rec, profiles)
satisfies AM with respect to axes A iff for all distinct e_j, e_i in E:

    e_j ≤_rec e_i  ←→  for all a in A: magnitude_a(e_j) ≤ magnitude_a(e_i)

Forward  (→): if e_j ≤_rec e_i, then e_j dominates e_i on every A axis.
Backward (←): if e_j dominates e_i on every A axis, then e_j ≤_rec e_i.

**Sufficiency Theorem:** If (E, ≤_rec, profiles) satisfies AM w.r.t. A,
then the A-axis magnitude order is identical to ≤_rec.

Proof: AM says the two relations coincide on every distinct pair.
Reflexive pairs match trivially. Therefore the relations are identical.

## Four Tests

### 1. Sufficiency

Apply the AM check to the T48 witness (e1, e2, e3) with axes = (causal, info).

Expected: AM holds (0 violations). By the Sufficiency Theorem, 2-axis
magnitude order = record order. (Already confirmed by T49: 9/9 pairs match.)

### 2. Counterexample

Construct a violating witness by replacing e3 with e3_violating:
  - Source: U3 (unchanged from T48, records = {r_A_locked, r_B_locked, r_composite_raw})
  - Target: O3_violating with D1Profile(..., reversal_cost=1)
    - reversal_cost=1 < O1.reversal_cost=2 (causal axis reversed)

Record containment still holds: O1.records ⊆ U3.records → e1 ≤_rec e3_viol.
But: causal(e1)=2 > causal(e3_viol)=1 → NOT e1 ≤_mag e3_viol.

Expected: AM violated on pair (e1, e3_viol): MISSING violation.
Reconstruction fails: magnitude order is incompatible with record order
at this pair.

This proves AM is a genuine mathematical condition, not a definitional
tautology: it can be violated by a real system.

### 3. Axis Necessity

On the T48 witness, test reconstruction with one axis at a time:

Causal only (e1:causal=2, e2:causal=1, e3:causal=3):
  - e2 ≤_causal e1 (1 ≤ 2) — SPURIOUS; record order has e1 || e2
  - Causal alone is insufficient.

Info only (e1:info=2, e2:info=3, e3:info=4):
  - e1 ≤_info e2 (2 ≤ 3) — SPURIOUS; record order has e1 || e2
  - Info alone is insufficient.

2-axis (causal + info):
  - e1 || e2 correctly (Pareto incomparable: 2>1 but 2<3)
  - Exact match: 6/6 non-reflexive pairs correct.

Expected: both single-axis tests fail with exactly 1 spurious pair each.
The 2-axis combination is the minimal sufficient basis.

### 4. Anti-Scalar Corollary

Derive scalar-time impossibility as a consequence of AM + incomparability:

  (1) AM holds on T48 witness.
  (2) Sufficiency Theorem: magnitude order = record order.
  (3) Record order has incomparable pair (e1, e2).
  (4) T49 Anti-Scalar Theorem: no total preorder can match a partial
      order with incomparable elements.
  (5) Therefore no scalar f: Events → R can reproduce the record order.

Expected: corollary holds (AM=True, incomparable pairs exist).

## Hypotheses Evaluated

- H_AM_SUFFICIENCY: AM holds on T48 witness; 2-axis order matches record
  order exactly (0 violations, 6/6 pairs).

- H_AM_VIOLATION: AM fails on violating witness; exactly 1 MISSING violation
  at pair (e1, e3_violating); reconstruction diverges.

- H_AXIS_NECESSITY: Causal alone introduces spurious pair (e2, e1);
  info alone introduces spurious pair (e1, e2); 2-axis combination
  introduces no spurious pairs.

- H_ANTI_SCALAR_COROLLARY: AM + incomparability implies no scalar time
  coordinate can reproduce the record-dependency order.

## Success Criteria

1. T48 witness passes AM check: 0 violations on 6 non-reflexive pairs.
2. Violating witness fails AM check: exactly 1 MISSING violation at (e1, e3_viol).
3. Counterexample e3_violating is PO1-admissible (it is a valid FinaliEvent).
4. Causal-only test: 5/6 match, 1 spurious pair = (e2, e1).
5. Info-only test: 5/6 match, 1 spurious pair = (e1, e2).
6. 2-axis test: 6/6 match, 0 spurious, 0 missing.
7. Anti-scalar corollary confirmed: AM=True, incomparable pairs exist.

## Failure Criteria

1. T48 witness fails AM check.
   (Would mean T49's reconstruction was not an instance of AM — a structural
   inconsistency in the framework.)

2. Violating witness passes AM check.
   (Would mean the axis reversal is not detectable by AM — the counterexample
   is not a real violation, and AM is weaker than claimed.)

3. The counterexample event e3_violating fails PO1 admissibility.
   (Would mean the counterexample is not a legitimate FinaliEvent, invalidating
   the witness.)

4. Causal-only or info-only gives 6/6 match.
   (Would refute axis necessity — a single axis suffices, and the 2-axis
   claim is not the minimal basis.)

5. Anti-scalar corollary fails: AM holds but no incomparable pairs exist.
   (Would mean the T48 structure is totally ordered under AM — contradicting
   T48's H_INCOMPARABLE result.)

## Known Constraints

- Three events from T48, plus one new violating event. The counterexample
  shows that AM can fail; it does not characterize all failure modes.

- The counterexample constructs a single MISSING violation: record order
  has e1 ≤ e3_viol but magnitude order does not. A SPURIOUS violation
  (magnitude says ≤ but record does not) would require a structure where
  axis domination exists without record containment. This is a different
  failure mode not explored in T50.

- AM is stated for a fixed axis set A. The theorem does not specify which
  axes are necessary — this is addressed by the axis necessity test.
  A complete characterization of the minimal necessary axis set for
  general FinaliEvent Structures is deferred to future work.

- The sufficiency proof is by definition: if AM holds, the orders are
  identical by the AM condition itself. The non-trivial content is showing
  that AM can hold (T48 witness) and can fail (counterexample) — i.e.,
  it is a genuine mathematical condition on the structure, not a vacuous one.

## Connection to Prior Results

- T48: AM is the formal condition explaining WHY the T48 witness has a
  reconstructible partial order. T48 built the witness; T50 names the
  condition that makes reconstruction work.

- T49: T49 confirmed 9/9 pair match (equivalently: 0 AM violations on
  all pairs including reflexive). T50 restricts to 6 non-reflexive pairs
  (same result) and adds the counterexample and necessity tests.

- H1 (Record Reconstruction): AM is the reconstruction condition for H1.
  H1's target theorem is: "given suitable finality-axis profiles (i.e.,
  profiles satisfying AM), observer-relative temporal order is reconstructible
  as a partial order." T50 proves "suitable" = satisfies AM.
