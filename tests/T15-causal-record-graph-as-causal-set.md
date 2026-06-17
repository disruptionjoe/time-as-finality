# T15: Causal Record Graph as Causal Set

## Target Claims

- [C1: Experienced Time as Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [R1: Relativity No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)

## Origin

DAG/Partial-Order Causality lens, idea sprint 2026-06-16.

## Hypothesis

TaF's causal record graph satisfies the axioms of a causal set (locally finite, irreflexive, acyclic, transitively closed). If so, the existing causal-set quantum gravity program is formally running TaF physics in a specific limit, and two decades of causal-set results become available to TaF without re-derivation.

This is not the claim that TaF and causal set theory are the same — TaF adds a finality measure on top of causal structure that causal set theory does not have. But if the underlying graph is a valid causal set, TaF is a finality-semantics extension of a well-established formalism.

## Setup

1. State the causal set axioms precisely: the relation is a strict partial order (irreflexive, transitive) and the order is locally finite (no infinite antichains between any two elements).
2. Check whether T1's causal record graph satisfies each axiom. Identify any violations.
3. If violations exist: determine whether they are artifacts of T1's construction (fixable) or structural differences (informative about where TaF diverges from standard causal sets).
4. Assuming compatibility: identify which causal-set quantum gravity results (Sorkin's entropy formula, causal-set d'Alembertian, sprinkle models) carry over directly to TaF and which require the finality measure to be added.
5. State the converse: what does TaF's finality measure add to a causal set that causal-set theory currently lacks? This is TaF's contribution to the causal-set program.

## Success Criteria

- T1 satisfies all causal set axioms, or the violations are minor and fixable.
- A clear statement of which causal-set results apply directly and which require finality-measure extension.
- At least one result from causal-set theory is translated into TaF language and one TaF result is stated in causal-set language — demonstrating a working bidirectional translation.

## Failure Criteria

- T1 violates a causal set axiom in a way that is not fixable without changing the record-graph construction — identify the violation and determine its implications for C1.
- The finality measure and the causal-set structure are incompatible (e.g., finality requires a total order that causal sets forbid).

## Known Neighbors

- Sorkin's causal set program (1990s–present)
- Bombelli, Lee, Meyer, Sorkin (1987): spacetime as a causal set
- [N1: Known Neighbors](../literature/N1-known-neighbors.md)

## Contribution Needed

Run the axiom check on T1. Write the bidirectional translation. Identify the minimal extension needed to go from a bare causal set to a causal set with TaF finality semantics.
