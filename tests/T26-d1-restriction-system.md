# T26: D1 Restriction System

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D1-Field: Multiscale Observer Finality](../claims/D1-field-multiscale-observer-finality.md)
- [IPT: Invariant-Preserving Transformations](../claims/IPT-invariant-preserving-transformations.md)
- [T25: Minimal D1 Generalization](T25-minimal-d1-generalization.md)

## Question

Can the graph-indexed D1 restriction system identified by T25 be defined as a
precise finite mathematical object?

T26 tests this without assuming that full sheaf language or full IPT
representation is already justified.

## Competing Hypotheses

```text
H0: informal graph metadata is sufficient.
H1: finite graph-indexed D1 restriction system is sufficient.
H2: presheaf or sheaf structure is already required.
H3: categorical morphism structure is already required for IPT.
H4: no canonical formalization is currently justified.
```

## Formal Object

```text
D1RestrictionSystem =
  sites
  local D1 profiles
  proposition values
  trusted transport edges
  optional overlap tests
  optional patch constraints
  projection maps
  compatibility predicate
  global-section predicate
```

## Executable Criteria

- Validate finite axioms for all reused T25 scenarios.
- Recover scalar D1 in the uniform case.
- Recover vector D1 in the trusted-chain divergent-profile case.
- Detect graph necessity when the same vector has different trusted
  reachability.
- Detect a finite gluing obstruction.
- Execute one positive restriction morphism.
- Execute one failed restriction morphism.
- Defer full IPT representation if the required structure is absent.

## Result

Implemented as T26 v0.1.

Best-supported hypothesis:

```text
H1: finite graph-indexed D1 restriction system is sufficient.
```

The result upgrades T25's recommendation into an explicit object:

```text
D1RestrictionSystem
```

Scalar and vector D1 are now projection maps from this object. Full sheaf
semantics and full IPT representation remain deferred.

## Reproduction

```bash
python -m unittest tests.test_d1_restriction_system -v
python -m models.run_t26
```

Artifacts:

- [`models/d1_restriction_system.py`](../models/d1_restriction_system.py)
- [`models/run_t26.py`](../models/run_t26.py)
- [`tests/test_d1_restriction_system.py`](test_d1_restriction_system.py)
- [`results/d1-restriction-system-v0.1.json`](../results/d1-restriction-system-v0.1.json)
- [`results/d1-restriction-system-v0.1-results.md`](../results/d1-restriction-system-v0.1-results.md)

## Contribution Needed

Define composition laws for D1 restriction morphisms. That is the next missing
step before attempting a full IPT representation theorem.
