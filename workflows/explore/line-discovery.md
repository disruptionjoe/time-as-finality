---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: candidate_seed_proposal
summarizable: false
unit_of_review: one_discovery_run
---

# Line Discovery

**Family:** explore
**Mode:** search
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** current registry state, recent exploration outputs, and (optionally)
a `persona-idea-sprint` run.
**Emits:** `candidate_seed` proposals → `govern/line-intake` (which registers).

## Purpose

Widen the program's reachable search space by **generating and proposing
candidate research lines** that do not yet exist in `line-registry.md`. Discovery
exists to fight the local-optimum trap named in the operating model §1: it spends
budget on *possibility generation* so that exploitation never runs out of distant,
unexplored ridges to compare against.

Discovery **proposes**; it never creates registry state. The boundary is
deliberate and mirrors line-review/lifecycle-review: the workflow that *finds* a
candidate is not the workflow that *commits* it. Registration of a new `RL-NNN`
belongs to `govern/line-intake` (DEC-017). Discovery's output is a set of
well-formed `candidate_seed` objects that intake can accept, reject, merge into an
existing line, or send back for sharpening.

This is a **Search Mode** workflow (operating model §1): it maximizes diversity,
novelty, and information-gain potential, and it must not silently switch into
evaluation. It does not rank lines for promotion, score standing, or decide truth.

## Authority boundaries

- **May:** read registry + exploration state; invoke the `persona-idea-sprint`
  skill (or read its prior outputs); generate candidate research lines; cluster
  and de-duplicate candidates against existing lines; propose `candidate_seed`
  objects to `govern/line-intake`; record a discovery run log; flag a candidate as
  a possible duplicate/overlap of an existing line; emit governance signals for
  missing routes.
- **Must not:** create, register, or number a research line (→ `govern/line-intake`);
  edit `line-registry.md` canonical state; move any lifecycle stage or status
  (→ `govern/lifecycle-review`); assign standing scores (→ `govern/line-review`);
  decide a candidate is true/false or promote it; add personas (→
  `explore/persona-expansion`); declare a synthesis convergence as a finding (that
  is `explore/cross-disciplinary-synthesis`'s output, which discovery may *consume*).
- **Scoring authority:** judgment-with-rationale. Discovery may attach **cheap
  promise heuristics** (novelty, distance-from-existing-lines, cross-cluster
  reach, plausible-next-test) to help intake triage, but these are *not* standing
  scores and carry no lifecycle authority.
- **Write authority:** patch-first for the discovery run log (append) and for the
  candidate-seed bundle routed to intake; **no direct write** to any canonical
  registry.

## Read surfaces

- **Registry state (de-dup):** `registries/line-registry.md` — what lines already
  exist, their stages, relationships, and why-state, so discovery does not
  re-propose what is already tracked.
- **Recent exploration outputs:** `explorations/` (prior sprint runs, backlog),
  recent `logs/synthesis/`, prior discovery run logs.
- **Idea-generation machinery:** `agent-skills/persona-idea-sprint.md` /
  `.js` and `agent-skills/time-as-finality-persona-panel/` — invoked or read, not
  reimplemented.
- **Cluster map (breadth check):** `registries/persona-clusters.md` — to judge
  cross-cluster reach of a candidate.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — Search-Mode stance
  (§1), explore posture (§2), information-gain philosophy (§3), authority order (§11).
- **Decision History:** `registries/decision-history.md` — active constraints and
  to avoid re-proposing archived lines without a revival basis.
- **Authority surfaces (context only):** `../NORTH-STAR.md`, `CLAIM-LEDGER.md`,
  `ROADMAP.md`, `HYPOTHESES.md` — to anchor candidates to real gaps, not restate status.
- **Workflow catalog:** `README.md` / `WORKFLOW-SKELETON-PROPOSAL.md` — to validate
  route targets and avoid dangling routes.
- Explore Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- A **discovery run log** (operational log) to `logs/` — non-canonical record of
  what was generated, what was de-duped, and what was proposed.
- A **candidate-seed bundle** routed to `govern/line-intake` — the proposal, never
  a registry write.
- **Governance signals** → the docket (`govern/decision-review` (docket intake), later) when a route
  target is missing or a candidate exposes a policy gap.

**No patch back into canonical state.** Discovery never writes `RL-NNN` entries.
If a candidate clearly belongs as a relationship/edit on an *existing* line, that
is flagged to intake/line-review, not applied here.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): recurring duplicate-candidate patterns, idea families that
  have repeatedly failed intake, prior "discovery drift" notes (e.g. generating
  restatements of the primary line).
