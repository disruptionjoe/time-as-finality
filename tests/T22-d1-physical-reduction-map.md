# T22: D1 Physical Reduction Map

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [T2: Quantum Measurement Record Finality](T2-quantum-measurement-record-finality.md)
- [T21: Bell Contextuality Finality](T21-bell-contextuality-finality.md)

## Origin

The v2 idea sprint identified a hard gap in D1: each dimension needs an
explicit candidate physical observable, substrate assumptions, covariance or
frame-dependence status, and falsification condition.

T22 implements that audit and executes the strongest available reduction:
D1 holder redundancy compared with a Quantum-Darwinism-style count of
independent informative environment fragments.

## Setup

Use a binary pointer system with five environment fragments:

```text
E1: accessible, informative, independent, left branch
E2: accessible, informative, independent, right branch
E3: accessible, informative, correlated duplicate of E1
E4: informative but inaccessible to the observer
N1: accessible noise fragment
```

Compute:

- D1 accessible support;
- D1 holder redundancy;
- D1 independent branch support;
- D1 reversal cost;
- raw informative fragment count;
- independent informative fragment count.

## Success Criteria

- Every D1 dimension receives a reduction-map entry.
- Every entry states assumptions, frame status, and falsification condition.
- D1 holder redundancy equals independent informative fragment count.
- Raw informative fragment count can exceed holder redundancy when a fragment
  is a correlated duplicate.
- Inaccessible informative fragments are excluded from accessible support.
- The result states the guardrail: this is not a derivation of D1 from quantum
  mechanics.

## Failure Criteria

- Raw fragment count and D1 holder redundancy are treated as identical.
- Inaccessible fragments count as accessible support.
- Correlated duplicates raise independent holder redundancy.
- Reversal cost is presented as already physically reduced.
- The model claims detector-level quantum Darwinism or Bell-test realism.

## Status

Implemented as T22 v0.1.

## Reproduction

```bash
python -m unittest tests.test_d1_physical_reduction_map -v
python -m models.run_t22
```
