# T73: LossKernel Composition

**Status:** implemented — composition law verified; path-dependence biconditional established
**Depends on:** T34, T37, T69, TF1/LossKernel
**Strategic role:** completes the LossKernel program — turns it from a naming layer
into an algebraic object that governs path-dependent PO1 admissibility

---

## Question

Is T37's path-dependent PO1 admissibility exactly captured by unequal composed
LossKernels? And does loss compose functorially, lax-functorially, or only partially?

---

## Formal Setup

**LossKernel of a morphism f:**
```
LossKernel(f) = frozenset(f.forgotten_structure)
```
The set of structure names forgotten (projected away) by morphism f.

**Composition law candidate:**
```
LossKernel(g ∘ f) = LossKernel(f) ∪ LossKernel(g)
```
Union of individual loss kernels. This is the lax-functorial (monotone) law.

**AC5 condition restatement:**
AC5 (structure_forgotten) passes iff `LossKernel(path) ≠ ∅`.

**Main claim:**
For fixed source and target with the same endpoint AC conditions (AC1-AC4, AC6-AC7,
which T37 showed are path-invariant):
```
PO1(Path₁) ≠ PO1(Path₂)  ⟺  LossKernel(Path₁) ≠ LossKernel(Path₂)
                                  in the empty/non-empty sense
```

---

## Hypotheses

- **H1 (Composition law):** LossKernel(path) = union of per-step forgotten_structure.
  Verified on T34 spectre, stepwise, absorbed chains and T37 diamond paths.

- **H2 (Lax-functorial):** The union composition is monotone: LossKernel(g ∘ f) ⊇
  LossKernel(f). Loss can accumulate but never decrease. Identity: LossKernel(id) = ∅.

- **H3 (Path-dependence biconditional):** For fixed (source, target) with equal
  endpoint conditions: PO1 path-dependence is exactly the non-empty/empty difference
  in composed LossKernels. T37's diamond witnesses this with Path A = {type_guarantee}
  and Path B = {}.

- **H4 (T34 chain shapes as LossKernel patterns):**
  - Emergent: LossKernel(partial paths) non-empty, but targets not obstructed at
    partial paths. AC6 fails early; H1 passes everywhere. Endpoint: AC6 passes,
    LossKernel non-empty → PO1 admissible.
  - Stepwise: LossKernel non-empty at each step where target is obstructed → each
    qualifying pair is PO1 admissible.
  - Absorbed: LossKernel non-empty at mid-chain (SRC→MID), but endpoint target is
    unobstructed → AC6 fails at endpoint → endpoint verdict = not PO1.
    The non-empty LossKernel at endpoint is insufficient because AC6 is not satisfied.

---

## Pass / Fail Criteria

**H1 passes** if: for all T34 chains and T37 paths, computed composed LossKernel equals
the union of per-step forgotten_structure.

**H2 passes** if: monotonicity holds on all T34/T37 examples, and LossKernel(identity) = ∅.

**H3 passes** if: for T37's diamond, the empty/non-empty difference in composed LossKernels
exactly predicts which path is PO1-admissible and which is not.

**H4 passes** if: emergent = non-empty LossKernel but AC6 fails at partial paths;
absorbed = non-empty LossKernel at mid-chain but AC6 fails at endpoint.

---

## LossKernel Q2 Answer

The composition is **lax-functorial**: LossKernel(g ∘ f) = LossKernel(f) ∪ LossKernel(g).
It is NOT strictly functorial (structure forgotten in g does not depend on what was
forgotten in f — they are accumulated independently). It is NOT partial (the law is
total: it applies to all T34/T37 morphisms). The union law satisfies associativity and
has identity element ∅.

## LossKernel Q3 Answer

T34/T37 path dependence IS exactly unequal composed LossKernels for fixed endpoints,
when AC1-AC4, AC6-AC7 are equal (endpoint-determined). The path-dependence in T37 is
not an AC5 accident — it is the signature of different LossKernels accumulating different
forgotten structure.

---

## Artifacts

- Model: `models/losskernel_composition.py`
- Test: `tests/test_losskernel_composition.py`
- Results: `results/losskernel-composition-v0.1.json`
- Result note: `results/losskernel-composition-v0.1-results.md`
