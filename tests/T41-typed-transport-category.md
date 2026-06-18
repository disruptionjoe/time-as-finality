# T41: Typed Transport Category Prototype

## Target Claims

- D1 (D1RestrictionSystem as finite graph-indexed object)
- PO1 (Projection-Obstruction Schema)
- IPT (Invariant-Preserving Transformations)
- T26 (D1 restriction system)
- T31 (PO1 admissibility)
- T34 (PO1 chain theorem — endpoint independence)
- T37 (TypedTransportNetwork — path-dependent admissibility)

## Setup

Construct four minimal D1RestrictionSystems (Cat_A through Cat_D). Define
D1RestrictionMorphisms between them with varying preserved_dimensions subsets.
Import `_compose_morphisms` from transport_network.py. Implement `make_identity`
as a new constructor.

Category law tests:
- Associativity: (f;g);h == f;(g;h) for four composable triples.
- Left unit: id_{source(f)};f == f for five morphisms.
- Right unit: f;id_{target(f)} == f for five morphisms.
- Equality comparison: modulo morphism name (metadata), comparing source.name,
  target.name, site_map as frozenset of (src, tgt) pairs, preserved_dims as
  frozenset.

PO1 functor test:
- Build three systems: SRC (rich, unobstructed), MID (restricted, unobstructed),
  TGT (restricted, obstructed via 3-site gluing conflict).
- Check: f: SRC→MID (not PO1 — AC6 fails, no target obstruction).
- Check: g: MID→TGT (not PO1 — AC5 fails, no declared forgotten structure).
- Check: f;g: SRC→TGT (PO1 — SRC unobstructed, TGT obstructed, accumulated
  forgotten structure from f gives non-empty forgotten, profile loss from
  rich→restricted makes AC5 pass).
- Boolean "and" functor predicts: PO1(f;g) = PO1(f) ∧ PO1(g) = False ∧ False = False.
- Actual: PO1(f;g) = True. Functor law violated.

## Success Criteria

1. All four associativity tests pass (both site_map and preserved_dims components).
2. All five left unit tests pass.
3. All five right unit tests pass.
4. D1RestrictionMorphisms are declared to form a proper category.
5. PO1 functor test witnesses at least one violation of the Boolean-and functor law.
6. H_A (proper category) is best supported.
7. H_C (PO1 non-functor) is supported.

## Failure Criteria

1. Any associativity test fails: implementation bug in `_compose_morphisms`.
2. Any identity law test fails: `make_identity` constructor is malformed.
3. PO1(f;g) = False: the scenario construction is wrong.
4. PO1(f) = True or PO1(g) = True: the scenario doesn't isolate the functor failure.

## Known Physics Constraints

None directly. T41 is a pure mathematical structure theorem about the
D1RestrictionMorphism framework. The result confirms that the mathematical
objects accumulated from T26-T40 form a proper category, which is a
foundational prerequisite for applying standard categorical tools (functors,
natural transformations, adjunctions) to D1 transport problems.

## Contribution Needed

- Formal proof of associativity and identity laws (currently proved by
  construction; a written proof sketch is provided in the module docstring).
- Characterization of the full hom-sets Hom(A, B) for two D1RestrictionSystems.
- Investigation of whether PO1 can be made into a lax functor or indexed family.
- Check whether TypedTransportNetworks are internal categories in D1Cat.
