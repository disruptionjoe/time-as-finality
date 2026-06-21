---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: interpretation_lead_proposal
summarizable: false
unit_of_review: one_interpretation_tournament
---

# Theory Tournament

**Family:** govern
**Mode:** evaluation
**Status:** Phase 3 extension - v0.1 workflow proposal. Not yet mapped into the
Phase 4 automation scaffold.
**Consumes:** a shared corpus and a declared set of competing interpretations.
**Emits:** scored interpretation tournament, current lead interpretation proposal,
minority-program preservation notes, and routed tasks.

## Purpose

Prevent the repo from overcommitting to one grand interpretation before rivals
have competed on concrete criteria. The workflow creates competing schools of
interpretation, gives each a fresh-context advocate, and judges them against the
same corpus.

The winner is not truth. It is the current lead interpretation: the frame that
best explains artifacts, generates tasks, remains falsifiable, avoids
overclaiming, connects to external fields, and would matter if true. Runners-up
remain live minority programs when they preserve distinctive value.

## Authority boundaries

- **May:** define a tournament corpus; instantiate competing interpretation
  advocates; score interpretations; propose a current lead interpretation;
  preserve minority programs; route new tasks, line-review signals, or portfolio
  questions.
- **Must not:** declare the winning interpretation true; archive runner-up
  programs; rewrite North Star or claim surfaces; promote/demote lines directly;
  let one advocate see other advocates' arguments before submitting; treat
  publishability or transformative potential as evidence of truth.
- **Scoring authority:** judgment-with-rationale using declared criteria and
  evidence pointers.
- **Write authority:** direct write for tournament reports; patch-first for any
  proposed catalog, registry, or documentation changes.

## Read surfaces

- Shared tournament corpus: chosen claims, tests, models, papers, technical
  reports, persona-run artifacts, and synthesis logs.
- `Vision - North Star.md`, `Method - Research Program Guidelines.md`,
  `Lead Research Line - Time as Finality.md`, `FORMALISM.md`, `GLOSSARY.md`.
- `workflows/registries/line-registry.md`,
  `workflows/registries/research-line-scorecard.md`,
  `workflows/registries/persona-clusters.md`.
- Prior portfolio and landscape reassessment outputs.
- Govern Memory Pack load surface if present.

## Write surfaces

- Tournament report under `workflows/logs/synthesis/` or `explorations/`.
- Lead-interpretation proposal, non-canonical until accepted.
- Minority interpretation preservation notes.
- Routed tasks to line-review, portfolio-review, line-discovery, contradiction
  hunter, or landscape reassessment.

## Memory interface (Phase 3.5; may be inert)

- Reads: prior tournaments, recurring interpretation candidates, minority
  survival arguments, scoring pitfalls.
- Writes: `guidance_used`, `missing_guidance`, `confusion_or_conflict`,
  `observed_failure_mode`, `output_quality_signal`, `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** line registry, scorecard, persona clusters, decision history.
- **Writes:** none directly. Proposed lead/minority changes route to
  `govern/line-review`, `govern/portfolio-review`, or `govern/decision-review`.

## Procedure

1. **Declare corpus and interpretations.** Example interpretations:
   - TaF as observer epistemology;
   - TaF as information theory;
   - TaF as physics-adjacent reconstruction;
   - TaF as category theory of forgetting;
   - TaF as legitimacy/audit theory;
   - TaF as complexity science.
2. **Run independent advocate passes.** Each advocate receives the same corpus
   and argues why its interpretation explains the repo best.
3. **Score each interpretation.** Criteria:
   - artifact coverage;
   - quality of generated next tasks;
   - falsifiability;
   - overclaim avoidance;
   - external-field connection;
   - publishability;
   - transformative potential if true.
4. **Judge and rank.** Produce a lead interpretation proposal and runner-up
   preservation notes.
5. **Stress the winner.** State what would make the lead lose next time.
6. **Route consequences.** Any standing, portfolio, discovery, or contradiction
   effects route to owner workflows.

## Outputs

**Interpretation scorecard:**

```yaml
interpretation_scorecard:
  interpretation:
  advocate_artifact:
  explains_artifacts:
  generated_tasks:
  falsifiability:
  overclaim_control:
  external_connection:
  publishability:
  transformative_if_true:
  total_judgment:
  strongest_evidence:
  weakest_point:
```

**Tournament result:**

```yaml
tournament_result:
  corpus:
  lead_interpretation:
  why_lead:
  runner_up_programs:
  minority_survival_arguments:
  tasks_generated:
  what_would_change_the_result:
  owner_routes:
```

Every run ends with the verdict block.

## Escalation triggers

Route to `govern/line-review` when scores imply line standing changes; to
`govern/portfolio-review` when interpretations imply split/merge/overlap; to
`explore/landscape-reassessment` when the lead interpretation changes the
landscape; to `explore/line-discovery` for new tasks that are really new lines;
to `exploit/contradiction-hunter` when the lead depends on a weak claim; to
`govern/decision-review` when the repo needs a policy for lead-interpretation
status.

## Failure modes

- **Winner as dogma.** The lead interpretation becomes truth. Guard: state what
  would make it lose.
- **Pluralism as chaos.** Every interpretation remains equal forever. Guard:
  score concrete criteria and name a lead.
- **Advocate contamination.** Advocates react to each other. Guard: independent
  advocate passes before judging.
- **Popularity scoring.** The frame with best rhetoric wins. Guard: require
  artifact coverage and generated tasks.
- **Runner-up erasure.** Minority programs vanish. Guard: preserve runner-up
  survival notes and next tests.
- **Truth by publishability.** Ease of publication becomes evidence. Guard:
  publishability is one criterion only.

## Success criteria

A good run names a current lead interpretation, preserves meaningful runner-up
programs, and produces tasks that reveal how the lead could lose.

Cheap auditability test: a reviewer can see how each interpretation scored on the
same criteria, what artifacts it explains, what tasks it generated, and what
would change the tournament result.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/tournament-corpus-select` - choose corpus and interpretations.
- `govern/tournament-advocate-pass` - one interpretation advocate.
- `govern/tournament-judge` - score and rank.
- `govern/tournament-route` - package lead/minority outputs.

Likely cadence differences:
- Slow periodic run after major landscape changes.
- Event-triggered by theory compression, contradiction clusters, or cross-repo
  bridge results.

Likely context boundaries:
- Advocates load the shared corpus and their interpretation only.
- Judge loads advocate outputs plus scoring criteria.

Likely deterministic vs judgment split:
- Deterministic: corpus list, criteria table, route-target existence.
- Judgment-based: scoring, lead selection, survival notes.

Phase 4 coverage questions:
- Do all advocates receive the same corpus?
- Is the winner accompanied by a loss condition?
- Are runner-up programs preserved with concrete next tests?
- Are line/portfolio implications routed instead of executed?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```
