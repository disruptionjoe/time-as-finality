# T199: Reviewer-Facing Metric-Causal Separation Packet

## Correction Notice

Superseded/narrowed by T208. The packet below remains useful only as a
finite-harmonic-proxy packet. It must not be read as an exact Moses
optimization, arbitrary-DAG flow theorem, or continuum WBE bridge. T200-T209
are the required errata/follow-up tranche before external export.

## Target Claims

- MTI (`claims/MTI-metabolic-temporal-irreducibility.md`)
- T186 metric-vs-causal-order split
- T187 finite harmonic-proxy audit
- T195 metric-causal separation beyond tree fixtures
- T197 absorber audit against scheduling / queueing / flow theory
- T196 exact WBE-continuum bridge audit

## Purpose

Produce the cleanest exportable packet for the strongest surviving content of
the MTI / Cap_TI line.

The packet must:

- state the finite claim precisely;
- distinguish theorem-level content from interpretation;
- preserve the hostile narrowing from T195 / T197 / T196;
- avoid visionary or continuum inflation.

## Positive Control

The packet must preserve the strongest finite positive content:

- T186/T187 tree-style finite split;
- T195 non-tree finite extension.

If the packet cannot state those clearly, it is too weak.

## Negative Control

The packet must not smuggle in claims that the fanout did not earn.

The main export-null controls are:

- no independent Cap_TI theorem beyond the timing summary;
- no arbitrary-DAG theorem;
- no continuum WBE bridge;
- no H7 physical-arrow upgrade.

If any of those reappear implicitly, the packet has failed as an honest export.

## Reviewer-Facing Packet

## Working Claim

In the tested finite families, metric temporal structure can change the
Moses-style branching exponent even when causal order is held fixed.

More carefully:

```text
there exist finite weighted path families, including tree-style and tested
non-tree DAG fixtures, such that:

same causal order
same event count
same causal-set-style order data
different delivery-time metric
=> different beta under the finite harmonic-mean Moses proxy
```

This is the finite metric-causal separation result.

## Formal Spine

### Finite proxy used

For the tested finite family:

```text
T* = harmonic_mean(admissible path delivery times)
beta = 1 - log(T*) / log(n)
```

and for the broader tested non-tree family:

```text
T*_DAG = harmonic_mean(admissible source-to-sink path times)
beta_DAG = 1 - log(T*_DAG) / log(n)
```

### Core finite theorem-shape

The exportable content is:

```text
Fix a finite weighted path family with declared admissible paths and event count n.
Then beta is not determined by causal order alone, because two systems may share
the same causal order and still differ in T* (or T*_DAG), which changes beta.
```

### Positive examples

#### Example 1: Tree-style pair (T186/T187)

Same causal order:

```text
e1 -> {e2,e3} -> e5, and e4 -> e5
```

Different path times:

```text
Alpha = {4,2,1}
Beta  = {3,2,1}
```

Hence:

```text
beta_exact(Alpha) ≈ 0.6651
beta_exact(Beta)  ≈ 0.6941
```

#### Example 2: Non-tree reconvergent DAG pair (T195)

Same non-tree DAG, same reachability, different edge-time metric:

```text
Gamma -> T*_DAG ≈ 3.117 -> beta ≈ 0.293
Delta -> T*_DAG ≈ 2.824 -> beta ≈ 0.355
```

So the finite split is not confined to the original tree fixture.

## Hostile Narrowing

### Narrowing 1: the predictive object collapses to a timing summary

T193 and T194 show that in the current exact finite family:

```text
the predictive value is fully captured by T*
```

and in the tested non-tree extension:

```text
the predictive value is still captured by T*_DAG.
```

### Narrowing 2: matched-summary hostile controls collapse

Matched-`T*` and matched-`T*_DAG` families do not split, even when:

- branch labels change;
- higher moments change;
- tested topology changes.

### Narrowing 3: capability claim absorbed

T197 shows that the current Cap_TI Candidate C does not survive as an
independent capability theorem. In the present family it is absorbed by
standard timing-summary / scheduling / flow-style readings.

### Narrowing 4: no earned continuum bridge

T196 shows that the current finite witness stack does not earn a continuum
WBE bridge.

## Absorber Pass

The reviewer packet must carry forward, rather than hide, the main absorber
results:

- T197: current capability residue is absorbed by standard timing-summary /
  scheduling / flow-style readings;
- T196: current continuum WBE bridge attempt is killed;
- T195: the non-tree extension survives only at the level of `T*_DAG`, not as
  a deeper topology-sensitive theorem.

If the packet needs those absorbers to be omitted in order to look impressive,
it is not a valid export packet.

## Exportable Verdict

## Verdict: narrowed

The strongest reviewer-safe claim is:

```text
The repo has finite evidence that metric delivery-time structure can affect a
Moses-style branching exponent even when causal order is held fixed, and this
effect survives at least one step beyond the original tree fixture into tested
finite non-tree weighted DAGs. However, the currently earned predictive object
collapses to a harmonic-mean path-time summary, the associated capability claim
is absorbed by standard operations-style summaries, and no continuum WBE bridge
is presently earned.
```

## Non-Claims

This packet does **not** claim:

- a new physical law;
- a theorem for arbitrary DAGs;
- an independent Cap_TI capability theorem in the current family;
- a continuum WBE derivation from the finite witnesses;
- support for H7 as a physical-arrow claim.

## Assumptions

- finite weighted path-family proxy accepted;
- admissible path set declared;
- event count `n` fixed;
- path times positive;
- comparison is made at fixed causal order / reachability data.

## What Would Strengthen This Packet

1. A more faithful finite-to-continuum bridge with declared scaling controls.
2. A broader finite family where the split depends on more than `T*` / `T*_DAG`.
3. A reconciliation protocol that reopens nonabsorbed capability residue at
   fixed standard timing summaries.

## Why This Packet Exists

Without T199, the repo risks exporting one of two bad summaries:

- underselling the finite metric-causal split by calling it only a toy tree fact;
- overselling it as a continuum or independent capability theorem.

This packet holds the line between those errors.
