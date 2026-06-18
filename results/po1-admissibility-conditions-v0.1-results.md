# T31 Results: PO1 Admissibility Conditions

Generated from `run_t31_admissibility_audit()`.

## Summary

10 cases reclassified across T27, T28, T29, and T30.

| Verdict | Count | Cases |
| --- | --- | --- |
| fully_admissible | 4 | witten_1981, nielsen_ninomiya, cap_theorem, git_semantic_merge |
| boundary_non_definable | 2 | distler_garibaldi, type_system_macro_expansion |
| non_admissible_shared_obstruction | 2 | synthetic_shared_obstruction, access_control_inheritance |
| non_admissible_no_new_obstruction | 2 | synthetic_lossy_no_obstruction, database_expand_contract |

## Condition matrix

| Case | AC1 | AC2 | AC3 | AC4 | AC5 | AC6 | AC7 | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| witten_1981 | T | T | T | T | T | T | T | fully_admissible |
| nielsen_ninomiya | T | T | T | T | T | T | T | fully_admissible |
| distler_garibaldi | T | T | **F** | T | F | T | T | boundary_non_definable |
| cap_theorem | T | T | T | T | T | T | T | fully_admissible |
| synthetic_lossy_no_obstruction | T | T | T | T | F | **F** | T | non_admissible_no_new_obstruction |
| synthetic_shared_obstruction | T | T | T | T | F | T | **F** | non_admissible_shared_obstruction |
| git_semantic_merge | T | T | T | T | T | T | T | fully_admissible |
| database_expand_contract | T | T | T | T | T | **F** | T | non_admissible_no_new_obstruction |
| access_control_inheritance | T | T | T | T | T | T | **F** | non_admissible_shared_obstruction |
| type_system_macro_expansion | T | T | **F** | T | F | F | T | boundary_non_definable |

Bold = condition that determines verdict (primary failure).

## Positive cases (all 7 conditions satisfied)

**witten_1981 (T27):** Geometric stratification resolves chirality obstruction.
All 7 conditions hold: both systems valid, projection defined and lossy,
restricted obstructed (chirality_requirement conflicts with smooth_field),
richer unobstructed (anomaly_inflow patch provides global section).

**nielsen_ninomiya (T27):** Bulk SPT + boundary resolves lattice doubling
obstruction. All 7 conditions hold: restricted is chained (A=B, B=C, A!=C),
richer has global section via anomaly inflow.

**cap_theorem (T28):** Eventual consistency resolves the CAP impossibility.
All 7 conditions hold. Identical three-patch chaining structure to NN.

**git_semantic_merge (T30):** Rename-aware merge driver resolves path-level
conflict. All 7 conditions hold. Only non-physics positive case.

## Boundary cases (AC3 fails)

**distler_garibaldi (T27):** sm_chirality site has no target in single-E8
representation theory. site_map_total=False. Category change, not enrichment.
Not a failed PO1 instance; a correct identification of the boundary.

**type_system_macro_expansion (T30):** macro_expansion_phase site has no
target in the restricted no-macro system. site_map_total=False. Same structural
diagnosis as DG: the projected-away content involves a new syntactic category.

## Non-admissible cases

**synthetic_lossy_no_obstruction (T29):** Projection loses structure but
neither system is obstructed. AC6=False. Control case showing loss alone
is not sufficient.

**synthetic_shared_obstruction (T29):** Both systems obstructed. AC7=False.
Control case showing inherited obstruction does not count as PO1 evidence.

**database_expand_contract (T30):** Both systems have global sections.
AC6=False. A safe migration loses deployment-phase detail without creating an
impossibility.

**access_control_inheritance (T30):** Policy conflict exists in both richer
and restricted system. AC7=False. The richer system only names the conflict
with more metadata; it does not resolve it.

## Weakest PO1 (minimum correct conditions)

AC1 + AC2 + AC3 + AC6 + AC7

These five conditions correctly classify all 10 cases. No case in the test
set fails on AC4 or AC5 alone.

## Recommended PO1 (guarded against overcounting)

AC1 + AC2 + AC3 + AC4 + AC5 + AC6 + AC7

AC4 guards against trivially-broken restricted systems (locally inconsistent
patches that are not "surprisingly" obstructed).

AC5 guards against lossless or unlabeled projections (identity-like projections
or projections where no structure is identified as forgotten).

## PO1 status

`partially_supported_narrowed`

PO1 is retained at partially_supported and formally narrowed. The schema is:

> A definable projection from a globally satisfiable richer system to a
> non-trivially obstructed restricted system, where the projection forgets
> named and measurable structure, is a faithful finite
> Projection-Obstruction instance.

PO1 does not split into subclaims. The single positive schema survives all
hostile tests.
