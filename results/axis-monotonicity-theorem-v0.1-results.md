# T50 Results: Axis Monotonicity Theorem

**Date:** 2026-06-18
**Model:** `models/axis_monotonicity_theorem.py`
**Runner:** `models/run_t50.py`
**Output:** `results/axis-monotonicity-theorem-v0.1.json`

---

## Theorem Statement

**Axis Monotonicity (AM):** A FinaliEvent Structure (E, ≤_rec, profiles)
satisfies AM with respect to axes A iff for all distinct e_j, e_i in E:

    e_j ≤_rec e_i  ←→  for all a in A: magnitude_a(e_j) ≤ magnitude_a(e_i)

**Sufficiency Theorem:** If (E, ≤_rec, profiles) satisfies AM w.r.t. A,
then the A-axis magnitude order is identical to ≤_rec.

Proof: AM says the two relations coincide on every distinct pair.
Reflexive pairs match trivially. Therefore the relations are identical. □

---

## Test 1: Sufficiency — AM Check on T48 Normal Witness

Axes: (causal, info). Events: e1_A_locking, e2_B_locking, e3_composite_locking.

Axis profiles (from target system D1Profiles):

| Event | causal (reversal_cost) | info (holder_redundancy) |
|-------|----------------------|------------------------|
| e1_A_locking | 2 | 2 |
| e2_B_locking | 1 | 3 |
| e3_composite_locking | 3 | 4 |

Non-reflexive pair results (6 pairs):

| Pair (e_j, e_i) | record order | magnitude order | AM satisfied |
|-----------------|-------------|-----------------|-------------|
| (e1, e2) | False | False (2>1 on causal) | ✓ |
| (e1, e3) | True | True (2≤3, 2≤4) | ✓ |
| (e2, e1) | False | False (3>2 on info) | ✓ |
| (e2, e3) | True | True (1≤3, 3≤4) | ✓ |
| (e3, e1) | False | False (3>2 on causal) | ✓ |
| (e3, e2) | False | False (3>1 on causal) | ✓ |

**AM holds: True. Violations: 0. Pairs checked: 6.**

By the Sufficiency Theorem, the 2-axis magnitude order is identical to the
record-dependency order on this witness.

---

## Test 2: Counterexample — Minimal AM Violation

**Design:** Replace e3 with e3_violating (U3 → O3_violating), where
O3_violating has D1Profile(accessible_support=1, holder_redundancy=4,
branch_support=0, reversal_cost=1).

- Record containment preserved: O1.records = {r_A_locked} ⊆ U3.records →
  e1 ≤_rec e3_violating (U3 is unchanged from T48).
- Axis reversal: causal(e3_viol) = 1 < causal(e1) = 2 →
  NOT e1 ≤_mag e3_viol on causal axis.

Axis profiles for violating witness:

| Event | causal | info |
|-------|--------|------|
| e1_A_locking | 2 | 2 |
| e2_B_locking | 1 | 3 |
| e3_violating | 1 | 4 |

**AM check result:**

- AM holds: False
- Violations: 1 (MISSING)
- Pair (e1_A_locking, e3_violating): record=True, magnitude=False

The record order has e1 ≤ e3_viol (by record containment), but the magnitude
order does not (causal axis reversed). AM is violated at this pair.

**Significance:** This proves AM is a genuine mathematical condition. It can
be satisfied (T48 witness) and violated (this counterexample). It is not a
tautology. The counterexample event e3_violating is PO1-admissible: it is a
valid FinaliEvent in a parity-conflict triangle (same-same-different patch
pattern), satisfying all seven PO1 admissibility conditions.

---

## Test 3: Axis Necessity

On the T48 witness, comparing single-axis reconstructions against 2-axis:

### Causal only (e1:causal=2, e2:causal=1, e3:causal=3)

| Pair (e_j, e_i) | record order | causal-only order | match |
|-----------------|-------------|------------------|-------|
| (e1, e2) | False | False (2>1) | ✓ |
| (e1, e3) | True | True (2≤3) | ✓ |
| (e2, e1) | False | **True (1≤2)** | ✗ SPURIOUS |
| (e2, e3) | True | True (1≤3) | ✓ |
| (e3, e1) | False | False (3>2) | ✓ |
| (e3, e2) | False | False (3>1) | ✓ |

**Match: 5/6. Spurious pair: (e2_B_locking, e1_A_locking).**

Causal alone forces e2 ≤ e1 (because e2.causal=1 ≤ e1.causal=2), but the
record order has e1 || e2 (incomparable). Causal is insufficient.

### Info only (e1:info=2, e2:info=3, e3:info=4)

| Pair (e_j, e_i) | record order | info-only order | match |
|-----------------|-------------|-----------------|-------|
| (e1, e2) | False | **True (2≤3)** | ✗ SPURIOUS |
| (e1, e3) | True | True (2≤4) | ✓ |
| (e2, e1) | False | False (3>2) | ✓ |
| (e2, e3) | True | True (3≤4) | ✓ |
| (e3, e1) | False | False (4>2) | ✓ |
| (e3, e2) | False | False (4>3) | ✓ |

