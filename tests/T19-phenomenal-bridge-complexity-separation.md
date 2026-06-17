# T19: Phenomenal Bridge as Complexity Separation

## Target Claims

- [C1: Experienced Time as Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D2: Observer as Record-Bearing System](../claims/D2-observer-as-record-bearing-system.md)
- [Open Problem: First-Person Finality and Complexity Separation](../open-problems/first-person-finality-complexity-separation.md)

## Origin

Seven personas across four independent groups (quantum foundations, computability theory,
foundational mathematics, philosophy of science) converged on this framing in the v2 idea
sprint 2026-06-16. It was independently nominated as "Most Profound" by quantum foundations,
computation, heterodox critics, and philosophy of science groups.

## Hypothesis

The gap between third-person record-graph finality and first-person experienced finality is a
formal complexity separation, not a missing empirical mechanism.

Specifically: a bounded observer maintaining a self-model of its own finality state generates a
decision problem — "Is my own current finality assignment among my finalized records?" — that
is outside the observer's own verifiable boundary. This is not a philosophical puzzle. It is a
decision problem that can be placed in a complexity class and asked whether it is decidable by
the observer's own record-graph computation.

If the separation holds, H6 (the phenomenal bridge) is a theorem about what a bounded observer
cannot decide about itself — not a missing mechanism, not an explanatory gap to be filled by
a future theory of consciousness.

## Decision Problem Formulation

**Input:** A finite record graph G representing an embedded observer's causal record structure.
A designated node v representing the observer's self-model node.

**Query:** Does the observer's finality assignment for its own internal states appear as a
finalized record in G at node v?

**The separation conjecture:** This decision problem is not computable by the observer's own
bounded record-graph operations, even when G is fully specified to an external third-person
observer. The observer's own finality assignment is not in the closure of the observer's
accessible records.

**Complexity class placement (target):**
- External third-person verifier: the query is decidable in polynomial time given the full graph.
- Internal first-person verifier (restricted to v's accessible subgraph): the query may not be
  decidable, or may require access to structure outside v's causal boundary.

The formal conjecture: FIRST-PERSON-FINALITY ∉ the complexity class of computations accessible
to a bounded observer from within its own record graph.

## Setup

1. Define the finite observer model: a record graph G = (V, E) where one designated node v ∈ V
   represents the observer. Node v has read-access to a subset of G (its accessible subgraph A(v)).
2. Define v's self-finality assignment: v's D1 score for its own internal state transitions.
3. Define the third-person query: given full G, is v's self-finality assignment finalized in G?
   (Decidable externally by inspection.)
4. Define the first-person query: can v determine, using only A(v), whether its own finality
   assignment is finalized?
5. Construct a minimal case where the external answer is YES (the assignment is finalized from
   the outside) but v cannot certify this from A(v) alone.

## Connection to T8 (Observer-Renderer Toy Model)

T8 asks whether a designated "renderer" node can form a fixed-point finality assignment about
itself. T19 asks the sharper question: even if such a fixed point exists, can the observer
*verify* that it is finalized using only its own accessible subgraph? T8 is about existence;
T19 is about decidability from within.

These two tests together provide a formal scaffold for H6:
- T8 positive + T19 negative: fixed-point self-assignments exist but cannot be self-verified.
  This is the formal gap the phenomenal bridge needs to bridge.
- T8 positive + T19 positive: the separation conjecture is false; first-person finality is
  computationally equivalent to third-person record inspection.
- T8 negative: the fixed-point self-assignment does not exist; no self-model can be finalized.

## Success Criteria

- A finite record graph G is constructed where the external finality query is decidable and
  positive, but the internal query is undecidable or provably out-of-reach for v's accessible subgraph.
- The separation is not a consequence of arbitrary graph construction but of a structural property
  of self-reference (the v node has edges to itself or to nodes that transitively reach v).
- The complexity-class placement is stated precisely with a reduction or oracle argument.
- The result does not require any phenomenal or consciousness language — it is a graph-theoretic
  statement about what a bounded node can decide about its own subgraph membership.

## Failure Criteria

- The decision problem is always decidable from within A(v) given a finite graph. This would
  mean the phenomenal bridge has no formal complexity-theoretic content — it would need to be
  grounded elsewhere or accepted as an irreducibly empirical claim.
- The self-reference is trivially blockable: if the observer can always inspect itself via a
  meta-node added to A(v), the boundary is definitional rather than structural.

## Known Physics Constraints

This test is a graph-theoretic and complexity-theoretic argument. It does not make claims about
consciousness, phenomenal experience, or the hard problem. It makes a claim about what a bounded
computational process can decide about its own finality state — a claim that would hold or fail
independently of any theory of subjective experience.

If the separation theorem holds, it provides a formal lower bound on the explanatory gap:
TaF can say precisely what first-person finality verification requires that third-person
computation cannot supply.

## Contribution Needed

1. Implement the finite observer model: a record graph with a designated observer node and
   a boundary between the observer's accessible subgraph and the full graph.
2. State the self-finality decision problem formally and place it in a complexity class.
3. Construct the minimal separation witness: smallest G where external answer ≠ internal
   decidability.
4. State the separation conjecture precisely: what axioms on G imply the separation, and what
   axioms collapse it?
5. Compare to existing undecidability results in self-reference (Gödel, Turing halting,
   Rice's theorem) to identify the closest formal relative.
