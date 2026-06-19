# T52 Results: Symmetric Colimit Theorem

**Date:** 2026-06-19
**Model:** `models/symmetric_colimit_theorem.py`
**Runner:** `models/run_t52.py`
**Output:** `results/symmetric-colimit-theorem-v0.1.json`

---

## Events

| Event | causal (reversal_cost) | info (holder_redundancy) | PO1-admissible |
|-------|----------------------|------------------------|----------------|
| e1_alpha_locking | 2 | 1 | True |
| e2_beta_locking | 1 | 3 | True |
| e3_gamma_locking | 4 | 2 | True |
| e4_delta_locking | 3 | 4 | True |

Axis profiles designed so the 2-axis (causal, info) componentwise order matches
the full event-finality record order exactly. All four events are PO1-admissible
(source system unobstructed, target system obstructed, morphism admissible).

---

## Record Bases

| System | Full reference | Observer A | Observer B |
|--------|---------------|------------|------------|
| U1_alpha_source | {r1_raw} | (same) | (same) |
| U2_beta_source | {r2_raw} | (same) | (same) |
| U3_gamma_source | {r1_locked, r3_raw} | (same) | **{r3_raw}** |
| U4_delta_source | {r1_locked, r2_locked, r4_raw} | **{r2_locked, r4_raw}** | (same) |
| O1_alpha_locked | {r1_locked} | (same) | (same) |
| O2_beta_locked | {r2_locked} | (same) | (same) |
| O3_gamma_locked | {r3_locked} | (same) | (same) |
| O4_delta_locked | {r4_locked} | (same) | (same) |

Observer A: U4 missing r1_locked → cannot detect e1 ≤ e4.
Observer B: U3 missing r1_locked → cannot detect e1 ≤ e3.
The restrictions are complementary: each observer lacks exactly what the other has.

---

## Apparent Orders

**Full event-finality reference:**
- e1 ≤ e3: O1.records = {r1_locked} ⊆ U3.records = {r1_locked, r3_raw} ✓
- e1 ≤ e4: O1.records = {r1_locked} ⊆ U4.records = {r1_locked, r2_locked, r4_raw} ✓
- e2 ≤ e4: O2.records = {r2_locked} ⊆ U4.records ✓
- e1 || e2, e2 || e3, e3 || e4: no record containment in either direction

Reference non-reflexive order: {(e1,e3), (e1,e4), (e2,e4)}

**Observer A (U4 restricted):**
- e1 ≤ e3: r1_locked ∈ A's U3 ✓ — visible
- e1 ≤ e4: r1_locked ∉ A's U4 ✗ — **LOST**
- e2 ≤ e4: r2_locked ∈ A's U4 ✓ — visible

Observer A order: {(e1,e3), (e2,e4)} — missing (e1,e4).

**Observer B (U3 restricted):**
- e1 ≤ e3: r1_locked ∉ B's U3 ✗ — **LOST**
- e1 ≤ e4: r1_locked ∈ B's U4 ✓ — visible
- e2 ≤ e4: r2_locked ∈ B's U4 ✓ — visible

Observer B order: {(e1,e4), (e2,e4)} — missing (e1,e3).

**Symmetry:** A loses exactly one ordering (e1,e4); B loses a different one (e1,e3).
Neither observer's loss subsumes the other's — they are genuinely complementary.

---

## Colimit Construction

Merge A's and B's source record bases (pointwise union):

- U3_gamma_source merged: {r1_locked, r3_raw} ∪ {r3_raw} = {r1_locked, r3_raw} ✓
- U4_delta_source merged: {r2_locked, r4_raw} ∪ {r1_locked, r2_locked, r4_raw} = {r1_locked, r2_locked, r4_raw} ✓

Both restricted bases are restored to their full content. The colimit record
basis equals the full event-finality reference basis.

**Colimit order:** {(e1,e3), (e1,e4), (e2,e4)} = full reference. ✓

