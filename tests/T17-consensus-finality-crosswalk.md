# T17: Consensus Finality Crosswalk

## Target Claims

- [A1: Distributed Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)

## Origin

Direction 1 from the 42-persona convergence map: distributed consensus and
physical record formation share a formal problem.

## Setup

Model a bounded family of protocol configurations:

```text
(nodes, quorum, branches, confirmations, timeout)
```

For each configuration, compute:

- D1 vector: accessible support, holder redundancy, branch support, reversal
  cost;
- safety finality: whether the accessible quorum is majority-safe;
- liveness under bounded adversarial delay;
- economic finality: reversal cost only.

The lab then searches for:

1. collapse maps from distributed finality definitions into D1 dimensions;
2. divergence witnesses where standard distributed summaries agree but D1
   differs;
3. a bounded impossibility witness where no admissible configuration
   simultaneously maximizes all D1 dimensions;
4. an executable bounded theorem check where no admissible configuration
   simultaneously maximizes all D1 dimensions and bounded progress.

## Success Criteria

- Safety, liveness, and economic finality are mapped as explicit D1 collapses
  or non-D1 protocol conditions.
- At least one witness shows D1 distinguishes cases that a standard
  distributed summary collapses.
- The bounded search produces a Pareto frontier rather than one configuration
  maximizing all D1 dimensions.
- The theorem check declares its assumptions and returns no joint maximizer
  for D1 dimensions plus bounded progress.
- The result preserves the guardrail that physics is not reduced to a
  consensus protocol.

## Failure Criteria

- D1 adds no distinction beyond safety/liveness/economic finality.
- The bounded search finds one configuration maximizing every D1 dimension.
- The theorem check finds one configuration maximizing every D1 dimension and
  bounded progress under the stated assumptions.
- The model treats protocol confidence as truth.
- The result claims physical systems literally run distributed protocols.

## Known Constraints

This is a finite protocol analogy and crosswalk. It is not a physical theory,
not an FLP proof, and not a claim that consensus creates facts.

## Contribution Needed

Generalize the bounded theorem check into a parameterized result. State which
resource-budget families preserve the tradeoff and which added protocol
features break it.

## T20 Follow-On

[T20](T20-consensus-record-theorem-transfer.md) tests a stronger bridge:
whether a distributed-systems theorem transfers into physical-record finality
without changing proof structure. The first positive transfer is quorum
intersection safety mapped to redundant-holder overlap. The first boundary is
also explicit: quorum safety does not prove T13-style global-section
existence.
