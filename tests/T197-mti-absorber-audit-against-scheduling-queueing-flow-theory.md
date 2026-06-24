# T197: MTI Absorber Audit Against Scheduling / Queueing / Flow Theory

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. The absorption result below
is strengthened, not weakened: the surviving `T*` object is a conditional
harmonic proxy or equal-load timing summary, not an exact constrained Moses
optimization. T206 absorbs the repaired capacity-aware proxy into native
network/allometric transport theory.

## Target Claims

- Cap_TI Candidate C (`open-problems/cap-ti-capability-object-spec.md`)
- MTI (`claims/MTI-metabolic-temporal-irreducibility.md`)
- T193 minimal sufficient statistic result
- T194 hostile same-neighbor-data adversarial-family result
- T198 positive / null control suite

## Origin

The earlier MTI / Cap_TI pass left the capability in a much narrower state than
the original framing:

```text
T193: in the finite harmonic-proxy regime, Candidate C compresses to (n, T*)
T194: no stricter hostile survivor remains once (n, T*) are matched
T198: the reusable control rule is now "move T* -> split; preserve T* -> null"
```

That creates the right absorber question:

```text
If Candidate C is now exactly or nearly a harmonic-mean delivery-time summary,
does any nonabsorbed TaF residue remain once scheduling, queueing, network flow,
and control / operations viewpoints are granted their native objects and theorems?
```

This is the core T197 burden. If those neighbors already own the predictive
content of `T*`, then Candidate C is not a standalone capability theorem. At
best it becomes translation residue or a useful repo-facing normal form.

## Formal Target Or Obligation

Audit the surviving capability claim:

```text
Cap_TI^C(Y) = R(beta(Y), n(Y))
```

under the exact finite Moses/T187 reading:

```text
beta(Y) = 1 - log(T*(Y)) / log(n)
R(beta,n) = n^(1-beta) = T*(Y)
```

where `T*` is the harmonic mean of the path delivery times.

The typed question is:

```text
Does the predictive content "a lower harmonic-mean delivery time implies fewer
reconciliation rounds" survive after the neighboring theories are allowed their
standard state variables, service-time summaries, path-delay summaries,
throughput bounds, and queueing congestion models?
```

## Capability Under Audit

The current live capability is:

```text
Given a finite source system Y with event count n and path delivery times T,
predict a reconciliation-efficiency quantity R before multi-observer
reconciliation begins.
```

In the current exact family:

```text
R = T*
```

so the capability is already equivalent to predicting a harmonic-mean
delivery-time summary.

## Neighbor Theories Granted Full Legitimacy

### Neighbor 1: Scheduling / Operations

Native state granted:

- job or packet service times;
- path completion times;
- dispatch / allocation rules;
- aggregate latency summaries;
- pre-run completion-time predictors.

Native absorber pressure:

```text
harmonic-mean service-time summaries,
parallel-machine throughput approximations,
and load-balancing efficiency scores
already treat inverse-time sums as canonical predictors.
```

### Neighbor 2: Queueing Theory

Native state granted:

- arrival rate;
- service rate;
- service-time distribution summaries;
- congestion and waiting-time transforms;
- reconciliation-as-queue semantics.

Native absorber pressure:

```text
T185 already grounded C(lambda) via M/M/1-style reconciliation congestion.
Once service channels are summarized by effective rate, harmonic-mean timing
summaries are standard queueing objects rather than TaF-specific capability data.
```

### Neighbor 3: Network Flow / Transport

Native state granted:

- path travel times;
- inverse-time weighting;
- path-allocation efficiencies;
- effective end-to-end delivery summaries.

Native absorber pressure:

```text
T187 itself uses the standard inverse-time weighting rule
w_i* propto 1 / t_i,
which is a transport / flow-style allocation law.
If Candidate C depends only on the induced harmonic mean T*,
the predictive object looks flow-owned rather than TaF-native.
```

### Neighbor 4: Control / Performance Engineering

Native state granted:

- before-the-fact performance bounds;
- coarse-grained response-time objectives;
- summary-statistic predictors for convergence or completion time.

Native absorber pressure:

```text
predicting the number of rounds or time-to-agreement from a delay summary is
ordinary performance modeling unless the repo can show that the predictor
depends on PO1 / gluing structure in a way those neighbors cannot import.
```

## Positive Control

Use the T198 positive-control class `P1`:

```text
Alpha: {4,2,1}
Beta:  {3,2,1}
T*_Alpha != T*_Beta
=> Candidate C predicts a split
```

This confirms that the audit is not trivializing the capability away. The
question is who owns the split once the standard neighbors are fully credited.

## Negative Controls

