# 2026-07-03 Substrate-Law Admission Gate

## Run Envelope

- Run type: Progress
- Automation: Hourly Nobel Prize Winner
- Automation ID: `hourly-nobel-prize-winner`
- Target repository: Time as Finality
- Local start: 2026-07-03 08:03 CDT
- Operator: Codex
- Status: completed

## Governance Loaded

- Workspace routing instructions supplied in chat.
- CapacityOS entrypoint and run convention.
- `AGENTS.md`
- `steward/README.md`
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`,
  `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- Recent automation memory and `steward/memory-log.md`.
- Recent run receipts T432/T433 and adjacent open-problem context.
- Primary open problem context:
  - `open-problems/region-indexed-capability-discriminator.md`
  - `results/T406-transition-system-operation-unavailability-gate-v0.1-results.md`
  - `open-problems/computational-finality-arrow.md`
  - `open-problems/e3-admissibility-adapter-gu-taf.md`

## Recent-Run Collision Check

The worktree was clean on `main` and aligned with `origin/main` at run start.
`git worktree list` showed only this repository worktree:

```text
repos/public/time-as-finality caeb986 [main]
```

The latest landed run was T433, which discharged the classical C-fragment proof
certificate for the capability-boundary taxonomy. D2 computational-arrow redesign
and the specific GU/TaF E3 adapter revival are gated by their local records. This
run therefore selects a non-colliding Direction-A method gate under the primary
region-indexed capability discriminator.

## Selected Objective

Create a recorded-tier T434 substrate-law admission gate:

```text
post-T406 operation-unavailability progress requires a predeclared,
domain-native law or measured substrate dynamics package that forces the
transition relation without reading the transition table itself.
```

This is the biggest safe one-session Progress objective because T406 named the
next live burden directly, while stronger D2/E3 movements would cross explicit
redesign/revival gates.

## Governance Boundary

No North Star changes.

No claim-ledger edits, `TESTS.md` edits, `ROADMAP.md` edits, claim-status
movement, canon movement, public-posture movement, hard-policy edits, D2
redesign/abandon movement, T421/GU adapter revival, quantum E3 claim movement, or
cross-repo truth changes.

T434 is an admission gate and synthetic positive-control shape only. It does not
name a real substrate law and does not discharge the region-indexed capability
discriminator.

## Execution Plan

1. Freeze the T434 spec under `tests/`.
2. Implement an evaluator under `models/` that rejects no-law, transition-table,
   post hoc, pair-specific, hidden-label, non-native-observable, underpowered
   measurement, and fixed-accounting-change packets.
3. Include synthetic positive controls for the admitted shape without treating
   them as evidence.
4. Generate JSON/Markdown results.
5. Update the open problem and steward memory with a bounded status addendum.
6. Run focused tests, JSON parse, diff checks, and protected-surface checks.
7. Append the Run Receipt, then commit and push coherent repo-local changes.

## Execution Notes

Created:

- `tests/T434-substrate-law-admission-gate.md`
- `models/substrate_law_admission_gate.py`
- `tests/test_substrate_law_admission_gate.py`
- `results/T434-substrate-law-admission-gate-v0.1.json`
- `results/T434-substrate-law-admission-gate-v0.1-results.md`

Updated:

- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

## Run Receipt

- Outcome: completed.
- T434 verdict: `SUBSTRATE_LAW_ADMISSION_GATE_BUILT_CURRENT_T406_NOT_ADMITTED`.
- Research result: the current T406 transition split remains unadmitted because
  it has no independent domain-native law or measured-dynamics packet.
- Gate result: transition-table restatements, post hoc laws, pair-specific
  rules, hidden labels, non-native observables, underpowered measured dynamics,
  and fixed-accounting changes are rejected.
- Positive controls: only synthetic conservation-law and measured-dynamics
  controls pass; they calibrate the gate shape but do not supply real substrate
  evidence.
- Next burden: future Direction-A work must bring a concrete predeclared law or
  measured substrate-dynamics packet that clears T434 before re-running the
  region-indexed discriminator.
- Claim ledger: unchanged.
- Test registry: unchanged by design.
- Roadmap and North Star map: unchanged.
- D2 redesign/abandon, quantum E3, T421/GU adapter revival, public posture, hard
  policy, and cross-repo truth: unchanged.
- External action: GitHub commit / push only, as authorized by the automation
  request.
- Verification:
  - `python -m pytest tests/test_substrate_law_admission_gate.py -q` -> 10
    passed.
  - `python -m pytest tests/test_substrate_law_admission_gate.py
    tests/test_transition_system_operation_unavailability_gate.py -q` -> 19
    passed.
  - `python -m json.tool results/T434-substrate-law-admission-gate-v0.1.json`
    -> parsed.
  - `python -m models.substrate_law_admission_gate` -> emitted structured result.
  - `git diff --check` -> clean.
  - Protected-surface diff check -> `CLAIM-LEDGER.md`, `TESTS.md`, `ROADMAP.md`,
    North Star map files unchanged.
  - Scoped ASCII scan over new T434 files and run receipt -> clean.
