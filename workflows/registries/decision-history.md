---
document_type: historical_record
primary_reader: mixed
read_pattern: chronological
write_pattern: append
authority: historical_only
summarizable: false
---

# Decision History

A compact **constitutional registry** of major architectural and governance
decisions. This is **not** a narrative log — for that, see `../PROJECT-LOG.md`.
Each entry is a durable, citable decision record. Newest decisions append at the
bottom; superseded decisions are kept (never deleted) and cross-linked.

Entry schema:

```markdown
## DEC-NNN — [Decision Title]
Date:
Status: active | superseded | deferred
Decision:
Reason:
Applies to:
Supersedes:
Superseded by:
Evidence / Source:
Notes:
```

---

## DEC-001 — Four-posture model (Explore / Exploit / Foundation / Govern)
Date: 2026-06-19
Status: superseded
Decision: Organize work into four top-level postures, with Foundation (paper/
concept ingestion) as its own posture.
Reason: Foundation initially felt like a separate budget ("reading papers").
Applies to: research operating model; workflow families.
Supersedes: —
Superseded by: DEC-002
Evidence / Source: PROJECT-LOG Session 1.
Notes: Retained only as history; do not use.

## DEC-002 — Three postures: Explore / Exploit / Govern
Date: 2026-06-19
Status: active
Decision: Collapse to three postures; Foundation becomes an Explore workflow.
Reason: Paper ingestion, cross-disciplinary synthesis, new personas, math
imports, and landscape reassessment are all exploration — they expand the search
space.
Applies to: `RESEARCH-OPERATING-MODEL.md` §2, §10; workflow families.
Supersedes: DEC-001
Superseded by: —
Evidence / Source: PROJECT-LOG Session 2.
Notes: —

## DEC-003 — Terminology: "research line", not "branch"
Date: 2026-06-19
Status: active
Decision: Call a distinct line of inquiry a "research line"; reserve "branch" for
git branches/worktrees.
Reason: This project will involve agents, automation, logs, and possibly real
worktrees; remove the ambiguity before it propagates.
Applies to: all workflow docs, registries, logs.
Supersedes: —
Superseded by: —
Evidence / Source: PROJECT-LOG Session 2.
Notes: Glossary note carried in the Phase 1 docs.

## DEC-004 — Phase model with Phase 3.5 memory layer
Date: 2026-06-19
Status: active
Decision: Phases are 1 Operating Model → 2 Skeleton → 3 Workflow Design →
3.5 Workflow Memory Layer → 4 Automation. Automation must not begin until the
memory layer is designed.
Reason: Workflows should enter automation already carrying durable, bounded
learning; designing behavior before posture invites lock-in.
Applies to: whole project plan.
Supersedes: — (extends the original four-phase model)
Superseded by: —
Evidence / Source: PROJECT-LOG Sessions 1 and 5; `MEMORY-LAYER-PLAN.md`.
Notes: —

## DEC-005 — Family-level Memory Packs first
Date: 2026-06-19
Status: active
Decision: Instantiate Memory Packs at the workflow-family level only
(exploit / explore / govern). A workflow earns its own pack only after repeated
runs show workflow-specific lessons not captured by the family pack.
Reason: Keep the system simple; let specialization emerge from evidence.
Applies to: `MEMORY-LAYER-PLAN.md`; Phase 3.5.
Supersedes: —
Superseded by: —
Evidence / Source: PROJECT-LOG Session 5.
Notes: Promotion rule documented in the plan.

## DEC-006 — Canonical numbered persona panel under `personas/EXPERT-PANEL.md`
Date: 2026-06-19
Status: active
Decision: The 62 numbered expert personas are canonical in
`personas/EXPERT-PANEL.md`; the panel skill's `references/personas.md` is a mirror;
`personas/INDEX.md` (lenses) and `persona-clusters.md` reference the canonical
file.
Reason: Remove the multi-source ambiguity flagged as hygiene H1.
Applies to: persona system; persona panel skill; scoring.
Supersedes: — (resolves prior fragmentation)
Superseded by: —
Evidence / Source: PROJECT-LOG Session 5; `REPO-HYGIENE-REVIEW.md` H1.
Notes: `build_panel_prompt.py` reads the canonical file (62 personas).

