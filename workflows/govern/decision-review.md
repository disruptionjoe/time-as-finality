---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: decision_proposal
summarizable: false
unit_of_review: one_decision_candidate
---

# Decision Review

**Family:** govern
**Mode:** evaluation
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** accumulated **governance docket items** emitted by `govern/line-review`,
`govern/lifecycle-review`, `govern/portfolio-review`, `govern/line-intake`, and any
authorized governance source; recurring decision-worthy patterns surfaced across
runs (schema-inadequacy, promotion-threshold-needed, authority-conflict, policy
gaps, undefined-workflow-needed).
**Scope:** Evaluate **one decision candidate** — a docketed governance question that
may warrant a durable, citable rule — and either propose a Decision History entry
(patch-first), route it elsewhere, or hold it for more evidence.

## Purpose

`decision-review` is the **only** workflow that may **propose** an entry to
`registries/decision-history.md` (a `DEC-NNN`). It exists because the other govern
workflows deliberately refuse to canonize policy: they emit governance docket items
when they hit a schema gap, an authority conflict, a missing threshold, or a
missing workflow — and those signals must accumulate somewhere that can turn a
*recurring* governance problem into a *proposed durable decision*.

It governs: the **pathway from recurring governance signal to a proposed
constitutional decision** — recognizing when a docketed pattern is decision-worthy,
drafting a well-formed `DEC-NNN` proposal, and presenting it for human/authority
acceptance.

It does **not** govern: single-line standing (`line-review`); lifecycle stage/status
moves (`lifecycle-review`); cross-line structure (`portfolio-review`); new-line
creation (`line-intake`); and — critically — it **never self-canonizes**. A
proposed `DEC-NNN` is not active until an authority surface accepts it (ROM §11:
explicit user decisions and the canonical surfaces outrank any workflow).

A successful run answers: *does this docketed governance pattern warrant a durable
decision, and if so, what is the precise `DEC-NNN` proposal a human can accept,
reject, or amend?* It does not answer the underlying scientific question, and it
does not make the decision binding.

## Core invariant

Decision Review **proposes; it never canonizes.** Decision History is a
`historical_record` authority surface (DEC-010); only the correct authority
surface (ROM §11 — an explicit user/authority acceptance) may append a binding
`DEC-NNN`. Every output of this workflow is a **patch-first decision proposal**
addressed to that acceptance step. Self-canonization — a workflow writing its own
binding rule — is the precise failure this workflow is built to prevent in itself.

## Conservative default

When a docket item is ambiguous, isolated (not yet recurring), under-evidenced, or
better owned by another workflow, the default is: **do not propose a decision,
preserve the docket item, route or hold cleanly.** A single occurrence is rarely
decision-worthy; Decision Review prefers to **hold for recurrence** over minting a
premature rule (consistent with ROM §1: avoid lock-in to local optima). If the
needed acceptance authority or owning workflow does not exist, it emits a docket
item with `signal_type: undefined-workflow-needed` and holds the candidate.

## Relationship to docket-triage (RESOLVED)

Other workflows route governance signals to "`govern/docket-triage`". This workflow
**reconciles that reference**: **`docket-triage` is a lightweight Phase-4 intake/
triage execution-atom that feeds Decision Review — not a separate workflow.**

Rationale for choosing (a) intake-atom over (b) separate-workflow:
- The docket has exactly one consumer that can act on a decision-worthy pattern:
  Decision Review (the only proposer of `DEC-NNN`). A separate triage *workflow*
  with its own authority boundaries would either duplicate Decision Review's
  judgment or add an empty hop.
- ROM §13 distinguishes workflow (protocol/authority) from task (bounded execution
  unit). Triage is bounded, mostly deterministic intake work (normalize, dedupe,
  cluster, recurrence-count, route the non-decision items back out) — exactly the
  profile of a **task atom**, not a constitutional protocol.
