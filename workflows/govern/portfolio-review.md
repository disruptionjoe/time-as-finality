---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: structural_proposal
summarizable: false
unit_of_review: one_portfolio_question
---

# Portfolio Review

**Family:** govern
**Mode:** evaluation
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** `split` / `merge` candidates routed from `govern/lifecycle-review`;
`overlap` / duplication and dependency-graph flags routed from `govern/line-review`
(its portfolio-level signals); direct portfolio questions from an authorized
governance source.
**Scope:** Evaluate **one portfolio question** about the cross-line *structure* of
the research portfolio and recommend a structural change, no change, or escalation.

## Purpose

`portfolio-review` is the only workflow that holds the **whole-registry structural
view**. It reconciles the research portfolio *as a graph of related lines* rather
than line-by-line. It exists because `line-review` (single-line standing) and
`lifecycle-review` (single-line lifecycle posture) deliberately refuse cross-line
restructuring, yet split/merge/overlap/dependency questions can only be answered
with the whole registry in view.

It governs: cross-line **structure** — merge/split *execution proposals*, overlap
and duplication resolution, dependency-graph coherence (using the line-registry
relationship fields), and primary/secondary balance across persona clusters.

It does **not** govern: a single line's standing (that is `line-review`); a single
line's lifecycle stage/status move (that is `lifecycle-review`); claim truth;
promotion of any rule to Decision History (that is `govern/decision-review`).

A successful run answers: *given the whole registry, its relationship graph, the
health substrate, persona-cluster balance, and the authority surfaces, should the
portfolio's structure change — and if so, how, expressed as a patch a reviewer can
accept?* It does not answer: *is any line true?* or *should any single line move
lifecycle states?*

## Core invariant

Portfolio Review governs **structure, not standing, not lifecycle, not truth.** A
structural recommendation changes how lines are *grouped, related, or balanced*; it
never asserts a claim is true, never moves a line's `stage`/`status` by itself, and
never canonizes a rule. Every recommendation must preserve provenance, the
pre-change relationship graph, downstream effects on dependent lines, and
reversal conditions. **Structure is patch-first**: Portfolio Review proposes
changes to line-registry structure and never silently mutates canonical state.

## Conservative default

When authority, evidence, the relationship graph, or downstream routing is
insufficient, the default is: **no structural change, preserve the question,
escalate cleanly.** Portfolio Review must not improvise around missing authority.
If a required downstream workflow does not exist, it: (1) leaves structure
unchanged; (2) emits a governance docket item with
`signal_type: undefined-workflow-needed`; (3) names the missing workflow/task;
(4) explains why it cannot safely decide without it; (5) preserves the portfolio
question for later reconsideration.

## Relationship to Line Review and Lifecycle Review

- `line-review` produces single-line standing and may **flag** portfolio
  implications (overlap, duplication, a dependency-graph inconsistency). Those
  flags arrive here as portfolio questions; Line Review never reconciles cross-line
  structure itself (its own authority boundary).
- `lifecycle-review` evaluates one line's lifecycle posture and **routes
  `split`/`merge` here by default** — these are structural, multi-line actions it
  must not execute. A narrow internal split that does not alter cross-line
  relationships may be recommended there, but anything touching the graph,
  portfolio balance, or other lines' classification belongs here.
