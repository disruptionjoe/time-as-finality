# Research Operating Model

**Phase:** 1 (foundational definition). **Status:** living document; expected to
evolve. **Scope:** how the research program *thinks and allocates effort* — its
governance, memory, research-line lifecycle, voting, promotion, information-gain
philosophy, and workflow philosophy. It defines the operating model, not the
behavior of individual workflows (deferred to Phases 2–4; see
`WORKFLOW-SKELETON-PROPOSAL.md` and `PROJECT-LOG.md`).

**What this document is.** Although it is instantiated by the Time as Finality
program, this operating model is largely **domain-general**: it describes how an
autonomous, agentic research program should think — how it allocates effort,
preserves minority views, avoids premature convergence, scores ideas, and
remembers. The governance and workflow design matter as much as the physics,
because they determine the quality of *every* future investigation. Read TaF
here as the first program this model governs, not as its only possible subject.

**Generalization (deferred).** This architecture is intentionally being developed
inside Time as Finality first; generalization is intentionally deferred. The
immediate priority is making the TaF research program successful — the broader
framework should emerge only after it has earned that generalization through
sustained use. Intended long-term roadmap: (1) develop and validate the research
operating model inside Time as Finality; (2) demonstrate that it meaningfully
improves the quality, governance, and long-term evolution of this research
program; (3) once proven, extract the framework into the Architecture of
Legitimacy project; (4) use that framework to research decentralized legitimacy
itself — Bitcoin-inspired incentive structures, contribution markets, adaptive
governance, and mechanisms for producing highly legitimate outputs without
centralized executive authority; (5) after that matures, apply the resulting
governance architecture to additional research repositories. Deferred intent, not
current scope (see `registries/decision-history.md` DEC-009).

**Relationship to existing docs.** This extends, and does not replace,
[`NORTH-STAR.md`](../NORTH-STAR.md). North Star states the motivating intuition
and the five-level research stack; this document states the *operating model* —
the decision rules. Where the two conflict, North Star's philosophy of "preserve
failures, promote only what the evidence earns" wins, and this document should be
corrected.

**Terminology.** "Research line" means a distinct line of inquiry in the TaF
research program. It is unrelated to git branches or worktrees.

---

## 0. Foundational principle — the process is itself an object of optimization

> This repository treats not only its scientific hypotheses but also its own
> research process as objects of continual refinement. Improvements to how the
> program explores, evaluates, synthesizes, governs, and remembers are
> considered **first-class research contributions**, because they improve every
> future investigation.

A better definition or a sharper test advances one question. A better way of
*choosing* which questions to pursue, of scoring evidence fairly, of preserving
a minority view, or of remembering what was learned, advances all of them. The
program therefore spends real effort on its own machinery and records those
improvements with the same seriousness as a theorem. The rest of this document
is the current state of that machinery.

## 1. Research philosophy

The program does not optimize for the single next best action. It optimizes for
the **long-term rate of high-quality discovery while minimizing lock-in to local
optima**. A move that advances today's best result but narrows future options
can be worse than a move that yields less now but keeps more of the landscape
reachable.

Stated as the program's objective: **the goal is not to find the correct theory
as quickly as possible, but to maximize the probability that the research program
converges on the strongest available theory over time.**

The operating stance for any new idea is to take the **largest reversible,
ambitious swing that makes the idea visible**, then **reduce scope
intelligently** until the surviving claim is testable, rigorous, and
repo-integrable. Visibility first, rigor second — but rigor always arrives
before promotion.

Two failure modes are rejected symmetrically:

- **Timid incrementalism** — only ever taking the safe next step, which reliably
  traps the program in a local optimum.
- **Reckless grand synthesis** — declaring a sweeping unification before any
  piece is testable, which produces unfalsifiable narrative instead of
  knowledge.

The discipline that keeps the program between these traps is the one already in
`NORTH-STAR.md`: start bold, build the smallest executable mathematics, search
aggressively for counterexamples, narrow to what survives, preserve the
failures, promote only what is earned.

