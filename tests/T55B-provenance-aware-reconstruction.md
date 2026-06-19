# T55B: Provenance-Aware Reconstruction Separation Audit

**Status:** Implemented — v0.1  
**Date:** 2026-06-19  
**Model:** `models/provenance_aware_reconstruction.py`  
**Runner:** `models/run_t55b.py`  
**Output:** `results/provenance-aware-reconstruction-separation-v0.1.json`  
**Technical report:** `TECHNICAL-REPORT-provenance-aware-reconstruction-separation-v0.1.md`  
**Exploration:** `explorations/provenance-aware-reconstruction-v0.1.md`

---

## Purpose

T51-T54 merge observer record contents via colimit and quotient-union descent, but
do not track how records propagated between observers. This test asks whether that
omission is harmless (H4) or load-bearing (H1-H3).

**Central question:** Given a propagation graph — who learned what from whom, and
at what step relative to the FinaliEvent structure — does propagation history carry
independent reconstructive information beyond the record basis?

---

## Hypotheses

| ID | Claim |
|----|-------|
| H0 | Provenance is equivalent to record basis: both are mutually reconstructible. |
| H1 | Provenance strictly richer: identical bases admit different propagation histories. |
| H2 | Provenance strictly weaker: propagation topology cannot determine record basis. |
| H3 | Complementarity: neither representation fully determines the other. |
| H4 | Provenance varies but does not affect event-finality colimits, AM, or T54 descent. |

---

## Formal Objects

**PropagationEdge:** `(source_observer, target_observer, records, step, anchor_event?)`
- A transmits records R to B at monotone step index.
- `anchor_event` optionally names the FinaliEvent after which transmission occurs.

**OriginLabel:** `(observer, record)`
- This observer directly observed (is the first holder of) this record.

**PropagationScenario:** `(observers, edges, origins)`
- A complete propagation configuration.

**ProvenancePath:** `(record, target_observer, path, is_direct_observation)`
- A delivery chain from origin to target, as a sequence of observers.

**ObserverState:** `(accessible_records, provenance_paths)`
- Accessible records computed by BFS from origins along edges.
- Provenance paths enumerate all delivery chains for each accessible record.

---

## Witnesses

### W_A: Same Record Basis, Different Propagation Paths

**Setup:** 3 observers (A, B, C); A originates r1_locked; B originates r2_locked.

- **A1 (direct):** A→C: {r1_locked}, B→C: {r2_locked}.
  C's provenance: r1_locked via (A→C), r2_locked via (B→C).

- **A2 (transitive):** A→B: {r1_locked}, B→C: {r1_locked, r2_locked}.
  C's provenance: r1_locked via (A→B→C), r2_locked via (B→C).

C's accessible records: {r1_locked, r2_locked} in **both** scenarios.
C's provenance paths **differ** (direct vs multi-hop for r1_locked).

**Tests H1:** same basis does not determine provenance.

---

### W_B: Same Propagation Topology, Different Record Content

**Setup:** 3 observers (P, Q, R); topology P→R (step 1), Q→R (step 2) in both.

- **B1:** P originates r_alpha_locked; Q originates r_beta_locked.
  R's basis: {r_alpha_locked, r_beta_locked}.

- **B2:** P originates r_gamma_locked; Q originates r_delta_locked.
  R's basis: {r_gamma_locked, r_delta_locked}.

**Tests H2 (topology form):** abstract propagation topology cannot determine record basis.

---

### W_C: Propagation Determines Colimit (Positive Direction)

**Claim:** If the full propagation graph (topology + origin records + transmitted records)
is known, the accessible records at each observer are computable (BFS from origins along edges).

**Negative corollary:** Topology alone (without record labels) cannot determine accessible records.

**Key finding:** The global colimit (union of all accessible records) equals the union
of all origin records. Propagation only redistributes — it never creates records.
Therefore the colimit is fully determined by the origin set, not by propagation topology.

---

### W_D: Propagation Step-Order Compatible with Multiple Event-Finality Orders

**Setup:** Observer C has {r1_locked (step=1), r2_locked (step=2)}.

This propagation step-ordering is compatible with:

- **E_concurrent:** e1 || e2 (e2's source = {r2_raw} — does not require r1_locked).
  Non-reflexive event order: empty (no e1≤e2 or e2≤e1).

- **E_ordered:** e1 ≤ e2 (e2's source = {r1_locked, r2_raw} — requires r1_locked).
  Non-reflexive event order: {(e1, e2)}.

The propagation step-ordering (r1_locked before r2_locked) is consistent with both
event structures. Event-finality order is determined by record CONTAINMENT in the
formal D1 systems (O_j.records ⊆ U_i.records), not by propagation timing.

**Tests H4:** propagation order does not determine event-finality order.

---

### W_T54: T54 Quotient-Union is Provenance-Blind

T54's canonical_quotient_union consumes: observer-local event views (source/target
record sets), event identity maps, and axis profiles. None of these carry propagation
history. Two observers with identical accessible records (as in W_A scenarios A1 and A2)
produce identical T54 LocalEvent inputs, hence identical T54 classification.

**Tests H4:** same basis → same T54 descent output regardless of provenance.

---

## Expected Results

| Witness | Expected finding |
|---------|-----------------|
| W_A | same_record_basis=True, same_provenance_structure=False → H1 supported |
| W_B | same_topology, different basis → H2 partial |
| W_C | colimit = union of origins; topology insufficient → H0 partial refutation |
| W_D | propagation_order_determines_event_order=False → H4 supported |
| W_T54 | basis_identical=True, t54_input_identical=True → H4 supported |
| Colimit comparison (A1 vs A2) | event_order identical, AM identical → H4 supported |

---

## Target Claims

- **C1:** Record reconstruction from accessible records.
- **D1-Field:** Cross-observer finality and multi-observer colimits.
- **T51, T52, T54:** Colimit construction and descent conditions (provenance-blind).

---

## Boundary

- This test uses only honest (non-conflicting, non-Byzantine) record propagation.
  Conflicting records (where observers disagree on record content) are T55's territory.

- The test considers propagation topology (who-tells-whom) and full provenance
  (labeled propagation). It does not consider signed provenance (cryptographic attestation).

- The test does not model propagation of events themselves (only records). Whether
  FinaliEvent identity propagates alongside records is an open question.

- Whether propagation edges are D1RestrictionMorphisms is left open. Propagation
  preserves obstruction status (post-finality → post-finality) rather than crossing
  the finality boundary (pre- to post-finality). The morphism type may differ.

---

## Run Command

```
python -m models.run_t55b
```
