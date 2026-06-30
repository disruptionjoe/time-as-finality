# T378: Generated Shared-Compatibility Substrate

## Target Claims

R1, S1, D1, PO1, and the T377 shared-substrate relativism question:

```text
Can observer-relative relativistic structure be recovered from one shared
compatibility substrate without storing the observer coordinates or explicit
u/v ranks as source columns?
```

This is not a temporal issuance test. It is the next absorber test after T377:
remove the fixed rank table and ask whether the relativistic rendering survives.

## Setup

Generate a finite substrate by local compatibility closure.

Source rows contain only:

```text
record_id
parents
incoming_compatibility_channels
```

They do not contain:

```text
t
time
timestamp
x
space
metric
interval
u
v
u_rank
v_rank
left_rank
right_rank
coord_time
coord_space
```

Rank-like lineages are reconstructed by counting path steps through two local
compatibility channels. A valid substrate must be path-independent: every path
to the same record must yield the same derived lineage pair.

After reconstruction, multiple observer render maps use different line-scaling
factors:

```text
t_i = (scale_i * left + right / scale_i) / 2
x_i = (scale_i * left - right / scale_i) / 2
```

The derived interval is:

```text
Delta_left * Delta_right
```

## Success Criteria

- Source rows have no time, space, metric, interval, or stored rank columns.
- Rank-like values are derived from local compatibility paths.
- The derivation is path-independent.
- Reversing exported record/edge order leaves derived ranks unchanged.
- Multiple observers recover the same interval-like invariant on all generated
  record pairs.
- At least one simultaneity pair is shared-time for one observer and non-shared
  time for the boosted observers.
- Causal order alone does not determine interval magnitude.

## Failure Criteria

- The fixture stores `u_rank`, `v_rank`, `t`, `x`, or an interval in source rows.
- The result depends on append order or a hidden total foliation.
- The result is promoted as a nonfixed substrate even though the generator rule
  and finite closure are still fixed.

## Known Constraints

This improves T377 by replacing the explicit rank table with a generated local
compatibility substrate. It does not yet defeat all fixedness absorbers. A finite
deterministic generator with fixed bounds can still be expanded into a completed
compatibility table after the fact.

## Contribution Needed

The next version needs a stronger nonfixed object: either a changing
compatibility law, a no-fixed-completion theorem, or an adaptive substrate where
the interval-like structure cannot be precompiled from the generator rule and
finite bounds.
