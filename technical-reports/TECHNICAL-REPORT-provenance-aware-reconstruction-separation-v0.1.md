# Technical Report: Provenance-Aware Reconstruction Separation Audit (v0.1)

**Date:** 2026-06-19  
**Test:** T55B  
**Model:** `models/provenance_aware_reconstruction.py`  
**Runner:** `models/run_t55b.py`  
**Results:** `results/provenance-aware-reconstruction-separation-v0.1.json`

---

## Executive Summary

T55B tests whether propagation history — who learned what from whom, and in what order
relative to the FinaliEvent structure — carries independent reconstructive information
beyond the record basis formalized in T48-T54.

**Primary finding:** H4 is confirmed for all tested witnesses. Provenance variation does
not change event-finality colimits, axis monotonicity (AM) reconstruction, or T54
quotient-union descent classification.

**Secondary finding:** H0 is refuted. Provenance is not equivalent to the record basis:
the same record basis can arise from different propagation histories (W_A), so the
record basis does not uniquely determine provenance.

**Recommendation:** Provenance is an optional audit layer for the current TaF formalism.
It is not a first-class mathematical primitive at this stage. It may earn that status
if future witnesses show propagation order constraining event-finality order, or if
provenance provides identity evidence that resolves T54-type underdetermination.

---

## Background

T51-T54 merge observer record contents by pointwise union (colimit) and quotient-union
descent. They test whether the merged record basis recovers the full event-finality
partial order, whether axis monotonicity (AM) holds on the colimit, and under what
conditions the colimit is canonical.

None of T51-T54 tracks how records moved between observers. A record in observer C's
basis might have arrived via A→C (one hop) or A→B→C (two hops) without changing C's
accessible record set. The question T55B addresses: does this difference matter for
event-finality reconstruction?

The exploration note `explorations/provenance-aware-reconstruction-v0.1.md` defines
the symmetric hypotheses H0-H4 and outlines candidate witnesses. T55B executes
those witnesses and returns verdicts.

---

## Formal Objects

### PropagationScenario

A named configuration of:
- **Observers:** finite set of named observer nodes.
- **PropagationEdges:** directed edges `(source, target, records, step)` carrying a set
  of records from one observer to another at a monotone step index.
- **OriginLabels:** declarations that a specific observer is the first holder of a
  specific record (the observation that produced it).

### Accessible Records

Computed by BFS from origins along propagation edges (in step order):

```
held[obs] = {r : OriginLabel(obs, r)}
repeat until stable:
  for each edge (A→B, records, step):
    held[B] += held[A] ∩ records
```

### ProvenanceBasis

For each observer, the set of all delivery chains (ProvenancePaths) explaining how
each accessible record arrived. A ProvenancePath is a sequence of observers
`[o₁, o₂, ..., oₙ]` where o₁ is the origin and oₙ = the target observer, with a
directed edge (oᵢ, oᵢ₊₁) for each consecutive pair.

### Event-Finality Order (self-contained)

For comparison with T48-T54, a minimal event-finality order is computed:
- e_j ≤ e_i iff `e_j.target_records ⊆ e_i.source_records` (and target_records non-empty).
- Reflexive-transitive closure applied.

---

## Witnesses and Results

### W_A: Same Record Basis, Different Provenance (H1 Test)

**Scenarios:** 3 observers (A, B, C); A originates r1_locked; B originates r2_locked.

**A1 (direct):**
- A→C: {r1_locked} at step=1 (anchored to e1_locking)
- B→C: {r2_locked} at step=2 (anchored to e2_locking)

**A2 (transitive):**
- A→B: {r1_locked} at step=1
- B→C: {r1_locked, r2_locked} at step=2

**Observer C's accessible records:** {r1_locked, r2_locked} in **both** scenarios.

**Observer C's provenance paths:**

| Scenario | r1_locked delivery chain | r2_locked delivery chain |
|----------|--------------------------|--------------------------|
| A1 (direct) | A → C (1-hop) | B → C (1-hop) |
| A2 (transitive) | A → B → C (2-hop) | B → C (1-hop) |

