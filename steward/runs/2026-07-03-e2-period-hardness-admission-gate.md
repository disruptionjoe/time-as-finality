# 2026-07-03 E2 Period-Hardness Admission Gate

## Run Envelope

- Run type: Progress
- Automation: Hourly Nobel Prize Winner
- Automation ID: `hourly-nobel-prize-winner`
- Target repository: Time as Finality
- Local start: 2026-07-03 12:04 CDT
- Operator: Codex
- Status: completed

## Governance Loaded

- Workspace routing instructions supplied in chat.
- `CapacityOS\Agents Start Here.md`
- `CapacityOS\AGENTS.md`
- `AGENTS.md`
- `steward/README.md`
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`,
  `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `CapacityOS\kernel\run-convention\README.md`
- `CapacityOS\kernel\run-convention\standard-run-model.md`
- Automation memory and recent local run receipts.
- T417/T419/T420 D2 computational-finality context.
- Repaired capability-boundary taxonomy reference and T437 hostile-review result.

## Recent-Run Collision Check

The worktree was clean on `main` and aligned with `origin/main` at run start.
`git worktree list` showed only this repository worktree. The latest landed run
was T437, which cleared the repaired taxonomy only for internal use as a mode
classifier and explicitly left D2 redesign/abandon separately gated.

## Selected Objective

Create T438, an E2 period-hardness admission gate for future computational-finality
attempts:

```text
After T419/T420, a D2 computational-arrow candidate cannot rely on a toy finite
public cycle. It must supply a family-level period-hardness packet, leave the
closed public-permutation regime, change the public-transition-knowledge regime,
or demote to T417's static E2 boundary.
```

This is the biggest safe one-session Progress objective because it converts the
post-T420 redesign rule into an executable classifier without taking the gated
D2 redesign/abandon decision.

## Governance Boundary

No North Star changes.

No claim-ledger edits, `TESTS.md` edits, `ROADMAP.md` edits, claim-status movement,
canon movement, public-posture movement, hard-policy edits, D2 redesign/abandon
decision, public crypto/physics claim, or cross-repo truth movement.

T438 is a repo-local admission gate only.

## Execution Plan

1. Freeze the T438 spec under `tests/`.
2. Implement an executable classifier under `models/`.
3. Include positive, negative, and demotion controls for period-hardness packets.
4. Generate JSON/Markdown results.
5. Update the D2 open problem, taxonomy reference, and steward memory only if the
   result remains a guardrail.
6. Run focused and adjacent verification, JSON parse, model execution, diff checks,
   protected-surface checks, and scoped ASCII scan.
7. Append the Run Receipt, then commit and push coherent repo-local changes.

## Execution Notes

Created:

- `tests/T438-e2-period-hardness-admission-gate.md`
- `models/e2_period_hardness_admission_gate.py`
- `tests/test_e2_period_hardness_admission_gate.py`
- `results/T438-e2-period-hardness-admission-gate-v0.1.json`
- `results/T438-e2-period-hardness-admission-gate-v0.1-results.md`

Updated:

- `open-problems/computational-finality-arrow.md`
- `technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`
- `steward/memory-log.md`

## Run Receipt

- Outcome: completed.
- T438 verdict:
  `E2_PERIOD_HARDNESS_ADMISSION_GATE_BUILT_NO_D2_DECISION`.
- Research result: T438 admits only a predeclared family-level period-hardness
  packet as a future E2 redesign target. It rejects finite public cycles, bounded
  non-recovery, point-inversion-only static relabels, E1 thermodynamic packets,
  Brown-Susskind complexity-growth packets, single-instance claims, and post-hoc
  selectors. Changed-public-transition and open/nonpermutation packets route to a
  separate spec.
- Does not earn: D2 redesign, D2 abandonment, computational arrow, crypto theorem,
  physics claim, claim-ledger movement, public-posture movement, or cross-repo
  support.
- Claim ledger: unchanged.
- Test registry: unchanged by design.
- Roadmap and North Star map: unchanged.
- External action: GitHub commit / push only, as authorized by the automation
  request.
- Verification:
  - `python -m pytest tests/test_e2_period_hardness_admission_gate.py -q` ->
    10 passed.
  - `python -m pytest tests/test_e2_period_hardness_admission_gate.py
    tests/test_finite_cycle_anti_relabel_gate.py
    tests/test_computational_arrow_of_time.py -q` -> 30 passed.
  - `python -m json.tool results/T438-e2-period-hardness-admission-gate-v0.1.json`
    -> parsed.
  - `python -m models.e2_period_hardness_admission_gate` -> emitted structured
    result.
  - `git diff --check` -> clean.
  - Protected-surface diff check -> `CLAIM-LEDGER.md`, `TESTS.md`, `ROADMAP.md`,
    and North Star map files unchanged.
  - Scoped ASCII scan -> clean for new T438 files and run receipt.
