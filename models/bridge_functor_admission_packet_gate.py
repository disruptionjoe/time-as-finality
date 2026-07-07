"""T496 - bridge-functor admission packet gate.

This converts the all-persona synthesis recommendation into an executable
method gate. The gate admits future bridge/functor packets only as review
targets when they bring their own absorber checks, domain-native law source,
capability-spread evidence, controls, and demotion path.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T496-bridge-functor-admission-packet-gate-v0.1"
VERDICT = "BRIDGE_FUNCTOR_ADMISSION_GATE_BUILT_REVIEW_ONLY"
SOURCE_SYNTHESIS = "explorations/persona-missing-analysis-hegelian-metasynthesis-2026-07-07.md"
SOURCE_PACKET_REPORT = "technical-reports/TECHNICAL-REPORT-bridge-functor-admission-packet-v0.1.md"
SOURCE_PACKET_TEMPLATE = "workflows/templates/bridge-functor-admission-packet.template.md"

ALLOWED_DOMAIN_LAW_SOURCES = frozenset(
    {
        "domain_native_morphism_class",
        "cost_law",
        "measure_law",
        "source_checked_lower_bound",
        "finite_to_continuum_bridge",
        "adversarial_protocol",
        "direct_preservation_theorem",
        "direct_record_finality_bridge_theorem",
        "domain_native_certifiability_theorem",
    }
)

HONEST_CEILING = (
    "Admission gate only. T496 turns the all-persona synthesis into a hostile "
    "packet form for future work. Admission means review target, not theorem, "
    "claim movement, North Star movement, public posture, hard policy, external "
    "publication, or cross-repo truth."
)


@dataclass(frozen=True)
class ClosedRoute:
    route_id: str
    closing_tests: tuple[str, ...]
    required_new_keys: tuple[str, ...]
    note: str


@dataclass(frozen=True)
class AbsorberCheck:
    name: str
    status: str
    note: str


@dataclass(frozen=True)
class AdmissionPacket:
    packet_id: str
    title: str
    route_id: str
    closed_lineage_citations: tuple[str, ...]
    new_keys: tuple[str, ...]
    declares_native_capability_object: bool
    declares_task_family: bool
    declares_observer_access_boundary: bool
    declares_completion_rights: bool
    declares_visible_projection: bool
    absorber_checks: tuple[AbsorberCheck, ...]
    domain_law_source: str | None
    capability_spread_non_singleton: bool
    positive_controls_pass: bool
    minimality_condition_declared: bool
    demotion_path_declared: bool
    requests_claim_movement: bool = False
    requests_public_posture_movement: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth_movement: bool = False


@dataclass(frozen=True)
class AdmissionDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    missing_requirements: tuple[str, ...]
    blocked_shortcuts: tuple[str, ...]
    reason: str
    strongest_allowed_reading: str


def closed_routes() -> dict[str, ClosedRoute]:
    return {
        "generic_new_bridge": ClosedRoute(
            route_id="generic_new_bridge",
            closing_tests=(),
            required_new_keys=(),
            note="No specific closed lineage; generic packets still need the common form.",
        ),
        "s1_finite_colimit": ClosedRoute(
            route_id="s1_finite_colimit",
            closing_tests=("T490", "T491"),
            required_new_keys=(
                "independent_measure_law",
                "finite_to_continuum_bridge",
                "separate_formal_entry_point",
            ),
            note="T491 closes finite S1 colimit restarts without new measure/bridge/formal entry.",
        ),
        "rg_reachability_quotient": ClosedRoute(
            route_id="rg_reachability_quotient",
            closing_tests=("T487", "T488"),
            required_new_keys=(
                "independent_capability_object",
                "domain_native_morphism_class",
                "direct_record_finality_bridge_theorem",
            ),
            note="T488 closes reachability-quotient restarts without independent capability or morphism/theorem evidence.",
        ),
        "valid_coarse_graining": ClosedRoute(
            route_id="valid_coarse_graining",
            closing_tests=("T478", "T489"),
            required_new_keys=(
                "certified_record_capability_object",
                "domain_native_certifiability_theorem",
                "direct_observer_theory_taf_equivalence",
            ),
            note="T489 closes minor observer-budget/coarse-graining restarts.",
        ),
        "typed_gap_bridge": ClosedRoute(
            route_id="typed_gap_bridge",
            closing_tests=("T492",),
            required_new_keys=(
                "direct_preservation_theorem",
                "invariant_obstruction_class",
                "schema_to_object_identity_criterion",
            ),
            note="T492 supports a shared finite schema but blocks object identity and cohomology overreads.",
        ),
        "bounded_record_retrieval": ClosedRoute(
            route_id="bounded_record_retrieval",
            closing_tests=("T495",),
            required_new_keys=(
                "source_checked_lower_bound",
                "channel_resource_task",
                "indexed_retrieval_theorem_packet",
            ),
            note="T495 admits retention-axis review only; lower-bound language needs source checking.",
        ),
    }


def fixture_packets() -> tuple[AdmissionPacket, ...]:
    return (
        AdmissionPacket(
            packet_id="typed_gap_direct_preservation_packet",
            title="Typed-gap direct preservation theorem packet",
            route_id="typed_gap_bridge",
            closed_lineage_citations=("T492",),
            new_keys=("direct_preservation_theorem", "invariant_obstruction_class"),
            declares_native_capability_object=True,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("same_section_identity", "tested", "T492 block preserved."),
                AbsorberCheck("semantic_relabeling", "tested", "Relabel controls declared."),
                AbsorberCheck("cohomology_overread", "tested", "Obstruction class must be direct."),
            ),
            domain_law_source="direct_preservation_theorem",
            capability_spread_non_singleton=True,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
        ),
        AdmissionPacket(
            packet_id="s1_independent_measure_packet",
            title="S1 independent measure bridge packet",
            route_id="s1_finite_colimit",
            closed_lineage_citations=("T490", "T491"),
            new_keys=("independent_measure_law", "finite_to_continuum_bridge"),
            declares_native_capability_object=True,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("survivor_tail_circularity", "tested", "T490 control retained."),
                AbsorberCheck("screen_conditioning", "tested", "T491 closure retained."),
                AbsorberCheck("single_size_positive", "tested", "Multi-size burden declared."),
            ),
            domain_law_source="measure_law",
            capability_spread_non_singleton=True,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
        ),
        AdmissionPacket(
            packet_id="bounded_retrieval_lower_bound_packet",
            title="Bounded-record indexed retrieval lower-bound packet",
            route_id="bounded_record_retrieval",
            closed_lineage_citations=("T495",),
            new_keys=("source_checked_lower_bound", "indexed_retrieval_theorem_packet"),
            declares_native_capability_object=True,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("full_history_completion", "tested", "T495 positive control retained."),
                AbsorberCheck("compression_coding_theory", "tested", "Lower-bound source must be checked."),
                AbsorberCheck("competency_profile", "tested", "T493/T494 absorber declared."),
            ),
            domain_law_source="source_checked_lower_bound",
            capability_spread_non_singleton=True,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
        ),
        AdmissionPacket(
            packet_id="analogy_only_geometry_restart",
            title="Geometry analogy restart without law source",
            route_id="rg_reachability_quotient",
            closed_lineage_citations=("T487", "T488"),
            new_keys=("independent_capability_object",),
            declares_native_capability_object=True,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("reachability_completion", "tested", "Prior closure cited."),
            ),
            domain_law_source=None,
            capability_spread_non_singleton=True,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
        ),
        AdmissionPacket(
            packet_id="closed_route_without_new_key",
            title="S1 finite-colimit restart without the named new key",
            route_id="s1_finite_colimit",
            closed_lineage_citations=("T490", "T491"),
            new_keys=("screen_conditioning_variant",),
            declares_native_capability_object=True,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("screen_conditioning", "tested", "But only as a variant."),
            ),
            domain_law_source="measure_law",
            capability_spread_non_singleton=True,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
        ),
        AdmissionPacket(
            packet_id="missing_native_capability_object",
            title="Packet that names a bridge but not Cap",
            route_id="generic_new_bridge",
            closed_lineage_citations=(),
            new_keys=(),
            declares_native_capability_object=False,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("full_state_completion", "tested", "Declared."),
            ),
            domain_law_source="domain_native_morphism_class",
            capability_spread_non_singleton=True,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
        ),
        AdmissionPacket(
            packet_id="absorbers_declared_only",
            title="Packet with absorbers named but not tested",
            route_id="generic_new_bridge",
            closed_lineage_citations=(),
            new_keys=(),
            declares_native_capability_object=True,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("full_state_completion", "declared_only", "No hostile check."),
            ),
            domain_law_source="domain_native_morphism_class",
            capability_spread_non_singleton=True,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
        ),
        AdmissionPacket(
            packet_id="no_capability_spread_packet",
            title="Packet with law source but no spread evidence",
            route_id="generic_new_bridge",
            closed_lineage_citations=(),
            new_keys=(),
            declares_native_capability_object=True,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("full_state_completion", "tested", "Declared."),
            ),
            domain_law_source="domain_native_morphism_class",
            capability_spread_non_singleton=False,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
        ),
        AdmissionPacket(
            packet_id="public_posture_shortcut_packet",
            title="Packet requesting public-posture or claim movement",
            route_id="bounded_record_retrieval",
            closed_lineage_citations=("T495",),
            new_keys=("source_checked_lower_bound",),
            declares_native_capability_object=True,
            declares_task_family=True,
            declares_observer_access_boundary=True,
            declares_completion_rights=True,
            declares_visible_projection=True,
            absorber_checks=(
                AbsorberCheck("full_history_completion", "tested", "Declared."),
            ),
            domain_law_source="source_checked_lower_bound",
            capability_spread_non_singleton=True,
            positive_controls_pass=True,
            minimality_condition_declared=True,
            demotion_path_declared=True,
            requests_claim_movement=True,
            requests_public_posture_movement=True,
            requests_cross_repo_truth_movement=True,
        ),
    )


def evaluate_packet(packet: AdmissionPacket) -> AdmissionDecision:
    routes = closed_routes()
    route = routes[packet.route_id]
    blocked = blocked_shortcuts(packet)
    missing = missing_requirements(packet, route)

    if blocked:
        return AdmissionDecision(
            packet_id=packet.packet_id,
            admitted=False,
            label="BLOCKED_GOVERNANCE_OR_EXTERNAL_SHORTCUT",
            action="stop",
            review_target_only=False,
            missing_requirements=missing,
            blocked_shortcuts=blocked,
            reason="Admission packets cannot move claims, posture, publication, or cross-repo truth.",
            strongest_allowed_reading="No repo-local review target is admitted until shortcuts are removed.",
        )
    if "closed_route_new_key" in missing:
        return AdmissionDecision(
            packet_id=packet.packet_id,
            admitted=False,
            label="REJECTED_CLOSED_ROUTE_WITHOUT_REQUIRED_NEW_KEY",
            action="reject",
            review_target_only=False,
            missing_requirements=missing,
            blocked_shortcuts=blocked,
            reason="The cited closed route requires one of its named reopen keys.",
            strongest_allowed_reading="Protected lineage remains closed to minor variants.",
        )
    if "closed_lineage_citations" in missing:
        return AdmissionDecision(
            packet_id=packet.packet_id,
            admitted=False,
            label="REJECTED_CLOSED_LINEAGE_UNCITED",
            action="reject",
            review_target_only=False,
            missing_requirements=missing,
            blocked_shortcuts=blocked,
            reason="Closed routes must cite their closing tests before reopening.",
            strongest_allowed_reading="The packet is route-ambiguous intake only.",
        )
    if missing:
        return AdmissionDecision(
            packet_id=packet.packet_id,
            admitted=False,
            label="REJECTED_INCOMPLETE_ADMISSION_PACKET",
            action="reject",
            review_target_only=False,
            missing_requirements=missing,
            blocked_shortcuts=blocked,
            reason="The packet does not satisfy the common Bridge-Functor form.",
            strongest_allowed_reading="The idea may be rewritten as a complete packet.",
        )

    return AdmissionDecision(
        packet_id=packet.packet_id,
        admitted=True,
        label="ADMITTED_BRIDGE_FUNCTOR_REVIEW_TARGET",
        action="review",
        review_target_only=True,
        missing_requirements=(),
        blocked_shortcuts=(),
        reason="Packet supplies Cap, absorbers, law source, spread, controls, minimality, and demotion path.",
        strongest_allowed_reading=(
            "Review target only. The packet may be executed or inspected, but it "
            "does not count as theorem, physics support, claim movement, public "
            "posture, or cross-repo truth."
        ),
    )


def missing_requirements(packet: AdmissionPacket, route: ClosedRoute) -> tuple[str, ...]:
    missing: list[str] = []

    if route.closing_tests:
        cited = set(packet.closed_lineage_citations)
        if not set(route.closing_tests).issubset(cited):
            missing.append("closed_lineage_citations")
        if not set(route.required_new_keys).intersection(packet.new_keys):
            missing.append("closed_route_new_key")

    core_checks = (
        ("native_capability_object", packet.declares_native_capability_object),
        ("task_family", packet.declares_task_family),
        ("observer_access_boundary", packet.declares_observer_access_boundary),
        ("completion_rights", packet.declares_completion_rights),
        ("visible_projection", packet.declares_visible_projection),
    )
    missing.extend(name for name, ok in core_checks if not ok)

    if not packet.absorber_checks:
        missing.append("declared_mature_absorbers")
    else:
        unresolved = tuple(
            check.name
            for check in packet.absorber_checks
            if check.status not in {"tested", "not_applicable_with_reason"}
        )
        if unresolved:
            missing.append("tested_absorber_checks")

    if packet.domain_law_source not in ALLOWED_DOMAIN_LAW_SOURCES:
        missing.append("domain_native_law_or_theorem_source")
    if not packet.capability_spread_non_singleton:
        missing.append("capability_spread_evidence")
    if not packet.positive_controls_pass:
        missing.append("positive_controls")
    if not packet.minimality_condition_declared:
        missing.append("minimality_condition")
    if not packet.demotion_path_declared:
        missing.append("demotion_path")

    return tuple(missing)


def blocked_shortcuts(packet: AdmissionPacket) -> tuple[str, ...]:
    blocked: list[str] = []
    if packet.requests_claim_movement:
        blocked.append("claim_movement")
    if packet.requests_public_posture_movement:
        blocked.append("public_posture_movement")
    if packet.requests_external_publication:
        blocked.append("external_publication")
    if packet.requests_cross_repo_truth_movement:
        blocked.append("cross_repo_truth_movement")
    return tuple(blocked)


def run() -> dict[str, Any]:
    routes = closed_routes()
    packets = fixture_packets()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    admitted = tuple(decision.packet_id for decision in decisions if decision.admitted)
    rejected = tuple(decision.packet_id for decision in decisions if not decision.admitted)

    return {
        "artifact": ARTIFACT,
        "source_synthesis": SOURCE_SYNTHESIS,
        "source_packet_report": SOURCE_PACKET_REPORT,
        "source_packet_template": SOURCE_PACKET_TEMPLATE,
        "verdict": VERDICT,
        "honest_ceiling": HONEST_CEILING,
        "allowed_domain_law_sources": sorted(ALLOWED_DOMAIN_LAW_SOURCES),
        "closed_routes": {
            route_id: route_to_dict(route) for route_id, route in sorted(routes.items())
        },
        "packets": [packet_to_dict(packet) for packet in packets],
        "decisions": [decision_to_dict(decision) for decision in decisions],
        "admitted_packet_ids": list(admitted),
        "rejected_packet_ids": list(rejected),
        "overall": {
            "admitted_count": len(admitted),
            "rejected_count": len(rejected),
            "review_target_only": all(
                decision.review_target_only for decision in decisions if decision.admitted
            ),
            "claim_movement": False,
            "public_posture_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "strongest_result": (
            "The Bridge-Functor packet form admits only fully typed review "
            "targets that cite closed lineage, bring a required new key, declare "
            "Cap/pi/observer/completion rights, test mature absorbers, supply a "
            "domain-native law or theorem source, show capability-spread evidence, "
            "pass positive controls, and declare minimality plus demotion. It "
            "rejects analogy-only, incomplete, minor-restart, and governance "
            "shortcut packets."
        ),
        "recommended_next": (
            "Use T496 as the preflight gate before reopening S1, RG/reachability, "
            "valid-coarse-graining, typed-gap, or bounded-retrieval surfaces. "
            "Do not treat admission as evidence; execute the admitted packet first."
        ),
    }


def packet_to_dict(packet: AdmissionPacket) -> dict[str, Any]:
    payload = asdict(packet)
    payload["closed_lineage_citations"] = list(packet.closed_lineage_citations)
    payload["new_keys"] = list(packet.new_keys)
    payload["absorber_checks"] = [asdict(check) for check in packet.absorber_checks]
    return payload


def route_to_dict(route: ClosedRoute) -> dict[str, Any]:
    return {
        "route_id": route.route_id,
        "closing_tests": list(route.closing_tests),
        "required_new_keys": list(route.required_new_keys),
        "note": route.note,
    }


def decision_to_dict(decision: AdmissionDecision) -> dict[str, Any]:
    return {
        "packet_id": decision.packet_id,
        "admitted": decision.admitted,
        "label": decision.label,
        "action": decision.action,
        "review_target_only": decision.review_target_only,
        "missing_requirements": list(decision.missing_requirements),
        "blocked_shortcuts": list(decision.blocked_shortcuts),
        "reason": decision.reason,
        "strongest_allowed_reading": decision.strongest_allowed_reading,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    route_rows = [
        "| {route_id} | {closing} | {keys} | {note} |".format(
            route_id=route["route_id"],
            closing=", ".join(route["closing_tests"]) or "none",
            keys=", ".join(route["required_new_keys"]) or "none",
            note=route["note"],
        )
        for route in payload["closed_routes"].values()
    ]
    decision_rows = [
        "| {packet_id} | {admitted} | {label} | {action} | {missing} | {blocked} | {reason} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            action=decision["action"],
            missing=", ".join(decision["missing_requirements"]) or "none",
            blocked=", ".join(decision["blocked_shortcuts"]) or "none",
            reason=decision["reason"],
        )
        for decision in payload["decisions"]
    ]
    law_sources = [f"- {item}" for item in payload["allowed_domain_law_sources"]]

    return "\n".join(
        [
            "# T496 - Bridge-Functor Admission Packet Gate - v0.1 results",
            "",
            "> Admission gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T496-bridge-functor-admission-packet-gate.md`",
            "- Model: `models/bridge_functor_admission_packet_gate.py`",
            "- Tests: `tests/test_bridge_functor_admission_packet_gate.py`",
            "- Source synthesis: `explorations/persona-missing-analysis-hegelian-metasynthesis-2026-07-07.md`",
            "- Source packet report: `technical-reports/TECHNICAL-REPORT-bridge-functor-admission-packet-v0.1.md`",
            "- Source packet template: `workflows/templates/bridge-functor-admission-packet.template.md`",
            "- Artifact JSON: `results/T496-bridge-functor-admission-packet-gate-v0.1.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Closed Route Requirements",
            "",
            "| Route | Closing tests | Required new keys | Note |",
            "| --- | --- | --- | --- |",
            *route_rows,
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Action | Missing requirements | Blocked shortcuts | Reason |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *decision_rows,
            "",
            "## Allowed Domain Law Sources",
            "",
            *law_sources,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable hostile admission gate for future bridge/functor packets and closed-route restarts.",
            "",
            "Does not earn: any theorem, physics support, claim-ledger movement, roadmap movement, README movement, North Star movement, public-posture movement, hard-policy movement, external-publication permission, or cross-repo truth movement.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T496-bridge-functor-admission-packet-gate-v0.1.json"
        md_path = results_dir / "T496-bridge-functor-admission-packet-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