- DEC-013: a task atom **inherits** its workflow's authority and never exceeds it.
  `docket-triage` therefore inherits Decision Review's authority — it may sort and
  cluster docket items and hand decision-worthy clusters to the Decision Review
  judgment step, but it may **not** propose a `DEC-NNN` itself.

So in this design: **`govern/docket-triage` = the intake/triage atom of
Decision Review** (Phase 4). Until Phase 4 builds it, Decision Review performs that
intake inline (Procedure step 0–1). References to `docket-triage` in `line-review`,
`lifecycle-review`, and `portfolio-review` therefore resolve to *this workflow's
intake*, and no separate workflow needs to be created. This closes the open
reconciliation carried since DEC-017 / lifecycle-review Open Question #8. *(A
durable record of this resolution is itself a candidate `DEC-NNN` this workflow may
propose — see Open Questions.)*

## Decision-candidate taxonomy

A docket item becomes a **decision candidate** when it names a governance gap that a
durable rule would close. One run evaluates exactly one candidate, typically of:

```yaml
decision_candidate_type:
  - schema-inadequacy          # a registry/relationship vocabulary cannot express a needed state
  - promotion-threshold-needed # no accepted threshold for a promote/integrate/merge action
  - authority-conflict         # two surfaces conflict and no rule resolves precedence locally
  - policy-gap                 # a recurring decision the system keeps making ad hoc
  - undefined-workflow-needed  # a route has no owning workflow and one should exist
  - process-decision           # a change to how the program designs/governs itself (ROM §0)
```

Each maps to the same `DEC-NNN` proposal shape; the type only guides which authority
surfaces and prior decisions to check.

## Canonical decision-candidate encoding

Decision Review consumes the **governance docket item** shape emitted by the other
govern workflows (identical fields across line-review, lifecycle-review,
portfolio-review, line-intake):

```yaml
governance_docket_item:
  issue:
  affected_line:               # or affected_lines (portfolio) — may be empty for global policy
  signal_type:
  authority_surfaces_involved:
  why_<source>_cannot_resolve:
  recommended_owner_workflow:
  evidence_or_basis:
```

Intake normalizes `signal_type` values into `decision_candidate_type` and clusters
items that describe the **same** underlying governance gap (recurrence is the key
decision-worthiness signal).

## Authority boundaries

- **May:** read the whole governance docket, Decision History, the Research
  Operating Model, North Star, registries, and the workflow catalog; cluster and
  recurrence-count docket items; judge whether a clustered pattern is
  decision-worthy; draft a well-formed `DEC-NNN` **proposal** (patch-first); present
  it for human/authority acceptance with an explicit accept/reject/amend gate; route
  non-decision docket items to their correct owning workflow; emit `DEC-NNN`
  proposals that *recommend superseding* an existing decision (still acceptance-
  gated); preserve unresolved/held docket items; emit a Project Log entry text.
- **Must not:** append a binding `DEC-NNN` to Decision History itself (propose
  only — acceptance is an authority step, ROM §11); edit or delete existing
  Decision History entries (supersession is proposed, applied by the authority
  step; entries are never deleted — DEC schema); decide single-line standing
  (→ `line-review`), lifecycle moves (→ `lifecycle-review`), or cross-line
  structure (→ `portfolio-review`); create new research lines (→ `line-intake`);
  decide a claim is true/false; rewrite the Research Operating Model or North Star
  (it may *propose* a change to them as a `DEC-NNN`, never edit them); mint a rule
  from a single non-recurring occurrence without explicit justification.
- **Scoring authority — hybrid:** deterministic for recurrence counting,
  duplicate/cluster detection, signal-type normalization, and supersession-target
  validation; judgment (with rationale) for decision-worthiness and the drafted
  rule's wording/scope.
- **Write authority — patch-first; output_authority: decision_proposal.** Its
  highest-authority output is a *proposed* `DEC-NNN`, which is inert until accepted.

