# Progress Run: Reachability Quotient Capability Spread Gate

Status: completed
Run type: repo-progress-run
Mode: standard-progress
Started: 2026-07-07

## Target

- Repository: `repos/public/time-as-finality`
- Workflow: `system/runtime/workflows/repo-progress-run.md`
- Mode: `standard-progress`
- Writable boundary: this repository and this repo-local run artifact only.

## Objective

Build a post-T485 continuation that asks a non-overlapping question after
quotient stability: does the admitted reachability quotient determine a
declared transport-task capability spread, and which tempting capability
readings remain underdetermined?

## Context Reads

- CapacityOS `AGENTS.md`
- `Agents Start Here.md`
- `system/runtime/workflows/repo-progress-run.md`
- `system/runtime/workflows/standard-run-safety-rules.md`
- `system/runtime/flows/standard-run-safety-check.md`
- `system/runtime/flows/create-run-plan.md`
- `system/runtime/flows/append-run-receipt.md`
- `system/canon/modes/standard-progress.md`
- repo `AGENTS.md`
- `steward/README.md`
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, `Lead Research Line - Time as Finality.md`
- recent local runs: RUN-216, T485, T484, T483

## Expected Writable Surfaces

- `models/reachability_quotient_capability_spread_gate.py`
- `tests/test_reachability_quotient_capability_spread_gate.py`
- `tests/T487-reachability-quotient-capability-spread-gate.md`
- `results/T487-reachability-quotient-capability-spread-gate-v0.1.json`
- `results/T487-reachability-quotient-capability-spread-gate-v0.1-results.md`
- `TESTS.md`
- `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- `steward/memory-log.md`

This `steward/runs/` record is local ops material for a public repo and must
remain uncommitted.

## Recent Run Collision Check

Recent local records show T485 completed and pushed at `f08c8dc`. RUN-216
skipped because T485 was active at that time. No current tracked dirty files
exist. Existing untracked `steward/runs/` notes are local ops records and
separable.

This run must not rerun T485, T484, transport-topology refinement, internal
scale generator, record-finality, or finality-lock lanes. It consumes the
T485 quotient result as an anchor and asks a narrower capability-spread
question rather than changing the quotient gate.

## Forbidden Actions And Stop Conditions

- Do not change claim status, canon verdicts, public posture, North Star,
  hard policy, identity, protected license, README, ROADMAP, or
  `CLAIM-LEDGER.md`.
- Do not write outside this repo.
- Do not stage pre-existing untracked `steward/runs/` files.
- Stop on dirty-overlap or validation-generated unexpected tracked diffs.
- Do not publish, deploy, email, or write to non-GitHub external systems.

## Joe-Review Points

None expected. This is an internal finite gate with no governance promotion.

## Plan

1. Add T487 as a finite capability-spread gate over T485's committed result.
2. Admit only reachability-task sufficiency through the quotient signature.
3. Block path-latency, relay-budget, record-finality, scale, physics, and
   promotion readings as underdetermined or overread.
4. Generate result artifacts and run focused plus adjacent regressions.
5. Stage explicit versioned surfaces only; leave local ops notes untracked.

## Execution Notes

Created T487 after a concurrent untracked T486 closure-router lane appeared
during validation. The T-number was changed from the initially planned T486 to
T487 to avoid collision, and the concurrent T486 files were left untouched.

T487 consumes the committed T485 JSON result instead of calling the T485 runner.
It admits only source-target reachability and quotient role-profile capability
tasks as singleton-spread over quotient-visible fibers. It rejects path-latency,
relay-budget, component-size, finality, scale, physics, and promotion readings.

## Validation

- `python -m pytest tests/test_reachability_quotient_capability_spread_gate.py -q`
  passed, 8 tests.
- `python -m compileall -q models/reachability_quotient_capability_spread_gate.py`
  passed.
- `python -m json.tool results/T487-reachability-quotient-capability-spread-gate-v0.1.json`
  passed.
- `git diff --check` passed.
- T487 reference scan found no stale `T486-reachability` strings.
- Public path scan found no absolute home path leaks in T487/versioned reference
  surfaces.

## Receipt

Status: completed
Completed: 2026-07-07

Artifacts created:

- `models/reachability_quotient_capability_spread_gate.py`
- `tests/test_reachability_quotient_capability_spread_gate.py`
- `tests/T487-reachability-quotient-capability-spread-gate.md`
- `results/T487-reachability-quotient-capability-spread-gate-v0.1.json`
- `results/T487-reachability-quotient-capability-spread-gate-v0.1-results.md`

Artifacts updated:

- `TESTS.md`
- `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- `steward/memory-log.md`

Verdict:

```text
REACHABILITY_QUOTIENT_CAPABILITY_SPREAD_BUILT_TASK_ONLY
```

Commit and push:

- Committed and pushed versioned research artifacts as `f2e1821`
  (`Add T487 reachability quotient capability gate`).

Residual dirty state:

- Pre-existing and concurrent local `steward/runs/` ops records remain
  untracked and uncommitted, including this run note.
- A concurrent untracked T486 closure-router lane remains untouched.
