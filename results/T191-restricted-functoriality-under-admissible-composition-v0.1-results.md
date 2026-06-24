# T191 Results: Restricted Functoriality Under Admissible Composition

## Outcome

There is a genuine covariant `FinSets` repair, but it is too weak to carry the
MTI / PO1-NCK program.

The largest clean finite repair is the section-preserving subcategory:

```text
SectPres(Ext_S)
```

where each extension preserves every coherent section, equivalently
`F(S') = F(S)`.

## What Was Verified

| Property | Verdict |
| --- | --- |
| Identity closure | verified |
| Composition closure | verified |
| Covariant `FinSets` action on `SectPres(Ext_S)` | verified |
| Usefulness for NCK dynamics | fails |

## Why It Fails Strategically

Inside `SectPres(Ext_S)`:

```text
|F(S')| = |F(S)|
```

for every allowed arrow. So:

```text
N = 0
K = 0
```

for section-count dynamics along those arrows. The repair is mathematically
clean but dynamically sterile.

## Surviving Repair Options

The live choices are now:

1. `F_op : States(Ext_S)^op -> FinSets`
2. `F_partial : States(Ext_S) ->` partial-map / relation-valued semantics

The covariant `FinSets` subcategory is best treated as a boundary result, not
the main formal object.

## What This Changes

- `FUNCTOR-OBL-TaF-001` is narrowed further: the covariant `FinSets` version
  survives only in a section-preserving corner.
- `T192` must choose a repaired semantic direction before deriving
  `lambda*(S)`.
- The repo should stop speaking as if the original covariant coherent-section
  functor is one repair away from full verification; the main choice is now
  between contravariance and partial-map covariance.
