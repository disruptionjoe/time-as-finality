---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: registry_addition_proposal
summarizable: false
unit_of_review: one_candidate_line
---

# Line Intake

**Family:** govern
**Mode:** evaluation
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** research-line **seeds** from `explore/line-discovery` (and
`explore/cross-disciplinary-synthesis`); manual line proposals from an authorized
source.
**Scope:** Validate **one candidate line** and either propose adding it to the line
registry as a new `RL-NNN` (patch-first), route it out (duplicate / structural), or
reject it with rationale.

## Purpose

`line-intake` is the **front door** for new research lines. It exists so that line
*creation* is a governed, auditable act rather than an ad-hoc registry edit:
explore workflows generate seeds, but a seed must be validated, deduped against the
existing portfolio, and shaped into a well-formed registry entry before it becomes a
tracked research line.

It governs: the **creation/bootstrapping** of a new research line — validating a
candidate, deduping it against existing lines, and proposing a new `RL-NNN`
line-registry entry at `stage: seed`, `status: active` (the bottom of the maturity
ladder).

It does **not** govern: any maturity beyond `seed` (advancement is
`explore/line-incubation` then `govern/lifecycle-review`); single-line standing
(`line-review`); cross-line structure or overlap *resolution* (`portfolio-review`);
lifecycle moves (`lifecycle-review`); decision-history promotion (`decision-review`).

A successful run answers: *is this candidate a genuinely new, well-formed research
line that should enter the registry at seed — and if so, what is the registry-
addition patch a reviewer can accept?* It does not answer whether the line is
promising beyond the bar for tracking it, and it never assigns maturity above seed.

## Core invariant

Line Intake **creates at seed, never above.** Every accepted candidate enters the
registry at `stage: seed`, `status: active` — the minimum maturity. Maturity is
*earned later* through evidence (incubation, then lifecycle-review), never granted
at intake. Intake is **patch-first**: it proposes a registry ADD applied by an
authority/accept step and never mutates the registry itself. Provenance (which seed,
from which explore run or human) is preserved on every proposal.

## Conservative default

When a candidate is malformed, a probable duplicate, or its distinctness from
existing lines is unclear, the default is: **do not add, route or hold cleanly.** A
candidate that overlaps an existing line is **not** silently merged or rejected — it
is routed to `portfolio-review` as an overlap question (the owner of cross-line
structure). If a required downstream workflow does not exist, Line Intake leaves the
registry unchanged, emits a docket item with `signal_type: undefined-workflow-needed`,
and preserves the candidate.

## Relationship to explore, portfolio-review, and lifecycle

- `explore/line-discovery` and `explore/cross-disciplinary-synthesis` **produce
  seeds** — raw candidate lines — but do not write the registry. They route seeds
  here.
- Line Intake **validates and dedupes**. A clean, novel candidate → a registry ADD
  proposal at seed. A candidate that **overlaps** an existing line → routed to
  `portfolio-review` (which owns overlap resolution: merge into the existing line,
  demarcate, or accept as distinct). Intake does not itself resolve overlap; it only
  *detects* it.
- After a line exists at seed, **advancement is not Intake's job**:
  `explore/line-incubation` matures early-lifecycle lines and `govern/lifecycle-
  review` performs stage/status moves. Intake's authority ends at `stage: seed`.

## Candidate-line taxonomy

```yaml
candidate_source_type:
  - discovery-seed        # from explore/line-discovery
  - synthesis-seed        # from explore/cross-disciplinary-synthesis
  - manual-proposal       # from an authorized human/governance source
```

The source type only affects provenance and how much shaping the candidate needs;
all three follow the same validation → dedupe → propose path.

## Canonical candidate-line encoding

```yaml
candidate_line:
  proposed_title:
  one_line_question:        # the distinct line of inquiry, stated as a question
  rationale:                # why this is worth tracking as a line
  candidate_source_type: discovery-seed | synthesis-seed | manual-proposal
  source_workflow_or_author:
  source_report:
  seed_artifacts:           # any existing tests/results/notes that motivate it (may be empty)
  suspected_relationships:  # optional: depends_on / supports / competes_with / extends / imports to existing RL-NNN
  evidence_or_basis:
  confidence: low | med | high
```

Intake normalizes legacy aliases:

