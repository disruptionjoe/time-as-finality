---
document_type: registry
primary_reader: governance
read_pattern: current_state
write_pattern: edit_in_place
authority: guidance_only
summarizable: false
---

# Coverage Matrix — Workflow → Task Atoms

**Phase 4 design/spec only. No trigger here is armed (see `TRIGGER-REGISTRY.md`).**

For every one of the 18 Phase-3 workflows, this matrix enumerates the task atoms
named in that workflow's *Future automation decomposition notes* and records one
YAML block per atom. Atom names are taken verbatim from the workflows where given.

**Field key.** `deterministic_or_judgment` = the atom's core nature (deterministic
| judgment | hybrid). `cadence` = intended rhythm (often | periodic | rare |
on-event | accumulated). `trigger` = type only (event | periodic | threshold |
manual). `patch_only_fields` = fields this atom may only *propose* a change to
(patch-first). `direct_write_fields` = fields/objects it may write directly (audit
artifacts, run logs, non-canonical notes). `escalation_target` = where its
route-out signals go. `memory_pack_used` = exploit | explore | govern (load
surface only; inert if absent). `too_large_risk` = low | med | high.

**Authority reminder (DEC-013):** every atom inherits its workflow's authority and
never exceeds it. Acceptance atoms that touch canonical state never auto-run.

---

## govern/line-review (LOCKED v1.2)

```yaml
- workflow: govern/line-review
  task_name: line-hygiene-check
  unit_of_work: one research line registry entry
  loads: [line-registry entry, artifact links, relationship targets]
  emits: [hygiene report, clerical patch]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: hygiene report (logs/), clerical patch proposal
  patch_only_fields: [clerical/mechanical metadata, broken artifact links]
  direct_write_fields: [hygiene report artifact in logs/]
  downstream_consumers: [single-line-standing-review (gate), patch accept step]
  escalation_target: govern/decision-review (docket) on schema inadequacy
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: short-circuits scored review on failure; does not score.

- workflow: govern/line-review
  task_name: single-line-standing-review
  unit_of_work: one research line -> all seven standing dimensions -> one snapshot
  loads: [line entry, artifacts, relationships, research-line-scorecard, authority surfaces]
  emits: [standing snapshot, interpretive patch proposal, lifecycle candidates, governance signals]
  deterministic_or_judgment: judgment
  cadence: often
  trigger: periodic
  writes: standing snapshot (logs/, non-canonical)
  patch_only_fields: [stale source-state fields, evidence pointers, relationship fields, mis-scored substrate entries]
  direct_write_fields: [standing snapshot audit artifact]
  downstream_consumers: [audit, patch accept step, govern/lifecycle-review, govern/decision-review (docket)]
  escalation_target: lifecycle-review (candidates); decision-review/docket (governance signals); line-review never acts
  memory_pack_used: govern
  too_large_risk: med
  coverage_notes: do NOT split below the line level; snapshot never becomes canonical. deep-panel-review is an event sub-atom only on needs-persona-review.
```

## govern/lifecycle-review (LOCKED v1.0)

```yaml
- workflow: govern/lifecycle-review
  task_name: lifecycle-candidate-intake
  unit_of_work: one lifecycle candidate
  loads: [candidate, line-registry, vocabulary schema]
  emits: [validated/normalized candidate or intake failure]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: normalized candidate object
  patch_only_fields: []
  direct_write_fields: [normalized candidate, intake-failure note]
  downstream_consumers: [single-line-lifecycle-review]
  escalation_target: govern/decision-review (docket) on dangling route
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: alias/schema/required-field validation only.

- workflow: govern/lifecycle-review
  task_name: single-line-lifecycle-review
  unit_of_work: one line, one lifecycle question
  loads: [line entry, standing snapshot, artifacts, line-registry]
  emits: [decision report, patch proposal]
  deterministic_or_judgment: judgment
  cadence: on-event
  trigger: event
  writes: decision report (logs/)
  patch_only_fields: [status (active|held|archived), stage (promote/demote/integrate)]
  direct_write_fields: [decision report]
  downstream_consumers: [lifecycle-patch-acceptance, portfolio-review (split/merge), information-portfolio (retire)]
  escalation_target: portfolio-review (structural); decision-review (recurring patterns)
  memory_pack_used: govern
  too_large_risk: med
  coverage_notes: promote/integrate high-scrutiny; never canonizes truth; split/merge route out.

- workflow: govern/lifecycle-review
  task_name: lifecycle-patch-acceptance
  unit_of_work: one accepted recommendation
  loads: [accepted recommendation, line-registry]
  emits: [registry update, Project Log entry]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: manual
  writes: line-registry (stage/status), PROJECT-LOG.md
  patch_only_fields: []
  direct_write_fields: [line-registry stage/status fields, PROJECT-LOG entry]
  downstream_consumers: [information-portfolio (archival-gain-capture on retire)]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: REQUIRES EXPLICIT AUTHORITY; never auto-runs. Only atom that writes lifecycle state.

- workflow: govern/lifecycle-review
  task_name: lifecycle-preservation-check
  unit_of_work: one hold/retire/split/merge/demote
  loads: [the action's preservation note]
  emits: [preservation-completeness verdict]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: preservation-check note (logs/)
  patch_only_fields: []
  direct_write_fields: [preservation-check note]
  downstream_consumers: [lifecycle-patch-acceptance (gate)]
  escalation_target: govern/decision-review (docket) if revival conditions missing
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: guarantees archive-never-delete revival conditions exist (ROM §5).
```

## govern/portfolio-review

