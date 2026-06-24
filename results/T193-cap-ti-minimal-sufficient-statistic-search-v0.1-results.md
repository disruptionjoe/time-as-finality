# T193 Results: Cap_TI Minimal Sufficient Statistic Search

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. The result below is
conditional on the finite harmonic-proxy regime. `(n, T*)` is not an exact
Moses minimal sufficient statistic unless a future objective derives the
harmonic proxy. See T207 for the corrected cross-regime statistic audit.

## Outcome

Cap_TI Candidate C narrows to a much smaller predictive object than the full
metric-decorated transport structure.

For the exact finite Moses/T187 reading, the best current sufficient statistic
is:

```text
(n, T*)
```

where `T*` is the harmonic mean of path delivery times.

## Main Compression Result

T187 gives:

```text
beta = 1 - log(T*) / log(n)
```

Therefore:

```text
R(beta,n) = n^(1-beta) = T*.
```

So the Cap_TI value is exactly determined by the harmonic-mean delivery-time
summary in the tested family.

## What This Means

- Causal order is not sufficient.
- Full path-time structure is sufficient but not minimal.
- CV is useful but only approximate.
- Harmonic mean is the best current exact reduced invariant.

## Repo-Safe Reading

Candidate C survives, but in a narrowed form:

```text
the capability depends on a specific metric summary,
not the whole metric transport object.
```

That still keeps it outside pure causal-order / entropy-only absorbers, but it
changes what T194 should freeze.

## What This Changes

- T194 should target `(n, T*)` as the reduced object and test whether richer
  details matter beyond it.
- If a future hostile family keeps `(n, T*)` fixed but changes the capability,
  this reduction fails.
- If no such family exists, Candidate C becomes a harmonic-mean-based
  capability rather than a full-transport capability.
