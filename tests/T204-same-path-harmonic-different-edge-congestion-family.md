# T204: Same Path Harmonic, Different Edge Congestion Family

## Target Claims

- T203 corrected capacitated DAG model
- T195 independent-path proxy weakness
- T199 reviewer-facing metric-causal packet

## Origin

If path harmonic alone were sufficient, two DAGs with the same free
source-to-sink path-time multiset would agree. T203 predicts this can fail when
shared edges create different congestion.

## Formal Target

Construct two finite DAGs with identical free path-time multiset and identical
unweighted harmonic mean, but different `C_flow(D,q)`.

## Setup / Fixtures

Use:

```text
q = 1
phi(u) = 1/(1-u)
C_flow = min max loaded path latency
```

### System D: Disjoint

```text
p1 = s-a-t
p2 = s-b-t
each edge tau = 1, c = 2
free path times = {2,2}
harmonic mean = 2
```

By symmetry, split flow `(1/2, 1/2)`. Each used edge has load `1/2`,
utilization `1/4`, delay `4/3`, and loaded path latency:

```text
C_flow(D,1) = 8/3
```

### System S: Shared Prefix

```text
p1 = s-u-a-t
p2 = s-u-b-t
s-u has tau = 1, c = 2
each branch edge has tau = 1/2, c = 2
free path times = {2,2}
harmonic mean = 2
```

By symmetry, split flow `(1/2, 1/2)`. The shared edge has load `1`,
utilization `1/2`, delay `2`; each branch edge has delay `2/3`. Loaded path
latency is:

```text
C_flow(S,1) = 10/3
```

## Positive Control

The systems have the same free path harmonic but:

```text
C_flow(D,1) = 8/3
C_flow(S,1) = 10/3
```

## Negative Control

Relabeling either system without changing incidence, capacities, times, or
demand leaves `C_flow` unchanged.

## Absorber Pass

The split is standard edge-congestion state completion. The value survives
only because the path-harmonic projection omitted legitimate flow variables.

## Results

Same path harmonic does not determine corrected finite DAG capability.

## Verdict: promoted

Promoted as a reusable counterexample to independent-path sufficiency in
overlapping DAGs.

## Falsification Conditions

Revisit if the optimal flow calculation is wrong, if the congestion law is
rejected without replacement, or if a canonical path-weighted harmonic exactly
recovers `C_flow`.

## Next Step

T205 audits refinement/continuum stability of the unweighted path proxy.