```yaml
legacy_or_flag_aliases:
  new-line-seed:     { candidate_source_type: discovery-seed }
  synthesis-line:    { candidate_source_type: synthesis-seed }
  proposed-line:     { candidate_source_type: manual-proposal }
```

If the candidate cannot be normalized into a single intelligible line of inquiry,
emit an intake failure and stop.

## Authority boundaries

- **May:** read the line registry, health substrate, persona clusters, information
  portfolio, foundation queue, and authority surfaces; validate one candidate line;
  dedupe it against existing lines; propose a new `RL-NNN` registry **ADD** at
  `stage: seed`, `status: active` (patch-first); propose `suspected_relationships`
  edges to existing lines (as part of the ADD proposal, for portfolio-review to
  later reconcile); route overlap to `govern/portfolio-review`; emit
  `govern/decision-review` signals when intake repeatedly hits a schema/policy gap;
  emit governance docket items; preserve unresolved candidates.
- **Must not:** write the registry directly (patch-first only); assign any `stage`
  above `seed` or any `status` other than `active` at creation; resolve overlap or
  perform merges (→ `portfolio-review`); move lifecycle states (→ `lifecycle-
  review`); compute or assert standing (→ `line-review`); promote to Decision
  History (→ `decision-review`); restate claim/roadmap/hypothesis status (DEC-007);
  invent a stage/status not in the registry schema; create a line that duplicates an
  existing one; delete or overwrite an existing line.
- **Scoring authority — hybrid:** deterministic for well-formedness checks,
  next-RL-number assignment, title/artifact-overlap detection against existing
  lines, relationship-target existence; judgment (with rationale) for whether a
  candidate is genuinely distinct and worth tracking.
- **Write authority — patch-first; output_authority: registry_addition_proposal.**
  Its highest-authority output is a *proposed* new registry entry, inert until
  accepted.

## Read surfaces

- **Line registry:** `registries/line-registry.md` — the full current portfolio,
  to assign the next `RL-NNN`, dedupe against existing titles/questions/artifacts,
  and validate `suspected_relationships` targets. **Read-only here.**
- **Health substrate:** `registries/research-line-scorecard.md` — for context on
  what lines already cover (not scored at intake).
