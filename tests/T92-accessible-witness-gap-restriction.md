# T92: Accessible-Witness Gap Restriction

## Route

Spacetime / observer reconstruction, with C1 phenomenal-bridge discipline.

## Question

Does the T19 proposition-domain gap object

```text
G(U) = A(U) - F(U)
```

restrict like the T57 gap object, or is T19 only an isolated finite accessible
witness lemma?

## Motivation

T89 showed that T19 and T58 share the same H0 failure shape, but not the same
section object. T19 uses unary truth-valued propositions about an observer.
T58 uses non-reflexive order pairs. The missing theorem target is whether the
T19 proposition-domain gap has restriction closure under nested observer
patches.

## Setup

For each finite typed proposition-domain witness:

- `A(U)` is the ambient/third-person proposition object;
- `F(U)` is the locally auditable proposition object;
- `G(U)=A(U)-F(U)` is the accessible-witness gap.

T92 checks:

```text
rho_{U->V}(G(U)) subset G(V)
```

for nested patches `V subset U`.

## Success Criteria

- The T19 unary witness satisfies ambient restriction, audit monotonicity,
  stable proposition typing, and gap restriction closure.
- A non-chain joint-witness system satisfies the same checks.
- Semantic relabeling breaks closure.
- Audit-monotonicity violation breaks closure.
- The result is stated as a conditional finite theorem audit, not a
  consciousness claim or a general cohomology theorem.

## Failure Criteria

- A well-typed, audit-monotone nested witness has a larger-patch gap whose
  restriction is not a smaller-patch gap.
- T92 proves closure only by circularly defining `F` or `G`.
- T92 identifies T19 proposition gaps with T58 order-pair gaps rather than
  saying they share H0 failure shape under different section objects.

## Claim Impact

If T92 passes, C1 may be sharpened but not upgraded:

```text
The first-person/third-person finality gap has a finite degree-0
accessible-witness form with restriction closure for typed proposition-domain
witness systems.
```

If T92 fails, T19 remains a finite Accessible Witness Gap Lemma without a
gap-presheaf theorem.

## Reproduction

```bash
python -m unittest tests.test_accessible_witness_gap_restriction -v
python -m models.run_t92
```
