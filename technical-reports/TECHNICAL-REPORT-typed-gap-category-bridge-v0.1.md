# Technical Report: Typed Gap Category Bridge v0.1

## Claim Under Test

T113 and T92 both use a gap object `G(U)=A(U)-F(U)`, but they do not use the
same carrier:

- T113 uses nonreflexive ordered event-pair sections.
- T92 uses unary typed proposition sections.

The question is whether these are instances of one typed gap schema or only a
loose H0 analogy.

## Result

T492 supports the common schema but blocks object identity.

The shared finite schema is:

```text
finite patch family
ambient object A(U)
local or auditable subobject F(U)
gap object G(U)=A(U)-F(U)
typed admissibility predicate tau
restriction closure for typed gaps
domain-specific target interpretation
```

T113 and T92 both instantiate this schema. T113 classifies phantom
incomparability witnesses in the tested finite family after typed filtering.
T92 classifies accessible-witness unauditability gaps for typed proposition
systems under explicit closure hypotheses.

## What This Strengthens

The T19/T58 bridge can now be described as a typed-gap bridge rather than a
bare metaphor. The useful abstraction is the interface:

```text
(patches, A, F, G, tau, restriction)
```

not a claim that proposition gaps and order-pair gaps are the same object.

## What This Blocks

T492 blocks:

- raw `H0(G)` as the common classifier;
- identical section-object language;
- physical torsion or GU validation;
- general cohomology or sheafification claims;
- consciousness or complexity-class claims from T92;
- claim-ledger or public-posture movement.

## Current Strongest Claim

T92 and T113 instantiate a common finite typed-gap schema while preserving
distinct section objects, classifiers, and theorem targets.

## Open Blocker

This is not yet a category theorem. A future stronger result would need to
define actual morphisms between typed gap systems and prove a naturality,
equivalence, or transfer theorem across at least one additional carrier kind.

## Reproduction

```bash
python -m pytest tests/test_typed_gap_category_bridge.py -q
python -m models.typed_gap_category_bridge --write-results
```
