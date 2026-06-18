# T27 Bridge Audit Results: GU Class-Relative No-Go Analysis

Generated from `run_t27_analysis()`.

## Summary

| Case | Hypothesis | Richer obstruction | Restricted obstruction | Morphism failure |
| --- | --- | --- | --- | --- |
| Witten 1981 | H1 | False (2 witnesses) | True (0 witnesses) | local_profile_mismatch |
| Nielsen-Ninomiya | H1 | False (2 witnesses) | True (0 witnesses) | local_profile_mismatch |
| Distler-Garibaldi | H3 | False (4 witnesses) | True (0 witnesses) | site_map_incomplete |

Top-level verdict: **H2** (bridge is structurally faithful for two of three cases).

Stretch goal: **REACHED** — Projection-Obstruction Pattern detected across Witten and Nielsen-Ninomiya.

## Case 1: Witten 1981

Richer system `witten_stratified_richer`: 2 sites, 3 patches, 1 edge.
Restricted system `witten_smooth_restricted`: 2 sites, 3 patches, 1 edge.

Richer global section: EXISTS (global_witness_count=2, local_witness_count=3).
Restricted global section: OBSTRUCTED (global_witness_count=0, local_witness_count=3).

Morphism `witten_smoothing_functor`:
- site_map_total: True
- local_profiles_preserved: False
- trust_path_preserved: True
- obstruction_status_preserved: False
- reached: False
- obstruction: local_profile_mismatch

Forgotten: defect stratum profile, anomaly_inflow patch, singular/brane/flux data.
Preserved: reversal_cost, trust path, smooth-shadow proposition values.

## Case 2: Nielsen-Ninomiya

Richer system `nn_bulk_boundary_richer`: 3 sites, 3 patches, 2 edges.
Restricted system `nn_onsit_lattice_restricted`: 3 sites, 3 patches, 2 edges.

Richer global section: EXISTS (global_witness_count=2, local_witness_count=3).
Restricted global section: OBSTRUCTED (global_witness_count=0, local_witness_count=3).

Morphism `nn_onsit_locality_functor`:
- site_map_total: True
- local_profiles_preserved: False
- trust_path_preserved: True
- obstruction_status_preserved: False
- reached: False
- obstruction: local_profile_mismatch

Forgotten: bulk SPT data, anomaly_inflow patch, modified Ginsparg-Wilson algebra.
Preserved: reversal_cost, trust path, lattice proposition values.

## Case 3: Distler-Garibaldi

Richer system `dg_e8xe8_bundle_richer`: 4 sites, 5 patches, 3 edges.
Restricted system `dg_single_e8_restricted`: 3 sites, 6 patches, 2 edges.

Richer global section: EXISTS (global_witness_count=4, local_witness_count=5).
Restricted global section: OBSTRUCTED (global_witness_count=0, local_witness_count=6).

Morphism `dg_single_e8_adjoint_functor`:
- site_map_total: **False** (sm_chirality has no target in single-E8)
- local_profiles_preserved: False
- trust_path_preserved: True
- obstruction_status_preserved: False
- reached: False
- obstruction: **site_map_incomplete**

Forgotten: sm_chirality site, second E8 factor, CY bundle data.
Preserved: individual ToE1/ToE2/ToE3 constraints (each locally satisfiable).

Key distinction: for Witten and NN the morphism is defined (site_map_total=True)
but blocked by profile mismatch and obstruction change.  For Distler-Garibaldi
the morphism cannot even be defined (site_map_total=False).  This reflects the
qualitative difference: DG's richer objects are category changes, not enrichments.

## Projection-Obstruction Pattern

Applies to: witten_1981, nielsen_ninomiya.
Does not apply to: distler_garibaldi.

Pattern definition: a theorem proved within a projected class corresponds to a
finite local-to-global obstruction in the restricted D1RestrictionSystem.  The
richer object resolves this obstruction by supplying extra patch data.  The
forgetful morphism is site-map-complete but loses exactly that patch data —
detected as local_profile_mismatch and obstruction_status_preserved=False.

## Recommendation

H2 is the correct top-level verdict.  The bridge is structurally faithful for
Witten 1981 and Nielsen-Ninomiya, and informatively fails for Distler-Garibaldi.
The Distler-Garibaldi result is not a failure of the framework; it is a correct
identification of the framework's boundary.
