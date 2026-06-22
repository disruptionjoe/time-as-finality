# T173 Results: Detector Claim-Review Authority Bound

## Partition audits

| Profile | Authorities | Admissible | Governance conflicts | Escrow conflicts | Reason |
| --- | --- | --- | --- | --- | --- |
| `merge_analysis_governor+archive_custodian+control_designer+escrow_custodian+instrument_operator+trust_auditor` | 1 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `analysis_governor`, `instrument_operator`, `control_designer`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer+escrow_custodian+instrument_operator+trust_auditor` | 2 | `False` | `control_designer=archive_custodian` | `instrument_operator`, `control_designer`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__control_designer+escrow_custodian+instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=archive_custodian` | `instrument_operator`, `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer__escrow_custodian+instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `instrument_operator`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer+escrow_custodian__instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `analysis_governor`, `control_designer`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer+escrow_custodian+instrument_operator` | 2 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `analysis_governor`, `instrument_operator`, `control_designer`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+control_designer+escrow_custodian+trust_auditor` | 2 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `analysis_governor`, `control_designer`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer+instrument_operator__escrow_custodian+trust_auditor` | 2 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer+instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer+trust_auditor__escrow_custodian+instrument_operator` | 2 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+escrow_custodian__control_designer+instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+escrow_custodian+instrument_operator__control_designer+trust_auditor` | 2 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `instrument_operator`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+escrow_custodian+instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `instrument_operator`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+escrow_custodian+trust_auditor__control_designer+instrument_operator` | 2 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+instrument_operator__control_designer+escrow_custodian+trust_auditor` | 2 | `False` | `analysis_governor=archive_custodian` | `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+instrument_operator+trust_auditor__control_designer+escrow_custodian` | 2 | `False` | `analysis_governor=archive_custodian` | `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+trust_auditor__control_designer+escrow_custodian+instrument_operator` | 2 | `False` | `analysis_governor=archive_custodian` | `instrument_operator`, `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__archive_custodian+escrow_custodian+instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=control_designer` | `instrument_operator`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+escrow_custodian__archive_custodian+instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+escrow_custodian+instrument_operator__archive_custodian+trust_auditor` | 2 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `instrument_operator`, `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+escrow_custodian+instrument_operator+trust_auditor` | 2 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `instrument_operator`, `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+escrow_custodian+trust_auditor__archive_custodian+instrument_operator` | 2 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+instrument_operator__archive_custodian+escrow_custodian+trust_auditor` | 2 | `False` | `analysis_governor=control_designer` | `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+instrument_operator+trust_auditor__archive_custodian+escrow_custodian` | 2 | `False` | `analysis_governor=control_designer` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+trust_auditor__archive_custodian+escrow_custodian+instrument_operator` | 2 | `False` | `analysis_governor=control_designer` | `instrument_operator`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+control_designer+instrument_operator+trust_auditor` | 2 | `False` | `control_designer=archive_custodian` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+instrument_operator__archive_custodian+control_designer+trust_auditor` | 2 | `False` | `control_designer=archive_custodian` | `analysis_governor`, `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+instrument_operator+trust_auditor__archive_custodian+control_designer` | 2 | `False` | `control_designer=archive_custodian` | `analysis_governor`, `instrument_operator`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+trust_auditor__archive_custodian+control_designer+instrument_operator` | 2 | `False` | `control_designer=archive_custodian` | `analysis_governor`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__archive_custodian+control_designer+escrow_custodian+trust_auditor` | 2 | `False` | `control_designer=archive_custodian` | `control_designer`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator+trust_auditor__archive_custodian+control_designer+escrow_custodian` | 2 | `False` | `control_designer=archive_custodian` | `control_designer`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+control_designer+escrow_custodian+instrument_operator` | 2 | `False` | `control_designer=archive_custodian` | `instrument_operator`, `control_designer`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_control_designer+escrow_custodian+instrument_operator+trust_auditor` | 3 | `False` | `none` | `instrument_operator`, `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer__escrow_custodian+instrument_operator+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `instrument_operator`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer+escrow_custodian__instrument_operator+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `control_designer`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer+escrow_custodian+instrument_operator` | 3 | `False` | `control_designer=archive_custodian` | `instrument_operator`, `control_designer`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_archive_custodian+control_designer+escrow_custodian+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `control_designer`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer+instrument_operator__escrow_custodian+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer+instrument_operator+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer+trust_auditor__escrow_custodian+instrument_operator` | 3 | `False` | `control_designer=archive_custodian` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_archive_custodian+escrow_custodian__control_designer+instrument_operator+trust_auditor` | 3 | `False` | `none` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_archive_custodian+escrow_custodian+instrument_operator__control_designer+trust_auditor` | 3 | `False` | `none` | `instrument_operator`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_archive_custodian+escrow_custodian+instrument_operator+trust_auditor` | 3 | `False` | `none` | `instrument_operator`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+escrow_custodian+trust_auditor__control_designer+instrument_operator` | 3 | `False` | `none` | `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+instrument_operator__control_designer+escrow_custodian+trust_auditor` | 3 | `False` | `none` | `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+instrument_operator+trust_auditor__control_designer+escrow_custodian` | 3 | `False` | `none` | `control_designer` | `trust_auditor_not_independent` |
| `merge_archive_custodian+trust_auditor__control_designer+escrow_custodian+instrument_operator` | 3 | `False` | `none` | `instrument_operator`, `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__escrow_custodian+instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `instrument_operator`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__control_designer+escrow_custodian__instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__control_designer+escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=archive_custodian` | `instrument_operator`, `control_designer` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian__control_designer+escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__control_designer+instrument_operator__escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__control_designer+instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__control_designer+trust_auditor__escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=archive_custodian` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer__instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer__escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `instrument_operator` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+control_designer__escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer+escrow_custodian` | 3 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `analysis_governor`, `control_designer`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+control_designer+instrument_operator` | 3 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+control_designer+trust_auditor` | 3 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+escrow_custodian__instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+escrow_custodian__control_designer+instrument_operator` | 3 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+escrow_custodian__control_designer+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `instrument_operator`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+instrument_operator__escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+instrument_operator__control_designer+escrow_custodian` | 3 | `False` | `analysis_governor=archive_custodian` | `control_designer` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+instrument_operator__control_designer+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+trust_auditor__escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=archive_custodian` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+trust_auditor__control_designer+escrow_custodian` | 3 | `False` | `analysis_governor=archive_custodian` | `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+trust_auditor__control_designer+instrument_operator` | 3 | `False` | `analysis_governor=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__escrow_custodian+instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `instrument_operator`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__archive_custodian+escrow_custodian__instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__archive_custodian+escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=control_designer` | `instrument_operator`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer__archive_custodian+escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__archive_custodian+instrument_operator__escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__archive_custodian+instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__archive_custodian+trust_auditor__escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=control_designer` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+escrow_custodian__instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+escrow_custodian__archive_custodian+instrument_operator` | 3 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `control_designer` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer+escrow_custodian__archive_custodian+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `instrument_operator`, `control_designer` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer+escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+instrument_operator__escrow_custodian+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+instrument_operator__archive_custodian+escrow_custodian` | 3 | `False` | `analysis_governor=control_designer` | `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer+instrument_operator__archive_custodian+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+instrument_operator+trust_auditor` | 3 | `False` | `analysis_governor=control_designer` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+trust_auditor__escrow_custodian+instrument_operator` | 3 | `False` | `analysis_governor=control_designer` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+trust_auditor__archive_custodian+escrow_custodian` | 3 | `False` | `analysis_governor=control_designer` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+trust_auditor__archive_custodian+instrument_operator` | 3 | `False` | `analysis_governor=control_designer` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__control_designer+instrument_operator+trust_auditor` | 3 | `False` | `none` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+control_designer__instrument_operator+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+control_designer+instrument_operator` | 3 | `False` | `control_designer=archive_custodian` | `analysis_governor` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+control_designer+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+instrument_operator__control_designer+trust_auditor` | 3 | `False` | `none` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+instrument_operator+trust_auditor` | 3 | `False` | `none` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+trust_auditor__control_designer+instrument_operator` | 3 | `False` | `none` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+instrument_operator__control_designer+trust_auditor` | 3 | `False` | `none` | `analysis_governor`, `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+instrument_operator__archive_custodian+control_designer` | 3 | `False` | `control_designer=archive_custodian` | `analysis_governor`, `instrument_operator` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+escrow_custodian+instrument_operator__archive_custodian+trust_auditor` | 3 | `False` | `none` | `analysis_governor`, `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+instrument_operator+trust_auditor` | 3 | `False` | `none` | `analysis_governor`, `instrument_operator`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+trust_auditor__control_designer+instrument_operator` | 3 | `False` | `none` | `analysis_governor`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+trust_auditor__archive_custodian+control_designer` | 3 | `False` | `control_designer=archive_custodian` | `analysis_governor`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+trust_auditor__archive_custodian+instrument_operator` | 3 | `False` | `none` | `analysis_governor`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__control_designer+escrow_custodian+trust_auditor` | 3 | `False` | `none` | `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__archive_custodian+control_designer__escrow_custodian+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__archive_custodian+control_designer+escrow_custodian` | 3 | `False` | `control_designer=archive_custodian` | `control_designer`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+instrument_operator__archive_custodian+control_designer+trust_auditor` | 3 | `False` | `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__archive_custodian+escrow_custodian__control_designer+trust_auditor` | 3 | `False` | `none` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__archive_custodian+escrow_custodian+trust_auditor` | 3 | `False` | `none` | `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__archive_custodian+trust_auditor__control_designer+escrow_custodian` | 3 | `False` | `none` | `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator+trust_auditor__control_designer+escrow_custodian` | 3 | `False` | `none` | `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator+trust_auditor__archive_custodian+control_designer` | 3 | `False` | `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator+trust_auditor__archive_custodian+escrow_custodian` | 3 | `False` | `none` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__control_designer+escrow_custodian+instrument_operator` | 3 | `False` | `none` | `instrument_operator`, `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+control_designer__escrow_custodian+instrument_operator` | 3 | `False` | `control_designer=archive_custodian` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+control_designer+escrow_custodian` | 3 | `False` | `control_designer=archive_custodian` | `control_designer`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+control_designer+instrument_operator` | 3 | `False` | `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+escrow_custodian__control_designer+instrument_operator` | 3 | `False` | `none` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+escrow_custodian+instrument_operator` | 3 | `False` | `none` | `instrument_operator`, `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+instrument_operator__control_designer+escrow_custodian` | 3 | `False` | `none` | `control_designer` | `trust_auditor_not_independent` |
| `merge_escrow_custodian+instrument_operator+trust_auditor` | 4 | `False` | `none` | `instrument_operator`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_control_designer+escrow_custodian__instrument_operator+trust_auditor` | 4 | `False` | `none` | `control_designer` | `trust_auditor_not_independent` |
| `merge_control_designer+escrow_custodian+instrument_operator` | 4 | `False` | `none` | `instrument_operator`, `control_designer` | `escrow_not_independent` |
| `merge_control_designer+escrow_custodian+trust_auditor` | 4 | `False` | `none` | `control_designer`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_control_designer+instrument_operator__escrow_custodian+trust_auditor` | 4 | `False` | `none` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_control_designer+instrument_operator+trust_auditor` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_control_designer+trust_auditor__escrow_custodian+instrument_operator` | 4 | `False` | `none` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer__instrument_operator+trust_auditor` | 4 | `False` | `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer__escrow_custodian+instrument_operator` | 4 | `False` | `control_designer=archive_custodian` | `instrument_operator` | `governance_control_archive_role_merge` |
| `merge_archive_custodian+control_designer__escrow_custodian+trust_auditor` | 4 | `False` | `control_designer=archive_custodian` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer+escrow_custodian` | 4 | `False` | `control_designer=archive_custodian` | `control_designer`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_archive_custodian+control_designer+instrument_operator` | 4 | `False` | `control_designer=archive_custodian` | `none` | `governance_control_archive_role_merge` |
| `merge_archive_custodian+control_designer+trust_auditor` | 4 | `False` | `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_archive_custodian+escrow_custodian__instrument_operator+trust_auditor` | 4 | `False` | `none` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_archive_custodian+escrow_custodian__control_designer+instrument_operator` | 4 | `False` | `none` | `archive_custodian` | `escrow_not_independent` |
| `merge_archive_custodian+escrow_custodian__control_designer+trust_auditor` | 4 | `False` | `none` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_archive_custodian+escrow_custodian+instrument_operator` | 4 | `False` | `none` | `instrument_operator`, `archive_custodian` | `escrow_not_independent` |
| `merge_archive_custodian+escrow_custodian+trust_auditor` | 4 | `False` | `none` | `archive_custodian`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+instrument_operator__escrow_custodian+trust_auditor` | 4 | `False` | `none` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_archive_custodian+instrument_operator__control_designer+escrow_custodian` | 4 | `False` | `none` | `control_designer` | `escrow_not_independent` |
| `merge_archive_custodian+instrument_operator__control_designer+trust_auditor` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_archive_custodian+instrument_operator+trust_auditor` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_archive_custodian+trust_auditor__escrow_custodian+instrument_operator` | 4 | `False` | `none` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_archive_custodian+trust_auditor__control_designer+escrow_custodian` | 4 | `False` | `none` | `control_designer` | `trust_auditor_not_independent` |
| `merge_archive_custodian+trust_auditor__control_designer+instrument_operator` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__instrument_operator+trust_auditor` | 4 | `False` | `analysis_governor=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__escrow_custodian+instrument_operator` | 4 | `False` | `analysis_governor=archive_custodian` | `instrument_operator` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian__escrow_custodian+trust_auditor` | 4 | `False` | `analysis_governor=archive_custodian` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian__control_designer+escrow_custodian` | 4 | `False` | `analysis_governor=archive_custodian` | `control_designer` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian__control_designer+instrument_operator` | 4 | `False` | `analysis_governor=archive_custodian` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian__control_designer+trust_auditor` | 4 | `False` | `analysis_governor=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian+control_designer` | 4 | `False` | `analysis_governor=control_designer`, `analysis_governor=archive_custodian`, `control_designer=archive_custodian` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+escrow_custodian` | 4 | `False` | `analysis_governor=archive_custodian` | `analysis_governor`, `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+instrument_operator` | 4 | `False` | `analysis_governor=archive_custodian` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+archive_custodian+trust_auditor` | 4 | `False` | `analysis_governor=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__instrument_operator+trust_auditor` | 4 | `False` | `analysis_governor=control_designer` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__escrow_custodian+instrument_operator` | 4 | `False` | `analysis_governor=control_designer` | `instrument_operator` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer__escrow_custodian+trust_auditor` | 4 | `False` | `analysis_governor=control_designer` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer__archive_custodian+escrow_custodian` | 4 | `False` | `analysis_governor=control_designer` | `archive_custodian` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer__archive_custodian+instrument_operator` | 4 | `False` | `analysis_governor=control_designer` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer__archive_custodian+trust_auditor` | 4 | `False` | `analysis_governor=control_designer` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+control_designer+escrow_custodian` | 4 | `False` | `analysis_governor=control_designer` | `analysis_governor`, `control_designer` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer+instrument_operator` | 4 | `False` | `analysis_governor=control_designer` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer+trust_auditor` | 4 | `False` | `analysis_governor=control_designer` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__instrument_operator+trust_auditor` | 4 | `False` | `none` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__control_designer+instrument_operator` | 4 | `False` | `none` | `analysis_governor` | `escrow_not_independent` |
| `merge_analysis_governor+escrow_custodian__control_designer+trust_auditor` | 4 | `False` | `none` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+control_designer` | 4 | `False` | `control_designer=archive_custodian` | `analysis_governor` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+instrument_operator` | 4 | `False` | `none` | `analysis_governor` | `escrow_not_independent` |
| `merge_analysis_governor+escrow_custodian__archive_custodian+trust_auditor` | 4 | `False` | `none` | `analysis_governor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+escrow_custodian+instrument_operator` | 4 | `False` | `none` | `analysis_governor`, `instrument_operator` | `escrow_not_independent` |
| `merge_analysis_governor+escrow_custodian+trust_auditor` | 4 | `False` | `none` | `analysis_governor`, `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__escrow_custodian+trust_auditor` | 4 | `False` | `none` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__control_designer+escrow_custodian` | 4 | `False` | `none` | `control_designer` | `escrow_not_independent` |
| `merge_analysis_governor+instrument_operator__control_designer+trust_auditor` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator__archive_custodian+control_designer` | 4 | `False` | `control_designer=archive_custodian` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+instrument_operator__archive_custodian+escrow_custodian` | 4 | `False` | `none` | `archive_custodian` | `escrow_not_independent` |
| `merge_analysis_governor+instrument_operator__archive_custodian+trust_auditor` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+instrument_operator+trust_auditor` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__escrow_custodian+instrument_operator` | 4 | `False` | `none` | `instrument_operator` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__control_designer+escrow_custodian` | 4 | `False` | `none` | `control_designer` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__control_designer+instrument_operator` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+control_designer` | 4 | `False` | `control_designer=archive_custodian` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+escrow_custodian` | 4 | `False` | `none` | `archive_custodian` | `trust_auditor_not_independent` |
| `merge_analysis_governor+trust_auditor__archive_custodian+instrument_operator` | 4 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_instrument_operator+trust_auditor` | 5 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_escrow_custodian+instrument_operator` | 5 | `False` | `none` | `instrument_operator` | `escrow_not_independent` |
| `merge_escrow_custodian+trust_auditor` | 5 | `False` | `none` | `trust_auditor` | `trust_auditor_not_independent` |
| `merge_control_designer+escrow_custodian` | 5 | `False` | `none` | `control_designer` | `escrow_not_independent` |
| `merge_control_designer+instrument_operator` | 5 | `True` | `none` | `none` | `conflict_free_claim_review_partition` |
| `merge_control_designer+trust_auditor` | 5 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_archive_custodian+control_designer` | 5 | `False` | `control_designer=archive_custodian` | `none` | `governance_control_archive_role_merge` |
| `merge_archive_custodian+escrow_custodian` | 5 | `False` | `none` | `archive_custodian` | `escrow_not_independent` |
| `merge_archive_custodian+instrument_operator` | 5 | `True` | `none` | `none` | `conflict_free_claim_review_partition` |
| `merge_archive_custodian+trust_auditor` | 5 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `merge_analysis_governor+archive_custodian` | 5 | `False` | `analysis_governor=archive_custodian` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+control_designer` | 5 | `False` | `analysis_governor=control_designer` | `none` | `governance_control_archive_role_merge` |
| `merge_analysis_governor+escrow_custodian` | 5 | `False` | `none` | `analysis_governor` | `escrow_not_independent` |
| `merge_analysis_governor+instrument_operator` | 5 | `True` | `none` | `none` | `conflict_free_claim_review_partition` |
| `merge_analysis_governor+trust_auditor` | 5 | `False` | `none` | `none` | `trust_auditor_not_independent` |
| `fully_separated_five_domain_profile` | 6 | `True` | `none` | `none` | `conflict_free_claim_review_partition` |

