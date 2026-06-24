# T187: Moses Finite Harmonic-Proxy Audit

## Target Claims

- MTI (`claims/MTI-metabolic-temporal-irreducibility.md`)
- Cap_TI Candidate C (`open-problems/cap-ti-capability-object-spec.md`)
- T186 metric-vs-causal-order beta test

## Correction Status

**Corrected after mathematical review.** This artifact is no longer treated as
an exact constrained optimization result. The harmonic-mean calculation is
retained only as a finite proxy / directional sign check.

The original T187 derivation incorrectly claimed that the linear program

```text
minimize sum_i w_i t_i
subject to sum_i w_i = 1
           w_i >= d
```

yields inverse-time weights by KKT conditions. It does not. The plain linear
program is degenerate, and adding lower-bound diversity constraints alone puts
all excess mass on a shortest path. T200 carries the explicit correction, and
T201 tests whether a different fairness/equal-load objective can legitimately
earn the harmonic proxy.

## Origin

T186 found a metric-vs-causal-order split using a CV-based approximation:

```text
beta_CV(Alpha) = 0.3491
beta_CV(Beta)  = 0.4438
```

The original T187 attempted to remove the T186 open blocker by presenting an
exact finite Moses optimization. The corrected reading is narrower:

```text
T187 cross-checks the sign under a finite harmonic proxy,
but exact finite Moses optimization remains open.
```

## Corrected Formal Target

The proxy retained from T187 is:

```text
T*_HM(t_1, ..., t_k) = harmonic_mean(t_1, ..., t_k)
                     = k / sum_i (1/t_i)

beta_HM(Y) = 1 - log(T*_HM(Y)) / log(n(Y))
R_HM(beta,n) = n^(1-beta) = T*_HM
```

This proxy is mathematically well-defined for positive path times, but it is
not derived here from the stated LP. It should be read as conditional on a
future objective, bridge, or declared equal-load interpretation.

## Setup / Fixtures

### System Alpha

```text
n = 5
causal order = e1 -> {e2,e3} -> e5, e4 -> e5
path times = {4, 2, 1}
```

### System Beta

```text
n = 5
causal order = identical to Alpha
path times = {3, 2, 1}
```

## Harmonic-Proxy Computation

### Alpha

```text
T*_HM(Alpha) = 3 / (1/4 + 1/2 + 1)
             = 3 / 1.75
             = 1.714285714...

beta_HM(Alpha) = 1 - log(1.714285714...) / log(5)
               = 0.6651...
```

### Beta

```text
T*_HM(Beta) = 3 / (1/3 + 1/2 + 1)
            = 3 / 1.833333333...
            = 1.636363636...

beta_HM(Beta) = 1 - log(1.636363636...) / log(5)
              = 0.6941...
```

So:

```text
beta_HM(Beta) > beta_HM(Alpha)
```

The harmonic proxy agrees with the T186 CV proxy on the sign of the split.

## Positive Control

The Alpha/Beta pair is a positive control for the finite proxy:

```text
same causal order
same event count
different delivery-time metric
different T*_HM
different beta_HM
```

This keeps the metric-causal separation live as a finite proxy phenomenon.

## Negative Control

The stated linear program is a negative control for the original derivation.
For times `(4,2,1)` and diversity floor `d = 0.1`, the LP optimum is:

```text
w = (0.1, 0.1, 0.8)
objective = 1.4
```

Inverse-time weights are:

```text
w = (1/7, 2/7, 4/7)
objective = 12/7 = 1.714...
```

The inverse-time allocation is feasible for this `d`, but it is not optimal.

## Absorber Pass

Standard linear programming absorbs the original KKT claim:

```text
linear objective + simplex/lower-bound constraints
=> optimum at an extreme point, except for ties
```

Inverse-time weights require a different premise, such as minimax equal-load
allocation, explicit fairness, entropy-like constraints with a different
solution form, or a domain-native flow law. Those premises are not supplied by
T187.

## Results

What survives:

```text
The harmonic proxy gives the same sign as T186:
beta_HM(Beta) > beta_HM(Alpha).
```

What does not survive:

```text
T187 does not derive the proxy from exact constrained optimization.
T187 does not remove the exact-Moses open blocker.
T187 does not establish a WBE continuum bridge.
```

## Verdict: narrowed

The T186 positive direction survives as a harmonic-proxy sign check. The exact
optimization claim is demoted and sent to T200/T201 for repair or death.

## Falsification Conditions

Revise this narrowed verdict only if a future artifact supplies:

1. a declared objective or physical flow law whose solution is inverse-time
   allocation;
2. a normalization-consistent derivation of `T*_HM`;
3. controls showing the result is not merely a chosen fairness proxy;
4. a typed bridge if the result is exported toward WBE / continuum language.

## Next Step

Use T200-T202 to repair the provenance:

```text
T200: audit the LP/KKT error directly.
T201: test possible fairness/equal-load repairs.
T202: test whether DAG path-harmonic summaries fail under shared-edge accounting.
```
