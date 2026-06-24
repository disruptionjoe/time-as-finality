# T207 Results: Cap_TI Minimal Statistic After Corrections

## Outcome

`narrowed`

## Main Readout

T193's exact minimal-statistic result is demoted to proxy-only status.

| Regime | Sufficient statistic | Status |
| --- | --- | --- |
| Harmonic proxy | `(n, T_H)` | valid proxy-only |
| Pure LP | `(n, min(t_i))` if `R` uses LP optimum | not harmonic |
| Lower-bound LP | `(n, k, d, t_min, sum_{i != min} t_i)` for unique shortest path | not inverse-time |
| Shared-edge DAG flow | incidence/capacity plus objective | path harmonic underdeclared |

## Verdict: narrowed

Cap_TI currently has a timing-summary proxy, not an exact minimal sufficient
statistic theorem.

## Next Step

Apply errata through T208 and executable checks through T209.
