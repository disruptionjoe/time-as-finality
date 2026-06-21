# T134 Results: Detector Dry-Run Tier Gate

## T97 native field coverage

| T121/T133 field | T97 coverage |
| --- | --- |
| `detector_identity` | `covered_by_event_time_tag_stream.detector_id` |
| `run_session_id` | `covered_by_preregistration_manifest.run_id` |
| `causal_ordering_data` | `covered_by_event_time_tag_stream_and_control_pair_manifest` |
| `raw_measurement_payload` | `missing_from_t97_raw_log_scaffold` |
| `calibration_reference` | `missing_from_t97_raw_log_scaffold` |
| `provenance_chain` | `partial_via_signature_log_ancestry_dag_and_trust_audit` |
| `signatures` | `covered_by_signature_verification_log` |
| `authority_domains` | `missing_from_t97_raw_log_scaffold` |
| `publication_status` | `missing_from_t97_raw_log_scaffold` |
| `revocation_status` | `missing_from_t97_raw_log_scaffold` |
| `key_state` | `missing_from_t97_raw_log_scaffold` |
| `witness_references` | `partial_via_control_and_challenge_tables` |
| `reconstruction_paths` | `missing_from_t97_raw_log_scaffold` |
| `admissibility_tokens` | `partial_via_policy_schema_and_demotion_hashes` |
| `challenge_status` | `missing_from_t97_raw_log_scaffold` |

## Integrated tier audits

| Case | Claimed tier | T97 real rows | Raw preserved | Provisional | Claim review | Blocking reasons |
| --- | --- | --- | --- | --- | --- | --- |
| `locked_t97_predata_scaffold_only` | `raw_log_scaffold` | `False` | `False` | `False` | `False` | `no_real_t97_rows, missing_t121_t133_packet_wrapper, t97_native_gap:raw_measurement_payload, t97_native_gap:calibration_reference, t97_native_gap:provenance_chain, t97_native_gap:authority_domains, t97_native_gap:publication_status, t97_native_gap:revocation_status, t97_native_gap:key_state, t97_native_gap:admissibility_tokens, t97_native_claim_review_gap:witness_references, t97_native_claim_review_gap:reconstruction_paths, t97_native_claim_review_gap:challenge_status` |
| `filled_t97_raw_log_only` | `provisional_admission` | `True` | `False` | `False` | `False` | `missing_t121_t133_packet_wrapper, t97_native_gap:raw_measurement_payload, t97_native_gap:calibration_reference, t97_native_gap:provenance_chain, t97_native_gap:authority_domains, t97_native_gap:publication_status, t97_native_gap:revocation_status, t97_native_gap:key_state, t97_native_gap:admissibility_tokens, t97_native_claim_review_gap:witness_references, t97_native_claim_review_gap:reconstruction_paths, t97_native_claim_review_gap:challenge_status` |
| `filled_t97_with_reference_wrapper` | `claim_review` | `True` | `True` | `True` | `True` | `none` |
| `filled_t97_missing_provenance_wrapper` | `provisional_admission` | `True` | `True` | `False` | `False` | `wrapper_provisional_failure:provenance_chain, wrapper_provisional_failure:signatures, wrapper_provisional_failure:admissibility_tokens` |
| `filled_t97_missing_witnesses_wrapper` | `claim_review` | `True` | `True` | `True` | `False` | `wrapper_claim_review_failure:witness_references` |
| `filled_t97_open_challenge_wrapper` | `claim_review` | `True` | `True` | `True` | `False` | `wrapper_claim_review_failure:challenge_status, wrapper_claim_review_failure:admissibility_tokens` |

## Strongest claim

T97 is necessary but not sufficient for Q1B tier admission. A schema-complete raw-log packet, even after real rows populate all T97 tables, cannot be treated as provisionally admissible or claim-review ready until a T121/T133 wrapper supplies raw payload, calibration, authority, publication, revocation, key-state, admissibility-token, reconstruction, and dispute fields.

## What this improved

T134 turns the T133 recommendation into an executable integration gate. Future detector packets now report three explicit tier outputs instead of one flat verdict: raw evidence preserved, provisionally admissible, and claim-review ready.

## What this weakened

This weakens the apparent sufficiency of the T97 dry-run scaffold. T97 raw-log readiness is only a lower layer; it must not be used as detector evidence admission or as a Q1B upgrade by itself.

## Falsification condition

T134 fails if real T97 rows alone are enough for provisional admission under the packet policy, or if a complete T121/T123 wrapper plus real T97 rows still cannot clear the three declared tiers without adding post hoc fields.

## Q1B update

Q1B remains externally blocked. The next admissible detector deployment must pre-register both the T97 raw-log scaffold and the T121/T133 wrapper, then state before events whether it claims only raw-log preservation, provisional admission, or full claim-review readiness.

## Claim ledger update

Add T134 to Q1B: T97 raw-log packets now feed an explicit tier gate. Filled T97 rows are necessary but not sufficient; missing T121/T133 wrapper fields block provisional admission, while missing witnesses or open challenges preserve intake but block claim review.

## Open blocker

No real deployment has frozen the combined T97 raw-log packet and T121/T133 wrapper before data collection.

## Recommended next

Build a single pre-registration manifest that binds T97 table hashes, T121 packet-wrapper fields, T100 authority-domain evidence, and the claimed tier before the first detector event.
