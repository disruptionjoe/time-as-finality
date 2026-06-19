---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: memory_maintenance_patch_proposal
summarizable: false
unit_of_review: one_memory_maintenance_pass
---

# Research Memory

**Family:** govern
**Mode:** evaluation
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** accumulated `logs/runs/` entries, prior `logs/synthesis/` notes,
verdict blocks in `logs/best-next-move/`, the current registries, `PROJECT-LOG.md`,
the Document-Contract rollout backlog (files lacking a contract), and — once the
memory layer is built (Phase 3.5) — the family Memory Pack raw logs in its
SUMMARIZER role.
**Scope:** Perform **one memory-maintenance pass** — keep long-term memory
coherent and compaction-resilient: log hygiene, cross-run synthesis, PROJECT-LOG
upkeep, Document-Contract rollout, and (interface/spec only) the Memory Pack
summarizer role.

## Purpose

Make the program's memory survive context compaction and agent/personnel turnover
(operating model §9). It maintains the operational-log substrate, writes cross-run
synthesis notes, keeps `PROJECT-LOG.md` (the canonical narrative memory) current,
drives the incremental Document-Contract rollout (DEC-010), and **owns the
Phase-3.5 Memory Pack SUMMARIZER role** — specified here as an interface and
contract, **not built**, because the memory layer is plan-only (DEC-004,
`MEMORY-LAYER-PLAN.md`).

The governance meaning: this workflow **proposes; it does not silently rewrite
history.** Logs are append/prepend per their own Document Contracts; the decision
history and PROJECT-LOG are never edited by this workflow as a source of new
policy. Its job is *hygiene, synthesis, and rollout*, not authorship of truth.

## Governing decisions (preserve)

- **Read before acting; append after acting** (operating model §9). No memory pass
  starts from a blank slate.
- **Registries are current state; logs are history; logs are never overwritten**
  (operating model §9, §12). Operational logs are prepend newest-first; historical
  records are append chronological; current-state registries are edit-in-place —
  per each file's Document Contract.
- **PROJECT-LOG is the canonical narrative memory** (operating model §9). This
  workflow appends entries (an Operational Log, prepend newest-first) but does not
  rewrite prior entries.
- **Decision History is append-only and is NOT modified by this workflow**
  (historical-record; the run brief and DEC schema both forbid silent rewrites).
  A memory-derived lesson implying a DEC change is routed out as a proposal.
- **The Memory Pack is guidance-only** and sits second-lowest in the authority
  order (operating model §11; `MEMORY-LAYER-PLAN.md`). The summarizer **never
  writes new policy onto the pack**; policy-class lessons route out as proposals.
- **Document-Contract rollout is incremental** (DEC-010): exemplars first, then the
  rest as this workflow's housekeeping; a file without a contract is not broken.

## Authority boundaries

- **May:** read all logs, registries, and PROJECT-LOG; propose a cross-run
  synthesis note to `logs/synthesis/`; propose a `PROJECT-LOG.md` entry (append,
  prepend-newest-first); propose Document-Contract front-matter for files that
  lack one; propose log-hygiene fixes (indexing, broken-link repair,
  `last-summarized` marker placement) consistent with each file's contract; specify
  and (when the layer exists) execute the Memory Pack summarizer contract; run the
  compaction-resilience self-test; route policy-class lessons out as proposals.
- **Must not:** overwrite or reorder existing log entries; rewrite prior
  PROJECT-LOG entries; modify `registries/decision-history.md` (append-only,
  owned by a decision/governance review); change any registry's *content* (only
  propose a Document Contract or flag drift — content fixes route to the owning
  workflow); promote a memory lesson into policy by writing it onto a higher
  surface; let the Memory Pack become a queue, an authority, or a source of truth
  (operating model §11); summarize a canonical (`summarizable: false`) surface
  onto a load surface; delete anything ("pruning" = summarizing out of the
  surface, never deleting from disk).
- **Scoring authority:** judgment-with-rationale for synthesis content; deterministic
  for contract presence, link integrity, and summarizer marker placement.
