# T468: Coarse-Graining Positive-Control Independence

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T10: Finality Superselection Rule](T10-finality-superselection-rule.md)
- [T29: Projection-Obstruction Schema](T29-projection-obstruction-schema.md)
- [valid-coarse-graining-as-finality-admissibility](../open-problems/valid-coarse-graining-as-finality-admissibility.md)
- [T467: Valid Coarse-Graining Admissibility Gate](T467-valid-coarse-graining-admissibility-gate.md)

## Question

Did T467's two admitted positive controls provide independent support for the
valid-coarse-graining admission gate, and is bounded observer certification
enough without a finality-native task?

## Setup

T468 compares the two T467 positive-control shapes:

- finality band: all-zero, all-one, and unsettled holder configurations;
- local count: the number of one-valued finalized holders.

It checks these partitions across binary holder widths and then probes a cheap
accessible xor partition that satisfies the mechanical access and cost fields
but lacks an independently declared finality-native task.

## Success Criteria

T468 succeeds if it:

- identifies whether the T467 positive controls are extensionally independent
  in the binary two-holder fixture;
- finds the minimum binary holder width where the two controls diverge;
- shows whether the finality-native task requirement is load-bearing;
- leaves claim status, public posture, and North Star untouched.

## Failure Criteria

T468 fails if it:

- treats the T467 positive controls as independent when their partitions are
  identical;
- claims that bounded computation alone selects valid finality
  coarse-grainings;
- promotes D1, T10, T29, Observer Theory, valid coarse-graining, or any
  physics/consciousness claim.

## Result

Implemented as T468 v0.1.

Verdict:

```text
T467_POSITIVE_CONTROLS_COLLAPSE_TASK_GATE_LOAD_BEARING
```

T467's two admitted positive controls are extensionally identical on the binary
two-holder fixture. They first separate at three holders. The cheap-xor probe
also shows that finality-task semantics is load-bearing: bounded access and
cost alone do not select a valid finality coarse-graining.
