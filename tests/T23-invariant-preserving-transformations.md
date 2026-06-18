# T23: Invariant-Preserving Transformations

## Target Claims

- D1: physical finality definition
- Q1: quantum under-finalization
- A1: distributed-systems finality analogy
- IPT: invariant-preserving transformations
- T2: quantum measurement record finality
- T20: consensus-record theorem transfer
- T22: D1 physical reduction map

## Setup

Define an invariant-preserving transformation as a typed finite object:

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

The executable model represents each source and target as a finite structured
object with named, typed invariants. A transformation succeeds only when every
declared preserved invariant agrees between source and target and no declared
obstruction condition is triggered.

T23 instantiates the same interface on four cases:

| Transformation | Relationship class | Domains | Result |
| --- | --- | --- | --- |
| observer access restriction | reduction | quantum measurement -> observer access | preserves pointer basis and system-record correlation |
| consensus-record theorem transfer | homology | distributed consensus -> physical record finality | preserves quorum-intersection safety |
| quantum redundancy reduction | reduction | observer access -> D1 physical reduction schema | preserves holder redundancy and accessible support |
| weak quorum boundary | analogy | record finality -> weak quorum record boundary | triggers weak-quorum obstruction |

## Success Criteria

- A precise relationship taxonomy distinguishes analogy, homology, reduction,
  and equivalence.
- At least three positive transformations use the same typed IPT interface.
- The model distinguishes preserved invariants from allowed losses.
- The model reports triggered obstructions separately from ordinary invariant
  mismatch.
- At least one compositional positive case is executable.
- At least one compositional obstruction case is executable.
- The output gives a repo-level independence verdict.

## Failure Criteria

- Every cross-domain case requires a different interface.
- The interface cannot distinguish analogy from reduction or homology.
- The composition rule silently preserves invariants across triggered
  obstructions.
- The model treats any case as equivalence without inverse maps.
- The result claims mathematical independence without a representation theorem
  or a domain outside the Time as Finality test suite.

## Known Constraints

- T23 does not prove that all Time as Finality domains are equivalent.
- T23 does not prove that IPT is ready for a separate repository.
- T23 does not replace D1; it tests whether D1, Q1, A1, T2, T20, and T22 can
  be expressed through one transport interface.
- T23 is finite and standard-library executable. It is not a categorical
  semantics or general representation theorem.
- T24 shows that future IPT tests should transport D1 field values when
  observer graph, scale, time, or gluing data matters.

## Executable Artifacts

```bash
python -m unittest tests.test_invariant_preserving_transformations -v
python -m models.run_t23
```

Artifacts:

- [`models/invariant_preserving_transformations.py`](../models/invariant_preserving_transformations.py)
- [`models/run_t23.py`](../models/run_t23.py)
- [`tests/test_invariant_preserving_transformations.py`](test_invariant_preserving_transformations.py)
- [`results/invariant-preserving-transformations-v0.1.json`](../results/invariant-preserving-transformations-v0.1.json)
- [`results/invariant-preserving-transformations-v0.1-results.md`](../results/invariant-preserving-transformations-v0.1-results.md)

## Contribution Needed

Turn the finite IPT kernel into a representation theorem. The next test should
add at least one domain not inherited from the existing Time as Finality suite
and prove which invariants are forced by the IPT axioms rather than selected by
hand.

## T24 Follow-On

[T24](T24-d1-multiscale-observer-field.md) upgrades the likely target of the
representation theorem. IPT should not only transport isolated observer D1
profiles. It should also state when transport preserves a D1 field's local
profiles, graph edges, trust paths, and gluing constraints.
