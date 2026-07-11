# Progress Run: Coupling-Graph Forcing Gate

- Date: 2026-07-02
- Mode: Progress
- Repository: Time as Finality
- Run objective: Build a bounded executable gate for the R2 question exposed by T412/T414/T415: when is the operational factorization or coupling graph independently forced, rather than merely selected because it protects the separator?
- Status: active

## Governance Loaded

- Workspace root instructions from `JB\AGENTS.md` in chat.
- CapacityOS entrypoint: `CapacityOS\Agents Start Here.md`.
- CapacityOS agent map: `CapacityOS\AGENTS.md`.
- CapacityOS run convention: `kernel/run-convention/README.md` and `standard-run-model.md`.
- CapacityOS architecture and subsidiarity context.
- Repo instructions: `AGENTS.md`.
- Repo steward: `steward/README.md`.
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, `Lead Research Line - Time as Finality.md`.
- Contribution and test conventions: `CONTRIBUTING.md`.

## Recent-Run Check

The worktree is clean and aligned with `origin/main`.

Automation memory ended at the T413/T414 numbering-normalization run, but the repository already contains a newer pushed T415 commit:

- `71956c1` - `T415: admissibility-derivation probe (bridge obligation #2) -> structurally bridged, R2-conditional`

T415 is explicitly provisional in its spec and results: `TESTS.md` and `CLAIM-LEDGER.md` were intentionally left untouched and registration pauses for Joe / numbering automation. This run will not normalize or register T415. It will choose a non-overlapping follow-on lane: the R2 coupling/factorization-forcing gate.

## Boundaries

- No North Star, canon, public-posture, cross-repo truth, or claim-ledger movement.
- Cross-domain governance/game material remains object of study, never evidence.
- T416 may register its own executable artifact if verification passes.
- T415 remains provisional and untouched except as cited context.
- GitHub commit/push is authorized by this automation request and is the normal versioning surface.

## Planned Artifact

T416: Coupling-Graph Forcing Gate.

Question:

Does the parity separator itself force the operational automorphism group, or is independent operation/coupling evidence required?

Predeclared expected outcomes:

1. Separator-only evidence does not force the product/coupling automorphism group; it admits the T415 equality-preserving class, including entangling equality-preservers.
2. Independent singleton-operation support evidence forces the product atom structure up to permutation and excludes entangling equality-preservers.
3. Adding a coupling graph further restricts admissible relabels to graph automorphisms.
4. Therefore R2 is not discharged by the separator. It is only locally forced when independent operational evidence supplies the factorization/coupling structure.

Writable surfaces:

- `models/coupling_graph_forcing_gate.py`
- `tests/test_coupling_graph_forcing_gate.py`
- `tests/T416-coupling-graph-forcing-gate.md`
- `results/T416-coupling-graph-forcing-gate-v0.1.json`
- `results/T416-coupling-graph-forcing-gate-v0.1-results.md`
- `TESTS.md`
- `ROADMAP.md`
- `steward/memory-log.md`
- this run artifact

## Execution Log

- 2026-07-02 15:04 CDT: Run plan opened.
- 2026-07-02 15:06 CDT: Implemented T416 model, frozen spec, focused tests, generated JSON, and result summary.
- 2026-07-02 15:08 CDT: Updated `ROADMAP.md`, `TESTS.md`, and `steward/memory-log.md`.

## Run Receipt

- Status: completed
- Completed: 2026-07-02 15:09 CDT
- Objective executed: T416 coupling-graph forcing gate.
- Files created:
  - `models/coupling_graph_forcing_gate.py`
  - `tests/T416-coupling-graph-forcing-gate.md`
  - `tests/test_coupling_graph_forcing_gate.py`
  - `results/T416-coupling-graph-forcing-gate-v0.1.json`
  - `results/T416-coupling-graph-forcing-gate-v0.1-results.md`
- Files updated:
  - `ROADMAP.md`
  - `TESTS.md`
  - `steward/memory-log.md`
  - `steward/runs/2026-07-02-coupling-graph-forcing-gate.md`
- Result: separator-only evidence over `GL(3,2)` admits 24 equality-preserving maps including 18 entangling equality-preservers; singleton-operation support restricts admissibility to 6 product atom permutations; adding a path coupling graph restricts it to 2 graph automorphisms. R2 is not discharged by the separator; it requires independent operation/coupling evidence.
- Claim movement: none.
- North Star / canon / public posture movement: none.
- T415 handling: left provisional and unregistered as its own spec/results request.
- External actions during execution: none before git versioning.
- Verification:
  - `python -m pytest tests/test_coupling_graph_forcing_gate.py -q` -> 7 passed
  - `python -m pytest tests/test_coupling_graph_forcing_gate.py tests/test_admissibility_derivation_probe.py tests/test_separator_refactorization_gate.py -q` -> 21 passed
  - `python -m models.coupling_graph_forcing_gate` -> generated JSON
  - `python -m json.tool results\T416-coupling-graph-forcing-gate-v0.1.json` -> parsed
  - `git diff --check` -> clean
  - scoped ASCII scan on new T416/run files -> clean
- Follow-up: future R2 work should not cite separator-preserving relabels as enough; it must supply independent physical operation, support, or coupling evidence.
