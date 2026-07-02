# 2026-07-02 Boundary-Crossing Intervention Screen Progress Run

## Governance Loaded

- `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `ROADMAP.md`
- `TESTS.md`
- `open-problems/region-indexed-capability-discriminator.md`
- T397/T398 region-capability and resource-profile artifacts

## Worktree State

Before edits, the only visible untracked file was `results/_rmtest.json`,
treated as scratch / non-artifact material and left untouched.

## Objective

Run the stronger post-T398 discriminator gate in the smallest safe form:

```text
all R-supported statistics and interventions agree;
only a boundary-crossing menu separates capability.
```

The artifact must record absorber status if the separator is just ordinary
enlarged-state access.

## Planned Verification

- `python -m pytest tests/test_boundary_crossing_intervention_screen.py -q`
- `python -m models.boundary_crossing_intervention_screen`
- JSON parse of generated results
- focused T397/T398 regression
- `git diff --check`

## Receipt

Completed.

## Artifacts Created

- `tests/T399-boundary-crossing-intervention-screen.md`
- `models/boundary_crossing_intervention_screen.py`
- `tests/test_boundary_crossing_intervention_screen.py`
- `results/T399-boundary-crossing-intervention-screen-v0.1.json`
- `results/T399-boundary-crossing-intervention-screen-v0.1-results.md`

## Surfaces Updated

- `TESTS.md`
- `ROADMAP.md`
- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

## Result

T399 creates a finite Bell-pair boundary screen:

- Main pair: `phi_plus` vs `psi_plus`.
- `R` trace distance: `0.0`.
- Boundary-local trace distance: `0.0`.
- Generic all-`R`-supported statistic bound: `0.0`.
- Finite 8-unitary x 3-readout `R` menu max diff: `0.0`.
- Region-only and boundary-local binary success: `0.5`.
- Full-state trace distance: `1.0`.
- Joint parity and Bell-basis boundary-crossing success: `1.0`.

Interpretation: the strengthened formal discriminator shape exists, but it is
absorbed by ordinary enlarged-state access. Once the boundary system and joint
`RB` readout are admitted, the full states are orthogonal and the separator is
ordinary cross-boundary correlation. T399 is therefore
`absorbed_boundary_access_translation`, not a claim upgrade.

No claim-ledger movement. No North Star/canon/public-posture change. No
external prior-art verification was claimed.

## Verification

Passed:

```text
python -m pytest tests/test_boundary_crossing_intervention_screen.py -q
9 passed in 0.22s

python -m pytest tests/test_boundary_crossing_intervention_screen.py tests/test_resource_profile_absorber.py tests/test_region_capability_no_go.py -q
53 passed in 9.89s

python -m models.boundary_crossing_intervention_screen | python -m json.tool
json-ok

python -m json.tool results\T399-boundary-crossing-intervention-screen-v0.1.json
json-ok

git diff --check
clean
```

## Next Safe Lane

The next Direction-A version has to make the boundary-crossing task physically
forced by the declared setup rather than merely admitted as an ordinary
enlarged-state completion.
