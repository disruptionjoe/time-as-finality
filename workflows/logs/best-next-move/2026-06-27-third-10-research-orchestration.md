# Third 10 Research Orchestration

Date: 2026-06-27
Status: completed-or-in-progress orchestration batch
Scope: synthesis/preflight artifacts only

This batch follows the 2026-06-27 next-10 queue and the completed synthesis
artifacts from the second batch. It deliberately avoids canonical edits:
no claim-ledger changes, no roadmap changes, no tests, no models, no results,
and no open-problem rewrites.

## Shared Constraints

- Every output is a non-authoritative synthesis/preflight log.
- Every output must include no-promotion guardrails.
- External-data branches remain blocked unless a named external packet exists.
- Dormant open problems stay dormant unless the artifact explicitly supplies a
  bounded executable next step.
- Success means the next admissible object is clearer, not that a claim is
  stronger.

## Task 1 - Q1A Same-Closure-Key Reopen Preflight

Owner: worker A
Output:
`workflows/logs/synthesis/2026-06-27-q1a-same-closure-key-reopen-preflight.md`

Source surfaces:

- `open-problems/q1a-same-closure-key-handoff.md`
- `CLAIM-LEDGER.md` Q1/Q1A rows
- T102/T104/T105/T109/T118/T147 context

Acceptance:

- Freezes the same-closure-key burden.
- Names admissible same-closure-key split and physical partition-rule routes.
- Rejects closed-family toy-model restarts.
- Keeps Q1A `bookkeeping_only`.

## Task 2 - Q1B Federated Detector Manifest Preflight

Owner: worker A
Output:
`workflows/logs/synthesis/2026-06-27-q1b-federated-detector-manifest-preflight.md`

Source surfaces:

- `open-problems/q1b-federated-detector-deployment-handoff.md`
- `CLAIM-LEDGER.md` Q1/Q1B rows
- T136/T138/T161/T173/T175/T176/T178 context

Acceptance:

- Converts the external blocker into a pre-data manifest checklist.
- Separates raw-log, provisional-admission, and claim-review tiers.
- Requires event-level rows and challenge-window rights.
- Keeps Q1B externally blocked without a named signatory.

## Task 3 - Q1C Auxiliary-Channel Platform Preflight

Owner: worker A
Output:
`workflows/logs/synthesis/2026-06-27-q1c-auxiliary-channel-platform-preflight.md`

Source surfaces:

- `open-problems/q1c-auxiliary-channel-platform-handoff.md`
- `CLAIM-LEDGER.md` Q1/Q1C rows
- T146/T149/T150/T158/T166/T182/T183 context

Acceptance:

- Freezes the `R, A, H, V, L` packet burden.
- Requires full ordinary event-level record, not dashboard summaries.
- Blocks auxiliary-defined, rare-target, postselected, and screened-off routes.
- Keeps Q1C dormant without a named platform packet.

## Task 4 - H7 Physical-Deletion Substrate Preflight

Owner: worker B
Output:
`workflows/logs/synthesis/2026-06-27-h7-physical-deletion-substrate-preflight.md`

Source surfaces:

- `open-problems/h7-physical-deletion-substrate-handoff.md`
- H7 ledger rows and T145/T148/T152/T160/T168 context
- N8/N11/N12/N14 absorber maps

Acceptance:

- Converts H7's reinstatement gate into a substrate intake packet.
- Distinguishes physical deletion from access loss, provenance loss, and copy
  removal.
- Requires matched absorber vector and finite control class.
- Keeps H7 demoted absent a named substrate.

## Task 5 - Barandes Null-Model Comparator Preflight

Owner: worker B
Output:
`workflows/logs/synthesis/2026-06-27-barandes-null-model-comparator-preflight.md`

Source surfaces:

- `open-problems/barandes-stochastic-quantum-comparison-note-2026-06-24.md`
- Q1/T10/T131 and record/readout separation context

Acceptance:

- Treats stochastic/CPTP/unitary dilation as a strong null model.
- Requires future quantum-facing notes to separate absorber-owned behavior from
  surviving record/finality/access structure.
- Does not treat Barandes as TaF evidence.

## Task 6 - Observer-Shadow Category Bounded-Run Preflight

Owner: worker C
Output:
`workflows/logs/synthesis/2026-06-27-observer-shadow-category-bounded-run-preflight.md`

Source surfaces:

- `open-problems/observer-shadow-category.md`
- typed transport and LossKernel finite-family context

Acceptance:

- States object and morphism schema.
- Names composition-preservation hypotheses and obstruction classes.
- Produces a bounded-run plan over two finite families.
- Does not claim a North Star geometry.

## Task 7 - Cross-Domain Shadow Protection Two-Fill Preflight

Owner: worker C
Output:
`workflows/logs/synthesis/2026-06-27-cross-domain-shadow-protection-two-fill-preflight.md`

Source surfaces:

- `open-problems/cross-domain-shadow-protection-theorem.md`
- `workflows/templates/north-star-shadow-audit.template.md` if present

Acceptance:

- Converts the first bounded run into two fill packets.
- Compares only proof spine: visible fiber, capability spread, native absorber,
  minimal enrichment.
- Preserves dormant status until filled.

## Task 8 - Obstruction Relocation / Reconstruction Debt Preflight

Owner: worker C
Output:
`workflows/logs/synthesis/2026-06-27-obstruction-relocation-reconstruction-debt-preflight.md`

Source surfaces:

- `open-problems/obstruction-relocation-reconstruction-debt.md`
- LossKernel, provenance, gap, and admissibility examples

Acceptance:

- Uses relocation/debt language, not conservation-law language.
- Defines audit fields and candidate classifications.
- Includes a negative-control requirement.
- Keeps the line dormant until a bounded audit exists.

## Task 9 - Non-Static Boundary D1 Preflight

Owner: worker B
Output:
`workflows/logs/synthesis/2026-06-27-non-static-boundary-d1-preflight.md`

Source surfaces:

- `open-problems/finality-under-non-static-boundaries.md`
- D1/B1/R1 context

Acceptance:

- Defines moving-boundary data without a hidden global clock.
- Names the comparable-timescale record class and sweep-region signature.
- States static-boundary absorption conditions.
- Keeps the line dormant absent a finite fixture.

## Task 10 - Typed-Loss Kappa Transport Preflight

Owner: worker C
Output:
`workflows/logs/synthesis/2026-06-27-typed-loss-kappa-transport-preflight.md`

Source surfaces:

- `open-problems/typed-loss-transport-test.md`
- T39 CSP-PO1, T21 Bell/CHSH, T28 CAP/consensus context
- T220 obligation-factorization context

Acceptance:

- Freezes domain-neutral kappa before native B computation.
- Names A -> B map obligations and prediction protocol.
- Requires pass/fail verdicts that are non-vacuous.
- Avoids physics, geometry, or new-object promotion.

## Verification Plan

After all worker outputs land:

1. Confirm all 10 files exist under `workflows/logs/synthesis/`.
2. Check for guardrail and acceptance sections.
3. Run `git diff --check`.
4. Run the runner-focused tests.
5. Run full unit discovery unless no code changed after the previous full pass.