- Writes (learning-return, after a run): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** `line-registry.md` (de-dup), `persona-clusters.md` (breadth),
  `decision-history.md` (constraints/archived lines).
- **Writes:** none to canonical registries. Proposes `candidate_seed` objects to
  `govern/line-intake`; appends a run log.

## Procedure (runnable scope: one discovery run)

1. **Frame the gap (cheap precondition).** State what region of the search space
   this run targets and why — e.g. "under-covered adjacency flagged by
   landscape-reassessment", "free-form widening", or a `focus` argument. Read the
   current registry so generation is grounded against what exists.
2. **Generate.** Either invoke the `persona-idea-sprint` skill (preferred for
   breadth — it already produces a cross-persona convergence map) or read a recent
   sprint output, or run a lighter free-form generation. Capture raw candidates.
3. **De-duplicate and cluster.** For each raw candidate, check it against existing
   `RL-NNN` lines and archived lines. Mark each as: `novel`, `overlaps-RL-NNN`
   (refine-or-fold), or `restates-RL-NNN` (discard, log why). Group survivors by
   the cluster(s) that would care about them.
4. **Attach cheap promise heuristics** (judgment, with rationale) so intake can
   triage — not standing scores:

   ```yaml
   promise_heuristics:
     novelty: low | med | high          # absent from existing repo state
     cross_cluster_reach: low | med | high  # how many distant clusters would care
     plausible_next_test: <one concrete bounded move, or "none yet">
     information_gain_if_wrong: <what the program would learn even on failure>
   ```
5. **Emit candidate seeds** (the deliverable) and route to `govern/line-intake`.
   End with the verdict block.

## Outputs (shapes)

**Candidate seed** (one per proposed line; the routed deliverable):

```yaml
candidate_seed:
  working_title:
  one_line_claim:            # what this line would assert or investigate
  why_not_already_covered:   # de-dup basis vs existing/archived lines
  origin:                    # persona-idea-sprint | synthesis-handoff | free-form | focus:<x>
  source_report:             # sprint/synthesis run pointer, if any
  related_existing_lines:    # depends_on / supports / competes_with / extends / imports (proposed)
  promise_heuristics: { novelty:, cross_cluster_reach:, plausible_next_test:, information_gain_if_wrong: }
  recommended_intake_action: register | merge_into:<RL-NNN> | sharpen_then_register | reject
  confidence: low | med | high
```

**Discovery run log** (operational log): run date, trigger/focus, generation
method, raw-count, de-dup results, candidate-seed list, routes emitted.

**Governance docket item** (when a route is missing or a policy gap appears):

```yaml
governance_docket_item:
  issue:
  signal_type:   # undefined-workflow-needed | seed-threshold-needed | duplicate-policy-gap | manual-review-required
  authority_surfaces_involved:
  why_line_discovery_cannot_resolve:
  recommended_owner_workflow:
  evidence_or_basis:
```

Every run ends with the verdict block.

## Escalation triggers

Route OUT (never act unilaterally): a candidate that should become a line →
`govern/line-intake`; a candidate that is really an *edit/relationship* on an
existing line → `govern/line-intake` (or flag for `govern/line-review`); a
candidate that looks like a cross-cluster convergence rather than a single seed →
`explore/cross-disciplinary-synthesis`; a candidate requiring a new persona lens →
`explore/persona-expansion`; reviving an archived line → note the
`revival condition` and route to `govern/lifecycle-review` (revive), not a new
seed; missing route target → docket `undefined-workflow-needed`; registry/authority
conflict → log as `confusion_or_conflict` and defer to the authority surface (§11).

