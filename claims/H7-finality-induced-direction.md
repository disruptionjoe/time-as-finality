# H7: Finality-Induced Direction

## Claim

Finality structure can induce an observer-relative temporal direction when
admissible transformations are monotone in D1 finality.

## Class

Conjecture.

## Status

Partially supported only as a conditional constructor-style theorem; weakened
against direct physical reading by T80.

## What This Does Not Claim

- This does not derive the thermodynamic arrow.
- This does not replace coordinate time, proper time, relativity, or entropy.
- This does not prove that every physical system instantiates the constructor
  rule used in T18.
- This does not turn the finality partial order into a universal total order.

## Why It Might Be Useful

If finalized records are defined by transformations that cannot be undone
without decreasing D1 structure, then strict finalization has an intrinsic
direction. The direction comes from the asymmetry of admissible transformations:

```text
less finalized record -> more finalized record
```

is possible, while the reverse is not admissible under the same rule.

## How It Could Fail

- A physically grounded model may allow D1-decreasing transformations.
- The constructor rule may merely repackage thermodynamic irreversibility.
- The D1 dimensions may collapse in the relevant substrate.
- The induced direction may be too weak to explain any experienced or
  physical arrow.

## Tests

- [T18: Finality Direction Theorem](../tests/T18-finality-direction-theorem.md)
- [T80: Reversible Finality Nonmonotonicity](../tests/T80-reversible-finality-nonmonotonicity.md)
- [T5: Thermodynamic Record Support](../tests/T5-thermodynamic-record-support.md)
- [T9: Emergence Laboratory](../tests/T9-emergence-laboratory.md)

## T18 Result

[T18](../tests/T18-finality-direction-theorem.md) verifies a finite theorem:
in a constructor-style model where admissible transformations are D1-monotone,
strict finalization induces an acyclic partial order and every strict
finalization has an impossible reverse.

The result also finds a thermodynamic-divergence witness: a strict finality
increase where the thermodynamic-cost proxy does not increase. That supports
the narrow claim that finality direction is not defined by the thermodynamic
proxy in this toy model.

## T80 Result

[T80](../tests/T80-reversible-finality-nonmonotonicity.md) tests whether T18's
D1-monotone admissibility rule is automatically grounded by reversible local
dynamics. It is not. A width-3 second-order reversible lift of elementary Rule
30 has an injective transition map, zero logical information-loss bound, and a
checked direct inverse, but a fixed observer window sees the raw D1 trace
profile decrease:

```text
(2, 2, 1, 2) -> (1, 1, 1, 1)
```

T18 classifies that physical step as `strict_definalization` and therefore
impossible under the constructor rule. H7 therefore needs an added persistence,
coarse-graining, or constructor-impossibility condition before it can be read
as a physical arrow rather than a conditional ordering theorem.
