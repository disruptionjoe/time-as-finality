# T25: Minimal D1 Generalization

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D1-Field: Multiscale Observer Finality](../claims/D1-field-multiscale-observer-finality.md)
- [IPT: Invariant-Preserving Transformations](../claims/IPT-invariant-preserving-transformations.md)
- [T13: Finality Sheaf Cohomology](T13-finality-sheaf-cohomology.md)
- [T21: Bell Contextuality Finality](T21-bell-contextuality-finality.md)
- [T23: Invariant-Preserving Transformations](T23-invariant-preserving-transformations.md)
- [T24: D1 Multiscale Observer Field](T24-d1-multiscale-observer-field.md)

## Question Zero

Before asking whether D1-Field exists, T25 asks:

```text
What is the minimal mathematical structure required before a field-like
generalization becomes unavoidable?
```

T25 compares scalar, vector, graph-indexed, sheaf-like, and noncanonical
alternatives without assuming that any one of them is correct.

## Competing Hypotheses

```text
H0: Scalar D1 is sufficient.
H1: Vector-valued D1 is sufficient.
H2: Field-valued D1 is required.
H3: Another finite local-to-global structure is required.
H4: No canonical generalization is currently justified.
```

## Setup

T25 reuses T24's finite observer-field cases and adds a trusted-chain case
where vector-valued D1 is enough. It then evaluates an incremental theorem
ladder:

1. scalar recovery theorem;
2. vector sufficiency theorem;
3. transport necessity theorem;
4. gluing obstruction theorem;
5. local morphism theorem;
6. IPT representation theorem, attempted only if justified.

## Success Criteria

- All five hypotheses H0 through H4 are explicitly evaluated.
- At least one scalar recovery condition is executable.
- At least one vector-sufficient case is executable.
- At least one vector-insufficient transport case is executable.
- At least one local-to-global obstruction case is executable.
- At least one local IPT factorization is tested.
- At least one failed or deferred theorem attempt is preserved as an
  informative result.
- The final recommendation identifies the simplest supported mathematical
  object.

## Failure Criteria

- The implementation assumes D1-Field or sheaf language in advance.
- The report treats failure to prove full IPT representation as project
  failure.
- Negative results are hidden or renamed as success.
- The recommendation chooses the richest structure rather than the smallest
  sufficient one.

## Result

Implemented as T25 v0.1.

Best-supported hypothesis:

```text
H3: another finite local-to-global structure is required.
```

T25's recommended object is:

```text
finite graph-indexed local-to-global D1 restriction system
```

with:

- local D1 profiles;
- observer sites;
- trusted transport edges;
- optional patch constraints.

Scalar and vector D1 remain valid special cases. Full sheaf language and full
IPT representation are deferred.

## Reproduction

```bash
python -m unittest tests.test_minimal_d1_generalization -v
python -m models.run_t25
```

Artifacts:

- [`models/minimal_d1_generalization.py`](../models/minimal_d1_generalization.py)
- [`models/run_t25.py`](../models/run_t25.py)
- [`tests/test_minimal_d1_generalization.py`](test_minimal_d1_generalization.py)
- [`results/minimal-d1-generalization-v0.1.json`](../results/minimal-d1-generalization-v0.1.json)
- [`results/minimal-d1-generalization-v0.1-results.md`](../results/minimal-d1-generalization-v0.1-results.md)

## Contribution Needed

T26 formalizes the graph-indexed D1 restriction system as
`D1RestrictionSystem`. The next contribution is to define composition laws for
restriction morphisms before attempting either full sheaf semantics or a full
IPT representation theorem.
