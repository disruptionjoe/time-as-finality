# T492: Typed Gap Category Bridge

## Target Claims

- [Gap Presheaf Classification](../open-problems/gap-presheaf-classification.md)
- [Accessible Witness Gap Restriction Theorem](../open-problems/accessible-witness-gap-restriction-theorem.md)
- T113 gap-presheaf classification
- T92 accessible-witness gap restriction

## Question

Do T113 order-pair phantom gaps and T92 unary proposition gaps share a common
typed gap category, or only the same H0 failure shape?

## Setup

T113 supports a typed subobject of `H0(G)` for order-pair phantom
incomparability. T92 supports restriction closure for T19-style unary
proposition gaps under ambient restriction, audit monotonicity, and stable
proposition typing.

T492 compares them through a minimal finite schema:

```text
patch family + restriction maps
A(U) ambient object
F(U) local/auditable subobject
G(U)=A(U)-F(U)
typed predicate tau selecting meaningful gap sections
rho(tau(G(U))) subset tau(G(V)) for V subset U
domain-specific target interpretation
```

## Success Criteria

- The common minimal typed-gap schema is admitted.
- Raw `H0(G)` identity is rejected because T113 refutes raw gap classification.
- Same-section-object identity is rejected because T113 uses order pairs and T92
  uses unary propositions.
- Cohomology, physical torsion, consciousness, and complexity-class promotion
  shortcuts are rejected.
- T92 semantic-relabeling controls and T113 local-reversal/malformed controls
  remain blockers.

## Failure Criteria

- The artifact treats T92 and T113 as the same section object.
- The artifact promotes raw `H0(G)` as the shared classifier.
- The artifact upgrades T92 to a consciousness or complexity-class claim.
- The artifact upgrades T113/T492 to physical torsion, GU validation, or a
  general cohomology theorem.

## Claim Impact

No claim promotion. If T492 passes, the safe update is only:

```text
T92 and T113 instantiate a common finite typed-gap schema, while preserving
distinct section objects, classifiers, and theorem targets.
```

## Reproduction

```bash
python -m pytest tests/test_typed_gap_category_bridge.py -q
python -m models.typed_gap_category_bridge --write-results
```
