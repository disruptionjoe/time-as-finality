# T82: Persistent Reconciler Cost Boundary

## Route

Thermodynamic arrow of time.

## Question

Can the T9/T80 terminal observer window be replaced by an endogenous
persistent reconciler subsystem that makes retained-record D1 monotone without
collapsing H7 into ordinary thermodynamic irreversibility?

## Result

The finite witness is a boundary result, not a support theorem.

Using the T80 reversible Rule 30 observation sequence:

```text
observed masks = (10, 11, 10, 00, 10, 11)
raw support = (1, 2, 1, 0, 1, 2)
```

three reconciler updates separate the assumptions:

```text
bounded OR memory:
  support = (1, 2, 2, 2, 2, 2)
  monotone = true
  injective = false

bounded XOR memory:
  support = (1, 1, 2, 2, 1, 1)
  monotone = false
  injective = true

append-only reversible ledger:
  support = (1, 3, 4, 4, 5, 7)
  monotone = true
  injective = true on the blank-slot subspace
```

The append-only repair consumes one fresh observation slot per layer. A
three-slot ledger exhausts at observation layer 3.

## Claim Impact

H7 remains only conditionally supported. Persistent reconciliation must be
resource-accounted: bounded monotone OR memory is irreversible, bounded
reversible XOR memory is not monotone, and reversible append-only memory moves
the arrow into blank ledger capacity.

## Falsification Condition

T82 fails if a fixed-size finite reversible reconciler implements
componentwise monotone retained support for the T80 observation sequence
without preserving old memory as garbage, consuming blank slots, or using a
non-injective update.

## Reproduction

```bash
python -m unittest tests.test_persistent_reconciler_cost_boundary -v
python -m models.run_t82
```
