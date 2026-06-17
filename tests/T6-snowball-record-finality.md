# T6: Snowball Record Finality

## Target Claims

- [A1: Distributed-Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)

## Setup

Build a toy model where an observer-system does not inspect every record directly. Instead, it repeatedly samples accessible record fragments and updates confidence in a candidate proposition.

The model should include:

- a population of record-bearing systems;
- at least two candidate propositions or histories;
- a causal accessibility relation limiting which records can be sampled;
- a sampling rule analogous to Snowball parameters such as sample size, quorum threshold, and confidence threshold;
- a finality score that increases when repeated samples reinforce the same candidate state;
- a reversal-cost estimate after finality is reached.

## Success Criteria

- The test shows how repeated local sampling can produce probabilistic finality without requiring a global observer.
- The finality score is defined in terms of record stability, redundancy, accessibility, and reversal cost, not primitive time.
- The model distinguishes truth, local confidence, and protocol finality.
- The model can express metastability before convergence.
- The model preserves no-signalling if applied to quantum measurement records.

## Failure Criteria

- The model treats the universe as literally running Avalanche, Snowball, or a blockchain.
- The finality threshold is arbitrary and adds no clarity beyond ordinary redundancy language.
- The model requires a hidden global commit order.
- The model implies faster-than-light finality transfer.
- The model treats probabilistic protocol finality as absolute truth.

## Known Physics Constraints

- Quantum entanglement is not usable faster-than-light communication.
- Decoherence is not by itself a full solution to the measurement problem.
- Relativity forbids a universal global present or globally available commit order.
- Physical record-stability must remain distinct from social agreement.

## Contribution Needed

Write a finite-record toy example comparing:

```text
local record samples
  -> confidence update
  -> metastable convergence
  -> observer-relative finality
  -> reversal-cost estimate
```

Then compare the result to a simple quantum measurement scenario with two observers who can only reconcile records after causal contact.
