# T96 Results: Detector Feasibility Checklist

## Route status

Checklist: `t75_t87_t95_detector_route_feasibility`

Route status: `feasible_as_governance_heavy_dry_run_only`

Next allowed step: `publish_locked_dry_run_packet_before_any_q1_claim`

## Requirement split

- Native tables: event_time_tag_stream
- Middleware tables: signature_verification_log, ancestry_dag_edge_export
- Custom control tables: control_pair_manifest, tag_ambiguity_challenge_log, perturbation_trial_log
- Governance tables: preregistration_manifest, trust_boundary_audit_log, demotion_decision_log
- Blocker tables: control_pair_manifest, tag_ambiguity_challenge_log, perturbation_trial_log, demotion_decision_log

## Required T87 tables

- `preregistration_manifest`: `run_id`, `registered_at`, `first_event_not_before`, `policy_hash`, `analysis_code_hash`, `evidence_schema_hash`, `demotion_rules_hash`, `confidence_floor_low`, `max_false_risk_high`
- `control_pair_manifest`: `pair_id`, `role`, `expected_relation`, `local_record_id`, `archive_record_id`, `source_event_id`, `timing_bin_id`, `randomization_seed_commitment`, `declared_before_event`
- `event_time_tag_stream`: `event_id`, `detector_id`, `local_time`, `local_sigma`, `archive_time`, `archive_sigma`, `batch_id`, `batching_window`, `timing_uncertainty_model_id`
- `signature_verification_log`: `event_id`, `tag_id`, `signature_id`, `verification_result`, `signer_key_id`, `forgery_challenge_id`, `spoof_challenge_id`, `verification_timestamp`
- `tag_ambiguity_challenge_log`: `challenge_id`, `event_id`, `role`, `retained_tag`, `accepted_forged_tag`, `accepted_spoofed_independent_tag`, `unique_independent_tag`, `verdict`
- `perturbation_trial_log`: `trial_id`, `pair_id`, `perturbed_record_id`, `perturbation_type`, `response_changed`, `independent_false_change`, `back_action_detected`, `pre_trial_state_hash`, `post_trial_state_hash`
- `ancestry_dag_edge_export`: `edge_id`, `child_record_id`, `parent_record_id`, `edge_signature_id`, `edge_verified`, `export_snapshot_id`, `truncation_flag`, `false_shared_edge_challenge_id`
- `trust_boundary_audit_log`: `audit_id`, `component`, `boundary_type`, `integrity_check_passed`, `key_scope`, `operator_id_hash`, `audit_timestamp`
- `demotion_decision_log`: `run_id`, `control_role`, `demotion_condition`, `triggered`, `applied_before_d1`, `reason`

## Strongest claim

The surviving detector-side Q1 route is not a native detector measurement path. It survives only as a governance-heavy dry-run protocol in which the decisive bottlenecks are copied/independent controls, ambiguity challenges, perturbation controls, and pre-data demotion rules rather than detector timing itself.

## What this improved

T96 converts the vague phrase 'instrument-facing feasibility' into a table-by-table burden split. A serious reader can now see which requirements come from hardware, which come from provenance logging, and which are pre-data governance commitments that can kill the route before any D1 audit.

## What this weakened

This weakens the detector branch again. Only one required T87 table is native to the named time-tagging hardware. The rest of the route is carried by archive middleware, control design, and analysis governance, so the branch should not be described as a detector-physics discriminator.

## Falsification condition

T96 fails if a realistic detector stack can natively export most of the T87 control, provenance, and demotion packet without custom middleware or governance locks, or if a dry run lacking the listed blocker tables still legitimately upgrades Q1.

## Q1 update

Q1 remains partially supported, but the detector branch should now be read as a dry-run admissibility program over classical record governance. Until a locked packet with copied/independent controls, ambiguity challenges, perturbation trials, signed raw ancestry edges, trust audits, and pre-data demotion rules is executed, the route does not rise above provenance bookkeeping.

## Open blocker

The repo still has no locked dry-run packet with real rows. The main blocker is not timing hardware; it is the pre-data assembly of control manifests and governance logs that would let a hostile reviewer reject post hoc choices.

## Recommended next

Build one dry-run packet skeleton with file names, row schemas, hash commitments, copied/independent controls, ambiguity challenges, perturbation trial plan, trust audit template, and demotion log template, then reject the route if a lab cannot fill it before data collection.
