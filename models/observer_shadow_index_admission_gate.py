"""T472: observer-shadow index admission gate.

T470 showed that a shared observer-shadow schema is possible only when
load-bearing indices are declared before morphism comparison. This module turns
that follow-up burden into an executable admission gate over the same finite
transport and LossKernel fixtures.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models.observer_shadow_composition_gate import (
    ShadowAuditObject,
    ShadowMorphismCheck,
    run_t470_analysis,
)


ARTIFACT_ID = "T472-observer-shadow-index-admission-gate-v0.1"
VERDICT = "OBSERVER_SHADOW_INDEX_GATE_BUILT_COMPLETION_SEPARATED_NO_PROMOTION"


@dataclass(frozen=True)
class IndexPacket:
    """A proposed observer-shadow packet presented to the index gate."""

    packet_id: str
    check_id: str
    declared_indices: tuple[str, ...]
    required_indices: tuple[str, ...]
    completion_kind: str
    expected_route: str
    intended_use: str


@dataclass(frozen=True)
class IndexAdmission:
    """Gate decision for one proposed observer-shadow packet."""

    packet_id: str
    check_id: str
    admitted: bool
    route_label: str
    missing_indices: tuple[str, ...]
    classification: str
    same_shadow: bool
    capability_equivalent: bool
    protection_preserved: bool
    completion_kind: str
    counts_as_preservation_control: bool
    notes: tuple[str, ...]


@dataclass(frozen=True)
class T472Result:
    """Complete T472 gate result."""

    packets: tuple[IndexPacket, ...]
    admissions: tuple[IndexAdmission, ...]
    verdict: str
    claim_ledger_update: str
    admitted_preservation_controls: tuple[str, ...]
    admitted_indexed_completions: tuple[str, ...]
    absorber_completions: tuple[str, ...]
    rejected_packets: tuple[str, ...]
    global_category_theorem_supported: bool
    strongest_reading: str
    future_packet_minimum: tuple[str, ...]
    not_earned: tuple[str, ...]


def run_t472_analysis() -> T472Result:
    """Run the T472 observer-shadow index admission gate."""

    t470 = run_t470_analysis()
    checks = {check.check_id: check for check in t470.checks}
    objects = {obj.object_id: obj for obj in t470.objects}
    packets = _candidate_packets(checks, objects)
    admissions = tuple(
        _evaluate_packet(packet, checks[packet.check_id]) for packet in packets
    )

    admitted_preservation_controls = tuple(
        admission.packet_id
        for admission in admissions
        if admission.route_label == "admitted_preservation_control"
    )
    admitted_indexed_completions = tuple(
        admission.packet_id
        for admission in admissions
        if admission.route_label == "admitted_indexed_completion"
    )
    absorber_completions = tuple(
        admission.packet_id
        for admission in admissions
        if admission.route_label == "absorber_completion_recorded"
    )
    rejected_packets = tuple(
        admission.packet_id for admission in admissions if not admission.admitted
    )

    return T472Result(
        packets=packets,
        admissions=admissions,
        verdict=VERDICT,
        claim_ledger_update="none",
        admitted_preservation_controls=admitted_preservation_controls,
        admitted_indexed_completions=admitted_indexed_completions,
        absorber_completions=absorber_completions,
        rejected_packets=rejected_packets,
        global_category_theorem_supported=False,
        strongest_reading=(
            "T472 makes T470's index burden executable: endpoint-only transport "
            "and hidden-source omission fail admission, path-indexed transport "
            "is admitted only as indexed bookkeeping, LossKernel neighbor "
            "factoring is the genuine preservation control, and hidden-source "
            "completion is recorded as absorber/state-completion bookkeeping. "
            "This supports an index-admission guardrail, not a global "
            "observer-shadow category theorem."
        ),
        future_packet_minimum=(
            "declare all load-bearing indices before morphism comparison",
            "include one genuine preservation control with same shadow and same capability",
            "include one omitted-index hostile control that fails the gate",
            "separate indexed bookkeeping completion from absorber state completion",
            "block category, fibration, or theorem language until preservation survives beyond finite controls",
        ),
        not_earned=(
            "observer-shadow category theorem",
            "indexed category or fibration theorem",
            "North Star geometry proof",
            "D1, PO1, TF1, or LossKernel promotion",
            "physics or consciousness claim",
            "claim-ledger movement",
            "public-posture movement",
        ),
    )


def _candidate_packets(
    checks: dict[str, ShadowMorphismCheck],
    objects: dict[str, ShadowAuditObject],
) -> tuple[IndexPacket, ...]:
    return (
        _packet_from_check(
            "transport_endpoint_only_packet",
            checks["transport_endpoint_only_collapse"],
            objects,
            required_indices=("endpoint", "path_label", "accumulated_forgotten_structure"),
            completion_kind="none",
            expected_route="reject_missing_load_bearing_indices",
            intended_use="collapse transport paths to endpoint-only observer shadow",
        ),
        _packet_from_check(
            "transport_path_indexed_packet",
            checks["transport_path_indexed_completion"],
            objects,
            required_indices=("endpoint", "path_label", "accumulated_forgotten_structure"),
            completion_kind="indexed_bookkeeping",
            expected_route="admitted_indexed_completion",
            intended_use="compare transport paths only after path and accumulated-loss indices are declared",
        ),
        _packet_from_check(
            "losskernel_neighbor_preservation_packet",
            checks["losskernel_neighbor_factoring_preserves"],
            objects,
            required_indices=("neighbor_signature",),
            completion_kind="none",
            expected_route="admitted_preservation_control",
            intended_use="preserve the T220 canonical obligation under same neighbor-visible signature",
        ),
        _packet_from_check(
            "losskernel_hidden_source_omitted_packet",
            checks["losskernel_hidden_source_omitted"],
            objects,
            required_indices=("neighbor_signature", "hidden_source_datum"),
            completion_kind="none",
            expected_route="reject_missing_load_bearing_indices",
            intended_use="omit source datum while using a capability object that reads it",
        ),
        _packet_from_check(
            "losskernel_hidden_source_completed_packet",
            checks["losskernel_hidden_source_completed"],
            objects,
            required_indices=("neighbor_signature", "hidden_source_datum"),
            completion_kind="absorber_state_completion",
            expected_route="absorber_completion_recorded",
            intended_use="record that hidden-source completion repairs the bookkeeping by ordinary state completion",
        ),
    )


def _packet_from_check(
    packet_id: str,
    check: ShadowMorphismCheck,
    objects: dict[str, ShadowAuditObject],
    *,
    required_indices: tuple[str, ...],
    completion_kind: str,
    expected_route: str,
    intended_use: str,
) -> IndexPacket:
    source = objects[check.source_object_id]
    target = objects[check.target_object_id]
    declared_indices = tuple(sorted(set(source.declared_indices + target.declared_indices)))
    return IndexPacket(
        packet_id=packet_id,
        check_id=check.check_id,
        declared_indices=declared_indices,
        required_indices=required_indices,
        completion_kind=completion_kind,
        expected_route=expected_route,
        intended_use=intended_use,
    )


def _evaluate_packet(
    packet: IndexPacket,
    check: ShadowMorphismCheck,
) -> IndexAdmission:
    missing = tuple(
        index for index in packet.required_indices if index not in packet.declared_indices
    )
    notes: list[str] = []

    if missing:
        route = "reject_missing_load_bearing_indices"
        admitted = False
        notes.append("packet omits indices required by the T470 obstruction")
    elif check.classification == "state_completion_required":
        route = "reject_state_completion_required"
        admitted = False
        notes.append("capability reads state outside the declared shadow")
    elif packet.completion_kind == "absorber_state_completion":
        route = "absorber_completion_recorded"
        admitted = True
        notes.append("completion repairs bookkeeping only by ordinary state completion")
    elif check.same_shadow and check.capability_equivalent and check.protection_preserved:
        route = "admitted_preservation_control"
        admitted = True
        notes.append("same declared shadow preserves the native capability value")
    elif not check.same_shadow and check.protection_preserved:
        route = "admitted_indexed_completion"
        admitted = True
        notes.append("declared indices separate the shadows before comparison")
    else:
        route = "reject_unrepaired_nonpreservation"
        admitted = False
        notes.append("same declared shadow still fails capability preservation")

    return IndexAdmission(
        packet_id=packet.packet_id,
        check_id=packet.check_id,
        admitted=admitted,
        route_label=route,
        missing_indices=missing,
        classification=check.classification,
        same_shadow=check.same_shadow,
        capability_equivalent=check.capability_equivalent,
        protection_preserved=check.protection_preserved,
        completion_kind=packet.completion_kind,
        counts_as_preservation_control=route == "admitted_preservation_control",
        notes=tuple(notes),
    )


def t472_result_to_dict(result: T472Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "packets": [_packet_to_dict(packet) for packet in result.packets],
        "admissions": [_admission_to_dict(admission) for admission in result.admissions],
        "claim_ledger_update": result.claim_ledger_update,
        "admitted_preservation_controls": list(result.admitted_preservation_controls),
        "admitted_indexed_completions": list(result.admitted_indexed_completions),
        "absorber_completions": list(result.absorber_completions),
        "rejected_packets": list(result.rejected_packets),
        "global_category_theorem_supported": result.global_category_theorem_supported,
        "strongest_reading": result.strongest_reading,
        "future_packet_minimum": list(result.future_packet_minimum),
        "not_earned": list(result.not_earned),
    }


def render_markdown(result: T472Result) -> str:
    admission_rows = []
    for admission in result.admissions:
        missing = ", ".join(admission.missing_indices) or "none"
        notes = "; ".join(admission.notes) or "none"
        admission_rows.append(
            "| {packet_id} | {admitted} | {route_label} | {classification} | "
            "{missing} | {completion_kind} | {counts} | {notes} |".format(
                packet_id=admission.packet_id,
                admitted=admission.admitted,
                route_label=admission.route_label,
                classification=admission.classification,
                missing=missing,
                completion_kind=admission.completion_kind,
                counts=admission.counts_as_preservation_control,
                notes=notes,
            )
        )

    minimum = [f"- {item}" for item in result.future_packet_minimum]
    not_earned = [f"- {item}" for item in result.not_earned]

    return "\n".join(
        [
            "# T472 - Observer-Shadow Index Admission Gate - v0.1 results",
            "",
            "> Index-admission guardrail only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T472-observer-shadow-index-admission-gate.md`",
            "- Model: `models/observer_shadow_index_admission_gate.py`",
            "- Tests: `tests/test_observer_shadow_index_admission_gate.py`",
            "- Artifact JSON: `results/T472-observer-shadow-index-admission-gate-v0.1.json`",
            "- Source open problem: `open-problems/observer-shadow-category.md`",
            "- Prior gate: T470",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## Packet Decisions",
            "",
            "| packet | admitted? | route | source classification | missing indices | completion kind | counts as preservation control? | notes |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *admission_rows,
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


def _packet_to_dict(packet: IndexPacket) -> dict[str, Any]:
    return {
        "packet_id": packet.packet_id,
        "check_id": packet.check_id,
        "declared_indices": list(packet.declared_indices),
        "required_indices": list(packet.required_indices),
        "completion_kind": packet.completion_kind,
        "expected_route": packet.expected_route,
        "intended_use": packet.intended_use,
    }


def _admission_to_dict(admission: IndexAdmission) -> dict[str, Any]:
    return {
        "packet_id": admission.packet_id,
        "check_id": admission.check_id,
        "admitted": admission.admitted,
        "route_label": admission.route_label,
        "missing_indices": list(admission.missing_indices),
        "classification": admission.classification,
        "same_shadow": admission.same_shadow,
        "capability_equivalent": admission.capability_equivalent,
        "protection_preserved": admission.protection_preserved,
        "completion_kind": admission.completion_kind,
        "counts_as_preservation_control": admission.counts_as_preservation_control,
        "notes": list(admission.notes),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t472_analysis()
    payload = t472_result_to_dict(result)
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
