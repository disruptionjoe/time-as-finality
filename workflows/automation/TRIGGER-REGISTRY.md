---
document_type: registry
primary_reader: governance
read_pattern: current_state
write_pattern: edit_in_place
authority: guidance_only
summarizable: false
---

# Trigger Registry

**EVERY TRIGGER BELOW IS A SPEC, NOT A LIVE TRIGGER. `status: NOT-ARMED` for all.**

> **No live triggers are armed in this phase; arming is a separate, later,
> human-gated step.** Reading or editing this file does not arm anything. No
> scheduled task, cron job, webhook, or event listener exists for any row here.
> Arming requires a deliberate, human-gated action that satisfies the row's
> `arming_prerequisites` — performed elsewhere, later, not by this file.

One object per intended trigger. `cadence` and `trigger_condition` are the
*intended* design (see `SCHEDULE-SPEC.md`); concrete values marked `UNDECIDED` are
themselves arming prerequisites. Atom definitions live in `COVERAGE-MATRIX.md`.

**Shared arming prerequisites (apply to all unless noted):**
- `repo-state: workflow LOCKED` — the owning workflow is locked for the current
  operating model.
- `governance: nothing armed without an explicit human-gated arming action.`

---

## Govern triggers

```yaml
- trigger_id: TRG-001
  atom: govern/line-hygiene-check
  cadence: on-event
  trigger_condition: a line-registry entry changes
  owning_workflow: govern/line-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED (done), patch-acceptance owner decided]

- trigger_id: TRG-002
  atom: govern/single-line-standing-review
  cadence: often (round-robin)
  trigger_condition: round-robin cursor reaches a line; period UNDECIDED
  owning_workflow: govern/line-review
  status: NOT-ARMED
  arming_prerequisites: [round-robin period set, 0-3 calibration anchors, patch-acceptance owner decided]

- trigger_id: TRG-003
  atom: govern/lifecycle-candidate-intake
  cadence: on-event
  trigger_condition: a lifecycle candidate is emitted upstream
  owning_workflow: govern/lifecycle-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED (done)]

- trigger_id: TRG-004
  atom: govern/single-line-lifecycle-review
  cadence: on-event
  trigger_condition: a validated lifecycle candidate exists
  owning_workflow: govern/lifecycle-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED (done)]

- trigger_id: TRG-005
  atom: govern/lifecycle-patch-acceptance
  cadence: manual
  trigger_condition: a human authority accepts a lifecycle recommendation
  owning_workflow: govern/lifecycle-review
  status: NOT-ARMED
  arming_prerequisites: [NEVER auto-armed; explicit authority each run; line-registry two-axis schema live (DEC-020, done)]

- trigger_id: TRG-006
  atom: govern/lifecycle-preservation-check
  cadence: on-event
  trigger_condition: a hold/retire/split/merge/demote is recommended
  owning_workflow: govern/lifecycle-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED (done)]

- trigger_id: TRG-007
  atom: govern/portfolio-question-intake
  cadence: on-event
  trigger_condition: a portfolio question / structural flag is routed in
  owning_workflow: govern/portfolio-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-008
  atom: govern/dependency-graph-audit
  cadence: periodic
  trigger_condition: registry-size / drift threshold crossed; threshold UNDECIDED
  owning_workflow: govern/portfolio-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, threshold defined]

- trigger_id: TRG-009
  atom: govern/overlap-resolution
  cadence: on-event
  trigger_condition: an overlap pair/cluster is flagged
  owning_workflow: govern/portfolio-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, patch-acceptance owner decided]

- trigger_id: TRG-010
  atom: govern/merge-split-execution-proposal
  cadence: on-event
  trigger_condition: a merge/split is routed from lifecycle-review
  owning_workflow: govern/portfolio-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, patch-acceptance owner decided]

- trigger_id: TRG-011
  atom: govern/portfolio-balance-check
  cadence: periodic
  trigger_condition: balance-check threshold crossed; threshold UNDECIDED
  owning_workflow: govern/portfolio-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, threshold defined]

- trigger_id: TRG-012
  atom: govern/docket-triage
  cadence: accumulated/periodic
  trigger_condition: docket reaches a triage cadence; cadence UNDECIDED
  owning_workflow: govern/decision-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, triage cadence set]

- trigger_id: TRG-013
  atom: govern/decision-worthiness-judgment
  cadence: accumulated/periodic
  trigger_condition: a clustered decision-worthy candidate exists
  owning_workflow: govern/decision-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-014
  atom: govern/decision-proposal-draft
  cadence: accumulated/periodic
  trigger_condition: a candidate is judged decision-worthy
  owning_workflow: govern/decision-review
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-015
  atom: govern/decision-acceptance
  cadence: manual
  trigger_condition: a human authority accepts a DEC proposal
  owning_workflow: govern/decision-review
  status: NOT-ARMED
  arming_prerequisites: [NEVER auto-armed; explicit authority each run; only atom that writes canonical Decision History]

- trigger_id: TRG-016
  atom: govern/candidate-line-intake
  cadence: on-event
  trigger_condition: an explore seed or manual proposal arrives
  owning_workflow: govern/line-intake
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-017
  atom: govern/line-dedupe-check
  cadence: on-event
  trigger_condition: a normalized candidate exists
  owning_workflow: govern/line-intake
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-018
  atom: govern/line-add-proposal
  cadence: on-event
  trigger_condition: a candidate is judged novel
  owning_workflow: govern/line-intake
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-019
  atom: govern/line-add-acceptance
  cadence: manual
  trigger_condition: a human authority accepts an RL-NNN ADD proposal
  owning_workflow: govern/line-intake
  status: NOT-ARMED
  arming_prerequisites: [NEVER auto-armed; explicit authority each run; only atom that writes the line registry]

- trigger_id: TRG-020
  atom: govern/persona-integrity-check
  cadence: on-event
  trigger_condition: a persona/registry surface changes
  owning_workflow: govern/persona-governance
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-021
  atom: govern/persona-mirror-sync
  cadence: on-event
  trigger_condition: canonical panel vs skill mirror diverge
  owning_workflow: govern/persona-governance
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, post-acceptance sync step owner decided]

- trigger_id: TRG-022
  atom: govern/single-persona-recluster
  cadence: periodic/on-event
  trigger_condition: a recluster is requested or due
  owning_workflow: govern/persona-governance
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, patch-acceptance owner decided]

- trigger_id: TRG-023
  atom: govern/cluster-normalization-review
  cadence: manual (rare)
  trigger_condition: a voting-weight rule change is proposed
  owning_workflow: govern/persona-governance
  status: NOT-ARMED
  arming_prerequisites: [HIGH-SCRUTINY; explicit authority; fairness review; never scheduled]

- trigger_id: TRG-024
  atom: govern/cross-run-synthesis
  cadence: periodic
  trigger_condition: a run window closes; cadence UNDECIDED
  owning_workflow: govern/research-memory
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, window cadence set]

- trigger_id: TRG-025
  atom: govern/contract-rollout
  cadence: on-event
  trigger_condition: a file lacks a document contract / changes
  owning_workflow: govern/research-memory
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, patch-acceptance owner decided]

- trigger_id: TRG-026
  atom: govern/log-hygiene-sweep
  cadence: often/on-event
  trigger_condition: logs/indices/markers change
  owning_workflow: govern/research-memory
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, patch-acceptance owner decided]

- trigger_id: TRG-027
  atom: govern/project-log-catchup
  cadence: periodic
  trigger_condition: PROJECT-LOG falls behind recent runs; cadence UNDECIDED
  owning_workflow: govern/research-memory
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, cadence set]

- trigger_id: TRG-028
  atom: govern/memory-pack-summarizer
  cadence: threshold/periodic
  trigger_condition: a family memory-log grows past a summarization threshold
  owning_workflow: govern/research-memory
  status: NOT-ARMED
  arming_prerequisites: [memory layer LIVE (Phase 3.5 built + validated), summarizer cadence set]

- trigger_id: TRG-029
  atom: govern/compaction-resilience-check
  cadence: periodic
  trigger_condition: periodic self-test; cadence UNDECIDED
  owning_workflow: govern/research-memory
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, cadence set]

- trigger_id: TRG-030
  atom: govern/line-information-gain-entry
  cadence: on-event
  trigger_condition: a run changed a line's understanding
  owning_workflow: govern/information-portfolio
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-031
  atom: govern/archival-gain-capture
  cadence: on-event (mandatory)
  trigger_condition: a line is retired (lifecycle-patch-acceptance retire outcome)
  owning_workflow: govern/information-portfolio
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, wired to lifecycle retire so it cannot be skipped]

- trigger_id: TRG-032
  atom: govern/portfolio-balance-read
  cadence: periodic
  trigger_condition: periodic balance read; cadence UNDECIDED
  owning_workflow: govern/information-portfolio
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, cadence set]

- trigger_id: TRG-033
  atom: govern/ledger-coverage-check
  cadence: periodic
  trigger_condition: periodic coverage check; cadence UNDECIDED
  owning_workflow: govern/information-portfolio
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, cadence set]
```

