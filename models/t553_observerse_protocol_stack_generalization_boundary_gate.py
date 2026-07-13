"""T553: Observerse protocol-stack generalization-boundary gate.

T551 and T552 are two bounded native survivors for the frozen five-layer
Observerse protocol stack. T553 asks the next narrower question: what boundary
keeps that transfer from turning into source-law promotion, TAF4 movement, or a
TAF8 cross-domain theorem?
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t551_observerse_protocol_stack_source_law_stress_packet as t551
from models import t552_observerse_protocol_stack_independent_transfer_gate as t552


ARTIFACT = "T553-observerse-protocol-stack-generalization-boundary-gate-v0.1"
VERDICT = "observerse_protocol_stack_generalization_boundary_mapped"
GENERALIZATION_STATUS = "BOUNDARY_MAPPED_NO_SOURCE_LAW_STATUS"
NEXT_PACKET = "t554_observerse_protocol_stack_minimality_gate"

FROZEN_LAYERS = (
    "issuance",
    "admissibility",
    "sybil_finality",
    "consensus",
    "governance",
)

NOT_CLAIMED = (
    "T553 does not validate Observerse, establish a source law, prove a "
    "shadow-protection theorem, derive spacetime, prove manifoldlikeness, "
    "repair T528, reverse T223, unpause S1, promote S1, change claim status, "
    "change Canon Index tiers, change canon verdicts, change public posture, "
    "change the North Star, authorize external publication, move TAF4, execute "
    "TAF8, or move cross-repo truth. It maps a bounded generalization boundary "
    "for the frozen T550-T552 protocol-stack route only."
)


@dataclass(frozen=True)
class BoundaryCase:
    case_id: str
    description: str
    expected_status: str
    native_finality: bool
    bounded_fixture: bool
    target_blind: bool
    frozen_layers: tuple[str, ...]
    conditional_governance: bool
    trusted_consensus: bool
    cross_domain_packet: bool = False
    imports_external_target: bool = False
    retunes_aprd: bool = False
    asserts_source_law: bool = False
    moves_taf4: bool = False
    executes_taf8: bool = False


@dataclass(frozen=True)
class BoundaryOutcome:
    case_id: str
    expected_status: str
    actual_status: str
    matched: bool
    in_generalization_class: bool
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
class T553Result:
    artifact: str
    source_t551_verdict: str
    source_t552_verdict: str
    source_t552_selected_next_packet: str
    frozen_layers: tuple[str, ...]
    generalization_status: str
    boundary_outcomes: tuple[BoundaryOutcome, ...]
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


def run_t553_analysis() -> T553Result:
    t551_result = t551.run_t551_analysis()
    t552_result = t552.run_t552_analysis()
    cases = _boundary_cases(t551_result, t552_result)
    outcomes = tuple(_evaluate_case(case) for case in cases)
    gates = _gate_decisions(t551_result, t552_result, outcomes)
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gates) else "none"
    verdict = (
        VERDICT
        if t551_result.verdict == t551.VERDICT
        and t552_result.verdict == t552.VERDICT
        and t552_result.selected_next_packet == t552.NEXT_PACKET
        and all(outcome.matched for outcome in outcomes)
        and selected_next_packet == NEXT_PACKET
        else "observerse_protocol_stack_generalization_boundary_unexpected_status"
    )

    return T553Result(
        artifact=ARTIFACT,
        source_t551_verdict=t551_result.verdict,
        source_t552_verdict=t552_result.verdict,
        source_t552_selected_next_packet=t552_result.selected_next_packet,
        frozen_layers=FROZEN_LAYERS,
        generalization_status=GENERALIZATION_STATUS,
        boundary_outcomes=outcomes,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should test whether every frozen layer is "
            "minimal across the admitted bounded-native class before any "
            "source-law, TAF4, TAF8, claim-ledger, or public-posture movement."
        ),
        taf11_update=(
            "TAF11 remains active. T553 maps the current generalization class "
            "as bounded native finality fixtures with frozen layers, target "
            "blindness, trusted consensus, and conditional governance. The "
            "next burden is layer minimality, not promotion."
        ),
        taf4_update=(
            "TAF4 remains blocked. A bounded native generalization boundary is "
            "not a finite-to-continuum bridge or causal-set/Lorentzian descent."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T553 explicitly rejects treating internal TAF11 generalization as "
            "TAF8 execution."
        ),
        source_law_reading=(
            "The stack now has a mapped bounded-native transfer class and "
            "clear rejection boundaries. That is stronger route control, not "
            "source-law status."
        ),
        claim_labels=_claim_labels(outcomes),
        claim_ledger_update=(
            "No claim-ledger update is earned. T553 is a boundary map and next "
            "minimality-gate selector; it leaves claim rows, Canon Index tiers, "
            "canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t553_result_to_dict(result: T553Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t551_verdict": result.source_t551_verdict,
        "source_t552_verdict": result.source_t552_verdict,
        "source_t552_selected_next_packet": result.source_t552_selected_next_packet,
        "frozen_layers": list(result.frozen_layers),
        "generalization_status": result.generalization_status,
        "boundary_outcomes": [
            {
                "case_id": outcome.case_id,
                "expected_status": outcome.expected_status,
                "actual_status": outcome.actual_status,
                "matched": outcome.matched,
                "in_generalization_class": outcome.in_generalization_class,
                "reason": outcome.reason,
            }
            for outcome in result.boundary_outcomes
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


def _boundary_cases(
    t551_result: t551.T551Result,
    t552_result: t552.T552Result,
) -> tuple[BoundaryCase, ...]:
    t551_passed = t551_result.verdict == t551.VERDICT
    t552_passed = t552_result.verdict == t552.VERDICT
    return (
        BoundaryCase(
            case_id="t551_bounded_native_fixture",
            description="The original bounded native fixture survivor.",
            expected_status="inside_bounded_native_class",
            native_finality=t551_passed,
            bounded_fixture=True,
            target_blind=True,
            frozen_layers=FROZEN_LAYERS,
            conditional_governance=True,
            trusted_consensus=True,
        ),
        BoundaryCase(
            case_id="t552_independent_transfer_fixture",
            description="The independent handoff/partition/repair survivor.",
            expected_status="inside_bounded_native_class",
            native_finality=t552_passed,
            bounded_fixture=True,
            target_blind=True,
            frozen_layers=tuple(t552_result.source_t550_layer_ids),
            conditional_governance=True,
            trusted_consensus=True,
        ),
        BoundaryCase(
            case_id="third_phase_rotated_native_fixture",
            description="A new native, bounded, target-blind fixture shape.",
            expected_status="inside_bounded_native_class",
            native_finality=True,
            bounded_fixture=True,
            target_blind=True,
            frozen_layers=FROZEN_LAYERS,
            conditional_governance=True,
            trusted_consensus=True,
        ),
        BoundaryCase(
            case_id="single_observer_consensus_light_fixture",
            description="Native bounded records without trusted shared consensus.",
            expected_status="boundary_consensus_insufficient",
            native_finality=True,
            bounded_fixture=True,
            target_blind=True,
            frozen_layers=FROZEN_LAYERS,
            conditional_governance=True,
            trusted_consensus=False,
        ),
        BoundaryCase(
            case_id="near_term_only_governance_fixture",
            description="Native bounded records with governance made unconditional.",
            expected_status="boundary_conditional_governance_missing",
            native_finality=True,
            bounded_fixture=True,
            target_blind=True,
            frozen_layers=FROZEN_LAYERS,
            conditional_governance=False,
            trusted_consensus=True,
        ),
        BoundaryCase(
            case_id="aprd_retuned_fixture",
            description="A family-local APRD retune is substituted for the stack.",
            expected_status="blocked_retreated_route",
            native_finality=True,
            bounded_fixture=True,
            target_blind=True,
            frozen_layers=FROZEN_LAYERS,
            conditional_governance=True,
            trusted_consensus=True,
            retunes_aprd=True,
        ),
        BoundaryCase(
            case_id="cross_domain_taf8_packet",
            description="A cross-domain transfer packet is imported into TAF11.",
            expected_status="out_of_scope_cross_domain",
            native_finality=False,
            bounded_fixture=False,
            target_blind=True,
            frozen_layers=FROZEN_LAYERS,
            conditional_governance=True,
            trusted_consensus=True,
            cross_domain_packet=True,
            executes_taf8=True,
        ),
        BoundaryCase(
            case_id="lorentzian_target_import_fixture",
            description="A Lorentzian or causal-set target is imported as success.",
            expected_status="blocked_target_import",
            native_finality=True,
            bounded_fixture=True,
            target_blind=False,
            frozen_layers=FROZEN_LAYERS,
            conditional_governance=True,
            trusted_consensus=True,
            imports_external_target=True,
            moves_taf4=True,
        ),
        BoundaryCase(
            case_id="source_law_overread_fixture",
            description="Two bounded survivors are asserted as source-law proof.",
            expected_status="blocked_source_law_overread",
            native_finality=True,
            bounded_fixture=True,
            target_blind=True,
            frozen_layers=FROZEN_LAYERS,
            conditional_governance=True,
            trusted_consensus=True,
            asserts_source_law=True,
        ),
    )


def _evaluate_case(case: BoundaryCase) -> BoundaryOutcome:
    actual_status = _classify_case(case)
    in_generalization_class = actual_status == "inside_bounded_native_class"
    return BoundaryOutcome(
        case_id=case.case_id,
        expected_status=case.expected_status,
        actual_status=actual_status,
        matched=actual_status == case.expected_status,
        in_generalization_class=in_generalization_class,
        reason=_case_reason(actual_status),
    )


def _classify_case(case: BoundaryCase) -> str:
    if case.asserts_source_law:
        return "blocked_source_law_overread"
    if case.cross_domain_packet or case.executes_taf8:
        return "out_of_scope_cross_domain"
    if case.imports_external_target or case.moves_taf4 or not case.target_blind:
        return "blocked_target_import"
    if case.retunes_aprd:
        return "blocked_retreated_route"
    if tuple(case.frozen_layers) != FROZEN_LAYERS:
        return "blocked_layer_retune"
    if not case.conditional_governance:
        return "boundary_conditional_governance_missing"
    if not case.trusted_consensus:
        return "boundary_consensus_insufficient"
    if case.native_finality and case.bounded_fixture:
        return "inside_bounded_native_class"
    return "outside_current_class"


def _case_reason(status: str) -> str:
    reasons = {
        "inside_bounded_native_class": (
            "The case preserves bounded native finality, target blindness, "
            "frozen layers, trusted consensus, and conditional governance."
        ),
        "boundary_consensus_insufficient": (
            "The stack is not generalized to records that lack trusted shared consensus."
        ),
        "boundary_conditional_governance_missing": (
            "The governance layer remains conditional rather than an unconditional primitive."
        ),
        "blocked_retreated_route": "APRD retuning is a retired route, not this stack boundary.",
        "out_of_scope_cross_domain": (
            "TAF8 cross-domain packets require their own domain-native spine."
        ),
        "blocked_target_import": (
            "TAF4 or Lorentzian target import cannot define stack success."
        ),
        "blocked_source_law_overread": (
            "Bounded survivors do not establish source-law status."
        ),
        "blocked_layer_retune": "The layer contract must remain frozen.",
        "outside_current_class": "The case lacks the current bounded-native shape.",
    }
    return reasons[status]


def _gate_decisions(
    t551_result: t551.T551Result,
    t552_result: t552.T552Result,
    outcomes: tuple[BoundaryOutcome, ...],
) -> tuple[GateDecision, ...]:
    inside_count = sum(outcome.in_generalization_class for outcome in outcomes)
    outcome_by_id = {outcome.case_id: outcome for outcome in outcomes}
    decisions = (
        (
            "t551_t552_authority",
            t551_result.verdict == t551.VERDICT
            and t552_result.verdict == t552.VERDICT
            and t552_result.selected_next_packet == t552.NEXT_PACKET,
            "T551 and T552 are completed bounded native survivors and T552 selected T553.",
            "The required T551/T552 source state is not present.",
        ),
        (
            "frozen_layer_contract_preserved",
            tuple(t552_result.source_t550_layer_ids) == FROZEN_LAYERS,
            "The five-layer contract remains frozen.",
            "The layer contract drifted.",
        ),
        (
            "bounded_native_class_has_multiple_members",
            inside_count >= 3,
            "The bounded-native class includes T551, T552, and a third phase-rotated candidate shape.",
            "The admitted class has not generalized beyond the prior two fixtures.",
        ),
        (
            "consensus_boundary_detected",
            outcome_by_id["single_observer_consensus_light_fixture"].actual_status
            == "boundary_consensus_insufficient",
            "The gate refuses single-observer consensus-light overreach.",
            "Consensus-light cases were admitted too easily.",
        ),
        (
            "conditional_governance_boundary_detected",
            outcome_by_id["near_term_only_governance_fixture"].actual_status
            == "boundary_conditional_governance_missing",
            "The gate preserves conditional governance.",
            "Governance became unconditional.",
        ),
        (
            "external_and_cross_domain_boundaries_detected",
            outcome_by_id["cross_domain_taf8_packet"].actual_status
            == "out_of_scope_cross_domain"
            and outcome_by_id["lorentzian_target_import_fixture"].actual_status
            == "blocked_target_import",
            "TAF8 and TAF4 shortcuts are rejected.",
            "External target or cross-domain overreach was admitted.",
        ),
        (
            "source_law_status_not_earned",
            outcome_by_id["source_law_overread_fixture"].actual_status
            == "blocked_source_law_overread",
            "The gate keeps source-law status unearned.",
            "The packet promoted bounded survivors to source-law status.",
        ),
        (
            "all_boundary_predictions_match",
            all(outcome.matched for outcome in outcomes),
            "Every boundary case matched the predeclared status.",
            "At least one boundary case missed its predeclared status.",
        ),
        (
            "next_packet_specific",
            NEXT_PACKET.startswith("t554_"),
            "A single layer-minimality gate is named as the next packet.",
            "No specific next packet is named.",
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
            control_id="source_law_overread_control",
            blocks="Treating bounded native survivors as source-law proof.",
            reason="T553 maps a class boundary; it does not promote the class.",
        ),
        HostileControl(
            control_id="taf4_target_import_control",
            blocks="Using Lorentzian, causal-set, or finite-to-continuum targets as success criteria.",
            reason="T553 is internal TAF11 route control, not TAF4 bridge evidence.",
        ),
        HostileControl(
            control_id="taf8_cross_domain_control",
            blocks="Executing TAF8 or importing a cross-domain transfer packet.",
            reason="TAF8 still needs a real domain-native packet under its own spine.",
        ),
        HostileControl(
            control_id="aprd_retune_control",
            blocks="Retuning APRD to rescue the protocol-stack route.",
            reason="The post-APRD route was reset by T549 and stays reset.",
        ),
        HostileControl(
            control_id="conditional_governance_control",
            blocks="Making governance unconditional after two bounded survivors.",
            reason="Near-term versus full-horizon governance remains load-bearing.",
        ),
        HostileControl(
            control_id="layer_retune_control",
            blocks="Adding, dropping, or renaming layers after outcomes.",
            reason="T553 inherits the frozen T550-T552 layer contract unchanged.",
        ),
    )


def _claim_labels(outcomes: tuple[BoundaryOutcome, ...]) -> tuple[ClaimLabel, ...]:
    inside_ids = tuple(
        outcome.case_id for outcome in outcomes if outcome.in_generalization_class
    )
    blocked_ids = tuple(
        outcome.case_id for outcome in outcomes if not outcome.in_generalization_class
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The admitted bounded-native class currently includes: "
                + ", ".join(inside_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The gate blocks or bounds these overreach cases: "
                + ", ".join(blocked_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Conditional governance, trusted consensus, frozen layers, and "
                "target blindness are load-bearing boundary conditions."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The next useful test is layer minimality across the admitted "
                "bounded-native class, not source-law or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T553 Results: Observerse Protocol-Stack Generalization-Boundary Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Generalization status: `{payload['generalization_status']}`",
        f"- Source T551 verdict: `{payload['source_t551_verdict']}`",
        f"- Source T552 verdict: `{payload['source_t552_verdict']}`",
        f"- Source T552 selected next packet: `{payload['source_t552_selected_next_packet']}`",
        "- Frozen layers: " + ", ".join(f"`{item}`" for item in payload["frozen_layers"]),
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Boundary Outcomes",
        "",
        "| case | expected | actual | matched? | in class? | reason |",
        "| --- | --- | --- | :---: | :---: | --- |",
    ]
    for outcome in payload["boundary_outcomes"]:
        lines.append(
            "| "
            f"`{outcome['case_id']}` | "
            f"`{outcome['expected_status']}` | "
            f"`{outcome['actual_status']}` | "
            f"{outcome['matched']} | "
            f"{outcome['in_generalization_class']} | "
            f"{outcome['reason']} |"
        )
    lines.extend(["", "## Gate Decisions", "", "| gate | outcome | passed? | reason |", "| --- | --- | :---: | --- |"])
    for gate in payload["gate_decisions"]:
        lines.append(
            "| "
            f"`{gate['gate_id']}` | "
            f"`{gate['outcome']}` | "
            f"{gate['passed']} | "
            f"{gate['reason']} |"
        )
    lines.extend(["", "## Hostile Controls", "", "| control | blocks | reason |", "| --- | --- | --- |"])
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


def write_results(result: T553Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t553_result_to_dict(result)
    json_path = (
        results_dir
        / "T553-observerse-protocol-stack-generalization-boundary-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T553-observerse-protocol-stack-generalization-boundary-gate-v0.1-results.md"
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

    result = run_t553_analysis()
    payload = t553_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
