# T161 Results: Detector Control-Root Independence

## Workflow audits

| Profile | Nominal profile | Effective profile | Nominal count | Effective count | Effective admissible | Shared critical roots | Ignored noncritical roots |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `four_domain_distinct_critical_roots` | `merge_analysis_governor+instrument_operator` | `merge_analysis_governor+instrument_operator` | `4` | `4` | `True` | `none` | `none` |
| `five_domain_shared_archive_audit_hsm` | `fully_separated_five_domain_profile` | `merge_archive_custodian+trust_auditor` | `5` | `4` | `False` | `root_shared_archive_audit_hsm:archive_custodian+trust_auditor:archive_write+audit_attestation` | `none` |
| `five_domain_shared_governance_archive_release_root` | `fully_separated_five_domain_profile` | `merge_analysis_governor+archive_custodian` | `5` | `4` | `False` | `root_shared_release_gate:analysis_governor+archive_custodian:manifest_registration+publication_release` | `none` |
| `five_domain_shared_noncritical_dashboard` | `fully_separated_five_domain_profile` | `fully_separated_five_domain_profile` | `5` | `5` | `True` | `none` | `root_shared_dashboard:analysis_governor+trust_auditor:dashboard_observability` |

## Strongest claim

Nominal authority labels are insufficient for Q1B. A T100/T138-valid role partition is null if critical control roots are shared, because the effective authority partition collapses back into self-certifying governance, archive, or audit control.

## What this improved

T161 converts an implicit governance loophole into an executable screen. Detector proposals can now be rejected before data if their archive, audit, publication, manifest, or revocation control roots quietly merge nominally separate authorities.

## What this weakened

This weakens Q1B again. A workflow does not clear the detector handoff merely by naming four or five roles; it must also show that critical packet-control roots do not collapse those roles in practice.

## Falsification condition

T161 fails if shared critical control roots can coexist with an honest detector packet while preserving independent archive and trust audit powers, or if only noncritical shared services are sufficient to collapse the effective authority partition.

## Q1B update

Q1B remains externally blocked. A future detector deployment must freeze not only a T100-compatible nominal authority partition but also evidence that manifest registration, archive mutation, audit attestation, publication release, and revocation roots are not shared in a way that collapses the effective partition.

## Claim ledger update

Add T161 to Q1B: nominal four- or five-domain staffing is null when critical control roots are shared. The operative object is the effective authority partition after quotienting by shared critical packet-control roots.

## Open blocker

No named detector workflow in the repo currently exposes its critical control-root map well enough to prove that nominal authority separation is operationally real.

## Recommended next

Extend the Q1B handoff so a proposed deployment must disclose its manifest-registration, archive-write, audit-attestation, publication, and revocation control roots alongside the nominal authority roles.
