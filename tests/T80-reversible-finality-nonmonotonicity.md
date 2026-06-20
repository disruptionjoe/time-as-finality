# T80: Reversible Finality Nonmonotonicity

## Route

Thermodynamic arrow of time.

## Question

Does T18's D1-monotone constructor rule follow from T9-style reversible local
dynamics, or is it an extra admissibility assumption?

## Result

The raw observer-window trace profile is not monotone under reversible local
dynamics. A width-3 second-order reversible lift of elementary Rule 30 has an
injective global transition map and zero logical information-loss bound, but
the fixed observer window sees:

```text
layer 0: (1, 1, 1, 1)
layer 1: (2, 2, 1, 2)
layer 2: (1, 1, 1, 1)
layer 3: (0, 0, 0, 0)
```

The physical step from layer 1 to layer 2 is a strict definalization under
T18's classifier, so T18 admissibility cannot be identified with arbitrary
physical time evolution in reversible substrates.

## Claim Impact

H7 is weakened. A finality-induced direction remains available only under an
added persistence, coarse-graining, or constructor-impossibility condition.
Raw reversible trace dynamics do not supply that condition.

## Falsification Condition

T80 fails if every reversible second-order CA trajectory with a nonzero
observer-window trace has componentwise nondecreasing raw D1 trace profiles
across physical steps.

## Reproduction

```bash
python -m unittest tests.test_reversible_finality_nonmonotonicity -v
python -m models.run_t80
```