**New orderings relative to each observer:**
- New from A (in colimit, not in S_A): {(e1_alpha_locking, e4_delta_locking)}
- New from B (in colimit, not in S_B): {(e1_alpha_locking, e3_gamma_locking)}

Both observers contribute a genuinely new ordering to the colimit. Neither
observer alone reconstructs the full event-finality order. Together they do.

**Colimit partial order axioms:**

| Axiom | Result |
|-------|--------|
| Reflexive | True |
| Antisymmetric | True |
| Transitive | True |
| **Is valid partial order** | **True** |
| **Equals reference** | **True** |

---

## Axis Monotonicity (AM) Checks

AM condition: e_j ≤_rec e_i ↔ causal(e_j) ≤ causal(e_i) AND info(e_j) ≤ info(e_i).

| Witness | AM holds | Spurious pairs | Missing pairs |
|---------|----------|---------------|---------------|
| Reference | **True** | none | none |
| Observer A | **False** | {(e1,e4)}: mag says e1≤e4, A's record says || | none |
| Observer B | **False** | {(e1,e3)}: mag says e1≤e3, B's record says || | none |
| Colimit | **True** | none | none |

**The AM-restored phenomenon:**

For Observer A: the magnitude order has causal(e1)=2 ≤ causal(e4)=3 AND info(e1)=1 ≤ info(e4)=4,
so the 2-axis magnitude order says e1 ≤ e4. But A's restricted record basis does not have
r1_locked in U4, so A's apparent record order says e1 || e4. The magnitude order
over-represents A's apparent structure — a SPURIOUS AM violation.

For Observer B: causal(e1)=2 ≤ causal(e3)=4 AND info(e1)=1 ≤ info(e3)=2, so magnitude
says e1 ≤ e3. But B's restricted U3 lacks r1_locked, so B's apparent record says e1 || e3.
Another SPURIOUS AM violation — symmetric to A's.

The SPURIOUS violations are not errors in the axis profiles. The axis profiles correctly
reflect the full event-finality order (they were designed to match the reference, and
they do: AM holds on the reference). The violations arise because each observer's
restricted apparent order *under-represents* what the axis profiles encode.

**AM is an event-finality property.** It holds when the record basis is complete.
Restricted record access breaks AM locally by creating phantom incomparabilities —
pairs that appear unordered in the apparent structure but are ordered in the axis
magnitudes (which carry global information about the finality crossing). The colimit,
by merging record bases, restores both the record order and AM simultaneously.

---

## Phantom Incomparabilities

| Observer | Pair | Observer says | Colimit says | Phantom? |
|----------|------|--------------|-------------|---------|
| Observer_A | (e1_alpha, e4_delta) | incomparable | e1 ≤ e4 | **YES** |
| Observer_B | (e1_alpha, e3_gamma) | incomparable | e1 ≤ e3 | **YES** |

Two phantom incomparabilities, one per observer, distinct pairs.

Both phantoms arise from the same structural cause: r1_locked was produced by
e1's finality crossing (O1.records = {r1_locked}), but is missing from the
relevant source system in each observer's restricted view. Each observer cannot
detect that e1's locked record was absorbed downstream.

The phantoms are not symmetric in the sense of being mirror images — they
involve different downstream systems (U4 for A, U3 for B). But they are
symmetric in structure: each observer loses exactly one ordered pair involving e1,
and the two pairs are distinct.

---

## T47 Consistency

Colimit is antisymmetric: T47 acyclicity guarantees no record cycle for
PO1-admissible events. No colimit of PO1-admissible FinaliEvent Structures
can violate antisymmetry. Confirmed at 4 events with 8 D1 systems.

The record cycle that would produce an antisymmetry violation would require
O_j.records ⊆ U_i.records AND O_i.records ⊆ U_j.records for some j ≠ i.
In this witness: O_j.records = {rj_locked} and U_i.records never contains
rj_locked unless that specific dependency was designed in. The design is
acyclic; T47's theorem applies.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
|------------|-------|--------|
| H_COLIMIT_CONSISTENT | Colimit is a valid partial order (T47 holds at 4 events) | **supported** |
| H_SYMMETRIC_PHANTOM | A loses (e1,e4); B loses (e1,e3) — distinct and symmetric | **supported** |
| H_COLIMIT_COMPLETE | Colimit = reference; both observers contribute new orderings | **supported** |
| H_AM_RESTORED | AM fails locally (1 SPURIOUS each); AM holds on colimit | **supported** |

