---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: noncanonical_audit_snapshot
summarizable: false
unit_of_review: one_research_line
---

# Line Review

**Family:** govern
**Mode:** evaluation
**Status:** Phase 3 design — v1.2 LOCKED for current operating model (design loop
complete; DEC-008, DEC-012, DEC-014, DEC-015). Phase 4 will map this protocol to
execution atoms.

## Purpose

Produce a reconciled **standing** projection for a research line: a legible,
auditable read of where the line stands today. Standing is **governance
legibility**, not scientific validation and not lifecycle authority.

## Governing decisions (preserve)

- Standing is a **derived, non-authoritative projection** — it never becomes
  canonical state.
- Standing is **recomputed each run** from: the **health substrate**
  (`registries/research-line-scorecard.md`), **registry state**
  (`registries/line-registry.md`), the line's **artifacts**, and the **authority
  surfaces** (`CLAIM-LEDGER.md`, `ROADMAP.md`, `HYPOTHESES.md`, `../NORTH-STAR.md`).
  It is not accumulated or hand-edited.
- **Standing snapshots may be retained as audit artifacts** (in `logs/`) but are
  **not canonical state**.
- **Lifecycle actions** belong to `govern/lifecycle-review`.
- **Portfolio reconciliation** belongs to `govern/portfolio-review` (a separate
  workflow) — not line-review.
- **Decision-history promotion** belongs to a later decision/governance review —
  not line-review.
- **Hygiene failures short-circuit scored review** (see Procedure).
- **Mechanical metadata may self-apply** later; **interpretive changes remain
  patch-first**.

## Authority boundaries

- **May:** read the substrate; compute a standing snapshot; raise flags (stale,
  weak-evidence, overlap, mis-scored, blocker, needs-persona-review); mark
  lifecycle candidates; propose interpretive patches; route governance signals.
- **Must not:** move lifecycle states (→ `lifecycle-review`); perform portfolio
  reconciliation (→ `portfolio-review`); promote anything to decision-history;
  treat the standing snapshot as canonical; apply interpretive changes directly.
- **Scoring authority — hybrid:** deterministic where derivable from substrate
  fields; judgment only with explicit rationale.
- **Write authority — patch-first** for interpretive changes. Mechanical/clerical
  metadata may self-apply in a later automation atom; in v1 everything is
  patch-first.

## Read surfaces

- **Health substrate:** `registries/research-line-scorecard.md`.
- **Registry state:** `registries/line-registry.md` (stage, relationships, why-state).
- **Artifacts:** the line's `models/`, `results/`, `tests/`, `claims/`.
- **Authority surfaces:** `CLAIM-LEDGER.md`, `ROADMAP.md`, `HYPOTHESES.md`,
  `../NORTH-STAR.md`.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — authority order
  (§11) and workflow-legitimacy rules.
- **Decision History:** `registries/decision-history.md` — active governance
  constraints and accepted prior decisions.
- **Workflow catalog / skeleton:** `README.md` and `WORKFLOW-SKELETON-PROPOSAL.md`
  — to validate route targets and avoid routing to workflows that do not exist.
- `../personas/EXPERT-PANEL.md` — distilled panel input, only via a deep-panel
  trigger; not loaded by default.
- Govern Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- A **standing snapshot** (audit artifact) to `logs/` — non-canonical.
- A **patch proposal** for interpretive registry fields — patch-first, applied by
  an authority/accept step, not by line-review.
- **Lifecycle candidates** → `lifecycle-review`.
- **Governance signals** → the docket (`govern/docket-triage`, later).

**Patch targets.** A patch proposal may target stale or inconsistent *source-state*
fields — registry metadata, evidence pointers, relationship fields, or
health-substrate entries that appear mis-scored. The **standing snapshot itself is
never patched back into canonical state**; it is retained as a log artifact only.
Any patch that would change lifecycle state, portfolio structure, accepted
decisions, or schema is **routed to the owning workflow**, not proposed by Line
Review.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): recurring line-review heuristics, known false-positive
  flags, prior mis-scoring patterns.
- Writes (learning-return, after acceptance): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** research-line-scorecard (substrate), line-registry (state).
- **Writes:** a standing snapshot (audit artifact, `logs/`); proposes patches —
  does not directly write canonical fields in v1.

## Procedure (runnable scope: one research line)

1. **Hygiene check (deterministic precondition).** Verify the line's registry
   entry is well-formed: required fields present, artifact links resolve,
   relationships point at existing lines. **If hygiene fails, emit a hygiene
   report + clerical patch and STOP — do not run scored review** (short-circuit).
2. **Load and understand the line** (the expensive step): registry entry,
   artifacts, relationships, health substrate, authority-surface status.
3. **Compute standing.** Score all **seven** standing dimensions freshly from the
   substrate, each `0–3` with `rationale`, `evidence_or_basis`, `confidence`,
   `flags`. No weighted aggregate, no single number, no cross-line ranking.
4. **Emit.** A standing snapshot (audit artifact), a patch proposal for any
   interpretive changes, lifecycle candidates (→ `lifecycle-review`), and
   governance signals (→ docket). End with the verdict block.

## Standing scorecard (v1 rubric)