- **Write authority — patch-first.** Synthesis notes, PROJECT-LOG entries,
  Document-Contract additions, and summarizer rollups are **proposed** and applied
  by an authority/accept step; in v1 nothing is silently applied to canonical
  surfaces. Appends to operational logs follow each file's contract.

## Read surfaces

- **Logs (history):** `logs/runs/`, `logs/synthesis/`, `logs/best-next-move/`.
- **Narrative memory:** `PROJECT-LOG.md`.
- **Registries (current state):** `line-registry`, `persona-clusters`,
  `foundation-queue`, `information-portfolio`, `research-line-scorecard`,
  `decision-history` (read-only — constraints + DEC-004/010 context).
- **Contract spec:** `DOCUMENT-CONTRACT.md` (the schema for rollout).
- **Memory plan:** `MEMORY-LAYER-PLAN.md` — the five-piece pack structure, the
  summarizer contract, the learning-return schema, the authority hierarchy.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — §9 (memory), §11
  (authority order), §12 (document classes).
- **Workflow catalog / skeleton:** `README.md`, `WORKFLOW-SKELETON-PROPOSAL.md` —
  to validate route targets.
- **Family Memory Pack raw log** (Phase 3.5; inert if absent) — read **only** in
  the summarizer role, and only the summarizer reads it.

## Write surfaces

- A **memory-maintenance report** (audit artifact) to `logs/runs/` — non-canonical.
- A **cross-run synthesis note** proposed to `logs/synthesis/` (Operational Log,
  prepend newest-first).
- A **PROJECT-LOG entry** proposed for `PROJECT-LOG.md` (append/prepend per its
  contract — Operational Log, newest-first).
- A **Document-Contract patch proposal** adding front-matter to a file that lacks
  one (one file per pass unit, or a small named batch).
- A **log-hygiene patch proposal** (index/link repair; `last-summarized` marker).
- A **Memory Pack rollup** onto the family `MEMORY.md` load surface — only in the
  summarizer role, only when the layer exists, per the summarizer contract.
- **Policy-class lesson** routed OUT as a proposal → `govern/decision-review`.
- **Registry content drift / fixes** → the owning govern workflow (e.g.
  line-registry drift → `govern/line-review` / `govern/lifecycle-review`).
- **Governance signals** → the docket (`govern/decision-review` (docket intake)).

**Patch targets.** Patches may add a Document Contract to a contract-less file,
repair a log index or broken link, place/update a `last-summarized` marker, append
a synthesis note or PROJECT-LOG entry, and (summarizer role) rewrite the
*Current Memory Summary* and append to the *Principles & Decisions* table on a
pack load surface. **Decision History, registry content, and any
`summarizable: false` canonical surface are never rewritten by this workflow.**

## Memory interface (Phase 3.5; may be inert) — and the SUMMARIZER role it owns

This workflow has a **dual relationship** to the memory layer: like every
workflow it *consumes* the govern family pack's load surface; and uniquely it
**owns the summarizer** that produces that surface.

- Reads (load surface, as a consumer): recurring memory-hygiene heuristics, prior
  synthesis patterns, known compaction-failure modes.
- Writes (learning-return, after acceptance): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- **Summarizer role (interface/spec only — not built).** Per
  `MEMORY-LAYER-PLAN.md`, the summarizer: reads each family pack's prepend-only
  `memory-log.md` to the `last-summarized` marker; groups entries by failure mode /
  heuristic / anti-pattern; discards one-off noise, keeps recurring or
  user-corrected lessons; rewrites the *Current Memory Summary* as guidance (never
  hand-written); promotes durable lessons into the dated *Principles & Decisions*
  table; drops a new `last-summarized` marker. It **never writes new policy** onto
  the pack; policy-class lessons route out as proposals. Cadence is left open
  (Phase 3.5 build choice). The summarizer is the **only** reader of the raw
  `memory-log.md`; ordinary agents read only `MEMORY.md`.
- Does not depend on memory existing — until the layer is built, the summarizer
  role is inert and this workflow runs its log/synthesis/contract duties only.

## Registry interactions

- **Reads:** all registries (for synthesis + drift detection) and PROJECT-LOG.
- **Writes:** proposes Document-Contract front-matter to files that lack one;
  proposes synthesis notes and PROJECT-LOG entries; **does not** edit registry
  *content* or Decision History. Registry content drift is routed to the owning
  workflow, not fixed here.

