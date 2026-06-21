# T69 Results: LossKernel Failure Type — v0.1

**Date:** 2026-06-19
**Model:** `models/losskernel_failure_type.py`
**Tests:** 7/7 pass

---

## Main Fixture Result: ESTABLISHED

**In the implemented finite witness family, loss morphisms are failure-type
monotone.**

For TaF loss morphisms (topology-preserving and sub-cover restriction):
```
failure_type(target) <= failure_type(source)
in the ordering H1 > H0 > none
```

H0 → H1 is impossible. H1 → H0 is possible (via cycle destruction). H0 → H0 is
the generic topology-preserving case.

---

## Diligence Caveat

Do not cite this as a general Cech/sheaf-cohomology theorem. The broad claim
that acyclic cover topology alone forces H1 to vanish for every presheaf is not
valid without additional hypotheses. This result is limited to the coefficient
systems, support semantics, cover shapes, and loss-morphism classes implemented
in `models/losskernel_failure_type.py`.

Before promotion, the next version must explicitly separate:

- nerve topology of the cover,
- the coefficient system or support presheaf,
- global-section obstruction,
- the paper's custom H0/H1 failure labels,
- and the allowed class of loss morphisms.

If those assumptions cannot be stated cleanly, T69 should remain a toy-model
diagnostic rather than theorem-level support for TF1.

---

## Witness Results

**W1 — H0 preserved under topology-preserving loss:** SUPPORTED
- Source: nested cover {U₀ ⊂ U₁}, H0 gap at U₀ (v₀=1 inaccessible), H1 = 0
- Loss: project away v₁ (keep only v₀ at all patches)
- Target: same nesting topology, H0 gap preserved at U₀, H1 = 0
- H1 created by loss: False

**W2 — H1 destroyed by sub-cover restriction:** SUPPORTED
- Source: CHSH 4-cycle cover, H1 ≠ 0 (non-trivial Z/2Z class), quantum holonomy = −1
- Loss: restrict to Alice's 2-context sub-cover {A0B0, A0B1}
- Target: 2-element cover (acyclic), H1 = 0, 8 global sections exist
- H1 destroyed: True
- Confirms T131 distributed contextuality as a loss morphism in canonical form

**W3 — H0 → H1 impossible (exhaustive + algebraic):** SUPPORTED
- 0 counterexamples found in 4 acyclic covers × all sub-cover restrictions
- Algebraic argument: acyclic nerve + topology-preserving loss = same acyclic nerve;
  sub-cover of acyclic cover = sub-acyclic (forest of tree is forest). Both force H1 = 0.
- Patch identification excluded: this creates cycles but is NOT a TaF loss operation
  (it's context reidentification, not forgetting)

**W4 — Cyclic cover projection (bonus):** SUPPORTED
- Projecting Alice's outcome from 4-cycle cover collapses nerve to two disjoint edges (acyclic)
- Section-space projection can itself change cover topology when the projected variable was
  the sole shared variable between certain patches
- Global (Bob-only) sections survive: 4 sections

---

## Key Findings

**1. Cover topology is an invariant barrier in the implemented family.**
The tested nerve topology determines whether H1 is possible under the chosen
coefficient/support semantics. This should not be generalized to every
presheaf. Loss morphisms that preserve the tested nerve preserve the fixture's
failure type. Loss morphisms that destroy cycles (sub-cover restriction) can
only decrease the fixture failure type.

**2. H1 destruction is the canonical loss-morphism effect on cyclic covers.**
T58's distributed contextuality theorem is now interpretable as a loss morphism:
restricting from the 4-context CHSH cover to a 2-context Alice (or Bob) sub-cover
is a cover-collapsing loss that destroys the H1 obstruction. The LossKernel of this
morphism contains the cycle-destroying structure.

**3. Patch identification is not a TaF loss operation.**
The only mechanism that could create H1 from an acyclic cover (via merging non-adjacent
patches to form cycles) is explicitly excluded from TaF's loss vocabulary. TaF loss
morphisms reduce information within contexts; they do not reidentify distinct contexts.

**4. Section-space projection can change cover topology as a side effect.**
W4 shows: projecting Alice's outcome away from each context makes formerly-distinct contexts
share no overlap variables, disconnecting the nerve. This is topology-change via section-space
loss (not sub-cover restriction). Result: H1 destroyed (4-cycle → two disjoint edges → acyclic).
This is a second mechanism for H1 destruction, distinct from patch-dropping.

---

## LossKernel Implications

For TF1/LossKernel typed loss accounting:

| Loss morphism type | Failure type change | LossKernel flag |
|---|---|---|
| Topology-preserving (section-space) | H0 → H0, H1 → H1 or smaller | `topology_preserved = True` |
| Sub-cover restriction (drop patches, break cycle) | H1 → H0 possible | `cycle_destroying = True` |
| Section-space projection (disconnects nerve) | H1 → H0 possible | `cycle_destroying = True` |
| Patch identification (excluded) | H0 → H1 possible | NOT a TaF loss operation |

**Candidate law for TF1:** `LossKernel(f).cycle_destroying` is True iff f can reduce failure
type from H1 to H0. When `cycle_destroying = False`, failure type is monotone-preserved.

This remains audit-blocked as a general theorem. The minimum resolution is an
explicit theorem statement naming the coefficient system, support presheaf,
cover hypotheses, and allowed loss morphisms, plus counterexample checks against
same-cover support shrinkage.

---

## Falsification Condition

T69 would fail if:
- A topology-preserving loss morphism is found that converts an acyclic cover to a cyclic
  one without adding new patches (would require topological magic — impossible by definition)
- A sub-cover restriction of an acyclic cover produces a cyclic sub-cover (impossible:
  subgraph of a forest is a forest)
- A loss morphism is defined that merges non-adjacent patches in an acyclic cover and
  this is accepted as a valid TaF loss operation (would require expanding the definition
  of TaF loss to include context reidentification)
