# H⁰/H¹ Cover Structure Conditions

**Status:** investigation complete
**Date:** 2026-06-19
**Depends on:** T19, T51-T54, T56, T58 (gap + Bell), T59, T63, T65, T37, T39, T40
**Prior investigations:**
- [Boundary Duality and H¹ Reconstruction Failure](boundary-duality-h1-reconstruction-failure.md)
- [Reconstruction Failure Taxonomy](reconstruction-failure-taxonomy.md)

**Question:** What structural properties of the cover determine whether a reconstruction
failure is H⁰ (existence-without-access) or H¹ (local-consistency-without-global-existence)?

---

## Assessment (Lead)

**Cover topology is the primary determinant.** Acyclic nerve → H^n = 0 for n ≥ 1, so all
failures are H⁰. A 1-cycle in the nerve is necessary (not sufficient) for H¹. The cyclic
structure must also carry non-trivial transition functions.

**Physical mechanism follows mathematical structure.** Spacelike causal separation between
observers forces cyclic context covers (T63/T65). Temporal access restriction forces nested
linear covers (T19). Sparse overlaps force vacuous H¹ (T56). The physics determines the
cover; the cover determines the failure type.

**Projection and forgetting do not move the failure type across the H⁰/H¹ boundary by
themselves.** They change which sections exist, not the cover topology. The exception is when
projection induces a topology change on the section space that creates or destroys cycles in
the effective transition structure.

**Type C (Provenance) and Type D (Attribution) are separate branches:** Type C is
pre-cohomological (determines what presheaf to use); Type D is post-cohomological (explains
what caused a known H¹ obstruction). Neither is a refinement of H⁰ or H¹.

---

## Part A: The Two-Form Schema

The taxonomy investigation established two complementary failure forms. This investigation
determines what makes each form occur.

```
H⁰ failure (Type B):
  - Global section EXISTS (in ambient sheaf or external record structure)
  - Observer's accessible cover CANNOT REACH the global section
  - Invariant: H⁰(gap presheaf G = A - F) ≠ 0
  - Characterization: "The answer is there. I cannot reach it."

H¹ failure (Type A):
  - No globally consistent section EXISTS
  - Local sections are pairwise compatible on overlaps
  - They cannot be patched into a global assignment
  - Invariant: H¹(cover, G) ≠ 0
  - Characterization: "No global answer is possible in this framework."
```

---

## Part B: Cover Structural Conditions for H⁰-Only

### Theorem B1 — Acyclic Nerve Implies H^n = 0 for n ≥ 1

**Statement:** Let U = {U_i} be a finite cover of X. If the nerve N(U) is acyclic
(contractible as a simplicial complex), then H^n(X, F) = 0 for every sheaf F and every n ≥ 1
(using Čech cohomology for this cover).

**Consequence:** All reconstruction failures over an acyclic cover are H⁰ failures. No
globally inconsistent section assignment is possible — local sections always stitch.

**Proof sketch:** For a contractible nerve, the Čech cochain complex is acyclic in degrees
≥ 1. The cohomology groups H^n reduce to H^0 (global sections). For a good cover (all
pairwise intersections contractible or empty), this follows directly from the Nerve Theorem.
For finite combinatorial covers, the result holds without Nerve Theorem conditions by explicit
cochain calculation: a contractible simplicial complex has trivial reduced homology, so its
cohomology with any coefficient group is concentrated in degree 0.

**What makes a nerve acyclic:**
- Single-patch cover: trivial (N(U) = point)
- Two-element cover: N(U) is either disjoint points (no overlap) or a line segment
  (one edge). Both are contractible.
- Three-element cover with total containment U₀ ⊂ U₁ ⊂ U₂: N(U) = filled simplex.
  Contractible.
- n-element nested chain: N(U) = tree. Contractible.
- Three-element cover with all pairwise overlaps non-empty AND triple overlap non-empty:
  N(U) = filled triangle = 2-simplex. Contractible.
- Three-element cover with all pairwise overlaps non-empty BUT triple overlap empty:
  N(U) = hollow triangle = 1-cycle (S¹ topologically). H¹ can be non-trivial.

**Key dividing line:** The nerve contains a topological 1-cycle iff the cover's patches form
a cycle with no shared "center" (no element belongs to all patches in the cycle).

