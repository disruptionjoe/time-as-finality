# C1: Experienced Time As Record Finality

## Claim

The stabilization frontiers of records available to an embedded reconciler can
reconstruct an observer-relative partial temporal order. This formal result
does not by itself explain phenomenal temporal experience or guarantee a total
sequence.

## Class

Core claim.

## Status

Weakened.

## What This Does Not Claim

- It does not replace coordinate time, proper time, relativity, or thermodynamics.
- It does not claim that records create all physical reality.
- It does not claim that human memory is perfect or that observer access only grows.
- It does not identify a graph traversal order with experienced succession.

## Why It Might Be True

Embedded systems encounter bounded records rather than a God's-eye event
order. T1 demonstrates that record-stabilization frontiers recover causal
precedence where the graph supports it while preserving incomparability for
spacelike-independent records.

## How It Could Fail

- Temporal order cannot be reconstructed without primitive time.
- Record formation turns out to be derivative in a way that adds no explanatory value.
- The claim cannot distinguish physical finality from memory, belief, or local access.
- A physics-grounded model makes stabilization order equivalent to ordinary
  causal reachability with no additional explanatory work.

## Tests

- [T1: Record Graph Temporal Reconstruction](../tests/T1-record-graph-temporal-reconstruction.md)
- [T5: Thermodynamic Record Support](../tests/T5-thermodynamic-record-support.md)

## Contribution Needed

Test whether the partial-order result remains nontrivial in a model where
record formation and robustness arise from dynamics rather than being assigned
as graph data. Any renewed claim about experience also needs a separate bridge
from reconciliation to phenomenal succession.

## T1 Result

The v0.1 model reconstructs `A < C` and `B < C` while leaving spacelike `A`
and `B` incomparable. A three-event graph is a counterexample to the stronger
claim that accessible finalized records always determine a total order.
