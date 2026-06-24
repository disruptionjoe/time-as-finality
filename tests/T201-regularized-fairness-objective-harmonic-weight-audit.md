# T201: Regularized / Fairness Objective Harmonic-Weight Audit

## Target Claims

- T187 harmonic-proxy repair route
- MTI / Cap_TI finite timing summary provenance

## Origin

T200 killed the linear-program derivation, but left open whether inverse-time
weights can be justified by a different objective.

## Formal Target

Find a declared optimization problem over `w_i >= 0`, `sum_i w_i = 1`, whose
solution is:

```text
w_i = (1/t_i) / sum_j (1/t_j)
```

without changing the meaning of the capability value midstream.

## Setup / Fixtures

Use:

```text
t = (4, 2, 1)
```

Candidate objective families:

```text
A. linear time + entropy regularization
B. minimax equal-load objective
C. hard equal-contribution constraint w_i t_i = constant
D. generic convex regularizer without equal-load semantics
```

## Positive Control

The minimax/equal-load objective:

```text
minimize max_i w_i t_i
subject to sum_i w_i = 1
           w_i >= 0
```

equalizes all active `w_i t_i`. Therefore:

```text
w_i t_i = c
sum_i w_i = 1
=> c = 1 / sum_j (1/t_j)
=> w_i = (1/t_i) / sum_j (1/t_j)
```

For `(4,2,1)`, this gives:

```text
w = (1/7, 2/7, 4/7)
sum_i w_i t_i = 12/7
```

## Negative Control

Entropy-regularized linear cost does not generally yield reciprocal weights.
Its interior solution has softmin form:

```text
w_i proportional to exp(-t_i / lambda)
```

not `1/t_i`.

## Absorber Pass

Convex optimization absorbs the distinction. Inverse-time weights are not a
generic KKT consequence; they arise only after adding an equal-load, minimax, or
similar fairness principle. That principle must be physically or operationally
justified before it can carry Moses/WBE weight.

## Results

The harmonic proxy is mathematically coherent under an equal-load model. It is
not justified by T187's original weighted-sum LP.

## Verdict: narrowed

The proxy is narrowed to a fairness/equal-load model unless a stronger
domain-native derivation appears.

## Falsification Conditions

Promote only if a transport law, WBE derivation, or physical flow principle
requires equalized `w_i t_i`. Kill if the equal-load premise is merely chosen
for algebraic convenience.

## Next Step

Propagate the downgrade through T193-T199 and test DAG shared-edge behavior in
T202.