## Procedure (runnable scope: one memory-maintenance pass)

1. **Scope the pass (deterministic precondition).** Pick **one** maintenance unit:
   a synthesis window (a named set of recent runs), a Document-Contract rollout
   batch (named files), a log-hygiene sweep, a PROJECT-LOG catch-up, or a
   summarizer cycle (one family pack). Do not bundle all five in one pass; queue
   the rest.
2. **Read before acting** (operating model §9). Load the relevant logs,
   registries, PROJECT-LOG, and the pack load surface. No pass starts blank.
3. **Run the chosen maintenance:**
   - *Synthesis:* read the run window, extract recurring patterns / cross-run
     findings (NOT new policy), draft a synthesis note grounded in cited run logs.
   - *Contract rollout:* for each named file, classify it (Current State /
     Historical Record / Operational Log) per DEC-010 and `DOCUMENT-CONTRACT.md`,
     propose the front-matter; do not change the file's content.
   - *Log hygiene:* check link integrity, index freshness, contract conformance,
     and `last-summarized` markers; propose fixes consistent with each file's
     contract (never reorder/overwrite history).
   - *PROJECT-LOG catch-up:* draft an entry summarizing what changed since the last
     entry, with pointers; append (prepend newest-first) — never rewrite prior
     entries.
   - *Summarizer cycle (if the layer exists):* run the summarizer contract above on
     one family pack.
4. **Compaction-resilience self-test.** Verify the success-criteria test below:
   could a new agent, given only registries + logs + PROJECT-LOG, state the
   current primary/secondary lines, why each is there, and the next move? Record
   pass/fail and any gap.
5. **Emit.** The chosen patch/note proposal(s), the memory-maintenance report, any
   routed signals (policy lesson → decision-review; registry drift → owning
   workflow; unresolved issue → docket), and the verdict block.

## Outputs (shapes)

Memory-maintenance report (audit artifact, `logs/runs/`):

```markdown
# Memory Maintenance Report
## Metadata
- Workflow / version / run date / trigger / maintenance unit:
## What Was Maintained
- Synthesis window / contract batch / hygiene sweep / PROJECT-LOG catch-up / summarizer cycle:
## Findings
- Cross-run patterns (cited) / contract gaps / hygiene issues / drift detected:
## Compaction-Resilience Self-Test
- Can a fresh agent resume from logs + registries alone? (pass/fail + gap):
## Proposals
- Synthesis note / PROJECT-LOG entry / contract patch / hygiene patch / summarizer rollup:
## Routed Signals
- Policy lesson → decision-review / registry drift → owning workflow / docket items:
```

Document-Contract patch proposal:

```yaml
document_contract_patch:
  file:
  document_class: current_state | historical_record | operational_log
  proposed_frontmatter:    # document_type / primary_reader / read_pattern / write_pattern / authority / summarizable
  rationale:
  requires_acceptance_by: <authority/accept step>
```

Governance docket item:

```yaml
governance_docket_item:
  issue:
  affected_surface:
  signal_type:
  authority_surfaces_involved:
  why_research_memory_cannot_resolve:
  recommended_owner_workflow:
  evidence_or_basis:
```

Every run ends with the verdict block.

## Escalation triggers

Route OUT (never act unilaterally): a synthesis finding that implies a policy /
operating-model / DEC change → `govern/decision-review` (operating model §0, §11);
registry *content* drift or conflict → the owning workflow (`govern/line-review`,
`govern/lifecycle-review`, `govern/information-portfolio`, `govern/persona-governance`);
a needed Decision-History append → a decision/governance review (never written
here); a compaction-resilience failure that needs new registry fields →
`signal_type: schema-inadequacy` to the docket; an undefined sink →
`signal_type: undefined-workflow-needed`; registry/authority conflict → log as
`confusion_or_conflict` and defer to the authority surface.

## Failure modes

- **Silently rewriting history.** Guard: logs are append/prepend per contract;
  prior entries are never reordered/overwritten; PROJECT-LOG entries only append.
- **Editing Decision History.** Guard: hard Must-not; DEC changes route to
  decision-review as proposals.