### Negative Control N1: Branch relabeling

Use T198 branch-label null:

```text
same path-time multiset
same T*
different branch labels
=> no capability split
```

This checks that the absorber audit is not mistaking pure representation
changes for predictive content.

### Negative Control N2: Compensated same-T* tradeoff

Use T198 compensated-harmonic-mean null:

```text
different higher moments
same T*
=> no capability split
```

This checks whether the exact finite family keeps any hidden dependence beyond
the standard transport summary.

### Negative Control N3: Topology variation with matched T*

Use T198 topology-variation null:

```text
same n
same T*
different richer branching detail
=> no capability split
```

This checks whether the repo can still claim a TaF-specific topological residue
once the performance summary is matched.

## Absorber Pass

### Step 1: Scheduling reading

Under the scheduling / operations reading, `R = T*` is already an ordinary
performance summary:

```text
faster effective path mix -> lower completion proxy
slower effective path mix -> higher completion proxy
```

The positive-control split is therefore predicted by standard service-time and
dispatch summaries without any TaF-specific formal machinery.

### Step 2: Queueing reading

T185 already translated the issuance dynamics into reconciliation congestion
language. Once Candidate C itself collapses to `T*`, the remaining predictor is
just an effective service-time statistic feeding a pre-run delay estimate.

No extra PO1 structure is used to compute the current exact-family capability
value beyond the already-absorbed congestion semantics.

### Step 3: Flow / transport reading

T187's exact formula uses:

```text
w_i* = (1/t_i) / sum_j (1/t_j)
T*   = harmonic_mean(t_1, ..., t_k)
```

This is already a canonical flow-allocation summary. The current Candidate C
value is the same object the flow model optimizes.

So under same-neighbor-data honesty:

```text
the flow model is not a neighbor metaphor;
it is already the object supplying the predictive statistic.
```

### Step 4: Search for surviving residue

A nonabsorbed residue would need one of the following:

1. two systems with the same standard performance summaries but different
   Cap_TI values;
2. a reconciliation protocol whose value depends on PO1 / gluing structure
   beyond what the standard timing summaries already encode;
3. a control family where matched `T*` still yields different predictive
   content because of genuinely TaF-native structure.

T193, T194, and T198 now weigh against all three in the current exact family:

- T193: the value already compresses to `T*`;
- T194: matched `(n, T*)` collapses the split;
- T198: all reusable null controls are phrased exactly in those terms.

## Results

### 1. Positive split survives, but as absorber-owned content

The Alpha / Beta split remains real:

```text
T*_Alpha != T*_Beta => R_Alpha != R_Beta
```

But the split is already predicted by standard scheduling / flow summaries of
effective delivery time.

### 2. No same-summary residue survives in the current exact family

The T198 null controls remain null under the current reading:

```text
same T* => same R
```

So the current capability adds no predictive content beyond the standard
harmonic-mean timing summary.

### 3. Candidate C is absorbed as an independent capability claim

What survives is not a new standalone capability theorem, but a translation:

```text
the repo's reconciliation-bound language
<-> a standard effective-delay summary T*
```

That may still be useful operationally inside the repo, but it is not enough to
claim that Candidate C remains an independent MTI / TaF capability result in
the current exact finite family.

### 4. What remains live after absorption

This test does NOT kill all future MTI / Cap_TI work.

What remains open is a narrower burden:

```text
find a reconciliation protocol or broader graph family where the predictive
value depends on PO1 / gluing / observer-reconciliation structure beyond the
standard harmonic-mean timing summary.
```

Until that happens, the current exact-family Candidate C is absorber-owned.

## Verdict: absorbed

T197 returns `absorbed`.

Repo-safe statement:

```text
In the current harmonic-proxy regime, Cap_TI Candidate C is absorbed
by standard scheduling / queueing / flow / performance-theory summaries.
Its predictive content collapses to the harmonic-mean delivery-time statistic T*,
and the current control suite shows no surviving same-summary TaF residue.
```

## Falsification Conditions

This absorbed verdict should be revisited if any of the following occurs:

1. a matched-`T*` family is found with different reconciliation predictions;
2. T195 shows a broader graph class where the predictive value depends on
   structure beyond harmonic mean;
3. a formal reconciliation protocol is supplied where PO1 / gluing structure
   changes the value at fixed standard timing summaries;
4. T196 identifies a continuum bridge quantity that survives standard
   operations-style absorption.

## Next Step

The best next move after T197 is not more rhetoric about Candidate C. It is:

```text
T195: test whether the metric-causal separation survives beyond the current
      tree-style exact family;
```

because only a broader family or a richer reconciliation protocol can reopen a
nonabsorbed capability claim.
