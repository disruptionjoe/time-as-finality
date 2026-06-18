# PO1: Projection-Obstruction Schema

## Claim

Some class-relative no-go patterns admit a finite abstraction as
projection-created gluing obstructions between `D1RestrictionSystem` objects.

The positive schema is:

```text
If:
  a richer restriction system has a global section,
  a restricted system has no global section,
  a projection morphism from richer to restricted is definable,
  and the projection forgets obstruction-resolving structure,
then:
  the restricted no-go is represented as a projection-created finite gluing
  obstruction.
```

## Class

Formal schema.

## Status

Partially supported.

## What This Does Not Claim

- It does not prove any original physics no-go theorem.
- It does not show that Time as Finality proves GU.
- It does not show that GU proves Time as Finality.
- It does not replace the original mathematical proofs.
- It does not apply when the projection is not definable.
- It does not claim continuous, sheaf-level, or category-level generality.

## Why It Might Be True

T27 found the same finite pattern in Witten 1981 and Nielsen-Ninomiya: a richer
system has a global section, a restricted system has a finite gluing
obstruction, and the projection loses the data that made the richer global
section possible.

T29 turns that pattern into an explicit finite object and tests two boundaries:

- loss without obstruction;
- obstruction inherited from the richer system.

T28 adds CAP as a distributed-systems stress test. The CAP restricted system
has the same three-patch chaining obstruction as the Nielsen-Ninomiya
restricted system, while the richer eventual-consistency system restores a
global section by adding branch-support and reconciliation structure.

## How It Could Fail

- The pattern may be an artifact of the chosen T27 encodings.
- Future examples may require sheaf or category-level morphisms.
- Projection may preserve theorem validity without producing a gluing
  obstruction.
- Forgotten structure may not be representable as finite patch data.

## Tests

- [T27: Class-Relative Bridge Audit](../tests/T27-class-relative-bridge-audit.md)
- [T28: CAP Theorem Bridge](../tests/T28-cap-theorem-bridge.md)
- [T29: Projection-Obstruction Schema](../tests/T29-projection-obstruction-schema.md)

## Contribution Needed

Test PO1 on a domain not inherited from GU or Time as Finality. A stronger
result would show whether Projection-Obstruction is domain-neutral rather than
a useful abstraction of the current bridge audit.
