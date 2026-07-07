# 2026-07-06 Coarse-Graining Budget-Index Gate

## Run Envelope

- Run family: Repo Progress Run
- Resolved run packet: `repo=time-as-finality`, `workflow=repo-progress-run`, `mode=standard-progress`
- Target repository: Time as Finality
- Local start: 2026-07-06 17:04 CDT
- Operator: Codex automation `hourly-nobel-prize-winner`
- Status: complete

## Context Reads

- JB root instructions from active chat
- CapacityOS `Agents Start Here.md`
- CapacityOS `AGENTS.md`
- CapacityOS run convention and repo-progress workflow safety files
- Repo `AGENTS.md`
- Repo `steward/README.md`
- North Star map:
  - `Vision - North Star.md`
  - `Method - Research Program Guidelines.md`
  - `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- Current git state, recent local run artifacts, recent git log
- Recent context:
  - T467 valid coarse-graining admissibility gate
  - T468 positive-control independence audit
  - T469 task-naturalness gate
  - T471 multivalued fixture gate
  - T476 observer-shadow category closure router
  - `open-problems/valid-coarse-graining-as-finality-admissibility.md`
  - `models/coarse_graining_task_naturalness_gate.py`
  - `models/coarse_graining_multivalued_fixture_gate.py`
  - `models/valid_coarse_graining_admissibility_gate.py`

## Recent Run Collision Check

The tracked worktree is clean and aligned with `origin/main`. Only local ops
records under `steward/runs/` are untracked from closed prior runs. The most
recent tracked work, T476, closes the observer-shadow category lane to minor
restarts. The valid-coarse-graining lane has no active tracked edits and its
last local receipt, T471, is complete.

This run continues the T467-T471 valid-coarse-graining lane as a new
budget-index stress gate. It does not repeat T471's alphabet stress or touch
claim-ledger, roadmap, README, North Star, public-posture, hard-policy,
protected-license, or cross-repo truth surfaces.

## Selected Objective

Build T477 as an executable budget-index gate for valid coarse-graining
packets. The objective is to test whether the repaired T469/T471 admission
shape is genuinely observer-budget indexed: positives should persist under
larger access budgets, hidden-field tasks should route from inaccessible to
admitted only when the observer budget actually includes the field, and cheap
arithmetic/label-restatement/microstate/observer-creates-truth controls should
remain blocked.

## Expected Writable Surfaces

- `models/coarse_graining_budget_index_gate.py`
- `tests/test_coarse_graining_budget_index_gate.py`
- `tests/T477-coarse-graining-budget-index-gate.md`
- `results/T477-coarse-graining-budget-index-gate-v0.1.json`
- `results/T477-coarse-graining-budget-index-gate-v0.1-results.md`
- `open-problems/valid-coarse-graining-as-finality-admissibility.md`
- `steward/memory-log.md`
- This local run artifact

## Forbidden Actions And Stop Conditions

- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, README, North Star files,
  public posture, hard policy, protected licenses, or cross-repo truth.
- Do not promote D1, T10, T29, Observer Theory, valid coarse-graining, or any
  physics/consciousness claim.
- Do not claim that bounded computation alone selects valid finality
  coarse-grainings.
- Do not publish, deploy, send, or write to any non-GitHub external system.
- Stop if the objective requires external publication, non-GitHub external
  action, claim promotion, hard promotion mailbox notices, or cross-repo truth
  movement.

## Joe-Review Points

None expected. This run stays below claim, canon, public-posture,
external-action, and cross-repo gates.

## Plan

1. Add a T477 model that evaluates valid coarse-graining packets across nested
   observer budgets.
2. Add focused tests and a frozen T477 spec.
3. Generate JSON and Markdown results.
4. Update the valid-coarse-graining open problem with a compact T477 addendum.
5. Append steward memory and this receipt.
6. Verify focused tests, adjacent T477/T471/T469/T468/T467 regression, JSON
   parse, model compile/run, diff checks, protected-surface checks, and scoped
   ASCII / absolute-path scans.

## Execution Notes

- Created `models/coarse_graining_budget_index_gate.py`.
- Created `tests/test_coarse_graining_budget_index_gate.py`.
- Created `tests/T477-coarse-graining-budget-index-gate.md`.
- Generated `results/T477-coarse-graining-budget-index-gate-v0.1.json`.
- Generated `results/T477-coarse-graining-budget-index-gate-v0.1-results.md`.
- Appended a T477 addendum to
  `open-problems/valid-coarse-graining-as-finality-admissibility.md`.
- Appended the T477 summary to `steward/memory-log.md`.
- Left `CLAIM-LEDGER.md`, `ROADMAP.md`, README, North Star files, public
  posture, hard policy, protected licenses, and cross-repo truth untouched.
- Per `standard-run-safety-rules.md` section 11, this `steward/runs/`
  artifact remains local and is not staged for the public repo commit.

## Validation

- `python -m pytest tests/test_coarse_graining_budget_index_gate.py -q`
  - `8 passed`
- `python -m pytest tests/test_coarse_graining_budget_index_gate.py tests/test_coarse_graining_multivalued_fixture_gate.py tests/test_coarse_graining_task_naturalness_gate.py tests/test_coarse_graining_positive_control_independence.py tests/test_valid_coarse_graining_admissibility_gate.py -q`
  - `40 passed`
- `python -m compileall -q models\coarse_graining_budget_index_gate.py`
- `python -m json.tool results\T477-coarse-graining-budget-index-gate-v0.1.json`
- `python -m models.coarse_graining_budget_index_gate`
- `git diff --check`
- `git diff --cached --check`
- Protected-surface check:
  - no diffs in `CLAIM-LEDGER.md`, `ROADMAP.md`, README,
    `Vision - North Star.md`, `Method - Research Program Guidelines.md`,
    `Lead Research Line - Time as Finality.md`, or `LICENSE.md`
- Scoped ASCII scan:
  - new T477 files passed
  - added lines in touched existing files passed
  - pre-existing non-ASCII punctuation remains in `steward/memory-log.md`
- Scoped absolute-path scan of T477 files and touched notes:
  - no workspace absolute paths found

## Receipt

Status: completed and pushed at 2026-07-06 17:11 CDT.

Outcome: T477 makes the T469/T471 valid-coarse-graining repair
observer-budget indexed. Three-holder finality-band and support-count
positives persist under expanded access. A boundary-pair record is rejected as
inaccessible under the three-holder budget and admitted only when holder 3
enters the declared observer budget. Cheap arithmetic, label restatement,
microstate identity, and observer-creates-truth controls remain blocked. This
is a budget-index guardrail only; no D1/T10/T29 promotion, Observer Theory
equivalence theorem, global valid-coarse-graining criterion, physics/
consciousness claim, claim-ledger movement, public-posture movement,
hard-policy movement, protected-license change, or cross-repo truth movement
is earned.

GitHub versioning: committed and pushed to `main` as
`a6450be Add T477 budget-index gate`.
