# T31 Test Specification: PO1 Admissibility Conditions

## Purpose

T31 refines PO1 from a broad pattern into a constrained theorem schema.
It identifies the necessary and sufficient conditions a projection must
satisfy before obstruction behavior counts as a PO1 instance, and
reclassifies all cases from T27, T28, T29, and T30 under the rules.

## Seven admissibility conditions

| Condition | Field | Requirement |
| --- | --- | --- |
| AC1 | richer_valid | Richer D1RestrictionSystem satisfies all T26 axioms |
| AC2 | restricted_valid | Restricted D1RestrictionSystem satisfies all T26 axioms |
| AC3 | projection_definable | Site map is total (site_map_total=True) |
| AC4 | local_compat | Restricted system has all patches locally satisfiable |
| AC5 | structure_forgotten | Projection forgets named structure AND loses measurable profile data |
| AC6 | restricted_obstructed | Restricted system has a gluing obstruction (global_witness_count=0) |
| AC7 | richer_unobstructed | Richer system has a global section (obstruction_detected=False) |

A case is a **positive PO1 instance** if and only if all seven hold.

## Failure verdicts (priority order)

1. AC1 or AC2 fail: `non_admissible_system_invalid`
2. AC3 fails: `boundary_non_definable` (category change)
3. AC7 fails: `non_admissible_shared_obstruction`
4. AC6 fails: `non_admissible_no_new_obstruction`
5. AC4 fails: `non_admissible_trivial_obstruction`
6. AC5 fails: `non_admissible_no_forgotten_structure`

## Acceptance criteria

1. At least one positive admissible case (all 7 conditions satisfied).
2. At least one non-admissible case.
3. At least one boundary case.
4. Reclassification covers T27 and T30 cases explicitly.
5. Recommendation on PO1 status is produced.

## Expected case verdicts

| Case | Source | AC1 | AC2 | AC3 | AC4 | AC5 | AC6 | AC7 | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| witten_1981 | T27 | T | T | T | T | T | T | T | fully_admissible |
| nielsen_ninomiya | T27 | T | T | T | T | T | T | T | fully_admissible |
| distler_garibaldi | T27 | T | T | F | T | F | T | T | boundary_non_definable |
| cap_theorem | T28 | T | T | T | T | T | T | T | fully_admissible |
| synthetic_lossy_no_obstruction | T29 | T | T | T | T | F | F | T | non_admissible_no_new_obstruction |
| synthetic_shared_obstruction | T29 | T | T | T | T | F | T | F | non_admissible_shared_obstruction |
| git_semantic_merge | T30 | T | T | T | T | T | T | T | fully_admissible |
| database_expand_contract | T30 | T | T | T | T | T | F | T | non_admissible_no_new_obstruction |
| access_control_inheritance | T30 | T | T | T | T | T | T | F | non_admissible_shared_obstruction |
| type_system_macro_expansion | T30 | T | T | F | T | F | F | T | boundary_non_definable |

Summary: 4 positive, 2 boundary, 4 non-admissible.

## Test classes

| Class | Key assertions |
| --- | --- |
| `AdmissibilityConditionSchemaTests` | 7 conditions defined; IDs are AC1-AC7 |
| `PositiveAdmissibleCasesTests` | Witten, NN, CAP, Git merge are fully_admissible; all 7 conditions pass |
| `BoundaryCasesTests` | DG and type-system-macro are boundary_non_definable; AC3 fails |
| `NonAdmissibleSharedObstructionTests` | Synthetic shared and ACL are non_admissible_shared_obstruction; AC7 fails |
| `NonAdmissibleNoObstructionTests` | Synthetic lossy and database are non_admissible_no_new_obstruction; AC6 fails |
| `AuditResultTests` | 10 cases; 4 positive; 2 boundary; 4 non-admissible; weakest=5 conditions; recommended=7 |

## Weakest vs. recommended PO1

The **weakest correct PO1** uses 5 conditions: AC1, AC2, AC3, AC6, AC7.
These 5 correctly classify all 10 tested cases.

The **recommended PO1** adds AC4 and AC5:
- AC4 guards against trivially-broken restricted systems
- AC5 guards against lossless or unlabeled projections

No current case fails on AC4 or AC5 in isolation; both are guards for future
applications, not corrections to current evidence.

## Artifacts

- `models/po1_admissibility_conditions.py` — conditions and audit runner
- `models/run_t31.py` — JSON runner
- `tests/test_po1_admissibility_conditions.py` — test suite
- `results/po1-admissibility-conditions-v0.1.json` — machine-readable results
- `results/po1-admissibility-conditions-v0.1-results.md` — results summary
- `TECHNICAL-REPORT-po1-admissibility-conditions-v0.1.md` — full report
- `claims/PO1-projection-obstruction-schema.md` — updated claim
