# T138 Results: Detector Manifest Workflow Fit

## Human-fillable manifest template

| Section | Item | Tier | Pre-event | Acceptable fill | Null if missing |
| --- | --- | --- | --- | --- | --- |
| `run_identity` | `run_id` | `raw_log_preservation` | `True` | Stable run/session identifier shared by every table. | Rows cannot be joined to a frozen event collection. |
| `run_identity` | `claimed_tier` | `raw_log_preservation` | `True` | One of raw_log_preservation, provisional_admission, claim_review. | Later tier upgrades are post hoc. |
| `run_identity` | `first_event_not_before` | `raw_log_preservation` | `True` | Timestamp later than manifest registration. | The manifest cannot prove it was locked pre-data. |
| `t97_tables` | `table_hashes` | `raw_log_preservation` | `True` | Schema hash and empty-export checksum for preregistration_manifest, control_pair_manifest, event_time_tag_stream, signature_verification_log, tag_ambiguity_challenge_log, perturbation_trial_log, ancestry_dag_edge_export, trust_boundary_audit_log, demotion_decision_log. | The raw-log scaffold can drift during collection. |
| `authority` | `authority_partition` | `provisional_admission` | `True` | At least four T100-compatible domains, with trust_auditor independent of analysis, instrument, control, and archive roles. | The packet collapses into self-certification. |
| `wrapper` | `provisional_fields` | `provisional_admission` | `True` | detector_identity, run_session_id, causal_ordering_data, raw_measurement_payload, calibration_reference, provenance_chain, signatures, authority_domains, publication_status, revocation_status, key_state, admissibility_tokens | The packet cannot enter provisional review. |
| `wrapper` | `claim_review_fields` | `claim_review` | `True` | witness_references, reconstruction_paths, challenge_status | The packet can at most be provisionally admitted. |
| `payload_boundary` | `raw_measurement_payload` | `provisional_admission` | `True` | Export-rule commitment only; no observed payload values. | Pre-known detector outcomes invalidate the preregistration boundary. |
| `integrity` | `manifest_hash` | `raw_log_preservation` | `True` | Top-level hash binding tables, wrappers, tier, and authority. | The manifest contents are not fixed. |

## Workflow audits

| Workflow | Claimed tier | Max tier | Admissible | Verdict | Missing template items | Failures |
| --- | --- | --- | --- | --- | --- | --- |
| `common_single_lab_photonic_coincidence_workflow` | `claim_review` | `none` | `False` | `workflow_null_for_q1b` | `authority:authority_partition, run_identity:first_event_not_before, wrapper:authority_domains, wrapper:publication_status, wrapper:revocation_status, wrapper:key_state, wrapper:admissibility_tokens, wrapper:witness_references, wrapper:reconstruction_paths, wrapper:challenge_status` | `manifest_not_registered_before_first_event, data_accessed_before_manifest_lock, authority_partition_inadmissible:trust_auditor_not_independent, authority_partition_below_t100_lower_bound, missing_provisional_wrapper_commitments, missing_claim_review_wrapper_commitments` |
| `predata_single_lab_with_public_archive_workflow` | `provisional_admission` | `none` | `False` | `workflow_null_for_q1b` | `authority:authority_partition` | `authority_partition_inadmissible:trust_auditor_not_independent, authority_partition_below_t100_lower_bound` |
| `federated_predata_claim_review_workflow` | `claim_review` | `claim_review` | `True` | `claim_review_scaffold_fit` | `none` | `none` |
| `federated_but_preknown_payload_workflow` | `claim_review` | `none` | `False` | `workflow_null_for_q1b` | `payload_boundary:raw_measurement_payload_export_rule` | `predata_manifest_claims_observed_payload_values` |

## Strongest claim

T138 converts T136 into a human-fillable workflow gate. A common single-lab photonic coincidence workflow is null for Q1B, even if it has time tags and signed exports, because it is post hoc and authority-collapsed. A federated pre-data workflow can clear the manifest only as an evidence scaffold, not as detector support.

## What this improved

The detector branch now has a reviewer-facing template and a workflow-fit audit. Review can reject concrete lab plans before event collection instead of debating detector interpretations after data are seen.

## What this weakened

This weakens Q1B against realistic small-lab deployment stories. Pre-data table hashes and signatures are not enough when analysis, control design, archive custody, and trust audit collapse into the same authority structure.

## Falsification condition

T138 fails if a common single-lab or three-domain workflow can legitimately claim provisional or claim-review status without the T100-compatible authority split, or if the federated scaffold cannot actually be signed before data despite satisfying the manifest fields.

## Q1B update

Q1B remains externally blocked. Its current non-null path is no longer 'a lab with time tags'; it is a federated preregistration scaffold with T136 fields and T100-compatible authorities fixed before the first event.

## Claim ledger update

Add T138 to Q1B: the human-fillable manifest template rejects the common single-lab photonic workflow and a public-archive repair with merged authorities. Only a federated pre-data scaffold clears T136, and even that is not detector evidence until real rows populate the bound packet.

## Open blocker

No named real lab has agreed to fill and sign the federated T138/T136 template before detector event collection.

## Recommended next

Send the T138 template to one realistic detector group or map one named public experiment against it. If the group cannot provide independent archive and trust-audit roles pre-data, demote Q1B below active quantum-measurement work.