### Research mode

Every workflow should be explicit about whether it is operating in:

- **Search Mode** — maximize possibility generation, diversity, and information
  gain.
- **Evaluation Mode** — maximize rigor, criticism, formalization, and evidence
  quality.

These are complementary modes, and a workflow should avoid silently switching
between them: the behaviors that produce novel ideas are often not the behaviors
that rigorously evaluate them. Naming the mode keeps Explore from becoming timid
and Exploit from becoming speculative.

## 2. Exploit / Explore / Govern

The program separates three kinds of work so that attention to one never
silently consumes the others. These are postures, not yet workflows.

- **Explore** expands and searches the idea landscape. It widens the reachable
  search space *and* moves candidate research lines up the early lifecycle.
  Everything that grows the space of considered ideas lives here: line
  discovery, line incubation, **foundation ingestion** (outside papers,
  mathematics, concepts), cross-disciplinary synthesis, landscape reassessment,
  and persona expansion.
- **Exploit** develops the strongest active research lines — deepening,
  challenging, and integrating the lines currently judged best.
- **Govern** continuously improves the *quality, fairness, memory, and
  allocation* of the research program itself: registries, logs, lifecycle
  states, persona clustering, scoring integrity, terminology, and balance across
  the three postures.

Foundation is **not** a separate posture. Reading papers, importing mathematics,
synthesizing across disciplines, adding personas, and reassessing the landscape
are all fundamentally *exploration* — they expand the search space — so they are
realized as Explore workflows. The earlier four-posture model (which treated
Foundation as its own budget) is superseded; see `PROJECT-LOG.md`, Session 2.

The point of the split is **allocation honesty**. A healthy program spends on all
three, and the thing it is spending is its **research budget**: compute, agent
attention, automation cadence, human attention, and review effort. Govern is what
makes that allocation visible and adjustable rather than accidental. Governance
does not merely maintain the system; it continually improves the way the research
program allocates attention and makes decisions — and, per §0, improving that
allocation is itself first-class work.

### Landscape reassessment vs synthesis

Two Explore activities are easy to conflate and must be kept distinct.
Cross-disciplinary **synthesis** asks: *what patterns connect what we already
have?* **Landscape reassessment** asks a larger question: *given everything we
now know, how has the topology of the research landscape itself changed?* — which
regions are now promoted, which have collapsed, which adjacencies opened, and
whether the current primary research line is still on the most promising ridge.
Reassessment is one of the program's highest-value periodic moves, because it is
the main defense against optimizing hard inside a landscape that has quietly
shifted.

## 3. Information-gain philosophy

Exploration is evaluated by **how much it changes understanding**, not only by
whether its hypothesis survives. Exploration succeeds if it raises information
gain *even when the explored idea is wrong*.

A failed research line can still be a success when it does any of the following:

- reveals a missing definition,
- exposes a flaw in a stronger line,
- inspires a new theorem,
- improves persona clustering,
- produces a better test,
- or seeds a stronger exploit candidate.

The consequence for governance is concrete: a research line archived as "wrong"
should still have its information gain recorded as a positive outcome. The unit
of value is the **change in the program's understanding**, tracked over time, not
the win/loss record of individual hypotheses. (Phase 3 proposes an *Information
Portfolio* to make this ledger explicit.)

## 4. Research-line lifecycle

Research lines move through a lifecycle rather than being capped by a fixed
number. There is no quota on lines; movement is governed by criteria.

```text
seed → explored → validated → incubated → secondary-exploit → primary-exploit → integrated / archived
```

Two exploit tiers are distinguished because they answer different questions:

- A **primary research line** (lifecycle stage `primary-exploit`) is selected for
  **broad legitimacy**: it wins pairwise comparisons across persona clusters and
  represents the current best formalization path.
- A **secondary research line** (lifecycle stage `secondary-exploit`) is selected
  for **pluralistic interest**: it receives meaningful support across *distant*
  persona clusters, **or** unusually strong specialist support from a cluster
  that may see something others miss.