```yaml
- workflow: govern/portfolio-review
  task_name: portfolio-question-intake
  unit_of_work: one portfolio question
  loads: [the question, line-registry]
  emits: [validated/normalized question or intake failure]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: normalized question object
  patch_only_fields: []
  direct_write_fields: [normalized question, intake-failure note]
  downstream_consumers: [dependency-graph-audit, overlap-resolution, merge-split-execution-proposal, portfolio-balance-check]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: the unit of review is a portfolio question, not a single line.

- workflow: govern/portfolio-review
  task_name: dependency-graph-audit
  unit_of_work: whole line-registry dependency graph
  loads: [line-registry, relationship edges]
  emits: [cycles/dangling/contradicting edges, edge-correction patch proposal]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: threshold
  writes: graph-audit report (logs/)
  patch_only_fields: [relationship edges]
  direct_write_fields: [graph-audit report]
  downstream_consumers: [patch accept step]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: med
  coverage_notes: whole-graph load is irreducible; threshold on registry size (UNDECIDED).

- workflow: govern/portfolio-review
  task_name: overlap-resolution
  unit_of_work: one overlap pair/cluster
  loads: [affected lines' entries, artifacts, standing snapshots]
  emits: [merge | demarcate | accept recommendation]
  deterministic_or_judgment: judgment
  cadence: on-event
  trigger: event
  writes: overlap recommendation (logs/)
  patch_only_fields: [relationship/demarcation fields]
  direct_write_fields: [overlap recommendation]
  downstream_consumers: [merge-split-execution-proposal, patch accept step]
  escalation_target: govern/lifecycle-review (per-line consequences)
  memory_pack_used: govern
  too_large_risk: med
  coverage_notes: triggered by line-review overlap flags.

- workflow: govern/portfolio-review
  task_name: merge-split-execution-proposal
  unit_of_work: one routed merge/split
  loads: [affected lines, artifacts, information-portfolio]
  emits: [structural patch, routed lifecycle candidates]
  deterministic_or_judgment: judgment
  cadence: on-event
  trigger: event
  writes: structural patch proposal (logs/)
  patch_only_fields: [line-registry structure (merge/split), relationship edges]
  direct_write_fields: [structural patch proposal]
  downstream_consumers: [patch accept step (authority), lifecycle-review (per-line moves)]
  escalation_target: govern/decision-review (recurring structural patterns)
  memory_pack_used: govern
  too_large_risk: med
  coverage_notes: information gain must be preserved across merge/split; stage moves route to lifecycle-review.

- workflow: govern/portfolio-review
  task_name: portfolio-balance-check
  unit_of_work: whole line roster
  loads: [line-registry, persona-clusters, information-portfolio]
  emits: [cluster-balance diagnosis, routed lifecycle candidates]
  deterministic_or_judgment: hybrid
  cadence: periodic
  trigger: threshold
  writes: balance diagnosis (logs/)
  patch_only_fields: []
  direct_write_fields: [balance diagnosis]
  downstream_consumers: [lifecycle-review, govern/decision-review (allocation targets)]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: med
  coverage_notes: cross-line reconciliation owned by exactly this workflow (not line-review).
```

## govern/decision-review

```yaml
- workflow: govern/decision-review
  task_name: docket-triage
  unit_of_work: the accumulated governance docket
  loads: [docket, workflow catalog]
  emits: [normalized/deduped/clustered items, recurrence counts, routed non-decision items, one decision-worthy cluster]
  deterministic_or_judgment: deterministic
  cadence: accumulated
  trigger: periodic
  writes: triaged docket (logs/)
  patch_only_fields: []
  direct_write_fields: [triaged docket, routing notes]
  downstream_consumers: [decision-worthiness-judgment, owning workflows (routed items)]
  escalation_target: owning workflow per item; held items stay on docket
  memory_pack_used: govern
  too_large_risk: med
  coverage_notes: DEC-022 intake atom of decision-review; MAY NOT propose a DEC-NNN.

- workflow: govern/decision-review
  task_name: decision-worthiness-judgment
  unit_of_work: one clustered candidate
  loads: [candidate cluster, Decision History, ROM, North Star, touched registries]
  emits: [outcome class + rationale]
  deterministic_or_judgment: judgment
  cadence: accumulated
  trigger: periodic
  writes: worthiness verdict (logs/)
  patch_only_fields: []
  direct_write_fields: [worthiness verdict]
  downstream_consumers: [decision-proposal-draft, hold]
  escalation_target: explicit hold (no destination forced)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: decides worthiness only; does not write DEC.

- workflow: govern/decision-review
  task_name: decision-proposal-draft
  unit_of_work: one decision-worthy candidate
  loads: [candidate, Decision History, ROM, North Star]
  emits: [drafted DEC-NNN proposal (inert), acceptance gate]
  deterministic_or_judgment: judgment
  cadence: accumulated
  trigger: periodic
  writes: drafted proposal (logs/, inert)
  patch_only_fields: [proposed DEC text, supersession target]
  direct_write_fields: [inert proposal artifact]
  downstream_consumers: [decision-acceptance]
  escalation_target: high-scrutiny flag if it contradicts North Star/ROM
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: proposal is inert; carries an explicit accept/reject/amend gate.

- workflow: govern/decision-review
  task_name: decision-acceptance
  unit_of_work: one accepted proposal
  loads: [accepted proposal, Decision History]
  emits: [appended DEC-NNN, supersession edit, Project Log entry]
  deterministic_or_judgment: deterministic
  cadence: rare
  trigger: manual
  writes: decision-history.md, PROJECT-LOG.md
  patch_only_fields: []
  direct_write_fields: [Decision History append + supersession edit, PROJECT-LOG entry]
  downstream_consumers: [all workflows (new active decision)]
  escalation_target: none (terminal, authority-gated)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: REQUIRES EXPLICIT AUTHORITY; only atom that writes canonical Decision History; never auto-runs; supersession never a delete.
```

