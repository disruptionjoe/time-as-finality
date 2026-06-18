# T22: D1 Physical Reduction Map

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [T2: Quantum Measurement Record Finality](T2-quantum-measurement-record-finality.md)
- [T21: Bell Contextuality Finality](T21-bell-contextuality-finality.md)

## Origin

The repo now has several results downstream of D1: T17/T20 connect D1 to
distributed consensus, T21 connects local finality without global assignment
to Bell/CHSH contextuality, T13 supplies a sheaf/global-section obstruction,
and T18 derives a model-relative finality direction.

T22 asks whether D1 itself has measurable physical content.

```text
Are D1's four dimensions physical observables, or only useful graph quantities?
```

## Setup

Build a reduction map for all four D1 dimensions:

- accessible support;
- holder redundancy;
- branch support;
- reversal cost.

For each dimension, record:

- candidate physical observable;
- substrate assumptions;
- Lorentz/frame-dependence status;
- supporting tests;
- falsification conditions;
- confidence level.

Then run one executable comparison in the strongest current location:
holder redundancy against a Quantum-Darwinism-style environmental redundancy
quantity in a small system-environment toy model.

The toy model uses:

- a binary pointer state `S0/S1` with one bit of entropy;
- environment fragments `E1`, `E2`, `E3`, `E4`, and `N1`;
- perfect pointer records in `E1`, `E2`, `E3`, and inaccessible `E4`;
- one noise fragment `N1` with zero mutual information;
- a declared observer access set `{E1, E2, E3, N1}`;
- a delta threshold of `0.1`, so the information threshold is `0.9` bits.

## Success Criteria

- The reduction map contains all four D1 dimensions.
- Every dimension has at least one falsification condition.
- Confidence levels use the explicit vocabulary:
  `physically supported`, `partially supported`, `formal only`,
  `failed/rejected`.
- The toy model computes mutual information for each environment fragment.
- D1 holder redundancy is compared with an R_delta-style environmental
  redundancy count.
- The result distinguishes raw fragment count from an independence-corrected
  redundancy count.
- The result states the guardrail that T22 does not derive D1 from quantum
  mechanics or prove quantum Darwinism.

## Failure Criteria

- Any D1 dimension lacks a candidate observable or falsification condition.
- The executable model silently treats raw environmental copies as independent
  holders when the scenario declares a shared independence class.
- The result claims all D1 dimensions are physically reduced.
- Reversal cost is asserted to equal thermodynamic work without a substrate
  model.
- The toy model is presented as a proof of quantum Darwinism.

## Status

Implemented as T22 v0.1.

## Reproduction

```bash
python -m unittest tests.test_d1_physical_reduction_map -v
python -m models.run_t22
```

## T23 Follow-On

[T23](T23-invariant-preserving-transformations.md) uses the T22 reduction
schema as the target of a quantum redundancy reduction:

```text
T2 local observer D1 view
  -> T22 reduction schema
```

The preserved invariants are pointer basis, holder redundancy, accessible
support, and observer-access indexing. This makes T22 part of a typed
transport kernel, but it does not improve T22's confidence levels for branch
support or reversal cost.
