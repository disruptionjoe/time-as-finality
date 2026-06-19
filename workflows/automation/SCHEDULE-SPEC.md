---
document_type: specification
primary_reader: governance
read_pattern: current_state
write_pattern: edit_in_place
authority: guidance_only
summarizable: false
---

# Schedule Spec — Cadences, Trigger Types, and Ordering

**Phase 4 design/spec only.** This document states the *intended* cadences and
trigger **types**, the ordering/dependencies between atoms, and the
research-budget posture. It arms nothing. Every concrete trigger is listed in
`TRIGGER-REGISTRY.md` with `status: NOT-ARMED`.

> **No live triggers are armed in this phase; arming is a separate, later,
> human-gated step.**

Atom names and properties are defined in `COVERAGE-MATRIX.md`. This file groups
them by trigger type and describes how they would sequence *if and when* arming
occurs.

---

## 1. Trigger-type groups

Four trigger types are used (§13): **event**, **periodic**, **threshold**,
**manual**. Atoms are grouped by their primary type; some atoms are dual-natured
(noted inline).

### 1a. Event-driven

Fire when an upstream atom emits a specific object. These are the connective
tissue of the system — most routing and acceptance preconditions live here.

- `govern/line-hygiene-check` — on a registry entry change.
- `govern/lifecycle-candidate-intake` -> `single-line-lifecycle-review` ->
  `lifecycle-preservation-check` — on a lifecycle candidate from line-review,
  incubation, challenge, or integrate.
- `govern/portfolio-question-intake` -> `overlap-resolution` /
  `merge-split-execution-proposal` — on an overlap/structural flag.
- `govern/contract-rollout`, `govern/log-hygiene-sweep` — on file/log change.
- `govern/line-information-gain-entry` — on a run that changed understanding.
- `govern/archival-gain-capture` — **must** fire on every lifecycle retirement
  (wired to `lifecycle-patch-acceptance` retire outcome).
- `explore/foundation-item-select` -> `foundation-note-write` ->
  `foundation-flag-route` — on a queued item / high-priority add.
- `explore/incubation-probe-design` -> `incubation-probe-run` ->
  `incubation-promotion-judgment` — on a line-review lifecycle-candidate.
- `explore/persona-draft` -> `persona-proposal-emit` — on a confirmed gap.
- `explore/synthesis-corpus-assemble` ... `synthesis-route` — after a persona
  sprint or a batch of foundation ingestions (event), also periodic (see 1b).
- `exploit/primary-move-select` -> `primary-move-execute` ->
  `status-patch-propose` — the main forward cadence (event-chained).
- `exploit/secondary-budget-check` -> `secondary-move-execute` ->
  `status-patch-propose`.
- `exploit/challenge-select` -> `challenge-execute` -> `challenge-route`.
- `exploit/integration-readiness-check` -> `integration-assemble` ->
  `integration-route` — on a maturity signal.

### 1b. Periodic

Run on a recurring rhythm to keep the program fresh; **cadence values are
deliberately UNDECIDED** (arming prerequisite).

- `govern/single-line-standing-review` — round-robin across lines (often).
- `govern/cross-run-synthesis`, `govern/project-log-catchup`,
  `govern/compaction-resilience-check` — periodic memory upkeep.
- `govern/portfolio-balance-read`, `govern/ledger-coverage-check` — periodic
  ledger upkeep.
- `explore/landscape-reassessment` (all four atoms) — **the program's main
  periodic move** (ROM §2); also event-triggered after a major synthesis
  convergence or a ridge-moving primary result.
- `explore/cross-disciplinary-synthesis` — periodic once enough new exploration
  has accumulated.
- `explore/line-discovery` (generation/dedup/seed-emit) — low-cadence widening.

### 1c. Threshold-based

Fire when an accumulated quantity crosses a bar; **bars are UNDECIDED**.

- `govern/dependency-graph-audit`, `govern/portfolio-balance-check` — on a
  registry-size / drift threshold.
- `govern/memory-pack-summarizer` — when a family raw log grows past a
  summarization threshold (cadence set at memory-layer build).
- `govern/docket-triage` -> `decision-worthiness-judgment` ->
  `decision-proposal-draft` — periodic over the accumulating docket; recurrence
  count is the worthiness threshold.
- `explore/persona-gap-collect` — when a recurring blind spot crosses a bar.

### 1d. Manual-only (never scheduled, never event-armed)

These touch canonical state or fairness-class policy. They are listed for
completeness and **require explicit authority each time**.

- `govern/lifecycle-patch-acceptance` — writes line-registry stage/status.
- `govern/decision-acceptance` — writes canonical Decision History.
- `govern/line-add-acceptance` — writes the line registry.
- `govern/cluster-normalization-review` — changes voting-weight rules
  (high-scrutiny).
- Every "patch accept step" referenced by the patch-first atoms (owner UNDECIDED).

---

## 2. Ordering and dependencies

The system is a small number of chains plus a shared governance sink. The
invariant: **proposing atoms run automatically; accepting atoms never do.**

