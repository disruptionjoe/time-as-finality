# Progress Run: Finite-Cycle Anti-Relabel Gate

- Date: 2026-07-02
- Mode: Progress
- Repository: Time as Finality
- Automation: Hourly Nobel Prize Winner
- Run objective: Formalize the T419 anti-relabel failure as an executable finite-cycle guardrail without taking the gated D2 redesign/abandon decision.
- Status: completed

## Governance Loaded

- Workspace root instructions from `JB\AGENTS.md` in chat.
- CapacityOS entrypoint: `CapacityOS\Agents Start Here.md`.
- CapacityOS agent map: `CapacityOS\AGENTS.md`.
- CapacityOS run convention: `kernel/run-convention/README.md` and `standard-run-model.md`.
- Repo instructions: `AGENTS.md`.
- Repo steward: `steward/README.md`.
- North Star map: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, and `Lead Research Line - Time as Finality.md`.
- Contribution and local run conventions: `CONTRIBUTING.md`, recent `steward/runs/`, and `steward/memory-log.md`.
- Current D2 context: `open-problems/computational-finality-arrow.md`, `technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`, T419 spec/model/results, T110 finite-permutation obstruction, and recent D2/taxonomy receipts.

## Recent-Run Check

The worktree was clean and aligned with `origin/main` at run start. The most recent
run closed the T419 computational-arrow record repair with a completed receipt and
a pushed commit. No active dirty work was present.

The D2 open problem says the redesign/abandon decision pauses for Joe. This run
therefore does not choose redesign or abandon. It selects a non-promotional
guardrail: make the failure condition executable so the later decision has a clear
test.

## Boundaries

- Do not promote a claim.
- Do not edit `CLAIM-LEDGER.md`.
- Do not alter North Star, canon, hard policy, public posture, or cross-repo truth.
- Do not claim a computational arrow or discharge D2.
- Do not treat cryptography, number theory, or cross-domain material as physics evidence.
- GitHub commit/push is authorized by this automation request and is the normal versioning surface.

## Planned Artifact

T420 finite-cycle anti-relabel gate.

Question:

Can the T419 K4 failure be stated as a finite public-permutation guardrail?

Expected result:

```text
If an alleged arrow is exhibited on a closed finite public permutation and the
cycle containing the observed state is discoverable within the declared feasible
bound, then the predecessor is recovered by public forward iteration:

  predecessor(y) = F^(L-1)(y)

where L is the cycle length.
```

Therefore a toy closed permutation cycle cannot by itself support the D2 temporal
arrow. A later D2 redesign must either declare a family-level period-hardness
assumption, leave the closed public-permutation toy regime, or demote to T417's
static E2 boundary.

## Execution Log

- 2026-07-02 CDT: Governance and recent receipts loaded; D2 redesign/abandon treated as gated.
- 2026-07-02 19:01 CDT: Added T420 spec, model, focused tests, result note, and initial run artifact.
- 2026-07-02 19:04 CDT: Focused T420 test and model execution passed.
- 2026-07-02 19:07 CDT: Linked T420 from `TESTS.md`, the D2 open problem, the capability-boundary taxonomy reference, and the lead-line status paragraph.
- 2026-07-02 19:08 CDT: Ran adjacent T419/T110 regressions and closeout checks.

## Verification

- `python -m pytest tests/test_finite_cycle_anti_relabel_gate.py -q` - 8 passed.
- `python -m models.finite_cycle_anti_relabel_gate` - deterministic JSON emitted.
- `python -m pytest tests/test_finite_cycle_anti_relabel_gate.py tests/test_computational_arrow_of_time.py tests/test_finite_permutation_monotone_obstruction.py -q` - 26 passed.
- `python -m models.finite_cycle_anti_relabel_gate | python -m json.tool > $null` - passed.
- `git diff --check` - clean.
- Scoped ASCII scan on the new T420 support/run files - clean.

## Run Receipt

- Status: completed
- Completed: 2026-07-02 19:08 CDT
- Objective executed: finite-cycle anti-relabel gate v0.1.
- Files created:
  - `models/finite_cycle_anti_relabel_gate.py`
  - `tests/test_finite_cycle_anti_relabel_gate.py`
  - `tests/T420-finite-cycle-anti-relabel-gate.md`
  - `results/T420-finite-cycle-anti-relabel-gate-v0.1-results.md`
  - `steward/runs/2026-07-02-finite-cycle-anti-relabel-gate.md`
- Files updated:
  - `TESTS.md`
  - `open-problems/computational-finality-arrow.md`
  - `technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`
  - `Lead Research Line - Time as Finality.md`
  - `steward/memory-log.md`
- Result: T420 formalizes the finite-cycle anti-relabel guard. On a closed finite public permutation, a state on a cycle of length `L` has predecessor `F^(L-1)(y)`, so a traversable toy cycle cannot support the D2 temporal anti-relabel leg. Applied to T419's `QR_77` squaring permutation, every cycle publicly reverses within at most three forward steps and the seed-4 predecessor is `9`.
- Claim movement: none.
- D2 decision movement: none; redesign/abandon still pauses for Joe.
- North Star / canon / public posture / cross-repo truth movement: none.
- `CLAIM-LEDGER.md` movement: none.
- External actions during execution: none before git versioning.
- Verification: see above.
- Follow-up: any later D2 redesign must declare family-level period hardness, change public-transition knowledge, leave the closed public-permutation regime, or demote the temporal story to T417.
- Current run time: about 20 minutes.