---

### Theorem B2 — Two-Element Nested Cover: H¹ = 0 (Mayer-Vietoris)

**Statement:** Let U = {U₀, U₁} with U₀ ⊆ U₁. Then H¹(F) = 0 for any presheaf F.

**Proof:** Mayer-Vietoris exact sequence for the cover {U₀, U₁}:
```
0 → F(U₀ ∪ U₁) → F(U₀) ⊕ F(U₁) → F(U₀ ∩ U₁) → H¹ → ...
```
Since U₀ ⊆ U₁, we have U₀ ∩ U₁ = U₀. The restriction map F(U₀) → F(U₀ ∩ U₁) = F(U₀)
is the identity, which is surjective. So the Mayer-Vietoris map is surjective onto F(U₀ ∩ U₁),
which forces H¹ = 0.

**TaF canonical case (T19):** The T19 cover is {A*(R), G} where A*(R) ⊂ G (R's accessible
subgraph is a subset of the full record graph G). This is exactly the two-element nested case.
H¹ = 0. The failure is H⁰: the global section (finalization certificate for R) exists in G but
R cannot access it because the witnessing records are in R's causal future, outside A*(R).

---

### Result B3 — Sparse Pairwise Overlaps: H¹ = 0 Vacuously

**Statement:** If the pairwise overlaps U_i ∩ U_j have trivial section data (the section
group F(U_i ∩ U_j) is trivial or zero for all pairs), then C¹ = 0 and H¹ = 0 vacuously.

**TaF canonical case (T56):** The T56 cover {U_P, U_A, U_B} has pairwise overlaps each
containing ≤ 1 accessible event. No non-reflexive order pairs exist at any overlap. The
section data at each pairwise overlap is trivial (one-element set or empty). C¹ = 0.
H¹ = ker(δ¹)/im(δ⁰) = 0/0 = 0. Vacuously trivial.

**Why this is H⁰ and not H¹:** The phantom pair (e_j, e_i) is detected as a gap in the
section space of the patch U_P (gap presheaf G(U_P) = A(U_P) \ F(U_P) ≠ ∅). This is a
section-mismatch at a single patch, not a cocycle-that-is-not-a-coboundary. It lives at H⁰
of the gap presheaf G, not H¹ of F.

**Sparse overlap as cover design choice:** T56's cover was chosen to be sparse. A denser
cover where the pairwise overlaps include multiple events could have non-trivial C¹. T56 Q3
(Čech cohomology of the dense cover) is open and may produce H¹ ≠ 0.

---

### Summary of H⁰-Only Conditions

A reconstruction failure is H⁰-only (Type B) when at least one of:
1. The nerve N(U) is acyclic (contractible)
2. The cover is two-element and nested (Mayer-Vietoris kills H¹)
3. All pairwise overlaps have trivial section data (H¹ = 0 vacuously)
4. The global section exists in the ambient structure; accessibility, not existence, fails

All TaF Type B failures (T19, T51-T54, T56, T58-gap) satisfy condition 4 and at least
one of 1-3.

---

## Part C: Cover Structural Conditions for H¹

### Condition C1 — 1-Cycle in Nerve is Necessary

**Statement:** If H¹(cover, G) ≠ 0 for some coefficient group G, then the nerve N(U) contains
a topological 1-cycle.

**Proof:** H¹ is computed from the Čech cochain complex C⁰ → C¹ → C². If N(U) has no
1-cycle (acyclic), then by Theorem B1, H¹ = 0. Contrapositive: H¹ ≠ 0 ⟹ N(U) has a 1-cycle.

**Necessary but not sufficient:** Not every cyclic cover has non-trivial H¹. The transition
functions around the cycle must also be non-trivial. A cyclic cover where every transition
function is identity has H¹ = 0 (the 1-cochain is a coboundary).

---

### Theorem C2 — Holonomy Characterizes H¹ for 4-Cycle Cover

**Statement:** Let U be the CHSH context cover {A0B0, A0B1, A1B1, A1B0} arranged in a
4-cycle. Let G = Z/2Z with multiplication. A 1-cochain f ∈ C¹(U, Z/2Z) is a coboundary iff
its holonomy Hol(f) = Π_{edges in cycle} f(edge) = +1 (identity in Z/2Z).

