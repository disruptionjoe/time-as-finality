# 2026-07-03 M2 Separator-Object Support Gate

## Run Envelope

- Run type: Progress
- Automation: Hourly Nobel Prize Winner
- Automation ID: `hourly-nobel-prize-winner`
- Target repository: Time as Finality
- Local start: 2026-07-03 02:42 CDT
- Operator: Codex
- Status: completed

## Governance Loaded

- Workspace / CapacityOS routing instructions.
- `AGENTS.md`
- `steward/README.md`
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`,
  `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- Recent automation memory and `steward/memory-log.md`.
- Recent M2 artifacts and receipts: T425, T426, T427, and T428.

## Recent-Run Collision Check

The worktree was clean on `main` and aligned with `origin/main` at run start.
`git worktree list` showed only this repository worktree:

```text
repos/public/time-as-finality 3d0e550 [main]
```

The latest completed run was T428. It blocked the common nonquota full-judgment
selector branch and left a genuinely different separator object, or a stronger
aggregation rule with no-selector-leakage controls, as the remaining M2 route.

No open or pending repo-local run artifact overlaps a separator-object support
gate. This run does not continue threshold tuning, does not add a social-choice
claim, and does not touch claim, registry, North Star, canon, or public-posture
surfaces.

## Selected Objective

Create a recorded-tier T429 guardrail for the remaining simple separator-object
escape hatch:

```text
Can a separator object create larger-n SURVIVES-R1 positives without merely
reading support counts, ambient size, deletion-critical wording, or graph
diagnostics already reducible to full support fibers?
```

This is the biggest safe one-session Progress objective because:

- T428 explicitly left separator objects as the next bounded M2 branch.
- It can be tested by finite enumeration without claim-status movement.
- A negative or narrowing result prevents the M2 redesign lane from mistaking
  support/deletion-critical completion for independent canonicity progress.

## Governance Boundary

No North Star changes.

No claim-ledger edits, `TESTS.md` edits, `ROADMAP.md` edits, claim-status
movement, canon movement, public-posture movement, hard-policy edits, or cross-repo
truth changes.

Cross-domain social-choice / index language remains object-of-study only, never
evidence for physics or a sibling repo. Code imports stay standard-library-only.

## Execution Plan

1. Freeze a T429 spec under `tests/`.
2. Build a finite exact model over judgment-state profiles for `n in {3,4,5}` and
   predeclared separator-object predicates.
3. Add focused tests covering the object family, size-local support positives,
   graph-style controls, the ambient-size support leak, and the final verdict.
4. Generate JSON and Markdown results.
5. Append this run receipt, verify, commit, and push coherent repo-local changes.

## Execution Notes

Created:

- `tests/T429-m2-separator-object-support-gate.md`
- `models/m2_separator_object_support_gate.py`
- `tests/test_m2_separator_object_support_gate.py`
- `results/T429-m2-separator-object-support-gate-v0.1.json`
- `results/T429-m2-separator-object-support-gate-v0.1-results.md`

Updated:

- `steward/memory-log.md`

No `TESTS.md`, `CLAIM-LEDGER.md`, `ROADMAP.md`, North Star map, canon,
public-posture, hard-policy, or cross-repo truth edits.

## Run Receipt

- Outcome: completed.
- T429 verdict: `REDESIGN_SEPARATOR_SUPPORT_COMPLETION`.
- Research result: in the bounded `n in {3,4,5}` separator-object family, the only
  object with positives at both n=4 and n=5 is `ambient_even_support_shape`, with
  24 n=4 positives and 240 n=5 positives.
- Guardrail result: the stable object reads ambient support shape directly. Every
  tested separator status is constant on full support-count fibers over
  `(00, 01, 10, 11)`, so support completion recovers the signal.
- Non-ambient controls: all-four-support and both-cross-diagonal objects give only
  n=4 positives and are absorbed at n=5; compatibility-cycle positives are also
  absorbed at n=5; signed-frustration and one-crossing controls do not create
  larger-size SURVIVES-R1 targets.
- Claim ledger: unchanged.
- Test registry: unchanged by design.
- External action: GitHub commit / push only, as authorized by the automation
  request.
- Verification:
  - `python -m pytest tests/test_m2_separator_object_support_gate.py tests/test_m2_nonquota_aggregation_family_gate.py tests/test_m2_threshold_index_leakage_gate.py tests/test_m2_threshold_rule_rescue_gate.py tests/test_m2_size_sweep_absorption_gate.py -q` -> 30 passed.
  - `python -m json.tool results/T429-m2-separator-object-support-gate-v0.1.json > $null` -> parsed.
  - `git diff --check` -> clean.
  - `git diff -- CLAIM-LEDGER.md TESTS.md ROADMAP.md "Vision - North Star.md" "Method - Research Program Guidelines.md" "Lead Research Line - Time as Finality.md"` -> clean.
  - `rg -n "[^\x00-\x7F]"` over new T429/run files -> no non-ASCII matches.
