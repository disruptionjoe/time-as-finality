# C2: Typed Compositional Finality

## Claim

Finality composes only through a typed sequence of operations. Underlying
evidence can form a provenance-preserving join, while inherited expression,
observer projection, profile construction, coarse-graining, proof validation,
protocol confidence, readout, and decision thresholds need not preserve that
algebra.

## Class

Core claim.

## Status

Weakened from the stronger conjecture that finality profiles themselves form
a universal join-semilattice.

## What This Does Not Claim

- Every hierarchy is fractal or has infinitely many layers.
- Physical, biological, cognitive, and social systems use one mechanism.
- Coarse-graining preserves every finality dimension.
- Local consistency guarantees a global history.
- Inherited context changes the identity of the stored record.

## Evidence

[T11](../tests/T11-compositional-finality.md) demonstrates a join-semilattice
for compatible evidence-token states. It also supplies minimal
counterexamples to profile-level join, decision preservation under conflict,
coarse-graining invariance, and local-to-global consistency.

[T13](../tests/T13-signed-interfering-readout.md) extends the typed pipeline
one step further: a stable finality profile still need not determine
phase-sensitive readout.

[T14](../tests/T14-integrated-observer-context-finality.md) composes coupling,
inherited expression, proof filtering, Snowball-style confidence, finality
profiling, and signed readout in one finite witness. It supports C2 by showing
that the framework remains coherent only when those stages are not collapsed.

[T15](../tests/T15-generated-integrated-finality-stress.md) replaces that
single witness with a 448-case deterministic sweep. It finds repeatable
success regions and breakpoints, which supports typed separation as a
family-level constraint rather than a one-off repair.

[T16](../tests/T16-dynamical-phase-bearing-records.md) adds one more typed
stage: signs can be generated from local trace direction while finality
profiles remain phase-blind.

[T17](../tests/T17-persistent-dynamical-reconciler.md) adds another typed
separation inside the observer role: stored value, write status, generated
access boundary, finality profile, and comparator decision are distinct state
or evaluation layers. The written flag is necessary because stored false is
not the same as no record.

## Failure Conditions

- Provenance-preserving evidence merge fails its algebraic laws.
- A richer physically grounded profile preserves joins under every admissible
  merge and makes the typed distinction unnecessary.
- The inherited-expression layer adds no behavior beyond ordinary access
  control.

## Contribution Needed

Replace tree-only composition with overlapping record covers and characterize
the exact conditions under which compatible local records admit a global
section.