## Strongest claim

T173 upgrades the T100 lower bound for the only surviving T171 claim-review route. Once full reviewable rows with independent escrow are treated as a real authority burden, no four-domain profile survives. The exact minimum becomes five authority domains, with only three minimal merge classes: instrument operation merged with exactly one of governance, control design, or archive custody.

## What this improved

T173 removes another ambiguity from Q1B. The repo no longer has to talk loosely about a reviewable-row federation. It can state the exact operational lower bound for the surviving claim-review path.

## What this weakened

This weakens Q1B again. T100's four-domain lower bound still covers weaker pre-data packet or scaffold talk, but it is no longer enough for the lone T171 live route. Any claim-review deployment that lacks a separate escrow authority should be rejected before detector evidence is discussed.

## Falsification condition

T173 fails if T171-level independent escrow can be implemented without a separate escrow authority while preserving outside challenge rights, or if a four-domain claim-review partition survives once escrow independence is stated operationally.

## Q1B update

Q1B remains externally blocked. For the only surviving T171 claim-review route, the detector packet now has a hard five-domain lower bound: governance, control, archive, trust audit, and independent escrow must remain conflict-free, with instrument operation mergeable into only one of governance, control, or archive.

## Claim ledger update

Add T173 to Q1B: the T171 reviewable-row route is stricter than the older T100 packet. Once independent escrow is included, no four-domain claim-review profile survives; the exact minimum is five authority domains.

## Open blocker

The repo still has no named workflow that can supply both a T161-valid control-root map and the extra independent escrow authority demanded by T171 claim review.

## Recommended next

Update the Q1B deployment handoff to require a named escrow authority and then map one realistic collaboration onto one of the three surviving five-domain claim-review profiles. If none fits, demote Q1B below the active frontier.
