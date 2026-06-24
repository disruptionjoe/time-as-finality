# T201 Results: Regularized / Fairness Objective Harmonic-Weight Audit

## Outcome

`narrowed`

## Main Readout

Inverse-time weights can be derived from a minimax/equal-load objective, but
not from the original T187 LP.

## Positive Control

For `t = (4,2,1)`:

```text
w = (1/7, 2/7, 4/7)
w_i t_i = 4/7 for all i
sum_i w_i t_i = 12/7
harmonic_mean(t) = 12/7
```

## Negative Control

Entropy-regularized linear cost produces softmin weights, not reciprocal
weights.

## Absorber Pass

The result is absorbed by standard objective-choice taxonomy: different
objectives yield different allocation laws.

## Verdict: narrowed

The harmonic proxy is conditionally coherent under equal-load semantics, but
not yet physically or WBE-derived.
