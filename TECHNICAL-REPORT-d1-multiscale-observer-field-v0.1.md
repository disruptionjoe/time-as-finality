# Technical Report: D1 Multiscale Observer Field v0.1

## Summary

T24 evaluates whether D1 should generalize from one selected observer-indexed
profile into a vector or field over observers, scales, communication
structures, and local-to-global constraints.

The result is not that the current D1 formalism is wrong. The result is that
the current D1 profile is best understood as a local value. For many existing
repo claims, especially T2, T13, T21, T22, and T23, the natural object is a
field of local D1 values over observer sites and transport/gluing structure.

## Terminology

The current D1 profile is already a four-component tuple:

```text
F_O,e(x) = (A, R, B, C)
```

So "scalar" in T24 does not mean a literal real number. It means one selected
or aggregated D1 profile for a record. T24 compares:

| Representation | Definition |
| --- | --- |
| scalar D1 | one selected or aggregated D1 profile for a record |
| vector D1 | a finite map from observer population to D1 profile |
| field D1 | a vector D1 plus observer sites, time/scale labels, communication or trust edges, and gluing constraints |

## Formal Object

The field-valued extension is:

```text
D1Field(x) = (
  observer sites,
  local D1 profiles,
  proposition values,
  transport edges,
  local patches,
  gluing constraints
)
```

Each local value remains:

```text
site -> (accessible support, holder redundancy, branch support, reversal cost)
```

The field adds information that the local profile cannot carry:

- which observer population holds the profile;
- which scale it belongs to;
- when it is evaluated;
- whether transport from one observer to another exists;
- whether transport preserves trust;
- whether local assignments glue globally.

## Toy Models

### 1. Uniform Broadcast

All observer populations share:

```text
(4, 4, 2, 3)
```

over trusted connected transport.

Scalar reduction succeeds. This proves that field-valued D1 is not always
needed.

### 2. Stratified Access Delay

Profiles diverge:

| Observer | D1 profile |
| --- | --- |
| individual | `(1, 1, 1, 1)` |
| family | `(2, 2, 1, 1)` |
| lab | `(4, 3, 2, 2)` |
| scientific community | `(2, 2, 1, 1)` |
| institution | `(0, 0, 0, 0)` |
| civilization | `(0, 0, 0, 0)` |

The componentwise minimum gives:

```text
(0, 0, 0, 0)
```

The componentwise maximum gives:

```text
(4, 3, 2, 2)
```

Both are misleading. The first erases local/lab finality. The second erases
institutional and civilizational non-finality. A vector is required.

### 3. Same Vector, Different Field

Two models have the same observer-profile vector:

```text
individual, family, lab, institution -> (2, 2, 1, 1)
```

In the connected model, a trust-preserving path exists from individual to
institution. In the partitioned model, it does not.

The vector is identical. The transport result differs. Field structure is
therefore required for transport claims.

### 4. Contextual Gluing Obstruction

Four local patches impose:

```text
A0B0 = same
A0B1 = same
A1B0 = same
A1B1 = different
```

Each local patch is satisfiable. No global assignment exists.

This is the D1-field version of the existing T13/T21 warning: local finality
sections need not glue into a global section.

## Reduction Test

Scalar D1 is recoverable under explicit assumptions:

1. **Chosen-observer reduction.** Fix one observer and declare all other
   observer populations out of scope.
2. **Uniform-field reduction.** All observer sites have the same D1 profile
   and trusted transport is connected.
3. **Declared aggregate reduction.** Use min, max, or another aggregate rule
   while explicitly accepting the loss of observer distribution, graph
   transport, and gluing data.

Without one of these assumptions, scalar D1 loses information.

## Relation To Existing Tests

T2 already implies a vector view because observer access changes D1 profiles
inside one measurement model.

T21 already implies a field/gluing view because local finality sections can
exist without a global assignment.

T22 remains a local observable audit: it tells what each D1 dimension reduces
to at one observer boundary.

T23 becomes more natural over the field object because IPT can transport local
D1 values along maps while preserving or losing declared invariants.

## Verdict

T24 recommends:

```text
retain existing D1 local profile
introduce field-valued D1 extension
do not replace D1
do not use one scalar for multiscale claims without assumptions
```

The simplest representation capable of explaining the existing phenomena is:

```text
local D1 profile as stalk value
field-valued D1 for cross-observer structure
```

Vector D1 is useful but incomplete. It captures observer distribution, but not
transport, trust, time/scale adjacency, or gluing obstruction.

## Artifacts

- [`tests/T24-d1-multiscale-observer-field.md`](tests/T24-d1-multiscale-observer-field.md)
- [`models/multiscale_observer_field.py`](models/multiscale_observer_field.py)
- [`models/run_t24.py`](models/run_t24.py)
- [`tests/test_multiscale_observer_field.py`](tests/test_multiscale_observer_field.py)
- [`results/d1-multiscale-observer-field-v0.1.json`](results/d1-multiscale-observer-field-v0.1.json)
- [`results/d1-multiscale-observer-field-v0.1-results.md`](results/d1-multiscale-observer-field-v0.1-results.md)
