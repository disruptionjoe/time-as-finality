---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: motif_map_and_definition_candidate
summarizable: false
unit_of_review: one_motif_census_scope
---

# Motif Census / Emergence Detector

**Family:** explore
**Mode:** search
**Status:** Phase 3 extension - v0.1 workflow proposal. Not yet mapped into the
Phase 4 automation scaffold.
**Consumes:** recent artifacts, persona runs, tests, explorations, and technical
reports.
**Emits:** motif map, formalization candidates, metaphor-only demotions, and
routed candidate research tasks.

## Purpose

Detect recurring structures that keep appearing across the repo even when they
were not deliberately planted. The workflow asks what the project is becoming
about by scanning for repeated roles such as witnesses, transport, forgetting,
reconstruction, loops, records, irreversibility, admissibility, settlement, and
observer limits.

The workflow does not promote a motif merely because it is frequent. It tests
whether the motif is metaphorical, operational, formal, or definition-ready, then
routes the next step.

## Authority boundaries

- **May:** scan recent and historical artifacts for recurring motifs; assign
  motif-specialist passes; classify each occurrence by role and formal status;
  produce a motif map; propose definition candidates or new research-line seeds;
  route definition work to the relevant explore/exploit workflow.
- **Must not:** declare a motif to be a new primitive; rewrite glossary or
  formalism directly; promote a motif to claim status; merge research lines;
  treat shared vocabulary as shared structure without role comparison.
- **Scoring authority:** judgment-with-rationale over motif recurrence,
  independence, role stability, and formal readiness.
- **Write authority:** direct write for motif census reports; patch-first for
  definition or glossary proposals.

## Read surfaces

- `explorations/`, especially recent persona-goal runs and synthesis reports.
- `tests/`, `models/`, `claims/`, `technical-reports/`, `papers/`, and
  `open-problems/`.
- `GLOSSARY.md`, `FORMALISM.md`, `Method - Research Program Guidelines.md`.
- `workflows/README.md`, `workflows/RESEARCH-OPERATING-MODEL.md`,
  `workflows/registries/line-registry.md`, and prior synthesis logs.
- Explore Memory Pack load surface if present.

## Write surfaces

- A motif map under `workflows/logs/synthesis/` or `explorations/`.
- Candidate definition proposals routed to the owner surface.
- Candidate research-line seeds routed to `explore/line-discovery`.
- Docket items for missing routes or definition policy gaps.
- Run log and verdict block.

## Memory interface (Phase 3.5; may be inert)

- Reads: motifs previously found, false motif collapses, repeated metaphor traps,
  prior definition candidates.
- Writes: `guidance_used`, `missing_guidance`, `confusion_or_conflict`,
  `observed_failure_mode`, `output_quality_signal`, `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** line registry for motif distribution by research line; persona
  clusters for independent-origin checks; decision history for authority rules.
- **Writes:** none directly. Routes candidate seeds to line-discovery/intake and
  definition proposals to the owner surface.

## Procedure

1. **Set census scope.** Choose a bounded slice: recent artifacts, one research
   line, one motif family, or a time window.
2. **Extract candidate motifs.** Record recurring roles, not just recurring
   words.
3. **Assign motif-specialist passes.** Each pass searches for one motif across
   the scope and records every occurrence, including cases where the same role is
   called something else.
4. **Classify occurrence status.**
   - `metaphorical`
   - `operational`
   - `formal`
   - `definition_candidate`
   - `absorbed_by_existing_term`
5. **Synthesize motif structure.** Ask whether the occurrences are separate
   metaphors, repeated local tools, or symptoms of one deeper structure.
6. **Route consequences.** Definition candidates route to the owner surface;
   line-worthy structures route to `explore/line-discovery`; overused metaphors
   route to cleanup or guardrail tasks.

## Outputs

**Motif occurrence:**

```yaml
motif_occurrence:
  motif:
  artifact:
  local_name:
  role_played:
  status: metaphorical | operational | formal | definition_candidate | absorbed_by_existing_term
  evidence_excerpt_or_pointer:
  could_be_definition_if:
  demote_if:
```

**Motif map:**

```yaml
motif_map:
  census_scope:
  motifs:
    - motif:
      occurrence_count:
      independent_origins:
      role_stability:
      formal_readiness:
      candidate_definition:
      proposed_owner_workflow:
  synthesis_question:
  verdict:
```

Every run ends with the verdict block.

## Escalation triggers

Route to `explore/line-discovery` when a motif suggests a new research line; to
`explore/cross-disciplinary-synthesis` when it is cross-cluster convergence; to
`govern/portfolio-review` when motifs imply line merge/split/overlap; to
`govern/decision-review` when motif promotion needs a policy decision; to
`exploit/challenge-primary` when a motif exposes an overclaim in a central line.

## Failure modes

- **Word-count fallacy.** Frequency of a term is mistaken for structure. Guard:
  classify roles, not words.
- **Metaphor inflation.** A repeated metaphor becomes a primitive. Guard: require
  operational or formal status before definition work.
- **Over-compression.** Different mechanisms are collapsed because they feel
  similar. Guard: record role differences and absorber fields.
- **Authority creep.** The workflow edits glossary or claims directly. Guard:
  patch-first proposals only.
- **Recentness bias.** Only the newest artifacts count. Guard: scope must state
  whether the run is recent-only or historical.

## Success criteria

A good run produces a motif map that separates metaphor from formal structure,
names at least one definition candidate or demotion, and routes each consequence
to an owner.

Cheap auditability test: a reviewer can see where the motif appears, what role it
plays in each place, whether the role is stable, and what would make it a real
definition rather than repeated language.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `explore/motif-scope-assemble` - build artifact slice.
- `explore/motif-specialist-pass` - one motif search.
- `explore/motif-status-classify` - classify occurrences.
- `explore/motif-synthesis-route` - synthesize and route.

Likely cadence differences:
- Periodic after batches of persona runs.
- Event-triggered when multiple artifacts repeat an unowned term.

Likely context boundaries:
- Specialist passes load only one motif plus the scoped corpus.
- Synthesis loads occurrence tables, not every source document.

Likely deterministic vs judgment split:
- Deterministic: source collection, occurrence table formatting.
- Judgment-based: role equivalence, formal readiness, definition candidacy.

Phase 4 coverage questions:
- Does every motif occurrence have an artifact pointer?
- Does every definition candidate have an owner?
- Are metaphor-only cases explicitly demoted?
- Does the synthesis distinguish shared vocabulary from shared role?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```
