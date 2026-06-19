---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: convergence_finding_and_candidate_proposal
summarizable: false
unit_of_review: one_synthesis_run
---

# Cross-Disciplinary Synthesis

**Family:** explore
**Mode:** search
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** existing exploration outputs across clusters (sprint runs,
incubation/ingestion notes, line artifacts, literature).
**Emits:** a **convergence map** (which independent disciplines arrived at the same
structure); candidate research lines → `explore/line-discovery` → `govern/line-intake`.

## Purpose

Find **independent convergences across distant persona clusters** — places where
different disciplines, using different vocabulary and formalisms, have arrived at
*structurally the same claim without coordinating*. Operating model §8 names this
the strongest positive signal the program has; this workflow is its dedicated
producer. Synthesis asks one question: **what patterns connect what we already
have?**

Synthesis is deliberately **distinct from `explore/landscape-reassessment`**.
Synthesis asks *what connects the existing pieces* (a pattern question over current
content); reassessment asks *how the topology of the whole landscape has changed*
(a structural question over the line graph). Synthesis can feed reassessment, but a
convergence finding is not by itself a landscape move. (Operating model §2,
"Landscape reassessment vs synthesis".)

This is **Search Mode**: it maximizes connection-finding and information gain, not
rigor or promotion. A convergence is a *signal to investigate*, not a validated
claim. Synthesis proposes candidate lines (routed through line-discovery →
line-intake) but registers nothing, scores no standing, and moves no lifecycle.

## Authority boundaries

- **May:** read exploration outputs across clusters; identify structural
  convergences and genuine tensions; produce a convergence map; propose candidate
  research lines arising from a convergence; flag convergences that warrant a
  landscape reassessment; emit governance signals for missing routes.
- **Must not:** register/number a line (→ `explore/line-discovery` →
  `govern/line-intake`); move lifecycle (→ govern); assign standing
  (→ `govern/line-review`); decide a claim is true/false or write the claim ledger;
  declare a convergence a *finding of physics* (it is an exploration signal);
  perform a landscape reassessment itself (→ `explore/landscape-reassessment`);
  count same-vocabulary agreement as convergence (that is coordination, not signal).
- **Scoring authority:** judgment-with-rationale, descriptive — synthesis rates a
  convergence's *strength* (distance between clusters, number of independent
  formalisms, structural sameness), not a line's standing.
- **Write authority:** patch-first / proposal-only. The convergence map is written
  as a non-canonical synthesis log; candidate lines are *proposals* routed onward;
  no canonical registry write.

## Read surfaces

- **Exploration corpus (the raw material):** recent `explorations/` (persona-idea-
  sprint runs and their convergence maps), `logs/synthesis/`, incubation reports,
  foundation `literature/` notes.
- **Line artifacts across clusters:** the `models/`, `results/`, `tests/`, `claims/`
  of existing `RL-NNN` lines — to compare structures, not statuses.
- **Cluster map (distance check):** `registries/persona-clusters.md` — to verify a
  convergence spans **distant** clusters, not one cluster in several vocabularies.
- **Sprint machinery:** `agent-skills/persona-idea-sprint.md` — its
  cross-persona convergence map is a primary input; synthesis may re-invoke it for a
  focused pass or read its prior output.
- **Line registry:** `registries/line-registry.md` — to relate convergences to
  existing lines and avoid re-proposing covered ground.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — cross-cluster
  reasoning (§8), synthesis-vs-reassessment (§2), Search Mode (§1), information-gain
  (§3), authority order (§11).
- **Decision History:** `registries/decision-history.md` — constraints.
- **Workflow catalog:** `README.md` / `WORKFLOW-SKELETON-PROPOSAL.md` — validate routes.
- Explore Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- A **convergence map** (synthesis log, operational) to `logs/synthesis/` —
  non-canonical.
- **Candidate research lines** → `explore/line-discovery` (which de-dups and
  forwards to `govern/line-intake`).
- **Reassessment flags** → `explore/landscape-reassessment` when a convergence
  implies the landscape topology has shifted.
- **Governance signals** → the docket.

