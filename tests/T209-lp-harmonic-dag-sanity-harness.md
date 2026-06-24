# T209: LP-Harmonic-DAG Sanity Harness

## Target Claims

- T187 correction guardrail
- T207 statistic re-audit
- T208 errata verification

## Origin

The repo needs a lightweight executable check that prevents LP optima, harmonic
proxies, and shared-edge DAG flow assumptions from being conflated again.

## Formal Target

Define arithmetic checks for:

```text
harmonic_mean(ts)
lp_optimum(ts,d)
beta(T,n)
shared_edge_loads(paths)
```

## Setup / Fixtures

```text
Alpha {4,2,1}: T_H = 12/7, pure LP = 1, LP d=.1 = 7/5
Beta  {3,2,1}: T_H = 18/11, pure LP = 1, LP d=.1 = 13/10
Gamma {4,2,5,3}: T_H = 240/77
Delta {3,2,4,3}: T_H = 48/17
```

The T195 reconvergent DAG paths must flag shared edges.

## Positive Control

The harness passes if it reports LP/harmonic mismatch on Alpha/Beta and flags
shared edges in T195-style reconvergent paths.

## Negative Control

The harness must not flag all-equal path times, where LP and harmonic can
coincide. It must not treat an explicitly path-independent model as an
edge-flow model.

## Absorber Pass

The harness grants ordinary LP/network-flow arithmetic priority over repo
terminology. Any promoted claim must declare which objective the harness is
checking.

## Results

The arithmetic gate catches the T187 failure mode and forces DAG claims to
declare whether path summaries are independent proxies or edge-flow models.

## Verdict: promoted

Promote T209 as a required sanity gate before future MTI/Cap_TI metric-causal
claims are registered.

## Falsification Conditions

Fails if the harness cannot distinguish pure LP, lower-bound LP, and harmonic
proxy, or if it ignores shared-edge incidence in DAG fixtures.

## Next Step

Run `tests/test_mti_lp_harmonic_sanity.py` whenever this line is extended.
