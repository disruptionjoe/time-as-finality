# T193: Cap_TI Minimal Sufficient Statistic Search

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. Every statement below that
treats `T*` as "exact" should be read as conditional on the finite harmonic
proxy. T193's minimal-statistic result is not an exact Moses theorem; it says
that `(n, T*)` is sufficient for the declared harmonic-proxy regime. T207
re-audits the statistic under corrected LP and shared-edge DAG regimes.

## Target Claims

- Cap_TI Candidate C (`open-problems/cap-ti-capability-object-spec.md`)
- MTI (`claims/MTI-metabolic-temporal-irreducibility.md`)
- T186 / T187 physical-substrate fixture

## Origin

Cap_TI Candidate C currently reads as if the capability may depend on a rich
physical object:

```text
the full metric-decorated branching transport structure
```

But T186 and T187 already compute the discriminating quantity `beta` from much
smaller summaries of the delivery-time data. T193 asks the right compression
question:

```text
What is the smallest object that still determines the Cap_TI reconciliation
prediction?
```

This is necessary before the hostile family in T194. If a smaller standard
invariant already carries the full predictive load, the capability survives
only in that narrower form.

## Formal Target Or Obligation

For Cap_TI Candidate C, the operative value is:

```text
R(beta,n) = n^(1-beta)
```

where `n = |r|` is event count and `beta` is the branching exponent.

T193 tests candidate reduced invariants `I` such that:

```text
I(Y_1) = I(Y_2)  =>  R(Y_1) = R(Y_2)
```

for the physical-substrate systems under consideration.

The search is not for any arbitrary sufficient invariant, but for the smallest
repo-honest one among the quantities already in play.

## Candidate Reduced Invariants

### Candidate I1: Full time-decorated path multiset

```text
I1(Y) = (n, {t_1, ..., t_k})
```

where `{t_i}` are the delivery times of the independent source-to-sink paths.

This is the obvious sufficient object if T187 is correct.

### Candidate I2: Harmonic mean of path times

From T187:

```text
T*(Y) = harmonic_mean(t_1, ..., t_k)
beta(Y) = 1 - log(T*(Y)) / log(n)
```

So a much smaller candidate is:

```text
I2(Y) = (n, T*(Y))
```

### Candidate I3: Inverse-time sum

Equivalent to harmonic mean up to the known path count `k`:

```text
H(Y) = sum_i 1/t_i
T*(Y) = k / H(Y)
```

Candidate:

```text
I3(Y) = (n, k, H(Y))
```

### Candidate I4: Coefficient of variation proxy

From T186:

```text
beta_CV(Y) = calibration_beta * (1 - CV(T))
```

Candidate:

```text
I4(Y) = (n, CV(T))
```

### Candidate I5: Causal order plus event count only

Candidate:

```text
I5(Y) = (n, causal_order(Y))
```

This is the strongest absorber-owned small object and serves as a null
candidate.

## Setup / Fixtures

Use the Alpha / Beta systems from T186 / T187.

### System Alpha

```text
n = 5
path times = {4, 2, 1}
harmonic mean T*_A = 3 / (1/4 + 1/2 + 1) = 1.714...
H_A = 1.75
beta_exact(A) = 0.6650
R_A(n) = n^(1-beta_A)
```

### System Beta

```text
n = 5
path times = {3, 2, 1}
harmonic mean T*_B = 3 / (1/3 + 1/2 + 1) = 1.636...
H_B = 1.833...
beta_exact(B) = 0.6944
R_B(n) = n^(1-beta_B)
```

Both systems have:

```text
same causal order
same event count
same entropy production class
same gluing topology type
```

and differ only in delivery-time metric.

## Positive Control

Positive control for sufficiency:

Use `I2 = (n, T*)`.

Since T187 gives:

```text
beta = 1 - log(T*) / log(n),
```

we have

```text
R(beta,n) = n^(1-beta) = n^(log(T*)/log(n)) = T*.
```

So in the exact Moses finite formula:

```text
R(beta,n) = T*.
```

This means the harmonic mean `T*` is not just sufficient for `beta`; it is
already sufficient for the Cap_TI value itself once `n` is fixed, and in fact
determines it exactly.

## Negative Controls

### Negative Control A: Causal order only

Alpha and Beta have identical causal order and identical `n`, but different
`R`. Therefore:

```text
I5(Y) = (n, causal_order(Y))
```

is not sufficient.

### Negative Control B: Full path multiset is not minimal

If `I2` already determines `R`, then `I1` is sufficient but not minimal.

### Negative Control C: CV proxy is not exact

The CV proxy distinguishes Alpha and Beta and is therefore informative, but it
does not recover the exact T187 values. So `I4` is a useful heuristic summary,
not the exact minimal sufficient statistic for the exact Moses/T187 reading.

## Absorber Pass

The natural absorber is standard statistics / optimization compression:

```text
If a decision value depends only on a low-dimensional summary, that summary is
the sufficient statistic for that decision task.
```

Under that absorber:

1. The full time-decorated transport object is overdescribed for Candidate C.
2. The harmonic mean of path times is the exact sufficient statistic for the
   T187 finite Moses formula.
3. The capability does not need the entire delivery-time distribution once the
   summary `T*` is known.

This does not absorb the capability away entirely. It narrows it:

```text
Cap_TI Candidate C depends on a specific metric summary, not the whole metric
transport object.
```

That is a useful reduction, not a defeat.

## Results

### 1. Causal order is insufficient

T186/T187 already establish:

```text
same causal order
same n
different beta
different R
```

So causal order plus size is not sufficient for Cap_TI Candidate C.

### 2. The exact T187 formula compresses the metric object drastically

From T187:

```text
beta = 1 - log(T*) / log(n)
```

Therefore:

```text
R(beta,n) = n^(1-beta) = T*.
```

This is the key compression result.

For the exact finite Moses reading used in T187, the Cap_TI value equals the
harmonic mean of path delivery times. The whole path multiset is not needed
once its harmonic mean is known.

### 3. Minimal sufficient object for Candidate C

The best current reduced invariant is:

```text
I_min(Y) = (n, T*(Y))
```

and for the fixed-path-count T186/T187 family this can be sharpened even
further to:

```text
I_min(Y) = T*(Y)
```

because `R = T*` directly in the exact formula.

To stay slightly more conservative across nearby families, T193 keeps the
official reduced invariant as:

```text
(n, harmonic_mean_of_path_times)
```

rather than just `T*`.

### 4. What this means for the capability claim

Cap_TI Candidate C does **not** require the full time-decorated branching
transport object for prediction. It requires a smaller metric summary:

```text
the harmonic-mean delivery-time statistic together with event count.
```

This is still beyond causal order and beyond the current gluing-topology-only
`G`, but it is less structurally rich than the original full-object reading.

## Verdict: narrowed

T193 narrows Cap_TI Candidate C.

Not supported:

```text
the full metric-decorated transport object is the minimal predictive object.
```

Supported:

```text
for the finite harmonic-proxy regime, the harmonic mean of path delivery
times (with n declared) is a sufficient and currently best minimal statistic
for the Candidate C reconciliation prediction.
```

## Falsification Conditions

This verdict should be revisited if any of the following occurs:

1. A hostile family is found where two systems have the same `(n, T*)` but
   different exact Cap_TI values.
2. The exact Moses finite formula is replaced by a richer reconciliation
   protocol that depends on more than `T*`.
3. A gluing-data extension `G+time` is defined that makes `T*` already part of
   the declared same-neighbor-data surface, absorbing Candidate C more deeply.

Without one of those, the harmonic-mean summary is the best current minimal
sufficient statistic.

## Next Step

T194 should now be designed against the reduced invariant, not the full object:

```text
construct hostile families that try to hold (n, T*) fixed while varying richer
metric or topological detail, and see whether Candidate C still splits.
```
