---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: persona_registry_patch_proposal
summarizable: false
unit_of_review: one_persona_or_cluster_change
---

# Persona Governance

**Family:** govern
**Mode:** both (search when proposing coverage; evaluation when re-clustering)
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** coverage-gap signals and cluster-integrity flags from
`govern/line-review`, `explore/persona-expansion`, scoring runs that surfaced an
under-represented discipline, and the standing open question in
`registries/persona-clusters.md` (unmapped personas 19, 20, 28, 29, 30, 33, 44).
**Scope:** Evaluate **one** persona-or-cluster change — a single persona's
cluster assignment, one cluster definition change, one normalization-weight
change, or one mirror-sync reconciliation — and propose it patch-first.

## Purpose

Keep the persona system a **fair, legible scoring substrate**: maintain the
discipline clustering, the cross-cluster weighting/normalization that lets
breadth across distant clusters outweigh raw headcount (operating model §7–§8),
and registry integrity across the canonical panel, the cluster map, and the lens
index. It keeps `personas/EXPERT-PANEL.md` canonical (DEC-006) and the panel
skill mirror in sync, and it owns the **persona-cluster coverage-gap decision** —
which it does not decide itself but routes to `govern/decision-review`.

The governance meaning: personas are reusable review postures, never authorities
or evidence by themselves (operating model §6; `personas/INDEX.md`). This
workflow protects that — it tunes *how persona signal is weighted and grouped*,
never *what a persona concludes*.

## Governing decisions (preserve)

- **`personas/EXPERT-PANEL.md` is canonical** for the numbered personas (DEC-006);
  the skill's `references/personas.md` is a **mirror**, and
  `scripts/build_panel_prompt.py` reads the canonical file. Edits originate at the
  canonical file; the mirror is reconciled, never hand-authored as a source.
- **Clustering is a scoring-time concern layered on top of `personas/INDEX.md`**,
  expected to evolve; it is not baked into the lens index (operating model §6).
- **Seven clusters** are the current basis (math/formalism; physics/decoherence;
  distributed-systems/consensus; information/networking; sheaf/category/geometry;
  simulation/MMO/game-mechanism; philosophy/testability/skepticism).
- **Adding coverage extends, never replaces, the existing list** (operating model
  §6): new personas are added as numbered personas + a lens family, preserving
  historical numbering (EXPERT-PANEL "Panel Evolution"); existing personas are
  rarely removed — deprecate/merge/supersede instead.
- **Normalization weighs breadth across *distant* clusters**, protects informed
  minorities via survival arguments, and never lets one homogeneous cluster
  dominate by headcount (operating model §5, §7–§8).
- **Adding/expanding the persona set is an Explore workflow** (`persona-expansion`),
  not this one. Persona Governance maintains the *clustering, weighting, and
  registry integrity*; it does not author new disciplinary lenses.

## Authority boundaries

- **May:** read the persona registries and canonical panel; propose one persona's
  primary-cluster assignment; propose one cluster definition or rename; propose a
  cross-cluster normalization-weight rule change; flag mirror drift and propose a
  reconciliation patch to the skill mirror; flag registry-integrity issues
  (unmapped persona, duplicate, broken cross-reference, numbering gap); raise the
  coverage-gap decision as a routed signal; route persona-set expansion to
  `explore/persona-expansion`.
- **Must not:** invent a replacement persona list; delete a persona (deprecate/
  supersede via patch instead); author new disciplinary personas (→
  `explore/persona-expansion`); **decide** whether to add an eighth cluster or
  accept best-fit (→ `govern/decision-review`); edit `personas/INDEX.md` lens
  *definitions* as physics rather than method; change scoring *conclusions* or any
  persona's vote; hand-edit the skill mirror as a source of truth; rewrite the
  operating model or Decision History; treat persona output as evidence or
  authority by itself.
- **Scoring authority:** judgment-with-rationale for cluster assignment and weight
  rules; deterministic for mirror-sync and integrity checks (diff/parse).
