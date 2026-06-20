# T78 Results: Pre-registered Detector Deployment Protocol

Strongest claim: The detector branch now has a pre-data gate: a real deployment can only test Q1 if it fixes the T76 evidence schema, T77-safe policy corridor, negative controls, raw log sources, and demotion rule before the first event.

Weakened claim: T78 weakens the detector branch by making T76/T77 insufficient for any further Q1 upgrade. Fixture counts, post hoc policy choice, missing unsigned controls, and permissive corridors are all rejected before D1 scoring.

## Required evidence fields

- `local_sigma`
- `archive_sigma`
- `batching_window`
- `tag_retention`
- `signature_verification`
- `accepted_forged_tags`
- `accepted_spoofed_independent_tags`
- `independent_unique_tags`
- `detector_boundary_integrity`
- `archive_boundary_integrity`
- `transport_boundary_integrity`
- `dependent_perturbation_changes`
- `independent_perturbation_false_changes`
- `perturbation_back_action_events`
- `dag_observability`
- `signed_dag_edges`
- `dag_truncation_events`
- `false_shared_dag_edges`
- `pre_registered_threshold_coverage`

## Required controls

- `timing_only_unsigned_negative_control`
- `copied_record_spoof_challenge`
- `independent_record_uniqueness_challenge`
- `perturbation_positive_negative_controls`
- `dag_truncation_and_replay_challenge`

## Required raw log sources

- `raw_time_tag_stream`
- `signature_verification_log`
- `archive_receipt_chain`
- `trust_boundary_audit_log`
- `perturbation_protocol_log`
- `ancestry_dag_export`

## Audit table

| Plan | Verdict | Failure reasons | Next allowed audit |
| --- | --- | --- | --- |
| complete_signed_detector_deployment_preregistration | admissible_for_real_deployment_audit | none | run_t76_t77_on_real_log |
| posthoc_policy_after_data_control | inadmissible_for_q1_upgrade | policy_chosen_after_data | withhold_detector_q1_upgrade |
| missing_unsigned_timing_control | inadmissible_for_q1_upgrade | missing_required_negative_controls | withhold_detector_q1_upgrade |
| fixture_counts_without_raw_log | inadmissible_for_q1_upgrade | no_real_raw_deployment_log, fixture_counts_only | withhold_detector_q1_upgrade |
| permissive_policy_control_leak | inadmissible_for_q1_upgrade | policy_outside_t77_safe_corridor | withhold_detector_q1_upgrade |

## Falsification condition

Demote detector-level Q1 if no real deployment can satisfy this pre-data contract and still preserve signed recovery, unsigned withhold, and incomplete-pre-registration failure under the locked T76/T77 audit.

## Q1 update

Keep Q1 partially supported only as a pre-registered, real-log detector-provenance protocol claim. Synthetic fixtures and post hoc policy selection cannot upgrade the detector branch.

## Blocker

No real deployment log is present; T78 only defines the gate that future evidence must pass.

## Next move

Populate the T78 contract from an actual detector run, then run the locked T76/T77 pipeline without changing the evidence fields or policy corridor.
