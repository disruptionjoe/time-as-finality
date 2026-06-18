# Quantum Measurement Record Finality

## Abstract

T2 v0.1 upgrades the T22 reduction-map audit from a hand-declared
system-environment table into a small dynamical measurement model.

The lab uses reversible unitary CNOT interactions in an explicit pointer
basis:

```text
system qubit S -> apparatus pointer A -> environment fragments E1, E2, E3
```

It computes reduced system-apparatus pointer coherence, fragment mutual
information, Quantum-Darwinism-style environmental redundancy, and
observer-relative D1 profiles.

The result is a partial success for Q1. The model produces a concrete
decohered-but-inaccessible case: after environment copying, pointer coherence
is zero and environmental `R_delta` is `3`, but an outside observer with no
access has D1 profile `(0, 0, 0, 0)`. This shows that D1 adds an
observer-access distinction beyond decoherence and raw environmental
redundancy in this toy substrate.

The result is not a solution to the measurement problem. It uses unitary
dynamics only, never selects a collapse outcome, and does not derive Born
probabilities.

## 1. Model

Qubits:

```text
S  = system qubit
A  = apparatus pointer
E1 = environment fragment 1
E2 = environment fragment 2
E3 = environment fragment 3
```

Initial state:

```text
(|0>_S + |1>_S) / sqrt(2)
```

with `A`, `E1`, `E2`, and `E3` initialized to `|0>`.

Pointer basis:

```text
computational_z
```

Interaction chain:

| Step | Interaction | Meaning |
| ---: | --- | --- |
| 1 | `CNOT(S -> A)` | apparatus pointer record |
| 2 | `CNOT(A -> E1)` | first environmental record |
| 3 | `CNOT(A -> E2)` | second environmental record |
| 4 | `CNOT(A -> E3)` | third environmental record |

All interactions are reversible. The named reversal-cost proxy counts inverse
operations needed to put an observer below its reconstruction threshold.

## 2. Decoherence And Redundancy

T2 tracks the off-diagonal coherence between the correlated pointer states
`|S=0,A=0>` and `|S=1,A=1>` after tracing over environment fragments.

| Step | Pointer coherence | Environment `R_delta` |
| ---: | ---: | ---: |
| 1 | `0.5` | `0` |
| 2 | `0.0` | `1` |
| 3 | `0.0` | `2` |
| 4 | `0.0` | `3` |

Decoherence occurs after the first environment copy. Redundancy continues to
grow as additional fragments record the apparatus pointer.

At the final step, each record-bearing qubit has one bit of mutual
information with the system in the pointer basis:

| Record | I(S;record) |
| --- | ---: |
| A | `1.0` |
| E1 | `1.0` |
| E2 | `1.0` |
| E3 | `1.0` |

## 3. Observer Windows

T2 evaluates four observers against the same final global state:

| Observer | Access window | Threshold | Final D1 profile |
| --- | --- | ---: | --- |
| apparatus observer | `A` | 1 | `(1, 1, 1, 1)` |
| local lab observer | `A`, `E1` | 2 | `(2, 2, 1, 1)` |
| remote environment observer | `E2`, `E3` | 2 | `(2, 2, 1, 1)` |
| outside observer | none | 1 | `(0, 0, 0, 0)` |

The tuple order is:

```text
(accessible support, holder redundancy, branch support, reversal cost)
```

The outside observer is the key divergence case. The global measurement chain
is decohered in the pointer basis and environmental redundancy is high, but
that observer has no accessible finalized record.

## 4. D1 Versus Quantum Darwinism

Quantum-Darwinism-style redundancy grows from `0` to `3` as environment
fragments are copied:

```text
R_delta total = 0, 1, 2, 3
```

D1 agrees that redundant records exist for observers who can access enough
fragments. But D1 keeps two distinctions that the raw redundancy count does
not:

- observer access: the outside observer has no finality despite global
  decoherence and `R_delta = 3`;
- branch support: all redundant records descend from the same pointer
  measurement branch, so final observer branch support remains `1`.

This is a narrow positive result for D1: the model shows why "decohered" and
"final for this observer" are not identical predicates.

## 5. Interpretation Boundary

T2 uses a unitary/no-collapse reading as a guardrail. The global state remains
a coherent entangled state under reversible interactions. Finality is computed
from reduced states, pointer-basis records, and observer access windows.

This does not endorse any interpretation of quantum mechanics. It only shows
that Q1 can be stated without selecting a collapse outcome.

## 6. Claim Impact

Q1 should remain `partially_supported`. T21 supplies the contextuality
boundary; T22 supplies the first environmental redundancy bridge; T2 v0.1
adds a dynamical measurement substrate and finds a decohered-but-inaccessible
case.

D1 should remain `weakened`. T2 strengthens accessible support and holder
redundancy as substrate-generated quantities, but branch support and reversal
cost are still proxy-level in this model.

## 7. Limits

- The pointer basis is declared, not dynamically selected from a Hamiltonian.
- The environment copies are ideal CNOT records, not noisy scattering.
- The model does not derive Born probabilities.
- The reversal-cost proxy counts inverse operations, not thermodynamic work.
- Branch support is one because the toy model has one pointer-measurement
  root.
- No relativistic causal structure is modeled.

## 8. Reproduction

```bash
python -m unittest tests.test_quantum_measurement_finality -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t2
```

Machine-readable output:

- [results/quantum-measurement-finality-v0.1.json](results/quantum-measurement-finality-v0.1.json)

Human-readable result note:

- [results/quantum-measurement-finality-v0.1-results.md](results/quantum-measurement-finality-v0.1-results.md)
