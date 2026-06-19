---
document_type: memory_pack
primary_reader: automation
read_pattern: current_state
write_pattern: edit_in_place
authority: guidance_only
summarizable: false
scope: govern
---

# Govern Family — Memory Pack (load surface)

> **This file is the compact load surface — the only thing ordinary agents read.**
> Never read the raw `memory-log.md`; that is summarizer-only.

## Brief

- **Purpose.** Carry durable, compact guidance for the **govern** family so its
  workflows improve across runs without re-reading raw history.
- **Scope.** The govern family: `line-review`, `lifecycle-review`,
  `portfolio-review`, `decision-review`, `line-intake`, `persona-governance`,
  `research-memory`, `information-portfolio`. Recurring lessons, heuristics,
  anti-patterns, and failure modes specific to improving the program's quality,
  fairness, memory, and allocation accumulate here.
- **How it may help.** Read this surface before acting to pick up accumulated
  heuristics and known failure modes; after acceptance, append a learning-return
  entry to the log (below) so the next run is better informed. **Guidance only —
  it never overrides a higher authority surface.**
- **Note:** `govern/research-memory` has a dual relationship to this pack — it is
  a consumer like any govern workflow, **and** it owns the summarizer that
  produces this surface.

## Principles & Decisions

Dated, **append-only** table of durable lessons the summarizer has promoted from
the log. Entries are added, never edited away (a superseded entry is marked, not
deleted). No lessons are invented; the example row below is illustrative only.

| date | lesson (heuristic / anti-pattern / failure mode) | source (log entry / round_ref) | status |
|---|---|---|---|
| _example_ | _(e.g. "A standing snapshot that disagrees with an authority surface is logged as conflict, never used to overwrite it.")_ | _none — illustrative_ | _example_ |
| — | _none yet — no lessons promoted_ | — | — |

## Current Memory Summary

_No entries yet — nothing summarized._ The raw `memory-log.md` is empty, so the
summarizer has produced no rolled-up guidance. This section is rewritten **from**
the log by the summarizer and is **never hand-written**.

## Summarizer Contract

The summarizer role is **owned by `govern/research-memory`** (see that workflow
for the authoritative interface). It is the **only** reader of `memory-log.md`.
Per `MEMORY-LAYER-PLAN.md`, one summarizer cycle on this pack:

1. **Read to the marker** — read `memory-log.md` newest-first down to the
   `last-summarized` marker (everything below is already rolled up).
2. **Group** — cluster the new entries by failure mode / heuristic / anti-pattern.
3. **Discard noise** — drop one-off noise; keep recurring or user-corrected
   lessons.
4. **Rewrite the summary** — rewrite the *Current Memory Summary* above as
   guidance (never hand-written prose; always derived from the log).
5. **Promote durable lessons** — append durable, recurring lessons to the
   *Principles & Decisions* table (dated, append-only).
6. **Drop a new marker** — place a fresh `last-summarized` marker at the new top
   of the log.

The summarizer **never writes new policy** onto the pack. Cadence is left open
(Phase 4 build choice). Nothing is deleted from disk — "pruning" = summarizing a
lesson out of the surface, not removing it from the log.

## Authority disclaimer & escalation

This pack is **guidance/memory only** and sits at **rank 6** in the authority
order (`RESEARCH-OPERATING-MODEL.md` §11). The surfaces that **outrank** it, in
order, always win on conflict:

```text
1. NORTH-STAR.md
2. RESEARCH-OPERATING-MODEL.md
3. Workflow definition
4. Registry schemas
5. Explicit user decisions
6. Memory Pack  ← this file (guidance only)
7. Raw logs
```

- Conflicts are **logged, never silently resolved** — record a
  `confusion_or_conflict` learning-return entry and defer to the higher surface.
- **Policy-class lessons route OUT** to `govern/decision-review`; they **never
  become policy inside this pack**.
- A lesson implying a change to a higher surface is a **proposal**, not a fact in
  the pack.
- **Promotion rule:** a workflow earns its own pack only after repeated
  workflow-specific lessons exceed what this family pack captures (`DEC-005`).

**Learning-return schema:** see the template in `memory-log.md` and
`MEMORY-LAYER-PLAN.md` (fields: `pack_ref`, `work_ref`, `round_ref`,
`guidance_used`, `missing_guidance`, `confusion_or_conflict`,
`observed_failure_mode`, `output_quality_signal`, `suggested_summary_update`).