## govern/line-intake

```yaml
- workflow: govern/line-intake
  task_name: candidate-line-intake
  unit_of_work: one seed/proposal
  loads: [candidate, line-registry]
  emits: [validated/normalized candidate or intake failure]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: normalized candidate object
  patch_only_fields: []
  direct_write_fields: [normalized candidate, intake-failure note]
  downstream_consumers: [line-dedupe-check]
  escalation_target: govern/decision-review (docket) on dangling route
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: never assigns maturity above seed.

- workflow: govern/line-intake
  task_name: line-dedupe-check
  unit_of_work: one candidate vs the whole registry
  loads: [candidate, line-registry (incl. archived lines), information-portfolio, foundation-queue]
  emits: [duplicate | archived-revival | partial-overlap | novel verdict]
  deterministic_or_judgment: hybrid
  cadence: on-event
  trigger: event
  writes: dedupe verdict (logs/)
  patch_only_fields: []
  direct_write_fields: [dedupe verdict]
  downstream_consumers: [line-add-proposal (novel), portfolio-review (overlap), lifecycle-review (archived-revival)]
  escalation_target: portfolio-review (overlap); lifecycle-review (revive)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: duplicates/overlaps never minted in parallel.

- workflow: govern/line-intake
  task_name: line-add-proposal
  unit_of_work: one novel candidate
  loads: [candidate, North Star, ROM, authority surfaces]
  emits: [drafted RL-NNN ADD proposal at seed/active]
  deterministic_or_judgment: judgment
  cadence: on-event
  trigger: event
  writes: drafted ADD proposal (logs/)
  patch_only_fields: [proposed RL-NNN entry]
  direct_write_fields: [inert ADD proposal]
  downstream_consumers: [line-add-acceptance]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: created at exactly seed/active; preserves provenance.

- workflow: govern/line-intake
  task_name: line-add-acceptance
  unit_of_work: one accepted proposal
  loads: [accepted proposal, line-registry]
  emits: [appended RL-NNN entry, Project Log entry]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: manual
  writes: line-registry.md, PROJECT-LOG.md
  patch_only_fields: []
  direct_write_fields: [line-registry entry, PROJECT-LOG entry]
  downstream_consumers: [exploit/explore workflows (new line)]
  escalation_target: none (authority-gated)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: REQUIRES EXPLICIT AUTHORITY; only atom that writes the line registry; never auto-runs.
```

## govern/persona-governance

```yaml
- workflow: govern/persona-governance
  task_name: persona-integrity-check
  unit_of_work: the three persona surfaces + skill mirror
  loads: [persona surfaces, mirror, parser]
  emits: [integrity report, clerical patch]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: integrity report (logs/)
  patch_only_fields: [clerical persona metadata]
  direct_write_fields: [integrity report]
  downstream_consumers: [single-persona-recluster (gate), patch accept step]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: short-circuits scored re-cluster on structural break.

- workflow: govern/persona-governance
  task_name: persona-mirror-sync
  unit_of_work: canonical panel vs skill mirror
  loads: [canonical panel, skill mirror]
  emits: [reconciliation patch (apply-after-canonical-acceptance)]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: reconciliation patch proposal
  patch_only_fields: [skill mirror entries]
  direct_write_fields: [reconciliation patch proposal]
  downstream_consumers: [post-acceptance sync step]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: mirror is synced post-acceptance, never authored here.

- workflow: govern/persona-governance
  task_name: single-persona-recluster
  unit_of_work: one persona
  loads: [the persona, neighboring clusters, ROM §5-§8]
  emits: [proposed primary cluster + rationale]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: event
  writes: recluster proposal (logs/)
  patch_only_fields: [persona-clusters assignment]
  direct_write_fields: [recluster proposal]
  downstream_consumers: [patch accept step]
  escalation_target: explore/persona-expansion (coverage gap); decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: governance clusters; expansion authors — must not both author personas.

- workflow: govern/persona-governance
  task_name: cluster-normalization-review
  unit_of_work: one weight-rule change
  loads: [persona-clusters, ROM §7-§8 voting rules]
  emits: [normalization-weight patch proposal]
  deterministic_or_judgment: judgment
  cadence: rare
  trigger: manual
  writes: normalization patch proposal (logs/)
  patch_only_fields: [cluster normalization weight rules]
  direct_write_fields: [normalization patch proposal]
  downstream_consumers: [patch accept step]
  escalation_target: govern/decision-review (fairness-class decision)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: HIGH-SCRUTINY — touches voting fairness; rare cadence.
```

## govern/research-memory