## Read surfaces

- **Governance docket** — the accumulated `governance_docket_item` set from
  line-review, lifecycle-review, portfolio-review, line-intake (Phase 4 names the
  concrete docket file; until then items travel with their source reports and are
  gathered at intake).
- **Decision History:** `registries/decision-history.md` — the canonical
  `DEC-NNN` record; read to assign the next number, check for an existing decision
  that already covers the pattern, and identify supersession targets. **Read-only
  here.**
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — authority order
  (§11), the process-as-object principle (§0), workflow/task split (§13), and the
  "conflicts are logged, never silently resolved" rule.
- **North Star:** `../NORTH-STAR.md` — top authority; a proposed decision must not
  contradict it (and if it implies a North Star change, that is itself the proposal).
- **Registries:** `line-registry.md`, `research-line-scorecard.md`,
  `persona-clusters.md`, `information-portfolio.md`, `foundation-queue.md` — to
  ground a candidate's evidence and check schema-inadequacy claims.
- **Workflow catalog / skeleton:** `README.md`, `WORKFLOW-SKELETON-PROPOSAL.md` —
  to validate route targets and check whether an `undefined-workflow-needed`
  candidate truly lacks an owner.
- **Project Log:** `PROJECT-LOG.md` — narrative context for whether a pattern recurs.
- **Govern Memory Pack load surface** (Phase 3.5; inert if absent).

## Write surfaces

- A **decision review report** (the run's primary artifact).
- A **`DEC-NNN` decision proposal** (patch-first) — a fully-drafted Decision History
  entry **addressed to an acceptance step**, never appended to the registry by this
  workflow. May propose `Status: active` *on acceptance* and may name a
  `Supersedes:` target (the actual append and any supersession edit are applied by
  the authority/accept step).
- **Routed docket items** → the correct owning workflow for any item that is not
  decision-worthy (e.g. a misfiled lifecycle question → `lifecycle-review`).
- **Governance docket items** of its own → for anything it cannot resolve (e.g. an
  acceptance authority that does not yet exist).
- A **Project Log entry** text (orchestrator appends to `PROJECT-LOG.md`).

**Patch target.** The only canonical surface a Decision Review output targets is
`registries/decision-history.md`, and only as a **proposal applied by an authority/
accept step** — never a direct write. Because Decision History is a Historical
Record (append-only, DEC-010), an accepted proposal *appends* a new `DEC-NNN`;
supersession marks the prior entry via the authority step, never deleting it.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): recurring decision-worthiness heuristics, prior
  premature-decision regrets, signal-type clustering patterns, known
  not-yet-decision-worthy issues.
- Writes (learning-return, after acceptance): `pack_ref`, `work_ref`, `round_ref`,
  `guidance_used`, `missing_guidance`, `confusion_or_conflict`,
  `observed_failure_mode`, `output_quality_signal`, `suggested_summary_update`.
- Does not depend on memory existing. The Memory Pack is guidance only and may
  never become the source of a decision (ROM §11: a memory-derived lesson that
  implies a higher-surface change is routed out as a proposal — i.e. *to this
  workflow* — and must not become policy by living in the pack).

## Registry interactions

- **Reads:** decision-history (next number, existing coverage, supersession
  targets), all registries (to ground evidence and verify schema-inadequacy /
  undefined-workflow claims).
- **Writes:** proposes a `DEC-NNN` to decision-history (patch-first; appended by an
  accept step, **not** by this workflow). Writes nothing else canonical.
- **Docket:** consumes the governance docket; re-emits routed and held items.

## Procedure (runnable scope: one decision candidate)

0. **Docket intake / triage** *(the `docket-triage` atom, inline until Phase 4).*
   Gather the accumulated governance docket items; normalize `signal_type` →
   `decision_candidate_type`; deduplicate; **cluster** items describing the same
   governance gap; count recurrence. Route any item that is not decision-worthy
   (misfiled lifecycle/standing/structure/intake questions) back to its owning
   workflow. Select **one** candidate (one clustered governance gap) for this run.
   On an empty or all-routed docket, emit a no-candidate report and stop.
