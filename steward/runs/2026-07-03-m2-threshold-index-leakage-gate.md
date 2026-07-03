# 2026-07-03 M2 Threshold-Index Leakage Gate

## Run Envelope

- Run type: Progress
- Automation: Hourly Nobel Prize Winner
- Automation ID: `hourly-nobel-prize-winner`
- Target repository: Time as Finality
- Local start: 2026-07-03 01:02 CDT
- Operator: Codex
- Status: completed

## Governance Loaded

- `AGENTS.md`
- `steward/README.md`
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- Recent automation memory and steward memory.
- Recent M2 receipts and artifacts: T423, T424, T425, and T426.

## Recent-Run Collision Check

The worktree was clean on `main` and aligned with `origin/main` at run start.
`git worktree list` showed only this repository worktree:

```text
C:/Users/joe/JB/CapacityOS/repos/public/time-as-finality 81b0df1 [main]
```

No open or pending repo-local run artifact overlaps the threshold-index leakage
gate selected here.

## Selected Objective

Create a recorded-tier T427 guardrail for the T426 high-quota positive cells:

```text
Can any candidate index distinguish the size-matched high-quota SURVIVES-R1
targets without merely reading the quota/size step or the profile support
pattern that creates that step?
```

This is the biggest safe one-session Progress objective because:

- T426 explicitly says follow-up index work must include threshold-tuning
  controls before any canonicity reading.
- The test can be finite, exact, repo-local, and non-promotional.
- A negative or narrowing result prevents quota-tuned witnesses from being
  mistaken for stable M2 progress.

## Governance Boundary

No North Star changes.

No claim-ledger edits, claim-status movement, canon movement, public-posture
movement, hard-policy edits, or cross-repo truth changes.

Cross-domain social-choice / index language remains object-of-study only, never
evidence for physics or a sibling repo. Code imports must stay TaF-native plus
standard library modules.

## Execution Plan

1. Freeze a T427 spec under `tests/`.
2. Build a finite model that inspects the T426 positive cells and matched
   controls for index leakage through quota/size/support-shape data.
3. Add focused tests covering leakage controls, T426 regression, and the final
   guardrail verdict.
4. Generate JSON and Markdown results.
5. Append this run receipt, verify, commit, and push coherent repo-local changes.

## Execution Notes

Created:

- `tests/T427-m2-threshold-index-leakage-gate.md`
- `models/m2_threshold_index_leakage_gate.py`
- `tests/test_m2_threshold_index_leakage_gate.py`
- `results/T427-m2-threshold-index-leakage-gate-v0.1.json`
- `results/T427-m2-threshold-index-leakage-gate-v0.1-results.md`

Updated:

- `steward/memory-log.md`

No `TESTS.md`, `CLAIM-LEDGER.md`, North Star, canon, public-posture,
hard-policy, or cross-repo truth edits.

## Run Receipt

- Outcome: completed.
- T427 verdict: `REDESIGN_THRESHOLD_INDEX_LEAKAGE`.
- Research result: across the four high-quota target/control cells
  `3/4@n=4`, `3/4@n=5`, `4/5@n=4`, and `4/5@n=5`, there are 2,560 profiles
  and 32 SURVIVES-R1 targets. The only perfect separator channels are
  cell-local support, support plus quota step, and quota-margin signature
  `(0, 0, -1, 0)`, all direct quota/support leaks.
- Candidate-index result: crossing count, compatibility cycle rank, signed
  frustration index, and their graph diagnostic triple all collide with
  nonseparator profiles. No clean quota-independent index channel was found in
  the tested family.
- Reading: T426's high-quota positives remain finite threshold testbeds, not a
  stable M2 canonicity lift. Future M2 work should move to a genuinely different
  aggregation family or separator object, or predeclare a new index with a
  stronger no-leakage control.
- Claim ledger: unchanged.
- Test registry: unchanged by design.
- External action: GitHub commit / push only, as authorized by the automation
  request.
- Verification:
  - `python -m pytest tests/test_m2_threshold_index_leakage_gate.py tests/test_m2_threshold_rule_rescue_gate.py tests/test_m2_size_sweep_absorption_gate.py -q` -> 18 passed.
  - `python -m json.tool results/T427-m2-threshold-index-leakage-gate-v0.1.json > $null` -> parsed.
  - `git diff --check` -> clean.
  - `git diff -- CLAIM-LEDGER.md TESTS.md` -> clean.
