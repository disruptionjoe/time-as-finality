# T383 Results: Relativity Pattern Falsification Suite

## Current Strongest Claim

The two-null-channel relativity pattern survives the baseline case and fails in
targeted, interpretable ways when its core premises are perturbed.

The clean adapter is therefore not arbitrary, but it is premise-sensitive.

## Result Summary

| perturbation | status | classification |
|---|---|---|
| `baseline_two_null` | `survives` | `survivor` |
| `anisotropic_signal_speed` | `falsifies_signal_speed` | `falsifier` |
| `nonreciprocal_scaling` | `falsifies_signal_speed` | `falsifier` |
| `delayed_left_channel` | `falsifies_signal_speed` | `falsifier` |
| `deterministic_noise` | `falsifies_exact_access` | `falsifier` |
| `missing_right_channel` | `falsifies_channel_completeness` | `falsifier` |
| `extra_primitive_channel` | `falsifies_minimality` | `falsifier` |
| `coarse_grained_access` | `partial_subset_only` | `partial` |

## Hostile Comparators

| comparator | absorbs? | status |
|---|---:|---|
| `robustness` | `false` | `fragile_but_informative` |
| `finite_perturbation_catalog` | `true` | `still_absorbs` |
| `exact_invariance_requirement` | `false` | `strict` |

## Plain-English Reading

T383 says:

```text
The two-null adapter works, but only when the key premises stay intact.
```

The useful result is not "it survives everything." It does not. The useful
result is that each failure points to a specific dependency:

- anisotropy/nonreciprocity break shared signal calibration,
- delay breaks invariant signal timing,
- missing channels break two-sided relativity,
- extra primitive channels break minimality,
- noise/coarse access demote exact record-level invariance.

## What Improved

We now have a falsification map for the clean adapter. This makes the synthesis
sharper because the premise bundle is no longer vague.

## What Weakened

The pattern is not broadly robust. It is a precise structure:

```text
two complete primitive null channels
+ reciprocal scaling
+ invariant signal calibration
+ exact access
+ minimality
```

Relaxing those conditions often breaks or demotes the result.

## Claim Ledger Update

Register T383 as falsification evidence. The clean adapter is not arbitrary, but
it is premise-sensitive. The synthesis should state the exact premise bundle.

## Next

Write the T384 synthesis packet:

```text
Given X, Lorentz-pattern observer relativity is forced.
What remains open is Y.
```
