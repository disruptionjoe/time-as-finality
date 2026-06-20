# T69: LossKernel Failure Type

**Status:** implemented on finite witnesses; general theorem audit-blocked
**Depends on:** T19, T37, T39, T56, T58 (gap + Bell), T63, T65
**Strategic role:** connects the typed-forgetting spine (TF1/LossKernel) to the
reconstruction-failure hierarchy (H⁰/H¹ cover structure investigation)

---

## Diligence Note

This test must not be read as a general Cech/sheaf-cohomology theorem. External
skeptical diligence flags the broad claim "acyclic cover implies H1 vanishes
for every presheaf" as false without stronger hypotheses. The T69 result is
therefore restricted to the finite coefficient systems, support choices, and
loss-morphism classes implemented here.

Before public or canon promotion, the report must state the exact coefficient
system, cover hypotheses, and support-presheaf assumptions under which the H0/H1
failure-type ordering is valid. If those assumptions cannot be made explicit,
T69 should remain a useful toy-model diagnostic rather than a theorem.

---

## Question

Can a typed forgetting (loss) morphism change reconstruction failure type across
the H⁰/H¹ boundary?

Specifically:
- Can a loss morphism convert an H⁰ accessibility failure (global section exists,
  observer cannot reach it) into an H¹ existence obstruction (no global section)?
- Or does loss only destroy H¹ (by collapsing cyclic covers) while preserving H⁰?

---

## Why This Matters

The H⁰/H¹ cover-structure investigation suggested, within the implemented
fixture family, that cover topology constrains failure type once the coefficient
system, support semantics, and allowed loss morphisms are fixed. Loss morphisms
are the algebraic objects that transform one restriction system into another.
Whether they can change failure type determines:

1. Whether H⁰ and H¹ failures are stable under the typed-forgetting operations
   in the repo (PO1 projection, access restriction, record filtering).
2. Whether TF1/LossKernel must track failure-type change as part of its typed
   loss accounting.
3. Whether there is a conservation law: "loss morphisms are failure-type monotone"
   (H⁰ stays H⁰, H¹ may decrease to H⁰ but cannot increase from H⁰ to H¹).

---

## Two Classes of Loss Morphism

**Class 1 — Topology-preserving (section-space morphism):**
Same cover U, same patches, same overlap structure. The loss morphism reduces or
relabels the section space at each patch. Cover topology (nerve graph) is unchanged.

**Class 2 — Cover-collapsing (sub-cover restriction):**
The cover changes: some patches are dropped (sub-cover) or collapsed. The nerve graph
changes. Can remove cycles (cyclic → acyclic).

