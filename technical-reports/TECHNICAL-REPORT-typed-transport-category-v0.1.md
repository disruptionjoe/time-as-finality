# Technical Report: Typed Transport Category Prototype (T41)

**Version:** v0.1
**Date:** 2026-06-18
**Depends on:** T26, T31, T34, T37, T38, T39, T40

---

## Summary

T41 asks whether D1RestrictionMorphisms under `_compose_morphisms` form a proper
category. Two theorems are earned:

1. **Typed Transport Category Theorem:** D1RestrictionMorphisms form a proper
   category. Associativity holds. Identity morphisms exist. Unit laws hold.

2. **PO1 Non-Functor Theorem:** PO1 admissibility is not a Boolean functor from
   D1Cat to {True, False}. A composed morphism can be PO1 even when neither
   factor is. This is the T34 PO1 Chain Theorem restated in categorical language.

---

## Background

The Mathematical Independence Audit (post-T40) noted one open item under Own
Operations:

> Composition of D1RestrictionMorphisms (partial — associativity and identity
> morphisms not yet formally established).

T41 closes this. The T26-T40 work has accumulated a composition law
(`_compose_morphisms` in `transport_network.py`), a type system
(D1RestrictionMorphisms with `preserved_dimensions` and `site_map`), and a
collection of theorems. T41 verifies that these objects satisfy the axioms of
a category.

---

## Category Axioms

A category requires:

| Axiom | Requirement |
| --- | --- |
| Objects | A collection of objects |
| Morphisms | For each pair (A, B), a set Hom(A, B) of morphisms |
| Composition | For f: A→B and g: B→C, a morphism g∘f: A→C |
| Associativity | (h∘g)∘f = h∘(g∘f) for all composable triples |
| Identity | For each A, an id_A: A→A |
| Left unit | id_B∘f = f for all f: A→B |
| Right unit | f∘id_A = f for all f: A→B |

The notation used in this report is diagrammatic: f;g means "apply f first,
then g," which corresponds to `_compose_morphisms(f, g)`.

---

## Objects and Morphisms

**Objects:** D1RestrictionSystems. Each carries a finite set of observer sites,
local D1 profiles, transport edges, and optional patch constraints.

**Morphisms:** D1RestrictionMorphisms. Each carries a `site_map` (tuple of
SiteMap pairs), a `preserved_dimensions` tuple (subset of the four D1
dimensions), and two optional preservation requirements
(`require_trust_path_preservation`, `require_obstruction_preservation`).

**Hom-sets:** Hom(A, B) consists of all D1RestrictionMorphisms from A to B.
The size of Hom(A, B) depends on the site structures of A and B; it is finite
and can in principle be enumerated (not done here — open for T42+).

---

## Composition

`_compose_morphisms(f: A→B, g: B→C) → A→C` (from `transport_network.py`):

```python
def _compose_morphisms(f, g):
    f_map = {sm.source_site: sm.target_site for sm in f.site_map}
    g_map = {sm.source_site: sm.target_site for sm in g.site_map}
    composed_site_map = tuple(
        SiteMap(src, g_map[f_map[src]])
        for src in sorted(f_map)
        if f_map[src] in g_map
    )
    f_dims = set(f.preserved_dimensions)
    g_dims = set(g.preserved_dimensions)
    preserved_dims = tuple(d for d in D1_DIMENSIONS if d in f_dims and d in g_dims)
    return D1RestrictionMorphism(
        name=f"composed_{f.name}_{g.name}",
        source=f.source, target=g.target,
        site_map=composed_site_map, preserved_dimensions=preserved_dims,
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )
```

Two components:
- `site_map`: sequential application of f then g (function composition).
- `preserved_dims`: intersection of f's and g's dimensions, filtered through D1_DIMENSIONS.

---

## Identity Morphisms

`make_identity(A: D1RestrictionSystem) → D1RestrictionMorphism`:

```python
def make_identity(system):
    sites = sorted(system.site_ids())
    return D1RestrictionMorphism(
        name=f"id_{system.name}",
        source=system, target=system,
        site_map=tuple(SiteMap(s, s) for s in sites),
        preserved_dimensions=D1_DIMENSIONS,
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )
```

The identity morphism maps every site to itself and preserves all four D1
dimensions. This is the canonical construction; no other choices are available.

---

## Proof of Category Axioms

### Associativity

**Claim:** For all composable f: A→B, g: B→C, h: C→D:
`(f;g);h = f;(g;h)` (modulo morphism name, which is metadata).

**Proof sketch:**

*site_map component:*
- f;g has site_map: `{src → g_map[f_map[src]] : src ∈ sorted(A.sites), f_map[src] ∈ g_map}`
- (f;g);h applies h_map to f;g's targets: `{src → h_map[g_map[f_map[src]]] : ...}`
- f;(g;h) applies the same chain in a different order:
  - g;h has site_map: `{mid → h_map[g_map[mid]] : mid ∈ sorted(B.sites), g_map[mid] ∈ h_map}`
  - f;(g;h) applies g;h to f's targets: `{src → h_map[g_map[f_map[src]]] : ...}`
