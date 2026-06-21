# T100 Results: Detector Authority-Domain Bound

## Partition audit

| Profile | Authorities | Admissible | Trust auditor independent | Governance conflicts | Reason |
| --- | --- | --- | --- | --- | --- |
| merge_analysis_governor+archive_custodian+control_designer+instrument_operator+trust_auditor | 1 | False | False | analysis_governor=control_designer, analysis_governor=archive_custodian, control_designer=archive_custodian | trust_auditor_not_independent |
| merge_archive_custodian+control_designer+instrument_operator+trust_auditor | 2 | False | False | control_designer=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian__control_designer+instrument_operator+trust_auditor | 2 | False | False | analysis_governor=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian+control_designer__instrument_operator+trust_auditor | 2 | False | False | analysis_governor=control_designer, analysis_governor=archive_custodian, control_designer=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian+control_designer+instrument_operator | 2 | False | True | analysis_governor=control_designer, analysis_governor=archive_custodian, control_designer=archive_custodian | governance_control_archive_role_merge |
| merge_analysis_governor+archive_custodian+control_designer+trust_auditor | 2 | False | False | analysis_governor=control_designer, analysis_governor=archive_custodian, control_designer=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian+instrument_operator__control_designer+trust_auditor | 2 | False | False | analysis_governor=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian+instrument_operator+trust_auditor | 2 | False | False | analysis_governor=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian+trust_auditor__control_designer+instrument_operator | 2 | False | False | analysis_governor=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+control_designer__archive_custodian+instrument_operator+trust_auditor | 2 | False | False | analysis_governor=control_designer | trust_auditor_not_independent |
| merge_analysis_governor+control_designer+instrument_operator__archive_custodian+trust_auditor | 2 | False | False | analysis_governor=control_designer | trust_auditor_not_independent |
| merge_analysis_governor+control_designer+instrument_operator+trust_auditor | 2 | False | False | analysis_governor=control_designer | trust_auditor_not_independent |
| merge_analysis_governor+control_designer+trust_auditor__archive_custodian+instrument_operator | 2 | False | False | analysis_governor=control_designer | trust_auditor_not_independent |
| merge_analysis_governor+instrument_operator__archive_custodian+control_designer+trust_auditor | 2 | False | False | control_designer=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+instrument_operator+trust_auditor__archive_custodian+control_designer | 2 | False | False | control_designer=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+trust_auditor__archive_custodian+control_designer+instrument_operator | 2 | False | False | control_designer=archive_custodian | trust_auditor_not_independent |
| merge_control_designer+instrument_operator+trust_auditor | 3 | False | False | none | trust_auditor_not_independent |
| merge_archive_custodian+control_designer__instrument_operator+trust_auditor | 3 | False | False | control_designer=archive_custodian | trust_auditor_not_independent |
| merge_archive_custodian+control_designer+instrument_operator | 3 | False | True | control_designer=archive_custodian | governance_control_archive_role_merge |
| merge_archive_custodian+control_designer+trust_auditor | 3 | False | False | control_designer=archive_custodian | trust_auditor_not_independent |
| merge_archive_custodian+instrument_operator__control_designer+trust_auditor | 3 | False | False | none | trust_auditor_not_independent |
| merge_archive_custodian+instrument_operator+trust_auditor | 3 | False | False | none | trust_auditor_not_independent |
| merge_archive_custodian+trust_auditor__control_designer+instrument_operator | 3 | False | False | none | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian__instrument_operator+trust_auditor | 3 | False | False | analysis_governor=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian__control_designer+instrument_operator | 3 | False | True | analysis_governor=archive_custodian | governance_control_archive_role_merge |
| merge_analysis_governor+archive_custodian__control_designer+trust_auditor | 3 | False | False | analysis_governor=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian+control_designer | 3 | False | True | analysis_governor=control_designer, analysis_governor=archive_custodian, control_designer=archive_custodian | governance_control_archive_role_merge |
| merge_analysis_governor+archive_custodian+instrument_operator | 3 | False | True | analysis_governor=archive_custodian | governance_control_archive_role_merge |
| merge_analysis_governor+archive_custodian+trust_auditor | 3 | False | False | analysis_governor=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+control_designer__instrument_operator+trust_auditor | 3 | False | False | analysis_governor=control_designer | trust_auditor_not_independent |
| merge_analysis_governor+control_designer__archive_custodian+instrument_operator | 3 | False | True | analysis_governor=control_designer | governance_control_archive_role_merge |
| merge_analysis_governor+control_designer__archive_custodian+trust_auditor | 3 | False | False | analysis_governor=control_designer | trust_auditor_not_independent |
| merge_analysis_governor+control_designer+instrument_operator | 3 | False | True | analysis_governor=control_designer | governance_control_archive_role_merge |
| merge_analysis_governor+control_designer+trust_auditor | 3 | False | False | analysis_governor=control_designer | trust_auditor_not_independent |
| merge_analysis_governor+instrument_operator__control_designer+trust_auditor | 3 | False | False | none | trust_auditor_not_independent |
| merge_analysis_governor+instrument_operator__archive_custodian+control_designer | 3 | False | True | control_designer=archive_custodian | governance_control_archive_role_merge |
| merge_analysis_governor+instrument_operator__archive_custodian+trust_auditor | 3 | False | False | none | trust_auditor_not_independent |
| merge_analysis_governor+instrument_operator+trust_auditor | 3 | False | False | none | trust_auditor_not_independent |
| merge_analysis_governor+trust_auditor__control_designer+instrument_operator | 3 | False | False | none | trust_auditor_not_independent |
| merge_analysis_governor+trust_auditor__archive_custodian+control_designer | 3 | False | False | control_designer=archive_custodian | trust_auditor_not_independent |
| merge_analysis_governor+trust_auditor__archive_custodian+instrument_operator | 3 | False | False | none | trust_auditor_not_independent |
| merge_instrument_operator+trust_auditor | 4 | False | False | none | trust_auditor_not_independent |
| merge_control_designer+instrument_operator | 4 | True | True | none | conflict_free_partition |
| merge_control_designer+trust_auditor | 4 | False | False | none | trust_auditor_not_independent |
| merge_archive_custodian+control_designer | 4 | False | True | control_designer=archive_custodian | governance_control_archive_role_merge |
| merge_archive_custodian+instrument_operator | 4 | True | True | none | conflict_free_partition |
| merge_archive_custodian+trust_auditor | 4 | False | False | none | trust_auditor_not_independent |
| merge_analysis_governor+archive_custodian | 4 | False | True | analysis_governor=archive_custodian | governance_control_archive_role_merge |
| merge_analysis_governor+control_designer | 4 | False | True | analysis_governor=control_designer | governance_control_archive_role_merge |
| merge_analysis_governor+instrument_operator | 4 | True | True | none | conflict_free_partition |
| merge_analysis_governor+trust_auditor | 4 | False | False | none | trust_auditor_not_independent |
| fully_separated_five_domain_profile | 5 | True | True | none | conflict_free_partition |

