# T98 Results: Detector Operator-Handoff Audit

## Staffing profiles

| Profile | Verdict | Distinct operators | Independent trust auditor | Failure reasons | Next step |
| --- | --- | --- | --- | --- | --- |
| independent_five_domain_profile | admissible_predata_handoff_profile | 5 | True | none | freeze_t97_packet_with_named_operator_handoffs |
| four_domain_cross_handoff_profile | admissible_predata_handoff_profile | 4 | True | none | freeze_t97_packet_with_named_operator_handoffs |
| three_person_small_lab_profile | inadmissible_due_role_conflicts | 3 | False | trust_auditor_not_independent, governance_control_archive_role_merge | split_conflicting_authority_domains_before_freeze |
| two_person_pi_student_profile | inadmissible_due_role_conflicts | 2 | False | trust_auditor_not_independent, governance_control_archive_role_merge | split_conflicting_authority_domains_before_freeze |

## Authority domains

| Domain | T97-owned tables |
| --- | --- |
| analysis_governor | preregistration_manifest, demotion_decision_log |
| instrument_operator | event_time_tag_stream |
| control_designer | control_pair_manifest, tag_ambiguity_challenge_log, perturbation_trial_log |
| archive_custodian | signature_verification_log, ancestry_dag_edge_export |
| trust_auditor | trust_boundary_audit_log |

## Strongest claim

The surviving detector-side Q1 route is operationally admissible only if the T97 packet is carried by at least four non-conflicting authority domains, including an independent trust auditor. Common two- and three-person role merges collapse the route into self-certification before any detector evidence exists.

## What this improved

T98 converts T97's vague 'operator handoff checks' into an executable staffing criterion. The detector route can now fail before data if the same authority both defines controls and audits them, or both owns the archive and sets demotion policy.

## What this weakened

This weakens detector-side Q1 again. The live bottleneck is not timing hardware or even schema design; it is conflict-free role separation. Small labs with merged governance, archive, and audit roles collapse back into self-certification and should not treat a filled packet as independent support.

## Falsification condition

Demote the detector branch if a realistic deployment cannot name at least four non-conflicting authority domains with an independent trust auditor before the first event, or if merged governance/control/archive roles are allowed to certify the packet without independent review.

## Q1 update

Q1 remains partially supported only as a detector-record admissibility protocol. T98 adds that even the T97 dry-run packet counts only if its preregistration, control design, archive custody, instrument operation, and trust audit are separated enough to prevent self-certification.

## Claim ledger update

Add T98 to Q1 as an operational narrowing: detector-side Q1 now requires at least four non-conflicting authority domains, including an independent trust auditor. Common two- and three-person role merges should demote the route before any event-level evidence is scored.

## Open blocker

No concrete lab deployment in the repo yet names independent operators for the T97 packet. The live blocker is organizational: identify a realistic authority split that survives trust-audit and governance-conflict checks.

## Recommended next

Instantiate one named lab staffing plan against the T97 packet with real operator roles, signed handoff points, and explicit external or functionally independent trust auditing. If no such plan is realistic, demote detector provenance below the active Q1 frontier.