- **Write authority — patch-first.** Patch-first to
  `registries/persona-clusters.md`. **Proposes (does not apply)** changes to
  `personas/` via patch; an authority/accept step applies them, and the skill
  mirror is reconciled only after the canonical panel is accepted.

## Read surfaces

- **Cluster registry:** `registries/persona-clusters.md` (the scoring-time view).
- **Canonical panel:** `personas/EXPERT-PANEL.md` (numbered personas 1–62).
- **Lens index:** `personas/INDEX.md` (review postures; lens families).
- **Skill mirror:** `agent-skills/time-as-finality-persona-panel/references/personas.md`
  and `scripts/build_panel_prompt.py` (to detect mirror drift).
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — §5, §6, §7, §8
  (persona/voting/cross-cluster rules) and §11 (authority order).
- **Decision History:** `registries/decision-history.md` — DEC-006 and any active
  persona constraints, and to validate that a proposed change is not already
  decided.
- **Workflow catalog / skeleton:** `README.md`, `WORKFLOW-SKELETON-PROPOSAL.md` —
  to validate route targets and avoid routing to workflows that do not exist.
- Govern Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- A **persona-governance report** (audit artifact) to `logs/runs/` — non-canonical.
- A **patch proposal** to `registries/persona-clusters.md` (cluster assignment,
  cluster definition, normalization-weight rule) — patch-first, applied by an
  authority/accept step, not by this workflow.
- A **mirror-reconciliation patch proposal** for the skill mirror — applied only
  after the canonical panel change (if any) is accepted; never authored as source.
- A **persona patch proposal** to `personas/` (deprecate/supersede/renumber note,
  cross-reference fix) — proposed, not applied.
- **Coverage-gap decision signal** → `govern/decision-review`.
- **Persona-set expansion request** → `explore/persona-expansion`.
- **Governance signals** → the docket (`govern/decision-review` (docket intake)).

**Patch targets.** Patches may fix stale or inconsistent *cluster assignments*,
*cluster definitions*, *normalization-weight rules*, and *cross-reference
integrity* in `registries/persona-clusters.md`, plus deprecate/supersede/
renumber notes in `personas/`. Any change that adds a cluster, removes a persona,
adds a new disciplinary persona, or alters operating-model voting policy is
**routed to the owning surface**, not applied here.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): recurring cluster-assignment heuristics for cross-cutting
  personas; known mirror-drift patterns; prior normalization-weight rationales;
  false-positive integrity flags.
- Writes (learning-return, after acceptance): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** persona-clusters (current state), EXPERT-PANEL (canonical), INDEX
  (lenses), the skill mirror (drift check), decision-history (constraints).
- **Writes:** proposes patches to persona-clusters (canonical cluster registry)
  and to `personas/`; emits a non-canonical report to `logs/runs/`. Does not
  directly write canonical fields in v1.

## Procedure (runnable scope: one persona-or-cluster change)

1. **Intake and scope check (deterministic precondition).** Identify the single
   unit of change: one persona's cluster, one cluster definition, one weight rule,
   or one mirror-sync reconciliation. If the request bundles several, split it and
   process one; preserve the rest as queued signals. If the request is actually a
   *new persona* or *new lens family*, STOP and route to
   `explore/persona-expansion`.
2. **Integrity scan (deterministic).** Parse the three registries + the mirror:
   confirm numbering continuity (1–62), no duplicate assignment, every cluster
   entry resolves to a real persona, every persona maps to ≤ one *primary*
   cluster, and the mirror matches the canonical panel. Emit an integrity report;
   if a structural break is found, propose a clerical patch and continue only on
   the scoped unit.
3. **Load and understand** (the expensive step): the persona(s) involved, their
   discipline, current cluster rationale, neighboring clusters, and the relevant
   operating-model rules (§5–§8).
4. **Evaluate the change** against the governing decisions: does it extend (not
   replace) the list? Does it preserve breadth-over-headcount normalization? Does
   it protect informed minorities? Does it keep the canonical panel as source and
   the mirror downstream? Record rationale, evidence/basis, confidence.
