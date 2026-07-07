"""T482: internal scale-generator invariance probe.

T481 admitted a future internal-scale packet only as a review target if the
packet predeclares a TaF-native generator, comparison domain, controls, and a
relabel-invariance check. This module makes one concrete attempt: a finite
D1-support-gradient generator over T24 field-valued D1 profiles.

The result is intentionally conservative. The support-gradient packet is
admitted only as review-grade D1 bookkeeping because the generated scale bands
factor entirely through the existing D1 profile tuple. It earns no independent
internal scale structure, clock, duration, finality change, scale-genesis
theorem, physics support, or claim movement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from models.internal_scale_structure_admission_gate import run as run_t481
from models.multiscale_observer_field import (
    D1FieldScenario,
    D1Profile,
    FieldEdge,
    ObserverProfile,
    stratified_access_scenario,
    uniform_broadcast_scenario,
)


ARTIFACT_ID = "T482-internal-scale-generator-invariance-probe-v0.1"
VERDICT = "D1_SUPPORT_GRADIENT_PROBE_BUILT_BOOKKEEPING_ONLY_NO_SCALE_STRUCTURE"


@dataclass(frozen=True)
class ScaleGeneratorCandidate:
    """One proposed post-T481 internal-scale generator packet."""

    candidate_id: str
    role: str
    generator_rule: str
    comparison_domain: str
    local_taf_anchor: str
    predeclared_generator: bool
    comparison_domain_predeclared: bool
    positive_negative_controls_declared: bool
    relabel_invariance_check_declared: bool
    factors_through_d1_profile: bool = False
    posthoc_thresholds: bool = False
    label_only_without_generator: bool = False
    uses_observer_id_order: bool = False
    uses_hidden_calendar_or_time_order: bool = False
    derives_clock_duration_or_arrow: bool = False
    changes_record_finality: bool = False
    imports_rg_or_conformal_mechanism: bool = False
    claims_scale_genesis_or_physics: bool = False
    requests_claim_or_posture_promotion: bool = False


def scale_generator_candidates() -> tuple[ScaleGeneratorCandidate, ...]:
    """Return the finite T482 candidate catalogue."""

    return (
        ScaleGeneratorCandidate(
            candidate_id="d1_support_gradient_review_packet",
            role="positive_review_control",
            generator_rule=(
                "sum D1 tuple components into support_depth and assign "
                "predeclared bands low<=4, middle<=8, high>8"
            ),
            comparison_domain=(
                "T24 observer sites and declared T38/T480 transport edges over "
                "field-valued D1 profiles"
            ),
            local_taf_anchor="T24/T38/T480/T481",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            positive_negative_controls_declared=True,
            relabel_invariance_check_declared=True,
            factors_through_d1_profile=True,
        ),
        ScaleGeneratorCandidate(
            candidate_id="label_word_internal_scale",
            role="hostile_control",
            generator_rule="call each observer label a scale",
            comparison_domain="observer labels",
            local_taf_anchor="T481 shortcut",
            predeclared_generator=False,
            comparison_domain_predeclared=False,
            positive_negative_controls_declared=False,
            relabel_invariance_check_declared=False,
            label_only_without_generator=True,
        ),
        ScaleGeneratorCandidate(
            candidate_id="posthoc_support_thresholds",
            role="hostile_control",
            generator_rule="choose support-depth thresholds after seeing the split",
            comparison_domain="selected after separator construction",
            local_taf_anchor="T24/T481 overread",
            predeclared_generator=False,
            comparison_domain_predeclared=False,
            positive_negative_controls_declared=True,
            relabel_invariance_check_declared=True,
            factors_through_d1_profile=True,
            posthoc_thresholds=True,
        ),
        ScaleGeneratorCandidate(
            candidate_id="observer_id_rank_generator",
            role="hostile_control",
            generator_rule="rank observer identifiers alphabetically",
            comparison_domain="observer-id order",
            local_taf_anchor="T24 labels only",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            positive_negative_controls_declared=True,
            relabel_invariance_check_declared=True,
            uses_observer_id_order=True,
        ),
        ScaleGeneratorCandidate(
            candidate_id="hidden_time_step_generator",
            role="hostile_control",
            generator_rule="derive scale from hidden time_step or calendar order",
            comparison_domain="hidden temporal order",
            local_taf_anchor="T24 metadata overread",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            positive_negative_controls_declared=False,
            relabel_invariance_check_declared=True,
            uses_hidden_calendar_or_time_order=True,
            derives_clock_duration_or_arrow=True,
        ),
        ScaleGeneratorCandidate(
            candidate_id="finality_by_support_band",
            role="hostile_control",
            generator_rule="mark high support-depth sites final",
            comparison_domain="support-depth bands",
            local_taf_anchor="T24/D1 overread",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            positive_negative_controls_declared=True,
            relabel_invariance_check_declared=True,
            factors_through_d1_profile=True,
            changes_record_finality=True,
        ),
        ScaleGeneratorCandidate(
            candidate_id="rg_fixed_point_scale_generator",
            role="hostile_control",
            generator_rule="import RG or conformal fixed point as scale source",
            comparison_domain="external RG scale classes",
            local_taf_anchor="external RG/conformal mechanism",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            positive_negative_controls_declared=False,
            relabel_invariance_check_declared=False,
            imports_rg_or_conformal_mechanism=True,
            claims_scale_genesis_or_physics=True,
        ),
        ScaleGeneratorCandidate(
            candidate_id="promotion_shortcut_generator",
            role="hostile_control",
            generator_rule="declare support bands to be internal scale structure",
            comparison_domain="T24 sites",
            local_taf_anchor="T24/T38/T481 promotion shortcut",
            predeclared_generator=True,
            comparison_domain_predeclared=True,
            positive_negative_controls_declared=True,
            relabel_invariance_check_declared=True,
            factors_through_d1_profile=True,
            claims_scale_genesis_or_physics=True,
            requests_claim_or_posture_promotion=True,
        ),
    )


def support_depth(profile: D1Profile) -> int:
    """Predeclared support-depth score for the T482 review packet."""

    return sum(profile.as_tuple())


def support_band(depth: int) -> str:
    """Predeclared finite bands used by the D1-support-gradient probe."""

    if depth <= 4:
        return "low_support"
    if depth <= 8:
        return "middle_support"
    return "high_support"


def run() -> dict[str, Any]:
    """Run the T482 internal scale-generator invariance probe."""

    anchor_checks = _anchor_checks()
    generator_probe = _support_gradient_probe()
    evaluations = [
        _evaluate_candidate(candidate, anchor_checks, generator_probe)
        for candidate in scale_generator_candidates()
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
    expected_admissions = ["d1_support_gradient_review_packet"]
    gate_passed = (
        anchor_checks["t481_gate_passed"]
        and anchor_checks["t481_synthetic_review_target_admitted"]
        and admitted == expected_admissions
        and generator_probe["controls"]["stratified_packet_nontrivial"]
        and generator_probe["controls"]["uniform_packet_collapses_to_single_band"]
        and generator_probe["controls"]["support_gradient_relabel_invariant"]
        and not hostile_violations
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Make T481's synthetic internal-scale review target concrete by "
            "testing a predeclared D1-support-gradient generator for "
            "comparison-domain discipline, controls, and relabel invariance."
        ),
        "local_anchor_checks": anchor_checks,
        "support_gradient_probe": generator_probe,
        "candidate_evaluations": evaluations,
        "admitted_candidate_ids": admitted,
        "hostile_violations": hostile_violations,
        "overall_verdict": {
            "verdict": VERDICT,
            "gate_passed": gate_passed,
            "support_gradient_review_packet_admitted": (
                admitted == expected_admissions
            ),
            "hostile_controls_blocked": not hostile_violations,
            "factors_through_existing_d1_profile": True,
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
                "T482 makes T481's review target concrete with a D1-support "
                "gradient generator. The packet is predeclared, uses the T24 "
                "field-valued D1 profile and T38/T480 comparison edges, passes "
                "positive/null controls, and is invariant under observer-label "
                "relabeling. It is still only D1-support bookkeeping because "
                "the bands factor entirely through the existing D1 profile "
                "tuple; no independent internal scale structure is earned."
            ),
        },
        "future_packet_minimum": [
            "keep support-gradient packets labeled as D1 bookkeeping unless an independent generator is supplied",
            "predeclare bands, comparison domain, controls, and relabel-invariance checks before witness construction",
            "include a null control where uniform D1 support collapses to one band",
            "include hostile controls for label order, posthoc thresholds, hidden time, finality changes, RG imports, and promotion shortcuts",
            "block clock, duration, temporal-arrow, finality, scale-genesis, physics, and claim movement unless separately earned",
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
    """Render T482 results as Markdown."""

    verdict = result["overall_verdict"]
    anchor_rows = [
        f"| {key} | {value} |"
        for key, value in result["local_anchor_checks"].items()
    ]
    control_rows = [
        f"| {key} | {value} |"
        for key, value in result["support_gradient_probe"]["controls"].items()
    ]
    assignment_rows = []
    for row in result["support_gradient_probe"]["stratified_assignments"]:
        assignment_rows.append(
            "| {observer_id} | {profile_tuple} | {support_depth} | {support_band} |".format(
                observer_id=row["observer_id"],
                profile_tuple=row["profile_tuple"],
                support_depth=row["support_depth"],
                support_band=row["support_band"],
            )
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
            "# T482 - Internal Scale Generator Invariance Probe - v0.1 results",
            "",
            "> Review probe only. No claim status, roadmap, README, North Star, "
            "public-posture, hard-policy, physics, scale-genesis, clock, "
            "duration, finality, or cross-repo movement.",
            "",
            "- Spec: `tests/T482-internal-scale-generator-invariance-probe.md`",
            "- Model: `models/internal_scale_generator_invariance_probe.py`",
            "- Tests: `tests/test_internal_scale_generator_invariance_probe.py`",
            "- Artifact JSON: `results/T482-internal-scale-generator-invariance-probe-v0.1.json`",
            "- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`",
            "- Local anchors: T24, T38, T480, and T481",
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
            "## Support-Gradient Controls",
            "",
            "| check | value |",
            "| --- | --- |",
            *control_rows,
            "",
            "## Stratified Assignments",
            "",
            "| observer | D1 profile tuple | support depth | band |",
            "| --- | --- | --- | --- |",
            *assignment_rows,
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
    t481 = run_t481()
    return {
        "t481_gate_passed": t481["overall_verdict"]["gate_passed"],
        "t481_synthetic_review_target_admitted": (
            "synthetic_internal_scale_review_target"
            in t481["admitted_candidate_ids"]
        ),
        "t481_external_bookkeeping_still_admitted": (
            "external_scale_label_bookkeeping" in t481["admitted_candidate_ids"]
        ),
        "t481_no_internal_scale_structure_earned": (
            t481["overall_verdict"]["internal_scale_structure_earned"] is False
        ),
        "t481_no_clock_or_duration_earned": (
            t481["overall_verdict"]["record_clock_or_duration_earned"] is False
        ),
        "t481_future_packet_requires_relabel_invariance": (
            "include positive and negative controls plus a relabel-invariance check"
            in t481["future_packet_minimum"]
        ),
    }


def _support_gradient_probe() -> dict[str, Any]:
    stratified = stratified_access_scenario()
    uniform = uniform_broadcast_scenario()
    relabeled = _relabel_scenario(stratified)

    stratified_assignments = _assign_scale_bands(stratified)
    uniform_assignments = _assign_scale_bands(uniform)
    relabeled_assignments = _assign_scale_bands(relabeled)

    stratified_signature = _assignment_signature(stratified_assignments)
    relabeled_signature = _assignment_signature(relabeled_assignments)
    class_counts = _class_counts(stratified_assignments)
    uniform_counts = _class_counts(uniform_assignments)

    controls = {
        "stratified_packet_nontrivial": len(class_counts) > 1,
        "uniform_packet_collapses_to_single_band": len(uniform_counts) == 1,
        "support_gradient_relabel_invariant": (
            stratified_signature == relabeled_signature
        ),
        "comparison_domain_predeclared_as_transport_edges": (
            len(stratified.edges) > 0
            and all(
                edge.source in _observer_ids(stratified)
                and edge.target in _observer_ids(stratified)
                for edge in stratified.edges
            )
        ),
        "generator_factors_through_d1_profile": True,
        "uses_clock_duration_or_finality_status": False,
        "imports_rg_or_conformal_mechanism": False,
    }

    return {
        "generator_rule": (
            "support_depth = accessible_support + holder_redundancy + "
            "branch_support + reversal_cost; bands are low<=4, middle<=8, high>8"
        ),
        "comparison_domain": (
            "declared T24 observer sites and transport edges, with no hidden "
            "calendar, clock, RG scale, or finality-status field"
        ),
        "stratified_assignments": stratified_assignments,
        "uniform_assignments": uniform_assignments,
        "class_counts": class_counts,
        "uniform_class_counts": uniform_counts,
        "relabel_signature": relabeled_signature,
        "controls": controls,
        "reading": (
            "The finite support-gradient generator is stable under observer-label "
            "relabeling and produces a nontrivial stratified fixture, but it is "
            "not independent of D1 because every band is computed directly from "
            "the D1 profile tuple."
        ),
    }


def _evaluate_candidate(
    candidate: ScaleGeneratorCandidate,
    anchor_checks: dict[str, Any],
    generator_probe: dict[str, Any],
) -> dict[str, Any]:
    blockers: list[str] = []

    if not anchor_checks["t481_gate_passed"]:
        blockers.append("t481_gate_missing")
    if not anchor_checks["t481_synthetic_review_target_admitted"]:
        blockers.append("t481_review_target_not_admitted")
    if not candidate.predeclared_generator:
        blockers.append("generator_not_predeclared")
    if not candidate.comparison_domain_predeclared:
        blockers.append("comparison_domain_not_predeclared")
    if not candidate.positive_negative_controls_declared:
        blockers.append("positive_negative_controls_missing")
    if not candidate.relabel_invariance_check_declared:
        blockers.append("relabel_invariance_check_missing")
    if candidate.label_only_without_generator:
        blockers.append("label_word_without_generator")
    if candidate.posthoc_thresholds:
        blockers.append("posthoc_thresholds")
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
    if (
        candidate.candidate_id == "d1_support_gradient_review_packet"
        and not generator_probe["controls"]["support_gradient_relabel_invariant"]
    ):
        blockers.append("support_gradient_relabel_invariance_failed")

    admitted = not blockers and candidate.role == "positive_review_control"
    if admitted and candidate.factors_through_d1_profile:
        route_label = "D1_SUPPORT_GRADIENT_REVIEW_ADMITTED_BOOKKEEPING_ONLY"
        decision = "admit_review_packet_no_scale_structure"
    elif admitted:
        route_label = "INTERNAL_SCALE_GENERATOR_REVIEW_ADMITTED_NO_PROMOTION"
        decision = "admit_review_packet"
    else:
        route_label = "INTERNAL_SCALE_GENERATOR_PACKET_BLOCKED"
        decision = "reject_or_block"

    return {
        "candidate_id": candidate.candidate_id,
        "role": candidate.role,
        "generator_rule": candidate.generator_rule,
        "comparison_domain": candidate.comparison_domain,
        "local_taf_anchor": candidate.local_taf_anchor,
        "factors_through_d1_profile": candidate.factors_through_d1_profile,
        "admitted": admitted,
        "decision": decision,
        "route_label": route_label,
        "blockers": blockers,
    }


def _assign_scale_bands(scenario: D1FieldScenario) -> list[dict[str, Any]]:
    rows = []
    for observer in sorted(
        scenario.observer_profiles,
        key=lambda item: item.site.observer_id,
    ):
        depth = support_depth(observer.profile)
        rows.append(
            {
                "observer_id": observer.site.observer_id,
                "profile_tuple": list(observer.profile.as_tuple()),
                "support_depth": depth,
                "support_band": support_band(depth),
            }
        )
    return rows


def _assignment_signature(assignments: list[dict[str, Any]]) -> list[tuple[str, int]]:
    return sorted(
        (row["support_band"], row["support_depth"])
        for row in assignments
    )


def _class_counts(assignments: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in assignments:
        band = row["support_band"]
        counts[band] = counts.get(band, 0) + 1
    return dict(sorted(counts.items()))


def _observer_ids(scenario: D1FieldScenario) -> set[str]:
    return {profile.site.observer_id for profile in scenario.observer_profiles}


def _relabel_scenario(scenario: D1FieldScenario) -> D1FieldScenario:
    """Return a scenario with observer IDs permuted but D1 data preserved."""

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
