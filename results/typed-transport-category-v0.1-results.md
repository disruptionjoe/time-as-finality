# Typed Transport Category v0.1 Results

**Test:** T41 — Typed Transport Category Prototype
**Date:** 2026-06-18
**Status:** Implemented — two theorems earned

---

## Category Law Results

| Law | Tests Run | Tests Passed | Holds |
| --- | --- | --- | --- |
| Associativity | 4 | 4 | Yes |
| Left unit | 5 | 5 | Yes |
| Right unit | 5 | 5 | Yes |

**Forms proper category: True**

### Associativity Tests

| Test | site_map assoc. | dims assoc. | Holds |
| --- | --- | --- | --- |
| all_dims: (f1;g1);h1 == f1;(g1;h1) | Yes | Yes | Yes |
| mixed_dims: (f2;g2);h2 == f2;(g2;h2) | Yes | Yes | Yes |
| minimal_dims: (f3;g3);h3 == f3;(g3;h3) | Yes | Yes | Yes |
| with_identity: (id_A;f1);g1 == id_A;(f1;g1) | Yes | Yes | Yes |

### Identity Law Tests (Left Unit)

| Morphism | id;f == f |
| --- | --- |
| f1_A_B (all dims) | Yes |
| f2_A_B (AS+HR) | Yes |
| f3_A_B (AS only) | Yes |
| g1_B_C | Yes |
| h1_C_D | Yes |

### Identity Law Tests (Right Unit)

| Morphism | f;id == f |
| --- | --- |
| f1_A_B (all dims) | Yes |
| f2_A_B (AS+HR) | Yes |
| f3_A_B (AS only) | Yes |
| g1_B_C | Yes |
| h1_C_D | Yes |

---

## PO1 Functor Test

| Morphism | PO1? | Failed conditions |
| --- | --- | --- |
| f: SRC→MID | No | AC6 (MID not obstructed) |
| g: MID→TGT | No | AC5 (no declared forgotten structure) |
| f;g: SRC→TGT | **Yes** | none |

Boolean-AND predicts PO1(f;g): False
Actual PO1(f;g): True
**Functor law violated: Yes**

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
| --- | --- | --- |
| H_A | D1RestrictionMorphisms form a proper category | best_supported |
| H_B | Associativity holds but identities are external/missing | partially_supported |
| H_C | PO1 admissibility is not a Boolean functor on D1Cat | best_supported |

**Best supported:** H_A (proper category)

---

## Theorems Earned

### Typed Transport Category Theorem (T41)

D1RestrictionMorphisms under `_compose_morphisms`, with identity morphisms
constructed by `make_identity()`, form a proper category.

- **Associativity:** proved by function-composition associativity (site_map is
  sequential function application; associativity is then trivial) and
  set-intersection associativity (preserved_dims uses `∩`; set intersection is
  associative).
- **Identity morphisms:** `make_identity(A)` maps each site to itself and
  preserves all four D1 dimensions. Left and right unit laws hold because:
  - Left: `id_A;f` has site_map `{s → f(s) : s ∈ A}` = f's site_map, and
    preserved_dims `D1_DIMS ∩ f.dims = f.dims`.
  - Right: `f;id_B` has site_map `{s → id_B(f(s)) = f(s) : s ∈ A}` = f's
    site_map, and preserved_dims `f.dims ∩ D1_DIMS = f.dims`.

### PO1 Non-Functor Theorem (T41)

PO1 admissibility is not a Boolean functor from D1Cat to {True, False}.

Witness: f: SRC→MID fails PO1 (AC6 fails — no target obstruction); g: MID→TGT
fails PO1 (AC5 fails — no declared forgotten structure); f;g: SRC→TGT is PO1
(AC5 passes via accumulated forgotten structure, AC6 passes via TGT's gluing
conflict, AC7 passes via SRC's satisfiability).

Boolean-AND functor would predict PO1(f;g) = PO1(f) ∧ PO1(g) = False.
Actual: True. Functor law violated.

This is the T34 PO1 Chain Theorem restated in categorical language: endpoint
admissibility is determined by the endpoint pair, not by intermediate
admissibility.

---

## Boundary

Category structure is proved for D1RestrictionMorphisms as constructed here.
The result does not extend automatically to:

1. Presheaves or sheaves (H2) — these require additional structure.
2. General categorical tools (limits, colimits, adjunctions) — require further development.
3. Morphisms with `require_trust_path_preservation=True` or
   `require_obstruction_preservation=True` — their behavior under composition is
   not yet characterized.
4. The identity morphism constructor `make_identity()` is external to
   `_compose_morphisms`; it cannot be derived from composition alone (this is
   expected for any category).

---

## Independence Audit Update

T41 resolves the "Own operations: Present but INCOMPLETE" status in the
Mathematical Independence Audit. The composition law (associativity) is now
formally established. Identity morphisms are now defined. D1RestrictionMorphisms
form a proper category.

Updated status: **Own operations: Present and COMPLETE (T41).**

---

## Machine-Readable Output

Full structured output in `results/typed-transport-category-v0.1.json`.