1. **Load authority and decision context** — Decision History (full), Research
   Operating Model, North Star, the registries the candidate touches, the workflow
   catalog, Project Log. If required context is unavailable, emit
   `outcome_class: manual_review_required`.
2. **State the decision question precisely** — one question, one candidate. E.g.
   "Should the program adopt a numeric promotion threshold before a line may move to
   `primary-exploit`?" or "Should `docket-triage` be recorded as an intake atom of
   decision-review rather than a separate workflow?" The question must be explicit.
3. **Check for existing coverage and conflicts** — does an active `DEC-NNN` already
   decide this (then route as already-decided, no new proposal)? Does the candidate
   contradict North Star or the ROM (then the proposal must be a change *to* them,
   flagged high-scrutiny)? Is there a supersession target? Does ROM §11 actually
   leave this to a decision rather than to an existing authority surface?
4. **Test decision-worthiness** across: recurrence (how many independent docket
   items / runs raised it), durability (would a one-off note suffice instead?),
   scope (does it bind multiple workflows or the whole program?), reversibility
   (ROM §1 — prefer the rule that keeps the most landscape reachable), and evidence
   (is the gap demonstrated, not hypothetical?). If not yet decision-worthy →
   **hold for recurrence**, preserve the candidate, do not propose.
5. **Choose one primary outcome class:**

   ```yaml
   outcome_class:
     - decision_proposed            # a DEC-NNN proposal drafted and gated for acceptance
     - hold_for_recurrence          # plausible but not yet decision-worthy; preserved
     - already_decided              # an active DEC-NNN already covers it; route/close
     - routed_to_other_workflow     # not a decision; belongs to another govern workflow
     - schema_or_authority_escalation # needs a higher surface / missing acceptance authority
     - manual_review_required
   ```

   One is primary; when in doubt, choose `hold_for_recurrence` over proposing.
6. **Draft the `DEC-NNN` proposal** (if `decision_proposed`) using the exact
   Decision History entry schema, marked clearly as a **proposal**:

   ```markdown
   ## DEC-NNN — [Decision Title]   (PROPOSAL — inert until accepted)
   Date:                # date of acceptance, filled at accept step
   Status: active       # becomes active ONLY on acceptance
   Decision:
   Reason:
   Applies to:
   Supersedes:          # named target if any; applied by the accept step
   Superseded by: —
   Evidence / Source:   # docket items, runs, registries grounding the decision
   Notes:
   ```

   plus a proposal wrapper:

   ```yaml
   decision_proposal:
     proposed_dec_number:        # next available DEC number, read from decision-history
     decision_candidate_type:
     recurrence_count:
     decision_worthiness_rationale:
     supersedes:                 # existing DEC-NNN or —
     authority_check:            # North Star / ROM consistency; any high-scrutiny flag
     confidence: low | med | high
     requires_acceptance_by:     # the authority/accept step (human/authority; never this workflow)
     reversal_or_amendment_note:
     patch_required: true
   ```

7. **Gate for acceptance.** State the explicit accept / reject / amend choices. The
   proposal is **inert** until the authority step acts; this workflow records it as
   proposed, never as active.
8. **Route non-decision items** to their owning workflow and **emit any new docket
   items** for what it cannot resolve (e.g. acceptance authority undefined):

   ```yaml
   governance_docket_item:
     issue:
     affected_line:
     signal_type:
     authority_surfaces_involved:
     why_decision_review_cannot_resolve:
     recommended_owner_workflow:
     evidence_or_basis:
   ```

9. **Preserve the candidate** with `candidate_status`: proposed_pending_acceptance |
   held_for_recurrence | routed_to_other_workflow | rejected_with_rationale |
   already_decided. No candidate disappears silently.
