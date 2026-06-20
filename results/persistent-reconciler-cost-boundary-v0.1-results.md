# T82 Results: Persistent Reconciler Cost Boundary

Strongest claim: In the T80 reversible trace witness, an endogenous finite reconciler gets monotone retained records only by using a non-injective coarse-graining update or by consuming append-only blank ledger state.

Weakened claim: H7 is not rescued by adding persistent memory unless the memory resource or erasure rule is physically accounted for.

## T80 observation sequence

- Observed masks: `[[1, 0], [1, 1], [1, 0], [0, 0], [1, 0], [1, 1]]`
- Raw support sequence: `[1, 2, 1, 0, 1, 2]`
- Raw support monotone: `False`

## Reconciler policies

| Policy | Support sequence | Monotone | Injective | Lost bits | Boundary |
| --- | --- | --- | --- | ---: | --- |
| `bounded_irreversible_or_memory` | `[1, 2, 2, 2, 2, 2]` | `True` | `False` | `1.0` | Fixed-width memory; monotone because OR coalesces old and new support states. |
| `bounded_reversible_xor_memory` | `[1, 1, 2, 2, 1, 1]` | `False` | `True` | `0.0` | Fixed-width memory; injective because observation is preserved in the one-step map. |
| `reversible_append_only_ledger_h6` | `[1, 3, 4, 4, 5, 7]` | `True` | `True` | `0.0` | Injective only on the blank-slot subspace; consumes 12 blank memory bits for 6 observation slots. |
| `reversible_append_only_ledger_h3` | `[1, 3, 4]` | `True` | `True` | `0.0` | Exhausted at observation layer 3; continuing would require either more blank slots or an erasing/recycling rule. |

## Verdicts

- `bounded_irreversible_or_memory`: Monotone retained support is bought by a non-injective update, so this repair reduces H7 to irreversible coarse-graining.
- `bounded_reversible_xor_memory`: Reversibility is preserved, but retained support can decrease; fixed reversible memory does not recover T18 monotonicity.
- `reversible_append_only_ledger_h6`: Monotone and injective for the checked horizon, but only by turning elapsed observations into growing ledger state.
- `reversible_append_only_ledger_h3`: Monotone and injective for the checked horizon, but only by turning elapsed observations into growing ledger state.

## Falsification condition

T82 fails if a fixed-size finite reversible reconciler implements componentwise monotone retained support for the T80 observation sequence without preserving old memory as garbage, consuming blank slots, or using a non-injective update.

## H7 update

H7 should remain partially supported only as a conditional constructor theorem. T82 adds that persistent reconciliation must be resource-accounted: bounded OR memory is irreversible, bounded XOR memory is reversible but nonmonotone, and append-only reversible memory shifts the arrow into blank ledger capacity.

## Blocker

No physically autonomous reconciler has yet been shown to refresh or compress records indefinitely while preserving D1 monotonicity without ordinary thermodynamic irreversibility.

## Next move

Model a cyclic reversible reconciler with explicit garbage export or heat bath coupling, then test whether the H7 direction differs from entropy export rather than merely tracking it.
