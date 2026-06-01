# Tests

The project is useful only if claims can be formalized, stressed, or broken.

## Test Index

| ID | Test | Target claims | Status |
| --- | --- | --- | --- |
| [T1](tests/T1-record-graph-temporal-reconstruction.md) | Record graph temporal reconstruction | C1, D1, D2 | open |
| [T2](tests/T2-quantum-measurement-record-finality.md) | Quantum measurement record finality | Q1, G2 | open |
| [T3](tests/T3-spacelike-events-no-global-commit-order.md) | Spacelike events and no global commit order | R1, G2 | open |
| [T4](tests/T4-black-hole-causal-access-boundary.md) | Black-hole causal access boundary | B1, G2 | open |
| [T5](tests/T5-thermodynamic-record-support.md) | Thermodynamic record support | D1, C1 | open |

## Minimum Compatibility Constraints

Any formalization must:

- preserve no-signalling;
- preserve proper time and invariant interval structure;
- distinguish physical record-stability from human belief;
- distinguish local access loss from physical reversal;
- not treat decoherence as a complete measurement-problem solution;
- not derive the thermodynamic arrow by assertion;
- not require a hidden universal present.

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
