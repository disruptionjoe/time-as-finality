# Boundary Duality and H¹ Reconstruction Failure

**Status:** investigation complete — recommendation: two-form schema, not unified H¹ principle
**Date:** 2026-06-19
**Depends on:** T19, T63, T65, T56, T58 (both variants)
**Question:** Are T19 and T65 two witnesses of the same structure — H¹ as the universal
signature of bounded reconstruction failure across causal boundaries?

---

## Executive Summary

They are not the same structure. T19 and T65 share a causal-boundary explanation but
are formally distinct obstruction types:

- **T19** is an **H⁰ accessibility failure**: a global fact exists and is recorded externally,
  but the bounded observer cannot access the witnesses due to temporal causal ordering.
  The cover is linear (A*(R) ⊂ G). H¹ = 0 by Mayer-Vietoris.

- **T65** is an **H¹ existence obstruction**: no globally consistent LC assignment exists.
  The cover is cyclic (4-context CHSH cycle). H¹(4-cycle, Z/2Z) = Z/2Z ≠ 0.
  The non-trivial class captures the impossibility of globally patching local sections.

Both arise from causal boundaries, but different aspects of causality produce different
obstruction degrees. H¹ is not the universal signature of causal-boundary failure.

The correct principle: **cover cycle topology is the source of H¹ obstructions.** Causal
boundaries can enforce cycle topologies (T65: spacelike separation forces a cyclic context
cover), but they can also produce linear covers (T19: temporal ordering produces nested
accessibility sets, no cycle). And cycles can arise without causal boundaries (PO1:
structural information loss in projection).

---

## 1. Comparison Table: T19 vs T65

```
+--------------------------+------------------------------------------+------------------------------------------+
| Aspect                   | T19 (Phenomenal Bridge)                  | T65 (CHSH Holonomy)                      |
+--------------------------+------------------------------------------+------------------------------------------+
| Obstruction degree       | H^0 (accessibility failure)              | H^1 (existence obstruction)              |
| Global fact status       | EXISTS externally; inaccessible to R     | DOES NOT EXIST for any LC mechanism      |
| Cover topology           | Linear: A*(R) subset G                  | Cyclic: 4-context CHSH cycle             |
| H^1 of the cover         | 0 (two-element cover, Mayer-Vietoris)   | Z/2Z (4-cycle, Cech computation)         |
| Causal boundary type     | Temporal: R's future                    | Spatial: spacelike separation            |
| Formal test              | accessible_support(R_self_finality) = 0 | holonomy(quantum section) = -1           |
| What local region has    | R_obs records, world_fact records       | a_i (Alice's outcome), b_j (Bob's)       |
| What local region lacks  | R_self_finality witnesses               | P(a,b|x,y) joint distribution            |
| Why local region lacks it| Witnesses are in R's causal FUTURE      | Joint info is in NEITHER party's region  |
| Reconstruction failure   | R cannot ACCESS the global fact         | No global fact EXISTS to LC mechanism    |
| Logical form             | exists x. externally_true(x) AND        | NOT exists f. globally_consistent(f)     |
|                          |   NOT internally_accessible(R, x)       |                                          |
| Formal relative          | H^0 section mismatch (T56/T58 gap)     | Cech H^1 = Z/2Z (T63 direct computation)|
| Physical mechanism       | Causal ordering: past cannot access     | Spacelike: neither party has joint info  |
|                          |   its own future                        |   at measurement time                    |
+--------------------------+------------------------------------------+------------------------------------------+
```

### The structural gap

For T19 to be H¹, we would need local sections on overlapping subgraphs that are
locally compatible but globally incompatible. But A*(R) ⊂ G means:
- "Section on A*(R)": R_self_finality inaccessible → value 0
- "Section on G": R_self_finality accessible externally → value 1
- "Overlap A*(R) ∩ G = A*(R)": restriction of G-section to A*(R) = 0 (same as A*(R)-section)

The two sections ARE compatible at the overlap (both give 0). There is no 1-cochain
mismatch. H¹ = 0. The failure is H⁰: the global section takes value 1 on G, while
the local accessible region A*(R) gives value 0. These are different RESTRICTIONS, not
incompatible sections.