## DEC-007 — Line registry is a portfolio layer, not a status ledger
Date: 2026-06-19
Status: active
Decision: `line-registry.md` groups research lines and links out to authoritative
surfaces (`CLAIM-LEDGER.md`, `ROADMAP.md`, `HYPOTHESES.md`, tests/results/
open-problems); it never restates their status. On conflict the authoritative
surface wins and the discrepancy is logged.
Reason: Prevent status drift between the registry and the existing surfaces
(hygiene H2).
Applies to: `registries/line-registry.md`; govern workflows.
Supersedes: —
Superseded by: —
Evidence / Source: PROJECT-LOG Session 5; `REPO-HYGIENE-REVIEW.md` H2.
Notes: —

## DEC-008 — First Phase 3 workflow is `govern/line-review`
Date: 2026-06-19
Status: active
Decision: Begin Phase 3 by designing `govern/line-review`, not
`exploit/advance-primary`.
Reason: Establish honest scoring/standing of research lines before pouring effort
into advancing any single line; governance integrity precedes exploitation.
Applies to: Phase 3 sequencing.
Supersedes: — (refines the earlier "line-review OR advance-primary" suggestion)
Superseded by: —
Evidence / Source: Build Agent Note, 2026-06-19.
Notes: —

## DEC-009 — Generalization deferred (develop inside Time as Finality first)
Date: 2026-06-19
Status: deferred
Decision: Develop and prove the governance/workflow architecture inside Time as
Finality before extracting any reusable framework. Do not generalize prematurely.
Reason: The architecture must first show it helps this repo move, learn, govern
itself, and produce useful outputs.
Applies to: project scope; future repos.
Supersedes: —
Superseded by: —
Evidence / Source: Build Agent Note, 2026-06-19; `PROJECT-LOG.md` Session 6;
`RESEARCH-OPERATING-MODEL.md` (Generalization note).
Notes: Intended long-term roadmap — (1) develop and validate the research
operating model inside TaF; (2) demonstrate it meaningfully improves the quality,
governance, and long-term evolution of this program; (3) once proven, extract the
framework into the Architecture of Legitimacy project; (4) use it to research
decentralized legitimacy itself — Bitcoin-inspired incentive structures,
contribution markets, adaptive governance, and mechanisms for producing highly
legitimate outputs without centralized executive authority; (5) after that
matures, apply across additional research repositories. Deferred intent, not
current scope; immediate priority remains TaF's success.

## DEC-010 — Optimize document layout for dominant consumption pattern
Date: 2026-06-19
Status: active
Decision: Optimize each document's layout for its dominant *read* pattern, not its
write pattern (guideline, not rigid rule). Define three classes — Current State
(edit in place), Historical Record (append chronologically), Operational Log
(prepend newest-first). Significant files should eventually declare a machine-
readable Document Contract in front-matter.
Reason: "Prepend everything" is too blunt; different files have different access
patterns. Telling agents how to use a file beats forcing them to infer it, and
allows different structures where they make sense.
Applies to: all significant repo documents; `RESEARCH-OPERATING-MODEL.md` §12;
`DOCUMENT-CONTRACT.md`.
Supersedes: — (refines the earlier prepend-only memory-log guidance)
Superseded by: —
Evidence / Source: Build Agent Note, 2026-06-19; `DOCUMENT-CONTRACT.md`.
Notes: Rollout is incremental (a `govern/research-memory` task). The decision
history is itself a Historical Record (append); the project log and memory logs
are Operational Logs (prepend newest-first); registries are Current State (edit
in place).


## DEC-011 — Phase 3 collaborative design loop
Date: 2026-06-19
Status: superseded
Decision: Each Phase 3 workflow is designed via a fixed loop: (1) this agent
drafts the workflow; (2) Joe shares the draft with another agent; (3) Joe returns
that agent's thinking plus its critique of this model's version; (4) this agent
synthesizes all inputs into a final version; (5) Joe gives one final critique.
Repeat per workflow. The loop and each workflow's pass through it are recorded in
`PROJECT-LOG.md`.
Reason: cross-model critique reduces single-model blind spots (directly addresses
the persona-independence / monoculture risk) while keeping a human final gate.
Applies to: all Phase 3 workflow design.
Supersedes: —
Superseded by: DEC-016
Evidence / Source: user direction, Session 8.
Notes: This is a process decision for the whole phase, not a one-off.

