# A1: Distributed-Systems Finality Analogy

## Claim

Distributed-systems finality provides useful bridge language for candidate states becoming committed states.

## Class

Analogy.

## Status

Revised.

## What This Does Not Claim

- The universe is not claimed to be a blockchain.
- Relativity is not reduced to database replication.
- Physical finality should be defined as record-stability before importing distributed-systems language.

## Why It Might Be Useful

Distributed systems distinguish local views, message propagation, pending states, forks, quorums, probabilistic finality, deterministic finality, and commit order. Those distinctions help discuss quantum/classical transition, relativity of simultaneity, and black-hole causal access without assuming one global state visible to all observers.

T10 shows one precise use. Repeated bounded sampling can turn individually
verified records into a metastable network decision while making sampling,
quorum, confidence, and liveness assumptions explicit.

The result is limited. Against forged opposition, proof-carrying Snowball
substantially outperforms raw Snowball. Against valid conflicting records,
proof verification provides no advantage and confidence dynamics can amplify
the wrong majority. A verified Bayesian/majority baseline matches or exceeds
Snowball truth accuracy in every reported configuration.

T14 preserves this limit inside the integrated observer-context pipeline.
Proof-carrying Snowball reduces forged false finality in the probe, but valid
dissent still passes verification and can drive false consensus.

T15 preserves the same distinction in a generated family. Forged records are
rejected whenever proof filtering is required, while valid dissent remains
visible in every generated dissent case.

## How It Could Mislead

- Distributed systems usually presuppose time and protocol steps.
- Consensus mechanisms are engineered; physical systems are not necessarily protocol-governed.
- The analogy can tempt readers into thinking "commit order" is literal.
- Confidence accumulation can be mistaken for evidence creation.
- Protocol agreement can be mistaken for truth.
- Protocol metastability can be mistaken for a thermodynamic barrier.

## Tests

- [T1: Record Graph Temporal Reconstruction](../tests/T1-record-graph-temporal-reconstruction.md)
- [T3: Spacelike Events And No Global Commit Order](../tests/T3-spacelike-events-no-global-commit-order.md)
- [T10: Proof-Carrying Metastable Finality](../tests/T10-proof-carrying-metastable-finality.md)
- [T14: Integrated Observer-Context Finality](../tests/T14-integrated-observer-context-finality.md)
- [T15: Generated Integrated Finality Stress Lab](../tests/T15-generated-integrated-finality-stress.md)

## Contribution Needed

Test stale but valid certificates and changing hidden states. Determine whether
epoching and revocation can preserve correction without destroying the
bounded-access benefit.
