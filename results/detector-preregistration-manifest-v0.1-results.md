# T136 Results: Detector Pre-registration Manifest

## Manifest requirements

- T97 tables: `['preregistration_manifest', 'control_pair_manifest', 'event_time_tag_stream', 'signature_verification_log', 'tag_ambiguity_challenge_log', 'perturbation_trial_log', 'ancestry_dag_edge_export', 'trust_boundary_audit_log', 'demotion_decision_log']`
- Provisional fields: `['detector_identity', 'run_session_id', 'causal_ordering_data', 'raw_measurement_payload', 'calibration_reference', 'provenance_chain', 'signatures', 'authority_domains', 'publication_status', 'revocation_status', 'key_state', 'admissibility_tokens']`
- Claim-review fields: `['detector_identity', 'run_session_id', 'causal_ordering_data', 'raw_measurement_payload', 'calibration_reference', 'provenance_chain', 'signatures', 'authority_domains', 'publication_status', 'revocation_status', 'key_state', 'admissibility_tokens', 'witness_references', 'reconstruction_paths', 'challenge_status']`

## Manifest audits

| Manifest | Claimed tier | Max tier | Claimed admissible | T97 valid | Wrapper valid | Authority valid | Predata valid | Hash valid | Failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `complete_claim_review_manifest` | `claim_review` | `claim_review` | `True` | `True` | `True` | `True` | `True` | `True` | `none` |
| `provisional_only_manifest` | `provisional_admission` | `provisional_admission` | `True` | `True` | `True` | `True` | `True` | `True` | `none` |
| `raw_log_only_manifest` | `provisional_admission` | `raw_log_preservation` | `False` | `True` | `False` | `True` | `True` | `True` | `missing_provisional_wrapper_commitments` |
| `claim_review_missing_witness_manifest` | `claim_review` | `provisional_admission` | `False` | `True` | `False` | `True` | `True` | `True` | `missing_claim_review_wrapper_commitments` |
| `posthoc_claim_review_manifest` | `claim_review` | `none` | `False` | `True` | `True` | `True` | `False` | `True` | `manifest_not_registered_before_first_event, data_accessed_before_manifest_lock` |
| `three_domain_authority_manifest` | `claim_review` | `none` | `False` | `True` | `True` | `False` | `True` | `True` | `authority_partition_inadmissible:trust_auditor_not_independent, authority_partition_below_t100_lower_bound` |
| `deferred_tier_manifest` | `undeclared` | `claim_review` | `False` | `True` | `True` | `True` | `True` | `True` | `invalid_or_undeclared_claimed_tier` |
| `manifest_hash_mismatch_case` | `claim_review` | `none` | `False` | `True` | `True` | `True` | `True` | `False` | `manifest_hash_mismatch` |
| `observed_payload_value_manifest` | `claim_review` | `none` | `False` | `True` | `False` | `True` | `True` | `True` | `predata_manifest_claims_observed_payload_values` |

## Strongest claim

Q1B now has a concrete pre-event manifest gate. A detector deployment may claim only the strongest tier whose T97 table hashes, T121/T133 wrapper-field commitments, T100 authority partition, top-level manifest hash, no-data boundary, and claimed tier were frozen before the first event.

## What this improved

T136 closes the T134 integration gap without requiring impossible pre-event detector outcomes. It freezes export rules and field commitments before data, then makes any later tier upgrade a manifest failure rather than a matter of interpretation.

## What this weakened

This weakens Q1B operationally. Filled T97 rows, a post hoc wrapper, or a deferred tier declaration cannot upgrade detector evidence. A lab that cannot name the manifest, authority partition, and claimed tier pre-data has no admissible detector-branch claim.

## Falsification condition

T136 fails if a real detector deployment can legitimately claim provisional or claim-review status without pre-event wrapper-field commitments and authority evidence, or if the manifest requires actual detector outcomes before events rather than export-rule commitments.

## Q1B update

Q1B remains externally blocked, but its blocker is now sharper: produce one signed T136 manifest before event collection, then fill the bound packet without schema, authority, tier, or wrapper-policy changes.

## Claim ledger update

Add T136 to Q1B: detector packet admission now requires a pre-event manifest binding T97 table hashes, T121/T133 wrapper commitments, T100 authority separation, and the claimed tier. T97-only, post hoc, invalid-authority, deferred-tier, and pre-known-payload variants are null for the claimed tier.

## Open blocker

No real lab has signed and frozen a T136 manifest before detector event collection.

## Recommended next

Draft a human-fillable T136 manifest template and try to map one specific lab workflow onto it. If no plausible workflow can sign it pre-data, demote Q1B below active quantum-measurement work.