**Result:** `same_record_basis=True`, `same_provenance_structure=False`.

The record basis is identical; the provenance structure differs. Provenance is not
recoverable from the record basis alone. **H1 is supported.**

---

### W_B: Same Topology, Different Record Content (H2 Partial Test)

**Scenarios:** 3 observers (P, Q, R); topology is P→R (step=1), Q→R (step=2) in both.

| Scenario | P originates | Q originates | R's accessible records |
|----------|-------------|-------------|------------------------|
| B1 | r_alpha_locked | r_beta_locked | {r_alpha_locked, r_beta_locked} |
| B2 | r_gamma_locked | r_delta_locked | {r_gamma_locked, r_delta_locked} |

**Result:** Same who-tells-whom topology, completely different record content at R.

Abstract propagation topology (which observer transmits to which) cannot determine
the record basis. Record content is not derivable from topology alone.

**Verdict:** H2 supported in the **topology-only** sense. Full provenance (labeled
propagation with specific records) does determine accessible records — so H2 does not
hold in its strongest form. Topology-only provenance is strictly weaker than record basis.

---

### W_C: Propagation Determines Colimit iff Origins Known

**Claim:** The global colimit (union of all observers' accessible records) equals
the union of all origin records.

**Proof sketch:** Propagation edges redistribute records from origins but never
create new records. Every accessible record traces to exactly one origin. Therefore:

```
∪_obs accessible_records(obs) = ∪_origin origin.record
```

**Corollary (positive):** Given the full propagation graph (including origin records),
the colimit is computable without explicitly simulating propagation.

**Corollary (negative):** Given only the propagation topology (who-tells-whom), without
the origin record labels, the colimit is underdetermined. Different origin assignments
yield different colimits.

**Finding:** The colimit is an origin-determined object, not a topology-determined object.
Provenance topology adds no information about the colimit beyond what the origins carry.

---

### W_D: Propagation Step-Order Does Not Determine Event-Finality Order

**Setup:** Observer C has {r1_locked (step=1), r2_locked (step=2)}.

The propagation step-ordering (r1_locked arrived before r2_locked) is compatible
with two event structures:

**E_concurrent (e1 || e2):**
- e1: source={r1_raw}, target={r1_locked}, profile=(causal=2, info=1)
- e2: source={r2_raw}, target={r2_locked}, profile=(causal=1, info=3)
- Record order: no cross-dependency → e1 || e2
- Non-reflexive order pairs: **none**

**E_ordered (e1 ≤ e2):**
- e1: source={r1_raw}, target={r1_locked}, profile=(causal=2, info=1)
- e2: source={r1_locked, r2_raw}, target={r2_locked}, profile=(causal=3, info=3)
- Record order: r1_locked ⊆ {r1_locked, r2_raw} → e1 ≤ e2
- Non-reflexive order pairs: **{(e1, e2)}**

**C's accessible records are identical in both:** {r1_locked, r2_locked}.

The propagation step-ordering is consistent with both event structures. C knowing
"r1_locked arrived before r2_locked" does NOT establish e1 ≤ e2.

**Key distinction:** Event-finality order is determined by record CONTAINMENT in the
formal D1 systems (O_j.records ⊆ U_i.source_records). Propagation step-order is the
timing of inter-observer record transfer. These are orthogonal. Propagation timing
tells us about acquisition order, not causal precedence.

**Result:** `propagation_order_determines_event_order = False`

**H4 is supported:** Propagation ordering does not determine the event-finality partial
order, and therefore cannot change colimit construction or AM.

---

### W_T54: T54 Quotient-Union is Provenance-Blind

T54's `canonical_quotient_union` consumes:
- Observer-local `LocalEvent` data: `(source_records, target_records, axis_profile)`
- `EventIdentityMap`: which local events correspond to global events
- `overlap_witnesses`: inter-observer event identity evidence

None of these fields carry propagation history. Two scenarios with identical accessible
records (as in W_A's A1 and A2) produce identical `LocalEvent` inputs to T54.

**Result:** `basis_identical=True`, `t54_input_identical=True`.

Same record basis → same T54 input → same T54 classification, regardless of whether
records arrived by direct or transitive propagation.

**H4 is confirmed for T54 descent.**

---

### Colimit Comparison (A1 vs A2)

Both scenarios give C the same accessible records. Computing the event-finality order
over the two-event structure {e1, e2} (both concurrent — no cross-dependency in source
records):

| Scenario | Accessible at C | Event order (non-refl) | AM holds |
|----------|----------------|------------------------|----------|
| A1_direct | {r1_locked, r2_locked} | [] (e1 \|\| e2) | True |
| A2_transitive | {r1_locked, r2_locked} | [] (e1 \|\| e2) | True |

**Colimit orders identical: True.** AM identical: True.

Provenance variation produces no change in event-finality reconstruction. H4 confirmed.

---

## Hypothesis Verdicts

| ID | Claim | Verdict | Key witness |
|----|-------|---------|-------------|
| H0 | Provenance ≡ record basis (mutually reconstructible) | **Refuted** | W_A |
| H1 | Provenance strictly richer: same basis, different provenances | **Supported** | W_A |
| H2 | Provenance strictly weaker: topology cannot determine basis | **Partial** | W_B |
| H3 | Complementarity: neither fully determines the other | **Partial** | W_A, W_B |
| H4 | Provenance variation does not affect colimits, AM, or descent | **Supported** | W_A, W_D, W_T54 |

### H0: Refuted

Mutual reconstructibility requires both:
- Provenance → record basis: **succeeds** (BFS from origins computes accessible records).
- Record basis → provenance: **fails** (W_A: same basis, different provenances).

The second direction fails. H0 is refuted.

### H1: Supported

W_A confirms same accessible records at C, distinct provenance structures in A1 vs A2.
The record basis does not uniquely determine propagation history.

Important caveat: H1's claim that "identical record bases can arise from different
propagation histories with **different reconstructive consequences**" is only partially
confirmed. The histories are different, but the reconstructive consequences (colimit,
AM, T54 classification) are identical (H4). H1's evidentiary claim holds; its
reconstructive-consequence claim does not.

### H2: Partial

Topology-only provenance (who-tells-whom without record labels) cannot determine the
record basis (W_B). Full labeled provenance determines accessible records. H2 holds in
the topology sense, not in the full-provenance sense.

### H3: Partial

H1 confirms basis → provenance fails (one direction of H3). Full provenance → basis
succeeds (opposite of H3 in the other direction). True H3 (neither determines the
other) holds only for the topology-only form. The full-labeled provenance → basis
direction is constructive.

### H4: Supported

Three independent witnesses:
1. **W_A colimit:** identical colimit and AM for A1 and A2.
2. **W_D:** propagation step-order compatible with multiple event-finality orders.
3. **W_T54:** T54 is provenance-blind by construction.

H4 is the strongest result in this audit.

---

## Recommendation: Optional Audit Layer

Provenance does not currently earn first-class status as a mathematical primitive in
the TaF event-finality program. The grounds:

1. **H4 holds for all tested witnesses.** Provenance variation changes neither the
   event-finality colimit, AM reconstruction, nor T54 descent classification.

2. **The colimit is origin-determined.** Propagation topology adds no information
   about the global colimit beyond what the origin record sets already carry.

3. **Propagation order is orthogonal to event-finality order.** The temporal sequence
   in which records arrive at an observer does not determine the record-dependency
   partial order on FinaliEvents.

Provenance remains useful as:
- **Auditability:** tracking how records moved between observers for trust and attribution.
- **Potential identity evidence:** if A transmitted record r_a to B before B's event
  used r_a in its source, that is evidence connecting the events. But this requires
  extending T54's identity-map conditions, not replacing the record basis.

### Conditions for Promotion to First-Class Primitive

Provenance would earn first-class status if any of the following hold:

1. **Propagation causal constraint:** A witness showing that enforcing "records can only
   propagate after the events that produced them have run" implies propagation step-order
   constrains event-finality order in a strict, non-redundant way.

2. **T53 identity resolution:** A witness where provenance (A told B about record r_a)
   provides the identity-map evidence T54 needs to resolve T53-type underdetermination —
   confirming two local events are instances of the same global event class.

3. **Order enrichment:** A witness where the provenance-aware colimit (weighting record
   union by propagation order) produces a different, more refined event-finality partial
   order than the plain T54 pointwise union.

None of these conditions is met by the current witness set.

---

## Open Questions

1. **Propagation causal constraint:** If records can only propagate after their originating
   FinaliEvent has occurred, does step-order imply event-finality order? This would
   require connecting the PropagationEdge step ordering to the FinaliEvent temporal anchor.
   The current model has `anchor_event` as an optional field; formalizing it as a mandatory
   ordering constraint is a natural next step.

2. **T53 identity resolution via provenance:** Can provenance evidence (A transmitted
   r_a to B, B's source system then required r_a) provide the identity-map and overlap
   evidence T54 needs? This would connect the provenance exploration directly to T54's
   C1-C7 descent conditions and is the most promising path to first-class status.

3. **Propagation edges as D1RestrictionMorphisms:** Is a PropagationEdge (A→B carrying
   records R) representable as a D1RestrictionMorphism? Propagation is post-finality to
   post-finality (preserving obstruction status), unlike a FinaliEvent crossing (pre- to
   post-finality, creating obstruction). These morphism types may be distinct. If distinct,
   the propagation graph requires a new morphism class in D1Cat.

4. **Provenance-aware colimit:** Does a colimit that incorporates propagation order (e.g.,
   merging record bases with step-timestamps rather than plain union) refine or alter the
   event-finality partial order? The current T52/T54 construction uses plain union. A
   step-weighted merge could potentially resolve some phantom incomparabilities or reveal
   new orderings.

---

## Connection to Prior Results

**T51-T52 (colimit):** T55B confirms that the T51/T52 colimit construction is provenance-blind.
Two structurally different propagation scenarios that give the same record basis at each observer
produce the same colimit event order and the same AM result. This validates the T51/T52 choice
to work at the record-basis level, not the provenance level.

**T54 (descent theorem):** T55B confirms that T54's C1-C7 descent conditions are provenance-blind
by construction. Provenance could become relevant to T54 only via conditions that T54 does not
currently include — specifically, conditions on identity-map evidence and overlap witnesses.

**T53 (descent boundary):** The most promising connection. T53's "underdetermined" classification
arises when observers have no identity-map evidence to link their local events. Provenance
(A transmitted r_a to B, making it plausible that B's use of r_a depends on A's event) is
a candidate source of that evidence. This connection is an open question, not a confirmed result.

**Exploration note:** The symmetric hypotheses H0-H4 in
`explorations/provenance-aware-reconstruction-v0.1.md` were the basis for this test design.
H4 is the best-supported outcome, consistent with the exploration note's recommendation to
test for equivalence and separation before committing to provenance as a new primitive.

---

## Boundary

- Only honest propagation (non-conflicting, monotone) is tested. Byzantine equivocation
  (an observer transmitting different records to different peers) is T55's territory.

- The model uses unlabeled D1 systems (records are named strings, not full D1RestrictionSystems).
  Whether the full PO1 admissibility apparatus applies to propagation edges is open.

- Signed provenance (cryptographic attestation of transmission history) is not modeled.
  The model tracks provenance as a mathematical structure, not a trust mechanism.

- Three observers (A, B, C) are the minimum to distinguish multi-hop from single-hop
  propagation. The colimit associativity question (does (A ⊔ B) ⊔ C = A ⊔ (B ⊔ C)
  in provenance-enriched systems?) is open and not tested here.