## DEC-012 — govern/line-review v1 scope and authority
Date: 2026-06-19
Status: active
Decision: `line-review` is standing-review only — reconcile the standing
scorecard, detect issues, flag lifecycle candidates. It does NOT move lifecycle
states (that is `lifecycle-review`). Scoring authority is hybrid (deterministic
rubric where derivable; judgment only with rationale). Write authority is
patch-first in v1 (propose scorecard updates, not direct writes). Granularity is
both (per-line then portfolio reconciliation). v1 uses a light 0–3 ordinal rubric
over seven governance-legibility dimensions (North Star Alignment, Line Clarity,
Evidence Posture, Conceptual Stability, Dependency Clarity, Boundary Health,
Routing Readiness) with rationale, evidence_or_basis, confidence, flags — no
weighted aggregates, decimals, auto transitions, or cross-line rankings.
Reason: governance legibility, not scientific validation or lifecycle authority;
avoid false precision; keep authority boundaries clean.
Applies to: `workflows/govern/line-review.md`; `research-line-scorecard.md`.
Supersedes: —
Superseded by: —
Evidence / Source: Phase 3 design session (Session 8); user direction.
Notes: Memory Pack interface specified but v1 does not depend on it. Open
reconciliation: the 7 standing dims vs the existing 9 research-health dims.


## DEC-013 — Workflow vs task vs schedule (decomposition guidance)
Date: 2026-06-19
Status: active
Decision: Distinguish three layers. **Workflow = governance protocol** (Phase 3):
purpose, authority boundaries, read/write surfaces, memory interface, registry
interactions, outputs, escalation triggers, failure modes, success criteria, and
report/patch/docket shapes. **Task = bounded execution unit** an agent can load,
complete, audit, and rerun in one context window (Phase 4). **Schedule = when** a
task runs. Phase 3 designs at protocol level and includes an advisory "Future
automation decomposition notes" section naming likely Phase-4 seams; it does not
force a workflow into one run, nor pre-split into many tasks unless the boundary is
already obvious and architecture-relevant. Phase 4 builds a coverage matrix
mapping workflow -> task atoms -> cadence -> outputs -> downstream consumers,
splitting by cadence, context-shape, determinism, and audit boundary (not step
count). A good task has one object, one job, one main output, one escalation path,
and is idempotent/resumable.
Reason: keep workflows constitutionally clear while automation units stay small,
schedulable, auditable, and safe.
Applies to: all Phase 3 workflow files; `RESEARCH-OPERATING-MODEL.md` §13; the
Phase 4 coverage matrix.
Supersedes: — (generalizes the line-review job-split discussion)
Superseded by: —
Evidence / Source: user guidance, Session 9.
Notes: **Decomposition is not authority decomposition** — a task atom inherits its
workflow's authority and may never exceed it; smaller does not mean more powerful.
Only the correct authority surface (§11) accepts/canonizes changes. The
decomposition notes are advisory until Phase 4 formalizes them.


## DEC-014 — govern/line-review governing decisions (v1.1)
Date: 2026-06-19
Status: active
Decision: Standing is a **derived, non-authoritative projection** recomputed each
run from the health substrate (`research-line-scorecard.md`), registry state,
artifacts, and authority surfaces; standing snapshots are audit artifacts in
`logs/`, never canonical state. The runnable atom is **one research line -> all
seven standing dimensions -> one standing snapshot** (do not split below the line
level). **Hygiene failures short-circuit** scored review. Mechanical metadata may
self-apply later; **interpretive changes remain patch-first**. Outside
line-review's authority: lifecycle actions (-> `lifecycle-review`), portfolio
reconciliation (-> `govern/portfolio-review`, a separate workflow), and
decision-history promotion (-> a later decision/governance review).
Reason: keep standing legible but non-authoritative; keep the runnable atom
right-sized; keep authority boundaries clean across govern workflows.
Applies to: `workflows/govern/line-review.md`; `research-line-scorecard.md` (as
health substrate); future `govern/portfolio-review` and `govern/docket-triage`.
Supersedes: — (refines DEC-012)
Superseded by: —
Evidence / Source: user end-note, Session 10.
Notes: Resolves the two-scorecard open question — research-line-scorecard = health
substrate (input); standing snapshot = derived, non-canonical output.


