---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: persona_addition_proposal
summarizable: false
unit_of_review: one_persona_expansion_proposal
---

# Persona Expansion

**Family:** explore
**Mode:** search
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** persona-gap signals (from `foundation-ingestion`, sprint runs,
synthesis, or a recurring blind spot) plus the canonical persona system.
**Emits:** **persona addition/refinement proposals** → `govern/persona-governance`
(which reviews, clusters, and integrates).

## Purpose

Widen the program's *review coverage* by **proposing new persona lenses and
numbered experts** (or refinements to existing ones) when repeated research exposes
a missing discipline or a recurring blind spot. Persona maintenance is itself an
Explore activity (operating model §6): expanding the persona set expands the kinds
of ideas and critiques the program can generate, so it widens the search space.

Expansion **proposes**; it does not integrate. The boundary mirrors the rest of the
family: the workflow that *finds* a coverage gap is not the workflow that *commits*
a persona to the canonical system. Cluster assignment, normalization weighting,
canonical-source/skill-mirror synchronization, and registry integrity belong to
`govern/persona-governance` (operating model §6–§8; DEC-006 keeps
`personas/EXPERT-PANEL.md` canonical with the skill `references/personas.md` as a
mirror). Expansion's output is a well-formed proposal that persona-governance can
accept, refine, defer, or reject.

This is **Search Mode**: it maximizes coverage and discipline-distance, favoring
lenses that would let the program *see failure modes it currently cannot*. It does
not score lines, does not vote, and does not edit the canonical persona files
directly.

## Authority boundaries

- **May:** read the canonical persona system and the cluster map; read persona-gap
  signals; propose a new lens (posture) for `personas/INDEX.md`; propose a new
  numbered expert for `personas/EXPERT-PANEL.md`; propose a refinement/deprecation
  of an existing persona; suggest a candidate cluster for a proposed persona (as a
  *suggestion*, not an assignment); emit governance signals for missing routes.
- **Must not:** edit `personas/EXPERT-PANEL.md` or `personas/INDEX.md` canonical
  content directly; assign or change cluster membership / normalization weights
  (→ `govern/persona-governance`); edit the skill mirror by hand (DEC-006 —
  governance/build script owns sync); number a persona authoritatively (governance
  allocates the canonical number); use personas as evidence or authorities (operating
  model §6); score lines or vote.
- **Scoring authority:** judgment-with-rationale, descriptive — expansion argues a
  lens's *coverage value* and *discipline-distance*, not any line's standing.
- **Write authority:** patch-first / proposal-only for all persona files. The only
  net-new artifact it may write directly is its **proposal/run log** (non-canonical);
  every persona change is a proposal to `govern/persona-governance`.

## Read surfaces

- **Canonical persona system:** `personas/EXPERT-PANEL.md` (numbered experts 1–62,
  canonical) and `personas/INDEX.md` (lens registry / postures).
- **Cluster map:** `registries/persona-clusters.md` — the seven clusters, current
  assignments, the **unmapped/cross-cutting gap** (causal inference, physics-informed
  ML, evolutionary/systems biology, neuro, cognitive, ecology) it already flags.
- **Gap signals (the trigger material):** persona `candidate_flag`s from
  `explore/foundation-ingestion`; recurring blind spots noted in sprint runs
  (`agent-skills/persona-idea-sprint.md` outputs) and `logs/synthesis/`; a direct
  user request.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — persona governance
  (§6), voting/cross-cluster reasoning (§7–§8), Search Mode (§1), authority order (§11).
- **Decision History:** `registries/decision-history.md` — DEC-006 (canonical panel +
  mirror), persona-related constraints.
- **Panel skill:** `agent-skills/time-as-finality-persona-panel/` and its
  `scripts/build_panel_prompt.py` — to understand how a new numbered persona would be
  consumed (read, not edited).
- **Workflow catalog:** `README.md` / `WORKFLOW-SKELETON-PROPOSAL.md` — validate routes.
- Explore Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- A **persona-expansion proposal** → `govern/persona-governance` (the deliverable).
- A **proposal/run log** (operational log) to `logs/` — non-canonical.
- **Governance signals** → the docket.

