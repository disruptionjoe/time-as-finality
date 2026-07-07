# Progress Run: T493 Levin Competency C(R) Absorber Gate

Date: 2026-07-07
Mode: standard-progress
Repo: time-as-finality

## Objective

Convert the new N16 Levin/Fields competency calibration note into a narrow
executable gate for `C(R)`: distinguish what is absorbed by competency-style
intervention reachability from what remains only as TaF-local calibration or a
future surplus target.

## Context Loaded

- JB root workspace contract.
- CapacityOS start surface and constitutional root.
- Automation memory for `hourly-nobel-prize-winner`.
- Repo `AGENTS.md`.
- `steward/README.md`.
- `Vision - North Star.md`.
- `Method - Research Program Guidelines.md`.
- `Lead Research Line - Time as Finality.md`.
- `CONTRIBUTING.md`.
- `TESTS.md`.
- Recent steward memory and recent local run receipts.
- N16 Levin/Fields competency note.
- Region-indexed capability discriminator open problem.
- T407/T398/T460 model/test precedents.

## Initial State

`main` is aligned with `origin/main` at `16e9da9`. The only visible local
untracked files are prior `steward/runs/` receipts, which are local ops records
under the existing public-repo pattern.

## Safety

- Do not change North Star, canon, claim status, public posture, hard policy,
  protected-license material, or cross-repo truth.
- Treat N16 as pointer-grade; do not assert primary-source-checked standing.
- Build an executable internal gate only; no external publication.
- Avoid the recently closed T490/T491 S1, T488 RG/reachability, T489
  valid-coarse-graining, and T492 typed-gap lanes.

## Planned Artifact Set

- `models/levin_competency_cr_absorber_gate.py`
- `tests/test_levin_competency_cr_absorber_gate.py`
- `tests/T493-levin-competency-cr-absorber-gate.md`
- `results/T493-levin-competency-cr-absorber-gate-v0.1.json`
- `results/T493-levin-competency-cr-absorber-gate-v0.1-results.md`
- Focused updates to `TESTS.md`, `open-problems/region-indexed-capability-discriminator.md`,
  and `steward/memory-log.md`.

## Receipt

Completed.

Created T493:

- `models/levin_competency_cr_absorber_gate.py`
- `tests/test_levin_competency_cr_absorber_gate.py`
- `tests/T493-levin-competency-cr-absorber-gate.md`
- `results/T493-levin-competency-cr-absorber-gate-v0.1.json`
- `results/T493-levin-competency-cr-absorber-gate-v0.1-results.md`

Updated:

- `TESTS.md`
- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

Verdict:

`N16_COMPETENCY_GATE_BUILT_FULL_PROFILE_ABSORBS_SURPLUS_REVIEW_ONLY`.

Full intervention-measured task-success competency absorbs the current T407/T398
`C(R)` profile as capability bookkeeping. A single observed navigation/readout
statistic does not absorb the multi-task `C(R)` profile. T407 zero-trace
statistics/capability flatness remains a review target over simple observed
statistics only, not a novelty claim over a full competency profile.

N16 remains pointer-grade and primary sources are not checked. No
active-inference/free-energy mechanism import, region-indexed discriminator
success, claim-ledger movement, roadmap movement, README movement, North Star
movement, public-posture movement, hard-policy movement, protected-license
movement, external-publication, or cross-repo truth movement was made.

Verification:

- `python -m pytest tests/test_levin_competency_cr_absorber_gate.py -q`
  passed: 6 tests.
- `python -m models.levin_competency_cr_absorber_gate --write-results`
  passed.
- `python -m pytest tests/test_levin_competency_cr_absorber_gate.py tests/test_region_capability_no_go.py tests/test_resource_profile_absorber.py -q`
  passed: 50 tests.
- `python -m compileall models/levin_competency_cr_absorber_gate.py` passed.
- `python -m json.tool results/T493-levin-competency-cr-absorber-gate-v0.1.json`
  passed.
- `git diff --check` and staged `git diff --cached --check` passed.
- Staged protected-surface check found no claim ledger, roadmap, README,
  North Star, agent instruction, license, or published-paper files.
- New-file ASCII scan passed.

Committed and pushed:

- Commit: `cb1d828` (`Add T493 competency absorber gate`)
- Remote: `origin/main`

Final tracked state: `main` aligned with `origin/main`. Local `steward/runs/`
receipts, including this one and a concurrent blocked `run-224` receipt, remain
untracked by the public-repo ops-record pattern.
