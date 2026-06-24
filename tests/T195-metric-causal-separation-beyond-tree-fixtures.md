# T195: Metric-Causal Separation Beyond Tree Fixtures

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. The `T*_DAG` construction
below is a path-summary proxy only. It does not model shared-edge capacity,
flow conservation, or congestion. T202-T204 provide the corresponding
shared-edge and edge-capacity corrections.

## Target Claims

- MTI (`claims/MTI-metabolic-temporal-irreducibility.md`)
- Cap_TI Candidate C (`open-problems/cap-ti-capability-object-spec.md`)
- T186 metric-vs-causal-order split
- T187 finite harmonic-proxy audit
- T194 hostile same-neighbor-data adversarial-family result
- T197 absorber audit against scheduling / queueing / flow theory

## Origin

T186 and T187 established a real metric-causal split on the original finite
fixture family:

```text
same causal order
different delivery-time metric
=> different beta
```

But the current evidence is tree-shaped and exact-family specific. T197 then
narrowed the live burden further:

```text
if the split does survive beyond trees,
does it do so as anything more than a path-summary / harmonic-mean effect?
```

T195 tests exactly that.

## Formal Target Or Obligation

Determine whether the T186/T187 metric-causal separation:

1. extends beyond the current tree-style fixtures to finite non-tree DAG
   families such as reconvergent and layered DAGs; or
2. collapses once the causal graph is no longer tree-like.

The honest target is not "all DAGs." The test is narrower:

```text
Can we exhibit finite non-tree DAG families where identical causal order but
different edge-time metrics still induce different beta values under the same
harmonic-mean Moses proxy?
```

and then:

```text
If yes, does any residue survive beyond the generalized path-time summary T*_DAG?
```

## Generalized Finite-DAG Proxy

T187 used the exact finite proxy:

```text
T* = harmonic_mean(path delivery times)
beta = 1 - log(T*) / log(n)
R(beta,n) = T*
```

T195 uses the same proxy on a broader finite class:

```text
Given a finite DAG D with declared admissible source-to-sink paths P(D),
let T*_DAG(D) = harmonic_mean({tau(p) : p in P(D)}),
where tau(p) is the total delivery time along path p.
Define:
beta_DAG(D) = 1 - log(T*_DAG(D)) / log(n(D)).
```

This is a deliberate finite generalization, not a continuum theorem.

## Setup / Fixtures

### Family A: Same-DAG Weighted Reconvergent Pair (Positive Control)

Use one non-tree reconvergent DAG topology with identical reachability data in
both systems:

```text
s -> a
s -> b
a -> c
b -> c
a -> t
b -> t
c -> t
```

This is non-tree because `c` has two parents.

The admissible source-to-sink paths are:

```text
p1 = s-a-t
p2 = s-b-t
p3 = s-a-c-t
p4 = s-b-c-t
```

#### System Gamma

Assign edge times:

```text
s-a = 3
s-b = 1
a-c = 1
b-c = 1
a-t = 1
b-t = 1
c-t = 1
```

Then path times are:

```text
{4, 2, 5, 3}
```

and

```text
T*_Gamma = 4 / (1/4 + 1/2 + 1/5 + 1/3)
         = 4 / (77/60)
         = 240/77
         ≈ 3.117
```

With `n = 5` events:

```text
beta_Gamma = 1 - log(240/77) / log(5) ≈ 0.293
```

#### System Delta

Keep the identical DAG and identical causal order, but shorten only one edge:

```text
s-a = 2
```

All other edge times unchanged.

Then path times are:

```text
{3, 2, 4, 3}
```

and

```text
T*_Delta = 4 / (1/3 + 1/2 + 1/4 + 1/3)
         = 4 / (17/12)
         = 48/17
         ≈ 2.824
```

With `n = 5`:

```text
beta_Delta = 1 - log(48/17) / log(5) ≈ 0.355
```

Expected positive result:

```text
same DAG
same causal order
different metric
=> beta_Gamma < beta_Delta
```

### Family B: Same-DAG Matched-T*_DAG Higher-Moment Null

Keep the same reconvergent DAG and same event count, but compare two different
path-time multisets with matched reciprocal sum.

Take:

```text
Y1 path times = {4, 2, 5, 3}
```

and

```text
Y2 path times = {4, 2, 6, 30/11}
```

Check:

```text
1/4 + 1/2 + 1/5 + 1/3 = 77/60
1/4 + 1/2 + 1/6 + 11/30 = 77/60
```

So:

```text
T*_DAG(Y1) = T*_DAG(Y2) = 240/77
```

Expected null result:

```text
same T*_DAG
different higher moments / asymmetry
=> same beta_DAG and same R
```

### Family C: Topology-Variation Non-Tree Null

Compare two different non-tree DAG topologies with the same event count.

