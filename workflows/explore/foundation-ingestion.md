---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: literature_note_and_candidate_flags
summarizable: false
unit_of_review: one_foundation_item
---

# Foundation Ingestion

**Family:** explore
**Mode:** search
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** the next `proposed` item(s) from `registries/foundation-queue.md`.
**Emits:** a durable known-neighbor note under `literature/`; persona/test/claim
**candidate flags** routed to their owners; a queue status patch (`proposed → noted`).

## Purpose

Bring outside knowledge — papers, mathematics, neighboring concepts — into the
program's reach by **ingesting the next item from the foundation queue** and
producing a durable, reusable known-neighbor note. Foundation work is exploration
(DEC-002, operating model §2, §10): reading a paper expands the search space, so it
lives here, not as a separate posture.

Ingestion is **Search Mode**: it maximizes connection-finding and information gain
("what does this neighbor let us see, ask, or test that we couldn't before?"). It
does **not** evaluate whether a TaF claim is true, does not promote anything, and
does not decide lifecycle. Its job is to *land the knowledge well* and *flag where
it touches the program*, then route those touches to the workflows that own them.

The boundary is the same family discipline: ingestion **flags** candidates
(personas to add, tests to write, claims to challenge, lines to seed) but does not
*act* on them. Persona additions belong to `explore/persona-expansion`; new lines
to `explore/line-discovery` → `govern/line-intake`; claim challenges to the
authority surfaces / `exploit/challenge-primary`; standing/lifecycle to govern.

## Authority boundaries

- **May:** read the foundation queue and the inbound item; write a durable
  known-neighbor note under `literature/`; summarize the neighbor faithfully and
  map its adjacency to existing lines/claims/tests; flag persona/test/claim/line
  candidates; propose a queue status patch (`proposed → ingested → noted`); emit
  governance signals for missing routes.
- **Must not:** add or number personas (→ `explore/persona-expansion`); register a
  research line (→ `explore/line-discovery` then `govern/line-intake`); write or
  change claim status (→ `CLAIM-LEDGER.md` via its owner / `exploit/challenge-primary`);
  move any lifecycle stage/status (→ govern); assign standing (→ `govern/line-review`);
  promote the neighbor's framing into TaF physics (a Search-Mode note is a neighbor
  map, not a finding); silently overwrite the queue (patch-first).
- **Scoring authority:** judgment-with-rationale, descriptive only — the note
  characterizes adjacency and risk, it does not score TaF lines.
- **Write authority:** **direct write for the `literature/` note** (a new note is a
  net-add artifact, the natural product of this workflow), but **patch-first for the
  queue** (status change is a registry edit) and **flag-only** for everything routed
  out. The note is non-authoritative literature, not a claim.

## Read surfaces

- **Foundation queue:** `registries/foundation-queue.md` — the `proposed` items and
  their target clusters; the queue's maintenance contract.
- **Existing notes (de-dup / continuity):** `literature/` (N1–N6, distinguishing-
  predictions) and `papers/` — so a new note links to, rather than duplicates,
  prior known-neighbor work.
- **The inbound item itself** (paper / concept / math source). External fetch (web)
  is permitted in service of ingestion when the item is a URL/paper reference.
- **Program touchpoints (adjacency map targets):** `line-registry.md`,
  `CLAIM-LEDGER.md`, `HYPOTHESES.md`, `ROADMAP.md`, `tests/` — read to locate where
  the neighbor touches the program (not to restate their status).
- **Cluster map:** `registries/persona-clusters.md` — to judge which cluster a new
  persona flag would belong to.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — Search Mode (§1),
  explore posture (§2, §10), information-gain (§3), authority order (§11).
- **Decision History:** `registries/decision-history.md` — constraints (e.g. DEC-002
  foundation-is-explore; DEC-006 persona canonicalization).
- **Workflow catalog:** `README.md` / `WORKFLOW-SKELETON-PROPOSAL.md` — validate routes.
- Explore Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- A **known-neighbor note** in `literature/` (e.g. `N<k>-<slug>.md`) — direct
  write; non-authoritative literature.
- A **queue status patch** for `foundation-queue.md` (`proposed → noted`, with note
  pointer) — patch-first.
- **Candidate flags** routed out: persona → `explore/persona-expansion`; new line →
  `explore/line-discovery`; test → `tests/` proposal; claim challenge → the claim
  surface / `exploit/challenge-primary`.
- An **ingestion run log** (operational log) to `logs/`.
- **Governance signals** → the docket.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): note-quality heuristics, recurring adjacency patterns,
  prior "ingested-but-never-used" items, known-neighbor families already covered.
- Writes (learning-return, after a run): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** `foundation-queue.md`, `line-registry.md`, `persona-clusters.md`,
  `decision-history.md`.
- **Writes:** a `literature/` note (direct); a **patch** to `foundation-queue.md`
  status (patch-first); a run log (append). No other canonical registry write.

## Procedure (runnable scope: one foundation item; small batch allowed)

1. **Select the next item (deterministic).** Pull the next `proposed` item(s) from
   `foundation-queue.md` (respecting target-cluster priority if set). Confirm it is
   not already `noted` and not duplicated by an existing `literature/` note. Mark it
   `ingested` (patch) while the note is being written.
2. **Read and characterize.** Read the source. Produce a faithful summary: what it
   claims/proves/offers, and — critically for Search Mode — what it lets the program
   *see, ask, or test* that it could not before.
3. **Map adjacency.** Locate where the neighbor touches existing lines, claims,
   hypotheses, and tests. State adjacency as *crosswalk*, never as status change:
   "this supports/pressures/duplicates/extends RL-NNN or claim C-x" — without editing
   those surfaces.
