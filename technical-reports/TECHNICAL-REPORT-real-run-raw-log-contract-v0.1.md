# Technical Report: Real-Run Raw-Log Contract v0.1

## Claim Under Test

T86 left the detector branch at a sharp boundary. Perturbation response and
signed ancestry DAGs can be independently decisive when timing and tags are
ambiguous, but the result is still a constructed fixture. The next question is
not whether D1 can be rescored. It is whether a real detector deployment can
produce the event-level logs needed to instantiate that fixture without post
hoc choices.

## Artifact

T87 adds an executable raw-log contract. It specifies the tables, columns,
controls, and pre-data commitments required before a real ambiguous-tag
deployment may populate the locked T76/T86 evidence counts.

Required event-level tables:

- `preregistration_manifest`;
- `control_pair_manifest`;
- `event_time_tag_stream`;
- `signature_verification_log`;
- `tag_ambiguity_challenge_log`;
- `perturbation_trial_log`;
- `ancestry_dag_edge_export`;
- `trust_boundary_audit_log`;
- `demotion_decision_log`.

The validator rejects dashboard-only summaries, missing copied/independent
witness labels, post hoc policy or demotion rules, summary-only DAG exports,
and mutable or unjoinable event tables.

## Current Strongest Claim

T87 turns T86's next-work item into a falsifiable admission contract: only
pre-registered, event-level, joinable, immutable raw logs with
copied/independent controls and isolated perturbation/DAG tests may populate
the locked T76/T86 counts.

## What This Improved

The detector branch now has a concrete empirical intake standard. A future
run cannot claim support from coarse dashboards, fixture counts, or narrative
provenance. It must publish enough raw rows to compute the T76 evidence fields
and reproduce the T86 ambiguous-tag controls without changing the schema.

## What This Weakened Or Falsified

T87 weakens Q1 by making the detector route even more conditional. Passing
T87 does not support Q1; it only permits the next audit. If no detector stack
can export these tables before analysis, the T86 positive fixtures remain
non-empirical and the detector branch should be demoted.

## Falsification Condition

Demote the detector branch if no feasible deployment can publish these
event-level tables before analysis, or if a complete raw log populates the
locked T76/T86 adapter but loses the signed recovery, all-ambiguous withhold,
perturbation/DAG rescue, or contaminated-control withhold separations.

## Claim Ledger Update

Q1 remains `partially_supported`, but the detector branch should be stated as:

```text
Detector-level Q1 is only a pre-registered detector-record admissibility
protocol. A real ambiguous-tag deployment must pass the T87 raw-log contract
before its counts can be treated as evidence. Dashboard summaries, post hoc
demotion rules, missing copied/independent witness labels, mutable event logs,
and summary-only DAG exports withhold the detector branch rather than support
it.
```

## Open Blocker

No actual detector event log is present. T87 supplies the table contract and
rejection rules, but cannot populate evidence counts or compare the result
with decoherence, quantum Darwinism, relational quantum mechanics, consistent
histories, many-worlds, or QBism.

## Next Work

Pick a concrete photon time-tagging or Stern-Gerlach readout stack, map each
instrument export to the T87 tables, then run the locked T76/T86 scorer
without adding fields or changing policy.

## Reproduction

```bash
python -m unittest tests.test_real_run_raw_log_contract -v
python -m models.run_t87
```