**No canonical write.** Convergences are signals; lines route through discovery/intake.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): convergence patterns already surfaced (so a "new"
  convergence is not last quarter's restated), known false-convergence traps
  (same-vocabulary coordination), prior synthesis-quality signals.
- Writes (learning-return, after a run): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** `persona-clusters.md` (distance), `line-registry.md` (existing-line
  relation), `decision-history.md` (constraints).
- **Writes:** none to canonical state. Convergence map → synthesis log; candidate
  lines → line-discovery; appends a run log.

## Procedure (runnable scope: one synthesis run)

1. **Assemble the corpus.** Gather recent exploration outputs spanning multiple
   clusters (sprint maps, incubation reports, literature notes, line artifacts).
   State the scope of this run (whole-corpus, or a focus area).
2. **Extract structural claims, vocabulary-stripped.** For each piece, state its
   *structural* claim independent of disciplinary vocabulary — what relation/shape
   it asserts — so that matches are on structure, not words.
3. **Find convergences (and tensions).** Group structural claims that match across
   **distant clusters**. For each group, record the contributing clusters, the
   distinct formalisms, and the shared structure. Separately record genuine
   *tensions* (distant clusters that structurally disagree) — these are also
   information.
4. **Reject manufactured convergence.** Discard any "convergence" where the
   agreeing sources share vocabulary or a single underlying model — same words mean
   coordination, not independent convergence (§8). Note the rejection.
5. **Propose candidate lines.** Where a real convergence opens a new line of
   inquiry not already in the registry, draft a candidate-line proposal and route it
   to `explore/line-discovery`. Where it instead implies the landscape has shifted,
   flag `explore/landscape-reassessment`.
6. **Emit.** Convergence map, candidate-line proposals, reassessment flags, run log,
   governance signals. End with the verdict block.

## Outputs (shapes)

**Convergence map** (synthesis log): for each convergence —

```yaml
convergence:
  shared_structure:           # the vocabulary-stripped claim/relation
  contributing_clusters:      # >=2 DISTANT clusters (per persona-clusters.md)
  distinct_formalisms:        # the different languages used (must differ)
  strength: weak | moderate | strong   # by cluster-distance x independent-formalism count
  relation_to_existing_lines: # supports / pressures / opens-new vs RL-NNN
  candidate_line_proposed: yes | no
  manufactured_convergence_check: passed   # vocabulary/model independence confirmed
```

Plus a **tensions** list (distant clusters that structurally disagree) with the
same independence check.

**Candidate-line proposal** (routed to `explore/line-discovery`): a pre-`candidate_
seed` payload — working title, the convergence it rests on, contributing clusters,
why it is not already covered, suggested next move.

**Governance docket item** (missing route / policy gap): standard shape with
`signal_type` ∈ {undefined-workflow-needed, convergence-threshold-needed,
manual-review-required}.

Every run ends with the verdict block.

## Escalation triggers

Route OUT: a convergence that should become a line → `explore/line-discovery`
(→ `govern/line-intake`); a convergence implying topology change →
`explore/landscape-reassessment`; a convergence that pressures an existing claim →
the claim surface / `exploit/challenge-primary`; a convergence needing a discipline
the panel lacks → `explore/persona-expansion`; a tension severe enough to be a
lifecycle signal → `govern/line-review` (it scores standing; synthesis does not);
missing route → `undefined-workflow-needed`; registry/authority conflict →
`confusion_or_conflict`, defer to §11.

## Failure modes

- **Manufactured convergence.** Same-vocabulary or single-model agreement counted
  as independent convergence. Guard: vocabulary-stripped structural extraction +
  explicit independence check (steps 2, 4); distant-cluster requirement.
- **Synthesis/reassessment conflation.** Synthesis quietly starts re-surveying the
  whole landscape. Guard: synthesis answers "what connects existing pieces"; topology
  change routes to landscape-reassessment (§2).
- **Convergence treated as a finding of physics.** Guard: Search Mode; a convergence
  is a signal to investigate, not a validated claim; it routes to discovery/intake.
- **Re-surfacing old convergences as new.** Guard: read prior synthesis logs / memory;
  the run log states what is new vs already-surfaced.
- **Authority creep.** Synthesis registers a line or scores standing. Guard:
  proposal-only; lines route through discovery/intake; standing is line-review's.
- **Tensions discarded.** A real cross-cluster disagreement is dropped because it is
  not a convergence. Guard: tensions are a first-class output (also information, §3).

## Success criteria

A good run yields a convergence map in which each entry is a **genuine,
independence-checked structural agreement across distant clusters** (or a genuine
tension), each tied to existing content, with any line-worthy convergence routed to
discovery and any topology-shifting convergence routed to reassessment.

Cheap test: a reviewer can tell, for each convergence, *which distant clusters and
which distinct formalisms* support it, why it is not just one discipline restated,
whether it is new vs previously surfaced, and where each consequence was routed.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `explore/synthesis-corpus-assemble` — gather recent cross-cluster outputs;
  **mostly deterministic** (collect + scope).
- `explore/synthesis-structural-extract` — pieces → vocabulary-stripped structural
  claims; judgment-based.
- `explore/synthesis-convergence-match` — structural claims → convergence map +
  independence check + tensions; judgment-based; the analytic core.
- `explore/synthesis-route` — convergences → candidate-line proposals + reassessment
  flags; deterministic packaging.

Likely cadence differences:
- Periodic (after enough new exploration has accumulated), or event-triggered after
  a `persona-idea-sprint` or a batch of foundation ingestions.

Likely context boundaries:
- Assemble loads the corpus index; structural-extract loads pieces in batches;
  convergence-match loads only the extracted structural claims + cluster map (cheap);
  route loads only the map.

Likely deterministic vs judgment split:
- Deterministic: corpus assembly, cluster-distance lookup, route-target existence,
  new-vs-old check against prior synthesis logs.
- Judgment-based: structural extraction, convergence detection, independence
  adjudication, strength rating, candidate-line framing.

Phase 4 coverage questions:
- Does every convergence have a downstream consumer? (line-worthy → discovery;
  topology → reassessment; claim-pressuring → claim surface.)
- Does every convergence pass an explicit independence check?
- Are tensions preserved, not just convergences?
- Is synthesis kept distinct from reassessment (no double-survey of the landscape)?
- Is the convergence-match seam (expensive) separable from assembly/route for cadence?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Convergence strength threshold** — how distant must clusters be, and how many
   independent formalisms required, before a convergence is "strong" enough to
   propose a line? (Docketed: `convergence-threshold-needed`.)
2. **Synthesis ↔ reassessment handoff** — exact trigger that makes a convergence a
   *reassessment* flag rather than a *line* proposal; reconcile with
   `explore/landscape-reassessment`'s intake.
3. **Independence test mechanics** — how is "same model in different words" detected
   reliably (beyond shared vocabulary)? Needs worked examples before automation.
4. **Corpus freshness window** — how far back the corpus should reach so old
   convergences are not re-surfaced as new.
