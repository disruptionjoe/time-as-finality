# 2026-07-04 Dolev Redundancy Feasibility Gate

## Run Envelope

- Run type: Progress
- Target repository: Time as Finality
- Local start: 2026-07-04 09:05 CDT
- Operator: Automation `hourly-nobel-prize-winner`
- Status: completed

## Governance Loaded

- Workspace and CapacityOS routing instructions supplied in chat.
- `C:\Users\joe\JB\CapacityOS\Agents Start Here.md`
- `C:\Users\joe\JB\CapacityOS\AGENTS.md`
- `C:\Users\joe\JB\CapacityOS\kernel\run-convention\README.md`
- `C:\Users\joe\JB\CapacityOS\kernel\run-convention\standard-run-model.md`
- CapacityOS architecture/subsidiarity/decision-index orientation.
- Repo `AGENTS.md`, `steward/README.md`, North Star map, and `CONTRIBUTING.md`.

## Recent-Run Collision Check

The worktree was dirty before this run. Preexisting local changes include
modified governance files plus untracked T442 artifacts and a T442 hostile
review. Those files are treated as user/prior-run owned. This run will not edit,
stage, commit, or revert them.

T442's hostile review refuted the topological heat-cost interpretation and
relocated the surviving topology lead to fault-tolerant feasibility. T443 is
free in `tests/`, `models/`, and `results/`.

## Selected Objective

Build T443: a Dolev-style redundancy feasibility gate for Direction C after the
T442 hostile review.

The objective is to preserve the valid part of the topology intuition without
reintroducing the refuted thermodynamic surcharge: topology may determine
whether robust distributed finality is feasible under Byzantine holder faults,
but this is an admission/feasibility condition, not a heat-cost term.

## Scope Boundaries

- Add new T443 model/test/result/report artifacts.
- Add this repo-local run artifact.
- Append steward memory after completion.
- Do not edit `AGENTS.md`, `CONTRIBUTING.md`, `CLAIM-LEDGER.md`,
  `steward/README.md`, `TESTS.md`, `ROADMAP.md`, North Star files, or any
  preexisting T442 artifact.
- No claim promotion, public-posture change, hard-policy change, H7 movement,
  thermodynamic-arrow theorem, or cross-repo truth movement.

## Execution Plan

1. Implement an exact finite vertex-connectivity calculator for small undirected
   graphs.
2. Encode the synchronous point-to-point Byzantine feasibility admission gate:
   `n >= 3f + 1` and vertex connectivity `kappa(G) >= 2f + 1`.
3. Run line/star/cycle/complete and K3,3 fixtures, including the T442 graph
   family reframed as feasibility rather than cost.
4. Verify focused tests, result JSON, diff hygiene, protected-surface boundary,
   and ASCII for this run's new files.

## Run Receipt

- Outcome: completed.
- Artifacts added:
  - `models/dolev_redundancy_feasibility_gate.py`
  - `tests/test_dolev_redundancy_feasibility_gate.py`
  - `tests/T443-dolev-redundancy-feasibility-gate.md`
  - `results/T443-dolev-redundancy-feasibility-gate-v0.1.json`
  - `results/T443-dolev-redundancy-feasibility-gate-v0.1-results.md`
  - `technical-reports/TECHNICAL-REPORT-dolev-redundancy-feasibility-gate-v0.1.md`
  - `steward/runs/2026-07-04-dolev-redundancy-feasibility-gate.md`
- Verdict: `DOLEV_REDUNDANCY_FEASIBILITY_GATE_BUILT_NO_COST_CLAIM`.
- Research result: topology is preserved only as a robust-finality feasibility
  screen after T442, not as a thermodynamic surcharge. The finite gate encodes
  the known synchronous point-to-point Byzantine condition `n >= 3f + 1` and
  `kappa(G) >= 2f + 1`, using exact small-graph vertex connectivity.
- Fixture result: line/star/cycle k=5 all fail the `f=1` gate; complete k=5
  passes. `K4` is the minimal complete `f=1` pass; `K6` fails `f=2` by node
  count; `K7` passes `f=2`; `K3,3` shows completeness is not required.
- Does not earn: thermodynamic cost floor, H7 support, new distributed-systems
  theorem, claim-ledger movement, TESTS.md/ROADMAP movement, North Star/canon
  movement, public-posture movement, or cross-repo truth movement.
- Verification:
  - `python -m unittest tests.test_dolev_redundancy_feasibility_gate -v` passed
    7 tests.
  - `python -m models.dolev_redundancy_feasibility_gate --write-results`
    emitted the result JSON.
  - `python -m json.tool results/T443-dolev-redundancy-feasibility-gate-v0.1.json`
    parsed successfully.
- Protected-surface boundary: this run did not edit the preexisting dirty
  `AGENTS.md`, `CONTRIBUTING.md`, `CLAIM-LEDGER.md`, `steward/README.md`, or any
  preexisting T442 artifact.
- External action: source check only; no non-GitHub external write.

## Recommended Next

Use T443 as an admission screen before future D1 holder-redundancy artifacts:
declare the fault model, communication model, holder graph, tolerated `f`, and
native feasibility absorber before treating topology as evidence. Any later cost
or thermodynamic reading must come from a separate substrate gate.
