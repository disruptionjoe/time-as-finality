# T87 Results: Real-Run Raw-Log Contract

Strongest claim: T87 turns T86's next-work item into a falsifiable admission contract: only pre-registered, event-level, joinable, immutable raw logs with copied/independent controls and isolated perturbation/DAG tests may populate the locked T76/T86 counts.

Weakened claim: T87 does not score D1, does not claim detector dynamics, and does not provide empirical support. It only specifies what a future detector deployment must log before Q1 can leave the fixture stage.

## Required T86 controls

- `copied_record_control_pairs`
- `independent_record_control_pairs`
- `all_channels_ambiguous_negative_control`
- `clean_perturbation_only_positive_control`
- `backaction_perturbation_contamination_control`
- `clean_signed_dag_positive_control`
- `dag_truncation_false_edge_control`

## Required event-level tables

- `preregistration_manifest`: `run_id`, `registered_at`, `first_event_not_before`, `policy_hash`, `analysis_code_hash`, `evidence_schema_hash`, `demotion_rules_hash`, `confidence_floor_low`, `max_false_risk_high`
- `control_pair_manifest`: `pair_id`, `role`, `expected_relation`, `local_record_id`, `archive_record_id`, `source_event_id`, `timing_bin_id`, `randomization_seed_commitment`, `declared_before_event`
- `event_time_tag_stream`: `event_id`, `detector_id`, `local_time`, `local_sigma`, `archive_time`, `archive_sigma`, `batch_id`, `batching_window`, `timing_uncertainty_model_id`
- `signature_verification_log`: `event_id`, `tag_id`, `signature_id`, `verification_result`, `signer_key_id`, `forgery_challenge_id`, `spoof_challenge_id`, `verification_timestamp`
- `tag_ambiguity_challenge_log`: `challenge_id`, `event_id`, `role`, `retained_tag`, `accepted_forged_tag`, `accepted_spoofed_independent_tag`, `unique_independent_tag`, `verdict`
- `perturbation_trial_log`: `trial_id`, `pair_id`, `perturbed_record_id`, `perturbation_type`, `response_changed`, `independent_false_change`, `back_action_detected`, `pre_trial_state_hash`, `post_trial_state_hash`
- `ancestry_dag_edge_export`: `edge_id`, `child_record_id`, `parent_record_id`, `edge_signature_id`, `edge_verified`, `export_snapshot_id`, `truncation_flag`, `false_shared_edge_challenge_id`
- `trust_boundary_audit_log`: `audit_id`, `component`, `boundary_type`, `integrity_check_passed`, `key_scope`, `operator_id_hash`, `audit_timestamp`
- `demotion_decision_log`: `run_id`, `control_role`, `demotion_condition`, `triggered`, `applied_before_d1`, `reason`

## T76 field mapping

- `preregistration_manifest` -> `pre_registered_threshold_coverage`
- `event_time_tag_stream` -> `local_sigma`, `archive_sigma`, `batching_window`
- `signature_verification_log` -> `tag_retention`, `signature_verification`, `accepted_forged_tags`, `accepted_spoofed_independent_tags`, `independent_unique_tags`
- `tag_ambiguity_challenge_log` -> `tag_retention`, `accepted_forged_tags`, `accepted_spoofed_independent_tags`, `independent_unique_tags`
- `perturbation_trial_log` -> `dependent_perturbation_changes`, `independent_perturbation_false_changes`, `perturbation_back_action_events`
- `ancestry_dag_edge_export` -> `dag_observability`, `signed_dag_edges`, `dag_truncation_events`, `false_shared_dag_edges`
- `trust_boundary_audit_log` -> `detector_boundary_integrity`, `archive_boundary_integrity`, `transport_boundary_integrity`

## Audit table

| Contract | Verdict | Failure reasons | Next allowed audit |
| --- | --- | --- | --- |
| complete_t86_event_level_raw_log_contract | admissible_for_t86_real_log_population | none | populate_t76_t86_counts_without_schema_changes |
| dashboard_only_summary_control | inadmissible_for_q1_upgrade | no_real_raw_deployment_log, fixture_counts_only, raw_tables_not_joinable_by_stable_event_id, event_level_logs_not_public_or_exportable, missing_required_evidence_fields, missing_required_raw_log_sources, missing_required_raw_log_tables | withhold_detector_q1_upgrade |
| missing_copied_independent_control_labels | inadmissible_for_q1_upgrade | copied_independent_labels_not_preregistered, missing_t86_control_roles | withhold_detector_q1_upgrade |
| posthoc_policy_and_demotion_control | inadmissible_for_q1_upgrade | policy_chosen_after_data, no_predeclared_demote_rule_for_control_leak, demotion_rules_chosen_after_data, incomplete_threshold_preregistration, policy_outside_t77_safe_corridor | withhold_detector_q1_upgrade |
| dag_export_without_raw_edge_columns | inadmissible_for_q1_upgrade | missing_required_raw_log_columns | withhold_detector_q1_upgrade |
| unlinked_or_mutable_event_tables | inadmissible_for_q1_upgrade | raw_tables_not_joinable_by_stable_event_id, required_tables_not_immutable_exports | withhold_detector_q1_upgrade |

## Falsification condition

Demote the detector branch if no feasible deployment can publish these event-level tables before analysis, or if a complete raw log populates the locked T76/T86 adapter but loses the signed recovery, all-ambiguous withhold, perturbation/DAG rescue, or contaminated-control withhold separations.

## Q1 update

Keep Q1 partially supported only as a pre-registered detector record admissibility protocol. A real ambiguous-tag deployment must first pass T87 before its counts can be treated as evidence; dashboard summaries, post hoc demotion rules, missing witness labels, and summary-only DAG exports withhold the detector branch.

## Open blocker

No actual detector event log is present. T87 supplies the table contract and rejection rules, but cannot populate the evidence counts or compare the result with decoherence/QD alternatives.

## Next move

Pick a concrete photon time-tagging or Stern-Gerlach readout stack, map each instrument export to the T87 tables, then run the locked T76/T86 scorer without adding fields or changing policy.