**No canonical persona write.** Lens text, expert entries, numbering, clustering,
and skill-mirror sync are all governance-owned (DEC-006).

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): coverage gaps repeatedly flagged but not yet filled,
  proposed personas previously rejected (and why), recurring blind-spot patterns.
- Writes (learning-return, after a run): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** `persona-clusters.md`, `personas/EXPERT-PANEL.md`, `personas/INDEX.md`,
  `decision-history.md`.
- **Writes:** none to canonical persona files. Proposals → `govern/persona-governance`;
  appends a run log.

## Procedure (runnable scope: one persona-expansion proposal set)

1. **Gather gap signals.** Collect the persona-gap signals driving this run
   (ingestion flags, recurring sprint/synthesis blind spots, the documented
   cluster-coverage gap, or a user request). State the gap precisely: *what failure
   mode or discipline is the current panel unable to voice?*
2. **De-duplicate against existing coverage.** Check each gap against the existing
   62 experts and the lens families. Discard gaps already covered (log why); keep
   genuine gaps.
3. **Decide lens vs numbered expert (proposal-level).** For each genuine gap, judge
   whether it warrants a **lens** (a reusable posture, lighter weight, lives in
   `INDEX.md`) or a **numbered expert** (a named scoring participant in
   `EXPERT-PANEL.md`) — and state the criterion used. This is a *recommendation*;
   governance makes the call.