**Match: 5/6. Spurious pair: (e1_A_locking, e2_B_locking).**

Info alone forces e1 ≤ e2 (because e1.info=2 ≤ e2.info=3), but the record
order has e1 || e2. Info is insufficient.

### 2-axis (causal + info)

The Pareto incomparability of e1 and e2 — e1 has higher causal (2>1) but lower
info (2<3) — correctly identifies them as incomparable under componentwise order.
Neither axis alone can do this; both are required.

**Match: 6/6. Exact match: True. Spurious: 0. Missing: 0.**

**Conclusion:** {causal, info} is the minimal sufficient basis for the T48
witness. Neither axis alone is sufficient. Their combination is.

---

## Test 4: Anti-Scalar Corollary

*Derived from AM + Sufficiency + T49 Anti-Scalar Theorem.*

1. AM holds on T48 witness (Test 1).
2. Sufficiency Theorem: AM → magnitude order = record order.
3. Record order has incomparable pair: (e1_A_locking, e2_B_locking).
4. Therefore magnitude order has incomparable elements.
5. T49 Anti-Scalar Theorem: no total preorder can replicate a partial order
   with incomparable elements (proof: totality requires e_j ≤ e_i or e_i ≤ e_j
   for all pairs; this pair satisfies neither).
6. Therefore no scalar f: Events → R can reproduce the record order.

**Corollary holds: True.**

Scalar time is ruled out by incomparability, not by model complexity.
Any FinaliEvent Structure satisfying AM with incomparable events lacks a
single global time coordinate — not because the model is too complex, but
because the structure is genuinely partial.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
|------------|-------|--------|
| H_AM_SUFFICIENCY | AM holds on T48 witness; 2-axis order matches record order exactly | **supported** |
| H_AM_VIOLATION | AM fails on violating witness; exactly 1 MISSING violation | **supported** |
| H_AXIS_NECESSITY | Causal alone and info alone each introduce exactly 1 spurious pair | **supported** |
| H_ANTI_SCALAR_COROLLARY | AM + incomparability implies no scalar reproduces the order | **supported** |

**Best supported:** all four hypotheses hold.

---

## What T50 Proves

T50 establishes four results from one theorem:

1. **Reconstruction condition:** AM is the exact condition under which
   finality-axis dominance equals record-dependency order. The T48 witness
   satisfies it; reconstruction is not a coincidence — it follows from AM.

2. **Failure mode:** AM can fail when axis magnitudes do not covary monotonically
   with record containment. The minimal failure is a single-pair MISSING violation
   (record has e_j ≤ e_i but magnitude order does not). This failure is
   constructible using only PO1-admissible events.

3. **Axis necessity:** Two axes are necessary for the T48 witness. No single
   axis reconstructs the partial order; each introduces a spurious ordering
   on the (e1, e2) pair. Minimality of the basis is confirmed.

4. **Scalar impossibility:** AM + incomparability → no scalar time. This is
   the formal statement that temporal order is irreducibly partial when spacelike-
   separated events exist (events incomparable in the FinaliEvent Structure).

---

## Connection to Prior Results

**T48 (FinaliEvent Structure):** T48 built the witness. T50 names the condition
(AM) explaining why reconstruction worked in T49 for that witness. T48's
incomparable pair (e1, e2) is the structural fact that makes the Anti-Scalar
Corollary non-trivial.

**T49 (Reconstruction Without Background Time):** T49 confirmed 9/9 pair match
(equivalently: 0 AM violations on all pairs including reflexive). T50 restricts
to 6 non-reflexive pairs, adds the counterexample and necessity tests, and
names the general condition. T50's Anti-Scalar Corollary subsumes T49's
Anti-Scalar Theorem for AM-satisfying structures.

**H1 (Record Reconstruction):** AM is the reconstruction condition for H1.
"Suitable finality-axis profiles" in H1's target theorem means "profiles
satisfying AM." T50 proves that AM is the right condition: necessary (the
violation shows reconstruction fails without it) and sufficient (the Sufficiency
Theorem).

**T47 (PO1 DAG Theorem):** Axis magnitudes are properties of the post-finality
(obstructed) systems in T47's bipartite DAG. AM says the DAG's direction
is detectable from magnitude monotonicity. T47 proved the DAG is acyclic;
AM characterizes when the DAG's order is axis-readable.

---

## Boundary

- Three events in the normal witness; four in the violating witness. AM is a
  general condition, but the necessity result (minimality of {causal, info})
  is specific to this witness. A witness with different axis profiles may require
  additional axes or permit fewer.

- Only MISSING violations are demonstrated. A SPURIOUS violation (magnitude says
  e_j ≤ e_i but record order does not) would require axis domination without
  record containment. This failure mode is consistent with AM's definition but
  not explored in T50.

- The Sufficiency Theorem is definitional: AM is stated as "orders coincide,"
  so if AM holds, they coincide. The non-trivial content is that AM is satisfiable
  (T48 witness) and violable (counterexample) — i.e., it is a real constraint,
  not a vacuous one.

- A complete characterization of the minimal necessary axis set for general
  FinaliEvent Structures — beyond the 3-event T48 witness — is deferred to
  future work.
