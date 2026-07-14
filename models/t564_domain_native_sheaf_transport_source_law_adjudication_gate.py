"""T564: domain-native sheaf transport source-law adjudication gate.

T563 separated the minimal T559/T560/T561 bounded class from four mature
absorbers. T564 asks the stricter question: is that enough to call the route a
source law, or does the candidate still need an independent predictive holdout
and a typed generator before any claim, canon, TAF4, TAF8, S1, or public-posture
movement?
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t563_domain_native_sheaf_transport_absorber_separation_gate as t563


ARTIFACT = "T564-domain-native-sheaf-transport-source-law-adjudication-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_source_law_adjudication_requires_predictive_holdout"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_PREDICTIVE_HOLDOUT_REQUIRED"
ROUTE_STATUS = "bounded_absorber_separated_candidate_requires_holdout_review_only"
NEXT_PACKET = "t565_domain_native_sheaf_transport_predictive_holdout_gate"

EXPECTED_BOUNDED_CLASS = t563.EXPECTED_BOUNDED_CLASS
BLOCKING_BURDENS = (
    "independent_predictive_holdout",
    "typed_source_generator",
)

NOT_CLAIMED = (
    "T564 does not establish a source law, validate sheaf obstruction transport "
    "as a source family, prove shadow protection, derive spacetime, prove "
    "manifoldlikeness, repair T528, reverse T223, unpause S1, promote S1, "
    "change claim status, change Canon Index tiers, change canon verdicts, "
    "change public posture, change the North Star, authorize external "
    "publication, move TAF4, execute TAF8, or move cross-repo truth. It "
    "adjudicates the absorber-separated bounded class and requires a predictive "
    "holdout before source-law reading."
)


@dataclass(frozen=True)
class SourceLawBurden:
    burden_id: str
    status: str
    cleared: bool
    blocking: bool
    reason: str


@dataclass(frozen=True)
class RouteDecision:
    decision_id: str
    outcome: str
    selected: bool
    next_packet: str
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
class T564Result:
    artifact: str
    source_t563_verdict: str
    source_t563_selected_next_packet: str
    source_t563_bounded_class: tuple[str, ...]
    source_t563_absorber_status: str
    source_law_status: str
    route_status: str
    source_law_burdens: tuple[SourceLawBurden, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    source_law_earned: bool
    blocking_burdens: tuple[str, ...]
    selected_next_packet: str
    verdict: str
    source_law_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t564_analysis() -> T564Result:
    t563_result = t563.run_t563_analysis()
    burdens = _source_law_burdens(t563_result)
    source_law_earned = all(burden.cleared for burden in burdens)
    blocking_burdens = tuple(
        burden.burden_id for burden in burdens if burden.blocking and not burden.cleared
    )
    route_decisions = _route_decisions(source_law_earned, blocking_burdens)
    selected_next_packet = _selected_next_packet(route_decisions)
    gates = _gate_decisions(
        t563_result=t563_result,
        burdens=burdens,
        source_law_earned=source_law_earned,
        blocking_burdens=blocking_burdens,
        route_decisions=route_decisions,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if t563_result.verdict == t563.VERDICT
        and t563_result.selected_next_packet == t563.NEXT_PACKET
        and tuple(t563_result.source_t562_bounded_class) == EXPECTED_BOUNDED_CLASS
        and not source_law_earned
        and blocking_burdens == BLOCKING_BURDENS
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gates)
        else "domain_native_sheaf_transport_source_law_adjudication_unexpected_status"
    )

    return T564Result(
        artifact=ARTIFACT,
        source_t563_verdict=t563_result.verdict,
        source_t563_selected_next_packet=t563_result.selected_next_packet,
        source_t563_bounded_class=t563_result.source_t562_bounded_class,
        source_t563_absorber_status=t563_result.absorber_status,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        source_law_burdens=burdens,
        route_decisions=route_decisions,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        source_law_earned=source_law_earned,
        blocking_burdens=blocking_burdens,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T563 gives the sheaf transport route real review-grade pressure: "
            "the minimal bounded class remains separated from ordinary sheaf "
            "gluing, resource transport, consensus/state-machine, and "
            "record-provenance absorbers. That still does not establish a "
            "source law because the route has not predicted an independent "
            "holdout fixture and has not typed a generator that selects future "
            "cases without manual fixture design."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should freeze the T557-T564 family contract, "
            "predeclare an independent holdout shape before outcome reading, "
            "and test whether the same source variables and absorber boundaries "
            "predict the holdout without target labels, cross-repo truth, "
            "Observerse replay, APRD replay, TAF4 movement, TAF8 execution, S1 "
            "movement, claim-ledger movement, or public-posture movement."
        ),
        taf11_update=(
            "TAF11 remains active and narrowed. T564 rejects immediate "
            "source-law status, but it does not park the route: absorber "
            "separation is strong enough to require one predictive holdout gate."
        ),
        taf4_update=(
            "TAF4 remains blocked. Source-law adjudication over a bounded finite "
            "class is not a finite-to-continuum bridge, causal-set descent, "
            "Lorentzian target import, or manifoldlikeness result."
        ),
        taf8_update=(
            "TAF8 remains waiting. T564 is internal TAF11 adjudication, not a "
            "domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(burdens, blocking_burdens),
        claim_ledger_update=(
            "No claim-ledger update is earned. T564 adjudicates source-law "
            "burdens and selects a predictive holdout gate; it leaves claim rows, "
            "Canon Index tiers, canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t564_result_to_dict(result: T564Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t563_verdict": result.source_t563_verdict,
        "source_t563_selected_next_packet": result.source_t563_selected_next_packet,
        "source_t563_bounded_class": list(result.source_t563_bounded_class),
        "source_t563_absorber_status": result.source_t563_absorber_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "source_law_burdens": [
            {
                "burden_id": burden.burden_id,
                "status": burden.status,
                "cleared": burden.cleared,
                "blocking": burden.blocking,
                "reason": burden.reason,
            }
            for burden in result.source_law_burdens
        ],
        "route_decisions": [
            {
                "decision_id": decision.decision_id,
                "outcome": decision.outcome,
                "selected": decision.selected,
                "next_packet": decision.next_packet,
                "reason": decision.reason,
            }
            for decision in result.route_decisions
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
        "source_law_earned": result.source_law_earned,
        "blocking_burdens": list(result.blocking_burdens),
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "source_law_reading": result.source_law_reading,
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


def _source_law_burdens(result: t563.T563Result) -> tuple[SourceLawBurden, ...]:
    bounded_class = tuple(aggregate.fixture_id for aggregate in result.fixture_aggregates)
    all_fixture_separated = all(
        aggregate.all_absorbers_separated for aggregate in result.fixture_aggregates
    )
    all_absorber_controls = all(
        control.native_control_absorbed and control.matched
        for control in result.absorber_controls
    )
    all_absorbers_clean = all(
        aggregate.native_control_absorbed and aggregate.all_fixtures_separated
        for aggregate in result.absorber_aggregates
    )
    t563_authority = result.verdict == t563.VERDICT and result.selected_next_packet == t563.NEXT_PACKET

    return (
        SourceLawBurden(
            burden_id="t563_absorber_separation_authority",
            status="CLEARED",
            cleared=t563_authority,
            blocking=not t563_authority,
            reason=(
                "T563 completed absorber separation and selected T564."
                if t563_authority
                else "T563 did not provide the expected authority."
            ),
        ),
        SourceLawBurden(
            burden_id="minimal_bounded_class_preserved",
            status="CLEARED" if bounded_class == EXPECTED_BOUNDED_CLASS else "FAILED",
            cleared=bounded_class == EXPECTED_BOUNDED_CLASS,
            blocking=bounded_class != EXPECTED_BOUNDED_CLASS,
            reason=(
                "The T559/T560/T561 bounded class is preserved."
                if bounded_class == EXPECTED_BOUNDED_CLASS
                else "The bounded class drifted before source-law adjudication."
            ),
        ),
        SourceLawBurden(
            burden_id="absorber_separation_survives",
            status="CLEARED" if all_fixture_separated and all_absorbers_clean else "FAILED",
            cleared=all_fixture_separated and all_absorbers_clean,
            blocking=not (all_fixture_separated and all_absorbers_clean),
            reason=(
                "Every bounded fixture remains separated from every mature absorber."
                if all_fixture_separated and all_absorbers_clean
                else "At least one fixture or absorber failed the T563 separation screen."
            ),
        ),
        SourceLawBurden(
            burden_id="native_absorber_controls_still_absorb",
            status="CLEARED" if all_absorber_controls else "FAILED",
            cleared=all_absorber_controls,
            blocking=not all_absorber_controls,
            reason=(
                "Each mature absorber still absorbs its native positive-control case."
                if all_absorber_controls
                else "At least one mature absorber failed its native control."
            ),
        ),
        SourceLawBurden(
            burden_id="target_import_and_replay_controls",
            status="CLEARED",
            cleared=True,
            blocking=False,
            reason=(
                "T563 preserves controls against target labels, cross-repo truth, "
                "Observerse replay, APRD replay, relabel-only success, TAF4, and TAF8."
            ),
        ),
        SourceLawBurden(
            burden_id="independent_predictive_holdout",
            status="BLOCKED_HOLDOUT_NOT_RUN",
            cleared=False,
            blocking=True,
            reason=(
                "The bounded class contains three admitted fixtures, but T564 has "
                "not yet tested a predeclared independent holdout after the source "
                "variables and absorber boundaries were frozen."
            ),
        ),
        SourceLawBurden(
            burden_id="typed_source_generator",
            status="BLOCKED_GENERATOR_NOT_TYPED",
            cleared=False,
            blocking=True,
            reason=(
                "The route has a frozen family contract, but no typed generator "
                "yet selects future admissible cases without manual fixture design."
            ),
        ),
        SourceLawBurden(
            burden_id="governance_boundaries_preserved",
            status="CLEARED",
            cleared=True,
            blocking=False,
            reason=(
                "The adjudication makes no claim-ledger, Canon Index, canon, "
                "public-posture, North Star, external-publication, TAF4, TAF8, "
                "S1, or cross-repo movement."
            ),
        ),
    )


def _route_decisions(
    source_law_earned: bool,
    blocking_burdens: tuple[str, ...],
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_SOURCE_LAW_PROMOTION"
                if source_law_earned
                else "REJECTED_BURDEN_NOT_CLEARED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Every source-law burden cleared."
                if source_law_earned
                else "Source-law promotion is rejected because "
                + ", ".join(blocking_burdens)
                + " remain open."
            ),
        ),
        RouteDecision(
            decision_id="run_predictive_holdout_gate",
            outcome="SELECTED_NEXT_BURDEN",
            selected=not source_law_earned and blocking_burdens == BLOCKING_BURDENS,
            next_packet=NEXT_PACKET,
            reason=(
                "Absorber separation survives, so the next honest test is a "
                "predeclared predictive holdout rather than route reset or promotion."
            ),
        ),
        RouteDecision(
            decision_id="route_reset_now",
            outcome="PAUSED_CANDIDATE_NOT_ABSORBED",
            selected=False,
            next_packet="none",
            reason=(
                "Immediate route reset is premature because T563 separated the "
                "bounded class from every mature absorber."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t564",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="A bounded source-law adjudication is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t564",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 adjudication is not a cross-domain shadow-protection packet.",
        ),
        RouteDecision(
            decision_id="claim_canon_public_posture_shortcut",
            outcome="BLOCKED_GOVERNANCE",
            selected=False,
            next_packet="none",
            reason="The packet has no authority to move claim, canon, public posture, or external state.",
        ),
    )


def _selected_next_packet(decisions: tuple[RouteDecision, ...]) -> str:
    selected = tuple(decision for decision in decisions if decision.selected)
    if len(selected) != 1:
        return "none"
    return selected[0].next_packet


def _gate_decisions(
    t563_result: t563.T563Result,
    burdens: tuple[SourceLawBurden, ...],
    source_law_earned: bool,
    blocking_burdens: tuple[str, ...],
    route_decisions: tuple[RouteDecision, ...],
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    burdens_by_id = {burden.burden_id: burden for burden in burdens}
    decisions_by_id = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t563_authority",
            t563_result.verdict == t563.VERDICT
            and t563_result.selected_next_packet == t563.NEXT_PACKET,
            "T563 is consumed as absorber-separation authority.",
            "T563 did not provide the expected source state.",
        ),
        (
            "positive_burdens_cleared",
            all(
                burdens_by_id[burden_id].cleared
                for burden_id in (
                    "minimal_bounded_class_preserved",
                    "absorber_separation_survives",
                    "native_absorber_controls_still_absorb",
                    "target_import_and_replay_controls",
                    "governance_boundaries_preserved",
                )
            ),
            "The positive review burdens are cleared.",
            "At least one positive review burden failed.",
        ),
        (
            "source_law_rejected_until_holdout",
            not source_law_earned and blocking_burdens == BLOCKING_BURDENS,
            "Source-law status is rejected until holdout and generator burdens clear.",
            "Source-law status was promoted or rejected for the wrong reason.",
        ),
        (
            "predictive_holdout_selected",
            selected_next_packet == NEXT_PACKET
            and decisions_by_id["run_predictive_holdout_gate"].selected,
            "The next packet is the predictive holdout gate.",
            "The adjudication did not select the expected holdout gate.",
        ),
        (
            "taf4_taf8_boundaries_preserved",
            decisions_by_id["move_taf4_from_t564"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decisions_by_id["execute_taf8_from_t564"].outcome
            == "BLOCKED_TAF8_OVERREAD",
            "TAF4 and TAF8 shortcuts are blocked.",
            "TAF4 or TAF8 moved from internal TAF11 adjudication.",
        ),
        (
            "governance_boundaries_preserved",
            decisions_by_id["claim_canon_public_posture_shortcut"].outcome
            == "BLOCKED_GOVERNANCE",
            "No claim, canon, public-posture, external, S1, or cross-repo movement is attempted.",
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
            control_id="bounded_class_overread_control",
            blocks="Treating three admitted fixtures as a source law.",
            reason="Bounded absorber-separated evidence still needs an independent predictive holdout.",
        ),
        HostileControl(
            control_id="generator_underdeclaration_control",
            blocks="Calling the route a law without a typed case generator.",
            reason="The current family contract names variables, not an admissible-case generator.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks="Using target labels, Lorentzian structure, or cross-repo truth to make the holdout work.",
            reason="T564 preserves the T557-T563 target-blind boundary.",
        ),
        HostileControl(
            control_id="taf4_taf8_shortcut_control",
            blocks="Moving TAF4 or executing TAF8 from a bounded TAF11 adjudication.",
            reason="The packet is neither finite-to-continuum descent nor a cross-domain packet.",
        ),
        HostileControl(
            control_id="public_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet has no governance movement authority.",
        ),
    )


def _claim_labels(
    burdens: tuple[SourceLawBurden, ...],
    blocking_burdens: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    cleared = ", ".join(burden.burden_id for burden in burdens if burden.cleared)
    blocked = ", ".join(blocking_burdens)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The positive source-law review burdens cleared: {cleared}.",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text=f"Source-law status is not earned because these burdens remain open: {blocked}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Absorber separation is strong enough to justify a predictive "
                "holdout gate, but not strong enough for claim, canon, TAF4, "
                "TAF8, S1, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T564 Results: Domain-Native Sheaf Transport Source-Law Adjudication Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T563 verdict: `{payload['source_t563_verdict']}`",
        f"- Source T563 selected next packet: `{payload['source_t563_selected_next_packet']}`",
        "- Source T563 bounded class: "
        + ", ".join(f"`{item}`" for item in payload["source_t563_bounded_class"]),
        f"- Source law earned: {payload['source_law_earned']}",
        "- Blocking burdens: "
        + ", ".join(f"`{item}`" for item in payload["blocking_burdens"]),
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Source-Law Burdens",
        "",
        "| burden | status | cleared? | blocking? | reason |",
        "| --- | --- | :---: | :---: | --- |",
    ]
    for burden in payload["source_law_burdens"]:
        lines.append(
            "| "
            f"`{burden['burden_id']}` | "
            f"`{burden['status']}` | "
            f"{burden['cleared']} | "
            f"{burden['blocking']} | "
            f"{burden['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Route Decisions",
            "",
            "| decision | outcome | selected? | next packet | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for decision in payload["route_decisions"]:
        lines.append(
            "| "
            f"`{decision['decision_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected']} | "
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


def write_results(result: T564Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t564_result_to_dict(result)
    json_path = (
        results_dir
        / "T564-domain-native-sheaf-transport-source-law-adjudication-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T564-domain-native-sheaf-transport-source-law-adjudication-gate-v0.1-results.md"
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

    result = run_t564_analysis()
    payload = t564_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
