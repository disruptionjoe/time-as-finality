# T2: Quantum Measurement Record Finality

## Target Claims

- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [G2: Not A Replacement Theory](../guardrails/G2-not-a-replacement-theory.md)

## Setup

T2 v0.1 uses a simple measurement scenario:

- a system qubit `S`;
- an apparatus pointer qubit `A`;
- three environment fragments `E1`, `E2`, and `E3`;
- four observers with different access to records.

The interaction chain is:

```text
CNOT(S -> A)
CNOT(A -> E1)
CNOT(A -> E2)
CNOT(A -> E3)
```

The pointer basis is explicitly `computational_z`. The model represents when
records become stable, redundant, and accessible without selecting a collapse
outcome.

## Success Criteria

- The test clarifies what "under-finalized" means without treating the quantum state as unreal.
- The test distinguishes decoherence from a full solution to the measurement problem.
- No-signalling is preserved.
- Basis-dependence / pointer-basis questions are explicit.

## Failure Criteria

- The model smuggles in collapse.
- The model reduces to naive hidden variables.
- The model adds no clarity beyond standard decoherence language.
- The model implies faster-than-light finality transfer.

## Contribution Needed

Extend T2 from ideal CNOT records to a noisy system-apparatus-environment
model with partial scattering, nonideal detector access, and a dynamically
selected pointer basis.

## T2 v0.1 Result

Implemented as T2 v0.1.

The model computes:

- reduced system-apparatus pointer coherence;
- fragment mutual information;
- Quantum-Darwinism-style environmental `R_delta`;
- observer-relative D1 profiles;
- an inverse-operation reversal-cost proxy.

Main result:

```text
after CNOT(A -> E1): pointer coherence = 0.0
after CNOT(A -> E3): environment R_delta = 3
outside observer D1 = (0, 0, 0, 0)
```

This gives Q1 a concrete decohered-but-inaccessible case. Decoherence and
environmental redundancy can exist in the model while an observer with no
access has no finalized record.

The result remains narrow. It does not solve the measurement problem, derive
Born probabilities, or model noisy detectors.

## T23 Follow-On

[T23](T23-invariant-preserving-transformations.md) uses T2 as a source for an
invariant-preserving transformation:

```text
T2 global measurement state
  -> T2 local observer D1 view
  -> T22 reduction schema
```

The transported invariant is the `computational_z` pointer basis. The result
does not make T2 equivalent to T22; it only shows that this finite measurement
model can supply source and intermediate objects for the IPT kernel.

## Reproduction

```bash
python -m unittest tests.test_quantum_measurement_finality -v
python -m models.run_t2
```
