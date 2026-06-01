# T1: Record Graph Temporal Reconstruction

## Target Claims

- [C1: Experienced Time As Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D2: Observer As Record-Bearing System](../claims/D2-observer-as-record-bearing-system.md)

## Setup

Build a finite directed causal record graph:

- nodes are record-bearing systems;
- edges are record-transfer relations;
- propositions have local records distributed across nodes;
- observer-system `O` has access to a causally bounded subgraph.

Define a finality score or preorder for proposition `p` relative to `O` using:

- redundancy;
- stability;
- reversal cost;
- causal reachability.

## Success Criteria

- The observer-relative temporal order can be reconstructed from the causal partial order plus finality stabilization profile.
- The model distinguishes record formation, local access, and physical reversal.
- The model does not assume a global clock or hidden universal present.

## Failure Criteria

- The reconstruction requires primitive time in disguise.
- The finality function is arbitrary or uninformative.
- The graph cannot represent loss of local access vs physical reversal.
- The model cannot handle spacelike-independent records.

## Contribution Needed

Create the smallest nontrivial toy graph and show what the reconstruction returns.