## Failure modes

- **Discovery drift (restating the primary line).** Many "new" candidates are
  RL-001/RL-002 in fresh vocabulary. Guard: de-dup step 3 is mandatory; restatements
  are discarded with logged rationale; the run log reports the novel fraction.
- **Search→evaluation leak.** Discovery starts ranking lines for promotion. Guard:
  Search Mode declared; promise heuristics are explicitly *not* standing scores and
  carry no lifecycle authority.
- **Authority creep (creating lines).** Guard: no canonical registry write; all
  candidates route to `govern/line-intake`.
- **Manufactured convergence.** Same-vocabulary persona agreement read as a real
  cross-cluster signal. Guard: defer convergence claims to
  `cross-disciplinary-synthesis`; here, convergence is at most an `origin` tag.
- **Silent candidate loss.** Generated candidates vanish without disposition.
  Guard: every raw candidate gets a status in the run log (novel/overlap/restate).
- **Dangling route.** Guard: emit `undefined-workflow-needed`, preserve the
  candidate in the run log.

## Success criteria

A good run yields a small set of **genuinely novel, well-formed candidate seeds**
that intake can triage quickly, each with a defensible de-dup basis and at least
one plausible next move or stated information-gain-if-wrong — and it widens the
landscape rather than re-describing the current frontier.

Cheap test: a reviewer can tell, without re-reading the whole registry, *which*
candidates are new (vs restatements of existing lines), why each is worth
registering, and what `govern/line-intake` should do with each — and the run log
reports what fraction of generated candidates were novel vs duplicates.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `explore/discovery-generation` — one generation pass (sprint invocation or
  free-form); emits raw candidates; judgment-based, possibly expensive.
- `explore/discovery-dedup` — raw candidates vs registry; emits novel/overlap/
  restate classification; **largely deterministic** (string/semantic match against
  existing + archived lines).
- `explore/discovery-seed-emit` — survivors → `candidate_seed` bundle + run log;
  judgment for heuristics, deterministic for packaging.

Likely cadence differences:
- Periodic widening (low cadence) to keep the search space fresh.
- Event-triggered when `landscape-reassessment` flags an under-covered region, or
  when the active frontier narrows and a comparison ridge is wanted.

Likely context boundaries:
- Generation loads the theory surfaces + sprint machinery; de-dup loads only the
  registry + archived lines; emit loads only survivors. The full panel is invoked
  via the skill, not inlined.

Likely deterministic vs judgment split:
- Deterministic: de-dup matching, duplicate/restate flags, run-log assembly,
  route-target existence checks.
- Judgment-based: candidate generation, novelty/reach heuristics,
  recommended-intake-action.

Phase 4 coverage questions:
- Does every candidate seed have a destination? (→ `govern/line-intake`.)
- Does every raw candidate get a disposition in the run log?
- Does every governance signal have a destination?
- Is generation (expensive) cleanly separable from de-dup (cheap) for cadence?
- Is anything reviewed twice by competing tasks? (discovery proposes; intake
  decides; they must not both register.)

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Seed threshold / cap per run** — how many candidate seeds is a healthy run,
   and what novelty floor justifies emitting one? (Docketed: `seed-threshold-needed`.)
2. **Duplicate policy** — when a candidate overlaps an existing line, default to
   `merge_into` vs `sharpen_then_register`? Shared with `govern/line-intake`.
   (Docketed: `duplicate-policy-gap`.)
3. **line-intake existence** — `govern/line-intake` is sequenced (DEC-017) but not
   yet locked; until it exists, candidate seeds route there as `undefined-workflow-
   needed` and are preserved in the run log.
4. **Sprint output reuse vs fresh run** — when may a recent `persona-idea-sprint`
   output be reused rather than re-invoked? (cost vs freshness; defer to Phase 4
   cadence.)