TaF loss operations primarily belong to Class 1 (forgetting record content, projecting
dimensions) or Class 2 variant where patches are dropped (restricting to a sub-cover,
as in T58 distributed contextuality: 4-cycle → Alice's 2-context sub-cover).

A third variant — **patch identification** (merging two non-adjacent patches, which
can CREATE cycles from acyclic covers) — is NOT a loss operation in the TaF sense:
it would mean declaring two distinct contexts to be the same, which is not forgetting
but reidentification. This class is explicitly excluded from the witnesses below.

---

## Hypotheses

- **H1**: Topology-preserving loss morphisms cannot change failure type. H⁰ stays H⁰;
  H¹ stays H¹ (or becomes smaller within the same type).

- **H2**: Sub-cover restriction loss morphisms CAN change H¹ to H⁰ (by dropping
  enough patches to remove the cycle from the nerve). H¹ destruction is possible.

- **H3**: No TaF loss morphism (topology-preserving or sub-cover restriction) can
  convert an H⁰ accessibility failure into an H¹ existence obstruction.
  **H⁰ → H¹ is impossible for these classes.**

- **H4**: On a cyclic cover, topology-preserving loss can INTRODUCE new non-trivial
  H¹ elements (previously hidden by over-constraint) while global sections from the
  source presheaf survive in the target.

---

## Three Witnesses

### Witness 1 — H⁰ Preserved (topology-preserving loss, nested cover)

**Cover:** U₀ = {v₀}, U₁ = {v₀, v₁} with U₀ ⊂ U₁ (nested, acyclic)

**Source presheaves:**
- A(U₀) = {(0,), (1,)} — ambient sees all values of v₀
- F(U₀) = {(0,)} — observer at U₀ only sees v₀ = 0 (blocked from v₀ = 1)
- A(U₁) = {(0,0), (0,1), (1,0), (1,1)} — full variable access
- F(U₁) = A(U₁) — observer at U₁ has full access

**Gap:** G(U₀) = A(U₀) − F(U₀) = {(1,)} ≠ ∅ → H⁰ failure at U₀
**H¹:** 0 (nested cover, Mayer-Vietoris)

**Loss morphism π (section-space, topology-preserving):**
"Forget v₁ — only track v₀ at both patches."
- π maps U₁ sections to single-variable v₀ projections
- Cover becomes {U₀ = {v₀}, U₁ = {v₀}} (both patches track only v₀)
- Same nesting topology (U₀ ⊂ U₁ in original; both now have same variable set)

**Target presheaves after π:**
- π(A)(U₀) = {(0,), (1,)}, π(F)(U₀) = {(0,)} — same as before at U₀
- π(A)(U₁) = {(0,), (1,)}, π(F)(U₁) = {(0,), (1,)} — projected
- Gap after π: π(G)(U₀) = {(1,)} ≠ ∅ → H⁰ failure preserved
- H¹ after π: 0 (cover still nested, even after v₁ is projected away)

**Expected result:** H⁰ failure preserved; H¹ remains 0.

---

### Witness 2 — H¹ Destroyed (sub-cover restriction, 4-cycle)

**Cover:** CHSH 4-cycle {A0B0, A0B1, A1B1, A1B0} with:
- A0B0 ∩ A0B1 = shared Alice A0 setting
- A0B1 ∩ A1B1 = shared Bob B1 setting
- A1B1 ∩ A1B0 = shared Alice A1 setting
- A1B0 ∩ A0B0 = shared Bob B0 setting

**Source:** Quantum majority-outcome sections. Holonomy = −1 for quantum section.
H¹ ≠ 0 (non-trivial class in Z/2Z cohomology). Established in T63/T65.

**Loss morphism π (sub-cover restriction):**
"Forget Bob's measurements — restrict to Alice-only sub-cover."
- Drop A0B1 and A1B1 (contexts where Bob's B1 setting appears as the transition)
- Retain A0B0 (Alice A0) and A1B0 (Alice A1)
- New cover: {A0B0, A1B0} — two-element, no shared variable between them
  (Alice's A0 setting is not the same as her A1 setting)

Actually, the sub-cover that T58 uses is Alice's sub-cover:
- A0-contexts: A0B0 and A0B1 (both have Alice's A0 setting as shared variable in one transition)
- A1-contexts: A1B0 and A1B1

T58 showed: Alice's 2-context sub-cover {A0B0, A0B1} has:
- Nerve = single edge (two patches, one shared variable: Alice A0)
- H¹ = 0 (two-element cover, acyclic)

**Target after restriction to {A0B0, A0B1}:**
- Cover is 2-element, acyclic
- H¹ = 0 (by Theorem B2)
- For any section assignment (a₀b₀, a₀b₁) where Alice's A0 outcome is the same in both
  contexts, there's a globally consistent section
- Global sections exist

**Expected result:** H¹ destroyed (non-trivial → 0); failure type changes from A to at
most B or no-failure.

---

### Witness 3 — H⁰ → H¹ Impossible (exhaustive search on small covers)

**Protocol:**
For all topology-preserving loss morphisms π applied to all acyclic covers with ≤ 3
patches and ≤ 4 binary variables, verify H¹(π(F)) = 0.

**Key argument (fixture-local, not general sheaf theory):**
If the source cover U is acyclic (contractible nerve), then:
1. Every topology-preserving loss morphism keeps the same cover U.
2. The nerve is unchanged: still acyclic.
3. In the implemented finite fixture family, H1 = 0 on the acyclic covers
   under the chosen coefficient/support semantics.
4. Therefore, H¹ cannot become non-zero through topology-preserving loss.

For sub-cover restriction:
1. Dropping patches from an acyclic cover gives a sub-acyclic cover.
2. Sub-acyclic covers are acyclic (a subgraph of a tree/forest is a forest).
3. H¹ = 0 for any sub-acyclic cover.
4. Therefore, sub-cover restriction also cannot create H¹ from H⁰.

**Exhaustive verification:** The enumeration over small covers confirms no counterexample
exists in the finite case, consistent with the algebraic argument.

---

## Pass / Fail Criteria

**H1 passes** if:
- W1 shows gap presheaf H⁰ preserved and H¹ = 0 preserved after π.
- W3 algebraic argument is valid.

**H2 passes** if:
- W2 shows H¹ = Z/2Z before π and H¹ = 0 after π (sub-cover restriction).

**H3 passes** if:
- W3 exhaustive search finds zero counterexamples.
- Algebraic argument (acyclic sub-cover stays acyclic) is confirmed.

**H4 passes** if:
- A cyclic-cover witness shows: source presheaf has only LC sections (H¹ = 0 for LC
  sub-presheaf), and after relaxing to all CHSH sections, H¹ ≠ 0 appears.
- Global section from LC sub-presheaf survives in the larger presheaf.

---

## Connection to TF1/LossKernel

**Implication for TF1 (Typed Forgetting Attribution):**
The candidate lemma says an obstruction is admissibly attributable to f only if
LossKernel(f) is non-empty and names the relevant forgotten structure.

T69 adds a structural constraint: admissible attribution also requires that the
FAILURE TYPE is consistent. Specifically:
- A loss morphism that destroys H¹ (W2 case) cannot carry an H¹ attribution
  unless the source had H¹ ≠ 0. The morphism REMOVES the obstruction, not creates it.
- A loss morphism from a source with H⁰ failure cannot produce H¹ in the target.
  If the target has H¹ ≠ 0, the source must have had H¹ ≠ 0 (and the morphism
  must be on a cyclic cover that preserved the cycle).

**LossKernel failure-type monotonicity (candidate law):**
For any TaF loss morphism f (topology-preserving or sub-cover restriction):
- failure_type(target) ≤ failure_type(source) in the ordering H¹ > H⁰ > none
- Loss morphisms can only DECREASE the failure type, not increase it
- This is a directional conservation law on reconstruction failure type

This is a candidate law for the implemented finite families, not a general
cohomology monotonicity theorem. External review blocks promotion until the
allowed morphism class and coefficient/support hypotheses are stated tightly
enough to exclude known same-cover support-presheaf counterexamples.

---

## Artifacts

- Model: `models/losskernel_failure_type.py`
- Test: `tests/test_losskernel_failure_type.py`
- Results: `results/losskernel-failure-type-v0.1.json`
- Result note: `results/losskernel-failure-type-v0.1-results.md`
