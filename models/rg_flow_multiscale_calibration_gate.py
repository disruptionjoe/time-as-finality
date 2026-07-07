"""T479: RG-flow multiscale calibration gate.

This module turns the RG-flow-as-multiscale-transport analogy into a finite
repo-local calibration gate. It checks whether the analogy can name the three
minimum objects requested by the open problem without importing RG mechanics
as TaF record mechanics:

1. transported structure,
2. transport law,
3. fixed-point / scale-genesis endpoint.

The result is analogy-ledger only.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models.minimal_multiscale_transport import (
    run_t38_analysis,
    t38_result_to_dict,
)
from models.multiscale_observer_field import run_t24_analysis


ARTIFACT_ID = "T479-rg-flow-multiscale-calibration-gate-v0.1"
VERDICT = "RG_FLOW_CALIBRATION_GATE_BUILT_ANALOGY_ONLY_NO_PROMOTION"


@dataclass(frozen=True)
class CalibrationCandidate:
    """One proposed RG/TaF calibration packet."""

    candidate_id: str
    role: str
    transported_structure: str
    transport_law: str
    fixed_point_analogue: str
    local_taf_anchor: str
    external_anchor_grade: str
    imports_coupling_flow_as_record_flow: bool = False
    imports_lagrangian_action: bool = False
    fixed_point_has_intrinsic_scale_or_clock: bool = False
    derives_record_finality_from_rg: bool = False
    uses_conformal_phenomenology_as_support: bool = False
    claims_physics_or_public_posture: bool = False


def calibration_candidates() -> tuple[CalibrationCandidate, ...]:
    """Return the candidate catalogue for the T479 gate."""

    return (
        CalibrationCandidate(
            candidate_id="taf_d1_h1_plus_scale_calibration",
            role="positive_control",
            transported_structure=(
                "field-valued D1 profile: local observer profiles plus "
                "transport and gluing data"
            ),
            transport_law=(
                "finite TypedTransportNetwork/H1+ transport with compression "
                "and emergence annotations"
            ),
            fixed_point_analogue=(
                "scale-invariant calibration endpoint with no intrinsic "
                "record-clock scale until a declared scale-label operation"
            ),
            local_taf_anchor="T24 field-valued D1 plus T38 H1+ transport",
            external_anchor_grade="pointer_grade_rg_conformal_neighbor",
        ),
        CalibrationCandidate(
            candidate_id="coupling_flow_import",
            role="hostile_control",
            transported_structure="coupling constants",
            transport_law="beta function copied from RG",
            fixed_point_analogue="field-theory coupling fixed point",
            local_taf_anchor="external RG only",
            external_anchor_grade="external_mechanism_import",
            imports_coupling_flow_as_record_flow=True,
        ),
        CalibrationCandidate(
            candidate_id="lagrangian_record_action",
            role="hostile_control",
            transported_structure="record action functional",
            transport_law="Euler-Lagrange flow over records",
            fixed_point_analogue="stationary action endpoint",
            local_taf_anchor="no existing TaF action",
            external_anchor_grade="external_mechanism_import",
            imports_lagrangian_action=True,
        ),
        CalibrationCandidate(
            candidate_id="clocked_fixed_point_overread",
            role="hostile_control",
            transported_structure="field-valued D1 profile",
            transport_law="finite scale transport",
            fixed_point_analogue=(
                "scale-invariant endpoint already carrying intrinsic clocks"
            ),
            local_taf_anchor="T24/T38 named but fixed-point guard violated",
            external_anchor_grade="pointer_grade_rg_conformal_neighbor",
            fixed_point_has_intrinsic_scale_or_clock=True,
        ),
        CalibrationCandidate(
            candidate_id="record_finality_from_rg_claim",
            role="hostile_control",
            transported_structure="record/finality structure",
            transport_law="RG flow as record flow",
            fixed_point_analogue="scale genesis proves record finality",
            local_taf_anchor="T24/T38 overread",
            external_anchor_grade="pointer_grade_rg_conformal_neighbor",
            derives_record_finality_from_rg=True,
            claims_physics_or_public_posture=True,
        ),
        CalibrationCandidate(
            candidate_id="fixed_point_only_no_transport",
            role="hostile_control",
            transported_structure="",
            transport_law="",
            fixed_point_analogue="scale-free endpoint",
            local_taf_anchor="N15 pointer only",
            external_anchor_grade="pointer_grade_rg_conformal_neighbor",
        ),
        CalibrationCandidate(
            candidate_id="conformal_phenomenology_support",
            role="hostile_control",
            transported_structure="record/finality structure",
            transport_law="finite scale transport",
            fixed_point_analogue="scale-free conformal endpoint",
            local_taf_anchor="T24/T38 named but support source misused",
            external_anchor_grade="pointer_grade_rg_conformal_neighbor",
            uses_conformal_phenomenology_as_support=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T479 calibration gate."""

    t24 = run_t24_analysis()
    t38 = t38_result_to_dict(run_t38_analysis())
    anchor_checks = _anchor_checks(t24, t38)
    evaluations = [
        _evaluate_candidate(candidate, anchor_checks)
        for candidate in calibration_candidates()
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
    positive_admitted = admitted == ["taf_d1_h1_plus_scale_calibration"]
    gate_passed = (
        anchor_checks["t24_field_d1_required_for_transport_and_gluing_claims"]
        and anchor_checks["t38_h1_plus_is_best_supported"]
        and positive_admitted
        and not hostile_violations
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Test whether the RG-flow multiscale-transport analogy can name "
            "a TaF transported structure, transport law, and fixed-point / "
            "scale-genesis endpoint using existing finite TaF objects while "
            "blocking mechanism import and claim overread."
        ),
        "local_anchor_checks": anchor_checks,
        "candidate_evaluations": evaluations,
        "admitted_candidate_ids": admitted,
        "hostile_violations": hostile_violations,
        "overall_verdict": {
            "verdict": VERDICT,
            "gate_passed": gate_passed,
            "positive_calibration_packet_admitted": positive_admitted,
            "hostile_controls_blocked": not hostile_violations,
            "claim_ledger_update": "none",
            "north_star_update": "none",
            "roadmap_update": "none",
            "public_posture_update": "none",
            "physics_claim_earned": False,
            "observer_theory_or_rg_equivalence_earned": False,
            "reading": (
                "The RG-flow analogy clears only as a calibration scaffold: "
                "T24 supplies field-valued D1 as the transported structure, "
                "T38 supplies finite H1+ transport as the transport-law "
                "analogue, and the conformal/fixed-point neighbor is usable "
                "only as a no-intrinsic-scale endpoint that requires a "
                "declared scale-label operation before record-clock structure "
                "appears. Coupling flow, Lagrangian/action import, conformal "
                "phenomenology, and record-finality-from-RG overreads stay "
                "blocked."
            ),
        },
        "future_packet_minimum": [
            "declare the TaF transported structure, not just the word multiscale",
            "declare the TaF transport law separately from RG beta functions",
            "state whether the fixed-point analogue carries no intrinsic scale",
            "declare the scale-label or symmetry-breaking operation before using clocks or durations",
            "keep external RG and conformal-gravity sources at analogy-ledger grade until primary sources are checked",
            "block coupling-flow, action-functional, phenomenology, physics-claim, and public-posture overreads",
        ],
        "not_earned": [
            "D1 promotion",
            "field-valued D1 canon update",
            "RG/TaF equivalence theorem",
            "scale-genesis theorem",
            "physics or conformal-gravity claim",
            "claim-ledger movement",
            "roadmap movement",
            "North Star movement",
            "public-posture movement",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Render T479 results as Markdown."""

    verdict = result["overall_verdict"]
    anchor = result["local_anchor_checks"]
    anchor_rows = [
        f"| {key} | {value} |"
        for key, value in anchor.items()
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
            "# T479 - RG-Flow Multiscale Calibration Gate - v0.1 results",
            "",
            "> Analogy-ledger calibration gate only. No claim status, roadmap, "
            "README, North Star, public-posture, hard-policy, physics, or "
            "cross-repo movement.",
            "",
            "- Spec: `tests/T479-rg-flow-multiscale-calibration-gate.md`",
            "- Model: `models/rg_flow_multiscale_calibration_gate.py`",
            "- Tests: `tests/test_rg_flow_multiscale_calibration_gate.py`",
            "- Artifact JSON: `results/T479-rg-flow-multiscale-calibration-gate-v0.1.json`",
            "- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`",
            "- Local anchors: T24 and T38",
            "- Literature neighbor: `literature/N15-conformal-gravity-scale-genesis-calibration.md`",
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


def _anchor_checks(t24: dict[str, Any], t38: dict[str, Any]) -> dict[str, Any]:
    return {
        "t24_vector_d1_required_for_multiscale_snapshots": (
            t24["verdict"]["vector_d1_required_for_multiscale_snapshots"]
        ),
        "t24_field_d1_required_for_transport_and_gluing_claims": (
            t24["verdict"]["field_d1_required_for_transport_and_gluing_claims"]
        ),
        "t24_scalar_recoverable_only_as_special_case": (
            t24["verdict"]["scalar_d1_recoverable_as_special_case"]
        ),
        "t38_h1_plus_is_best_supported": (
            t38["best_supported_hypothesis"] == "H1_extended"
        ),
        "t38_compression_record_present": (
            "CompressionRecord" in t38["new_objects_required"]
        ),
        "t38_emergence_record_present": (
            "EmergenceRecord" in t38["new_objects_required"]
        ),
        "t38_h2_required": t38["h2_required"],
        "t38_h3_required": t38["h3_required"],
    }


def _evaluate_candidate(
    candidate: CalibrationCandidate,
    anchor_checks: dict[str, Any],
) -> dict[str, Any]:
    blockers: list[str] = []

    if not candidate.transported_structure:
        blockers.append("transported_structure_not_named")
    if not candidate.transport_law:
        blockers.append("transport_law_not_named")
    if not candidate.fixed_point_analogue:
        blockers.append("fixed_point_analogue_not_named")
    if candidate.local_taf_anchor.startswith("external") or "N15 pointer only" in candidate.local_taf_anchor:
        blockers.append("no_local_taf_transport_anchor")
    if candidate.imports_coupling_flow_as_record_flow:
        blockers.append("coupling_flow_imported_as_record_flow")
    if candidate.imports_lagrangian_action:
        blockers.append("lagrangian_action_imported_onto_records")
    if candidate.fixed_point_has_intrinsic_scale_or_clock:
        blockers.append("fixed_point_carries_intrinsic_scale_or_clock")
    if candidate.derives_record_finality_from_rg:
        blockers.append("record_finality_derived_from_rg_overread")
    if candidate.uses_conformal_phenomenology_as_support:
        blockers.append("conformal_phenomenology_used_as_support")
    if candidate.claims_physics_or_public_posture:
        blockers.append("physics_or_public_posture_overread")
    if not anchor_checks["t24_field_d1_required_for_transport_and_gluing_claims"]:
        blockers.append("t24_field_anchor_missing")
    if not anchor_checks["t38_h1_plus_is_best_supported"]:
        blockers.append("t38_transport_anchor_missing")

    admitted = not blockers and candidate.role == "positive_control"
    route_label = (
        "ANALOGY_CALIBRATION_ADMITTED_NO_PROMOTION"
        if admitted
        else "ANALOGY_CALIBRATION_BLOCKED"
    )

    return {
        "candidate_id": candidate.candidate_id,
        "role": candidate.role,
        "transported_structure": candidate.transported_structure,
        "transport_law": candidate.transport_law,
        "fixed_point_analogue": candidate.fixed_point_analogue,
        "local_taf_anchor": candidate.local_taf_anchor,
        "external_anchor_grade": candidate.external_anchor_grade,
        "admitted": admitted,
        "decision": "admit_as_analogy_calibration" if admitted else "reject_or_block",
        "route_label": route_label,
        "blockers": blockers,
    }


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
