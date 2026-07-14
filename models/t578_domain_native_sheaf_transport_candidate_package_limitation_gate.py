"""T578: limitation gate for the TAF11 source-law candidate package.

T577 allowed the T559-T576 route to be bundled only as a firewalled internal
candidate package. T578 stress-tests that package's limitations before any
stronger source-law reading. The result keeps the package useful as review
material, but blocks promotion by inertia and selects an out-of-panel absorber
probe as the next burden.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t577_domain_native_sheaf_transport_source_law_firebreak_gate as t577,
)


ARTIFACT = (
    "T578-domain-native-sheaf-transport-candidate-package-limitation-gate-v0.1"
)
VERDICT = "domain_native_sheaf_transport_candidate_package_limited_review_only"
LIMITATION_STATUS = "CANDIDATE_PACKAGE_LIMITED_REVIEW_ONLY"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_LIMITATIONS_LOAD_BEARING"
NEXT_PACKET = "t579_domain_native_sheaf_transport_out_of_panel_absorber_probe_gate"

NOT_CLAIMED = (
    "T578 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It keeps the T559-T577 "
    "candidate package as review-only and requires an out-of-panel absorber "
    "probe before any stronger reading."
)


@dataclass(frozen=True)
class LimitationAxis:
    axis_id: str
    exposed: bool
    evidence: tuple[str, ...]
    limits_to: str
    next_pressure: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["evidence"] = list(self.evidence)
        return data


@dataclass(frozen=True)
class PackagePressure:
    pressure_id: str
    outcome: str
    passed: bool
    evidence: tuple[str, ...]
    reason: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["evidence"] = list(self.evidence)
        return data


@dataclass(frozen=True)
class RouteDecision:
    decision_id: str
    outcome: str
    selected: bool
    next_packet: str
    reason: str

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
class T578Result:
    artifact: str
    source_t577_verdict: str
    source_t577_selected_next_packet: str
    source_package_label: str
    limitation_status: str
    source_law_status: str
    limitation_axes: tuple[LimitationAxis, ...]
    package_pressures: tuple[PackagePressure, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    package_remains_review_only: bool
    source_law_earned: bool
    selected_next_packet: str
    verdict: str
    limitation_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t578_analysis() -> T578Result:
    source = t577.run_t577_analysis()
    axes = _limitation_axes(source)
    pressures = _package_pressures(source=source, axes=axes)
    package_remains_review_only = all(axis.exposed for axis in axes) and all(
        pressure.passed for pressure in pressures
    )
    source_law_earned = False
    route_decisions = _route_decisions(
        package_remains_review_only=package_remains_review_only,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        source=source,
        axes=axes,
        pressures=pressures,
        route_decisions=route_decisions,
        package_remains_review_only=package_remains_review_only,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if package_remains_review_only
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_candidate_package_limitation_unexpected_status"
    )

    return T578Result(
        artifact=ARTIFACT,
        source_t577_verdict=source.verdict,
        source_t577_selected_next_packet=source.selected_next_packet,
        source_package_label=source.package_label,
        limitation_status=LIMITATION_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        limitation_axes=axes,
        package_pressures=pressures,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        package_remains_review_only=package_remains_review_only,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        limitation_reading=(
            "T578 keeps the T559-T577 candidate package useful only as an "
            "internal review object. The package is finite, route-internal, "
            "limited to the declared absorber and hostile panels, and lacks a "
            "downstream bridge to TAF4, TAF8, S1, claim, canon, public-posture, "
            "publication, or cross-repo movement."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should add an out-of-panel "
            "absorber or adversarial family and ask whether the package still "
            "survives without relying only on the T559-T577 internal panel."
        ),
        taf11_update=(
            "TAF11 remains the top active lane, but T578 narrows the candidate "
            "package to review-only status and selects an out-of-panel absorber "
            "probe before any stronger source-law reading."
        ),
        taf4_update=(
            "TAF4 remains blocked. T578 exposes that the candidate package has "
            "no finite-to-continuum, causal-set, Lorentzian, or manifoldlikeness "
            "bridge."
        ),
        taf8_update=(
            "TAF8 remains waiting. T578 is an internal TAF11 limitation gate, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(axes, pressures, package_remains_review_only),
        claim_ledger_update=(
            "No claim-ledger update is earned. T578 records limitations on a "
            "review-only candidate package; claim rows, Canon Index tiers, "
            "canon verdicts, and public posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t578_result_to_dict(result: T578Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t577_verdict": result.source_t577_verdict,
        "source_t577_selected_next_packet": result.source_t577_selected_next_packet,
        "source_package_label": result.source_package_label,
        "limitation_status": result.limitation_status,
        "source_law_status": result.source_law_status,
        "limitation_axes": [axis.to_dict() for axis in result.limitation_axes],
        "package_pressures": [
            pressure.to_dict() for pressure in result.package_pressures
        ],
        "route_decisions": [decision.to_dict() for decision in result.route_decisions],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "package_remains_review_only": result.package_remains_review_only,
        "source_law_earned": result.source_law_earned,
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "limitation_reading": result.limitation_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [claim.to_dict() for claim in result.claim_labels],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _limitation_axes(source: t577.T577Result) -> tuple[LimitationAxis, ...]:
    decisions = {decision.decision_id: decision for decision in source.route_decisions}
    boundaries = {boundary.boundary_id: boundary for boundary in source.package_boundaries}
    return (
        LimitationAxis(
            axis_id="finite_synthetic_scope",
            exposed=source.candidate_packaging_allowed and not source.source_law_earned,
            evidence=(
                source.package_label,
                "T559-T576 internal review route",
                boundaries["content_firewall"].required_label,
            ),
            limits_to="finite synthetic review package, not a general source law",
            next_pressure="test an out-of-panel absorber or family",
        ),
        LimitationAxis(
            axis_id="route_internality",
            exposed=True,
            evidence=(
                "bounded class",
                "same TAF11 sheaf-transport route chain",
                "candidate package rather than independent theorem",
            ),
            limits_to="same-route evidence aggregation",
            next_pressure="seek pressure outside the T559-T577 route chain",
        ),
        LimitationAxis(
            axis_id="absorber_panel_incompleteness",
            exposed=boundaries["content_firewall"].satisfied,
            evidence=(
                "ordinary sheaf gluing",
                "resource transport",
                "consensus/state-machine",
                "record provenance",
                "declared hostile panel",
            ),
            limits_to="declared absorber and hostile panels only",
            next_pressure="add an out-of-panel absorber or adversarial frame",
        ),
        LimitationAxis(
            axis_id="downstream_bridge_absence",
            exposed=(
                decisions["move_taf4_from_t577"].outcome == "BLOCKED_TAF4_OVERREAD"
                and decisions["execute_taf8_from_t577"].outcome
                == "BLOCKED_TAF8_OVERREAD"
                and decisions["move_s1_or_cross_repo_truth"].outcome
                == "BLOCKED_GOVERNANCE"
            ),
            evidence=(
                "TAF4 blocked",
                "TAF8 blocked",
                "S1 and cross-repo movement blocked",
            ),
            limits_to="no downstream bridge or governance movement",
            next_pressure="earn any downstream bridge in a separate packet",
        ),
        LimitationAxis(
            axis_id="label_status_gap",
            exposed=source.package_label == t577.PACKAGE_LABEL,
            evidence=(
                source.package_label,
                source.source_law_status,
                "review-only candidate label",
            ),
            limits_to="candidate label only, not public status",
            next_pressure="keep the firebreak until a new burden is earned",
        ),
    )


def _package_pressures(
    source: t577.T577Result,
    axes: tuple[LimitationAxis, ...],
) -> tuple[PackagePressure, ...]:
    exposed_axes = tuple(axis.axis_id for axis in axes if axis.exposed)
    return (
        PackagePressure(
            pressure_id="source_law_promotion_pressure",
            outcome="BLOCKED_BY_LIMITATIONS",
            passed=source.candidate_packaging_allowed and len(exposed_axes) == len(axes),
            evidence=exposed_axes,
            reason="Every limitation axis remains load-bearing.",
        ),
        PackagePressure(
            pressure_id="claim_canon_public_posture_pressure",
            outcome="BLOCKED_BY_GOVERNANCE_FIREWALL",
            passed=True,
            evidence=("claim ledger unchanged", "canon unchanged", "public posture unchanged"),
            reason="The candidate package supplies no governed status movement.",
        ),
        PackagePressure(
            pressure_id="downstream_lane_pressure",
            outcome="BLOCKED_BY_NO_BRIDGE",
            passed=True,
            evidence=("TAF4 waiting", "TAF8 waiting", "S1 waiting"),
            reason="The package does not contain a downstream bridge.",
        ),
        PackagePressure(
            pressure_id="review_package_retention_pressure",
            outcome="RETAINED_AS_LIMITED_REVIEW_TARGET",
            passed=source.package_label == t577.PACKAGE_LABEL,
            evidence=(source.package_label, LIMITATION_STATUS),
            reason="The package remains useful as a bounded review target.",
        ),
    )


def _route_decisions(
    package_remains_review_only: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_from_package",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "BLOCKED_LIMITATIONS_LOAD_BEARING"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "The limitation gate finds the review package too limited for source-law status."
            ),
        ),
        RouteDecision(
            decision_id="retain_candidate_package",
            outcome=(
                "SELECTED_REVIEW_ONLY_RETENTION"
                if package_remains_review_only
                else "BLOCKED_PACKAGE_NOT_STABLE"
            ),
            selected=package_remains_review_only,
            next_packet="none",
            reason=(
                "The package remains useful as a bounded internal review object."
                if package_remains_review_only
                else "The package failed its limitation gate."
            ),
        ),
        RouteDecision(
            decision_id="run_out_of_panel_absorber_probe",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if package_remains_review_only and not source_law_earned
                else "PAUSED_UNTIL_LIMITATION_STATUS_CLEAR"
            ),
            selected=package_remains_review_only and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The next honest pressure is outside the existing absorber and hostile panels."
                if package_remains_review_only
                else "No next probe selected until limitation status is clear."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t578",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Limitation exposure is not continuum descent or target-spacetime recovery.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t578",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="The limitation gate is not a cross-domain shadow-protection theorem packet.",
        ),
        RouteDecision(
            decision_id="move_s1_or_cross_repo_truth",
            outcome="BLOCKED_GOVERNANCE",
            selected=False,
            next_packet="none",
            reason="No S1, cross-repo, publication, claim, canon, or public-posture movement is authorized.",
        ),
    )


def _selected_next_packet(decisions: tuple[RouteDecision, ...]) -> str:
    next_packets = tuple(
        decision.next_packet
        for decision in decisions
        if decision.selected and decision.next_packet != "none"
    )
    if len(next_packets) != 1:
        return "none"
    return next_packets[0]


def _gate_decisions(
    source: t577.T577Result,
    axes: tuple[LimitationAxis, ...],
    pressures: tuple[PackagePressure, ...],
    route_decisions: tuple[RouteDecision, ...],
    package_remains_review_only: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    decisions = {decision.decision_id: decision for decision in route_decisions}
    all_axes_exposed = all(axis.exposed for axis in axes)
    all_pressures_pass = all(pressure.passed for pressure in pressures)
    gates = (
        (
            "t577_authority",
            source.verdict == t577.VERDICT
            and source.selected_next_packet == t577.NEXT_PACKET
            and source.package_label == t577.PACKAGE_LABEL,
            "T577 supplies candidate-package limitation authority.",
            "T577 did not supply candidate-package limitation authority.",
        ),
        (
            "limitation_axes_exposed",
            all_axes_exposed,
            "Every declared limitation axis is exposed.",
            "One or more limitation axes failed to expose.",
        ),
        (
            "package_pressures_resisted",
            all_pressures_pass,
            "Every promotion or downstream pressure is resisted.",
            "One or more package pressures escaped the limitation gate.",
        ),
        (
            "package_remains_review_only",
            package_remains_review_only
            and not source_law_earned
            and decisions["retain_candidate_package"].selected
            and decisions["promote_source_law_from_package"].outcome
            == "BLOCKED_LIMITATIONS_LOAD_BEARING",
            "The package remains review-only and source-law promotion stays blocked.",
            "The package moved too far or was not retained as review-only.",
        ),
        (
            "out_of_panel_absorber_probe_selected",
            selected_next_packet == NEXT_PACKET
            and decisions["run_out_of_panel_absorber_probe"].selected,
            "The out-of-panel absorber probe is selected as the next burden.",
            "The expected out-of-panel absorber probe was not selected.",
        ),
        (
            "protected_boundaries_preserved",
            decisions["move_taf4_from_t578"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decisions["execute_taf8_from_t578"].outcome == "BLOCKED_TAF8_OVERREAD"
            and decisions["move_s1_or_cross_repo_truth"].outcome == "BLOCKED_GOVERNANCE",
            "TAF4, TAF8, S1, cross-repo, publication, claim, canon, and public-posture shortcuts are blocked.",
            "A protected movement was allowed.",
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
    axes: tuple[LimitationAxis, ...],
    pressures: tuple[PackagePressure, ...],
    package_remains_review_only: bool,
) -> tuple[ClaimLabel, ...]:
    exposed_axes = tuple(axis.axis_id for axis in axes if axis.exposed)
    resisted_pressures = tuple(
        pressure.pressure_id for pressure in pressures if pressure.passed
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Limitation axes exposed: " + ", ".join(exposed_axes) + ".",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Package pressures resisted: " + ", ".join(resisted_pressures) + ".",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The candidate package remains useful only as review material."
                if package_remains_review_only
                else "The candidate package is not retained."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law promotion and downstream movement remain blocked.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T578 Results: Domain-Native Sheaf Transport Candidate Package Limitation Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Limitation status: `{payload['limitation_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Source package label: `{payload['source_package_label']}`",
        f"- Source T577 verdict: `{payload['source_t577_verdict']}`",
        f"- Source T577 selected next packet: `{payload['source_t577_selected_next_packet']}`",
        f"- Package remains review-only: {payload['package_remains_review_only']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Limitation Axes",
        "",
        "| axis | exposed? | evidence | limits to | next pressure |",
        "| --- | :---: | --- | --- | --- |",
    ]
    for axis in payload["limitation_axes"]:
        evidence = ", ".join(f"`{item}`" for item in axis["evidence"])
        lines.append(
            "| "
            f"`{axis['axis_id']}` | "
            f"{axis['exposed']} | "
            f"{evidence} | "
            f"{axis['limits_to']} | "
            f"{axis['next_pressure']} |"
        )
    lines.extend(
        [
            "",
            "## Package Pressures",
            "",
            "| pressure | outcome | passed? | evidence | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for pressure in payload["package_pressures"]:
        evidence = ", ".join(f"`{item}`" for item in pressure["evidence"])
        lines.append(
            "| "
            f"`{pressure['pressure_id']}` | "
            f"`{pressure['outcome']}` | "
            f"{pressure['passed']} | "
            f"{evidence} | "
            f"{pressure['reason']} |"
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
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Limitation Reading", "limitation_reading"),
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


def write_results(result: T578Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t578_result_to_dict(result)
    json_path = (
        results_dir
        / "T578-domain-native-sheaf-transport-candidate-package-limitation-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T578-domain-native-sheaf-transport-candidate-package-limitation-gate-v0.1-results.md"
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

    result = run_t578_analysis()
    payload = t578_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
