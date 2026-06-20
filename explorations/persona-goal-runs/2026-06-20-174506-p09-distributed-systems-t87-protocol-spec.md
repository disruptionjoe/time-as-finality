# P09 Bounded Run - T87 Protocol Specification Rewrite

- Run timestamp: 2026-06-20T17:45:06-05:00
- Persona: P09 - Distributed Systems Researcher
- Goal id: P09
- Queue goal: Rewrite T87 as a protocol specification with threat model, fault model, synchrony assumptions, replay/spoof adversaries, signed logs, and demotion rules.
- Bounded scope: repo-only audit of the current detector-provenance route centered on `T87`, using the existing executable contract, adjacent detector tests, and prior exploration notes. No claim-status, roadmap, workflow, or automation edits.

## Repo Context Read

- `tests/T78-preregistered-detector-deployment-protocol.md`
- `tests/T87-real-run-raw-log-contract.md`
- `tests/T95-detector-stack-export-map.md`
- `tests/T96-detector-feasibility-checklist.md`
- `tests/T97-detector-dry-run-packet-skeleton.md`
- `tests/test_real_run_raw_log_contract.py`
- `models/run_t87.py`
- `TECHNICAL-REPORT-real-run-raw-log-contract-v0.1.md`
- `TECHNICAL-REPORT-detector-feasibility-checklist-v0.1.md`
- `explorations/all-persona-last-24h-review-2026-06-20.md`
- `explorations/research-constellation-orchestrator-2026-06-20.md`

## Work Performed

1. Read the current T87 prose contract and its executable tests to separate what is already enforced from what is still implicit.
2. Read T78, T95, T96, and T97 to identify the surrounding pre-registration, export-map, feasibility, and dry-run assumptions that a protocol rewrite must preserve.
3. Collapsed the detector route into distributed-systems terms: principals, logs, synchrony assumptions, fault classes, adversaries, safety gate, and availability gate.
4. Produced a bounded protocol rewrite below that keeps T87's current no-overclaim posture while making its security and systems assumptions explicit.

## Result

### Protocol reading of current T87

Current T87 is already close to a safety-only admission protocol:

- it defines the required log packet;
- it rejects mutable, summary-only, post hoc, and unjoinable evidence;
- it names the next allowed transition as population of locked `T76/T86` counts.

What it lacks is protocol-paper framing. The missing pieces are not new tables.
They are explicit assumptions about who can write which records, what timing
guarantees are assumed, what faults are tolerated, and which adversaries force
automatic demotion.

### Proposed bounded rewrite: T87 as a protocol spec

#### Protocol objective

Admit a detector deployment for `T76/T86` population only when an observer can
verify, from immutable signed raw logs, that the copied/independent controls,
ambiguity challenges, perturbation trials, ancestry edges, trust audits, and
demotion policy were fixed before data collection and were not subsequently
replayed, spoofed, truncated, or rewritten.

#### Principals

- instrument operator: emits time-tag events;
- provenance middleware: verifies signatures and exports ancestry edges;
- control operator: instantiates copied/independent and ambiguity challenges;
- trust auditor: records authority, custody, and boundary crossings;
- policy authority: freezes thresholds and demotion rules pre-data;
- verifier: runs the T87 admission audit before any `T76/T86` scoring.

#### Required signed / immutable logs

- `preregistration_manifest`
- `control_pair_manifest`
- `event_time_tag_stream`
- `signature_verification_log`
- `tag_ambiguity_challenge_log`
- `perturbation_trial_log`
- `ancestry_dag_edge_export`
- `trust_boundary_audit_log`
- `demotion_decision_log`

Interpretation: these are not generic metadata. Together they form the event
history the verifier must replay.

#### Synchrony assumptions

- Event rows carry stable event identifiers that remain joinable across all
  required tables.
- Clock discipline is bounded well enough that copied/independent and
  perturbation challenge windows can be matched without post hoc retiming.
- Signed archive publication is delayed by at most a declared bound; later
  publication is logged as a protocol event rather than silently tolerated.
- Policy and manifest hashes are frozen before the first admitted event.

This is partial synchrony, not perfect synchrony. T87 should not require exact
simultaneity; it requires bounded, auditable timing alignment.

#### Fault model

- crash / omission faults: missing rows, missing exports, archive gaps;
- timing faults: clock drift, retimestamping, unstable join keys;
- integrity faults: mutable tables, unsigned rows, signature failures;
- governance faults: incomplete threshold preregistration, post hoc demotion
  selection, merged operator/auditor authority;
- provenance faults: missing raw DAG edges, hidden challenge events, incomplete
  copied/independent labels.

#### Adversary classes

- replay adversary: republishes prior signed rows as fresh detector evidence;
- spoof adversary: forges or relabels independent tags, signatures, or control
  identities;
- truncation adversary: omits ancestry edges, challenge rows, or demotion
  events while preserving a dashboard-level summary;
- delay adversary: withholds publication until outcome-dependent policy choice
  is possible;
- authority adversary: exploits key custody, delegated write access, or missing
  revocation boundaries to rewrite provenance;
- policy adversary: chooses thresholds or demotion behavior after seeing data.

#### Safety property

No detector run is admitted for `Q1` upgrade or even `T76/T86` population if
any required table is missing, mutable, unjoinable, unsigned where required,
missing copied/independent control declarations, or governed by post hoc
policy.

This matches the existing executable T87 verdict boundary:
`inadmissible_for_q1_upgrade`.

#### Availability property

If all principals act within the declared synchrony bounds and publish the full
immutable packet before analysis, then the verifier can populate the locked
`T76/T86` evidence schema without adding fields or relaxing controls.

This is intentionally narrow. Availability means "the next audit can run," not
"Q1 receives support."

#### Demotion rules

Automatic withhold or demotion should occur when any of the following holds:

- copied/independent labels were not preregistered;
- policy corridor or demotion rules were chosen after data;
- raw tables are not joinable by stable event id;
- required signed DAG edge columns are absent;
- required tables are mutable exports;
- challenge or trust-boundary events are summarized but not exported as raw
  rows;
- authority separation collapses so the same actor both defines and certifies
  the decisive evidence path without an independent audit trail.

### Why this rewrite matters

The detector route currently reads like a schema contract plus a feasibility
checklist. In distributed-systems language it becomes clearer that:

1. T87 is a safety gate over evidence history, not a detector-dynamics claim.
2. The load-bearing object is an auditable event packet with authority and
   ancestry structure, not the dashboard or even the native timing stream.
3. The missing next artifact is an adversary-indexed dry run, not more prose
   about provenance.

## Blocker

No real detector deployment packet exists, and the current repo surfaces do not
yet encode explicit key-compromise, revocation, publication-delay, or
authority-separation scenarios as first-class T87/T97 packet rows. The
protocol rewrite therefore sharpens the admission gate but does not by itself
establish a feasible real deployment.

## Proposed Next Action

Take one of these bounded follow-ups:

1. Extend the `T97` dry-run packet with protocol fields for key custody,
   revocation, archive publication delay, and authority-role separation.
2. Build one adversary table mapping each T87 executable rejection case to a
   concrete replay, spoof, truncation, delay, or authority-compromise story.
3. Choose one lab stack and try to populate the full packet pre-data; if the
   governance and authority logs cannot be frozen honestly, demote the route.

## Claim-Status Posture

- `Q1B` remains an externally blocked detector-record admissibility branch.
- `T87` should be read as a protocol safety specification for evidence intake,
  not as empirical detector support and not as new measurement dynamics.
- The detector path still survives only as a narrow raw-log governance route
  until a real packet passes the admission gate.
