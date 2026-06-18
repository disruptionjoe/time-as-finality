# D1-Field: Multiscale Observer Finality

## Claim

For claims that cross observers, populations, institutions, communication
networks, scales, or time, D1 should be represented as a field of local D1
profiles rather than as one global profile.

The local value remains the existing D1 profile:

```text
F_O,e(x) = (accessible support, holder redundancy, branch support, reversal cost)
```

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

## Class

Formal extension.

## Status

Partially supported.

## What This Does Not Claim

- It does not replace the existing D1 profile.
- It does not claim finality is continuous over spacetime.
- It does not claim one institution or civilization has a literal mind.
- It does not identify social consensus with physical truth.
- It does not prove a full sheaf or bundle theory of D1.

## Why It Might Be True

Existing tests already pressure D1 away from a single global profile:

- T2 gives different D1 profiles to different observers in one measurement
  chain.
- T21 shows local finality sections can fail to glue globally.
- T23 makes observer access and reduction maps explicit transport objects.

T24 adds direct counterexamples:

- scalar min and max both lose observer-distribution data in a stratified
  access model;
- two scenarios with the same observer-profile vector differ in transport
  because their communication graphs differ;
- local patches can each be satisfiable while the global assignment fails.

## How It Could Fail

- A better aggregate rule may recover all relevant multiscale information.
- Field edges may be unnecessary once observer access boundaries are stated
  more carefully.
- Gluing obstruction may belong only to T13/T21 contextuality, not to D1
  generally.
- The field object may be too flexible to constrain predictions.

## T24 Result

[T24](../tests/T24-d1-multiscale-observer-field.md) compares scalar, vector,
and field interpretations across finite toy models.

The verdict is:

```text
single_global_scalar_sufficient = false
vector_d1_required_for_multiscale_snapshots = true
field_d1_required_for_transport_and_gluing_claims = true
scalar_d1_recoverable_as_special_case = true
replace_existing_d1 = false
```

The recommended interpretation is:

```text
existing D1 profile = local value
D1 field = extension for multiscale and global claims
```

## Tests

- [T24: D1 Multiscale Observer Field](../tests/T24-d1-multiscale-observer-field.md)

## Contribution Needed

Define the field-valued D1 object as a proper graph field, presheaf, or sheaf
with explicit restriction maps. Then test whether T13/T21 obstruction and T23
transport share the same field semantics.
