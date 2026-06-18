# Technical Report: Invariant-Preserving Transformations v0.1

## Summary

T23 tests whether the repository can move toward mathematical independence by
extracting a transport structure from existing Time as Finality results.

The result is promising but not complete: invariant-preserving transformations
now exist as a typed executable kernel, with positive cases, a composition
check, and an obstruction witness. The honest verdict is **proto-independent**.
IPT is strong enough to become the next formal spine of the project, but not
yet strong enough to justify a separate repository or a claim of independent
mathematical theory.

## Formal Object

An invariant-preserving transformation is represented as:

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

A structured object is finite and carries named typed invariants:

```text
StructuredObject = (name, domain, structure_type, invariants)
TypedInvariant = (name, value, value_type, description)
```

An IPT succeeds on its declared invariants when:

1. each declared invariant exists on both source and target;
2. each source value equals the target value for that invariant;
3. no declared obstruction condition is triggered.

This is deliberately conservative. The model does not infer preservation from
semantic similarity, prose analogy, or downstream usefulness.

## Relationship Discipline

T23 classifies cross-domain relationships by proof burden:

| Level | Meaning in T23 |
| --- | --- |
| analogy | Surface similarity. No proof obligation. |
| homology | Shared formal structure or proof pattern under typed assumptions. |
| reduction | Target obtained from source by an explicit map preserving named invariants and losing declared quantities. |
| equivalence | Two structures preserve each other's named invariants under inverse maps. |

T23 establishes no equivalence cases.

## Executable Cases

| Case | Source | Target | Class | Verdict |
| --- | --- | --- | --- | --- |
| observer access restriction | T2 global measurement state | local observer D1 view | reduction | preserves pointer basis and system-record correlation |
| consensus-record theorem transfer | consensus quorum certificate system | record certificate system | homology | preserves quorum-intersection safety |
| quantum redundancy reduction | T2 local observer D1 view | T22 reduction schema | reduction | preserves holder redundancy and accessible support |
| weak quorum boundary | record majority safety | weak quorum record boundary | analogy | rejected as invariant-preserving due to weak-quorum obstruction |

## Composition Theorem

The finite executable composition rule is:

```text
Given IPT f: A -> B and IPT g: B -> C,
the composite preserves requested invariant i when:

1. target(f) = source(g);
2. i is declared preserved by both f and g;
3. source(A).i = target(C).i;
4. no obstruction condition in f or g is triggered.
```

This is not yet a category-theoretic theorem. It is a finite theorem schema
implemented over typed records.

Positive composition:

```text
T2 global measurement state
  -> T2 local observer D1 view
  -> T22 reduction schema
```

Requested invariant:

```text
pointer_basis = computational_z
```

Result: preserved.

## Obstruction Theorem

The weak-quorum boundary gives the first executable obstruction:

```text
n = 4
q = 2
2q > n is false
```

So quorum-intersection safety is not preserved:

```text
consensus majority safety
  -> record majority safety
  -> weak quorum boundary
```

The model reports:

```text
theorem_status = composition_blocked_by_obstruction
```

This matters because the IPT kernel is not only a way to draw analogies. It can
refuse transformations that break named invariants.

## Independence Audit

| Criterion | Status | Interpretation |
| --- | --- | --- |
| Formal IPT definition | pass | The core object is explicit and executable. |
| Multiple domains through same interface | pass | Observer access, consensus theorem transfer, and quantum redundancy use one typed interface. |
| Composition law | pass, finite | A conservative composition check exists. |
| Obstruction handling | pass, finite | The weak-quorum boundary blocks preservation. |
| Representation theorem | missing | No theorem yet says all valid IPTs have this form. |
| External non-TaF domain | missing | All positive cases are inherited from existing TaF test tracks. |
| Equivalence results | absent by design | No inverse-map equivalence is claimed. |

## Verdict

T23 moves the project from "Time as Finality explains many domains" toward
"there may be a general theory of invariant transport behind these domains."

But the current kernel is not mathematically independent yet. It is
**proto-independent**:

- strong enough to guide the next phase of formalization;
- strong enough to add a new test track and claim-led documentation;
- not strong enough for a separate repo;
- not strong enough for a publishable representation theorem.

## Recommendation

Keep IPT inside this repository for one more phase. The next grand goal should
prove or reject a representation theorem:

```text
Every admissible observer-change, theorem-transfer, or record-reduction map
that preserves a named invariant factors through the IPT interface.
```

A new repository becomes justified when IPT has:

1. a representation theorem or uniqueness theorem;
2. at least one external domain not derived from Time as Finality;
3. one impossible-transformation theorem that does not depend on D1 language;
4. clear examples at analogy, homology, reduction, and equivalence levels.

## Artifacts

- [`tests/T23-invariant-preserving-transformations.md`](tests/T23-invariant-preserving-transformations.md)
- [`models/invariant_preserving_transformations.py`](models/invariant_preserving_transformations.py)
- [`models/run_t23.py`](models/run_t23.py)
- [`tests/test_invariant_preserving_transformations.py`](tests/test_invariant_preserving_transformations.py)
- [`results/invariant-preserving-transformations-v0.1.json`](results/invariant-preserving-transformations-v0.1.json)
- [`results/invariant-preserving-transformations-v0.1-results.md`](results/invariant-preserving-transformations-v0.1-results.md)
