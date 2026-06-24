# T210: C_flow Solver Base Cases

## Target Claims

- T203 edge-capacity / flow-conservation DAG model
- T204 same-harmonic congestion counterfixture
- T209 executable guardrail standard

## Origin

T203 introduced `C_flow(D,q)` as the corrected finite DAG capability, but left
it as a paper definition. T210 makes the object executable on small fixtures.

## Formal Target

Implement:

```text
d_e(f_e) = tau_e / (1 - f_e / c_e)
C_flow(D,q) = min_x max_{p:x_p>0} sum_{e in p} d_e(f_e)
```

for small finite path networks.

## Setup / Fixtures

Executable surface:

```text
models/mti_cflow_solver.py
tests/test_mti_cflow_solver.py
```

The solver enumerates small path-flow allocations over the demand simplex and
computes max loaded path latency.

## Positive Control

Two symmetric disjoint paths with edge `tau=1`, `capacity=2`, and demand `1`
split flow evenly:

```text
flows = (1/2, 1/2)
C_flow = 8/3
```

## Negative Control

The same free path times on a shared-prefix network produce a different
capacity-aware value:

```text
C_flow = 10/3
```

so free path harmonic is not silently reused.

## Absorber Pass

This is standard finite network-flow / congestion accounting. Its value is not
new physics; it is an executable state-completion guardrail for MTI/Cap_TI.

## Results

The base solver reproduces the hand-computed values from T204 and exposes
`free_path_times`, `edge_loads`, `path_latency`, and `solve_minimax_cflow`.

## Verdict: promoted

Promoted as the executable finite `C_flow` base object for this line.

## Falsification Conditions

Demote if the solver fails exact small controls, miscomputes shared-edge loads,
or treats path harmonic as a flow optimum.

## Next Step

T211 uses the solver to rerun T204 as an executable counterexample.