## Explore triggers

```yaml
- trigger_id: TRG-034
  atom: explore/synthesis-corpus-assemble
  cadence: periodic/on-event
  trigger_condition: enough new exploration accumulated, or after a persona sprint/foundation batch
  owning_workflow: explore/cross-disciplinary-synthesis
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, accumulation threshold set]

- trigger_id: TRG-035
  atom: explore/synthesis-structural-extract
  cadence: periodic/on-event
  trigger_condition: a scoped corpus exists
  owning_workflow: explore/cross-disciplinary-synthesis
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-036
  atom: explore/synthesis-convergence-match
  cadence: periodic/on-event
  trigger_condition: structural claims extracted
  owning_workflow: explore/cross-disciplinary-synthesis
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-037
  atom: explore/synthesis-route
  cadence: periodic/on-event
  trigger_condition: a convergence map exists
  owning_workflow: explore/cross-disciplinary-synthesis
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-038
  atom: explore/foundation-item-select
  cadence: periodic/on-event
  trigger_condition: queue has a 'proposed' item, or a high-priority add arrives
  owning_workflow: explore/foundation-ingestion
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, drain cadence set]

- trigger_id: TRG-039
  atom: explore/foundation-note-write
  cadence: on-event
  trigger_condition: an item is selected/ingested
  owning_workflow: explore/foundation-ingestion
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, per-source budget/size bound set]

- trigger_id: TRG-040
  atom: explore/foundation-flag-route
  cadence: on-event
  trigger_condition: a literature note is finished
  owning_workflow: explore/foundation-ingestion
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-041
  atom: explore/reassessment-landscape-load
  cadence: periodic/on-event
  trigger_condition: periodic (main periodic move), or a ridge-moving event; cadence UNDECIDED
  owning_workflow: explore/landscape-reassessment
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, cadence set]

- trigger_id: TRG-042
  atom: explore/reassessment-topology-survey
  cadence: periodic/on-event
  trigger_condition: a landscape is assembled
  owning_workflow: explore/landscape-reassessment
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, per-run budget cap set]

- trigger_id: TRG-043
  atom: explore/reassessment-shift-test
  cadence: periodic/on-event
  trigger_condition: a topology survey proposes shifts
  owning_workflow: explore/landscape-reassessment
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-044
  atom: explore/reassessment-route
  cadence: periodic/on-event
  trigger_condition: supported shifts exist
  owning_workflow: explore/landscape-reassessment
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-045
  atom: explore/discovery-generation
  cadence: periodic/on-event
  trigger_condition: low-cadence widening, or an under-covered-region flag
  owning_workflow: explore/line-discovery
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, cadence set]

- trigger_id: TRG-046
  atom: explore/discovery-dedup
  cadence: periodic/on-event
  trigger_condition: raw candidates generated
  owning_workflow: explore/line-discovery
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-047
  atom: explore/discovery-seed-emit
  cadence: periodic/on-event
  trigger_condition: candidates survive dedup
  owning_workflow: explore/line-discovery
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-048
  atom: explore/incubation-probe-design
  cadence: periodic/on-event
  trigger_condition: round-robin over early lines, or a lifecycle-candidate flag
  owning_workflow: explore/line-incubation
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-049
  atom: explore/incubation-probe-run
  cadence: on-event
  trigger_condition: a probe plan exists
  owning_workflow: explore/line-incubation
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, per-run budget cap set (escalate not overspend)]

- trigger_id: TRG-050
  atom: explore/incubation-promotion-judgment
  cadence: on-event
  trigger_condition: a probe result exists
  owning_workflow: explore/line-incubation
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-051
  atom: explore/persona-gap-collect
  cadence: threshold/accumulated
  trigger_condition: a recurring blind spot crosses a bar; bar UNDECIDED
  owning_workflow: explore/persona-expansion
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, gap-recurrence bar defined]

- trigger_id: TRG-052
  atom: explore/persona-draft
  cadence: on-event
  trigger_condition: a genuine gap is confirmed
  owning_workflow: explore/persona-expansion
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-053
  atom: explore/persona-proposal-emit
  cadence: on-event
  trigger_condition: persona proposals drafted
  owning_workflow: explore/persona-expansion
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]
```

