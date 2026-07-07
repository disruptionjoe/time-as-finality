# Progress Run: Internal Scale Generator Invariance Probe

Status: complete
Date: 2026-07-07
Run family: Repo Progress Run
Mode: standard-progress
Target repo: time-as-finality

## Objective

Build T482 as a concrete post-T481 stress test: attempt a TaF-native internal
scale generator over D1 field patches, then test whether it survives
predeclared comparison-domain, relabel-invariance, positive/negative-control,
clock/finality, RG/conformal, and promotion-overread guards.

## Context Reads

- JB root `AGENTS.md` from active chat
- `CapacityOS/Agents Start Here.md`
- `CapacityOS/AGENTS.md`
- CapacityOS canonical architecture, subsidiarity architecture, run convention,
  standard run model, and decision index
- repo `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- recent local run receipts and automation memory
- `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- T24/T38/T479/T480/T481 specs, models, and results

## Recent Run Collision Check

Latest tracked HEAD is T481 (`3f7ed4d`) and is aligned with `origin/main`.
Only intentionally untracked local `steward/runs/` receipts are present. No
other worktree is present. T482 is unused.

Working-tree classification before writes: dirty but separable. Dirty files
are local `steward/runs/` receipts that must remain untracked in this public
repo.

## Expected Writable Surfaces

- `models/internal_scale_generator_invariance_probe.py`
- `tests/test_internal_scale_generator_invariance_probe.py`
- `tests/T482-internal-scale-generator-invariance-probe.md`
- `results/T482-internal-scale-generator-invariance-probe-v0.1.json`
- `results/T482-internal-scale-generator-invariance-probe-v0.1-results.md`
- `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- `steward/memory-log.md`
- this local run artifact

## Forbidden Actions And Stop Conditions

- Do not change North Star, canon, claim status, claim ledger, roadmap, README,
  public posture, hard policy, protected license, papers, or cross-repo truth.
- Do not write outside this repo.
- Do not stage local `steward/runs/` receipts in this public repo.
- Stop if the probe would require an actual physics, conformal-gravity,
  scale-genesis, record-clock, duration, temporal-arrow, record-finality, D1
  promotion, or RG/TaF equivalence claim.

## Plan

1. Add T482 model/spec/tests around a finite D1-support-gradient generator.
2. Generate JSON/Markdown results.
3. Append a narrow T482 addendum to the RG-flow multiscale analogy open
   problem and append steward memory.
4. Run focused and adjacent regressions, diff hygiene, ASCII/path checks.
5. Append receipt here, commit and push coherent tracked repo changes only.

## Execution Notes

- Selected T482 because T481 admits only a synthetic future internal-scale
  review target. The next worthy safe move is to make that target concrete and
  see whether it is just D1-support bookkeeping or a candidate internal-scale
  object.
- Implemented T482 as a D1-support-gradient invariance probe. The packet clears
  the review mechanics but factors through the existing D1 profile tuple, so it
  remains bookkeeping only.

## Validation

- `python -m pytest tests/test_internal_scale_generator_invariance_probe.py -q`
  passed: 8 tests.
- `python -m models.internal_scale_generator_invariance_probe` completed.
- `python -m models.internal_scale_generator_invariance_probe --write-results`
  generated JSON/Markdown results.
- Adjacent regression passed: `python -m pytest
  tests/test_internal_scale_generator_invariance_probe.py
  tests/test_internal_scale_structure_admission_gate.py
  tests/test_scale_label_operation_gate.py
  tests/test_rg_flow_multiscale_calibration_gate.py
  tests/test_multiscale_observer_field.py
  tests/test_minimal_multiscale_transport.py -q` passed: 98 tests.
- `python -m json.tool
  results/T482-internal-scale-generator-invariance-probe-v0.1.json` passed.
- `python -m compileall models/internal_scale_generator_invariance_probe.py`
  completed.
- `git diff --check` and `git diff --cached --check` passed.
- New T482 files are ASCII-only.
- Added-line ASCII and absolute-path checks passed.
- Staged protected-surface check passed.

## Receipt

Outcome: completed.

Created T482 as a concrete post-T481 review-target probe. A predeclared
D1-support-depth generator produces nontrivial bands on the stratified T24
fixture, collapses the uniform null control to one band, and survives
observer-label relabeling. The packet is admitted only as review-grade D1
bookkeeping because every band factors through the existing D1 profile tuple.

Changed versioned repo surfaces:

- `models/internal_scale_generator_invariance_probe.py`
- `tests/test_internal_scale_generator_invariance_probe.py`
- `tests/T482-internal-scale-generator-invariance-probe.md`
- `results/T482-internal-scale-generator-invariance-probe-v0.1.json`
- `results/T482-internal-scale-generator-invariance-probe-v0.1-results.md`
- `open-problems/rg-flow-as-multiscale-transport-analogy.md`
- `steward/memory-log.md`

No North Star, canon, claim status, claim ledger, roadmap, README,
public posture, hard policy, protected license, physics claim, internal
scale-structure theorem, scale-genesis theorem, D1 promotion, RG/TaF
equivalence theorem, cross-repo truth, or non-GitHub external action.

Local ops note: this `steward/runs/` receipt remains untracked per public-repo
ops-record policy.

Commit/push: committed and pushed `d00b883` (`Add T482 internal scale
generator probe`) to `origin/main`.
