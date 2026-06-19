# Line Discovery

**Family:** explore
**Mode:** search
**Status:** placeholder (Phase 2). Behavior designed in Phase 3.

## Purpose
Generate and seed candidate research lines to widen the reachable search space
and reduce local-optimum risk.

## Expected inputs
`registries/line-registry.md` (to avoid duplicates); `explorations/BACKLOG.md`;
recent sprint outputs in `explorations/`; prior discovery runs. May invoke
`agent-skills/persona-idea-sprint`.

## Expected outputs
New `RL-NNN` seeds in the line registry; sketches in `explorations/`; candidate
scores; run record; verdict block.

## Related registries
`line-registry` (write), `persona-clusters` (read).

## Open questions
How many seeds per run? What is the seed-vs-discard threshold?
