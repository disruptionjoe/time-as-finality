# T477: Coarse-Graining Budget-Index Gate

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T10: Finality Superselection Rule](T10-finality-superselection-rule.md)
- [T29: Projection-Obstruction Schema](T29-projection-obstruction-schema.md)
- [valid-coarse-graining-as-finality-admissibility](../open-problems/valid-coarse-graining-as-finality-admissibility.md)
- [T467: Valid Coarse-Graining Admissibility Gate](T467-valid-coarse-graining-admissibility-gate.md)
- [T468: Coarse-Graining Positive-Control Independence](T468-coarse-graining-positive-control-independence.md)
- [T469: Coarse-Graining Task-Naturalness Gate](T469-coarse-graining-task-naturalness-gate.md)
- [T471: Coarse-Graining Multivalued Fixture Gate](T471-coarse-graining-multivalued-fixture-gate.md)

## Question

Is the repaired valid-coarse-graining packet genuinely indexed to the declared
observer budget, or did T469/T471 create a fixed global whitelist of admissible
relations?

## Setup

T477 evaluates the same finite four-holder record universe under two nested
observer budgets:

- `three_holder_budget`: fields 0, 1, and 2 are accessible.
- `four_holder_budget`: fields 0, 1, 2, and 3 are accessible.

The gate checks that three-holder positive controls persist under expanded
access, that a boundary-pair record using holder 3 is admitted only when holder
3 is inside the declared access boundary, and that cheap arithmetic,
label-restatement, microstate identity, and observer-creates-truth controls
remain blocked under expanded access.

## Success Criteria

T477 succeeds if it:

- admits the three-holder finality-band and support-count positives under both
  budgets;
- rejects `boundary_pair_status` as inaccessible under the three-holder budget;
- admits `boundary_pair_status` under the four-holder budget;
- keeps cheap arithmetic and label-restatement controls blocked under the
  expanded budget;
- keeps microstate identity blocked even under full access;
- keeps observer-creates-truth overread blocked;
- leaves claim status, public posture, North Star, roadmap, README, hard
  policy, and cross-repo truth untouched.

## Failure Criteria

T477 fails if it:

- treats access expansion as global claim support rather than an
  observer-indexed admission;
- loses the already admitted three-holder positives under a larger budget;
- admits cheap arithmetic or label restatement because access is expanded;
- admits microstate identity as a valid coarse-graining;
- promotes D1, T10, T29, Observer Theory, valid coarse-graining, or any
  physics/consciousness claim.

## Result

Implemented as T477 v0.1.

Verdict:

```text
BUDGET_INDEX_GATE_BUILT_OBSERVER_INDEXED_NO_PROMOTION
```

The repaired valid-coarse-graining packet is observer-budget indexed. Expanded
access can admit a new finality-natural boundary-pair record task, but it does
not admit arbitrary cheap arithmetic, label restatement, microstate identity,
or observer-creates-truth overread. This is a budget-index guardrail only, not
an Observer Theory equivalence theorem, D1/T10/T29 promotion, claim upgrade, or
physics/consciousness result.
