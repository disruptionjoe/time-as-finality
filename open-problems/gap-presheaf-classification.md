# Gap Presheaf Classification

## Problem

Can the gap assignment

```text
G(U) = A(U) - F(U)
```

be promoted from a useful diagnostic to a classification theorem for phantom
incomparability?

## Working Claim

T56 found that apparent/event-finality mismatch lives at H0 level rather than
as a sparse-cover H1 obstruction. T57 proved the Finality Reflection Property
needed for `G` to restrict correctly in the tested finite model. T58 then
checked the first gap/phantom equivalence family.

T113 determined that raw global sections of `G` are too broad, but a typed
subobject of them exactly matches the phantom incomparability witnesses in the
tested finite family.

## Why It Matters

This is the strongest immediate way to make the GU integration roadmap
mathematically honest. If the classification holds, "finality torsion" can be
used as disciplined analogy for a TaF-native defect object:

```text
locally apparent order differs from ambient restricted event order.
```

T113 therefore permits only disciplined "typed torsion-like gap" language. Raw
`H0(G)` and physical torsion language remain blocked.

## How It Could Mislead

- `G` being restriction-closed does not automatically mean it classifies all
  phantom witnesses.
- Complements of subpresheaves are not generally presheaves; FRP is
  load-bearing.
- A T53-style underdetermined colimit is not the same thing as a phantom repair.
- A malformed local reversal can create fake gaps if `F(U) subset A(U)` is not
  enforced.

## Formal Entry Point

Run [T113: Gap Presheaf Classification](../tests/T113-gap-presheaf-classification.md).

T113's output is:

```text
A typed subobject of H0(G) classifies phantom incomparability in the tested
finite family.
Raw H0(G) is refuted as too broad.
```

## Connection to Existing Claims and Tests

- [T51: Multi-Observer Apparent Finality Colimit](../tests/T51-multi-observer-apparent-finality-colimit.md)
- [T52: Symmetric Colimit Theorem](../tests/T52-symmetric-colimit-theorem.md)
- [T53: Observer-Colimit Descent Boundary](../tests/T53-observer-colimit-descent-boundary.md)
- [T56: Sheaf Cohomology of Apparent Finality](../tests/T56-sheaf-cohomology-apparent-finality.md)
- [T57: Finality Reflection Property](../tests/T57-finality-reflection-property.md)
- [T58: Gap-Phantom Equivalence](../tests/T58-gap-phantom-equivalence.md)
- [Geometric Unity Integration Roadmap](../TECHNICAL-REPORT-geometric-unity-integration-roadmap-v0.1.md)

## Contribution Needed

Give the typed subobject an abstract definition that is not merely a checklist
over the current finite witnesses, and compare it against the T19
accessible-witness gap to test whether both are instances of one typed gap
category.

## Status Addendum (2026-07-07): typed-gap bridge

T492 answers the contribution-needed item conservatively:
`results/T492-typed-gap-category-bridge-v0.1-results.md`; spec
`tests/T492-typed-gap-category-bridge.md`; model
`models/typed_gap_category_bridge.py`.

Verdict:
`COMMON_TYPED_GAP_SCHEMA_SUPPORTED_OBJECT_IDENTITY_BLOCKED`. T113 order-pair
phantom gaps and T92 unary proposition gaps share a finite typed-gap schema:
patches, ambient object `A`, local/auditable subobject `F`, gap object `G`, a
typed admissibility predicate `tau`, and restriction closure. They are not the
same section object, classifier, or theorem target. Raw `H0(G)` remains blocked
by T113, while T92 continues to block identity with T58 order-pair gaps.

This sharpens the abstract definition into a schema, not a category theorem.
Future stronger work would need explicit morphisms between typed gap systems and
a naturality/equivalence theorem across at least one additional carrier kind.
No claim-ledger, roadmap, public-posture, physical-torsion, cohomology, GU,
consciousness, complexity-class, or cross-repo truth movement is earned.