Seven dimensions, each `0–3` with mandatory `rationale`, `evidence_or_basis`,
`confidence`, `flags`:

- North Star Alignment
- Line Clarity
- Evidence Posture
- Conceptual Stability
- Dependency Clarity
- Boundary Health
- Routing Readiness

Scale anchors: **0** absent / blocked · **1** weak · **2** adequate · **3** strong.
Not in v1: weighted aggregates, decimals, a single "viability" number, automatic
lifecycle transitions, or cross-line rankings.

Per-dimension shape:

```yaml
dimension: North Star Alignment
score: 0-3
rationale: <why this score>
evidence_or_basis: <substrate fields / artifacts / authority surface cited>
confidence: low | med | high
flags: [stale | weak-evidence | overlap | mis-scored | blocker | needs-persona-review | lifecycle-candidate]
```

## Escalation triggers

Route OUT (never act unilaterally): lifecycle-candidate flag → `lifecycle-review`;
portfolio implication → `portfolio-review`; decision-history-worthy outcome → a
later decision/governance review; unresolved governance blocker → docket;
`needs-persona-review` → a `deep-panel-review` job; registry/authority conflict →
log as `confusion_or_conflict` and defer to the authority surface (operating model
§11).

## Governance docket item shape

Lifecycle candidates and governance issues stay distinct. Governance issues land
as docket items (routed to `govern/docket-triage`) with this minimal shape:

```yaml
governance_docket_item:
  issue:
  affected_line:
  signal_type:
  authority_surfaces_involved:
  why_line_review_cannot_resolve:
  recommended_owner_workflow:
  evidence_or_basis:
```

This gives schema-inadequacy, registry/authority conflict, undefined-workflow, and
decision-worthy-pattern signals a clear place to land.

## Failure modes

- **Running scored review on a hygiene-failed line.** Guard: hygiene short-circuit
  (Procedure step 1).
- **Treating the standing snapshot as canonical.** Guard: snapshots are audit
  artifacts only; standing is recomputed each run.
- **False precision:** 0–3 read as a viability verdict. Guard: legibility signal,
  not validation.
- **Manufactured convergence:** full-panel agreement read as independent support
  though all personas share one model. Guard: panel is distilled input (and only
  on trigger), never an aggregated vote.
- **Authority creep:** a patch that effectively decides a lifecycle/portfolio move.
  Guard: standing-only; patch-first; those belong to other workflows.

## Success criteria

A good run yields, for one line, a standing snapshot whose seven scores are each
defensible from cited substrate evidence, surfaces the governance issues a careful
human would (stale, mis-score, overlap, blocker), proposes a patch a reviewer can
accept or reject quickly, and routes every lifecycle/portfolio/docket signal to
the right destination — without changing any canonical state itself. Cheap test: a reviewer can tell, without rereading the whole line history, why each score was assigned, what evidence it rests on, what changed since the prior review, and which downstream workflow owns any unresolved issue.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

**Runnable atom (Phase 4): one research line → all seven standing dimensions →
one standing snapshot.** Do not split below the line level — loading and
understanding the line is the expensive part; once loaded, scoring all seven
dimensions is the right-sized task.

Likely atoms / separate workflows:
- `govern/line-hygiene-check` — deterministic precheck; one registry entry; emits
  a hygiene report + clerical patch; **short-circuits** scored review on failure.
- `govern/single-line-standing-review` — the runnable atom above.
- `govern/portfolio-review` — **separate workflow**: cross-line reconciliation.
- `govern/docket-triage` — **separate workflow**: governance docket / promotion
  triage.

Likely cadence differences:
- Often: single-line standing review (round-robin); hygiene on registry change.
- On events: deep-panel-review (only when `needs-persona-review` is flagged).
- Periodic / accumulated: portfolio-review and docket-triage (separate workflows).

Likely context boundaries:
- The standing-review atom loads only that line's entry, artifacts, relationships,
  substrate, and the govern Memory Pack load surface.
- The full 62-panel is NOT loaded unless a deep-panel-review is triggered.

Likely deterministic vs judgment split:
- Deterministic: hygiene / link checks, stale-by-date detection, dependency-target
  existence, the round-robin cursor.
- Judgment-based: the seven standing scores and rationales, lifecycle-candidate
  flagging.

Phase 4 coverage questions:
- Does every output have a downstream consumer? (snapshot → audit; patch → accept
  step; candidates → lifecycle-review; signals → docket.)
- Does every registry write have an owning task?
- Does every escalation signal have a destination?
- Does every scheduled task have a bounded object?
- Is anything reviewed twice by competing tasks? (line-review vs portfolio-review
  must not both reconcile cross-line.)
- Is any unit too large for one agent run?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions / reconciliation

1. **Resolved (Session 10).** Health substrate (`research-line-scorecard.md`) =
   input; standing snapshot (the 7 governance dims) = derived, non-canonical
   output. Two artifacts, distinct roles — not duplicates.
2. **Patch acceptance:** who applies interpretive patches (an authority/accept
   step? `lifecycle-review`?) — open.
3. **0–3 calibration anchors** need worked examples before the rubric is reliable
   across agents — open.
4. **Snapshot storage location** (`logs/runs/` vs a dedicated `logs/standing/`) —
   minor, open.