For T65, the 4-cycle cover {A0B0 → A0B1 → A1B1 → A1B0 → A0B0} has:
- Local sections on each context (outcome pairs)
- Compatibility on overlapping contexts (shared settings)
- The cycle holonomy = product of all 4 transition functions = -1 for quantum sections
- A non-coboundary 1-cochain (holonomy ≠ 0 in Z/2Z) → non-trivial H¹ class

---

## 2. Survey of Other Tests

### T56 and T58 (Gap-Phantom Equivalence)

T56 found: H¹ = 0 for the apparent finality presheaf F over a sparse 3-observer cover.
The phantom incomparability (a pair globally ordered but locally incomparable because an
intermediary is hidden) is an H⁰ phenomenon — specifically, H⁰(G) where G = A - F is
the gap presheaf.

T58 (Bell-H¹) found:
- Distribution presheaf over R-modules: H¹ = 0 (too flasque; any 1-cochain is a
  coboundary)
- Sheaf-of-sets (Abramsky-Brandenburger 2011): H¹ ≠ 0. The correct mathematical home is
  categorical cohomology of the sheaf of deterministic outcome functions, not Cech H¹ of
  a sheaf of abelian groups
- The classical Bell bound 2 emerges as the global-section threshold (Fine's theorem)
- The Tsirelson bound 2√2 does NOT emerge without importing QM structure

T58 Distributed Contextuality (three-angle investigation, Agent 3):
- Alice's sub-cover: H¹ = 0 (contractible; 2 contexts with one overlap)
- Bob's sub-cover: H¹ = 0 (contractible; 2 contexts with one overlap)
- Combined 4-context cover: H¹ ≠ 0
- Obstruction site: B-setting overlaps {B0, B1} that cross the inter-observer boundary

This is the clearest evidence for the medium-form thesis: the H¹ obstruction appears
precisely at the CYCLE boundary crossing, not at any single observer's boundary.

### T63 (Cech H¹ Direct Computation)

H¹(4-cycle, Z/2Z) = Z/2Z confirmed by simplicial cohomology. This is the fundamental
computation:
- |C⁰| = 4 elements (function from 4 vertices to Z/2Z)
- |ker(δ)| = 2 (constant functions)
- |B¹| = |image(δ)| = 8 (coboundaries)
- |Z¹| = 16 (all 1-cochains are cocycles because C² = 0 from empty triple overlaps)
- |H¹| = 16/8 = 2 → H¹ = Z/2Z

The quantum majority-outcome section has holonomy = -1 = non-trivial generator of Z/2Z.
All LC sections have holonomy = +1 = trivial class.

T63 also identifies the T58 distinction: the correct obstruction for deterministic sections
is the abstract Z/2Z holonomy; for probabilistic sections it requires the sheaf-of-sets
framework of Abramsky-Brandenburger.

### T19 (Observer Closure and Phenomenal Bridge)

The T60 + T19 pair provides:
- T60: observer closure is structurally guaranteed (R's accessible set includes R itself)
- T19: R cannot self-verify its finalization (witnesses are in causal future)

T19 correctly places the obstruction at the causal-future boundary, but this is an
accessibility/H⁰ failure, not H¹. The formal test (accessible_support = 0) is the
direct H⁰ computation.

### Observer-Colimit Tests (T51-T54)

Phantom incomparability (T51: bounded observer misses the intermediary event e_k and sees
e_j, e_i as incomparable when they are ordered) is:
- H⁰(G) where G = A - F (gap presheaf)
- NOT H¹
- The causal mechanism: observer's accessible subgraph omits e_k, which is in the observer's
  causal past but not accessed

This is the same structure as T19: linear cover, H⁰ failure, global fact exists but
bounded region misses it.

### T64 and T66 (Detector Calibration)

Threshold-sensitivity and provenance underdetermination in detector models. These are
not H¹ or H⁰ in the causal-boundary sense — they are underdetermination problems
about which physics determines D1 calibration. No cover structure applies.

### PO1 (T29-T35)

The PO1 gluing obstruction (a parity-conflicting binary CSP) has H¹-type structure
(no global section) but arises from structural information loss in projection (forgotten
structure AC5), not from causal boundaries. This is an H¹ obstruction WITHOUT a
causal-boundary explanation.

---

## 3. General Boundary-Reconstruction Schema

```
+--------------------------+--------------------+-----------------------------+
| Cover topology           | Obstruction degree | Mechanism                   |
+--------------------------+--------------------+-----------------------------+
| Linear: A subset B       | H^0                | Global section exists;      |
|                          | (accessibility)    | bounded A cannot access     |
|                          |                    | witnesses outside A         |
+--------------------------+--------------------+-----------------------------+
| Cyclic: A -> B -> ... -> A| H^1               | No global section exists;   |
|                          | (existence)        | cycle forces incompatibility|
|                          |                    | across the cover            |
+--------------------------+--------------------+-----------------------------+
| No cover cycle, dense    | H^0 or 0           | Flasque sheaves; no         |
| real-valued stalk        |                    | obstruction                 |
+--------------------------+--------------------+-----------------------------+
```

**Causal boundary → cover topology:**

| Causal boundary type | Typical cover topology | Obstruction |
|---------------------|------------------------|-------------|
| Temporal (A*(R) ⊂ G) | Linear (R's past ⊂ full graph) | H⁰ |
| Spacelike (Alice/Bob) | Cyclic if contexts alternate between parties | H¹ |
| Observer-colimit (T51) | Linear (observer ⊂ full record set) | H⁰ |
| Distributed (T58) | Cyclic (B-settings cross inter-observer boundary) | H¹ |

**H¹ obstruction → cover must be cyclic:** This is the key topological requirement.
A cycle in the cover nerve (contexts arranged in a loop) generates H¹ ≠ 0. Causal
boundaries can enforce cyclic context covers when measurement settings alternate between
spacelike-separated parties. But not all causal boundaries do this (temporal boundaries
produce nested accessibility sets, not cycles).

---

## 4. Candidate Theorem Statements

### Strong Form (REJECTED)

**Claim:** H¹ is the obstruction class of bounded reconstruction across causal boundaries.

**Refutation:** T19 is a causal-boundary failure (temporal boundary) with H¹ = 0.
T19 has a linear cover (A*(R) ⊂ G), not cyclic. The obstruction is H⁰. The strong
form conflates the causal boundary (explanation) with H¹ (fingerprint). H¹ requires
cycle topology; temporal causal boundaries produce nested sets, not cycles.

### Medium Form (SUPPORTED — promote to theorem candidate)

**Claim:** Spacelike causal boundaries that force measurement contexts to cycle between
bounded regions produce H¹(context cover, Z/2Z) ≠ 0. Temporal causal boundaries that
produce nested accessibility sets (A*(R) ⊂ G) produce H⁰ failure. The degree of
cohomological obstruction is determined by the topology of the induced cover, not
by the presence of a causal boundary alone.

**Formal version:**
Let C be a context cover over a region divided by a causal boundary B. If:
(a) contexts alternate between regions separated by B (cyclic nerve), then H¹(C, Z/2Z) ≠ 0
    is possible and quantum sections will occupy the non-trivial class.
(b) one region is contained in the other's causal past (linear nerve), then H¹ = 0 and any
    reconstruction failure is H⁰ (accessibility-type).

**Support:**
- T65: spacelike separation enforces cyclic CHSH context cover → H¹ ≠ 0 (T63)
- T58 distributed contextuality: B-setting overlaps cross inter-observer boundary → H¹ ≠ 0
- T19: temporal ordering enforces A*(R) ⊂ G → H¹ = 0, H⁰ failure
- T51-T54: observer-colimit with accessible ⊂ full record → H¹ = 0, H⁰ failure (gap presheaf)

### Weak Form (SUPPORTED — already known, less interesting)

**Claim:** Some TaF reconstruction failures correlate with causal-boundary inaccessibility.
H¹ is one fingerprint when the cover has cyclic topology, and H⁰ is the fingerprint when
the cover is linear. Both arise from bounded causal access, but through topologically
distinct mechanisms.

**Note:** This is essentially what T63/T65 and T19 already established. The medium form
adds the specific topological condition (cycle vs linear) that predicts the obstruction degree.

### Negative Form (ALSO SUPPORTED — limits the principle)

**Claim:** H¹ obstructions can arise without causal boundaries (PO1 structural information
loss), and causal boundaries can produce failures without H¹ (T19 temporal boundary). H¹ is
neither necessary nor sufficient for causal-boundary obstruction.

**Support:**
- PO1: H¹-type gluing obstruction from structural information loss, no causal boundary
- T19: causal boundary (temporal) with H¹ = 0, only H⁰ failure

---

## 5. Counterexample Search Results

### Causal boundary without H¹

**T19 (temporal boundary, H⁰ failure):**
The strongest counterexample. R's observable horizon (e_R_final) is a genuine causal
boundary. Yet H¹ = 0 for the cover {A*(R), G}. The obstruction is H⁰: R cannot access
R_self_finality witnesses, which are in R's causal future.

**T51-T54 (observer-colimit, H⁰ failure):**
Phantom incomparability is a bounded-access failure. Observer accesses only a subset of
the full record set. Cover = {observer's subgraph, full record graph}. H¹ = 0 (two-element
cover). Gap presheaf G = A - F captures the failure at H⁰ level.

### H¹ without causal boundary

**PO1 (T29-T35, structural information loss):**
The PO1 gluing obstruction is a parity-conflicting binary CSP. Local sections
(partial HV assignments) exist for each context but cannot be patched into a global
assignment. This is formally equivalent to H¹ ≠ 0 in the appropriate sheaf. But the
obstruction arises from named forgotten structure (AC5: structured information lost in
projection) — not from spacelike separation or temporal ordering. The mechanism is
information-theoretic (lossy projection), not causal.

### H¹ with cyclic cover but trivial obstruction

**T58 Boolean variant:**
The parity constraint cochain c over Z/2Z has holonomy = 0 (even number of alternating
terms sum to 0 mod 2 for the Boolean CHSH encoding used). The 1-cochain IS a coboundary.
H¹ = 0. A cyclic cover with the wrong coefficient encoding produces trivial H¹ even when
the physical system is contextual. Cover topology alone is necessary but not sufficient —
the right coefficient group and stalk definition are also required.

**Lesson:** The H¹ obstruction requires: (1) cyclic cover, (2) correct coefficient group
(Z/2Z for binary outcomes, Z for integer-valued, R for continuous — but R makes the sheaf
flasque), (3) sections in the non-trivial class. The T58 Boolean variant failed condition (3).

### Summary of counterexamples

```
+----------------------------------+------------------+--------------------+
| Case                             | Causal boundary? | H^1?               |
+----------------------------------+------------------+--------------------+
| T65 (quantum CHSH)               | YES (spatial)    | YES                |
| T19 (phenomenal bridge)          | YES (temporal)   | NO (H^0 failure)  |
| T51-T54 (observer-colimit)       | YES (local access)| NO (H^0 failure)  |
| PO1 (structural projection)      | NO               | YES (cover cycle)  |
| T58 Boolean variant              | YES (spatial)    | NO (wrong coeff.)  |
+----------------------------------+------------------+--------------------+
```

**Finding:** Causal boundary and H¹ obstruction are NOT equivalent. Neither implies the other.
The correct mediating factor is **cover topology** (cyclic vs linear).

---

## 6. Formal Separation: Accessibility vs Existence

The T19/T65 split maps precisely onto a classical distinction in cohomology:

**Accessibility failure (H⁰ type):**
The global section s ∈ H⁰(G, F) exists but cannot be obtained by restricting to the
bounded subregion A: ρ(s)|_A ≠ what A can locally compute.

In T19: the global finality assignment exists (external observer sees R_self_finality = YES)
but ρ(s)|_{A*(R)} = 0 because R_self_finality witnesses are not in A*(R).

This is H⁰ of the gap presheaf: H⁰(A*(R), G) where G = accessibility - apparent finality.

**Existence obstruction (H¹ type):**
There is no global section: H⁰(G, F) = ∅ for the relevant sheaf of deterministic
assignments. Local sections exist on each context but the obstruction to patching them
is a class in H¹(G, F) ≠ 0.

In T65: no LC global assignment exists. The obstruction is in H¹(CHSH cover, Z/2Z) = Z/2Z.
Quantum sections occupy the non-trivial generator.

**The deep distinction:**
- Accessibility failure: "the answer is there, but I can't reach it"
- Existence obstruction: "the answer cannot exist in my framework"

Both are "reconstruction failures" but they have different logical structure, different
mathematical signatures, and different physical implications.

---

## 7. Recommendation

### Do not unify T19 and T65 under a single H¹ principle

They are formally distinct. Unification would require forcing T19's H⁰ structure into H¹
language, which obscures the correct mathematical statement and produces wrong predictions
(e.g., "temporal causal boundaries should also give H¹ obstructions" — they don't).

### Adopt the two-form schema as the organizing principle for TaF's H-branch

**Form 1 — H⁰ Accessibility Failure (T19 type):**
Applicable when: a global fact is recorded externally; the bounded observer cannot access
the witnesses due to temporal causal ordering or local access limitations.
Cover topology: linear (bounded region ⊂ full graph).
Formal signature: H⁰(bounded region, gap presheaf) — as developed in T56, T57, T58 gap-phantom.
Physical examples: T19 (phenomenal bridge), T51-T54 (phantom incomparability).

**Form 2 — H¹ Existence Obstruction (T63/T65 type):**
Applicable when: no global assignment consistent with local observations can exist.
Cover topology: cyclic (contexts form a loop in the cover nerve).
Formal signature: H¹(context cover, Z/2Z) ≠ 0 — as computed in T63, exhibited in T65.
Physical examples: Bell/CHSH violation, distributed contextuality (T58), any scenario where
contexts alternate between spacelike-separated bounded regions.

### Promote the medium-form theorem to the next test target

**Medium-form theorem (T66-next candidate):**
"For a context cover where (a) the nerve is a cycle and (b) the contexts alternate between
bounded regions separated by a causal boundary, the H¹ obstruction (T63/T65) is not merely
a topological artifact but is forced by the causal structure: no causal mechanism can produce
a globally consistent assignment because the joint information required is inaccessible from
any bounded region in the cover."

This would unify T65's causal reduction claim with the Distributed Contextuality finding
from T58, and distinguish the class of H¹ obstructions that arise from causal boundaries
from those that arise from structural information loss (PO1).

### Keep H¹ and H⁰ as separate branches of the reconstruction-failure program

The H⁰ branch (accessibility, linear covers) is productive: T56/T57/T58 gap-phantom program,
observer-colimit descent (T51-T54). This branch addresses temporal causality and bounded access.

The H¹ branch (existence, cyclic covers) is the Bell-violation branch: T63, T65, T58-Bell-H¹.
This branch addresses spacelike causality and contextuality.

They share a family resemblance (both are about reconstruction failure from bounded regions)
but require different tools and have different physical implications.

### The H¹ branch organizing principle (revised)

Not: "H¹ is the signature of causal-boundary reconstruction failure."

Correct: "H¹ is the signature of cyclic-cover existence obstruction. Causal boundaries that
enforce cyclic context topologies (spacelike separation, distributed contextuality) produce H¹
obstructions. Temporal causal boundaries and access limitations produce H⁰ failures on the
gap presheaf. Both are physically real phenomena with precise mathematical signatures."

---

## Open Questions

1. **Does every cyclic context cover crossing a spacelike boundary give H¹ ≠ 0?**
   (Medium-form theorem, not yet proved in general.)

2. **Is there a unified sheaf framework that places H⁰ and H¹ failures as degrees of
   the same cohomology theory?** (Arguably yes via the long exact sequence H⁰ → H⁰ → H¹
   for a pair of sheaves, but this has not been computed for TaF's specific objects.)

3. **Can the T58 Tsirelson bound (2√2) emerge from finality-presheaf structure without
   importing QM?** (Currently requires importing quantum amplitude structure. Open.)

4. **Is T19's temporal boundary obstruction the degree-0 case of a more general degree-n
   causal-boundary cohomology?** (Speculative: temporal boundary → H⁰, spatial boundary
   cycle → H¹, higher-order cycle structures → H²? Not explored.)

5. **Do PO1 obstructions have a causal-boundary interpretation?** (The information-loss
   mechanism in projection is structurally different from causal ordering, but both involve
   "forgetting." Investigate whether AC5 maps onto an access-boundary condition.)
