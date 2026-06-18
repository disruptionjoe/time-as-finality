"""T34: Chained projection analysis for PO1.

T33 derives PO1's conditions from IPT and RMT. T34 asks whether PO1 can handle
chains of projections — specifically whether a finite gluing obstruction can
emerge from the full chain even when no partial prefix of the chain (from the
source to any intermediate level) is a PO1 instance.

The code-to-transistors chain provides the hostile test case:

  source_code → compiler_IR → assembly → machine_code → microarchitecture

At each step from source to an intermediate level, the intermediate system
still has a global section (no obstruction). Only the microarchitecture
endpoint has a finite gluing obstruction, modelling Spectre-class timing side
channels: speculative execution causes cache state and timing to expose the
secret access level, violating the security policy.

"Emergent obstruction" is defined precisely: the endpoint pair (source, final)
is a PO1 instance, but no partial-chain pair (source, Li) for any intermediate
Li is a PO1 instance. The obstruction is only visible at the full chain level.

Three chain shapes are analyzed:

  emergent_obstruction   endpoint is PO1; no source→intermediate pair is PO1
                         (Spectre: obstruction only visible at endpoint level)
  stepwise_propagation   obstruction appears at an intermediate step and
                         the endpoint pair is also a PO1 instance
  absorbed_obstruction   obstruction appears at an intermediate step but
                         endpoint pair is NOT a PO1 instance
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    global_section,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import AdmissibilityCheck, check_admissibility
from models.projection_obstruction_schema import ProjectionCase


# ---------------------------------------------------------------------------
# Chain data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ChainLink:
    """One projection step in a chain."""
    step_name: str
    source_level: str
    target_level: str
    source_system: D1RestrictionSystem
    target_system: D1RestrictionSystem
    forgotten_at_this_step: tuple[str, ...]
    target_obstructed: bool


@dataclass(frozen=True)
class CheckpointPair:
    """Source→intermediate pair admissibility check."""
    intermediate_level: str
    admissibility: AdmissibilityCheck


@dataclass(frozen=True)
class ProjectionChain:
    """A sequence of ChainLinks from an unobstructed source to a final target."""
    chain_name: str
    description: str
    abstraction_levels: tuple[str, ...]
    links: tuple[ChainLink, ...]
    checkpoint_pairs: tuple[CheckpointPair, ...]  # source→Li for each intermediate Li
    endpoint_case: ProjectionCase
    endpoint_admissibility: AdmissibilityCheck


@dataclass(frozen=True)
class ChainAnalysis:
    """Full analysis of a ProjectionChain."""
    chain: ProjectionChain
    step_count: int
    obstruction_first_appears_at: str   # level name of first obstructed target
    admissible_checkpoint_pairs: tuple[str, ...]  # source→Li pairs that are PO1
    emergent_obstruction: bool   # endpoint is PO1; no source→intermediate is PO1
    stepwise_propagation: bool   # obstruction appears mid-chain; endpoint also PO1
    absorbed_obstruction: bool   # obstruction appears mid-chain; endpoint NOT PO1
    endpoint_verdict: str
    chain_po1_conclusion: str


@dataclass(frozen=True)
class T34Result:
    spectre_chain: ChainAnalysis
    stepwise_chain: ChainAnalysis
    absorbed_chain: ChainAnalysis
    emergent_obstruction_confirmed: bool
    absorbed_obstruction_confirmed: bool
    stepwise_propagation_confirmed: bool
    po1_chain_theorem: str
    boundary: str
    recommendation: str


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _local(site_id: str, tag: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(
        site=ObserverSite(site_id, tag, "finite_site", 0, "chain"),
        proposition_value="true",
        profile=profile,
    )


def _three_site_system(
    prefix: str,
    tag: str,
    profile: D1Profile,
    obstructed: bool = False,
) -> D1RestrictionSystem:
    patches: tuple[RestrictionPatch, ...] = ()
    if obstructed:
        patches = (
            RestrictionPatch(
                f"{prefix}_ab",
                (f"{prefix}_A", f"{prefix}_B"),
                ("a", "b"),
                (PatchConstraint("a", "b", "same"),),
            ),
            RestrictionPatch(
                f"{prefix}_bc",
                (f"{prefix}_B", f"{prefix}_C"),
                ("b", "c"),
                (PatchConstraint("b", "c", "same"),),
            ),
            RestrictionPatch(
                f"{prefix}_ac",
                (f"{prefix}_A", f"{prefix}_C"),
                ("a", "c"),
                (PatchConstraint("a", "c", "different"),),
            ),
        )
    return D1RestrictionSystem(
        name=prefix,
        proposition="abstraction_level",
        local_values=(
            _local(f"{prefix}_A", tag, profile),
            _local(f"{prefix}_B", tag, profile),
            _local(f"{prefix}_C", tag, profile),
        ),
        transport_edges=(
            TransportEdge(f"{prefix}_A", f"{prefix}_B", "trusted_AB"),
            TransportEdge(f"{prefix}_B", f"{prefix}_C", "trusted_BC"),
        ),
        source_site=f"{prefix}_A",
        target_site=f"{prefix}_C",
        patches=patches,
    )


def _morphism(
    name: str,
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
    src_prefix: str,
    tgt_prefix: str,
    preserved_dimensions: tuple[str, ...],
) -> D1RestrictionMorphism:
    return D1RestrictionMorphism(
        name=name,
        source=source,
        target=target,
        site_map=(
            SiteMap(f"{src_prefix}_A", f"{tgt_prefix}_A"),
            SiteMap(f"{src_prefix}_B", f"{tgt_prefix}_B"),
            SiteMap(f"{src_prefix}_C", f"{tgt_prefix}_C"),
        ),
        preserved_dimensions=preserved_dimensions,
        require_trust_path_preservation=True,
        require_obstruction_preservation=False,
    )


def _projection_case(
    name: str,
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
    morphism: D1RestrictionMorphism,
    forgotten: tuple[str, ...],
    reading: str,
) -> ProjectionCase:
    return ProjectionCase(
        name=name,
        source="T34_chain",
        richer_system=source,
        restricted_system=target,
        morphism=morphism,
        forgotten_structure=forgotten,
        preserved_structure=("causal_order",),
        intended_reading=reading,
    )


def _checkpoint_pair(
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
    src_prefix: str,
    tgt_prefix: str,
    intermediate_level: str,
    forgotten: tuple[str, ...],
    preserved_dimensions: tuple[str, ...],
) -> CheckpointPair:
    """Build a (source, intermediate) pair and check its admissibility."""
    m = _morphism(
        f"checkpoint_{intermediate_level}",
        source, target, src_prefix, tgt_prefix, preserved_dimensions,
    )
    case = _projection_case(
        f"checkpoint_{intermediate_level}", source, target, m, forgotten,
        f"Source code projects to {intermediate_level}.",
    )
    return CheckpointPair(
        intermediate_level=intermediate_level,
        admissibility=check_admissibility(case),
    )


def _analyze_chain(chain: ProjectionChain) -> ChainAnalysis:
    first_obstructed = "none"
    for link in chain.links:
        if link.target_obstructed:
            first_obstructed = link.target_level
            break

    admissible_checkpoints = tuple(
        cp.intermediate_level
        for cp in chain.checkpoint_pairs
        if cp.admissibility.po1_evidence
    )
    endpoint_po1 = chain.endpoint_admissibility.po1_evidence
    endpoint_verdict = chain.endpoint_admissibility.verdict

    emergent = endpoint_po1 and len(admissible_checkpoints) == 0
    propagated = (
        first_obstructed != "none"
        and endpoint_po1
        and not emergent
    )
    absorbed = (
        first_obstructed != "none"
        and not endpoint_po1
        and chain.endpoint_admissibility.verdict in (
            "non_admissible_no_new_obstruction",
        )
    )

    if emergent:
        conclusion = (
            "EMERGENT OBSTRUCTION: the endpoint pair is a PO1 instance, "
            "but no source→intermediate pair is. "
            f"Obstruction only becomes visible at '{chain.abstraction_levels[-1]}'."
        )
    elif propagated:
        conclusion = (
            "STEPWISE PROPAGATION: obstruction appears at "
            f"'{first_obstructed}' and the endpoint pair is a PO1 instance. "
            f"Admissible source→intermediate pairs: {list(admissible_checkpoints)}."
        )
    elif absorbed:
        conclusion = (
            "ABSORBED OBSTRUCTION: obstruction appeared at "
            f"'{first_obstructed}' but was resolved before the endpoint. "
            "The endpoint pair is NOT a PO1 instance (AC6=False at endpoint)."
        )
    else:
        conclusion = f"Endpoint verdict: {endpoint_verdict}."

    return ChainAnalysis(
        chain=chain,
        step_count=len(chain.links),
        obstruction_first_appears_at=first_obstructed,
        admissible_checkpoint_pairs=admissible_checkpoints,
        emergent_obstruction=emergent,
        stepwise_propagation=propagated,
        absorbed_obstruction=absorbed,
        endpoint_verdict=endpoint_verdict,
        chain_po1_conclusion=conclusion,
    )


# ---------------------------------------------------------------------------
# Case 1: Spectre-class emergent obstruction
# ---------------------------------------------------------------------------


def _spectre_timing_chain() -> ProjectionChain:
    """
    source_code → compiler_IR → assembly → machine_code → microarchitecture

    At source level: the type system enforces memory isolation.
    At each intermediate level: no timing side-channel obstruction is present.
    At microarchitecture: speculative execution creates a 3-patch contradiction:
      (1) access_level determines cache_state (speculation fills cache),
      (2) cache_state determines timing (hit vs miss latency),
      (3) security policy requires timing to be independent of access_level.
    This is the A=B, B=C, A≠C gluing obstruction.

    Emergent claim: (source_code, microarchitecture) IS a PO1 instance, but no
    partial chain (source_code, Li) for intermediate Li is a PO1 instance.
    """
    tag = "T34_spectre"
    # accessible_support encodes "safety structure visible at this level"
    # branch_support encodes "memory isolation guarantee strength"
    L0 = _three_site_system("spec_L0", tag, D1Profile(4, 4, 2, 4), obstructed=False)
    L1 = _three_site_system("spec_L1", tag, D1Profile(3, 3, 2, 3), obstructed=False)
    L2 = _three_site_system("spec_L2", tag, D1Profile(2, 2, 1, 2), obstructed=False)
    L3 = _three_site_system("spec_L3", tag, D1Profile(1, 1, 1, 1), obstructed=False)
    L4 = _three_site_system("spec_L4", tag, D1Profile(1, 1, 0, 1), obstructed=True)

    links = (
        ChainLink("source_to_IR", "source_code", "compiler_IR", L0, L1,
                  ("type_safety_guarantee",), False),
        ChainLink("IR_to_assembly", "compiler_IR", "assembly", L1, L2,
                  ("control_flow_isolation",), False),
        ChainLink("assembly_to_machine", "assembly", "machine_code", L2, L3,
                  ("memory_access_abstraction",), False),
        ChainLink("machine_to_microarch", "machine_code", "microarchitecture", L3, L4,
                  ("execution_order_guarantee",), True),
    )

    # Checkpoint pairs: (source=L0, target=Li) for each intermediate Li
    # Use accessible_support as the declared-preserved dimension that mismatches,
    # so local_profiles_preserved=False and AC5 can be True.
    checkpoint_pairs = (
        _checkpoint_pair(L0, L1, "spec_L0", "spec_L1", "compiler_IR",
                         ("type_safety_guarantee",),
                         ("accessible_support",)),    # 4 → 3: mismatch
        _checkpoint_pair(L0, L2, "spec_L0", "spec_L2", "assembly",
                         ("type_safety_guarantee", "control_flow_isolation"),
                         ("accessible_support",)),    # 4 → 2: mismatch
        _checkpoint_pair(L0, L3, "spec_L0", "spec_L3", "machine_code",
                         ("type_safety_guarantee", "control_flow_isolation",
                          "memory_access_abstraction"),
                         ("accessible_support",)),    # 4 → 1: mismatch
    )

    # Endpoint morphism: source → microarchitecture
    # accessible_support: 4 → 1 (mismatch → local_profiles_preserved=False → AC5)
    m_endpoint = _morphism(
        "spec_source_to_microarch", L0, L4, "spec_L0", "spec_L4",
        ("accessible_support",),
    )
    endpoint_case = _projection_case(
        "spectre_endpoint", L0, L4, m_endpoint,
        ("type_safety_guarantee", "control_flow_isolation",
         "memory_access_abstraction", "execution_order_guarantee"),
        "Source-code type safety does not prevent Spectre-class timing side "
        "channels at the microarchitecture level.",
    )

    return ProjectionChain(
        chain_name="spectre_timing_chain",
        description=(
            "Spectre-class timing side channel: type-safe source code projects "
            "to a microarchitecture where speculative execution creates a "
            "finite gluing obstruction. No partial chain from source reveals "
            "the obstruction."
        ),
        abstraction_levels=("source_code", "compiler_IR", "assembly",
                            "machine_code", "microarchitecture"),
        links=links,
        checkpoint_pairs=checkpoint_pairs,
        endpoint_case=endpoint_case,
        endpoint_admissibility=check_admissibility(endpoint_case),
    )


# ---------------------------------------------------------------------------
# Case 2: Stepwise propagation
# ---------------------------------------------------------------------------


def _stepwise_obstruction_chain() -> ProjectionChain:
    """
    Obstruction appears at step 2 (IR → assembly) and propagates to endpoint.

    source_code → compiler_IR → assembly (obstructed) → machine_code (obstructed)

    The source_code→assembly pair IS individually a PO1 instance (assembly is
    the obstructed intermediate). The source_code→machine_code endpoint pair is
    ALSO a PO1 instance. This is stepwise propagation.
    """
    tag = "T34_step"
    L0 = _three_site_system("step_L0", tag, D1Profile(4, 4, 2, 4), obstructed=False)
    L1 = _three_site_system("step_L1", tag, D1Profile(3, 3, 1, 3), obstructed=False)
    L2 = _three_site_system("step_L2", tag, D1Profile(2, 2, 1, 2), obstructed=True)
    L3 = _three_site_system("step_L3", tag, D1Profile(1, 1, 0, 1), obstructed=True)

    links = (
        ChainLink("source_to_IR_step", "source_code", "compiler_IR", L0, L1,
                  ("abstract_control_flow",), False),
        ChainLink("IR_to_assembly_step", "compiler_IR", "assembly", L1, L2,
                  ("register_allocation_freedom",), True),
        ChainLink("assembly_to_machine_step", "assembly", "machine_code", L2, L3,
                  ("instruction_encoding_freedom",), True),
    )

    # accessible_support: 4 → 3 (no obstruction); 4 → 2 (obstructed); 4 → 1 (obstructed)
    checkpoint_pairs = (
        _checkpoint_pair(L0, L1, "step_L0", "step_L1", "compiler_IR",
                         ("abstract_control_flow",),
                         ("accessible_support",)),  # 4→3: mismatch, L1 unobstructed → AC6=F
        _checkpoint_pair(L0, L2, "step_L0", "step_L2", "assembly",
                         ("abstract_control_flow", "register_allocation_freedom"),
                         ("accessible_support",)),  # 4→2: mismatch, L2 obstructed → PO1
    )

    m_endpoint = _morphism(
        "step_source_to_machine", L0, L3, "step_L0", "step_L3",
        ("accessible_support",),
    )
    endpoint_case = _projection_case(
        "stepwise_endpoint", L0, L3, m_endpoint,
        ("abstract_control_flow", "register_allocation_freedom",
         "instruction_encoding_freedom"),
        "Source-code abstract flow doesn't prevent machine-level register conflicts.",
    )

    return ProjectionChain(
        chain_name="stepwise_obstruction_chain",
        description=(
            "Stepwise propagation: register coloring conflict appears at IR→assembly "
            "step and propagates to machine code. Both source→assembly and "
            "source→machine_code are PO1 instances."
        ),
        abstraction_levels=("source_code", "compiler_IR", "assembly", "machine_code"),
        links=links,
        checkpoint_pairs=checkpoint_pairs,
        endpoint_case=endpoint_case,
        endpoint_admissibility=check_admissibility(endpoint_case),
    )


# ---------------------------------------------------------------------------
# Case 3: Absorbed obstruction (negative control)
# ---------------------------------------------------------------------------


def _absorbed_obstruction_chain() -> ProjectionChain:
    """
    Obstruction appears at the IR level, but the optimizer resolves it.

    source_code → unoptimized_IR (obstructed) → optimized_IR (clean) → assembly

    The source→unoptimized_IR pair IS a PO1 instance (obstruction at IR).
    The source→assembly endpoint pair is NOT a PO1 instance (assembly is clean).

    This case shows that a chain can absorb an intermediate obstruction — if
    structure resolving the obstruction is re-introduced (by optimization), PO1
    does not apply at the endpoint level.
    """
    tag = "T34_absorb"
    L0 = _three_site_system("absorb_L0", tag, D1Profile(4, 4, 2, 4), obstructed=False)
    L1 = _three_site_system("absorb_L1", tag, D1Profile(2, 2, 1, 2), obstructed=True)
    L2 = _three_site_system("absorb_L2", tag, D1Profile(3, 3, 2, 3), obstructed=False)
    L3 = _three_site_system("absorb_L3", tag, D1Profile(1, 1, 1, 1), obstructed=False)

    links = (
        ChainLink("source_to_IR_absorb", "source_code", "unoptimized_IR", L0, L1,
                  ("dead_branch_elimination",), True),
        ChainLink("IR_to_optIR_absorb", "unoptimized_IR", "optimized_IR", L1, L2,
                  (), False),
        ChainLink("optIR_to_assembly_absorb", "optimized_IR", "assembly", L2, L3,
                  ("optimization_annotations",), False),
    )

    # accessible_support: 4→2 (mismatch, L1 obstructed→PO1); 4→3 (mismatch, L2 clean→no PO1)
    checkpoint_pairs = (
        _checkpoint_pair(L0, L1, "absorb_L0", "absorb_L1", "unoptimized_IR",
                         ("dead_branch_elimination",),
                         ("accessible_support",)),  # 4→2: mismatch, L1 obstructed → PO1
        _checkpoint_pair(L0, L2, "absorb_L0", "absorb_L2", "optimized_IR",
                         ("dead_branch_elimination",),
                         ("accessible_support",)),  # 4→3: mismatch, L2 clean → not PO1
    )

    m_endpoint = _morphism(
        "absorb_source_to_assembly", L0, L3, "absorb_L0", "absorb_L3",
        ("accessible_support",),
    )
    endpoint_case = _projection_case(
        "absorbed_endpoint", L0, L3, m_endpoint,
        ("dead_branch_elimination",),
        "Dead-code elimination resolved the IR contradiction; assembly is clean.",
    )

    return ProjectionChain(
        chain_name="absorbed_obstruction_chain",
        description=(
            "Absorbed obstruction: phi-node contradiction at IR level is resolved "
            "by dead-code elimination before assembly. The endpoint is NOT a PO1 instance."
        ),
        abstraction_levels=("source_code", "unoptimized_IR", "optimized_IR", "assembly"),
        links=links,
        checkpoint_pairs=checkpoint_pairs,
        endpoint_case=endpoint_case,
        endpoint_admissibility=check_admissibility(endpoint_case),
    )


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------


def run_t34_analysis() -> T34Result:
    spectre_chain = _analyze_chain(_spectre_timing_chain())
    stepwise_chain = _analyze_chain(_stepwise_obstruction_chain())
    absorbed_chain = _analyze_chain(_absorbed_obstruction_chain())

    return T34Result(
        spectre_chain=spectre_chain,
        stepwise_chain=stepwise_chain,
        absorbed_chain=absorbed_chain,
        emergent_obstruction_confirmed=spectre_chain.emergent_obstruction,
        absorbed_obstruction_confirmed=absorbed_chain.absorbed_obstruction,
        stepwise_propagation_confirmed=stepwise_chain.stepwise_propagation,
        po1_chain_theorem=(
            "PO1 CHAIN THEOREM (T34): "
            "A chained projection is a PO1 instance when its endpoint pair "
            "satisfies AC1-AC7, independent of whether any source→intermediate "
            "pair in the chain is a PO1 instance. "
            "EMERGENT CASE: the obstruction at the endpoint is invisible when "
            "looking at source→Li for any intermediate Li; only the full chain "
            "endpoint reveals the PO1 instance (Spectre case). "
            "ABSORBED CASE: a PO1 instance visible at an intermediate level "
            "can be resolved before the endpoint; the chain theorem does not "
            "guarantee PO1 persists to the endpoint."
        ),
        boundary=(
            "T34 boundary: the chain theorem characterizes the endpoint pair only. "
            "It does not localize which step in the chain is responsible for the "
            "obstruction. The Spectre case models the timing side channel as a "
            "finite 3-patch local-to-global constraint contradiction. Physical "
            "Spectre attacks involve probabilistic timing and micro-op semantics "
            "not captured here. The optimized_IR level in the absorbed case has a "
            "higher accessible_support than the input IR — this models the optimizer "
            "recovering structure — which is unusual for a restriction projection "
            "and marks a boundary of the current T26 morphism formalism."
        ),
        recommendation=(
            "Extend PO1 with a formal chain composition theorem: given a chain "
            "f1∘f2∘...∘fn: L0→Ln where each fi is a D1RestrictionMorphism, "
            "the composed projection is a PO1 instance iff (L0, Ln) is admissible. "
            "AC5 (named forgetting) should accumulate across steps: the endpoint "
            "forgotten_structure should include all structure lost at any step. "
            "This is modeled in the Spectre case and is the natural next target "
            "for a composition law (Best First Contribution #2 in ROADMAP.md)."
        ),
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _link_dict(link: ChainLink) -> dict[str, Any]:
    return {
        "step_name": link.step_name,
        "source_level": link.source_level,
        "target_level": link.target_level,
        "forgotten_at_this_step": list(link.forgotten_at_this_step),
        "target_obstructed": link.target_obstructed,
    }


def _checkpoint_dict(cp: CheckpointPair) -> dict[str, Any]:
    return {
        "intermediate_level": cp.intermediate_level,
        "verdict": cp.admissibility.verdict,
        "is_po1": cp.admissibility.po1_evidence,
        "ac6_restricted_obstructed": cp.admissibility.ac6_restricted_obstructed,
        "ac5_structure_forgotten": cp.admissibility.ac5_structure_forgotten,
    }


def _chain_analysis_dict(ca: ChainAnalysis) -> dict[str, Any]:
    return {
        "chain_name": ca.chain.chain_name,
        "description": ca.chain.description,
        "abstraction_levels": list(ca.chain.abstraction_levels),
        "step_count": ca.step_count,
        "steps": [_link_dict(link) for link in ca.chain.links],
        "checkpoint_pairs": [_checkpoint_dict(cp) for cp in ca.chain.checkpoint_pairs],
        "admissible_checkpoint_pairs": list(ca.admissible_checkpoint_pairs),
        "obstruction_first_appears_at": ca.obstruction_first_appears_at,
        "emergent_obstruction": ca.emergent_obstruction,
        "stepwise_propagation": ca.stepwise_propagation,
        "absorbed_obstruction": ca.absorbed_obstruction,
        "endpoint_verdict": ca.endpoint_verdict,
        "endpoint_ac_vector": {
            "AC1": ca.chain.endpoint_admissibility.ac1_richer_valid,
            "AC2": ca.chain.endpoint_admissibility.ac2_restricted_valid,
            "AC3": ca.chain.endpoint_admissibility.ac3_projection_definable,
            "AC4": ca.chain.endpoint_admissibility.ac4_local_compat,
            "AC5": ca.chain.endpoint_admissibility.ac5_structure_forgotten,
            "AC6": ca.chain.endpoint_admissibility.ac6_restricted_obstructed,
            "AC7": ca.chain.endpoint_admissibility.ac7_richer_unobstructed,
        },
        "chain_po1_conclusion": ca.chain_po1_conclusion,
    }


def t34_result_to_dict(result: T34Result) -> dict[str, Any]:
    return {
        "spectre_chain": _chain_analysis_dict(result.spectre_chain),
        "stepwise_chain": _chain_analysis_dict(result.stepwise_chain),
        "absorbed_chain": _chain_analysis_dict(result.absorbed_chain),
        "emergent_obstruction_confirmed": result.emergent_obstruction_confirmed,
        "absorbed_obstruction_confirmed": result.absorbed_obstruction_confirmed,
        "stepwise_propagation_confirmed": result.stepwise_propagation_confirmed,
        "po1_chain_theorem": result.po1_chain_theorem,
        "boundary": result.boundary,
        "recommendation": result.recommendation,
    }
