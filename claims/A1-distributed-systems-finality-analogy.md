# A1: Distributed-Systems Finality Analogy

## Claim

Distributed-systems finality provides useful bridge language for candidate states becoming committed states.

## Class

Analogy.

## Status

Active.

## What This Does Not Claim

- The universe is not claimed to be a blockchain.
- Relativity is not reduced to database replication.
- Physical finality should be defined as record-stability before importing distributed-systems language.

## Why It Might Be Useful

Distributed systems distinguish local views, message propagation, pending states, forks, quorums, probabilistic finality, deterministic finality, and commit order. Those distinctions help discuss quantum/classical transition, relativity of simultaneity, and black-hole causal access without assuming one global state visible to all observers.

Avalanche / Snowball style protocols add a narrower analogy: finality can emerge from repeated bounded local sampling, confidence accumulation, and metastable convergence. That is useful for modeling observer-relative record finality because an observer-system may not inspect every record directly. It may sample accessible fragments until reversal becomes negligible for the domain.

The safe abstraction is:

```text
local record samples
  -> confidence update
  -> metastable convergence
  -> observer-relative finality
  -> reversal-cost estimate
```

## How It Could Mislead

- Distributed systems usually presuppose time and protocol steps.
- Consensus mechanisms are engineered; physical systems are not necessarily protocol-governed.
- The analogy can tempt readers into thinking "commit order" is literal.
- Probabilistic protocol finality can be mistaken for absolute truth.
- Avalanche / Snowball language can mislead readers into thinking physics literally runs a consensus protocol.

## Tests

- [T1: Record Graph Temporal Reconstruction](../tests/T1-record-graph-temporal-reconstruction.md)
- [T3: Spacelike Events And No Global Commit Order](../tests/T3-spacelike-events-no-global-commit-order.md)
- [T6: Snowball Record Finality](../tests/T6-snowball-record-finality.md)
- [T17: Consensus Finality Crosswalk](../tests/T17-consensus-finality-crosswalk.md)

## Contribution Needed

Map which distributed-systems concepts are safe analogies and which should be avoided. Start with Avalanche / Snowball as a bounded toy model of probabilistic confidence accumulation, not as a literal physics claim.

## T17 Result

[T17](../tests/T17-consensus-finality-crosswalk.md) makes the analogy
explicit. Safety, liveness, and economic finality are modeled as collapses or
projections of D1-style record finality. The bounded search also finds cases
where standard distributed summaries agree while D1 profiles differ.

The follow-on theorem check verifies, within the stated finite asynchronous
model, that no admissible configuration simultaneously maximizes all D1
dimensions and bounded progress. That makes A1 stronger than a metaphor while
keeping liveness as a protocol-side condition rather than a D1 dimension.

This strengthens A1 as a formal analogy, not as a claim that physics literally
runs a consensus protocol.

## T20 Result

[T20](../tests/T20-consensus-record-theorem-transfer.md) tests the stronger
claim that theorem structure can transfer across the analogy. Quorum
intersection safety transfers into physical-record finality as a
redundant-holder overlap theorem: if `2q > n` and local holders are
consistent, two incompatible classical records cannot both be finalized.

T20 also narrows A1. Weak quorum breaks the transfer, and T13-style
global-section questions are not solved by quorum safety. The analogy is
theorem-bearing in one checked case, but it is not total.
