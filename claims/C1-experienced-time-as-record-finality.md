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
- It has not established a bridge from third-person record finality to
  first-person experience.

The phenomenal bridge is not closed off. It is an open formal target: the
repo may investigate whether the gap is a type gap, complexity separation,
self-reference obstruction, or category-theoretic non-factorability.

## Why It Might Be True

Embedded systems encounter bounded records rather than a God's-eye event
order. T1 demonstrates that record-stabilization frontiers recover causal
precedence where the graph supports it while preserving incomparability for
spacelike-independent records.

T48-T51 strengthen the finite version of this claim by treating
PO1-admissible morphisms as FinaliEvents ordered by record containment, then
showing that finality-axis dominance can reconstruct that order under Axis
Monotonicity. T51 adds the apparent/event distinction: a bounded observer may
see a phantom incomparability that disappears in the observer colimit.

T53 adds an important boundary. A valid colimit is not automatically a unique
canonical event-finality reconstruction. Observer-relative temporal order needs
descent data when multiple observer views are merged.

## How It Could Fail

- Temporal order cannot be reconstructed without primitive time.
- Record formation turns out to be derivative in a way that adds no explanatory value.
- The claim cannot distinguish physical finality from memory, belief, or local access.
- A physics-grounded model makes stabilization order equivalent to ordinary
  causal reachability with no additional explanatory work.

## Tests

- [T1: Record Graph Temporal Reconstruction](../tests/T1-record-graph-temporal-reconstruction.md)
- [T5: Thermodynamic Record Support](../tests/T5-thermodynamic-record-support.md)
- [T48: FinaliEvent Structure](../tests/T48-finali-event-structure.md)
- [T49: Reconstruction Without Background Time](../tests/T49-reconstruction-without-background-time.md)
- [T50: Axis Monotonicity Theorem](../tests/T50-axis-monotonicity-theorem.md)
- [T51: Multi-Observer Apparent Finality Colimit](../tests/T51-multi-observer-apparent-finality-colimit.md)
- [T53: Observer-Colimit Descent Boundary](../tests/T53-observer-colimit-descent-boundary.md)
- [First-Person Finality and Complexity Separation](../open-problems/first-person-finality-complexity-separation.md)
- [Observer Closure Theorem](../open-problems/observer-closure-theorem.md)

## Contribution Needed

Test whether the partial-order result remains nontrivial in a model where
record formation and robustness arise from dynamics rather than being assigned
as graph data. Any renewed claim about experience also needs a separate bridge
from reconciliation to phenomenal succession.

For the phenomenal bridge track, the minimum contribution is not a theory of
consciousness. It is a precise statement of what a third-person record graph
cannot represent, if anything, about first-person finality.

## T1 Result

The v0.1 model reconstructs `A < C` and `B < C` while leaving spacelike `A`
and `B` incomparable. A three-event graph is a counterexample to the stronger
claim that accessible finalized records always determine a total order.

## T53 Result

[T53](../tests/T53-observer-colimit-descent-boundary.md) shows that
partial-order consistency, canonical global completion, and axis-based
reconstruction are distinct properties. The finite audit supports H2, H3, and
H4: compatible completions can remain valid partial orders while observer data
underdetermine event identity, while AM can fail independently of record-order
validity, and while some incompleteness can be repaired by hidden records.

This keeps C1 weakened rather than upgraded. The project can reconstruct
observer-relative partial orders in finite witnesses, but it must not claim
that merged observer views automatically select one canonical history.