4. **Draft the persona and a suggested cluster.** Write the proposed lens/expert in
   the existing house style (definition, best use, misuse risk for a lens; the
   panel's section style for an expert). Suggest which of the seven clusters it would
   join, or flag that it needs a new cluster (the documented gap).
5. **Emit the proposal.** Route the proposal set to `govern/persona-governance`.
   End with the verdict block.

## Outputs (shapes)

**Persona-expansion proposal** (one per proposed persona; routed to
`govern/persona-governance`):

```yaml
persona_proposal:
  proposed_kind: lens | numbered_expert
  working_name:
  discipline_gap:            # the failure mode / discipline the panel cannot voice
  why_not_already_covered:   # de-dup basis vs the 62 experts + lens families
  draft_text:                # lens row (definition/best-use/misuse-risk) or expert section
  suggested_cluster:         # one of the seven, or "needs-new-cluster: <reason>"
  origin:                    # foundation-ingestion-flag | sprint-blindspot | synthesis | user
  source_report:
  recommended_action: add | refine_existing:<#/name> | deprecate:<#/name> | defer
  confidence: low | med | high
  why_expansion_cannot_decide: "expansion proposes coverage; clustering, numbering, weighting, and mirror sync are governance-owned (DEC-006, ROM §6)."
```

**Proposal/run log** (operational log): gap signals consumed, de-dup results,
lens-vs-expert reasoning, proposals emitted, route.

**Governance docket item** (missing route / policy gap): standard shape with
`signal_type` ∈ {undefined-workflow-needed, lens-vs-expert-criterion-needed,
new-cluster-needed, manual-review-required}.

Every run ends with the verdict block.

## Escalation triggers

Route OUT: every persona add/refine/deprecate → `govern/persona-governance`; a gap
that is really a *new cluster* need (the documented biology/neuro/cognitive/ecology
gap) → `govern/persona-governance` with `new-cluster-needed`; a gap that is really a
missing *research line* rather than a missing lens → `explore/line-discovery`; a gap
surfaced by a foundation neighbor → trace back to the `foundation-ingestion` flag
and confirm; missing route → `undefined-workflow-needed`; registry/authority
conflict (e.g. canonical vs mirror drift) → `confusion_or_conflict`, defer to §11
and flag persona-governance (which owns sync).

## Failure modes

- **Inventing a replacement persona list.** Operating model §6 forbids it. Guard:
  read and extend the existing 62 experts + lens families; de-dup mandatory; never
  propose a parallel registry.
- **Editing canonical persona files / the skill mirror directly.** Guard:
  proposal-only; DEC-006 makes governance/build-script the owner of canonical text,
  numbering, and mirror sync.
- **Persona-as-authority.** A proposed lens framed as evidence. Guard: personas are
  reusable postures, not authorities (§6); the proposal argues coverage, not truth.
- **Lens/expert confusion.** Proposing a numbered expert where a lighter lens
  suffices (or vice versa). Guard: explicit lens-vs-expert criterion in step 3;
  governance makes the final call.
- **Rhetorical-flavor lenses.** A lens with no testable consequence (INDEX.md's own
  misuse caution). Guard: every proposed lens must name a misuse risk and a failure
  mode it would help catch.
- **Re-proposing rejected personas.** Guard: read memory/prior proposals; the run
  log states what is new vs previously rejected.
- **Dangling route / silent loss.** Guard: every gap reaches a disposition in the
  run log; missing route → `undefined-workflow-needed`.

## Success criteria

A good run turns genuine, de-duplicated coverage gaps into **well-formed persona
proposals** — each in house style, with a clear discipline-distance argument, a
named failure mode it would help catch, a suggested cluster, and a lens-vs-expert
recommendation — all routed to `govern/persona-governance`, with no canonical
persona file touched.

Cheap test: a reviewer can tell, without re-deriving it, what failure mode the new
persona would let the program catch, why the existing 62 experts/lenses do not
already cover it, whether it should be a lens or a numbered expert, and which
cluster it would join — and confirm no canonical persona file was edited.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `explore/persona-gap-collect` — gather + de-dup gap signals vs existing coverage;
  **mostly deterministic** (match against the 62 experts + lens families).
- `explore/persona-draft` — one genuine gap → a drafted lens/expert + suggested
  cluster + lens-vs-expert recommendation; judgment-based.
- `explore/persona-proposal-emit` — proposals → routed to `govern/persona-governance`
  + run log; deterministic packaging.

Likely cadence differences:
- Event-triggered (when ingestion flags a persona, or a recurring blind spot
  crosses a threshold) rather than periodic; persona churn should be slow (§6: add
  for under-represented disciplines, rarely remove).

Likely context boundaries:
- Collect loads the persona system + gap signals; draft loads the relevant cluster +
  house-style exemplars; emit loads only the drafted proposals. The full panel text
  is read for de-dup, not regenerated.

Likely deterministic vs judgment split:
- Deterministic: de-dup against existing experts/lenses, route-target existence,
  new-vs-previously-rejected check, presence of misuse-risk/failure-mode fields.
- Judgment-based: gap identification, lens-vs-expert decision, draft text, suggested
  cluster, discipline-distance argument.

Phase 4 coverage questions:
- Does every persona proposal have a destination? (→ `govern/persona-governance`.)
- Does every gap reach a disposition (proposed / covered / deferred)?
- Does every proposed lens name a misuse risk + a failure mode it helps catch?
- Is canonical persona text / numbering / mirror sync owned only by governance (never here)?
- Is the slow-churn cadence respected (no persona-list thrash)?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Lens-vs-expert criterion** — the precise rule for when a coverage gap warrants
   a numbered expert vs a lighter lens. (Docketed: `lens-vs-expert-criterion-needed`;
   shared with `govern/persona-governance`.)
2. **New-cluster decision** — the documented coverage gap (causal inference,
   physics-informed ML, evolutionary/systems biology, neuro, cognitive, ecology):
   add an eighth+ cluster, or accept best-fit? Owned by `govern/persona-governance`;
   expansion only surfaces and proposes. (Docketed: `new-cluster-needed`.)
3. **Numbering allocation** — confirm governance (not expansion) allocates the next
   canonical expert number and drives the skill-mirror rebuild (DEC-006).
4. **Deprecation pathway** — expansion may *propose* deprecating/merging a persona;
   confirm governance owns the deprecation mechanics that preserve historical
   numbering (EXPERT-PANEL "Panel Evolution").
