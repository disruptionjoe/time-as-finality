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

Independence requires at least:

1. a representation theorem or uniqueness theorem;
2. one domain not inherited from the existing Time as Finality test suite;
3. a nontrivial obstruction theorem not imported from D1 or quorum language;
4. clear examples that separate analogy, homology, reduction, and equivalence.

## Tests

- [T23: Invariant-Preserving Transformations](../tests/T23-invariant-preserving-transformations.md)
- [T24: D1 Multiscale Observer Field](../tests/T24-d1-multiscale-observer-field.md)

## Contribution Needed

Prove or reject a representation theorem for admissible IPTs. The next model
should include one external domain and show whether the same finite interface
still preserves meaningful invariants without importing Time as Finality
vocabulary.
