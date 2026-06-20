# T87: Real-Run Raw-Log Contract

## Route

Quantum measurement / classical records.

## Question

What event-level raw-log contract must a real detector run satisfy before the
T86 ambiguous-tag channel-independence fixture can be treated as a real
deployment audit rather than another constructed count table?

## Motivation

T86 rescued perturbation response and signed ancestry DAGs from immediate
schema deletion, but only inside synthetic raw-log-count fixtures. The positive
cases rely on predeclared copied and independent controls, deliberately
ambiguous timing/tags, and isolated perturbation or DAG evidence.

T87 makes the next empirical step falsifiable before D1 scoring. It rejects
dashboard summaries, post hoc demotion rules, missing copied/independent
labels, summary-only DAG exports, and event tables that cannot be joined by
stable event identifiers.

## Contract

A future detector deployment is admissible only if it provides immutable,
event-level, joinable tables for:

- preregistration manifest;
- copied/independent control-pair manifest;
- event time-tag stream;
- signature verification log;
- tag-ambiguity challenge log;
- perturbation trial log;
- signed ancestry DAG edge export;
- trust-boundary audit log;
- demotion decision log.

The run must also fix the T78 evidence fields, T78 control roles, T86
ambiguous-tag control roles, T77-safe policy corridor, channel isolation tests,
and demotion rules before the first event.

## Success Criteria

- The complete event-level raw-log contract is admissible for T76/T86 count
  population without schema changes.
- A dashboard-only summary is rejected before scoring.
- Missing copied and independent witness labels are rejected.
- Post hoc policy and demotion rules are rejected.
- A DAG export without raw signed edge columns is rejected.
- Mutable or unjoinable event tables are rejected.

## Failure Criteria

- A dashboard summary or fixture-count table is allowed to upgrade Q1.
- A run without predeclared copied and independent controls is scored.
- A permissive or post hoc policy corridor is treated as equivalent to the
  T77-safe corridor.
- Summary-only DAG observability is treated as a signed ancestry export.
- The result is described as empirical support rather than an admission gate
  for a future real log.

## Claim Impact

If T87 passes, Q1 remains `partially_supported` only as a detector-record
admissibility protocol. T87 does not score D1 or claim detector dynamics. It
only specifies the raw-log table contract needed before a real ambiguous-tag
deployment can be evaluated.

If no feasible detector deployment can satisfy this contract, the detector
branch should be demoted further to a narrow record-audit discipline.

## Reproduction

```bash
python -m unittest tests.test_real_run_raw_log_contract -v
python -m models.run_t87
```