```yaml
- workflow: govern/research-memory
  task_name: cross-run-synthesis
  unit_of_work: one run window
  loads: [run logs in window, registries]
  emits: [one synthesis note]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: periodic
  writes: synthesis note (logs/synthesis)
  patch_only_fields: []
  direct_write_fields: [synthesis note]
  downstream_consumers: [logs/synthesis readers, decision-review (policy lessons)]
  escalation_target: govern/decision-review (policy-class lesson)
  memory_pack_used: govern
  too_large_risk: med
  coverage_notes: writes NO registry content; window can be split if too large.

- workflow: govern/research-memory
  task_name: contract-rollout
  unit_of_work: one file (or small batch)
  loads: [target file, DOCUMENT-CONTRACT schema]
  emits: [contract front-matter patch]
  deterministic_or_judgment: hybrid
  cadence: on-event
  trigger: event
  writes: contract patch proposal
  patch_only_fields: [document contract front-matter]
  direct_write_fields: [contract patch proposal]
  downstream_consumers: [patch accept step]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: classification is light judgment; applies the §12 contract.

- workflow: govern/research-memory
  task_name: log-hygiene-sweep
  unit_of_work: log/index/marker integrity
  loads: [logs, indices, summarizer markers]
  emits: [hygiene patch]
  deterministic_or_judgment: deterministic
  cadence: often
  trigger: event
  writes: hygiene patch proposal
  patch_only_fields: [broken links, indices, markers]
  direct_write_fields: [hygiene patch proposal]
  downstream_consumers: [patch accept step]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: integrity only; does not re-decide content.

- workflow: govern/research-memory
  task_name: project-log-catchup
  unit_of_work: one PROJECT-LOG entry
  loads: [recent runs, PROJECT-LOG]
  emits: [one appended PROJECT-LOG entry]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: periodic
  writes: PROJECT-LOG.md (narrative memory)
  patch_only_fields: []
  direct_write_fields: [PROJECT-LOG entry]
  downstream_consumers: [narrative memory readers]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: light judgment; narrative catch-up only.

- workflow: govern/research-memory
  task_name: memory-pack-summarizer
  unit_of_work: one family pack raw log
  loads: [one family memory-log.md (summarizer-only)]
  emits: [rolled load surface (MEMORY.md update)]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: threshold
  writes: family MEMORY.md Current Memory Summary + Principles
  patch_only_fields: []
  direct_write_fields: [MEMORY.md rollup, last-summarized marker]
  downstream_consumers: [all workflows of that family (load surface)]
  escalation_target: govern/decision-review (policy-class lesson routes out)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: ONLY atom that reads a pack's raw log; EXISTS ONLY once the memory layer is built (Phase 3.5); never writes new policy onto the pack.

- workflow: govern/research-memory
  task_name: compaction-resilience-check
  unit_of_work: registries + logs self-test
  loads: [registries, logs]
  emits: [gap list]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: periodic
  writes: gap-list report (logs/)
  patch_only_fields: []
  direct_write_fields: [gap-list report]
  downstream_consumers: [govern/decision-review (docket), project-log-catchup]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: tests the ROM §9 "new agent can resume from registries+logs" property.
```

## govern/information-portfolio

```yaml
- workflow: govern/information-portfolio
  task_name: line-information-gain-entry
  unit_of_work: one line
  loads: [line registry entry, relevant run logs, information-portfolio ledger]
  emits: [one ledger entry]
  deterministic_or_judgment: hybrid
  cadence: on-event
  trigger: event
  writes: information-portfolio.md (ledger)
  patch_only_fields: []
  direct_write_fields: [ledger entry (gain narrative + gain-type tag)]
  downstream_consumers: [ledger readers, portfolio-balance-read]
  escalation_target: govern/decision-review (target-ratio); portfolio-review (structural)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: status read deterministic; gain narrative judgment. Line-registry read-only here.

- workflow: govern/information-portfolio
  task_name: archival-gain-capture
  unit_of_work: one archived line
  loads: [retired line entry, run logs]
  emits: [one positive-framed gain entry]
  deterministic_or_judgment: judgment
  cadence: on-event
  trigger: event
  writes: information-portfolio.md (ledger)
  patch_only_fields: []
  direct_write_fields: [positive-framed ledger entry]
  downstream_consumers: [ledger readers]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: MUST fire on every lifecycle retirement (wired to lifecycle-patch-acceptance retire outcome); ROM §3 archived-as-wrong still records positive gain.

- workflow: govern/information-portfolio
  task_name: portfolio-balance-read
  unit_of_work: one balance read
  loads: [run-log posture tallies, ledger]
  emits: [posture tally + descriptive read]
  deterministic_or_judgment: hybrid
  cadence: periodic
  trigger: periodic
  writes: balance read (logs/)
  patch_only_fields: []
  direct_write_fields: [balance read artifact]
  downstream_consumers: [allocation visibility, govern/decision-review (target-ratio)]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: can window by posture if large; does not restructure (that is portfolio-review).

- workflow: govern/information-portfolio
  task_name: ledger-coverage-check
  unit_of_work: lines with changed understanding but no ledger entry
  loads: [line-registry, run logs, ledger]
  emits: [coverage gap list]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: periodic
  writes: coverage-gap list (logs/)
  patch_only_fields: []
  direct_write_fields: [coverage-gap list]
  downstream_consumers: [line-information-gain-entry]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: govern
  too_large_risk: low
  coverage_notes: dedup/coverage check only.
```

## explore/cross-disciplinary-synthesis

```yaml
- workflow: explore/cross-disciplinary-synthesis
  task_name: synthesis-corpus-assemble
  unit_of_work: recent cross-cluster outputs
  loads: [corpus index, prior synthesis logs]
  emits: [scoped corpus]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: event
  writes: corpus manifest (logs/)
  patch_only_fields: []
  direct_write_fields: [corpus manifest]
  downstream_consumers: [synthesis-structural-extract]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: collect + scope; new-vs-old check vs prior synthesis logs.

- workflow: explore/cross-disciplinary-synthesis
  task_name: synthesis-structural-extract
  unit_of_work: corpus pieces (batched)
  loads: [corpus pieces]
  emits: [vocabulary-stripped structural claims]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: event
  writes: structural-claim set (logs/)
  patch_only_fields: []
  direct_write_fields: [structural-claim set]
  downstream_consumers: [synthesis-convergence-match]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: med
  coverage_notes: load pieces in batches to bound context.

- workflow: explore/cross-disciplinary-synthesis
  task_name: synthesis-convergence-match
  unit_of_work: extracted structural claims + cluster map
  loads: [structural claims, persona-clusters distance map]
  emits: [convergence map, independence check, tensions]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: event
  writes: convergence map (logs/)
  patch_only_fields: []
  direct_write_fields: [convergence map incl. preserved tensions]
  downstream_consumers: [synthesis-route]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: med
  coverage_notes: ANALYTIC CORE; cheap once claims extracted; independence check mandatory (ROM §8). Same-vocab agreement != convergence.

- workflow: explore/cross-disciplinary-synthesis
  task_name: synthesis-route
  unit_of_work: convergences
  loads: [convergence map]
  emits: [candidate-line proposals, reassessment flags, claim-pressuring signals]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: event
  writes: routing bundle (logs/)
  patch_only_fields: []
  direct_write_fields: [routing bundle]
  downstream_consumers: [explore/line-discovery, explore/landscape-reassessment, claim surface]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: kept distinct from reassessment (no double-survey of landscape).
```

