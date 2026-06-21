# Record Finality On A Finite Causal Graph

## Abstract

This note tests a narrow version of the Time as Finality proposal: whether an
embedded record-processing system can reconstruct temporal order from causal
record structure without taking metric time, global simultaneity, or a total
event order as input. We define an observer-indexed componentwise finality
preorder over accessible support, holder redundancy, causal branch
independence, and graph reversal count. An executable finite-DAG model
reconstructs causal precedence among stabilization frontiers, distinguishes
local access loss from record erasure, and preserves spacelike
incomparability across topological traversals. A minimal three-event
counterexample refutes the stronger claim that finalized records generally
determine a total order. A reversal benchmark also shows that graph deletion
count does not determine an assigned erasure-cost proxy. The result is a
nontrivial toy formalism and limiting result, not a theory of physical or
phenomenal time.

## 1. Question

The motivating conjecture was that experienced time is the order in which
records become final for an embedded observer. That sentence combines three
questions:

1. Can record structure reconstruct any temporal order without using a hidden
   global clock?
2. Does a multi-dimensional finality relation add information beyond causal
   reachability or redundancy alone?
3. Does the result explain experienced temporal succession?

The v0.1 model addresses the first question, creates a benchmark for the
second, and does not answer the third.

## 2. Formal Object

The complete contract is in [FORMALISM.md](FORMALISM.md). The model takes a
finite causal partial order, record-bearing systems, record tokens, bounded
observer access, and a fixed reconstruction threshold as primitives.

For proposition-value pair `x`, observer `O`, and evaluation event `e`:

```text
F_O,e(x) = (accessible support,
            distinct-holder redundancy,
            causal-antichain branch support,
            graph reversal count)
```

Finality is componentwise comparison. No weighted scalar is used. The
stabilization frontier of a proposition is the set of causally minimal events
where one value uniquely reaches threshold.

## 3. Executable Test

The standard-library implementation is in
[`models/t1_record_graph.py`](models/t1_record_graph.py). Run:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t1
```

The ten tests cover:

- preorder reflexivity and transitivity;
- profile equivalence and genuine incomparability;
- sequential reconstruction;
- spacelike-independent records;
- traversal invariance;
- local access loss;
- physical erasure;
- finality equivalence and incomparability;
- graph-cost versus erasure-cost divergence;
- conflicting threshold values.

Detailed output and interpretation are in
[T1 v0.1 Results](results/T1-v0.1-results.md).

## 4. Result

The reference graph produces:

```text
A < C
B < C
A || B
```

This is not merely a chosen topological ordering. `A || B` remains invariant
under every valid traversal. The model therefore reconstructs a partial order
where the causal record graph warrants one and refuses a total order where it
does not.

The result is nontrivial in a limited sense: the stabilization threshold and
record distribution determine when a proposition enters the reconstructed
relation, while causal ancestry constrains which frontiers can precede which.
However, the model does not derive causal order. It takes the causal partial
order as primitive.

## 5. Counterexample And Claim Revision

Two independent formation events feeding one observation event form a
three-event counterexample to total reconstruction. Both propositions are
accessible and finalized at threshold one, but neither causally precedes the
other.

Accordingly, C1 is weakened. The supported claim is:

> An embedded reconciler can recover an observer-relative temporal partial
> order from accessible record-stabilization frontiers.

The unsupported stronger claims are:

- record finality always determines a total order;
- the reconstructed partial order is phenomenal temporal experience;
- record finality replaces proper time, coordinate time, or spacetime
  geometry.

## 6. Reversal Cost

Graph reversal count asks how many accessible records must be removed to put a
proposition below threshold. The erasure-cost proxy sums the cheapest assigned
costs for the same operation.

The reference propositions all require one graph deletion, but have proxy
costs `1.0`, `2.0`, and `0.5`. The quantities therefore do not collapse into
one another in the toy model.

This is not yet a Landauer calculation. A physical claim requires a concrete
memory substrate, temperature, dynamics, and erasure protocol. The present
result only establishes that topology and physical cost should not be
conflated by definition.

## 7. Prior Art And Remaining Delta

The closest primary-source neighbors are documented in
[N3](literature/N3-core-formalism-known-neighbors.md).

- Lamport already establishes causal partial order and the danger of imposing
  total order on independent events.
- Quantum Darwinism already connects redundant environmental records with
  effective objectivity.
- Hartle and Gell-Mann already model information gathering and utilizing
  systems and observer-relative temporal categories.
- Halliwell already connects records with decoherent histories.
- Landauer already constrains any move from logical erasure to physical cost.

The candidate delta is therefore not any ingredient. It is the packaging of
an observer-indexed multi-dimensional record-finality preorder with
stabilization-frontier reconstruction and explicit incomparability.

## 8. Verdict

The framework currently demonstrates **nontrivial toy-model content**, with
two major qualifications:

1. it survives as a partial-order reconstruction framework, not a total theory
   of time;
2. its physical novelty is unproven until the graph quantities are derived
   from a named dynamical model and compared directly with established
   records/decoherence formalisms.

It is more than vocabulary inside the finite model because it generates
checkable profiles, invariant reconstruction results, and a counterexample.
It is not yet evidence for new physics or an explanation of conscious
temporal experience.

## 9. Next Decisive Experiment

Implement the same preorder on a small system-apparatus-environment model and
compare it with quantum-Darwinism redundancy. The decisive question is
whether bounded accessibility, branch support, or reversal structure changes
any conclusion that redundancy and decoherence do not already provide. If
not, D1 should be weakened again to an interdisciplinary vocabulary layer.
