# IPT: Invariant-Preserving Transformations

## Claim

Observer changes, theorem transfers, record reductions, and obstruction
boundaries may share a substrate-neutral mathematical transport structure:
the invariant-preserving transformation.

The current version is:

```text
IPT = (
  source structure,
  target structure,
  transformation map,
  preserved invariants,
  allowed losses,
  obstruction conditions
)
```

## Class

Formal kernel.

## Status

Proto-independent.

## What This Does Not Claim

- It does not claim that all domains are equivalent.
- It does not claim that physics, consensus, cognition, and social reality are
  one phenomenon.
- It does not claim that Time as Finality should become a new repository yet.
- It does not claim an equivalence result without inverse maps.
- It does not provide a representation theorem.

## Why It Might Be True

Several successful repo tests already depend on structural preservation:

- T2 restricts a global measurement record to an observer access window while
  preserving pointer-basis and correlation invariants.
- T20 transfers quorum-intersection safety from distributed consensus to
  physical record finality.
- T22 reduces a local quantum-measurement D1 profile to a physical reduction
  schema for holder redundancy and accessible support.
- T24 shows that IPT should often transport local D1 field values rather than
  a single global D1 profile when communication graph or gluing data matters.
- T25 earns only a one-site local IPT morphism result and defers full IPT
  representation until site maps and restriction-map commutation are part of
  the formal object.
- T26 defines D1 restriction morphisms with explicit site maps, local-profile
  preservation, trusted-reachability preservation, and obstruction-status
  preservation.

T23 shows that these are not merely written in similar language. They can be
encoded with one typed interface, tested for invariant preservation, composed,
and rejected when an obstruction fires.

## How It Could Fail

- The interface may be too weak: any map can be forced into it by hand.
- The interface may be too narrow: future domains may require incompatible
  preservation semantics.
- The positive cases may only work because they were inherited from the same
  Time as Finality vocabulary.
- The composition rule may fail under richer transformations.
- No representation or uniqueness theorem may exist.

## T23 Result

[T23](../tests/T23-invariant-preserving-transformations.md) implements four
finite IPT cases:

| Case | Class | Result |
| --- | --- | --- |
| observer access restriction | reduction | preserves pointer basis and system-record correlation |
| consensus-record theorem transfer | homology | preserves quorum-intersection safety |
| quantum redundancy reduction | reduction | preserves holder redundancy and accessible support |
| weak quorum boundary | analogy | triggers a weak-quorum obstruction |

The positive composition is:

```text
T2 global measurement state
  -> T2 local observer D1 view
  -> T22 reduction schema
```

with:

```text
pointer_basis = computational_z
```

The obstruction composition is:

```text
record majority safety
  -> weak quorum record boundary
```

where `n = 4`, `q = 2`, and `2q > n` is false.

## Independence Verdict

T23 gives IPT a **proto-independent** status. It is now a candidate
mathematical spine for the next phase of the project, but not an independent
theory.

## T25 Result

[T25](../tests/T25-minimal-d1-generalization.md) tests whether IPT should be
upgraded directly to a representation theorem over D1 local-to-global
structure.

The result is conservative:

- a one-site local morphism succeeds for the quantum redundancy reduction;
- the weak-quorum boundary remains an obstructed morphism;
- full IPT representation is deferred because T23 IPTs do not yet carry site
  maps or restriction-map commutation data.

This keeps IPT at `proto_independent`.

## T26 Result

[T26](../tests/T26-d1-restriction-system.md) supplies a candidate target object
for later IPT representation work:

```text
D1RestrictionSystem
```

It also defines executable restriction morphisms. The positive case preserves
local profiles and trusted reachability under relabeling. The negative case
fails because trusted reachability is not preserved:

```text
trust_path_not_preserved
```

This is a readiness result, not a representation theorem. Current T23 IPT
objects still need site maps, restriction-map commutation checks, obstruction
preservation across composed IPTs, and domain-independent morphism typing.

Independence requires at least:

1. a representation theorem or uniqueness theorem;
2. one domain not inherited from the existing Time as Finality test suite;
3. a nontrivial obstruction theorem not imported from D1 or quorum language;
4. clear examples that separate analogy, homology, reduction, and equivalence.

## Tests

- [T23: Invariant-Preserving Transformations](../tests/T23-invariant-preserving-transformations.md)
- [T24: D1 Multiscale Observer Field](../tests/T24-d1-multiscale-observer-field.md)
- [T25: Minimal D1 Generalization](../tests/T25-minimal-d1-generalization.md)
- [T26: D1 Restriction System](../tests/T26-d1-restriction-system.md)

## Contribution Needed

First define composition laws for D1 restriction morphisms. Then prove or
reject a representation theorem for admissible IPTs over
`D1RestrictionSystem`, with at least one external domain that does not import
Time as Finality vocabulary.
