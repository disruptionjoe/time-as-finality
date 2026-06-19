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
