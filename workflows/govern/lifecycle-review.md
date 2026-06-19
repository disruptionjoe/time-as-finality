---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: lifecycle_decision_proposal
summarizable: false
unit_of_review: one_lifecycle_candidate
---

# Lifecycle Review

**Family:** govern
**Mode:** decision (evaluation)
**Status:** Phase 3 design — v1.0 LOCKED for current operating model (accepted
form of v0.4; DEC-016, DEC-018). Phase 4 will map this protocol to execution atoms.
**Consumes:** `lifecycle_candidate` outputs from `govern/line-review` or
equivalent authorized candidate sources.
**Scope:** Evaluate one lifecycle candidate for one research line and recommend
no change, a lifecycle change, or escalation.

## Purpose

`lifecycle-review` evaluates whether a research line's lifecycle posture should
remain unchanged or move to a different state. It exists because `line-review`
may detect lifecycle candidates but must not perform lifecycle actions. The
purpose is research-program stewardship.

It governs: attention, status, preservation, routing, reversibility.
It does **not** govern: truth, claim acceptance, portfolio restructuring by
itself, decision-history promotion, or deletion.

A successful run answers: *given current evidence, authority surfaces, the
standing projection, and project needs, should this line's lifecycle posture
change?* It does not answer: *is this line true?*

## Core invariant

Lifecycle Review governs **attention, status, and preservation, not truth.** A
lifecycle transition means the program is changing how it allocates attention to
this line under current conditions. It does not mean the line has been proven
true, proven false, erased, or forgotten. Every recommendation must preserve
provenance, rationale, affected relationships, downstream effects, and
reversal/revival conditions.

## Conservative default

When authority, evidence, schema, or downstream routing is insufficient, the
default is: **no lifecycle change, preserve the candidate, escalate cleanly.**
Lifecycle Review must not improvise around missing authority. If a required
downstream workflow does not exist, it: (1) leaves lifecycle state unchanged;
(2) emits a governance docket item with `signal_type: undefined-workflow-needed`;
(3) names the missing workflow/task; (4) explains why it cannot safely decide
without it; (5) preserves the candidate for later reconsideration.

## Relationship to Line Review

`line-review` produces standing projections and may emit lifecycle candidates;
`lifecycle-review` consumes those candidates and decides whether to recommend a
lifecycle action. Line Review says "this line appears to be a lifecycle
candidate"; Lifecycle Review asks "should this candidate become a recommended
action, remain unchanged, or be escalated?" In v0.x it is **patch-first** — it
proposes lifecycle changes and never silently mutates canonical registry state.

## Lifecycle ontology (two-axis model)

Lifecycle posture has **two independent axes**. Lifecycle Review may recommend
changes to either, but **must not collapse them**.

```yaml
stage:        # maturity
  - seed
  - explored
  - validated
  - incubated
  - secondary-exploit
  - primary-exploit
  - integrated

status:       # attention / disposition
  - active
  - held
  - archived
```