10. **Emit report and Project Log entry text.** End with the verdict block.

## Outputs (shapes)

### Decision Review Report

```markdown
# Decision Review Report
## Review Metadata
- Workflow / version / run date / trigger / docket items considered / candidate selected:
## Docket Triage
- Items gathered / normalized / deduped / clusters / recurrence counts / items routed back out:
## Decision Question
- The one candidate / its decision_candidate_type:
## Existing-Coverage & Authority Check
- Active DEC already covering it? / North Star or ROM conflict? / supersession target? / is this even a decision (vs an existing surface)?:
## Decision-Worthiness Test
- Recurrence / durability / scope / reversibility / evidence:
## Outcome
- Outcome class / rationale / confidence:
## Decision Proposal (if any)
- The drafted DEC-NNN proposal (inert) + proposal wrapper / requires acceptance by:
## Routed / Held Items
- Non-decision items routed out / items held for recurrence:
## Governance Docket Items Emitted
- New items (with signal_type):
## Candidate Disposition
- Candidate status / where preserved or routed:
## Project Log Entry
- Summary / output pointers:
```

Every run ends with the verdict block.

## Escalation triggers

Escalate rather than act when: the candidate contradicts North Star or the ROM
(→ high-scrutiny proposal explicitly framed as a change to that surface, never an
edit); no acceptance authority exists to make the decision binding
(→ `undefined-workflow-needed` / `manual-review-required`); the docket item is
actually a single-line / lifecycle / structural / intake question
(→ route to the owning workflow, do not propose); an active `DEC-NNN` already
covers it (→ already-decided, route/close); the candidate is plausible but not yet
recurring (→ hold for recurrence); two authority surfaces conflict and resolving
precedence would itself require a North Star / ROM change (→ high-scrutiny).

## Failure modes

- **Self-canonization** (writing a binding `DEC-NNN` directly). Guard: propose-only;
  Decision History append is an authority/accept step (ROM §11); the core invariant.
- **Premature rule from a one-off.** Guard: decision-worthiness test requires
  recurrence/durability/scope; default is hold-for-recurrence.
- **Duplicate decision** (re-deciding something an active DEC already covers).
  Guard: existing-coverage check reads full Decision History first.
- **Editing or deleting prior decisions.** Guard: Decision History is append-only;
  supersession is *proposed* and applied by the accept step; entries are never
  deleted.
- **Authority inversion** (a Memory Pack lesson becoming policy by living in the
  pack). Guard: memory is guidance only; policy-class lessons arrive here as
  proposals and still face the acceptance gate (ROM §11).
- **Scope creep into other govern workflows** (deciding a lifecycle/structure
  question under cover of a "decision"). Guard: route non-decision items out;
  authority boundaries.
- **Contradicting North Star/ROM silently.** Guard: authority check; any conflict
  becomes an explicit, high-scrutiny proposal *to change* that surface, logged not
  hidden.
- **Docket loss.** Guard: every item is routed, held, proposed, or rejected with a
  recorded `candidate_status`.
- **Dangling route.** Guard: emit `undefined-workflow-needed`, hold the candidate.
- **docket-triage drift** (someone rebuilding it as a separate authority). Guard:
  this file fixes `docket-triage` as decision-review's inherited-authority intake
  atom (DEC-013); it may sort/cluster but never propose a `DEC-NNN`.

## Success criteria

A good run yields, for one decision candidate: a clear statement of the governance
gap, evidence it recurs, a check that no active decision already covers it, a check
that it does not silently contradict a higher surface, and — if decision-worthy — a
fully-drafted `DEC-NNN` proposal a human can accept, reject, or amend in one read,
explicitly inert until accepted. Non-decision items are routed to their owners and
no docket item is lost.