## DEC-015 — govern/line-review v1.2 LOCKED
Date: 2026-06-19
Status: active
Decision: After the external-agent critique and the final user critique,
`govern/line-review` is **locked at v1.2** for the current operating model, with
five light edits applied: (1) frontmatter clarified — `write_pattern:
patch_proposal`, `authority: canonical_workflow`, `output_authority:
noncanonical_audit_snapshot`, `unit_of_review: one_research_line`; (2) added
authority read surfaces — Research Operating Model, Decision History, workflow
catalog/skeleton (to validate route targets); (3) clarified patch targets —
patches may fix stale source-state fields, the standing snapshot is never patched
back to canonical, and lifecycle/portfolio/decision/schema changes route to the
owning workflow; (4) added a governance-docket-item shape; (5) tightened success
criteria toward auditability. The DEC-011 design loop for line-review is complete.
Reason: structure was sound; edits were light; close the first Phase-3 workflow
cleanly.
Applies to: `workflows/govern/line-review.md`.
Supersedes: — (realizes DEC-012 and DEC-014 as the locked v1.2)
Superseded by: —
Evidence / Source: external-agent critique + user final critique, Session 11.
Notes: Non-blocking deferred items (not required for lock): 0–3 calibration
examples; snapshot storage location (`logs/runs/` vs `logs/standing/`);
patch-acceptance owner; whether `deep-panel-review` becomes a workflow or a
Phase-4 atom; stale-by-date thresholds. Next Phase-3 workflow:
`govern/lifecycle-review` (the downstream consumer of line-review's lifecycle
candidates).


## DEC-016 — Revised Phase 3 design loop (external-first)
Date: 2026-06-19
Status: active
Decision: Replace the DEC-011 loop. New per-workflow loop: (1) Joe iterates the
workflow with chat agents ("test, test, test") to produce a chat-optimized
version; (2) Joe shares that version here and this agent performs an **initial
synthesis**; (3) Joe gives one critique; (4) this agent performs the **final
synthesis** (and locks when accepted). This agent no longer produces the first
draft.
Reason: front-load cross-model testing where it is cheapest (chat), and reserve
this agent for synthesis and repo integration rather than first-draft generation.
Applies to: all remaining Phase 3 workflows (from `govern/lifecycle-review` on).
Supersedes: DEC-011.
Superseded by: —
Evidence / Source: user direction, Session 12.
Notes: `line-review` (DEC-015) was completed under the prior DEC-011 loop; the new
loop applies from lifecycle-review onward.

## DEC-017 — Phase 3 govern workflow sequence
Date: 2026-06-19
Status: active
Decision: Design the govern workflows in this order: (1) **lifecycle-review** —
line-review already routes lifecycle candidates to it; (2) **portfolio-review** —
split / merge / overlap cases need a whole-registry view; (3) **decision-review**
— repeated governance signals need a canonization pathway to decision-history;
(4) **line-intake** — creation/bootstrapping of new lines, less urgent than
lifecycle handling.
Reason: design downstream consumers before upstream emitters accumulate unrouted
outputs. Lifecycle-review gives line-review a safe destination for consequential
recommendations without making line-review powerful.
Applies to: Phase 3 sequencing (govern family).
Supersedes: —
Superseded by: —
Evidence / Source: user direction, Session 12.
Notes: `decision-review` and `line-intake` are new govern workflows beyond the
original skeleton; reconcile `decision-review` with the `docket-triage` signal
sink referenced in line-review when it is designed. The govern family is expected
to evolve (operating model §0).


