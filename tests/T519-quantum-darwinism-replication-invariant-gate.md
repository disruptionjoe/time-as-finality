# T519: Quantum-Darwinism / Replication Invariant Gate

## Target Claims

No claim-ledger target. Attacks T518's wake condition: test whether the
candidate dimensionless invariant `1 - f_delta/N` converts the structural
quantum-Darwinism redundancy / distributed-replication bridge into a quantitative
discovery.

## Setup

Reuse the T518 finite QD branching model. Compute `f_delta` exactly by averaging
over all same-size environment fragments. Compare the candidate
`D_delta = 1 - f_delta/N` against two distributed readings:

- crash-quorum survival, with quorum size `q`;
- Byzantine quorum-intersection survival, where pairwise quorums must intersect
  in more than the tolerated faulty nodes.

## Success Criteria

- If `D_delta` is a real shared invariant, it should survive a predeclared DS
  failure model rather than only restating `q = f_delta`.
- The gate should preserve the structural T518 bridge while blocking numerical
  overread if the invariant fails.

## Verdict

`CRASH_TRANSLATION_ONLY_BYZANTINE_INVARIANT_FAILS`. `D_delta` matches crash
survival exactly only when the DS quorum size is stipulated as `q = f_delta`.
It is delta-sensitive for fixed physics and fails the Byzantine
quorum-intersection reading. T518 remains a structural correspondence, not a
quantitative discovery. Model:
`models/quantum_darwinism_replication_invariant_gate.py`; tests:
`tests/test_quantum_darwinism_replication_invariant_gate.py`; results:
`results/T519-quantum-darwinism-replication-invariant-gate-v0.1-results.md`.
