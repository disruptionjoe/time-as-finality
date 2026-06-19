# Workflow Skeleton — Proposal (Phase 2 plan)

**Phase:** transitional (proposed in Phase 1; to be built in Phase 2).
**Status:** PROPOSAL. No workflow files are created yet. Per the phase
separation, the skeleton is only built once the operating model in
[`RESEARCH-OPERATING-MODEL.md`](RESEARCH-OPERATING-MODEL.md) is stable.

This document proposes (a) the folder structure, (b) the supporting registries,
and (c) the set of workflows to scaffold — as **lightweight placeholders only**.
Phase 2 establishes structure; behavior is designed later, one workflow at a
time, in Phase 3.

**Terminology.** "Research line" means a distinct line of inquiry in the TaF
research program. It is unrelated to git branches or worktrees.

---

## 1. Proposed folder structure

```text
workflows/
  RESEARCH-OPERATING-MODEL.md     How the program thinks (Phase 1). Done.
  WORKFLOW-SKELETON-PROPOSAL.md   This file.
  PROJECT-LOG.md                  Canonical, append-only project memory. Done.
  README.md                       (Phase 2) index: families, registries, how to run.

  exploit/                        (Phase 2 placeholders)
    advance-primary.md
    advance-secondary.md
    challenge-primary.md
    integrate-results.md

  explore/                        (Phase 2 placeholders)
    line-discovery.md
    line-incubation.md
    foundation-ingestion.md
    cross-disciplinary-synthesis.md
    landscape-reassessment.md
    persona-expansion.md

  govern/                         (Phase 2 placeholders)
    line-review.md
    persona-governance.md
    research-memory.md
    lifecycle-review.md
    information-portfolio.md

  registries/                     (Phase 2: schema + seed only)
    line-registry.md
    persona-clusters.md
    foundation-queue.md
    information-portfolio.md

  logs/                           (Phase 2: empty + .gitkeep)
    runs/
    synthesis/
    best-next-move/

  templates/                      (Phase 2)
    workflow-placeholder.template.md
    run-log.template.md
    line-card.template.md
    scorecard.template.md
    best-next-move.template.md
```

Three workflow families — **exploit / explore / govern** — match the operating
model. Foundation work sits inside `explore/`, because all of it (paper
ingestion, cross-disciplinary synthesis, persona expansion, landscape
reassessment) expands the search space.

## 2. Proposed workflows (placeholders only)

Fifteen workflows. In Phase 2 each is a thin placeholder; in Phase 3 each is
designed individually. The one-line purposes below are orientation, **not**
specifications.

**Exploit** — develop the strongest active research lines.

- `advance-primary` — take the next bounded move on the primary research line.
- `advance-secondary` — make progress on a secondary research line.
- `challenge-primary` — adversarially attack the primary line to test its standing.
- `integrate-results` — fold a matured line's results into the durable repo (claims/tests/ledger).

**Explore** — expand and search the idea landscape.

- `line-discovery` — generate and seed candidate research lines.
- `line-incubation` — move seeded/explored lines toward validated.
- `foundation-ingestion` — ingest outside papers/math/concepts to raise reasoning quality.
- `cross-disciplinary-synthesis` — find independent cross-cluster convergences.
- `landscape-reassessment` — step back and re-survey the whole landscape for blind spots / local-optimum risk.
- `persona-expansion` — add/refine persona lenses and coverage.

**Govern** — improve the quality, fairness, memory, and allocation of the program.

- `line-review` — re-score research lines; reconcile registry standing.
- `persona-governance` — maintain clustering, weighting, and registry integrity.
- `research-memory` — log hygiene, synthesis notes, project-log upkeep.
- `lifecycle-review` — apply promotion/demotion/archival rules and survival arguments.
- `information-portfolio` — maintain the information-gain ledger across explore/exploit.

## 3. Lightweight placeholder format

Every Phase-2 workflow file uses the same five-section placeholder (no behavior):

```markdown
# <Workflow Name>

**Family:** exploit | explore | govern
**Mode:** search | evaluation | both
**Status:** placeholder (Phase 2). Behavior designed in Phase 3.

## Purpose
One paragraph: what this workflow is for.

## Expected inputs
What it reads first (registries, logs, repo artifacts).

## Expected outputs
What durable artifacts it appends/updates, ending with the verdict block.

## Related registries
Which registries it reads and/or writes.

## Open questions
Design questions to resolve when this workflow is taken up in Phase 3.
```

The **Mode** field records whether the workflow runs in Search or Evaluation mode
(see `RESEARCH-OPERATING-MODEL.md`, §1 Research mode). A few workflows legitimately
do both and must say so rather than switch silently.

## 4. Supporting registries (purpose only; schema in Phase 2)

- **`line-registry.md`** — the research lines and their lifecycle states; the
  source of truth for primary/secondary standing.
- **`persona-clusters.md`** — the seven clusters mapping the existing
  `personas/INDEX.md` lenses plus the six new coverage areas; the scoring-time
  view of personas.
- **`foundation-queue.md`** — inbound reading/concept queue: proposed → ingested
  → noted, linked to `literature/` and `papers/`.
- **`information-portfolio.md`** — the information-gain ledger: what each research
  line (including archived/failed ones) taught the program. Operationalizes the
  information-gain philosophy.

Logs (`runs/`, `synthesis/`, `best-next-move/`) and `PROJECT-LOG.md` together
form long-term research memory: registries hold current state, logs hold history.

## 5. What Phase 2 will create

On approval: the folder tree in §1, fifteen five-section placeholders, four
registries (schema + a seed row each), the log directories (empty), and the
templates. No workflow behavior, no automation. Phase 2 is purely structural.

## 6. Open questions for the skeleton (carried to PROJECT-LOG)

1. Should the four registries be separate files (proposed) or sections of one
   `registries/REGISTRY.md`?
2. **Resolved (Session 2):** Foundation is an Explore workflow, not its own
   family — `foundation-ingestion` lives under `explore/`.
3. Should `line-registry` be seeded in Phase 2 from current repo state (the
   FinaliEvent → finite-descent → conflict-enriched-descent line as primary), or
   ship empty with only a schema and example row?
4. Should each workflow also get an optional `agent-skills/`-style runner later,
   or stay markdown-prompt-only?
5. **Resolved (Session 2):** terminology is "research line," not "branch."
