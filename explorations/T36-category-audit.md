# T36 Category Theory / Functorial Semantics Audit

## Verdict

The repo has a credible finite local-to-global obstruction formalism, but not
yet a category-theoretic or functorial semantics. The closest honest statement
is:

```text
PO1 is a predicate on typed pairs of finite D1RestrictionSystems
connected by a definable, lossy site-map projection.
```

Do not call current projections functors. Do not call T35 a finite category.
Do not call AC3 failures category failures except as "not morphisms in the
current T26 site-map formalism."

## Closest Existing Mathematics

- Finite CSP / constraint-hypergraph satisfiability: patches are finite
  constraints; global sections are satisfying assignments.
- Sheaf-style gluing obstruction, but only as a finite analogue. No presheaf
  category, restriction maps, cochains, or cohomology group are defined.
- Model reduct / forgetful-map semantics is nearby, but PO1 is not pure
  reduct: the target often has a different restricted constraint class.
- A possible future functor is `R(S) = global_assignment_exists` into the
  two-point poset, but only after a real projection category exists.

## Clean Mappings

- Objects: valid `D1RestrictionSystem`s are the best candidate objects.
- Internal data: sites, local D1 profiles, transport edges, patches, overlap
  tests.
- Global section: finite satisfying assignment over all patch constraints.
- Obstruction: local patches satisfiable and no global assignment.
- Morphism candidate: `D1RestrictionMorphism` with source, target, total or
  partial site map, preserved dimensions, trust-path flag, and
  obstruction-preservation flag.
- PO1 instance: a `ProjectionCase` where the richer system has a global
  assignment, the restricted system has a gluing obstruction, the site map is
  total, and named/measurable structure is lost.

## Failed or Weak Mappings

- `D1RestrictionMorphism` is not yet a categorical morphism class. There is no
  identity operation, composition operation, associativity proof, or closure
  theorem.
- Positive PO1 projections are usually not `reached` preservation morphisms.
  AC5 requires measurable loss, while `analyze_morphism(...).reached` requires
  local profile preservation.
- Scalar and vector projections are functions/views from systems to summaries.
  They do not map morphisms, so they are not functors.
- T23's `compose_ipts` is an executable composition check over selected
  invariants, not categorical composition.
- T34 analyzes endpoint pairs in chains; it does not construct the composite
  arrow.
- T35 enumerates a finite directed search space of generated systems and
  projection candidates. It does not include identities or closure under
  composition.

## Overclaims

- Names like `*_functor` should be treated as informal labels, not
  mathematical functors.
- "Category change" should be weakened to "not definable by the current total
  site-map projection."
- "H1 cohomological" is too strong unless cochains, coboundaries, and
  cohomology classes are actually defined. "Finite gluing obstruction" is
  earned.
- "Valid typed morphism + strict resource decrease" is misleading if
  "morphism" means preservation morphism. PO1 needs lossy projection arrows,
  not preservation arrows.
- "Resource-monotonicity theorem" is currently a checked polarity pattern, not
  a theorem over a proved category/order of projections.

## Underdeveloped Mathematics

- The repo has not chosen the category: preservation morphisms, lossy
  projections, partial maps, spans, or something else.
- Arrow orientation drifts. Code uses richer-to-restricted projections, while
  some theorem language suggests the opposite variance.
- AC5 is metadata, not first-class structure. This blocks functorial treatment
  of forgotten structure.
- Composition of loss is not defined. T34 explicitly needs cumulative AC5.
- Non-monotone transformations, such as optimizer recovery in T34, do not fit
  the current restriction direction.
- Site maps alone do not provide sheaf restriction maps.

## Required Mathematics Before Serious Uptake

1. Define a category `D1Proj`, or prove no such category is appropriate.
2. Specify objects, arrows, identities, composition, and typing.
3. Decide whether positive PO1 arrows are lossy projection arrows rather than
   preservation morphisms.
4. Prove closure of composition and identity laws.
5. Make forgotten structure first-class on arrows, with compositional union or
   another law.
6. Define scalar/vector/global-assignment views on arrows before calling them
   functors.
7. If using sheaf language, define the finite site category, presheaf of
   assignments, restriction maps, and global section as a limit/equalizer.

## Recommended Next Theorem or Counterexample

Prove this disambiguation theorem:

```text
In the category whose arrows are only D1RestrictionMorphisms with reached=True,
no fully admissible PO1 projection is an arrow.
```

Reason: PO1 requires AC5 measurable loss, while `reached=True` requires local
profile preservation. If this theorem holds, define a separate category of
lossy projections:

```text
objects = valid D1RestrictionSystems
arrows = total site maps + declared loss/forgotten-structure metadata
identity = identity site map + empty loss
composition = composed site maps + accumulated loss metadata
```

Then prove or refute T34 as a real composition theorem in that category.

## Notes for Synthesis

The synthesis should say: PO1 is category-ready, not category-theoretic yet.

Best current framing:

```text
finite local-to-global obstruction under typed lossy projection
```

Avoid:

```text
forgetful functor
finite category of projections
categorical failure
cohomology theorem
universal construction
```

T35's strongest contribution is generative finite search over projection
candidates, not categorical semantics. Its output can seed a future finite
category, but does not yet define one.
