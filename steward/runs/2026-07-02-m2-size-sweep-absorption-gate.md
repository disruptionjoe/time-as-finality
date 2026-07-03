# 2026-07-02 M2 Size-Sweep Absorption Gate

## Run Envelope

- Run type: Progress
- Automation: Hourly Nobel Prize Winner
- Automation ID: `hourly-nobel-prize-winner`
- Target repository: Time as Finality
- Local start: 2026-07-02 23:08 CDT
- Operator: Codex
- Status: active

## Governance Loaded

- Workspace / CapacityOS routing instructions.
- CapacityOS run convention.
- `AGENTS.md`
- `steward/README.md`
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `TESTS.md`, `ROADMAP.md`, `HYPOTHESES.md`, `CLAIM-LEDGER.md` scoped by the M2 / capability-boundary lane.
- Recent `steward/runs/` receipts and `steward/memory-log.md`.

## Recent-Run Collision Check

The worktree was clean on `main` and aligned with `origin/main` at run start.
`git worktree list` showed no alternate active worktree for this repository.

The latest committed state already includes T424, the M2 Route-A n=3 index probe:

- `9c5b733` - `Record M2 observer-game redesign finding`

No open or pending run artifact in `steward/runs/` overlaps a fresh n=3-5 M2
size-sweep stress test. The latest local receipt is the T423 record-coherence
repair; it explicitly left the then-dirty T424 lane untouched. T424 is now
committed, so this run can choose a new non-overlapping lane.

## Selected Objective

Create a recorded-tier T425 size-sweep stress test for the main T424 escape
hatch:

```text
Does moving from the n=3 doctrinal-paradox triangle to n=4 or n=5 give Route A a
real index target by preserving the inherited SURVIVES-R1 finality separator?
```

This is the biggest safe one-session Progress objective because:

- T424 left the n=3 Route-A verdict at REDESIGN but named the size limitation
  honestly.
- A bounded n=3-5 enumeration can directly test whether the size limitation is a
  live rescue route or another wall, including the n=4 even-size case and the
  n=5 odd-size control.
- The artifact can stay entirely repo-local and recorded-tier.

## Governance Boundary

No North Star changes.

No claim-ledger edits, claim-status movement, canon movement, public-posture
movement, hard-policy edits, or cross-repo truth changes.

Cross-domain material remains object-of-study only, never evidence for physics or
another repository. Code imports must stay TaF-native plus standard library
modules.

## Execution Notes

Created:

- `tests/T425-m2-size-sweep-absorption-gate.md`
- `models/m2_size_sweep_absorption_gate.py`
- `tests/test_m2_size_sweep_absorption_gate.py`
- `results/T425-m2-size-sweep-absorption-gate-v0.1.json`
- `results/T425-m2-size-sweep-absorption-gate-v0.1-results.md`

Scoped record-coherence repair:

- Updated `results/T424-m2-route-a-index-probe-v0.1-results.md` to replace stale
  committed-status text with the actual recorded-tier committed standing.
- Updated `explorations/meta-synthesis-reverse-pass-2026-07-02/SYNTHESIS.md` to
  replace stale "not committed" wording for the M2 status.

No `TESTS.md`, `CLAIM-LEDGER.md`, North Star, canon, public-posture, hard-policy,
or cross-repo truth edits.

## Run Receipt

- Outcome: completed.
- T425 verdict: REDESIGN. The inherited T423/T424 SURVIVES-R1 finality datum is
  atomic at n=3 in the finite AND strict-majority family. At n=4 and n=5, every
  nonzero gap is absorbed by a 3-judge proper subset, so a larger index complex is
  blocked before separator-agreement can be tested.
- Research result: the direct T424 larger-index-complex rescue is closed for this
  inherited fixture. Any future M2 rescue must predeclare a different aggregation
  family, threshold rule, or separator object.
- Claim ledger: unchanged.
- Test registry: unchanged by design.
- External action: GitHub commit / push only, as authorized by the automation
  request.
- Verification:
  - `python -m pytest tests/test_m2_observer_game.py tests/test_m2_route_a_index_probe.py tests/test_m2_size_sweep_absorption_gate.py -q` -> 49 passed.
  - `python -m json.tool results/T425-m2-size-sweep-absorption-gate-v0.1.json > $null` -> parsed.
  - `git diff --check` -> clean.
  - `git diff -- CLAIM-LEDGER.md TESTS.md` -> clean.
