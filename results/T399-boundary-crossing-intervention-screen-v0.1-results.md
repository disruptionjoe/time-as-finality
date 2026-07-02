# T399 Results: Boundary-Crossing Intervention Statistics Screen

- **Artifact:** `T399-boundary-crossing-intervention-screen-v0.1`
- **Spec:** [tests/T399-boundary-crossing-intervention-screen.md](../tests/T399-boundary-crossing-intervention-screen.md)
- **Model:** [models/boundary_crossing_intervention_screen.py](../models/boundary_crossing_intervention_screen.py)
- **Numbers:** [T399-boundary-crossing-intervention-screen-v0.1.json](T399-boundary-crossing-intervention-screen-v0.1.json)

## Verdict

The strengthened boundary-crossing discriminator shape exists in a finite
screen, but it is absorbed.

Two Bell states, `phi_plus` and `psi_plus`, have identical `R` marginals and
identical boundary-local marginals:

- `R` trace distance: `0.0`
- boundary-local trace distance: `0.0`
- generic bound for all `R`-supported statistics: `0.0`
- region-only binary success: `0.5`
- boundary-local binary success: `0.5`

The finite concrete menu also agrees: eight `R` unitaries times `Z/X/Y`
readouts, `24` statistics total, with max difference `0.0`.

The boundary-crossing menu separates the pair:

- full-state trace distance: `1.0`
- joint `Z` parity readout binary success: `1.0`
- Bell-basis readout binary success: `1.0`

## Interpretation

This satisfies the formal shape requested after T398:

```text
No R-supported statistic, including statistics under R-supported
interventions, separates the pair; a boundary-crossing menu separates it.
```

But the result is not residue. Once the boundary system and joint `RB`
measurements are admitted, the full states are orthogonal and the separator is
ordinary cross-boundary correlation. T399 therefore records
`absorbed_boundary_access_translation`, not a claim upgrade.

## Controls

- Region-visible control: `|00>` vs `|10>` has `R` trace distance `1.0`, so
  the statistics menu has teeth.
- Phase-correlation control: `phi_plus` vs `phi_minus` has equal `R` and
  boundary-local marginals and equal joint parity, but Bell readout separates
  it. Parity is not the whole boundary-crossing menu.

## Open Next

For stronger Direction-A work, the boundary crossing has to be physically
forced by the declared setup rather than merely admitted as the ordinary
enlarged-state completion.

No claim-ledger movement. No North Star, canon, public posture, or external
resource-theory language changed.

## Verification

```text
python -m pytest tests/test_boundary_crossing_intervention_screen.py -q
9 passed in 0.22s

python -m models.boundary_crossing_intervention_screen | python -m json.tool
json-ok
```
