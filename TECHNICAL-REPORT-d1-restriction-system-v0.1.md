# Technical Report: D1 Restriction System v0.1

## Summary

T26 formalizes the finite graph-indexed object selected by T25. The result is
not a full sheaf theory and not a full IPT representation theorem. It is a
finite local-to-global structure that is strong enough to reproduce the current
scalar, vector, graph, gluing, and morphism tests.

Best-supported hypothesis:

```text
H1: finite graph-indexed D1 restriction system is sufficient.
```

## Definition

T26 defines:

```text
D1RestrictionSystem =
  finite observer sites
  one local D1 profile per site
  one proposition value per site
  trusted transport edges
  optional overlap tests
  optional finite patch constraints
  scalar and vector projection maps
  compatibility and global-section predicates
```

The object is intentionally smaller than a sheaf. It stores the finite data
needed by the current repo tests without importing unnecessary continuous,
topological, or categorical machinery.

## Axioms

| Axiom | Meaning |
| --- | --- |
| A1 | observer sites are finite and unique |
| A2 | each site has one local D1 profile and proposition value |
| A3 | transport edges reference known sites |
| A4 | patches reference known sites and closed finite variables |
| A5 | D1 dimensions are nonnegative integers |
| A6 | local compatibility is checked before global-section claims |
| A7 | morphisms preserve declared local dimensions and selected global obstructions |

## Hypothesis Comparison

| ID | Hypothesis | T26 status |
| --- | --- | --- |
| H0 | informal graph metadata is sufficient | rejected |
| H1 | finite graph-indexed D1 restriction system is sufficient | best supported |
| H2 | presheaf or sheaf structure is already required | not required by current evidence |
| H3 | categorical morphism structure is already required for IPT | partially supported but deferred |
| H4 | no canonical formalization is currently justified | not best supported |

## Theorem Ladder

### 1. Minimal Axiom Sufficiency Theorem

Reached.

```text
The finite axioms validate every T25 scenario used by T26.
```

Boundary: this is finite validation only. It does not claim continuous or
Lorentz-covariant semantics.

### 2. Scalar Recovery Theorem

Reached.

```text
Scalar D1 is recovered when local profiles are uniform and no transport or
gluing data is lost.
```

Boundary: scalar projection fails as a general global object when local
profiles diverge, transport matters, or patches are present.

### 3. Vector Recovery Theorem

Reached.

```text
Vector D1 is faithful when observer profiles diverge but graph and gluing data
add no distinction.
```

Boundary: vector projection fails when reachability or patch compatibility
matters.

### 4. Graph Necessity Theorem

Reached.

```text
Graph transport data is necessary when identical vectors have different trusted
reachability.
```

Boundary: this does not require sheaf language by itself.

### 5. Gluing Obstruction Theorem

Reached.

```text
Locally satisfiable D1 patches need not admit a global assignment.
```

Boundary: this is a finite obstruction. Cohomological semantics remain a
candidate extension, not a required assumption.

### 6. Restriction Morphism Theorem

Reached.

```text
A D1 restriction morphism is executable and can distinguish preserved transport
from failed transport.
```

T26 includes:

- a positive relabeling morphism that preserves local profiles and trusted
  reachability;
- a failed connected-to-partitioned morphism blocked by
  `trust_path_not_preserved`.

### 7. IPT Representation Theorem

Not reached.

This is an informative boundary. Current T23 IPT objects still lack:

- site maps;
- restriction-map commutation checks;
- obstruction preservation across composed IPTs;
- domain-independent morphism typing.

## Informative Failures

| Attempted claim | Failure | Boundary |
| --- | --- | --- |
| scalar projection is generally faithful | scalar projection loses observer distribution, graph data, or patch data | scalar D1 remains valid as a local or recovered projection |
| vector projection is generally faithful | identical vectors can differ in trusted reachability | vector D1 remains valid for observer-distribution snapshots |
| local compatibility implies global section | local patch witnesses do not globalize | full sheaf language remains optional, not disproved |
| current IPT already has full D1 restriction representation | T23 IPT objects lack site maps and restriction commutation data | T26 supplies a target morphism notion for later IPT work |

## Recommendation

Adopt `D1RestrictionSystem` as the repo's next formal D1 extension.

Use:

- scalar D1 for fixed-site or uniform projections;
- vector D1 for observer-distribution snapshots;
- graph and patch data for transport and gluing claims;
- restriction morphisms for the next IPT readiness step.

Do not yet claim full sheaf semantics or a full IPT representation theorem.

## Artifacts

- [`tests/T26-d1-restriction-system.md`](tests/T26-d1-restriction-system.md)
- [`models/d1_restriction_system.py`](models/d1_restriction_system.py)
- [`models/run_t26.py`](models/run_t26.py)
- [`tests/test_d1_restriction_system.py`](tests/test_d1_restriction_system.py)
- [`results/d1-restriction-system-v0.1.json`](results/d1-restriction-system-v0.1.json)
- [`results/d1-restriction-system-v0.1-results.md`](results/d1-restriction-system-v0.1-results.md)
