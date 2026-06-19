# T55B Results: Provenance-Aware Reconstruction Separation Audit

**Date:** 2026-06-19  
**Model:** `models/provenance_aware_reconstruction.py`  
**Runner:** `models/run_t55b.py`  
**Output:** `results/provenance-aware-reconstruction-separation-v0.1.json`

---

## Scenarios

### A1 (direct propagation)

| Observer | Edge | Records | Step |
|----------|------|---------|------|
| A → C | direct | {r1_locked} | 1 |
| B → C | direct | {r2_locked} | 2 |

Origins: A observes r1_locked; B observes r2_locked.

### A2 (transitive propagation)

| Observer | Edge | Records | Step |
|----------|------|---------|------|
| A → B | first hop | {r1_locked} | 1 |
| B → C | second hop | {r1_locked, r2_locked} | 2 |

Origins: A observes r1_locked; B observes r2_locked.

### B1 and B2 (same topology, different content)

Both: topology P→R (step=1), Q→R (step=2).

| Scenario | P origin | Q origin | R accessible |
|----------|---------|---------|-------------|
| B1 | r_alpha_locked | r_beta_locked | {r_alpha_locked, r_beta_locked} |
| B2 | r_gamma_locked | r_delta_locked | {r_gamma_locked, r_delta_locked} |

---

## Observer States

| Observer | Scenario | Accessible Records | Provenance Paths |
|----------|----------|--------------------|------------------|
| C | A1_direct | {r1_locked, r2_locked} | r1_locked: A→C (1-hop); r2_locked: B→C (1-hop) |
| C | A2_transitive | {r1_locked, r2_locked} | r1_locked: A→B→C (2-hop); r2_locked: B→C (1-hop) |
| R | B1_alpha_beta | {r_alpha_locked, r_beta_locked} | r_alpha: P→R; r_beta: Q→R |
| R | B2_gamma_delta | {r_gamma_locked, r_delta_locked} | r_gamma: P→R; r_delta: Q→R |

---

## Separation Witnesses

### W_A (H1 test)

| Property | Value |
|----------|-------|
| same_record_basis | **True** |
| same_provenance_structure | **False** |
| Finding | SEPARATION CONFIRMED |

C's record basis is identical in A1 and A2. C's provenance paths differ (direct vs transitive
delivery of r1_locked). Record basis does not determine provenance. **H1 supported.**

### W_B (H2 partial test)

| Property | Value |
|----------|-------|
| same_topology | True |
| same_record_basis | **False** |
| Finding | TOPOLOGY-CONTENT SEPARATION |

R's record basis differs between B1 and B2 despite identical abstract topology.
Abstract propagation topology cannot determine record basis. **H2 partial.**

---

## Colimit Comparison (W_A scenarios)

| Scenario | Accessible Records | Event Order (non-refl) | AM Holds |
|----------|--------------------|------------------------|----------|
| A1_direct | {r1_locked, r2_locked} | [] (e1 \|\| e2) | True |
| A2_transitive | {r1_locked, r2_locked} | [] (e1 \|\| e2) | True |

**Colimit orders identical: True.**

Same record basis → same event-finality order → same AM result, regardless of provenance.

---

## W_D: Propagation Order vs Event-Finality Order

C's accessible records: {r1_locked, r2_locked}  
Propagation step-order: r1_locked at step=1, r2_locked at step=2

| Event Structure | Non-reflexive order | Compatible with propagation history? |
|----------------|---------------------|--------------------------------------|
| E_concurrent (e1 \|\| e2) | [] | **Yes** |
| E_ordered (e1 ≤ e2) | [(e1, e2)] | **Yes** |

`propagation_order_determines_event_order = False`

The same propagation history is consistent with both a concurrent and a causally ordered
event-finality structure. Propagation step-order does NOT determine event-finality order.

---

## W_T54: T54 Provenance-Blindness

| Property | Value |
|----------|-------|
| basis_identical | **True** |
| t54_input_identical | **True** |

T54's quotient-union consumes record sets and axis profiles only. Same record basis → same
T54 LocalEvent inputs → identical T54 classification in A1 and A2.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
|------------|-------|--------|
| H0 | Provenance ≡ record basis (mutually reconstructible) | **Refuted** |
| H1 | Provenance strictly richer: same basis, different provenances | **Supported** |
| H2 | Provenance topology strictly weaker than record basis | **Partial** |
| H3 | Complementarity: neither fully determines the other | **Partial** |
| H4 | Provenance variation does not affect colimits, AM, or descent | **Supported** |

**Best supported:** H4 and H1. H0 refuted. H2 and H3 partially confirmed (topology form only).

---

## Recommendation

**Provenance is an optional audit layer** for the current TaF event-finality formalism.

Provenance is NOT a first-class mathematical primitive at this stage because:
1. H4 holds: provenance variation does not change event-finality colimits or AM.
2. The global colimit equals the union of origin records — topology adds no information.
3. Propagation step-order is orthogonal to event-finality order.

Provenance may earn first-class status if:
- Propagation timing is formally linked to FinaliEvent anchor ordering, and this implies
  event-finality order in some constrained regime.
- Provenance provides identity evidence resolving T53-type underdetermination.
- A provenance-aware colimit (step-weighted merge) produces a strictly refined event order.

---

## Open Questions

1. Can propagation causal constraints (records propagate only after origin event) link
   step-order to event-finality order?

2. Can provenance serve as identity evidence for T54's C1/C2 descent conditions (event
   identity maps and overlap witnesses)?

3. Is a PropagationEdge a D1RestrictionMorphism? Propagation is post-finality to
   post-finality — distinct from FinaliEvent crossings (pre- to post-finality).

4. Does a step-weighted provenance-aware colimit refine the plain T52/T54 union?
