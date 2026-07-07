"""T483: internal scale-generator independence gate.

T482 showed that a D1-support-gradient generator passes review mechanics but
factors through the existing D1 profile tuple. This module makes the next
burden executable: a future internal-scale generator must survive a fixed-D1
counterfactual independence check before it can even be admitted as a review
target.

The admitted positive control is intentionally weak. It uses T24/T38 transport
topology to separate connected vs partitioned fixtures with the same D1 vector.
That clears D1-completion independence as review metadata only. It earns no
internal scale structure, clock, duration, finality change, scale-genesis
theorem, physics support, claim movement, or public-posture movement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from models.internal_scale_generator_invariance_probe import run as run_t482
from models.multiscale_observer_field import (
    D1FieldScenario,
    FieldEdge,
    ObserverProfile,
    connected_transport_scenario,
    partitioned_transport_scenario,
)


ARTIFACT_ID = "T483-internal-scale-generator-independence-gate-v0.1"
VERDICT = "INTERNAL_SCALE_INDEPENDENCE_GATE_BUILT_REVIEW_TARGET_ONLY_NO_PROMOTION"


@dataclass(frozen=True)
class IndependenceCandidate:
    """One proposed post-T482 internal-scale generator packet."""

    candidate_id: str
    role: str
    generator_rule: str
    comparison_domain: str
    local_taf_anchor: str
    predeclared_generator: bool
    comparison_domain_predeclared: bool
    fixed_d1_counterfactual_control_declared: bool
    relabel_invariance_check_declared: bool
    d1_profile_completion_sufficient: bool = False
    separates_fixed_d1_transport_counterfactual: bool = False
    uses_transport_topology: bool = False
    label_only_without_generator: bool = False
    posthoc_counterfactual: bool = False
    uses_observer_id_order: bool = False
    uses_hidden_calendar_or_time_order: bool = False
    derives_clock_duration_or_arrow: bool = False
    changes_record_finality: bool = False
    imports_rg_or_conformal_mechanism: bool = False
    claims_scale_genesis_or_physics: bool = False
    requests_claim_or_posture_promotion: bool = False


def independence_candidates() -> tuple[IndependenceCandidate, ...]:
    """Return the finite T483 candidate catalogue."""

    return (
        IndependenceCandidate(
            candidate_id="t482_d1_support_gradient",
            role="absorbed_control",
            generator_rule=(
                "support_depth = accessible_support + holder_redundancy + "
                "branch_support + reversal_cost"
            ),
            comparison_domain="T24 observer sites with D1 profile tuples",
            local_taf_anchor="T482",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            fixed_d1_counterfactual_control_declared=True,
            relabel_invariance_check_declared=True,
            d1_profile_completion_sufficient=True,
        ),
        IndependenceCandidate(
            candidate_id="transport_topology_review_target",
            role="positive_review_control",
            generator_rule=(
                "classify observer sites by trust-preserving transport "
                "component relative to the declared source and target"
            ),
            comparison_domain=(
                "T24/T38 connected and partitioned transport fixtures with "
                "identical observer IDs and D1 profile vectors"
            ),
            local_taf_anchor="T24/T38/T480/T481/T482",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            fixed_d1_counterfactual_control_declared=True,
            relabel_invariance_check_declared=True,
            separates_fixed_d1_transport_counterfactual=True,
            uses_transport_topology=True,
        ),
        IndependenceCandidate(
            candidate_id="label_word_independence",
            role="hostile_control",
            generator_rule="call the generator independent",
            comparison_domain="declared after the packet is named",
            local_taf_anchor="T482 shortcut",
            predeclared_generator=False,
            comparison_domain_predeclared=False,
            fixed_d1_counterfactual_control_declared=False,
            relabel_invariance_check_declared=False,
            label_only_without_generator=True,
        ),
        IndependenceCandidate(
            candidate_id="posthoc_counterfactual_selector",
            role="hostile_control",
            generator_rule="choose the counterfactual pair after seeing the split",
            comparison_domain="selected after the separating topology is known",
            local_taf_anchor="T24/T38 overread",
            predeclared_generator=False,
            comparison_domain_predeclared=False,
            fixed_d1_counterfactual_control_declared=True,
            relabel_invariance_check_declared=True,
            uses_transport_topology=True,
            posthoc_counterfactual=True,
        ),
        IndependenceCandidate(
            candidate_id="observer_id_rank_independence",
            role="hostile_control",
            generator_rule="rank observer identifiers alphabetically",
            comparison_domain="observer-id order",
            local_taf_anchor="T24 labels only",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            fixed_d1_counterfactual_control_declared=True,
            relabel_invariance_check_declared=True,
            uses_observer_id_order=True,
        ),
        IndependenceCandidate(
            candidate_id="hidden_time_order_independence",
            role="hostile_control",
            generator_rule="derive scale from hidden time_step or calendar order",
            comparison_domain="hidden temporal order",
            local_taf_anchor="T24 metadata overread",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            fixed_d1_counterfactual_control_declared=False,
            relabel_invariance_check_declared=True,
            uses_hidden_calendar_or_time_order=True,
            derives_clock_duration_or_arrow=True,
        ),
        IndependenceCandidate(
            candidate_id="finality_by_transport_component",
            role="hostile_control",
            generator_rule="mark the target-side component as final",
            comparison_domain="transport component labels",
            local_taf_anchor="T24/T38 overread",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            fixed_d1_counterfactual_control_declared=True,
            relabel_invariance_check_declared=True,
            uses_transport_topology=True,
            changes_record_finality=True,
        ),
        IndependenceCandidate(
            candidate_id="rg_fixed_point_independence_source",
            role="hostile_control",
            generator_rule="import RG or conformal fixed point as generator",
            comparison_domain="external RG scale classes",
            local_taf_anchor="external RG/conformal mechanism",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            fixed_d1_counterfactual_control_declared=False,
            relabel_invariance_check_declared=False,
            imports_rg_or_conformal_mechanism=True,
            claims_scale_genesis_or_physics=True,
        ),
        IndependenceCandidate(
            candidate_id="promotion_shortcut_independence",
            role="hostile_control",
            generator_rule="declare fixed-D1 separation to be internal scale",
            comparison_domain="T24/T38 fixtures",
            local_taf_anchor="T24/T38/T482 promotion shortcut",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            fixed_d1_counterfactual_control_declared=True,
            relabel_invariance_check_declared=True,
            uses_transport_topology=True,
            claims_scale_genesis_or_physics=True,
            requests_claim_or_posture_promotion=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T483 internal scale-generator independence gate."""

    anchor_checks = _anchor_checks()
    independence_probe = _fixed_d1_transport_topology_probe()
    evaluations = [
        _evaluate_candidate(candidate, anchor_checks, independence_probe)
        for candidate in independence_candidates()
    ]
    admitted = [
        row["candidate_id"]
        for row in evaluations
        if row["admitted"]
    ]
    hostile_violations = [
        row["candidate_id"]
        for row in evaluations
        if row["role"] == "hostile_control" and row["admitted"]
    ]
    expected_admissions = ["transport_topology_review_target"]
    support_gradient_absorbed = _candidate_decision(
        evaluations,
        "t482_d1_support_gradient",
    )["decision"] == "reject_d1_completion_absorbed"
    gate_passed = (
        anchor_checks["t482_gate_passed"]
        and anchor_checks["t482_support_gradient_factors_through_d1"]
        and independence_probe["controls"]["fixed_d1_vectors_match"]
        and independence_probe["controls"]["transport_topology_separates"]
        and independence_probe["controls"]["transport_topology_relabel_invariant"]
        and independence_probe["controls"]["d1_profile_completion_insufficient"]
        and admitted == expected_admissions
        and support_gradient_absorbed
        and not hostile_violations
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Convert T482's independence burden into an executable fixed-D1 "
            "counterfactual gate for future internal-scale generator packets."
        ),
        "local_anchor_checks": anchor_checks,
        "fixed_d1_independence_probe": independence_probe,
        "candidate_evaluations": evaluations,
        "admitted_candidate_ids": admitted,
        "hostile_violations": hostile_violations,
        "overall_verdict": {
            "verdict": VERDICT,
            "gate_passed": gate_passed,
            "transport_topology_review_target_admitted": (
                admitted == expected_admissions
            ),
            "d1_completion_control_blocked": support_gradient_absorbed,
            "hostile_controls_blocked": not hostile_violations,
            "claim_ledger_update": "none",
            "north_star_update": "none",
            "roadmap_update": "none",
            "public_posture_update": "none",
            "physics_claim_earned": False,
            "scale_genesis_theorem_earned": False,
            "record_clock_or_duration_earned": False,
            "record_finality_change_earned": False,
            "internal_scale_structure_earned": False,
            "reading": (
                "T483 rejects T482-style support-gradient generators as D1 "
                "completion. A synthetic transport-topology generator separates "
                "T24/T38 connected vs partitioned fixtures while their D1 vectors "
                "are fixed and survives observer-label relabeling. This is "
                "admitted only as a future review target and transport-topology "
                "bookkeeping; it earns no internal scale structure, clock, "
                "duration, finality change, scale-genesis theorem, physics "
                "support, claim movement, or public-posture movement."
            ),
        },
        "future_packet_minimum": [
            "prove the generator is not recoverable from the existing D1 profile tuple",
            "include a fixed-D1 counterfactual pair before claiming independence",
            "separate transport topology from scale, clock, duration, and finality language",
            "preserve relabel-invariance under observer ID permutation",
            "block label-only, posthoc, hidden-time, finality, RG/conformal, physics, and promotion shortcuts",
            "treat fixed-D1 transport-topology separation as review metadata unless a separate theorem earns more",
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
    """Render T483 results as Markdown."""

    verdict = result["overall_verdict"]
    anchor_rows = [
        f"| {key} | {value} |"
        for key, value in result["local_anchor_checks"].items()
    ]
    control_rows = [
        f"| {key} | {value} |"
        for key, value in result["fixed_d1_independence_probe"]["controls"].items()
    ]
    connected_rows = _assignment_rows(
        result["fixed_d1_independence_probe"]["connected_assignments"],
    )
    partitioned_rows = _assignment_rows(
        result["fixed_d1_independence_probe"]["partitioned_assignments"],
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
            "# T483 - Internal Scale Generator Independence Gate - v0.1 results",
            "",
            "> Review gate only. No claim status, roadmap, README, North Star, "
            "public-posture, hard-policy, physics, scale-genesis, clock, "
            "duration, finality, or cross-repo movement.",
            "",
            "- Spec: `tests/T483-internal-scale-generator-independence-gate.md`",
            "- Model: `models/internal_scale_generator_independence_gate.py`",
            "- Tests: `tests/test_internal_scale_generator_independence_gate.py`",
            "- Artifact JSON: `results/T483-internal-scale-generator-independence-gate-v0.1.json`",
            "- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`",
            "- Local anchors: T24, T38, T480, T481, and T482",
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
            "## Fixed-D1 Independence Controls",
            "",
            "| check | value |",
            "| --- | --- |",
            *control_rows,
            "",
            "## Connected Transport Assignments",
            "",
            "| observer | D1 profile tuple | topology band | component size |",
            "| --- | --- | --- | --- |",
            *connected_rows,
            "",
            "## Partitioned Transport Assignments",
            "",
            "| observer | D1 profile tuple | topology band | component size |",
            "| --- | --- | --- | --- |",
            *partitioned_rows,
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
    t482 = run_t482()
    return {
        "t482_gate_passed": t482["overall_verdict"]["gate_passed"],
        "t482_support_gradient_admitted_as_bookkeeping": (
            t482["overall_verdict"]["support_gradient_review_packet_admitted"]
        ),
        "t482_support_gradient_factors_through_d1": (
            t482["overall_verdict"]["factors_through_existing_d1_profile"]
        ),
        "t482_no_internal_scale_structure_earned": (
            t482["overall_verdict"]["internal_scale_structure_earned"] is False
        ),
        "t482_no_clock_or_duration_earned": (
            t482["overall_verdict"]["record_clock_or_duration_earned"] is False
        ),
        "t482_future_packet_requires_independent_generator": (
            "keep support-gradient packets labeled as D1 bookkeeping unless an independent generator is supplied"
            in t482["future_packet_minimum"]
        ),
    }


def _fixed_d1_transport_topology_probe() -> dict[str, Any]:
    connected = connected_transport_scenario()
    partitioned = partitioned_transport_scenario()
    relabeled_connected = _relabel_scenario(connected)

    connected_assignments = _transport_topology_assignments(connected)
    partitioned_assignments = _transport_topology_assignments(partitioned)
    relabeled_assignments = _transport_topology_assignments(relabeled_connected)

    connected_signature = _topology_signature(connected_assignments)
    partitioned_signature = _topology_signature(partitioned_assignments)
    relabeled_signature = _topology_signature(relabeled_assignments)
    fixed_d1_vectors_match = _d1_vector(connected) == _d1_vector(partitioned)

    controls = {
        "fixed_d1_vectors_match": fixed_d1_vectors_match,
        "transport_topology_separates": (
            connected_signature != partitioned_signature
        ),
        "transport_topology_relabel_invariant": (
            connected_signature == relabeled_signature
        ),
        "connected_source_target_reachable": _source_target_same_component(
            connected_assignments,
        ),
        "partitioned_source_target_reachable": _source_target_same_component(
            partitioned_assignments,
        ),
        "d1_profile_completion_insufficient": (
            fixed_d1_vectors_match and connected_signature != partitioned_signature
        ),
        "uses_clock_duration_or_finality_status": False,
        "imports_rg_or_conformal_mechanism": False,
    }

    return {
        "generator_rule": (
            "transport_topology_band = source_target_component if the site is "
            "in the trust-preserving component containing both source and target; "
            "otherwise source_side_component, target_side_component, or other_component"
        ),
        "comparison_domain": (
            "connected_transport_scenario vs partitioned_transport_scenario from "
            "T24, holding observer IDs and D1 profile vectors fixed"
        ),
        "connected_assignments": connected_assignments,
        "partitioned_assignments": partitioned_assignments,
        "connected_signature": connected_signature,
        "partitioned_signature": partitioned_signature,
        "relabel_signature": relabeled_signature,
        "controls": controls,
        "reading": (
            "The transport-topology generator separates connected and partitioned "
            "fixtures even though their D1 profile vectors match. This is enough "
            "to reject D1-profile completion, but it is only transport-topology "
            "bookkeeping unless a separate theorem connects it to internal scale."
        ),
    }


def _evaluate_candidate(
    candidate: IndependenceCandidate,
    anchor_checks: dict[str, Any],
    independence_probe: dict[str, Any],
) -> dict[str, Any]:
    blockers: list[str] = []

    if not anchor_checks["t482_gate_passed"]:
        blockers.append("t482_gate_missing")
    if not candidate.predeclared_generator:
        blockers.append("generator_not_predeclared")
    if not candidate.comparison_domain_predeclared:
        blockers.append("comparison_domain_not_predeclared")
    if not candidate.fixed_d1_counterfactual_control_declared:
        blockers.append("fixed_d1_counterfactual_control_missing")
    if not candidate.relabel_invariance_check_declared:
        blockers.append("relabel_invariance_check_missing")
    if candidate.d1_profile_completion_sufficient:
        blockers.append("d1_profile_completion_absorbs_generator")
    if (
        candidate.role == "positive_review_control"
        and not candidate.separates_fixed_d1_transport_counterfactual
    ):
        blockers.append("fixed_d1_counterfactual_not_separated")
    if (
        candidate.uses_transport_topology
        and not independence_probe["controls"]["transport_topology_separates"]
    ):
        blockers.append("transport_topology_control_failed")
    if candidate.label_only_without_generator:
        blockers.append("label_word_without_generator")
    if candidate.posthoc_counterfactual:
        blockers.append("posthoc_counterfactual_selection")
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
        route_label = "TRANSPORT_TOPOLOGY_REVIEW_TARGET_ADMITTED_NO_SCALE_STRUCTURE"
        decision = "admit_review_target_no_scale_structure"
    elif "d1_profile_completion_absorbs_generator" in blockers:
        route_label = "D1_COMPLETION_ABSORBED_GENERATOR"
        decision = "reject_d1_completion_absorbed"
    else:
        route_label = "INDEPENDENCE_PACKET_BLOCKED"
        decision = "reject_or_block"

    return {
        "candidate_id": candidate.candidate_id,
        "role": candidate.role,
        "generator_rule": candidate.generator_rule,
        "comparison_domain": candidate.comparison_domain,
        "local_taf_anchor": candidate.local_taf_anchor,
        "uses_transport_topology": candidate.uses_transport_topology,
        "d1_profile_completion_sufficient": (
            candidate.d1_profile_completion_sufficient
        ),
        "separates_fixed_d1_transport_counterfactual": (
            candidate.separates_fixed_d1_transport_counterfactual
        ),
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


def _transport_topology_assignments(
    scenario: D1FieldScenario,
) -> list[dict[str, Any]]:
    component_by_observer = _component_ids(scenario)
    source_component = component_by_observer[scenario.source_observer]
    target_component = component_by_observer[scenario.target_observer]
    component_sizes: dict[int, int] = {}
    for component_id in component_by_observer.values():
        component_sizes[component_id] = component_sizes.get(component_id, 0) + 1

    rows = []
    for observer in sorted(
        scenario.observer_profiles,
        key=lambda item: item.site.observer_id,
    ):
        observer_id = observer.site.observer_id
        component_id = component_by_observer[observer_id]
        rows.append(
            {
                "observer_id": observer_id,
                "profile_tuple": list(observer.profile.as_tuple()),
                "component_id": component_id,
                "component_size": component_sizes[component_id],
                "topology_band": _topology_band(
                    component_id,
                    source_component,
                    target_component,
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


def _topology_band(
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


def _topology_signature(assignments: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in assignments:
        band = row["topology_band"]
        counts[band] = counts.get(band, 0) + 1
    return dict(sorted(counts.items()))


def _source_target_same_component(assignments: list[dict[str, Any]]) -> bool:
    bands = _topology_signature(assignments)
    return set(bands) == {"source_target_component"}


def _assignment_rows(assignments: list[dict[str, Any]]) -> list[str]:
    return [
        "| {observer_id} | {profile_tuple} | {topology_band} | {component_size} |".format(
            observer_id=row["observer_id"],
            profile_tuple=row["profile_tuple"],
            topology_band=row["topology_band"],
            component_size=row["component_size"],
        )
        for row in assignments
    ]


def _d1_vector(scenario: D1FieldScenario) -> tuple[tuple[str, tuple[int, ...]], ...]:
    return tuple(
        (observer.site.observer_id, observer.profile.as_tuple())
        for observer in sorted(
            scenario.observer_profiles,
            key=lambda item: item.site.observer_id,
        )
    )


def _observer_ids(scenario: D1FieldScenario) -> set[str]:
    return {profile.site.observer_id for profile in scenario.observer_profiles}


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
