# T518: Quantum-Darwinism Redundancy <-> Replication-Factor Bridge

## Target Claims

No claim-ledger target. Attacks prospecting corner 1 (strongest unbuilt lead) of
`explorations/lane-status-and-adjacent-space-prospecting-2026-07-09.md`.

## Setup

Zurek's quantum Darwinism already speaks in distributed-systems terms (redundant
copies proliferate; the environment is a channel; many observers reach consensus
by reading fragments), but the searched literature does not draw the
quantitative correspondence. T518 builds a finite executable version of both
sides.

- QD: system qubit `|+>`, `N = 8` environment qubits each an imperfect copy via
  controlled `Ry(theta)`. Exact partial information `I(S:F)`; redundancy
  `R_delta = N/f_delta` with `f_delta` the smallest fragment reaching
  `(1-delta) H(S)`.
- DS image: N replicas; `R_delta` disjoint quorums each reconstruct the value to
  staleness `delta`; the record survives losing all but one sufficient quorum.

## Success Criteria

- Sanity: `H(S) ~ 1`; perfect copies give `I(S:1 qubit) = 1`.
- A redundancy plateau exists and falls monotonically as copy quality drops.
- Honest test: `R_delta` is not `delta`-invariant (so it is not yet a
  well-defined replication factor).

## Verdict

`STRUCTURAL_CORRESPONDENCE_CONFIRMED_QUANTITATIVE_BRIDGE_OPEN`. The redundancy
plateau maps structurally to eventual-consistency replication (more than
vocabulary), but the quantitative map `R_delta = replication factor` is unbuilt
(no shared dimensionless invariant). Deprioritized with a wake condition (find an
invariant both sides compute identically). Model:
`models/quantum_darwinism_replication_bridge.py`;
tests: `tests/test_quantum_darwinism_replication_bridge.py`;
results: `results/T518-quantum-darwinism-replication-bridge-v0.1-results.md`.
