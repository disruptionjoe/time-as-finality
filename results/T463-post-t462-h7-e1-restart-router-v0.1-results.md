# T463 - Post-T462 H7/E1 Restart Router - v0.1 results

> Routing/admission gate only. `CLAIM-LEDGER.md`, `TESTS.md`, `ROADMAP.md`, README, North Star files, public posture, hard policy, and cross-repo truth are untouched.

- Spec: `tests/T463-post-t462-h7-e1-restart-router.md`
- Model: `models/post_t462_h7_e1_restart_router.py`
- Tests: `tests/test_post_t462_h7_e1_restart_router.py`
- Artifact JSON: `results/T463-post-t462-h7-e1-restart-router-v0.1.json`
- Sources: H7 handoff, T439, T440, T441, T461, T462, E2 gates, E3 gates, and the taxonomy reference

## Overall verdict: POST_T462_H7_E1_RESTART_ROUTER_BUILT_FULL_BURDEN_ONLY

T463 closes the post-T462 H7/E1 restart surface against minor variations. T461/T462 reopen attempts do not reopen H7; E1, E2, E3, finite-time/catalytic, and ideal/sector packets route to their existing gates; access-loss, name-only, absorber-uncleared, missing-control, cross-repo, external-action, and promotion shortcuts are rejected or blocked. Only a full-burden H7 packet can be admitted as a future review target, with no promotion.

## Restart Requirements

- reverse edge typed as physical_record_deletion
- named physical substrate
- full T462 H7 object frozen before scoring
- T462 absorber cleared
- negative controls declared
- real substrate evidence before evidential reading
- no current T461/T462 minor variation
- no cross-repo truth shortcut
- no public-posture or claim-promotion shortcut
- no non-GitHub external action requirement

## Proposal Evaluation

| proposal | router action | admitted? | gate label | missing requirements |
| --- | --- | --- | --- | --- |
| t461_locality_depth_reopen_attempt | do_not_reopen | no | CLOSED_T461_T462_VARIATION_DO_NOT_REOPEN_H7 | reverse_edge_typed_physical_record_deletion, named_physical_substrate, full_h7_object_frozen, clears_t462_absorber, negative_controls_declared, real_substrate_evidence_present, not_current_t461_t462_variation |
| t462_full_burden_without_real_substrate | do_not_reopen | no | CLOSED_T461_T462_VARIATION_DO_NOT_REOPEN_H7 | real_substrate_evidence_present, not_current_t461_t462_variation |
| new_e1_family_limit_candidate | route_to_T441 | no | ROUTE_TO_T441_E1_FAMILY_LIMIT_GATE | reverse_edge_typed_physical_record_deletion, named_physical_substrate, full_h7_object_frozen, clears_t462_absorber, negative_controls_declared, real_substrate_evidence_present |
| new_e2_hardness_candidate | route_to_T438_T444_T451 | no | ROUTE_TO_T438_T444_T451_E2_GATES | reverse_edge_typed_physical_record_deletion, named_physical_substrate, full_h7_object_frozen, clears_t462_absorber, negative_controls_declared, real_substrate_evidence_present |
| new_e3_exact_no_go_candidate | route_to_T440_T436_T447 | no | ROUTE_TO_T440_T436_T447_E3_RESOURCE_LIFT_GATES | reverse_edge_typed_physical_record_deletion, named_physical_substrate, full_h7_object_frozen, clears_t462_absorber, negative_controls_declared, real_substrate_evidence_present |
| finite_time_catalytic_candidate | route_to_T439 | no | ROUTE_TO_T439_FINITE_TIME_CATALYTIC_GATE | named_physical_substrate, full_h7_object_frozen, clears_t462_absorber, negative_controls_declared, real_substrate_evidence_present |
| ideal_sector_lock_candidate | route_to_T440_T168 | no | ROUTE_TO_T440_T168_IDEAL_OR_SECTOR_ABSORBER | named_physical_substrate, full_h7_object_frozen, clears_t462_absorber, negative_controls_declared, real_substrate_evidence_present |
| access_revocation_reopen_attempt | reject | no | REJECTED_NOT_PHYSICAL_RECORD_DELETION | reverse_edge_typed_physical_record_deletion, named_physical_substrate, full_h7_object_frozen, clears_t462_absorber, negative_controls_declared, real_substrate_evidence_present |
| substrate_name_only_packet | route_to_T462 | no | ROUTE_TO_T462_FULL_OBJECT_CHECK | full_h7_object_frozen, clears_t462_absorber, negative_controls_declared, real_substrate_evidence_present |
| full_object_not_absorber_cleared | route_to_T462 | no | ROUTE_TO_T462_ABSORBER_BEFORE_RESTART | clears_t462_absorber, real_substrate_evidence_present |
| full_object_missing_negative_controls | reject | no | REJECTED_NO_NEGATIVE_CONTROLS | negative_controls_declared, real_substrate_evidence_present |
| cross_repo_support_shortcut | stop | no | BLOCKED_CROSS_REPO_TRUTH_REQUEST | real_substrate_evidence_present, no_cross_repo_truth_request |
| external_substrate_investigation_shortcut | stop | no | BLOCKED_EXTERNAL_ACTION_REQUIRED | real_substrate_evidence_present, no_non_github_external_action_required |
| claim_promotion_shortcut | stop | no | BLOCKED_CLAIM_PROMOTION_REQUEST | real_substrate_evidence_present, no_claim_promotion_request |
| synthetic_full_burden_restart_target | record_synthetic_future_target | yes | ADMITTED_SYNTHETIC_FULL_BURDEN_TARGET_NO_REOPENING | real_substrate_evidence_present |
| future_named_substrate_review_packet | admit_future_h7_review_target | yes | ADMITTED_NAMED_SUBSTRATE_REVIEW_TARGET_NO_PROMOTION | none |

## Route Disposition

- T461/T462 minor variations do not reopen H7.
- E1, E2, and E3 candidates route through existing mode gates first.
- Cross-repo, external-action, public-posture, and claim-promotion shortcuts block.
- Full-burden H7 packets are admitted only as review targets, not evidence or promotion.

## What this earns / does not earn

Earns: a reusable router for post-T462 H7/E1-adjacent work.

Does not earn: H7 promotion, physical-deletion substrate evidence, an E1 theorem, an E2 theorem, an E3 theorem, a thermodynamic-arrow theorem, stochastic-thermodynamic theorem, claim-ledger movement, public posture, or cross-repo support.

Honest ceiling: Routing/admission gate only. T463 does not reopen H7, does not supply physical-deletion substrate evidence, does not prove a thermodynamic-arrow theorem, does not prove an E1/E2/E3 theorem, does not move claim status, and does not authorize public posture.

## Recommended Next

- Use T463 before restarting H7/E1-adjacent work after T462.
- Choose a different lane unless a named real physical-deletion substrate packet clears the full T462 object.
- Route E1, E2, and E3 candidates through their existing mode gates before any H7 reading.
