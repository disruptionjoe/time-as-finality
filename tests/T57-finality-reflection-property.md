# T57: Finality Reflection Property

## Target Claims

- [C1: Experienced Time As Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1-Field: Multiscale Observer Finality](../claims/D1-field-multiscale-observer-finality.md)
- [T56: Sheaf Cohomology of Apparent Finality](T56-sheaf-cohomology-apparent-finality.md)

## Central Question

Does the T56 gap assignment

```text
G(U) = A(U) - F(U)
```

actually restrict like a presheaf, or did T56 assume a complement property that
does not hold in general?

Phase 21 identified this as the first concrete mathematical obligation before
using the gap-presheaf language downstream.

## Theorem Target

For nested observer patches `V < U` in record-access order:

```text
F(V) subset rho_{U->V}(F(U))
```

Equivalently:

```text
(a,b) not in F(U) implies (a,b) not in F(V)
```

for every `V`-accessible event pair `(a,b)`.

This is the **Finality Reflection Property**.

## Why It Should Hold in TaF

In T56,

```text
F(U) = transitive closure of record-dependency edges over U-accessible events.
```

If `V < U`, every event accessible to `V` is also accessible to `U`. Any
witnessing chain used by `F(V)` is therefore also available to `F(U)`. The
larger patch may see additional intermediaries, but it cannot lose a smaller
patch's apparent-order witness.

## Required Witnesses

T57 must provide:

1. A hidden-intermediary record lattice extending the T56 witness.
2. A branching-dependency record lattice so the result is not only a chain case.
3. A check that FRP holds over all nested patch pairs in each lattice.
4. A check that `G(U)` restricts into `G(V)`.
5. A non-lifting example: smaller-patch gaps need not lift to larger patches.
6. A generic complement counterexample showing that FRP is not automatic.

## Success Criteria

T57 succeeds if:

- no FRP violations are found in the TaF witnesses;
- no gap-restriction violations are found in the TaF witnesses;
- at least one smaller-patch gap fails to lift to a larger patch, preserving the
  closure-versus-surjectivity boundary;
- the generic complement counterexample fails FRP and fails complement closure;
- the result explicitly leaves the arrow-direction circularity question open.

## Failure Criteria

T57 fails if:

- any TaF nested patch pair has `F(V)` not included in `rho(F(U))`;
- any larger-patch gap restricts outside the smaller-patch gap;
- no generic complement counterexample is found;
- the result claims to derive finality-arrow direction rather than only proving
  a conditional monotonicity lemma.

## Run Command

```bash
python -m pytest tests/test_finality_reflection_property.py -v
python -m models.run_t57
```

## Artifacts

- Model: `models/finality_reflection_property.py`
- Tests: `tests/test_finality_reflection_property.py`
- Results: `results/finality-reflection-property-v0.1.json`
- Results summary: `results/finality-reflection-property-v0.1-results.md`
- Technical report: `TECHNICAL-REPORT-finality-reflection-property-v0.1.md`

## Boundary

T57 does not solve the T56 Q4 circular-risk problem. It assumes the T56
source/target event structure and proves that, once that structure is admitted,
the gap-presheaf restriction step is mathematically licensed for the tested
finite model.