## explore/foundation-ingestion

```yaml
- workflow: explore/foundation-ingestion
  task_name: foundation-item-select
  unit_of_work: next 'proposed' queue item
  loads: [foundation-queue, existing note index]
  emits: [selected item marked 'ingested', dedup result]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: event
  writes: foundation-queue.md (status: ingested)
  patch_only_fields: []
  direct_write_fields: [queue cursor + status transition]
  downstream_consumers: [foundation-note-write]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: queue cursor + duplicate check; high-priority add can event-trigger.

- workflow: explore/foundation-ingestion
  task_name: foundation-note-write
  unit_of_work: one queue item
  loads: [the source, touchpoint surfaces]
  emits: [one literature/ note + adjacency map]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: event
  writes: literature/ note + adjacency map
  patch_only_fields: []
  direct_write_fields: [literature note, adjacency map]
  downstream_consumers: [foundation-flag-route]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: high
  coverage_notes: EXPENSIVE (reads the source); a very large paper may need its own bounding.

- workflow: explore/foundation-ingestion
  task_name: foundation-flag-route
  unit_of_work: one finished note
  loads: [the finished note]
  emits: [candidate flags routed, queue patched to 'noted']
  deterministic_or_judgment: hybrid
  cadence: periodic
  trigger: event
  writes: foundation-queue.md (status: noted)
  patch_only_fields: []
  direct_write_fields: [status transition, flag routing]
  downstream_consumers: [explore/line-discovery, explore/cross-disciplinary-synthesis, explore/persona-expansion]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: every queued item reaches a terminal status with a note pointer.
```

## explore/landscape-reassessment

```yaml
- workflow: explore/landscape-reassessment
  task_name: reassessment-landscape-load
  unit_of_work: whole line graph + standing + portfolio + prior snapshot
  loads: [line-registry graph, standing snapshots, information-portfolio, prior reassessment snapshot]
  emits: [assembled landscape]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: periodic
  writes: landscape assembly (logs/)
  patch_only_fields: []
  direct_write_fields: [landscape assembly]
  downstream_consumers: [reassessment-topology-survey]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: med
  coverage_notes: the ONE workflow that legitimately needs a whole-landscape view; per-line deep artifacts loaded on demand only.

- workflow: explore/landscape-reassessment
  task_name: reassessment-topology-survey
  unit_of_work: the loaded landscape
  loads: [assembled landscape]
  emits: [re-imagined topology + ridge call]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: periodic
  writes: topology survey (logs/)
  patch_only_fields: []
  direct_write_fields: [topology survey + explicit ridge call]
  downstream_consumers: [reassessment-shift-test]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: high
  coverage_notes: SEARCH MODE; EXPENSIVE over a large graph; must make an explicit primary-ridge call.

- workflow: explore/landscape-reassessment
  task_name: reassessment-shift-test
  unit_of_work: each proposed shift
  loads: [proposed shifts, evidence]
  emits: [supported/unsupported shift verdicts]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: periodic
  writes: shift-test results (logs/)
  patch_only_fields: []
  direct_write_fields: [shift-test results]
  downstream_consumers: [reassessment-route]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: med
  coverage_notes: EVALUATION MODE; flags shifts lacking an evidence basis; diff vs prior snapshot incl. "no change".

- workflow: explore/landscape-reassessment
  task_name: reassessment-route
  unit_of_work: supported shifts
  loads: [supported-shift list]
  emits: [lifecycle candidates, reprioritization, discovery prompts, portfolio flags]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: periodic
  writes: routing bundle (logs/)
  patch_only_fields: []
  direct_write_fields: [routing bundle]
  downstream_consumers: [lifecycle-review, portfolio-review, line-discovery, decision-review (allocation)]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: kept distinct from synthesis (no content-pattern double-work).
```

## explore/line-discovery

```yaml
- workflow: explore/line-discovery
  task_name: discovery-generation
  unit_of_work: one generation pass
  loads: [theory surfaces, persona-idea-sprint machinery]
  emits: [raw candidates]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: periodic
  writes: raw candidate list (logs/)
  patch_only_fields: []
  direct_write_fields: [raw candidate list]
  downstream_consumers: [discovery-dedup]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: med
  coverage_notes: SEARCH MODE; possibly expensive; full panel invoked via skill, not inlined; event-trigger on reassessment under-covered-region flag.

- workflow: explore/line-discovery
  task_name: discovery-dedup
  unit_of_work: raw candidates vs registry
  loads: [raw candidates, line-registry incl. archived lines]
  emits: [novel/overlap/restate classification]
  deterministic_or_judgment: deterministic
  cadence: periodic
  trigger: periodic
  writes: dedup classification (logs/)
  patch_only_fields: []
  direct_write_fields: [dedup classification]
  downstream_consumers: [discovery-seed-emit]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: cheap; cleanly separable from generation for cadence.

- workflow: explore/line-discovery
  task_name: discovery-seed-emit
  unit_of_work: surviving candidates
  loads: [survivors]
  emits: [candidate_seed bundle, run log]
  deterministic_or_judgment: hybrid
  cadence: periodic
  trigger: periodic
  writes: candidate_seed bundle (logs/)
  patch_only_fields: []
  direct_write_fields: [candidate_seed bundle, run log]
  downstream_consumers: [govern/line-intake]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: discovery proposes; intake decides — must not both register.
```

