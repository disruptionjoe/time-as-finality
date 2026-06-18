# D1 Multiscale Observer Field v0.1 Results

## Command

```bash
python -m models.run_t24
```

Focused tests:

```bash
python -m unittest tests.test_multiscale_observer_field -v
```

## Verdict

T24 rejects a single global scalar D1 for multiscale claims, but it does not
replace the existing D1 profile.

The existing observer-indexed D1 profile should be retained as the local value.
For cross-observer, institutional, civilizational, communication, or
local-to-global claims, D1 should be treated as a field-valued extension:

```text
observer/scale/time site -> D1 profile
```

plus transport edges and gluing constraints.

| Criterion | Result |
| --- | --- |
| Single global scalar sufficient | false |
| Vector D1 required for multiscale snapshots | true |
| Field D1 required for transport and gluing claims | true |
| Scalar D1 recoverable as special case | true |
| Replace existing D1 | false |
| Recommendation class | introduce_field_extension |

## Toy Model Results

| Model | Representation needed | Finding |
| --- | --- | --- |
| uniform_broadcast | scalar | all observer populations share `(4, 4, 2, 3)` over trusted transport |
| stratified_access_delay | field | scalar min gives `(0, 0, 0, 0)`, scalar max gives `(4, 3, 2, 2)`, both lose observer distribution |
| connected_same_vector | scalar | same vector with trusted connected transport reaches the target |
| partitioned_same_vector | field | same vector fails to transport because the graph is partitioned |
| contextual_gluing_obstruction | field | all local patches are satisfiable but no global assignment exists |

## Counterexamples

Scalar insufficiency:

```text
stratified_access_delay
```

The individual, family, lab, scientific community, institution, and
civilization have different profiles. A componentwise minimum erases live lab
finality; a componentwise maximum erases institutional non-finality.

Vector insufficiency:

```text
connected_same_vector
partitioned_same_vector
```

Both have the same observer-profile vector. Only the field graph distinguishes
whether finality can transport from individual to institution.

Local-to-global obstruction:

```text
contextual_gluing_obstruction
```

Each local patch is satisfiable, but the full set of constraints has no global
assignment. This is the multiscale D1 analogue of the existing
sheaf/contextuality warning: local finality need not imply global finality.

## Scalar Recovery

Scalar D1 is recovered without material loss when:

- the observer is fixed explicitly and all other observer claims are out of
  scope; or
- all observer sites share the same D1 profile and trusted transport is
  connected; or
- an aggregate rule is declared and the lost information is explicitly
  accepted.

## Recommendation

Adopt field-valued D1 as an extension, not a replacement.

The repo should treat the existing D1 profile as the local stalk value and use
the field object only when a claim crosses observers, populations, scales,
communication networks, time steps, institutions, or gluing boundaries.
