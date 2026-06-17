# T21: Bell Contextuality Finality

## Target Claims

- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [A1: Distributed Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [T13: Finality Sheaf Cohomology](T13-finality-sheaf-cohomology.md)
- [T20: Consensus-Record Theorem Transfer](T20-consensus-record-theorem-transfer.md)

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

## Reproduction

```bash
python -m unittest tests.test_bell_contextuality_finality -v
python -m models.run_t21
```
