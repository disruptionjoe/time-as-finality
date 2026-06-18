# Projection-Obstruction Schema v0.1 Results

## Command

```bash
python -m models.run_t29
```

Focused tests:

```bash
python -m unittest tests.test_projection_obstruction_schema -v
```

## Verdict

T29 turns the T27 stretch result into a finite reusable schema.

Recommended named claim:

```text
PO1: Projection-Obstruction Schema
status = partially_supported
```

## Case Classification

| Case | Outcome | Schema instance |
| --- | --- | --- |
| Witten 1981 | `faithful_projection_obstruction` | yes |
| Nielsen-Ninomiya | `faithful_projection_obstruction` | yes |
| Distler-Garibaldi | `non_definable_projection` | no |
| synthetic lossy projection | `lossy_projection_no_new_obstruction` | no |
| synthetic shared obstruction | `shared_obstruction_not_projection_created` | no |

## Theorem Attempts

| Attempt | Reached |
| --- | --- |
| Positive Projection-Obstruction Schema | yes |
| Non-Definable Projection Boundary | yes |
| Loss Without Obstruction Counterexample | yes |
| Inherited Obstruction Counterexample | yes |

## Interpretation

The positive schema applies only when:

- the projection site map is total;
- the richer system has a global section;
- the restricted system has a gluing obstruction;
- the projection loses the structure that resolved the obstruction.

Distler-Garibaldi is not a failed positive instance. It is a non-definable
projection boundary inside T26.

## Non-Claims

T29 does not claim that Time as Finality proves GU, that GU proves Time as
Finality, or that a finite model replaces any original physics proof.

It claims only a finite abstraction pattern for class-relative no-go structure.
