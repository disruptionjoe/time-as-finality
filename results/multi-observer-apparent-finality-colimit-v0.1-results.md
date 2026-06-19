# T51 Results: Multi-Observer Apparent Finality Colimit

**Date:** 2026-06-19
**Model:** `models/multi_observer_apparent_finality_colimit.py`
**Runner:** `models/run_t51.py`
**Output:** `results/multi-observer-apparent-finality-colimit-v0.1.json`

---

## Setup

Reuse the T48 events (e1_A_locking, e2_B_locking, e3_composite_locking) with
two different record-basis views of the same underlying D1 systems.

**Record bases — U3_composite_source (the only difference):**

| System | Observer A (full) | Observer B (restricted) |
|--------|------------------|------------------------|
| U3_composite_source | {r_A_locked, r_B_locked, r_composite_raw} | {r_B_locked, r_composite_raw} |

All other record bases are identical across observers. Observer B cannot see
r_A_locked in U3's source records — their causal boundary excludes it.

---

## Apparent Orders

### Observer A (full access)

Direct containment checks:
- e1 ≤ e3: O1.records = {r_A_locked} ⊆ U3.records = {r_A_locked, r_B_locked, r_composite_raw} ✓
- e2 ≤ e3: O2.records = {r_B_locked} ⊆ U3.records ✓
- e1 || e2: O1.records ⊄ U2.records, O2.records ⊄ U1.records ✓

**Observer A apparent order:** {e1 ≤ e3, e2 ≤ e3, e1 || e2} = T48 partial order.

### Observer B (restricted access — missing r_A_locked in U3)

Direct containment checks:
- e1 ≤ e3: O1.records = {r_A_locked} ⊆ {r_B_locked, r_composite_raw}? **NO** ✗
- e2 ≤ e3: O2.records = {r_B_locked} ⊆ {r_B_locked, r_composite_raw} ✓
- e1 || e2: same as A ✓

**Observer B apparent order:** {e2 ≤ e3 only}.
- e1 and e3 appear **incomparable** to Observer B.
- Observer B also sees e1 || e2 (same as A — no change here).

Observer B's incomparable pairs: {(e1_A_locking, e2_B_locking), **(e1_A_locking, e3_composite_locking)**}

The second pair is new — it does not appear in Observer A's incomparable set.
This is the phantom incomparability.

---

## Colimit Construction

**Merge rule:** For each system, take the union of record sets across both observers.

U3_composite_source (merged):
{r_B_locked, r_composite_raw} ∪ {r_A_locked, r_B_locked, r_composite_raw}
= {r_A_locked, r_B_locked, r_composite_raw}

All other systems: unchanged (already identical across observers).

**Colimit record basis = Observer A's record basis.**

**Colimit order (recomputed from merged bases):**

| Pair (e_j, e_i) | record order | new (not in S_B) |
|-----------------|-------------|-----------------|
| (e1, e2) | False | — |
| **(e1, e3)** | **True** | **YES** |
| (e2, e1) | False | — |
| (e2, e3) | True | — (already in S_B) |
| (e3, e1) | False | — |
| (e3, e2) | False | — |

**New ordering recovered by colimit:** (e1_A_locking, e3_composite_locking)

This ordering was invisible to Observer B. The colimit recovers it from Observer
A's record basis. The event-finality order is strictly richer than Observer B's
apparent finality order.

---

## Phantom Incomparability

**Definition:** A phantom incomparability is a pair (e_j, e_i) that a bounded
observer reports as incomparable, but which the colimit (event finality) orders.

**Result:**

| Observer | Pair | Observer sees | Colimit says | Phantom? |
|----------|------|--------------|-------------|---------|
| Observer_B | (e1_A_locking, e3_composite_locking) | incomparable | e1 ≤ e3 | **YES** |
| Observer_A | (e1_A_locking, e3_composite_locking) | e1 ≤ e3 | e1 ≤ e3 | no |
| Observer_A | (e1_A_locking, e2_B_locking) | incomparable | incomparable | no |
| Observer_B | (e1_A_locking, e2_B_locking) | incomparable | incomparable | no |

**One phantom incomparability confirmed:** Observer B sees e1 || e3 but the
colimit has e1 ≤ e3.

The (e1, e2) incomparability is NOT a phantom — it is genuine in the event-finality
structure too. Observer B correctly identifies it. Observer A correctly identifies it.
Bounded access does not distort this pair.

