---
artifact_type: agent_run
status: complete
run_id: RUN-20260720-233708-time-as-finality
parent_run: RUN-20260720-233708-repository-work-cycle-cai-hourly
started: 2026-07-20T23:43:27-05:00
completed: 2026-07-20T23:43:27-05:00
workflow: CapacityOS repository-work-cycle
mode: execute
scope: cai_directed
lane: A
purpose: mailbox
claim_movement: false
external_action: false
---

# RUN-20260720-233708 TaF Involution-Refute Follow-up Disposition

## Target and proposal

Processed as untrusted proposal data after selecting Lane A:

- Runtime mailbox `time-as-finality/20260720-involution-refute-next-and-gu-vindication.md`
- SHA-256: `15706d6fc051ea5527758ec2e27c1a7b699fa471135a41cb359bc13fd65c5195`
- Cited TaF commit: `e99f8c58dfd7690323af2dcdf1145b6955cf8203`

The cited commit and its executable fixture resolve. TaF already owns the
fixture-grade `T-REFUTE`: for the T19 construction with at least two independent
future witnesses, the causal-past retraction is idempotent, oriented, and
non-invertible, while a fixpoint-free involution is an order-two automorphism.
The coincidence occurs only on the single-witness `k = 1` control.

The mailbox adds no source evidence. Its claim that the result supports TaF's
causal-boundary reading is accepted only as a pointer to the repo-owned result,
not as an imported conclusion or instruction.

## Disposition

Close the previously gated involution-typing target as
`CLOSED_REFUTED_FIXTURE_GRADE`. Preserve the exact scope: the GU/TaF time-face
comparison is leg-deep at this fixture, not mechanism-deep. No C1, T19, T92,
Canon Index, Complexity Ledger, physical-source gate, or public posture moves.

The proposed operator-grade lift is a named reopener, not an automatic next
run. It supplies no provenance-valid physical source packet or frozen witness
and does not close Lane 1's active source/issuance blocker. No technical swing
was selected after mailbox disposition.

## Receipt

```yaml
result: progressed
purpose: mailbox
lane: A
proposal_disposition: closed_refuted_fixture_grade_awareness_only
proposal_sha256: 15706d6fc051ea5527758ec2e27c1a7b699fa471135a41cb359bc13fd65c5195
technical_progress_selected: false
claim_status_change: none
canon_verdict_change: none
external_action: false
runtime_mailbox_archive: parent_recorder_handoff
next_handoff: wait_for_physical_source_packet_or_operator_grade_reopener_that_changes_the_active_blocker
```

The parent recorder may archive the exact hash-pinned Runtime proposal after
this receipt. This child did not write the Runtime mailbox.

## Validation

- Re-run `tests/involution_typing_probe.py`.
- Parse portfolio JSON and Lane-state YAML.
- Inspect the declared diff and run `git diff --check`.
- Run the portfolio contract test if present.