- **Memory becoming policy.** Guard: summarizer never writes new policy onto the
  pack; policy-class lessons route out (operating model §11;
  `MEMORY-LAYER-PLAN.md`).
- **Summarizing a canonical surface.** Guard: `summarizable: false` surfaces are
  never rolled onto a load surface.
- **Pruning as deletion.** Guard: pruning = summarizing out of the surface, never
  deleting from disk.
- **Fixing registry content under the guise of hygiene.** Guard: only Document
  Contracts / links / markers are touched; content drift routes to the owning
  workflow.
- **Building the memory layer prematurely.** Guard: summarizer is interface/spec
  only; inert until Phase 3.5 builds the packs (DEC-004).
- **Authority inversion** (a memory lesson overriding a higher surface). Guard:
  authority order §11; conflict logged, not resolved.

## Success criteria

A good pass yields one well-scoped maintenance output a reviewer can accept
quickly, leaves every log append/prepend-consistent with its contract, and — the
defining test of program memory (operating model §9) — keeps the repo in a state
where **a new agent, given only the registries, logs, and PROJECT-LOG, can state
the current primary and secondary research lines, why each is there, and the next
move, without re-deriving it.** Cheap test: run the compaction-resilience
self-test (step 4) and confirm it passes; if it fails, the pass names the exact
missing pointer and routes it.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/cross-run-synthesis` — one run window → one synthesis note; judgment.
- `govern/contract-rollout` — one file (or small batch) → contract patch; mostly
  deterministic (classification is light judgment).
- `govern/log-hygiene-sweep` — link/index/marker integrity → hygiene patch;
  deterministic.
- `govern/project-log-catchup` — append one PROJECT-LOG entry; light judgment.
- `govern/memory-pack-summarizer` — one family pack raw log → rolled load surface;
  the summarizer contract; exists only once the memory layer is built.
- `govern/compaction-resilience-check` — deterministic self-test; emits a gap list.

Likely cadence differences:
- Often / on events: log-hygiene + contract-rollout as files change.
- Periodic: cross-run synthesis; PROJECT-LOG catch-up; compaction-resilience check.
- Phase-3.5+ only: the memory-pack summarizer (cadence set at build).

Likely context boundaries:
- Synthesis loads only its run window + registries; the summarizer atom is the
  ONLY thing that loads a pack's raw `memory-log.md`; ordinary atoms load only
  `MEMORY.md`.

Likely deterministic vs judgment split:
- Deterministic: contract presence, link/index integrity, marker placement,
  compaction self-test.
- Judgment-based: synthesis content, document-class classification, which lessons
  are durable vs one-off (summarizer).

Phase 4 coverage questions:
- Does every output have a downstream consumer? (synthesis → logs/synthesis;
  PROJECT-LOG entry → narrative memory; contract patch → accept step; rollup →
  pack surface; policy lesson → decision-review.)
- Does every registry write have an owning task? (this workflow writes NO registry
  content — drift routes out.)
- Does every escalation signal have a destination?
- Does every scheduled task have a bounded object (one window / one file / one
  pack)?
- Is anything reviewed twice by competing tasks? (research-memory does hygiene/
  synthesis; it must not re-decide lifecycle/portfolio/persona content.)
- Is any unit too large for one agent run? (split synthesis windows.)

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Log rotation / archival policy.** When do `logs/runs/` entries get rolled
   into a synthesis and the raw run archived? Cadence undefined — Phase 4 /
   docketed if it blocks.
2. **Summarizer cadence.** Left open by `MEMORY-LAYER-PLAN.md`; set at Phase-3.5
   build, not here.
3. **PROJECT-LOG write pattern confirmation.** PROJECT-LOG is an Operational Log
   (prepend newest-first) per DEC-010; its own Document Contract should be
   confirmed in a contract-rollout pass.
4. **Patch-acceptance owner** — human, a dedicated accept step, or `docket-triage`?
   Shared open item with line-review / lifecycle-review.
5. **decision-review vs docket-triage** — the two govern sinks need reconciliation
   (carried from DEC-017); policy lessons currently route to decision-review,
   other governance signals to the docket.