## DEC-018 — Two-axis lifecycle model adopted; lifecycle-review LOCKED (v1.0)
Date: 2026-06-19
Status: active
Decision: Adopt the **two-axis lifecycle model** program-wide — `stage` (maturity:
seed, explored, validated, incubated, secondary-exploit, primary-exploit,
integrated) and `status` (attention/disposition: active, held, archived).
`archived` is a **status**, not a stage; `integrated` is the **terminal mature
stage**. `govern/lifecycle-review` is **locked at v1.0** (the accepted form of
v0.4): hold/revive/retire act only on `status`; promote/demote/integrate only on
`stage`; split/merge are structural and route to `portfolio-review`; promote and
integrate are high-scrutiny.
Reason: the single ladder conflated maturity with attention, leaving `hold` with
no home; two axes resolve it cleanly.
Applies to: `workflows/govern/lifecycle-review.md` (locked); `line-registry.md`
schema (requires update); future govern workflows that read lifecycle posture.
Supersedes: refines the lifecycle vocabulary used by DEC-007 (the line registry
stays a portfolio layer; its single lifecycle ladder becomes two axes).
Superseded by: —
Evidence / Source: lifecycle-review design loop (Sessions 13–15); user approval.
Notes: **Implementation follow-up** — `registries/line-registry.md` must be updated
to the two-axis schema (add a `status` field; remove `archived` from the stage
ladder; reclassify RL-006 as `status: archived`). Until then, lifecycle-review
patches would propose a `status` field the registry does not yet carry.
`decision-review` vs `docket-triage` reconciliation still open (DEC-017).


## DEC-019 — Autonomous Phase 3 completion run (supersedes DEC-016 for this run)
Date: 2026-06-19
Status: active
Decision: Complete the remaining Phase 3 workflow designs in a single autonomous
run. Scope: all remaining Phase 3 workflows — govern (portfolio-review,
decision-review, line-intake, persona-governance, research-memory,
information-portfolio), explore (line-discovery, line-incubation,
foundation-ingestion, cross-disciplinary-synthesis, landscape-reassessment,
persona-expansion), exploit (advance-primary, advance-secondary, challenge-primary,
integrate-results). For this run only, the DEC-016 human/chat loop is replaced by
an autonomous subagent loop: family-level drafting subagents that each perform an
internal adversarial double-critique, followed by a cross-cutting fresh-eyes
reviewer and an orchestrator system-consistency pass. Lock criteria unchanged (no
unresolved lock-gating blocker). Commit is deferred to an external agent; this run
leaves the local working tree complete and in-scope-only.
Reason: user chose full autonomous completion over the slower human loop.
Applies to: all remaining Phase 3 workflow files.
Supersedes: DEC-016 (for this run only; DEC-016 remains the default loop after).
Superseded by: —
Evidence / Source: user direction, Session 16.
Notes: Trade-off acknowledged — the autonomous loop is lower-fidelity than the
chat+human loop that produced the two-axis insight; quality risk mitigated by
double self-critique + a fresh-eyes pass + the system-consistency pass, and by
leaving everything resumable via logs.

## DEC-020 — line-registry two-axis schema applied
Date: 2026-06-19
Status: active
Decision: `registries/line-registry.md` updated to the two-axis model (DEC-018):
`stage` (maturity ladder, `archived` removed) plus `status` (active | held |
archived). RL-001…005 set `status: active`; RL-006 set `stage: validated,
status: archived`.
Reason: implement DEC-018 so lifecycle-review and portfolio-review bind to a
registry that carries both axes.
Applies to: `registries/line-registry.md`.
Supersedes: — (implements DEC-018; refines the registry shape under DEC-007)
Superseded by: —
Evidence / Source: Session 16 (autonomous run, step 0).
Notes: —

## DEC-021 — Orchestrator-mediated critique in the autonomous run
Date: 2026-06-19
Status: active
Decision: Within the DEC-019 autonomous run, critique is **orchestrator-mediated**
rather than subagent self-critique: drafting subagents hand back to the
orchestrator; the orchestrator (a different agent — genuine fresh eyes) critiques;
revisions are then applied with the drafting context preserved. Drafter and critic
are separated.
Reason: a subagent critiquing its own draft is not independent; this restores
independence.
Applies to: the DEC-019 run and future autonomous workflow design.
Supersedes: refines DEC-019's internal-double-critique step.
Superseded by: —
Evidence / Source: user idea, Session 16.
Notes: SendMessage (continue-same-subagent) was unavailable in this environment, so
the orchestrator applied cross-cutting critique fixes directly; substantive future
revisions would spawn a revision subagent.

