# Finite-Closed Extraction-Resource Measure v0.1 Results

- Artifact: `finite-closed-extraction-resource-measure-v0.1`
- Model: `models/finite_closed_extraction_resource_measure.py`
- Test: `tests/test_finite_closed_extraction_resource_measure.py`
- Report: `technical-reports/TECHNICAL-REPORT-finite-closed-extraction-resource-measure-v0.1.md`
- Status: support artifact only; no claim promotion

## Verdict

The v0.1 support artifact formalizes the single-instance extraction-resource
ceiling for the finite-closed capability-boundary scope theorem candidate.

If a separating datum is determined by a finite closed code `F`, then a finite
lookup extractor exists:

```text
E_I : im(F) -> K
E_I(F(c)) = d(c)
L(I) = |im(F)| <= |C| < infinity
```

Therefore a single finite closed instance is declared/crackable unless the run
adds a family-level resource theorem (`E1`) or a forcing assumption (`E2`). A
finite budget by itself remains an `E0` declaration.

## Witness Checks

The model compresses three existing witness shadows into the shared normal form:

| Witness | Boundary present | Closed code determines datum | Single-instance upper bound | Gap mode |
| --- | --- | --- | --- | --- |
| T411 departed-record shadow | yes | yes | 2 | `E0_declared_or_crackable` |
| T413 grand-coalition shadow | yes | yes | 2 | `E0_single_instance_or_E1_nonatomic_limit` |
| T417 quadratic-residuosity shadow | yes | yes | 2 | `E2_hardness_assumption_plus_E1_family_growth` |

T417's illustrative family costs remain strictly increasing:

```text
[2, 6, 10, 28, 58]
```

This keeps T417's contribution in the correct place: not a single-instance
physical boundary, but a family-level computational boundary conditional on
QRA/factoring hardness.

## Verification

```bash
python -m pytest tests/test_finite_closed_extraction_resource_measure.py -q
python -m models.finite_closed_extraction_resource_measure
```

Expected focused test result: `5 passed`.

## Non-Movement

No `CLAIM-LEDGER.md`, `TESTS.md`, North Star, canon, public posture, or cross-repo
truth changed. The scope theorem remains a candidate. The next internal work is
model-class formalization plus hostile review.
