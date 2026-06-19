---
document_type: specification
primary_reader: mixed
read_pattern: current_state
write_pattern: edit_in_place
authority: guidance_only
summarizable: false
---

# Context Packs — the Workflow Memory Layer (Phase 3.5)

This directory is the **substrate** for the program's workflow memory layer. It
lets workflows accumulate durable, compact learning across runs **without
re-reading raw history every time**. It is built per `MEMORY-LAYER-PLAN.md` and is
**inert until workflows run** — creating these files installs no automation, no
load hook, and no summarizer cadence (those are Phase 4 / build choices).

A Context Pack is **guidance and memory only**. It is never an authority, never a
queue, never a source of truth. On any conflict, a higher surface always wins
(see Authority below).

## Family packs only (for now)

Per `DEC-005`, packs exist at the **workflow-family** level only — three packs,
one per family, because each family accumulates distinct recurring lessons,
heuristics, anti-patterns, and failure modes:

```text
workflows/context-packs/
  exploit/   MEMORY.md  memory-log.md
  explore/   MEMORY.md  memory-log.md
  govern/    MEMORY.md  memory-log.md
```

- **exploit/** serves `advance-primary`, `advance-secondary`, `challenge-primary`,
  `integrate-results`.
- **explore/** serves `line-discovery`, `line-incubation`, `foundation-ingestion`,
  `cross-disciplinary-synthesis`, `landscape-reassessment`, `persona-expansion`.
- **govern/** serves `line-review`, `lifecycle-review`, `portfolio-review`,
  `decision-review`, `line-intake`, `persona-governance`, `research-memory`,
  `information-portfolio`.

### Promotion rule (future workflow-specific packs)

A workflow earns its **own** pack only after repeated runs demonstrate
workflow-specific lessons not adequately captured by its family-level pack. Until
then every workflow in a family shares the family pack. This keeps the system
simple and lets specialization emerge from evidence, not anticipation.

## Two files per pack — separate reading audiences

| file | role | who reads it | write pattern |
|---|---|---|---|
| `MEMORY.md` | **compact load surface** | every ordinary agent, before acting | edit in place (summarizer rewrites the summary; appends to the table) |
| `memory-log.md` | **prepend-only raw log** | the **summarizer only** | prepend newest-first; learning-return entries appended after acceptance |

**Ordinary agents read only `MEMORY.md`. They never read the log.** Only the
summarizer reads `memory-log.md` and rolls accepted lessons up onto the load
surface. "Pruning" means **summarizing a lesson out of the surface — never
deleting it from disk**; the log is non-destructive.

## Authority — rank 6 (guidance only)

The pack is the second-lowest surface in the program's authority order
(`RESEARCH-OPERATING-MODEL.md` §11). Authority flows downward; a lower surface
never overrides a higher one:

```text
1. NORTH-STAR.md
2. RESEARCH-OPERATING-MODEL.md
3. Workflow definition
4. Registry schemas
5. Explicit user decisions
6. Memory Pack  ← this layer (guidance/memory only)
7. Raw logs
```

Conflicts are **logged, never silently resolved** (recorded as a
`confusion_or_conflict` learning-return signal). A lesson that implies a change to
a higher surface is **routed out as a proposal** to `govern/decision-review` — it
must not become policy by living in the pack. **Policy-class lessons never become
policy inside a pack.**

## Ownership

`govern/research-memory` **owns the summarizer role** and is the only workflow
that rolls the raw log up onto the load surface. It specifies the summarizer
contract; each `MEMORY.md` carries the same contract for legibility. The layer is
plan-built here (`DEC-004`) and remains inert — no live triggers — until Phase 4
wires the load hook and summarizer cadence.

## See also

- `../MEMORY-LAYER-PLAN.md` — the spec (the five required pieces, the summarizer
  contract, the learning-return schema, inheritance rules).
- `../DOCUMENT-CONTRACT.md` — front-matter schema used by every file here.
- `../RESEARCH-OPERATING-MODEL.md` §9 (memory), §11 (authority), §12 (document
  classes).
- `../govern/research-memory.md` — the workflow that owns the summarizer.
- `../registries/decision-history.md` — `DEC-004`, `DEC-005`, `DEC-010`.
