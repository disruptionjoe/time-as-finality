# T518 Results -- quantum-Darwinism redundancy <-> replication-factor bridge

**Verdict:** `STRUCTURAL_CORRESPONDENCE_CONFIRMED_QUANTITATIVE_BRIDGE_OPEN`
**Model:** `models/quantum_darwinism_replication_bridge.py` (exit 0, 5/5 checks)
**Attacks:** prospecting corner 1 (strongest unbuilt lead) of
`explorations/lane-status-and-adjacent-space-prospecting-2026-07-09.md`.

## What was built

A finite, executable version of **both sides**:

- **QD side (standard branching model):** system qubit `|+>`, `N = 8`
  environment qubits, each an imperfect copy via a controlled `Ry(theta)`
  (`theta = pi` = perfect copy). Global pure state
  `|Psi> = (|0>_S|0..0> + |1>_S|phi..phi>)/sqrt2`. Partial information `I(S:F)`
  is computed **exactly** for fragments of each size; redundancy
  `R_delta = N / f_delta`, where `f_delta` is the smallest fragment size
  reaching `(1-delta) H(S)`.
- **DS image:** N replicas; each holds the pointer with quality `theta`;
  `R_delta` disjoint quorums each reconstruct the value to staleness `delta`;
  the record survives losing all but one sufficient quorum.

## Redundancy plateau (delta = 0.1, N = 8)

| copy quality theta | f_delta | R_delta |
|---|---|---|
| 1.00 pi (perfect) | 1 | 8.0 |
| 0.60 pi | 2 | 4.0 |
| 0.35 pi | 4 | 2.0 |
| 0.20 pi | 4 | 2.0 |

High-quality copies give a large redundancy plateau (`R >= N/2`); redundancy
falls monotonically as copy quality drops. Sanity: with perfect copies a single
fragment qubit already carries the full classical bit (`I(S:1) = 1.0`).

## The honest quantitative test

Fixed physics (`theta = 0.6 pi`): `delta = 0.05 -> R = 2.67` (f=3);
`delta = 0.20 -> R = 4.0` (f=2). **`R_delta` is not delta-invariant**, so it is
not yet a well-defined "replication factor."

## Verdict -- confirmed correspondence, not yet a discovery

- **Structural match is real and non-trivial.** The redundancy plateau (many
  disjoint fragments each *independently* sufficient) is exactly the
  eventual-consistency replication property (any read quorum reconstructs the
  value; the record survives losing all but one quorum). Both are "objectivity
  via redundant independent access" -- more than vocabulary.
- **Quantitative bridge is unbuilt.** `R_delta` depends on `delta`; the DS
  replication factor depends on the failure model (crash vs Byzantine) and the
  quorum-intersection rule. No shared dimensionless invariant computes the same
  number on both sides yet.

## Wake condition (deprioritize, do not close)

Find a dimensionless invariant -- candidate: the information deficit
`1 - f_delta/N` vs a quorum-intersection redundancy -- that both sides compute
identically. If it exists, the bridge converts from analogy to discovery.
