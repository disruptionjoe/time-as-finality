---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: constellation_report_and_candidate_proposals
summarizable: false
unit_of_review: one_constellation_run
---

# Research Constellation Orchestrator

**Family:** explore
**Mode:** search
**Status:** Phase 3 addendum - v0.1 PROPOSED (not automation-armed).
Phase 4 automation must explicitly opt in before this workflow is scheduled.
**Consumes:** current repo state, persona panel, persona clusters, recent
explorations, active open problems, and North Star surfaces.
**Emits:** a non-canonical constellation report; candidate directions routed to
the owning explore/exploit/govern workflow.

## Purpose

Create a structured multi-perspective research process that explores several
important research directions simultaneously through independent persona rooms.

The workflow is not trying to make the rooms agree. It is designed to expose
overlooked connections, productive tensions, minority views, and directions that
linear next-task execution would likely miss.

This is **Search Mode**. A constellation report is a discovery artifact, not
claim evidence, not a roadmap update, and not a governance decision.

## Authority Boundaries

- **May:** choose three research directions from current repo state; select
  diverse non-overlapping personas from the canonical panel; simulate three
  structured multi-round room discussions; synthesize each room; compare the
  rooms; propose next directions; write a non-canonical exploration/report
  artifact.
- **Must not:** update claim statuses, `CLAIM-LEDGER.md`, `ROADMAP.md`, test
  status, line registry state, persona registries, automation schedules, or
  trigger specs; register new research lines directly; promote a room insight
  to canon; collapse disagreement into forced consensus.
- **Scoring authority:** descriptive judgment only. The workflow may attach
  confidence assessments to insights and next directions, but these are
  exploration confidence signals, not line standing or truth scores.
- **Write authority:** patch-first exploration/report output. Canonical
  consequences route to the owning workflow.

## Read Surfaces

- **Persona sources:** `personas/EXPERT-PANEL.md` and `personas/INDEX.md`.
- **Persona cluster map:** `workflows/registries/persona-clusters.md`.
- **Current research state:** recent `explorations/`, active `open-problems/`,
  `claims/`, `tests/`, and relevant technical reports.
- **North Star context:** `NORTH-STAR.md`, `workflows/RESEARCH-OPERATING-MODEL.md`,
  and `explorations/BACKLOG.md`.
- **Workflow catalog:** `workflows/README.md` and this workflow file, to validate
  route targets.
- **Explore Memory Pack load surface** if present; inert if absent.

## Write Surfaces

- A timestamped **constellation report** under `explorations/`, normally named:

  ```text
  explorations/research-constellation-orchestrator-YYYY-MM-DD.md
  ```

- Optional candidate direction payloads routed to:
  `explore/line-discovery`, `explore/cross-disciplinary-synthesis`,
  `explore/landscape-reassessment`, `explore/persona-expansion`,
  `exploit/challenge-primary`, `exploit/advance-primary`,
  `exploit/advance-secondary`, or the appropriate govern workflow.
- A run log only if the surrounding workflow runner requires one.

**No canonical write by default.** The report may recommend follow-up artifacts,
but it does not create or update canonical state.

## Memory Interface (Phase 3.5; may be inert)

- Reads: prior constellation reports, known room-selection pitfalls, repeated
  cross-room signals, previously routed next directions.
- Writes after a run: `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Procedure

### 1. Establish Scope

Read current repo state and state the run scope:

- whether this is a whole-program constellation or a focused constellation;
- the current active frontier;
- the strongest secondary branch;
- the long-horizon North Star direction that should be represented even if it
  lacks a current path to proof.

### 2. Choose Three Rooms

Create exactly three independent research rooms unless the user explicitly asks
for a different count:

1. **Primary active research line.** The most important active formal or
   exploit-facing line.
2. **Strongest secondary branch.** The best-supported or most actionable
   alternate direction.
3. **Broader North Star direction.** The long-horizon intuition or program
   spine, even if current evidence has not established a path to it.

For each room, write:

```yaml
room:
  name:
  research_direction:
  why_this_direction_now:
  relevant_repo_context:
```

### 3. Select Personas

Use only existing personas. Prefer the canonical numbered panel in
`personas/EXPERT-PANEL.md`; lens registry entries from `personas/INDEX.md` may
be used as supplementary posture labels, not as substitutes for named personas
unless the run explicitly chooses lens rooms.

Selection constraints:

- Each room must contain a diverse set of personas.
- Prefer representation across distant persona clusters.
- No persona may appear in more than one room.
- Each room should include constructive, skeptical, formal, empirical, and
  cross-domain pressure where possible.
- Preserve valuable cross-cutting personas even when they are not cleanly
  clustered.

Record the assignment table:

```yaml
persona_assignment:
  room:
  persona_id:
  persona_name:
  cluster_or_role:
  why_selected:
