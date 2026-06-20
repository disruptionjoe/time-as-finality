# T80 Results: Reversible Finality Nonmonotonicity

Strongest claim: Raw observer-window D1 trace profiles are not monotone under reversible local dynamics, even when the global transition map is injective and has zero logical information-loss bound.

Weakened claim: T18's finality arrow remains only a conditional constructor theorem; its admissible transformations cannot be identified with arbitrary physical time steps in reversible substrates.

## Configuration

- Rule: `30` second-order reversible lift
- Width: `3`
- Initial previous/current: `[0, 0, 0]` / `[0, 0, 0]`
- Seed index: `0`
- Observer window: `[0, 1]`

## Reversibility check

- State count: `64`
- Image count: `64`
- Injective: `True`
- Lost bits: `0.0`
- Landauer lower-bound proxy: `0.0`
- Direct inverse checked: `True`

## Layer profiles

| Layer | Trace mask | D1 trace profile |
| ---: | --- | --- |
| 0 | `[1, 0, 0]` | `(1, 1, 1, 1)` |
| 1 | `[1, 1, 1]` | `(2, 2, 1, 2)` |
| 2 | `[1, 0, 0]` | `(1, 1, 1, 1)` |
| 3 | `[0, 0, 0]` | `(0, 0, 0, 0)` |
| 4 | `[1, 0, 0]` | `(1, 1, 1, 1)` |
| 5 | `[1, 1, 1]` | `(2, 2, 1, 2)` |

## First nonmonotone physical step

- Layers: `1 -> 2`
- D1 trace profile: `(2, 2, 1, 2) -> (1, 1, 1, 1)`
- Decreased dimensions: `['accessible_support', 'spatial_redundancy', 'terminal_intervention_cost']`
- T18 classification: `strict_definalization`, possible under T18: `False`

## Persistent-memory control

- Retained support sequence: `[1, 3, 4, 4, 5, 7]`
- Monotone: `True`

Interpretation: A retained external memory is monotone by construction; raw terminal traces are not. The next question is whether such memory can be made endogenous and physically grounded.

## Falsification condition

T80 fails if every reversible second-order CA trajectory with a nonzero observer-window trace has componentwise nondecreasing raw D1 trace profiles across physical steps.

## H7 update

H7 should be weakened: finality-induced direction is not grounded by raw reversible trace dynamics alone. It requires an added persistence, coarse-graining, or constructor-impossibility condition.

## Blocker

No internal dynamical record-bearing observer has yet been shown to retain traces while preserving the intended D1 dimensions.

## Next move

Build the T9 requested persistent reconciler subsystem and test whether its retained-record D1 profile is monotone without reducing the claim to thermodynamic erasure.
