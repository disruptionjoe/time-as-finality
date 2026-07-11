# 2026-07-11 RUN-336 Child Progress: Public Path Hygiene

Status: active

## Target

- Repo: `repos/public/time-as-finality`
- Parent run: `RUN-20260711-336-progress-fanout-hourly`
- Workflow: `repo-progress-run`
- Mode: `execute`

## Run Family

Progress.

## Objective

Remove tracked absolute home-path references from historical steward run records by
normalizing them to workspace-relative `CapacityOS/...` or `JB/...` wording.

## Context Reads

- CapacityOS root instructions and repo progress workflow/safety files.
- Run-packet contract and execute mode.
- Repository registry entry for `time-as-finality`.
- Repo `AGENTS.md`.
- `steward/README.md`.
- Current North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, `Lead Research Line - Time as Finality.md`.
- `CONTRIBUTING.md`.
- Recent local run records and recent git history.

## Expected Writable Surfaces

- Historical Markdown records under `steward/runs/` that contain absolute home paths.
- This run plan/receipt.
- `steward/memory-log.md` only if closeout memory is useful.

## Recent Run Collision Check

`main` was clean and aligned with `origin/main` before writes. The latest visible
local run record, RUN-330, is closed and covers the Observerse/T527 lane. Recent
history also includes S1/T526, T527, and ledger-frontier/T249-T255 work. This run
does not touch those research artifacts, claim status, canon verdicts, public
posture, North Star, or test registration.

## Forbidden Actions And Stop Conditions

- Do not write outside `repos/public/time-as-finality`.
- Do not edit CapacityOS parent records.
- Do not change claim status, canon verdicts, North Star, public posture,
  protected research status, hard policy, or external-publication state.
- Do not touch recent RUN-334/RUN-335 lanes or the recent T526/T527/ledger-frontier
  research surfaces.
- Stop on dirty-and-overlapping tracked changes, ambiguous artifact classification,
  unexpected tracked validation diffs, or any non-GitHub external action need.

## Joe-Review Points

None expected for a bounded public path-hygiene repair.

## Plan

1. Scan tracked files for absolute home-path references.
2. Normalize only tracked historical run-record references to workspace-relative
   paths.
3. Validate that no tracked absolute home-path references remain.
4. Run Markdown/diff hygiene checks.
5. Append this receipt, stage explicit paths, commit, and push if still aligned.

## Execution Notes

- 2026-07-11 02:10 CDT: Dirty-tree preflight found `main` clean and aligned
  with `origin/main` before creating this run plan.
- 2026-07-11 02:12 CDT: Scanned tracked repo text for absolute home-path
  references and found them only in historical `steward/runs/` records.
- 2026-07-11 02:13 CDT: Mechanically normalized 32 historical run records from
  local home-root paths to workspace-relative `CapacityOS/...`, `JB/...`, or
  `repos/public/time-as-finality` references.

## Validation

- `rg` scan for tracked absolute home-path references: no matches.
- `git diff --check`: passed.
- Reviewed representative diff hunks for both context-read paths and worktree-list
  path lines.

## Receipt

Completed: 2026-07-11 02:14 CDT.

Outcome: public path hygiene repaired for the historical steward run-record set
that contained absolute home-root references. The run did not touch S1/T526,
T527/Observerse, ledger-frontier/T249-T255, claim status, canon verdicts, public
posture, North Star, external publication, or cross-repo truth surfaces.

Versioned files changed:

- 32 historical `steward/runs/*.md` files with path-only normalizations.
- `steward/runs/2026-07-11-run-336-public-path-hygiene.md`.
- `steward/memory-log.md`.

Commit/push: completed by this run; see final response for the resulting commit
hash.
