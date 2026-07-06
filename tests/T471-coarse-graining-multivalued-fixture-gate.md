# T471: Coarse-Graining Multivalued Fixture Gate

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T10: Finality Superselection Rule](T10-finality-superselection-rule.md)
- [T29: Projection-Obstruction Schema](T29-projection-obstruction-schema.md)
- [valid-coarse-graining-as-finality-admissibility](../open-problems/valid-coarse-graining-as-finality-admissibility.md)
- [T467: Valid Coarse-Graining Admissibility Gate](T467-valid-coarse-graining-admissibility-gate.md)
- [T468: Coarse-Graining Positive-Control Independence](T468-coarse-graining-positive-control-independence.md)
- [T469: Coarse-Graining Task-Naturalness Gate](T469-coarse-graining-task-naturalness-gate.md)

## Question

Does the T469 repaired valid-coarse-graining packet survive a non-binary record
alphabet, or was the repair an artifact of binary holder values?

## Setup

T471 evaluates the T469 packet shape over binary and ternary finite record
states. The observer can access the first three holders; a fourth holder remains
outside the access boundary for hidden-field hostile controls.

For each alphabet, the packet uses two positive controls:

- `finality_band`: all observed holders carry one stable value, or the observed
  holder set is unsettled;
- `support_count`: count of observed holders carrying a nonzero finalized value.

The packet must also block:

- a cheap accessible modular-sum partition with a finality-task label asserted;
- a bounded label-restatement lookup;
- a hidden fourth-field task;
- microstate identity;
- observer-creates-truth overread.

## Success Criteria

T471 succeeds if it:

- admits both the binary reference packet and the ternary packet;
- shows ternary finality band and support count are independent positive
  controls;
- blocks the cheap modular-sum hostile control even though it passes the old
  mechanical base gate;
- blocks label restatement, hidden-field, microstate, and observer-creates-truth
  controls;
- leaves claim status, public posture, North Star, roadmap, README, and
  cross-repo truth untouched.

## Failure Criteria

T471 fails if it:

- treats binary-only evidence as enough for the repaired packet;
- lets a cheap arithmetic partition pass because it is accessible and low cost;
- treats label restatement or microstate identity as task-natural finality;
- accepts inaccessible fields or observer-creates-truth overreads;
- promotes D1, T10, T29, Observer Theory, valid coarse-graining, or any
  physics/consciousness claim.

## Result

Implemented as T471 v0.1.

Verdict:

```text
MULTIVALUED_FIXTURE_GATE_BUILT_NO_PROMOTION
```

The T469 packet shape survives the ternary alphabet stress test while the
hostile controls remain blocked. This is an alphabet-stress gate only, not an
Observer Theory equivalence theorem, D1/T10/T29 promotion, claim upgrade, or
physics/consciousness result.