- Both produce the same mapping: the filter condition `f_map[src] ∈ g_map AND g_map[f_map[src]] ∈ h_map` is identical. ✓

*preserved_dims component:*
- (f_dims ∩ g_dims) ∩ h_dims = f_dims ∩ (g_dims ∩ h_dims) by set-intersection associativity. ✓

*Morphism equality:* both composed morphisms have source=A, target=D, same
site_map (as functions), same preserved_dims (as sets). ✓

**Verified:** 4/4 concrete tests pass (varying dimension subsets, including a
triple containing an identity morphism).

### Identity Laws

**Left unit claim:** `id_A;f = f` (modulo name) for all f: A→B.

*site_map:* id_A's site_map is `{s → s : s ∈ A.sites}`. Composing with f:
`{src → f_map[id_map[src]] = f_map[src] : src ∈ sorted(A.sites)}` = f's
site_map. ✓

*preserved_dims:* id_A has D1_DIMENSIONS (all four); intersecting with f's dims
gives f's dims. ✓

**Right unit claim:** `f;id_B = f` (modulo name) for all f: A→B.

*site_map:* id_B's site_map is `{t → t : t ∈ B.sites}`. Composing f then id_B:
`{src → id_map[f_map[src]] = f_map[src] : src ∈ sorted(A.sites)}` = f's
site_map. ✓

*preserved_dims:* f's dims intersected with id_B's (all four) = f's dims. ✓

**Verified:** 5/5 left unit tests pass, 5/5 right unit tests pass.

---

## PO1 Non-Functor Theorem

### Setup

A functor F: D1Cat → BoolCat would require F(f;g) = F(f) ∧ F(g) for all
composable f, g (under the "Boolean and" composition in BoolCat = {True, False}
with ∧).

### Witness

Three systems:
- **SRC:** 2-site, rich profile (accessible_support=2), no gluing obstruction.
- **MID:** 3-site, restricted profile (accessible_support=1), no obstruction.
- **TGT:** 3-site, restricted profile, **with gluing obstruction**
  (A=B, B=C, A≠C parity conflict).

| Morphism | forgotten | AC5 | AC6 | AC7 | PO1? |
| --- | --- | --- | --- | --- | --- |
| f: SRC→MID | ("type_guarantee",) | passes | **fails** (MID not obstructed) | passes | **No** |
| g: MID→TGT | () | **fails** (empty) | passes | passes | **No** |
| f;g: SRC→TGT | ("type_guarantee",) | passes | passes | passes | **Yes** |

Boolean-AND functor predicts: PO1(f;g) = False ∧ False = **False**.
Actual: PO1(f;g) = **True**. Functor law violated.

### Interpretation

PO1 admissibility is an endpoint property of morphisms in D1Cat. It is
determined by the richer system (source), the restricted system (target), and
the accumulated forgotten structure — not by the admissibility of intermediate
projections. This is the T34 PO1 Chain Theorem in categorical language.

PO1 is not a functor to a Boolean category. Investigating whether PO1 can be
repaired as a lax functor or as a fibration is open.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Verdict |
| --- | --- | --- |
| H_A | D1RestrictionMorphisms form a proper category | **Best supported** |
| H_B | Associativity holds but identity is external/missing | **Partially supported** (misleading framing; identities exist and are canonical) |
| H_C | PO1 is not a Boolean functor on D1Cat | **Best supported** |

H_B is partially supported in that `make_identity` is indeed external to
`_compose_morphisms` — but this is expected. Every category requires an explicit
identity construction. H_B's framing overstates the gap.

---

## Impact on the Mathematical Independence Audit

The audit (post-T40) listed "Own operations: Present but INCOMPLETE" because
associativity and identity morphisms were not formally established.

T41 resolves this:
- Associativity: proved by construction (see above).
- Identity morphisms: canonically defined via `make_identity`.
- Unit laws: proved by construction.

**Updated status: Own operations — Present and COMPLETE.**

The Independence Audit now shows 5/6 criteria fully present and complete,
with "Independent motivation" still requiring external testing.

---

## Open Questions (Not Addressed Here)

1. **Hom-set characterization:** How many morphisms exist between two given
   D1RestrictionSystems? Is Hom(A, B) non-empty for all pairs?

2. **PO1 as lax functor or fibration:** Can PO1 admissibility be repaired into
   a weaker but still functorial structure?

3. **Internal categories:** Are TypedTransportNetworks internal categories in
   D1Cat? (A TypedTransportNetwork is a directed graph of D1RestrictionSystems
   connected by D1RestrictionMorphisms — exactly the data of a small category
   internal to D1Cat if composition and identities are compatible.)

4. **Limits and colimits:** Does D1Cat have products, coproducts, equalizers, or
   other universal constructions?

5. **Finite-to-infinite boundary (T42):** Do the category laws generalize when
   D1RestrictionSystems are allowed to be infinite?

---

## Executable Output

```bash
python -m models.run_t41
```

Results in: `results/typed-transport-category-v0.1.json`

72 tests in `tests/test_typed_transport_category.py`. All pass.
