"""T480: scale-label operation gate.

This module turns the T479 follow-up burden into an executable gate. It checks
whether a packet has declared a TaF-native scale-label operation before using
clock, duration, or scale-genesis language.

The admitted positive control is bookkeeping only: it labels scale indices for
field-valued D1 / H1+ transport review. It does not create record clocks,
durations, scale genesis, or physics support.
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
from models.rg_flow_multiscale_calibration_gate import run as run_t479


ARTIFACT_ID = "T480-scale-label-operation-gate-v0.1"
VERDICT = "SCALE_LABEL_OPERATION_GATE_BUILT_BOOKKEEPING_ONLY_NO_CLOCK_PROMOTION"


@dataclass(frozen=True)
class ScaleLabelCandidate:
    """One proposed post-T479 scale-label packet."""

    candidate_id: str
    role: str
    transported_structure: str
    transport_law: str
    scale_label_operation: str
    admitted_reading: str
    local_taf_anchor: str
    imports_rg_scale_as_record_clock: bool = False
    fixed_point_generates_intrinsic_clock: bool = False
    label_only_without_operation: bool = False
    uses_hidden_calendar_or_time_order: bool = False
    derives_duration_or_arrow_from_scale_label: bool = False
    changes_record_finality_by_label: bool = False
    uses_conformal_phenomenology_as_support: bool = False
    claims_scale_genesis_or_physics: bool = False


def scale_label_candidates() -> tuple[ScaleLabelCandidate, ...]:
    """Return the finite T480 candidate catalogue."""

    return (
        ScaleLabelCandidate(
            candidate_id="declared_scale_section_bookkeeping",
            role="positive_control",
            transported_structure=(
                "field-valued D1 profile over observer, trust, time, and "
                "scale sites"
            ),
            transport_law=(
                "T38 H1+ typed transport with compression and emergence "
                "records retained separately"
            ),
            scale_label_operation=(
                "attach an external finite scale label sigma in {micro, "
                "meso, macro} to each ObserverSite and allow only declared "
                "transport-edge comparisons between labeled sites"
            ),
            admitted_reading=(
                "scale-index bookkeeping for future review; no clock, "
                "duration, scale genesis, or finality promotion"
            ),
            local_taf_anchor="T24 field-valued D1 plus T38 H1+ plus T479 guard",
        ),
        ScaleLabelCandidate(
            candidate_id="fixed_point_intrinsic_clock",
            role="hostile_control",
            transported_structure="field-valued D1 profile",
            transport_law="finite scale transport",
            scale_label_operation="fixed point emits an intrinsic record clock",
            admitted_reading="clock appears at the fixed point",
            local_taf_anchor="T479 overread",
            fixed_point_generates_intrinsic_clock=True,
        ),
        ScaleLabelCandidate(
            candidate_id="rg_scale_parameter_as_clock",
            role="hostile_control",
            transported_structure="RG effective couplings",
            transport_law="beta function",
            scale_label_operation="identify RG scale mu with record-clock time",
            admitted_reading="RG scale becomes TaF duration",
            local_taf_anchor="external RG mechanism import",
            imports_rg_scale_as_record_clock=True,
        ),
        ScaleLabelCandidate(
            candidate_id="label_only_no_operation",
            role="hostile_control",
            transported_structure="field-valued D1 profile",
            transport_law="T38 H1+ typed transport",
            scale_label_operation="",
            admitted_reading="uses the word scale without an operation",
            local_taf_anchor="T24/T38 named but T479 burden unpaid",
            label_only_without_operation=True,
        ),
        ScaleLabelCandidate(
            candidate_id="hidden_calendar_breaking",
            role="hostile_control",
            transported_structure="field-valued D1 profile",
            transport_law="T38 H1+ typed transport",
            scale_label_operation=(
                "assign scale labels by an undeclared calendar order hidden "
                "from the packet"
            ),
            admitted_reading="clock order smuggled through labels",
            local_taf_anchor="T24/T38 named but hidden time source",
            uses_hidden_calendar_or_time_order=True,
        ),
        ScaleLabelCandidate(
            candidate_id="duration_from_scale_order",
            role="hostile_control",
            transported_structure="field-valued D1 profile",
            transport_law="T38 H1+ typed transport",
            scale_label_operation="order the labels micro < meso < macro",
            admitted_reading="ordered labels define duration and arrow",
            local_taf_anchor="T24/T38 named but clock overread",
            derives_duration_or_arrow_from_scale_label=True,
        ),
        ScaleLabelCandidate(
            candidate_id="record_finality_by_relabel",
            role="hostile_control",
            transported_structure="field-valued D1 profile",
            transport_law="T38 H1+ typed transport",
            scale_label_operation="rename a site macro and mark it final",
            admitted_reading="label change changes record finality status",
            local_taf_anchor="T24/T38 named but finality overread",
            changes_record_finality_by_label=True,
        ),
        ScaleLabelCandidate(
            candidate_id="conformal_phenomenology_support",
            role="hostile_control",
            transported_structure="record/finality structure",
            transport_law="finite scale transport",
            scale_label_operation="use conformal-gravity phenomenology as support",
            admitted_reading="phenomenology supports TaF scale genesis",
            local_taf_anchor="N15 pointer overread",
            uses_conformal_phenomenology_as_support=True,
            claims_scale_genesis_or_physics=True,
        ),
        ScaleLabelCandidate(
            candidate_id="scale_genesis_claim_promotion",
            role="hostile_control",
            transported_structure="field-valued D1 profile",
            transport_law="T38 H1+ typed transport",
            scale_label_operation="declare a scale label",
            admitted_reading="scale genesis theorem and physics posture earned",
            local_taf_anchor="T24/T38/T479 promotion shortcut",
            claims_scale_genesis_or_physics=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T480 scale-label operation gate."""

    anchor_checks = _anchor_checks()
    evaluations = [
        _evaluate_candidate(candidate, anchor_checks)
        for candidate in scale_label_candidates()
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
    positive_admitted = admitted == ["declared_scale_section_bookkeeping"]
    gate_passed = (
        anchor_checks["t479_scale_label_burden_declared"]
        and anchor_checks["t24_field_d1_required_for_transport_and_gluing_claims"]
        and anchor_checks["t38_h1_plus_is_best_supported"]
        and positive_admitted
        and not hostile_violations
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Make T479's scale-label operation burden executable: admit only "
            "declared TaF-native scale-index bookkeeping before future "
            "review, while blocking fixed-point clocks, RG-scale imports, "
            "label-only shortcuts, hidden calendar order, duration/arrow "
            "overreads, finality-by-relabeling, phenomenology support, and "
            "claim promotion."
        ),
        "local_anchor_checks": anchor_checks,
        "candidate_evaluations": evaluations,
        "admitted_candidate_ids": admitted,
        "hostile_violations": hostile_violations,
        "overall_verdict": {
            "verdict": VERDICT,
            "gate_passed": gate_passed,
            "positive_bookkeeping_packet_admitted": positive_admitted,
            "hostile_controls_blocked": not hostile_violations,
            "claim_ledger_update": "none",
            "north_star_update": "none",
            "roadmap_update": "none",
            "public_posture_update": "none",
            "physics_claim_earned": False,
            "scale_genesis_theorem_earned": False,
            "record_clock_or_duration_earned": False,
            "reading": (
                "T480 admits a single declared scale-label operation only as "
                "bookkeeping over T24 field-valued D1 and T38 H1+ transport. "
                "The operation may label sites for future review, but it does "
                "not create clocks, durations, record finality, scale genesis, "
                "or physics support. Fixed-point clock language, RG-scale "
                "imports, label-only packets, hidden calendar order, duration "
                "or arrow extraction, finality-by-relabeling, conformal "
                "phenomenology, and promotion shortcuts stay blocked."
            ),
        },
        "future_packet_minimum": [
            "declare the scale-label operation as an operation, not a label word",
            "keep transported structure and transport law separate from the scale label",
            "state whether the label is external bookkeeping or earned internal structure",
            "state what observers and transport edges can compare after labeling",
            "block clocks, durations, temporal arrows, and finality changes unless separately earned",
            "keep RG and conformal-gravity sources at analogy-ledger grade",
        ],
        "not_earned": [
            "record clock",
            "duration or temporal arrow",
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
    """Render T480 results as Markdown."""

    verdict = result["overall_verdict"]
    anchor_rows = [
        f"| {key} | {value} |"
        for key, value in result["local_anchor_checks"].items()
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
            "# T480 - Scale-Label Operation Gate - v0.1 results",
            "",
            "> Bookkeeping gate only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, physics, scale-genesis, "
            "or cross-repo movement.",
            "",
            "- Spec: `tests/T480-scale-label-operation-gate.md`",
            "- Model: `models/scale_label_operation_gate.py`",
            "- Tests: `tests/test_scale_label_operation_gate.py`",
            "- Artifact JSON: `results/T480-scale-label-operation-gate-v0.1.json`",
            "- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`",
            "- Local anchors: T24, T38, and T479",
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


def _anchor_checks() -> dict[str, Any]:
    t24 = run_t24_analysis()
    t38 = t38_result_to_dict(run_t38_analysis())
    t479 = run_t479()

    return {
        "t479_gate_passed": t479["overall_verdict"]["gate_passed"],
        "t479_scale_label_burden_declared": (
            "declare the scale-label or symmetry-breaking operation before using clocks or durations"
            in t479["future_packet_minimum"]
        ),
        "t479_no_record_clock_earned": (
            t479["overall_verdict"]["physics_claim_earned"] is False
            and "scale-genesis theorem" in t479["not_earned"]
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
        "t38_compression_and_emergence_records_present": (
            "CompressionRecord" in t38["new_objects_required"]
            and "EmergenceRecord" in t38["new_objects_required"]
        ),
    }


def _evaluate_candidate(
    candidate: ScaleLabelCandidate,
    anchor_checks: dict[str, Any],
) -> dict[str, Any]:
    blockers: list[str] = []

    if not candidate.transported_structure:
        blockers.append("transported_structure_not_named")
    if not candidate.transport_law:
        blockers.append("transport_law_not_named")
    if not candidate.scale_label_operation:
        blockers.append("scale_label_operation_not_declared")
    if candidate.label_only_without_operation:
        blockers.append("label_word_without_operation")
    if candidate.local_taf_anchor.startswith("external"):
        blockers.append("no_local_taf_anchor")
    if "N15 pointer" in candidate.local_taf_anchor:
        blockers.append("no_local_taf_transport_anchor")
    if candidate.imports_rg_scale_as_record_clock:
        blockers.append("rg_scale_imported_as_record_clock")
    if candidate.fixed_point_generates_intrinsic_clock:
        blockers.append("fixed_point_generates_intrinsic_clock")
    if candidate.uses_hidden_calendar_or_time_order:
        blockers.append("hidden_calendar_or_time_order")
    if candidate.derives_duration_or_arrow_from_scale_label:
        blockers.append("duration_or_arrow_derived_from_scale_label")
    if candidate.changes_record_finality_by_label:
        blockers.append("record_finality_changed_by_label")
    if candidate.uses_conformal_phenomenology_as_support:
        blockers.append("conformal_phenomenology_used_as_support")
    if candidate.claims_scale_genesis_or_physics:
        blockers.append("scale_genesis_or_physics_claim_overread")
    if not anchor_checks["t479_scale_label_burden_declared"]:
        blockers.append("t479_scale_label_burden_missing")
    if not anchor_checks["t24_field_d1_required_for_transport_and_gluing_claims"]:
        blockers.append("t24_field_anchor_missing")
    if not anchor_checks["t38_h1_plus_is_best_supported"]:
        blockers.append("t38_transport_anchor_missing")

    admitted = not blockers and candidate.role == "positive_control"
    route_label = (
        "SCALE_LABEL_BOOKKEEPING_ADMITTED_NO_CLOCK_PROMOTION"
        if admitted
        else "SCALE_LABEL_PACKET_BLOCKED"
    )

    return {
        "candidate_id": candidate.candidate_id,
        "role": candidate.role,
        "transported_structure": candidate.transported_structure,
        "transport_law": candidate.transport_law,
        "scale_label_operation": candidate.scale_label_operation,
        "admitted_reading": candidate.admitted_reading,
        "local_taf_anchor": candidate.local_taf_anchor,
        "admitted": admitted,
        "decision": "admit_as_bookkeeping" if admitted else "reject_or_block",
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
