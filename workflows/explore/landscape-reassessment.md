---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: topology_assessment_and_lifecycle_candidate_proposal
summarizable: false
unit_of_review: one_landscape_reassessment
---

# Landscape Reassessment

**Family:** explore
**Mode:** both (search to re-imagine the topology; evaluation to test whether the
re-survey holds against current evidence)
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** the **whole** research-line landscape (the line graph + standing +
recent exploration), not a single line.
**Emits:** a topology-assessment snapshot; `lifecycle_candidate`s →
`govern/lifecycle-review`; reprioritization signals; discovery prompts for
under-covered regions → `explore/line-discovery`.

## Purpose

Re-survey the **topology of the whole research-line landscape** given everything
the program now knows, and ask the operating model's highest-value periodic
question (§2): *has the landscape itself shifted?* Which regions are now promoted,
which have collapsed, which adjacencies have opened, and **is the current primary
research line still on the most promising ridge?** Reassessment is the program's
main defense against optimizing hard inside a landscape that has quietly moved.

Reassessment is explicitly **distinct from `explore/cross-disciplinary-synthesis`**
and the constraint is constitutional (operating model §2). Synthesis asks *what
patterns connect what we already have* (content-level pattern-finding).
Reassessment asks *how the topology of the landscape has changed* (structure-level
re-survey of the line graph and the program's bets). Synthesis can *feed*
reassessment; it cannot *be* it. Reassessment consumes synthesis output as one
input among many.

This is a **both-Mode** workflow and must name the mode per phase: Search Mode when
re-imagining the topology (entertaining that the primary ridge may be wrong,
generating where the landscape may have shifted); Evaluation Mode when testing each
proposed topology change against current standing and evidence before emitting it.

Reassessment **proposes**; it never acts. It can recommend that a line be promoted,
demoted, held, or revived — but every such recommendation is a `lifecycle_candidate`
for `govern/lifecycle-review`. It can recommend new exploration in an under-covered
region — but that is a prompt to `explore/line-discovery`. It changes no canonical
state and scores no individual line's standing (that is `govern/line-review`).

## Authority boundaries

- **May:** read the whole line graph, standing snapshots, health substrate, recent
  exploration, and synthesis output; assess how the topology has changed; judge
  whether the primary line is still on the best ridge; emit lifecycle candidates;
  emit reprioritization signals; prompt discovery for under-covered regions; emit
  governance signals for missing routes.
- **Must not:** move any lifecycle stage/status (→ `govern/lifecycle-review`);
  perform whole-portfolio *reconciliation* of overlaps/splits/merges
  (→ `govern/portfolio-review`); score an individual line's standing
  (→ `govern/line-review`); register a line (→ discovery/intake); decide claims
  true/false; reallocate the actual research budget (it signals; allocation is a
  govern/human decision); conflate itself with synthesis.
- **Scoring authority:** judgment-with-rationale, topology-level — it characterizes
  *regions* and *ridges* and the *relative position of bets*, not per-line standing
  scores (which it reads as input from line-review).
- **Write authority:** patch-first / proposal-only. The topology assessment is a
  non-canonical snapshot; lifecycle candidates and reprioritization signals are
  proposals; no canonical registry write.

## Read surfaces

- **The whole line graph:** `registries/line-registry.md` — all `RL-NNN`, their
  stages, statuses, relationships (depends_on/supports/competes_with/extends/
  imports), why-state, and which is currently primary.
- **Standing (per-line input):** the latest `govern/line-review` standing snapshots
  in `logs/`, and `registries/research-line-scorecard.md` (health substrate).
- **Recent exploration & synthesis:** `logs/synthesis/` convergence maps,
  incubation reports, foundation `literature/` notes — what new knowledge could have
  moved the topology.
- **Information portfolio:** `govern/information-portfolio` entries — what the
  program has *learned* (including from failures, §3), which is the substance of a
  topology shift.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — reassessment-vs-
  synthesis (§2), both-Mode discipline (§1), lifecycle (§4), promotion/demotion
  (§5), cross-cluster reasoning (§8), authority order (§11).
- **Decision History:** `registries/decision-history.md` — constraints, prior
  reassessments, the two-axis model (DEC-018).
- **Authority surfaces (context):** `../NORTH-STAR.md`, `CLAIM-LEDGER.md`,
  `ROADMAP.md`, `HYPOTHESES.md`.
- **Workflow catalog:** `README.md` / `WORKFLOW-SKELETON-PROPOSAL.md` — validate routes.
- Explore Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- A **topology-assessment snapshot** (operational log) to `logs/` — non-canonical
  record of how the landscape now looks and what changed since the last reassessment.
- **`lifecycle_candidate`s** → `govern/lifecycle-review`.
- **Reprioritization signals** (which regions/lines deserve more or less budget) →
  the docket / a govern allocation review (signal only).
- **Discovery prompts** for under-covered regions → `explore/line-discovery`.
- **Portfolio-structure flags** (overlaps/splits/merges spotted at topology level) →
  `govern/portfolio-review`.
- **Governance signals** → the docket.

**No canonical write.** Every consequential recommendation is a candidate/signal to
an owning workflow.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): the prior topology snapshot (the diff baseline), recurring
  "false topology shift" patterns, prior reassessment cadence/quality notes.
