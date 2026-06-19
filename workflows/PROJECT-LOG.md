---
document_type: operational_log
primary_reader: mixed
read_pattern: newest_first
write_pattern: prepend
authority: historical_only
summarizable: true
---

# Project Log — Workflow-System Design Effort

This is the **canonical narrative memory** for the Time as Finality
workflow-system design effort. It exists so the project can be resumed after
context compaction or in a future session without reconstructing prior
reasoning.

**Rules for this log.** It is an **operational log** (see `DOCUMENT-CONTRACT.md`):
**prepend** new entries so the newest session is first; **never overwrite or
delete** previous entries. One entry per work session. Record: date, goals,
decisions made, rationale, open questions, deferred ideas, next recommended step.
*(Sessions 1–7 below are ordered newest-first as of the Session 7 reflow.)*

**Phase model (agreed 2026-06-19).**

1. **Phase 1 — Research Operating Model**: how the program thinks. *(done; living)*
2. **Phase 2 — Workflow Skeleton**: folder structure + registries; lightweight
   placeholders only. *(done)*
3. **Phase 3 — Workflow Design** *(complete — 18 workflows, lock-candidate)*:
   each workflow designed individually.
4. **Phase 3.5 — Workflow Memory Layer**: reusable memory substrate (family-level
   Memory Packs) so workflows accumulate learning without re-reading raw history.
   Planned in `MEMORY-LAYER-PLAN.md`. *(built — family packs under `context-packs/`)*
5. **Phase 4 — Automation**: recurring triggers, cadence, scheduling, resource
   allocation. *(designed — scaffold in `automation/`; triggers NOT armed)*

**Key artifacts.**

- [`RESEARCH-OPERATING-MODEL.md`](RESEARCH-OPERATING-MODEL.md) — Phase 1
  deliverable (renamed from `RESEARCH-POSTURE.md` in Session 2); §11 = authority
  order; §12 = document layout & contracts.
- [`WORKFLOW-SKELETON-PROPOSAL.md`](WORKFLOW-SKELETON-PROPOSAL.md) — Phase 2 plan.
- `README.md`, `registries/`, `exploit|explore|govern/`, `templates/`, `logs/` —
  Phase 2 skeleton.
- [`MEMORY-LAYER-PLAN.md`](MEMORY-LAYER-PLAN.md) — Phase 3.5 plan.
- [`DOCUMENT-CONTRACT.md`](DOCUMENT-CONTRACT.md) — document classes + front-matter schema.
- [`REPO-HYGIENE-REVIEW.md`](REPO-HYGIENE-REVIEW.md) — redundancy/conflict review.
- `../personas/EXPERT-PANEL.md` — canonical numbered personas (H1).
- [`registries/decision-history.md`](registries/decision-history.md) —
  constitutional decision record (DEC-NNN).
- [`registries/research-line-scorecard.md`](registries/research-line-scorecard.md)
  — per-line portfolio health signal.
- `context-packs/` — Phase 3.5 family Memory Packs (exploit/explore/govern).
- `automation/` — Phase 4 scaffold: COVERAGE-MATRIX, SCHEDULE-SPEC, TRIGGER-REGISTRY (NOT-ARMED).
- [`PROJECT-LOG.md`](PROJECT-LOG.md) — this file.

---

## Session 17 — 2026-06-19

**Goals**

- Same autonomous process for Phase 3.5 (build the memory layer) and Phase 4
  (design the automation scaffold) — up to but NOT including arming triggers.

**Decisions made**

- **DEC-023** — Phase 3.5 Workflow Memory Layer **built** (family packs under
  `context-packs/`).
- **DEC-024** — Phase 4 automation scaffold **designed**; triggers **NOT armed**.

**Built (2 area subagents + orchestrator critique)**

- `context-packs/`: `README.md` + `{exploit,explore,govern}/MEMORY.md` (five
  required pieces each) + `{...}/memory-log.md` (prepend-only, empty) — guidance
  only (authority rank 6), inert until used, summarized by `govern/research-memory`.
- `automation/`: `COVERAGE-MATRIX.md` (18 workflows, 65 task atoms),
  `SCHEDULE-SPEC.md`, `TRIGGER-REGISTRY.md` (65 triggers, all `NOT-ARMED` with
  arming prerequisites), `README.md` (hard rule: no live triggers this phase).

**Critique + verification (orchestrator fresh-eyes)**

- Five pieces present in each MEMORY.md; 18/18 workflows covered; ARMED triggers =
  0; no scheduler/cron calls; no truncation; no protected files modified.

**Status / not done by design**