#### Topology Nu

```text
s -> a -> d -> t
s -> b -> d -> t
s -> c -> t
```

This is non-tree because `d` has two parents.

Choose admissible path times:

```text
{4, 2, 3}
```

Then:

```text
T*_Nu = 3 / (1/4 + 1/2 + 1/3)
      = 3 / (13/12)
      = 36/13
      ≈ 2.769
```

#### Topology Xi

```text
s -> a -> t
s -> b -> e -> t
s -> c -> e -> t
```

This is also non-tree because `e` has two parents.

Choose admissible path times:

```text
{5, 2, 60/23}
```

Check:

```text
1/5 + 1/2 + 23/60 = 12/60 + 30/60 + 23/60 = 65/60 = 13/12
```

So:

```text
T*_Xi = 3 / (13/12) = 36/13 = T*_Nu
```

Expected null result:

```text
different non-tree topology
same n
same T*_DAG
=> same beta_DAG and same R
```

## Positive Control

Family A is the positive control:

```text
same causal order on the same non-tree DAG
different edge-time metric
=> different beta_DAG
```

This ensures the test is not just replaying the tree result rhetorically; it
shows the split on a genuinely reconvergent non-tree family.

## Negative Controls

### Negative Control 1: Same non-tree DAG, same T*_DAG

Family B checks whether higher moments beyond `T*_DAG` matter inside the same
non-tree topology.

### Negative Control 2: Different non-tree topology, same T*_DAG

Family C checks whether topology alone restores a surviving residue once the
generalized path summary is matched.

## Absorber Pass

### Step 1: Rule out disguised causal-graph change on the positive split

Family A keeps:

- the same node set;
- the same reachability relation;
- the same admissible path family;
- the same non-tree topology.

Only the edge-time metric changes.

So if `beta_Gamma != beta_Delta`, the split is metric, not a disguised causal
graph change.

### Step 2: Test whether non-tree generalization restores more than T*

Families B and C test whether either:

- higher moments of the path-time distribution; or
- richer non-tree branching detail

can change the value once `T*_DAG` is matched.

If both remain null, then the non-tree extension survives only as the same
path-summary effect, not as a deeper topology-sensitive theorem.

## Results

### 1. The metric-causal split survives on a genuinely non-tree family

For Family A:

```text
T*_Gamma = 240/77 ≈ 3.117
T*_Delta = 48/17 ≈ 2.824
beta_Gamma ≈ 0.293
beta_Delta ≈ 0.355
```

Therefore:

```text
beta_Gamma < beta_Delta
```

even though the causal order and non-tree DAG topology are identical.

So the T186/T187 style separation is not tree-only in the narrowest sense.
It survives at least to finite weighted reconvergent DAGs under the same
harmonic-mean finite proxy.

### 2. Same-summary nulls still collapse in the non-tree setting

For Family B:

```text
T*_DAG(Y1) = T*_DAG(Y2) = 240/77
=> beta_DAG(Y1) = beta_DAG(Y2)
=> R(Y1) = R(Y2)
```

For Family C:

```text
T*_Nu = T*_Xi = 36/13
=> beta_DAG(Nu) = beta_DAG(Xi)
=> R(Nu) = R(Xi)
```

So neither higher moments nor non-tree topology restore a residue once the
generalized harmonic-mean summary is matched.

### 3. What survives

The surviving statement is narrower than "arbitrary DAG theorem":

```text
Within the tested finite weighted non-tree DAG families,
metric-causal separation survives,
but only through the generalized path-time summary T*_DAG.
```

This does extend the old tree-shaped result, but it does not reopen an
independent Cap_TI capability claim beyond the generalized harmonic-mean proxy.

## Verdict: narrowed

T195 returns `narrowed`.

What is supported:

```text
the metric-causal split survives beyond tree fixtures to at least finite
weighted reconvergent and layered non-tree DAG families under the same
harmonic-mean Moses proxy.
```

What is not supported:

```text
that the split becomes a topology-sensitive theorem beyond the generalized
path summary,
or that arbitrary DAG structure beyond T*_DAG currently carries additional
predictive content.
```

## Falsification Conditions

This verdict should be revisited if:

1. a finite non-tree family is found where same causal order and different
   edge weights do NOT change `beta_DAG`;
2. a matched-`T*_DAG` family is found where higher moments or topology alone
   still change the value;
3. a more faithful finite Moses generalization to DAGs replaces the current
   harmonic-mean proxy and changes these conclusions.

## Next Step

T195 sharpens the Wave 3 burden:

```text
T196 should ask whether any continuum/WBE bridge earns more than this finite
weighted-DAG harmonic-mean proxy;
T199 should present the reviewer-facing packet as a narrowed metric-causal
separation result, not as a broad non-tree theorem.
```
