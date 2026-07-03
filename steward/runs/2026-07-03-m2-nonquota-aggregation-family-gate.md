# 2026-07-03 M2 Nonquota Aggregation Family Gate

## Run Envelope

- Run type: Progress
- Automation: Hourly Nobel Prize Winner
- Automation ID: `hourly-nobel-prize-winner`
- Target repository: Time as Finality
- Local start: 2026-07-03 02:04 CDT
- Operator: Codex
- Status: completed

## Governance Loaded

- Workspace / CapacityOS routing instructions.
- CapacityOS canonical architecture, subsidiarity architecture, run convention,
  and standard Progress run model.
- `AGENTS.md`
- `steward/README.md`
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`,
  `Lead Research Line - Time as Finality.md`
- Recent automation memory and `steward/memory-log.md`.
- Recent M2 artifacts and receipts: T423, T424, T425, T426, and T427.

## Recent-Run Collision Check

The worktree was clean on `main` and aligned with `origin/main` at run start.
`git worktree list` showed only this repository worktree:

```text
C:/Users/joe/JB/CapacityOS/repos/public/time-as-finality 10d09d3 [main]
```

The latest completed run is T427. It blocks the threshold-index reading and names
the remaining safe M2 escape hatches:

```text
genuinely different aggregation family or separator object
```

No open or pending repo-local run artifact overlaps a nonquota aggregation-family
gate. This run will not continue threshold tuning, not change the inherited M2
recorded-tier standing, and not edit claim or public-posture surfaces.

## Selected Objective

Create a recorded-tier T428 guardrail for the first remaining M2 escape hatch:

```text
Can a genuinely nonquota aggregation family create a larger-n SURVIVES-R1
finality target without merely hard-coding the premise/conclusion choice,
selecting a representative judgment, or reading full support counts?
```

This is the biggest safe one-session Progress objective because:

- T427 explicitly closed the threshold-index reading and pointed to a different
  aggregation family as one remaining lane.
- Common judgment-aggregation repairs can be tested by finite enumeration without
  moving any claim status.
- A negative or narrowing result prevents the M2 redesign lane from mistaking a
  rule-completion artifact for canonicity progress.

## Governance Boundary

No North Star changes.

No claim-ledger edits, claim-status movement, canon movement, public-posture
movement, hard-policy edits, or cross-repo truth changes.

Cross-domain social-choice / judgment-aggregation language remains object-of-study
only, never evidence for physics or a sibling repo. Code imports must stay
TaF-native plus standard library modules.

## Execution Plan

1. Freeze a T428 spec under `tests/`.
2. Build a finite exact model over AND-doctrine profiles for `n in {3, 4, 5}` and
   predeclared nonquota aggregation families.
3. Add focused tests covering nonquota status, T423/T425 regression, selector and
   tie-completion controls, and the final guardrail verdict.
4. Generate JSON and Markdown results.
5. Append this run receipt, verify, commit, and push coherent repo-local changes.

## Execution Notes

Created:

- `tests/T428-m2-nonquota-aggregation-family-gate.md`
- `models/m2_nonquota_aggregation_family_gate.py`
- `tests/test_m2_nonquota_aggregation_family_gate.py`
- `results/T428-m2-nonquota-aggregation-family-gate-v0.1.json`
- `results/T428-m2-nonquota-aggregation-family-gate-v0.1-results.md`

Updated:

- `steward/memory-log.md`

No `TESTS.md`, `CLAIM-LEDGER.md`, `ROADMAP.md`, North Star map, canon,
public-posture, hard-policy, or cross-repo truth edits.

## Run Receipt

- Outcome: completed.
- T428 verdict: `REDESIGN_NONQUOTA_SELECTOR_COMPLETION`.
- Research result: common nonquota full-judgment selectors do not repair M2
  canonicity in the bounded `n in {3,4,5}` AND-doctrine test. Conservative
  plurality/reject and minimax/reject create 24 n=4 `SURVIVES-R1` profiles each,
  but no tested selector has positives at both n=4 and n=5.
- Guardrail result: every selector separator is constant on full support-count
  fibers over `(00, 01, 10, 11)`, so the positives are selector/full-support
  completion artifacts rather than independent finality channels.
- Baseline control: strict conclusion-majority reproduces the inherited M2 size
  pattern: 6 n=3 positives, 0 n=4 positives, 0 n=5 positives, with n=4 and n=5
  nonzero gaps absorbed into proper subsets.
- Claim ledger: unchanged.
- Test registry: unchanged by design.
- External action: GitHub commit / push only, as authorized by the automation
  request.
- Verification:
  - `python -m pytest tests/test_m2_nonquota_aggregation_family_gate.py tests/test_m2_threshold_index_leakage_gate.py tests/test_m2_threshold_rule_rescue_gate.py tests/test_m2_size_sweep_absorption_gate.py -q` -> 24 passed.
  - `python -m json.tool results/T428-m2-nonquota-aggregation-family-gate-v0.1.json > $null` -> parsed.
  - `git diff --check` -> clean.
  - `git diff -- CLAIM-LEDGER.md TESTS.md ROADMAP.md "Vision - North Star.md" "Method - Research Program Guidelines.md" "Lead Research Line - Time as Finality.md"` -> clean.
