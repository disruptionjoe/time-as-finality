# T247: Attribution Strong-Subsumption Theorem

## Verdict

Implemented/verdict closed at the bounded finite-witness level.

T247 normalizes the tracked `models/attribution_strong_subsumption.py` model into
the test registry. It promotes the T230/T235/T240 witness-by-witness gate-2
closures into one bounded universal statement over the unified off-`nu` witness
family `F`: every relabel-stable local attribution invariant on `F` that
separates a same-`nu` pair is reproduced by the join enlargement
`nu_join = (nu_prime, nu_struct, nu_cocycle)`.

This is a test-level bounded negative only. It does not move TF1, criterion 6,
claim status, canon status, public posture, or any LossKernel ledger tier.

## Target Claims

- TF1
- T220
- T230
- T235
- T240
- T99
- T107
- T108
- T127

## Setup

The model builds a finite family of 8 same-`nu` cases spanning exactly three
off-`nu` structural strata:

- source field value, absorbed by `nu_prime` from T230;
- source gluing relation, absorbed by `nu_struct` from T235;
- transition cocycle over a finite cover, absorbed by `nu_cocycle` from T240.

It then enumerates every separation pattern a relabel-stable local invariant can
induce on the finite structural-fingerprint set. With 8 distinct fingerprints,
that is 4,140 set partitions.

## Result

`results/attribution-strong-subsumption/T247-results.json` records:

- family size: 8;
- distinct `nu` signatures: 1;
- distinct structural fingerprints: 8;
- separation patterns enumerated: 4,140;
- separating patterns: 4,139;
- route-B clears found: 0;
- all separating patterns absorbed by `nu_join`: true;
- trichotomy exhaustive on the family: true;
- nonvacuity injector clears: true.

The per-stratum absorber census is:

| Absorber | Pair count |
| --- | ---: |
| `nu_prime` | 16 |
| `nu_struct` | 8 |
| `nu_cocycle` | 4 |
| `none` | 0 |

## Success Criteria

- All cases share one `nu` signature while spanning the three intended off-`nu`
  strata.
- The three-stratum trichotomy is exhaustive on `F`.
- The refinement chain from `nu_prime` to `nu_struct` to `nu_cocycle` holds.
- Every separating partition is reproduced by `nu_join`.
- The harness can report a clear on a synthetic non-absorbed injector, so the
  negative is not a constant-no artifact.
- Imported T230/T235/T240 objects are used by object identity, not retuned.

## Failure Criteria

T247 fails if any relabel-stable local invariant on `F` separates a same-`nu`
pair whose separation is not reproduced by `nu_join`, or if the family contains
a fourth off-`nu` structural stratum not covered by field, gluing, and cocycle.

## Known Physics Constraints

None. This is a finite typed-machinery audit over hand-built attribution cases.
No physics, geometry, continuum, curvature, connection, quantum, gravity,
hardness, scale, or public-posture claim is earned.

## Contribution Needed

To extend this beyond the finite family, build a categorical decomposition
theorem showing that arbitrary typed-lossy morphisms decompose into admissible
off-`nu` strata with no fourth non-absorbable stratum. The orthogonal criterion-6
surface is the kappa map-between-absorbers line, not another same-neighbor-data
LossKernel search.

## Reproduction

```bash
python -m pytest tests/test_attribution_strong_subsumption.py -q
python -m models.attribution_strong_subsumption
```
