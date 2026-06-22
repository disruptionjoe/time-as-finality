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
