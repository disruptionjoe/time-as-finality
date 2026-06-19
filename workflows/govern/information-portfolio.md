---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: information_ledger_patch_proposal
summarizable: false
unit_of_review: one_line_information_gain_entry
---

# Information Portfolio

**Family:** govern
**Mode:** evaluation
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** run outputs in `logs/runs/`, `registries/line-registry.md` (lines +
two-axis lifecycle posture), and lifecycle outcomes from `govern/lifecycle-review`
(especially retirements/archivals, which must still record information gain).
**Scope:** Record **one line's information-gain entry** (active OR archived/failed),
plus a **periodic portfolio-balance read** across explore / exploit / govern.

## Purpose

Maintain the **information-gain ledger** (`registries/information-portfolio.md`):
the program's record that value is measured by **change in understanding over
time, not the win/loss record of hypotheses** (operating model §3). A line
archived as "wrong" still has its information gain recorded as a positive outcome.
This workflow makes that ledger explicit and reports **portfolio balance** across
the three postures so the program can see whether it is over- or under-investing
in any one (operating model §2, §3).

The governance meaning: this is the program's defense against confusing *failure*
with *waste*. Every line — alive, held, or archived — that changed the program's
understanding earns a ledger entry; the entry is the unit of accounting, and the
balance read is the allocation-honesty signal.

## Governing decisions (preserve)

- **Information gain is the unit of value** (operating model §3): a line raises it
  by revealing a missing definition, exposing a flaw in a stronger line, inspiring
  a new theorem, improving persona clustering, producing a better test, or seeding
  a stronger exploit candidate. The ledger uses exactly this gain-type vocabulary.
- **Failed/archived lines are recorded as positive information gain** (operating
  model §3): archival is an occasion to record gain, never to erase it. This
  workflow is the consumer that ensures every retirement leaves a ledger entry.
- **Allocation honesty** (operating model §2): the balance read across
  explore/exploit/govern exists to make spending visible and adjustable, not to
  rank lines. The thing being allocated is the research budget (compute, agent
  attention, cadence, human/review effort).
- **Line registry is a portfolio layer, not a status ledger** (DEC-007): this
  workflow reads line status/stage from the registry and links out to authoritative
  surfaces; it never restates claim/roadmap/hypothesis status.
- **Two-axis lifecycle** (DEC-018/020): a line's `stage` (maturity) and `status`
  (active|held|archived) are read from the registry; an archived line is still a
  first-class ledger subject.
