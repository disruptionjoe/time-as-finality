# T516: Closed Form for the Isotropic 2-Shareability Wall

## Target Claims

No claim-ledger target. Closes honest-limit #1 of the qudit ladder result
("confirm `F_share = 0.670` against a closed form").

## Setup

The qudit ladder computed the isotropic 2-shareability wall by POCS (a tolerance
verdict, not a certified value). T516 supplies the closed form and lets an
independent POCS be the arbiter.

```
F_share(d) = (d + 1) / (2 d)          visibility form: v_share(d) = (d+2)/(2(d+1))
```

the symmetric-extendibility boundary for isotropic states (Johnson & Viola, PRA
88, 032323 (2013); arXiv 0906.5255) in the singlet-fraction convention.

## Success Criteria

- Structural: `F_share(d) > 1/d` for all `d`; monotone decreasing, `-> 1/2`.
- Independent POCS brackets the wall just below/above the closed form and
  contains it at d = 2 (0.750), 3 (0.667), 4 (0.625). (POCS iterations scale
  with `d^3`; d=4 needs ~1500.)
- `F_share(3) = 2/3 = 0.6667`, matching the ladder's POCS value 0.670.

## Verdict

`ISOTROPIC_2SHAREABILITY_WALL_HAS_CLOSED_FORM_(d+1)/2d`. The wall is certified as
`(d+1)/2d` and independently bracketed by POCS at d=2,3,4. Honest-limit #1 is
closed. Model: `models/finality_isotropic_shareability_closed_form.py`;
tests: `tests/test_finality_isotropic_shareability_closed_form.py`;
results: `results/T516-isotropic-shareability-closed-form-v0.1-results.md`.
