# PO1: Projection-Obstruction Schema

## Claim

A definable projection from a globally satisfiable richer D1RestrictionSystem
to a non-trivially obstructed restricted D1RestrictionSystem, where the
projection forgets named and measurable structure, is a faithful finite
Projection-Obstruction instance.

The expanded audit checklist has seven admissibility conditions (AC1-AC7):

```text
AC1  Richer system satisfies all T26 axioms.
AC2  Restricted system satisfies all T26 axioms.
AC3  Site map is total (projection is definable).
AC4  Restricted system has all patches locally satisfiable (non-trivial obstruction).
AC5  Projection forgets named structure AND loses measurable profile data.
AC6  Restricted system has a gluing obstruction (global_witness_count=0).
AC7  Richer system has a global section (obstruction_detected=False).

If AC1-AC7 all hold:
  the restricted no-go is represented as a projection-created finite gluing
  obstruction.
```

T32 derives a smaller formal condition basis:

```text
AC1 + AC2 + AC3 + AC5 + AC6 + AC7
```

AC4 is derived from AC6 because the T26 `obstruction_detected` predicate
already means local patches are satisfiable and no global assignment exists.
AC5 remains independent of `D1RestrictionSystem` alone because named forgotten
structure is stored on `ProjectionCase` metadata.

At the principle level, PO1 uses four admissibility principles:

```text
typed restriction-system pair
definable finite projection
projection-created nontrivial obstruction
informative forgotten structure
```

## Class

Formal schema.

## Status

Partially supported (formally narrowed by T31, structurally compressed by T32,
and partially derived by T33). T33 shows PO1 is a partially derived theorem:
conditions arise from IPT (typing/definability) + RMT (resource decrease) +
P5 (named mechanism). AC5-naming is the only condition not derivable from either
framework.

## What This Does Not Claim

- It does not prove any original physics no-go theorem.
- It does not show that Time as Finality proves GU.
- It does not show that GU proves Time as Finality.
- It does not replace the original mathematical proofs.
- It does not apply when the projection is not definable (AC3 fails).
- It does not apply when the obstruction is shared/inherited (AC7 fails).
- It does not claim continuous, sheaf-level, or category-level generality.

## Why It Might Be True

T27 found the same finite pattern in Witten 1981 and Nielsen-Ninomiya: a richer
system has a global section, a restricted system has a finite gluing
obstruction, and the projection loses the data that made the richer global
section possible.

T29 turns that pattern into an explicit finite object and tests two boundaries:
loss without obstruction; obstruction inherited from the richer system.

T28 adds CAP as a distributed-systems stress test. The CAP restricted system
has the same three-patch chaining obstruction as the Nielsen-Ninomiya
restricted system, while the richer eventual-consistency system restores a
global section by adding branch-support and reconciliation structure.

T30 hostile-tests PO1 in non-physics domains. Git semantic merge supplies one
positive PO1 instance. Database schema migration, access-control inheritance,
and type-system macro expansion supply negative and boundary controls.

T31 formalizes seven admissibility conditions and reclassifies all 10 cases
from T27, T28, T29, and T30. Four cases satisfy all seven: witten_1981,
nielsen_ninomiya, cap_theorem, and git_semantic_merge. No case in the test set
requires splitting PO1 into subclaims.

T32 asks why AC1-AC7 exist. It finds that AC4 is not independent: AC6 implies
AC4 under the current T26 definition of finite gluing obstruction. It also
finds that AC1 and AC2 are typed-object obligations, AC3 is projection
definability, AC6 and AC7 are independent gluing-polarity requirements, and
AC5 is the one non-intrinsic guard because it depends on named forgotten
structure.

T34 extends PO1 to chains of projections across the code-to-transistors
compilation chain. Three chain shapes are confirmed:

1. Emergent obstruction (Spectre timing side channel): the endpoint pair
   (source_code, microarchitecture) is a PO1 instance, but no source→intermediate
   pair is. The finite 3-patch gluing obstruction is invisible at every strict
   prefix of the chain and only appears at the full endpoint level.
2. Stepwise propagation: obstruction appears at an intermediate step (assembly)
   and the endpoint pair is also a PO1 instance.
3. Absorbed obstruction: obstruction appears at an intermediate step
   (unoptimized_IR) but is resolved by dead-code elimination; the endpoint pair
   is NOT a PO1 instance. This is the negative control.

T34 derives the PO1 Chain Theorem: a chained projection is a PO1 instance when
its endpoint pair satisfies AC1-AC7, independent of whether any partial prefix
pair is a PO1 instance. Emergent obstruction is the case of greatest interest:
the no-go is only visible from the chain's source to its full target.

T33 derives conditions from two deeper frameworks and evaluates H0-H5:

| Framework | Derives |
| --- | --- |
| IPT (Invariant-Preservation Theorem) | AC1, AC2, AC3, AC4 (via AC6), AC5-measurable (partial) |
| RMT (Resource-Monotonicity Theorem) | AC4, AC5-measurable, AC6, AC7 |

Best hypothesis: H3 — both IPT and RMT are required; neither alone suffices.
H0 (all independent) and H5 (no derivation) are rejected. AC5-naming is the
only condition not derivable from either framework. T33 recommends promoting
AC5-naming to **Principle P5 (Informative Forgetting)**, making the full theorem:

> A projection is a PO1 instance iff it is a valid typed morphism (IPT) that
> witnesses strict global satisfiability resource decrease R=1→R=0 (RMT) with
> named mechanism (P5).

Three finite counterexamples mark the IPT/RMT boundary: resource decrease does
not entail naming (AC5), RMT does not require a total site map (AC3), and IPT
does not require obstruction (AC6).

## Admissibility failure types

| Failure | Verdict | Examples |
| --- | --- | --- |
| AC3 fails | boundary_non_definable | distler_garibaldi, type_system_macro_expansion |
| AC7 fails | non_admissible_shared_obstruction | access_control_inheritance, synthetic_shared |
| AC6 fails | non_admissible_no_new_obstruction | database_expand_contract, synthetic_lossy |
| AC4 fails | non_admissible_trivial_obstruction | impossible if AC6 holds under current semantics |
| AC5 fails | non_admissible_no_forgotten_structure | generated T32 lossless projection witness |

## How It Could Fail

- Future examples may require sheaf or category-level morphisms.
- AC5 is not derivable from `D1RestrictionSystem` alone; future work should
  decide whether forgotten structure becomes first-class formal data.
- If AC6 is ever weakened to mean only `global_witness_count == 0`, AC4 must
  return as an independent nontriviality guard.
- Three-patch contradictions constructed post-hoc to force an obstruction
  rather than encoding a domain constraint remain a risk for overcounting.
- Forgotten structure may not always be representable as finite patch data.

## Tests

- [T27: Class-Relative Bridge Audit](../tests/T27-class-relative-bridge-audit.md)
- [T28: CAP Theorem Bridge](../tests/T28-cap-theorem-bridge.md)
- [T29: Projection-Obstruction Schema](../tests/T29-projection-obstruction-schema.md)
- [T30: Cross-Domain Projection-Obstruction Validation](../tests/T30-cross-domain-projection-obstruction-validation.md)
- [T31: PO1 Admissibility Conditions](../tests/T31-po1-admissibility-conditions.md)
- [T32: PO1 Admissibility Derivation](../tests/T32-admissibility-derivation.md)
- [T33: PO1 Foundational Derivation](../tests/T33-po1-foundational-derivation.md)
- [T34: Chained Projection Analysis](../tests/T34-po1-chained-projection.md)
