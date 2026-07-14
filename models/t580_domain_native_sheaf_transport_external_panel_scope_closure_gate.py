"""T580: external-panel scope closure for the TAF11 review package.

T579 applied out-of-panel absorber pressure to the T559-T578 candidate
package. This gate decides whether the current external panel can be closed as
enough for the package's limited review status, or whether unattended Progress
should keep expanding absorber panels before any stronger reading.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t579_domain_native_sheaf_transport_out_of_panel_absorber_probe_gate as t579,
)


ARTIFACT = "T580-domain-native-sheaf-transport-external-panel-scope-closure-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_external_panel_scope_closed_review_only"
SCOPE_STATUS = "EXTERNAL_PANEL_SCOPE_CLOSED_FOR_LIMITED_REVIEW"
PACKAGE_STATUS = "PACKAGE_PARKED_AS_LIMITED_REVIEW_TARGET"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_SCOPE_CLOSURE_IS_NOT_PROMOTION"
NEXT_PACKET = "t581_domain_native_sheaf_transport_review_package_closeout_router"

NOT_CLAIMED = (
    "T580 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, create detector evidence, or move cross-repo truth. "
    "It closes the current external-panel scope only for review-package "
    "discipline."
)


@dataclass(frozen=True)
class ScopeAxis:
    axis_id: str
    source: str
    covered_for_review: bool
    requires_immediate_expansion: bool
    stronger_reading_blocked: str
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ScopeDecision:
    decision_id: str
    outcome: str
    selected: bool
    reason: str
    next_packet: str = "none"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class GateDecision:
    gate_id: str
    outcome: str
    passed: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class T580Result:
    artifact: str
    source_t579_verdict: str
    source_t579_selected_next_packet: str
    scope_status: str
    package_status: str
    source_law_status: str
    scope_axes: tuple[ScopeAxis, ...]
    scope_decisions: tuple[ScopeDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    current_external_panel_closed: bool
    immediate_expansion_required: bool
    source_law_earned: bool
    selected_next_packet: str
    verdict: str
    scope_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t580_analysis() -> T580Result:
    source = t579.run_t579_analysis()
    axes = _scope_axes(source)
    immediate_expansion_required = any(axis.requires_immediate_expansion for axis in axes)
    current_external_panel_closed = (
        source.verdict == t579.VERDICT
        and source.selected_next_packet == t579.NEXT_PACKET
        and source.package_survives_as_limited_review
        and not immediate_expansion_required
    )
    source_law_earned = False
    decisions = _scope_decisions(
        current_external_panel_closed=current_external_panel_closed,
        immediate_expansion_required=immediate_expansion_required,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(decisions)
    gates = _gate_decisions(
        source=source,
        axes=axes,
        current_external_panel_closed=current_external_panel_closed,
        immediate_expansion_required=immediate_expansion_required,
        source_law_earned=source_law_earned,
        decisions=decisions,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if all(gate.passed for gate in gates)
        and selected_next_packet == NEXT_PACKET
        else "domain_native_sheaf_transport_external_panel_scope_unexpected_status"
    )

    return T580Result(
        artifact=ARTIFACT,
        source_t579_verdict=source.verdict,
        source_t579_selected_next_packet=source.selected_next_packet,
        scope_status=SCOPE_STATUS,
        package_status=PACKAGE_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        scope_axes=axes,
        scope_decisions=decisions,
        gate_decisions=gates,
        current_external_panel_closed=current_external_panel_closed,
        immediate_expansion_required=immediate_expansion_required,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        scope_reading=(
            "T580 closes the current external panel only for the review-package "
            "question. The T559-T579 route has faced internal route pressure, "
            "hostile search, blind-family pressure, and four out-of-panel "
            "absorber families. More panels would be useful only if a new "
            "domain-native packet, empirical manifest, continuum bridge, or "
            "cross-domain shadow-protection packet appears."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should route the limited TAF11 "
            "package into closeout discipline: preserve it as review material, "
            "name the reopen conditions, and prevent promotion by momentum."
        ),
        taf11_update=(
            "TAF11 remains open as a limited review target only. The current "
            "external panel is closed enough for no stronger unattended reading."
        ),
        taf4_update=(
            "TAF4 remains blocked. T580 treats continuum, causal-set, and "
            "measure-law questions as a separate future packet, not as an "
            "implicit consequence of the TAF11 package."
        ),
        taf8_update=(
            "TAF8 remains waiting. Access-structure pressure is absorber context, "
            "not a domain-native cross-domain shadow-protection theorem."
        ),
        claim_labels=_claim_labels(axes, current_external_panel_closed),
        claim_ledger_update=(
            "No claim-ledger update is earned. T580 is a review-scope closure "
            "gate; claim rows, Canon Index tiers, canon verdicts, and public "
            "posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t580_result_to_dict(result: T580Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t579_verdict": result.source_t579_verdict,
        "source_t579_selected_next_packet": result.source_t579_selected_next_packet,
        "scope_status": result.scope_status,
        "package_status": result.package_status,
        "source_law_status": result.source_law_status,
        "scope_axes": [axis.to_dict() for axis in result.scope_axes],
        "scope_decisions": [
            decision.to_dict() for decision in result.scope_decisions
        ],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "current_external_panel_closed": result.current_external_panel_closed,
        "immediate_expansion_required": result.immediate_expansion_required,
        "source_law_earned": result.source_law_earned,
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "scope_reading": result.scope_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [claim.to_dict() for claim in result.claim_labels],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _scope_axes(source: t579.T579Result) -> tuple[ScopeAxis, ...]:
    external_probe_ids = ", ".join(probe.probe_id for probe in source.external_probes)
    return (
        ScopeAxis(
            axis_id="internal_route_scope",
            source="T559-T578 internal panel plus T579 authority",
            covered_for_review=True,
            requires_immediate_expansion=False,
            stronger_reading_blocked="source-law status",
            reason=(
                "T559-T578 already supplied minimality, absorber separation, "
                "predictive, hostile, blind, and limitation pressure before T579."
            ),
        ),
        ScopeAxis(
            axis_id="external_absorber_scope",
            source=external_probe_ids,
            covered_for_review=True,
            requires_immediate_expansion=False,
            stronger_reading_blocked="source-law and downstream overread",
            reason=(
                "T579 applied four out-of-panel absorber families and every one "
                "absorbed stronger readings while leaving limited review value."
            ),
        ),
        ScopeAxis(
            axis_id="empirical_detector_scope",
            source="detector metrology and provenance probe",
            covered_for_review=True,
            requires_immediate_expansion=False,
            stronger_reading_blocked="empirical detector evidence",
            reason=(
                "Detector data remain gated on real manifests; more abstract "
                "detector probing would only repeat the same no-data boundary."
            ),
        ),
        ScopeAxis(
            axis_id="continuum_taf4_scope",
            source="causal-set measure-law probe",
            covered_for_review=True,
            requires_immediate_expansion=False,
            stronger_reading_blocked="TAF4 continuum bridge or S1 movement",
            reason=(
                "The measure-law probe blocks continuum overread; a true TAF4 "
                "move requires a separate finality-native continuum packet."
            ),
        ),
        ScopeAxis(
            axis_id="cross_domain_taf8_scope",
            source="quantum access-structure monogamy probe",
            covered_for_review=True,
            requires_immediate_expansion=False,
            stronger_reading_blocked="TAF8 theorem or shadow protection",
            reason=(
                "Access-structure pressure is absorber context only; a TAF8 move "
                "requires a domain-native cross-domain packet."
            ),
        ),
        ScopeAxis(
            axis_id="future_reopen_scope",
            source="new evidence only",
            covered_for_review=True,
            requires_immediate_expansion=False,
            stronger_reading_blocked="unbounded absorber-panel churn",
            reason=(
                "Unattended Progress should not keep inventing panels without a "
                "new packet, empirical manifest, continuum bridge, or cross-domain "
                "claim to test."
            ),
        ),
    )


def _scope_decisions(
    current_external_panel_closed: bool,
    immediate_expansion_required: bool,
    source_law_earned: bool,
) -> tuple[ScopeDecision, ...]:
    return (
        ScopeDecision(
            decision_id="close_current_external_panel_scope",
            outcome=(
                "SELECTED_SCOPE_CLOSURE"
                if current_external_panel_closed
                else "BLOCKED_SCOPE_STILL_OPEN"
            ),
            selected=current_external_panel_closed,
            reason=(
                "The current panel is closed for limited review-package use."
                if current_external_panel_closed
                else "The current panel still needs immediate expansion."
            ),
        ),
        ScopeDecision(
            decision_id="expand_absorber_panel_now",
            outcome=(
                "SELECTED_EXPANSION"
                if immediate_expansion_required
                else "BLOCKED_AS_CHURN_WITHOUT_NEW_PACKET"
            ),
            selected=immediate_expansion_required,
            reason=(
                "A live axis requires another panel."
                if immediate_expansion_required
                else "More panels would be speculative churn without a new packet or evidence source."
            ),
        ),
        ScopeDecision(
            decision_id="promote_taf11_source_law",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "BLOCKED_SCOPE_CLOSURE_IS_NOT_PROMOTION"
            ),
            selected=source_law_earned,
            reason=(
                "Source-law promotion was earned."
                if source_law_earned
                else "Closing review scope does not convert the package into source-law status."
            ),
        ),
        ScopeDecision(
            decision_id="route_to_review_package_closeout",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if current_external_panel_closed and not source_law_earned
                else "PAUSED_UNTIL_SCOPE_STATUS_CLEAR"
            ),
            selected=current_external_panel_closed and not source_law_earned,
            reason=(
                "The package needs closeout discipline and explicit reopen conditions."
                if current_external_panel_closed
                else "Closeout waits until scope status is clear."
            ),
            next_packet=NEXT_PACKET,
        ),
        ScopeDecision(
            decision_id="move_taf4_taf8_s1_or_cross_repo_truth",
            outcome="BLOCKED_GOVERNANCE",
            selected=False,
            reason=(
                "TAF4, TAF8, S1, claim, canon, public-posture, publication, "
                "and cross-repo movements stay outside this gate."
            ),
        ),
    )


def _selected_next_packet(decisions: tuple[ScopeDecision, ...]) -> str:
    next_packets = tuple(
        decision.next_packet
        for decision in decisions
        if decision.selected and decision.next_packet != "none"
    )
    if len(next_packets) != 1:
        return "none"
    return next_packets[0]


def _gate_decisions(
    source: t579.T579Result,
    axes: tuple[ScopeAxis, ...],
    current_external_panel_closed: bool,
    immediate_expansion_required: bool,
    source_law_earned: bool,
    decisions: tuple[ScopeDecision, ...],
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    decision_map = {decision.decision_id: decision for decision in decisions}
    all_axes_covered_for_review = all(axis.covered_for_review for axis in axes)
    all_stronger_readings_blocked = all(axis.stronger_reading_blocked for axis in axes)
    gates = (
        (
            "t579_authority",
            source.verdict == t579.VERDICT
            and source.selected_next_packet == t579.NEXT_PACKET
            and source.package_survives_as_limited_review
            and not source.source_law_earned,
            "T579 supplies scope-closure authority.",
            "T579 did not supply expected scope-closure authority.",
        ),
        (
            "review_scope_axes_declared",
            len(axes) == 6 and all_axes_covered_for_review,
            "All six review-scope axes are declared and covered for limited review.",
            "The review-scope axes are incomplete.",
        ),
        (
            "no_immediate_panel_expansion",
            not immediate_expansion_required
            and decision_map["expand_absorber_panel_now"].outcome
            == "BLOCKED_AS_CHURN_WITHOUT_NEW_PACKET",
            "No immediate panel expansion is selected without new evidence.",
            "The run selected more panel expansion without a new packet.",
        ),
        (
            "scope_closure_not_promotion",
            current_external_panel_closed
            and not source_law_earned
            and decision_map["promote_taf11_source_law"].outcome
            == "BLOCKED_SCOPE_CLOSURE_IS_NOT_PROMOTION",
            "Scope closure is separated from source-law promotion.",
            "Scope closure was allowed to act as source-law promotion.",
        ),
        (
            "closeout_router_selected",
            selected_next_packet == NEXT_PACKET
            and decision_map["route_to_review_package_closeout"].selected,
            "Review-package closeout router is selected as the next burden.",
            "The expected closeout router was not selected.",
        ),
        (
            "protected_movements_blocked",
            all_stronger_readings_blocked
            and decision_map["move_taf4_taf8_s1_or_cross_repo_truth"].outcome
            == "BLOCKED_GOVERNANCE",
            "Protected claim, canon, public, publication, TAF4, TAF8, S1, and cross-repo movements are blocked.",
            "A protected movement was not blocked.",
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


def _claim_labels(
    axes: tuple[ScopeAxis, ...],
    current_external_panel_closed: bool,
) -> tuple[ClaimLabel, ...]:
    axis_ids = ", ".join(axis.axis_id for axis in axes)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"External-panel scope axes evaluated: {axis_ids}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Current external panel is closed for limited review."
                if current_external_panel_closed
                else "Current external panel is not closed."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="Further absorber panels need a new packet or evidence source, not unattended churn.",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source law, claim, canon, public posture, TAF4, TAF8, S1, publication, and cross-repo movement remain blocked.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T580 Results: Domain-Native Sheaf Transport External-Panel Scope Closure Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Scope status: `{payload['scope_status']}`",
        f"- Package status: `{payload['package_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Source T579 verdict: `{payload['source_t579_verdict']}`",
        f"- Source T579 selected next packet: `{payload['source_t579_selected_next_packet']}`",
        f"- Current external panel closed: {payload['current_external_panel_closed']}",
        f"- Immediate expansion required: {payload['immediate_expansion_required']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Scope Axes",
        "",
        "| axis | source | covered for review? | immediate expansion? | stronger reading blocked | reason |",
        "| --- | --- | :---: | :---: | --- | --- |",
    ]
    for axis in payload["scope_axes"]:
        lines.append(
            "| "
            f"`{axis['axis_id']}` | "
            f"{axis['source']} | "
            f"{axis['covered_for_review']} | "
            f"{axis['requires_immediate_expansion']} | "
            f"{axis['stronger_reading_blocked']} | "
            f"{axis['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Scope Decisions",
            "",
            "| decision | outcome | selected? | next packet | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for decision in payload["scope_decisions"]:
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
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Scope Reading", "scope_reading"),
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


def write_results(result: T580Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t580_result_to_dict(result)
    json_path = (
        results_dir
        / "T580-domain-native-sheaf-transport-external-panel-scope-closure-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T580-domain-native-sheaf-transport-external-panel-scope-closure-gate-v0.1-results.md"
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

    result = run_t580_analysis()
    payload = t580_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