## explore/line-incubation

```yaml
- workflow: explore/line-incubation
  task_name: incubation-probe-design
  unit_of_work: one early-lifecycle line
  loads: [line entry, artifacts, standing snapshot, relevant literature]
  emits: [bounded probe plan with pass/fail criteria]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: event
  writes: probe plan (logs/)
  patch_only_fields: []
  direct_write_fields: [probe plan]
  downstream_consumers: [incubation-probe-run]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: SEARCH MODE; round-robin across early lines, or event on line-review lifecycle-candidate.

- workflow: explore/line-incubation
  task_name: incubation-probe-run
  unit_of_work: one probe plan
  loads: [probe plan, line artifacts]
  emits: [result + artifact]
  deterministic_or_judgment: hybrid
  cadence: periodic
  trigger: event
  writes: probe result + artifact (logs/ + line artifacts)
  patch_only_fields: []
  direct_write_fields: [probe result, probe artifact]
  downstream_consumers: [incubation-promotion-judgment]
  escalation_target: budget escalation if over-budget (ROM §2)
  memory_pack_used: explore
  too_large_risk: high
  coverage_notes: EXPENSIVE SEAM; budget-enforced; over-budget probe escalates rather than overspends.

- workflow: explore/line-incubation
  task_name: incubation-promotion-judgment
  unit_of_work: one probe result
  loads: [probe result, standing snapshot]
  emits: [promote candidate OR stay/weaken signal, information-gain entry]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: event
  writes: promotion verdict (logs/)
  patch_only_fields: []
  direct_write_fields: [promotion verdict]
  downstream_consumers: [govern/lifecycle-review (promote/weaken), govern/information-portfolio (gain)]
  escalation_target: govern/lifecycle-review
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: records info-gain pass OR fail; stage move owned only by lifecycle-review.
```

## explore/persona-expansion

```yaml
- workflow: explore/persona-expansion
  task_name: persona-gap-collect
  unit_of_work: accumulated gap signals
  loads: [persona system (62 experts + lens families), gap signals]
  emits: [deduped genuine gaps]
  deterministic_or_judgment: deterministic
  cadence: accumulated
  trigger: threshold
  writes: gap list (logs/)
  patch_only_fields: []
  direct_write_fields: [gap list]
  downstream_consumers: [persona-draft]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: match against existing coverage; threshold = recurring blind spot crosses bar (UNDECIDED).

- workflow: explore/persona-expansion
  task_name: persona-draft
  unit_of_work: one genuine gap
  loads: [relevant cluster, house-style exemplars]
  emits: [drafted lens/expert + suggested cluster + lens-vs-expert recommendation]
  deterministic_or_judgment: judgment
  cadence: on-event
  trigger: event
  writes: drafted persona proposal (logs/)
  patch_only_fields: []
  direct_write_fields: [drafted persona proposal]
  downstream_consumers: [persona-proposal-emit]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: each proposed lens must name a misuse risk + a failure mode it catches.

- workflow: explore/persona-expansion
  task_name: persona-proposal-emit
  unit_of_work: drafted proposals
  loads: [drafted proposals]
  emits: [proposals routed + run log]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: routing bundle (logs/)
  patch_only_fields: []
  direct_write_fields: [routing bundle, run log]
  downstream_consumers: [govern/persona-governance]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: explore
  too_large_risk: low
  coverage_notes: expansion AUTHORS; governance CLUSTERS + owns canonical text/numbering/mirror; slow churn respected.
```

## exploit/advance-primary

```yaml
- workflow: exploit/advance-primary
  task_name: primary-move-select
  unit_of_work: the single primary line
  loads: [line-registry (primary), next candidate move]
  emits: [move spec OR no_move_available / ambiguous-primary signal]
  deterministic_or_judgment: hybrid
  cadence: often
  trigger: event
  writes: move spec (logs/)
  patch_only_fields: []
  direct_write_fields: [move spec]
  downstream_consumers: [primary-move-execute]
  escalation_target: govern/line-review (ambiguous-primary); decision-review (docket)
  memory_pack_used: exploit
  too_large_risk: low
  coverage_notes: single-primary check + move-bounded check.

- workflow: exploit/advance-primary
  task_name: primary-move-execute
  unit_of_work: one primary line + one bounded move
  loads: [primary line entry, artifacts, standing snapshot, health profile, authority-surface rows, recent runs]
  emits: [one artifact, optional status patch proposal]
  deterministic_or_judgment: judgment
  cadence: often
  trigger: event
  writes: move artifact (line artifacts/repo)
  patch_only_fields: [line status fields]
  direct_write_fields: [move artifact, run log]
  downstream_consumers: [repo/integrate-results, status-patch-propose, information-portfolio, line-review]
  escalation_target: govern/line-review / lifecycle-review (posture signals)
  memory_pack_used: exploit
  too_large_risk: high
  coverage_notes: PROGRAM'S MAIN FORWARD CADENCE; more than one move is too large; does NOT do challenge or integrate work; never loads full panel.

- workflow: exploit/advance-primary
  task_name: status-patch-propose
  unit_of_work: one executed move
  loads: [move report]
  emits: [accept-gated status patch]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: status patch proposal (logs/)
  patch_only_fields: [line status fields]
  direct_write_fields: [status patch proposal]
  downstream_consumers: [patch accept step]
  escalation_target: govern/line-review (re-score on material change)
  memory_pack_used: exploit
  too_large_risk: low
  coverage_notes: shared shape with advance-secondary; only when a move earns a change.
```

