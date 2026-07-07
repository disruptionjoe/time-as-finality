# 2026-07-06 Valid Coarse-Graining Admissibility Gate

## Run Envelope

- Run family: Repo Progress Run
- Resolved run packet: `repo=time-as-finality`, `workflow=repo-progress-run`, `mode=standard-progress`
- Target repository: Time as Finality
- Local start: 2026-07-06 08:03 CDT
- Operator: Codex automation `hourly-nobel-prize-winner`
- Status: complete

## Context Reads

- Automation memory for `hourly-nobel-prize-winner`
- CapacityOS `Agents Start Here.md`
- CapacityOS `AGENTS.md`
- CapacityOS run-packet, workflow, mode, safety, plan, and receipt surfaces
- Repo `AGENTS.md`
- Repo `steward/README.md`
- North Star map:
  - `Vision - North Star.md`
  - `Method - Research Program Guidelines.md`
  - `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- Current git state, worktree list, recent git log, recent local run artifacts
- Recent context:
  - T460-T466 recent route closures
  - `steward/memory-log.md`
  - `open-problems/valid-coarse-graining-as-finality-admissibility.md`
  - T10 finality-superselection prompt
  - T29 projection-obstruction schema
  - D1 physical finality definition

## Recent Run Collision Check

The worktree is dirty but separable: only public-repo local ops records under
`steward/runs/` are untracked from recent completed T465/T466 runs. Only the
main repo worktree exists. T465 and T466 are closed and pushed, and the current
kappa lane is route-closed as a synthetic future-target burden only.

This run avoids the T460 Direction-A, T463 H7/E1, T464 S1, and T466 kappa
surfaces. `T467` is unused in the scoped repo-local search.

## Selected Objective

Build T467 as a finite valid-coarse-graining admissibility gate for the older
Wolfram/observer-theory open problem. The objective is to make the repo's
candidate answer executable: a coarse-graining is admissible only when a
bounded observer can form and certify the corresponding finalized record under
explicit D1-style budget and selection fields. The run should expose where that
criterion is too weak, too strong, or absorbed by ordinary computation-cost and
record-certification bookkeeping.

## Expected Writable Surfaces

- `models/valid_coarse_graining_admissibility_gate.py`
- `tests/test_valid_coarse_graining_admissibility_gate.py`
- `tests/T467-valid-coarse-graining-admissibility-gate.md`
- `results/T467-valid-coarse-graining-admissibility-gate-v0.1.json`
- `results/T467-valid-coarse-graining-admissibility-gate-v0.1-results.md`
- `open-problems/valid-coarse-graining-as-finality-admissibility.md`
- `steward/memory-log.md`
- This local run artifact

## Forbidden Actions And Stop Conditions

- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, README, North Star files,
  public posture, hard policy, or cross-repo truth.
- Do not promote D1, T10, T29, Observer Theory, valid coarse-graining, H7, or
  any physics/observer claim.
- Do not claim that observer equivalencing creates reality or that projection
  by itself is finality.
- Stop if the objective requires external publication, non-GitHub external
  action, claim promotion, or cross-repo truth movement.

## Plan

1. Add a T467 model that enumerates finite candidate equivalence relations and
   classifies them under a bounded-observer certification rule.
2. Add a frozen T467 spec and focused tests.
3. Generate JSON and Markdown results.
4. Update the valid-coarse-graining open problem with a compact T467 addendum.
5. Append steward memory and this receipt.
6. Verify focused tests, adjacent T29/T80-style regression if useful, JSON
   parse, model compile, diff checks, protected-surface checks, and scoped ASCII
   / absolute-path scans.

## Execution Notes

- Created `models/valid_coarse_graining_admissibility_gate.py`.
- Created `tests/test_valid_coarse_graining_admissibility_gate.py`.
- Created `tests/T467-valid-coarse-graining-admissibility-gate.md`.
- Generated `results/T467-valid-coarse-graining-admissibility-gate-v0.1.json`.
- Generated `results/T467-valid-coarse-graining-admissibility-gate-v0.1-results.md`.
- Appended a T467 addendum to
  `open-problems/valid-coarse-graining-as-finality-admissibility.md`.
- Appended the T467 summary to `steward/memory-log.md`.
- Left `CLAIM-LEDGER.md`, `ROADMAP.md`, README, North Star files, public
  posture, hard policy, and cross-repo truth untouched.
- Per `standard-run-safety-rules.md` section 11, this `steward/runs/`
  artifact remains local and is not staged for the public repo commit.

## Validation

- `python -m pytest tests/test_valid_coarse_graining_admissibility_gate.py -q`
  - `9 passed`
- `python -m compileall -q models\valid_coarse_graining_admissibility_gate.py`
- `python -m models.valid_coarse_graining_admissibility_gate --write-results`
- `python -m pytest tests/test_valid_coarse_graining_admissibility_gate.py tests/test_projection_obstruction_schema.py tests/test_reversible_finality_nonmonotonicity.py -q`
  - `25 passed`
- `python -m json.tool results\T467-valid-coarse-graining-admissibility-gate-v0.1.json`
- `python -m models.valid_coarse_graining_admissibility_gate`
- `git diff --check`
- `git diff --cached --check`
- Protected-surface check:
  - no diffs in `CLAIM-LEDGER.md`, `ROADMAP.md`, README,
    `Vision - North Star.md`, `Method - Research Program Guidelines.md`, or
    `Lead Research Line - Time as Finality.md`
- Scoped ASCII scan of new versioned T467 files:
  - no non-ASCII bytes found
- Scoped absolute-path scan of T467 files and touched notes:
  - no workspace absolute paths found

## Receipt

Status: completed and pushed at 2026-07-06 08:09 CDT.

Outcome: T467 makes the valid-coarse-graining open problem executable as an
admission gate. In the finite fixture, bounded-observer certification admits
only the predeclared finality-record positive controls and rejects microstate
identity, trivial collapse, hidden fields, ornate lookup, posthoc partitioning,
projection-only shadows, one-holder dashboards, and observer-creates-truth
overreads.

GitHub versioning: committed and pushed to `main` as
`4d95007 Add T467 coarse-graining admissibility gate`.
