# Technical Report: Minimal D1 Generalization v0.1

## Summary

T25 asks what mathematical structure is minimally required to generalize D1
without overfitting. It does not assume D1-Field, sheaf language, or IPT
representation in advance.

The executable result supports a modest conclusion:

```text
H3: another finite local-to-global structure is required.
```

The smallest earned structure is a graph-indexed D1 restriction system. Scalar
D1, vector D1, field language, sheaf language, and IPT representation are all
treated as candidates or special cases, not destinations.

## Question Zero

The investigation begins with:

```text
What is the minimal mathematical structure required before a field-like
generalization becomes unavoidable?
```

T25's answer:

```text
local D1 profiles
+ observer sites
+ trusted transport edges
+ optional patch constraints
```

This is less than a full sheaf theory and more than a vector.

## Hypotheses

| ID | Hypothesis | T25 status |
| --- | --- | --- |
| H0 | Scalar D1 is sufficient. | rejected for multiscale claims |
| H1 | Vector-valued D1 is sufficient. | partially supported but insufficient |
| H2 | Field-valued D1 is required. | partially supported |
| H3 | Another finite local-to-global structure is required. | best supported |
| H4 | No canonical generalization is currently justified. | not best supported |

## Candidate Structures

### Scalar D1

Scalar D1 here means one selected or aggregated D1 profile, not a literal real
number.

It succeeds when:

- one observer is explicitly fixed;
- all observer sites share one profile;
- trusted transport is connected;
- no gluing constraints are in scope.

It fails when observer distribution, transport, or gluing matters.

### Vector D1

Vector D1 succeeds in the trusted-chain case where observer profiles diverge
but graph transport and gluing add no extra distinction.

It fails when two scenarios have the same observer-profile vector but different
trust-path reachability.

### Graph-Indexed Restriction System

This is the best-supported structure in T25.

It carries:

- local D1 profiles;
- observer sites;
- transport edges;
- trust-preserving labels;
- optional patch constraints.

It explains the scalar recovery, vector sufficiency, transport necessity, and
gluing obstruction cases without requiring full sheaf language.

### Presheaf Or Sheaf Language

Sheaf language remains promising, especially for T13/T21-style obstruction.
But T25 does not force it. The finite evidence is handled by graph-indexed
restriction and patch constraints.

### IPT Representation

T25 earns a local morphism theorem: the T23 quantum redundancy reduction
factors through a one-site D1 structure because it preserves declared local D1
invariants.

It does not earn the full IPT representation theorem. Current IPTs do not
carry site maps or restriction-map commutation data.

## Theorem Ladder

### 1. Scalar Recovery Theorem

Reached.

```text
If all local D1 profiles are uniform, trusted transport is connected, and no
gluing constraints are in scope, scalar D1 recovers without material loss.
```

### 2. Vector Sufficiency Theorem

Reached.

```text
If local profiles diverge but transport is trusted/connected and no gluing
constraints are in scope, vector D1 is sufficient.
```

### 3. Transport Necessity Theorem

Reached.

```text
If two cases have the same observer-profile vector but different trust-path
reachability, graph transport data is required.
```

### 4. Gluing Obstruction Theorem

Reached.

```text
Local D1-compatible patches can be individually satisfiable while no global
assignment exists.
```

### 5. Morphism Theorem

Reached locally only.

```text
A local IPT can factor through a one-site D1 restriction system when it
preserves declared local D1 invariants.
```

### 6. IPT Representation Theorem

Not reached.

This is an informative negative result. A full theorem would require:

- site maps;
- restriction-map commutation;
- obstruction preservation;
- morphism behavior across all relevant IPT classes.

Current T23 IPTs do not contain enough structure to test that honestly.

## Informative Failure Register

| Attempted structure | Failed claim | Interpretation |
| --- | --- | --- |
| scalar D1 | one aggregate explains multiscale finality | scalar aggregation loses observer distribution and gluing data |
| vector D1 | observer vector explains transport | vector loses graph reachability and trust-path distinctions |
| global gluing | local finality always globalizes | contextual obstruction is mathematical, not an implementation failure |
| full IPT representation | all current IPTs factor through D1 local-to-global structure | current IPT type lacks restriction-map data |

## Recommendation

Adopt a finite graph-indexed local-to-global D1 restriction system as the next
formal target.

Do not yet claim:

- full D1 sheaf theory;
- full field-valued D1 as a complete answer;
- full IPT representation theorem.

The repo should next formalize the graph-indexed restriction system directly.
Only after that should it attempt full sheaf semantics or full IPT
representation.

T26 follow-on: [T26](tests/T26-d1-restriction-system.md) implements this
formalization as `D1RestrictionSystem`. The next open step is morphism
composition and IPT representation over that object.

## Artifacts

- [`tests/T25-minimal-d1-generalization.md`](tests/T25-minimal-d1-generalization.md)
- [`models/minimal_d1_generalization.py`](models/minimal_d1_generalization.py)
- [`models/run_t25.py`](models/run_t25.py)
- [`tests/test_minimal_d1_generalization.py`](tests/test_minimal_d1_generalization.py)
- [`results/minimal-d1-generalization-v0.1.json`](results/minimal-d1-generalization-v0.1.json)
- [`results/minimal-d1-generalization-v0.1-results.md`](results/minimal-d1-generalization-v0.1-results.md)
