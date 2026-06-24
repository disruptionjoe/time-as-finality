# T200: T187 Linear-Program / KKT Audit

## Target Claims

- T187 finite harmonic-proxy audit
- MTI / Cap_TI metric-causal separation provenance

## Origin

T187 originally claimed that minimizing `sum_i w_i t_i` under `sum_i w_i = 1`
and `w_i >= d` gives inverse-time weights. T200 checks that claim directly.

## Formal Target

Solve:

```text
minimize sum_i w_i t_i
subject to sum_i w_i = 1
           w_i >= d
           0 <= d <= 1/k
```

for positive path times `t_i`.

## Setup / Fixtures

Use the Alpha path times:

```text
t = (4, 2, 1)
k = 3
```

## Positive Control

For `d = 0`, the LP optimum puts all mass on a shortest path:

```text
w* = (0, 0, 1)
objective = 1
```

For `d = 0.1`, the lower-bound optimum is:

```text
w* = (0.1, 0.1, 0.8)
objective = 1.4
```

## Negative Control

Inverse-time weights are:

```text
w_H = (1/7, 2/7, 4/7)
objective = 12/7 = 1.714...
```

This point is feasible for `d <= 1/7`, but it is not optimal for `d = 0` or
`d = 0.1`.

## Absorber Pass

Standard LP/KKT theory absorbs the claimed result. A linear objective over a
simplex with lower bounds optimizes at an extreme point unless active path
times tie. A diversity floor changes which constraints bind; it does not create
interior reciprocal weights.

## Results

The T187 KKT step is invalid as stated. The harmonic-mean quantity may remain a
declared proxy, but it is not the solution of the stated LP.

## Verdict: killed

Killed as an exact derivation from the stated linear program.

## Falsification Conditions

Revise only if a different objective, convex constraint, fairness condition, or
physical flow law is supplied and its KKT equations actually imply
`w_i proportional to 1/t_i`.

## Next Step

T201 tests whether a nearby regularized or equal-load objective can earn the
harmonic proxy honestly.