**Interpretation:** Observer B is missing r_A_locked from their view of U3's
source records. From their perspective, the A-locking event (e1) produced a
record that does not appear to have been absorbed by the composite event's
source system. They cannot detect the dependency. This is not a reasoning error —
it is correct given their accessible records. The incomparability is real within
their apparent finality structure. It is only a phantom relative to the event
finality structure (the colimit).

---

## Colimit Partial Order Verification

| Axiom | Result |
|-------|--------|
| Reflexive | True |
| Antisymmetric | True |
| Transitive | True |
| **Is partial order** | **True** |

**T47 consistency:** Colimit antisymmetry is guaranteed by T47 (PO1 DAG
Theorem). A record cycle — O_j.records ⊆ U_i.records AND O_i.records ⊆ U_j.records
for distinct i,j — is the only route to an antisymmetry violation in the colimit.
T47 proves no such cycle exists for PO1-admissible events. The colimit of any
two PO1-admissible FinaliEvent Structures is guaranteed consistent.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
|------------|-------|--------|
| H_COLIMIT_CONSISTENT | Colimit is a valid partial order (no antisymmetry violations) | **supported** |
| H_PHANTOM_INCOMPARABILITY | Observer B sees e1 \|\| e3; colimit says e1 ≤ e3 | **supported** |
| H_COLIMIT_EXTENDS | Colimit adds e1 ≤ e3 not present in Observer B's apparent order | **supported** |

**Best supported:** all three hypotheses hold.

---

## What T51 Proves

**1. Colimit consistency (T47 restated at multi-observer level):**
The colimit of PO1-admissible FinaliEvent Structures is always a consistent
partial order. Antisymmetry violations require record cycles; T47 rules these
out. Multi-observer event-finality reconstruction is safe: merging record bases
can never produce a logically inconsistent temporal order.

**2. Phantom incomparability (bounded access loses real orderings):**
A bounded observer with restricted record access may classify two events as
incomparable when they are actually ordered in the event-finality structure.
This is not a reasoning failure — it is an epistemic limitation. The observer's
apparent finality structure is locally correct; it is globally incomplete.

This is the first concrete witness for the apparent/event finality distinction
proposed in `explorations/apparent-vs-event-finality-v0.1.md`. Apparent finality
is reconstructible from accessible records. Event finality requires merging
across observer boundaries.

**3. Colimit extension (event finality ≥ any apparent finality):**
Event finality is at least as rich as any individual observer's apparent finality.
The colimit never loses orderings that appear in any individual structure — it
only adds them. (Proof: if (e_j, e_i) is in S_A or S_B, the record containment
O_j.records ⊆ U_i.records holds in those bases, and the merged basis contains
the same records, so the containment still holds in the colimit.)

---

## Connection to Prior Results

**T48:** T51 reuses T48's events and record bases unchanged. The T48 partial
order is Observer A's apparent order and the colimit order simultaneously:
a fully-informed observer already sees event finality for this witness.

**T50 (AM):** Axis Monotonicity holds on both apparent structures and on the
colimit (same as Observer A's order). T51 does not break AM — it demonstrates
that AM can hold locally for each observer while the apparent orders differ.
Observer B's apparent order also satisfies AM on its restricted event set
(e2 ≤ e3, and causal(e2)=1 ≤ causal(e3)=3, info(e2)=3 ≤ info(e3)=4 — check).

**T47 (PO1 DAG):** T47's acyclicity theorem is the underlying guarantee for
colimit consistency. T51 makes this explicit: the colimit-consistency condition
IS T47 restated for multi-observer record merging.

**Exploration (apparent-vs-event-finality):** T51 is the first runnable test
of this distinction. The exploration note predicted: "Apparent finality is locally
reconstructible from accessible records. Event finality is globally defined over
the full finality trace." T51 confirms both halves and witnesses the gap between
them with a concrete phantom incomparability.

---

## Boundary

- Two observers, three events. The colimit equals Observer A's full structure
  because Observer A already has complete access. A strictly more interesting
  witness — two observers each with complementary partial access (neither has
  the full picture, both are needed for the colimit) — requires a 4-event
  structure. This is deferred to T52.

- Only one restriction pattern tested: removing r_A_locked from U3's source.
  Other restrictions (removing r_B_locked, or restricting target record bases
  rather than source) would produce different phantom patterns.

- The "genuine" incomparability (e1 || e2) is preserved correctly across all
  observers and in the colimit. T51 does not test whether bounded access can
  create phantom *orderings* (observer wrongly believes e_j ≤ e_i when the
  colimit has e_j || e_i). This would require a different restriction pattern.

- Colimit associativity (colimit of colimits = colimit of all) is assumed but
  not tested. A 3-observer witness would check this.
