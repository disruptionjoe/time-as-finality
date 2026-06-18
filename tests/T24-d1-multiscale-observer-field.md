# T24: D1 Multiscale Observer Field

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D1-Field: Multiscale Observer Finality](../claims/D1-field-multiscale-observer-finality.md)
- [IPT: Invariant-Preserving Transformations](../claims/IPT-invariant-preserving-transformations.md)
- [T13: Finality Sheaf Cohomology](T13-finality-sheaf-cohomology.md)
- [T21: Bell Contextuality Finality](T21-bell-contextuality-finality.md)
- [T23: Invariant-Preserving Transformations](T23-invariant-preserving-transformations.md)

## Setup

T24 tests three representations:

| Representation | Meaning in T24 |
| --- | --- |
| scalar D1 | one selected or aggregated D1 profile for a record |
| vector D1 | a finite observer-indexed vector of D1 profiles |
| field-valued D1 | a vector of local D1 profiles plus observer sites, communication/trust edges, time/scale labels, and gluing constraints |

The current D1 profile remains the local value:

```text
F_O,e(x) = (accessible support, holder redundancy, branch support, reversal cost)
```

T24 asks whether cross-observer and multiscale claims need a richer container
for these local values.

## Toy Models

T24 implements five finite models:

| Model | Purpose | Result |
| --- | --- | --- |
| uniform_broadcast | all observer populations share the same profile over trusted transport | scalar reduction succeeds without material loss |
| stratified_access_delay | individual, family, lab, community, institution, and civilization have different profiles | vector D1 is required |
| connected_same_vector | all observers have the same vector and trusted transport connects source to target | scalar/vector sufficient for this case |
| partitioned_same_vector | same observer vector as connected case, but transport graph is partitioned | field data is required |
| contextual_gluing_obstruction | local finality patches are each satisfiable, but no global assignment exists | sheaf/contextuality-style obstruction |

## Success Criteria

- At least three toy models compare scalar, vector, and field interpretations.
- Scalar reduction is recovered under explicit assumptions.
- At least one model shows scalar D1 losing observer-distribution data.
- At least one model shows vector D1 losing field/transport data.
- At least one model gives a local-to-global obstruction.
- The recommendation says whether D1 should be retained, vectorized, fielded,
  or deferred.

## Failure Criteria

- The richer representations add no information beyond scalar D1.
- Every vector or field example can be reduced to scalar D1 without declared
  loss.
- Field structure is introduced but never changes transport or gluing results.
- The result replaces the existing D1 profile without proving that replacement
  is necessary.

## Result

Implemented as T24 v0.1.

Verdict:

```text
single_global_scalar_sufficient = false
vector_d1_required_for_multiscale_snapshots = true
field_d1_required_for_transport_and_gluing_claims = true
scalar_d1_recoverable_as_special_case = true
replace_existing_d1 = false
recommendation_class = introduce_field_extension
```

Recommendation: retain the existing observer-indexed D1 profile as the local
value. Introduce a field-valued D1 extension for claims about observer
populations, communication transport, scale, time, and local-to-global gluing.

## Reproduction

```bash
python -m unittest tests.test_multiscale_observer_field -v
python -m models.run_t24
```

Artifacts:

- [`models/multiscale_observer_field.py`](../models/multiscale_observer_field.py)
- [`models/run_t24.py`](../models/run_t24.py)
- [`tests/test_multiscale_observer_field.py`](test_multiscale_observer_field.py)
- [`results/d1-multiscale-observer-field-v0.1.json`](../results/d1-multiscale-observer-field-v0.1.json)
- [`results/d1-multiscale-observer-field-v0.1-results.md`](../results/d1-multiscale-observer-field-v0.1-results.md)

## Contribution Needed

Turn field-valued D1 from a finite audit object into a formal sheaf or graph
field with explicit restriction maps. Then test whether T13/T21 obstructions
and T23 invariant transport can be expressed over the same D1 field object.
