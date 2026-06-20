# Typed Forgetting and Local-to-Global Obstruction in Finite Record Systems

## Status

Draft neutral mathematical program note.

## Abstract

We study finite systems of local records connected by typed restriction and
projection maps. Each system consists of finite sites, local values, patch
constraints, and a global-assignment predicate. Morphisms map sites and declare
preserved and forgotten structure. We define admissibility conditions for
information-losing morphisms and distinguish local satisfiability, endpoint
admissibility, and pathwise admissibility. The finite gluing obstruction itself
reduces to known signed-graph parity constraint satisfaction, but the typed
attribution layer adds data not present in ordinary CSP: typed source and target
systems, explicit forgotten structure, preserved structure, path-dependent
accumulated loss, and non-functorial obstruction attribution. The goal is a
finite calculus for when projection, restriction, or morphism composition
creates, hides, displaces, or reveals local-to-global obstruction.

## Framing

This note avoids the following as primitives:

- time;
- consciousness;
- physics;
- quantum mechanics;
- observer interpretation.

The question is whether the mathematics survives without Time as Finality
framing.

## Core Objects

### Finite Restriction System

```text
RestrictionSystem =
  finite sites
  local values
  patch constraints
  compatibility predicate
  global-assignment predicate
```

### Typed Morphism

```text
TypedMorphism =
  source system
  target system
  total site map
  preserved structure
  forgotten structure
```

### Loss Kernel

```text
LossKernel(f) = typed structure forgotten by morphism f
```

The LossKernel phase asks whether `forgotten_structure` can be upgraded from
metadata into a composable mathematical object.

### Admissible Obstruction Attribution

A projection-obstruction event is not merely:

```text
source satisfiable
target obstructed
```

It also requires:

```text
projection definable
loss named and typed
loss relevant to the target obstruction
```

## Known Results To Reframe Neutrally

| Repo result | Neutral mathematical reading |
| --- | --- |
| T26 | Finite graph-indexed restriction systems are sufficient for scalar/vector/transport/gluing cases. |
| T29-T33 | Projection obstruction requires typed source/target data plus named forgotten structure. |
| T34 | Endpoint obstruction can emerge, propagate, or be absorbed along a morphism chain. |
| T37 | Same endpoints can have different admissibility verdicts because paths accumulate different forgotten structure. |
| T39 | The gluing obstruction is signed-graph parity CSP; typed attribution is the added layer. |
| T40 | Cross-level obstruction attribution requires named cross-level forgotten dimensions. |
| T41 | Restriction morphisms form a category; obstruction admissibility is not a Boolean functor. |

## Candidate Theorem Units

### 1. CSP Equivalence With Typed Attribution

The finite local-to-global obstruction is equivalent to a parity-conflicting
binary CSP, but ordinary CSP does not express typed source, typed target,
forgotten structure, or admissibility classification.

### 2. Typed Transport Category

Restriction morphisms compose associatively and admit identity morphisms.
Therefore they form a category.

### 3. Non-Functorial Obstruction Admissibility

The predicate "is an admissible projection obstruction" is not a Boolean functor
from the restriction-morphism category to truth values.

### 4. Path-Dependent Admissibility

In a typed transport network, two paths with the same source and target can
yield different admissibility verdicts when their accumulated forgotten
structure differs.

### 5. Loss Kernel Attribution Lemma

A projection-created obstruction is admissibly attributable only when the
projection carries a typed loss object naming structure that resolves the
obstruction in the source.

This fifth item is not yet proved. It is the next formal target.

## Prior-Art Discipline

The following should be foregrounded in any external version:

- gluing obstruction is known;
- signed-graph parity CSP is known;
- sheaf/contextuality obstruction is known;
- category-theoretic morphism language is known.

The possible contribution is the typed attribution calculus around finite
satisfiability loss, not the existence of local-to-global obstruction.

## Publishability Assessment

This is not yet a mature mathematical paper. It can become a workshop-style
note if the next pass does three things:

1. Define `LossKernel` as first-class data.
2. Prove or executable-check identity and composition laws over T34/T37.
3. State TF1 as a precise lemma with at least one counterexample boundary.

## Working Title Options

- Typed Forgetting and Local-to-Global Obstruction in Finite Record Systems
- Finite Typed Lossy Constraint Projections
- Path-Dependent Admissibility Under Information-Losing Morphisms
- Typed Obstruction Attribution for Finite Restriction Systems
