# Technical Report: Reversible Finality Nonmonotonicity v0.1

## Claim Under Test

H7 says finality structure can induce an observer-relative temporal direction
when admissible transformations are monotone in D1 finality. T18 proves that
conditional theorem in a finite constructor model. T9 shows that reversible
local dynamics can carry observer-indexed traces with zero logical
information-loss bound.

T80 asks whether those two results compose: does reversible local dynamics
itself ground the T18 monotone-admissibility rule?

## Artifact

T80 builds an executable bridge from T9 to T18. It computes layer-by-layer
observer-window trace profiles for a second-order reversible cellular automaton
and classifies each physical step using the T18 transformation classifier.

The canonical witness is the width-3 second-order reversible lift of elementary
Rule 30 with all-zero previous/current registers, seed index 0, and observer
window `(0, 1)`.

## Current Strongest Claim

Raw observer-window D1 trace profiles are not monotone under reversible local
dynamics, even when the global transition map is injective and has zero logical
information-loss bound.

## Evidence

The global transition map is injective:

```text
state count = 64
image count = 64
lost bits = 0
Landauer lower-bound proxy = 0 J
direct inverse checked = true
```

The fixed observer window sees this raw D1 trace-profile sequence:

```text
layer 0: (1, 1, 1, 1)
layer 1: (2, 2, 1, 2)
layer 2: (1, 1, 1, 1)
layer 3: (0, 0, 0, 0)
layer 4: (1, 1, 1, 1)
layer 5: (2, 2, 1, 2)
```

The physical step from layer 1 to layer 2 decreases accessible support,
spatial redundancy, and terminal intervention cost. T18 classifies that same
profile transition as `strict_definalization` and therefore impossible under
the constructor rule.

## What This Improved

T80 separates two claims that were easy to blur:

```text
T18: if transformations are D1-monotone, strict finalization has a direction.
T80: reversible local dynamics do not automatically satisfy D1 monotonicity.
```

This makes H7 more evaluable. It identifies the missing physical assumption:
some persistence, coarse-graining, or constructor-impossibility condition must
be added before finality direction can be treated as a physical arrow.

## What This Weakened

H7 is weakened. The project should not claim that finality-induced direction
survives in a zero-information-loss substrate merely because reversible
dynamics can carry traces. Raw terminal traces can disappear under perfectly
reversible dynamics.

## Control

T80 includes a persistent-memory control. If an external memory simply retains
each observed trace event, retained support is monotone. That does not repair
H7 by itself; it shows exactly why the next model must make the observer
memory endogenous rather than externally imposed.

## Falsification Condition

T80 fails if every reversible second-order CA trajectory with a nonzero
observer-window trace has componentwise nondecreasing raw D1 trace profiles
across physical steps.

## Claim Ledger Update

H7 should remain `partially_supported` only as a conditional constructor
theorem, and should be weakened against physical overread:

```text
T80 shows that raw reversible local dynamics can violate D1 monotonicity.
Finality-induced direction requires an added persistence, coarse-graining, or
constructor-impossibility condition; it is not grounded by reversible trace
propagation alone.
```

## Next Work

Build the T9 requested persistent reconciler subsystem: a local component that
receives traces, stores them, compares retained state with current input, and
changes future behavior. Then test whether its retained-record D1 profile is
monotone without reducing the claim to thermodynamic erasure.

## Reproduction

```bash
python -m unittest tests.test_reversible_finality_nonmonotonicity -v
python -m models.run_t80
```
