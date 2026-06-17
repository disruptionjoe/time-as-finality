# T14: Finality FLP Impossibility Theorem

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [A1: Distributed Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)

## Origin

BFT/CAP Impossibility and Constructor Theory lenses, idea sprint 2026-06-16.

## Hypothesis

No algorithm can simultaneously maximize all four D1 finality dimensions (accessible support, distinct-holder redundancy, causal branch support, graph reversal count) for a bounded observer under arbitrary message delay — a TaF-specific impossibility theorem in the style of FLP.

FLP proved that no deterministic consensus algorithm can simultaneously guarantee safety (all nodes agree), liveness (all nodes eventually decide), and fault tolerance (one node can fail) in an asynchronous network. TaF's analogous result would ground D1's four-dimensional structure in a computability constraint rather than an empirical observation, showing that the dimensions cannot be collapsed without loss because no algorithm can achieve all four under adversarial timing.

## Setup

1. Formalize the setting: N observer-nodes with bounded record access, asynchronous message passing with arbitrary delay, possible node failures.
2. Define the four optimization targets precisely from D1: maximize accessible supporting records, distinct-holder redundancy, causally independent branch support, and graph reversal count resistance simultaneously.
3. Prove or disprove: there exists a configuration and adversarial message schedule such that any deterministic algorithm fails to achieve all four maxima simultaneously.
4. Identify which pairs of dimensions are jointly achievable and which are not — the impossibility may be partial rather than total.

## Success Criteria

- A formal proof that the four-dimensional maximization is impossible under stated conditions.
- Identification of which D1 dimension combinations are achievable (analogous to: safety+liveness under no faults; safety+fault-tolerance under synchrony; etc.).
- The proof assumptions are stated explicitly so the result is not overgeneralized.

## Failure Criteria

- An algorithm achieves all four maxima simultaneously — identify it and revise D1 or the setup conditions.
- The impossibility is trivial (all four dimensions are in direct conflict by construction) rather than non-trivial (they are in tension because of asynchrony/faults).

## Publication Target

PODC, DISC, or a theoretical computer science journal. Self-contained result requiring no physics commitment.

## Contribution Needed

State the four optimization targets formally. Construct an adversarial execution to break any candidate algorithm. The proof strategy from FLP (consider indistinguishable execution prefixes) is likely the right starting point.