**Best supported:** all four hypotheses hold.

---

## What T52 Proves

**1. Colimit consistency at 4 events:** The T47 guarantee extends cleanly to
a 4-event, 8-system witness with two bounded observers. No special structure
of the 3-event T48 witness was needed; the result holds at this scale.

**2. Symmetric phantom incomparability:** Two observers with complementary
bounded access each lose exactly one real ordering. The losses are distinct,
non-overlapping, and structurally symmetric (both arise from missing r1_locked
in different downstream systems). T52 generalizes T51 from asymmetric to
symmetric loss.

**3. Colimit completeness:** Two complementary observers, together, are
sufficient to reconstruct the full 4-event event-finality order. Neither alone
is. This is the minimal result required to justify the colimit as a model of
event finality: two bounded perspectives that cover the full record structure
jointly recover it.

**4. AM is an event-finality property (new):** This is the result T51 did not
produce. In T51, each observer's apparent AM held (T51 observer A had full access).
In T52, each observer's apparent AM fails — the axis profiles exceed what the
restricted record bases support. The colimit repairs both failures simultaneously,
because the colimit restores the full record basis and therefore restores AM.

The precise claim: axis magnitudes encode event-finality information (they track
global D1Profile properties of the target systems). Restricted apparent record
orders encode only local information (accessible records). When the local information
is incomplete, apparent AM fails — the magnitude order is "more global" than the
apparent record order. The colimit brings the record order up to the level of
information that the magnitudes already carry.

---

## Boundary

- Two observers, four events. Colimit completeness holds because the two observers
  together cover the full record structure (their union = reference basis). A third
  observer with a different restriction could test whether (S_A ⊔ S_B) ⊔ S_C =
  S_A ⊔ (S_B ⊔ S_C) — the colimit associativity question. Deferred to T53.

- Only SPURIOUS AM violations observed (magnitude over-represents restricted
  record order). MISSING AM violations (record order asserts ≤ but magnitude
  does not) would require a restriction that adds record dependencies without
  increasing axis magnitudes — a different failure mode not explored here.

- The "minimal extension" property of the colimit (colimit is the smallest
  consistent partial order containing both S_A and S_B) follows from the
  construction (transitive closure of the union) but is not separately tested.

- AM holds on the colimit because the axis profiles were designed to match
  the full reference order. A witness where AM fails on the reference (like
  T50's counterexample) would produce a colimit where AM also fails. T52's
  AM-restored result is contingent on the axis profiles being event-finality-aligned.

## Connection to Prior Results

**T51:** T51 showed asymmetric phantom incomparability (one observer has full access,
one is bounded). T52 lifts this to the symmetric case. The AM-restored phenomenon
did not appear in T51 because T51's fully-informed observer already satisfied AM.

**T50 (AM):** T50 proved AM is the reconstruction condition for a single observer
with full access. T52 shows what happens when access is restricted: AM breaks
locally. The colimit is the multi-observer operation that restores AM by restoring
the record basis. AM is the single-observer reconstruction theorem; the colimit
is its multi-observer extension.

**T47 (PO1 DAG):** T47's acyclicity guarantee is confirmed at 4 events and
8 D1 systems. The colimit is always consistent for PO1-admissible events.

**H1 (Record Reconstruction):** H1 targets reconstruction of temporal order from
accessible records. T52 shows that the reconstructible order depends on record
access: bounded observers reconstruct only their apparent finality order. Full
event-finality order requires either complete access or colimit over multiple
bounded perspectives. H1 for a single bounded observer reconstructs apparent
finality; H1 for event finality requires the colimit formulation.
