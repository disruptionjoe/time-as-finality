---
document_type: synthesis_preflight
batch_item: third_batch_task_2
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# Q1B Federated Detector Manifest Preflight

## Scope

This note completes third-batch task 2 from
`workflows/logs/best-next-move/2026-06-27-third-10-research-orchestration.md`.
It is a synthesis/preflight artifact only. It does not update
`CLAIM-LEDGER.md`, `ROADMAP.md`, tests, results, models, README, or
open-problem files.

This preflight does not supply detector evidence. It converts the current Q1B
external blocker into a pre-data manifest checklist for a future named
deployment.

## Grounding Readout

Read surfaces used:

- `open-problems/q1b-federated-detector-deployment-handoff.md`.
- `CLAIM-LEDGER.md` Q1 and Q1B rows.
- Q1B deployment context from T136, T138, T161, T173, T175, T176, and T178, as
  named by the orchestration file and handoff.

Current baseline:

- Q1 remains `demoted` as a roadmap umbrella.
- Q1B remains `externally_blocked`.
- Q1B is an admissibility protocol over already formed detector records, not
  empirical support.
- The only live route is a named deployment that signs a pre-data manifest,
  preserves a real authority split, later exposes full event-level packet rows
  during the challenge window, and survives the relevant detector packet gates.

## Pre-Data Manifest Checklist

Before the first detector event, a candidate deployment must freeze:

1. Stable deployment name, run id, detector group, and signatory authority.
2. Claimed tier: `raw_log_preservation`, `provisional_admission`, or
   `claim_review`.
3. T97 table schema hashes and empty-export checksums.
4. T121/T133 wrapper-field commitments for the claimed tier.
5. Raw-payload export rule, without observed detector payload values.
6. T100-compatible authority partition.
7. T161 control-root map for manifest registration, archive mutation, audit
   attestation, publication release, and revocation control.
8. Hostile-control plan for replay/spoof, perturbation/back-action,
   provenance-DAG truncation or false ancestry, signature/key failure, and
   delayed publication.
9. Top-level manifest hash and timestamp before event data are inspected.
10. For claim review, an independent escrow authority and a five-domain minimum
    effective partition.
11. If threshold keys or multisig are used, a T175-valid quorum map proving that
    archive custody, escrow, and trust audit are mandatory guardians of every
    authorized challenge-window release, revocation, and audit path.
12. A T176-valid freeze policy for guardian identity and critical
    challenge-window rights, or a T178-valid preserved-rights successor policy
    with fixed triggers, preserved guardians, full row-review access, preserved
    identity, and immutable transition logs.

The manifest is invalid for Q1B if it is assembled after event collection or if
its schema, wrapper policy, authority partition, control roots, export rule,
guardian map, or critical challenge-window rights can drift after hashing.

## Tier Separation

| Tier | Minimum purpose | Required boundary | Not enough |
| --- | --- | --- | --- |
| `raw_log_preservation` | Preserve event-level raw-log evidence under a frozen schema and export rule. | T97-style table hashes, empty-export checksums, and post-event raw rows. | A dashboard, aggregate timing plot, or post hoc schema. |
| `provisional_admission` | Add packet wrappers and authority commitments sufficient for provisional review. | T121/T133 wrapper commitments plus non-collapsed authority roles. | Raw rows without wrapper policy or a tier declared after data. |
| `claim_review` | Support D1-facing review during a challenge window. | Full event-level rows, independent escrow, at least five effective authority domains, mandatory guardians, and frozen rights. | Proof-only, sampled-row, private-escrow-only, delayed-release, or summary-only substitutes. |

Tier labels must be pre-data. A deployment cannot collect data at a weaker tier
and later relabel itself as claim review.

## Required After-Data Packet

After event collection, the deployment must publish or make reviewable:

1. Event-level raw measurement payload rows under the precommitted export rule.
2. Event loss and retention rows.
3. Signature verification and key-state rows.
4. Replay/spoof control rows.
5. Perturbation or back-action control rows.
6. Provenance-DAG ancestry and truncation-control rows.
7. Publication timing and immutable archive rows.
8. For claim review, reconstruction-path, witness-reference, revocation, and
   challenge-state rows.
