# T30: Cross-Domain Projection-Obstruction Validation

## Purpose

T30 tests whether PO1 generalizes beyond the physics and GU no-go examples
that motivated it.

This is a hostile validation track. Success does not mean PO1 is confirmed
universally. Success means the repo has executable evidence about where PO1
works, where it fails, and where it should refuse to apply.

## Linked Claim

- [PO1: Projection-Obstruction Schema](../claims/PO1-projection-obstruction-schema.md)

## Hypotheses

| Hypothesis | Meaning |
| --- | --- |
| H0 | PO1 is domain-specific to GU/no-go style cases |
| H1 | PO1 applies to at least one non-physics inherited domain |
| H2 | PO1 applies across multiple unrelated domains with the same finite structure |
| H3 | PO1 requires modification to handle non-physics domains |
| H4 | PO1 is too broad or underconstrained to be useful |

## Implemented Cases

| Domain | Expected role | Expected classification |
| --- | --- | --- |
| Git merge conflict | clean positive | projection-created obstruction |
| Financial risk model | high-stakes positive | projection-created obstruction |
| Translator / poet | anti-overclaim boundary | no meaningful PO1 fit |

## Acceptance Criteria

- At least three non-physics domains are modeled.
- At least one case is a positive PO1 instance.
- At least one case is negative or boundary.
- H0-H4 receive explicit verdicts.
- PO1 receives a recommendation: strengthen, weaken, constrain, or retain.

## Test Structure

| Test | Assertion |
| --- | --- |
| `test_t30_has_at_least_three_non_physics_cases` | candidate coverage |
| `test_git_merge_is_positive_po1_instance` | Git supports PO1 |
| `test_financial_risk_is_positive_po1_instance` | financial-risk toy supports PO1 |
| `test_translator_poet_is_no_meaningful_po1_fit` | lost meaning alone does not support PO1 |
| `test_hypothesis_verdict_keeps_po1_constrained` | PO1 remains partially supported and constrained |
| `test_run_t30_analysis_shape` | JSON runner shape |

## Commands

```bash
python -m unittest tests.test_cross_domain_projection_obstruction_validation -v
python -m models.run_t30
```

## Artifacts

- `models/cross_domain_projection_obstruction_validation.py`
- `models/run_t30.py`
- `tests/test_cross_domain_projection_obstruction_validation.py`
- `results/cross-domain-projection-obstruction-validation-v0.1.json`
- `results/cross-domain-projection-obstruction-validation-v0.1-results.md`
- `TECHNICAL-REPORT-cross-domain-projection-obstruction-validation-v0.1.md`

## Result

Implemented as T30 v0.1.

Best supported verdict:

```text
H2 with H4 admissibility constraints
```

Recommendation:

```text
Keep PO1 partially_supported, with stronger evidence inside that status and
an admissibility checklist for future examples.
```
