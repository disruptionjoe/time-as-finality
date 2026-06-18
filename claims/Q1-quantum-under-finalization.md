# Q1: Quantum Under-Finalization

## Claim

Quantum states can be real but not yet finalized as classical records in a particular observer-environment context.

## Class

Conjecture.

## Status

Partially supported.

## What This Does Not Claim

- It does not say quantum states are unreal.
- It does not say human consciousness collapses the wavefunction.
- It does not say decoherence alone solves the measurement problem.
- It does not restore naive local hidden variables.
- It does not allow faster-than-light signalling.

## Why It Might Be True

The quantum/classical transition is deeply tied to record formation, decoherence, pointer bases, environmental redundancy, and observer access. "Under-finalized" may help distinguish real quantum constraint from settled classical fact.

For entanglement, the safe finality chain is:

```text
entangled joint state
  -> local measurement interaction
  -> local record formation
  -> decoherence / environmental redundancy
  -> observer-relative finality
  -> later causal comparison
  -> globally reconciled correlation record
```

The key distinction is that an entangled joint constraint can be real before separated local observers share a classical finalized record. Shared classical finality requires causal reconciliation. The correlation is not a controllable faster-than-light message.

Proof-carrying language may help here: later comparison can certify a nonclassical joint constraint without implying that either local observer had full access to the global state or a hidden local answer in advance.

## How It Could Fail

- It adds no clarity beyond decoherence or quantum Darwinism.
- It smuggles in collapse without saying so.
- It cannot handle basis-dependence.
- It violates Bell/no-signalling constraints.
- It treats a later correlation record as if it were an earlier local hidden variable.
- It turns proof or verification language into an encrypted-message metaphor for entanglement.

## Tests

- [T2: Quantum Measurement Record Finality](../tests/T2-quantum-measurement-record-finality.md)
- [T6: Snowball Record Finality](../tests/T6-snowball-record-finality.md)
- [T21: Bell Contextuality Finality](../tests/T21-bell-contextuality-finality.md)
- [T22: D1 Physical Reduction Map](../tests/T22-d1-physical-reduction-map.md)
- [T23: Invariant-Preserving Transformations](../tests/T23-invariant-preserving-transformations.md)

## T21 Result

[T21](../tests/T21-bell-contextuality-finality.md) gives Q1 a finite
contextuality model. Four CHSH-style local measurement contexts each have
valid local finality sections, but no global assignment satisfies all
contexts.

This supports the narrow under-finalization claim: local classical records can
be finalized in their own measurement contexts while a single global
noncontextual record assignment remains unavailable. The result is structural,
not a detector-level simulation.

The probability-bearing extension compares three CHSH regimes: classical
noncontextual score `2`, quantum Tsirelson score `2*sqrt(2)`, and PR-box
no-signalling score `4`. This sharpens Q1's claim: quantum contextuality sits
between global classical finality and post-quantum no-signalling consistency.
- [Proof-Carrying Record Finality](../open-problems/proof-carrying-record-finality.md)

## T22 Result

[T22](../tests/T22-d1-physical-reduction-map.md) gives Q1 the first executable
comparison requested by the quantum-Darwinism neighbor. In a binary
system-environment toy model, each informative environment fragment has
`I(S;E_i) = 1.0` bit and the noise fragment has `I(S;N1) = 0.0`.

With delta `0.1`, the information threshold is `0.9` bits. Raw accessible
environmental redundancy counts `E1`, `E2`, and `E3`, for a value of `3`.
After quotienting the correlated duplicate `E3` with `E1`, the
independence-corrected accessible redundancy is `2`, matching D1 holder
redundancy.

This partially supports Q1 only as a record-finality vocabulary for
environmental redundancy. It does not simulate quantum amplitudes,
decoherence dynamics, detector noise, or collapse.

## T2 v0.1 Result

[T2](../tests/T2-quantum-measurement-record-finality.md) extends T22 into a
small dynamical measurement model:

```text
S -> A -> E1, E2, E3
```

using reversible CNOT interactions in the `computational_z` pointer basis.
The model computes reduced pointer coherence, fragment mutual information,
environmental `R_delta`, and observer-relative D1 profiles.

The main positive result is a decohered-but-inaccessible case. After the first
environment copy, pointer coherence is `0.0`; after all copies,
environmental `R_delta` is `3`. But an outside observer with no access has:

```text
D1 = (0, 0, 0, 0)
```

This supports Q1's narrow claim that "decohered in the pointer basis" and
"final as a classical record for this observer" are distinct predicates in
the toy substrate. It also preserves the guardrail: T2 uses unitary dynamics
only and never selects a collapse outcome.

## T23 Result

[T23](../tests/T23-invariant-preserving-transformations.md) turns the T2 to
T22 quantum bridge into a typed invariant-preserving reduction:

```text
T2 global measurement state
  -> T2 local observer D1 view
  -> T22 reduction schema
```

The composition preserves:

```text
pointer_basis = computational_z
```

and the second reduction preserves holder redundancy, accessible support, and
observer-access indexing. This supports Q1 as part of a broader invariant
transport program, while keeping the same limits: no collapse, no Born-rule
derivation, no detector-level model, and no claim that quantum measurement is
equivalent to the other T23 domains.

## Contribution Needed

Extend T2 from ideal CNOT records to noisy scattering, detector inefficiency,
partial decoherence, and dynamically selected pointer bases. Then compare
"under-finalized classical record" with decoherence, quantum Darwinism,
relational QM, consistent histories, many-worlds, and QBism.
