# PO1: Projection-Obstruction Schema

## Claim

A definable projection from a globally satisfiable richer D1RestrictionSystem
to a non-trivially obstructed restricted D1RestrictionSystem, where the
projection forgets named and measurable structure, is a faithful finite
Projection-Obstruction instance.

The positive schema requires seven admissibility conditions (AC1–AC7):

```text
AC1  Richer system satisfies all T26 axioms.
AC2  Restricted system satisfies all T26 axioms.
AC3  Site map is total (projection is definable).
AC4  Restricted system has all patches locally satisfiable (non-trivial obstruction).
AC5  Projection forgets named structure AND loses measurable profile data.
AC6  Restricted system has a gluing obstruction (global_witness_count=0).
AC7  Richer system has a global section (obstruction_detected=False).

If AC1–AC7 all hold:
  the restricted no-go is represented as a projection-created finite gluing
  obstruction.
```

The weakest correct schema uses AC1–AC3, AC6–AC7 (five conditions). AC4 and
AC5 are added as guards against trivial and structure-free instances.

## Class

Formal schema.

## Status

Partially supported (formally narrowed by T31).

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

## Admissibility failure types

| Failure | Verdict | Examples |
| --- | --- | --- |
| AC3 fails | boundary_non_definable | distler_garibaldi, type_system_macro_expansion |
| AC7 fails | non_admissible_shared_obstruction | access_control_inheritance, synthetic_shared |
| AC6 fails | non_admissible_no_new_obstruction | database_expand_contract, synthetic_lossy |
| AC4 fails | non_admissible_trivial_obstruction | (no current case) |
| AC5 fails | non_admissible_no_forgotten_structure | (no current case in isolation) |

## How It Could Fail

- Future examples may require sheaf or category-level morphisms.
- AC4 and AC5 guards have not been tested by a case that fails them in
  isolation; a manufactured case could reveal that the guards are insufficient.
- Three-patch contradictions constructed post-hoc to force an obstruction
  rather than encoding a domain constraint remain a risk for overcounting.
- Forgotten structure may not always be representable as finite patch data.

## Tests

- [T27: Class-Relative Bridge Audit](../tests/T27-class-relative-bridge-audit.md)
- [T28: CAP Theorem Bridge](../tests/T28-cap-theorem-bridge.md)
- [T29: Projection-Obstruction Schema](../tests/T29-projection-obstruction-schema.md)
- [T30: Cross-Domain Projection-Obstruction Validation](../tests/T30-cross-domain-projection-obstruction-validation.md)
- [T31: PO1 Admissibility Conditions](../tests/T31-po1-admissibility-conditions.md)
