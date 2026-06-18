# T27 Test Specification: GU Class-Relative No-Go Bridge Audit

## Purpose

T27 tests whether selected GU no-go analyses can be represented as finite
D1RestrictionSystems whose projections preserve the original theorem structure
while identifying the additional structure carried by the richer model.

The test suite verifies three independent bridge cases and the cross-case
Projection-Obstruction Pattern.

## Acceptance criteria

The goal succeeds if it produces:

1. At least one faithful finite bridge model (H1 case with obstruction detected
   in restricted system and global section existing in richer system).
2. At least one failed bridge model or one requiring richer mathematics (H3 case
   or H2 case with incomplete morphism).
3. An explicit comparison of what is preserved and what is lost under projection.
4. A recommendation on whether the bridge is conceptual only, structurally
   faithful, mathematically equivalent, or currently unsupported.

## Test structure

| Test class | Case | Key assertions |
| --- | --- | --- |
| `WittenBridgeCaseTests` | Witten 1981 | richer has global section; restricted obstructed; morphism defined but blocked |
| `NielsenNinomiyaBridgeCaseTests` | Nielsen-Ninomiya | richer has global section; restricted obstructed; morphism defined but blocked |
| `DistlerGaribaldiCaseTests` | Distler-Garibaldi | site_map_total=False; H3 verdict |
| `BridgeAuditResultTests` | Cross-case | pattern detected; stretch goal reached; H2 top-level |

## Per-case test logic

### Witten 1981

**Richer system (witten_stratified_richer)**

- 2 sites: `smooth_bulk` and `defect_stratum`
- 3 patches: `bulk_local`, `defect_local`, `anomaly_inflow`
- `anomaly_inflow` patch: `chiral_bulk different chiral_defect`
- Global variables: `{chiral_bulk, chiral_defect}`; constraint: `chiral_bulk != chiral_defect`
- Global witness count: 2 (assignments `{+1,-1}` and `{-1,+1}`)
- `obstruction_detected = False`

**Restricted system (witten_smooth_restricted)**

- 2 sites: `smooth_site_A` and `smooth_site_B`
- 3 patches encoding the Witten class assumptions:
  - `patch_A_smooth`: `chiral_A same smooth_field`
  - `patch_B_smooth`: `chiral_B same smooth_field`
  - `chirality_requirement`: `chiral_A different chiral_B`
- Global variables: `{chiral_A, chiral_B, smooth_field}`
- All 8 assignments fail: `smooth_field` forces `chiral_A = chiral_B = smooth_field`,
  but `chirality_requirement` forces `chiral_A != chiral_B`.
- Global witness count: 0
- `obstruction_detected = True`
- All 3 patches locally satisfiable

**Morphism (witten_smoothing_functor)**

- Site map: `smooth_bulk -> smooth_site_A`, `defect_stratum -> smooth_site_B`
- `site_map_total = True`
- `local_profiles_preserved = False` (defect profile differs from smooth_site_B)
- `trust_path_preserved = True`
- `obstruction_status_preserved = False` (richer=False, restricted=True)
- `morphism_failure_kind = "local_profile_mismatch"`

### Nielsen-Ninomiya

**Richer system (nn_bulk_boundary_richer)**

- 3 sites: `bulk_spt`, `boundary_site`, `modified_algebra`
- 3 patches: `anomaly_inflow_local`, `boundary_chiral`, `algebra_consistency`
- `boundary_chiral`: `chiral_left different chiral_right`
- `algebra_consistency`: `anomaly_in same chiral_left`
- Global witness count: 2
- `obstruction_detected = False`

**Restricted system (nn_onsit_lattice_restricted)**

- 3 sites: `lattice_A`, `lattice_B`, `lattice_C`
- 3 patches encoding the three Nielsen-Ninomiya assumption groups:
  - `locality_hermitian` (sites A, B): `chiral_A same chiral_B`
  - `translation_invariance` (sites B, C): `chiral_B same chiral_C`
  - `exact_onsit_ua` (sites A, C): `chiral_A different chiral_C`
- Chaining forces `chiral_A = chiral_B = chiral_C` while `exact_onsit_ua`
  forces `chiral_A != chiral_C` — a local-to-global contradiction.
- Global witness count: 0
- `obstruction_detected = True`
- All 3 patches locally satisfiable

**Morphism (nn_onsit_locality_functor)**

- Site map: `bulk_spt -> lattice_A`, `boundary_site -> lattice_B`,
  `modified_algebra -> lattice_C`
- `site_map_total = True`
- `local_profiles_preserved = False`
- `trust_path_preserved = True`
- `obstruction_status_preserved = False`
- `morphism_failure_kind = "local_profile_mismatch"`

### Distler-Garibaldi

**Richer system (dg_e8xe8_bundle_richer)**

- 4 sites: `e8_factor_1`, `e8_factor_2`, `cy_bundle`, `sm_chirality`
- 5 patches
- Global witness count: 4
- `obstruction_detected = False`

**Restricted system (dg_single_e8_restricted)**

- 3 sites: `sl2c_sector`, `g_centralizer`, `matter_spectrum`
- 6 patches encoding the single-E8 structure constraint and the three
  ToE assumptions plus the Distler-Garibaldi theorem
- Global witness count: 0
- `obstruction_detected = True`
- All 6 patches locally satisfiable

**Morphism (dg_single_e8_adjoint_functor)**

- Site map covers only 3 of 4 source sites; `sm_chirality` has no target
- `site_map_total = False` — this is the key structural finding
- `morphism_failure_kind = "site_map_incomplete"`
- `hypothesis = "H3"`

The failure mode for Distler-Garibaldi is categorically different from Witten
and NN: the morphism cannot even be stated (incomplete site map) rather than
being defined but obstructed (profile mismatch + obstruction non-preservation).

## Cross-case tests

### Projection-Obstruction Pattern

Detected when all H1 cases satisfy simultaneously:

- `richer_global_section.obstruction_detected = False`
- `restricted_global_section.obstruction_detected = True`
- `morphism_analysis.site_map_total = True`
- `morphism_analysis.obstruction_status_preserved = False`

Expected: pattern applies to `witten_1981` and `nielsen_ninomiya`; not to
`distler_garibaldi`.

T27 detects the pattern but does not finish its general formalization.
[T29](T29-projection-obstruction-schema.md) promotes the stretch result to
the named finite schema `PO1`, and adds synthetic cases where projection does
not create an obstruction or where obstruction is already present in both
systems.

### Top-level verdict

- `hypothesis_summary`: `{witten_1981: H1, nielsen_ninomiya: H1, distler_garibaldi: H3}`
- `stretch_goal_status`: `"REACHED"`
- Recommendation identifies H2 as top-level: bridge is structurally faithful
  for two of three cases, fails for one due to category change.

## Artifacts

- `models/gu_class_relative_bridge.py` — bridge models and audit runner
- `models/run_t27.py` — JSON runner
- `tests/test_gu_class_relative_bridge.py` — test suite (this spec)
- `results/gu-class-relative-bridge-v0.1.json` — machine-readable results
- `TECHNICAL-REPORT-class-relative-bridge-audit-v0.1.md` — full report
