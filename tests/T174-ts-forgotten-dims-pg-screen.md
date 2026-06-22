# T174: Forgotten-Dims Persistence-Gap Screen

## Route

Typed transport / holarchy time-series boundary.

## Target Claims

- [HYPOTHESES: Known Boundary - TypedTransportNetwork Recovery Propagation](../HYPOTHESES.md)
- [T40: Holarchy Lab](T40-holarchy-lab.md)
- [TS-PERSONA-SPRINT-001 synthesis](../explorations/TS-PERSONA-SPRINT-001-synthesis-v0.1.md)

## Question

Does non-empty cross-level `forgotten_dims` generate a holonic persistence gap
after all lower-level obstructions have recovered, without an explicit holonic
persistence window?

T174 distinguishes:

```text
PG relative to micro
  = holonic last obstruction - micro last obstruction

residual PG after lower-level recovery
  = holonic last obstruction - max(micro last obstruction, meso last obstruction)
```

The second quantity is the load-bearing one for MINI-GOAL-TS-002.

## Setup

The finite trajectory keeps the TS sprint timing:

```text
micro obstruction:   t=10..24
meso obstruction:    t=15..29
baseline holonic:    t=10..34
```

Four fixtures are audited:

1. `scheduled_persistence_baseline`
   The original-style scheduled holonic persistence control.
2. `no_explicit_persistence_with_forgotten_dims`
   Holonic obstruction is only the current propagated lower-level obstruction,
   while `forgotten_dims` is non-empty.
3. `no_forgotten_dims_control`
   Same propagated-current-lower rule, but no `forgotten_dims`.
4. `explicit_recovery_retention_positive_control`
   A positive control showing that the metric detects residual PG when an
   explicit retention rule exists.

## Success Criteria

- The scheduled baseline has residual PG after lower-level recovery.
- The no-explicit-persistence fixture has non-empty `forgotten_dims` but zero
  residual PG after lower-level recovery.
- The no-forgotten-dims control also has zero residual PG.
- The explicit retention control has residual PG and is classified as an
  explicit-retention result, not a `forgotten_dims` result.

## Failure Criteria

- PG relative to micro is treated as evidence of holonic persistence without
  subtracting meso inheritance.
- Non-empty `forgotten_dims` is treated as a dynamic recovery-memory operation.
- Explicit retention is mistaken for an emergent topology result.

## Claim Impact

No claim status changes.

T174 is a boundary screen. In this finite fixture, `forgotten_dims` is
attribution metadata for cross-level loss, not an automatic dynamic memory
that keeps the holonic level obstructed after lower-level recovery.

## Reproduction

```bash
python -m unittest tests.test_ts_forgotten_dims_pg_screen -v
python -m models.run_t174
```
