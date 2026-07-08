# Progress Run: T506 Boundary-Adapter Dimension-Carrying Embedding Gate

Status: closed
Run family: Repo Progress Run
Mode: execute
Target repo: time-as-finality
Workflow: repo-progress-run

## Objective

Make the named post-faithfulness defect in the boundary-adapter lane
executable: the current flat D1 profile collapses the pure-physical dimension
distinction `F(W+) -> F(W+0)`. Build a TaF-side synthetic gate that tests
whether a dimension-carrying capability encoding blocks that collapse while
preserving the already-protected physical/mirror face distinction.

## Context Reads

- JB root `AGENTS.md`
- CapacityOS `Agents Start Here.md`
- CapacityOS `AGENTS.md`
- Repo `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `TESTS.md`
- `steward/memory-log.md`
- `steward/runs/2026-07-07-observer-system-gauge-reality-gate.md`
- `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`
- `models/boundary_adapter_functor.py`
- `models/boundary_adapter_functor_faithfulness.py`
- `models/boundary_adapter_second_ti.py`
- `models/observer_system_gauge_reality_gate.py`
- `models/typed_transport_category.py`
- `models/d1_restriction_system.py`

## Recent Run Collision Check

At run start, `main` was aligned with `origin/main` at `e9279f3`. `T506` was
unused in `TESTS.md`, `tests/`, `models/`, `results/`, and `steward/`. One
worktree was registered. The working tree was clean and no newer active
overlapping local run record was present.

## Expected Writable Surfaces

- `models/boundary_adapter_dimension_carrying_embedding_gate.py`
- `tests/test_boundary_adapter_dimension_carrying_embedding_gate.py`
- `tests/T506-boundary-adapter-dimension-carrying-embedding-gate.md`
- `results/T506-boundary-adapter-dimension-carrying-embedding-gate-v0.1.json`
- `results/T506-boundary-adapter-dimension-carrying-embedding-gate-v0.1-results.md`
- `TESTS.md`
- `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`
- `steward/memory-log.md`
- this run artifact

## Forbidden Actions And Stop Conditions

- Do not inspect or modify sibling repos.
- Do not change North Star, claim ledger, roadmap, README, public posture,
  hard policy, protected license, papers/published, or cross-repo truth.
- Do not assert real GU source-category truth, real TI source truth, real
  adapter identity, or two-adapter gate closure.
- Stop if the objective requires external publication or non-GitHub external
  action.
- Stop if another active run creates overlapping tracked edits.

## Plan

1. Build a small classifier/model for flat versus dimension-carrying adapter
   encodings.
2. Include controls for the known flat-profile collapse, a dimension-carrying
   positive fixture, a mirror-face preservation check, a too-coarse dimension
   token, a hidden-retuning shortcut, a physics-wrong mirror shortcut, and
   claim/cross-repo shortcut packets.
3. Generate JSON and Markdown results.
4. Register T506 and update the boundary-adapter open problem plus steward
   memory.
5. Validate focused and adjacent suites, run diff/protected-surface checks,
   append receipt, commit, and push.

## Execution Notes

- Added T506 as a repo-local synthetic gate for the boundary-adapter
  dimension-carrying fix.
- Built a packet evaluator for flat D1 encoding, exact dimension-carrying
  embedding, cardinality-only physics-wrong control, noninjective dimension
  control, post-hoc retuning, and governance shortcuts.
- The flat baseline reproduces the known `F(W+) -> F(W+0)` collapse.
- The exact dimension encoding reflects the finite boundary-sector order
  exactly under predeclared dimension atoms, injective site maps, and
  physical/mirror face preservation.
- Generated T506 JSON and Markdown results.
- Updated `TESTS.md`, the boundary-adapter open problem, and steward memory.

## Validation

- Focused T506 suite: `python -m pytest tests/test_boundary_adapter_dimension_carrying_embedding_gate.py -q` -> 11 passed.
- Adjacent T506/T505/T504/T41 regression: `python -m pytest tests/test_boundary_adapter_dimension_carrying_embedding_gate.py tests/test_observer_system_gauge_reality_gate.py tests/test_boundary_adapter_source_category_functor_gate.py tests/test_typed_transport_category.py -q` -> 104 passed.
- Source adapter scripts: `python -m models.boundary_adapter_functor_faithfulness`; `python -m models.boundary_adapter_second_ti` -> both exited 0.
- Result generation and JSON parse passed.
- Compile: `python -m compileall -q models\boundary_adapter_dimension_carrying_embedding_gate.py` passed.
- Diff check: `git diff --check` passed.
- Protected-surface scan passed; no claim ledger, roadmap, README, North Star,
  method, lead-line, AGENTS, license, public-posture, hard-policy, or
  papers/published movement.
- Scoped ASCII scan passed for the new T506 model, test, spec, results, and run
  artifact.
- Added-line absolute-path scan passed.

## Receipt

- Closed: 2026-07-07 20:10 CDT.
- Result: completed.
- Verdict: `DIMENSION_CARRYING_EMBEDDING_GATE_BUILT_REVIEW_ONLY`.
- Files changed for repo work:
  - `models/boundary_adapter_dimension_carrying_embedding_gate.py`
  - `tests/test_boundary_adapter_dimension_carrying_embedding_gate.py`
  - `tests/T506-boundary-adapter-dimension-carrying-embedding-gate.md`
  - `results/T506-boundary-adapter-dimension-carrying-embedding-gate-v0.1.json`
  - `results/T506-boundary-adapter-dimension-carrying-embedding-gate-v0.1-results.md`
  - `TESTS.md`
  - `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`
  - `steward/memory-log.md`
  - this run artifact
- Strongest result: exact dimension atoms plus injective, face-preserving maps
  block the known flat-profile physical-dimension collapse in the local
  synthetic fixture, while preserving the mirror/physical guard.
- Claim/public posture: no real GU source category, real TI source truth,
  GU/TI/TaF adapter identity, two-adapter gate closure, de-correlated adapter
  arrival, claim-ledger movement, roadmap movement, README movement, North Star
  movement, public-posture movement, hard-policy movement, external-publication,
  or cross-repo truth movement.
- External actions: GitHub commit/push authorized as normal repo versioning; no
  other external action.
- Current run time: about 20 minutes after objective selection.
