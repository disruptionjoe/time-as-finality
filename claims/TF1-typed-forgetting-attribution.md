# TF1: Typed Forgetting Attribution

## Claim

A projection-created obstruction is admissibly attributable only when the
projection carries a typed loss object naming structure that resolves the
obstruction in the source.

## Class

Formal target.

## Status

Open formal target.

## Candidate Lemma

Let:

```text
f: Source -> Target
```

be a definable morphism between finite restriction systems. Suppose:

```text
Source has a global section
Target has no global section
```

Then the target obstruction is admissibly attributable to `f` only if:

```text
LossKernel(f)
```

is non-empty and names structure whose presence in `Source` is relevant to the
source's global satisfiability.

This is a candidate attribution lemma, not a proven theorem.

## Why It Might Be True

The repo repeatedly finds that obstruction by itself is not enough:

- T39 shows the finite gluing obstruction is signed-graph parity CSP, a known
  mechanism.
- T31-T33 isolate AC5/P5: a projection-created obstruction needs named
  forgotten structure, not just source satisfiability and target obstruction.
- T34 shows endpoint obstruction can emerge, propagate, or be absorbed across
  chains.
- T37 shows same endpoints can receive different PO1 verdicts when paths
  accumulate different forgotten structure.
- T40 shows cross-level source-satisfiable plus target-obstructed is
  insufficient for holonic PO1 without named cross-level forgotten dimensions.

Together these suggest the original contribution is not "obstruction exists,"
but a typed attribution calculus for obstruction under information-losing
morphisms.

## How It Could Fail

- `LossKernel(f)` may collapse to existing `forgotten_structure` metadata
  without adding mathematical content.
- A non-empty loss object may be neither necessary nor sufficient once richer
  morphism classes are tested.
- Some projection-created obstructions may be attributable purely from a
  resource monotone without naming the lost structure.
- Absorbed obstruction cases may require recovery or optimizer morphisms that
  do not fit the proposed kernel laws.
- The admissibility checklist may remain a useful engineering discipline rather
  than a theorem.

## Tests / Work Items

- [Loss Kernel Formalization](../open-problems/loss-kernel-formalization.md)
- [T31: PO1 Admissibility Conditions](../tests/T31-po1-admissibility-conditions.md)
- [T32: PO1 Admissibility Derivation](../tests/T32-admissibility-derivation.md)
- [T33: PO1 Foundational Derivation](../tests/T33-po1-foundational-derivation.md)
- [T34: PO1 Chained Projection](../tests/T34-po1-chained-projection.md)
- [T37: Typed Transport Network](../tests/T37-typed-transport-network.md)
- [T39: CSP Satisfiability Reframing](../tests/T39-csp-satisfiability-reframing.md)
- [T40: Holarchy Lab](../tests/T40-holarchy-lab.md)
- [T41: Typed Transport Category](../tests/T41-typed-transport-category.md)

## Guardrails

- This does not claim that TaF discovered gluing obstruction.
- This does not claim obstruction conservation.
- This does not claim every information-losing map creates obstruction.
- This does not claim that access, provenance, or auditability are the whole
  structure; they are candidate corollaries or laboratories.

## Next Step

Define `LossKernel` as a first-class object and re-run T34/T37/T39/T40 through
it. Only after that should TF1 be upgraded from open formal target.
