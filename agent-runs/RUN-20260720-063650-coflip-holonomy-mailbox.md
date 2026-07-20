---
artifact_type: agent_run
status: complete
run_id: RUN-20260720-063650-time-as-finality
parent_run: RUN-20260720-063650-repository-work-cycle-cai
started: 2026-07-20T06:39:25-05:00
completed: 2026-07-20T06:40:39-05:00
workflow: CapacityOS repository-work-cycle
mode: execute
scope: cai_directed
lane: A
purpose: mailbox
claim_movement: false
external_action: false
---

# RUN-20260720-063650 TaF Co-Flip Holonomy Mailbox Disposition

## Target and Trigger

One bounded repository-work-cycle child attempt for `time-as-finality`.
Processed as untrusted proposal data:

- `system/mailboxes/time-as-finality/20260720-coflip-holonomy-upgrade-notice.md`

Mailbox was selected before Stewardship, Discovery, or Progress, and Lane A
was selected before disposition.

## Safety and Selection Pins

- Checkout began clean/even on `main` at `7adf3e2d4dd1e69475fb88aea8850b34ea7aad44`.
- Free memory was about 3.96 GiB of 15.65 GiB; no heavy build or test ran.
- No pre-existing owner writer claim, Git index lock, or open overlapping run
  was present. The recent RUN-568 receipt was complete.
- Lane A definition/control revision: 1/1. `LANES.yaml` SHA-256:
  `ff803b58e09bbbc12a35fb165e60b5f1848058d86185565713c781598dc67b8b`.
- Emergency-revocation revision 1 remained empty; SHA-256:
  `8a992d3eb3f61b51ef83aa7cb8f85a1865fd0bf76c1f690429fa200a1c698723`.
- Writable footprint: `steward/research-portfolio.json`, `LANE-STATE.yaml`,
  and this run receipt only.

## Provenance Check

The cited GU objects were inspected read-only. Commit `32e3603` contains the
machine-verification report and `sig_b5_habitat_probe.py`. The frozen packet
wrapper itself first appears in GU commit `cbcff7d`; it pins the underlying
evidence blobs to `32e3603`. No GU file was changed and no probe was rerun.

## Disposition

Accepted as a source-adjacent derivation-grade upgrade only:

- The GU finite-class co-flip is now supported as a machine-derived geometric
  Z/2 holonomy result, not merely an accounting identity.
- The packet remains GU-owned, conditional matrix-grade evidence. It is not a
  TaF-owned or independently sourced physical packet and does not supply a
  native record-issuance rule, frozen TaF-adjudicable witness, or finality-axis
  datum.
- T587's park therefore remains. No Lane 1 Progress, claim status, Canon Index,
  canon verdict, public posture, publication, or cross-owner truth moved.

Discovery and Progress were not selected after mailbox close because the
upgrade itself names the remaining gates and supplies none of them.

## Receipt

```yaml
result: progressed
purpose: mailbox
lane: A
notice_disposition: source_adjacent_derivation_upgrade
technical_progress_selected: false
claim_status_change: none
canon_verdict_change: none
external_action: false
root_mailbox_archive: parent_recorder_handoff
next_handoff: wait_for_independently_sourced_physical_packet_with_record_issuance
```

The parent recorder should append the mailbox processing receipt and move the
notice to `system/mailboxes/time-as-finality/archive/`. This child did not
write CapacityOS Runtime because its one writable repository was TaF.

## Validation

- Parsed `steward/research-portfolio.json` and asserted the new disposition ID.
- Parsed `LANE-STATE.yaml`, asserted schema coverage and this run reference.
- Inspected the exact declared diff; `git diff --check` passed.
- No heavy tests ran because this was a provenance and stewardship disposition,
  not a change to executable or scientific artifacts.
