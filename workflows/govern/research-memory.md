# Research Memory

**Family:** govern
**Mode:** evaluation
**Status:** placeholder (Phase 2). Behavior designed in Phase 3.

## Purpose
Keep long-term memory coherent and compaction-resilient: log hygiene, synthesis
notes, and project-log upkeep.

## Expected inputs
`logs/` (runs, synthesis, best-next-move); all registries; `PROJECT-LOG.md`.

## Expected outputs
Synthesis notes in `logs/synthesis/`; log rotation/indexing; `PROJECT-LOG.md`
entries; run record; verdict block.

## Related registries
All registries (read).

## Open questions
Log rotation policy. What compaction-resilience checks confirm a new agent can
resume from logs + registries alone?
