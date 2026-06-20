# T97 Results: Detector Dry-Run Packet Skeleton

## Audit table

| Packet | Verdict | Evidence verdict | Failures | T87 verdict now | T87 failures now | Next step |
| --- | --- | --- | --- | --- | --- | --- |
| locked_t97_detector_dry_run_packet_skeleton | schema_complete_predata_scaffold_only | withhold_detector_q1_upgrade | none | inadmissible_for_q1_upgrade | no_real_raw_deployment_log | collect_real_rows_without_schema_or_policy_changes |
| placeholder_population_attempt_packet | inadmissible_dry_run_packet | withhold_detector_q1_upgrade | attempts_to_populate_counts_from_placeholders | inadmissible_for_q1_upgrade | no_real_raw_deployment_log, fixture_counts_only | repair_packet_before_collection |
| schema_drift_dry_run_packet | inadmissible_dry_run_packet | withhold_detector_q1_upgrade | unregistered_schema_columns | inadmissible_for_q1_upgrade | no_real_raw_deployment_log | repair_packet_before_collection |
| posthoc_detector_packet_skeleton | inadmissible_dry_run_packet | withhold_detector_q1_upgrade | packet_not_locked_before_first_event, data_accessed_before_packet_lock | inadmissible_for_q1_upgrade | contract_not_registered_before_first_event, policy_chosen_after_data, analysis_code_not_frozen, no_real_raw_deployment_log, demotion_rules_chosen_after_data | repair_packet_before_collection |
| missing_ambiguous_and_dag_control_roles_packet | inadmissible_dry_run_packet | withhold_detector_q1_upgrade | missing_t86_control_roles | inadmissible_for_q1_upgrade | no_real_raw_deployment_log, copied_independent_labels_not_preregistered, missing_t86_control_roles | repair_packet_before_collection |

## Locked packet manifest

Packet: `locked_t97_detector_dry_run_packet_skeleton`

Run id: `t97-dry-run-0001`

Manifest hash: `680f82152df4620d0f5fb13b09b945aafda4e857fe1e4e2c3f5032b09f4e63d0`

## Frozen table files

| Table | File | Join keys | Planned rows | Real rows present |
| --- | --- | --- | --- | --- |
| preregistration_manifest | dry-run/t97/preregistration_manifest.jsonl | run_id | 1 | False |
| control_pair_manifest | dry-run/t97/control_pair_manifest.jsonl | pair_id, source_event_id, timing_bin_id | 7 | False |
| event_time_tag_stream | dry-run/t97/event_time_tag_stream.jsonl | event_id, batch_id | 1 | False |
| signature_verification_log | dry-run/t97/signature_verification_log.jsonl | event_id, tag_id | 1 | False |
| tag_ambiguity_challenge_log | dry-run/t97/tag_ambiguity_challenge_log.jsonl | challenge_id, event_id | 4 | False |
| perturbation_trial_log | dry-run/t97/perturbation_trial_log.jsonl | trial_id, pair_id | 4 | False |
| ancestry_dag_edge_export | dry-run/t97/ancestry_dag_edge_export.jsonl | edge_id, child_record_id, parent_record_id | 1 | False |
| trust_boundary_audit_log | dry-run/t97/trust_boundary_audit_log.jsonl | audit_id, component | 5 | False |
| demotion_decision_log | dry-run/t97/demotion_decision_log.jsonl | run_id, control_role | 7 | False |

## Strongest claim

A detector-side Q1 dry-run packet can now be specified without schema ambiguity, but it remains only a pre-data scaffold. T87 would still reject it as evidence until real event rows replace template exports without changing schema, policy, demotion rules, or control roles.

## What this improved

T97 turns the T96 next-work item into a concrete, reviewable packet skeleton: every T87 table has an exact schema, file name, join key, schema hash, export checksum, and pre-data role. A lab can now fail the detector route by failing to freeze this packet before the first event.

## What this weakened

This weakens detector-side Q1 again. The route is no longer blocked by vague schema design; it is blocked by actual pre-data execution and real event-row population. Template rows, post hoc schema drift, and missing hostile controls do not upgrade Q1.

## Falsification condition

Demote the detector branch if a realistic lab workflow cannot freeze the T97 packet before event collection, or if the filled packet cannot pass T87 and preserve the T86 signed-DAG, perturbation, ambiguous-control, and contaminated-control separations under the locked schema.

## Q1 update

Q1 remains partially supported only as a detector-record admissibility protocol. T97 supplies a pre-data dry-run scaffold, not evidence; detector-side Q1 still withholds until real rows populate the locked packet and pass T87 before T76/T86 scoring.

## Claim ledger update

Add T97 to Q1 as a further narrowing: the detector branch has a schema-complete dry-run packet skeleton, but the strongest current claim is only that reviewers can check pre-data packet freezing. Placeholder rows, schema drift, post hoc packets, and missing hostile controls falsify any attempted detector upgrade.

## Open blocker

No actual detector event rows have been collected under the locked packet. The live blocker is operational: freeze the packet before first event, then fill it without schema changes.

## Recommended next

Instantiate the T97 packet in a real lab dry run with empty files, signed manifests, immutable export points, and operator handoff checks. If the lab cannot do that pre-data, demote the detector route below the active Q1 frontier.