`stage` expresses **maturity**; `status` expresses **attention / disposition**.
`archived` is a **status**, not a stage; `integrated` is the **terminal mature
stage**. (Recommended Line Registry schema update — see Open Questions #1.)

Candidate types bind to the axes as:

```yaml
hold:      { changes: "status -> held" }
revive:    { changes: "status -> active" }
retire:    { changes: "status -> archived" }
promote:   { changes: "stage upward" }
demote:    { changes: "stage downward" }
integrate: { changes: "stage -> integrated" }   # high-scrutiny, like promote
split:     { changes: "structure", default_owner: govern/portfolio-review }
merge:     { changes: "structure", default_owner: govern/portfolio-review }
```

So `hold` / `revive` / `retire` act **only on `status`**; `promote` / `demote` /
`integrate` act **only on `stage`**; `split` / `merge` are **structural** and
route to `govern/portfolio-review`. A single candidate changes one axis; a
combined maturity-and-attention change is two candidates.

## Canonical lifecycle candidate encoding

One canonical candidate object:

```yaml
lifecycle_candidate:
  candidate_type: hold | revive | retire | promote | demote | integrate | split | merge
  affected_line:
  current_state:
  proposed_state_or_direction:
  reason:
  evidence_or_basis:
  source_workflow:
  source_report:
  confidence: low | med | high
  why_source_workflow_cannot_decide:
```

"Candidate-ness" is encoded by the object type `lifecycle_candidate`; do not use
`hold-candidate` etc. as canonical values. Intake normalizes legacy/flag aliases:

```yaml
legacy_or_flag_aliases:
  hold-candidate:    { candidate_type: hold }
  revival-candidate: { candidate_type: revive }
  retire-candidate:  { candidate_type: retire }
  promote-candidate: { candidate_type: promote }
  demote-candidate:  { candidate_type: demote }
  integrate-candidate: { candidate_type: integrate }
  split-candidate:   { candidate_type: split }
  merge-candidate:   { candidate_type: merge }
```

If the candidate type cannot be normalized unambiguously, emit an intake failure
and stop.

## Authority boundaries

**May:** evaluate lifecycle candidates from Line Review, from an authorized
reviewer, or from another governance workflow; recommend lifecycle state changes;
propose registry patches for lifecycle fields; propose preservation notes for
held/retired/demoted/split/merged lines; propose revival/reversal conditions;
route merge/split to `govern/portfolio-review`; route unresolved authority issues
to `govern/docket-triage`; route stale/missing standing snapshots back to
`govern/line-review`; route evidence gaps to an evidence-review workflow if one
exists; route persona-sensitive questions to a deep-panel/persona review if one
exists; emit decision-review signals when repeated cases suggest a policy gap.

**Must not:** decide a claim is true or false; erase a line's reasoning; delete
archived materials; rewrite the Research Operating Model; update Decision History
directly; perform whole-portfolio reconciliation; invent lifecycle states not in
the registry schema; treat standing snapshots as canonical; override the claim
ledger or Decision History; silently apply lifecycle changes; execute merge/split
across multiple lines without Portfolio Review; turn promotion into hidden
canonization.

## Lifecycle action taxonomy

Use the registry's lifecycle/stage vocabulary wherever available. If the current
vocabulary cannot express the needed action, emit a governance docket item with
`signal_type: schema-inadequacy`.

- **Hold** — `status: active -> held` (`stage` unchanged): preserved but no longer
  actively advanced. Use when evidence is insufficient for current attention,
  dependencies are unresolved, the line is not wrong but not yet actionable,
  others should advance first, or a future condition is needed. **Must include
  revival conditions.**
- **Revive** — `status -> active` (retain `stage` unless a separate stage change is
  justified): a held or archived line re-enters active consideration (new
  evidence, resolved dependency, renewed relevance, or the prior hold/retire
  reason no longer applies). **Must include why the prior status no longer holds.**
- **Retire** — `status -> archived` (`stage` unchanged): a preservation /
  disposition action, **not a maturity judgment** (superseded, exhausted,
  conflicts with accepted authority, no longer serves the North Star, or too
  underdefined after repeated review). **Must preserve rationale, artifacts, and
  revival conditions. Retirement is not deletion.**
- **Promote** — `stage` upward: move to a more central maturity position
  (structurally important, strengthened evidence, clearer dependencies, needed by
  multiple lines, moved from speculative toward core). **Must identify authority
  basis, downstream effects, which workflows may rely on it, and
  premature-canonization risk.**
- **Integrate** — `stage -> integrated` (terminal mature stage): makes the line
  part of the accepted working architecture. **High-scrutiny, like promotion**
  (see the safety rule). **Must identify authority basis and downstream effects.**
- **Demote** — `stage` downward: move to a less central maturity position
  (overpromoted, weakened evidence, better understood as supporting/speculative/
  parked). **Must clarify downstream dependency effects.**
- **Split** — divide into multiple lines (separable questions, mixed strength,
  differing governance status, incoherent evidence/dependencies). **Default: route
  to `govern/portfolio-review`.** Narrow exception — a simple internal split that
  does not alter cross-line relationships, dependencies, portfolio balance,
  reclassify others, or need a new state — may be *recommended* here, but v0.x
  emits a patch proposal only.
- **Merge** — combine lines (duplication, distinction no longer carries
  governance value, converged evidence/dependencies, separation causes drift).
  **Default: route to `govern/portfolio-review`.** May recommend routing; never
  execute without portfolio review.

### v0.x promotion / integration safety rule

Until formal promotion/integration thresholds exist, **all `promote` and
`integrate` candidates are high-scrutiny.** Lifecycle Review may recommend them,
but any promotion or integration that would let other workflows depend on the line
as core requires explicit human acceptance or governance escalation before
registry state changes. **Promotion and integration are never proof.**

## Expected inputs

Read first: the `lifecycle_candidate` object; the latest `govern/line-review`
standing snapshot for the affected line; `registries/line-registry.md`;
`registries/research-line-scorecard.md` (health substrate);
`registries/decision-history.md`; `RESEARCH-OPERATING-MODEL.md`;
`CLAIM-LEDGER.md`; `ROADMAP.md`; `HYPOTHESES.md`; `../NORTH-STAR.md`; relevant
artifacts in `models/`, `results/`, `tests/`, `claims/`; recent `logs/runs/` and
`logs/synthesis/`; the Govern Memory Pack if present.

Optional, only when triggered: prior Portfolio/Evidence/Persona review output; a
direct human note requesting lifecycle action.

## Treatment of standing snapshots

Standing snapshots are useful evidence but **not canonical state.** Use them to
understand recent standing, Line Review flags, evidence posture, dependency
clarity, boundary health, routing readiness, and candidate rationale — then still
check the underlying registry, health substrate, authority surfaces, and
artifacts before recommending change. A stale/missing/malformed snapshot should
usually produce `outcome_class: line_review_needed` rather than lifecycle action.

## Evidence-related exits

- **`line_review_needed`** — snapshot missing/stale/malformed/inconsistent/
  insufficient. Destination: `recommended_owner_workflow: govern/line-review`.
- **`more_evidence_needed`** — the question can't be decided from current evidence
  but the needed evidence task isn't yet specific. Default: no change, preserve
  candidate, emit a docket item if the gap recurs or blocks progress.
- **`evidence_review_needed`** — only if a defined evidence-review workflow exists
  and the missing question can be routed there. If no such workflow exists, emit
  `signal_type: undefined-workflow-needed` (or `manual-review-required`) and leave
  lifecycle state unchanged.

## Write surfaces

May emit: a lifecycle decision report; a lifecycle registry **patch proposal**; a
preservation note; revival/reversal conditions; a downstream routing
recommendation; a governance docket item; a Project Log entry; a decision-review
signal. In v0.x all lifecycle state changes are **patch proposals** unless a later
accepted authority grants direct write authority.

## Procedure

0. **Intake and candidate validation.** Check the candidate object exists; type is
   recognized or normalizable; affected line exists; reason + evidence basis
   present; source workflow/authorized source present; current stage readable;
   proposed direction intelligible; source explains why it could not decide. On
   failure, emit an intake-failure report and stop.
1. **Load authority and line context** — current registry entry, latest standing
   snapshot, health substrate, claim-ledger state, artifacts, Decision History,
   Research Operating Model, North Star, Project Log. If required context is
   unavailable, emit `outcome_class: manual_review_required`.
2. **State the lifecycle question** precisely, and never mix axes — e.g. "Should
   RL-003 remain `stage: incubated` but move `status: active -> held`?" or "Should
   RL-006 move `status: archived -> active`, retaining its prior `stage` unless a
   separate stage change is justified?" The question must be explicit before
   continuing.
3. **Check authority constraints** — does the schema allow the proposed state?
   Does Decision History constrain this line? Does the ROM allow this
   workflow to make/propose this action? Conflict with the claim ledger? Require
   Portfolio Review / Decision Review / human review / new schema vocabulary? Does
   the required downstream workflow exist? If authority is insufficient, emit a
   governance docket item — do not improvise.
4. **Evaluate lifecycle basis** across: current standing (and freshness),
   evidence posture, dependency state, boundary state, program role, opportunity
   cost, preservation need, reversibility.
5. **Choose one primary outcome class:**

   ```yaml
   outcome_class:
     - no_change
     - lifecycle_change_proposed
     - more_evidence_needed
     - evidence_review_needed
     - line_review_needed
     - portfolio_review_needed
     - schema_review_needed
     - decision_review_signal
     - manual_review_required
   ```

   Others may attach as downstream signals, but one is primary. When in doubt,
   choose `no_change` plus escalation.
6. **Produce a lifecycle recommendation** (if proposing change):

   ```yaml
   lifecycle_recommendation:
     affected_line:
     candidate_type:
     current_state:
     recommended_state_or_direction:
     outcome_class:
     rationale:
     evidence_or_basis:
     authority_basis:
     confidence: low | med | high
     risks:
     downstream_effects:
     preservation_requirements:
     revival_or_reversal_conditions:
     patch_required: true
   ```

   Hold/retire/demote/split/merge → preservation requirements mandatory. Promote →
   downstream effects + authority basis mandatory. Revive → prior-state reversal
   rationale mandatory. Split/merge → Portfolio Review requirement explicitly
   evaluated.
7. **Emit a patch proposal** separating lifecycle/stage changes, why-state
   rationale, relationship changes, preservation notes, revival conditions, and
   downstream route changes. Do not alter canonical state directly in v0.x.
8. **Emit governance docket items** for anything it cannot resolve:

   ```yaml
   governance_docket_item:
     issue:
     affected_line:
     signal_type:
     authority_surfaces_involved:
     why_lifecycle_review_cannot_resolve:
     recommended_owner_workflow:
     evidence_or_basis:
   ```

   Typical `signal_type`: schema-inadequacy, authority-conflict,
   decision-history-gap, undefined-workflow-needed, manual-review-required,
   portfolio-review-required, evidence-review-required, claim-ledger-conflict,
   promotion-threshold-needed.
9. **Preserve the candidate if unresolved** with `candidate_status`:
   unresolved_preserved | routed_to_other_workflow | rejected_with_rationale |
   superseded. Unresolved candidates must not disappear silently.
10. **Emit report and Project Log entry** (plus patch, preservation note, docket
    items as relevant).

## Output: Lifecycle Review Report

```markdown
# Lifecycle Review Report
## Review Metadata
- Workflow / version / run date / trigger / candidate source / affected line / candidate type:
## Candidate Validation
- Valid? / normalized type / intake issues:
## Lifecycle Question
- Question / current stage / proposed stage or direction:
## Authority Check
- Schema allows? / Decision History / ROM constraints / Claim Ledger conflicts / downstream workflow exists? / Portfolio Review required? / manual review required?:
## Evidence Review
- Latest snapshot / freshness / evidence posture / dependency state / boundary state / program role / opportunity cost / preservation need / reversibility:
## Outcome
- Outcome class / recommendation / confidence / rationale / evidence / risks / downstream effects:
## Patch Proposal
- Registry fields affected / proposed patch / requires acceptance by:
## Preservation / Revival
- Preservation requirements / revival or reversal conditions:
## Governance Docket Items
- Items emitted:
## Candidate Disposition
- Candidate status / where preserved or routed:
## Project Log Entry
- Summary / output pointers:
```

## Escalation triggers

Escalate rather than act when: the proposed state is not in the schema; the action
affects multiple lines; merge/split is required; claim ledger and registry
conflict; Decision History conflicts; ROM authority is unclear; the latest
snapshot is stale/missing; evidence is too weak to act but strong enough to
prevent dismissal; promotion would let others depend on the line as core;
retirement would affect downstream dependencies; revival contradicts a prior
retirement rationale; no workflow exists to own the next step.

## Failure modes

- **Lifecycle as truth judgment** ("retired" = "false"). Guard: lifecycle governs
  attention/status, not truth.
- **Retirement as deletion.** Guard: preservation note + revival conditions
  required.
- **Promotion as canonization.** Guard: authority basis + downstream note +
  explicit acceptance.
- **Merge/split swallowing Portfolio Review.** Guard: default to Portfolio Review.
- **Standing snapshot treated as canonical.** Guard: snapshot is evidence only;
  check substrate and freshness.
- **Patch as hidden action.** Guard: patch-first; explicit acceptance step.
- **Schema improvisation.** Guard: schema inadequacy routes to a docket item.
- **Authority inversion** (memory/persona/snapshot overrides Decision History).
  Guard: authority surfaces outrank memory and advisory outputs (operating model §11).
- **Silent candidate loss.** Guard: unresolved candidates preserved with status.
- **Dangling route.** Guard: emit `undefined-workflow-needed`, leave state
  unchanged, preserve candidate.

## Success criteria

A good run lets a reviewer understand: the lifecycle question asked; why the line
was considered; what authority allows/blocks it; what evidence supports the
recommendation; the risks and downstream effects; what must be preserved; what
would reverse it later; the proposed patch; what unresolved issues were routed
elsewhere; and what happened to the candidate.

Cheap test: a reviewer can accept, reject, or escalate the recommendation without
rereading the entire line history.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/lifecycle-candidate-intake` — one candidate; validated/normalized
  candidate or intake failure; mostly deterministic.
- `govern/single-line-lifecycle-review` — one line, one lifecycle question;
  decision report + patch proposal; judgment-based.
- `govern/lifecycle-patch-acceptance` — one accepted recommendation; registry
  update + Project Log entry; requires explicit authority.
- `govern/lifecycle-preservation-check` — one hold/retire/split/merge/demote;
  preservation-note completeness; mostly deterministic.

Likely cadence: event-triggered when Line Review emits a candidate or a human
requests action; periodic only for stale held/retired lines if a revival policy
later exists.

Deterministic: candidate validation, alias normalization, schema vocabulary check,
required-field existence, stale-snapshot detection, relationship-target
validation, downstream-workflow existence check. Judgment-based: the
recommendation, opportunity cost, preservation adequacy, reversibility,
promotion/demotion rationale.

Phase 4 coverage questions: Does every candidate have a destination? Does every
unresolved candidate get preserved? Does every recommendation have an
accept/reject path? Does every accepted action update registry + Project Log? Does
every hold/retire preserve revival conditions? Are merge/split routed through
Portfolio Review? Are promotions prevented from becoming truth-canonization? Is
any action made by a workflow with only advisory authority? Does every dangling
route produce a docket item?

## Verdict block

```text
Lifecycle recommendation:
Reason:
Evidence:
Authority basis:
Risks:
Downstream effects:
Preservation requirements:
What would reverse this recommendation:
Patch proposed:
Escalation required:
Candidate disposition:
```

## Open questions

1. **Registry schema update.** Two-axis lifecycle model adopted in this draft:
   `stage` (maturity: seed…integrated) and `status` (attention/disposition:
   active | held | archived), with `archived` removed from the stage ladder. Needs
   line-registry schema implementation/acceptance (a registry change — likely a
   `decision-review` item).
2. **Direct write authority** — patch-only permanently, or direct apply after
   acceptance later?
3. **Internal split exception** — exact conditions qualifying a split as purely
   internal (no Portfolio Review).
4. **Patch acceptance owner** — human, a dedicated accept step, or `docket-triage`?
   (Shared with line-review's open item.)
5. **Cadence for held/retired lines** — periodic reconsideration or trigger-only?
6. **Promotion threshold** — minimum evidence/standing before promotion to core
   (until set, all promotions high-scrutiny).
7. **Evidence-review workflow** — create one, or route evidence gaps to manual/
   docket until later?
8. **decision-review vs docket-triage** — reconcile the two govern sinks
   (carried from DEC-017).
