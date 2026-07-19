---
artifact_type: agent_run
status: complete
run_id: RUN-20260718-516-time-as-finality
started: 2026-07-18T22:41:00-05:00
completed: 2026-07-18T22:45:00-05:00
workflow: CapacityOS repository-work-cycle
mode: execute
scope: cai_directed
lane: '1'
purpose: progress
claim_movement: false
external_action: false
---

# RUN-20260718-516 TaF T587 Causal-Collapse Boundary Attack

## Trigger

CapacityOS CAI repository-work-cycle selected Time as Finality for a bounded
repo-local child run. The run loaded local authority, the Lane manifest and
state, the System steward routing package, current mailbox presence, and the
emergency revocation file before consequence.

Checked evidence:

- Target checkout clean on `main` before edits.
- No `capacityos-writer.lock` was present.
- `system/operations/lane-emergency-revocations.yaml` had no entries.
- No unarchived `system/mailboxes/time-as-finality` proposal files were present.
- CAI quick-load constitution digest matched the pinned digest in the parent
  instruction.

## Purpose Selection

Mailbox disposition was not selected because no unarchived mailbox item was
present. Lane A was green from the prior rerank. Lane 1 progress was justified
by `steward/research-portfolio.json`, which named
`TAF-T586-CAUSAL-COLLAPSE-ATTACK` as `ACTIVE_NEXT`.

## Work Performed

Added T587 as an executable attack gate:

- `models/t587_t586_causal_collapse_boundary_attack.py`
- `tests/test_t587_t586_causal_collapse_boundary_attack.py`
- `tests/T587-t586-causal-collapse-boundary-attack.md`
- `results/T587-t586-causal-collapse-boundary-attack-v0.1.json`
- `results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md`

Updated:

- `ROADMAP.md`
- `TESTS.md`
- `steward/research-portfolio.json`
- `LANE-STATE.yaml`

## Result

T587 returns a review-only downgrade. On the frozen T586 event system, ordinary
task-prerequisite dependency exactly reproduces the record-capability order,
and the strongest standard dependency and supplied causal comparators strictly
absorb it. The surviving value is only a typed record-prerequisite filter over
issued records.

The boundary-input screen admits only explicit physical record production and
native record-issuance rules as record-order sources. Access changes,
capability deltas by themselves, final-boundary selection, observer readout,
physical intervention, autonomous feedback, edge/defect degrees of freedom,
continuous flux, and stochastic input do not count without issued records.

No physical time, temporal issuance, causal-order replacement, source-law
novelty, universal capability measure, claim-ledger movement, Canon Index
movement, canon verdict, public posture, publication, TAF3, TAF8, S1, or
cross-repo truth movement is earned.

## Rerank

`CAPABILITY-TO-TEMPORAL-ORDER` is now `WAITING_FOR_SOURCE_PACKET` in
`steward/research-portfolio.json`; the T586 attack item is
`ENDPOINT_NEGATIVE_REVIEW_ONLY`. Reopen Lane 1 only for a provenance-valid
physical source packet, frozen capability witness, or sharper counterexample
that changes the record-issuance contract.

## Validation

Run:

```text
python -m models.t587_t586_causal_collapse_boundary_attack --write-results
python -m unittest tests.test_t587_t586_causal_collapse_boundary_attack
```