- Portfolio Review never reaches back into single-line standing or lifecycle moves.
  When a structural change *implies* lifecycle moves on specific lines (e.g. a merge
  retires one line's identity), it **proposes the structure** and **routes the
  per-line lifecycle moves to `lifecycle-review`** as lifecycle candidates. The two
  workflows must never both reconcile the same axis.

## Structural question taxonomy

One run evaluates exactly one of:

```yaml
portfolio_question_type:
  - merge            # combine 2+ lines into one (structural execution of a routed merge)
  - split            # divide 1 line into 2+ lines (structural execution of a routed split)
  - overlap          # two+ lines overlap / duplicate; resolve (merge, demarcate, or accept)
  - dependency-graph # relationship-field coherence: cycles, dangling/contradictory edges
  - balance          # primary/secondary distribution across persona clusters (ROM §4, §7-8)
```

`merge` / `split` are the *structural execution* of candidates routed from
lifecycle-review; `overlap` resolves duplication (which may resolve **to** a merge,
a demarcation patch, or "accept as distinct"); `dependency-graph` audits the
relationship fields (`depends_on`, `supports`, `competes_with`, `extends`,
`imports`) for cycles, dangling targets, and contradictions; `balance` checks that
no single homogeneous persona cluster dominates the primary/secondary roster
(ROM §4, §7-8) — it **diagnoses and proposes**, it does not itself promote/demote
(those are lifecycle moves routed out).

## Canonical portfolio question encoding

```yaml
portfolio_question:
  question_type: merge | split | overlap | dependency-graph | balance
  affected_lines:           # one or more existing RL-NNN (must exist in registry)
  current_structure:        # relevant relationship edges / grouping today
  proposed_direction:       # the structural change being asked about (may be open)
  reason:
  evidence_or_basis:
  source_workflow:          # govern/lifecycle-review | govern/line-review | authorized source
  source_report:
  confidence: low | med | high
  why_source_workflow_cannot_decide:
```

Intake normalizes legacy/flag aliases routed from upstream:

```yaml
legacy_or_flag_aliases:
  split-candidate:   { question_type: split }
  merge-candidate:   { question_type: merge }
  overlap:           { question_type: overlap }
  overlap-flag:      { question_type: overlap }
  dependency-flag:   { question_type: dependency-graph }
  balance-flag:      { question_type: balance }
```

If the question type cannot be normalized unambiguously, emit an intake failure
and stop.

## Authority boundaries

- **May:** read the whole line registry and its relationship graph; read the
  health substrate, persona-cluster registry, information portfolio, and authority
  surfaces; evaluate one portfolio question; propose structural **patches** to
  line-registry grouping and relationship fields; propose new RL identities created
  *by a split* and merged-away identities *by a merge* (as patch proposals only);
  diagnose dependency-graph incoherence and primary/secondary cluster imbalance;
  route the per-line lifecycle consequences of a structural change to
  `govern/lifecycle-review` as lifecycle candidates; route single-line standing
  questions back to `govern/line-review`; emit `govern/decision-review` signals when
  a structural pattern recurs or a policy gap is exposed; emit governance docket
  items for anything it cannot resolve; preserve unresolved portfolio questions.
- **Must not:** perform single-line standing review (→ `line-review`); perform
  lifecycle stage/status moves itself (→ `lifecycle-review`); promote anything to
  Decision History (→ `decision-review`); decide a claim is true or false; delete
  any line or its reasoning; rewrite the Research Operating Model; update Decision
  History or any authority surface directly; invent relationship-field vocabulary
  not in the registry schema; silently apply structural changes; execute a
  merge/split as a canonical registry write (patch-first only); promote/demote
  lines to fix balance (those are lifecycle moves routed out).
- **Scoring authority — hybrid:** deterministic where derivable from the registry
  graph and substrate (dangling edges, cycles, duplicate-artifact overlap, cluster
  headcount on the primary/secondary roster); judgment only with explicit
  rationale (whether overlap warrants merge, whether a split is coherent, whether
  imbalance is harmful).
- **Write authority — patch-first.** All structural changes are patch proposals
  applied by an authority/accept step, never by Portfolio Review.

## Read surfaces

- **Whole registry + graph:** `registries/line-registry.md` — every line's stage,
  status, relationship fields (`depends_on`, `supports`, `competes_with`,
  `extends`, `imports`), why-state, and artifacts. The graph is the primary object.
- **Health substrate:** `registries/research-line-scorecard.md` — per-line health
  profile, esp. `Dependency centrality` and `Cross-cluster support`.
- **Persona clusters:** `registries/persona-clusters.md` — the seven discipline
  clusters, for primary/secondary balance reasoning (ROM §4, §7-8).
- **Information portfolio:** `registries/information-portfolio.md` — so a merge/
  split/retire-by-merge preserves recorded information gain.
- **Standing snapshots (evidence only):** the latest `govern/line-review` snapshots
  for affected lines in `logs/` — useful but **not canonical**; re-check substrate.
- **Authority surfaces:** `CLAIM-LEDGER.md`, `ROADMAP.md`, `HYPOTHESES.md`,
  `../NORTH-STAR.md`.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — authority order
  (§11), lifecycle ontology (§4), voting/cross-cluster rules (§7-8), document
  layout (§12), workflow/task split (§13).
- **Decision History:** `registries/decision-history.md` — active governance
  constraints (esp. DEC-007 portfolio-layer rule, DEC-018/DEC-020 two-axis model).
- **Workflow catalog / skeleton:** `README.md`, `WORKFLOW-SKELETON-PROPOSAL.md` —
  to validate route targets and avoid routing to workflows that do not exist.
- **Govern Memory Pack load surface** (Phase 3.5; inert if absent).

## Write surfaces

- A **portfolio review report** (the run's primary artifact).
- A **structural patch proposal** against `line-registry.md` — relationship-field
  edits, grouping changes, a split's new RL stubs, a merge's consolidation — applied
  by an authority/accept step, **not** by Portfolio Review.
- **Lifecycle candidates** → `govern/lifecycle-review` (the per-line stage/status
  consequences of an accepted structural change).
- **Governance docket items** → the docket consumed by `govern/decision-review`
  (see Registry interactions).
- **decision-review signals** → `govern/decision-review` when a structural pattern
  recurs or a policy gap is exposed.
- A **Project Log entry** (orchestrator appends to `PROJECT-LOG.md`; this workflow
  supplies the entry text, it does not edit the log directly).

**Patch targets.** A patch may edit line-registry relationship fields, grouping/
why-state prose, and (for split) add new RL stubs at the *same* stage/status the
parent carried, or (for merge) mark a consolidated line for retirement **via a
routed lifecycle candidate** — the structural patch sets up the grouping; the
actual `status -> archived` move is owned by lifecycle-review. The patch never edits
claim/roadmap/hypothesis status (DEC-007) and never edits Decision History.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): recurring portfolio heuristics, known false-positive
  overlap pairs, prior merge/split outcomes, dependency-graph anti-patterns.
- Writes (learning-return, after acceptance): `pack_ref`, `work_ref`, `round_ref`,
  `guidance_used`, `missing_guidance`, `confusion_or_conflict`,
  `observed_failure_mode`, `output_quality_signal`, `suggested_summary_update`.
- Does not depend on memory existing; the Memory Pack is guidance only and never
  outranks an authority surface (ROM §11).

## Registry interactions

- **Reads:** line-registry (graph + grouping), research-line-scorecard
  (substrate), persona-clusters (balance), information-portfolio (gain
  preservation), decision-history (constraints).
- **Writes:** proposes structural patches to line-registry (patch-first; applied by
  an accept step, not here). Never writes claim/roadmap/hypothesis status (DEC-007).
- **Docket:** governance docket items are written to the governance docket consumed
  by `govern/decision-review` (Phase 4 names the concrete docket file; until then
  the item travels with the report and is addressed to `govern/decision-review` via
  its `docket-triage` intake atom — see decision-review).

## Procedure (runnable scope: one portfolio question)

0. **Intake and question validation.** Confirm the `portfolio_question` object
   exists; type is recognized or normalizable; every `affected_line` exists in the
   registry; reason + evidence basis present; source workflow/authorized source
   present; the source explains why it could not decide. On failure, emit an
   intake-failure report and stop.
1. **Load the whole graph and authority context** — the full line registry with
   relationship fields, health substrate, persona clusters, information portfolio,
   relevant standing snapshots, authority surfaces, Decision History, Research
   Operating Model, Project Log. If required context is unavailable, emit
   `outcome_class: manual_review_required`.
2. **State the portfolio question precisely** — one question, one type. E.g.
   "Should RL-003 and RL-005 merge, given both `supports RL-001` and share T-range
   artifacts?" or "Is the `competes_with` edge between RL-001 and RL-002 consistent
   with both also being `supports`?" The question must be explicit before
   continuing.
3. **Check authority constraints** — does the registry schema express the proposed
   structure (relationship vocabulary)? Does Decision History constrain it (esp.
   DEC-007: the registry never restates claim/roadmap/hypothesis status)? Does ROM
   allow this workflow to propose this structural action? Does the change *imply*
   lifecycle moves (then route them to lifecycle-review) or a new schema/policy
   (then docket to decision-review)? Does every required downstream workflow exist?
   If authority is insufficient, emit a docket item — do not improvise.
4. **Evaluate the structural basis** for the question type:
   - **merge:** are the lines genuinely the same question? do evidence/dependencies
     converge? does merging preserve each line's information gain and provenance?
     which identity survives, and which becomes a routed retire?
   - **split:** are the sub-questions genuinely separable (different evidence,
     governance status, or dependencies)? do the resulting lines each carry a
     coherent why-state? what stage/status do the children inherit (default: the
     parent's, pending lifecycle-review)?
   - **overlap:** is the overlap real duplication (→ merge), a sharable boundary
     (→ demarcation patch to relationship/why-state), or acceptable distinctness
     (→ no change + note)?
   - **dependency-graph:** are there cycles, dangling targets (edge → nonexistent
     line), or contradictions (e.g. A `supports` B while B `competes_with` A in a
     way the why-states do not reconcile)? Propose edge corrections.
   - **balance:** does one homogeneous persona cluster dominate the primary/
     secondary roster by headcount (ROM §7-8)? Diagnose; if a rebalance implies
     promotion/demotion, **route those as lifecycle candidates** — do not move
     stages here.
5. **Choose one primary outcome class:**

   ```yaml
   outcome_class:
     - no_change
     - structural_change_proposed
     - lifecycle_consequences_routed   # structure proposed; per-line moves → lifecycle-review
     - line_review_needed              # a single line's standing must be refreshed first
     - schema_review_needed            # relationship/grouping vocabulary inadequate
     - decision_review_signal          # recurring pattern / policy gap → decision-review
     - manual_review_required
   ```

   Others may attach as downstream signals, but one is primary. When in doubt,
   choose `no_change` plus escalation.
6. **Produce a structural recommendation** (if proposing change):

   ```yaml
   structural_recommendation:
     question_type:
     affected_lines:
     current_structure:
     recommended_structure:
     outcome_class:
     rationale:
     evidence_or_basis:
     authority_basis:
     confidence: low | med | high
     risks:
     graph_effects:                 # how the relationship graph changes
     downstream_lifecycle_candidates: # per-line moves routed to lifecycle-review
     information_gain_preservation:   # how merged/split/retired gain is preserved
     reversal_conditions:
     patch_required: true
   ```

   merge → surviving identity + retired identity + gain preservation mandatory.
   split → child identities + inherited stage/status + per-child why-state
   mandatory. overlap → explicit choice among merge / demarcate / accept.
   dependency-graph → exact edge edits. balance → diagnosis + any routed lifecycle
   candidates (never a stage move here).
7. **Emit a structural patch proposal** against line-registry, separating
   relationship-field edits, grouping/why-state edits, new/retired RL stubs, and
   the lifecycle candidates that must be routed. Do not alter canonical state in
   v1.0.
8. **Route per-line lifecycle consequences** to `govern/lifecycle-review` as
   `lifecycle_candidate` objects (e.g. a merge's `retire` on the consolidated line,
   a split's `promote`/`demote` if a child warrants it). Portfolio Review proposes
   the structure; lifecycle-review owns the stage/status moves.
9. **Emit governance docket items** for anything it cannot resolve:

   ```yaml
   governance_docket_item:
     issue:
     affected_lines:
     signal_type:
     authority_surfaces_involved:
     why_portfolio_review_cannot_resolve:
     recommended_owner_workflow:
     evidence_or_basis:
   ```

   Typical `signal_type`: schema-inadequacy, authority-conflict,
   decision-history-gap, undefined-workflow-needed, manual-review-required,
   merge-split-policy-needed, overlap-resolution-policy-needed,
   balance-policy-needed, dependency-schema-needed.
10. **Preserve the question if unresolved** with `question_status`:
    unresolved_preserved | routed_to_other_workflow | rejected_with_rationale |
    superseded. Unresolved portfolio questions must not disappear silently.
11. **Emit report and Project Log entry text** (plus patch, routed lifecycle
    candidates, docket items as relevant). End with the verdict block.

## Outputs (shapes)

### Portfolio Review Report

```markdown
# Portfolio Review Report
## Review Metadata
- Workflow / version / run date / trigger / question source / affected lines / question type:
## Question Validation
- Valid? / normalized type / intake issues:
## Portfolio Question
- Question / current structure / proposed direction:
## Authority Check
- Schema expresses it? / Decision History (DEC-007 etc.) / ROM constraints / implies lifecycle moves? / implies new schema/policy? / downstream workflows exist?:
## Structural Evaluation
- Graph state / overlap or duplication / dependency coherence (cycles, dangling, contradictions) / persona-cluster balance / information-gain at risk:
## Outcome
- Outcome class / recommendation / confidence / rationale / evidence / risks / graph effects:
## Structural Patch Proposal
- Registry fields/edges affected / proposed patch / new or retired RL stubs / requires acceptance by:
## Routed Lifecycle Candidates
- Per-line stage/status moves routed to govern/lifecycle-review:
## Information-Gain Preservation
- How merged/split/retired gain is preserved (information-portfolio pointer):
## Governance Docket Items
- Items emitted (with signal_type):
## Question Disposition
- Question status / where preserved or routed:
## Project Log Entry
- Summary / output pointers:
```

### Structural patch proposal shape

```yaml
structural_patch_proposal:
  target: registries/line-registry.md
  relationship_edits:        # add/remove/correct edges on named lines
  grouping_or_why_state_edits:
  new_line_stubs:            # for split: RL-NNN stubs at inherited stage/status
  retire_via_lifecycle:      # for merge: line(s) to be retired by routed candidate
  requires_acceptance_by:    # authority/accept step (never portfolio-review itself)
  reversal_conditions:
```

### Routed lifecycle candidate shape (to lifecycle-review)

Uses lifecycle-review's canonical `lifecycle_candidate` object verbatim, with
`source_workflow: govern/portfolio-review` and
`why_source_workflow_cannot_decide:` set to "stage/status move is lifecycle-review's
authority; portfolio-review proposes only the structure."

Every run ends with the verdict block.

## Escalation triggers

Escalate rather than act when: a `affected_line` does not exist; the relationship
vocabulary cannot express the needed structure (→ schema docket); the structural
change would restate claim/roadmap/hypothesis status (DEC-007 conflict); Decision
History constrains the structure; ROM authority is unclear; the change implies
lifecycle moves (→ route to lifecycle-review, never execute); a single line's
standing is stale and the structure depends on it (→ line-review); balance can only
be fixed by promotion/demotion (→ route lifecycle candidates, never move stages);
the same merge/overlap/imbalance recurs across runs (→ decision-review signal); no
workflow exists to own the next step (→ `undefined-workflow-needed`).

## Failure modes

- **Structure as lifecycle move** (a merge silently archiving a line). Guard:
  structure is patch-first; per-line stage/status moves are routed to
  lifecycle-review, never executed here.
- **Structure as standing review** (re-scoring one line under cover of a graph
  pass). Guard: single-line standing belongs to line-review; route it out.
- **Structure as canonization** (a relationship edit treated as a policy rule).
  Guard: recurring/structural-policy patterns route to decision-review; the patch
  changes the registry only after an accept step.
- **Merge erasing information gain or provenance.** Guard: information-gain
  preservation + provenance pointer mandatory on every merge/retire-by-merge.
- **Split producing incoherent children.** Guard: each child must carry its own
  coherent why-state and inherited stage/status, or the split is rejected with
  rationale.
- **Dangling or cyclic edges introduced by a patch.** Guard: dependency-graph
  validation runs on the *proposed* graph, not only the current one.
- **Balance fixed by hidden promotion.** Guard: balance diagnoses and routes
  lifecycle candidates; it never moves stages.
- **Status drift** (registry restating claim/roadmap/hypothesis status). Guard:
  DEC-007 — the registry links out; the patch never edits those surfaces.
- **Standing snapshot treated as canonical.** Guard: snapshot is evidence only;
  re-check substrate and graph.
- **Patch as hidden action.** Guard: patch-first; explicit acceptance step.
- **Both line-review and portfolio-review reconciling cross-line structure.**
  Guard: line-review only flags; portfolio-review owns reconciliation.
- **Silent question loss.** Guard: unresolved questions preserved with status.
- **Dangling route.** Guard: emit `undefined-workflow-needed`, leave structure
  unchanged, preserve the question.

## Success criteria

A good run yields, for one portfolio question, a structural recommendation whose
basis is defensible from the cited graph, substrate, and authority surfaces;
preserves provenance and information gain across any merge/split; routes every
per-line lifecycle consequence to lifecycle-review and every single-line standing
question to line-review; proposes a patch a reviewer can accept or reject quickly;
and changes no canonical state itself.

Cheap auditability test: a reviewer can tell, without rebuilding the whole graph by
hand, which lines the question touches, what the proposed structure changes in the
relationship graph, which lifecycle moves were routed out (not executed), how
information gain is preserved, and which downstream workflow owns any unresolved
issue.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/portfolio-question-intake` — one question; validated/normalized question
  or intake failure; mostly deterministic.
- `govern/dependency-graph-audit` — whole registry → cycles, dangling, contradicting
  edges → edge-correction patch proposal; mostly deterministic.
- `govern/overlap-resolution` — one overlap pair/cluster → merge | demarcate |
  accept recommendation; judgment-based.
- `govern/merge-split-execution-proposal` — one routed merge/split → structural
  patch + routed lifecycle candidates; judgment-based.
- `govern/portfolio-balance-check` — whole roster → cluster-balance diagnosis +
  routed lifecycle candidates; hybrid.

Likely cadence: event-triggered when lifecycle-review routes a split/merge or
line-review flags overlap/dependency issues; periodic for whole-graph audits
(dependency-graph, balance) on a slow cadence once a registry-size threshold exists.

Likely context boundaries: the structural atoms load the whole registry graph +
substrate + persona clusters + information portfolio (the graph is irreducible —
the unit of review is a portfolio question, not a single line); overlap/merge/split
atoms additionally load the affected lines' artifacts and standing snapshots.

Likely deterministic vs judgment split:
- Deterministic: question validation, alias normalization, edge existence /
  cycle / dangling-target detection, duplicate-artifact detection, cluster
  headcount on the roster, relationship-target validation.
- Judgment-based: whether overlap warrants merge, split coherence, surviving merge
  identity, whether imbalance is harmful, the structural recommendation.

Phase 4 coverage questions:
- Does every portfolio question have a destination?
- Does every unresolved question get preserved?
- Does every structural recommendation have an accept/reject path?
- Does every accepted structural change update the registry + Project Log via an
  authority step (never this workflow)?
- Are all per-line lifecycle consequences routed to lifecycle-review (never
  executed here)?
- Are all single-line standing questions routed to line-review?
- Are recurring structural patterns routed to decision-review?
- Is information gain preserved across every merge/split?
- Does the proposed graph stay acyclic and dangle-free?
- Does every dangling route produce a docket item?
- Is cross-line reconciliation owned by exactly one workflow (this one)?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Authority basis:
Risks:
Graph effects:
Routed lifecycle candidates:
Information-gain preservation:
What would reverse this recommendation:
Patch proposed:
Escalation required:
Question disposition:
```

## Open questions

1. **Merge/split execution policy.** No accepted threshold yet for *when* overlap
   warrants a merge vs a demarcation, nor for what makes a split coherent. Until
   set, all merges/splits are recommendations only and high-scrutiny. Docketed:
   `signal_type: merge-split-policy-needed` → `govern/decision-review`.
   **(Non-lock-gating: conservative default — propose, never execute — holds.)**
2. **Primary/secondary balance policy.** ROM §7-8 forbids single-cluster
   domination but sets no numeric balance target. Until set, balance runs diagnose
   and route lifecycle candidates only. Docketed:
   `signal_type: balance-policy-needed` → `govern/decision-review`.
   **(Non-lock-gating.)**
3. **Dependency-graph schema completeness.** The five relationship fields may not
   express every needed structural relation (e.g. "supersedes", "mutually-exclusive
   role"). Docketed: `signal_type: dependency-schema-needed` → `govern/decision-review`.
   **(Non-lock-gating: current vocabulary is sufficient for v1.0 cases.)**
4. **Concrete docket file location.** Where governance docket items physically land
   (a `registries/governance-docket.md` vs traveling with reports) is a Phase-4
   plumbing question shared with line-review and lifecycle-review.
   **(Non-lock-gating.)**
5. **Patch-acceptance owner.** Who applies accepted structural patches (a human
   accept step, a dedicated atom, or `docket-triage`) — shared open item across the
   govern family. **(Non-lock-gating: patch-first holds regardless.)**
