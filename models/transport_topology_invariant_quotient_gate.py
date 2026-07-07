"""T485: transport-topology invariant quotient gate.

T484 left one narrow caveat: component-size and path-length readings are
blocked unless a future packet declares an invariant morphism class. This
module makes that caveat executable over the T24/T38 fixed-D1 transport
fixtures.

The positive result is intentionally weak. The finite trust-reachability
quotient over original observer sites is stable under observer relabeling and
iterated edge subdivision. Component size, path length, hop bands, and relay
count are not stable under that same benign refinement. The quotient therefore
remains reachability bookkeeping only; it earns no internal scale structure,
clock, duration, record-finality change, scale-genesis theorem, physics
support, claim movement, or public-posture movement.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from models.multiscale_observer_field import (
    D1FieldScenario,
    FieldEdge,
    ObserverProfile,
    connected_transport_scenario,
    partitioned_transport_scenario,
)
from models.transport_topology_refinement_naturalness_gate import (
    run as run_t484,
)


ARTIFACT_ID = "T485-transport-topology-invariant-quotient-gate-v0.1"
VERDICT = "TRANSPORT_TOPOLOGY_INVARIANT_QUOTIENT_BUILT_REACHABILITY_ONLY"


@dataclass(frozen=True)
class QuotientCandidate:
    """One proposed post-T484 invariant topology packet."""

    candidate_id: str
    role: str
    generator_rule: str
    comparison_domain: str
    local_taf_anchor: str
    predeclared_morphism_class: bool
    quotient_or_invariant_declared: bool
    fixed_d1_control_declared: bool
    refinement_invariance_check_declared: bool
    relabel_invariance_check_declared: bool
    uses_reachability_quotient: bool = False
    uses_component_count: bool = False
    uses_component_size: bool = False
    uses_path_length: bool = False
    uses_hop_band: bool = False
    uses_relay_count: bool = False
    derived_from_reachability_quotient: bool = False
    treats_quotient_as_scale_structure: bool = False
    uses_hidden_calendar_or_time_order: bool = False
    derives_clock_duration_or_arrow: bool = False
    changes_record_finality: bool = False
    imports_rg_or_conformal_mechanism: bool = False
    claims_scale_genesis_or_physics: bool = False
    requests_claim_or_posture_promotion: bool = False


def quotient_candidates() -> tuple[QuotientCandidate, ...]:
    """Return the finite T485 candidate catalogue."""

    return (
        QuotientCandidate(
            candidate_id="reachability_quotient_packet",
            role="positive_review_control",
            generator_rule=(
                "collapse trust-preserving transport refinements to the finite "
                "same-component quotient over original observer sites, typed by "
                "source/target reachability role"
            ),
            comparison_domain=(
                "T24/T38 connected and partitioned fixed-D1 fixtures, observer "
                "relabelings, and iterated trust-edge subdivisions"
            ),
            local_taf_anchor="T24/T38/T480/T481/T482/T483/T484",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_reachability_quotient=True,
        ),
        QuotientCandidate(
            candidate_id="component_count_summary",
            role="absorbed_control",
            generator_rule="count source/target reachability quotient blocks",
            comparison_domain="same quotient used by the positive packet",
            local_taf_anchor="T484 caveat",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_component_count=True,
            derived_from_reachability_quotient=True,
        ),
        QuotientCandidate(
            candidate_id="component_size_invariant_scale",
            role="hostile_control",
            generator_rule="use total trust-component size as internal scale",
            comparison_domain="original and edge-subdivided T24/T38 fixtures",
            local_taf_anchor="T484 overread",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_component_size=True,
            claims_scale_genesis_or_physics=True,
        ),
        QuotientCandidate(
            candidate_id="shortest_path_invariant_scale",
            role="hostile_control",
            generator_rule="use source-target shortest trust path as internal scale",
            comparison_domain="original and edge-subdivided T24/T38 fixtures",
            local_taf_anchor="T484 overread",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_path_length=True,
            claims_scale_genesis_or_physics=True,
        ),
        QuotientCandidate(
            candidate_id="finite_hop_band_scale",
            role="hostile_control",
            generator_rule="bucket source-target hop count into short/middle/long scale bands",
            comparison_domain="iterated edge subdivisions of the same connected fixture",
            local_taf_anchor="T484 caveat",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_hop_band=True,
            claims_scale_genesis_or_physics=True,
        ),
        QuotientCandidate(
            candidate_id="relay_count_internal_clock",
            role="hostile_control",
            generator_rule="treat inserted refinement relays as elapsed record time",
            comparison_domain="edge-subdivision metadata",
            local_taf_anchor="T484 relay overread",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=False,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_relay_count=True,
            uses_hidden_calendar_or_time_order=True,
            derives_clock_duration_or_arrow=True,
        ),
        QuotientCandidate(
            candidate_id="quotient_as_internal_scale_structure",
            role="hostile_control",
            generator_rule="declare the reachability quotient itself to be internal scale",
            comparison_domain="T24/T38/T484 reachability quotient",
            local_taf_anchor="T484 promotion shortcut",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_reachability_quotient=True,
            treats_quotient_as_scale_structure=True,
        ),
        QuotientCandidate(
            candidate_id="reachability_finality_status",
            role="hostile_control",
            generator_rule="mark source-target reachable blocks as record-final",
            comparison_domain="reachability quotient roles",
            local_taf_anchor="T484 finality overread",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_reachability_quotient=True,
            changes_record_finality=True,
        ),
        QuotientCandidate(
            candidate_id="rg_conformal_morphism_class_import",
            role="hostile_control",
            generator_rule="use RG or conformal fixed-point equivalence as the topology morphism class",
            comparison_domain="external RG/conformal scale classes",
            local_taf_anchor="external RG/conformal mechanism",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=False,
            refinement_invariance_check_declared=False,
            relabel_invariance_check_declared=False,
            imports_rg_or_conformal_mechanism=True,
            claims_scale_genesis_or_physics=True,
        ),
        QuotientCandidate(
            candidate_id="promotion_shortcut_quotient",
            role="hostile_control",
            generator_rule="promote refinement-stable reachability quotient to D1 or scale theorem",
            comparison_domain="T24/T38/T484 quotient evidence",
            local_taf_anchor="T484 promotion shortcut",
            predeclared_morphism_class=True,
            quotient_or_invariant_declared=True,
            fixed_d1_control_declared=True,
            refinement_invariance_check_declared=True,
            relabel_invariance_check_declared=True,
            uses_reachability_quotient=True,
            treats_quotient_as_scale_structure=True,
            claims_scale_genesis_or_physics=True,
            requests_claim_or_posture_promotion=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T485 transport-topology invariant quotient gate."""

    anchor_checks = _anchor_checks()
    quotient_probe = _quotient_probe()
    evaluations = [
        _evaluate_candidate(candidate, anchor_checks, quotient_probe)
        for candidate in quotient_candidates()
    ]
    admitted = [row["candidate_id"] for row in evaluations if row["admitted"]]
    hostile_violations = [
        row["candidate_id"]
        for row in evaluations
        if row["role"] == "hostile_control" and row["admitted"]
    ]
    expected_admissions = ["reachability_quotient_packet"]
    component_count_absorbed = _candidate_decision(
        evaluations,
        "component_count_summary",
    )["decision"] == "absorb_quotient_summary_no_independent_generator"
    component_size_blocked = _candidate_decision(
        evaluations,
        "component_size_invariant_scale",
    )["decision"] == "reject_refinement_variant"
    path_length_blocked = _candidate_decision(
        evaluations,
        "shortest_path_invariant_scale",
    )["decision"] == "reject_refinement_variant"
    hop_band_blocked = _candidate_decision(
        evaluations,
        "finite_hop_band_scale",
    )["decision"] == "reject_refinement_variant"
    gate_passed = (
        anchor_checks["t484_gate_passed"]
        and anchor_checks["t484_reachability_bookkeeping_only"]
        and quotient_probe["controls"]["original_d1_vectors_fixed"]
        and quotient_probe["controls"]["reachability_quotient_separates_fixed_d1_pair"]
        and quotient_probe["controls"]["connected_quotient_stable_under_refinement"]
        and quotient_probe["controls"]["partitioned_quotient_stable_under_refinement"]
        and quotient_probe["controls"]["quotient_relabel_invariant"]
        and quotient_probe["controls"]["component_size_changes_under_iterated_refinement"]
        and quotient_probe["controls"]["path_length_changes_under_iterated_refinement"]
        and quotient_probe["controls"]["hop_band_changes_under_iterated_refinement"]
        and quotient_probe["controls"]["component_count_is_quotient_summary"]
        and admitted == expected_admissions
        and component_count_absorbed
        and component_size_blocked
        and path_length_blocked
        and hop_band_blocked
        and not hostile_violations
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Make T484's invariant-morphism caveat executable by admitting only "
            "the trust-reachability quotient over original observer sites, while "
            "rejecting component size, path length, hop bands, relay count, "
            "clock/finality, RG/conformal, physics, and promotion overreads."
        ),
        "local_anchor_checks": anchor_checks,
        "quotient_probe": quotient_probe,
        "candidate_evaluations": evaluations,
        "admitted_candidate_ids": admitted,
        "hostile_violations": hostile_violations,
        "overall_verdict": {
            "verdict": VERDICT,
            "gate_passed": gate_passed,
            "reachability_quotient_admitted": admitted == expected_admissions,
            "component_count_absorbed": component_count_absorbed,
            "component_size_scale_blocked": component_size_blocked,
            "path_length_scale_blocked": path_length_blocked,
            "hop_band_scale_blocked": hop_band_blocked,
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
                "T485 turns T484's invariant-morphism caveat into a finite gate. "
                "After quotienting away trust-edge subdivisions and observer "
                "relabelings, the only admitted topology datum is the "
                "source/target trust-reachability quotient over original "
                "observer sites. Component count is a derived quotient summary, "
                "not an independent generator. Component size, shortest path, "
                "hop bands, and relay counts vary under benign refinement, so "
                "they remain blocked as internal-scale, clock, duration, "
                "finality, or scale-genesis evidence."
            ),
        },
        "future_packet_minimum": [
            "declare the topology morphism or refinement class before using topology as a generator",
            "quotient relay/refinement artifacts away from original observer-site reachability",
            "treat component count as a quotient summary, not an independent internal-scale generator",
            "reject component size, shortest path length, hop bands, and relay count under trust-edge subdivision unless a stricter domain-native morphism class is justified",
            "preserve fixed-D1 controls and observer-label relabel invariance",
            "keep reachability topology separate from scale, clock, duration, finality, RG/conformal, physics, and promotion language",
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
    """Render T485 results as Markdown."""

    verdict = result["overall_verdict"]
    anchor_rows = [
        f"| {key} | {value} |"
        for key, value in result["local_anchor_checks"].items()
    ]
    control_rows = [
        f"| {key} | {value} |"
        for key, value in result["quotient_probe"]["controls"].items()
    ]
    fixture_rows = [
        _fixture_row(name, fixture)
        for name, fixture in result["quotient_probe"]["fixture_summaries"].items()
    ]
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
            "# T485 - Transport Topology Invariant Quotient Gate - v0.1 results",
            "",
            "> Review gate only. No claim status, roadmap, README, North Star, "
            "public-posture, hard-policy, physics, scale-genesis, clock, "
            "duration, finality, or cross-repo movement.",
            "",
            "- Spec: `tests/T485-transport-topology-invariant-quotient-gate.md`",
            "- Model: `models/transport_topology_invariant_quotient_gate.py`",
            "- Tests: `tests/test_transport_topology_invariant_quotient_gate.py`",
            "- Artifact JSON: `results/T485-transport-topology-invariant-quotient-gate-v0.1.json`",
            "- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`",
            "- Local anchors: T24, T38, T480, T481, T482, T483, and T484",
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
            "## Quotient Controls",
            "",
            "| check | value |",
            "| --- | --- |",
            *control_rows,
            "",
            "## Fixture Summaries",
            "",
            "| fixture | quotient signature | component sizes | path length | hop band |",
            "| --- | --- | --- | --- | --- |",
            *fixture_rows,
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
    t484 = run_t484()
    verdict = t484["overall_verdict"]
    return {
        "t484_gate_passed": verdict["gate_passed"],
        "t484_reachability_bookkeeping_only": (
            verdict["verdict"]
            == "TRANSPORT_TOPOLOGY_REFINEMENT_GATE_BUILT_REACHABILITY_BOOKKEEPING_ONLY"
        ),
        "t484_component_size_blocked": verdict["component_size_scale_blocked"],
        "t484_path_length_blocked": verdict["path_length_scale_blocked"],
        "t484_no_internal_scale_structure_earned": (
            verdict["internal_scale_structure_earned"] is False
        ),
        "t484_future_packet_requires_refinement_controls": (
            "include transport-refinement controls before using topology as a generator"
            in t484["future_packet_minimum"]
        ),
    }


def _quotient_probe() -> dict[str, Any]:
    connected = connected_transport_scenario()
    partitioned = partitioned_transport_scenario()
    connected_once = _subdivide_trust_edges(connected, "connected", rounds=1)
    connected_twice = _subdivide_trust_edges(connected, "connected", rounds=2)
    partitioned_once = _subdivide_trust_edges(partitioned, "partitioned", rounds=1)
    partitioned_twice = _subdivide_trust_edges(partitioned, "partitioned", rounds=2)
    relabeled_connected, relabel_map = _relabel_scenario(connected)

    connected_ids = _original_observer_ids(connected)
    partitioned_ids = _original_observer_ids(partitioned)
    relabeled_ids = tuple(sorted(relabel_map[observer_id] for observer_id in connected_ids))

    fixtures = {
        "connected_original": _fixture_summary(connected, connected_ids),
        "connected_subdivided_once": _fixture_summary(connected_once, connected_ids),
        "connected_subdivided_twice": _fixture_summary(connected_twice, connected_ids),
        "partitioned_original": _fixture_summary(partitioned, partitioned_ids),
        "partitioned_subdivided_once": _fixture_summary(partitioned_once, partitioned_ids),
        "partitioned_subdivided_twice": _fixture_summary(partitioned_twice, partitioned_ids),
        "connected_relabel": _fixture_summary(relabeled_connected, relabeled_ids),
    }

    connected_signature = fixtures["connected_original"]["quotient_signature"]
    partitioned_signature = fixtures["partitioned_original"]["quotient_signature"]
    connected_size_variants = {
        tuple(fixtures[name]["component_size_signature"])
        for name in (
            "connected_original",
            "connected_subdivided_once",
            "connected_subdivided_twice",
        )
    }
    connected_path_variants = {
        fixtures[name]["source_target_path_length"]
        for name in (
            "connected_original",
            "connected_subdivided_once",
            "connected_subdivided_twice",
        )
    }
    connected_hop_variants = {
        fixtures[name]["source_target_hop_band"]
        for name in (
            "connected_original",
            "connected_subdivided_once",
            "connected_subdivided_twice",
        )
    }

    controls = {
        "original_d1_vectors_fixed": (
            _d1_vector_for_observers(connected, connected_ids)
            == _d1_vector_for_observers(partitioned, partitioned_ids)
            == _d1_vector_for_observers(connected_once, connected_ids)
            == _d1_vector_for_observers(partitioned_once, partitioned_ids)
            == _d1_vector_for_observers(connected_twice, connected_ids)
            == _d1_vector_for_observers(partitioned_twice, partitioned_ids)
        ),
        "reachability_quotient_separates_fixed_d1_pair": (
            connected_signature != partitioned_signature
        ),
        "connected_quotient_stable_under_refinement": (
            connected_signature
            == fixtures["connected_subdivided_once"]["quotient_signature"]
            == fixtures["connected_subdivided_twice"]["quotient_signature"]
        ),
        "partitioned_quotient_stable_under_refinement": (
            partitioned_signature
            == fixtures["partitioned_subdivided_once"]["quotient_signature"]
            == fixtures["partitioned_subdivided_twice"]["quotient_signature"]
        ),
        "quotient_relabel_invariant": (
            connected_signature
            == fixtures["connected_relabel"]["quotient_signature"]
        ),
        "component_size_changes_under_iterated_refinement": (
            len(connected_size_variants) > 1
        ),
        "path_length_changes_under_iterated_refinement": (
            len(connected_path_variants) > 1
        ),
        "hop_band_changes_under_iterated_refinement": (
            len(connected_hop_variants) > 1
        ),
        "component_count_is_quotient_summary": (
            fixtures["connected_original"]["quotient_block_count"] == 1
            and fixtures["partitioned_original"]["quotient_block_count"] == 2
            and fixtures["connected_original"]["quotient_block_count"]
            == len(fixtures["connected_original"]["quotient_signature"])
        ),
        "uses_clock_duration_or_finality_status": False,
        "imports_rg_or_conformal_mechanism": False,
    }

    return {
        "generator_rule": (
            "same trust-preserving component quotient over original observer "
            "sites, with quotient blocks typed by source/target reachability role"
        ),
        "morphism_class": (
            "observer-label relabeling plus finite subdivision of trust-preserving "
            "transport edges, with relay sites forgotten back to original observer sites"
        ),
        "fixture_summaries": fixtures,
        "controls": controls,
        "reading": (
            "The reachability quotient survives the declared refinement class and "
            "still separates the connected and partitioned fixed-D1 pair. The "
            "quantities that look scale-like before quotienting are exactly the "
            "refinement artifacts: component size, path length, hop bands, and "
            "relay count."
        ),
    }


def _evaluate_candidate(
    candidate: QuotientCandidate,
    anchor_checks: dict[str, Any],
    quotient_probe: dict[str, Any],
) -> dict[str, Any]:
    blockers: list[str] = []

    if not anchor_checks["t484_gate_passed"]:
        blockers.append("t484_gate_missing")
    if not candidate.predeclared_morphism_class:
        blockers.append("morphism_class_not_predeclared")
    if not candidate.quotient_or_invariant_declared:
        blockers.append("quotient_or_invariant_not_declared")
    if not candidate.fixed_d1_control_declared:
        blockers.append("fixed_d1_control_missing")
    if not candidate.refinement_invariance_check_declared:
        blockers.append("refinement_invariance_check_missing")
    if not candidate.relabel_invariance_check_declared:
        blockers.append("relabel_invariance_check_missing")
    if (
        candidate.uses_reachability_quotient
        and not quotient_probe["controls"]["connected_quotient_stable_under_refinement"]
    ):
        blockers.append("reachability_quotient_refinement_invariance_failed")
    if candidate.uses_component_count and candidate.derived_from_reachability_quotient:
        blockers.append("component_count_derived_from_reachability_quotient")
    if (
        candidate.uses_component_size
        and quotient_probe["controls"]["component_size_changes_under_iterated_refinement"]
    ):
        blockers.append("component_size_refinement_variant")
    if (
        candidate.uses_path_length
        and quotient_probe["controls"]["path_length_changes_under_iterated_refinement"]
    ):
        blockers.append("path_length_refinement_variant")
    if (
        candidate.uses_hop_band
        and quotient_probe["controls"]["hop_band_changes_under_iterated_refinement"]
    ):
        blockers.append("hop_band_refinement_variant")
    if candidate.uses_relay_count:
        blockers.append("relay_count_is_refinement_artifact")
    if candidate.treats_quotient_as_scale_structure:
        blockers.append("reachability_quotient_not_internal_scale_structure")
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
        route_label = "REACHABILITY_QUOTIENT_BOOKKEEPING_ADMITTED_NO_SCALE_STRUCTURE"
        decision = "admit_reachability_quotient_no_scale_structure"
    elif "component_count_derived_from_reachability_quotient" in blockers:
        route_label = "QUOTIENT_SUMMARY_ABSORBED"
        decision = "absorb_quotient_summary_no_independent_generator"
    elif any(
        blocker in blockers
        for blocker in (
            "component_size_refinement_variant",
            "path_length_refinement_variant",
            "hop_band_refinement_variant",
            "relay_count_is_refinement_artifact",
        )
    ):
        route_label = "REFINEMENT_VARIANT_SCALE_READING_BLOCKED"
        decision = "reject_refinement_variant"
    else:
        route_label = "TOPOLOGY_QUOTIENT_PACKET_BLOCKED"
        decision = "reject_or_block"

    return {
        "candidate_id": candidate.candidate_id,
        "role": candidate.role,
        "generator_rule": candidate.generator_rule,
        "comparison_domain": candidate.comparison_domain,
        "local_taf_anchor": candidate.local_taf_anchor,
        "uses_reachability_quotient": candidate.uses_reachability_quotient,
        "uses_component_count": candidate.uses_component_count,
        "uses_component_size": candidate.uses_component_size,
        "uses_path_length": candidate.uses_path_length,
        "uses_hop_band": candidate.uses_hop_band,
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


def _fixture_summary(
    scenario: D1FieldScenario,
    original_observer_ids: tuple[str, ...],
) -> dict[str, Any]:
    quotient_blocks = _quotient_blocks(scenario, original_observer_ids)
    component_sizes = _component_size_signature(scenario, original_observer_ids)
    path_length = _shortest_path_length(
        scenario,
        scenario.source_observer,
        scenario.target_observer,
    )
    return {
        "quotient_blocks": quotient_blocks,
        "quotient_signature": _quotient_signature(quotient_blocks),
        "quotient_block_count": len(quotient_blocks),
        "component_size_signature": component_sizes,
        "source_target_path_length": path_length,
        "source_target_hop_band": _hop_band(path_length),
        "relay_site_count": len(_observer_ids(scenario) - set(original_observer_ids)),
    }


def _quotient_blocks(
    scenario: D1FieldScenario,
    original_observer_ids: tuple[str, ...],
) -> list[dict[str, Any]]:
    component_by_observer = _component_ids(scenario)
    source_component = component_by_observer[scenario.source_observer]
    target_component = component_by_observer[scenario.target_observer]
    component_sizes: dict[int, int] = {}
    for component_id in component_by_observer.values():
        component_sizes[component_id] = component_sizes.get(component_id, 0) + 1

    originals_by_component: dict[int, list[str]] = {}
    for observer_id in original_observer_ids:
        component_id = component_by_observer[observer_id]
        originals_by_component.setdefault(component_id, []).append(observer_id)

    blocks = []
    for component_id, observers in sorted(
        originals_by_component.items(),
        key=lambda item: (_component_role(item[0], source_component, target_component), sorted(item[1])),
    ):
        role = _component_role(component_id, source_component, target_component)
        blocks.append(
            {
                "role": role,
                "original_observer_count": len(observers),
                "component_size_including_relays": component_sizes[component_id],
                "original_observers": sorted(observers),
            }
        )
    return blocks


def _quotient_signature(blocks: list[dict[str, Any]]) -> tuple[tuple[str, int], ...]:
    return tuple(
        sorted(
            (block["role"], block["original_observer_count"])
            for block in blocks
        )
    )


def _component_role(
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


def _component_size_signature(
    scenario: D1FieldScenario,
    original_observer_ids: tuple[str, ...],
) -> tuple[tuple[str, int], ...]:
    component_by_observer = _component_ids(scenario)
    component_sizes: dict[int, int] = {}
    for component_id in component_by_observer.values():
        component_sizes[component_id] = component_sizes.get(component_id, 0) + 1
    return tuple(
        (observer_id, component_sizes[component_by_observer[observer_id]])
        for observer_id in sorted(original_observer_ids)
    )


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


def _subdivide_trust_edges(
    scenario: D1FieldScenario,
    prefix: str,
    rounds: int,
) -> D1FieldScenario:
    """Subdivide each trust-preserving edge for a finite number of rounds."""

    refined = scenario
    for round_index in range(rounds):
        profile_by_id = _profile_by_observer(refined)
        profiles = list(refined.observer_profiles)
        edges: list[FieldEdge] = []
        for edge_index, edge in enumerate(refined.edges):
            if not edge.trust_preserving:
                edges.append(edge)
                continue
            relay_id = (
                f"{prefix}_r{round_index}_relay_{edge_index}_"
                f"{edge.source}_{edge.target}"
            )
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
        refined = replace(
            refined,
            name=f"{refined.name}_subdivided_r{round_index}",
            observer_profiles=tuple(profiles),
            edges=tuple(edges),
        )
    return refined


def _relabel_scenario(
    scenario: D1FieldScenario,
) -> tuple[D1FieldScenario, dict[str, str]]:
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
    return (
        replace(
            scenario,
            observer_profiles=profiles,
            edges=edges,
            source_observer=relabel_map[scenario.source_observer],
            target_observer=relabel_map[scenario.target_observer],
        ),
        relabel_map,
    )


def _relabel_profile(
    profile: ObserverProfile,
    relabel_map: dict[str, str],
) -> ObserverProfile:
    site = replace(profile.site, observer_id=relabel_map[profile.site.observer_id])
    return replace(profile, site=site)


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


def _hop_band(path_length: int | None) -> str:
    if path_length is None:
        return "unreachable"
    if path_length <= 4:
        return "short"
    if path_length <= 8:
        return "middle"
    return "long"


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


def _fixture_row(name: str, fixture: dict[str, Any]) -> str:
    return "| {name} | {signature} | {sizes} | {path} | {band} |".format(
        name=name,
        signature=fixture["quotient_signature"],
        sizes=fixture["component_size_signature"],
        path=fixture["source_target_path_length"],
        band=fixture["source_target_hop_band"],
    )


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
