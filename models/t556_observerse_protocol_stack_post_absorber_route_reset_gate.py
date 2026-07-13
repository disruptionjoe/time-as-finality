"""T556: Observerse protocol-stack post-absorber route reset gate.

T555 granted mature protocol, consensus, governance, and provenance absorbers
their normal state and comparison rights, absorbing the strong Observerse
source-law reading. T556 consumes that result and resets TAF11: the Observerse
protocol-stack route can stay as audit translation residue, but it cannot be
extended as source-law evidence without a fresh family and predeclared
absorbers.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t555_observerse_protocol_stack_absorber_separation_gate as t555


ARTIFACT = "T556-observerse-protocol-stack-post-absorber-route-reset-gate-v0.1"
VERDICT = "observerse_protocol_stack_route_parked_after_absorber_completion"
ROUTE_RESET_STATUS = "TAF11_ROUTE_RESET_TO_FRESH_FAMILY_PREFLIGHT"
PARKED_ROUTE_ID = "park_observerse_protocol_stack_as_audit_translation_residue"
NEXT_PACKET = "t557_taf11_fresh_source_law_family_preflight_gate"

NOT_CLAIMED = (
    "T556 does not validate Observerse, establish a source law, prove a "
    "shadow-protection theorem, derive spacetime, prove manifoldlikeness, "
    "repair T528, reverse T223, unpause S1, promote S1, change claim status, "
    "change Canon Index tiers, change canon verdicts, change public posture, "
    "change the North Star, authorize external publication, move TAF4, execute "
    "TAF8, or move cross-repo truth. It parks the absorbed Observerse "
    "protocol-stack route and requires a fresh source-law family preflight "
    "before any renewed TAF11 source-law attempt."
)


@dataclass(frozen=True)
class ResetOption:
    option_id: str
    description: str
    next_packet: str
    fresh_source_family_named: bool
    absorbers_predeclared: bool
    source_variables_declared: bool
    falsifier_predeclared: bool
    continues_observerse_protocol_stack: bool
    treats_absorbed_route_as_source_law: bool
    parks_absorbed_route: bool
    keeps_audit_translation_value: bool
    computable_without_target_import: bool
    blocks_more_fixture_accumulation: bool
    blocks_taf4_movement: bool
    blocks_taf8_execution: bool
    no_claim_canon_public_external_movement: bool


@dataclass(frozen=True)
class ResetDecision:
    option_id: str
    outcome: str
    selected: bool
    role: str
    missing_requirements: tuple[str, ...]
    reason: str
    next_packet: str


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
class T556Result:
    artifact: str
    source_t555_verdict: str
    source_t555_selected_next_packet: str
    source_t555_route_residue: str
    source_t555_absorber_status: str
    route_reset_status: str
    reset_decisions: tuple[ResetDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_reset_id: str
    selected_next_packet: str
    verdict: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t556_analysis() -> T556Result:
    t555_result = t555.run_t555_analysis()
    decisions = tuple(_evaluate_option(option) for option in _reset_options())
    selected = tuple(decision for decision in decisions if decision.selected)
    gates = _gate_decisions(t555_result, decisions, selected)
    selected_reset_id = selected[0].option_id if len(selected) == 1 else "none"
    selected_next_packet = selected[0].next_packet if len(selected) == 1 else "none"
    verdict = (
        VERDICT
        if t555_result.verdict == t555.VERDICT
        and t555_result.selected_next_packet == t555.NEXT_PACKET
        and t555_result.route_residue == t555.ROUTE_RESIDUE
        and selected_reset_id == PARKED_ROUTE_ID
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gates)
        else "observerse_protocol_stack_post_absorber_route_reset_unexpected_status"
    )

    return T556Result(
        artifact=ARTIFACT,
        source_t555_verdict=t555_result.verdict,
        source_t555_selected_next_packet=t555_result.selected_next_packet,
        source_t555_route_residue=t555_result.route_residue,
        source_t555_absorber_status=t555_result.absorber_status,
        route_reset_status=ROUTE_RESET_STATUS,
        reset_decisions=decisions,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_reset_id=selected_reset_id,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET} only as a fresh-family preflight: name a new "
            "TAF11 source-law family, declare its source variables, predeclare "
            "mature absorbers and falsifiers, and reject if it reuses the "
            "absorbed Observerse protocol-stack route as evidence."
        ),
        taf11_update=(
            "TAF11 remains the active high-value route, but the T550-T555 "
            "Observerse protocol-stack branch is parked as audit translation "
            "residue after absorber completion. Any next TAF11 swing must start "
            "from a fresh source-law family preflight, not another bounded "
            "Observerse stack extension."
        ),
        taf4_update=(
            "TAF4 remains blocked. Parking the absorbed Observerse route supplies "
            "no finite-to-continuum bridge, causal-set descent, or Lorentzian "
            "target import."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T556 is an internal TAF11 route reset, not TAF8 execution."
        ),
        claim_labels=_claim_labels(t555_result, decisions),
        claim_ledger_update=(
            "No claim-ledger update is earned. T556 is route reset and parking "
            "only; it leaves claim rows, Canon Index tiers, canon verdicts, and "
            "public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t556_result_to_dict(result: T556Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t555_verdict": result.source_t555_verdict,
        "source_t555_selected_next_packet": result.source_t555_selected_next_packet,
        "source_t555_route_residue": result.source_t555_route_residue,
        "source_t555_absorber_status": result.source_t555_absorber_status,
        "route_reset_status": result.route_reset_status,
        "reset_decisions": [
            {
                "option_id": decision.option_id,
                "outcome": decision.outcome,
                "selected": decision.selected,
                "role": decision.role,
                "missing_requirements": list(decision.missing_requirements),
                "reason": decision.reason,
                "next_packet": decision.next_packet,
            }
            for decision in result.reset_decisions
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
        "selected_reset_id": result.selected_reset_id,
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
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


def _reset_options() -> tuple[ResetOption, ...]:
    return (
        ResetOption(
            option_id=PARKED_ROUTE_ID,
            description=(
                "Park the absorbed Observerse protocol-stack route as audit "
                "translation residue and require a fresh-family TAF11 preflight."
            ),
            next_packet=NEXT_PACKET,
            fresh_source_family_named=False,
            absorbers_predeclared=False,
            source_variables_declared=False,
            falsifier_predeclared=False,
            continues_observerse_protocol_stack=False,
            treats_absorbed_route_as_source_law=False,
            parks_absorbed_route=True,
            keeps_audit_translation_value=True,
            computable_without_target_import=True,
            blocks_more_fixture_accumulation=True,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
        ),
        ResetOption(
            option_id="name_fresh_source_law_family_now",
            description=(
                "Select a new source-law family immediately from current context."
            ),
            next_packet="none",
            fresh_source_family_named=False,
            absorbers_predeclared=False,
            source_variables_declared=False,
            falsifier_predeclared=False,
            continues_observerse_protocol_stack=False,
            treats_absorbed_route_as_source_law=False,
            parks_absorbed_route=True,
            keeps_audit_translation_value=True,
            computable_without_target_import=False,
            blocks_more_fixture_accumulation=True,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
        ),
        ResetOption(
            option_id="extend_observerse_protocol_stack_with_more_fixtures",
            description=(
                "Continue T550-T555 by adding more bounded native fixtures."
            ),
            next_packet="none",
            fresh_source_family_named=False,
            absorbers_predeclared=False,
            source_variables_declared=False,
            falsifier_predeclared=False,
            continues_observerse_protocol_stack=True,
            treats_absorbed_route_as_source_law=True,
            parks_absorbed_route=False,
            keeps_audit_translation_value=False,
            computable_without_target_import=True,
            blocks_more_fixture_accumulation=False,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
        ),
        ResetOption(
            option_id="taf4_from_observerse_stack",
            description=(
                "Treat the protocol stack as finite-to-continuum or Lorentzian "
                "movement."
            ),
            next_packet="none",
            fresh_source_family_named=False,
            absorbers_predeclared=False,
            source_variables_declared=False,
            falsifier_predeclared=False,
            continues_observerse_protocol_stack=True,
            treats_absorbed_route_as_source_law=True,
            parks_absorbed_route=False,
            keeps_audit_translation_value=False,
            computable_without_target_import=False,
            blocks_more_fixture_accumulation=False,
            blocks_taf4_movement=False,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
        ),
        ResetOption(
            option_id="taf8_from_internal_stack",
            description=(
                "Treat the internal TAF11 stack as a cross-domain "
                "shadow-protection packet."
            ),
            next_packet="none",
            fresh_source_family_named=False,
            absorbers_predeclared=False,
            source_variables_declared=False,
            falsifier_predeclared=False,
            continues_observerse_protocol_stack=True,
            treats_absorbed_route_as_source_law=True,
            parks_absorbed_route=False,
            keeps_audit_translation_value=False,
            computable_without_target_import=True,
            blocks_more_fixture_accumulation=False,
            blocks_taf4_movement=True,
            blocks_taf8_execution=False,
            no_claim_canon_public_external_movement=True,
        ),
        ResetOption(
            option_id="claim_canon_public_posture_shortcut",
            description=(
                "Move claims, Canon Index, public posture, or external state "
                "from the route reset."
            ),
            next_packet="none",
            fresh_source_family_named=False,
            absorbers_predeclared=False,
            source_variables_declared=False,
            falsifier_predeclared=False,
            continues_observerse_protocol_stack=False,
            treats_absorbed_route_as_source_law=True,
            parks_absorbed_route=False,
            keeps_audit_translation_value=False,
            computable_without_target_import=False,
            blocks_more_fixture_accumulation=False,
            blocks_taf4_movement=False,
            blocks_taf8_execution=False,
            no_claim_canon_public_external_movement=False,
        ),
    )


def _evaluate_option(option: ResetOption) -> ResetDecision:
    missing = _missing_requirements(option)
    if not option.no_claim_canon_public_external_movement:
        outcome = "BLOCKED_GOVERNANCE"
        selected = False
        role = "forbidden"
        reason = "Route reset cannot move claims, canon, public posture, or external state."
        next_packet = "none"
    elif not option.blocks_taf4_movement:
        outcome = "BLOCKED_TAF4_OVERREAD"
        selected = False
        role = "blocked"
        reason = "An absorbed protocol-stack route is not a finite-to-continuum bridge."
        next_packet = "none"
    elif not option.blocks_taf8_execution:
        outcome = "BLOCKED_TAF8_OVERREAD"
        selected = False
        role = "blocked"
        reason = "Internal TAF11 absorber work is not a domain-native TAF8 packet."
        next_packet = "none"
    elif option.continues_observerse_protocol_stack:
        outcome = "REJECTED_ABSORBER_REPLAY"
        selected = False
        role = "retired_route"
        reason = "T555 absorbed the strong Observerse source-law reading."
        next_packet = "none"
    elif option.option_id == "name_fresh_source_law_family_now":
        outcome = "PAUSED_UNDERDECLARED_FRESH_FAMILY"
        selected = False
        role = "future_preflight"
        reason = (
            "No fresh source-law family, source variables, absorbers, and "
            "falsifier are declared in the current packet."
        )
        next_packet = "none"
    elif option.option_id == PARKED_ROUTE_ID and option.parks_absorbed_route:
        outcome = "SELECTED_ROUTE_RESET"
        selected = True
        role = "taf11_reset_state"
        reason = (
            "The Observerse protocol-stack route keeps audit translation value "
            "but cannot carry source-law status after absorber completion."
        )
        next_packet = option.next_packet
    elif missing:
        outcome = "REVIEW_ONLY_UNDERDECLARED"
        selected = False
        role = "underdeclared"
        reason = "The option lacks one or more post-absorber reset requirements."
        next_packet = "none"
    else:
        outcome = "REVIEW_ONLY_UNEXPECTED"
        selected = False
        role = "unexpected"
        reason = "The option was not selected by this route reset."
        next_packet = "none"

    return ResetDecision(
        option_id=option.option_id,
        outcome=outcome,
        selected=selected,
        role=role,
        missing_requirements=missing,
        reason=reason,
        next_packet=next_packet,
    )


def _missing_requirements(option: ResetOption) -> tuple[str, ...]:
    missing: list[str] = []
    if option.option_id == PARKED_ROUTE_ID:
        if not option.parks_absorbed_route:
            missing.append("parks_absorbed_route")
        if not option.keeps_audit_translation_value:
            missing.append("keeps_audit_translation_value")
        if not option.computable_without_target_import:
            missing.append("computable_without_target_import")
        if not option.blocks_more_fixture_accumulation:
            missing.append("blocks_more_fixture_accumulation")
        if not option.blocks_taf4_movement:
            missing.append("blocks_taf4_movement")
        if not option.blocks_taf8_execution:
            missing.append("blocks_taf8_execution")
        if not option.no_claim_canon_public_external_movement:
            missing.append("no_claim_canon_public_external_movement")
        return tuple(missing)

    if not option.fresh_source_family_named:
        missing.append("fresh_source_family_named")
    if not option.absorbers_predeclared:
        missing.append("absorbers_predeclared")
    if not option.source_variables_declared:
        missing.append("source_variables_declared")
    if not option.falsifier_predeclared:
        missing.append("falsifier_predeclared")
    if option.continues_observerse_protocol_stack:
        missing.append("does_not_continue_absorbed_observerse_stack")
    if option.treats_absorbed_route_as_source_law:
        missing.append("does_not_treat_absorbed_route_as_source_law")
    if not option.parks_absorbed_route:
        missing.append("parks_absorbed_route")
    if not option.computable_without_target_import:
        missing.append("computable_without_target_import")
    if not option.blocks_more_fixture_accumulation:
        missing.append("blocks_more_fixture_accumulation")
    if not option.blocks_taf4_movement:
        missing.append("blocks_taf4_movement")
    if not option.blocks_taf8_execution:
        missing.append("blocks_taf8_execution")
    if not option.no_claim_canon_public_external_movement:
        missing.append("no_claim_canon_public_external_movement")
    return tuple(missing)


def _gate_decisions(
    t555_result: t555.T555Result,
    decisions: tuple[ResetDecision, ...],
    selected: tuple[ResetDecision, ...],
) -> tuple[GateDecision, ...]:
    decision_by_id = {decision.option_id: decision for decision in decisions}
    gates = (
        (
            "t555_absorber_completion_authority",
            t555_result.verdict == t555.VERDICT
            and t555_result.selected_next_packet == t555.NEXT_PACKET
            and t555_result.route_residue == t555.ROUTE_RESIDUE,
            "T555 completed absorber separation and selected T556 route reset.",
            "T555 did not provide the expected absorber-completion authority.",
        ),
        (
            "fresh_family_not_ready_in_current_packet",
            decision_by_id["name_fresh_source_law_family_now"].outcome
            == "PAUSED_UNDERDECLARED_FRESH_FAMILY",
            "No fresh source-law family is declared strongly enough to run now.",
            "A fresh source-law family was selected without predeclared absorbers.",
        ),
        (
            "observerse_stack_extension_rejected",
            decision_by_id[
                "extend_observerse_protocol_stack_with_more_fixtures"
            ].outcome
            == "REJECTED_ABSORBER_REPLAY",
            "More bounded Observerse fixtures are rejected after absorber completion.",
            "The absorbed Observerse route was allowed to continue as source-law evidence.",
        ),
        (
            "parked_route_selected",
            len(selected) == 1
            and selected[0].option_id == PARKED_ROUTE_ID
            and selected[0].next_packet == NEXT_PACKET,
            "Exactly one route reset is selected: park Observerse and require fresh-family preflight.",
            "The route reset did not select the expected parking state.",
        ),
        (
            "taf4_taf8_boundaries_preserved",
            decision_by_id["taf4_from_observerse_stack"].outcome
            == "BLOCKED_TAF4_OVERREAD"
            and decision_by_id["taf8_from_internal_stack"].outcome
            == "BLOCKED_TAF8_OVERREAD",
            "TAF4 and TAF8 shortcuts are blocked.",
            "TAF4 or TAF8 moved from an internal absorbed route.",
        ),
        (
            "governance_boundaries_preserved",
            decision_by_id["claim_canon_public_posture_shortcut"].outcome
            == "BLOCKED_GOVERNANCE",
            "No claim, canon, public-posture, external, or cross-repo movement is attempted.",
            "A forbidden governance movement was allowed.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=pass_reason if passed else fail_reason,
        )
        for gate_id, passed, pass_reason, fail_reason in gates
    )


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="absorber_completion_control",
            blocks="Continuing T550-T555 as source-law evidence.",
            reason="T555 absorbed the strong Observerse reading once mature state and comparisons were granted.",
        ),
        HostileControl(
            control_id="more_fixture_accumulation_control",
            blocks="Adding more bounded native fixtures after absorption.",
            reason="More fixtures do not beat same-neighbor-data absorption.",
        ),
        HostileControl(
            control_id="fresh_family_underdeclaration_control",
            blocks="Naming a fresh source-law route without declared absorbers and falsifiers.",
            reason="A fresh family must be predeclared before any target reading.",
        ),
        HostileControl(
            control_id="taf4_taf8_shortcut_control",
            blocks="Moving TAF4 or executing TAF8 from an internal TAF11 route reset.",
            reason="Route reset is neither a finite-to-continuum bridge nor a cross-domain packet.",
        ),
        HostileControl(
            control_id="public_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet has no governance movement authority.",
        ),
    )


def _claim_labels(
    t555_result: t555.T555Result,
    decisions: tuple[ResetDecision, ...],
) -> tuple[ClaimLabel, ...]:
    parked = next(decision for decision in decisions if decision.option_id == PARKED_ROUTE_ID)
    fresh = next(
        decision
        for decision in decisions
        if decision.option_id == "name_fresh_source_law_family_now"
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T555 is consumed as absorber-completion authority: "
                f"{t555_result.verdict}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The Observerse protocol-stack route is parked with outcome "
                f"{parked.outcome} and next packet {parked.next_packet}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Immediate fresh-family selection pauses because "
                + ", ".join(fresh.missing_requirements[:4])
                + " are not declared in this packet."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The next honest TAF11 burden is a fresh-family preflight with "
                "absorbers and falsifiers declared before target outcomes are read."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T556 Results: Observerse Protocol-Stack Post-Absorber Route Reset Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Route reset status: `{payload['route_reset_status']}`",
        f"- Source T555 verdict: `{payload['source_t555_verdict']}`",
        f"- Source T555 selected next packet: `{payload['source_t555_selected_next_packet']}`",
        f"- Source T555 route residue: `{payload['source_t555_route_residue']}`",
        f"- Source T555 absorber status: `{payload['source_t555_absorber_status']}`",
        f"- Selected reset: `{payload['selected_reset_id']}`",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Reset Decisions",
        "",
        "| option | outcome | selected? | role | missing requirements | next packet | reason |",
        "| --- | --- | :---: | --- | --- | --- | --- |",
    ]
    for decision in payload["reset_decisions"]:
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['option_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected']} | "
            f"`{decision['role']}` | "
            f"{missing} | "
            f"`{decision['next_packet']}` | "
            f"{decision['reason']} |"
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


def write_results(result: T556Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t556_result_to_dict(result)
    json_path = (
        results_dir
        / "T556-observerse-protocol-stack-post-absorber-route-reset-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T556-observerse-protocol-stack-post-absorber-route-reset-gate-v0.1-results.md"
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

    result = run_t556_analysis()
    payload = t556_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
