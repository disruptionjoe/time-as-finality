# T18: Finality Direction Theorem

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [Arrow of Time as Constructor Theorem](../open-problems/arrow-of-time-as-constructor-theorem.md)

## Origin

Direction 3 from the 42-persona convergence map: temporal direction may be
derivable from impossible transformations on finalized records, without
asserting a thermodynamic boundary condition.

## Setup

Model finite states carrying a D1 vector:

```text
(accessible support, holder redundancy, branch support, reversal cost)
```

A transformation is admissible when no D1 dimension decreases.

Strict finalization means:

```text
after >= before componentwise
and at least one component strictly increases
```

The lab tracks a separate thermodynamic-cost proxy but does not use it to
orient transformations.

## Success Criteria

- Strict finalization edges form an acyclic graph.
- The reverse of every strict finalization edge is impossible under the same
  constructor rule.
- The set of impossible transformations is not closed under reversal.
- At least one strict finalization witness does not require an increase in the
  thermodynamic-cost proxy.
- The resulting arrow is partial rather than a hidden total order.

## Failure Criteria

- Strict finalization admits a directed cycle.
- A strict finalization edge has an admissible reverse.
- Direction depends on the thermodynamic-cost proxy.
- The model silently replaces coordinate time, proper time, or entropy
  increase.
- The finality relation collapses into a total order.

## Known Constraints

This is a conditional finite theorem check. It derives a finality direction
from D1-monotone admissibility. It does not prove that physical systems
instantiate this constructor rule.

## Status

Implemented as T18 v0.1.

## Reproduction

```bash
python -m unittest tests.test_finality_direction_theorem -v
python -m models.run_t18
```
