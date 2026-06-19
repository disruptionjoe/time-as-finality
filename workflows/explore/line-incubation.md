---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: stage_advance_candidate_proposal
summarizable: false
unit_of_review: one_research_line
---

# Line Incubation

**Family:** explore
**Mode:** both (search to find the cheapest discriminating probe; evaluation to
run it and judge what survived)
**Status:** Phase 3 design — v1.0 LOCK-CANDIDATE (autonomous run, DEC-019).
Phase 4 will map this protocol to execution atoms.
**Consumes:** one early-lifecycle research line (`stage: seed | explored |
validated`) from `line-registry.md`.
**Emits:** `lifecycle_candidate` (type `promote`) → `govern/lifecycle-review`
(which decides the stage move); information-gain entries → `information-portfolio`.

## Purpose

Move a **single early-lifecycle research line** toward maturity through **light,
bounded validation** — the smallest probe that would change the program's belief
about whether the line deserves more attention. Incubation is the explore-side
counterpart to exploitation: it does the cheap, exploratory work that turns a
`seed` into something `explored` or `validated` *enough to be judged*, without yet
committing the deep effort that exploitation reserves for active lines.

Incubation **proposes** stage advancement; it does not move stage. The two-axis
model (DEC-018) is authoritative: `stage` is maturity, `status` is attention.
Incubation only ever speaks to **maturity** — and only as a *candidate*. The
actual stage move belongs to `govern/lifecycle-review`. This keeps the
explore/govern boundary clean: the workflow that *advances understanding* of a
line is not the workflow that *re-allocates the program's attention* to it.

This is a **both-Mode** workflow and must name the mode per phase: Search Mode when
designing the discriminating probe (what cheap test would most change belief);
Evaluation Mode when running the probe and judging the result. It must not silently
blur them — the probe is *designed* permissively and *judged* strictly.

## Authority boundaries

- **May:** read one line's registry entry, artifacts, and standing; design and run
  a *bounded* validation probe (a toy model, a small derivation check, a
  literature cross-check, a counterexample search); record what was learned;
  propose a `promote` `lifecycle_candidate`; record an information-gain entry even
  when the probe fails the line; flag new test/claim/persona candidates; emit
  governance signals for missing routes.
- **Must not:** move `stage` or `status` (→ `govern/lifecycle-review`); register or
  number lines (→ `govern/line-intake`); assign standing scores
  (→ `govern/line-review`); decide a claim is true/false or write the claim ledger;
  perform deep exploitation work reserved for active lines (→ `exploit/*`);
  archive/retire a line directly; exceed the bounded-probe budget (escalate instead).
- **Scoring authority:** judgment-with-rationale, bounded. Incubation reports
  *what the probe showed* and a *promotion-readiness read*; it does not compute the
  seven standing dimensions (that is line-review).
- **Write authority:** patch-first. Bounded artifacts (toy models, probe notes)
  may be written under the line's working area as **exploratory** material; any
  change to canonical line state, stage, or authority surfaces is a proposal only.

## Read surfaces

- **Target line:** its `line-registry.md` entry (stage, status, relationships,
  why-state, next candidate move) and its `models/`, `results/`, `tests/`, `claims/`.
- **Standing (context):** the latest `govern/line-review` standing snapshot for the
  line, if present — used to understand evidence posture, not re-derived.
- **Health substrate:** `registries/research-line-scorecard.md`.
- **Foundation neighbors:** relevant `literature/` notes (cheap cross-check basis).
- **Research Operating Model:** `RESEARCH-OPERATING-MODEL.md` — both-Mode discipline
  (§1), lifecycle (§4), promotion criteria (§5), information-gain (§3),
  authority order (§11).
- **Decision History:** `registries/decision-history.md` — two-axis model (DEC-018),
  constraints on the line.
- **Authority surfaces (context only):** `../NORTH-STAR.md`, `CLAIM-LEDGER.md`,
  `ROADMAP.md`, `HYPOTHESES.md`.
- **Workflow catalog:** `README.md` / `WORKFLOW-SKELETON-PROPOSAL.md` — validate routes.
- Explore Memory Pack load surface (Phase 3.5; inert if absent).

## Write surfaces

