# Provenance-Aware Reconstruction

**Status:** Exploration — pre-formal, not yet a runnable test.
**Trigger:** Research Guidance Note (2026-06-19) following T51-T52 colimit results.
**Relationship:** Parallel question to apparent/event finality; not a sub-question of it.

---

## Motivation

The T51-T52 colimit construction merges observer record *contents*: the colimit
of two observer bases is the pointwise union of their record sets. No test so
far has asked whether the *history of how those records propagated between
observers* carries independent reconstructive information.

This exploration asks that question. The objective is to determine the
relationship between two representations:

- **Record basis** — the set of records an observer holds at a given moment
  (what T48-T52 formalize).
- **Provenance** — the history of how each record in that basis was acquired:
  who observed it originally, who transmitted it to whom, and in what order
  relative to the FinaliEvent structure.

The question is whether these two representations are equivalent, or whether
one is strictly richer, strictly weaker, or complementary.

No conclusion is assumed. Both equivalence and separation results would be
informative.

---

## Formal Sketch

**Definition (Propagation Edge):** A directed edge P = (A, B, R, e) where:
- A, B are bounded observers (each holding a FinaliEvent Structure)
- R is a non-empty set of records (R ⊆ A's accessible records)
- e is a FinaliEvent after which the propagation occurs (optional temporal anchor)

A propagation edge represents: "Observer A transmitted records R to Observer B."
After the edge, B's accessible records include R.

**Definition (Propagation Graph):** A directed multigraph G = (Observers, Edges)
where each edge is a Propagation Edge. Allows multiple edges between the same
pair of observers (different records, different times).

**Definition (Provenance of record r at observer X):** The set of all paths
in the propagation graph that could have delivered r to X. This includes:
- Direct observation: X is the observer for whom the finality crossing produced r
  (no incoming edge — X is the origin).
- One-hop propagation: some A observed r and transmitted it directly to X.
- Multi-hop: r propagated through a chain A → B → ... → X.

**Definition (Provenance basis of observer X):** For each record r in X's
accessible records, the set of all provenance paths leading to r. This is
richer than the record basis (which only says "X has r") — it describes
*how* X came to have r.

---

## The Core Questions

### 1. What is reconstructible from propagation history alone?

Given only the propagation graph G (who told whom what, and when relative
to the FinaliEvent order), what aspects of the event-finality colimit
are determinable?

Candidates:
- The colimit record basis (union of all accessible records) — is G sufficient?
- The colimit partial order (record-dependency order over the union) — is G sufficient?
- The axis magnitudes (causal, info profiles of each FinaliEvent) — are these
  derivable from G, or do they require direct access to the D1Profiles?

### 2. What is the relationship between provenance and record basis?

Four possible answers, each worth testing:

**Equivalent:** Provenance and record basis are mutually derivable. Knowing one
is sufficient to reconstruct the other. This would mean provenance is a
redundant representation — the record basis already captures all the information
that propagation history would add.

**Provenance strictly richer:** Multiple distinct propagation histories can
produce the same record basis. Two observers can end up with the same records
via different propagation paths. Provenance is not recoverable from the record
basis alone; it contains additional information.

**Record basis strictly richer:** There exist records in an observer's basis
that cannot be explained by any propagation graph (e.g., direct observation
of a finality crossing that was not transmitted from anyone). The record basis
contains "origination facts" that a purely propagational model cannot represent.

**Complementary:** Neither determines the other. Some information in the record
basis is not captured by any propagation graph, and some provenance structure
is not captured by the record basis. Both are needed for full reconstruction.

### 3. Witness candidates

Before choosing a hypothesis, the following candidate witnesses should be
constructed and tested:

**Candidate A (same basis, different propagation):**
- Observer A performs a finality crossing that produces r1_locked.
- Scenario 1: A → C (A tells C about r1_locked directly)
- Scenario 2: A → B → C (A tells B; B tells C)
- Result: C holds r1_locked in both scenarios. Record basis is identical.
  Propagation history differs.
- If confirmed: propagation is not recoverable from record basis alone.
  Provenance is strictly richer than (or at least different from) record basis.

**Candidate B (same propagation history, different record bases):**
- Does there exist a propagation graph G such that two observers X and Y
  have identical provenance paths for all records, but different record sets?
- This would require X and Y to have identical "who told whom" structure
  but diverge on origination (which finality crossings each directly performed).
- If confirmed: record basis is not derivable from propagation alone.
  Record basis is strictly richer than (or complementary to) provenance.

**Candidate C (provenance determines colimit):**
- Construct a propagation graph G that encodes which observer learned which
  records from which other observer.
- Show that the colimit (union of all record bases) is computable from G
  alone, without explicitly merging record sets.
- This would be the Hashgraph-style positive result: propagation history
  is sufficient for canonical reconstruction.

**Candidate D (propagation graph is ambiguous re: colimit):**
- Construct two propagation graphs G1 and G2 that have the same topological
  structure (same edges, same temporal ordering) but are compatible with
  different colimit record bases.
- This would show: propagation graph does not uniquely determine the colimit.
  Record content is essential; propagation structure alone is insufficient.

---

## Relationship to Existing Framework

**D1Cat:** Propagation events may themselves be D1RestrictionMorphisms — a
record transmitted from observer A to observer B is a morphism from A's
D1RestrictionSystem to B's. If so, the propagation graph is a subgraph of
D1Cat, and provenance is a path-in-D1Cat question.

Alternatively, propagation events may require a distinct type of morphism —
not a "finality crossing" (pre- to post-finality) but a "record transport"
(post-finality to post-finality). These two morphism types are distinguishable:
finality crossings change obstruction status (AC6); record transport preserves it.

Whether propagation events are representable within D1Cat or require an
extension is itself an open question.

**FinaliEvent colimit (T51-T52):** The T51-T52 colimit merges record bases
by pointwise union. This is a record-content operation with no propagation
information. If Candidate A (same basis, different propagation) is confirmed,
the colimit is provenance-blind: two structurally different propagation
situations produce the same colimit. Whether this matters for reconstruction
depends on whether provenance encodes additional constraints on the event-finality
order that record-content merging does not.

**Apparent vs. event finality (T51-T52):** The apparent/event finality
distinction is a question about the record-dependency *order* reconstructed
from accessible records. Provenance-aware reconstruction is a question about
the *history* of how those records were assembled. These are parallel questions,
not nested ones. The apparent/event finality gap could exist even with perfect
provenance information, and provenance questions could be asked even with
a single observer (no colimit needed).

---

## What Would Make Provenance a New Primitive

Provenance would earn status as a first-class mathematical object if any of
the following are confirmed:

1. **Provenance encodes constraints invisible to record-content merging.**
   The colimit of two observers with different provenance histories would need
   to produce different event-finality orders — same records, different order
   — for provenance to be load-bearing.

2. **Provenance enables reconstruction that record content cannot.**
   A bounded observer who knows the propagation history but not the full
   record content could reconstruct the colimit order; a bounded observer
   who knows the full record content but not the propagation history could not.

3. **Provenance prevents spurious reconstruction.**
   A provenance-aware colimit might rule out orderings that a naive
   record-content colimit permits — reducing phantom incomparabilities
   or eliminating spurious orderings — because propagation history encodes
   constraints on which records could coherently precede which others.

If none of these hold — if record content is sufficient for reconstruction
and provenance is derivable from it — then provenance is not a new primitive
for this framework, even if it is useful for other purposes (auditability,
trust, attribution).

---

## Failure Modes Worth Preserving

If any of the following hold, the conclusion is equally valuable:

- **Provenance is derivable from record content + FinaliEvent structure.**
  This would mean the existing formalism already implicitly encodes provenance,
  and no new primitive is needed. The framework is more complete than expected.

- **Provenance and record content are complementary but neither is fundamental.**
  Both might be specializations of a third, more abstract object — perhaps
  a typed transport morphism that encodes both content and history simultaneously.
  This would point toward a categorical representation.

- **Provenance introduces underdetermination rather than resolving it.**
  Multiple distinct provenances could produce the same event-finality order,
  making provenance add structure without adding reconstructive power.

---

## Proposed Witness Construction for T53

If the four-way classification is to be tested, the minimum witness needs:

- At least 3 observers (so that multi-hop propagation is distinguishable
  from single-hop)
- At least 2 records with distinct provenance paths (so that Candidate A
  and Candidate B are independently testable)
- At least 1 origination event (a finality crossing where the observing
  system is itself the origin, not a recipient of propagated records)

A concrete candidate: 3 observers (A, B, C), 2 finality crossings (e1 by A,
e2 by B), propagation paths A→C and B→C (both direct) vs. A→B→C and B→A→C
(crossed). Both scenarios give C access to both e1 and e2's locked records.
The record basis is identical. The propagation histories differ. The colimit
is the same. This would confirm Candidate A — but would not establish whether
the different propagation history carries any reconstructive information about
the *order* of events.

The order-sensitive version: does C's knowledge that r1_locked arrived before
r2_locked (from the propagation ordering) affect C's reconstruction of e1 ≤ e2
or e1 || e2? This requires connecting propagation timing to the FinaliEvent
partial order — which is the formal question T53 would need to answer.

---

## Open Questions for Future Work

1. Is a propagation event (A transmits R to B) a D1RestrictionMorphism?
   If yes: what kind? If no: what axioms distinguish it from a finality crossing?

2. Does propagation order (temporal ordering of propagation edges) carry
   information beyond what the FinaliEvent partial order encodes?

3. Can two FinaliEvent Structures with the same events and record-dependency
   order have different provenance structures? (Provenance-opaque structures
   vs. provenance-transparent structures.)

4. Is the T51-T52 colimit operation a special case of a provenance-aware
   colimit in which propagation history is collapsed? Or is it orthogonal?

5. In the Hashgraph setting, gossip history determines event order. In the
   finality-theoretic setting, record-dependency order determines event order.
   What is the precise relationship between these two order-determination
   mechanisms? Are they dual? Isomorphic? Distinct?
