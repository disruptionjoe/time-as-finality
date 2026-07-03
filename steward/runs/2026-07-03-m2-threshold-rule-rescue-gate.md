# 2026-07-03 M2 Threshold-Rule Rescue Gate

## Run Envelope

- Run type: Progress
- Automation: Hourly Nobel Prize Winner
- Automation ID: `hourly-nobel-prize-winner`
- Target repository: Time as Finality
- Local start: 2026-07-03 00:03 CDT
- Operator: Codex
- Status: active

## Governance Loaded

- Workspace / CapacityOS routing instructions.
- CapacityOS run convention and standard Progress run model.
- `AGENTS.md`
- `steward/README.md`
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- Recent `steward/runs/` receipts, especially T423-T425.
- M2 artifacts: T423 observer-game, T424 Route-A index probe, and T425 size-sweep absorption gate.

## Recent-Run Collision Check

The worktree was clean on `main` and aligned with `origin/main` at run start.
`git worktree list` showed only this repository worktree:

```text
C:/Users/joe/JB/CapacityOS/repos/public/time-as-finality 5ed68d3 [main]
```

The latest completed run is T425. It closed the direct larger-index rescue for
the inherited AND / strict-majority rule, and explicitly named the remaining
rescue classes:

```text
different aggregation family, threshold rule, or separator object
```

No open or pending repo-local run artifact overlaps a threshold-rule rescue gate.

## Selected Objective

Create a recorded-tier T426 threshold-rule rescue gate for M2:

```text
Can a predeclared quota threshold rule create a non-atomic n=4 or n=5
SURVIVES-R1 finality target under the same AND doctrine, or is every candidate
either absent, absorbed by a proper subset, or threshold-tuned residue?
```

This is the biggest safe one-session Progress objective because:

- T425 already says the inherited strict-majority rule is atomic at n=3.
- A threshold rule is one of the explicitly named remaining M2 rescue classes.
- The test can stay fully finite, exact, repo-local, and non-promotional.
- A negative result prevents arbitrary quota tuning from being mistaken for
  canonical index progress.

## Governance Boundary

No North Star changes.

No claim-ledger edits, claim-status movement, canon movement, public-posture
movement, hard-policy edits, or cross-repo truth changes.

Cross-domain social-choice / index language remains object-of-study only, never
evidence for physics or a sibling repo. Code imports must stay TaF-native plus
standard library modules.

## Execution Plan

1. Freeze a T426 spec under `tests/`.
2. Build a finite exact model over AND-doctrine profiles for `n in {3, 4, 5}` and
   predeclared quota fractions.
3. Add focused tests covering threshold predeclaration, strict-majority
   regression to T425, larger-n rescue detection, and tuning-risk classification.
4. Generate JSON and Markdown results.
5. Append this run receipt, verify, commit, and push coherent repo-local changes.

## Execution Notes

Created:

- `tests/T426-m2-threshold-rule-rescue-gate.md`
- `models/m2_threshold_rule_rescue_gate.py`
- `tests/test_m2_threshold_rule_rescue_gate.py`
- `results/T426-m2-threshold-rule-rescue-gate-v0.1.json`
- `results/T426-m2-threshold-rule-rescue-gate-v0.1-results.md`

Updated:

- `steward/memory-log.md`

No `TESTS.md`, `CLAIM-LEDGER.md`, North Star, canon, public-posture,
hard-policy, or cross-repo truth edits.

## Run Receipt

- Outcome: completed.
- T426 verdict: `RECHECK_SIZE_MATCHED_THRESHOLD_ONLY`.
- Research result: high fixed quota fractions can create larger-n SURVIVES-R1
  targets, but only in size-matched cells. `3/4` creates 12 n=4 targets and then
  absorbs at n=5; `4/5` creates 20 n=5 targets and has no n=4 target. No single
  fixed quota survives both n=4 and n=5.
- Threshold reading: the positive cells share the rule shape "grand accepts at
  n-1 of n while top proper coalitions require unanimity." Treat them as finite
  testbeds, not a stable M2 rescue.
- Claim ledger: unchanged.
- Test registry: unchanged by design.
- External action: GitHub commit / push only, as authorized by the automation
  request.
- Verification:
  - `python -m pytest tests/test_m2_threshold_rule_rescue_gate.py tests/test_m2_size_sweep_absorption_gate.py -q` -> 13 passed.
  - `python -m json.tool results/T426-m2-threshold-rule-rescue-gate-v0.1.json > $null` -> parsed.
  - `git diff --check` -> clean.
  - `git diff -- CLAIM-LEDGER.md TESTS.md` -> clean.
