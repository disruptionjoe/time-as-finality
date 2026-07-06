# Observer-Shadow Category

## Status

Open formalization target. This file is a research target extracted from the
North Star v0.8 62-persona steelman and Hegelian pass.

The goal is to test whether observer shadows and capability objects need
categorical structure, or whether set-level projection-sufficiency bookkeeping
is enough.

## Problem

Can the North Star data shape be organized compositionally?

Minimal data:

```text
source systems Y
observer/access profiles O
shadow projections pi_O : Y -> X_O
capability objects Cap_{O,T,h,B} : Y -> K
native comparisons R_K
observer changes O -> O'
source morphisms Y -> Y'
shadow-protection verdicts
```

The question is whether these form a category, indexed category, fibration,
double category, or only a family of set-level audits.

## Candidate Objects

Start with conservative objects:

```text
(Y, O, pi_O, Cap, R_K)
```

where:

- `Y` is a typed source system;
- `O` is an observer/access profile;
- `pi_O` is a declared projection;
- `Cap` is a domain-native capability object;
- `R_K` is the declared native comparison.

## Candidate Morphisms

A morphism should preserve enough structure to make comparison meaningful.
Candidate components:

```text
source map          f : Y -> Y'
shadow map          x : X_O -> X'_{O'}
capability map      k : K -> K'
observer map        o : O -> O'
compatibility       x(pi_O(y)) = pi'_{O'}(f(y)) where defined
comparison respect  Cap(y) R_K Cap(z) => k(Cap(y)) R_K' k(Cap(z))
```

## The First Gate

Do not seek elegance first. The first gate is:

```text
Does composition preserve shadow-protection verdicts under explicit
hypotheses?
```

If yes, identify the hypotheses.

If no, classify the obstruction:

- capability object changes;
- observer access changes;
- native comparison changes;
- visible equivalence changes;
- absorber state completion changes;
- path-dependent loss changes;
- gauge or representation quotient changes.

## Success Criteria

This target is useful if it yields at least one of:

- a compositional preservation rule for shadow-protection audits;
- a counterexample showing why observer-shadow composition fails;
- a typed reason that a fibration or indexed category is needed;
- a proof that set-level fiber-constancy is the right minimal object for now.

## Failure Criteria

Demote categorical language if:

- objects and morphisms are chosen only to force commutative diagrams;
- the construction adds no check beyond the existing capability-spread audit;
- mature domains require incompatible notions of morphism;
- observer changes cannot be typed without reselecting `Cap` by hand.

## First Bounded Run

Use two existing finite families:

1. a typed transport network path;
2. a database/view projection or LossKernel witness-obligation fixture.

Try to express both with the same object/morphism schema. If either cannot be
expressed without hand-built data, record the obstruction and stop.

## Claim Impact If Successful

A successful result supports only this modest claim:

```text
Observer-shadow audits admit a compositional bookkeeping structure in at least
one finite family.
```

It does not prove the North Star geometry.

## Claim Impact If Refuted

If the category fails, preserve the negative result:

```text
The North Star currently needs an atlas of domain-specific audits rather than
a single observer-shadow category.
```

## T470 addendum: bounded composition gate

T470 runs the first bounded object/morphism check requested above:
`results/T470-observer-shadow-composition-gate-v0.1-results.md`; spec
`tests/T470-observer-shadow-composition-gate.md`; model
`models/observer_shadow_composition_gate.py`.

Verdict:

```text
OBSERVER_SHADOW_SCHEMA_BUILT_INDEXED_COMPLETION_REQUIRED_NO_PROMOTION
```

The shared audit-object schema can express both finite families tested:
T37/T41 typed transport and T220 LossKernel factorization. The transport family
shows the obstruction: collapsing two diamond paths to the same endpoint shadow
breaks protection because the paths have different accumulated forgotten
structure and different PO1 capability verdicts. Adding path label and
accumulated forgotten-structure indices repairs the bookkeeping by separating
the shadows.

The LossKernel family gives the positive preservation control: the canonical
same-neighbor pair factors through `nu` and preserves the witness obligation.
The hidden-source escape fails when the source datum is omitted from `nu`, and
is repaired only by state completion, which routes back to ordinary absorption.

This supports an indexed audit-atlas reading, not a single global
observer-shadow category theorem. Future packets must declare source system,
observer/access profile, shadow projection, capability object, native
comparison, and load-bearing indices before morphism comparison; include both
positive preservation and omitted-index hostile controls; and name whether
completion repairs the object or routes to an absorber. No observer-shadow
category theorem, North Star geometry proof, D1/PO1/TF1/LossKernel promotion,
physics/consciousness claim, claim-ledger movement, roadmap movement, or
public-posture movement is earned.

## T472 addendum: index admission gate

T472 turns T470's future-packet minimum into an executable admission gate:
`results/T472-observer-shadow-index-admission-gate-v0.1-results.md`; spec
`tests/T472-observer-shadow-index-admission-gate.md`; model
`models/observer_shadow_index_admission_gate.py`.

Verdict:

```text
OBSERVER_SHADOW_INDEX_GATE_BUILT_COMPLETION_SEPARATED_NO_PROMOTION
```

Endpoint-only transport comparison fails because path label and accumulated
forgotten structure are load-bearing indices. Path-indexed transport is
admitted only as indexed bookkeeping, not as a theorem. LossKernel
neighbor-visible factoring is the genuine preservation control. Hidden-source
omission fails the gate, and hidden-source completion is recorded as ordinary
absorber/state-completion bookkeeping rather than new category evidence.

This adds an index-admission guardrail for future observer-shadow packets:
declare all load-bearing indices before morphism comparison, include one
genuine preservation control, include an omitted-index hostile control, and
separate indexed bookkeeping completion from absorber state completion. No
observer-shadow category theorem, indexed-category/fibration theorem, North
Star geometry proof, D1/PO1/TF1/LossKernel promotion, physics/consciousness
claim, claim-ledger movement, roadmap movement, or public-posture movement is
earned.

## T473 addendum: indexed-composition gate

T473 tests whether T472-admitted indexed packets compose in finite controls:
`results/T473-observer-shadow-indexed-composition-gate-v0.1-results.md`; spec
`tests/T473-observer-shadow-indexed-composition-gate.md`; model
`models/observer_shadow_indexed_composition_gate.py`.

Verdict:

```text
INDEXED_COMPOSITION_GATE_BUILT_ASSOCIATIVE_BOOKKEEPING_ONLY
```

In the finite three-step transport fixture, the current D1 morphism core is
associative up to structural fields, and forgotten-structure index accumulation
is association-invariant. Repeated path-indexed transport packets compose only
as indexed bookkeeping. Repeated LossKernel neighbor-visible preservation
packets compose only as a finite preservation control. Hidden-source completion
taints any composition as absorber/state-completion bookkeeping, rejected T472
packets stay blocked, and transport/LossKernel cross-family composition is
rejected without a declared bridge.

This supports only an indexed audit-atlas guardrail: future observer-shadow
composition packets must declare source/target family, test associativity for
their chosen indices, separate preservation controls from bookkeeping, route
absorber completion outside category evidence, and supply an explicit
cross-family bridge before composing unlike packet families. No observer-shadow
category theorem, indexed-category/fibration theorem, North Star geometry
proof, D1/PO1/TF1/LossKernel promotion, physics/consciousness claim,
claim-ledger movement, roadmap movement, or public-posture movement is earned.
