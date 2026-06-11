# Evidence Joins, Inherited Context, And The Failure Of A Finality Semilattice

## Abstract

Time as Finality has so far studied record reconstruction, dynamically
generated traces, and proof-carrying metastable consensus. T11 asks whether
finality itself composes across scales.

The model represents record systems as recursively nested structures of
immutable provenance-bearing tokens and inherited expression marks.
Compatible evidence states merge by set union and satisfy the
join-semilattice laws. The observer-facing finality profile does not inherit
that algebra. Across all 225 ordered pairs generated from four supporting
sources, transparent merge is monotone, but the merged profile equals the
componentwise least upper bound in only 51.11% of pairs. Conflict can destroy
a previously local decision, coarse-graining can change profile ordering, and
local consistency need not glue into a global assignment.

An operational epigenetic layer adds inherited, context-dependent expression
without changing stored record identity. It makes hierarchy placement matter
while allowing later reprogramming. The result supports a typed compositional
pipeline, not a universal or fractal algebra of finality.

## 1. The Strong Conjecture

The original compositional intuition was:

> Finalized subgraphs become stable objects for higher-level systems, and
> finality itself combines through a join.

If true at the profile level, the D1 preorder might form a graded
join-semilattice under record merge. That would provide one algebra for the
fact-ladder from observation to institutional record.

T11 rejects that unrestricted version.

## 2. The Typed Pipeline

The experiment separates:

```text
stored evidence E
  -> expression X_k(E)
  -> observer projection A_O(X_k(E))
  -> finality profile F
  -> threshold decision D
```

`k` is inherited context. Treating `E`, `X`, `A`, `F`, and `D` as one object
would manufacture composition by definition.

## 3. Evidence Join

A token contains:

- stable token identity;
- unique source provenance;
- proposition and value;
- holder and causal branch labels;
- reversal cost;
- optional expression tags and local assignments.

Evidence states merge by compatible token identity. The operation is
associative, commutative, and idempotent. Duplicate delivery therefore does
not create new evidence.

This is a real semilattice, but it belongs to evidence state, not finality
profile.

## 4. Why Profiles Do Not Form The Same Join

For one proposition-value pair, T11 computes:

```text
F = (unique provenance, holders, branches, minimum reversal cost)
```

Two independent one-record profiles are each `(1,1,1,1)`. Their
componentwise least upper bound is also `(1,1,1,1)`. Physically merging the
records produces `(2,2,2,2)`.

The merge is an upper bound, but not the least upper bound in profile space.
It contains additional structure created by aggregation.

The exhaustive four-source sweep confirms this is structural:

- profile monotonicity under transparent merge: `100%`;
- profile merge equal to componentwise LUB: `51.11%`.

Finality profiles behave as monotone summaries for this restricted merge, not
as the state space's join operator.

## 5. Conflict And Local-To-Global Failure

Composition can fail more strongly.

Two threshold-one records supporting opposite values are each locally final.
Their merge has two threshold-reaching values and therefore no unique
decision.

Likewise, two local assignments can each be internally consistent while
disagreeing on an overlap variable. They do not admit one global assignment.
The implementation is a minimal compatibility test, not a full sheaf
cohomology calculation, but it exposes the same local-to-global question.

## 6. Coarse-Graining Is An Intervention

T11 compares:

- lossy checkpoints that create one new source;
- provenance checkpoints that retain the hidden source union.

Provenance checkpoints preserve support in all 15 non-empty states, but
preserve holder and branch dimensions only for the four singleton states,
`26.67%` of the sweep. Lossy checkpoints preserve support only in those same
singleton states.

Checkpointing is therefore not neutral summarization. It selects which
finality dimensions survive and can change profile ordering.

## 7. Operational Epigenetic Structure

The epigenetic lens is included only where it creates a formal distinction.

The stored token is analogous to stable inherited substrate. Expression marks
are context state inherited by descendants. A local descendant can overwrite
an inherited mark, analogous to reprogramming.

In the minimal witness:

```text
stored source identity: unchanged
visible support:         1 -> 0 -> 1
operation:               expression -> inherited silence -> reactivation
```

This distinguishes record existence from record expression. It also makes
composition history-sensitive: neutral grouping is invariant, while applying
the same mark to one child or to an ancestor changes which records are
visible.

The analogy stops there. The model contains no DNA, chromatin, organism,
reproduction, or biological generation.

## 8. No Fixed Fractal Layers

The recursive type has no built-in number of semantic levels. Evaluation is
iterative and was tested through depth 1,024.

That result means the implementation does not depend on a chosen three-layer
or seven-layer story. It does not prove:

- infinitely many levels;
- self-similarity;
- scale invariance;
- a fractal dimension.

Those would require separate measurements.

## 9. Comparison Across Viewpoints

| Viewpoint | What survives | What fails |
| --- | --- | --- |
| CRDT | evidence union is a join-semilattice | profile merge is not the same join |
| coarse-graining / RG | macrostates can carry selected information upward | dimensions and ordering need not be preserved |
| sheaf / local-to-global | overlap consistency is a precise gluing question | local finality does not guarantee a global section |
| epigenetic | inherited context modulates expression over stable identity | biological mechanism is not imported |
| fractal / recursive | arbitrary finite nesting is supported | self-similarity and infinite depth are untested |

## 10. Claim Verdict

The strong claim is rejected:

> Finality profiles universally compose as a join-semilattice.

The surviving C2 claim is:

> Finality is compositional only through a typed pipeline. Evidence may join
> cleanly while inherited context, observer access, coarse-graining, profiles,
> and decisions transform or break that structure.

This is more constrained than the original intuition, but more useful. It
identifies exactly where cross-scale inheritance can fail.

## 11. Next Decisive Experiment

Move from trees to overlapping covers with nontrivial shared records. Define
restriction maps between local observer contexts and search for the precise
conditions under which compatible local finality assignments admit a unique,
multiple, or nonexistent global extension.
