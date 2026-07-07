# Progress Run: Internal Scale Structure Admission Gate

Status: active
Date: 2026-07-06
Run family: Repo Progress Run
Mode: standard-progress
Target repo: time-as-finality

## Objective

Make T480's "external bookkeeping vs earned internal structure" burden
executable as T481, without promoting clocks, durations, record finality, scale
genesis, RG/TaF equivalence, physics posture, claim status, public posture, or
cross-repo truth.

## Context Reads

- JB root `AGENTS.md` from active chat
- `CapacityOS/Agents Start Here.md`
- `CapacityOS/AGENTS.md`
- CapacityOS canonical architecture, subsidiarity architecture, run convention,
  repo-progress workflow, run-packet contract, standard-progress mode, and
  standard safety rules
- `system/meta/maps/repository-contract-registry.yaml`
- repo `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- T24, T38, T479, and T480 specs/models/results
- recent local run receipts and automation memory

## Recent Run Collision Check

Latest tracked HEAD is T480 (`726ae9c`) and is aligned with `origin/main`.
Only intentionally untracked local `steward/runs/` receipts are present. The
latest local receipt in this lane is closed and more than an hour old by local
file timestamp. No other worktree is present. T481 is unused.

Working-tree classification before writes: dirty but separable. Dirty files are
local `steward/runs/` receipts that must remain untracked in this public repo.

## Expected Writable Surfaces

- `models/internal_scale_structure_admission_gate.py`
- `tests/test_internal_scale_structure_admission_gate.py`
- `tests/T481-internal-scale-structure-admission-gate.md`
- `results/T481-internal-scale-structure-admission-gate-v0.1.json`
- `results/T481-internal-scale-structure-admission-gate-v0.1-results.md`
- `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- `steward/memory-log.md`
- this local run artifact

## Forbidden Actions And Stop Conditions

- Do not change North Star, canon, claim status, public posture, hard policy,
  protected license, roadmap, README, or cross-repo truth.
- Do not write outside this repo.
- Do not stage local `steward/runs/` receipts in this public repo.
- Stop if the gate would require an actual physics, conformal-gravity,
  scale-genesis, record-clock, duration, temporal-arrow, or D1-promotion claim.

## Plan

1. Add T481 model/spec/tests that classify scale packets as external
   bookkeeping, synthetic internal-structure review targets, or blocked
   shortcuts.
2. Generate JSON/Markdown results.
3. Append a narrow T481 addendum to the RG-flow multiscale analogy open problem
   and append steward memory.
4. Run focused and adjacent regressions, diff hygiene, ASCII/path checks.
5. Append receipt here, commit and push coherent tracked repo changes only.

## Execution Notes

- Selected T481 because T480 directly named this burden and the lane remains
  analogy-ledger/bookkeeping-only.

## Validation

- `python -m pytest tests/test_internal_scale_structure_admission_gate.py -q`
  passed: 9 tests.
- `python -m pytest tests/test_internal_scale_structure_admission_gate.py tests/test_scale_label_operation_gate.py tests/test_rg_flow_multiscale_calibration_gate.py tests/test_multiscale_observer_field.py tests/test_minimal_multiscale_transport.py -q`
  passed: 90 tests.
- `python -m models.internal_scale_structure_admission_gate` completed.
- `python -m models.internal_scale_structure_admission_gate --write-results`
  generated JSON/Markdown results.
- T481 JSON parsed and verdict/gate checks passed.
- `python -m compileall models/internal_scale_structure_admission_gate.py`
  completed.
- `git diff --check` and `git diff --cached --check` passed.
- New T481 files are ASCII-only.
- Added-line ASCII check passed for modified repo records.
- Added-line absolute path check passed.

## Receipt

Outcome: completed.

Created T481 as a review-only admission gate. External scale labels are
admitted only as comparison-domain bookkeeping over T24/T38/T480. A synthetic
internal-scale packet is admitted only as a future review target when it
predeclares a TaF-native internal generating rule, comparison domain, positive
and negative controls, and relabel-invariance checks. Hostile shortcuts for
assertion-only internal structure, label-only structure, posthoc comparison
domains, hidden calendar order, duration/arrow extraction, finality changes,
RG/conformal mechanism import, physics support, and claim/public-posture
promotion are blocked.

Changed versioned repo surfaces:

- `models/internal_scale_structure_admission_gate.py`
- `tests/test_internal_scale_structure_admission_gate.py`
- `tests/T481-internal-scale-structure-admission-gate.md`
- `results/T481-internal-scale-structure-admission-gate-v0.1.json`
- `results/T481-internal-scale-structure-admission-gate-v0.1-results.md`
- `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- `steward/memory-log.md`

No North Star, canon, claim status, claim ledger, roadmap, README, public
posture, hard policy, protected license, physics claim, scale-genesis theorem,
D1 promotion, RG/TaF equivalence theorem, cross-repo truth, or non-GitHub
external action.

Local ops note: this `steward/runs/` receipt remains untracked per public-repo
ops-record policy.

Commit/push: committed and pushed `3f7ed4d` (`Add T481 internal scale gate`) to
`origin/main`.
