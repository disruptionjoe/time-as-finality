"""T27: GU class-relative no-go bridge audit.

T27 asks whether selected GU no-go analyses can be represented as finite
D1RestrictionSystems whose projections preserve the original theorem while
identifying the additional structure carried by the richer model.

Three candidate case studies are examined independently:
  1. Witten 1981 — chirality from smooth Kaluza-Klein reduction
  2. Nielsen-Ninomiya — lattice fermion doubling
  3. Distler-Garibaldi — single-E8 representation-theoretic obstruction

For each case:
  - a richer D1RestrictionSystem is constructed (the fuller substrate)
  - a restricted D1RestrictionSystem is constructed (the projected class)
  - a D1RestrictionMorphism models the forgetful map
  - the morphism analysis reveals what is preserved and what is lost

D1Profile dimensions are reinterpreted for this domain:
  accessible_support: count of sites from which chiral data is accessible
  holder_redundancy:  number of independent chirality-carrying mechanisms
  branch_support:     degree of chiral branching (left/right separation)
  reversal_cost:      cost to suppress or reverse chirality (higher = harder)

The goal is not to model the physics.  The goal is to determine whether the
local-to-global restriction structure — obstruction, projection, compatibility —
appears faithfully in the finite abstraction.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    MorphismAnalysis,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    ValidationResult,
    GlobalSectionResult,
    analyze_morphism,
    global_section,
    validate_system,
)
from models.multiscale_observer_field import (
    D1Profile,
    ObserverSite,
    PatchConstraint,
)


# ---------------------------------------------------------------------------
# Shared vocabulary
# ---------------------------------------------------------------------------

HYPOTHESES = (
    "H0: no useful mathematical bridge exists (conceptual similarity only)",
    "H1: the case admits a faithful finite restriction-system abstraction",
    "H2: only some cases admit abstractions; bridge identifies which structure matters",
    "H3: abstraction requires richer mathematics than T26 currently supports",
)

CASE_NAMES = ("witten_1981", "nielsen_ninomiya", "distler_garibaldi")


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class BridgeCase:
    name: str
    theorem: str
    richer_system: D1RestrictionSystem
    restricted_system: D1RestrictionSystem
    morphism: D1RestrictionMorphism
    morphism_analysis: MorphismAnalysis
    richer_global_section: GlobalSectionResult
    restricted_global_section: GlobalSectionResult
    richer_validation: ValidationResult
    restricted_validation: ValidationResult
    forgotten_structure: tuple[str, ...]
    preserved_structure: tuple[str, ...]
    hypothesis: str
    bridge_verdict: str
    morphism_failure_kind: str


@dataclass(frozen=True)
class ProjectionObstructionPattern:
    applies: bool
    cases: tuple[str, ...]
    description: str


@dataclass(frozen=True)
class BridgeAuditResult:
    cases: tuple[BridgeCase, ...]
    common_pattern: ProjectionObstructionPattern
    hypothesis_summary: tuple[tuple[str, str], ...]
    recommendation: str
    stretch_goal_status: str
    stretch_goal_description: str


# ---------------------------------------------------------------------------
# Case 1: Witten 1981
# ---------------------------------------------------------------------------

def _witten_richer_system() -> D1RestrictionSystem:
    """Stratified geometric substrate: smooth bulk + defect stratum.

    The richer object is (X_tilde, S, B) where X_tilde is a singular variety,
    S is the singular/defect stratum, and B is brane/flux data at S.
    Chirality lives at the stratum; the global section EXISTS.
    """
    smooth_bulk = LocalD1Value(
        site=ObserverSite("smooth_bulk", "smooth_bulk", "smooth_manifold", 0, "geometric"),
        proposition_value="non_chiral",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    defect_stratum = LocalD1Value(
        site=ObserverSite("defect_stratum", "singular_stratum", "defect", 0, "geometric"),
        proposition_value="chiral",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=2,
            branch_support=1,
            reversal_cost=1,
        ),
    )
    patches = (
        RestrictionPatch(
            patch_id="bulk_local",
            site_ids=("smooth_bulk",),
            variables=("chiral_bulk",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="defect_local",
            site_ids=("defect_stratum",),
            variables=("chiral_defect",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="anomaly_inflow",
            site_ids=("smooth_bulk", "defect_stratum"),
            variables=("chiral_bulk", "chiral_defect"),
            constraints=(PatchConstraint("chiral_bulk", "chiral_defect", "different"),),
        ),
    )
    return D1RestrictionSystem(
        name="witten_stratified_richer",
        proposition="chiral_fermion_spectrum",
        local_values=(smooth_bulk, defect_stratum),
        transport_edges=(
            TransportEdge("smooth_bulk", "defect_stratum", "stratum_inclusion", trust_preserving=True),
        ),
        source_site="smooth_bulk",
        target_site="defect_stratum",
        patches=patches,
    )


def _witten_restricted_system() -> D1RestrictionSystem:
    """Smooth-shadow class: two patches of a smooth compact manifold.

    The restricted system models the Witten 1981 class: X smooth, compact,
    no background gauge data.  The chirality requirement conflicts with the
    smooth-field constraint, producing a gluing obstruction.
    The no-go theorem is the statement that this obstruction exists.
    """
    smooth_a = LocalD1Value(
        site=ObserverSite("smooth_site_A", "smooth_patch", "smooth_manifold", 0, "geometric"),
        proposition_value="non_chiral",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    smooth_b = LocalD1Value(
        site=ObserverSite("smooth_site_B", "smooth_patch", "smooth_manifold", 0, "geometric"),
        proposition_value="non_chiral",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    patches = (
        RestrictionPatch(
            patch_id="patch_A_smooth",
            site_ids=("smooth_site_A",),
            variables=("chiral_A", "smooth_field"),
            constraints=(PatchConstraint("chiral_A", "smooth_field", "same"),),
        ),
        RestrictionPatch(
            patch_id="patch_B_smooth",
            site_ids=("smooth_site_B",),
            variables=("chiral_B", "smooth_field"),
            constraints=(PatchConstraint("chiral_B", "smooth_field", "same"),),
        ),
        RestrictionPatch(
            patch_id="chirality_requirement",
            site_ids=("smooth_site_A", "smooth_site_B"),
            variables=("chiral_A", "chiral_B"),
            constraints=(PatchConstraint("chiral_A", "chiral_B", "different"),),
        ),
    )
    return D1RestrictionSystem(
        name="witten_smooth_restricted",
        proposition="chiral_fermion_spectrum",
        local_values=(smooth_a, smooth_b),
        transport_edges=(
            TransportEdge("smooth_site_A", "smooth_site_B", "smooth_overlap", trust_preserving=True),
        ),
        source_site="smooth_site_A",
        target_site="smooth_site_B",
        patches=patches,
    )


def _witten_morphism(
    richer: D1RestrictionSystem,
    restricted: D1RestrictionSystem,
) -> D1RestrictionMorphism:
    """Smoothing functor phi_smooth: (X_tilde, S, B) -> (X', trivial-bg).

    Maps the defect stratum to a smooth patch, losing the defect profile.
    Expected to fail on both local_profiles_preserved and
    obstruction_status_preserved.
    """
    return D1RestrictionMorphism(
        name="witten_smoothing_functor",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("smooth_bulk", "smooth_site_A"),
            SiteMap("defect_stratum", "smooth_site_B"),
        ),
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=True,
        require_obstruction_preservation=True,
    )


def witten_bridge_case() -> BridgeCase:
    richer = _witten_richer_system()
    restricted = _witten_restricted_system()
    morphism = _witten_morphism(richer, restricted)
    analysis = analyze_morphism(morphism)
    richer_gs = global_section(richer)
    restricted_gs = global_section(restricted)
    richer_val = validate_system(richer)
    restricted_val = validate_system(restricted)

    return BridgeCase(
        name="witten_1981",
        theorem=(
            "Smooth compact Kaluza-Klein compactification produces no chiral "
            "fermions (Witten 1981).  Inside the smooth class the 4d Dirac "
            "index vanishes."
        ),
        richer_system=richer,
        restricted_system=restricted,
        morphism=morphism,
        morphism_analysis=analysis,
        richer_global_section=richer_gs,
        restricted_global_section=restricted_gs,
        richer_validation=richer_val,
        restricted_validation=restricted_val,
        forgotten_structure=(
            "defect stratum profile (accessible_support, holder_redundancy, branch_support)",
            "anomaly_inflow patch: chiral_defect != chiral_bulk",
            "singular/brane/flux data that allowed global section to exist",
        ),
        preserved_structure=(
            "reversal_cost dimension at the smooth bulk site",
            "trust transport path (smooth_bulk -> defect_stratum maps to smooth_A -> smooth_B)",
            "the smooth-shadow sites and their non-chiral proposition value",
        ),
        hypothesis="H1",
        bridge_verdict=(
            "FAITHFUL BRIDGE.  The finite restriction system captures the Witten "
            "class-relative structure.  The richer stratified system has a global "
            "section (chirality is consistently assigned via the defect).  The "
            "smooth-shadow system is obstructed (the chirality requirement conflicts "
            "with the smooth-field constraint).  The smoothing morphism is blocked "
            "by local_profile_mismatch and global_obstruction_not_preserved, "
            "identifying exactly what is lost: defect data and anomaly-inflow structure."
        ),
        morphism_failure_kind=analysis.obstruction,
    )


# ---------------------------------------------------------------------------
# Case 2: Nielsen-Ninomiya
# ---------------------------------------------------------------------------

def _nn_richer_system() -> D1RestrictionSystem:
    """Bulk SPT + boundary + modified-algebra substrate.

    The richer object is a (d+1)-bulk together with a d-dimensional boundary
    and a modified Ginsparg-Wilson algebra.  Chirality lives in the bulk-boundary
    anomaly-inflow pair.  The global section EXISTS.
    """
    bulk_spt = LocalD1Value(
        site=ObserverSite("bulk_spt", "spt_bulk", "bulk", 0, "lattice"),
        proposition_value="anomaly_inflow",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=2,
            branch_support=1,
            reversal_cost=1,
        ),
    )
    boundary_site = LocalD1Value(
        site=ObserverSite("boundary_site", "boundary", "boundary", 0, "lattice"),
        proposition_value="chiral",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=1,
            reversal_cost=2,
        ),
    )
    modified_algebra = LocalD1Value(
        site=ObserverSite("modified_algebra", "gw_algebra", "algebra", 0, "lattice"),
        proposition_value="modified_chiral",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=1,
        ),
    )
    patches = (
        RestrictionPatch(
            patch_id="anomaly_inflow_local",
            site_ids=("bulk_spt",),
            variables=("anomaly_in",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="boundary_chiral",
            site_ids=("boundary_site",),
            variables=("chiral_left", "chiral_right"),
            constraints=(PatchConstraint("chiral_left", "chiral_right", "different"),),
        ),
        RestrictionPatch(
            patch_id="algebra_consistency",
            site_ids=("modified_algebra",),
            variables=("anomaly_in", "chiral_left"),
            constraints=(PatchConstraint("anomaly_in", "chiral_left", "same"),),
        ),
    )
    return D1RestrictionSystem(
        name="nn_bulk_boundary_richer",
        proposition="net_chiral_spectrum",
        local_values=(bulk_spt, boundary_site, modified_algebra),
        transport_edges=(
            TransportEdge("bulk_spt", "boundary_site", "anomaly_inflow_edge", trust_preserving=True),
            TransportEdge("boundary_site", "modified_algebra", "gw_algebra_edge", trust_preserving=True),
        ),
        source_site="bulk_spt",
        target_site="modified_algebra",
        patches=patches,
    )


def _nn_restricted_system() -> D1RestrictionSystem:
    """On-site local lattice fermion system.

    The restricted system imposes: locality, hermiticity, and translation
    invariance (patches locality_hermitian and translation_invariance) together
    with on-site exact U(1)_A (patch exact_onsit_ua).  The three patches are
    each locally satisfiable but globally obstructed.
    The no-go theorem is the statement that this obstruction exists.
    """
    lattice_a = LocalD1Value(
        site=ObserverSite("lattice_A", "lattice_site", "lattice", 0, "lattice"),
        proposition_value="non_chiral",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=2,
        ),
    )
    lattice_b = LocalD1Value(
        site=ObserverSite("lattice_B", "lattice_site", "lattice", 0, "lattice"),
        proposition_value="non_chiral",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=2,
        ),
    )
    lattice_c = LocalD1Value(
        site=ObserverSite("lattice_C", "lattice_site", "lattice", 0, "lattice"),
        proposition_value="non_chiral",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=2,
        ),
    )
    patches = (
        RestrictionPatch(
            patch_id="locality_hermitian",
            site_ids=("lattice_A", "lattice_B"),
            variables=("chiral_A", "chiral_B"),
            constraints=(PatchConstraint("chiral_A", "chiral_B", "same"),),
        ),
        RestrictionPatch(
            patch_id="translation_invariance",
            site_ids=("lattice_B", "lattice_C"),
            variables=("chiral_B", "chiral_C"),
            constraints=(PatchConstraint("chiral_B", "chiral_C", "same"),),
        ),
        RestrictionPatch(
            patch_id="exact_onsit_ua",
            site_ids=("lattice_A", "lattice_C"),
            variables=("chiral_A", "chiral_C"),
            constraints=(PatchConstraint("chiral_A", "chiral_C", "different"),),
        ),
    )
    return D1RestrictionSystem(
        name="nn_onsit_lattice_restricted",
        proposition="net_chiral_spectrum",
        local_values=(lattice_a, lattice_b, lattice_c),
        transport_edges=(
            TransportEdge("lattice_A", "lattice_B", "lattice_link_AB", trust_preserving=True),
            TransportEdge("lattice_B", "lattice_C", "lattice_link_BC", trust_preserving=True),
        ),
        source_site="lattice_A",
        target_site="lattice_C",
        patches=patches,
    )


def _nn_morphism(
    richer: D1RestrictionSystem,
    restricted: D1RestrictionSystem,
) -> D1RestrictionMorphism:
    """On-site locality functor phi_local.

    Maps (bulk + boundary + modified-algebra) -> d-dim on-site lattice,
    forgetting the bulk SPT data and the Ginsparg-Wilson algebra structure.
    Expected to fail on local_profiles_preserved and
    obstruction_status_preserved.
    """
    return D1RestrictionMorphism(
        name="nn_onsit_locality_functor",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("bulk_spt", "lattice_A"),
            SiteMap("boundary_site", "lattice_B"),
            SiteMap("modified_algebra", "lattice_C"),
        ),
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=True,
        require_obstruction_preservation=True,
    )


def nielsen_ninomiya_bridge_case() -> BridgeCase:
    richer = _nn_richer_system()
    restricted = _nn_restricted_system()
    morphism = _nn_morphism(richer, restricted)
    analysis = analyze_morphism(morphism)
    richer_gs = global_section(richer)
    restricted_gs = global_section(restricted)
    richer_val = validate_system(richer)
    restricted_val = validate_system(restricted)

    return BridgeCase(
        name="nielsen_ninomiya",
        theorem=(
            "A local Hermitian translation-invariant lattice fermion action with "
            "exact on-site U(1)_V and U(1)_A cannot produce a net chiral spectrum "
            "(Nielsen-Ninomiya 1981).  The doubling theorem."
        ),
        richer_system=richer,
        restricted_system=restricted,
        morphism=morphism,
        morphism_analysis=analysis,
        richer_global_section=richer_gs,
        restricted_global_section=restricted_gs,
        richer_validation=richer_val,
        restricted_validation=restricted_val,
        forgotten_structure=(
            "bulk SPT data (accessible_support, holder_redundancy, branch_support)",
            "anomaly_inflow patch connecting bulk to boundary chiral modes",
            "modified Ginsparg-Wilson algebra structure at the algebra site",
        ),
        preserved_structure=(
            "reversal_cost dimension at each mapped site",
            "trust transport path (bulk -> boundary -> algebra maps to A -> B -> C)",
            "the lattice proposition_value (non_chiral in both shadows)",
        ),
        hypothesis="H1",
        bridge_verdict=(
            "FAITHFUL BRIDGE.  The finite restriction system captures the NN "
            "class-relative structure.  The bulk+boundary richer system has a "
            "global section (anomaly_in ties to chiral_left, which differs from "
            "chiral_right via inflow).  The on-site lattice restricted system is "
            "obstructed: locality_hermitian forces chiral_A=chiral_B, translation "
            "invariance forces chiral_B=chiral_C, and exact on-site U(1)_A forces "
            "chiral_A!=chiral_C — a finite local-to-global contradiction.  The "
            "on-site-locality morphism is blocked by local_profile_mismatch and "
            "global_obstruction_not_preserved, identifying the bulk SPT data and "
            "modified algebra as the forgotten structure."
        ),
        morphism_failure_kind=analysis.obstruction,
    )


# ---------------------------------------------------------------------------
# Case 3: Distler-Garibaldi
# ---------------------------------------------------------------------------

def _dg_richer_system() -> D1RestrictionSystem:
    """E8 x E8 + Calabi-Yau bundle substrate (candidate a).

    Sites represent the E8 x E8 factors and the CY bundle with flux.
    All local patches are satisfiable and the global section EXISTS.
    The sm_chirality site has no counterpart in single-E8 representation
    theory — this is the structural fact that blocks the morphism.
    """
    e8_1 = LocalD1Value(
        site=ObserverSite("e8_factor_1", "e8_factor", "lie_group", 0, "representation"),
        proposition_value="e8_rep",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=1,
            reversal_cost=2,
        ),
    )
    e8_2 = LocalD1Value(
        site=ObserverSite("e8_factor_2", "e8_factor", "lie_group", 0, "representation"),
        proposition_value="e8_rep",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=1,
            reversal_cost=2,
        ),
    )
    cy_bundle = LocalD1Value(
        site=ObserverSite("cy_bundle", "cy_bundle", "bundle", 0, "representation"),
        proposition_value="bundle_with_flux",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=2,
            branch_support=1,
            reversal_cost=1,
        ),
    )
    sm_chirality = LocalD1Value(
        site=ObserverSite("sm_chirality", "sm_matter", "spectrum", 0, "representation"),
        proposition_value="chiral_sm_generations",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=1,
            reversal_cost=1,
        ),
    )
    patches = (
        RestrictionPatch(
            patch_id="e8_1_rep",
            site_ids=("e8_factor_1",),
            variables=("v_e81",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="e8_2_rep",
            site_ids=("e8_factor_2",),
            variables=("v_e82",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="bundle_twist",
            site_ids=("cy_bundle",),
            variables=("v_bundle",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="sm_chirality_req",
            site_ids=("cy_bundle", "sm_chirality"),
            variables=("v_bundle", "v_sm"),
            constraints=(PatchConstraint("v_bundle", "v_sm", "same"),),
        ),
        RestrictionPatch(
            patch_id="e8_compat",
            site_ids=("e8_factor_1", "e8_factor_2"),
            variables=("v_e81", "v_e82"),
            constraints=(PatchConstraint("v_e81", "v_e82", "same"),),
        ),
    )
    return D1RestrictionSystem(
        name="dg_e8xe8_bundle_richer",
        proposition="sm_three_generation_chirality",
        local_values=(e8_1, e8_2, cy_bundle, sm_chirality),
        transport_edges=(
            TransportEdge("e8_factor_1", "cy_bundle", "e8_bundle_coupling", trust_preserving=True),
            TransportEdge("e8_factor_2", "cy_bundle", "e8_bundle_coupling_2", trust_preserving=True),
            TransportEdge("cy_bundle", "sm_chirality", "bundle_sm_projection", trust_preserving=True),
        ),
        source_site="e8_factor_1",
        target_site="sm_chirality",
        patches=patches,
    )


def _dg_restricted_system() -> D1RestrictionSystem:
    """Single-E8 representation-theoretic restricted class.

    Sites represent the SL(2,C) x G decomposition of one real E8 adjoint.
    The Distler-Garibaldi theorem is encoded as: the ToE1+ToE2 structure
    constraint forces g_connected=v_high_spin, while the SM physics demand
    forces v21_complex=g_connected, and the DG theorem simultaneously forces
    v21_complex!=g_connected — a gluing obstruction.
    """
    sl2c = LocalD1Value(
        site=ObserverSite("sl2c_sector", "sl2c_sector", "representation", 0, "representation"),
        proposition_value="lorentz_sector",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    g_centralizer = LocalD1Value(
        site=ObserverSite("g_centralizer", "g_centralizer", "representation", 0, "representation"),
        proposition_value="internal_gauge",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    matter = LocalD1Value(
        site=ObserverSite("matter_spectrum", "matter_spectrum", "representation", 0, "representation"),
        proposition_value="matter_content",
        profile=D1Profile(
            accessible_support=0,
            holder_redundancy=0,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    patches = (
        RestrictionPatch(
            patch_id="toe1",
            site_ids=("g_centralizer",),
            variables=("g_connected",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="toe2",
            site_ids=("matter_spectrum",),
            variables=("v_high_spin",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="toe3",
            site_ids=("sl2c_sector",),
            variables=("v21_complex",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="e8_structure",
            site_ids=("sl2c_sector", "g_centralizer"),
            variables=("g_connected", "v_high_spin"),
            constraints=(PatchConstraint("g_connected", "v_high_spin", "same"),),
        ),
        RestrictionPatch(
            patch_id="sm_physics_demand",
            site_ids=("sl2c_sector", "matter_spectrum"),
            variables=("v21_complex", "g_connected"),
            constraints=(PatchConstraint("v21_complex", "g_connected", "same"),),
        ),
        RestrictionPatch(
            patch_id="dg_theorem",
            site_ids=("sl2c_sector", "g_centralizer", "matter_spectrum"),
            variables=("g_connected", "v_high_spin", "v21_complex"),
            constraints=(
                PatchConstraint("g_connected", "v_high_spin", "same"),
                PatchConstraint("v21_complex", "g_connected", "different"),
            ),
        ),
    )
    return D1RestrictionSystem(
        name="dg_single_e8_restricted",
        proposition="sm_three_generation_chirality",
        local_values=(sl2c, g_centralizer, matter),
        transport_edges=(
            TransportEdge("sl2c_sector", "g_centralizer", "centralizer_inclusion", trust_preserving=True),
            TransportEdge("g_centralizer", "matter_spectrum", "rep_decomposition", trust_preserving=True),
        ),
        source_site="sl2c_sector",
        target_site="matter_spectrum",
        patches=patches,
    )


def _dg_morphism(
    richer: D1RestrictionSystem,
    restricted: D1RestrictionSystem,
) -> D1RestrictionMorphism:
    """Single-E8-adjoint functor phi_singleE8 — INCOMPLETE BY DESIGN.

    The richer E8 x E8 + bundle system has a site (sm_chirality) with no
    counterpart in single-E8 representation theory.  The site map is therefore
    incomplete.  This is the key structural finding for Distler-Garibaldi:
    the forgetful map cannot even be defined as a restriction-system morphism.
    The failure kind is site_map_incomplete, not obstruction_status_preserved.
    """
    return D1RestrictionMorphism(
        name="dg_single_e8_adjoint_functor",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("e8_factor_1", "sl2c_sector"),
            SiteMap("e8_factor_2", "g_centralizer"),
            SiteMap("cy_bundle", "matter_spectrum"),
        ),
        preserved_dimensions=(),
        require_trust_path_preservation=True,
        require_obstruction_preservation=True,
    )


def distler_garibaldi_bridge_case() -> BridgeCase:
    richer = _dg_richer_system()
    restricted = _dg_restricted_system()
    morphism = _dg_morphism(richer, restricted)
    analysis = analyze_morphism(morphism)
    richer_gs = global_section(richer)
    restricted_gs = global_section(restricted)
    richer_val = validate_system(richer)
    restricted_val = validate_system(restricted)

    return BridgeCase(
        name="distler_garibaldi",
        theorem=(
            "No single real form of E8 contains subgroups SL(2,C) and G satisfying "
            "simultaneously: G connected compact centralizing SL(2,C), V_{m,n}=0 "
            "for m+n>4, and V_{2,1} complex as a G-representation "
            "(Distler-Garibaldi 2010)."
        ),
        richer_system=richer,
        restricted_system=restricted,
        morphism=morphism,
        morphism_analysis=analysis,
        richer_global_section=richer_gs,
        restricted_global_section=restricted_gs,
        richer_validation=richer_val,
        restricted_validation=restricted_val,
        forgotten_structure=(
            "sm_chirality site: has no counterpart in single-E8 representation theory",
            "second E8 factor and product-group structure",
            "Calabi-Yau bundle data and flux (bundle_twist patch)",
        ),
        preserved_structure=(
            "the abstract notion that ToE1/ToE2/ToE3 are individual constraints",
            "the local satisfiability of each assumption separately",
        ),
        hypothesis="H3",
        bridge_verdict=(
            "BRIDGE FAILS: CATEGORY CHANGE.  The E8 x E8 + bundle richer system "
            "has a site (sm_chirality) with no counterpart in single-E8 "
            "representation theory.  The morphism cannot be completed: "
            "site_map_total=False.  This failure is categorically different from "
            "Witten and Nielsen-Ninomiya, where the morphism is defined but "
            "blocked by profile mismatch and obstruction non-preservation.  Here "
            "the forgetful map cannot even be stated as a restriction-system "
            "morphism.  The DG richer objects (E8xE8, K(E10), SO(3,11)) are "
            "not enrichments of single-E8 — they are category changes.  T26 "
            "does not currently support this kind of bridge.  Conclusion: H3."
        ),
        morphism_failure_kind=analysis.obstruction,
    )


# ---------------------------------------------------------------------------
# Cross-case analysis
# ---------------------------------------------------------------------------

def _projection_obstruction_pattern(cases: tuple[BridgeCase, ...]) -> ProjectionObstructionPattern:
    """Check whether the Witten and NN cases share a common structural pattern."""
    h1_cases = [c for c in cases if c.hypothesis == "H1"]
    pattern_holds = all(
        (
            not c.richer_global_section.obstruction_detected
            and c.restricted_global_section.obstruction_detected
            and c.morphism_analysis.site_map_total
            and not c.morphism_analysis.obstruction_status_preserved
        )
        for c in h1_cases
    )
    case_names = tuple(c.name for c in h1_cases)
    if pattern_holds and len(h1_cases) >= 2:
        description = (
            "PROJECTION-OBSTRUCTION PATTERN DETECTED across cases: "
            + ", ".join(case_names) + ".  "
            "In each case: (1) the richer system has no gluing obstruction; "
            "(2) the restricted system has a gluing obstruction; "
            "(3) the forgetful morphism is site-map-complete; "
            "(4) the morphism is blocked by obstruction_status_preserved=False.  "
            "The theorem proved within the projected class corresponds to a finite "
            "local-to-global obstruction.  The richer object resolves this "
            "obstruction by supplying extra patch data — the defect/brane "
            "structure (Witten) or the bulk SPT data (Nielsen-Ninomiya) — "
            "that allows a consistent global assignment to exist.  The forgetful "
            "morphism loses exactly this extra patch data."
        )
    elif pattern_holds:
        description = (
            "Pattern holds for " + ", ".join(case_names) + " but only one H1 case present."
        )
    else:
        description = "Pattern does not hold uniformly across H1 cases."
    return ProjectionObstructionPattern(
        applies=pattern_holds and len(h1_cases) >= 2,
        cases=case_names,
        description=description,
    )


# ---------------------------------------------------------------------------
# Main audit runner
# ---------------------------------------------------------------------------

def run_t27_bridge_audit() -> BridgeAuditResult:
    cases = (
        witten_bridge_case(),
        nielsen_ninomiya_bridge_case(),
        distler_garibaldi_bridge_case(),
    )
    pattern = _projection_obstruction_pattern(cases)
    hypothesis_summary = tuple(
        (c.name, c.hypothesis) for c in cases
    )
    stretch_status = "REACHED" if pattern.applies else "NOT_REACHED"
    stretch_description = (
        "The two H1 cases (Witten, Nielsen-Ninomiya) instantiate a common "
        "finite Projection-Obstruction Schema: a theorem proved within a "
        "projected class corresponds to a gluing obstruction in the restricted "
        "D1RestrictionSystem, while the richer object resolves that obstruction "
        "via extra patch data.  The forgetful morphism loses exactly that patch "
        "data.  The Distler-Garibaldi case is excluded because its bridge "
        "failure is a site-map incompleteness (category change), not an "
        "obstruction-status divergence (enrichment)."
        if pattern.applies
        else "Stretch goal not reached."
    )
    return BridgeAuditResult(
        cases=cases,
        common_pattern=pattern,
        hypothesis_summary=hypothesis_summary,
        recommendation=(
            "H2 is the top-level verdict: the bridge is structurally faithful "
            "for two of three cases (Witten 1981, Nielsen-Ninomiya), and fails "
            "for one (Distler-Garibaldi) because the richer objects involve a "
            "category change that T26 cannot represent as a restriction-system "
            "morphism.  The Projection-Obstruction Schema formalizes the common "
            "pattern for the two faithful cases.  The Distler-Garibaldi result "
            "is an informative negative: it identifies the boundary of T26 and "
            "calls for richer morphism machinery (presheaf-level or category-level "
            "functors) for that case.  Do not claim that any physical no-go theorem "
            "has been overturned.  The abstract structure survives; the physics is "
            "unchanged."
        ),
        stretch_goal_status=stretch_status,
        stretch_goal_description=stretch_description,
    )


def run_t27_analysis() -> dict[str, Any]:
    result = run_t27_bridge_audit()
    return {
        "hypotheses": list(HYPOTHESES),
        "cases": [_bridge_case_to_dict(c) for c in result.cases],
        "common_pattern": {
            "applies": result.common_pattern.applies,
            "cases": list(result.common_pattern.cases),
            "description": result.common_pattern.description,
        },
        "hypothesis_summary": {name: h for name, h in result.hypothesis_summary},
        "recommendation": result.recommendation,
        "stretch_goal_status": result.stretch_goal_status,
        "stretch_goal_description": result.stretch_goal_description,
    }


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------

def _bridge_case_to_dict(c: BridgeCase) -> dict[str, Any]:
    return {
        "name": c.name,
        "theorem": c.theorem,
        "richer_system": {
            "name": c.richer_system.name,
            "site_count": len(c.richer_system.site_ids()),
            "patch_count": len(c.richer_system.patches),
            "edge_count": len(c.richer_system.transport_edges),
            "validation_valid": c.richer_validation.valid,
            "global_section_exists": c.richer_global_section.global_assignment_exists,
            "obstruction_detected": c.richer_global_section.obstruction_detected,
            "local_witness_count": c.richer_global_section.local_witness_count,
            "global_witness_count": c.richer_global_section.global_witness_count,
        },
        "restricted_system": {
            "name": c.restricted_system.name,
            "site_count": len(c.restricted_system.site_ids()),
            "patch_count": len(c.restricted_system.patches),
            "edge_count": len(c.restricted_system.transport_edges),
            "validation_valid": c.restricted_validation.valid,
            "global_section_exists": c.restricted_global_section.global_assignment_exists,
            "obstruction_detected": c.restricted_global_section.obstruction_detected,
            "local_witness_count": c.restricted_global_section.local_witness_count,
            "global_witness_count": c.restricted_global_section.global_witness_count,
        },
        "morphism": {
            "name": c.morphism.name,
            "site_map_total": c.morphism_analysis.site_map_total,
            "local_profiles_preserved": c.morphism_analysis.local_profiles_preserved,
            "trust_path_preserved": c.morphism_analysis.trust_path_preserved,
            "obstruction_status_preserved": c.morphism_analysis.obstruction_status_preserved,
            "reached": c.morphism_analysis.reached,
            "obstruction": c.morphism_analysis.obstruction,
            "interpretation": c.morphism_analysis.interpretation,
        },
        "forgotten_structure": list(c.forgotten_structure),
        "preserved_structure": list(c.preserved_structure),
        "hypothesis": c.hypothesis,
        "bridge_verdict": c.bridge_verdict,
        "morphism_failure_kind": c.morphism_failure_kind,
    }
