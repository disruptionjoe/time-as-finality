# Technical Report: Finality Reflection Property v0.1

## Summary

T57 discharges the first Phase 21 mathematical obligation created by the T56
gap-presheaf result.

T56 refined phantom incomparability from an H1 obstruction into an H0-level gap:

```text
G(U) = A(U) - F(U)
```

where `A(U)` is the ambient global-order restriction and `F(U)` is the locally
computed apparent order. Phase 21 correctly warned that complements of
subpresheaves are not automatically presheaves. T57 proves the condition needed
in the specific T56 model: the Finality Reflection Property (FRP).

Best-supported verdict:

```text
FRP holds for the T56 apparent-order model.
The gap assignment is restriction-closed.
Complement closure is not automatic in general.
The arrow-direction circularity risk remains open.
```

## Core Result

Finality Reflection Property v0.1:

```text
For the T56 apparent-order construction, if V is a proper subpatch of U in
record-access order, then every non-reflexive pair in F(V) appears in the
restriction of F(U) to V-accessible events.

Equivalently:

  (a,b) not in F(U) implies (a,b) not in F(V)

for every event pair accessible to V.

Therefore G(U) = A(U) - F(U) is closed under restriction.
```

This closure is conditional on the TaF apparent-order definition. It is not a
general theorem about complements.

## Proof Sketch

Let `Events(U)` be the events whose target records are contained in the
record-access set of `U`.

If `V < U`, then:

```text
records(V) subset records(U)
```

so:

```text
Events(V) subset Events(U)
```

In T56:

```text
F(U) = transitive closure of direct record-dependency edges over Events(U)
```

Any chain witnessing `(a,b) in F(V)` uses only events in `Events(V)`. Since
`Events(V) subset Events(U)`, the same chain is available in `F(U)`. Therefore:

```text
F(V) subset rho_{U->V}(F(U))
```

Taking the contrapositive over `V`-accessible pairs gives FRP:

```text
(a,b) not in F(U) => (a,b) not in F(V)
```

Now suppose `(a,b) in G(U)` and both endpoints are accessible to `V`. Then
`(a,b) in A(U)` and `(a,b) not in F(U)`. Ambient restriction gives
`(a,b) in A(V)`. FRP gives `(a,b) not in F(V)`. Therefore:

```text
rho_{U->V}(G(U)) subset G(V)
```

So `G` is restriction-closed in the finite T56 model.

## Executable Evidence

T57 checked two finite record-lattice witnesses:

| Cover | Nested patch pairs | Checked event pairs | FRP violations |
| --- | ---: | ---: | ---: |
| `hidden_intermediary_record_lattice` | 19 | 6 | 0 |
| `branching_dependency_record_lattice` | 65 | 60 | 0 |

It also checked gap restriction closure:

| Cover | Gap violations | Non-lifting examples |
| --- | ---: | ---: |
| `hidden_intermediary_record_lattice` | 0 | 1 |
| `branching_dependency_record_lattice` | 0 | 6 |

The non-lifting examples are important. They show that restriction closure does
not mean every smaller-patch phantom gap comes from a larger-patch gap. Larger
patches may expose hidden intermediaries and erase a smaller observer's gap.

## Generic Complement Counterexample

T57 also preserves a hostile control:

```text
A(U) = A(V) = {(x,y)}
F(U) = empty
F(V) = {(x,y)}
```

Then:

```text
G(U) = {(x,y)}
G(V) = empty
```

Restricting `G(U)` to `V` leaves `(x,y)`, which is outside `G(V)`. This
counterexample proves that the Phase 21 warning was substantive: complement
closure requires FRP or an equivalent condition.

## Hypothesis Evaluation

### H0

The T56 apparent-order construction need not satisfy FRP.

Status: refuted for the tested finite model.

Evidence: FRP held across both record-lattice witnesses.

### H1

Apparent order is monotone under record-access inclusion.

Status: supported.

Evidence: for every nested patch pair `V < U`, `F(V)` was included in
`rho(F(U))`.

### H2

The T56 gap assignment is restriction-closed once FRP holds.

Status: supported.

Evidence: every larger-patch gap restricted into the smaller-patch gap.

### H3

Complement restriction closure is automatic for any subassignment.

Status: refuted.

Evidence: the generic complement counterexample violates FRP and its larger
complement restricts outside the smaller complement.

### H4

FRP resolves the T56 medium circular risk on arrow direction.

Status: left open.

Evidence: FRP proves monotonicity after directed source/target records are
given. It does not derive that direction from substrate-free task
composability.

## What T57 Strengthens

T57 strengthens the T56 refinement:

```text
phantom incomparability lives in G(U) = A(U) - F(U)
```

by proving that `G` is restriction-closed in the actual TaF model, not merely
asserted as a complement.

It also strengthens the Phase 21 roadmap by converting the first obligation
from an open warning into an executable finite theorem check.

## What T57 Weakens or Rejects

T57 rejects the overbroad claim:

```text
the complement of an apparent-order assignment is automatically presheaf-like
```

The generic counterexample shows this is false without FRP.

T57 also weakens any temptation to treat FRP as an arrow-of-time derivation.
It is a conditional structural lemma, not a solution to the origin of finality
direction.

## Limits

- The executable witnesses are finite record lattices, not a machine-checked
  proof over all finite covers.
- The proof assumes the T56 event-access rule and source/target
  record-dependency relation.
- FRP gives restriction closure only. Smaller-patch gaps need not lift to
  larger patches.
- FRP does not derive the direction of finality arrows.

## Repository Recommendation

Treat the T56 gap-presheaf language as conditionally licensed:

```text
G is restriction-closed because T56 apparent order satisfies FRP.
```

Do not treat gap-presheaf closure as an automatic property of complements.

## Next Research Target

The next natural T56/T57 step is to test whether:

```text
H0(G) is exactly the set of T51-T52 phantom incomparability witnesses.
```

The separate circular-risk question should remain a distinct T56B target:

```text
Can finality-arrow direction be derived from substrate-free task
composability, or must it stay as directed input structure?
```