4. **Flag candidates.** From the adjacency map, flag (do not act on): persona lenses
   the neighbor's discipline would justify; bounded tests it suggests; existing
   claims it pressures; new candidate lines it opens.
5. **Write the note and patch the queue.** Write the `literature/` note; patch the
   queue item to `noted` with the note pointer. Route all flags to their owners.
6. **Emit.** Note, queue patch, candidate flags, run log, governance signals. End
   with the verdict block.

## Outputs (shapes)

**Known-neighbor note** (`literature/N<k>-<slug>.md`): source identity; faithful
summary; "what this lets us see/ask/test"; adjacency map (touchpoints to lines/
claims/hypotheses/tests, each labeled supports | pressures | duplicates | extends |
orthogonal); misuse risk (how this neighbor could be over-imported into TaF
physics); links to related existing notes.

**Queue status patch** (for `foundation-queue.md`):

```yaml
queue_patch:
  item:
  from_status: proposed
  to_status: noted
  note_pointer: literature/N<k>-<slug>.md
  applied_by: explore/foundation-ingestion   # patch-first; accepted by queue owner
```

**Candidate flag** (one per flagged touchpoint):

```yaml
candidate_flag:
  flag_type: persona | test | claim_challenge | new_line
  what:
  why:                       # the adjacency basis
  evidence_or_basis:         # note section / source citation
  recommended_owner_workflow: explore/persona-expansion | tests/ | exploit/challenge-primary | explore/line-discovery
  confidence: low | med | high
```

**Governance docket item** (missing route / queue-policy gap): standard shape with
`signal_type` ∈ {undefined-workflow-needed, queue-priority-policy-needed,
duplicate-note-detected, manual-review-required}.

Every run ends with the verdict block.

## Escalation triggers

Route OUT: persona-worthy discipline → `explore/persona-expansion`; line-worthy gap
→ `explore/line-discovery`; claim the neighbor pressures → the claim surface /
`exploit/challenge-primary`; test-worthy probe → `tests/` proposal; an item that is
really a cross-cluster *convergence* across several neighbors → flag for
`explore/cross-disciplinary-synthesis`; an item whose ingestion shifts the landscape
topology → flag for `explore/landscape-reassessment`; a duplicate of an existing
note → do not re-note; patch the queue and log; missing route →
`undefined-workflow-needed`; registry/authority conflict → `confusion_or_conflict`,
defer to §11.

## Failure modes

- **Over-import (neighbor framing becomes TaF physics).** Guard: Search Mode; the
  note is a neighbor map with a mandatory misuse-risk section; it makes no claims.
- **Acting on flags instead of routing them.** Ingestion adds a persona or a line
  itself. Guard: flag-only; persona/line/claim changes route to their owners.
- **Status drift in the queue.** Silent overwrite, or marking `noted` with no note.
  Guard: patch-first; `noted` requires a `note_pointer`; intermediate `ingested`
  state.
- **Duplicate notes.** Re-noting an already-covered neighbor. Guard: step 1 de-dup
  against `literature/`/`papers/`.
- **Restating authority-surface status.** The note edits claim/roadmap status.
  Guard: adjacency is crosswalk only; those surfaces stay authoritative (DEC-007).
- **Dangling route / silent flag loss.** Guard: every flag gets a recommended owner
  and appears in the run log; missing routes → `undefined-workflow-needed`.

## Success criteria

A good run turns one queued item into a **durable, faithful known-neighbor note**
that any later workflow can reuse, with a clear adjacency map and a misuse-risk
guardrail, plus correctly-routed persona/test/claim/line flags — and leaves the
queue honestly updated (`proposed → noted`, with a note pointer).

Cheap test: a reviewer can tell, without reading the source, what the neighbor
offers, where it touches the program, what it would be a mistake to import, what
follow-ups were flagged and to whom — and the queue shows the item as `noted` with
a resolvable note link.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `explore/foundation-item-select` — next `proposed` item; de-dup + mark `ingested`;
  **mostly deterministic** (queue cursor + duplicate check).
- `explore/foundation-note-write` — one item → one `literature/` note + adjacency
  map; judgment-based, possibly expensive (reading the source).
- `explore/foundation-flag-route` — note → candidate flags routed + queue patched to
  `noted`; deterministic packaging, judgment for flag selection.

Likely cadence differences:
- Periodic drain of the queue (one item per run), or event-triggered when a high-
  priority item is added (e.g. by landscape-reassessment or a user).

Likely context boundaries:
- Select loads only the queue + existing note index; note-write loads the source +
  touchpoint surfaces; flag-route loads only the finished note.

Likely deterministic vs judgment split:
- Deterministic: queue cursor, duplicate detection, status transition,
  note-pointer presence, route-target existence.
- Judgment-based: the summary, the adjacency map, misuse-risk, candidate-flag selection.

Phase 4 coverage questions:
- Does every queued item reach a terminal status with a note pointer?
- Does every candidate flag have an owning workflow?
- Does every `noted` transition have a resolvable note link?
- Is the expensive note-write seam separable from the cheap select/route seams for cadence?
- Is any unit too large for one agent run? (a very large paper may need its own bounding.)

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Queue prioritization policy** — when multiple `proposed` items exist, what
   orders them (target-cluster need, dependency, recency)? (Docketed:
   `queue-priority-policy-needed`.)
2. **Note numbering / naming** — `N<k>` numbering is currently manual; confirm the
   allocation scheme and whether `papers/` vs `literature/` placement is rule-based.
3. **External fetch scope** — how much live web/paper fetching is in-scope per item
   vs requiring a human to supply the source? (cost/safety; defer to Phase 4 cadence.)
4. **Batch size** — one item per run (default) vs a small bounded batch; reconcile
   with the "one foundation item" unit-of-review.
