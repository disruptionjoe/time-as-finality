# Finality as Anomaly Cancellation

## Problem

Does distinct-holder redundancy — D1's second dimension — map onto an anomaly cancellation condition in a field-theoretic or lattice-theoretic setting, such that under-finalized states are anomalous (forbidden in the infrared theory) rather than merely unstable?

## Working Claim

In gauge theories, 't Hooft anomaly matching requires that the number of charged species satisfies a consistency condition. States that violate the matching condition are anomalous and do not appear in the physical spectrum of the infrared theory — they are not merely suppressed, they are structurally forbidden.

The Lattice QFT/Anomaly Theorist lens in the 2026-06-16 idea sprint proposed that distinct-holder redundancy may function analogously: a record configuration is finalized only if the number of independent record-holders satisfies a consistency condition analogous to 't Hooft anomaly matching. Under-finalized states would then be anomalous — forbidden in the IR theory by a structural constraint rather than excluded by a dynamical process.

## Why It Matters

This would be a significant result if it holds: it would mean that the classical world is not merely the high-decoherence limit of quantum mechanics, but the anomaly-free sector of a theory with finality structure. Classical objectivity would be protected by symmetry in the field-theoretic sense, not just by environmental suppression of interference.

It would also connect TaF to the anomaly cancellation literature in a way that is independently checkable by lattice QFT specialists, without requiring them to accept the full TaF framework.

## How It Could Mislead

- Anomaly cancellation in gauge theories is a property of the UV theory, not the IR. Finality is an IR concept. The mapping must bridge this gap explicitly.
- 't Hooft anomaly matching is a precise technical constraint; calling D1's redundancy dimension "anomaly-like" without showing the formal equivalence is only a suggestive analogy.
- The holder-count condition must be shown to transform correctly under gauge transformations. [T111: D1 Gauge-Invariance Audit](../tests/T111-d1-gauge-invariance-audit.md) shows distinct-holder redundancy is invariant under pure relabeling maps and covariant under access-boundary changes. That is an entry condition, not yet an anomaly coefficient.

## Formal Entry Points

1. **Lattice check:** On a finite lattice, define a "finality charge" for each record configuration as the number of distinct record-holders exceeding a threshold. Ask whether the finality charge must satisfy a mod-N consistency condition (analogous to anomaly cancellation mod N in lattice gauge theories).
2. **Continuum limit:** Ask whether the observer-certification step in TaF introduces a lattice-discretization artifact when taking the continuum limit — specifically whether the grain size of the observer (D2's recorder capability level) must be renormalized.
3. **IR constraint:** Ask whether the IR theory (classical records, high-redundancy regime) has a different field content than the UV theory (under-finalized quantum states) in a way that is consistent with decoupling theorems in QFT.

## Connection to Existing Claims and Tests

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [T10: Finality Superselection Rule](../tests/T10-finality-superselection-rule.md)
- [N1: Known Neighbors](../literature/N1-known-neighbors.md)

## Contribution Needed

Using T111 as the invariance gate, state the anomaly matching condition precisely for a simple model (e.g., a U(1) gauge theory on a 2D lattice with finality-structured matter fields). Check whether the under-finalized sector carries a nonzero anomaly coefficient. A positive result would be a clean, publishable result in lattice QFT that is independently verifiable.
