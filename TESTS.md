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
| [T6](tests/T6-snowball-record-finality.md) | Snowball record finality | A1, D1, Q1 | open |
| [T7](tests/T7-overlapping-causal-domains.md) | Overlapping causal domains | R1, B1, S1 | open |
| [T8](tests/T8-observer-renderer-toy-model.md) | Observer renderer toy model | D2, G3 | open |
| [T9](tests/T9-emergence-laboratory.md) | Emergent records across reversible and irreversible local dynamics | D1, C1, T5 | implemented: comparative success |
| [T16](tests/T16-spacetime-aggregation.md) | Spacetime aggregation toy model | S1, H5, R1 | implemented: finite gluing and obstruction witnesses |
| [T17](tests/T17-consensus-finality-crosswalk.md) | Consensus finality crosswalk | A1, D1 | implemented: collapse maps and bounded impossibility witness |

## Minimum Compatibility Constraints

Any formalization must:

- preserve no-signalling;
- preserve proper time and invariant interval structure;
- distinguish physical record-stability from human belief;
- distinguish local access loss from physical reversal;
- not treat decoherence as a complete measurement-problem solution;
- not derive the thermodynamic arrow by assertion;
- not require a hidden universal present;
- not treat probabilistic consensus finality as absolute truth.
- not deny remote observation as causal record access.
- not treat observer rendering as mind-created matter.

## Executable Suite

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t1
python -m models.run_emergence_lab
python -m models.run_t16
python -m models.run_t17
```

The suites use only Python's standard library. Evidence records:

- [T1 v0.1 Results](results/T1-v0.1-results.md)
- [Emergence Laboratory v0.1 Results](results/emergence-lab-v0.1-results.md)
- [Spacetime Aggregation v0.1 Results](results/spacetime-aggregation-v0.1-results.md)
- [Consensus Finality Crosswalk v0.1 Results](results/consensus-finality-crosswalk-v0.1-results.md)

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
