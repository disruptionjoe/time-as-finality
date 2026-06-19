# Operators Scaffold — Setup Plan (for review)

**Status:** PLAN ONLY. Nothing operational is created yet. This document
describes the files to be added under `operators/` so that an in-repo agent can
run four recurring research operators. Scheduled triggers are explicitly **out
of scope** — this scaffold is the substrate a trigger would invoke, not the
trigger.

**Review gate:** Once you approve (or edit) this plan, the build step creates the
file tree in [§4 File Manifest](#4-file-manifest). Until then, only this plan
exists.

---

## 0. One naming decision to confirm

The spec calls the lifecycle unit a "branch." In this repo "branch" already
means a git worktree (see `.claude/worktrees/`). To avoid collision this plan
uses **research line** (registry = **Line Registry**, unit ID = `RL-NNN`).
This matches the spec's own phrase "the strongest active *line of work*."

Clean alternatives if you prefer: **track** (`TR-NNN`) or **strand**
(`ST-NNN`). The build will do a single find-replace on whichever term you pick,
so this is cheap to change — but it is the one decision worth locking before
build, because the term appears in registry IDs, operator prompts, and logs.

Everywhere below, read "research line" as the spec's "branch."

---

## 1. Design principles

These govern every file in the scaffold.

1. **No external dependencies.** Nothing references Capacity OS or any general
   agent framework. An operator is a markdown prompt + repo conventions. Any
   agent that can read/write files in this repo can run it. The existing
   `agent-skills/` JS workflow pattern is reused only optionally (§6), never
   required.
2. **Cumulative research memory.** Every operator *reads prior logs before
   acting* and *appends durable output after acting*. Logs are append-only and
   dated; operators never overwrite history. This is the core of the "long-term
   rate of high-quality discovery" goal.
3. **Registries are the shared state.** The Line Registry, persona clusters,
   and paper queue are the small, human-readable source of truth that all four
   operators read and update. Logs are the audit trail; registries are the
   current state.
4. **Explore / Exploit / Foundation / Stewardship stay separated.** Each
   operator has a distinct job, distinct inputs, and distinct outputs, so a
   scheduled trigger can run any one independently.
5. **Reuse, don't fork, existing assets.** The persona registry stays at
   `personas/INDEX.md` (operators reference it; clustering is layered on top, not
   copied). The paper queue references `literature/` and `papers/`. Operator
   outputs route into the existing `tests/`, `open-problems/`, `claims/`,
   `ROADMAP.md`, `HYPOTHESES.md`, `CLAIM-LEDGER.md` — not into private silos.
6. **Every run ends with one standard verdict block** (§7), so outputs are
   comparable across operators and over time.

---

## 2. Proposed folder structure

```text
operators/
  README.md                       Index + how an agent runs an operator. Entry point.
  SETUP-PLAN.md                   This file (can be deleted after build).

  operators/
    01-current-best-path.md       EXPLOIT  — advance the strongest active line.
    02-branch-discovery.md        EXPLORE  — find/validate/incubate new lines.
    03-foundation-raising.md      FOUNDATION — ingest papers/math/personas/critiques.
    04-repo-stewardship.md        STEWARDSHIP — coherence, logs, registries, hygiene.

  registries/
    line-registry.md              All research lines + lifecycle state + scores. SOURCE OF TRUTH.
    persona-clusters.md           7 discipline clusters; new coverage areas; cross-cluster rules.
    paper-queue.md                Inbound reading queue: proposed → ingested → noted.

  protocols/
    scoring-protocol.md           Per-persona metrics, Condorcet, quadratic, cross-cluster norm.
    lifecycle-protocol.md         seed→…→integrated/archived; promotion, demotion, survival args.

  logs/
    runs/                         One dated file per operator run (append-only).
      .gitkeep
    synthesis/                    Cross-run synthesis notes (governance-layer aggregation).
      .gitkeep
    best-next-move/               The candidate verdict block from each run, dated.
      .gitkeep

  templates/
    run-log.template.md
    line-card.template.md
    scorecard.template.md
    paper-intake.template.md
    best-next-move.template.md
```

Rationale: a single self-contained top-level dir (your chosen layout) keeps the
orchestration legible and lets Stewardship police one tree. Persona additions
are the one exception — they edit `personas/INDEX.md` in place (§5) so the
existing 43-lens panel and `persona-idea-sprint` workflow keep working unchanged.

---

## 3. The four operators (behavioral spec)

Each operator file is a self-contained prompt with the same skeleton:
**Role → Read-first list → Procedure → Output routing → Verdict block.** Drafts
of the read/route contracts below; full prompt prose is written at build.

### 3.1 `01-current-best-path.md` — EXPLOIT (Current Best Path)

- **Goal:** advance the single strongest active line one concrete step.
- **Reads first:** `line-registry.md` (current primary-exploit line), the most
  recent `logs/runs/` and `logs/synthesis/` entries, plus that line's linked
  artifacts (`models/`, `results/`, `tests/`, relevant `claims/`).
- **Does:** picks the next bounded move on the primary line (new toy model,
  theorem check, counterexample search, claim tightening), executes or specifies
  it, and records what changed.
- **Appends/routes:** results into `results/` + `tests/`; status into
  `line-registry.md`; run record into `logs/runs/`; verdict into
  `logs/best-next-move/`. Updates `CLAIM-LEDGER.md`/`ROADMAP.md` if a claim moved.
- **Guard:** must take the *largest reversible ambitious swing* that stays
  testable, then narrow — not timid incrementalism.

### 3.2 `02-branch-discovery.md` — EXPLORE (Branch Discovery)

- **Goal:** discover/validate/incubate alternative lines so the repo avoids a
  local optimum. May spawn new `RL-NNN` entries at `seed`/`explored`.
- **Reads first:** `line-registry.md` (avoid duplicating active lines),
  `explorations/BACKLOG.md`, recent sprint outputs in `explorations/`, the prior
  Branch Discovery runs in `logs/runs/`.
- **Does:** generates candidate lines (can invoke the existing
  `agent-skills/persona-idea-sprint` for fan-out), runs a light validation pass,
  and decides seed vs discard. Scores candidates via `scoring-protocol.md`.
- **Appends/routes:** new lines into `line-registry.md`; sketches into
  `explorations/`; run record + scores into `logs/runs/`; verdict into
  `logs/best-next-move/`.
- **Success criterion (from spec):** counts as success if it raises information
  gain — a failed candidate that exposes a missing definition, a flaw in the
  primary line, or a better test is a *win* and is logged as such.

### 3.3 `03-foundation-raising.md` — FOUNDATION (Paper / concept ingestion)

- **Goal:** raise the quality of future reasoning by ingesting outside papers,
  math, personas, critiques, and cross-disciplinary concepts.
- **Reads first:** `paper-queue.md` (next `proposed` items), `literature/`
  known-neighbor notes, `personas/INDEX.md`, prior Foundation runs.
- **Does:** ingests the next queued item(s), writes a known-neighbor /
  literature note, and flags any concept that should become a new persona lens,
  a new test, or a challenge to an existing claim.
- **Appends/routes:** notes into `literature/` (or `papers/`); persona
  candidates into `persona-clusters.md` + proposed edits to `personas/INDEX.md`;
  queue status update in `paper-queue.md`; run record + verdict into `logs/`.

### 3.4 `04-repo-stewardship.md` — STEWARDSHIP (Governance / hygiene)

- **Goal:** keep the whole system legible and governable.
- **Reads first:** all registries, recent `logs/runs/`, and the durable indexes
  (`README.md`, `ROADMAP.md`, `CLAIM-LEDGER.md`, `GLOSSARY.md`,
  `MATHEMATICAL-INDEPENDENCE-AUDIT.md`).
- **Does:** reconciles registries against reality (orphaned lines, stale states,
  broken links), runs the governance-layer score aggregation (§6) to confirm
  primary/secondary exploit selection, updates persona clustering, checks
  terminology drift against `GLOSSARY.md`, and performs automation hygiene
  (log rotation, template conformance).
- **Appends/routes:** corrections into the registries; a cross-run synthesis
  note into `logs/synthesis/`; governance verdict into `logs/best-next-move/`.

---

## 4. File manifest

What the build step will create (≈18 files). Registries/templates ship with a
worked example row so the format is unambiguous; logs ship empty with `.gitkeep`.

| path | type | seeded content |
|---|---|---|
| `operators/README.md` | index | how to run each operator; map of the tree |
| `operators/operators/01-current-best-path.md` | prompt | full operator prompt |
| `operators/operators/02-branch-discovery.md` | prompt | full operator prompt |
| `operators/operators/03-foundation-raising.md` | prompt | full operator prompt |
| `operators/operators/04-repo-stewardship.md` | prompt | full operator prompt |
| `operators/registries/line-registry.md` | registry | schema + 1–2 example lines back-filled from current repo state (e.g. the FinaliEvent / descent line as primary) |
| `operators/registries/persona-clusters.md` | registry | 7 clusters + 6 new coverage areas (§5) |
| `operators/registries/paper-queue.md` | registry | schema + existing `literature/` notes listed as `ingested` |
| `operators/protocols/scoring-protocol.md` | protocol | metrics + aggregation (§6) |
| `operators/protocols/lifecycle-protocol.md` | protocol | lifecycle + promotion/demotion/survival (§7) |
| `operators/templates/*.template.md` | templates | 5 templates (§8) |
| `operators/logs/{runs,synthesis,best-next-move}/.gitkeep` | dirs | empty |

No edits to existing files at build **except** the persona additions in §5
(proposed as an append to `personas/INDEX.md`) and one new "Operators" link in
`README.md`'s repository map. Both are called out so you can veto them.

---

## 5. Persona governance additions

The spec says: keep the full existing persona list, do **not** replace it, but
add coverage and cluster the personas. Plan:

**(a) New coverage — appended to `personas/INDEX.md`** as a new family
"Simulation / MMO / Game-Mechanism Lenses," six lenses:

- game mechanism design,
- MMO networking architecture,
- distributed simulation,
- virtual economies,
- interest management,
- bandwidth-bounded simulated worlds.

Each gets the same `lens | definition | best use | misuse risk` row format as
the existing tables, framed for Time as Finality (e.g. *interest management* →
"observer access to records is bandwidth-bounded; finality is what survives the
relevance filter," misuse → "treating the universe as literally running a netcode
server").

**(b) Clustering — new file `operators/registries/persona-clusters.md`** maps
all personas (existing 43 + 6 new) into the seven clusters the spec names:

1. math / formalism
2. physics / decoherence
3. distributed systems / consensus
4. information / networking
5. sheaf / category / geometry
6. simulation / MMO / game-mechanism
7. philosophy / testability / skepticism

Clustering lives in the operators dir (not in `INDEX.md`) so scoring can evolve
without churning the canonical lens registry.

---

## 6. Scoring protocol (`protocols/scoring-protocol.md`)

Two layers, exactly as the spec asks.

**Per-persona report (not just a vote).** Each persona reporting on a line
returns a scorecard with: confidence, novelty, expected impact, reversibility,
mathematical readiness, empirical readiness, dependency score, overclaim risk.
(Template in §8.)

**Governance aggregation layer.** Combines scorecards into a ranking using:

- **Condorcet-style pairwise comparison** of lines (per cluster, then overall);
- **quadratic / intensity-weighted support** (reuse the existing persona-panel
  rule: 100 points per persona, cost = `intensity²`);
- **cross-cluster normalization** so one large homogeneous cluster cannot
  dominate by headcount;
- **specialist survival arguments** — a line kept alive by a single
  high-conviction cluster must carry an explicit survival argument (§7).

**Selection outputs:**

- **Primary exploit line** = broad legitimacy: wins pairwise across clusters,
  best current formalization path.
- **Secondary exploit line** = pluralistic interest: meaningful support across
  *distant* clusters, **or** unusually strong specialist support from one
  cluster that may see something others miss.

This aggregation is what the Stewardship operator runs to keep the registry's
`primary`/`secondary` tags honest.

---

## 7. Lifecycle protocol (`protocols/lifecycle-protocol.md`)

**States:**

```text
seed → explored → validated → incubated → secondary-exploit → primary-exploit → integrated / archived
```

No fixed cap on the number of lines; movement is governed by criteria, not
quotas.

**Promote** when a line shows one or more of: cross-cluster support, strong
pairwise performance, high expected impact, clear mathematical traction, useful
repo traction, specialist high-conviction argument, a concrete next test.

**Demote / archive** — never merely because a line "looks failed." Archive only
when it loses cross-cluster support **and** no specialist cluster offers a clear
high-conviction survival argument. A **survival argument** must state: (1) what
the specialist cluster sees, (2) why other clusters may be missing it, (3) the
concrete next test that would clarify it, (4) how many more runs / what evidence
is required before reconsidering demotion.

**Archival, never deletion.** An archived line keeps: why it mattered, what was
learned, why it stopped, what could revive it. (This mirrors the repo's existing
"preserve failures explicitly" principle in `NORTH-STAR.md`.)

**Exploration success criteria.** A line is scored on *information gain*, not
only survival. A failed line still succeeds if it reveals a missing definition,
exposes a flaw in the primary line, inspires a theorem, improves clustering,
produces a better test, or seeds a stronger candidate. These are logged as
explicit "information-gain" wins.

---

## 8. The standard verdict block + templates

Every operator run ends by writing this block to `logs/best-next-move/<date>-<operator>.md`:

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

Five templates ship so runs are uniform:

- `run-log.template.md` — date, operator, inputs read, actions, artifacts
  touched, verdict block.
- `line-card.template.md` — `RL-NNN`, title, lifecycle state, cluster support,
  linked artifacts, last-moved date, score summary.
- `scorecard.template.md` — the 8 per-persona metrics + cluster tag.
- `paper-intake.template.md` — source, claim relevance, known-neighbor mapping,
  spawned tests/personas, status.
- `best-next-move.template.md` — the verdict block above.

---

## 9. Open questions for your review

1. **Naming:** confirm "research line" vs "track" vs "strand" (§0).
2. **Persona edits to `personas/INDEX.md`:** OK to append the 6-lens family in
   place, or keep all new personas inside `operators/` and leave `INDEX.md`
   untouched?
3. **Back-fill the Line Registry now?** I can seed `RL-001…` from the current
   repo state (the FinaliEvent → finite descent → conflict-enriched descent work
   reads as the current primary line) so the scaffold is live on day one — or
   ship the registry empty with just the schema.
4. **Operator runner:** markdown-prompt-only (any agent reads the file and
   acts), or also generate an optional `agent-skills/`-style `.js`/`SKILL.md`
   wrapper per operator to match the existing `persona-idea-sprint` pattern?

On approval I'll build the tree in §4 and report a file-by-file diff.
