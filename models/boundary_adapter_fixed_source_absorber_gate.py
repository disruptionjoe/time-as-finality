"""T512: boundary-adapter fixed-source absorber gate.

T511 requires any future boundary-adapter finality packet to include
fixed-richer-source disclosure as an absorber. This module makes that
requirement executable in TaF-local terms.

The fixture is review machinery only. It does not assert a real GU/TaF/TI
adapter, source crossing, physical irreversibility, claim movement, public
posture movement, or cross-repo truth.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T512-boundary-adapter-fixed-source-absorber-gate-v0.1"
VERDICT = "BOUNDARY_ADAPTER_FIXED_SOURCE_ABSORBER_GATE_BUILT_REVIEW_ONLY"
SOURCE_GATE = "tests/T511-boundary-adapter-finality-gate.md"


@dataclass(frozen=True)
class FixedSourcePacket:
    packet_id: str
    source_inventory_declared: bool
    source_inventory_predeclared: bool
    fixed_source_contains_record: bool
    fixed_source_can_generate_record: bool
    access_schedule_reveals_record: bool
    undo_handle_declared: bool
    undo_handle_inadmissibility_declared: bool
    undo_handle_admissible: bool
    ledger_declared: bool
    ledger_conserved: bool
    positive_control_included: bool
    failure_control_included: bool
    source_crossing_language: bool = False
    requests_claim_movement: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth_movement: bool = False


@dataclass(frozen=True)
class FixedSourceDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    fixed_source_absorbs: bool
    fixed_source_absorber_tested: bool
    posthoc_source_completion: bool
    undo_handle_admissible: bool
    ledger_conserved: bool
    source_crossing_claim_blocked: bool
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
        "source_gate": SOURCE_GATE,
        "objective": (
            "Make T511's fixed-richer-source absorber requirement checkable. "
            "A boundary-adapter packet must distinguish review material from "
            "fixed-source disclosure, fixed-source generation, post-hoc source "
            "completion, source-crossing language, and cross-repo shortcuts."
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
            "review_target_admitted": by_id[
                "predeclared_nonfixed_source_review_target"
            ].admitted,
            "fixed_source_disclosure_absorbed": by_id[
                "fixed_source_disclosure_control"
            ].label
            == "ABSORBED_BY_FIXED_SOURCE_DISCLOSURE",
            "fixed_source_generation_absorbed": by_id[
                "fixed_source_generation_control"
            ].label
            == "ABSORBED_BY_FIXED_SOURCE_GENERATION",
            "posthoc_source_completion_rejected": by_id[
                "posthoc_source_inventory_shortcut"
            ].label
            == "REJECTED_POSTHOC_SOURCE_COMPLETION",
            "missing_source_inventory_rejected": by_id[
                "missing_source_inventory_shortcut"
            ].label
            == "REJECTED_MISSING_FIXED_SOURCE_ABSORBER",
            "admissible_handle_rejected": by_id[
                "admissible_undo_handle_control"
            ].label
            == "REJECTED_HANDLE_ADMISSIBLE_NOT_FINAL",
            "source_crossing_language_blocked": by_id[
                "source_crossing_language_shortcut"
            ].source_crossing_claim_blocked,
            "cross_repo_shortcut_blocked": by_id[
                "cross_repo_identity_shortcut"
            ].label
            == "BLOCKED_CROSS_REPO_OR_GOVERNANCE_SHORTCUT",
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
            "real_adapter_claim_earned": False,
            "source_crossing_claim_earned": False,
            "physics_claim_earned": False,
        },
        "future_packet_minimum": future_packet_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T512 admits one synthetic review target only when a fixed source "
            "inventory is predeclared and fails to contain or generate the "
            "candidate record while the finality handle remains inadmissible "
            "and the ledger remains conserved. Fixed-source containment, "
            "fixed-source generation, post-hoc source completion, missing "
            "source inventory, admissible handles, source-crossing language, "
            "and cross-repo identity shortcuts are absorbed, rejected, or "
            "blocked."
        ),
    }


def fixture_packets() -> tuple[FixedSourcePacket, ...]:
    base = {
        "source_inventory_declared": True,
        "source_inventory_predeclared": True,
        "fixed_source_contains_record": False,
        "fixed_source_can_generate_record": False,
        "access_schedule_reveals_record": False,
        "undo_handle_declared": True,
        "undo_handle_inadmissibility_declared": True,
        "undo_handle_admissible": False,
        "ledger_declared": True,
        "ledger_conserved": True,
        "positive_control_included": True,
        "failure_control_included": True,
    }
    return (
        FixedSourcePacket(
            packet_id="predeclared_nonfixed_source_review_target",
            **base,
        ),
        FixedSourcePacket(
            packet_id="fixed_source_disclosure_control",
            **{
                **base,
                "fixed_source_contains_record": True,
                "access_schedule_reveals_record": True,
            },
        ),
        FixedSourcePacket(
            packet_id="fixed_source_generation_control",
            **{**base, "fixed_source_can_generate_record": True},
        ),
        FixedSourcePacket(
            packet_id="posthoc_source_inventory_shortcut",
            **{**base, "source_inventory_predeclared": False},
        ),
        FixedSourcePacket(
            packet_id="missing_source_inventory_shortcut",
            **{
                **base,
                "source_inventory_declared": False,
                "source_inventory_predeclared": False,
            },
        ),
        FixedSourcePacket(
            packet_id="admissible_undo_handle_control",
            **{**base, "undo_handle_admissible": True},
        ),
        FixedSourcePacket(
            packet_id="source_crossing_language_shortcut",
            **{
                **base,
                "source_inventory_declared": False,
                "source_inventory_predeclared": False,
                "undo_handle_declared": False,
                "undo_handle_inadmissibility_declared": False,
                "source_crossing_language": True,
            },
        ),
        FixedSourcePacket(
            packet_id="cross_repo_identity_shortcut",
            **{
                **base,
                "source_crossing_language": True,
                "requests_claim_movement": True,
                "requests_cross_repo_truth_movement": True,
            },
        ),
    )


def evaluate_packet(packet: FixedSourcePacket) -> FixedSourceDecision:
    blocked = blocked_shortcuts(packet)
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
                "The fixed-source absorber gate cannot move claims, public "
                "posture, external publication, or cross-repo identity/support."
            ),
        )
    if packet.source_crossing_language and (
        not packet.source_inventory_declared or not packet.undo_handle_declared
    ):
        return decision(
            packet,
            admitted=False,
            label="REJECTED_SOURCE_CROSSING_NOT_ABSORBER_TEST",
            action="reject",
            missing=missing,
            blocked=(),
            source_crossing_blocked=True,
            strongest=(
                "Source-crossing language is not a fixed-source absorber test "
                "unless source inventory and TaF finality handle controls are "
                "declared."
            ),
        )
    if not packet.source_inventory_declared:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_MISSING_FIXED_SOURCE_ABSORBER",
            action="reject",
            missing=missing + ("fixed richer source inventory",),
            blocked=(),
            strongest="No fixed-source absorber has been tested.",
        )
    if not packet.source_inventory_predeclared:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_POSTHOC_SOURCE_COMPLETION",
            action="reject",
            missing=missing + ("predeclared fixed source inventory",),
            blocked=(),
            strongest=(
                "A source inventory created after the witness is chosen is "
                "post-hoc completion, not an absorber control."
            ),
        )
    if packet.fixed_source_contains_record and packet.access_schedule_reveals_record:
        return decision(
            packet,
            admitted=False,
            label="ABSORBED_BY_FIXED_SOURCE_DISCLOSURE",
            action="record_absorption",
            missing=missing,
            blocked=(),
            fixed_source_absorbs=True,
            strongest=(
                "The adapter reveals a record already present in the fixed "
                "richer source, so the packet is disclosure."
            ),
        )
    if packet.fixed_source_can_generate_record:
        return decision(
            packet,
            admitted=False,
            label="ABSORBED_BY_FIXED_SOURCE_GENERATION",
            action="record_absorption",
            missing=missing,
            blocked=(),
            fixed_source_absorbs=True,
            strongest=(
                "The predeclared fixed source can generate the candidate "
                "record, so the packet is not a nonfixed-source review target."
            ),
        )
    if packet.undo_handle_admissible:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_HANDLE_ADMISSIBLE_NOT_FINAL",
            action="reject",
            missing=missing,
            blocked=(),
            strongest=(
                "Even after the fixed-source absorber is tested, an admissible "
                "undo handle blocks finality."
            ),
        )
    if not packet.ledger_conserved:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_LEDGER_DRIFT",
            action="reject",
            missing=missing + ("conserved ledger or invariant",),
            blocked=(),
            strongest="A nonconserved ledger cannot support adapter-finality review.",
        )
    if missing:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_INCOMPLETE_FIXED_SOURCE_PACKET",
            action="reject",
            missing=missing,
            blocked=(),
            strongest="The packet has not paid the T512 fixed-source minimum.",
        )
    return decision(
        packet,
        admitted=True,
        label="ADMITTED_NONFIXED_SOURCE_REVIEW_TARGET",
        action="review_only",
        missing=(),
        blocked=(),
        strongest=(
            "A TaF-local review target remains only after the fixed source "
            "inventory is predeclared and fails to contain or generate the "
            "candidate record. This is not a real source-crossing result."
        ),
    )


def missing_requirements(packet: FixedSourcePacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.source_inventory_declared:
        missing.append("fixed richer source inventory")
    if not packet.source_inventory_predeclared:
        missing.append("predeclared source inventory")
    if not packet.undo_handle_declared:
        missing.append("undo or readout handle")
    if not packet.undo_handle_inadmissibility_declared:
        missing.append("handle inadmissibility proof")
    if not packet.ledger_declared:
        missing.append("ledger or invariant")
    if not packet.positive_control_included:
        missing.append("positive control")
    if not packet.failure_control_included:
        missing.append("failure control")
    return tuple(missing)


def blocked_shortcuts(packet: FixedSourcePacket) -> tuple[str, ...]:
    blocked: list[str] = []
    if packet.requests_claim_movement:
        blocked.append("claim_movement")
    if packet.requests_external_publication:
        blocked.append("external_publication")
    if packet.requests_cross_repo_truth_movement:
        blocked.append("cross_repo_truth_movement")
    return tuple(blocked)


def decision(
    packet: FixedSourcePacket,
    admitted: bool,
    label: str,
    action: str,
    missing: tuple[str, ...],
    blocked: tuple[str, ...],
    strongest: str,
    fixed_source_absorbs: bool = False,
    source_crossing_blocked: bool = False,
) -> FixedSourceDecision:
    return FixedSourceDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        review_target_only=admitted,
        fixed_source_absorbs=fixed_source_absorbs,
        fixed_source_absorber_tested=(
            packet.source_inventory_declared and packet.source_inventory_predeclared
        ),
        posthoc_source_completion=(
            packet.source_inventory_declared
            and not packet.source_inventory_predeclared
        ),
        undo_handle_admissible=packet.undo_handle_admissible,
        ledger_conserved=packet.ledger_conserved,
        source_crossing_claim_blocked=source_crossing_blocked,
        missing_requirements=missing,
        blocked_shortcuts=blocked,
        strongest_allowed_reading=strongest,
    )


def decision_dict(item: FixedSourceDecision) -> dict[str, Any]:
    return {
        "packet_id": item.packet_id,
        "admitted": item.admitted,
        "label": item.label,
        "action": item.action,
        "review_target_only": item.review_target_only,
        "fixed_source_absorbs": item.fixed_source_absorbs,
        "fixed_source_absorber_tested": item.fixed_source_absorber_tested,
        "posthoc_source_completion": item.posthoc_source_completion,
        "undo_handle_admissible": item.undo_handle_admissible,
        "ledger_conserved": item.ledger_conserved,
        "source_crossing_claim_blocked": item.source_crossing_claim_blocked,
        "missing_requirements": list(item.missing_requirements),
        "blocked_shortcuts": list(item.blocked_shortcuts),
        "strongest_allowed_reading": item.strongest_allowed_reading,
    }


def future_packet_minimum() -> tuple[str, ...]:
    return (
        "predeclare the fixed richer source inventory before choosing the witness",
        "state whether the candidate record is already contained in that source",
        "state whether predeclared source generators can form the candidate record",
        "distinguish access-schedule disclosure from nonfixed-source review targets",
        "keep the operation/readout class and undo/readout handle fixed before scoring",
        "prove handle inadmissibility and ledger conservation after absorber pressure",
        "include fixed-source disclosure and fixed-source generation controls",
        "block post-hoc source completion and cross-repo identity shortcuts",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "real GU/TaF/TI boundary adapter",
        "source crossing",
        "GU support for Time as Finality",
        "Time as Finality support for GU",
        "Temporal Issuance support for Time as Finality",
        "physics-side irreversibility claim",
        "universal ledger",
        "hidden central server",
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
        "| {packet_id} | {admitted} | {label} | {absorbs} | {tested} | {posthoc} | {undo} | {ledger} | {missing} | {blocked} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            absorbs="yes" if decision["fixed_source_absorbs"] else "no",
            tested="yes" if decision["fixed_source_absorber_tested"] else "no",
            posthoc="yes" if decision["posthoc_source_completion"] else "no",
            undo="yes" if decision["undo_handle_admissible"] else "no",
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
            "# T512 - Boundary Adapter Fixed-Source Absorber Gate - v0.1 results",
            "",
            "> TaF-side fixed-source absorber gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T512-boundary-adapter-fixed-source-absorber-gate.md`",
            "- Model: `models/boundary_adapter_fixed_source_absorber_gate.py`",
            "- Tests: `tests/test_boundary_adapter_fixed_source_absorber_gate.py`",
            f"- Source gate: `{payload['source_gate']}`",
            f"- Artifact JSON: `results/{ARTIFACT_ID}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Fixed source absorbs? | Absorber tested? | Post-hoc source? | Undo handle admissible? | Ledger conserved? | Missing requirements | Blocked shortcuts |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
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
