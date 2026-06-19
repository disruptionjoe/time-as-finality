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
3. **Phase 3 — Workflow Design** *(next)*: design each workflow individually,
   collaboratively, one at a time.
4. **Phase 3.5 — Workflow Memory Layer**: reusable memory substrate (family-level
   Memory Packs) so workflows accumulate learning without re-reading raw history.
   Planned in `MEMORY-LAYER-PLAN.md`; built after Phase 3 stabilizes. **Automation
   must not begin until this layer is designed.**
5. **Phase 4 — Automation**: recurring triggers, cadence, scheduling, resource
   allocation — only after workflows and the memory layer are mature.

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
- [`PROJECT-LOG.md`](PROJECT-LOG.md) — this file.

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