- **Persona clusters:** `registries/persona-clusters.md` — to note which discipline
  cluster(s) a candidate plausibly engages (provenance only; not a balance decision,
  which is portfolio-review's job).
- **Information portfolio:** `registries/information-portfolio.md` — to check the
  candidate is not re-opening an archived line whose information gain already
  settled the question (which would instead be a `revive` for `lifecycle-review`).
- **Foundation queue:** `registries/foundation-queue.md` — synthesis seeds often
  trace to queued reading; preserve that provenance.
- **Authority surfaces:** `CLAIM-LEDGER.md`, `ROADMAP.md`, `HYPOTHESES.md`,
  `../NORTH-STAR.md` — to confirm the candidate aligns with the program and is not
  already an existing claim/hypothesis.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — lifecycle ontology
  (§4: seed is the entry stage), authority order (§11), workflow/task split (§13).
- **Decision History:** `registries/decision-history.md` — constraints (DEC-007
  portfolio-layer, DEC-018/DEC-020 two-axis model).
- **Workflow catalog / skeleton:** `README.md`, `WORKFLOW-SKELETON-PROPOSAL.md` —
  to validate route targets.
- **Govern Memory Pack load surface** (Phase 3.5; inert if absent).

## Write surfaces

- A **line intake report** (the run's primary artifact).
- A **registry-addition patch proposal** — a fully-drafted new `RL-NNN` entry at
  `stage: seed`, `status: active`, **addressed to an authority/accept step**, never
  appended to the registry by this workflow.
- An **overlap question** → `govern/portfolio-review` (when the candidate overlaps an
  existing line).
- A **revive candidate** → `govern/lifecycle-review` (when the candidate re-opens an
  archived line rather than being new).
- **Governance docket items** → consumed by `govern/decision-review` (for schema /
  policy / undefined-workflow gaps).
- A **Project Log entry** text (orchestrator appends to `PROJECT-LOG.md`).

**Patch target.** The only canonical surface a Line Intake output targets is
`registries/line-registry.md`, and only as an **ADD proposal applied by an accept
step** — never a direct write. The proposal sets `stage: seed`, `status: active`,
the why-state, artifact links, and any `suspected_relationships`; it never sets
claim/roadmap/hypothesis status (DEC-007).

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): recurring intake heuristics, known duplicate-prone topics,
  prior false-new lines that were actually revivals, naming/scoping anti-patterns.
- Writes (learning-return, after acceptance): `pack_ref`, `work_ref`, `round_ref`,
  `guidance_used`, `missing_guidance`, `confusion_or_conflict`,
  `observed_failure_mode`, `output_quality_signal`, `suggested_summary_update`.
- Does not depend on memory existing; the Memory Pack is guidance only and never
  outranks an authority surface (ROM §11).

## Registry interactions

- **Reads:** line-registry (dedupe + next number + relationship targets),
  research-line-scorecard, persona-clusters, information-portfolio, foundation-queue,
  decision-history.
- **Writes:** proposes a new `RL-NNN` ADD to line-registry (patch-first; applied by
  an accept step, **not** by this workflow). Writes nothing else canonical; never
  edits claim/roadmap/hypothesis status (DEC-007).
- **Docket:** emits governance docket items for schema/policy/undefined-workflow
  gaps; routes overlap and revive cases to their owning workflows.

## Procedure (runnable scope: one candidate line)

0. **Intake and candidate validation.** Confirm the `candidate_line` object exists;
   source type is recognized or normalizable; `one_line_question` is intelligible as
   a distinct line of inquiry; rationale + evidence basis present;
   source workflow/author present; `suspected_relationships` (if any) point at
   existing lines. On failure, emit an intake-failure report and stop.
1. **Load registry and authority context** — full line registry, health substrate,
   persona clusters, information portfolio, foundation queue, authority surfaces,
   Decision History, Research Operating Model, workflow catalog, Project Log. If
   required context is unavailable, emit `outcome_class: manual_review_required`.
2. **State the intake question precisely** — "Is `<one_line_question>` a genuinely
   new research line that should enter the registry at seed?" The question must be
   explicit before continuing.
3. **Dedupe against the existing portfolio** (the central step):
   - **Exact/near duplicate of an active line** → do not add; route to
     `portfolio-review` as an `overlap` question (the candidate may belong inside an
     existing line). Outcome `overlap_routed`.
   - **Re-opens an archived line** (matches an `RL-NNN` with `status: archived`,
     and the archival's information-gain entry does not already foreclose it) →
     route to `lifecycle-review` as a `revive` candidate, not a new line. Outcome
     `revive_routed`.
   - **Partial overlap** (shares some scope but poses a distinct question) → may
     propose as a new line **with** `suspected_relationships` edges, and note the
     overlap for portfolio-review to reconcile later. Outcome may be
     `add_proposed` plus a portfolio-review note.
   - **Genuinely novel** → proceed to propose.
4. **Validate well-formedness for a registry entry** — a clear title, a one-line
   question, a why-state (why it is worth tracking), at least a pointer to motivating
   evidence/artifacts (may be a foundation-queue item), and plausible discipline
   cluster(s). Alignment with North Star / ROM (a line that contradicts North Star
   is rejected with rationale, not added).
5. **Choose one primary outcome class:**

   ```yaml
   outcome_class:
     - add_proposed              # new RL-NNN ADD proposal at seed/active
     - overlap_routed            # duplicate/overlap → portfolio-review
     - revive_routed             # re-opens an archived line → lifecycle-review
     - rejected_with_rationale   # malformed, off-North-Star, or not a line
     - hold_for_more_basis       # plausible but under-specified; preserved
     - manual_review_required
   ```

   One is primary; when distinctness is unclear, prefer `overlap_routed` over a
   speculative new line.
6. **Draft the registry-addition proposal** (if `add_proposed`):

   ```yaml
   registry_addition_proposal:
     proposed_rl_number:       # next available RL number, read from line-registry
     proposed_title:
     stage: seed               # invariant — never above seed
     status: active            # invariant at creation
     mode_bias: search | evaluation | both
     why_this_stage:           # "newly seeded from <source>; not yet explored"
     one_line_question:
     seed_artifacts:           # links (may be a foundation-queue pointer)
     suspected_relationships:  # edges to existing RL-NNN (for portfolio-review to reconcile)
     maps_to_authoritative:    # CLAIM-LEDGER / ROADMAP / HYPOTHESES pointers if any
     provenance:               # source workflow/author + source report
     confidence: low | med | high
     requires_acceptance_by:   # authority/accept step (never line-intake itself)
     patch_required: true
   ```

   The drafted entry must match the live `line-registry.md` entry format (title
   heading, Stage/Status/Mode-bias line, Why-this-stage, Artifacts, Maps-to,
   Relationships, Next candidate move) so the accept step can paste it in directly.
7. **Emit the ADD patch proposal** addressed to the accept step. Do not write the
   registry in v1.0.
8. **Route overlap/revive cases** to their owning workflows and **emit governance
   docket items** for anything it cannot resolve:

   ```yaml
   governance_docket_item:
     issue:
     affected_line:           # the candidate (or the existing line it overlaps)
     signal_type:
     authority_surfaces_involved:
     why_line_intake_cannot_resolve:
     recommended_owner_workflow:
     evidence_or_basis:
   ```

   Typical `signal_type`: schema-inadequacy, undefined-workflow-needed,
   manual-review-required, overlap-resolution-policy-needed,
   intake-bar-policy-needed.
9. **Preserve the candidate** with `candidate_status`: add_proposed_pending_acceptance
   | routed_to_other_workflow | rejected_with_rationale | held_for_more_basis. No
   candidate disappears silently.
10. **Emit report and Project Log entry text.** End with the verdict block.

## Outputs (shapes)

### Line Intake Report

```markdown
# Line Intake Report
## Review Metadata
- Workflow / version / run date / trigger / candidate source / proposed title:
## Candidate Validation
- Valid? / normalized source type / intake issues:
## Intake Question
- "Is <one_line_question> a genuinely new research line for seed?":
## Dedupe Result
- Exact duplicate? / archived-line revival? / partial overlap (which RL)? / genuinely novel?:
## Well-Formedness & Alignment
- Title / question / why-state / motivating evidence / cluster(s) / North Star & ROM alignment:
## Outcome
- Outcome class / rationale / confidence:
## Registry Addition Proposal (if any)
- Drafted RL-NNN entry at seed/active + proposal wrapper / requires acceptance by:
## Routed Items
- Overlap → portfolio-review / revive → lifecycle-review:
## Governance Docket Items Emitted
- New items (with signal_type):
## Candidate Disposition
- Candidate status / where preserved or routed:
## Project Log Entry
- Summary / output pointers:
```

Every run ends with the verdict block.

## Escalation triggers

Escalate rather than act when: the candidate duplicates or overlaps an existing
line (→ `portfolio-review`); the candidate re-opens an archived line
(→ `lifecycle-review` as a revive); the candidate contradicts North Star
(→ reject with rationale); the registry schema cannot express the candidate's needed
fields (→ schema docket → `decision-review`); intake repeatedly faces an unclear
"is this worth tracking" bar (→ `intake-bar-policy-needed` docket → `decision-
review`); a route has no owning workflow (→ `undefined-workflow-needed`); required
context is unavailable (→ manual review).

## Failure modes

- **Creating a duplicate line.** Guard: dedupe step is mandatory; overlap routes to
  portfolio-review rather than minting a parallel line.
- **Granting maturity at intake** (seeding above `seed`). Guard: the core invariant
  — `stage: seed`, `status: active` always; maturity is earned later.
- **Reviving an archived line as "new."** Guard: dedupe checks archived lines +
  their information-portfolio entries; revivals route to lifecycle-review.
- **Direct registry write.** Guard: patch-first; ADD applied by an accept step.
- **Resolving overlap itself** (merging into an existing line). Guard: intake
  detects overlap but never resolves it; portfolio-review owns resolution.
- **Status drift** (writing claim/roadmap/hypothesis status into the entry). Guard:
  DEC-007 — the entry links out; intake never restates those surfaces.
- **Off-North-Star line admitted.** Guard: alignment check; contradiction → reject
  with rationale.
- **Schema improvisation** (inventing a stage/status/field). Guard: schema-
  inadequacy routes to a decision-review docket; no improvised vocabulary.
- **Silent candidate loss.** Guard: every candidate carries a `candidate_status`.
- **Dangling route.** Guard: emit `undefined-workflow-needed`, leave registry
  unchanged, preserve candidate.

## Success criteria

A good run yields, for one candidate line: a clear intake question, a defensible
dedupe result (genuinely new vs duplicate vs archived-revival vs partial overlap),
a well-formedness and North Star/ROM alignment check, and — if novel — a fully-
drafted `RL-NNN` ADD proposal at seed/active in the live registry format that a
reviewer can accept or reject in one read, with provenance preserved. Overlap and
revival cases are routed to their owners; no candidate is lost.

Cheap auditability test: a reviewer can tell, without scanning the whole registry by
hand, whether the candidate is genuinely new, where it would sit (seed/active, which
relationships), why it is worth tracking, and — if it was not added — exactly which
workflow now owns it.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/candidate-line-intake` — one seed/proposal → validated/normalized
  candidate or intake failure; mostly deterministic.
- `govern/line-dedupe-check` — one candidate vs the whole registry → duplicate /
  archived-revival / partial-overlap / novel verdict; hybrid (deterministic
  title/artifact match + judgment on distinctness).
- `govern/line-add-proposal` — one novel candidate → drafted `RL-NNN` ADD proposal
  at seed/active; judgment-based.
- `govern/line-add-acceptance` — one accepted proposal → append the `RL-NNN` entry +
  Project Log; **requires explicit authority** (the only atom that writes the
  registry; never auto-runs).

Likely cadence: event-triggered when an explore seed or manual proposal arrives;
acceptance is human/authority-triggered, never scheduled.

Likely context boundaries: the intake/dedupe atoms load the full registry +
information portfolio + foundation queue; the add-proposal atom additionally loads
North Star / ROM / authority surfaces; the acceptance atom loads only the accepted
proposal and the registry.

Likely deterministic vs judgment split:
- Deterministic: well-formedness checks, alias normalization, next-RL-number
  assignment, title/artifact-overlap detection, archived-line lookup, relationship-
  target existence.
- Judgment-based: genuine distinctness, worth-tracking bar, North Star alignment,
  the drafted entry's wording/scope.

Phase 4 coverage questions:
- Does every candidate get a disposition (added, routed, rejected, held)?
- Is every added line created at exactly seed/active?
- Is every duplicate/overlap routed to portfolio-review (never minted in parallel)?
- Is every archived-line re-open routed to lifecycle-review as a revive?
- Is the acceptance atom the only thing that writes the registry?
- Does every added entry preserve provenance and use the live registry format?
- Does intake ever assign maturity above seed? (must be: never.)
- Does every dangling route produce a docket item?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Authority basis:
Risks:
Dedupe result (new / duplicate / revival / partial-overlap):
What would change this recommendation:
Registry addition proposed (RL-NNN at seed/active, inert until accepted):
Requires acceptance by:
Escalation required:
Candidate disposition:
```

## Open questions

1. **Intake bar.** No accepted threshold yet for "promising enough to track as a
   line" vs "too thin to seed." Until set, the bar is judgment-with-rationale and the
   default leans toward seeding (cheap to track at seed, archivable later with
   information gain). Docketed: `signal_type: intake-bar-policy-needed` →
   `govern/decision-review`. **(Non-lock-gating: seed-and-let-lifecycle-prune is a
   safe default under ROM §1.)**
2. **Overlap vs new-line boundary.** The exact line between "partial overlap, still
   a new line with relationships" and "belongs inside an existing line" is judgment;
   recurring confusion routes to portfolio-review and, if it recurs, to decision-
   review as `overlap-resolution-policy-needed`. **(Non-lock-gating.)**
3. **Acceptance authority.** Shared with decision-review / portfolio-review: who
   applies an accepted ADD (human, a `line-add-acceptance` atom, or `docket-triage`).
   Until set, patch-first + manual acceptance. **(Non-lock-gating.)**
4. **Seed artifacts requirement.** Whether a brand-new synthesis seed with *no*
   existing artifacts (only a question) may be seeded, or must first pass through
   `explore/line-incubation`. Current default: seed it with a foundation-queue/seed-
   note pointer; incubation matures it. Docketed if it recurs. **(Non-lock-gating.)**