A single homogeneous cluster must not dominate selection merely because it
contains many similar personas — see §7–§8.

## 5. Promotion and demotion rules

**Promotion.** Promote a research line when it shows one or more of:
cross-cluster support, strong pairwise performance, high expected impact, clear
mathematical traction, useful repo traction, a specialist high-conviction
argument, or a concrete next test.

**Demotion / archival.** Do **not** archive a research line merely because it
looks like it failed. Archive or demote only when it **loses cross-cluster
support and no specialist cluster provides a clear high-conviction survival
argument.**

A **survival argument** is the instrument that protects a minority-supported
research line from premature death. To keep a line alive against the majority, a
specialist cluster must state all four of:

1. what the specialist cluster sees,
2. why other clusters may be missing it,
3. what concrete next test would clarify the line,
4. how many more runs, or what evidence, should be required before reconsidering
   demotion.

**Archive, never delete.** Reasoning is never destroyed. An archived research
line records: why it mattered, what was learned, why it stopped, and what could
revive it. This is the line-level expression of the repo-wide rule that failures
are preserved as labeled negative results.

## 6. Persona governance

Personas are reusable review postures, not authorities and not evidence by
themselves (consistent with `personas/INDEX.md`). The governance rules:

- **Use the full existing persona list.** Do not invent a replacement list. The
  43-lens registry in `personas/INDEX.md` and the `persona-idea-sprint` /
  `time-as-finality-persona-panel` machinery remain canonical.
- **Add coverage** for under-represented disciplines: game-mechanism design, MMO
  networking architecture, distributed simulation, virtual economies, interest
  management, and bandwidth-bounded simulated worlds. Added as a new lens family,
  not as replacements. (Maintaining and expanding the persona set is itself an
  Explore workflow — Persona Expansion.)
- **Cluster personas by discipline** when scoring research lines, into seven
  clusters: math/formalism; physics/decoherence; distributed systems/consensus;
  information/networking; sheaf/category/geometry; simulation/MMO/game-mechanism;
  philosophy/testability/skepticism.

Clustering is a scoring-time concern, intended to evolve; it is layered on top of
`personas/INDEX.md` rather than baked into it.

## 7. Voting and scoring philosophy

Personas do not merely vote. Each persona reporting on a research line returns a
structured **scorecard** with eight signals: **confidence, novelty, expected
impact, reversibility, mathematical readiness, empirical readiness, dependency
score, and overclaim risk.** A governance layer then aggregates these into a
ranking; no single persona's vote is itself a decision.

Aggregation uses, where applicable:

- **Condorcet-style pairwise comparison** of research lines;
- **quadratic / intensity-weighted support** (reusing the panel convention:
  ~100 points per persona, vote cost = `intensity²`), so a persona must spend
  disproportionately to express extreme conviction;
- **cross-cluster normalization**, so support is weighed by *breadth across
  clusters*, not raw persona headcount;
- **specialist survival arguments** (§5) as a protected override path for
  high-conviction minorities.

The philosophy: voting expresses *intensity and direction*; the governance layer
converts that into *legitimacy*, deliberately resisting domination by the largest
or most internally-similar group.

## 8. Cross-cluster reasoning

The strongest positive signal in this program is **independent convergence across
distant clusters** — different disciplines, using different vocabulary and
formalisms, arriving at structurally the same claim without coordinating. (The
persona-idea-sprint already treats such convergence as its primary output signal;
this operating model elevates it to a governance principle.)

Two guardrails make cross-cluster reasoning trustworthy:

- **Normalize across clusters** so a populous cluster cannot manufacture
  consensus by headcount; breadth across *distant* clusters counts for more than
  depth within one.
- **Protect informed minorities** via survival arguments, so a single cluster
  that genuinely sees something is not outvoted into silence.

Same-vocabulary agreement is treated as possible coordination, not convergence;
genuine convergence shows up as the *same structure described in different
languages*.

## 9. Long-term research memory

