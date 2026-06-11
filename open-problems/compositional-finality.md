# Compositional Finality

## Resolved v0.1 Question

Do finality profiles form a join-semilattice under record merge?

T11 answers: **not generally**.

Compatible evidence states form a join-semilattice under
provenance-preserving union. Finality profiles are monotone under transparent,
conflict-free merge in the finite sweep, but their physical merge equals the
componentwise least upper bound only about half the time.

## Surviving Problem

Characterize the admissible composition operators for which each stage of the
typed pipeline preserves useful structure:

```text
evidence join
  -> inherited expression
  -> access projection
  -> profile
  -> decision
```

The strongest open version concerns overlapping systems rather than trees.
Given locally consistent records on a cover:

1. when do they admit a global record assignment;
2. when is that assignment unique;
3. which finality dimensions survive restriction and gluing;
4. how do inherited expression marks alter the obstruction?

## Guardrail

Recursive structure is not automatically fractal. A fractal claim would
require demonstrated self-similarity or scaling behavior, neither of which
T11 assumes or establishes.