5. **Decide outcome class** (one primary; others attach as signals):

   ```yaml
   outcome_class:
     - no_change
     - cluster_assignment_proposed
     - cluster_definition_proposed
     - weight_rule_proposed
     - mirror_reconciliation_proposed
     - coverage_gap_decision_signal     # → govern/decision-review
     - persona_expansion_needed         # → explore/persona-expansion
     - integrity_patch_proposed
     - manual_review_required
   ```

6. **Emit.** The scoped patch proposal(s), the persona-governance report, any
   routed signals (coverage-gap → decision-review; expansion → persona-expansion;
   unresolved governance issue → docket), and the verdict block. The mirror patch,
   if any, is explicitly marked **apply-after-canonical-acceptance**.

## Coverage-gap handling (the owned decision, routed not decided)

The cluster map already records that the seven clusters do not cleanly cover
personas 19 (Causal Inference), 20 (Physics-Informed ML), 28 (Evolutionary
Biologist), 29 (Systems Biologist), 30 (Neuroscientist), 33 (Cognitive
Scientist), 44 (Ecologist). Persona Governance **owns surfacing this**, but the
policy choice — *add an eighth (observer/selection/biology) cluster vs accept
best-fit assignments* — is a policy decision. It is emitted as a
`coverage_gap_decision_signal` to `govern/decision-review` with both options, the
affected personas, and a best-fit *provisional* assignment proposed patch-first so
scoring is not blocked while the decision is pending. Persona Governance does not
canonize the choice itself.

## Outputs (shapes)

Persona-governance report (audit artifact, `logs/runs/`):

```markdown
# Persona Governance Report
## Metadata
- Workflow / version / run date / trigger / unit-of-change:
## Integrity Scan
- Numbering / duplicates / orphan entries / primary-cluster uniqueness / mirror match:
## Change Under Review
- Persona(s) or cluster / current state / proposed state:
## Evaluation
- Operating-model basis (§5–§8) / extends-not-replaces? / breadth-over-headcount preserved? / minority protection intact? / rationale / evidence / confidence:
## Outcome
- Outcome class / proposed patch summary / requires acceptance by:
## Mirror Sync
- Drift found? / reconciliation patch (apply-after-canonical-acceptance)?:
## Routed Signals
- Coverage-gap → decision-review / expansion → persona-expansion / docket items:
```

Cluster-assignment patch proposal:

```yaml
persona_cluster_patch:
  persona: <#, name>
  current_primary_cluster:
  proposed_primary_cluster:
  rationale:
  evidence_or_basis:
  confidence: low | med | high
  extends_not_replaces: true
  requires_acceptance_by: <authority/accept step>
```

Governance docket item:

```yaml
governance_docket_item:
  issue:
  affected_persona_or_cluster:
  signal_type:
  authority_surfaces_involved:
  why_persona_governance_cannot_resolve:
  recommended_owner_workflow:
  evidence_or_basis:
```

Every run ends with the verdict block.

## Escalation triggers

Route OUT (never act unilaterally): coverage-gap / add-a-cluster question →
`govern/decision-review`; new persona or new lens family →
`explore/persona-expansion`; a weight-rule change that implies an operating-model
voting-policy change → `govern/decision-review` (and log the conflict, operating
model §11); a needed persona-set evaluation requiring full-panel judgment → a
`deep-panel-review` job if one exists, else `signal_type:
undefined-workflow-needed`; canonical-panel vs mirror conflict that cannot be
mechanically reconciled → docket; registry/authority conflict → log as
`confusion_or_conflict` and defer to the authority surface.

## Failure modes

- **Replacing the persona list instead of extending it.** Guard: extends-not-
  replaces check (Procedure step 4); deprecate/supersede, never delete.
- **Manufacturing consensus by re-clustering.** Guard: breadth-over-headcount
  normalization is preserved; re-clustering that would let one cluster dominate is
  flagged and routed, not applied.
- **Hand-editing the skill mirror as a source.** Guard: canonical panel is source;
  mirror patch is apply-after-canonical-acceptance only.
