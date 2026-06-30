# T377: Relativistic Record Rendering Fixture

## Target Claims

R1, S1, D1, PO1, and the record-table / rendered-interface bridge imported
from Temporal Issuance.

## Setup

Build a finite 1+1-style record carrier with no primitive time column.

Source rows contain propagation lineage ranks:

```text
u_rank
v_rank
parents
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
proper_time
```

Two observers render source rows using different line-rank scalings:

```text
t_i = (scale_i * u + v / scale_i) / 2
x_i = (scale_i * u - v / scale_i) / 2
```

The carrier interval is:

```text
Delta_u * Delta_v
```

## Success Criteria

- Source rows have no primitive time column.
- Two observers disagree on simultaneity for at least one pair.
- Both observers recover the same interval-like invariant for every record pair.
- Causal order alone does not determine interval magnitude.
- Hidden preferred foliation is not required.

## Failure Criteria

- The invariant is imported by putting `t`, `x`, or metric fields in source rows.
- A hidden total order is required.
- Causal order alone explains the result.
- The fixture is promoted even though fixed-schema or fixed-completed-table
  absorbers still fire.

## Known Physics Constraints

This is a finite toy calibration, not a derivation of special relativity. The
u/v ranks are mathematically lightlike after rendering. A positive result here
only shows that an interval-like invariant can be recovered from a no-time-column
carrier; it does not prove that the carrier is physical.

## Contribution Needed

The next version must beat fixed-schema and fixed-completed-table absorption.
That likely requires nonfixed admissibility, nonfixed carrier schema, or a
no-fixed-completion theorem.
