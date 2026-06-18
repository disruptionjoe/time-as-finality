# T21: Bell Contextuality Finality

## Target Claims

- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [A1: Distributed Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [T13: Finality Sheaf Cohomology](T13-finality-sheaf-cohomology.md)
- [T20: Consensus-Record Theorem Transfer](T20-consensus-record-theorem-transfer.md)
- [T22: D1 Physical Reduction Map](T22-d1-physical-reduction-map.md)

## Origin

The v2 sprint identified the H1/sheaf obstruction as the repo's most
underexploited object and proposed a Bell/CHSH mapping as the most direct
physical referent.

T21 implements the finite contextuality version of that mapping.
The v0.2 extension adds probability-bearing CHSH scores.

## Setup

Use four CHSH-style measurement contexts:

```text
A0B0 = same
A0B1 = same
A1B0 = same
A1B1 = different
```

Each context has local finality sections: assignments of outcomes that satisfy
that context. The test then asks whether one global assignment to `A0`, `A1`,
`B0`, and `B1` can satisfy all four contexts.

## Success Criteria

- Each local context has valid finality sections.
- Contexts are compatible on named single-setting overlaps.
- No global assignment satisfies all four context constraints.
- The parity-product witness matches the CHSH-style contradiction:
  observed product `-1`, noncontextual global assignment product `+1`.
- The result states the guardrail: finite contextuality certificate, not a
  quantum-amplitude simulation.
- The probability extension compares classical, quantum Tsirelson, and PR-box
  CHSH scores.

## Failure Criteria

- Any local context lacks a valid finality section.
- A global assignment exists.
- The contradiction depends on probability values rather than the parity
  structure.
- The model claims to derive Bell probabilities or quantum mechanics.
- The quantum target fails to exceed the classical bound or violates the
  Tsirelson bound.

## Status

Implemented as T21 v0.1 parity certificate plus v0.2 probability-bearing CHSH
extension.

## T22 Boundary

[T22](T22-d1-physical-reduction-map.md) clarifies what T21 does and does not
establish for D1. T21 gives local finality without global assignment a
Bell/CHSH-style physical referent. It does not make all D1 dimensions
physical observables.

In the T22 audit, holder redundancy is the only D1 dimension with an
executable system-environment reduction check. Branch support remains formal
only, even though T21 and T13 show why local sections may fail to glue into a
global section.

## Reproduction

```bash
python -m unittest tests.test_bell_contextuality_finality -v
python -m models.run_t21
```

## T22 Follow-On

[T22](T22-d1-physical-reduction-map.md) complements the CHSH/global-section
result by auditing D1's physical observables. T21 shows why local finality
need not imply a global assignment; T22 asks what the D1 axes would reduce to
in a physical record substrate and implements the first holder-redundancy
comparison.

## T23 Boundary

[T23](T23-invariant-preserving-transformations.md) adds a general
invariant-transport interface, but it does not yet encode the T21 CHSH/sheaf
obstruction as an IPT obstruction. That is a next representation-theorem
target: determine whether global-section failure is a typed obstruction in
the same sense as the weak-quorum boundary.

## T24 Follow-On

[T24](T24-d1-multiscale-observer-field.md) translates the local-versus-global
lesson into D1 field language. A multiscale D1 field can have locally
satisfiable patches while no global assignment exists, so field-valued D1
inherits the same caution: local finality is not automatically global
finality.

## T25 Boundary

[T25](T25-minimal-d1-generalization.md) treats the CHSH-style obstruction as a
finite patch/gluing boundary first. Full sheaf language is not discarded, but
the simpler graph-indexed restriction system is the smallest object earned by
the current executable evidence.
