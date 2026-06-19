---
document_type: specification
primary_reader: mixed
read_pattern: current_state
write_pattern: edit_in_place
authority: guidance_only
summarizable: false
---

# Automation Scaffold (Phase 4) — Index

**Phase:** 4 (automation design). **Status:** DESIGN / SPEC ONLY. This phase maps
the locked Phase-3 workflow protocols into bounded execution atoms, names their
intended cadences and trigger *types*, and registers every intended trigger as a
spec. It stops one step short of turning anything on.

> **HARD RULE — No live triggers are armed in this phase; arming is a separate,
> later, human-gated step.**

Nothing in this directory creates a scheduled task, cron job, webhook, or live
event listener. Every intended trigger is recorded with `status: NOT-ARMED` and a
list of `arming_prerequisites`. Arming is performed later, deliberately, by a
human-gated step — never as a side effect of reading or writing these files.

## Why this phase exists

`RESEARCH-OPERATING-MODEL.md` §13 distinguishes three layers:

- **Workflow = protocol** — what the system may do, read, write; its authority and
  escalation (designed in Phase 3, many now LOCKED).
- **Task = bounded execution unit** — the smaller object an agent can load,
  complete, audit, and rerun in one context window (mapped here, Phase 4).
- **Schedule = when** a task runs — cadence or event (specced here, armed later).

DEC-013 formalizes the rule that governs this whole phase: **authority does not
decompose with size.** A task atom *inherits* its workflow's authority and may
never exceed it. Splitting a workflow into atoms reduces context burden and
improves auditability; it must never create hidden authority. Patch-first stays
patch-first at the atom level. Only the correct authority surface (§11) accepts or
canonizes a change.

A good atom (DEC-013, §13): **one object, one job, one main output, one escalation
path; idempotent and resumable.** Atoms are split by **cadence, context-shape,
determinism, and audit boundary — not by step count.**

## The three artifacts

1. **`COVERAGE-MATRIX.md`** — the workflow → task-atom map. For every one of the 18
   workflows, it enumerates the task atoms named in that workflow's *Future
   automation decomposition notes*, and for each atom records a YAML block (unit of
   work, loads, emits, determinism, cadence, trigger type, write target,
   patch-only vs direct-write fields, downstream consumers, escalation target,
   memory pack, too-large risk, notes). It closes with the cross-set **coverage
   questions** (every output has a consumer? every registry write has an owning
   task? every escalation has a destination? every scheduled task has a bounded
   object? anything reviewed twice? any unit too large?).

2. **`SCHEDULE-SPEC.md`** — the intended cadences and trigger *types* grouped as
   event-driven / periodic / threshold-based / manual-only, with the ordering and
   dependencies between atoms, research-budget and resource notes (ROM §2), and an
   explicit list of atoms that should **not** be automated yet. Spec only.

3. **`TRIGGER-REGISTRY.md`** — a registry that lists each intended trigger as a row
   (trigger_id, atom, cadence, condition, owning workflow, `status: NOT-ARMED`,
   arming prerequisites). It is the single place that makes explicit, per trigger,
   that nothing is live and what must be true before it could be.

## How to read these together

Coverage Matrix answers *what the atoms are and whether the system is closed*.
Schedule Spec answers *when and in what order they would run, and what we are
deliberately not automating*. Trigger Registry answers *which specific triggers
exist on paper, and what gates each one*. None of the three arms anything.

## Authority and scope reminders

- These files are `authority: guidance_only` / registry spec. They sit far below
  the canonical surfaces in §11 and grant **no** authority to any atom.
- Acceptance atoms (those that touch canonical Decision History, the line
  registry, durable claim/roadmap surfaces, or apply interpretive patches)
  **never auto-run**. They are listed for completeness with manual-only triggers
  and explicit arming prerequisites.
- Where a policy decision is missing (patch-acceptance owner, concrete cadences,
  numeric thresholds), it is recorded as an **Open Question / arming-prerequisite**
  here and in the Trigger Registry — it is **not** invented as policy.

## Coverage at a glance

- Workflows covered: **18 / 18** (govern 8, explore 6, exploit 4).
- Task atoms enumerated: **65** (govern 33, explore 20, exploit 12).
- Triggers specced: see `TRIGGER-REGISTRY.md` — **all `NOT-ARMED`.**