- A **bounded probe artifact** (toy model / probe note) under the line's working
  area, labeled exploratory — non-canonical.
- An **incubation report** (operational log) to `logs/`.
- A **`lifecycle_candidate`** (type `promote`) → `govern/lifecycle-review`.
- An **information-gain entry** → `govern/information-portfolio` (positive even on
  a failed probe, per §3).
- **New test/claim/persona candidates** → `tests/` proposal, `govern/line-review`,
  or `explore/persona-expansion` respectively (flags, not direct writes).
- **Governance signals** → the docket.

**No canonical write.** Stage advancement is always a candidate to lifecycle-review.

## Memory interface (Phase 3.5; may be inert)

- Reads (load surface): probe designs that have repeatedly discriminated (or
  failed to), known cheap-test patterns per cluster, prior "over-incubation" notes
  (running heavy validation on a line that should have escalated to exploit).
- Writes (learning-return, after a run): `guidance_used`, `missing_guidance`,
  `confusion_or_conflict`, `observed_failure_mode`, `output_quality_signal`,
  `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** `line-registry.md` (one line), `research-line-scorecard.md`,
  `decision-history.md`.
- **Writes:** none to canonical state. Proposes a `promote` candidate to
  lifecycle-review; proposes an information-portfolio entry; appends a run log.

## Procedure (runnable scope: one research line)

1. **Intake and bound (deterministic precondition).** Confirm the line exists, is
   early-lifecycle (`stage: seed | explored | validated`), and is `status: active`.
   If it is exploit-tier or `status: held | archived`, STOP and route (advancing a
   held/archived or exploit-tier line is not incubation's job). State an explicit
   **probe budget** (the bounded scope this run may spend).
2. **(Search Mode) Design the discriminating probe.** Identify the single cheapest
   test that would most change belief about whether the line should advance —
   informed by its standing, its `next candidate move`, and its open dependencies.
   Name what a pass vs a fail would mean *before* running it.
3. **(Evaluation Mode) Run the probe within budget.** Execute the bounded toy
   model / derivation check / literature cross-check / counterexample search.
   Record the result honestly, including a null or negative result.
4. **Judge promotion-readiness.** Decide whether the probe result, against the §5
   promotion criteria (cross-cluster support, mathematical/repo traction, a concrete
   next test, specialist conviction), makes the line a **promote candidate**, a
   **stay-put** (more incubation, or hand to exploit), or a **demote/retire signal**
   (route to lifecycle-review; incubation does not retire).
5. **Record information gain.** Whatever the outcome, write what the program now
   understands that it did not before (§3) — a failed probe that reveals a missing
   definition or kills a weak assumption is a successful run.
6. **Emit.** Probe artifact, incubation report, a `promote` `lifecycle_candidate`
   if warranted, an information-portfolio entry, flagged test/claim/persona
   candidates, governance signals. End with the verdict block.

## Outputs (shapes)

**Promote lifecycle candidate** (routed to `govern/lifecycle-review`, encoded per
its canonical schema):

```yaml
lifecycle_candidate:
  candidate_type: promote
  affected_line:
  current_state:                 # e.g. stage: explored, status: active
  proposed_state_or_direction:   # e.g. stage -> validated
  reason:
  evidence_or_basis:             # the probe result + cited artifacts
  source_workflow: explore/line-incubation
  source_report:                 # incubation report pointer
  confidence: low | med | high
  why_source_workflow_cannot_decide: "incubation may advance understanding but must not move stage (DEC-018); lifecycle-review owns the stage move."