## Summary

- Minimum admissible authority count: 4
- No three-domain profile survives: True
- Minimal surviving profiles: merge_control_designer+instrument_operator, merge_archive_custodian+instrument_operator, merge_analysis_governor+instrument_operator

## Strongest claim

T100 proves that the current T97/T98 detector route requires at least four non-conflicting authority domains. The lower bound is exact: there are exactly three admissible four-domain merge classes, each merging instrument operation with exactly one of governance, control design, or archive custody while keeping trust auditing separate.

## What this improved

T100 replaces T98's example-level staffing judgment with a finite combinatorial audit over every partition of the five T97 authority domains. The detector branch now has an exact operational lower bound rather than a suggestive staffing story.

## What this weakened

This narrows detector-side Q1 again. Any two- or three-person deployment is ruled out by structure, not pessimism: the trust auditor must be independent, and governance, control design, and archive custody cannot collapse into one authority. Small-lab future-deployment narratives should therefore be treated as null unless they change the packet itself.

## Falsification condition

T100 fails if the T97 packet can be redefined so that an admissible partition with three or fewer authority domains exists without allowing trust self-audit or governance/control/archive self-certification, or if a real deployment shows that one of T98's current separation constraints is unnecessary.

## Q1 update

Q1 remains partially supported only as a detector-record admissibility protocol. T100 strengthens the operational narrowing: under the current packet, detector-side Q1 has a hard four-authority lower bound and should be demoted for any proposed deployment that cannot meet it pre-data.

## Claim ledger update

Add T100 to Q1 as an exact combinatorial obstruction: the current T97/T98 packet admits no admissible staffing profile with fewer than four authority domains, and the only minimal surviving profiles merge instrument operation with exactly one other non-auditing role.

## Open blocker

The repo still lacks a named real lab organization that fits one of T100's three minimal four-domain patterns while also freezing the T97 packet before first event.

## Recommended next

Map one concrete lab onto each of the three minimal four-domain profiles and reject the detector route unless at least one can be staffed, signed, and frozen pre-data without hidden role merges.
