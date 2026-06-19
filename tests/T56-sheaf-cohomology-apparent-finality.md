# T56: Sheaf Cohomology of Apparent Finality — Test Specification

## Hypothesis Under Audit

**Attempt to realize phantom incomparability as an H¹ obstruction of an apparent-finality presheaf over a finite observer cover.**

The construction is treated as a research hypothesis. The audit tests which of four outcomes holds:
1. **SUCCESS** — H¹ works cleanly as the invariant
2. **PARTIAL_SUCCESS** — parts work, but a different invariant degree is needed
3. **FAILURE_ASSUMPTION** — construction is circular (imports temporal structure)
4. **FAILURE_MISMATCH** — Čech cohomology is the wrong tool entirely

## Formal Objects

### Events (hidden-intermediary witness)
| Event | source_records | target_records | causal | info |
|-------|----------------|----------------|--------|------|
| e_j   | ∅              | {r1}           | 1      | 1    |
| e_k   | {r1}           | {r2}           | 2      | 2    |
| e_i   | {r2}           | {r3}           | 3      | 3    |

**Global record-dependency order:** e_j ≤ e_k ≤ e_i (and transitively e_j ≤ e_i)

### Observer Cover (sparse — patches pairwise incomparable)
| Patch  | accessible_records | accessible_events | F(U)          | A(U) = ρ_U(S_global) |
|--------|--------------------|-------------------|---------------|----------------------|
| U_P    | {r1, r3}           | {e_j, e_i}        | ∅             | {(e_j, e_i)}         |
| U_A    | {r1, r2}           | {e_j, e_k}        | {(e_j, e_k)}  | {(e_j, e_k)}         |
| U_B    | {r2, r3}           | {e_k, e_i}        | {(e_k, e_i)}  | {(e_k, e_i)}         |

*All non-reflexive pairs shown. F(U) = locally-computed apparent order; A(U) = global restricted.*

**Phantom pair:** (e_j, e_i) at U_P — globally ordered (via e_k), locally incomparable (e_k hidden).

**Pairwise overlaps (all have ≤ 1 accessible event, so trivial order data):**
- U_P ∩ U_A = {r1} → accessible: {e_j} only
- U_P ∩ U_B = {r3} → accessible: {e_i} only
- U_A ∩ U_B = {r2} → accessible: {e_k} only

## Expected Results

### Presheaf Analysis
| Property | Expected | Reason |
|----------|----------|--------|
| A is functorial | TRUE | Restricting a global object is always consistent |
| F is a presheaf (closure) | FALSE | F(U_all) restricted to U_P-accessible events ⊃ F(U_P) |

### Section Compatibility
| Property | Expected | Reason |
|----------|----------|--------|
| {F(U_i)} compatible with S_global | FALSE | F(U_P) ≠ A(U_P) — phantom pair (e_j, e_i) missing |
| A(U_i) = ρ_{U_i}(S_global) is self-compatible | TRUE | By construction |

### Čech H¹ (sparse cover)
| Quantity | Expected | Reason |
|----------|----------|--------|
| dim(C¹) | 0 | All pairwise overlaps have ≤ 1 event → no non-reflexive pairs |
| dim(H¹) for apparent F | 0 | C¹ = 0 ⇒ H¹ = 0 |
| dim(H¹) for ambient A | 0 | A is globally consistent |
| Phantom pair in H¹ | FALSE | No C¹ capacity to host phantom pairs |

### Dense Cover Supplemental
| Property | Expected | Reason |
|----------|----------|--------|
| U_P ∩ U_full accessible events | 2 | U_P ∩ U_full = U_P = {r1,r3} → sees e_j and e_i |
| Phantom still detected at U_P | TRUE | U_full sees all, U_P still has phantom |

### Assumption Ledger
| Entry | circular_risk | status |
|-------|---------------|--------|
| arrow_direction | MEDIUM | definitional |
| record_dependency_order | MEDIUM | definitional |
| accessible_records | LOW | definitional |
| accessible_events | LOW | definitional |
| apparent_finality_order | MEDIUM | definitional |
| ambient_presheaf | LOW | derived |
| f_not_presheaf | NONE | derived |
| gap_presheaf | NONE | conjectural |
| observer_cover | NONE | definitional |
| z2_encoding | NONE | definitional |

**No HIGH circular risk entries** — construction does not collapse under W4 (arrow direction is MEDIUM only).

### Audit Outcome
**PARTIAL_SUCCESS**

## Scientific Content

**What works:** The sheaf language is the right framework. The ambient presheaf A is well-defined. Phantom incomparability is detected as G(U) = A(U) \ F(U) — the gap between what the colimit restricts to at U and what U computes locally. The colimit is confirmed as a global section of A.

**What doesn't work (at this level):** H¹ is at the wrong cohomological degree. The phantom pairs live in the section-compatibility mismatch (H⁰ level), not in a cocycle-that-is-not-a-coboundary (H¹). The sparse cover's pairwise overlaps have trivial order data, so dim(C¹) = 0 and H¹ = 0 vacuously.

**Refined hypothesis:** The correct invariant is H⁰(G), the global sections of the gap presheaf G = A/F, not H¹(F).

## Open Questions

1. Is H⁰(G) ≅ the set of phantom incomparability witnesses from T51–T52?
2. Is the sheafification of F equal to A (the ambient presheaf)?
3. Can the pre-presheaf structure of F be captured by Čech cohomology of the NERVE?
4. Does the medium circular risk on arrow direction have a constructor-theoretic resolution?

## Run Command

```bash
python -m pytest tests/test_sheaf_cohomology_apparent_finality.py -v
python -m models.run_t56
```

## Dependencies

- T48 (record-dependency order, FinaliEvent concept — via inherited definitions)
- T51/T52 (phantom incomparability phenomenon being analyzed)
- T55B (accessible records, propagation structure — concepts inherited)
- No direct code imports from T48/T54/T55B (self-contained)

## Boundary

Does not claim: H¹ = 0 in all covers. The dense cover {U_P, U_full} may have non-trivial H¹ if the C¹ slot for the phantom pair is occupied. This is left as Q3.

Does not address: the W4 circular risk resolution (left as Q4 / candidate T56B).
