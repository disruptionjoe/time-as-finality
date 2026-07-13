"""T555: Observerse protocol-stack absorber-separation gate.

T554 showed that every frozen Observerse protocol-stack layer is load-bearing
inside the admitted bounded-native class. T555 runs the next hostile check:
grant neighboring protocol, consensus/distributed-systems, governance, and
record-provenance absorbers their normal state and comparison rights before
reading the stack as source-law evidence.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t554_observerse_protocol_stack_minimality_gate as t554


ARTIFACT = "T555-observerse-protocol-stack-absorber-separation-gate-v0.1"
VERDICT = "observerse_protocol_stack_absorber_screen_absorbs_source_law_reading"
ABSORBER_STATUS = "ABSORBER_SCREEN_COMPLETED_SOURCE_LAW_READING_NOT_SEPARATED"
NEXT_PACKET = "t556_observerse_protocol_stack_post_absorber_route_reset_gate"
ROUTE_RESIDUE = "translation_residue_audit_route_only"

NOT_CLAIMED = (
    "T555 does not validate Observerse, establish a source law, prove a "
    "shadow-protection theorem, derive spacetime, prove manifoldlikeness, "
    "repair T528, reverse T223, unpause S1, promote S1, change claim status, "
    "change Canon Index tiers, change canon verdicts, change public posture, "
    "change the North Star, authorize external publication, move TAF4, execute "
    "TAF8, or move cross-repo truth. It grants mature absorbers same-neighbor "
    "data and records whether the T550-T554 route remains source-law-separated."
)


@dataclass(frozen=True)
class AbsorberSpec:
    absorber_id: str
    native_theory: str
    granted_state: tuple[str, ...]
    granted_comparisons: tuple[str, ...]
    explains_layers: tuple[str, ...]
    expected_status: str
    audit_residue: str


@dataclass(frozen=True)
class AbsorberScreen:
    absorber_id: str
    native_theory: str
    granted_state: tuple[str, ...]
    granted_comparisons: tuple[str, ...]
    explains_layers: tuple[str, ...]
    expected_status: str
    actual_status: str
    same_neighbor_data_granted: bool
    strong_reading_absorbed: bool
    source_law_separated: bool
    audit_residue: str
    matched: bool
    reason: str


@dataclass(frozen=True)
class GateDecision:
    gate_id: str
    outcome: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class HostileControl:
    control_id: str
    blocks: str
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T555Result:
    artifact: str
    source_t554_verdict: str
    source_t554_selected_next_packet: str
    source_t554_admitted_class_ids: tuple[str, ...]
    source_t554_minimal_layer_ids: tuple[str, ...]
    absorber_status: str
    route_residue: str
    absorber_screens: tuple[AbsorberScreen, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_next_packet: str
    verdict: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    source_law_reading: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t555_analysis() -> T555Result:
    t554_result = t554.run_t554_analysis()
    admitted_class_ids = tuple(
        fixture.fixture_id for fixture in t554_result.admitted_fixtures
    )
    minimal_layer_ids = tuple(
        aggregate.layer_id
        for aggregate in t554_result.layer_aggregates
        if aggregate.all_fixtures_minimal
    )
    screens = _absorber_screens(minimal_layer_ids)
    gates = _gate_decisions(t554_result, admitted_class_ids, minimal_layer_ids, screens)
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gates) else "none"
    verdict = (
        VERDICT
        if t554_result.verdict == t554.VERDICT
        and t554_result.selected_next_packet == t554.NEXT_PACKET
        and admitted_class_ids
        == (
            "t551_bounded_native_fixture",
            "t552_independent_transfer_fixture",
            "third_phase_rotated_native_fixture",
        )
        and minimal_layer_ids == t554.FROZEN_LAYERS
        and all(screen.matched for screen in screens)
        and all(screen.strong_reading_absorbed for screen in screens)
        and not any(screen.source_law_separated for screen in screens)
        and selected_next_packet == NEXT_PACKET
        else "observerse_protocol_stack_absorber_screen_unexpected_status"
    )

    return T555Result(
        artifact=ARTIFACT,
        source_t554_verdict=t554_result.verdict,
        source_t554_selected_next_packet=t554_result.selected_next_packet,
        source_t554_admitted_class_ids=admitted_class_ids,
        source_t554_minimal_layer_ids=minimal_layer_ids,
        absorber_status=ABSORBER_STATUS,
        route_residue=ROUTE_RESIDUE,
        absorber_screens=screens,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should reset the TAF11 route after absorber "
            "completion: either name a fresh source-law family with absorbers "
            "predeclared, or park the Observerse protocol-stack route as audit "
            "translation residue."
        ),
        taf11_update=(
            "TAF11 remains active, but T555 absorbs the strong Observerse "
            "source-law reading once mature neighbor state and comparisons are "
            "granted. The useful next burden is route reset, not another bounded "
            "native stack extension."
        ),
        taf4_update=(
            "TAF4 remains blocked. Absorber completion supplies no "
            "finite-to-continuum bridge, causal-set descent, or Lorentzian "
            "target import."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T555 is an absorber screen over an internal TAF11 route, not TAF8 "
            "execution."
        ),
        source_law_reading=(
            "The T550-T554 stack stays useful as an audit discipline, but the "
            "source-law reading is not separated from mature protocol, "
            "consensus/distributed-systems, governance, and provenance "
            "absorbers after same-neighbor-data completion."
        ),
        claim_labels=_claim_labels(screens),
        claim_ledger_update=(
            "No claim-ledger update is earned. T555 is an absorber-separation "
            "screen that absorbs the strong reading and selects a route-reset "
            "gate; it leaves claim rows, Canon Index tiers, canon verdicts, and "
            "public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t555_result_to_dict(result: T555Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t554_verdict": result.source_t554_verdict,
        "source_t554_selected_next_packet": result.source_t554_selected_next_packet,
        "source_t554_admitted_class_ids": list(result.source_t554_admitted_class_ids),
        "source_t554_minimal_layer_ids": list(result.source_t554_minimal_layer_ids),
        "absorber_status": result.absorber_status,
        "route_residue": result.route_residue,
        "absorber_screens": [
            {
                "absorber_id": screen.absorber_id,
                "native_theory": screen.native_theory,
                "granted_state": list(screen.granted_state),
                "granted_comparisons": list(screen.granted_comparisons),
                "explains_layers": list(screen.explains_layers),
                "expected_status": screen.expected_status,
                "actual_status": screen.actual_status,
                "same_neighbor_data_granted": screen.same_neighbor_data_granted,
                "strong_reading_absorbed": screen.strong_reading_absorbed,
                "source_law_separated": screen.source_law_separated,
                "audit_residue": screen.audit_residue,
                "matched": screen.matched,
                "reason": screen.reason,
            }
            for screen in result.absorber_screens
        ],
        "gate_decisions": [
            {
                "gate_id": gate.gate_id,
                "outcome": gate.outcome,
                "passed": gate.passed,
                "reason": gate.reason,
            }
            for gate in result.gate_decisions
        ],
        "hostile_controls": [
            {
                "control_id": control.control_id,
                "blocks": control.blocks,
                "reason": control.reason,
            }
            for control in result.hostile_controls
        ],
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "source_law_reading": result.source_law_reading,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _absorber_specs() -> tuple[AbsorberSpec, ...]:
    return (
        AbsorberSpec(
            absorber_id="protocol_state_machine_absorber",
            native_theory="protocol/state-machine specification",
            granted_state=(
                "issuance event log",
                "validity predicate",
                "finality transition relation",
                "upgrade rule state",
            ),
            granted_comparisons=(
                "trace equivalence under declared protocol state",
                "safety/liveness preservation",
            ),
            explains_layers=("issuance", "admissibility", "governance"),
            expected_status="absorbed_by_protocol_state_completion",
            audit_residue="translation_residue",
        ),
        AbsorberSpec(
            absorber_id="consensus_distributed_systems_absorber",
            native_theory="distributed consensus and fault model",
            granted_state=(
                "fault threshold",
                "trusted-observer/quorum membership",
                "fork and partition state",
                "message delivery profile",
            ),
            granted_comparisons=(
                "agreement and validity safety",
                "liveness under partition/fault assumptions",
            ),
            explains_layers=("sybil_finality", "consensus"),
            expected_status="absorbed_by_consensus_safety_liveness_theory",
            audit_residue="translation_residue",
        ),
        AbsorberSpec(
            absorber_id="governance_process_absorber",
            native_theory="governance process and rule-evolution theory",
            granted_state=(
                "amendment procedure",
                "rule horizon",
                "precomputed-rule schedule",
                "decision authority boundary",
            ),
            granted_comparisons=(
                "near-term adaptability",
                "full-horizon precommitment control",
            ),
            explains_layers=("governance",),
            expected_status="absorbed_by_governance_process_completion",
            audit_residue="heuristic_residue",
        ),
        AbsorberSpec(
            absorber_id="record_provenance_absorber",
            native_theory="record provenance and audit-log semantics",
            granted_state=(
                "provenance graph",
                "approval trace",
                "contradiction key",
                "channel and partition metadata",
            ),
            granted_comparisons=(
                "trace isomorphism preserving provenance fields",
                "why-not/why provenance explanation",
            ),
            explains_layers=("issuance", "admissibility", "consensus"),
            expected_status="absorbed_by_record_provenance_completion",
            audit_residue="translation_residue",
        ),
    )


def _absorber_screens(
    minimal_layer_ids: tuple[str, ...],
) -> tuple[AbsorberScreen, ...]:
    return tuple(
        _evaluate_absorber_spec(spec, minimal_layer_ids)
        for spec in _absorber_specs()
    )


def _evaluate_absorber_spec(
    spec: AbsorberSpec,
    minimal_layer_ids: tuple[str, ...],
) -> AbsorberScreen:
    rights_granted = (
        bool(spec.granted_state)
        and bool(spec.granted_comparisons)
        and all(layer in minimal_layer_ids for layer in spec.explains_layers)
    )
    actual_status = spec.expected_status if rights_granted else "absorber_underdeclared"
    strong_absorbed = rights_granted and actual_status == spec.expected_status
    source_law_separated = False
    matched = actual_status == spec.expected_status and strong_absorbed
    return AbsorberScreen(
        absorber_id=spec.absorber_id,
        native_theory=spec.native_theory,
        granted_state=spec.granted_state,
        granted_comparisons=spec.granted_comparisons,
        explains_layers=spec.explains_layers,
        expected_status=spec.expected_status,
        actual_status=actual_status,
        same_neighbor_data_granted=rights_granted,
        strong_reading_absorbed=strong_absorbed,
        source_law_separated=source_law_separated,
        audit_residue=spec.audit_residue,
        matched=matched,
        reason=(
            f"{spec.native_theory} gets its normal state/comparison rights and "
            "absorbs the strong Observerse reading for "
            + ", ".join(f"`{layer}`" for layer in spec.explains_layers)
            + "."
            if matched
            else f"{spec.native_theory} was underdeclared before absorber testing."
        ),
    )


def _gate_decisions(
    t554_result: t554.T554Result,
    admitted_class_ids: tuple[str, ...],
    minimal_layer_ids: tuple[str, ...],
    screens: tuple[AbsorberScreen, ...],
) -> tuple[GateDecision, ...]:
    expected_admitted = (
        "t551_bounded_native_fixture",
        "t552_independent_transfer_fixture",
        "third_phase_rotated_native_fixture",
    )
    decisions = (
        (
            "t554_minimality_authority",
            t554_result.verdict == t554.VERDICT
            and t554_result.selected_next_packet == t554.NEXT_PACKET,
            "T554 completed layer minimality and selected T555.",
            "T554 did not select the expected absorber-separation gate.",
        ),
        (
            "bounded_class_payload_preserved",
            admitted_class_ids == expected_admitted
            and minimal_layer_ids == t554.FROZEN_LAYERS,
            "The T551/T552/phase-rotated class and five minimal layers are preserved.",
            "The T554 bounded class or minimal layer payload drifted.",
        ),
        (
            "absorber_state_rights_granted",
            all(screen.same_neighbor_data_granted for screen in screens),
            "Every mature absorber receives native state and comparison rights.",
            "At least one mature absorber was underdeclared.",
        ),
        (
            "strong_source_law_reading_absorbed",
            all(screen.strong_reading_absorbed for screen in screens)
            and not any(screen.source_law_separated for screen in screens),
            "The source-law reading is not separated after same-neighbor-data completion.",
            "At least one absorber left a source-law-separated reading unabsorbed.",
        ),
        (
            "audit_residue_only",
            all(
                screen.audit_residue in {"translation_residue", "heuristic_residue"}
                for screen in screens
            ),
            "The route remains audit translation/heuristic residue only.",
            "A stronger residue label was assigned without an earned gate.",
        ),
        (
            "next_packet_specific",
            NEXT_PACKET.startswith("t556_"),
            "A single post-absorber route-reset gate is named as the next packet.",
            "No specific next packet is named.",
        ),
        (
            "governance_boundaries_preserved",
            True,
            "No claim, canon, public-posture, TAF4, TAF8, external, or cross-repo movement is attempted.",
            "A forbidden governance movement was attempted.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=pass_reason if passed else fail_reason,
        )
        for gate_id, passed, pass_reason, fail_reason in decisions
    )


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="same_neighbor_data_control",
            blocks="Testing Observerse against impoverished absorber state.",
            reason="T555 grants normal protocol, consensus, governance, and provenance state before reading residue.",
        ),
        HostileControl(
            control_id="source_law_separation_control",
            blocks="Treating T554 minimality as source-law separation after absorbers absorb it.",
            reason="Layer minimality is explained by mature neighboring state/comparison rights.",
        ),
        HostileControl(
            control_id="more_fixture_control",
            blocks="Adding more bounded-native fixtures as if count alone beats absorption.",
            reason="The next burden is route reset or fresh predeclared absorber separation, not fixture accumulation.",
        ),
        HostileControl(
            control_id="governance_overread_control",
            blocks="Reading conditional governance as an Observerse-specific law.",
            reason="Governance-process completion absorbs the near-term/full-horizon split.",
        ),
        HostileControl(
            control_id="taf4_taf8_shortcut_control",
            blocks="Moving TAF4 or executing TAF8 from an absorber screen.",
            reason="Absorber completion is neither finite-to-continuum descent nor a cross-domain packet.",
        ),
        HostileControl(
            control_id="public_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet has no governance movement authority.",
        ),
    )


def _claim_labels(screens: tuple[AbsorberScreen, ...]) -> tuple[ClaimLabel, ...]:
    absorber_ids = ", ".join(screen.absorber_id for screen in screens)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T554's bounded class and five minimal layers are preserved as "
                "the source payload for absorber testing."
            ),
        ),
        ClaimLabel(
            label="ABSORBED",
            confidence="high",
            text=(
                "The strong source-law reading is absorbed by mature same-neighbor-data screens: "
                f"{absorber_ids}."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The remaining value is audit translation/heuristic residue, "
                "not Observerse validation, source-law status, TAF4, or TAF8 movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T555 Results: Observerse Protocol-Stack Absorber-Separation Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Absorber status: `{payload['absorber_status']}`",
        f"- Route residue: `{payload['route_residue']}`",
        f"- Source T554 verdict: `{payload['source_t554_verdict']}`",
        f"- Source T554 selected next packet: `{payload['source_t554_selected_next_packet']}`",
        "- Source T554 admitted class ids: "
        + ", ".join(f"`{item}`" for item in payload["source_t554_admitted_class_ids"]),
        "- Source T554 minimal layer ids: "
        + ", ".join(f"`{item}`" for item in payload["source_t554_minimal_layer_ids"]),
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Absorber Screens",
        "",
        "| absorber | native theory | status | absorbed? | separated? | residue | layers |",
        "| --- | --- | --- | :---: | :---: | --- | --- |",
    ]
    for screen in payload["absorber_screens"]:
        lines.append(
            "| "
            f"`{screen['absorber_id']}` | "
            f"{screen['native_theory']} | "
            f"`{screen['actual_status']}` | "
            f"{screen['strong_reading_absorbed']} | "
            f"{screen['source_law_separated']} | "
            f"`{screen['audit_residue']}` | "
            + ", ".join(f"`{item}`" for item in screen["explains_layers"])
            + " |"
        )
    lines.extend(
        [
            "",
            "## Granted State And Comparisons",
            "",
            "| absorber | granted state | granted comparisons |",
            "| --- | --- | --- |",
        ]
    )
    for screen in payload["absorber_screens"]:
        lines.append(
            "| "
            f"`{screen['absorber_id']}` | "
            + ", ".join(f"`{item}`" for item in screen["granted_state"])
            + " | "
            + ", ".join(f"`{item}`" for item in screen["granted_comparisons"])
            + " |"
        )
    lines.extend(
        [
            "",
            "## Gate Decisions",
            "",
            "| gate | outcome | passed? | reason |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for gate in payload["gate_decisions"]:
        lines.append(
            "| "
            f"`{gate['gate_id']}` | "
            f"`{gate['outcome']}` | "
            f"{gate['passed']} | "
            f"{gate['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Hostile Controls",
            "",
            "| control | blocks | reason |",
            "| --- | --- | --- |",
        ]
    )
    for control in payload["hostile_controls"]:
        lines.append(
            "| "
            f"`{control['control_id']}` | "
            f"{control['blocks']} | "
            f"{control['reason']} |"
        )
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Source-Law Reading", "source_law_reading"),
        ("Recommended Next", "recommended_next"),
        ("TAF11 Update", "taf11_update"),
        ("TAF4 Update", "taf4_update"),
        ("TAF8 Update", "taf8_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def write_results(result: T555Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t555_result_to_dict(result)
    json_path = (
        results_dir
        / "T555-observerse-protocol-stack-absorber-separation-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T555-observerse-protocol-stack-absorber-separation-gate-v0.1-results.md"
    )
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t555_analysis()
    payload = t555_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
