# T379 Results: Lorentz Pattern From Compatibility Propagation

## Current strongest claim

Given a generated shared compatibility substrate, invariant primitive signal
speed, round-trip rest calibration, and reciprocal signal scaling, the
Lorentz-pattern render maps are derived rather than hand-chosen. The fixture
computes beta, gamma, time dilation, simultaneity disagreement, and interval
preservation from signal-transfer constraints.

This supports the pattern that perceived time differences can arise from how
fast compatibility information can propagate between records. In this fixture,
`c = 1` is the invariant compatibility-signal speed unit.

It is still not a physical derivation of relativity. The primitive light-channel
basis, the `c = 1` convention, and linear reciprocal scaling are premises.

## Result summary

| check | result |
|---|---:|
| source has no Minkowski columns | `true` |
| render maps derived from signal calibration | `true` |
| primitive signal speed invariant | `true` |
| round-trip balance satisfied | `true` |
| Lorentz-pattern coefficients recovered | `true` |
| time dilation recovered | `true` |
| simultaneity disagreement | `true` |
| interval invariant | `true` |
| observer count | `4` |
| generated record pairs checked | `4950` |
| signal speed unit | `1` |
| overall verdict | `lorentz_pattern_recovered_from_signal_constraints_but_channel_premises_absorb` |

## Derived observer maps

| observer | calibration left/right | scale | beta | gamma |
|---|---:|---:|---:|---:|
| `A_rest` | `1 / 1` | `1` | `0` | `1` |
| `B_fast_outbound` | `1 / 4` | `2` | `3/5` | `5/4` |
| `C_fast_return` | `4 / 1` | `1/2` | `-3/5` | `5/4` |
| `D_mild_outbound` | `4 / 9` | `3/2` | `5/13` | `13/12` |

## Hostile comparators

| comparator | absorbs? | status |
|---|---:|---|
| `minkowski_coordinate_import` | `false` | `not_imported_as_source` |
| `hand_chosen_observer_scale` | `false` | `weakened_by_round_trip_derivation` |
| `fixed_light_channel_basis` | `true` | `still_absorbs` |
| `linear_reciprocal_rendering` | `true` | `still_absorbs` |
| `finite_generated_closure` | `true` | `still_absorbs` |
| `causal_order_only` | `false` | `insufficient` |

## Plain-English reading

T379 says:

```text
If records are related by compatibility signals with a shared maximum signal
speed, then different observers can disagree about time while preserving the
same deeper interval relation.
```

The important clarification is:

```text
c is not the time difference itself.
c is the invariant propagation conversion that constrains time differences.
```

In units where `c = 1`, a primitive signal step has:

```text
Delta time = Delta compatibility distance
```

That is why the relativity pattern appears naturally here: perceived time is
being rendered from possible information transfer between records.

## What improved

T377 chose observer render scales directly. T378 removed the explicit rank table.
T379 now derives the observer scales from round-trip compatibility-signal
calibrations. That makes the Lorentz-looking part less arbitrary:

```text
round-trip signal counts -> scale -> beta/gamma -> time dilation and invariant interval
```

## What weakened

The result still depends on a fixed primitive signal basis:

```text
two compatibility channels with invariant c = 1
```

The fixture also assumes reciprocal linear scaling. A hostile reader can say:

```text
you have derived Lorentz-pattern behavior only after granting a light-channel
substrate and linear reciprocal observer calibration
```

That objection is correct. T379 is a pattern match and derivation-under-premises,
not a full derivation from arbitrary compatibility.

## Claim ledger update

Register T379 as a Lorentz-pattern propagation calibration. It supports the idea
that observer time differences can arise from invariant compatibility-signal
transfer constraints, but fixed light-channel and reciprocal-linearity premises
remain live absorbers.

## Next

The next live target is:

```text
derive or stress the primitive compatibility-signal basis
```

More precisely:

```text
test whether c=1 two-channel propagation is forced by compatibility consistency,
or whether it is still an imported lightcone axiom.
```
