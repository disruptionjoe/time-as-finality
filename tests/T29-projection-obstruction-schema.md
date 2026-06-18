# T29: Projection-Obstruction Schema

## Target Claims

- [PO1: Projection-Obstruction Schema](../claims/PO1-projection-obstruction-schema.md)
- [T26: D1 Restriction System](T26-d1-restriction-system.md)
- [T27: Class-Relative Bridge Audit](T27-class-relative-bridge-audit.md)

## Question

When does projection from a richer restriction system to a restricted class
create a gluing obstruction, and when is the projection not even definable?

## Setup

T29 works only at the finite abstraction level. It takes pairs of
`D1RestrictionSystem` objects plus a `D1RestrictionMorphism` and classifies the
projection outcome.

## Outcomes

```text
faithful_projection_obstruction
lossy_projection_no_new_obstruction
shared_obstruction_not_projection_created
non_definable_projection
```

## Required Cases

| Case | Required result |
| --- | --- |
| Witten 1981 | positive schema instance |
| Nielsen-Ninomiya | positive schema instance |
| Distler-Garibaldi | non-definable projection boundary |
| synthetic lossy case | projection exists but no obstruction appears |
| synthetic shared-obstruction case | obstruction exists in both systems |

## Success Criteria

- Define the finite `ProjectionObstructionSchema` object.
- Re-express Witten and Nielsen-Ninomiya as positive instances.
- Re-express Distler-Garibaldi as a non-definable boundary.
- Add a synthetic counterexample where projection exists but no obstruction
  appears.
- Add a synthetic case where obstruction exists in both rich and restricted
  systems.
- State what T27 did and did not prove.
- Decide whether Projection-Obstruction becomes a named repo claim.

## Result

Implemented as T29 v0.1.

T29 recommends promoting the schema to:

```text
PO1: Projection-Obstruction Schema
status = partially_supported
```

## Reproduction

```bash
python -m unittest tests.test_projection_obstruction_schema -v
python -m models.run_t29
```

Artifacts:

- [`models/projection_obstruction_schema.py`](../models/projection_obstruction_schema.py)
- [`models/run_t29.py`](../models/run_t29.py)
- [`tests/test_projection_obstruction_schema.py`](test_projection_obstruction_schema.py)
- [`results/projection-obstruction-schema-v0.1.json`](../results/projection-obstruction-schema-v0.1.json)
- [`results/projection-obstruction-schema-v0.1-results.md`](../results/projection-obstruction-schema-v0.1-results.md)

## Contribution Needed

Test PO1 on one domain not inherited from GU or Time as Finality. The next
stronger result would show whether the schema is domain-neutral or merely a
useful abstraction of the current bridge audit.
