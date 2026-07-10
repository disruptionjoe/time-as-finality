# T519 Results -- QD redundancy / replication invariant gate

**Verdict:** `CRASH_TRANSLATION_ONLY_BYZANTINE_INVARIANT_FAILS`
**Model:** `models/quantum_darwinism_replication_invariant_gate.py`
**Attacks:** T518 wake condition: candidate shared invariant `1 - f_delta/N`.

## Result

The candidate information-deficit invariant

```text
D_delta = 1 - f_delta / N
```

is not the discovery-level quantitative bridge T518 needed.

It matches a distributed crash-survival fraction only after importing the QD
fragment size as the DS quorum size:

```text
q = f_delta
crash survival = (N - q) / N = 1 - f_delta / N
```

That is a translation identity, not an independent prediction.

## Failure Against Byzantine Quorums

For `N = 8` and a predeclared `f = 2` Byzantine fault model, the minimum
pairwise-honest-intersection quorum is `q = 6`, so the survival fraction is
`(8 - 6) / 8 = 0.25`.

The QD rows do not share that invariant. Perfect copies give
`D_delta = 0.875`, which would badly overstate Byzantine tolerance if read as
the same number.

## Verdict

T518 remains correct as a structural bridge: QD objectivity and distributed
replication both use redundant independent access. But the proposed numerical
bridge fails:

- `D_delta` is delta-sensitive for fixed physics;
- crash-model agreement is tautological once `q = f_delta` is imported;
- Byzantine quorum-intersection does not compute the same invariant.

The quantitative bridge remains open only for a new invariant that survives a
predeclared DS failure model rather than adapting the DS model after the QD
threshold is known.