- Writes (learning-return, after a run): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** `line-registry.md` (whole graph), `research-line-scorecard.md`,
  standing snapshots, `information-portfolio`, `decision-history.md`.
- **Writes:** none to canonical state. Topology snapshot → log; lifecycle
  candidates → lifecycle-review; prompts/signals routed; appends a run log.

## Procedure (runnable scope: one whole-landscape reassessment)

1. **Load the landscape and the baseline.** Read the full line graph, current
   standing, the information portfolio, recent synthesis/exploration, and the prior
   topology snapshot (the diff baseline). Confirm this is a *topology* run, not a
   synthesis run.
2. **(Search Mode) Re-imagine the topology.** Treating the current bets as provisional,
   ask where the landscape may have moved: which regions look stronger/weaker now,
   which adjacencies opened (often from new convergences or ingested neighbors),
   which look collapsed, and — explicitly — *whether the primary line is still on the
   best ridge*. Generate the candidate re-survey freely.
3. **(Evaluation Mode) Test each proposed shift.** For each topology change, check it
   against current standing, the information portfolio, and authority surfaces. Keep
   only shifts the evidence supports; record rejected re-survey ideas as information.
4. **Diff against the baseline.** State what changed since the last reassessment:
   promoted regions, collapsed regions, new adjacencies, ridge-position of the
   primary line. A reassessment with *no* change is a valid, informative outcome.
5. **Derive consequences and route them.** For each supported shift: emit a
   `lifecycle_candidate` (promote/demote/hold/revive) to lifecycle-review; a
   reprioritization signal; a discovery prompt for an under-covered region; or a
   portfolio-structure flag for overlaps/splits/merges.
6. **Emit.** Topology snapshot, lifecycle candidates, reprioritization signals,
   discovery prompts, portfolio flags, run log, governance signals. End with the
   verdict block.

## Outputs (shapes)

**Topology-assessment snapshot** (log): per-region read (strengthened | weakened |
collapsed | newly-opened), the ridge-position read of the primary line (still-best |
challenged-by:<RL-NNN> | off-ridge), the diff vs the prior snapshot, and the
evidence basis for each call. Non-canonical.

**Lifecycle candidate** (per supported shift; encoded per `govern/lifecycle-review`'s
canonical schema):

```yaml
lifecycle_candidate:
  candidate_type: promote | demote | hold | revive
  affected_line:
  current_state:
  proposed_state_or_direction:
  reason:                        # the topology shift that motivates it
  evidence_or_basis:             # standing + information-portfolio + synthesis cited
  source_workflow: explore/landscape-reassessment
  source_report:                 # topology snapshot pointer
  confidence: low | med | high
  why_source_workflow_cannot_decide: "reassessment surveys topology but must not move lifecycle (DEC-018); lifecycle-review owns the move."
```

**Reprioritization signal** / **discovery prompt** / **portfolio flag**: short
routed objects naming the region/line, the topology basis, and the owning workflow.

**Governance docket item** (missing route / cadence/policy gap): standard shape with
`signal_type` ∈ {undefined-workflow-needed, reassessment-cadence-needed,
topology-threshold-needed, manual-review-required}.

Every run ends with the verdict block.

## Escalation triggers

