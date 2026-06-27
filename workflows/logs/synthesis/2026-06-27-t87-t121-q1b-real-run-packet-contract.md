---
document_type: synthesis_status
batch_item: seventh_20_task_3
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T87-T121 Q1B Real-Run Packet Contract

## Status

This note integrates two Q1B infrastructure gates. It supplies no detector data.

## Sources read

- `tests/T87-real-run-raw-log-contract.md`
- `results/real-run-raw-log-contract-v0.1-results.md`
- `tests/T121-real-detector-packet-schema-audit.md`
- `results/real-detector-packet-schema-audit-v0.1-results.md`

## Plain-English finding

Q1B needs both raw event logs and packet governance. Valid raw detector data is
not enough if the provenance, keys, revocation, publication, and dispute state
are missing.

## Technical conclusion

T87 defines the real-run raw-log contract: immutable, event-level, joinable
tables with preregistration, controls, time tags, signatures, ambiguity
challenges, perturbation trials, DAG edges, trust-boundary audit, and demotion
decisions.

T121 defines the minimal packet object around those rows: raw payload plus
provenance, authority, publication, revocation, key state, witnesses,
reconstruction paths, admissibility tokens, and challenge status.

Together they state the Q1B precondition before D1 scoring.

## Minimum next task

Build one combined Q1B packet template that maps T87 tables into T121 packet
fields and requires revocation, key-continuity, and dispute-state checks before
scoring.

## Stop condition

Reject dashboard summaries, post hoc demotion rules, missing copied/independent
controls, summary-only DAG exports, unjoinable tables, and raw-valid but
packet-inadmissible detector exports.

