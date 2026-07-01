# T379: Lorentz Pattern From Compatibility Propagation

## Target Claims

R1, S1, D1, PO1, and the T378 shared-substrate relativism line:

```text
Can the Lorentz-like part of observer relativity be recovered from shared
compatibility propagation constraints, rather than by choosing observer render
coordinates by hand?
```

The target is pattern recovery, not a full derivation of physical special
relativity.

## Setup

Use the T378 generated shared-compatibility substrate. Source rows still contain
only:

```text
record_id
parents
incoming_compatibility_channels
```

The source rows do not contain time, space, metric, interval, or explicit rank
columns.

Add observer calibrations as outbound/return compatibility-signal counts:

```text
A_rest:          left=1, right=1
B_fast_outbound: left=1, right=4
C_fast_return:   left=4, right=1
D_mild_outbound: left=4, right=9
```

The derivation constraints are:

- Primitive compatibility signals define the shared speed unit `c = 1`.
- An observer rest calibration balances outbound and return signal counts.
- Reciprocal scaling preserves the round-trip signal product.
- Therefore:

```text
scale^2 = return_right_ticks / outbound_left_ticks
```

From the derived `scale`, compute:

```text
beta = (scale^2 - 1) / (scale^2 + 1)
gamma = (scale + 1 / scale) / 2
```

Then render derived signal coordinates:

```text
signal_time  = (scale * left + right / scale) / 2
signal_space = (scale * left - right / scale) / 2
```

These are render outputs, not source fields.

## Success Criteria

- No Minkowski `t`, `x`, metric, or interval fields appear in source rows.
- Observer scales are derived from round-trip signal counts.
- Primitive left/right compatibility channels have invariant speed `+1` and
  `-1` for every observer.
- Derived transforms recover Lorentz-pattern coefficients with determinant 1.
- Observer rest calibrations exhibit time dilation matching `gamma`.
- Observers disagree on simultaneity for a shared pair.
- The interval-like product is invariant across all generated record pairs.

## Failure Criteria

- Observer scale is supplied directly rather than derived.
- Source rows store spacetime coordinates or a metric.
- Signal speed is observer-dependent.
- Time dilation or simultaneity disagreement has to be inserted manually.
- The fixture is promoted despite fixed light-channel and linear reciprocal
  scaling premises.

## Known Constraints

This fixture supports the pattern:

```text
shared compatibility substrate
+ invariant signal propagation
+ round-trip observer calibration
= Lorentz-like observer relativity
```

It does not derive the primitive light-channel basis, the `c = 1` convention, or
linearity from deeper data. Those remain live absorbers.

## Contribution Needed

The next version should try to derive, vary, or stress the primitive
compatibility-signal basis itself. The open question is whether the `c = 1`
channel structure is forced by compatibility, or still an imported lightcone
axiom.
