# T73 Results: LossKernel Composition — v0.1

**Date:** 2026-06-20
**Model:** `models/losskernel_composition.py`
**Tests:** 17/17 pass

---

## Main Fixture Result: ESTABLISHED

**For the tested finite T34/T37 family, LossKernel composes by union, and
path-dependent PO1 admissibility is exactly the empty/non-empty difference in
composed LossKernels.**

```
LossKernel(g ∘ f) = LossKernel(f) ∪ LossKernel(g)
```

For fixed (source, target) with equal endpoint AC conditions (AC1-AC4, AC6-AC7):
```
PO1(P₁) ≠ PO1(P₂)  ⟺  LossKernel(P₁) ≠ LossKernel(P₂) in the empty/non-empty sense
```

---

## Diligence Caveat

This result is not yet a publication-grade theorem of typed forgetting. It
shows that the current finite fixtures can be summarized by a powerset-union
annotation. That is mathematically legitimate, but it is close to standard
provenance/effect/writer-style bookkeeping. Promotion requires a semantic
witness obligation, a quotient/separation result, or another non-tautological
reason that LossKernel cannot be replaced by ordinary provenance or effect
annotations.

---

## Hypothesis Results

**H1 — Composition law (union):** PASS
- Verified on all T34/T37 paths: compose_loss(path) = union of per-step forgotten_structure
- 5 chains verified: T37 spectre, T37 diamond Path A, T37 diamond Path B, T34 spectre, T34 stepwise, T34 absorbed

**H2 — Lax-functorial (monotone):** PASS
- All prefix LossKernels are subsets of the full composed LossKernel
- Identity morphism (empty path) has LossKernel = ∅
- Union law is associative; identity element ∅ is confirmed

**H3 — Path-dependence biconditional:** PASS
- T37 diamond: Path A LossKernel = {type_guarantee} → AC5=True → PO1=True
- T37 diamond: Path B LossKernel = {} → AC5=False → PO1=False
- AC5 exactly tracks LossKernel non-emptiness (test: AC5 == (LossKernel ≠ ∅) for all paths)
- AC1-AC4, AC6-AC7 are endpoint-determined and path-invariant
- Therefore: PO1 path-dependence = exactly empty/non-empty LossKernel difference

**H4 — T34 chain shapes as LossKernel patterns:** PASS
- Emergent (Spectre): LossKernel = {type_safety_guarantee, control_flow_isolation,
  memory_access_abstraction, execution_order_guarantee}; AC5=True, AC6=True; endpoint=PO1
- Stepwise: LossKernel = {abstract_control_flow, register_allocation_freedom,
  instruction_encoding_freedom}; AC5=True, AC6=True at each obstructed step; endpoint=PO1
- Absorbed: LossKernel = {dead_branch_elimination, optimization_annotations};
  LossKernel non-empty but AC6=False at endpoint (target unobstructed); endpoint=NOT PO1
  Confirms: non-empty LossKernel is NECESSARY but not SUFFICIENT for PO1

---

## Key Findings

**1. LossKernel is the organizing object for path-dependent PO1 admissibility.**
The biconditional holds exactly because AC5 is the only path-varying AC condition when
(source, target) are fixed. All other conditions (AC1-AC4, AC6-AC7) are endpoint-determined.
So path-dependent PO1 = exactly empty/non-empty difference in composed LossKernels.

**2. The composition law is union-valued on the tested family.**
Strictly functorial would require LossKernel(g ∘ f) = some function of LossKernel(g)
applied to LossKernel(f). Instead, loss accumulates independently: g's forgotten structure
does not depend on what f forgot. Union law is total (no partial domain).

**3. LossKernel is not sufficient for PO1 — AC6 is co-required.**
The absorbed case shows: non-empty LossKernel + AC6 fails = NOT PO1. The full admissibility
check (AC1-AC7) governs; LossKernel governs only the AC5 dimension. For fixed endpoints
where AC6-AC7 are equal, LossKernel becomes the sole discriminating object.

**4. LossKernel now governs two levels of the hierarchy.**
- At the **path level**: LossKernel composition law determines which paths produce AC5=True.
- At the **failure-type level** (T69): LossKernel.cycle_destroying determines whether
  loss morphisms can reduce H¹ to H⁰.
Together, T69 + T73 give finite fixture evidence for the LossKernel program.
They do not complete the program until the prior-art and quotient tests pass.

---

## Falsification Condition

T73 would fail if:
- A T34/T37 path were found where compose_loss ≠ union of per-step forgotten_structure
  (would require a step to forget structure that doesn't appear in the composed kernel)
- A T37 diamond path were found where PO1 status and LossKernel emptiness disagree
  (would require AC5 to differ from the LossKernel non-empty signal)
- A T34 absorbed chain where AC6=True at endpoint despite the "absorbed" classification
  (would require the model to misclassify absorbed vs. stepwise)