```

### 4. Run Three Rounds Per Room

Each room is a discussion, not parallel independent memos. Every participant
has access to what earlier participants said in that room.

#### Round 1 - Divergence

Participants expand the space:

- new hypotheses;
- analogies;
- cross-disciplinary connections;
- unexpected interpretations;
- adjacent ideas worth investigating;
- minority or hostile possibilities.

#### Round 2 - Convergence

Participants react to earlier contributions:

- what changed their thinking;
- which ideas became more important;
- which conflicts are productive;
- where apparent disagreements point to a better framing.

#### Round 3 - Reflection And Judgment

Participants give final perspectives:

- what now seems most important;
- what direction appears most promising;
- what opportunity would be easiest to miss;
- what deserves immediate attention;
- confidence or uncertainty where useful.

### 5. Produce Room Synthesis

After each room, write a synthesis preserving disagreements and valuable
minority views:

```yaml
room_synthesis:
  strongest_insight:
  most_novel_insight:
  most_profound_implication:
  most_actionable_next_direction:
  additional_promising_directions:
  major_disagreements:
  areas_of_uncertainty:
  confidence_assessments:
  minority_viewpoints_to_preserve:
```

### 6. Orchestrator Comparison

Compare all room syntheses:

- recurring signals;
- uniquely important single-room insights;
- tensions and contradictions;
- unexpected cross-room connections;
- assumptions challenged;
- opportunities easy to overlook;
- directions deserving further investigation.

### 7. Route Consequences

Route, but do not apply, consequences:

- New candidate research line -> `explore/line-discovery`.
- Cross-cluster structural convergence -> `explore/cross-disciplinary-synthesis`.
- Landscape topology shift -> `explore/landscape-reassessment`.
- Existing primary line pressure -> `exploit/challenge-primary`.
- Direct next test on an active line -> relevant exploit workflow.
- Missing persona coverage -> `explore/persona-expansion`.
- Registry, policy, or authority issue -> appropriate govern workflow.

If a needed route does not exist, emit `undefined-workflow-needed` in the report
instead of inventing authority.

### 8. Emit Report

The report should include:

- status and authority caveat;
- repository context read;
- room framing decision;
- persona assignment strategy;
- room discussions;
- room syntheses;
- orchestrator cross-room report;
- proposed next artifacts or workflow routes;
- explicit non-actions: canonical files not updated, triggers not armed.

End with the verdict block.

## Output Shape

Every constellation report should answer:

- What appears important across multiple rooms?
- What appears uniquely important within a single room?
- What new research directions emerged?
- What assumptions were challenged?
- What opportunities might be easy to overlook?
- What deserves further investigation?

Suggested final section:

```text
Orchestrator Judgment

The strongest cross-room signal is ...

Proposed Next Concrete Artifact

...
```

Every run ends with:

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Escalation Triggers

- A room insight proposes an executable test -> route to the relevant exploit
  workflow or `explore/line-discovery`.
- A cross-room signal appears across distant clusters -> route to
  `explore/cross-disciplinary-synthesis`.
- The report shows the current landscape topology has changed -> route to
  `explore/landscape-reassessment`.
- The process reveals missing persona coverage -> route to
  `explore/persona-expansion`.
- The process suggests canonical updates -> route to the owning govern or
  exploit workflow; do not apply them here.

## Failure Modes

- **Consensus pressure.** The room synthesis averages away important minority
  views. Guard: explicitly preserve minority viewpoints.
- **Parallel memo drift.** Participants produce isolated analyses instead of
  reacting to one another. Guard: round 2 and round 3 must reference earlier
  room contributions.
- **Persona duplication.** One high-status persona appears in several rooms.
  Guard: assignment table with exclusivity check.
- **Cluster monoculture.** A room is diverse by headcount but not by discipline.
  Guard: cluster-distance check.
- **Authority creep.** The workflow updates claims, roadmap, registries, or
  automation state. Guard: report-only by default and route consequences.
- **North Star contamination.** Long-horizon intuition is treated as evidence.
  Guard: North Star room can generate questions, not claim support.
- **Efficiency bias.** The workflow shrinks too quickly to the most obvious next
  task. Guard: three-room design and divergence-first protocol.

## Success Criteria

A good run produces a report where:

- the three rooms are genuinely different research directions;
- persona assignments are diverse and non-overlapping;
- the room conversations visibly evolve across three rounds;
- room syntheses preserve disagreement;
- the cross-room report names signals that were not obvious from any one room;
- proposed next directions are routed without canonical overreach.

Cheap test: a reviewer can identify at least one insight that emerged only
because two or more rooms were compared.

## Future Automation Decomposition Notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it.*

Likely execution atoms:

- `explore/constellation-scope` - read current state and frame three rooms.
- `explore/constellation-persona-assign` - select non-overlapping persona sets.
- `explore/constellation-room-run` - run one room through three rounds.
- `explore/constellation-room-synthesize` - synthesize one room.
- `explore/constellation-cross-room-compare` - produce orchestrator report.
- `explore/constellation-route` - package next directions for owning workflows.

Likely deterministic vs judgment split:

- Deterministic: persona exclusivity, cluster coverage, route-target existence,
  report section checks.
- Judgment-based: room framing, discussion simulation, synthesis, confidence,
  cross-room insight extraction.

Likely cadence:

- Event-triggered after major exploration bursts, major claim weakening, or
  evidence that the program is stuck in local next-task execution.
- Low periodic cadence if used as a landscape-widening process.

## Verdict Block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open Questions

1. How many personas per room is optimal before discussion quality degrades?
2. Should room outputs be written as full transcripts or compressed dialogue?
3. Should this workflow have a dedicated log directory under `logs/synthesis/`
   or continue writing timestamped reports under `explorations/`?
4. What threshold makes a cross-room signal strong enough to route to
   `explore/cross-disciplinary-synthesis` rather than only appear in the report?