The program is built to **accumulate** understanding across sessions, surviving
context compaction and personnel/agent changes.

- **Read before acting; append after acting.** Every workflow reads prior logs
  and registries before it does anything, and appends durable output when it
  finishes. No workflow starts from a blank slate.
- **Registries are current state; logs are history.** A small set of
  human-readable registries (the line registry, persona clusters, foundation
  queue, information portfolio) hold the present truth. Append-only, dated logs
  hold the audit trail. Logs are never overwritten.
- **The project log is the canonical narrative memory.**
  [`PROJECT-LOG.md`](PROJECT-LOG.md) records goals, decisions, rationale, open
  questions, deferred ideas, and next steps per session, so the effort can be
  resumed without reconstructing prior reasoning.

The test of this memory: a new agent, given only the registries and logs, should
be able to state the current primary and secondary research lines, why each is
there, and what the next move is — without re-deriving it.

## 10. The operating model in one frame

```text
Explore expands and searches the idea landscape.

Exploit develops the strongest active research lines.

Govern continuously improves the quality, fairness, memory, and allocation
of the research program itself.
```

Foundation work — paper ingestion, cross-disciplinary synthesis, mathematical
imports, persona expansion, landscape reassessment — lives inside Explore,
because all of it expands the search space.

Every workflow run, regardless of posture, ends with one shared **verdict
block**, so outputs are comparable across postures and over time:

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

This block is the common currency of the operating model: it forces every run to
end with a falsifiable recommendation and an explicit statement of what would
overturn it. And, per §0, the model itself is on the table — when a better way to
explore, score, govern, or remember is found, it is adopted and logged as a
first-class contribution.

## 11. Authority order

When two surfaces appear to conflict, authority flows **downward** through this
fixed order. A lower surface never overrides a higher one. Conflicts are
**logged, never silently resolved**.

1. `NORTH-STAR.md`
2. `RESEARCH-OPERATING-MODEL.md` (this document)
3. Workflow definition (the workflow being run)
4. Registry schemas
5. Explicit user decisions
6. Memory Pack (the workflow memory layer — guidance/memory only)
7. Raw logs

This order is constitutional. It governs the Phase 3.5 workflow memory layer and
any future automation: a Memory Pack is guidance only, sits near the bottom, and
may never act as an authority, a queue, or a source of truth. If a memory-derived
lesson implies a change to a higher surface, it is routed out as a proposal — it
must not become policy by living in the pack. See `MEMORY-LAYER-PLAN.md`.

## 12. Document layout and contracts

Guideline (not a rigid rule): **optimize a document's layout for its dominant
consumption pattern, not its write pattern.** Storage order should minimize the
work of the reader who matters most for that file. This generalizes the earlier
"prepend logs" instinct: prepend is right *only* for files whose dominant read is
"what happened recently."

Three document classes:

| class | dominant read | maintenance | examples |
|---|---|---|---|
| **Current state** | read to know what is true now | **edit in place** | line registry, persona registry, foundation queue, scorecards |
| **Historical record** | searched for a specific item; sequence and stable references matter | **append chronologically** | decision history, operating-model revisions, theorem evolution, published-experiment history |
| **Operational log** | read newest-first to grasp recent state; readers stop after relevant recent entries | **prepend newest-first** | project log, memory logs, run logs, research observations, decision proposals, automation outputs |

Each significant file should eventually declare a **Document Contract** in
front-matter, so agents are *told* how to use it rather than inferring it. See
[`DOCUMENT-CONTRACT.md`](DOCUMENT-CONTRACT.md) for the schema and field
vocabulary. Rollout is incremental (a `govern/research-memory` task); see
`registries/decision-history.md` DEC-010.

---

## Deliberately deferred

To respect the phase separation, this model intentionally does **not** decide:
workflow-level behavior and prompts (Phase 3); automation cadence, scheduling, or
resource allocation (Phase 4); or the concrete schema of each registry beyond its
purpose (Phase 2). Those are recorded as open questions in `PROJECT-LOG.md`.
