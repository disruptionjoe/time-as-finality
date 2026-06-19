# T49 Results: Reconstruction Without Background Time

**Date:** 2026-06-18
**Model:** `models/reconstruction_without_background_time.py`
**Runner:** `models/run_t49.py`
**Output:** `results/reconstruction-without-background-time-v0.1.json`

---

## Axis Profiles

| Event | causal | info | obs_access | branch |
|-------|--------|------|------------|--------|
| e1_A_locking | 2 | 2 | 1 | 0 |
| e2_B_locking | 1 | 3 | 1 | 0 |
| e3_composite_locking | 3 | 4 | 1 | 0 |

Magnitudes are extracted from the D1Profile of each event's post-finality
(target) system. No temporal variable appears in this extraction.

**e1 vs e2 are Pareto-incomparable on (causal, info):** e1 has higher causal
(2 > 1) but lower info (2 < 3). Neither dominates the other componentwise.
This is the formal basis for their incomparability in the partial order.

---

## Order Comparisons

### 2-axis magnitude order: (causal, info)

e_j ≤_2 e_i iff causal_j ≤ causal_i AND info_j ≤ info_i

| Pair (e_j, e_i) | record order | 2-axis | match |
|-----------------|-------------|--------|-------|
| (e1, e1) | True | True | ✓ |
| (e1, e2) | False | False (2 ≤ 1 fails) | ✓ |
| (e1, e3) | True | True (2≤3, 2≤4) | ✓ |
| (e2, e1) | False | False (3 ≤ 2 fails) | ✓ |
| (e2, e2) | True | True | ✓ |
| (e2, e3) | True | True (1≤3, 3≤4) | ✓ |
| (e3, e1) | False | False (3 ≤ 2 fails) | ✓ |
| (e3, e2) | False | False (3 ≤ 1 fails) | ✓ |
| (e3, e3) | True | True | ✓ |

**Match: 9/9 (exact match: True)**

The 2-axis componentwise order exactly reproduces the T48 record-dependency
partial order. Causal and information finality axes alone reconstruct the
temporal ordering structure, with no background time variable.

### 3-axis order: (causal, info, obs_access)

All T48 target systems have obs_access = 1. Adding this axis adds no
new constraints: e_j ≤_3 e_i iff e_j ≤_2 e_i AND 1 ≤ 1 (always true).

**Match: 9/9 (exact match: True)**. The e1/e2 incomparability persists
because obs_access is degenerate (equal across all events) in this witness.
This confirms: the incomparability is not resolved by adding observer-access
finality — it is structurally genuine.

### 4-axis order: (causal, info, obs_access, branch)

All T48 target systems also have branch = 0. Same analysis applies.

**Match: 9/9 (exact match: True)**. Incomparability persists under
full 4-axis extension.

---

## Topological Sorts

Valid total orderings (linear extensions) of the record-dependency partial order:

| Sort | Valid |
|------|-------|
| [e1, e2, e3] | True — e1 < e3 ✓, e2 < e3 ✓, e1 || e2 (no constraint) ✓ |
| [e2, e1, e3] | True — e2 < e3 ✓, e1 < e3 ✓, e2 || e1 (no constraint) ✓ |
| [e1, e3, e2] | False — e2 < e3 requires e3 after e2, violated |
| [e2, e3, e1] | False — e1 < e3 requires e3 after e1, violated |
| [e3, e1, e2] | False — e3 comes last (has predecessors e1 and e2) |
| [e3, e2, e1] | False — same |

**Total valid sorts: 2**

Ambiguity = 2! = 2 interleavings of the incomparable root pair {e1, e2}.
These two sorts correspond to the two valid temporal orderings consistent
with all record dependencies: one in which A-locking precedes B-locking,
and one in which B-locking precedes A-locking. Both are consistent with
the record structure because neither event's locked records appear in the
other's source system.

---

## Anti-Scalar Theorem

**Statement:** No total preorder — including any positive scalar utility
function f: Events → ℝ — can replicate a partial order with incomparable
elements.

