# T194 Results: Cap_TI Hostile Same-Neighbor-Data Adversarial Family

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. The matched-`T*` collapse is
conditional on the harmonic-proxy regime. It does not apply to corrected LP or
edge-capacity DAG flow models without restating the capability object.

## Outcome

No stricter hostile survivor remains in the current exact finite Moses/T187
family once the reduced invariant `(n, T*)` is matched.

Candidate C is still live, but in a narrower form:

```text
it survives when T* differs;
it collapses when (n, T*) are matched.
```

## Family Summary

| Family | What is held fixed? | What varies? | Result |
| --- | --- | --- | --- |
| A: Alpha/Beta positive control | causal order, n, entropy class, topology type | `T*` | split survives |
| B: branch-label permutation | `n`, `T*`, full time multiset | branch labeling | collapses |
| C: compensated metric tradeoff | `n`, `T*` | higher moments / asymmetry | collapses |
| D: topology variation with matched `T*` | `n`, `T*` | richer branching detail | collapses under current exact formula |

## Main Finding

Because T187 gives:

```text
R(beta,n) = T*,
```

any exact hostile family with matched `(n, T*)` must also match the Candidate C
value.

So T194 does not find a stricter residue beyond the reduced invariant from
T193.

## Repo-Safe Reading

The right current statement is:

```text
Candidate C is a harmonic-mean-based capability in the exact finite family.
The original T188 split is real, but its whole predictive content is already
captured by T*.
```

## What This Changes

- T198 should use `T*` as the main control axis.
- T197 should test whether the harmonic-mean capability is mostly absorbed by
  scheduling / queueing / flow theory.
- If a future family matches `(n, T*)` but still splits, both T193 and T194
  need revision.