9. Control-root provenance sufficient to audit that the declared authority split
   was operationally real.
10. Full bound event rows during the challenge window, not just proofs,
    summaries, samples, delayed disclosures, or auditor statements.
11. Escrow provenance showing that the escrow custodian remained independent.
12. Threshold or multisig release logs showing that all critical authorized
    paths included the mandatory archive, escrow, and trust guardians.
13. Governance and change-log provenance showing that guardian identity and
    critical challenge-window rights stayed frozen after data collection.
14. If a successor policy was invoked, trigger and transition logs showing that
    the same guardians, identity, and full review access were preserved.

Dashboard summaries do not substitute for event-level packet rows.

## Null And Demotion Conditions

Treat the route as null for Q1B, or demote it to scaffold-only, if any of the
following occur:

- No named deployment or signatory exists.
- The manifest is assembled after data collection.
- The claimed tier changes after data.
- The payload field contains observed detector values before the event boundary.
- Schema hashes, wrapper policy, authority partition, control roots, guardian
  map, export rules, or challenge-window rights drift after the manifest hash.
- Authority labels hide shared critical control roots that collapse the
  effective partition.
- Archive custody and trust audit are controlled by the same authority.
- Escrow custody is absent, private-only, or merged into another authority for
  claim review.
- Hostile controls are absent or reported only as aggregate pass/fail claims.
- The deployment offers dashboard summaries, proof certificates, sampled rows,
  private escrow, or delayed release instead of reviewable full rows during the
  challenge window.
- A threshold or multisig quorum can bypass archive custody, escrow, or trust on
  a critical release, revocation, or audit action.
- Guardian replacement, trust suspension, break-glass override, or other
  challenge-window policy mutation remains available after data collection.
- A legal, safety, or emergency successor policy changes guardians, identity, or
  full row-review rights instead of preserving them under fixed triggers and
  immutable logs.

Without a named signatory and later full event-level packet review, Q1B remains
`externally_blocked`.

## Acceptance Criteria

This preflight satisfies the third-batch task by:

- Converting the external blocker into a concrete pre-data manifest checklist.
- Separating `raw_log_preservation`, `provisional_admission`, and
  `claim_review` tiers.
- Requiring event-level rows, full challenge-window row-review rights,
  independent escrow, effective authority separation, mandatory threshold
  guardians, and frozen critical rights.
- Keeping Q1B externally blocked unless a named deployment signs the manifest
  and later supplies the bound rows without drift.

## Next Executable Artifact Shape

The next non-null artifact should be a signed deployment-intake packet, not
another internal detector model. Its minimum shape is:

```text
q1b_detector_manifest_packet:
  deployment_name:
  signatory:
  run_id:
  claimed_tier:
  preregistration_timestamp:
  t97_schema_hashes:
  empty_export_checksums:
  wrapper_commitments:
  raw_payload_export_rule:
  authority_partition:
  control_root_map:
  escrow_authority:
  threshold_or_multisig_quorum_map:
  challenge_window_freeze_policy:
  preserved_rights_successor_policy:
  hostile_control_plan:
  top_level_manifest_hash:
  after_data_event_row_release_plan:
```

The executable follow-on should first validate the manifest before data. Only
after data collection should it validate row availability, authority behavior,
guardian logs, and challenge-window rights against the frozen manifest.

## No-Promotion Guardrails

- Do not cite this preflight as detector evidence, Q1B support, or a prediction.
- Do not promote Q1B above `externally_blocked` without a named signatory and a
  later reviewable event-level packet.
- Do not treat good detector hardware, accurate time tags, public dashboards, or
  ordinary lab provenance as satisfying Q1B.
- Do not replace full event-level challenge-window review with summaries,
  proof-only artifacts, sampled rows, private escrow, or delayed release.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, results, models, README,
  or open-problem files from this synthesis note.
