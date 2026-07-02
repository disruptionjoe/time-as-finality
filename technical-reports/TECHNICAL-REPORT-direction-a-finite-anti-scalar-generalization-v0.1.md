# Technical Report: Direction A Finite Anti-Scalar Generalization v0.1

## Status

Internal Direction A progress artifact.

This report does not promote a claim, change the North Star, alter Q1/Q1C
status, or update the test registry. It refines the first rung of Direction A
from `audits/2026-07-01-high-gravity-research-directions.md`: generalizing the
T49/T50 anti-scalar result toward an eventual temporal-order inequality.

The current worktree already contains active T392/T393 Direction B changes, so
this report intentionally stays in a separate documentation lane.

## Objective

The high-gravity audit names Direction A as:

```text
An inequality for temporal order.
```

The first rung is to generalize T49's anti-scalar result from the three-event
witness to arbitrary finite event structures.

The useful one-session objective is narrower:

```text
Separate the exact scalarization theorem that is already safe from the
tie-collapse loophole that must be handled before any inequality target is
credible.
```

## Existing Earned Inputs

T49 proves, on the T48 witness, that the two-axis magnitude order exactly
matches the record-dependency partial order and that the witness has an
incomparable root pair.

T50 packages this as Axis Monotonicity:

```text
record order = componentwise finality-axis order
```

when AM holds, and derives the anti-scalar corollary for AM structures with
incomparability.

Verification rerun for this report:

```text
python -m models.run_t49
python -m models.run_t50
```

Both runners completed successfully and rewrote no tracked T49/T50 result file.

## Definitions

Let `P = (E, <=_P)` be a finite event-finality partial order.

An **exact scalar preorder representation** is a map `s: E -> R` such that:

```text
e <=_P f  iff  s(e) <= s(f)
```

This is the strongest reading of "a scalar time coordinate replicates the
partial order."

A **strict scalar level representation** is a weaker map `s: E -> R` such that:

```text
e <_P f  iff  s(e) < s(f)
```

This weaker reading may collapse incomparable events into equal scalar levels.
It preserves strict before/after pairs but does not preserve incomparability as
a distinct relation.

An **incomparability-sensitive representation** preserves three outcomes:

```text
e before f
f before e
e incomparable with f
```

Direction A needs the third object, not just a linear extension or a scalar
rank function.

## Theorem 1: Exact Scalar Boundary

For a finite partial order `P`, an exact scalar preorder representation exists
only when `P` is total.

Proof:

1. Any scalar `s: E -> R` with the relation `s(e) <= s(f)` induces a total
   preorder on `E`: for every pair `e, f`, either `s(e) <= s(f)` or
   `s(f) <= s(e)`, or both.
2. If exact representation holds, `<=_P` must inherit that total comparability.
3. Therefore any incomparable pair in `P` makes exact scalar representation
   impossible.
4. Conversely, any finite total order can be represented by assigning
   increasing scalar values along the order.

For antisymmetric partial orders, scalar ties between distinct events add
mutual comparability in the scalar preorder and therefore cannot be exact.

This is the safe generalization of the T49 anti-scalar theorem.

## Boundary: Strict Scalars Can Hide Incomparability

The loose sentence "no scalar can reproduce a partial order with incomparable
elements" is too strong unless "reproduce" means exact preorder reproduction.

If only strict before/after pairs are checked, a scalar can sometimes hide
incomparability by assigning equal values.

The T49 shape has two incomparable roots below one top:

```text
e1 || e2
e1 < e3
e2 < e3
```

A strict scalar can represent the strict pairs by assigning:

```text
s(e1) = 0
s(e2) = 0
s(e3) = 1
```

That scalar does not preserve the partial order exactly. It replaces
incomparability with same-level tying. But if an external inequality only asks
which strict before/after pairs exist, this witness alone will not defeat a
scalar-level model.

Small exhaustive verification performed during this run:

```text
n=3: posets=19, exact total-order representable=6, strict scalar weak-order representable=13
n=4: posets=219, exact total-order representable=24, strict scalar weak-order representable=75
T49 shape: exact_total_preorder=False, strict_scalar=True via (0, 0, 1)
```

Interpretation:

- exact scalar preorder representation fails for every non-total finite poset;
- strict scalar level representation survives for weak-order-shaped posets;
- T49's three-event shape is exact-scalar negative but strict-scalar
  collapsible.

## Theorem 2: Tie-Collapse Classification Target

For finite partial orders, strict scalar level representation is possible
exactly for weak-order-shaped posets: the incomparability relation behaves like
an equivalence relation, and the quotient classes are totally ordered.

Equivalently:

```text
incomparable events can be grouped into scalar levels
and those levels form a chain.
```

This is not the Direction A victory condition. It is the loophole classifier.
It says which finite partial orders can be reduced to scalar levels once the
model is allowed to treat incomparable events as ties.

The next executable artifact should test this classifier over finite event
structures and then ask which structures survive the stronger
incomparability-sensitive gate.

## Implication For Direction A

The future temporal-order inequality should not be framed as:

```text
Does any scalar or linear extension exist?
```

Every finite poset has linear extensions, and many non-total posets have strict
scalar level representations.

The sharper target is:

```text
Can the observed structure be explained by scalar levels once ties are allowed,
or does it require preserving operational incomparability as distinct from
same-time tying?
```

For process-matrix or causal-order translation, the future bound must therefore
separate at least three model classes:

1. total background-time order;
2. scalar-level order with ties;
3. incomparability-sensitive partial temporal order.

The T49/T50 result supports class 3 only under exact preorder replication. To
make Direction A experimentally interesting, the next witness must either:

- impose an operational no-tie condition;
- show that scalar ties erase a measurable independence/access distinction; or
- move to a non-weak-order finite event structure that cannot be represented
  even by strict scalar levels.

## Recommended Next Artifact

Working title:

```text
Finite Temporal-Order Scalarization Taxonomy
```

Use the next free T-number only after the current T392/T393 worktree lane is
settled and `TESTS.md` can be edited safely.

Minimum executable scope:

1. Enumerate finite posets up to `n=4` or `n=5`.
2. Classify each as:
   - exact scalar preorder representable;
   - strict scalar level representable;
   - non-scalar even under tie collapse.
3. Include the T49 witness as a positive exact-scalar failure and a positive
   strict-scalar tie-collapse example.
4. Include at least one non-weak-order finite poset as the candidate Direction A
   hard case.
5. Emit demotion language: T49 alone is not enough for a scalar-tie-resistant
   temporal-order inequality.

Success criterion:

```text
The repo gains an executable intake gate for temporal-order inequality
candidates before any process-matrix or experimental language is attempted.
```

Failure criterion:

```text
Every candidate hard case collapses to scalar levels once the operational
comparison is stated honestly.
```

## Claim And Governance Impact

No claim status changes.

No claim-ledger update.

No roadmap edit.

No external-facing posture change.

The only durable result is a refined Direction A intake boundary:

```text
Exact scalar anti-representation is easy; tie-collapse resistance is the real
next gate.
```

