# Workflow Memory Layer — Plan (Phase 3.5)

**Phase:** 3.5 (sits between Phase 3 Workflow Design and Phase 4 Automation).
**Status:** BUILT (Session 17, DEC-023) — family packs live under `context-packs/`. (Originally PLAN ONLY.) The three family
packs now exist; they are inert until workflows run and are summarized by
`govern/research-memory`. **Automation (Phase 4) is designed but not armed.**

## Purpose

Establish a reusable memory substrate that lets workflows **accumulate learning
across runs without re-reading raw history every time**. The goal is not another
authority surface — it is durable, compact guidance so workflows improve over
time. A Memory Pack is **guidance and memory only**; on any conflict, the
authority surface wins (see authority order below).

## Position in the phase model

```text
Phase 1  Research Operating Model
   ↓
Phase 2  Workflow Skeleton
   ↓
Phase 3  Workflow Design (per workflow, collaboratively)
   ↓
Phase 3.5  Workflow Memory Layer   ← this plan
   ↓
Phase 4  Automation, scheduling, cadence, execution
```

The intent: workflows begin their automated life already equipped with a
lightweight, durable learning substrate.

## Initial scope — family-level packs only

Do **not** create a Memory Pack per workflow. Instantiate packs at the
**workflow-family** level only — three packs, because each family has distinct
recurring lessons, heuristics, anti-patterns, and failure modes that should
accumulate independently.

### Folder structure (created — Session 17)

```text
workflows/context-packs/
  exploit/
    MEMORY.md        # compact load surface (the only thing ordinary agents read)
    memory-log.md    # prepend-only raw log (summarizer-only)
  explore/
    MEMORY.md
    memory-log.md
  govern/
    MEMORY.md
    memory-log.md
```

## Promotion rule (future workflow-specific packs)

A workflow earns its **own** Memory Pack only after repeated executions
demonstrate workflow-specific lessons not adequately captured by its family-level
pack. This keeps the system simple while letting specialization emerge naturally.
Until then, all of a family's workflows share the family pack.

## Authority hierarchy

The Memory Pack is the second-lowest surface in the program's authority order
(canonical in `RESEARCH-OPERATING-MODEL.md` §11):

1. `NORTH-STAR.md`
2. `RESEARCH-OPERATING-MODEL.md`
3. Workflow definition
4. Registry schemas
5. Explicit user decisions
6. **Memory Pack** (guidance/memory only)
7. Raw logs

Authority flows downward. Conflicts are logged (as a `confusion_or_conflict`
signal), never silently resolved. A lesson that implies a change to a higher
surface is routed out as a proposal/work item — it must not become policy by
living in the pack.

## Required structure of each pack (the five pieces)

Adopted from the portable Agent Memory Pack pattern. Every pack instance must
include all five; none may be dropped. (Full mechanics are designed in
implementation, not here.)

1. **Compact load surface (`MEMORY.md`)** — the only thing ordinary agents load:
   brief (purpose, scope, how it may help); a dated append-only "Principles &
   Decisions" table (promoted rules); a "Current Memory Summary" rolled *from* the
   log (never hand-written); a summarizer-contract pointer; an authority
   disclaimer; a reference to the learning-return schema.
2. **Prepend-only raw memory log (`memory-log.md`)** — summarizer-only,
   newest-first, short evidence-grounded entries. Ordinary agents never load it.
   No destructive pruning ("pruning" = summarizing out of the surface, not
   deleting from disk).
3. **Summarizer contract** — defines what turns log → guidance: read to the
   `last-summarized` marker; group by failure mode / heuristic / anti-pattern;
   discard one-off noise, keep recurring or user-corrected lessons; rewrite the
   Current Memory Summary as guidance; promote durable lessons into Principles &
   Decisions; drop a new `last-summarized` marker. Cadence is left open.
4. **Learning-return schema** — what each consuming agent appends *after
   acceptance*: `pack_ref`, `work_ref`, `round_ref`, `guidance_used`,
   `missing_guidance`, `confusion_or_conflict`, `observed_failure_mode`,
   `output_quality_signal`, `suggested_summary_update`. Any field may be blank.
5. **Authority disclaimer + escalation path** — pack is guidance/memory only;
   named authority surfaces always win; conflicts are logged not resolved;
   policy-class lessons route out as proposals.

## Reading-audience separation

- **Ordinary agents** read only the compact load surface (`MEMORY.md`).
- **The summarizer** (and only it) reads the raw `memory-log.md` and rolls
  accepted lessons up onto the load surface.

## Instance family for this program

Of the three portable families (Stage Context Pack / Anchored-Agent Memory Layer
/ Job-Flow Pack), the workflow memory layer uses the **Stage Context Pack** form,
keyed by **workflow family** (exploit / explore / govern): lightest weight,
pure guidance + rolled memory, no persona, no triggers, no self-update. Loading
hooks, summarizer cadence, and schema specifics are implementation choices for
Phase 3.5 build, not fixed here.

## Inheritance rules (apply to every pack instance)

1. All five pieces present; none dropped.
2. Ordinary agents load the surface, not the log.
3. Prepend-only; no silent destructive prune; rollup via summarization.
4. Summarizer never writes new policy onto the pack; policy-class lessons route out.
5. Authority surface always wins on conflict; conflict is logged, not resolved.
6. Loading hooks, cadence, and schema changes are instance choices; the pattern
   installs none of them.

## Deferred to implementation (after Phase 3 stabilizes)

Creating the three packs and their files; wiring the load hook so workflows read
the surface before acting and return a learning signal after; writing the
summarizer; and validating (e.g. N shadow runs vs a no-pack baseline) before
trusting it unattended.
