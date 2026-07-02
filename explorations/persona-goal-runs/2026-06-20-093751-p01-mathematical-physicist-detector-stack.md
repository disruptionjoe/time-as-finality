# P01 Run - Mathematical Physicist

- timestamp: 2026-06-20T09:37:51-05:00
- goal_id: P01
- selected_persona: Mathematical Physicist
- selected_goal: Instantiate one TaF record/provenance model on a concrete weak-measurement or detector platform using platform-native variables: Hamiltonian or channel, instrument model, detector outputs, thermodynamic costs, and observable records.
- selected_platform: `hydraharp_wr_signed_archive` photon time-tagging detector stack

## Repo Context Read

- [`/Github Repos/time-as-finality/claims/Q1-quantum-under-finalization.md`](/Github%20Repos/time-as-finality/claims/Q1-quantum-under-finalization.md)
- [`/Github Repos/time-as-finality/claims/D1-physical-finality-definition.md`](/Github%20Repos/time-as-finality/claims/D1-physical-finality-definition.md)
- [`/Github Repos/time-as-finality/tests/T75-real-detector-stack-provenance.md`](/Github%20Repos/time-as-finality/tests/T75-real-detector-stack-provenance.md)
- [`/Github Repos/time-as-finality/tests/T78-preregistered-detector-deployment-protocol.md`](/Github%20Repos/time-as-finality/tests/T78-preregistered-detector-deployment-protocol.md)
- [`/Github Repos/time-as-finality/tests/T87-real-run-raw-log-contract.md`](/Github%20Repos/time-as-finality/tests/T87-real-run-raw-log-contract.md)
- [`/Github Repos/time-as-finality/tests/T91-weak-measurement-platform-audit.md`](/Github%20Repos/time-as-finality/tests/T91-weak-measurement-platform-audit.md)
- [`/Github Repos/time-as-finality/models/real_detector_stack_provenance.py`](/Github%20Repos/time-as-finality/models/real_detector_stack_provenance.py)
- [`/Github Repos/time-as-finality/models/preregistered_detector_deployment_protocol.py`](/Github%20Repos/time-as-finality/models/preregistered_detector_deployment_protocol.py)
- [`/Github Repos/time-as-finality/models/real_run_raw_log_contract.py`](/Github%20Repos/time-as-finality/models/real_run_raw_log_contract.py)

## Work Performed

1. Read the current Q1, D1, T75, T78, T87, and T91 materials to identify the strongest existing physical platform route.
2. Ran the existing bounded model artifacts for T75, T78, T87, and T91 to anchor this run in repo outputs rather than narrative summary.
3. Chose the detector route over the weak-measurement route because T91 shows every named superconducting weak-measurement family still fails the independent-axis gate.

## Platform-Native Instantiation

### 1. Physical channel and instrument stack

Use a channel-level model rather than a Hamiltonian-level model. The current repo has a concrete instrument stack for:

```text
photon detector
  -> PicoQuant HydraHarp 500 time tagger
  -> White Rabbit synchronized timing fabric
  -> hash-chained RFC 3161-style signed archive
```

The physically named channel coordinates already encoded in T75 are:

- local timing uncertainty `local_sigma in [0.003, 0.020]`
- archive timing uncertainty `archive_sigma in [0.010, 0.080]`
- archive batching window `batching_window in [0.020, 0.180]`
- tag retention `tag_retention in [0.975, 0.999]`
- signature verification `verification in [0.985, 0.9995]`
- spoof/forgery rates `spoof_independent in [0.000, 0.006]`, `forgery in [0.000, 0.004]`
- trust-boundary parameters for detector, archive, and transport
- perturbation-response, back-action, and signed-DAG observability parameters

This is already physics-facing enough to attack: each coordinate is an instrument, synchronization, signing, or control-layer assumption, not a free TaF label.

### 2. Instrument model

The minimal honest instrument model is:

- detector event formation: photon hit produces an event id and local time tag
- timing transport: White Rabbit distributes the clock used to compare local and archive times
- provenance authentication: each batch is signed or timestamp-tokenized
- ancestry observation: record copies and archival relations are exported as signed DAG edges
- intervention channel: perturbation trials distinguish copied dependence from genuinely independent channels

### 3. Observable records

The T87 contract makes the observable records explicit. A real run must expose event-level tables for:

- `event_time_tag_stream`
- `signature_verification_log`
- `tag_ambiguity_challenge_log`
- `perturbation_trial_log`
- `ancestry_dag_edge_export`
- `trust_boundary_audit_log`
- plus preregistration and demotion manifests

These are the actual record surfaces on which TaF would operate. They are not inferred from dashboard summaries.

### 4. TaF/D1 mapping on this platform

For this stack, the strongest defensible D1 reading is:

- accessible support: signed event records available to the observer inside the declared raw-log boundary
- holder redundancy: distinct record holders after collapsing copied archives and shared ancestry
- branch support: independently witnessed provenance channels, currently carried by authenticated tags, clean perturbation response, and signed ancestry DAG edges
- reversal cost: a named protocol-level undo burden, not yet a measured thermodynamic work variable

T75's bounded output is strong on the first three coordinates:

- signed stack verdict: `robust_recovery`
- robust rate: `1.0`
- unsigned control robust rate: `0.005`

So the platform does instantiate a concrete TaF record/provenance model. But it instantiates it as detector-record admissibility and provenance separation, not as a new measurement dynamics.

### 5. Thermodynamic-cost status

This is the main physics-side shortfall.

The stack does expose physical timing and reset-adjacent quantities such as detector dead time (`680 ps`) and batching latency, but the repo still does **not** supply:

- a calorimetric or work-metered reversal-cost observable;
- a Landauer-style erasure accounting tied to these event records;
- a physically measured cost coordinate that changes the TaF verdict independently of the provenance/readout channels.

So the thermodynamic-cost slot is only partially instantiated. It is named, but not yet experimentally reduced.

## Result

Bounded-run verdict: the detector route clears the platform-instantiation bar better than the weak-measurement route.

- Positive result: T75 provides a concrete detector platform with source-anchored timing hardware, synchronized transport, authenticated archive structure, and event-level record outputs that can be mapped into D1-style provenance scoring.
- Negative result: T91 shows the named weak-measurement families remain blocked because their proposed TaF axes collapse to the same monitored record or to postselected success.
- Boundary result: this detector instantiation is still a provenance/accounting model over already formed detector records. It is not yet a Hamiltonian measurement theory and not yet a thermodynamic finality theory.

## Blocker

Two load-bearing blockers remain:

1. No real deployment raw log is present. T78 and T87 define the admissible pre-registration and event-table contract, but the repo still lacks a measured run that populates those tables.
2. The reversal-cost / thermodynamic-cost coordinate is not physically measured on this stack. Current detector timing, batching, and trust quantities do not by themselves reduce D1 reversal cost to a lab meter.

## Proposed Next Action

Keep the platform fixed and make the next step narrower, not broader:

1. Use the T75 photon time-tagging stack as the designated P01 detector platform.
2. Map one concrete lab export into the T87 raw-log tables without changing the T76/T78 schema.
3. Add one explicitly metered physical cost observable for archive rewrite, detector reset, or signed-record invalidation, and test whether it changes any TaF verdict independently of provenance statistics.

## Claim-Status Posture

- Q1 posture from this run: unchanged `partially_supported`
- detector route posture: strengthened only as a pre-registered detector-record provenance protocol
- weak-measurement posture: remains blocked operationalization, not near-ready discriminator
- mathematical-physics posture: the repo now has one concrete detector-platform crosswalk, but not yet a full Hamiltonian-plus-thermodynamic instantiation
