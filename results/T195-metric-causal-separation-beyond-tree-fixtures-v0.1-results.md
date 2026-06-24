# T195 Results: Metric-Causal Separation Beyond Tree Fixtures

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. `T*_DAG` is a path-summary
proxy only. Shared-edge capacity and flow-conservation effects are not modeled
by this result; see T202-T204.

## Outcome

`narrowed`

The metric-causal separation from T186/T187 is not tree-only in the narrowest
sense. It survives on the tested finite weighted non-tree DAG families.

But the extension is still summary-level:

```text
the split survives when T*_DAG changes;
it collapses when T*_DAG is matched.
```

So T195 broadens the fixture class while still narrowing the theorem shape.

## Main Readout

| Family | What is fixed? | What changes? | Result |
| --- | --- | --- | --- |
| A: same non-tree DAG positive control | causal order, topology, admissible path family | edge-time metric | split survives |
| B: same non-tree DAG matched-`T*_DAG` null | topology, `n`, `T*_DAG` | higher moments / asymmetry | collapses |
| C: different non-tree topology matched-`T*_DAG` null | `n`, `T*_DAG` | non-tree topology | collapses |

## Positive Control

For the reconvergent non-tree DAG pair:

- `T*_Gamma = 240/77 ≈ 3.117`
- `T*_Delta = 48/17 ≈ 2.824`
- `beta_Gamma ≈ 0.293`
- `beta_Delta ≈ 0.355`

The causal order and topology are identical. Only the edge-time metric changes.

So the metric-causal split survives on a genuinely non-tree family.

## Null Controls

Two null classes still collapse:

1. Same non-tree DAG with matched `T*_DAG` but different higher moments.
2. Different non-tree DAG topologies with matched `T*_DAG`.

Under the generalized finite proxy, both produce the same `beta_DAG` and the
same `R`.

## Repo-Safe Reading

T195 supports a narrower but stronger statement than the original tree-only
reading:

```text
Finite weighted non-tree DAGs can still exhibit metric-causal separation,
but the currently earned predictive object is still just the generalized
harmonic-mean path-time summary T*_DAG.
```

What T195 does **not** support is:

```text
an arbitrary-DAG theorem,
a topology-sensitive capability beyond T*_DAG,
or a reopened independent Cap_TI residue.
```

## Why This Matters

T197 had already absorbed Candidate C inside the exact tree-style family.
T195 shows that moving to non-tree finite DAGs does not reopen that absorbed
capability claim by itself.

What it does do is prevent an overcorrection:

```text
the metric-causal split is not merely a tree artifact;
it extends at least one step outward to finite weighted reconvergent DAGs.
```

## Best Next Burdens

This result leaves two honest Wave 3 questions:

1. Does T196 find any continuum / WBE bridge quantity that is richer than the
   finite `T*_DAG` proxy?
2. Can T199 present the external packet as a narrowed metric-causal separation
   result without overselling it as a broad graph-theoretic theorem?