## exploit/advance-secondary

```yaml
- workflow: exploit/advance-secondary
  task_name: secondary-budget-check
  unit_of_work: secondary existence + primary pending move
  loads: [line-registry (secondary), thin read of primary's pending move]
  emits: [budget verdict (advance | defer) OR deferred_budget_tension]
  deterministic_or_judgment: hybrid
  cadence: on-event
  trigger: event
  writes: budget verdict (logs/)
  patch_only_fields: []
  direct_write_fields: [budget verdict]
  downstream_consumers: [secondary-move-execute]
  escalation_target: govern/decision-review (allocation/budget flag)
  memory_pack_used: exploit
  too_large_risk: low
  coverage_notes: BUDGET HONESTY (ROM §2); runs before every secondary move.

- workflow: exploit/advance-secondary
  task_name: secondary-move-execute
  unit_of_work: one secondary line + one bounded move
  loads: [secondary line, thin primary-pending read, both health profiles, recent runs]
  emits: [one artifact, optional conservative status patch]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: event
  writes: move artifact (line artifacts/repo)
  patch_only_fields: [secondary line status fields]
  direct_write_fields: [move artifact, run log]
  downstream_consumers: [repo/integrate-results, status-patch-propose, information-portfolio]
  escalation_target: challenge-primary (challenge-worthiness); line-review (re-score)
  memory_pack_used: exploit
  too_large_risk: high
  coverage_notes: lower frequency than primary; must not do primary's move nor reassign primacy.

- workflow: exploit/advance-secondary
  task_name: status-patch-propose
  unit_of_work: one executed secondary move
  loads: [secondary move report]
  emits: [conservative accept-gated status patch]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: status patch proposal (logs/)
  patch_only_fields: [secondary line status fields]
  direct_write_fields: [status patch proposal]
  downstream_consumers: [patch accept step]
  escalation_target: govern/line-review (re-score)
  memory_pack_used: exploit
  too_large_risk: low
  coverage_notes: conservative variant of advance-primary's status-patch-propose (shared atom).
```

## exploit/challenge-primary

```yaml
- workflow: exploit/challenge-primary
  task_name: challenge-select
  unit_of_work: the single primary line
  loads: [primary line, prior challenge runs]
  emits: [challenge spec OR ambiguous-primary]
  deterministic_or_judgment: hybrid
  cadence: periodic
  trigger: event
  writes: challenge spec (logs/)
  patch_only_fields: []
  direct_write_fields: [challenge spec]
  downstream_consumers: [challenge-execute]
  escalation_target: govern/line-review (ambiguous-primary)
  memory_pack_used: exploit
  too_large_risk: low
  coverage_notes: picks a not-yet-survived challenge type/target.

- workflow: exploit/challenge-primary
  task_name: challenge-execute
  unit_of_work: one primary line + one bounded challenge
  loads: [primary line, artifacts, standing snapshot, overclaim profile, claim wording, prior challenge runs, hostile/skeptic cluster posture]
  emits: [one challenge artifact, adjudication]
  deterministic_or_judgment: judgment
  cadence: periodic
  trigger: event
  writes: challenge artifact (logs/)
  patch_only_fields: [overclaim/weakening fields]
  direct_write_fields: [challenge artifact, adjudication]
  downstream_consumers: [challenge-route]
  escalation_target: deep-panel-review (only if skeptic cluster insufficient)
  memory_pack_used: exploit
  too_large_risk: high
  coverage_notes: RED-TEAMS PRIMARY (ROM §1); full panel NOT loaded unless deep-panel triggered; more than one challenge is too large.

- workflow: exploit/challenge-primary
  task_name: challenge-route
  unit_of_work: one adjudicated challenge
  loads: [adjudication]
  emits: [lifecycle (demote) candidate, re-score signal, optional weakening patch]
  deterministic_or_judgment: deterministic
  cadence: on-event
  trigger: event
  writes: routing bundle (logs/)
  patch_only_fields: [claim weakening fields]
  direct_write_fields: [routing bundle]
  downstream_consumers: [govern/lifecycle-review (demote), govern/line-review (re-score), patch accept step, information-portfolio (gain)]
  escalation_target: govern/lifecycle-review
  memory_pack_used: exploit
  too_large_risk: low
  coverage_notes: successful challenge ROUTES a candidate (never executes a move); survival-argument rule (ROM §5) applied before any demote candidate.
```

## exploit/integrate-results

