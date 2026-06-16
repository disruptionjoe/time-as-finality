# Tests

The project is useful only if claims can be formalized, stressed, or broken.

## Test Index

| ID | Test | Target claims | Status |
| --- | --- | --- | --- |
| [T1](tests/T1-record-graph-temporal-reconstruction.md) | Record graph temporal reconstruction | C1, D1, D2 | implemented: partial success |
| [T2](tests/T2-quantum-measurement-record-finality.md) | Quantum measurement record finality | Q1, G2 | open |
| [T3](tests/T3-spacelike-events-no-global-commit-order.md) | Spacelike events and no global commit order | R1, G2 | open |
| [T4](tests/T4-black-hole-causal-access-boundary.md) | Black-hole causal access boundary | B1, G2 | open |
| [T5](tests/T5-thermodynamic-record-support.md) | Thermodynamic record support | D1, C1 | structural benchmark implemented |
| [T9](tests/T9-emergence-laboratory.md) | Emergent records across reversible and irreversible local dynamics | D1, C1, T5 | implemented: comparative success |
| [T10](tests/T10-proof-carrying-metastable-finality.md) | Proof-carrying metastable finality | A1, D1, D2 | implemented: operational success, epistemic limit |
| [T11](tests/T11-compositional-finality.md) | Recursive compositional finality with inherited expression | C2, D1, D2 | implemented: evidence join, profile-level limit |
| [T12](tests/T12-coupling-profile-reconstruction.md) | Coupling-profile reconstruction | M1, D2 | implemented: observer-profile divergence without contradiction |
| [T13](tests/T13-signed-interfering-readout.md) | Signed and interfering readout | C3, D1, C2 | implemented: finality/readout separation |
| [T14](tests/T14-integrated-observer-context-finality.md) | Integrated observer-context finality | D1, D2, C2, C3, A1, M1 | implemented: typed-pipeline stress test |

## Minimum Compatibility Constraints

Any formalization must:

- preserve no-signalling;
- preserve proper time and invariant interval structure;
- distinguish physical record-stability from human belief;
- distinguish local access loss from physical reversal;
- not treat decoherence as a complete measurement-problem solution;
- not derive the thermodynamic arrow by assertion;
- not require a hidden universal present.

## Executable Suite

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t1
python -m models.run_emergence_lab
python -m models.run_proof_carrying_finality
python -m models.run_compositional_finality
python -m models.run_t12
python -m models.run_t13
python -m models.run_t14
```

The suites use only Python's standard library. Evidence records:

- [T1 v0.1 Results](results/T1-v0.1-results.md)
- [Emergence Laboratory v0.1 Results](results/emergence-lab-v0.1-results.md)
- [Proof-Carrying Metastable Finality v0.1 Results](results/proof-carrying-metastable-finality-v0.1-results.md)
- [Compositional Finality v0.1 Results](results/compositional-finality-v0.1-results.md)
- [T12 Coupling-Profile v0.1 Results](results/t12-coupling-v0.1-results.md)
- [T13 Signed Readout v0.1 Results](results/t13-signed-readout-v0.1-results.md)
- [T14 Integrated Finality v0.1 Results](results/t14-integrated-finality-v0.1-results.md)

## How To Add A Test

Create a file under `tests/` with:

```md
# T#: Test Name

## Target Claims

## Setup

## Success Criteria

## Failure Criteria

## Known Physics Constraints

## Contribution Needed
```