```text
Exploit forward chain (event):
  primary-move-select -> primary-move-execute -> status-patch-propose --> [accept step]
                                              \-> artifact --> integrate-results (later)
                                              \-> info-gain --> information-portfolio
                                              \-> posture signal --> line-review

Exploit challenge chain (periodic+event):
  challenge-select -> challenge-execute -> challenge-route --> lifecycle-review (demote candidate)
                                                          \-> line-review (re-score)

Govern standing/lifecycle chain:
  line-hygiene-check (gate) -> single-line-standing-review
        -> lifecycle candidate --> lifecycle-candidate-intake -> single-line-lifecycle-review
              -> lifecycle-preservation-check (gate) -> [lifecycle-patch-acceptance: MANUAL]
                    -> retire outcome --> archival-gain-capture (MUST fire)

Govern structural chain:
  (overlap/structural flag) -> portfolio-question-intake
        -> overlap-resolution / merge-split-execution-proposal --> [accept step]
              -> per-line moves --> lifecycle-review

Govern decision chain (DEC-022):
  (all governance signals) -> docket-triage -> decision-worthiness-judgment
        -> decision-proposal-draft (inert) -> [decision-acceptance: MANUAL]

Explore intake chain:
  discovery-generation -> discovery-dedup -> discovery-seed-emit
        --> candidate-line-intake -> line-dedupe-check -> line-add-proposal
              -> [line-add-acceptance: MANUAL]

Explore foundation chain:
  foundation-item-select -> foundation-note-write -> foundation-flag-route
        --> line-discovery / synthesis / persona-expansion

Explore synthesis/reassessment (kept distinct):
  synthesis-corpus-assemble -> structural-extract -> convergence-match -> route
  reassessment-landscape-load -> topology-survey -> shift-test -> route
```

**Hard ordering rules to enforce at arming time:**

1. Hygiene/readiness/budget/preservation **gates** precede their expensive atoms
   (hygiene before standing; readiness before assemble; budget before secondary
   move; preservation before lifecycle acceptance).
2. Every **acceptance** atom is downstream of, and gated separately from, its
   proposing atom. Acceptance never chains automatically from a proposal.
3. `archival-gain-capture` is a **mandatory** consequence of any retire — it must
   be wired so a retirement cannot complete without it.
4. **Sole-owner** boundaries (no double-review): portfolio-review owns all
   cross-line reconciliation; lifecycle-review owns all stage/status moves;
   decision-review owns canonization; persona-governance owns persona clustering;
   synthesis != reassessment.

---

## 3. Research-budget and resource notes (ROM §2)

The thing being scheduled is the **research budget**: compute, agent attention,
automation cadence, human attention, review effort (ROM §2). Allocation honesty
across Explore / Exploit / Govern is the point of the split.

- **Exploit cadence dominates forward progress but must not starve the others.**
  `primary-move-execute` is the highest-frequency atom; `secondary-move-execute`
  is deliberately interleaved at lower frequency, gated by
  `secondary-budget-check` every time (budget honesty).
- **The expensive seams are budget-bounded, not time-bounded.** The six
  `too_large_risk: high` atoms (foundation-note-write, reassessment-topology-survey,
  incubation-probe-run, primary/secondary-move-execute, challenge-execute) each
  need an explicit per-run budget cap before arming. `incubation-probe-run` must
  escalate rather than overspend.
- **Whole-graph atoms are rare by construction** (dependency-graph-audit,
  portfolio-balance-check, reassessment-landscape-load) — slow cadence / high
  threshold so the irreducible broad-context load is paid infrequently.
- **Govern upkeep is cheap and frequent** (log-hygiene, contract-rollout,
  standing round-robin) so the audit trail never drifts far.
- **Human attention is the scarcest budget.** Every manual-only acceptance atom
  spends it; the design minimizes how often acceptance is requested by clustering
  (docket-triage) and batching (contract-rollout).
- **Concrete numbers are NOT set here** (cadence values, thresholds, budget caps,
  round-robin period). They are arming prerequisites, not Phase-4 policy.

---

## 4. Atoms that should NOT be automated yet

Beyond the always-manual acceptance atoms (§1d), defer arming for:

- **All patch-first proposing atoms** until the **patch-acceptance owner is
  decided** (line-review OQ#2). Without a named accept step, auto-proposing
  patches would pile up unowned.
- **`memory-pack-summarizer` and every memory-pack read** until the Phase-3.5
  memory layer is built and validated (N shadow runs vs a no-pack baseline,
  per MEMORY-LAYER-PLAN).
- **`reassessment-topology-survey`, `foundation-note-write`, `challenge-execute`,
  `incubation-probe-run`, `primary/secondary-move-execute`** until per-run budget
  caps and size-bounds exist (the six high-risk seams).
- **`dependency-graph-audit` / `portfolio-balance-check` / `persona-gap-collect`**
  until their thresholds are defined.
- **`single-line-standing-review`** for high-stakes lines until the 0-3
  calibration anchors exist (OQ#3), to avoid inconsistent scoring across agents.
- **`deep-panel-review`** (event sub-atom) until it is decided whether it is a
  standalone workflow or an inline atom.

What is *closest* to safe-to-arm once an owner and caps exist: the deterministic
gates and routers (`line-hygiene-check`, `log-hygiene-sweep`, `*-intake`,
`*-route`, `*-dedup`) — they propose/route only and write no canonical state.

---

## 5. Open questions carried into arming

1. Patch-acceptance owner (blocks all patch-first atoms).
2. Concrete cadence values, thresholds, and per-run budget caps.
3. Memory layer build + validation (blocks summarizer and pack reads).
4. deep-panel-review: workflow vs inline atom.
5. 0-3 standing calibration anchors.
6. Snapshot/log storage location convention (`logs/runs/` vs `logs/standing/`).

None of these is resolved here; resolving them is part of the later, human-gated
arming step.
