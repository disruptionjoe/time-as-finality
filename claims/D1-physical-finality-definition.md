# D1: Physical Finality Definition

## Claim

Physical finality is a stability relation among records. A state is more final for an observer-network when it is redundantly encoded, causally accessible, robust under later compatible observations, and costly to reverse across the correlated record network.

## Class

Definition.

## Status

Open.

## What This Does Not Claim

- Finality is not absolute metaphysical impossibility.
- Finality is not a magic moment in time.
- Finality is not social agreement.

## Why It Might Be True

Classical records differ by redundancy, accessibility, stability, and reversal cost. These dimensions distinguish fragile private memories, laboratory measurements, environmental decoherence traces, public records, fossils, and macroscopic object persistence.

## How It Could Fail

- The four dimensions are insufficient or redundant.
- "Reversal cost" cannot be defined without circularly invoking time.
- Finality becomes too broad and merely renames entropy, decoherence, or information.

## Tests

- [T1: Record Graph Temporal Reconstruction](../tests/T1-record-graph-temporal-reconstruction.md)
- [T5: Thermodynamic Record Support](../tests/T5-thermodynamic-record-support.md)

## Contribution Needed

Propose a formal finality preorder or metric over a finite causal record graph.
