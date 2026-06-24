# T203: Edge-Capacity / Flow-Conservation DAG Model

## Target Claims

- T195 metric-causal separation beyond tree fixtures
- T199 reviewer-facing metric-causal packet
- Cap_TI / MTI finite timing proxy after T187/T202 narrowing

## Origin

T195 treated source-to-sink path times as independent entries. T202 showed that
this can double-count shared edges and ignore capacity, demand, and flow
conservation.

## Formal Target

Replace the independent-path proxy with a finite capacitated DAG model. Let
`D=(V,E)` have source `s`, sink `t`, edge time `tau_e > 0`, capacity `c_e > 0`,
and demand `q`. A path-flow `x_p >= 0` satisfies:

```text
sum_p x_p = q
f_e = sum_{p contains e} x_p
0 <= f_e < c_e
```

With congestion law:

```text
d_e(f_e) = tau_e * phi(f_e / c_e)
phi(u) = 1 / (1-u)
```

define:

```text
C_flow(D,q) = inf_x max_{p:x_p>0} sum_{e in p} d_e(f_e)
```

The old path-harmonic proxy is valid only as a declared approximation or a
special no-shared-capacity limit.

## Setup / Fixtures

Use two fixture classes:

```text
edge-disjoint paths, where path proxy and flow model should agree in ranking;
shared-edge DAGs, where corrected flow must count bottlenecks.
```

## Positive Control

For edge-disjoint, high-capacity paths, changing free path times changes both
the harmonic proxy and `C_flow` in the same direction.

## Negative Control

Relabeling nodes or paths while preserving incidence, `tau`, `c`, and `q` must
leave `C_flow` unchanged.

## Absorber Pass

Network flow, queueing, and performance theory are granted their native
variables: incidence, capacities, demand, delay functions, and feasible
allocations. Under that state completion, independent path harmonic is
underdescribed for overlapping DAGs.

## Results

The corrected finite object is `C_flow`, not unweighted harmonic mean over
listed paths. T195 remains useful only as proxy-level exploration.

## Verdict: narrowed

Arbitrary finite DAG claims must use edge-capacity and flow-conservation data;
the independent-path harmonic proxy is demoted to a special approximation.

## Falsification Conditions

Revisit if a theorem shows the unweighted path harmonic is invariant under
shared-edge flow conservation, or if a different canonical finite DAG
capability is justified.

## Next Step

T204 builds a hostile same-harmonic but different-congestion family.
