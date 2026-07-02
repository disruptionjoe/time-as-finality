# 2026-07-02 Boundary-Forced Task Gate Progress Run

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
- T397/T398/T399 region-capability artifacts

## Worktree State

Before edits, the only visible untracked file was `results/_rmtest.json`.
It was treated as pre-existing scratch / non-artifact material and left
untouched.

## Objective

Turn T399's remaining burden into an executable gate:

```text
boundary crossing must be forced by the declared task/setup,
not merely admitted as ordinary enlarged-state access.
```

This run should not promote any claim. A useful outcome is a finite gate that:

- rejects T399-style optional boundary access;
- has a positive control where the declared task is genuinely relational across
  `R` and `B`;
- blocks hidden-datum, closure-key, and class-marker shortcuts;
- records that a real future discriminator still needs a domain-native
  physical/finality task.

## Planned Verification

- `python -m pytest tests/test_boundary_forced_task_gate.py -q`
- `python -m models.boundary_forced_task_gate`
- generated JSON parse
- focused T399 regression
- `git diff --check`

## Receipt

Completed.

## Artifacts Created

- `tests/T400-boundary-forced-task-gate.md`
- `models/boundary_forced_task_gate.py`
- `tests/test_boundary_forced_task_gate.py`
- `results/T400-boundary-forced-task-gate-v0.1.json`
- `results/T400-boundary-forced-task-gate-v0.1-results.md`

## Surfaces Updated

- `TESTS.md`
- `ROADMAP.md`
- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

## Result

T400 operationalizes T399's remaining burden as a finite forced-task gate:

- the T399 substrate is preserved (`R` statistics/interventions equal,
  boundary-local statistics equal, boundary-crossing success `1.0` vs
  region-only success `0.5`);
- T399-style optional state-label readout fails as
  `optional_boundary_menu_only`;
- hidden-datum, closure-key, and class-marker shortcuts are blocked;
- a synthetic `R:B` parity task passes only as
  `formal_positive_control_only`;
- no domain-native physical/finality task is supplied, so no claim-ledger
  movement is earned.

This advances Direction A by making the next discriminator gate executable,
not by promoting the Bell-pair control.

No North Star, canon, claim status, public posture, or cross-repo truth changed.
No external action was performed beyond the authorized GitHub versioning step
planned for closeout.

## Verification

Passed:

```text
python -m pytest tests/test_boundary_forced_task_gate.py -q
8 passed in 0.18s

python -m pytest tests/test_boundary_forced_task_gate.py tests/test_boundary_crossing_intervention_screen.py -q
17 passed in 0.19s

python -m models.boundary_forced_task_gate | python -m json.tool
json-ok

python -m json.tool results\T400-boundary-forced-task-gate-v0.1.json
json-ok

git diff --check
clean
```

## Next Safe Lane

Use the T400 gate before any future Direction-A boundary-crossing artifact.
The next real progress target is a domain-native physical or finality task
whose boundary relation is forced by the declared setup before selecting the
witness pair.
