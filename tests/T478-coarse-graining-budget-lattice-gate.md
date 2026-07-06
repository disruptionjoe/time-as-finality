# T478: Coarse-Graining Budget-Lattice Gate

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T10: Finality Superselection Rule](T10-finality-superselection-rule.md)
- [T29: Projection-Obstruction Schema](T29-projection-obstruction-schema.md)
- [valid-coarse-graining-as-finality-admissibility](../open-problems/valid-coarse-graining-as-finality-admissibility.md)
- [T467: Valid Coarse-Graining Admissibility Gate](T467-valid-coarse-graining-admissibility-gate.md)
- [T469: Coarse-Graining Task-Naturalness Gate](T469-coarse-graining-task-naturalness-gate.md)
- [T471: Coarse-Graining Multivalued Fixture Gate](T471-coarse-graining-multivalued-fixture-gate.md)
- [T477: Coarse-Graining Budget-Index Gate](T477-coarse-graining-budget-index-gate.md)

## Question

Does the repaired valid-coarse-graining packet behave coherently across a
finite observer-budget lattice, or did T477 only pass a single hand-picked
nested-budget chain?

## Setup

T478 evaluates a four-holder binary record universe across a finite access
budget lattice containing holder `0`:

- `budget_01`
- `budget_02`
- `budget_03`
- `budget_012`
- `budget_013`
- `budget_023`
- `budget_0123`

The gate checks pairwise finality-status positives, a boundary-pair positive,
three-holder join positives, cheap arithmetic hostile controls,
label-restatement hostile controls, microstate identity, and
observer-creates-truth overread.

## Success Criteria

T478 succeeds if it:

- preserves admitted finality-natural relations across every budget-inclusion
  edge;
- preserves prior admissions at incomparable-budget joins;
- explains every new join admission by newly accessible certified record
  fields;
- gives the same top-budget verdict independent of the access-expansion path;
- keeps cheap arithmetic, label-restatement, microstate identity, and
  observer-creates-truth controls blocked whenever they become accessible;
- leaves claim status, public posture, North Star, roadmap, README, hard
  policy, protected-license, and cross-repo truth untouched.

## Failure Criteria

T478 fails if it:

- loses an admitted finality-natural relation under a strictly larger observer
  budget;
- lets a join admit a relation whose certified fields did not become available;
- admits cheap arithmetic or label restatement merely because access expands;
- admits microstate identity as a valid coarse-graining;
- treats observer equivalencing as creating truth;
- promotes D1, T10, T29, Observer Theory, valid coarse-graining, or any
  physics/consciousness claim.

## Result

Implemented as T478 v0.1.

Verdict:

```text
BUDGET_LATTICE_GATE_BUILT_PATH_INDEPENDENT_NO_PROMOTION
```

The repaired coarse-graining packet is coherent across this finite
observer-budget lattice. Admitted finality-natural relations do not disappear
under access expansion; joins preserve prior admissions and admit only
relations whose certified fields become available; top-budget verdicts are
independent of the expansion path; cheap arithmetic, label restatement,
microstate identity, and observer-creates-truth controls remain blocked when
accessible.

This is an observer-indexed intake guardrail only. It does not prove that TaF
supplies Observer Theory's missing valid-coarse-graining criterion and earns no
D1/T10/T29, Observer Theory, global valid-coarse-graining, physics,
consciousness, claim-ledger, roadmap, README, public-posture, hard-policy, or
cross-repo movement.