## DEC-022 — docket-triage is an intake atom of decision-review (not a workflow)
Date: 2026-06-19
Status: active
Decision: Governance signals route to `govern/decision-review`, whose intake
triages and clusters them; "docket-triage" names that bounded Phase-4 intake
EXECUTION ATOM of decision-review, not a separate workflow. Routes of the form
"-> govern/docket-triage" mean "-> govern/decision-review (docket intake)".
Reason: avoids workflow proliferation; resolves the DEC-017 open reconciliation and
lifecycle-review Open Question #8.
Applies to: all workflows that emit governance signals.
Supersedes: closes the decision-review-vs-docket-triage open item in DEC-017.
Superseded by: —
Evidence / Source: govern-core subagent design + orchestrator critique, Session 16.
Notes: Locked line-review/lifecycle-review say "docket-triage, later" —
forward-compatible; left unedited (locked), behavior unchanged.

## DEC-023 — Phase 3.5 Workflow Memory Layer built
Date: 2026-06-19
Status: active
Decision: Built the family-level Memory Packs under `workflows/context-packs/`
(exploit, explore, govern), each a load-surface `MEMORY.md` (five required pieces)
plus a prepend-only `memory-log.md`, guidance-only (authority rank 6, §11), inert
until used, owned/summarized by `govern/research-memory`. Per MEMORY-LAYER-PLAN and
DEC-005 (family-level first; promotion rule for workflow-specific packs).
Reason: Phase 3 stabilized; the memory substrate must exist before automation
(DEC-004).
Applies to: `workflows/context-packs/*`.
Supersedes: implements MEMORY-LAYER-PLAN.
Superseded by: —
Evidence / Source: Session 17 autonomous run.
Notes: memory-log authority recorded as guidance_only; `last-summarized` marker
syntax to be standardized when the summarizer is built (Phase 4).

## DEC-024 — Phase 4 automation scaffold designed (triggers NOT armed)
Date: 2026-06-19
Status: active
Decision: Designed the Phase 4 automation scaffold under `workflows/automation/`:
`COVERAGE-MATRIX.md` (18 workflows, 65 task atoms), `SCHEDULE-SPEC.md`
(cadences/trigger-types/ordering/budget), and `TRIGGER-REGISTRY.md` (65 triggers,
ALL `status: NOT-ARMED`, each with arming prerequisites). **No live trigger or
scheduled task was created** — arming is a separate, later, human-gated step.
Reason: complete the design up to (not including) automation arming, per user
direction.
Applies to: `workflows/automation/*`; gates Phase 4 execution.
Supersedes: —
Superseded by: —
Evidence / Source: Session 17 autonomous run.
Notes: Arming prerequisites include workflows formally LOCKED, patch-acceptance
owner decided, cadences/thresholds/budget caps set, memory layer validated.
Authority does not decompose with size (DEC-013).

## DEC-025 - Five research-machine extension workflows added
Date: 2026-06-21
Status: active
Decision: Add five protocol-level extension workflows to the canonical workflow
catalog: `exploit/contradiction-hunter`,
`explore/motif-census-emergence-detector`,
`govern/theory-compression-engine`, `explore/cross-repo-bridge-builder`, and
`govern/theory-tournament`.
Reason: Joe selected these as the first high-value research-machine workflows
for improving falsification, motif discovery, theory compression, cross-repo
bridging, and interpretation competition. They strengthen the program's ability
to change what it is allowed to believe, not merely produce more artifacts.
Applies to: `workflows/README.md`; the five extension workflow files.
Supersedes: -
Superseded by: -
Evidence / Source: User request, 2026-06-21.
Notes: These workflows are inert protocol definitions. They were added after
the Phase 4 automation scaffold in DEC-024 and are not mapped in
`automation/COVERAGE-MATRIX.md`, `automation/SCHEDULE-SPEC.md`, or
`automation/TRIGGER-REGISTRY.md`.
