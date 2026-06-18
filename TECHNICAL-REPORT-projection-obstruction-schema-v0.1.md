# Technical Report: Projection-Obstruction Schema v0.1

## Summary

T29 promotes the T27 stretch result from case-study pattern to a reusable
finite schema over `D1RestrictionSystem` projections.

The core question is:

```text
When does projection from a richer restriction system to a restricted class
create a gluing obstruction, and when is the projection not even definable?
```

The result is a narrow positive formalization:

```text
Projection-Obstruction is a finite class-relative schema, not a theorem about
the original physics.
```

T29 supports promoting the schema to a named formal claim:

```text
PO1: Projection-Obstruction Schema
status = partially_supported
```

## Formal Object

T29 defines:

```text
ProjectionObstructionSchema = (
  projection_definable,
  richer_obstructed,
  restricted_obstructed,
  obstruction_created_by_projection,
  projection_loses_structure,
  morphism_reaches_target,
  outcome,
  schema_instance,
  boundary
)
```

It is computed from:

```text
ProjectionCase = (
  richer D1RestrictionSystem,
  restricted D1RestrictionSystem,
  D1RestrictionMorphism,
  forgotten structure,
  preserved structure
)
```

## Outcomes

| Outcome | Meaning |
| --- | --- |
| `faithful_projection_obstruction` | projection is definable, richer system is globally satisfiable, restricted system is obstructed |
| `lossy_projection_no_new_obstruction` | projection exists and forgets structure, but no obstruction appears |
| `shared_obstruction_not_projection_created` | both rich and restricted systems are obstructed, so projection did not create the obstruction |
| `non_definable_projection` | site map is incomplete or the bridge requires a category change |

## Positive Schema

The positive finite schema is:

```text
If:
  richer system has a global section
  restricted system has no global section
  projection site map is total
  projection forgets obstruction-resolving structure
Then:
  the restricted no-go is represented as a projection-created gluing obstruction.
```

This is a statement about finite abstraction, not a replacement for source
proofs.

## Re-Expressed T27 Cases

| Case | T29 outcome | Schema instance |
| --- | --- | --- |
| Witten 1981 | `faithful_projection_obstruction` | yes |
| Nielsen-Ninomiya | `faithful_projection_obstruction` | yes |
| Distler-Garibaldi | `non_definable_projection` | no |

Witten and Nielsen-Ninomiya instantiate the positive schema inherited from T27.
Distler-Garibaldi remains the important boundary: the projection is not
definable inside T26 because the site map is incomplete.

## Synthetic Boundary Tests

T29 adds two synthetic cases so the schema is not just fitted to T27.

### Loss Without Obstruction

```text
synthetic_lossy_no_obstruction
```

Projection exists and forgets support, holder, and branch data. Both the richer
and restricted systems still have global sections.

Verdict:

```text
loss alone is insufficient
```

### Inherited Obstruction

```text
synthetic_shared_obstruction
```

Both richer and restricted systems are already obstructed.

Verdict:

```text
the obstruction is inherited, not projection-created
```

## What T27 Proved

T27 proved, at the finite abstraction level:

- Witten 1981 and Nielsen-Ninomiya admit faithful finite
  `D1RestrictionSystem` bridge models.
- Distler-Garibaldi does not admit the same bridge because the projection site
  map is incomplete.
- The faithful cases share a common projection-created obstruction pattern.

## What T27 Did Not Prove

T27 did not prove:

- any original physics no-go theorem;
- that Time as Finality proves GU;
- that GU proves Time as Finality;
- that finite models replace source mathematical proofs;
- that the pattern applies to category-change cases like Distler-Garibaldi.

## T29 Theorem Ladder

| Theorem attempt | Reached | Boundary |
| --- | --- | --- |
| Positive Projection-Obstruction Schema | yes | finite abstraction only |
| Non-Definable Projection Boundary | yes | may require category-level morphisms |
| Loss Without Obstruction Counterexample | yes | loss alone is insufficient |
| Inherited Obstruction Counterexample | yes | obstruction must be projection-created |

## Recommendation

Promote Projection-Obstruction to a named formal schema claim, `PO1`, with
`partially_supported` status.

Use it only for finite class-relative abstraction:

```text
projection-created obstruction = positive schema instance
site-map incomplete = non-definable boundary
loss without obstruction = counterexample
shared obstruction = inherited obstruction, not projection-created
```

Do not use PO1 as a claim about the correctness of any underlying physical
theory.

## Artifacts

| Artifact | Path |
| --- | --- |
| Model | `models/projection_obstruction_schema.py` |
| Runner | `models/run_t29.py` |
| Tests | `tests/test_projection_obstruction_schema.py` |
| Test spec | `tests/T29-projection-obstruction-schema.md` |
| JSON results | `results/projection-obstruction-schema-v0.1.json` |
| Results summary | `results/projection-obstruction-schema-v0.1-results.md` |
| Named claim | `claims/PO1-projection-obstruction-schema.md` |