**Proof:** A total preorder satisfies totality: for all e_j, e_i, either
e_j ≤ e_i or e_i ≤ e_j (or both). The record-dependency partial order is
NOT total: e1 and e2 satisfy neither e1 ≤ e2 nor e2 ≤ e1.

Therefore no total preorder can agree with the record-dependency order on
the pair (e1, e2). QED.

**Consequence:** A single global time coordinate (a total order on all events)
cannot exist for any FinaliEvent Structure containing incomparable events.
When spacelike-separated finality crossings exist — events whose locked
records do not appear in each other's source systems — the temporal order
is irreducibly partial.

**For the T49 witness:** e1 and e2 are Pareto-incomparable on (causal, info).
No positive linear combination of these axes can make them incomparable
(a linear combination gives a total order). Therefore the 2-axis
componentwise order (which correctly identifies them as incomparable) is
the appropriate order, not any scalar derived from those axes.

---

## No Time Input Confirmation

The T49 reconstruction uses these definitions, in order:

1. **D1Profile** (from `multiscale_observer_field.py`): four integer fields
   (accessible_support, holder_redundancy, branch_support, reversal_cost).
   No temporal variable.

2. **AxisProfile** (T49 layer): extracts four integers from D1Profile.
   No temporal variable.

3. **`_magnitude_leq(e_j, e_i, axes)`**: compares integers field by field.
   No temporal variable.

4. **`_build_magnitude_order`**: applies `_magnitude_leq` to all pairs.
   No temporal variable.

5. **`_all_topological_sorts`**: permutation enumeration with partial order
   consistency check. No temporal variable.

Temporal ordering (topological sort) is an **output** of step 5. It does
not appear in steps 1–4. The reconstruction is non-circular.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
|------------|-------|--------|
| H_MAGNITUDE_MATCH | 2-axis (causal, info) order matches record-dependency order exactly | **supported** |
| H_TOPO_AMBIGUITY | Valid topological sort count = 2 (one per root-event interleaving) | **supported** |
| H_ANTI_SCALAR | No scalar utility replicates a partial order with incomparable elements | **supported** |
| H_NO_TIME_INPUT | Reconstruction uses no temporal variable | **supported** |

**Best supported:** all four hypotheses hold.

---

## Connections to Prior Results

**T48 (FinaliEvent Structure):** T49 takes T48's partial order as input.
The 2-axis magnitude order and the record-containment order agree exactly
on this witness. The two approaches — axis comparison and record containment
— are provably equivalent for the T48 systems.

**T47 (PO1 DAG Theorem):** T47 proved that PO1-admissible morphisms form an
acyclic bipartite graph. T49 provides the axis-magnitude content of that
graph's direction: events with strictly higher (causal, info) values come
later. The graph direction is not postulated — it follows from axis profiles.

**H7 (Finality-Induced Direction):** T49 is the reconstruction side of H7.
Temporal direction is derived from axis magnitudes; it is not an input.
The anti-scalar theorem explains why this direction is irreducibly partial:
spacelike-separated events cannot be globally ordered by any scalar.

**H1 (Record Reconstruction):** T49 confirms H1 for the T48 witness: temporal
order is reconstructed from record dependencies (encoded in axis magnitudes)
with no background time variable. The two valid topological sorts are the
full set of consistent temporal orderings — the partial order does not
under-determine them further.

---

## Boundary

- Three events. The match result is a finite witness, not a general theorem.
  A FinaliEvent Structure where the record-containment order and the
  2-axis magnitude order diverge would refute H_MAGNITUDE_MATCH.

- The 3- and 4-axis extensions are degenerate in this witness (obs_access=1,
  branch=0 for all targets). A witness with variation in these axes is needed
  to test whether observer-access or environmental finality resolves
  incomparability that causal/info alone cannot.

- The anti-scalar theorem is general (definitional). The magnitude-match
  result is specific to this witness. The conjunction (partial order +
  exact axis match) is what T49 contributes.

- T49 does not prove that the 2-axis magnitude order is the UNIQUE function
  of axis magnitudes that reproduces the record-dependency order.
  Other componentwise functions might also match. Characterizing the class
  of order-preserving functions is deferred to T50.
