# Progress Run: Schwarzschild Horizon Access-Profile Screen

- Date: 2026-07-02
- Mode: Progress
- Repository: Time as Finality
- Automation: Hourly Nobel Prize Winner
- Run objective: Apply the access-profile alignment rule to a simple GR causal-accessibility witness without touching the active finite-closed taxonomy lane.
- Status: completed

## Governance Loaded

- Workspace root instructions from `C:\Users\joe\JB\AGENTS.md` in chat.
- CapacityOS entrypoint: `C:\Users\joe\JB\CapacityOS\Agents Start Here.md`.
- CapacityOS run model: `kernel/run-convention/standard-run-model.md`.
- Repo instructions: `AGENTS.md`.
- Repo steward: `steward/README.md`.
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, and `Lead Research Line - Time as Finality.md`.
- Contribution and local run conventions: `CONTRIBUTING.md`, recent `steward/runs/`.
- Current method context: `technical-reports/TECHNICAL-REPORT-access-profile-alignment-lemma-v0.1.md`, T153 Lorentzian causal-diamond screen, and the Method next-action list.

## Worktree State

At selection time, `open-problems/finite-closed-capability-boundary-scope-theorem.md`
already had a large unstaged edit withdrawing the universal no-go into a bounded
taxonomy. That lane also states that Joe must choose path A or B. This run treats
that file as pre-existing active work and does not edit or stage it.

## Objective

Create T418, a conservative Schwarzschild horizon access-profile screen:

```text
same exterior Schwarzschild shadow + different interior record
```

should not be counted as an exterior-native projection-sufficiency failure. If
the capability splits only after moving from the exterior observer to an
infalling/full-slice profile, the result is an access-profile mismatch absorbed
by ordinary horizon causal structure.

## Boundaries

- No North Star, canon, public-posture, cross-repo truth, or claim-ledger movement.
- No edits to the dirty finite-closed taxonomy file.
- No black-hole information, QFT, holography, evaporation, or semiclassical gravity claim.
- GitHub commit/push is authorized by this automation request and is the normal versioning surface.

## Planned Verification

- `python -m pytest tests/test_schwarzschild_horizon_access_profile_screen.py -q`
- focused regression with `tests/test_lorentzian_causal_diamond_screen.py`
- `python -m models.run_t418`
- JSON parse for generated T418 result
- `git diff --check`

## Run Receipt

- Status: completed
- Completed: 2026-07-02 17:08 CDT
- Objective executed: T418 Schwarzschild horizon access-profile screen.
- Files created:
  - `models/schwarzschild_horizon_access_profile_screen.py`
  - `models/run_t418.py`
  - `tests/test_schwarzschild_horizon_access_profile_screen.py`
  - `tests/T418-schwarzschild-horizon-access-profile-screen.md`
  - `technical-reports/TECHNICAL-REPORT-schwarzschild-horizon-access-profile-screen-v0.1.md`
  - `results/T418-schwarzschild-horizon-access-profile-screen-v0.1.json`
  - `results/T418-schwarzschild-horizon-access-profile-screen-v0.1-results.md`
  - `steward/runs/2026-07-02-schwarzschild-horizon-access-profile-screen.md`
- Files updated:
  - `TESTS.md`
  - `steward/memory-log.md`
- Result: radial Schwarzschild outgoing-null structure now has a repo-local access-profile guardrail. The exterior projection pair is equal and exterior capability does not split; infalling/full-slice capability does split, but only by changing profiles. The result is classified as `absorbed_by_schwarzschild_causal_access_and_profile_alignment`.
- Claim movement: none.
- North Star / canon / public posture movement: none.
- Black-hole information / QFT / holography / evaporation / semiclassical-gravity movement: none.
- Pre-existing work protected: the active finite-closed taxonomy file was not edited or staged.
- Verification:
  - `python -m pytest tests/test_schwarzschild_horizon_access_profile_screen.py -q` -> 8 passed
  - `python -m pytest tests/test_schwarzschild_horizon_access_profile_screen.py tests/test_lorentzian_causal_diamond_screen.py -q` -> 17 passed
  - `python -m models.schwarzschild_horizon_access_profile_screen | python -m json.tool` -> parsed
  - `python -m models.run_t418` -> generated JSON and Markdown result artifacts
  - `python -m json.tool results\T418-schwarzschild-horizon-access-profile-screen-v0.1.json` -> parsed
- Follow-up: a stronger GR-facing artifact would need matched access profiles plus a native black-hole information or algebraic-QFT capability object declared up front.
