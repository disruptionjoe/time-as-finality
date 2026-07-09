"""T511: boundary-adapter finality gate.

This module makes the 2026-07-09 boundary-adapter triangle intake executable in
TaF-local terms. It asks whether a boundary-supplied datum becomes final only
when the undo/readout handle is inadmissible under a predeclared operation
class.

The fixture is review machinery only. It does not assert GU/TaF/TI identity,
source-action truth, physical irreversibility, a universal ledger, claim
movement, public-posture movement, or cross-repo truth.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T511-boundary-adapter-finality-gate-v0.1"
VERDICT = "BOUNDARY_ADAPTER_FINALITY_GATE_BUILT_REVIEW_ONLY"
SOURCE_INTAKE = "explorations/boundary-adapter-triangle-intake-2026-07-09.md"
SOURCE_GUARDRAIL = "tests/T510-brst-conserved-ledger-compatibility-gate.md"


@dataclass(frozen=True)
class AdapterPacket:
    packet_id: str
    description: str
    domain_declared: bool
    boundary_adapter_declared: bool
    region_declared: bool
    admissible_operations: tuple[str, ...]
    candidate_record_declared: bool
    undo_handle: str
    readout_handle: str
    handle_inadmissibility_declared: bool
    ledger_declared: bool
    ledger_before: int
    ledger_after: int
    fixed_richer_source_absorber_tested: bool
    positive_control_included: bool
    failure_control_included: bool
    boundary_supplied: bool
    source_crossing_language: bool = False
    requests_claim_movement: bool = False
    requests_public_posture_movement: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth_movement: bool = False


@dataclass(frozen=True)
class AdapterDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    undo_handle_admissible: bool
    readout_handle_admissible: bool
    ledger_conserved: bool
    missing_requirements: tuple[str, ...]
    blocked_shortcuts: tuple[str, ...]
    strongest_allowed_reading: str


def run() -> dict[str, Any]:
    packets = fixture_packets()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    by_id = {decision.packet_id: decision for decision in decisions}

    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": VERDICT,
        "source_intake": SOURCE_INTAKE,
        "source_guardrail": SOURCE_GUARDRAIL,
        "objective": (
            "Make the boundary-adapter triangle intake checkable in TaF-local "
            "terms: a boundary-supplied datum is final only when the relevant "
            "undo/readout handle is inadmissible under a declared operation "
            "class and the ledger is conserved."
        ),
        "packets": [asdict(packet) for packet in packets],
        "decisions": [decision_dict(decision) for decision in decisions],
        "admitted_packet_ids": [
            decision.packet_id for decision in decisions if decision.admitted
        ],
        "rejected_packet_ids": [
            decision.packet_id for decision in decisions if not decision.admitted
        ],
        "overall": {
            "admitted_count": sum(1 for decision in decisions if decision.admitted),
            "rejected_count": sum(1 for decision in decisions if not decision.admitted),
            "positive_review_target_admitted": by_id[
                "inadmissible_handle_conserved_ledger"
            ].admitted,
            "admissible_handle_rejected": by_id[
                "admissible_undo_handle_control"
            ].label
            == "REJECTED_HANDLE_ADMISSIBLE_NOT_FINAL",
            "absent_handle_rejected": by_id[
                "absent_handle_prose_shortcut"
            ].label
            == "REJECTED_HANDLE_ABSENT_NOT_INADMISSIBLE",
            "drifting_ledger_rejected": by_id[
                "ledger_drift_control"
            ].label
            == "REJECTED_LEDGER_DRIFT",
            "fixed_source_absorber_required": by_id[
                "fixed_source_absorber_missing"
            ].label
            == "REJECTED_FIXED_SOURCE_ABSORBER_UNTESTED",
            "boundary_supply_only_rejected": by_id[
                "boundary_supply_only"
            ].label
            == "REJECTED_BOUNDARY_SUPPLY_NOT_FINALITY",
            "source_crossing_only_rejected": by_id[
                "source_crossing_language_only"
            ].label
            == "REJECTED_SOURCE_CROSSING_NOT_TAF_FINALITY",
            "claim_movement": False,
            "roadmap_movement": False,
            "readme_movement": False,
            "north_star_movement": False,
            "public_posture_movement": False,
            "hard_policy_movement": False,
            "protected_license_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
            "sibling_repo_inspection": False,
            "physics_claim_earned": False,
            "gu_support_earned": False,
            "temporal_issuance_support_earned": False,
            "universal_ledger_claimed": False,
        },
        "future_packet_minimum": future_packet_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T511 admits one synthetic TaF-local review target: boundary supply "
            "plus a conserved ledger plus an explicitly inadmissible undo/readout "
            "handle. It rejects admissible-handle, absent-handle, drifting-ledger, "
            "untested fixed-source, boundary-supply-only, source-crossing-only, "
            "and cross-repo shortcut packets. The result is an adapter-finality "
            "gate, not a cross-repo identity result."
        ),
    }


def fixture_packets() -> tuple[AdapterPacket, ...]:
    return (
        AdapterPacket(
            packet_id="inadmissible_handle_conserved_ledger",
            description=(
                "A boundary adapter supplies a record whose undo/readout handles "
                "are outside the declared operation class, while the ledger is "
                "conserved by the adapter dynamics."
            ),
            domain_declared=True,
            boundary_adapter_declared=True,
            region_declared=True,
            admissible_operations=("commit_record", "audit_ledger"),
            candidate_record_declared=True,
            undo_handle="reverse_record",
            readout_handle="read_hidden_boundary",
            handle_inadmissibility_declared=True,
            ledger_declared=True,
            ledger_before=1,
            ledger_after=1,
            fixed_richer_source_absorber_tested=True,
            positive_control_included=True,
            failure_control_included=True,
            boundary_supplied=True,
        ),
        AdapterPacket(
            packet_id="admissible_undo_handle_control",
            description="The undo handle is in the admissible operation class.",
            domain_declared=True,
            boundary_adapter_declared=True,
            region_declared=True,
            admissible_operations=("commit_record", "audit_ledger", "reverse_record"),
            candidate_record_declared=True,
            undo_handle="reverse_record",
            readout_handle="read_hidden_boundary",
            handle_inadmissibility_declared=True,
            ledger_declared=True,
            ledger_before=1,
            ledger_after=1,
            fixed_richer_source_absorber_tested=True,
            positive_control_included=True,
            failure_control_included=True,
            boundary_supplied=True,
        ),
        AdapterPacket(
            packet_id="absent_handle_prose_shortcut",
            description=(
                "The packet never proves inadmissibility; it merely omits the "
                "undo/readout handle from the prose."
            ),
            domain_declared=True,
            boundary_adapter_declared=True,
            region_declared=True,
            admissible_operations=("commit_record", "audit_ledger"),
            candidate_record_declared=True,
            undo_handle="reverse_record",
            readout_handle="read_hidden_boundary",
            handle_inadmissibility_declared=False,
            ledger_declared=True,
            ledger_before=1,
            ledger_after=1,
            fixed_richer_source_absorber_tested=True,
            positive_control_included=True,
            failure_control_included=True,
            boundary_supplied=True,
        ),
        AdapterPacket(
            packet_id="ledger_drift_control",
            description="The handle is inadmissible, but the ledger drifts.",
            domain_declared=True,
            boundary_adapter_declared=True,
            region_declared=True,
            admissible_operations=("commit_record", "audit_ledger"),
            candidate_record_declared=True,
            undo_handle="reverse_record",
            readout_handle="read_hidden_boundary",
            handle_inadmissibility_declared=True,
            ledger_declared=True,
            ledger_before=1,
            ledger_after=0,
            fixed_richer_source_absorber_tested=True,
            positive_control_included=True,
            failure_control_included=True,
            boundary_supplied=True,
        ),
        AdapterPacket(
            packet_id="fixed_source_absorber_missing",
            description=(
                "The packet gives a boundary/finality story without checking "
                "fixed-richer-source disclosure."
            ),
            domain_declared=True,
            boundary_adapter_declared=True,
            region_declared=True,
            admissible_operations=("commit_record", "audit_ledger"),
            candidate_record_declared=True,
            undo_handle="reverse_record",
            readout_handle="read_hidden_boundary",
            handle_inadmissibility_declared=True,
            ledger_declared=True,
            ledger_before=1,
            ledger_after=1,
            fixed_richer_source_absorber_tested=False,
            positive_control_included=True,
            failure_control_included=True,
            boundary_supplied=True,
        ),
        AdapterPacket(
            packet_id="boundary_supply_only",
            description="Boundary supply is present but no TaF finality handle is typed.",
            domain_declared=True,
            boundary_adapter_declared=True,
            region_declared=True,
            admissible_operations=("commit_record", "audit_ledger"),
            candidate_record_declared=True,
            undo_handle="",
            readout_handle="",
            handle_inadmissibility_declared=False,
            ledger_declared=True,
            ledger_before=1,
            ledger_after=1,
            fixed_richer_source_absorber_tested=True,
            positive_control_included=True,
            failure_control_included=True,
            boundary_supplied=True,
        ),
        AdapterPacket(
            packet_id="source_crossing_language_only",
            description=(
                "Source-crossing language is supplied, but no TaF ledger or "
                "inadmissible handle is declared."
            ),
            domain_declared=True,
            boundary_adapter_declared=True,
            region_declared=True,
            admissible_operations=("commit_record", "audit_ledger"),
            candidate_record_declared=True,
            undo_handle="",
            readout_handle="",
            handle_inadmissibility_declared=False,
            ledger_declared=False,
            ledger_before=1,
            ledger_after=1,
            fixed_richer_source_absorber_tested=True,
            positive_control_included=True,
            failure_control_included=True,
            boundary_supplied=True,
            source_crossing_language=True,
        ),
        AdapterPacket(
            packet_id="cross_repo_identity_shortcut",
            description=(
                "The packet attempts to convert the local adapter gate into "
                "GU/TaF/TI identity or support."
            ),
            domain_declared=True,
            boundary_adapter_declared=True,
            region_declared=True,
            admissible_operations=("commit_record", "audit_ledger"),
            candidate_record_declared=True,
            undo_handle="reverse_record",
            readout_handle="read_hidden_boundary",
            handle_inadmissibility_declared=True,
            ledger_declared=True,
            ledger_before=1,
            ledger_after=1,
            fixed_richer_source_absorber_tested=True,
            positive_control_included=True,
            failure_control_included=True,
            boundary_supplied=True,
            source_crossing_language=True,
            requests_claim_movement=True,
            requests_cross_repo_truth_movement=True,
        ),
    )


def evaluate_packet(packet: AdapterPacket) -> AdapterDecision:
    blocked = blocked_shortcuts(packet)
    undo_admissible = bool(packet.undo_handle) and (
        packet.undo_handle in packet.admissible_operations
    )
    readout_admissible = bool(packet.readout_handle) and (
        packet.readout_handle in packet.admissible_operations
    )
    ledger_conserved = packet.ledger_before == packet.ledger_after
    missing = missing_requirements(packet)

    if blocked:
        return decision(
            packet,
            admitted=False,
            label="BLOCKED_CROSS_REPO_OR_GOVERNANCE_SHORTCUT",
            action="stop",
            missing=missing,
            blocked=blocked,
            strongest=(
                "A TaF adapter gate cannot move claims, public posture, external "
                "publication, or cross-repo identity/support."
            ),
        )
    if packet.source_crossing_language and not packet.ledger_declared:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_SOURCE_CROSSING_NOT_TAF_FINALITY",
            action="reject",
            missing=missing,
            blocked=(),
            strongest=(
                "Source-crossing language is not TaF finality unless the TaF "
                "ledger and inadmissible finality handle are typed."
            ),
        )
    if packet.boundary_supplied and (not packet.undo_handle and not packet.readout_handle):
        return decision(
            packet,
            admitted=False,
            label="REJECTED_BOUNDARY_SUPPLY_NOT_FINALITY",
            action="reject",
            missing=missing,
            blocked=(),
            strongest=(
                "Boundary supply alone is not finality; the operation/readout "
                "handle must be declared and shown inadmissible."
            ),
        )
    if not packet.handle_inadmissibility_declared:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_HANDLE_ABSENT_NOT_INADMISSIBLE",
            action="reject",
            missing=missing + ("handle inadmissibility proof",),
            blocked=(),
            strongest=(
                "A missing or unmentioned handle is not the same as an "
                "inadmissible handle under a declared operation class."
            ),
        )
    if undo_admissible or readout_admissible:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_HANDLE_ADMISSIBLE_NOT_FINAL",
            action="reject",
            missing=missing,
            blocked=(),
            strongest=(
                "The candidate is not final for the declared observer boundary "
                "because an undo/readout handle is admissible."
            ),
        )
    if not ledger_conserved:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_LEDGER_DRIFT",
            action="reject",
            missing=missing + ("conserved ledger or invariant",),
            blocked=(),
            strongest=(
                "An inadmissible handle does not admit a finality review target "
                "when the candidate ledger drifts."
            ),
        )
    if not packet.fixed_richer_source_absorber_tested:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_FIXED_SOURCE_ABSORBER_UNTESTED",
            action="reject",
            missing=missing + ("fixed-richer-source absorber",),
            blocked=(),
            strongest=(
                "The packet must test fixed-richer-source disclosure before "
                "treating boundary-adapter finality as review material."
            ),
        )
    if missing:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_INCOMPLETE_ADAPTER_FINALITY_PACKET",
            action="reject",
            missing=missing,
            blocked=(),
            strongest="The packet has not paid the T511 adapter-finality minimum.",
        )

    return decision(
        packet,
        admitted=True,
        label="ADMITTED_ADAPTER_FINALITY_REVIEW_TARGET",
        action="review_only",
        missing=(),
        blocked=(),
        strongest=(
            "A TaF-local review target exists when boundary supply, a conserved "
            "ledger, and explicit operation-class inadmissibility for the "
            "undo/readout handle are all predeclared. This does not establish a "
            "real cross-repo adapter."
        ),
    )


def missing_requirements(packet: AdapterPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.domain_declared:
        missing.append("domain")
    if not packet.boundary_adapter_declared:
        missing.append("boundary adapter B")
    if not packet.region_declared:
        missing.append("region / observer boundary")
    if not packet.admissible_operations:
        missing.append("admissible operations")
    if not packet.candidate_record_declared:
        missing.append("candidate record")
    if not packet.undo_handle and not packet.readout_handle:
        missing.append("undo or readout handle")
    if not packet.ledger_declared:
        missing.append("ledger or invariant")
    if not packet.positive_control_included:
        missing.append("positive control")
    if not packet.failure_control_included:
        missing.append("failure control")
    return tuple(missing)


def blocked_shortcuts(packet: AdapterPacket) -> tuple[str, ...]:
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


def decision(
    packet: AdapterPacket,
    admitted: bool,
    label: str,
    action: str,
    missing: tuple[str, ...],
    blocked: tuple[str, ...],
    strongest: str,
) -> AdapterDecision:
    return AdapterDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        review_target_only=admitted,
        undo_handle_admissible=bool(packet.undo_handle)
        and packet.undo_handle in packet.admissible_operations,
        readout_handle_admissible=bool(packet.readout_handle)
        and packet.readout_handle in packet.admissible_operations,
        ledger_conserved=packet.ledger_before == packet.ledger_after,
        missing_requirements=missing,
        blocked_shortcuts=blocked,
        strongest_allowed_reading=strongest,
    )


def decision_dict(item: AdapterDecision) -> dict[str, Any]:
    return {
        "packet_id": item.packet_id,
        "admitted": item.admitted,
        "label": item.label,
        "action": item.action,
        "review_target_only": item.review_target_only,
        "undo_handle_admissible": item.undo_handle_admissible,
        "readout_handle_admissible": item.readout_handle_admissible,
        "ledger_conserved": item.ledger_conserved,
        "missing_requirements": list(item.missing_requirements),
        "blocked_shortcuts": list(item.blocked_shortcuts),
        "strongest_allowed_reading": item.strongest_allowed_reading,
    }


def future_packet_minimum() -> tuple[str, ...]:
    return (
        "declare the domain and boundary adapter B",
        "declare the region or observer boundary",
        "declare the admissible operation/readout class before choosing the witness",
        "declare the candidate record and undo/readout handle",
        "prove the handle is inadmissible rather than merely absent",
        "declare a ledger or invariant and check that it is conserved",
        "include fixed-richer-source disclosure as an absorber",
        "include positive and failure controls",
        "keep cross-repo identity and support claims gated",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "real GU/TaF/TI boundary adapter",
        "GU support for Time as Finality",
        "Time as Finality support for GU",
        "Temporal Issuance support for Time as Finality",
        "universal ledger",
        "hidden central server",
        "BRST physicality",
        "physics-side irreversibility claim",
        "claim-ledger movement",
        "roadmap movement",
        "README movement",
        "North Star movement",
        "public-posture movement",
        "hard-policy movement",
        "external publication",
        "cross-repo truth movement",
    )


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {packet_id} | {admitted} | {label} | {undo} | {readout} | {ledger} | {missing} | {blocked} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            undo="yes" if decision["undo_handle_admissible"] else "no",
            readout="yes" if decision["readout_handle_admissible"] else "no",
            ledger="yes" if decision["ledger_conserved"] else "no",
            missing=", ".join(decision["missing_requirements"]) or "none",
            blocked=", ".join(decision["blocked_shortcuts"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    future = [f"- {item}" for item in payload["future_packet_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T511 - Boundary Adapter Finality Gate - v0.1 results",
            "",
            "> TaF-side finite adapter/finality gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T511-boundary-adapter-finality-gate.md`",
            "- Model: `models/boundary_adapter_finality_gate.py`",
            "- Tests: `tests/test_boundary_adapter_finality_gate.py`",
            f"- Source intake: `{payload['source_intake']}`",
            f"- Source guardrail: `{payload['source_guardrail']}`",
            f"- Artifact JSON: `results/{ARTIFACT_ID}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Undo handle admissible? | Readout handle admissible? | Ledger conserved? | Missing requirements | Blocked shortcuts |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Future Packet Minimum",
            "",
            *future,
            "",
            "## What This Does Not Earn",
            "",
            *blocked,
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
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
