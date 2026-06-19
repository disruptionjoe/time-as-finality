# T49: Reconstruction Without Background Time

## Target Claims

- [H1: Record Reconstruction](../HYPOTHESES.md)
- [T48: FinaliEvent Structure](T48-finali-event-structure.md)
- [T47: PO1 DAG Theorem](T47-po1-dag-theorem.md)

## Central Question

Can the partial order on FinaliEvents (from T48) be reconstructed from
finality axis magnitudes alone, without presupposing a background time
variable? And when incomparable events exist, can any scalar utility function
(a single global time coordinate) replicate the partial order?

## Definitions

**AxisProfile:** The finality axis magnitudes of a FinaliEvent, extracted from
the D1Profile of the post-finality (target) system:
  - `causal` = reversal_cost (causal finality)
  - `info` = holder_redundancy (information finality)
  - `obs_access` = accessible_support (observer-access finality)
  - `branch` = branch_support (environmental/branch finality)

**k-axis magnitude order:** e_j ≤_k e_i iff, for every selected axis,
the magnitude of e_j ≤ the magnitude of e_i. This is the componentwise
(Pareto dominance) partial order on R^k.

**Topological sort:** A total ordering of events consistent with the
record-dependency partial order. A linear extension.

**Reconstruction:** The claim that the k-axis magnitude order matches the
record-dependency partial order exactly — all ordered pairs agree.

## Setup

Inputs: the three T48 FinaliEvents and their record-dependency partial order.

Axis profiles (computed from target D1Profiles):

| Event | causal | info | obs_access | branch |
|-------|--------|------|------------|--------|
| e1_A_locking (U1->O1) | 2 | 2 | 1 | 0 |
| e2_B_locking (U2->O2) | 1 | 3 | 1 | 0 |
| e3_composite_locking (U3->O3) | 3 | 4 | 1 | 0 |

Record-dependency partial order (from T48): {(e1,e1),(e2,e2),(e3,e3),(e1,e3),(e2,e3)}.

## Hypotheses Evaluated

- H_MAGNITUDE_MATCH: The 2-axis (causal, info) componentwise partial order
  matches the record-dependency partial order from T48 exactly (all 9
  ordered pairs among 3 events agree).

- H_TOPO_AMBIGUITY: The valid topological sort count equals the number of
  interleavings of incomparable root events. For T48's witness: exactly 2
  valid sorts (one per ordering of the incomparable pair {e1, e2}).

- H_ANTI_SCALAR: No total preorder (including any scalar utility function
  over finality axis magnitudes) can replicate a partial order with
  incomparable elements. Proof is formal (definitional), not empirical.

- H_NO_TIME_INPUT: The reconstruction — from axis magnitudes to partial
  order to valid topological sorts — uses no temporal variable. Temporal
  ordering is an output, not an input.

## Success Criteria

1. The 2-axis magnitude order produces exactly the same 5 pairs as the
   T48 record-dependency order (9/9 ordered pairs match).
2. The 3-axis and 4-axis orders (adding obs_access and branch) also match —
   confirming the 2-axis match is not accidental over-fitting.
3. Exactly 2 valid topological sorts exist: {e1,e2,e3} and {e2,e1,e3}.
4. The incomparable pair {e1,e2} is the same in the record order and the
   2-axis magnitude order.
5. The anti-scalar theorem holds: at least one incomparable pair exists,
   so no total preorder can replicate the partial order.
6. No temporal variable appears in any definition used by the reconstruction.

## Failure Criteria

1. The 2-axis order disagrees with the record order for any pair.
   (Would mean the causal and info axes are insufficient to reconstruct
   the record-dependency structure.)

2. More than 2 valid topological sorts exist.
   (Would mean there is additional incomparability not captured by the
   partial order — the structure is looser than expected.)

3. Exactly 1 valid topological sort exists.
   (Would mean the partial order is actually total — e1 and e2 are not
   genuinely incomparable. Would contradict T48's incomparability result.)

4. The anti-scalar theorem fails — every pair is comparable.
   (Would mean the partial order is total and a single global time
   coordinate exists, contradicting T48.)

5. A temporal variable is found in any reconstruction definition.
   (Would mean the reconstruction is circular.)

## Known Constraints

- Three events from T48. The match between 2-axis order and record order
  is a finite witness result; it holds here but is not a general theorem
  for all FinaliEvent Structures.

- The 3-axis and 4-axis extensions provide no additional resolution in
  this witness because all T48 target systems have obs_access=1, branch=0.
  These axes are degenerate for this witness. A witness with varying
  obs_access would be needed to test whether observer-access finality
  resolves incomparability that causal/info cannot.

- The anti-scalar theorem is definitional, not contingent on specific
  axis values. It holds for any partial order with incomparable elements.

- T49 does not prove UNIQUENESS of axis-based reconstruction in general:
  a different record-basis assignment could yield a different record order
  that the 2-axis magnitude order fails to match. Uniqueness characterization
  is deferred to T50.

## Connections to Prior Results

- T48: T49 takes T48's partial order as its input. The match result shows
  that T48's record-containment definition and the 2-axis magnitude order
  are equivalent on this witness — structural alignment between the two
  approaches to finality ordering.

- T47 (PO1 DAG Theorem): T47 proved that PO1-admissible morphisms form a
  DAG. T49 provides the semantic content of that DAG: the axis magnitudes
  that justify the DAG's direction. High-causal AND high-info events come
  after low-causal AND low-info events in the partial order.

- H7 (Finality-Induced Direction): T49 gives the reconstruction side of H7.
  Direction is not postulated; it is recovered from axis magnitudes. The
  anti-scalar theorem explains why this direction is irreducibly partial
  (not a total order) when spacelike-separated finality crossings exist.

- H1 (Record Reconstruction): T49 is the first direct test of H1's core
  claim within the T48/T49 framework. H1 asks whether temporal order can
  be reconstructed from record dependencies. T49 shows: yes, for the T48
  witness, using only two finality axis magnitudes and no background time.
