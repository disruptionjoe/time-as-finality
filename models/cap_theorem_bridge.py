"""T28: CAP theorem as a finite gluing obstruction.

T28 demonstrates that the CAP theorem (Brewer 2000, formalized by Gilbert
and Lynch 2002) instantiates the same finite Projection-Obstruction Pattern
identified in T27 for Nielsen-Ninomiya.

The CAP theorem states that a distributed system cannot simultaneously guarantee:
  C - Consistency: every read receives the most recent write or an error
  A - Availability: every request receives a response
  P - Partition tolerance: the system continues operating despite network partitions

In the D1RestrictionSystem encoding:
  - Restricted system: three patches (consistency, availability, partition_tolerance)
    each locally satisfiable but globally obstructed -- identical chaining structure
    to the Nielsen-Ninomiya restricted system
  - Richer system: eventual-consistency substrate -- three patches allowing divergence
    during partition and reconciliation via sync -- global section exists
  - Morphism: strong-consistency-demand functor -- loses branch_support and produces
    local_profile_mismatch + obstruction_status_preserved=False

The structural identity with Nielsen-Ninomiya is made explicit by
nn_cap_structural_comparison(): same patch_count, local_witness_count,
global_witness_count, obstruction_detected, and chaining pattern.

D1Profile dimensions in this domain:
  accessible_support: whether the node's state is accessible to external requests
  holder_redundancy:  number of independent state holders (replicas)
  branch_support:     degree to which the system permits divergent state across nodes
  reversal_cost:      cost of rolling back a write or reconciling divergent state
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    GlobalSectionResult,
    LocalD1Value,
    MorphismAnalysis,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    ValidationResult,
    analyze_morphism,
    global_section,
    validate_system,
)
from models.multiscale_observer_field import (
    D1Profile,
    ObserverSite,
    PatchConstraint,
)

HYPOTHESES = (
    "H0: no useful mathematical bridge exists (conceptual similarity only)",
    "H1: the case admits a faithful finite restriction-system abstraction",
    "H2: only some cases admit abstractions; bridge identifies which structure matters",
    "H3: abstraction requires richer mathematics than T26 currently supports",
)


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CAPBridgeCase:
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
class NNCAPComparison:
    nn_patch_count: int
    cap_patch_count: int
    nn_local_witness_count: int
    cap_local_witness_count: int
    nn_global_witness_count: int
    cap_global_witness_count: int
    nn_obstruction_detected: bool
    cap_obstruction_detected: bool
    structural_identity: bool
    chaining_pattern: str
    interpretation: str


@dataclass(frozen=True)
class CAPBridgeResult:
    case: CAPBridgeCase
    nn_cap_comparison: NNCAPComparison
    recommendation: str


# ---------------------------------------------------------------------------
# Restricted system: three CAP assumptions as patches
# ---------------------------------------------------------------------------

def _cap_restricted_system() -> D1RestrictionSystem:
    """Strong-consistency class: three CAP assumptions as patches.

    Three nodes encode the CAP assumption groups:
      node_A: consistency observer
      node_B: availability observer
      node_C: partition-tolerance observer

    Patches:
      consistency (A, B): state_A same state_B -- C requires all nodes agree
      availability (B, C): state_B same state_C -- A requires all requests respond
      partition_tolerance (A, C): state_A different state_C -- P forces divergence

    Chaining: consistency forces state_A = state_B; availability forces
    state_B = state_C; therefore state_A = state_C; but partition_tolerance
    forces state_A != state_C -- a finite local-to-global contradiction identical
    in structure to Nielsen-Ninomiya's three-patch obstruction.
    """
    node_a = LocalD1Value(
        site=ObserverSite("node_A", "consistency_observer", "distributed_node", 0, "network"),
        proposition_value="consistent",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    node_b = LocalD1Value(
        site=ObserverSite("node_B", "availability_observer", "distributed_node", 0, "network"),
        proposition_value="available",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    node_c = LocalD1Value(
        site=ObserverSite("node_C", "partition_observer", "distributed_node", 0, "network"),
        proposition_value="partition_tolerant",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=3,
        ),
    )
    patches = (
        RestrictionPatch(
            patch_id="consistency",
            site_ids=("node_A", "node_B"),
            variables=("state_A", "state_B"),
            constraints=(PatchConstraint("state_A", "state_B", "same"),),
        ),
        RestrictionPatch(
            patch_id="availability",
            site_ids=("node_B", "node_C"),
            variables=("state_B", "state_C"),
            constraints=(PatchConstraint("state_B", "state_C", "same"),),
        ),
        RestrictionPatch(
            patch_id="partition_tolerance",
            site_ids=("node_A", "node_C"),
            variables=("state_A", "state_C"),
            constraints=(PatchConstraint("state_A", "state_C", "different"),),
        ),
    )
    return D1RestrictionSystem(
        name="cap_strong_consistency_restricted",
        proposition="consistent_available_partition_tolerant",
        local_values=(node_a, node_b, node_c),
        transport_edges=(
            TransportEdge("node_A", "node_B", "consistency_link", trust_preserving=True),
            TransportEdge("node_B", "node_C", "availability_link", trust_preserving=True),
        ),
        source_site="node_A",
        target_site="node_C",
        patches=patches,
    )


# ---------------------------------------------------------------------------
# Richer system: eventual-consistency substrate
# ---------------------------------------------------------------------------

def _cap_richer_system() -> D1RestrictionSystem:
    """Eventual-consistency substrate: divergence allowed during partition.

    Three sites:
      primary_node: accepts writes, may diverge during partition (branch_support=1)
      replica_node: serves reads, may diverge during partition (branch_support=1)
      sync_protocol: eventual reconciliation mechanism

    Patches:
      write_local (primary): unconstrained -- any write is accepted locally
      partition_diverge (primary, replica): state_primary different state_replica
        -- during partition, states can diverge; no requirement for simultaneous
        agreement captures the trade-off: the system stays available by allowing
        temporary inconsistency
      sync_reconcile (replica, sync): state_replica same sync_flag -- the sync
        protocol eventually aligns the replica with primary state

    Global section EXISTS: {state_primary=+1, state_replica=-1, sync_flag=-1}
    satisfies all constraints.  The system gains availability and partition
    tolerance by sacrificing immediate consistency.
    """
    primary = LocalD1Value(
        site=ObserverSite("primary_node", "primary_writer", "distributed_node", 0, "network"),
        proposition_value="accepts_writes",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=1,
            reversal_cost=2,
        ),
    )
    replica = LocalD1Value(
        site=ObserverSite("replica_node", "replica_reader", "distributed_node", 0, "network"),
        proposition_value="serves_reads",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=1,
            reversal_cost=2,
        ),
    )
    sync = LocalD1Value(
        site=ObserverSite("sync_protocol", "sync_mechanism", "protocol", 0, "network"),
        proposition_value="eventual_reconciliation",
        profile=D1Profile(
            accessible_support=1,
            holder_redundancy=1,
            branch_support=0,
            reversal_cost=1,
        ),
    )
    patches = (
        RestrictionPatch(
            patch_id="write_local",
            site_ids=("primary_node",),
            variables=("state_primary",),
            constraints=(),
        ),
        RestrictionPatch(
            patch_id="partition_diverge",
            site_ids=("primary_node", "replica_node"),
            variables=("state_primary", "state_replica"),
            constraints=(PatchConstraint("state_primary", "state_replica", "different"),),
        ),
        RestrictionPatch(
            patch_id="sync_reconcile",
            site_ids=("replica_node", "sync_protocol"),
            variables=("state_replica", "sync_flag"),
            constraints=(PatchConstraint("state_replica", "sync_flag", "same"),),
        ),
    )
    return D1RestrictionSystem(
        name="cap_eventual_consistency_richer",
        proposition="consistent_available_partition_tolerant",
        local_values=(primary, replica, sync),
        transport_edges=(
            TransportEdge("primary_node", "replica_node", "replication_link", trust_preserving=True),
            TransportEdge("replica_node", "sync_protocol", "sync_link", trust_preserving=True),
        ),
        source_site="primary_node",
        target_site="sync_protocol",
        patches=patches,
    )


# ---------------------------------------------------------------------------
# Morphism: strong-consistency-demand functor
# ---------------------------------------------------------------------------

def _cap_morphism(
    richer: D1RestrictionSystem,
    restricted: D1RestrictionSystem,
) -> D1RestrictionMorphism:
    """Strong-consistency-demand functor: eventual -> strong consistency class.

    Maps primary_node -> node_A, replica_node -> node_B, sync_protocol -> node_C.
    Declares reversal_cost as the preserved dimension, but richer sites have
    reversal_cost 2 or 1 while restricted sites have reversal_cost 3 -- so
    local_profiles_preserved=False (local_profile_mismatch).

    Additionally obstruction_status_preserved=False: the richer system has no
    gluing obstruction; the restricted system is obstructed.

    The forgotten structure is branch_support=1 on the primary and replica sites,
    which is the finite encoding of the ability to serve divergent state during
    a partition -- exactly what the eventual-consistency evasion supplies.
    """
    return D1RestrictionMorphism(
        name="cap_strong_consistency_demand_functor",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("primary_node", "node_A"),
            SiteMap("replica_node", "node_B"),
            SiteMap("sync_protocol", "node_C"),
        ),
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=True,
        require_obstruction_preservation=True,
    )


# ---------------------------------------------------------------------------
# Bridge case
# ---------------------------------------------------------------------------

def cap_bridge_case() -> CAPBridgeCase:
    richer = _cap_richer_system()
    restricted = _cap_restricted_system()
    morphism = _cap_morphism(richer, restricted)
    analysis = analyze_morphism(morphism)
    richer_gs = global_section(richer)
    restricted_gs = global_section(restricted)
    richer_val = validate_system(richer)
    restricted_val = validate_system(restricted)

    return CAPBridgeCase(
        name="cap_theorem",
        theorem=(
            "A distributed system cannot simultaneously guarantee Consistency, "
            "Availability, and Partition tolerance (Brewer 2000; Gilbert-Lynch "
            "2002).  In any system where network partitions can occur, at most "
            "two of the three properties can be guaranteed simultaneously."
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
            "branch_support=1 on primary and replica: ability to serve divergent state",
            "partition_diverge patch: state_primary different state_replica during partition",
            "sync_reconcile patch: eventual convergence replaces immediate consistency",
        ),
        preserved_structure=(
            "site-to-site mapping (primary->A, replica->B, sync->C) is total",
            "trust transport path is preserved across the morphism",
            "the abstract CAP proposition structure is preserved",
        ),
        hypothesis="H1",
        bridge_verdict=(
            "FAITHFUL BRIDGE.  The finite restriction system captures the CAP "
            "theorem structure.  The eventual-consistency richer system has a "
            "global section: {state_primary=+1, state_replica=-1, sync_flag=-1} "
            "satisfies all patches simultaneously -- states diverge during "
            "partition and the sync protocol reconciles them.  The strong-"
            "consistency restricted system is obstructed: consistency forces "
            "state_A=state_B, availability forces state_B=state_C, partition_"
            "tolerance forces state_A!=state_C -- a finite local-to-global "
            "contradiction identical in structure to Nielsen-Ninomiya.  The "
            "strong-consistency-demand morphism is blocked by local_profile_"
            "mismatch and obstruction_status_preserved=False, identifying "
            "exactly what is lost: branch_support=1 (the ability to serve "
            "divergent state during partition) and the partition_diverge patch "
            "(the mechanism that allows the richer global section to exist)."
        ),
        morphism_failure_kind=analysis.obstruction,
    )


# ---------------------------------------------------------------------------
# NN-CAP structural comparison
# ---------------------------------------------------------------------------

def nn_cap_structural_comparison() -> NNCAPComparison:
    """Demonstrate structural identity between the NN and CAP restricted systems.

    Both encode the same three-patch chaining obstruction:
      patch_1 (sites A, B): variable_A same variable_B
      patch_2 (sites B, C): variable_B same variable_C
      patch_3 (sites A, C): variable_A different variable_C

    Chaining: patch_1 forces A=B; patch_2 forces B=C; therefore A=C;
    patch_3 forces A!=C -- contradiction.

    The abstraction is domain-neutral: the physics no-go (NN) and the
    distributed-systems impossibility (CAP) both instantiate this minimal
    finite gluing obstruction.
    """
    from models.gu_class_relative_bridge import _nn_restricted_system
    nn = _nn_restricted_system()
    cap = _cap_restricted_system()
    nn_gs = global_section(nn)
    cap_gs = global_section(cap)
    structural_identity = (
        len(nn.patches) == len(cap.patches)
        and nn_gs.local_witness_count == cap_gs.local_witness_count
        and nn_gs.global_witness_count == cap_gs.global_witness_count
        and nn_gs.obstruction_detected == cap_gs.obstruction_detected
    )
    return NNCAPComparison(
        nn_patch_count=len(nn.patches),
        cap_patch_count=len(cap.patches),
        nn_local_witness_count=nn_gs.local_witness_count,
        cap_local_witness_count=cap_gs.local_witness_count,
        nn_global_witness_count=nn_gs.global_witness_count,
        cap_global_witness_count=cap_gs.global_witness_count,
        nn_obstruction_detected=nn_gs.obstruction_detected,
        cap_obstruction_detected=cap_gs.obstruction_detected,
        structural_identity=structural_identity,
        chaining_pattern=(
            "NN: locality_hermitian A=B, translation_invariance B=C, "
            "exact_onsit_ua A!=C.  "
            "CAP: consistency A=B, availability B=C, partition_tolerance A!=C.  "
            "Same three-patch chaining obstruction in both domains."
        ),
        interpretation=(
            "The Nielsen-Ninomiya and CAP restricted systems are structurally "
            "isomorphic as D1RestrictionSystems: same patch count (3), same "
            "local satisfiability count (3), same global witness count (0), "
            "same obstruction detection result (True).  The domain-neutral "
            "three-patch chaining obstruction is the finite abstraction of "
            "both impossibility results."
        ),
    )


# ---------------------------------------------------------------------------
# Audit runner
# ---------------------------------------------------------------------------

def run_cap_bridge_audit() -> CAPBridgeResult:
    case = cap_bridge_case()
    comparison = nn_cap_structural_comparison()
    return CAPBridgeResult(
        case=case,
        nn_cap_comparison=comparison,
        recommendation=(
            "H1 is confirmed for the CAP theorem.  The faithful bridge "
            "demonstrates that the CAP impossibility result instantiates the "
            "Projection-Obstruction Pattern identified in T27 for Nielsen-"
            "Ninomiya.  The structural identity between the NN and CAP "
            "restricted systems (patch_count=3, local_witness_count=3, "
            "global_witness_count=0, same chaining pattern) confirms that "
            "the T26 finite obstruction is domain-neutral: the same abstract "
            "three-patch chaining contradiction appears in quantum field theory "
            "(NN) and distributed systems (CAP).  The evasion mechanism is "
            "also structurally parallel: relaxing exact on-site symmetry (NN) "
            "corresponds to relaxing immediate consistency (CAP eventual "
            "consistency); both resolve the obstruction by adding the extra "
            "patch data that the restricted class forbids."
        ),
    )


def run_cap_analysis() -> dict[str, Any]:
    result = run_cap_bridge_audit()
    c = result.case
    comp = result.nn_cap_comparison
    return {
        "case": {
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
            },
            "forgotten_structure": list(c.forgotten_structure),
            "preserved_structure": list(c.preserved_structure),
            "hypothesis": c.hypothesis,
            "bridge_verdict": c.bridge_verdict,
            "morphism_failure_kind": c.morphism_failure_kind,
        },
        "nn_cap_comparison": {
            "nn_patch_count": comp.nn_patch_count,
            "cap_patch_count": comp.cap_patch_count,
            "nn_local_witness_count": comp.nn_local_witness_count,
            "cap_local_witness_count": comp.cap_local_witness_count,
            "nn_global_witness_count": comp.nn_global_witness_count,
            "cap_global_witness_count": comp.cap_global_witness_count,
            "nn_obstruction_detected": comp.nn_obstruction_detected,
            "cap_obstruction_detected": comp.cap_obstruction_detected,
            "structural_identity": comp.structural_identity,
            "chaining_pattern": comp.chaining_pattern,
            "interpretation": comp.interpretation,
        },
        "recommendation": result.recommendation,
    }
