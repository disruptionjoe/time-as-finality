# T187: Moses Finite Harmonic-Proxy Audit - Results v0.2

**Date:** 2026-06-24
**Status:** CORRECTED - narrowed after mathematical review
**Test spec:** `tests/T187-moses-exact-constrained-optimization.md`
**Target claims:** MTI, Cap_TI Candidate C, T186 direction validation

---

## Summary Verdict

**Narrowed.** T187 no longer resolves the "exact Moses optimization" blocker.
The harmonic-mean calculation remains useful only as a finite proxy whose sign
agrees with the T186 CV proxy:

```text
beta_HM(Beta) = 0.6941... > beta_HM(Alpha) = 0.6651...
```

The original claim that inverse-time weights follow from KKT conditions for the
stated LP is mathematically incorrect.

---

## 1. Corrected Formula Status

The retained finite proxy is:

```text
T*_HM = harmonic_mean({t_1, ..., t_k})
      = k / sum_i (1/t_i)

beta_HM = 1 - log(T*_HM) / log(n)
R_HM = n^(1-beta_HM) = T*_HM
```

This is not an exact solution of:

```text
minimize sum_i w_i t_i
subject to sum_i w_i = 1
           w_i >= d
```

For that linear program, optima occur at extreme points. A lower-bound
diversity floor allocates the required minimum mass to non-shortest paths and
puts the remaining mass on a shortest path. It does not create reciprocal
weights.

---

## 2. Computation for T186 Systems

### System Alpha - delivery times `{4, 2, 1}`

```text
n = 5
T*_HM = 3 / (1/4 + 1/2 + 1)
      = 3 / 1.75
      = 1.714285714...

beta_HM(Alpha) = 1 - log(1.714285714...) / log(5)
               = 0.6651...
```

### System Beta - delivery times `{3, 2, 1}`

```text
n = 5
T*_HM = 3 / (1/3 + 1/2 + 1)
      = 3 / 1.833333333...
      = 1.636363636...

beta_HM(Beta) = 1 - log(1.636363636...) / log(5)
              = 0.6941...
```

---

## 3. Comparison Table

| Quantity | System Alpha | System Beta | Agreement |
|---|---:|---:|---|
| Event count `n` | 5 | 5 | matched |
| Causal order | same | same | matched |
| Delivery times | `{4,2,1}` | `{3,2,1}` | different |
| Harmonic proxy `T*_HM` | 1.7143 | 1.6364 | different |
| `beta_HM` | 0.6651 | 0.6941 | Beta > Alpha |
| `beta_CV` from T186 | 0.3491 | 0.4438 | Beta > Alpha |

---

## 4. Absorber / Correction Pass

Standard linear programming absorbs the old derivation:

```text
linear objective + simplex/lower-bound constraints
=> extreme-point optimum
```

For the concrete Alpha fixture and `d = 0.1`:

```text
LP optimum weights = (0.1, 0.1, 0.8)
LP objective       = 1.4
inverse-time weights = (1/7, 2/7, 4/7)
inverse-time objective = 12/7 = 1.714...
```

So reciprocal weights are feasible but not optimal. They require a different
objective, such as equal-load/minimax fairness, which T201 now tests.

---

## 5. MTI Impact

**MTI remains conditional / partially supported.** T187 still shows that the
metric-causal split is not unique to the CV approximation, but it does not
establish exact finite Moses optimization.

Updated status:

| Item | Status |
|---|---|
| T186 CV sign split | still supported |
| T187 harmonic proxy sign split | supported as proxy |
| Exact constrained optimization | not resolved |
| Continuum WBE bridge | not earned |
| Cap_TI Candidate C | conditional on proxy or future repaired objective |

---

## 6. Cap_TI Candidate C Impact

The current Cap_TI statement must be read as:

```text
under the harmonic proxy, metric timing data predicts a different beta/R value
than causal order alone.
```

It must not be read as:

```text
exact Moses optimization proves an independent Cap_TI capability theorem.
```

---

## Verdict: narrowed

The harmonic-proxy sign check survives. The exact-KKT derivation is killed and
the downstream packet is downgraded to conditional proxy status until T200/T201
or later work supplies a legitimate objective.

## Next Step

Run and register:

```text
T200: linear-program/KKT audit
T201: regularized/fairness objective audit
T202: shared-edge DAG path-harmonic counterexample
```
