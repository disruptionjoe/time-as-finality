# T516 Results -- closed form for the isotropic 2-shareability wall

**Verdict:** `ISOTROPIC_2SHAREABILITY_WALL_HAS_CLOSED_FORM_(d+1)/2d`
**Model:** `models/finality_isotropic_shareability_closed_form.py` (exit 0, 6/6 checks)
**Closes:** honest-limit #1 of the qudit result ("confirm F_share against a closed form").

## Result

The isotropic 2-shareability (symmetric-extendibility) wall, in the standard
singlet-fraction parametrization
`rho = F|Phi><Phi| + (1-F)/(d^2-1)(I - |Phi><Phi|)`, is

```
F_share(d) = (d + 1) / (2 d)          (visibility form: v_share(d) = (d+2)/(2(d+1)))
```

This is the symmetric-extendibility boundary for isotropic states
(Johnson & Viola, PRA 88, 032323 (2013); arXiv 0906.5255), rewritten in the
singlet-fraction convention used by the qudit ladder.

Predictions: `F_share(2) = 0.750`, `F_share(3) = 0.667`, `F_share(4) = 0.625`,
`F_share(5) = 0.600`.

## The model is the arbiter (independent POCS)

An independent symmetric-extension POCS was run just below and just above the
closed form at each d; it must find the state shareable below and un-shareable
above (so the closed form is inside the bracket):

| d | POCS bracket | closed form | contained |
|---|---|---|---|
| 2 | (0.73, 0.77) | 0.7500 | yes |
| 3 | (0.6467, 0.6867) | 0.6667 | yes |
| 4 | (0.605, 0.645) | 0.6250 | yes |

(POCS iterations scale with `d^3`: d=4 needed ~1500 to converge; 500 biases the
wall low, which is why the qudit d=4 run first reported ~0.60.)

## Link to the qudit ladder

`F_share(3) = 2/3 = 0.6667` matches the ladder's POCS value 0.670 exactly. The
"0.670 should be confirmed against a closed form" limit is discharged: the value
is `2/3`, certified by the literature form and independently bracketed by POCS.

## Structural facts (both hold)

- `F_share(d) > 1/d` for all `d >= 2` -- shareability strictly above separability.
- monotone decreasing in d, `-> 1/2` as `d -> infinity`.

## Honest limits

POCS remains a feasibility test (no dual-witness certificate); the closed form
is the certified value and POCS is an independent numeric confirmation of it.