- **No single number** (consistent with the scorecard's philosophy): information
  gain is described qualitatively by *what understanding changed* and a gain-type
  tag, not collapsed into a scalar score.

## Authority boundaries

- **May:** read `logs/runs/`, the line registry, and lifecycle-review outcomes;
  compose/append one information-gain entry per line to the ledger (active or
  archived); compute and append a periodic portfolio-balance read across the three
  postures; flag a line that changed understanding but lacks a ledger entry; flag a
  ledger entry inconsistent with current registry posture; propose all of these
  patch-first.
- **Must not:** decide a claim is true or false (→ authoritative surfaces /
  evidence review); move a lifecycle stage or status (→ `govern/lifecycle-review`);
  archive or revive a line (→ `govern/lifecycle-review`); restate claim/roadmap/
  hypothesis status (DEC-007); restructure the portfolio — split/merge/rebalance
  lines (→ `govern/portfolio-review`); set or enforce **target** balance ratios
  across postures (a policy decision → `govern/decision-review`); collapse gain to
  a single score; rewrite the operating model or Decision History; treat the
  ledger as a ranking of lines.
- **Scoring authority:** judgment-with-rationale for *what understanding changed*
  and the gain-type tag; deterministic for coverage checks (which lines lack an
  entry) and posture tallies (the balance read).
- **Write authority — patch-first** to `registries/information-portfolio.md`.
  Entries and balance reads are **proposed**, applied by an authority/accept step,
  not by this workflow in v1.

## Read surfaces

- **The ledger:** `registries/information-portfolio.md` (current state).
- **Line registry:** `registries/line-registry.md` — lines, stage, status,
  relationships (per DEC-007/018/020).
- **Run logs:** `logs/runs/` — the evidence that understanding changed.
- **Lifecycle outcomes:** `govern/lifecycle-review` reports / lifecycle patches —
  especially retirements (each must yield a gain entry).
- **Health substrate:** `registries/research-line-scorecard.md` — the
  Information-gain dimension is a cross-check, not the ledger itself.
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — §2 (postures), §3
  (information-gain philosophy), §11 (authority order).
- **Decision History:** `registries/decision-history.md` — DEC-007 and constraints.
- **Workflow catalog / skeleton:** `README.md`, `WORKFLOW-SKELETON-PROPOSAL.md` —
  to validate route targets.
- Govern Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- An **information-portfolio report** (audit artifact) to `logs/runs/` — non-canonical.
- A **ledger entry patch proposal** to `registries/information-portfolio.md` (one
  line's information-gain entry) — patch-first.
- A **portfolio-balance patch proposal** appending a dated balance read across
  explore/exploit/govern — patch-first.
- **Coverage flags** → as patches (lines lacking an entry) or, if they imply a
  missing run record, a `confusion_or_conflict` signal.
- **Target-ratio policy question** → `govern/decision-review`.
- **Structural/rebalancing implications** → `govern/portfolio-review`.
- **Governance signals** → the docket (`govern/decision-review` (docket intake)).

**Patch targets.** Patches may add/update an *information-gain entry* (line, status
read-from-registry, what-changed, gain type) and append a *balance read*. The
workflow **never** edits the line's lifecycle posture, claim status, or portfolio
structure; those route to the owning workflows.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): recurring gain-type classification heuristics; known
  patterns where a "failed" line produced large gain; prior balance-read
  observations.
- Writes (learning-return, after acceptance): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** information-portfolio (current ledger), line-registry (posture),
  research-line-scorecard (info-gain cross-check), decision-history (constraints).
- **Writes:** proposes ledger entries and balance reads to information-portfolio;
  emits a non-canonical report to `logs/runs/`. Does not write line-registry,
  scorecard, or any authoritative status surface.

## Procedure (runnable scope: one line information-gain entry, plus periodic balance)

1. **Scope the unit (deterministic precondition).** Either (a) one line whose
   understanding changed (from a run log or a lifecycle outcome), or (b) a periodic
   balance read. If a lifecycle retirement just occurred without a ledger entry,
   prioritize the retired line — archival must not erase gain.
2. **Read before acting** (operating model §9). Load the ledger, the line's
   registry entry (stage + status), the relevant run logs, and any lifecycle-review
   outcome for the line.
3. **For a line entry:**
   - Establish *what understanding changed*, grounded in cited run-log / result
     evidence (NOT a claim-truth judgment).
   - Tag the gain type(s) from the operating-model §3 vocabulary (definition
     revealed / flaw exposed in a stronger line / theorem inspired / clustering
     improved / better test produced / stronger exploit candidate seeded).
   - Read the line's `status` from the registry (active | held | archived) — do not
     decide it; if archived, confirm the entry frames the gain positively.
   - Compose the entry patch-first.
4. **For a balance read (periodic):**
   - Tally where the program's recent budget went across explore / exploit /
     govern, using run logs and ledger entries as evidence.
   - Report the balance **descriptively** (where effort went, where gain
     concentrated, any posture that is starved or saturated). Do **not** set or
     enforce a target ratio — if the read suggests a policy target is needed, route
     that question to `decision-review`.
5. **Coverage check (deterministic).** List any line whose registry posture or run
   logs indicate changed understanding but which lacks a ledger entry; propose the
   missing entries or flag the gap.
6. **Emit.** The entry/balance patch proposal(s), the information-portfolio report,
   any routed signals (target-ratio → decision-review; structural → portfolio-review;
   unresolved → docket), and the verdict block.

## Outputs (shapes)

Information-portfolio report (audit artifact, `logs/runs/`):

```markdown
# Information Portfolio Report
## Metadata
- Workflow / version / run date / trigger / unit (line entry | balance read):
## Line Information-Gain Entry (if applicable)
- Line / status (read from registry) / what understanding changed / gain type(s) / evidence (cited runs):
## Portfolio Balance Read (if applicable)
- Effort by posture (explore/exploit/govern) / where gain concentrated / starved or saturated postures / descriptive only:
## Coverage Check
- Lines changed-understanding-but-no-entry / proposed entries:
## Routed Signals
- Target-ratio → decision-review / structural → portfolio-review / docket items:
```

Information-gain ledger entry patch:

```yaml
information_gain_entry:
  line: <RL-id + name>
  status: active | held | archived     # read from line-registry, not decided here
  information_gain: <what understanding changed, cited>
  gain_type: [definition-sharpened | flaw-exposed | theorem-inspired | clustering-improved | better-test-produced | exploit-candidate-seeded]
  evidence_or_basis: <run logs / results cited>
  confidence: low | med | high
  requires_acceptance_by: <authority/accept step>
```

Portfolio-balance read patch (append, dated):

```yaml
portfolio_balance_read:
  date:
  effort_by_posture: { explore: , exploit: , govern: }     # descriptive
  gain_concentration:
  starved_or_saturated:
  note: "descriptive only; target ratios are a decision-review policy question"
```

Governance docket item:

```yaml
governance_docket_item:
  issue:
  affected_line:
  signal_type:
  authority_surfaces_involved:
  why_information_portfolio_cannot_resolve:
  recommended_owner_workflow:
  evidence_or_basis:
```

Every run ends with the verdict block.

## Escalation triggers

Route OUT (never act unilaterally): whether to set target balance ratios across
postures → `govern/decision-review` (policy); structural/rebalancing implications
(a posture is starved and lines should be split/merged/reallocated) →
`govern/portfolio-review`; a lifecycle change implied by the gain read →
`govern/lifecycle-review` (this workflow records gain, it does not move lifecycle);
a claim-truth question → an evidence-review workflow if one exists, else
`signal_type: undefined-workflow-needed`; a run that changed understanding but left
no run-log evidence → `confusion_or_conflict` (and route to `govern/research-memory`
for the missing record); registry/authority conflict → log and defer to the
authority surface (operating model §11).

## Failure modes

- **Treating archival as erasure of value.** Guard: every retirement must yield a
  positive-framed ledger entry (Procedure step 1, 3).
- **Confusing information gain with claim truth.** Guard: entries record *what
  understanding changed*, never a true/false verdict; truth routes out.
- **Collapsing gain to a single score / ranking lines.** Guard: qualitative
  what-changed + gain-type tag only; no scalar, no cross-line rank.
- **Setting target ratios unilaterally.** Guard: balance read is descriptive;
  target-ratio policy routes to decision-review.
- **Moving lifecycle or portfolio structure.** Guard: hard Must-nots; those route
  to lifecycle-review / portfolio-review.
- **Restating claim/roadmap/hypothesis status.** Guard: DEC-007 — read posture
  from the line registry; never restate authoritative status.
- **Double-counting gain across overlapping run logs.** Guard: cite specific runs;
  coverage check dedupes by line + evidence.
- **Authority creep via the balance read** (using it to reallocate budget). Guard:
  read is descriptive; allocation changes route to portfolio-review/decision-review.

## Success criteria

A good run yields, for one line, an information-gain entry a reviewer can accept
quickly — defensible from cited run evidence, correctly framing even a "failed"
line as positive gain, with status read (not decided) from the registry — and,
periodically, a descriptive posture-balance read that makes allocation visible
without prescribing a target. Cheap test: a reviewer can tell, without re-reading
the line's full history, what understanding the line changed, which gain type it
is, and that no archived line silently lost its gain entry; and the balance read
names where effort and gain concentrated without ranking lines or setting a quota.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/line-information-gain-entry` — one line → one ledger entry; judgment
  (the gain narrative) + deterministic status read.
- `govern/archival-gain-capture` — event-triggered on a lifecycle retirement; one
  archived line → one positive-framed entry; **must run** when a line is retired.
- `govern/portfolio-balance-read` — periodic; deterministic posture tally + a
  descriptive read.
- `govern/ledger-coverage-check` — deterministic; lines with changed understanding
  but no entry.

Likely cadence differences:
- On events: line-entry on a run that changed understanding; archival-gain-capture
  on every lifecycle retirement.
- Periodic: portfolio-balance read; ledger-coverage check.

Likely context boundaries:
- The line-entry atom loads only that line's registry entry + relevant run logs +
  the ledger; the balance-read atom loads run-log tallies + the ledger, not full
  line artifacts.

Likely deterministic vs judgment split:
- Deterministic: status read from registry, posture tallies, coverage/dedup check.
- Judgment-based: the gain narrative and gain-type tag.

Phase 4 coverage questions:
- Does every output have a downstream consumer? (entry → ledger; balance read →
  ledger/allocation visibility; target-ratio → decision-review; structural →
  portfolio-review.)
- Does every registry write have an owning task? (only the ledger; line-registry
  is read-only here.)
- Does every escalation signal have a destination?
- Does every scheduled task have a bounded object (one line / one balance read)?
- Is anything reviewed twice by competing tasks? (information-portfolio records
  gain; portfolio-review restructures; lifecycle-review moves posture — distinct.)
- Is any unit too large for one agent run? (one line entry is right-sized; large
  balance reads can window by posture.)
- Is archival-gain-capture guaranteed to fire on every retirement? (must be wired
  to lifecycle-review's retire outcome.)

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Target balance ratios (docketed).** Should the program set target
   explore/exploit/govern ratios, or keep the balance read descriptive only?
   Routed to `govern/decision-review`; balance read stays descriptive meanwhile.
2. **Quantifying information gain.** Whether gain ever needs a coarse ordinal
   (low/med/high) beyond the qualitative narrative + gain-type tag — kept
   qualitative in v1 (no single number), revisit if cross-line comparison is
   needed (would still avoid a single rank).
3. **Archival-gain-capture wiring.** Guaranteeing an entry on every
   lifecycle-review retirement is a Phase-4 wiring requirement (coverage question
   above); until then the coverage check is the backstop.
4. **Patch-acceptance owner** — human, a dedicated accept step, or `docket-triage`?
   Shared open item with the other govern workflows.
5. **decision-review vs docket-triage** — the two govern sinks need reconciliation
   (carried from DEC-017); policy questions route to decision-review, other
   governance signals to the docket.
