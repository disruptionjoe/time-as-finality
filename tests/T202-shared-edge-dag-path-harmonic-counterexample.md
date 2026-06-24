# T202: Shared-Edge DAG Path-Harmonic Counterexample

## Target Claims

- T195 metric-causal separation beyond tree fixtures
- T199 reviewer-facing metric-causal packet
- T187/T201 harmonic-proxy status

## Origin

T195 extends the harmonic proxy to non-tree DAGs by harmonically averaging
source-to-sink path times. That treats path entries as independent even when
paths share edges.

## Formal Target

Compare the path-harmonic summary with shared-edge accounting on a DAG where
many paths reuse the same bottleneck edge.

## Setup / Fixtures

Use:

```text
s -> a
a -> b1 -> t
a -> b2 -> t
a -> b3 -> t
```

with:

```text
s-a = L
a-bi = 1
bi-t = 1
```

All three source-to-sink paths share `s-a`.

## Positive Control

If `L = 1`, all path times are `3`, so:

```text
T*_path = 3
```

The proxy is harmless as a simple symmetric path-time summary.

## Negative Control

If `L = 100`, all path times are `102`, and the reciprocal sum counts three
path entries even though every unit must traverse the same bottleneck edge
`s-a`. Adding more downstream branches would increase path multiplicity without
adding upstream capacity.

## Absorber Pass

Network-flow theory absorbs the issue. DAG transport with shared edges must
account for edge capacities, congestion, conservation, and shared bottlenecks.
Unweighted harmonic summaries over simple paths are not invariant under path
expansion.

## Results

T195's `T*_DAG` is acceptable only as a declared path-summary statistic. It is
not a faithful DAG flow model unless paired with edge-capacity semantics.

## Verdict: narrowed

T195 remains useful as a proxy audit, but not as a general DAG transport theorem.

## Falsification Conditions

Revise if a path-decomposition theorem proves that the harmonic path summary
equals a legitimate edge-flow objective under stated capacities and
conservation laws.

## Next Step

T203 replaces the independent-path proxy with an explicit capacitated DAG flow
model.
