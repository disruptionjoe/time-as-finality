# T51: Multi-Observer Apparent Finality Colimit

## Target Claims

- [H1: Record Reconstruction](../HYPOTHESES.md)
- [T48: FinaliEvent Structure](T48-finali-event-structure.md)
- [T50: Axis Monotonicity Theorem](T50-axis-monotonicity-theorem.md)
- [explorations/apparent-vs-event-finality-v0.1.md](../explorations/apparent-vs-event-finality-v0.1.md)

## Central Question

When two observers have different bounded record access and each constructs
an apparent FinaliEvent Structure, does their colimit (the merged event-finality
structure over the union of their record bases) produce a consistent partial
order — and does bounded access create phantom incomparabilities (events that
appear unordered to a bounded observer but are actually ordered in the colimit)?

## Setup

Reuse the T48 events (e1_A_locking, e2_B_locking, e3_composite_locking) with
the same D1 systems. Assign two different record-basis views of the same
underlying systems:

**Observer A (full access):**
- U3_composite_source.records = {r_A_locked, r_B_locked, r_composite_raw}
- Apparent order: e1 ≤ e3 (r_A_locked ⊆ U3.records), e2 ≤ e3 (r_B_locked ⊆ U3.records)
- Same as the T48 partial order.

**Observer B (restricted access):**
- U3_composite_source.records = {r_B_locked, r_composite_raw} — missing r_A_locked
- Direct containment check for e1 ≤ e3: O1.records = {r_A_locked} ⊆ {r_B_locked, r_composite_raw}? NO.
- Apparent order: e2 ≤ e3 only; e1 and e3 appear incomparable.
- Observer B cannot detect that e1 precedes e3.

**Physical interpretation:** Observer B cannot access r_A_locked in U3's source
records — perhaps it is outside their causal boundary, beyond a horizon, or
not yet propagated to their accessible region. From B's bounded perspective,
the A-locking event produced a record that does not appear in the composite
event's source. B sees e1 and e3 as "spacelike separated" — a phantom.

**Colimit (event finality):**
- Merge record bases: U3.records = {r_A_locked} | {r_B_locked, r_composite_raw}
  = {r_A_locked, r_B_locked, r_composite_raw} (restored to full)
- Colimit order: e1 ≤ e3 is recovered (r_A_locked now in merged U3.records)
- Colimit = T48 partial order (Observer A already had the full structure)

## The Theorem Structure

**Colimit Existence:** The colimit of two apparent FinaliEvent Structures
S_A and S_B (over the union of their record bases) is a valid partial order
whenever both S_A and S_B are valid partial orders and the underlying events
are PO1-admissible.

Reason: PO1 admissibility + T47 acyclicity prevents record cycles
(O_j.records ⊆ U_i.records AND O_i.records ⊆ U_j.records for distinct i,j),
which is the only route to an antisymmetry violation in the colimit.

**Phantom Incomparability:** An observer with restricted record access may
assign "incomparable" to a pair (e_j, e_i) that is ordered in the colimit.
This is not an error in the observer's reasoning — it is correct given their
accessible records. It is a genuine limitation of bounded causal access.

**Colimit Extension:** The colimit may strictly extend each observer's apparent
structure by recovering orderings that require combining record bases. No
observer alone can reconstruct the full event finality order if their record
access is bounded.

## Hypotheses Evaluated

- H_COLIMIT_CONSISTENT: The colimit of S_A and S_B is a valid partial order
  (reflexive, antisymmetric, transitive). No antisymmetry violation arises from
  merging the two record bases.

- H_PHANTOM_INCOMPARABILITY: Observer B's apparent order reports e1_A_locking
  and e3_composite_locking as incomparable. The colimit reveals e1 ≤ e3.
  Bounded record access creates a phantom incomparability.

- H_COLIMIT_EXTENDS: The colimit strictly extends Observer B's apparent order.
  At least one ordering (e1 ≤ e3) appears in the colimit but not in S_B.

## Success Criteria

1. Colimit partial order axioms: reflexive=True, antisymmetric=True, transitive=True.
2. Observer B apparent order: e2 ≤ e3 only; (e1, e3) incomparable.
3. Colimit order includes e1 ≤ e3 (recovered from merged U3.records).
4. New orderings in colimit not in S_B: exactly {(e1_A_locking, e3_composite_locking)}.
5. Phantom incomparability confirmed: Observer B reports || but colimit says ≤.
6. Observer A has no phantom incomparabilities (A already has full access).
7. T47 consistency: colimit is antisymmetric (no PO1-admissible record cycle possible).

## Failure Criteria

1. Colimit is not a partial order (antisymmetry violation).
   (Would require a record cycle — ruled out by T47 for PO1-admissible events.
   If this occurs, T47 or the record-basis design contains an error.)

2. Observer B's apparent order already includes e1 ≤ e3.
   (Would mean the restriction of U3.records to remove r_A_locked was not applied
   correctly. The phantom incomparability would not be demonstrated.)

3. Colimit does not recover e1 ≤ e3.
   (Would mean the merge of record bases does not restore the lost relation —
   the colimit construction is flawed or the restriction does not target the
   right record.)

4. Colimit = S_B (no extension).
   (Would mean the colimit adds nothing — either S_A = S_B (bases are identical)
   or S_A's additional records have no effect on the computed order.)

## Known Constraints

- Two observers on the same three events. The phantom incomparability is exactly
  one pair: (e1, e3). A richer witness with more events and more observers could
  produce multiple phantom pairs and test whether colimit construction is
  associative (colimit of colimits = colimit of all).

- Observer B's restriction is the minimal restriction that loses exactly one
  direct dependency. Other restriction patterns (removing r_B_locked instead,
  or removing both) are not tested in T51.

- The colimit here is the pointwise union of record sets, which equals Observer
  A's full basis. A more interesting witness would have two observers with
  complementary partial access (neither seeing the full picture) whose colimit
  is strictly richer than either. That requires a 4-event structure and is
  deferred to T52.

- T51 confirms the apparent/event finality distinction is not vacuous:
  bounded access can lose real orderings. It does not yet characterize when
  convergence of apparent finality structures to event finality is guaranteed
  (the "colimit stability" question).

## Connection to Prior Results

- T48: T51 reuses T48's FinaliEvent Structure. The T48 partial order is the
  event-finality reference for this witness — what a fully-informed observer
  (Observer A) reconstructs. T51 probes what a bounded observer (Observer B)
  loses.

- T50: AM holds on both apparent structures and on the colimit. T51 does not
  break AM — it demonstrates that AM can hold locally (for each observer) while
  the apparent orders differ. The colimit inherits AM from Observer A's full basis.

- T47: T47's acyclicity guarantee is the reason the colimit is always consistent
  for PO1-admissible events. T51 makes this connection explicit: colimit
  consistency is T47 restated at the multi-observer level.

- Exploration (apparent-vs-event-finality): T51 is the first runnable test
  of the apparent/event finality distinction. It confirms the distinction is
  non-vacuous (apparent ≠ event for Observer B) and that event finality is
  recoverable as a colimit.