- No live triggers armed (deferred, human-gated). No git commit (local left
  complete for the external commit agent).
- Arming prerequisites: Phase 3 workflows formally LOCKED; patch-acceptance owner
  decided; cadences/thresholds/budget caps set; memory layer validated.

**Next recommended step**

- Flip Phase 3 workflows to LOCKED (your call), resolve arming prerequisites, then
  arm triggers in a separate human-gated step.

---

## Session 16 — 2026-06-19

**Goals**

- Execute the autonomous Phase 3 completion run (DEC-019): design all remaining
  workflows, leave the local complete (no commit).

**Decisions made**

- **DEC-019** — autonomous run; supersedes DEC-016 for this run.
- **DEC-020** — line-registry two-axis schema applied (step 0).
- **DEC-021** — orchestrator-mediated critique (drafter != critic), per Joe's idea.
- **DEC-022** — `docket-triage` is an intake atom of `decision-review`, not a
  separate workflow (resolves the DEC-017 open item + lifecycle-review OQ#8).

**Built (16 workflow protocol docs, via 4 family subagents)**

- govern-core: `portfolio-review`, `decision-review`, `line-intake`.
- govern-support: `persona-governance`, `research-memory`, `information-portfolio`.
- explore: `line-discovery`, `line-incubation`, `foundation-ingestion`,
  `cross-disciplinary-synthesis`, `landscape-reassessment`, `persona-expansion`.
- exploit: `advance-primary`, `advance-secondary`, `challenge-primary`,
  `integrate-results`.
- Each: document-contract frontmatter, full exemplar section set, verdict block,
  Phase-4 decomposition notes, and a critique log under `workflows/critiques/`.

**Critique + consistency (orchestrator fresh-eyes pass)**

- Harmonized `docket-triage` across all families to `decision-review` (docket
  intake) per DEC-022. SendMessage (continue-same-subagent) was unavailable, so the
  orchestrator applied this cross-cutting fix directly.
- Routing closure verified: actual cross-workflow routes resolve; remaining
  "unresolved" tokens are Phase-4 decomposition-atom names (advisory, DEC-013) plus
  the intentionally-undefined `deep-panel-review`/`evidence-review` sinks.
- Updated `README.md` govern catalog with the new workflows.

**Status**

- All 16 are **v1.0 LOCK-CANDIDATE** — complete, consistent, ready — **held pending
  Joe's spot-review before formal lock** (the human lock gate). Can flip all to
  LOCKED in one operation on approval.
- Per-workflow docketed decisions (patch-acceptance owner, thresholds, etc.) are
  non-lock-gating policy items for `decision-review` later.

**Not committed**

- Local left complete for the external commit agent (Joe's choice). No git commit
  performed by this agent.

**Next recommended step**

- Joe spot-reviews; flip lock-candidates to LOCKED on approval; then Phase 3.5
  (memory layer) or Phase 4 (the per-workflow coverage matrix + automation).

---

## Session 15 — 2026-06-19

**Goals**

- Pass the focused critique on `govern/lifecycle-review` and lock it.

**Decisions made (DEC-018)**

- `govern/lifecycle-review` **LOCKED at v1.0** (accepted form of v0.4).
- **Two-axis lifecycle model adopted program-wide:** `stage` (maturity) +
  `status` (attention/disposition); `archived` is a status, `integrated` the
  terminal stage. hold/revive/retire → status; promote/demote/integrate → stage;
  split/merge → portfolio-review; promote & integrate high-scrutiny.

**Follow-up created (not yet done)**

- **`line-registry.md` schema update** to the two-axis model (add `status`; remove
  `archived` from the stage ladder; reclassify RL-006 as `status: archived`).
  Should land before `portfolio-review` relies on lifecycle posture. Likely a
  `decision-review`-class change to a canonical registry.

**Next recommended step**

- Implement the line-registry two-axis schema update (offered), then begin
  `govern/portfolio-review` per DEC-017. Under DEC-016, portfolio-review starts
  from Joe's chat-tested draft, which this agent then synthesizes.

---

## Session 14 — 2026-06-19

**Goals**

- Apply Joe's critique to `govern/lifecycle-review`: adopt the two-axis lifecycle
  ontology (final synthesis → v0.4 DRAFT).

**Built**

- Revised `govern/lifecycle-review.md` to v0.4 with a **two-axis model**:
  `stage` (maturity: seed…integrated) and `status` (attention/disposition:
  active | held | archived). `archived` removed from the stage ladder;
  `integrated` is the terminal mature stage.
- Candidate binding: hold/revive/retire act only on `status`; promote/demote/
  integrate act only on `stage`; split/merge are structural → `portfolio-review`.
- Added `integrate` to the canonical `candidate_type` list and the alias map;
  made it **high-scrutiny like promote** (promotion/integration safety rule).
- Rewrote retire language (status→archived, preservation/disposition not maturity),
  updated lifecycle-question examples to not mix axes, and replaced open-question 1
  with the two-axis schema-update recommendation.

**Notes**

- This is the DEC-016 final synthesis for this round, but per Joe's disposition it
  stays **v0.4 DRAFT** pending one focused critique (axis separation; archived not
  a stage; integrate added/guarded; retire/revive/hold = status only; promote/
  demote/integrate = stage only; split/merge structural → portfolio-review).
- The two-axis model is a recommended **line-registry schema change**, not yet
  accepted — likely a `decision-review` item; no DEC recorded until accepted.

**Next recommended step**

- Joe runs the focused critique pass; on pass, lock lifecycle-review and record the
  two-axis schema adoption as a decision; then proceed to `govern/portfolio-review`
  (DEC-017).

---

## Session 13 — 2026-06-19

**Goals**

- Perform the **initial synthesis** of `govern/lifecycle-review` (DEC-016 step 2)
  from Joe's chat-optimized v0.2 draft.

**Built**

- Wrote `workflows/govern/lifecycle-review.md` v0.3 INITIAL SYNTHESIS: integrated
  the v0.2 draft into repo conventions (document contract frontmatter, "research
  line" terminology, repo paths), preserving its spine — unified candidate
  vocabulary, conservative no-action default, dangling-route behavior, promotion
  safety, evidence-exit classes, merge/split → portfolio-review, patch-first.
- Added a **Lifecycle vocabulary binding** section binding candidate types to the
  registry ladder (`seed → … → integrated/archived`).

**Synthesis finding (gates lock)**

- The registry ladder is a *maturity* axis only; `hold` (and the active/held/
  archived *attention* axis) has no ladder home. Two options surfaced: (1) add a
  `status: active|held|archived` axis to the line registry separate from `stage`
  (recommended); (2) stay ladder-only and drop `hold`. Until decided, `hold`
  emits `signal_type: schema-inadequacy`.

**Notes**

- Per DEC-016, I did not draft first; this is the initial synthesis of Joe's
  chat-tested v0.2. Next is Joe's single critique, then my final synthesis + lock.
- Carried open item: reconcile `decision-review` vs `docket-triage` (DEC-017).

**Next recommended step**

- Joe gives one critique of the v0.3 initial synthesis (especially the lifecycle
  vocabulary decision); I then produce the final synthesis and lock.

---

## Session 12 — 2026-06-19

**Goals**

- Revise the Phase 3 design loop and confirm the govern workflow order.

**Decisions made**

- **DEC-016 — revised design loop (external-first).** Joe iterates a workflow with
  chat agents, then shares the chat-optimized version here; this agent does the
  **initial synthesis**, Joe critiques once, this agent does the **final
  synthesis** and locks. This agent no longer drafts first. Supersedes DEC-011.
- **DEC-017 — govern workflow order:** lifecycle-review → portfolio-review →
  decision-review → line-intake (design downstream consumers before upstream
  emitters strand their outputs).

**Notes**

- `govern/lifecycle-review` is next. Under DEC-016 I will **not** draft it; I wait
  for Joe's chat-optimized version, then perform the initial synthesis.
- When designing it, reconcile `decision-review` with the `docket-triage` signal
  sink referenced by line-review.

**Next recommended step**

- Joe shares the chat-optimized `lifecycle-review` → this agent performs the
  initial synthesis.

---

## Session 11 — 2026-06-19

**Goals**

- Apply the final critique to `govern/line-review` and lock it; set the next
  Phase-3 target.

**Decisions made (DEC-015 — line-review v1.2 LOCKED)**

- Applied the five light edits from the external-agent + final user critique:
  (1) frontmatter (`write_pattern: patch_proposal`, `authority:
  canonical_workflow`, `output_authority: noncanonical_audit_snapshot`,
  `unit_of_review: one_research_line`); (2) added authority read surfaces (ROM,
  Decision History, workflow catalog); (3) clarified patch targets (fix stale
  source-state; snapshot never written back to canonical; lifecycle/portfolio/
  decision/schema route to owning workflow); (4) added a governance-docket-item
  shape; (5) tightened success criteria toward auditability.
- The DEC-011 design loop for line-review is **complete**; workflow is LOCKED for
  the current operating model.

**Deferred (non-blocking)**

- 0–3 calibration examples; snapshot storage location; patch-acceptance owner;
  deep-panel-review as workflow vs Phase-4 atom; stale-by-date thresholds.

**Next recommended step**

- Design **`govern/lifecycle-review`** next (DEC-008 sequencing logic continues):
  it is the legitimate downstream consumer of line-review's lifecycle candidates.
  Run it through the same design loop (DEC-011).

---

## Session 10 — 2026-06-19

**Goals**

- Fold the Phase 3 end-note governing decisions into `govern/line-review` (v1.1).

**Decisions made (DEC-014)**

- Standing is a **derived, non-authoritative projection**, recomputed each run
  from the health substrate + registry state + artifacts + authority surfaces;
  **snapshots are audit artifacts, not canonical**.
- **Runnable atom = one line / seven dimensions / one snapshot** — do not split
  below the line level (loading the line is the expensive part).
- **Hygiene failures short-circuit** scored review.
- Mechanical metadata may self-apply later; **interpretive changes patch-first**.
- Out of scope for line-review: lifecycle actions (`lifecycle-review`), portfolio
  reconciliation (`govern/portfolio-review`, separate workflow), decision-history
  promotion (later decision review).
- **Resolved** the two-scorecard question: `research-line-scorecard` = health
  substrate (input); standing snapshot = derived output.

**Built**

- Rewrote `govern/line-review.md` to v1.1 with a Governing-decisions section,
  hygiene short-circuit in the procedure, standing-as-projection framing, and
  decomposition notes naming portfolio-review and docket-triage as separate
  workflows.
- Clarified `research-line-scorecard.md` as the health substrate line-review reads.

**Notes**

- Still design-loop **step 1** (my draft). The other agent's thinking + critique
  will be reconciled in synthesis (step 4); these are governing constraints to
  preserve through that synthesis.

**Next recommended step**

- Receive the external agent's line-review critique; synthesize the final v1.

---

## Session 9 — 2026-06-19

**Goals**

- Adopt the workflow-vs-task-vs-schedule decomposition guidance as the Phase 3/4
  standard and apply it.

**Decisions made**

- **DEC-013 — Workflow = protocol, Task = bounded execution unit, Schedule =
  when.** Phase 3 designs at protocol level and includes an advisory "Future
  automation decomposition notes" section naming likely seams; Phase 4 builds a
  coverage matrix (workflow -> task atoms -> cadence -> outputs -> consumers),
  splitting by cadence, context-shape, determinism, and audit boundary. A good
  task has one object, one job, one main output, one escalation path, and is
  idempotent/resumable. **Decomposition is not authority decomposition** — a task
  atom inherits its workflow's authority and may never exceed it.
- Added operating model **§13** capturing this principle.

**Built**

- Upgraded the workflow template (`templates/workflow-placeholder.template.md`) to
  the Phase-3 protocol standard: purpose, authority boundaries, read/write
  surfaces, memory interface, registry interactions, output shapes, escalation
  triggers, failure modes, success criteria, and the decomposition-notes section.
- Enriched `govern/line-review.md` to meet the standard: added Escalation
  triggers, Failure modes, Success criteria, and Future automation decomposition
  notes (example atoms: line-hygiene-check, single-line-standing-review,
  portfolio-review, docket-triage).

**Notes / open**

- `line-review` is still mid design-loop (step 1). These additions are advisory
  and will be reconciled in the synthesis step (step 4) alongside the other
  agent's critique — the decomposition notes deliberately surface the seams the
  other agent may also raise.
- Phase 4 deliverable to build later: the per-workflow coverage matrix (YAML)
  confirming each task atom is loadable, bounded, auditable, and stoppable.

**Next recommended step**

- Continue the `line-review` loop: receive the other agent's thinking + critique,
  then synthesize the final v1 (steps 2–4).

---

## Session 8 — 2026-06-19

**Goals**

- Begin Phase 3. Design the first workflow (`govern/line-review`, per DEC-008) and
  establish the Phase 3 collaborative design loop.

**Decisions made**

- **Phase 3 design loop (DEC-011).** Per workflow: (1) this agent drafts; (2) Joe
  shares with another agent; (3) Joe returns that agent's thinking + critique of
  this version; (4) this agent synthesizes a final version; (5) Joe gives one
  final critique. Recorded here throughout the phase.
- **`govern/line-review` v1 (DEC-012).** Standing-review only (no lifecycle
  moves); hybrid scoring; patch-first writes; per-line then portfolio granularity;
  full 62-panel as distilled input; light 0–3 rubric over 7 governance dimensions
  (North Star Alignment, Line Clarity, Evidence Posture, Conceptual Stability,
  Dependency Clarity, Boundary Health, Routing Readiness) with rationale /
  evidence / confidence / flags. No aggregates, decimals, auto-transitions, or
  cross-line rankings.

**Built**

- Drafted `workflows/govern/line-review.md` v1 — this is **step 1** of the design
  loop (my draft), now awaiting the external-agent thinking + critique.
- Memory Pack interface specified in the workflow (read load surface / write a
  learning-return entry) but v1 does not depend on it (Phase 3.5 not built).

**Open questions** (carried in the workflow)

- Two scorecards: reconcile the 7 standing dims vs the existing 9 research-health
  dims (proposal: standing = output; research-health = inputs).
- Full-panel cost vs false-convergence risk (subset after v1?).
- Who applies the proposed patch.
- 0–3 scale needs calibration examples.

**Next recommended step**

- Joe shares the `line-review` draft with another agent and returns its thinking +
  critique; this agent then synthesizes the final v1 (design-loop steps 2–4).

---

## Session 7 — 2026-06-19

**Goals**

- Apply Phase 3 architectural refinements before designing individual workflows,
  and capture the document-layout principle as a governance decision.

**Decisions made**

- **Panel Evolution.** Added a "Panel Evolution" section to
  `personas/EXPERT-PANEL.md`: the panel is an evolving research instrument; add
  experts when research reveals missing perspectives/blind spots; rarely remove —
  deprecate/merge/supersede while preserving historical numbering.
- **Research-line dependencies.** Added optional relationship fields
  (`depends_on`, `supports`, `competes_with`, `extends`, `imports`) to the line
  registry and line-card template — relationships between *lines*, not files — so
  governance can eventually reason over a research *graph*. Seeded relationships
  on RL-001…006 (e.g. RL-001 competes_with RL-002, depends_on RL-004).
- **Research-line scorecard.** Created `registries/research-line-scorecard.md`: a
  portfolio health signal (cross-cluster support, math/empirical readiness,
  novelty, information gain, dependency centrality, overclaim risk, trajectory,
  confidence trend). Deliberately not collapsed to one number; provisional
  snapshot pending the first `line-review`.
- **Generalization wording** sharpened to the Architecture-of-Legitimacy roadmap
  (decentralized legitimacy, Bitcoin-inspired incentives, contribution markets,
  adaptive governance, legitimate outputs without central executive authority).
- **DEC-010 — document layout guideline.** Optimize a document's layout for its
  dominant *read* pattern, not its write pattern. Three classes: Current State
  (edit in place), Historical Record (append chronologically), Operational Log
  (prepend newest-first). Added operating model §12; created
  `DOCUMENT-CONTRACT.md` (front-matter schema + vocabulary). Applied contracts to
  exemplars: this log (operational), decision-history (historical), line-registry
  and research-line-scorecard (registry/current-state).
- **Reflowed this project log to newest-first** to conform to its operational-log
  class (this session at top). Prior sessions reproduced verbatim in reverse
  order; no content removed.

**Rationale**

- These are refinements, not direction changes; doing them before Phase 3 keeps
  behavior design building on a stable substrate.
- The document contract teaches agents how to use a file rather than forcing
  inference — a stronger, more general solution than "prepend everything."

**Open questions** — unchanged: hygiene M-items (stale `persona-idea-sprint`
counts, governance/ vs govern/ naming, agent-skills as canonical implementations,
root-README discoverability); persona cluster coverage gap; incremental rollout
of Document Contracts to remaining files.

**Deferred ideas** — unchanged (workflow behavior, scoring implementation →
Phase 3; automation → Phase 4).

**Next recommended step**

- Begin **Phase 3** by designing `govern/line-review` (DEC-008).

---

## Session 6 — 2026-06-19

**Goals**

- Add a constitutional decision registry and record the generalization path as
  deferred intent — before Phase 3 behavior begins.

**Decisions made**

- Created `registries/decision-history.md` — a compact constitutional registry
  (distinct from this narrative log). Seeded DEC-001…DEC-009 covering: the
  four-posture → three-posture change (DEC-001 superseded by DEC-002), "research
  line" terminology (DEC-003), the phase model incl. Phase 3.5 (DEC-004),
  family-level Memory Packs first (DEC-005), canonical persona panel (DEC-006),
  line registry as portfolio layer (DEC-007), **first Phase 3 workflow =
  `govern/line-review`, not `exploit/advance-primary` (DEC-008)**, and
  generalization deferred (DEC-009).
- DEC-008 supersedes the earlier "line-review OR advance-primary" suggestion:
  governance integrity (honest line scoring/standing) precedes exploitation.

**Generalization path (deferred intent — recorded, not current scope)**

This architecture is being developed inside Time as Finality first.
Generalization is deferred until the workflow system proves it can help this repo
actually move, learn, govern itself, and produce useful outputs. (Full roadmap
sharpened in Session 7; canonical in DEC-009 and the operating model.)

**Next recommended step**

- Begin **Phase 3** by designing `govern/line-review` (DEC-008).

---

## Session 5 — 2026-06-19

**Goals**

- Resolve hygiene findings H1 and H2 (structural authority only, no workflow
  behavior). Incorporate the new Phase 3.5 Workflow Memory Layer into the plan.

**H1 — Persona canonicalization (done)**

- Created `personas/EXPERT-PANEL.md` as the **canonical** numbered persona source
  (1–62), including new personas 57–62 (Game-Mechanism Designer, MMO Network
  Architect, Distributed-Simulation Engineer, Virtual-Economy Designer,
  Interest-Management Specialist, Bandwidth-Bounded-World Architect).
- Repointed `agent-skills/.../scripts/build_panel_prompt.py` to read the canonical
  file; `EXPECTED_PERSONA_COUNT` 56 → 62. Verified the script emits all 62.
- Reduced the skill's `references/personas.md` to a **mirror pointer**; updated
  the panel `SKILL.md` to read the canonical file.
- `personas/INDEX.md` now notes EXPERT-PANEL.md as canonical for numbered
  personas; `workflows/registries/persona-clusters.md` references it.
- Net: one canonical source; the lens registry (INDEX) and the numbered panel are
  complementary, not competing.

**H2 — Line registry as portfolio layer (done)**

- Rewrote `registries/line-registry.md` so it groups research lines and links out
  to authoritative surfaces (`CLAIM-LEDGER.md`, `ROADMAP.md`, `HYPOTHESES.md`,
  `tests/`/`results/`/`open-problems/`) instead of re-recording status.
- Added an explicit "Status authority" disclaimer: on conflict the authoritative
  surface wins and the discrepancy is logged, never silently reconciled.
- Each line now records: stage, why-this-stage, artifacts, maps-to, next move.

**Phase 3.5 — Workflow Memory Layer (planned, not implemented)**

- Inserted Phase 3.5 into the phase model (above): family-level Memory Packs
  (exploit/explore/govern), each `MEMORY.md` + `memory-log.md`.
- Recorded the **authority order** as constitutional in
  `RESEARCH-OPERATING-MODEL.md` §11 (NORTH-STAR → operating model → workflow def →
  registry schemas → user decisions → Memory Pack → raw logs).
- Wrote `MEMORY-LAYER-PLAN.md`: purpose, position, family-only initial scope,
  intended folder structure, the five required pack pieces, reading-audience
  separation, the **promotion rule** for future workflow-specific packs,
  instance-family choice (Stage Context Pack keyed by family), and inheritance
  rules. Implementation deferred until Phase 3 designs stabilize.

**Rationale**

- H1/H2 remove the two drift risks before Phase 3 wires behavior to registries.
- Phase 3.5 ensures workflows enter automation already carrying durable,
  bounded learning — and that memory can never silently become authority.

**Open questions**

- From `REPO-HYGIENE-REVIEW.md`: M1 (stale `persona-idea-sprint` counts — now an
  8th lens family / 62 personas), M2 (governance/ vs govern/ naming), M3
  (agent-skills as canonical implementations), M4 (root README discoverability);
  L-items. None actioned yet.
- Persona cluster coverage gap (dynamics/biology/neuro/cognitive/ecology) still
  needs a governance decision.

**Next recommended step**

- Optionally action the quick M-items, then begin **Phase 3** with the first
  workflow design.

---

## Session 4 — 2026-06-19

**Goals**

- With the five gating questions answered, build the Phase 2 skeleton.

**Decisions made (all five open questions resolved by Joe)**

- Registries: **four separate files** (line registry, persona clusters,
  foundation queue, information portfolio).
- Line registry: **seeded** — RL-001 = the FinaliEvent → finite-descent →
  conflict-enriched-descent line as the first `primary-exploit` line; RL-002…006
  seeded as secondary/incubated/explored/archived to make the registry live.
- Persona lenses: **appended to `personas/INDEX.md`** as a new "Simulation / MMO /
  Game-Mechanism Lenses" family (canonical), not kept inside `workflows/`.
- Runner format: **markdown-prompt-only** for now.
- `RESEARCH-POSTURE.md` redirect stub: **kept** for now.

**Built**

- `workflows/` tree: `exploit/` (4), `explore/` (6), `govern/` (5) lightweight
  placeholders (five-section + Mode); `README.md`; `templates/` (5);
  `logs/{runs,synthesis,best-next-move}/` with `.gitkeep`.
- Four seeded registries under `registries/`.
- Appended the six new lenses to `personas/INDEX.md`.

**Findings surfaced during the build (feed the hygiene review)**

- **Two persona systems** exist: `personas/INDEX.md` (lenses) and
  `agent-skills/time-as-finality-persona-panel/references/personas.md` (56
  numbered personas). The new 6 lenses now exist as lenses, but numbered personas
  57–62 do not yet exist. Migration owned by `govern/persona-governance`.
- **Cluster coverage gap:** the seven clusters do not cover all 56 personas
  (dynamics/biology/neuro/cognitive/ecology, plus causal-inference and
  physics-informed-ML). Governance decision needed.
- A separate **redundancy/conflict review** was requested and written to
  `workflows/REPO-HYGIENE-REVIEW.md`.

**Open questions** — Phase-2 gating questions now resolved. Remaining: items in
`REPO-HYGIENE-REVIEW.md` (persona consolidation, stale sprint counts, status-
tracking overlap, governance-dir naming, root-README discoverability).

**Next recommended step**

- Review `REPO-HYGIENE-REVIEW.md` and decide which cleanups to action. Then begin
  **Phase 3** by designing the first workflow (recommend `govern/line-review` or
  `exploit/advance-primary`, since RL-001 is live).

---

## Session 3 — 2026-06-19

**Goals**

- Apply the final review additions before freezing Phase 1.

**Decisions made** (all in `RESEARCH-OPERATING-MODEL.md` unless noted)

- **Added Research Mode** as a subsection of §1: every workflow declares whether
  it runs in **Search Mode** (possibility generation, diversity, information
  gain) or **Evaluation Mode** (rigor, criticism, formalization, evidence
  quality), and must not switch silently. Rationale: keeps Explore from becoming
  timid and Exploit from becoming speculative. This was the one major idea from
  prior discussion that had gone missing.
- **Operationalized mode in the skeleton:** added a `**Mode:** search |
  evaluation | both` field to the Phase-2 workflow placeholder format.
- **Made allocation explicit as the research budget** in §2: compute, agent
  attention, automation cadence, human attention, and review effort. "Research
  budget" is now a recurring term.
- **Sharpened the governance framing** in §2: "Governance does not merely
  maintain the system; it continually improves the way the research program
  allocates attention and makes decisions."
- **Distinguished landscape reassessment from synthesis** (new subsection in §2):
  synthesis asks what patterns connect; landscape reassessment asks how the
  topology of the research landscape itself has changed. Named as one of the
  highest-value periodic moves and the main defense against optimizing inside a
  shifted landscape.
- **Added the program's objective sentence** to §1: the goal is not to find the
  correct theory as quickly as possible, but to maximize the probability that the
  program converges on the strongest available theory over time.
- **Deliberately did not** add heavier optimization terminology; kept the
  document readable as something a researcher would actually maintain.

**Rationale**

- These five additions close the gap between "good operating model" and the
  intended "constitution of a research program" without expanding scope into
  workflow behavior (still Phase 3).

**Open questions** — unchanged from Session 2 (posture-doc home; registries one
file vs four; seed line registry vs empty; persona additions location; runner
format; whether to delete the `RESEARCH-POSTURE.md` redirect stub).

**Deferred ideas** — unchanged (workflow behavior, scoring implementation →
Phase 3; automation cadence and research-budget *allocation mechanics* → Phase 4).

**Next recommended step**

- Treat Phase 1 as ready to freeze. On your word, answer the still-open skeleton
  questions and begin **Phase 2** (build the `workflows/` tree, placeholders, and
  registry schemas).

---

## Session 2 — 2026-06-19

**Goals**

- Apply conceptual revisions to the Phase 1 document from review feedback.
- Lock terminology before any agents, automation, or worktrees exist.

**Decisions made**

- **Collapsed the four-posture model to three: Exploit / Explore / Govern.**
  Foundation is no longer a top-level posture; it is an Explore workflow.
  Rationale: once expanded, "Foundation" became paper ingestion,
  cross-disciplinary synthesis, new personas, mathematical imports, new concepts,
  and landscape reassessment — all of which are fundamentally exploration
  (expanding the search space). This was originally an open question (skeleton
  proposal Q2); now resolved.
- **Renamed the Phase 1 document** `RESEARCH-POSTURE.md` →
  `RESEARCH-OPERATING-MODEL.md`. Rationale: it now defines governance, memory,
  lifecycle, voting, promotion, information gain, and workflow philosophy — an
  operating model, not merely a posture.
- **Added a foundational principle (§0): the research process is itself an object
  of optimization.** Improvements to how the program explores, evaluates,
  synthesizes, governs, and remembers are first-class research contributions,
  because they improve every future investigation. Recorded as one of the
  biggest ideas surfaced in this effort.
- **Rewrote §10** to the three-posture frame: Explore expands and searches the
  landscape; Exploit develops the strongest active research lines; Govern
  continuously improves the program's own quality, fairness, memory, and
  allocation.
- **Leaned into the general framing:** the document is now positioned as a
  largely domain-general operating model for an agentic research program, with
  TaF as its first subject rather than its only possible one.
- **Terminology change: "branch" → "research line"** everywhere (skeleton
  proposal Q5 resolved). Rationale: "branch" already means git branch/worktree,
  and this project will involve agents, automation, logs, and possibly real
  worktrees — remove the ambiguity now. Applied: research-line lifecycle, line
registry, primary/secondary research line, line discovery, line incubation,
line review. Glossary note added to both Phase 1 documents.

**Rationale**

- Three postures are cleaner and map exactly to the activity types: expand/search
  vs develop vs improve-the-machine. Foundation-as-budget was an artifact of
  thinking narrowly about "reading papers."
- Locking the "research line" term before automation prevents a costly rename
  once logs, registries, and worktrees exist.

**Open questions** (unchanged from Session 1 except where resolved)

- Resolved: Foundation placement (Explore workflow); terminology (research line).
- Still open: posture-doc home (standalone vs fold into `NORTH-STAR.md`);
  registries as four files vs one; seed the line registry from current repo state
  vs ship empty; persona additions in `personas/INDEX.md` vs `workflows/`; runner
  format (markdown-only vs `agent-skills/` wrappers).

**Deferred ideas**

- Unchanged: full workflow behavior, scorecard/aggregation implementation, and
  the verdict-block tooling -> Phase 3; automation cadence -> Phase 4.

**Next recommended step**

- Confirm `RESEARCH-OPERATING-MODEL.md` reads as the intended "constitution" of
  the program. If the old `RESEARCH-POSTURE.md` stub should be removed entirely
  (rather than left as a redirect), say so and I will request deletion. Then
  answer the still-open skeleton questions and proceed to Phase 2.

---

## Session 1 — 2026-06-19

**Goals**

- Establish the project's phase separation as durable record.
- Deliver Phase 1: update the research posture.
- Propose (not build) the workflow skeleton.
- Create this project log.
- Surface unresolved design questions.

**Decisions made**

- Adopted the four-phase model above; current work is strictly Phase 1 plus a
  Phase 2 *proposal*. No workflow behavior and no automation were created.
- Project home directory is `workflows/` (not the earlier `operators/`).
- Wrote `RESEARCH-POSTURE.md` covering all eleven posture topics.
- Posture **extends** `NORTH-STAR.md` rather than replacing it.
- Workflow taxonomy fixed at three families — exploit / explore / govern — with
  the fifteen Phase-3 workflows mapped into them.
- Kept the term **"branch"** initially (later changed to "research line" in S2).
- The earlier `operators/SETUP-PLAN.md` is **superseded** but **not deleted**
  (deletion declined); retained as archived prior-art per "archive, never delete".

**Rationale**

- Phase separation prevents premature lock-in.
- A single durable log is the minimum viable long-term research memory.

**Open questions** (also tracked in the skeleton proposal)

1. Posture home: standalone under `workflows/` or fold into `NORTH-STAR.md`?
2. Registries: four files or one combined?
3. Foundation: feeder under `explore/` or its own family?
4. Seed line registry from current repo state, or ship empty?
5. Persona additions: append to `personas/INDEX.md` or keep inside `workflows/`?
6. Term: keep "branch" or alias?
7. Runner: markdown-only or `agent-skills/` wrappers?

**Deferred ideas**

- Full operator behavior, run/scorecard mechanics, verdict-block tooling -> Phase 3.
- Condorcet / quadratic / cross-cluster aggregation implementation -> Phase 3.
- Automation cadence and scheduling -> Phase 4.

**Next recommended step**

- Review and stabilize the Phase 1 document, answer the open questions
  (especially 2-5), then proceed to **Phase 2**.