```yaml
- workflow: exploit/integrate-results
  task_name: integration-readiness-check
  unit_of_work: one matured line
  loads: [line, readiness gate]
  emits: [ready / not-ready with failing items]
  deterministic_or_judgment: deterministic
  cadence: rare
  trigger: event
  writes: readiness verdict (logs/)
  patch_only_fields: []
  direct_write_fields: [readiness verdict]
  downstream_consumers: [integration-assemble]
  escalation_target: govern/decision-review (docket)
  memory_pack_used: exploit
  too_large_risk: low
  coverage_notes: gate runs before assembly; triggered on a maturity signal (line matured + survived challenge).

- workflow: exploit/integrate-results
  task_name: integration-assemble
  unit_of_work: one matured line -> one integration proposal bundle
  loads: [line artifacts, standing snapshot, readiness profile, durable surfaces touched, prior runs]
  emits: [patch bundle + consistency check]
  deterministic_or_judgment: judgment
  cadence: rare
  trigger: event
  writes: integration proposal bundle (logs/)
  patch_only_fields: [durable surfaces (CLAIM-LEDGER, ROADMAP, HYPOTHESES, glossary)]
  direct_write_fields: [integration proposal bundle]
  downstream_consumers: [patch accept step (authority), lifecycle-review (integrate candidate)]
  escalation_target: owning surface / portfolio-review (conflicts)
  memory_pack_used: exploit
  too_large_risk: med
  coverage_notes: bundle assembled + consistency-checked as ONE atomic accept/reject unit; least-frequent exploit workflow; does NOT load whole portfolio.

- workflow: exploit/integrate-results
  task_name: integration-route
  unit_of_work: the assembled bundle
  loads: [assembled bundle]
  emits: [integrate lifecycle candidate, re-score signal, conflict flags]
  deterministic_or_judgment: deterministic
  cadence: rare
  trigger: event
  writes: routing bundle (logs/)
  patch_only_fields: []
  direct_write_fields: [routing bundle]
  downstream_consumers: [govern/lifecycle-review (integrate stage move), govern/line-review (re-score), portfolio-review (conflicts), information-portfolio (gain)]
  escalation_target: govern/lifecycle-review
  memory_pack_used: exploit
  too_large_risk: low
  coverage_notes: integrate stage move stays owned by lifecycle-review; acceptance lives outside the exploit family.
```

---

# Coverage questions (whole-set answers)

These answer the §13 / DEC-013 coverage questions across all 65 atoms.

**1. Does every workflow output have a downstream consumer?**
Yes. Every atom's `emits` resolves to a named `downstream_consumers`: artifacts ->
repo / integrate-results / audit; standing snapshots -> audit + patch accept step;
patches -> accept step; lifecycle candidates -> lifecycle-review; structural ->
portfolio-review; governance signals -> decision-review (docket); ledger entries ->
information-portfolio; family rollups -> the family load surface. No atom emits
into a void.

**2. Does every registry write have an owning task?**
Yes, and every canonical-registry write is owned by exactly one accept-gated,
manual-only atom: line-registry -> `line-add-acceptance` (intake) and
`lifecycle-patch-acceptance` (stage/status); Decision History ->
`decision-acceptance` only; PROJECT-LOG -> `project-log-catchup` /
the acceptance atoms; foundation-queue status -> `foundation-item-select` /
`foundation-flag-route`; information-portfolio ledger ->
`line-information-gain-entry` / `archival-gain-capture`. All other atoms are
patch-first (propose only). research-memory writes NO registry content.

**3. Does every escalation signal have a destination?**
Yes. Lifecycle -> lifecycle-review; structural -> portfolio-review; governance /
schema-inadequacy / dangling-route -> decision-review (docket, DEC-022);
persona coverage gap -> persona-expansion; budget tension -> decision-review
allocation; needs-persona-review -> deep-panel-review (event sub-atom);
registry/authority conflict -> logged as `confusion_or_conflict`, deferred to the
authority surface (ROM §11). Held docket items remain on the docket (explicit
non-loss).

**4. Does every scheduled task have a bounded object?**
Yes. Each atom names one object: one line, one move, one challenge, one candidate,
one queue item, one note, one file, one pack, one window, one balance read, or one
portfolio question. The three whole-graph atoms (dependency-graph-audit,
portfolio-balance-check, reassessment-landscape-load) are bounded to the registry
graph (irreducible by design) and the survey atoms can window; none is unbounded.

**5. Is anything reviewed twice by competing tasks?**
No competing double-review found. Boundaries are explicit: line-review re-scores
standing; portfolio-review owns ALL cross-line reconciliation (sole owner);
lifecycle-review owns ALL stage/status moves; decision-review owns canonization;
advance-primary advances, challenge-primary attacks, integrate-results folds
(disjoint); information-portfolio records gain while portfolio-review restructures
and lifecycle-review moves posture (distinct jobs); persona-expansion AUTHORS while
persona-governance CLUSTERS. Synthesis and reassessment are deliberately kept
distinct (no landscape double-survey). These are asserted boundaries to enforce at
arming time, not yet mechanically guaranteed.

**6. Is any unit too large for one agent run?**
Six atoms carry `too_large_risk: high` and are flagged for bounding before arming:
`foundation-note-write` (large source), `reassessment-topology-survey` (large
graph), `incubation-probe-run` (open-ended probe), `primary-move-execute` /
`secondary-move-execute` (a single move can still be large), and
`challenge-execute`. Mitigations are specced (batch/window the source; bound the
probe by budget; one move / one challenge maximum) but the concrete size bounds and
budget caps are Open Questions (see SCHEDULE-SPEC ROM §2 notes). No atom is known
to be intrinsically un-runnable; each has a stated bounding strategy.

---

## Docketed gaps / Open Questions (carried, not invented)

- **Patch-acceptance owner is undecided** (line-review OQ#2). Every patch-first
  atom routes to an unnamed "patch accept step". Naming that owner is an arming
  prerequisite for all patch-emitting atoms.
- **Concrete cadences and numeric thresholds are undecided** (registry-size
  trigger for graph audits; round-robin period; summarizer cadence; persona-gap
  recurrence bar; budget caps). Recorded as threshold/periodic specs, not policy.
- **Memory layer not yet built** — `memory-pack-summarizer` and every
  `memory_pack_used` read are inert until Phase 3.5 build completes.
- **deep-panel-review** is treated as an event sub-atom (not its own workflow);
  whether it becomes a standalone workflow remains open (line-review deferred item).
- **0-3 standing calibration anchors** still pending (line-review OQ#3) — affects
  `single-line-standing-review` reliability across agents.