## Exploit triggers

```yaml
- trigger_id: TRG-054
  atom: exploit/primary-move-select
  cadence: often/on-event
  trigger_condition: the forward cadence ticks; cadence UNDECIDED
  owning_workflow: exploit/advance-primary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, forward cadence set]

- trigger_id: TRG-055
  atom: exploit/primary-move-execute
  cadence: often
  trigger_condition: a bounded move spec exists
  owning_workflow: exploit/advance-primary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, per-move budget cap set]

- trigger_id: TRG-056
  atom: exploit/status-patch-propose (primary)
  cadence: on-event
  trigger_condition: a move earns a status change
  owning_workflow: exploit/advance-primary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, patch-acceptance owner decided]

- trigger_id: TRG-057
  atom: exploit/secondary-budget-check
  cadence: on-event
  trigger_condition: a secondary move is contemplated
  owning_workflow: exploit/advance-secondary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-058
  atom: exploit/secondary-move-execute
  cadence: periodic (interleaved, lower freq)
  trigger_condition: budget verdict = advance
  owning_workflow: exploit/advance-secondary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, per-move budget cap set]

- trigger_id: TRG-059
  atom: exploit/status-patch-propose (secondary)
  cadence: on-event
  trigger_condition: a secondary move earns a conservative status change
  owning_workflow: exploit/advance-secondary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, patch-acceptance owner decided]

- trigger_id: TRG-060
  atom: exploit/challenge-select
  cadence: periodic/on-event
  trigger_condition: red-team cadence ticks, or a challenge-worthiness signal
  owning_workflow: exploit/challenge-primary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, red-team cadence set]

- trigger_id: TRG-061
  atom: exploit/challenge-execute
  cadence: periodic/on-event
  trigger_condition: a challenge spec exists
  owning_workflow: exploit/challenge-primary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, per-challenge budget cap set]

- trigger_id: TRG-062
  atom: exploit/challenge-route
  cadence: on-event
  trigger_condition: a challenge is adjudicated
  owning_workflow: exploit/challenge-primary
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, survival-argument rule enforced before any demote candidate]

- trigger_id: TRG-063
  atom: exploit/integration-readiness-check
  cadence: rare/on-event
  trigger_condition: a line emits a maturity signal
  owning_workflow: exploit/integrate-results
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]

- trigger_id: TRG-064
  atom: exploit/integration-assemble
  cadence: rare/on-event
  trigger_condition: the readiness gate passes
  owning_workflow: exploit/integrate-results
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED, patch-acceptance owner decided (durable surfaces)]

- trigger_id: TRG-065
  atom: exploit/integration-route
  cadence: rare/on-event
  trigger_condition: an integration bundle is assembled
  owning_workflow: exploit/integrate-results
  status: NOT-ARMED
  arming_prerequisites: [workflow LOCKED]
```

---

## Summary

- **65 intended triggers registered, TRG-001 .. TRG-065. Every one is
  `status: NOT-ARMED`.**
- **Manual-only / never-auto-armed:** TRG-005, TRG-015, TRG-019, TRG-023
  (acceptance + fairness-rule atoms that touch canonical state or voting policy).
- **Blocked on the patch-acceptance owner decision:** every patch-first proposing
  trigger (TRG-001, 002, 009, 010, 022, 025, 026, 056, 059, 064 and the wider
  patch-first set).
- **Blocked on the memory layer going live:** TRG-028.
- **Blocked on undecided thresholds/cadences/budget caps:** TRG-002, 008, 011,
  012, 024, 027, 028, 029, 032, 033, 034, 038, 039, 041, 042, 045, 049, 051,
  054, 055, 058, 060, 061.

No trigger in this registry is live. Arming any row is a separate, later,
human-gated step.
