# T207: Cap_TI Minimal Statistic After Corrections

## Target Claims

- Cap_TI Candidate C
- T193 minimal sufficient statistic
- T187-T199 harmonic-mean chain

## Origin

T200-T206 corrected the key provenance issue: inverse-time weights do not follow
from the stated LP, the harmonic mean is proxy-only unless separately derived,
and DAG path summaries need shared-edge state completion.

## Formal Target

Reclassify the minimal statistic by declared regime:

```text
harmonic proxy
stated pure LP
lower-bound LP
DAG shared-edge flow
```

## Setup / Fixtures

Use:

```text
Alpha = {4,2,1}
Beta = {3,2,1}
Gamma/Delta = T195 DAG path sets
```

Track objective, path times, path-edge incidence, `n`, and any diversity floor
`d`.

## Positive Control

Under the harmonic proxy:

```text
R_H = T_H
```

Therefore `(n, T_H)` is sufficient by definition for that proxy.

## Negative Control

Under the stated pure LP:

```text
optimum = min_i t_i
```

not `T_H`. With lower bound `d` and a unique shortest path:

```text
LP_d = (1 - (k-1)d) * t_min + d * sum_{i != min} t_i
```

not inverse-time weighting.

## Absorber Pass

Operations research absorbs the earlier exactness claim: the sufficient
statistic depends on the actual objective and constraints. DAG cases require
edge incidence/capacity data if shared edges carry flow constraints.

## Results

The old T193 claim is no longer exact. `(n, T_H)` remains sufficient only for
the harmonic proxy. For the corrected LP family, the candidate statistic
changes to the LP objective summary plus declared constraint regime. For
shared-edge DAGs, path harmonic is not enough for edge-flow capability unless
independence is explicitly assumed.

## Verdict: narrowed

Cap_TI Candidate C survives only as a regime-dependent timing-summary audit,
not as an exact harmonic-mean minimality theorem.

## Falsification Conditions

Reverse this narrowing only if a corrected derivation proves inverse-time
weights from a stated objective, or an executable hostile family shows same
corrected statistic but different Cap_TI value.

## Next Step

Use T208 as the reviewer-facing errata and T209 as the arithmetic guardrail.