Cheap auditability test: a reviewer can tell, without re-reading every prior run,
why this candidate was judged decision-worthy (or held), what the proposed rule
says and what it supersedes, that the proposal is not yet binding, and where every
non-decision docket item went.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/docket-triage` — **the intake/triage atom of this workflow** (see the
  reconciliation section): gather → normalize → dedupe → cluster → recurrence-count
  → route non-decision items out → hand one decision-worthy cluster to the judgment
  atom. Mostly deterministic; inherits decision-review's authority; **may not
  propose a `DEC-NNN`.**
- `govern/decision-worthiness-judgment` — one clustered candidate → outcome class +
  rationale; judgment-based.
- `govern/decision-proposal-draft` — one decision-worthy candidate → drafted
  `DEC-NNN` proposal (inert) + acceptance gate; judgment-based.
- `govern/decision-acceptance` — one accepted proposal → append `DEC-NNN` +
  supersession edit + Project Log; **requires explicit authority** (the only atom
  that touches canonical Decision History; never auto-runs).

Likely cadence: periodic / accumulated (the docket fills slowly); acceptance is
strictly human/authority-triggered, never scheduled.

Likely context boundaries: the triage atom loads the docket + workflow catalog;
the judgment/draft atoms additionally load full Decision History, ROM, North Star,
and the touched registries; the acceptance atom loads only the accepted proposal
and Decision History.

Likely deterministic vs judgment split:
- Deterministic: docket normalization, dedupe/clustering, recurrence counting,
  next-DEC-number assignment, existing-coverage lookup, supersession-target
  validation.
- Judgment-based: decision-worthiness, the rule's wording/scope, North Star/ROM
  consistency, supersession recommendation.

Phase 4 coverage questions:
- Does every docket item get triaged (routed, held, proposed, or rejected)?
- Is `docket-triage` strictly an atom that cannot propose a `DEC-NNN`?
- Does every proposed decision have an explicit accept/reject/amend gate?
- Is the acceptance atom the only thing that writes canonical Decision History?
- Is supersession always proposed (never a delete)?
- Does any proposal contradict North Star/ROM without being flagged high-scrutiny?
- Does every recurrence-worthy pattern eventually reach a decision or an explicit
  hold?
- Is anything decided here that belongs to line/lifecycle/portfolio/intake review?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Authority basis:
Risks:
Decision-worthiness (recurrence / scope / reversibility):
What would change this recommendation:
Decision proposed (DEC-NNN, inert until accepted):
Requires acceptance by:
Escalation required:
Candidate disposition:
```

## Open questions

1. **Acceptance authority.** Who is the authority/accept step that turns a proposed
   `DEC-NNN` into an active one — Joe directly, a dedicated `decision-acceptance`
   atom under explicit human trigger, or both? Until set, every proposal is inert
   and acceptance is manual (the conservative default). Docketed:
   `signal_type: undefined-workflow-needed` (acceptance step) → held.
   **(Non-lock-gating: propose-only invariant holds regardless of who accepts.)**
2. **docket-triage record.** This workflow *recommends* recording the docket-triage
   resolution (intake atom of decision-review, not a separate workflow) as a durable
   `DEC-NNN`, superseding the open reconciliation from DEC-017 and lifecycle-review
   Open Question #8. Drafted as a candidate proposal for the orchestrator/human to
   accept; this workflow does not self-append it. **(Non-lock-gating: the resolution
   is documented and operative in this file; canonization is a proposal.)**
3. **Recurrence threshold.** No numeric count yet defines "recurring enough to
   decide." Until set, decision-worthiness is judgment-with-rationale. Docketed:
   `signal_type: promotion-threshold-needed` (applied to decisions themselves).
   **(Non-lock-gating.)**
4. **Concrete docket file location.** Shared with line-review / lifecycle-review /
   portfolio-review — where docket items physically accumulate (a
   `registries/governance-docket.md` vs traveling with reports). A Phase-4 plumbing
   choice. **(Non-lock-gating.)**
