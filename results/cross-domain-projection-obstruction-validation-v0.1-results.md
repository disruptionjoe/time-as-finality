# Cross-Domain Projection-Obstruction Validation v0.1 Results

## Commands

```bash
python -m models.run_t30
python -m unittest tests.test_cross_domain_projection_obstruction_validation -v
```

## Verdict

T30 provides hostile cross-domain evidence for PO1 using the revised candidate
set:

1. Git merge conflicts
2. Financial risk model
3. Translator / poet

Best supported hypothesis:

```text
H2 with H4 admissibility constraints
```

PO1 recommendation:

```text
Keep PO1 partially_supported, but strengthen the evidence within that status.
```

## Case Classification

| Domain | Case | Classification | PO1 support |
| --- | --- | --- | --- |
| Git merge conflict | `git_semantic_merge` | projection-created obstruction | yes |
| Financial risk model | `financial_tail_risk_model` | projection-created obstruction | yes |
| Translator / poet | `translator_poet_boundary` | no meaningful PO1 fit | no |

## Hypothesis Verdicts

| Hypothesis | Status |
| --- | --- |
| H0 | rejected in finite scope |
| H1 | supported |
| H2 | supported in finite scope |
| H3 | not supported by current candidates |
| H4 | partially supported as warning |

## Admissibility Constraints

Future PO1 evidence should require:

- projection independently motivated by the domain;
- richer system has a global section;
- restricted system is obstructed;
- forgotten structure resolves the restricted obstruction;
- lossy projection without obstruction is excluded;
- shared obstruction is excluded;
- non-definable projection is treated as a boundary;
- loss of meaning or nuance alone is not sufficient.

## Non-Claims

T30 does not prove PO1 is universal.

T30 does not prove external theorems about Git, financial systems, translation,
or poetry.

T30 does not provide financial advice, risk-management advice, legal advice,
or investment guidance.

T30 does not promote PO1 beyond `partially_supported`.