```

**Incubation report** (operational log): line, run date, declared probe budget,
mode-per-phase, probe design, probe result (incl. nulls), promotion-readiness
judgment, information-gain note, flags emitted.

**Information-gain entry** (→ `information-portfolio`): what changed in program
understanding, positive even on a failed probe.

**Governance docket item** (missing route / over-budget / policy gap): standard
shape with `signal_type` ∈ {undefined-workflow-needed, probe-budget-policy-needed,
demote-or-retire-signal, manual-review-required}.

Every run ends with the verdict block.

## Escalation triggers

Route OUT: a `promote`-worthy result → `govern/lifecycle-review`; a line that has
outgrown incubation and deserves deep development → `exploit/advance-secondary`
(or `advance-primary` via lifecycle-review, never directly); a probe result that
*weakens* the line → a `demote`/`retire` **signal** to `govern/lifecycle-review`
(incubation never retires); a probe that needs more than the bounded budget →
stop and emit a `more-evidence-needed`/budget docket item rather than overspending;
a new persona lens needed → `explore/persona-expansion`; a new test worth keeping →
`tests/` proposal; missing route → docket `undefined-workflow-needed`;
registry/authority conflict → log as `confusion_or_conflict`, defer to §11.

## Failure modes

- **Stage creep (moving stage itself).** Guard: incubation only proposes `promote`
  candidates; the move belongs to lifecycle-review (DEC-018).
- **Over-incubation (heavy exploitation in disguise).** A line gets deep effort it
  should earn through lifecycle-review first. Guard: explicit probe budget in step
  1; over-budget → escalate, don't spend.
- **Mode blur.** Permissive design and strict judgment run together. Guard: name
  the mode per phase; define pass/fail *before* running the probe.
- **Failure treated as worthless.** A negative probe is discarded. Guard:
  mandatory information-gain entry (§3) — failed probes that teach are successes.
- **Axis collapse.** Confusing `stage` advance with a `status` change. Guard: the
  two-axis model; incubation speaks only to maturity.
- **Silent candidate loss / dangling route.** Guard: every outcome produces a
  report entry; missing routes → `undefined-workflow-needed`.

## Success criteria

A good run takes one early-lifecycle line, runs the *cheapest probe that could
change its standing*, and returns either a defensible `promote` candidate or a
defensible stay/weaken signal — plus a recorded information-gain entry — all within
a stated budget, without moving any canonical state.

Cheap test: a reviewer can tell, without re-running the probe, what was tested,
what a pass vs fail meant, what actually happened, what the program now understands
that it did not before, and which downstream workflow owns the consequence.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `explore/incubation-probe-design` — one line; (Search) emits a bounded probe
  plan with pass/fail criteria; judgment-based.
- `explore/incubation-probe-run` — one probe plan; (Evaluation) executes within
  budget, emits a result + artifact; deterministic-to-run, judgment-to-interpret.
- `explore/incubation-promotion-judgment` — one probe result; emits a `promote`
  candidate or stay/weaken signal + information-gain entry; judgment-based.

Likely cadence differences:
- Round-robin across early-lifecycle lines (periodic), or event-triggered when
  line-review flags a `lifecycle-candidate` on an early line.

Likely context boundaries:
- Each atom loads only the one line's entry, artifacts, standing snapshot, relevant
  literature, and the explore Memory Pack load surface. No full panel; no cross-line load.

Likely deterministic vs judgment split:
- Deterministic: intake/eligibility check (stage/status), budget enforcement,
  probe execution where the test is mechanical, route-target existence.
- Judgment-based: probe design, result interpretation, promotion-readiness,
  information-gain framing.

Phase 4 coverage questions:
- Does every probe result have a downstream consumer? (promote → lifecycle-review;
  weaken → lifecycle-review; gain → information-portfolio.)
- Does every run record an information-gain entry, pass or fail?
- Does every over-budget probe escalate rather than overspend?
- Is the stage move owned only by lifecycle-review (never by incubation)?
- Is any unit too large for one agent run? (probe-run is the expensive seam.)

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```

## Open questions

1. **Probe budget policy** — what bounds a "light" probe (time/compute/scope), and
   who sets it? Until set, runs declare a self-bound and over-budget escalates.
   (Docketed: `probe-budget-policy-needed`.)
2. **Weaken signals** — incubation can surface evidence that a line should be
   *demoted/retired*, but only lifecycle-review acts. Confirm `demote`/`retire`
   candidates may originate here (vs only from line-review).
3. **Hand-off to exploit** — exact threshold at which an incubated line stops being
   incubation's object and becomes `exploit/advance-secondary`'s; reconcile with
   lifecycle-review's promotion threshold (its Open Question #6).
4. **information-portfolio shape** — the entry schema is owned by
   `govern/information-portfolio`; incubation conforms to whatever it locks.
