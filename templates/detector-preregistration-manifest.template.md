# Detector Pre-Registration Manifest Template

Status: template
Use: T521 detector manifest template gate

This template is filled before detector event collection. It binds the T97 raw-log
packet scaffold, T121/T133 wrapper fields, T100 authority separation, and the
claimed review tier before the first event. It is not detector evidence by itself.

## Manifest Metadata

- Manifest name: `<manifest_name>`
- Run id: `<run_id>`
- Registered at UTC: `<registered_at>`
- First event not before UTC: `<first_event_not_before>`
- T97 manifest hash: `<t97_manifest_hash>`
- Top-level manifest hash: `<manifest_hash>`
- No data analyzed before manifest lock: `[ ] yes`
- Do not enter detector outcome values before event collection. Commit export
  rules, schemas, state sources, and hashes only.

## Claimed Tier

Check exactly one before event collection.

- [ ] raw_log_preservation
- [ ] provisional_admission
- [ ] claim_review

## T97 Table Commitments

| Table | File name | Schema hash | Export checksum | Join keys |
| --- | --- | --- | --- | --- |
| preregistration_manifest | `dry-run/t97/preregistration_manifest.jsonl` | `<schema_hash>` | `<export_checksum>` | `run_id` |
| control_pair_manifest | `dry-run/t97/control_pair_manifest.jsonl` | `<schema_hash>` | `<export_checksum>` | `pair_id, source_event_id, timing_bin_id` |
| event_time_tag_stream | `dry-run/t97/event_time_tag_stream.jsonl` | `<schema_hash>` | `<export_checksum>` | `event_id, batch_id` |
| signature_verification_log | `dry-run/t97/signature_verification_log.jsonl` | `<schema_hash>` | `<export_checksum>` | `event_id, tag_id` |
| tag_ambiguity_challenge_log | `dry-run/t97/tag_ambiguity_challenge_log.jsonl` | `<schema_hash>` | `<export_checksum>` | `challenge_id, event_id` |
| perturbation_trial_log | `dry-run/t97/perturbation_trial_log.jsonl` | `<schema_hash>` | `<export_checksum>` | `trial_id, pair_id` |
| ancestry_dag_edge_export | `dry-run/t97/ancestry_dag_edge_export.jsonl` | `<schema_hash>` | `<export_checksum>` | `edge_id, child_record_id, parent_record_id` |
| trust_boundary_audit_log | `dry-run/t97/trust_boundary_audit_log.jsonl` | `<schema_hash>` | `<export_checksum>` | `audit_id, component` |
| demotion_decision_log | `dry-run/t97/demotion_decision_log.jsonl` | `<schema_hash>` | `<export_checksum>` | `run_id, control_role` |

## T121/T133 Wrapper Field Commitments

Use `schema_commitment` for schema or source commitments, `state_commitment` for
predeclared status registries, and `export_rule_commitment` for future payload or
causal export rules. Hashes bind the rule, source, schema, or registry used later.

| Field | Commitment kind | Commitment hash | Notes |
| --- | --- | --- | --- |
| detector_identity | schema_commitment | `<commitment_hash>` | Detector identity source and stable naming rule. |
| run_session_id | schema_commitment | `<commitment_hash>` | Run/session id source and uniqueness rule. |
| timestamp | schema_commitment | `<commitment_hash>` | Timestamp format and clock/source rule. |
| causal_ordering_data | export_rule_commitment | `<commitment_hash>` | Causal-order export rule; no observed event values. |
| raw_measurement_payload | export_rule_commitment | `<commitment_hash>` | Raw payload export rule; no observed detector outcomes. |
| calibration_reference | schema_commitment | `<commitment_hash>` | Calibration artifact source and version rule. |
| provenance_chain | schema_commitment | `<commitment_hash>` | Provenance chain schema and source rule. |
| signatures | schema_commitment | `<commitment_hash>` | Signature scheme and verification-log rule. |
| authority_domains | schema_commitment | `<commitment_hash>` | Authority-domain partition evidence. |
| publication_status | state_commitment | `<commitment_hash>` | Publication or preregistration status source. |
| revocation_status | state_commitment | `<commitment_hash>` | Revocation registry and check-time source. |
| key_state | state_commitment | `<commitment_hash>` | Key-rotation, compromise, and continuity source. |
| witness_references | schema_commitment | `<commitment_hash>` | Witness/control reference schema. |
| reconstruction_paths | schema_commitment | `<commitment_hash>` | Reconstruction path schema and source rule. |
| admissibility_tokens | schema_commitment | `<commitment_hash>` | Token source and validation rule. |
| challenge_status | state_commitment | `<commitment_hash>` | Challenge/dispute lifecycle source. |

## Authority Partition

Keep authority domains separated at the claimed tier. For claim review, every
domain below must have a distinct responsible signer or organization.

- analysis_governor: `<signer_or_org>`
- control_designer: `<signer_or_org>`
- instrument_operator: `<signer_or_org>`
- archive_custodian: `<signer_or_org>`
- trust_auditor: `<signer_or_org>`

## Pre-Data Boundary Checks

- `[ ]` Manifest registered before `first_event_not_before`.
- `[ ]` No detector event rows or payload values inspected before manifest lock.
- `[ ]` Claimed tier selected before event collection.
- `[ ]` T97 table commitments are complete and hash-bound.
- `[ ]` Wrapper field commitments match the claimed tier.
- `[ ]` Authority partition satisfies the T100 lower bound.
- `[ ]` Any later schema, authority, tier, wrapper-policy, or hash change fails the claimed tier.

## Fill/Review Notes

- `raw_log_preservation` requires a valid T97 scaffold only.
- `provisional_admission` requires all provisional wrapper fields and T100 authority evidence.
- `claim_review` additionally requires witness references, reconstruction paths, and challenge/dispute state.
- This template does not move Q1B, D1, claim status, public posture, or external publication.