**Proof (T63, Step 1):** The nerve of the 4-cycle cover is a 1-dimensional simplicial complex
= the graph cycle C₄. There are no triple overlaps (C² = 0). The coboundary map δ⁰: C⁰ → C¹
sends a 0-cochain g (vertex labels) to f(U_i, U_j) = g(U_j)/g(U_i). The holonomy of any
coboundary is +1 (telescope product cancels). Conversely, f with holonomy +1 determines a
globally consistent vertex labeling (proved in T63 by constructing the labeling explicitly).
So: coboundary ⟺ holonomy = +1. The non-coboundaries form H¹(C₄, Z/2Z) = Z/2Z. □

**TaF consequences:**
- Local causality (LC) ⟹ holonomy = +1 (T65, exhaustively verified for all 16 LC sections)
- Holonomy = -1 ⟹ NOT locally causal (contrapositive; Bell's theorem as holonomy)
- Quantum majority-outcome sections have holonomy = -1 (T65, verified at standard angles)
- Biconditional FAILS: holonomy = +1 does not imply LC (128 sections with holonomy = +1; only 16 are LC)

---

### Physical Mechanism: Why Spacelike Separation Forces Cyclic Covers

The CHSH context cover is cyclic because measurement contexts are formed by pairing one of
Alice's settings with one of Bob's. The four settings {A0, A1} × {B0, B1} produce four
contexts {A0B0, A0B1, A1B1, A1B0}. Adjacent contexts share exactly one party's setting:
A0B0 — A0B1 (shared: Alice's A0)
A0B1 — A1B1 (shared: Bob's B1)
A1B1 — A1B0 (shared: Alice's A1)
A1B0 — A0B0 (shared: Bob's B0)

This is a 4-cycle with no "center" (no shared element across all four contexts). The nerve is
S¹ topologically, with H¹(S¹, Z/2Z) = Z/2Z.

The spacelike causal structure enforces this topology: Alice and Bob are spacelike separated,
so no context can contain both parties' joint measurement outcome as locally verifiable data.
The information required to "close" the cycle (joint distribution P(a,b|x,y)) is inaccessible
from any single party's causal region. The cyclic cover is not a design choice — it is forced
by the causal structure of the experiment.

**T58 Distributed Contextuality Theorem:** Alice's 2-context sub-cover {A0B0, A0B1} has
acyclic nerve (line segment) → H¹ = 0. Bob's 2-context sub-cover {A0B0, A1B0} has acyclic
nerve → H¹ = 0. The combined 4-context cover has cyclic nerve → H¹ = Z/2Z. The H¹ obstruction
lives strictly at the inter-observer overlaps {B0, B1} where Alice's and Bob's sub-covers join.

**General principle (candidate):** Spacelike causal separation between observers forces cyclic
multi-observer context covers when each party's measurement setting determines a partial context.
Any such cover has nerve containing a 1-cycle and is a candidate for non-trivial H¹.

---

### Summary of H¹ Conditions

A reconstruction failure may be H¹ (Type A) when:
1. The nerve N(U) contains a topological 1-cycle (necessary)
2. The coefficient group is non-trivial (Z/2Z for binary outcomes; R-modules are too flasque)
3. The transition functions around the cycle are non-trivial (holonomy ≠ identity)
4. Local sections exist on each patch (H¹ measures global consistency, not accessibility)

All TaF Type A failures (T63, T65, T58-Bell, PO1) satisfy all four conditions.

---

## Part D: Projection and Forgetting

### Can Projection Move a Failure from H⁰ to H¹?

The question is whether applying a projection π: P → Q (forgetting structure) can transform
a Type B (H⁰) failure into a Type A (H¹) failure.

**The cover topology argument:**

Projection affects the SECTION SPACE, not the cover topology. If the projection does not
change which covers are used or how they are organized:
- If cover was acyclic before → acyclic after → H¹ = 0 after projection
- If cover was cyclic before → cyclic after → H¹ may still be non-trivial

Projection cannot by itself introduce a cycle into an acyclic cover.

**The section-space argument:**

However, projection can change whether non-trivial 1-cocycles exist:
- Before projection: sections have fine-grained detail; compatibility conditions on overlaps
  are strong; some sections that would be compatible after projection are incompatible before.
- After projection: sections are coarser; previously incompatible sections become compatible
  on overlaps; now a non-trivial 1-cocycle might exist that couldn't before.

**The key subtlety:** To get H¹ ≠ 0 after projection on a previously acyclic cover,
projection would need to create a cycle in the nerve — which cannot happen if the cover is
unchanged. But if projection induces an identification of patches (collapsing U_i and U_j to
the same patch in the projected space), it can create or destroy cycles in the effective cover.

**TaF assessment — PO1 forgetting (AC5):**

In the PO1 typed transport network (T37), forgetting AC5 (reconstruction path) means:
- The cover structure is unchanged (same source, target, intermediate nodes)
- The section space changes (AC5 condition is no longer required)
- Path-dependence: two paths with different AC5 accumulations give different PO1 verdicts

This is not H⁰ → H¹ movement. The PO1 obstruction (H¹-type, gluing obstruction) was
already present. What changes when AC5 is forgotten is the ATTRIBUTION of that obstruction:
without AC5 labeling, we cannot determine which path caused the failure. This is Type D
(attribution underdetermination) applied to an existing Type A obstruction.

**Provisional answer:**
- Projection on an acyclic cover: cannot introduce H¹. H⁰ failures remain H⁰.
- Projection on a cyclic cover: can change which H¹ classes exist, but the failure type
  (H¹) was already possible from the cover.
- The only route from H⁰ → H¹ via forgetting requires a cover-topology change: identifying
  patches in a way that creates a cycle. This is a strong structural operation, not a
  typical typed forgetting step.

**Open target — LossKernel/TF1:** The typed forgetting spine being formalized in TF1/LossKernel
may provide the right formalism to make this analysis precise. If loss morphisms are
cover-topology-preserving (the standard case), they cannot move H⁰ → H¹.

---

### When Projection Destroys H¹

The reverse is possible: projection can eliminate non-trivial H¹ by destroying the structure
that made the transition functions non-trivial.

Example: In T58, the Boolean-variant CHSH encoding (parity constraint) has holonomy = 0
(coboundary). The correct Z/2Z encoding (outcome comparison) has holonomy = -1 (non-trivial).
"Projecting" from outcome-comparison to parity-sum encoding maps H¹ ≠ 0 to H¹ = 0 — not
because the physics changed, but because the coefficient encoding lost the information needed
to detect the obstruction.

This is Type A* (coefficient sensitivity): the H¹ obstruction is real but invisible under
some encodings. It is a methodological risk within Type A, not a genuine H¹ → H⁰ transition.

---

## Part E: Provenance and Attribution as Separate Branches

### Type C — Pre-Cohomological

Type C (Provenance) asks: before we apply any cohomology, do we know what presheaf to use?

The presheaf P encodes the independence structure of the records: which detector records are
independent witnesses (each contributes a separate D1 dimension) vs. which are downstream
copies (only count once).

When provenance is underdetermined (T67: identical passive statistics for dependent-copy vs.
independent-readout archives), we do not have a single presheaf to apply cohomology to. We
have a family of candidate presheaves with different section spaces.

**This is not an H⁰ failure:** The relevant records ARE accessible (Type B does not apply).
**This is not an H¹ failure:** The question is not whether a global section exists for a
fixed presheaf — it is which presheaf is correct.

**Formal slot:** Type C lives before the presheaf is defined. It is a meta-question about the
assignment of presheaf structure to physical data.

**Repair:** T68 showed that provenance can be recovered when records carry intervention-
sensitive metadata (origin tags, perturbation response, signed ancestry). This moves Type C
from "underdetermined" to "conditionally determined" — but only with access to causal
metadata, not from passive correlation.

---

### Type D — Post-Cohomological

Type D (Attribution) asks: given that H¹ ≠ 0 (a Type A failure is present), which step in
the projection sequence caused the obstruction?

This is a question about the HISTORY of the reconstruction, not about whether the current
obstruction exists. The current obstruction is present regardless of which step caused it.

**T37 (Typed Transport Network):** Same source/target; two paths; different PO1 verdicts
because AC5 accumulates differently. The H¹-type obstruction (gluing failure) is present on
both paths, but the cause differs. Without AC5 labeling, we cannot attribute the obstruction
to a specific forgetting step.

**Formal slot:** Type D is meta-level analysis on top of an existing H¹ obstruction. It is
not itself a cohomological computation — it is a reconstruction problem about the causal
history of the obstruction.

**Repair (P5 principle):** Always name the forgotten structure (AC5) when claiming a PO1
obstruction. This converts undetermined attribution to a named forgetting step, transforming
Type D from "cause unknown" to "cause is AC5 forgetting at this step."

---

### Diagram: Reconstruction Failure Branches

```
Physical data available
        |
        v
   Type C? (Do we know which presheaf to use?)
   |                    |
  YES: presheaf fixed    NO: provenance underdetermined (Type C)
        |                   → requires intervention / signed metadata to resolve
        v
  Is there a global section?
  |                          |
 YES: global section exists   NO: local sections exist but won't patch (Type A / H¹)
        |                            |
   Type B? (Can observer access it?) Attribution determined? (Type D question)
   |              |                  |               |
  YES: fine     NO: accessibility   YES: source     NO: attribution
                    failure             of H¹ named     underdetermined
                    (Type B / H⁰)      (Type A       (Type D — needs
                    → requires         resolved)      AC5 labeling)
                    colimit
                    or future
                    access
```

---

## Part F: Candidate Classification Theorem

### Finite Reconstruction Failure Classification

**Setup:** Let X be a finite observer space with cover U = {U_i}. Let A be an ambient
presheaf (globally consistent, full record structure). Let F be an observed presheaf (locally
computed). Let G = A - F be the gap presheaf.

**Theorem F1 (H⁰ condition):** If N(U) is acyclic, all failures are H⁰-type (Type B):
H⁰(G) captures all phantom incomparability witnesses; H^n(F) = 0 for n ≥ 1.

*TaF witness:* T19 (nested cover), T56 (sparse overlaps), T51-T54 (observer colimits).
*Status:* Supported by all tested examples; T19 and T56 proved as the canonical cases.

**Theorem F2 (H¹ condition):** If N(U) contains a 1-cycle with Z/2Z coefficients and
transition functions have non-trivial holonomy, then H¹(F, Z/2Z) ≠ 0. No globally consistent
section exists.

*TaF witness:* T63 (4-cycle, holonomy computed), T65 (quantum sections, holonomy = -1).
*Status:* Proved for the CHSH 4-cycle case.

**Theorem F3 (H⁰ of gap presheaf):** For F a subpresheaf of A (F(U) ⊆ A(U) for all U),
H⁰(G) is exactly the set of phantom incomparability witnesses (pairs ordered in A but not F).

*TaF witness:* T58-gap, verified exhaustively on T51/T52 witnesses.
*Status:* Proved for the T51/T52 finite witness class; not yet promoted to general theorem.

**Theorem F4 (Projection preserves failure type for topology-preserving π):** If π is a
presheaf morphism that does not change the cover topology, the failure type (H⁰ or H¹)
is determined by the cover, not the morphism.

*TaF witness:* T37 (AC5 forgetting — failure type is H¹ before and after; only attribution
changes). T59/T58 (coefficient encoding change — failure type is A* risk, not H⁰ → H¹).
*Status:* Supported; not yet proved as a general theorem.

**Theorem F5 (Type C and D are separate):** Type C (provenance) failures are pre-
cohomological (determine the presheaf before cohomology); Type D (attribution) failures are
post-cohomological (explain an existing H¹ obstruction). Neither reduces to H⁰ or H¹.

*TaF witness:* T67 (passive correlation fails to distinguish presheaves; pre-cohomological);
T37 (attribution of AC5 forgetting; post-cohomological).
*Status:* Supported; no reduction found between any of the four types.

---

## Part G: Open Questions

**Q1: Dense cover H¹ for T56**
T56 Q3: does the dense cover {U_P, U_full} produce non-trivial H¹ when pairwise overlaps
include multiple events? The nerve of {U_P, U_full} is still two-element (acyclic). But a
triple cover {U_P, U_A, U_B, U_full} might have non-trivial 1-cycles. Open.

**Q2: Can loss morphisms change failure type?**
The TF1/LossKernel spine (open-problems/loss-kernel-formalization.md) formalizes typed
forgetting as morphisms in a category of record structures. The critical question: are all
loss morphisms topology-preserving? If a loss morphism can identify patches in the cover
(merge two observation contexts into one), it could in principle move H⁰ → H¹. This would
require a morphism that contracts parts of the cover nerve in a way that creates cycles.
Whether any TaF operation does this is an open target for TF1.

**Q3: T65 converse direction**
T65 has the one-direction implication: LC ⟹ holonomy = +1. The converse fails (128 ≠ 16).
The candidate general principle was: H¹ ≠ 0 iff globally consistent assignment requires
evidence inaccessible from any bounded causal region.
This is not the same as LC ⟺ holonomy = +1 (too strong, disproved).
The correct formulation: H¹ ≠ 0 (non-trivial holonomy) iff no locally causal completion
exists. This is exactly: holonomy = -1 ⟹ NOT LC (proved as contrapositive). The converse
of THIS direction (NOT LC ⟹ holonomy = -1) is disproved: non-LC sections can have
holonomy = +1 (when they have 2 or 4 negative transitions, not 1 or 3). The general causal
principle needs a more careful formulation. Open.

**Q4: Higher-degree obstructions**
H² and higher are possible on more complex covers. The T16 spacetime aggregation test targets
a gluing obstruction for finality sections. If the spacetime cover has a non-trivial H² class,
this would be the first TaF example of a degree-2 failure. Currently classified as H¹-type
by analogy; needs direct computation to verify degree.

**Q5: Type C from causal graph**
T67 showed passive correlation cannot recover provenance class. T68 showed intervention-
sensitive metadata can. The open question: can causal GRAPH TOPOLOGY alone (edge direction,
fork-vs-chain structure) determine the independence partition without active intervention?
If so, provenance is recoverable from causal structure and Type C is not truly pre-
cohomological — it reduces to a graph reconstruction problem (itself H⁰ or H¹ depending
on the accessibility of graph structure).

---

## Summary Table

| Condition | Failure type | TaF witnesses | Status |
|-----------|-------------|---------------|--------|
| Acyclic nerve | H⁰ only (Type B) | T19, T51-T54, T56/T58-gap | Proved |
| Nested 2-element cover | H⁰ only (Type B) | T19 | Proved |
| Sparse pairwise overlaps | H⁰ only (vacuous H¹) | T56 | Proved |
| 4-cycle nerve + Z/2Z | H¹ possible (Type A) | T63, T65 | Proved |
| 4-cycle + non-trivial holonomy | H¹ active (Type A) | T63, T65 | Proved |
| Distributed contextuality | H¹ at inter-observer overlaps | T58-Bell | Proved |
| Projection (topology-preserving) | Type preserved | T37, T59/T58 | Supported |
| Provenance underdetermination | Pre-cohomological (Type C) | T67 | Supported |
| Attribution underdetermination | Post-cohomological (Type D) | T37, T39 | Supported |
| Dense cover / higher degree | Open | T56-Q3, T16 | Open |
| Loss morphisms / type change | Open | TF1/LossKernel | Open |

---

## Implications for Active Branches

**H¹ branch (T63/T65):** The relevant formal target is F3 (the general principle: H¹ ≠ 0
iff locally causal assignment cannot exist) — but its formulation must be revised after the
T65 biconditional failure. The weaker statement (LC ⟹ holonomy = +1; holonomy = -1 ⟹ NOT LC)
is proved. The stronger converse is open.

**Gap-presheaf branch (T56/T58-gap):** Theorem F3 gives a finite witness proof. Promotion
to a general theorem requires proving that F(U) ⊆ A(U) holds universally (F is a subpresheaf
of A) — this is T56 open question Q1 stated more precisely.

**Detector branch (T64/T66/T67/T68):** T68 conditionally resolves Type C by requiring
intervention-sensitive metadata. Q5 (whether causal graph structure alone suffices) is the
next open question for this branch.

**TF1/LossKernel spine:** The most important implication is Q2: the full typed forgetting
formalism should track whether its morphisms are topology-preserving. If any loss morphism
changes cover topology, it becomes a mechanism for moving reconstruction failures across the
H⁰/H¹ boundary — the first such mechanism in the TaF program.