Route OUT: any stage/status change → `govern/lifecycle-review`; overlap/split/merge
spotted at topology level → `govern/portfolio-review`; an under-covered region →
`explore/line-discovery`; a finding that is really a content-level pattern, not a
topology change → `explore/cross-disciplinary-synthesis` (do not absorb synthesis);
per-line standing questions → `govern/line-review`; budget reallocation → a govern
allocation review / human (signal only); missing route →
`undefined-workflow-needed`; registry/authority conflict → `confusion_or_conflict`,
defer to §11.

## Failure modes

- **Reassessment/synthesis conflation.** The run starts pattern-finding over content
  instead of re-surveying topology. Guard: the constitutional §2 distinction;
  topology run is declared in step 1; content patterns route to synthesis.
- **Acting on the topology (moving lifecycle / reallocating budget).** Guard:
  proposal-only; lifecycle → lifecycle-review; budget → allocation review/human.
- **Mode blur.** Re-imagining and testing run together so weak shifts survive.
  Guard: name the mode per phase; the Evaluation pass must reject unsupported shifts.
- **Phantom shift / churn.** Declaring topology change every run to look productive.
  Guard: diff against the prior snapshot; "no change" is a valid outcome; require an
  evidence basis per shift.
- **Anchoring on the current primary.** The re-survey never seriously questions the
  primary ridge. Guard: step 2 *requires* an explicit ridge-position call on the
  primary line.
- **Swallowing portfolio-review.** Reassessment performs splits/merges itself.
  Guard: structural reconciliation routes to `govern/portfolio-review`.
- **Dangling route.** Guard: `undefined-workflow-needed`; preserve in the snapshot.

## Success criteria

A good run produces a **whole-landscape topology read** that honestly diffs against
the prior one, makes an explicit call on whether the primary line is still on the
best ridge, and routes every consequence (lifecycle, reprioritization, discovery,
portfolio) to its owning workflow — without itself moving any state, and without
sliding into synthesis.

Cheap test: a reviewer can tell, without re-deriving it, how the landscape changed
since the last reassessment, whether the primary line is still best-placed and on
what evidence, and which workflow owns each recommended consequence.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `explore/reassessment-landscape-load` — assemble the line graph + standing +
  portfolio + prior snapshot; **mostly deterministic**.
- `explore/reassessment-topology-survey` — (Search) re-imagine topology + ridge call;
  judgment-based; expensive.
- `explore/reassessment-shift-test` — (Evaluation) test each proposed shift vs
  evidence; judgment-based.
- `explore/reassessment-route` — supported shifts → lifecycle candidates /
  reprioritization / discovery prompts / portfolio flags; deterministic packaging.

Likely cadence differences:
- **Periodic** (this is the program's main periodic move, §2) and event-triggered
  after a major synthesis convergence, a big foundation ingestion, or a primary-line
  result that could move the ridge.

Likely context boundaries:
- Load loads the whole graph + snapshots (the one workflow that legitimately needs a
  *whole-landscape* view); survey/test operate on the loaded landscape; route loads
  only the supported-shift list. Per-line deep artifacts loaded only on demand.

Likely deterministic vs judgment split:
- Deterministic: landscape assembly, diff-vs-prior-snapshot, route-target existence,
  detecting that a "shift" lacks an evidence basis.
- Judgment-based: the topology survey, the ridge-position call, shift testing,
  reprioritization.

Phase 4 coverage questions:
- Does every supported shift have a downstream consumer? (lifecycle / portfolio /
  discovery / allocation.)
- Does every run diff against the prior snapshot (including "no change")?
- Does every run make an explicit primary-ridge call?
- Is reassessment kept distinct from synthesis (no content-pattern double-work)?
- Is the whole-landscape load the only legitimately broad context, and bounded?
- Is any unit too large for one agent run? (the survey over a large graph is the seam.)

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Reassessment cadence** — how often is the whole-landscape re-survey run
   (periodic interval + which events trigger it)? (Docketed: `reassessment-cadence-
   needed`; a Phase 4 schedule question.)
2. **Topology-shift threshold** — how much movement justifies declaring a region
   promoted/collapsed or the primary ridge "challenged"? (Docketed: `topology-
   threshold-needed`.)
3. **Reprioritization sink** — which govern workflow owns budget reallocation
   signals (a future allocation review vs docket-triage vs decision-review)?
   Reconcile with the govern-family sinks.
4. **portfolio-review boundary** — exact line between a topology-level structural
   *flag* (here) and structural *reconciliation* (portfolio-review).