- **Deciding the coverage gap unilaterally.** Guard: coverage-gap is a routed
  decision signal to `decision-review`; only a provisional best-fit is proposed
  patch-first.
- **Treating a persona's view as evidence/authority.** Guard: personas are review
  postures (operating model §6); this workflow tunes weighting, not conclusions.
- **Authority creep:** a cluster/weight patch that effectively rewrites voting
  policy. Guard: such changes route to decision-review; persona-clusters patches
  stay within the registry's scope.
- **Silent integrity drift** (duplicate/orphan persona, broken cross-reference).
  Guard: deterministic integrity scan each run (Procedure step 2).

## Success criteria

A good run yields, for one persona-or-cluster change: a defensible patch a
reviewer can accept or reject quickly; an integrity scan that confirms the three
persona surfaces and the skill mirror are consistent (or proposes the exact
clerical fix); a clear routing of the coverage-gap decision and any expansion
need; and no change to any persona's conclusions or to canonical state by this
workflow itself. Cheap test: a reviewer can tell, without re-reading the whole
persona system, why a persona sits in its cluster, that the mirror matches the
canonical panel, and which downstream workflow owns any unresolved persona policy
question.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/persona-integrity-check` — deterministic; parse the three persona
  surfaces + mirror; emit integrity report + clerical patch; **short-circuits** a
  scored re-cluster on structural break.
- `govern/persona-mirror-sync` — deterministic; diff canonical panel vs skill
  mirror; emit reconciliation patch (apply-after-canonical-acceptance).
- `govern/single-persona-recluster` — judgment; one persona → proposed primary
  cluster + rationale.
- `govern/cluster-normalization-review` — judgment; one weight-rule change → patch
  proposal; high-scrutiny (touches voting fairness).

Likely cadence differences:
- On events: integrity-check + mirror-sync on any persona/registry change.
- Periodic: cluster-normalization review (rare; fairness-sensitive).
- After accumulated signals: coverage-gap decision signal when scoring repeatedly
  hits unmapped personas.

Likely context boundaries:
- Integrity/mirror atoms load only the persona surfaces + mirror + parser.
- Recluster atom loads the persona(s), neighboring clusters, and §5–§8.
- The full 62-persona panel is NOT loaded unless a deep-panel-review is triggered.

Likely deterministic vs judgment split:
- Deterministic: numbering/duplicate/orphan checks, mirror diff, cross-reference
  resolution.
- Judgment-based: cluster assignment for cross-cutting personas, normalization-
  weight rules, deprecate/supersede recommendations.

Phase 4 coverage questions:
- Does every output have a downstream consumer? (patch → accept step; mirror patch
  → post-acceptance sync; coverage-gap → decision-review; expansion →
  persona-expansion; signals → docket.)
- Does every registry write have an owning task?
- Does every escalation signal have a destination?
- Does every scheduled task have a bounded object (one persona / one cluster /
  one weight rule)?
- Is anything reviewed twice by competing tasks? (persona-governance vs
  persona-expansion must not both author personas — expansion authors, governance
  clusters.)
- Is any unit too large for one agent run?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Coverage-gap decision (docketed).** Add an eighth observer/selection/biology
   cluster (personas 28, 29, 30, 33, 44; possibly 19, 20) vs accept best-fit
   assignments? Routed to `govern/decision-review`; provisional best-fit proposed
   patch-first meanwhile. (Carried from `persona-clusters.md`.)
2. **Secondary-cluster support.** Should a persona be allowed a secondary cluster
   (cross-cutting personas like 19, 20), or strictly one primary? Currently single
   primary; revisit if scoring needs it.
3. **Normalization-weight schema.** The exact cross-cluster weighting rule (how
   "distance" between clusters is measured) is not yet formalized; until then,
   weight-rule changes are high-scrutiny and routed to decision-review.
4. **Mirror-sync ownership in Phase 4.** Whether mirror reconciliation is its own
   scheduled atom or folded into an acceptance step — minor, open.
5. **deep-panel-review existence** — shared with line-review/lifecycle-review; if
   a full-panel persona evaluation is needed it currently routes as
   `undefined-workflow-needed`.
