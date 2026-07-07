"""T484: transport-topology refinement naturalness gate.

T483 admitted a fixed-D1 transport-topology generator only as future review
metadata. This module tests the next burden: the topology generator must be
stable under benign transport-graph refinements before it can be treated even
as disciplined review bookkeeping.

The positive result is intentionally narrow. Source/target reachability roles
for the original T24/T38 observers are invariant under edge subdivision and
observer-label relabeling. Component size and shortest-path length are not
invariant under the same refinement, so they are rejected as scale-like
overreads. The result earns no internal scale structure, clock, duration,
record-finality change, scale-genesis theorem, physics support, claim
movement, or public-posture movement.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from models.internal_scale_generator_independence_gate import run as run_t483
from models.multiscale_observer_field import (
    D1FieldScenario,
    FieldEdge,
    ObserverProfile,
    connected_transport_scenario,
    partitioned_transport_scenario,
)


ARTIFACT_ID = "T484-transport-topology-refinement-naturalness-gate-v0.1"
VERDICT = "TRANSPORT_TOPOLOGY_REFINEMENT_GATE_BUILT_REACHABILITY_BOOKKEEPING_ONLY"


@dataclass(frozen=True)
class RefinementCandidate:
    """One proposed post-T483 transport-topology review packet."""

    candidate_id: str
    role: str
    generator_rule: str
    comparison_domain: str
    local_taf_anchor: str
    predeclared_generator: bool
    fixed_d1_counterfactual_control_declared: bool
    refinement_invariance_check_declared: bool
    relabel_invariance_check_declared: bool
    uses_reachability_relation: bool = False
    uses_component_size: bool = False
    uses_path_length_metric: bool = False
    label_only_without_generator: bool = False
    uses_observer_id_order: bool = False
    uses_hidden_calendar_or_time_order: bool = False
    derives_clock_duration_or_arrow: bool = False
    changes_record_finality: bool = False
    imports_rg_or_conformal_mechanism: bool = False
    claims_scale_genesis_or_physics: bool = False
    requests_claim_or_posture_promotion: bool = False


def refinement_candidates() -> tuple[RefinementCandidate, ...]:
    """Return the finite T484 candidate catalogue."""

    return (
        RefinementCandidate(
            candidate_id="source_target_reachability_packet",
            role="positive_review_control",
            generator_rule=(
                "classify original observer sites by trust-preserving component "
                "role relative to the declared source and target"
            ),
            comparison_domain=(
                "T24/T38 connected and partitioned transport fixtures, plus "
                "edge-subdivided refinements over the same original observer sites"
            ),
            local_taf_anchor="T24/T38/T480/T481/T482/T483",
            predeclared_generator=True,
            fixed_d1_counterfactual_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_reachability_relation=True,
        ),
        RefinementCandidate(
            candidate_id="component_size_as_scale",
            role="hostile_control",
            generator_rule="use the size of the source/target transport component as scale",
            comparison_domain="T24/T38 connected and subdivided transport fixtures",
            local_taf_anchor="T483 overread",
            predeclared_generator=True,
            fixed_d1_counterfactual_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_component_size=True,
        ),
        RefinementCandidate(
            candidate_id="shortest_path_length_as_scale",
            role="hostile_control",
            generator_rule="use source-to-target shortest path length as scale",
            comparison_domain="T24/T38 connected and subdivided transport fixtures",
            local_taf_anchor="T483 overread",
            predeclared_generator=True,
            fixed_d1_counterfactual_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_path_length_metric=True,
        ),
        RefinementCandidate(
            candidate_id="label_word_topology_scale",
            role="hostile_control",
            generator_rule="call the transport component an internal scale",
            comparison_domain="component labels",
            local_taf_anchor="T483 shortcut",
            predeclared_generator=False,
            fixed_d1_counterfactual_control_declared=True,
            refinement_invariance_check_declared=False,
            relabel_invariance_check_declared=False,
            label_only_without_generator=True,
        ),
        RefinementCandidate(
            candidate_id="observer_id_component_order",
            role="hostile_control",
            generator_rule="rank components by observer identifier order",
            comparison_domain="observer-id labels",
            local_taf_anchor="T24 labels only",
            predeclared_generator=True,
            fixed_d1_counterfactual_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_observer_id_order=True,
        ),
        RefinementCandidate(
            candidate_id="relay_count_as_clock",
            role="hostile_control",
            generator_rule="treat added relay count as elapsed record time",
            comparison_domain="subdivision relay metadata",
            local_taf_anchor="T24/T38 overread",
            predeclared_generator=True,
            fixed_d1_counterfactual_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_hidden_calendar_or_time_order=True,
            derives_clock_duration_or_arrow=True,
        ),
        RefinementCandidate(
            candidate_id="record_finality_by_reachability",
            role="hostile_control",
            generator_rule="mark source-target reachable sites as final",
            comparison_domain="transport reachability roles",
            local_taf_anchor="T483 overread",
            predeclared_generator=True,
            fixed_d1_counterfactual_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_reachability_relation=True,
            changes_record_finality=True,
        ),
        RefinementCandidate(
            candidate_id="rg_fixed_point_topology_source",
            role="hostile_control",
            generator_rule="import RG or conformal fixed point as topology source",
            comparison_domain="external RG scale classes",
            local_taf_anchor="external RG/conformal mechanism",
            predeclared_generator=True,
            fixed_d1_counterfactual_control_declared=False,
            refinement_invariance_check_declared=False,
            relabel_invariance_check_declared=False,
            imports_rg_or_conformal_mechanism=True,
            claims_scale_genesis_or_physics=True,
        ),
        RefinementCandidate(
            candidate_id="promotion_shortcut_topology",
            role="hostile_control",
            generator_rule="declare refinement-stable reachability to be internal scale",
            comparison_domain="T24/T38 transport fixtures",
            local_taf_anchor="T24/T38/T483 promotion shortcut",
            predeclared_generator=True,
            fixed_d1_counterfactual_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_reachability_relation=True,
            claims_scale_genesis_or_physics=True,
            requests_claim_or_posture_promotion=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T484 transport-topology refinement naturalness gate."""

    anchor_checks = _anchor_checks()
    refinement_probe = _refinement_probe()
    evaluations = [
        _evaluate_candidate(candidate, anchor_checks, refinement_probe)
        for candidate in refinement_candidates()
    ]
    admitted = [row["candidate_id"] for row in evaluations if row["admitted"]]
    hostile_violations = [
        row["candidate_id"]
        for row in evaluations
        if row["role"] == "hostile_control" and row["admitted"]
    ]
    expected_admissions = ["source_target_reachability_packet"]
    component_size_blocked = _candidate_decision(
        evaluations,
        "component_size_as_scale",
    )["decision"] == "reject_refinement_variant"
    path_length_blocked = _candidate_decision(
        evaluations,
        "shortest_path_length_as_scale",
    )["decision"] == "reject_refinement_variant"
    gate_passed = (
        anchor_checks["t483_gate_passed"]
        and anchor_checks["t483_transport_topology_review_target_admitted"]
        and refinement_probe["controls"]["original_d1_vectors_fixed"]
        and refinement_probe["controls"]["reachability_separates_fixed_d1_pair"]
        and refinement_probe["controls"]["connected_refinement_preserves_original_roles"]
        and refinement_probe["controls"]["partitioned_refinement_preserves_original_roles"]
        and refinement_probe["controls"]["reachability_relabel_invariant"]
        and refinement_probe["controls"]["component_size_changes_under_refinement"]
        and refinement_probe["controls"]["path_length_changes_under_refinement"]
        and admitted == expected_admissions
        and component_size_blocked
        and path_length_blocked
        and not hostile_violations
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Test whether T483's transport-topology review target survives "
            "benign graph refinement as reachability bookkeeping only, while "
            "rejecting refinement-sensitive scale overreads."
        ),
        "local_anchor_checks": anchor_checks,
        "refinement_probe": refinement_probe,
        "candidate_evaluations": evaluations,
        "admitted_candidate_ids": admitted,
        "hostile_violations": hostile_violations,
        "overall_verdict": {
            "verdict": VERDICT,
            "gate_passed": gate_passed,
            "reachability_packet_admitted": admitted == expected_admissions,
            "component_size_scale_blocked": component_size_blocked,
            "path_length_scale_blocked": path_length_blocked,
            "hostile_controls_blocked": not hostile_violations,
            "internal_scale_structure_earned": False,
            "claim_ledger_update": "none",
            "north_star_update": "none",
            "roadmap_update": "none",
            "public_posture_update": "none",
            "physics_claim_earned": False,
            "scale_genesis_theorem_earned": False,
            "record_clock_or_duration_earned": False,
            "record_finality_change_earned": False,
            "reading": (
                "T484 narrows the T483 transport-topology review target. "
                "Source/target reachability roles for the original T24/T38 "
                "observer sites are stable under edge subdivision and "
                "observer-label relabeling, so they remain admitted as "
                "review-grade reachability bookkeeping. Component size and "
                "shortest-path length change under the same benign refinement, "
                "so they are rejected as internal-scale, clock, duration, "
                "finality, or scale-genesis evidence."
            ),
        },
        "future_packet_minimum": [
            "treat fixed-D1 topology separation as reachability bookkeeping unless a separate theorem earns more",
            "include transport-refinement controls before using topology as a generator",
            "reject component-size and path-length scale readings unless an invariant morphism class is declared",
            "preserve observer-label relabel invariance",
            "separate reachability topology from scale, clock, duration, finality, RG/conformal, physics, and promotion language",
        ],
        "not_earned": [
            "independent internal scale structure",
            "record clock",
            "duration or temporal arrow",
            "record-finality change",
            "scale-genesis theorem",
            "physics or conformal-gravity claim",
            "D1 promotion",
            "RG/TaF equivalence theorem",
            "claim-ledger movement",
            "roadmap movement",
            "North Star movement",
            "public-posture movement",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Render T484 results as Markdown."""

    verdict = result["overall_verdict"]
    anchor_rows = [
        f"| {key} | {value} |"
        for key, value in result["local_anchor_checks"].items()
    ]
    control_rows = [
        f"| {key} | {value} |"
        for key, value in result["refinement_probe"]["controls"].items()
    ]
    connected_rows = _assignment_rows(
        result["refinement_probe"]["connected_original_assignments"],
    )
    connected_refined_rows = _assignment_rows(
        result["refinement_probe"]["connected_refined_original_assignments"],
    )
    partitioned_rows = _assignment_rows(
        result["refinement_probe"]["partitioned_original_assignments"],
    )
    partitioned_refined_rows = _assignment_rows(
        result["refinement_probe"]["partitioned_refined_original_assignments"],
    )
    candidate_rows = []
    for row in result["candidate_evaluations"]:
        blockers = ", ".join(row["blockers"]) or "none"
        candidate_rows.append(
            "| {candidate_id} | {role} | {decision} | {route_label} | {blockers} |".format(
                candidate_id=row["candidate_id"],
                role=row["role"],
                decision=row["decision"],
                route_label=row["route_label"],
                blockers=blockers,
            )
        )
    minimum = [f"- {item}" for item in result["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in result["not_earned"]]

    return "\n".join(
        [
            "# T484 - Transport Topology Refinement Naturalness Gate - v0.1 results",
            "",
            "> Review gate only. No claim status, roadmap, README, North Star, "
            "public-posture, hard-policy, physics, scale-genesis, clock, "
            "duration, finality, or cross-repo movement.",
            "",
            "- Spec: `tests/T484-transport-topology-refinement-naturalness-gate.md`",
            "- Model: `models/transport_topology_refinement_naturalness_gate.py`",
            "- Tests: `tests/test_transport_topology_refinement_naturalness_gate.py`",
            "- Artifact JSON: `results/T484-transport-topology-refinement-naturalness-gate-v0.1.json`",
            "- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`",
            "- Local anchors: T24, T38, T480, T481, T482, and T483",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Local Anchor Checks",
            "",
            "| check | value |",
            "| --- | --- |",
            *anchor_rows,
            "",
            "## Refinement Controls",
            "",
            "| check | value |",
            "| --- | --- |",
            *control_rows,
            "",
            "## Connected Original Assignments",
            "",
            "| observer | D1 profile tuple | topology role | component size | distance from source |",
            "| --- | --- | --- | --- | --- |",
            *connected_rows,
            "",
            "## Connected Refined Original Assignments",
            "",
            "| observer | D1 profile tuple | topology role | component size | distance from source |",
            "| --- | --- | --- | --- | --- |",
            *connected_refined_rows,
            "",
            "## Partitioned Original Assignments",
            "",
            "| observer | D1 profile tuple | topology role | component size | distance from source |",
            "| --- | --- | --- | --- | --- |",
            *partitioned_rows,
            "",
            "## Partitioned Refined Original Assignments",
            "",
            "| observer | D1 profile tuple | topology role | component size | distance from source |",
            "| --- | --- | --- | --- | --- |",
            *partitioned_refined_rows,
            "",
            "## Candidate Evaluations",
            "",
            "| candidate | role | decision | route | blockers |",
            "| --- | --- | --- | --- | --- |",
            *candidate_rows,
            "",
            "## Future Packet Minimum",
            "",
            *minimum,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _anchor_checks() -> dict[str, Any]:
    t483 = run_t483()
    return {
        "t483_gate_passed": t483["overall_verdict"]["gate_passed"],
        "t483_transport_topology_review_target_admitted": (
            t483["overall_verdict"]["transport_topology_review_target_admitted"]
        ),
        "t483_fixed_d1_control_passed": (
            t483["fixed_d1_independence_probe"]["controls"]["fixed_d1_vectors_match"]
            and t483["fixed_d1_independence_probe"]["controls"]["transport_topology_separates"]
        ),
        "t483_no_internal_scale_structure_earned": (
            t483["overall_verdict"]["internal_scale_structure_earned"] is False
        ),
        "t483_no_clock_or_duration_earned": (
            t483["overall_verdict"]["record_clock_or_duration_earned"] is False
        ),
        "t483_future_packet_requires_fixed_d1_control": (
            "include a fixed-D1 counterfactual pair before claiming independence"
            in t483["future_packet_minimum"]
        ),
    }


def _refinement_probe() -> dict[str, Any]:
    connected = connected_transport_scenario()
    partitioned = partitioned_transport_scenario()
    connected_refined = _subdivide_trust_edges(connected, "connected")
    partitioned_refined = _subdivide_trust_edges(partitioned, "partitioned")
    relabeled_connected = _relabel_scenario(connected)

    connected_ids = _original_observer_ids(connected)
    partitioned_ids = _original_observer_ids(partitioned)

    connected_original = _role_assignments(connected, connected_ids)
    connected_refined_original = _role_assignments(connected_refined, connected_ids)
    partitioned_original = _role_assignments(partitioned, partitioned_ids)
    partitioned_refined_original = _role_assignments(
        partitioned_refined,
        partitioned_ids,
    )
    relabeled_connected_original = _role_assignments(
        relabeled_connected,
        _original_observer_ids(relabeled_connected),
    )

    connected_signature = _role_signature(connected_original)
    connected_refined_signature = _role_signature(connected_refined_original)
    partitioned_signature = _role_signature(partitioned_original)
    partitioned_refined_signature = _role_signature(partitioned_refined_original)
    relabeled_signature = _role_signature(relabeled_connected_original)

    connected_sizes = _component_size_signature(connected_original)
    connected_refined_sizes = _component_size_signature(connected_refined_original)
    connected_length = _shortest_path_length(
        connected,
        connected.source_observer,
        connected.target_observer,
    )
    connected_refined_length = _shortest_path_length(
        connected_refined,
        connected_refined.source_observer,
        connected_refined.target_observer,
    )
    partitioned_length = _shortest_path_length(
        partitioned,
        partitioned.source_observer,
        partitioned.target_observer,
    )

    controls = {
        "original_d1_vectors_fixed": (
            _d1_vector_for_observers(connected, connected_ids)
            == _d1_vector_for_observers(partitioned, partitioned_ids)
            == _d1_vector_for_observers(connected_refined, connected_ids)
            == _d1_vector_for_observers(partitioned_refined, partitioned_ids)
        ),
        "reachability_separates_fixed_d1_pair": (
            connected_signature != partitioned_signature
        ),
        "connected_refinement_preserves_original_roles": (
            connected_signature == connected_refined_signature
        ),
        "partitioned_refinement_preserves_original_roles": (
            partitioned_signature == partitioned_refined_signature
        ),
        "reachability_relabel_invariant": (
            connected_signature == relabeled_signature
        ),
        "component_size_changes_under_refinement": (
            connected_sizes != connected_refined_sizes
        ),
        "path_length_changes_under_refinement": (
            connected_length != connected_refined_length
        ),
        "partitioned_source_target_remain_unreachable": (
            partitioned_length is None
            and _shortest_path_length(
                partitioned_refined,
                partitioned_refined.source_observer,
                partitioned_refined.target_observer,
            )
            is None
        ),
        "uses_clock_duration_or_finality_status": False,
        "imports_rg_or_conformal_mechanism": False,
    }

    return {
        "generator_rule": (
            "topology_role = source_target_component, source_side_component, "
            "target_side_component, or other_component for original observer "
            "sites under trust-preserving reachability"
        ),
        "comparison_domain": (
            "T24/T38 connected and partitioned transport fixtures plus edge "
            "subdivision refinements that preserve original observer D1 profiles"
        ),
        "connected_original_assignments": connected_original,
        "connected_refined_original_assignments": connected_refined_original,
        "partitioned_original_assignments": partitioned_original,
        "partitioned_refined_original_assignments": partitioned_refined_original,
        "connected_signature": connected_signature,
        "connected_refined_signature": connected_refined_signature,
        "partitioned_signature": partitioned_signature,
        "partitioned_refined_signature": partitioned_refined_signature,
        "connected_component_sizes": connected_sizes,
        "connected_refined_component_sizes": connected_refined_sizes,
        "connected_source_target_path_length": connected_length,
        "connected_refined_source_target_path_length": connected_refined_length,
        "partitioned_source_target_path_length": partitioned_length,
        "controls": controls,
        "reading": (
            "Reachability roles for original observers survive benign edge "
            "subdivision and relabeling. Component size and shortest path length "
            "change under the same refinement, so they cannot serve as natural "
            "internal-scale generators without a stronger invariant morphism class."
        ),
    }


def _evaluate_candidate(
    candidate: RefinementCandidate,
    anchor_checks: dict[str, Any],
    refinement_probe: dict[str, Any],
) -> dict[str, Any]:
    blockers: list[str] = []

    if not anchor_checks["t483_gate_passed"]:
        blockers.append("t483_gate_missing")
    if not anchor_checks["t483_transport_topology_review_target_admitted"]:
        blockers.append("t483_topology_review_target_not_admitted")
    if not candidate.predeclared_generator:
        blockers.append("generator_not_predeclared")
    if not candidate.fixed_d1_counterfactual_control_declared:
        blockers.append("fixed_d1_counterfactual_control_missing")
    if not candidate.refinement_invariance_check_declared:
        blockers.append("refinement_invariance_check_missing")
    if not candidate.relabel_invariance_check_declared:
        blockers.append("relabel_invariance_check_missing")
    if (
        candidate.uses_reachability_relation
        and not refinement_probe["controls"]["connected_refinement_preserves_original_roles"]
    ):
        blockers.append("reachability_refinement_invariance_failed")
    if (
        candidate.uses_component_size
        and refinement_probe["controls"]["component_size_changes_under_refinement"]
    ):
        blockers.append("component_size_refinement_variant")
    if (
        candidate.uses_path_length_metric
        and refinement_probe["controls"]["path_length_changes_under_refinement"]
    ):
        blockers.append("path_length_refinement_variant")
    if candidate.label_only_without_generator:
        blockers.append("label_word_without_generator")
    if candidate.uses_observer_id_order:
        blockers.append("observer_label_order_not_relabel_invariant")
    if candidate.uses_hidden_calendar_or_time_order:
        blockers.append("hidden_calendar_or_time_order")
    if candidate.derives_clock_duration_or_arrow:
        blockers.append("clock_duration_or_arrow_overread")
    if candidate.changes_record_finality:
        blockers.append("record_finality_change_overread")
    if candidate.imports_rg_or_conformal_mechanism:
        blockers.append("rg_or_conformal_mechanism_imported")
    if candidate.claims_scale_genesis_or_physics:
        blockers.append("scale_genesis_or_physics_claim_overread")
    if candidate.requests_claim_or_posture_promotion:
        blockers.append("claim_or_public_posture_promotion_shortcut")
    if candidate.local_taf_anchor.startswith("external"):
        blockers.append("no_local_taf_anchor")

    admitted = not blockers and candidate.role == "positive_review_control"
    if admitted:
        route_label = "REACHABILITY_BOOKKEEPING_ADMITTED_NO_SCALE_STRUCTURE"
        decision = "admit_reachability_bookkeeping_no_scale_structure"
    elif any(
        blocker in blockers
        for blocker in (
            "component_size_refinement_variant",
            "path_length_refinement_variant",
        )
    ):
        route_label = "REFINEMENT_VARIANT_SCALE_READING_BLOCKED"
        decision = "reject_refinement_variant"
    else:
        route_label = "TRANSPORT_TOPOLOGY_PACKET_BLOCKED"
        decision = "reject_or_block"

    return {
        "candidate_id": candidate.candidate_id,
        "role": candidate.role,
        "generator_rule": candidate.generator_rule,
        "comparison_domain": candidate.comparison_domain,
        "local_taf_anchor": candidate.local_taf_anchor,
        "uses_reachability_relation": candidate.uses_reachability_relation,
        "uses_component_size": candidate.uses_component_size,
        "uses_path_length_metric": candidate.uses_path_length_metric,
        "admitted": admitted,
        "decision": decision,
        "route_label": route_label,
        "blockers": blockers,
    }


def _candidate_decision(
    evaluations: list[dict[str, Any]],
    candidate_id: str,
) -> dict[str, Any]:
    return next(row for row in evaluations if row["candidate_id"] == candidate_id)


def _subdivide_trust_edges(
    scenario: D1FieldScenario,
    prefix: str,
) -> D1FieldScenario:
    """Subdivide each trust-preserving edge once with an unlabeled relay site."""

    profile_by_id = _profile_by_observer(scenario)
    profiles = list(scenario.observer_profiles)
    edges: list[FieldEdge] = []
    for index, edge in enumerate(scenario.edges):
        if not edge.trust_preserving:
            edges.append(edge)
            continue
        relay_id = f"{prefix}_relay_{index}_{edge.source}_{edge.target}"
        source_profile = profile_by_id[edge.source]
        relay_site = replace(
            source_profile.site,
            observer_id=relay_id,
            population="relay",
            scale="relay",
        )
        profiles.append(replace(source_profile, site=relay_site))
        relation = f"{edge.relation}_subdivision"
        edges.append(
            FieldEdge(
                source=edge.source,
                target=relay_id,
                relation=relation,
                trust_preserving=True,
            )
        )
        edges.append(
            FieldEdge(
                source=relay_id,
                target=edge.target,
                relation=relation,
                trust_preserving=True,
            )
        )
    return replace(
        scenario,
        name=f"{scenario.name}_subdivided",
        observer_profiles=tuple(profiles),
        edges=tuple(edges),
    )


def _role_assignments(
    scenario: D1FieldScenario,
    observer_ids: tuple[str, ...],
) -> list[dict[str, Any]]:
    component_by_observer = _component_ids(scenario)
    component_sizes: dict[int, int] = {}
    for component_id in component_by_observer.values():
        component_sizes[component_id] = component_sizes.get(component_id, 0) + 1
    source_component = component_by_observer[scenario.source_observer]
    target_component = component_by_observer[scenario.target_observer]
    profile_by_id = _profile_by_observer(scenario)

    rows = []
    for observer_id in sorted(observer_ids):
        component_id = component_by_observer[observer_id]
        profile = profile_by_id[observer_id].profile
        rows.append(
            {
                "observer_id": observer_id,
                "profile_tuple": list(profile.as_tuple()),
                "topology_role": _topology_role(
                    component_id,
                    source_component,
                    target_component,
                ),
                "component_size": component_sizes[component_id],
                "distance_from_source": _shortest_path_length(
                    scenario,
                    scenario.source_observer,
                    observer_id,
                ),
            }
        )
    return rows


def _component_ids(scenario: D1FieldScenario) -> dict[str, int]:
    observer_ids = sorted(_observer_ids(scenario))
    neighbors: dict[str, set[str]] = {observer_id: set() for observer_id in observer_ids}
    for edge in scenario.edges:
        if not edge.trust_preserving:
            continue
        neighbors.setdefault(edge.source, set()).add(edge.target)
        neighbors.setdefault(edge.target, set()).add(edge.source)

    component_by_observer: dict[str, int] = {}
    for observer_id in observer_ids:
        if observer_id in component_by_observer:
            continue
        component_id = len(set(component_by_observer.values()))
        pending = [observer_id]
        while pending:
            current = pending.pop()
            if current in component_by_observer:
                continue
            component_by_observer[current] = component_id
            pending.extend(
                neighbor
                for neighbor in sorted(neighbors.get(current, set()))
                if neighbor not in component_by_observer
            )
    return component_by_observer


def _topology_role(
    component_id: int,
    source_component: int,
    target_component: int,
) -> str:
    if component_id == source_component and component_id == target_component:
        return "source_target_component"
    if component_id == source_component:
        return "source_side_component"
    if component_id == target_component:
        return "target_side_component"
    return "other_component"


def _role_signature(assignments: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in assignments:
        role = row["topology_role"]
        counts[role] = counts.get(role, 0) + 1
    return dict(sorted(counts.items()))


def _component_size_signature(assignments: list[dict[str, Any]]) -> dict[str, int]:
    sizes: dict[str, int] = {}
    for row in assignments:
        sizes[row["observer_id"]] = row["component_size"]
    return dict(sorted(sizes.items()))


def _shortest_path_length(
    scenario: D1FieldScenario,
    source: str,
    target: str,
) -> int | None:
    if source == target:
        return 0
    neighbors: dict[str, set[str]] = {}
    for edge in scenario.edges:
        if not edge.trust_preserving:
            continue
        neighbors.setdefault(edge.source, set()).add(edge.target)
        neighbors.setdefault(edge.target, set()).add(edge.source)

    seen = {source}
    pending: deque[tuple[str, int]] = deque([(source, 0)])
    while pending:
        current, distance = pending.popleft()
        for neighbor in sorted(neighbors.get(current, set())):
            if neighbor == target:
                return distance + 1
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append((neighbor, distance + 1))
    return None


def _d1_vector_for_observers(
    scenario: D1FieldScenario,
    observer_ids: tuple[str, ...],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    profile_by_id = _profile_by_observer(scenario)
    return tuple(
        (observer_id, profile_by_id[observer_id].profile.as_tuple())
        for observer_id in sorted(observer_ids)
    )


def _profile_by_observer(scenario: D1FieldScenario) -> dict[str, ObserverProfile]:
    return {
        profile.site.observer_id: profile
        for profile in scenario.observer_profiles
    }


def _observer_ids(scenario: D1FieldScenario) -> set[str]:
    return {profile.site.observer_id for profile in scenario.observer_profiles}


def _original_observer_ids(scenario: D1FieldScenario) -> tuple[str, ...]:
    return tuple(
        sorted(
            profile.site.observer_id
            for profile in scenario.observer_profiles
            if "_relay_" not in profile.site.observer_id
        )
    )


def _relabel_scenario(scenario: D1FieldScenario) -> D1FieldScenario:
    observer_ids = sorted(_observer_ids(scenario))
    relabel_map = {
        old: f"site_{index}"
        for index, old in enumerate(reversed(observer_ids))
    }
    profiles = tuple(
        _relabel_profile(profile, relabel_map)
        for profile in scenario.observer_profiles
    )
    edges = tuple(
        FieldEdge(
            source=relabel_map[edge.source],
            target=relabel_map[edge.target],
            relation=edge.relation,
            trust_preserving=edge.trust_preserving,
        )
        for edge in scenario.edges
    )
    return replace(
        scenario,
        observer_profiles=profiles,
        edges=edges,
        source_observer=relabel_map[scenario.source_observer],
        target_observer=relabel_map[scenario.target_observer],
    )


def _relabel_profile(
    profile: ObserverProfile,
    relabel_map: dict[str, str],
) -> ObserverProfile:
    site = replace(profile.site, observer_id=relabel_map[profile.site.observer_id])
    return replace(profile, site=site)


def _assignment_rows(assignments: list[dict[str, Any]]) -> list[str]:
    return [
        "| {observer_id} | {profile_tuple} | {topology_role} | {component_size} | {distance_from_source} |".format(
            observer_id=row["observer_id"],
            profile_tuple=row["profile_tuple"],
            topology_role=row["topology_role"],
            component_size=row["component_size"],
            distance_from_source=row["distance_from_source"],
        )
        for row in assignments
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
