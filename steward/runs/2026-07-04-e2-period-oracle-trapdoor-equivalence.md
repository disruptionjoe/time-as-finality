# 2026-07-04 E2 Period-Oracle Trapdoor Equivalence

## Run Envelope

- Run type: Progress
- Target repository: Time as Finality
- Local start: 2026-07-04 14:18 CDT
- Operator: Codex
- Status: completed

## Governance Loaded

- `CapacityOS\Agents Start Here.md`
- Repo `AGENTS.md`
- Repo `steward/README.md`
- North Star map:
  - `Vision - North Star.md`
  - `Method - Research Program Guidelines.md`
  - `Lead Research Line - Time as Finality.md`
- D2/T438/T449 context.

## Collision Check

The worktree was already dirty before this run. Preexisting local changes include
modified governance files (`AGENTS.md`, `CLAIM-LEDGER.md`, `CONTRIBUTING.md`,
`steward/README.md`) plus untracked T442 artifacts. Those files are treated as
user/prior-run owned and must not be edited, staged, committed, reverted, or used
as writable surfaces by this run.

`T450` is free in repo-local search except for unrelated timestamp substrings
inside old persona-goal files.

## Selected Objective

Take the next best swing after T449: test whether the period-hardness target is
actually independent of the T417/Rabin trapdoor, or whether any useful period
oracle collapses to predecessor recovery and hence to factoring.

## Guardrails

- No North Star changes.
- No edits to `CLAIM-LEDGER.md`, `TESTS.md`, `ROADMAP.md`, dirty governance files,
  public posture, hard policy, or cross-repo truth.
- No D2 redesign/abandon decision unless earned by runnable artifact.
- Treat cryptography/complexity as the object of study, not evidence for physics.

## Plan

1. Build a T450 executable audit:
   - period oracle -> predecessor oracle;
   - predecessor oracle -> factorization by Rabin reduction;
   - factorization/group-order completion -> period computation.
2. Add a frozen spec and focused tests.
3. Generate JSON/Markdown result artifacts.
4. Append conservative context notes to the D2 open problem, taxonomy reference,
   steward memory, and this receipt.
5. Stage only this run's files, verify, commit, and push.

## Execution Notes

Created:

- `models/e2_period_oracle_trapdoor_equivalence.py`
- `tests/test_e2_period_oracle_trapdoor_equivalence.py`
- `tests/T450-e2-period-oracle-trapdoor-equivalence.md`
- `results/T450-e2-period-oracle-trapdoor-equivalence-v0.1.json`
- `results/T450-e2-period-oracle-trapdoor-equivalence-v0.1-results.md`

Updated:

- `open-problems/computational-finality-arrow.md`
- `technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`
- `steward/memory-log.md`

## Run Receipt

- Outcome: completed.
- Verdict:
  `PERIOD_ORACLE_COLLAPSES_TO_RABIN_TRAPDOOR_NO_INDEPENDENT_D2_ROUTE`.
- Result: for the current closed public-squaring route, an all-target period
  oracle is trapdoor-strength. A target period gives the unique predecessor by
  public forward iteration, and Rabin's square-root oracle reduction factors `N`
  from that predecessor oracle. Conversely, group-order/factorization completion
  computes periods.
- Interpretation: the current closed public-squaring period route has no
  independent finite-witness residue beyond the standard Rabin/factoring
  boundary. This strongly recommends a separate governed demotion packet unless a
  future D2 target changes the period-assumption scope.
- Recommended next: continue D2 only if a nonstandard period assumption is
  specified with scope that avoids both single-seed weakness and all-target
  trapdoor equivalence. Otherwise demote the temporal D2 route to T417's static
  E2 boundary in a separate governed decision packet.
- Does not earn: D2 redesign, D2 abandonment, computational-arrow theorem,
  period-hardness theorem, crypto theorem, physics claim, claim-ledger movement,
  TESTS.md movement, ROADMAP.md movement, North Star/canon movement,
  public-posture movement, hard-policy movement, or cross-repo truth movement.
- Protected-surface boundary: this run did not edit the preexisting dirty
  `AGENTS.md`, `CLAIM-LEDGER.md`, `CONTRIBUTING.md`, `steward/README.md`, or any
  preexisting T442 artifact.
- Verification:
  - `python -m pytest tests/test_e2_period_oracle_trapdoor_equivalence.py -q`
    passed 9 tests.
  - `python -m models.e2_period_oracle_trapdoor_equivalence --write-results`
    completed and wrote JSON/Markdown artifacts.
  - `python -m pytest tests/test_e2_period_oracle_trapdoor_equivalence.py
    tests/test_e2_period_hardness_packet_audit.py
    tests/test_e2_period_hardness_admission_gate.py
    tests/test_computational_arrow_of_time.py -q` passed 41 tests.
  - `python -m json.tool
    results/T450-e2-period-oracle-trapdoor-equivalence-v0.1.json` parsed.
  - `python -m compileall -q models/e2_period_oracle_trapdoor_equivalence.py`
    passed.
  - `git diff --check` passed.
- External action: GitHub commit / push only; no non-GitHub external write.
- Local end: 2026-07-04 14:29 CDT.
- Current run time: about 11 minutes.
