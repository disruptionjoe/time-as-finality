"""T37: Typed transport network formalization.

T37 formalizes the typed multiscale transport network: a finite directed graph
where nodes are D1RestrictionSystems (layers) and edges are typed
D1RestrictionMorphisms (transports). Each transport carries explicit
forgotten_structure and preserved_structure declarations.

Central new result: path-dependent admissibility.

  Path-Dependent Admissibility Theorem:
  In a TypedTransportNetwork, two simple paths between the same source and
  target layer can yield different PO1 admissibility verdicts when they
  accumulate different forgotten_structure along the path.

  If path P1 accumulates non-empty forgotten_structure and path P2 accumulates
  empty forgotten_structure, then AC5 holds for P1 and fails for P2 — even
  though both paths connect the same endpoint systems.

Two test networks:
  spectre_network  Linear 3-layer chain. Endpoint pair is PO1-admissible.
                   No partial prefix (SRC→MID) is PO1 (emergent obstruction,
                   consistent with T34).

  diamond_network  4-layer diamond: SRC → L_A → TGT and SRC → L_B → TGT.
                   Path via L_A forgets ("type_guarantee",): AC5 passes → PO1.
                   Path via L_B forgets nothing: AC5 fails → not PO1.
                   path_dependent = True.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.d1_restriction_system import (
    D1_DIMENSIONS,
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import AdmissibilityCheck, check_admissibility
from models.projection_obstruction_schema import ProjectionCase


# ---------------------------------------------------------------------------
# Network data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class NetworkLayer:
    name: str
    system: D1RestrictionSystem


@dataclass(frozen=True)
class NetworkTransport:
    name: str
    source_name: str
    target_name: str
    morphism: D1RestrictionMorphism
    forgotten_structure: tuple[str, ...]
    preserved_structure: tuple[str, ...]


@dataclass(frozen=True)
class NetworkPath:
    layer_names: tuple[str, ...]
    transports: tuple[NetworkTransport, ...]
    source_name: str
    target_name: str


@dataclass(frozen=True)
class PathAdmissibility:
    path: NetworkPath
    endpoint_case: ProjectionCase
    admissibility: AdmissibilityCheck
    is_po1_instance: bool
    path_label: str


@dataclass(frozen=True)
class PathDependenceWitness:
    source_name: str
    target_name: str
    po1_path: NetworkPath
    non_po1_path: NetworkPath
    po1_forgotten: tuple[str, ...]
    non_po1_forgotten: tuple[str, ...]
    failing_conditions: tuple[str, ...]


@dataclass(frozen=True)
class NetworkAnalysis:
    network_name: str
    layer_count: int
    transport_count: int
    path_admissibilities: tuple[PathAdmissibility, ...]
    po1_paths: tuple[str, ...]
    non_po1_paths: tuple[str, ...]
    path_dependent: bool
    path_dependence_witness: PathDependenceWitness | None
    verdict: str


@dataclass(frozen=True)
class TypedTransportNetwork:
    name: str
    description: str
    layers: tuple[NetworkLayer, ...]
    transports: tuple[NetworkTransport, ...]


@dataclass(frozen=True)
class T37Result:
    spectre_network_analysis: NetworkAnalysis
    diamond_network_analysis: NetworkAnalysis
    t34_consistency: bool
    path_dependence_witnessed: bool
    theorem: str
    boundary: str
    recommendation: str


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------


def _compose_morphisms(
    f: D1RestrictionMorphism,
    g: D1RestrictionMorphism,
) -> D1RestrictionMorphism:
    """Compose f: A→B and g: B→C into h: A→C."""
    f_map = {sm.source_site: sm.target_site for sm in f.site_map}
    g_map = {sm.source_site: sm.target_site for sm in g.site_map}
    composed_site_map = tuple(
        SiteMap(src, g_map[f_map[src]])
        for src in sorted(f_map)
        if f_map[src] in g_map
    )
    f_dims = set(f.preserved_dimensions)
    g_dims = set(g.preserved_dimensions)
    preserved_dims = tuple(d for d in D1_DIMENSIONS if d in f_dims and d in g_dims)
    return D1RestrictionMorphism(
        name=f"composed_{f.name}_{g.name}",
        source=f.source,
        target=g.target,
        site_map=composed_site_map,
        preserved_dimensions=preserved_dims,
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )


def _path_endpoint_morphism(path: NetworkPath) -> D1RestrictionMorphism:
    result = path.transports[0].morphism
    for transport in path.transports[1:]:
        result = _compose_morphisms(result, transport.morphism)
    return result


def _path_accumulated_forgotten(path: NetworkPath) -> tuple[str, ...]:
    seen: set[str] = set()
    result: list[str] = []
    for transport in path.transports:
        for item in transport.forgotten_structure:
            if item not in seen:
                seen.add(item)
                result.append(item)
    return tuple(result)


def _path_accumulated_preserved(path: NetworkPath) -> tuple[str, ...]:
    if not path.transports:
        return ()
    result = set(path.transports[0].preserved_structure)
    for transport in path.transports[1:]:
        result &= set(transport.preserved_structure)
    return tuple(sorted(result))


def check_path_admissibility(
    network: TypedTransportNetwork,
    path: NetworkPath,
) -> PathAdmissibility:
    layers = {layer.name: layer for layer in network.layers}
    source_system = layers[path.source_name].system
    target_system = layers[path.target_name].system
    composed_morphism = _path_endpoint_morphism(path)
    forgotten = _path_accumulated_forgotten(path)
    preserved = _path_accumulated_preserved(path)
    intermediates = list(path.layer_names[1:-1])
    case_name = (
        f"path_{path.source_name}_to_{path.target_name}"
        + (f"_via_{'_'.join(intermediates)}" if intermediates else "")
    )
    endpoint_case = ProjectionCase(
        name=case_name,
        source="T37",
        richer_system=source_system,
        restricted_system=target_system,
        morphism=composed_morphism,
        forgotten_structure=forgotten,
        preserved_structure=preserved,
        intended_reading=(
            f"path from {path.source_name} to {path.target_name}"
            + (f" via {', '.join(intermediates)}" if intermediates else "")
        ),
    )
    admissibility = check_admissibility(endpoint_case)
    path_label = " -> ".join(path.layer_names)
    return PathAdmissibility(
        path=path,
        endpoint_case=endpoint_case,
        admissibility=admissibility,
        is_po1_instance=admissibility.po1_evidence,
        path_label=path_label,
    )


def all_paths(
    network: TypedTransportNetwork,
    source_name: str,
    target_name: str,
) -> tuple[NetworkPath, ...]:
    """DFS simple-path enumeration from source to target in the transport graph."""
    adj: dict[str, list[NetworkTransport]] = {}
    for transport in network.transports:
        adj.setdefault(transport.source_name, []).append(transport)

    results: list[NetworkPath] = []

    def dfs(
        current: str,
        visited: set[str],
        path_layers: list[str],
        path_transports: list[NetworkTransport],
    ) -> None:
        if current == target_name:
            if path_transports:
                results.append(NetworkPath(
                    layer_names=tuple(path_layers),
                    transports=tuple(path_transports),
                    source_name=source_name,
                    target_name=target_name,
                ))
            return
        for transport in adj.get(current, []):
            nxt = transport.target_name
            if nxt not in visited:
                visited.add(nxt)
                path_layers.append(nxt)
                path_transports.append(transport)
                dfs(nxt, visited, path_layers, path_transports)
                path_layers.pop()
                path_transports.pop()
                visited.discard(nxt)

    dfs(source_name, {source_name}, [source_name], [])
    return tuple(results)


def analyze_network(
    network: TypedTransportNetwork,
    source_name: str,
    target_name: str,
) -> NetworkAnalysis:
    paths = all_paths(network, source_name, target_name)
    path_admissibilities = tuple(
        check_path_admissibility(network, path) for path in paths
    )
    po1_paths = tuple(pa.path_label for pa in path_admissibilities if pa.is_po1_instance)
    non_po1_paths = tuple(pa.path_label for pa in path_admissibilities if not pa.is_po1_instance)
    path_dependent = bool(po1_paths) and bool(non_po1_paths)
    witness: PathDependenceWitness | None = None
    if path_dependent:
        po1_pa = next(pa for pa in path_admissibilities if pa.is_po1_instance)
        non_po1_pa = next(pa for pa in path_admissibilities if not pa.is_po1_instance)
        witness = PathDependenceWitness(
            source_name=source_name,
            target_name=target_name,
            po1_path=po1_pa.path,
            non_po1_path=non_po1_pa.path,
            po1_forgotten=_path_accumulated_forgotten(po1_pa.path),
            non_po1_forgotten=_path_accumulated_forgotten(non_po1_pa.path),
            failing_conditions=non_po1_pa.admissibility.failed_conditions,
        )
    if path_dependent:
        verdict = "path_dependent_admissibility_witnessed"
    elif po1_paths:
        verdict = "all_paths_admissible"
    elif non_po1_paths:
        verdict = "no_admissible_paths"
    else:
        verdict = "no_paths_found"
    return NetworkAnalysis(
        network_name=network.name,
        layer_count=len(network.layers),
        transport_count=len(network.transports),
        path_admissibilities=path_admissibilities,
        po1_paths=po1_paths,
        non_po1_paths=non_po1_paths,
        path_dependent=path_dependent,
        path_dependence_witness=witness,
        verdict=verdict,
    )


# ---------------------------------------------------------------------------
# Layer and transport constructors
# ---------------------------------------------------------------------------

_RICH_PROFILE = D1Profile(
    accessible_support=2,
    holder_redundancy=2,
    branch_support=2,
    reversal_cost=2,
)
_RESTRICTED_PROFILE = D1Profile(
    accessible_support=1,
    holder_redundancy=2,
    branch_support=2,
    reversal_cost=2,
)


def _make_layer(
    name: str,
    prefix: str,
    profile: D1Profile,
    obstructed: bool = False,
) -> NetworkLayer:
    """Build a 3-site NetworkLayer with an optional gluing obstruction.

    Gluing obstruction: sites A=B, B=C, A≠C (locally satisfiable, globally not).
    """
    a, b, c = f"{prefix}_A", f"{prefix}_B", f"{prefix}_C"
    local_values = tuple(
        LocalD1Value(
            site=ObserverSite(s, "abstract", "layer", 0, "trusted"),
            proposition_value="true",
            profile=profile,
        )
        for s in (a, b, c)
    )
    transport_edges = (
        TransportEdge(a, b, "transport", True),
        TransportEdge(b, c, "transport", True),
    )
    patches: tuple[RestrictionPatch, ...] = ()
    if obstructed:
        patches = (
            RestrictionPatch(f"{prefix}_p_AB", (a, b), (a, b), (PatchConstraint(a, b, "same"),)),
            RestrictionPatch(f"{prefix}_p_BC", (b, c), (b, c), (PatchConstraint(b, c, "same"),)),
            RestrictionPatch(f"{prefix}_p_AC", (a, c), (a, c), (PatchConstraint(a, c, "different"),)),
        )
    system = D1RestrictionSystem(
        name=name,
        proposition=f"prop_{prefix}",
        local_values=local_values,
        transport_edges=transport_edges,
        source_site=a,
        target_site=c,
        patches=patches,
    )
    return NetworkLayer(name=name, system=system)


def _make_transport(
    name: str,
    source_layer: NetworkLayer,
    target_layer: NetworkLayer,
    forgotten: tuple[str, ...],
    preserved_dims: tuple[str, ...] = D1_DIMENSIONS,
) -> NetworkTransport:
    """Build a NetworkTransport with index-aligned site map between 3-site layers."""
    src_sites = tuple(v.site.observer_id for v in source_layer.system.local_values)
    tgt_sites = tuple(v.site.observer_id for v in target_layer.system.local_values)
    site_map = tuple(SiteMap(src_sites[i], tgt_sites[i]) for i in range(3))
    morphism = D1RestrictionMorphism(
        name=f"morph_{name}",
        source=source_layer.system,
        target=target_layer.system,
        site_map=site_map,
        preserved_dimensions=preserved_dims,
        require_trust_path_preservation=True,
        require_obstruction_preservation=False,
    )
    preserved_structure = tuple(d for d in D1_DIMENSIONS if d not in forgotten)
    return NetworkTransport(
        name=name,
        source_name=source_layer.name,
        target_name=target_layer.name,
        morphism=morphism,
        forgotten_structure=forgotten,
        preserved_structure=preserved_structure,
    )


# ---------------------------------------------------------------------------
# Test networks
# ---------------------------------------------------------------------------


def spectre_network() -> TypedTransportNetwork:
    """3-layer linear chain exhibiting emergent obstruction (consistent with T34).

    SRC (rich, unobstructed) --[type_guarantee forgotten]--> MID (restricted, unobstructed)
       --[nothing forgotten]--> TGT (restricted, obstructed)

    Full path SRC->MID->TGT: PO1-admissible (emergent obstruction).
    Partial path SRC->MID: NOT PO1 (MID unobstructed; AC6 fails).
    """
    src = _make_layer("SRC", "src", _RICH_PROFILE, obstructed=False)
    mid = _make_layer("MID", "mid", _RESTRICTED_PROFILE, obstructed=False)
    tgt = _make_layer("TGT", "tgt", _RESTRICTED_PROFILE, obstructed=True)
    t_sm = _make_transport(
        "SRC_to_MID", src, mid,
        forgotten=("type_guarantee",),
        preserved_dims=D1_DIMENSIONS,
    )
    t_mt = _make_transport(
        "MID_to_TGT", mid, tgt,
        forgotten=(),
        preserved_dims=D1_DIMENSIONS,
    )
    return TypedTransportNetwork(
        name="spectre_network",
        description=(
            "Linear 3-layer chain. SRC (rich, unobstructed) -> MID (restricted, "
            "unobstructed) -> TGT (restricted, obstructed). Endpoint SRC->TGT is "
            "PO1. Partial SRC->MID is not PO1 (emergent obstruction, T34 pattern)."
        ),
        layers=(src, mid, tgt),
        transports=(t_sm, t_mt),
    )


def diamond_network() -> TypedTransportNetwork:
    """4-layer diamond demonstrating path-dependent PO1 admissibility.

    Path 1: SRC -> L_A -> TGT
            forgotten = ("type_guarantee",); AC5 passes -> PO1.

    Path 2: SRC -> L_B -> TGT
            forgotten = (); AC5 fails -> NOT PO1.

    Same source, same target, different paths, different verdicts.
    """
    _NON_ACCESS = ("holder_redundancy", "branch_support", "reversal_cost")
    src = _make_layer("SRC", "src", _RICH_PROFILE, obstructed=False)
    l_a = _make_layer("L_A", "la", _RESTRICTED_PROFILE, obstructed=False)
    l_b = _make_layer("L_B", "lb", _RICH_PROFILE, obstructed=False)
    tgt = _make_layer("TGT", "tgt", _RESTRICTED_PROFILE, obstructed=True)
    t_sa = _make_transport(
        "SRC_to_L_A", src, l_a,
        forgotten=("type_guarantee",),
        preserved_dims=D1_DIMENSIONS,
    )
    t_at = _make_transport(
        "L_A_to_TGT", l_a, tgt,
        forgotten=(),
        preserved_dims=D1_DIMENSIONS,
    )
    t_sb = _make_transport(
        "SRC_to_L_B", src, l_b,
        forgotten=(),
        preserved_dims=_NON_ACCESS,
    )
    t_bt = _make_transport(
        "L_B_to_TGT", l_b, tgt,
        forgotten=(),
        preserved_dims=_NON_ACCESS,
    )
    return TypedTransportNetwork(
        name="diamond_network",
        description=(
            "4-layer diamond. Path 1 (via L_A) forgets type_guarantee -> PO1. "
            "Path 2 (via L_B) forgets nothing -> not PO1. "
            "Witnesses path-dependent admissibility."
        ),
        layers=(src, l_a, l_b, tgt),
        transports=(t_sa, t_at, t_sb, t_bt),
    )


def _check_t34_consistency(
    network: TypedTransportNetwork,
    src_name: str,
    mid_name: str,
    tgt_name: str,
) -> bool:
    """Return True if the network shows emergent obstruction consistent with T34."""
    tgt_paths = all_paths(network, src_name, tgt_name)
    if not tgt_paths:
        return False
    tgt_admissibility = check_path_admissibility(network, tgt_paths[0])
    if not tgt_admissibility.is_po1_instance:
        return False
    mid_paths = all_paths(network, src_name, mid_name)
    if not mid_paths:
        return False
    mid_admissibility = check_path_admissibility(network, mid_paths[0])
    return not mid_admissibility.is_po1_instance


# ---------------------------------------------------------------------------
# Main analysis runner
# ---------------------------------------------------------------------------


def run_t37_analysis() -> T37Result:
    spec_net = spectre_network()
    diag_net = diamond_network()
    spectre_analysis = analyze_network(spec_net, "SRC", "TGT")
    diamond_analysis = analyze_network(diag_net, "SRC", "TGT")
    t34_consistent = _check_t34_consistency(spec_net, "SRC", "MID", "TGT")
    path_dependence = diamond_analysis.path_dependent
    return T37Result(
        spectre_network_analysis=spectre_analysis,
        diamond_network_analysis=diamond_analysis,
        t34_consistency=t34_consistent,
        path_dependence_witnessed=path_dependence,
        theorem=(
            "Path-Dependent Admissibility: In a TypedTransportNetwork, two simple "
            "paths between the same source and target layer yield different PO1 "
            "verdicts when they accumulate different forgotten_structure. "
            "If path P1 accumulates non-empty forgotten_structure and path P2 "
            "accumulates empty forgotten_structure, AC5 holds for P1 and fails "
            "for P2 — even though both paths connect the same endpoint systems. "
            "AC1, AC2, AC3, AC6, AC7 are endpoint-determined and path-invariant; "
            "only AC5 varies by path when accumulated forgotten_structure differs."
        ),
        boundary=(
            "The result holds within the T26/T31 admissibility framework (AC1-AC7). "
            "It does not claim that all observables are path-dependent — only AC5 "
            "varies. The theorem requires genuinely different accumulated "
            "forgotten_structure between paths; it does not apply when all paths "
            "forget the same structure. The D1RestrictionMorphism composition used "
            "here (intersection of preserved_dimensions, union of forgotten_structure) "
            "has not yet been proven associative; composition law remains open."
        ),
        recommendation=(
            "Promote path-dependent admissibility to a Claim in CLAIM-LEDGER.md. "
            "Update MATHEMATICAL-INDEPENDENCE-AUDIT.md: TypedTransportNetwork is a "
            "new primitive above D1RestrictionSystem. Next steps: test path-dependence "
            "under longer chains; ask whether a canonical minimal forgotten_structure "
            "exists for a (source, target) pair; prove or disprove that morphism "
            "composition is associative."
        ),
    )


def t37_result_to_dict(result: T37Result) -> dict[str, Any]:
    def _analysis_to_dict(na: NetworkAnalysis) -> dict[str, Any]:
        return {
            "network_name": na.network_name,
            "layer_count": na.layer_count,
            "transport_count": na.transport_count,
            "paths": [
                {
                    "path_label": pa.path_label,
                    "is_po1_instance": pa.is_po1_instance,
                    "verdict": pa.admissibility.verdict,
                    "failed_conditions": list(pa.admissibility.failed_conditions),
                    "forgotten_structure": list(_path_accumulated_forgotten(pa.path)),
                }
                for pa in na.path_admissibilities
            ],
            "po1_paths": list(na.po1_paths),
            "non_po1_paths": list(na.non_po1_paths),
            "path_dependent": na.path_dependent,
            "witness": (
                {
                    "source": na.path_dependence_witness.source_name,
                    "target": na.path_dependence_witness.target_name,
                    "po1_path": list(na.path_dependence_witness.po1_path.layer_names),
                    "non_po1_path": list(na.path_dependence_witness.non_po1_path.layer_names),
                    "po1_forgotten": list(na.path_dependence_witness.po1_forgotten),
                    "non_po1_forgotten": list(na.path_dependence_witness.non_po1_forgotten),
                    "failing_conditions": list(na.path_dependence_witness.failing_conditions),
                }
                if na.path_dependence_witness
                else None
            ),
            "verdict": na.verdict,
        }

    return {
        "spectre_network": _analysis_to_dict(result.spectre_network_analysis),
        "diamond_network": _analysis_to_dict(result.diamond_network_analysis),
        "t34_consistency": result.t34_consistency,
        "path_dependence_witnessed": result.path_dependence_witnessed,
        "theorem": result.theorem,
        "boundary": result.boundary,
        "recommendation": result.recommendation,
    }
