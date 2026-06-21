# Technical Report: Persistent Reconciler Cost Boundary v0.1

## Claim Under Test

H7 says finality structure can induce an observer-relative temporal direction
when admissible transformations are monotone in D1 finality. T18 proves this
as a conditional constructor theorem. T80 then blocks a direct physical
reading: raw observer-window D1 profiles can decrease under reversible local
dynamics.

T82 tests the next repair candidate. Replace the terminal observer window with
a persistent reconciler subsystem that receives trace masks, compares current
input with retained state, and updates memory. Does this produce monotone
retained records without reducing the H7 arrow to ordinary thermodynamic
irreversibility or unaccounted memory growth?

## Artifact

T82 uses the T80 width-3 second-order reversible Rule 30 witness and feeds the
observer-window masks into three finite reconciler updates:

```text
observed masks = (10, 11, 10, 00, 10, 11)
raw support = (1, 2, 1, 0, 1, 2)
```

The reconciler updates are:

```text
bounded OR memory:
  M' = M OR O, with O preserved in the one-step map

bounded XOR memory:
  M' = M XOR O, with O preserved in the one-step map

append-only ledger:
  write O into the next blank slot and advance a cursor
```

The finite-map audit computes injectivity and logical information loss for
each update.

## Current Strongest Claim

In the T80 reversible trace witness, an endogenous finite reconciler gets
monotone retained records only by using a non-injective coarse-graining update
or by consuming append-only blank ledger state.

## Evidence

| Policy | Support sequence | Monotone | Injective | Logical loss |
| --- | --- | --- | --- | ---: |
| Bounded OR memory | (1, 2, 2, 2, 2, 2) | true | false | positive |
| Bounded XOR memory | (1, 1, 2, 2, 1, 1) | false | true | 0 bits |
| Append-only ledger | (1, 3, 4, 4, 5, 7) | true | true on blank-slot subspace | 0 bits |

The OR update is monotone because it coalesces old and new states. For a
two-bit observation window its finite map has fewer images than inputs and a
positive logical information-loss bound.

The XOR update is injective and has zero logical information loss, but it is
not a retained-record reconciler in the T18 sense: support can decrease when a
later observation toggles a prior bit.

The append-only ledger is monotone and injective for the checked horizon, but
only on the subspace where the next slot is blank. For six two-bit
observations it consumes twelve blank memory bits. A three-slot ledger
exhausts at observation layer 3.

## What This Improved

T82 makes the missing T80 persistence assumption precise. "Add memory" is not
a single physical move. It splits into:

```text
irreversible bounded reconciliation,
reversible but nonmonotone bounded reconciliation,
or reversible append-only reconciliation with growing blank state.
```

This makes H7 more testable because a proposed physical observer must now say
which resource pays for persistent monotone records.

## What This Weakened

H7 is further weakened as a physical arrow claim. Persistent memory does not
automatically repair the reversible-CA counterexample. If the memory is
bounded and monotone, it is non-injective. If it is bounded and reversible, it
need not be monotone. If it is reversible and monotone, it consumes fresh blank
ledger capacity and fails at finite horizon unless another physical process
refreshes or exports records.

## Falsification Condition

T82 fails if a fixed-size finite reversible reconciler implements
componentwise monotone retained support for the T80 observation sequence
without preserving old memory as garbage, consuming blank slots, or using a
non-injective update.

## Claim Ledger Update

H7 should remain `partially_supported` only as a conditional constructor
theorem. T82 adds a resource-accounting boundary: persistent reconciliation
must be paid for by irreversible coarse-graining, garbage/history retention,
or fresh blank ledger capacity. A finality-induced direction has not yet been
separated from entropy export or memory-resource depletion in a physically
autonomous observer.

## Open Blocker

No physically autonomous reconciler has yet been shown to refresh or compress
records indefinitely while preserving D1 monotonicity without ordinary
thermodynamic irreversibility.

## Next Work

Model a cyclic reversible reconciler with explicit garbage export or heat bath
coupling, then test whether the H7 direction differs from entropy export
rather than merely tracking it.

## Reproduction

```bash
python -m unittest tests.test_persistent_reconciler_cost_boundary -v
python -m models.run_t82
```
