"""T577: source-law firebreak for the TAF11 semantic generator route.

T576 closed the declared finite hostile-search scope as review-only and
selected a firebreak before any stronger source-law reading. T577 decides
whether the T559-T576 route may be packaged as an internal source-law candidate
without promotion by inertia. The answer is yes, but only as a review-only
candidate package with explicit limits and a next limitation gate.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t576_domain_native_sheaf_transport_hostile_search_scope_closure_gate as t576,
)


ARTIFACT = "T577-domain-native-sheaf-transport-source-law-firebreak-gate-v0.1"
VERDICT = (
    "domain_native_sheaf_transport_source_law_firebreak_allows_candidate_package_review_only"
)
FIREBREAK_STATUS = "INTERNAL_CANDIDATE_PACKAGE_ALLOWED_REVIEW_ONLY"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_CANDIDATE_PACKAGE_FIREWALLED"
PACKAGE_LABEL = "taf11_source_law_candidate_package_review_only"
NEXT_PACKET = "t578_domain_native_sheaf_transport_candidate_package_limitation_gate"

NOT_CLAIMED = (
    "T577 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It allows only an internal "
    "review candidate package and requires a limitation gate before any "
    "stronger reading."
)


@dataclass(frozen=True)
class FirebreakCriterion:
    criterion_id: str
    passed: bool
    evidence: tuple[str, ...]
    package_effect: str
    residual_risk: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["evidence"] = list(self.evidence)
        return data


@dataclass(frozen=True)
class PackageBoundary:
    boundary_id: str
    satisfied: bool
    required_label: str
    protects: tuple[str, ...]
    reason: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["protects"] = list(self.protects)
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
class T577Result:
    artifact: str
    source_t576_verdict: str
    source_t576_selected_next_packet: str
    firebreak_status: str
    source_law_status: str
    package_label: str
    firebreak_criteria: tuple[FirebreakCriterion, ...]
    package_boundaries: tuple[PackageBoundary, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    candidate_packaging_allowed: bool
    source_law_earned: bool
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


def run_t577_analysis() -> T577Result:
    source = t576.run_t576_analysis()
    criteria = _firebreak_criteria(source)
    boundaries = _package_boundaries()
    candidate_packaging_allowed = all(item.passed for item in criteria) and all(
        item.satisfied for item in boundaries
    )
    source_law_earned = False
    route_decisions = _route_decisions(
        candidate_packaging_allowed=candidate_packaging_allowed,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        source=source,
        criteria=criteria,
        boundaries=boundaries,
        route_decisions=route_decisions,
        candidate_packaging_allowed=candidate_packaging_allowed,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if candidate_packaging_allowed
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_source_law_firebreak_unexpected_status"
    )

    return T577Result(
        artifact=ARTIFACT,
        source_t576_verdict=source.verdict,
        source_t576_selected_next_packet=source.selected_next_packet,
        firebreak_status=FIREBREAK_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        package_label=PACKAGE_LABEL if candidate_packaging_allowed else "none",
        firebreak_criteria=criteria,
        package_boundaries=boundaries,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        candidate_packaging_allowed=candidate_packaging_allowed,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T577 allows the T559-T576 route to be bundled only as an internal "
            "review candidate package. The package may collect the bounded "
            "class, absorber separation, predictive holdout, typed generator, "
            "semantic strengthening, independent reimplementation, fresh-family "
            "stress, falsifier rotation, blind/adversarial holdouts, hostile "
            "search, and hostile-scope closure. That package is not a public "
            "source law and does not move claims, canon, public posture, TAF4, "
            "TAF8, S1, publication, or cross-repo truth."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should stress the candidate "
            "package's limitations, especially whether its finite synthetic "
            "scope, absorber list, and internal-family evidence are enough for "
            "anything stronger than review packaging."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. T577 permits a firewalled "
            "review-only candidate package and selects a limitation gate, not "
            "source-law promotion."
        ),
        taf4_update=(
            "TAF4 remains blocked. A review-only candidate package is not "
            "finite-to-continuum descent, causal-set recovery, Lorentzian "
            "target import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T577 packages internal TAF11 evidence; it is "
            "not a domain-native cross-domain shadow-protection theorem packet."
        ),
        claim_labels=_claim_labels(criteria, boundaries, candidate_packaging_allowed),
        claim_ledger_update=(
            "No claim-ledger update is earned. T577 allows only a firewalled "
            "internal candidate package and selects a limitation gate; claim "
            "rows, Canon Index tiers, canon verdicts, and public posture remain "
            "unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t577_result_to_dict(result: T577Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t576_verdict": result.source_t576_verdict,
        "source_t576_selected_next_packet": result.source_t576_selected_next_packet,
        "firebreak_status": result.firebreak_status,
        "source_law_status": result.source_law_status,
        "package_label": result.package_label,
        "firebreak_criteria": [
            criterion.to_dict() for criterion in result.firebreak_criteria
        ],
        "package_boundaries": [
            boundary.to_dict() for boundary in result.package_boundaries
        ],
        "route_decisions": [decision.to_dict() for decision in result.route_decisions],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "candidate_packaging_allowed": result.candidate_packaging_allowed,
        "source_law_earned": result.source_law_earned,
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "source_law_reading": result.source_law_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [claim.to_dict() for claim in result.claim_labels],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _firebreak_criteria(source: t576.T576Result) -> tuple[FirebreakCriterion, ...]:
    source_decisions = {decision.decision_id: decision for decision in source.route_decisions}
    return (
        FirebreakCriterion(
            criterion_id="t576_authority",
            passed=(
                source.verdict == t576.VERDICT
                and source.selected_next_packet == t576.NEXT_PACKET
                and source.finite_scope_closed
                and not source.source_law_earned
            ),
            evidence=(source.verdict, source.selected_next_packet),
            package_effect="Supplies firebreak authority without promotion.",
            residual_risk="T576 closed a finite hostile scope, not all future mathematics.",
        ),
        FirebreakCriterion(
            criterion_id="route_chain_packageable",
            passed=source.route_kept_open and source.finite_scope_closed,
            evidence=(
                "T559-T564 bounded class and absorber separation",
                "T565-T566 predictive holdout and typed generator",
                "T567-T568 hostile review and semantic strengthening",
                "T569-T570 independent reimplementation and fresh-family stress",
                "T571-T573 rotation, blind, and adversarial holdouts",
                "T574-T576 adjudication, hostile search, and scope closure",
            ),
            package_effect="Allows a compact internal evidence package.",
            residual_risk="Packageable evidence is still review-only.",
        ),
        FirebreakCriterion(
            criterion_id="hostile_pressure_complete_for_declared_scope",
            passed=(
                source.hostile_search_completed
                and not source.true_counterfamily_found
                and not source.route_breaks
            ),
            evidence=(
                "hostile_search_completed",
                "no_true_counterfamily_found",
                "route_does_not_break",
            ),
            package_effect="Prevents repeating T575/T576 before packaging.",
            residual_risk="No-counterfamily-in-panel is not a general theorem.",
        ),
        FirebreakCriterion(
            criterion_id="promotion_firebreak_needed",
            passed=source_decisions["promote_source_law_now"].outcome
            == "BLOCKED_FIREBREAK_REQUIRED",
            evidence=(source.source_law_status, "promotion_blocked_by_t576"),
            package_effect="Requires candidate packaging to carry a non-promotion label.",
            residual_risk="Readers could overread the package without explicit labels.",
        ),
        FirebreakCriterion(
            criterion_id="protected_boundaries_still_blocked",
            passed=(
                source_decisions["move_taf4_from_scope_closure"].outcome
                == "BLOCKED_TAF4_OVERREAD"
                and source_decisions["execute_taf8_from_scope_closure"].outcome
                == "BLOCKED_TAF8_OVERREAD"
                and source_decisions["move_s1_or_cross_repo_truth"].outcome
                == "BLOCKED_GOVERNANCE"
            ),
            evidence=(
                "taf4_blocked",
                "taf8_blocked",
                "s1_cross_repo_publication_claim_canon_blocked",
            ),
            package_effect="Keeps downstream movement outside the package.",
            residual_risk="A later packet must earn any downstream motion separately.",
        ),
    )


def _package_boundaries() -> tuple[PackageBoundary, ...]:
    protected_governance = (
        "claim_ledger",
        "canon_index",
        "canon_verdict",
        "public_posture",
        "north_star",
    )
    downstream = ("TAF4", "TAF8", "S1", "external_publication", "cross_repo_truth")
    return (
        PackageBoundary(
            boundary_id="label_firewall",
            satisfied=True,
            required_label=PACKAGE_LABEL,
            protects=("source_law_status",),
            reason="The package must say candidate and review-only in the label.",
        ),
        PackageBoundary(
            boundary_id="content_firewall",
            satisfied=True,
            required_label="evidence_summary_plus_residual_risks",
            protects=("scope_overread", "absorber_overread", "finite_panel_overread"),
            reason="The package may summarize evidence only with residual risks attached.",
        ),
        PackageBoundary(
            boundary_id="governance_firewall",
            satisfied=True,
            required_label="no_claim_or_canon_movement",
            protects=protected_governance,
            reason="Candidate packaging cannot edit protected governance surfaces.",
        ),
        PackageBoundary(
            boundary_id="downstream_firewall",
            satisfied=True,
            required_label="no_taf4_taf8_s1_publication_or_cross_repo_movement",
            protects=downstream,
            reason="Downstream lanes remain waiting for separately earned packets.",
        ),
        PackageBoundary(
            boundary_id="next_burden_firewall",
            satisfied=True,
            required_label=NEXT_PACKET,
            protects=("promotion_by_inertia",),
            reason="The next move must test package limitations before stronger readings.",
        ),
    )


def _route_decisions(
    candidate_packaging_allowed: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "BLOCKED_CANDIDATE_PACKAGE_ONLY"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "The firebreak allows candidate packaging only, not source-law status."
            ),
        ),
        RouteDecision(
            decision_id="allow_internal_candidate_package",
            outcome=(
                "SELECTED_REVIEW_ONLY_PACKAGE"
                if candidate_packaging_allowed
                else "BLOCKED_PACKAGE_CRITERIA_NOT_MET"
            ),
            selected=candidate_packaging_allowed,
            next_packet="none",
            reason=(
                "The T559-T576 route can be bundled as a firewalled internal candidate package."
                if candidate_packaging_allowed
                else "Package criteria did not pass."
            ),
        ),
        RouteDecision(
            decision_id="run_candidate_package_limitation_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if candidate_packaging_allowed and not source_law_earned
                else "PAUSED_UNTIL_PACKAGE_ALLOWED"
            ),
            selected=candidate_packaging_allowed and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "After candidate packaging, the next honest burden is a limitation gate."
                if candidate_packaging_allowed
                else "The limitation gate waits for an allowed candidate package."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t577",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Candidate packaging is not continuum descent or target-spacetime recovery.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t577",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 candidate packaging is not cross-domain shadow protection.",
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
    source: t576.T576Result,
    criteria: tuple[FirebreakCriterion, ...],
    boundaries: tuple[PackageBoundary, ...],
    route_decisions: tuple[RouteDecision, ...],
    candidate_packaging_allowed: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    criteria_by_id = {criterion.criterion_id: criterion for criterion in criteria}
    decisions = {decision.decision_id: decision for decision in route_decisions}
    all_criteria_pass = all(criterion.passed for criterion in criteria)
    all_boundaries_satisfied = all(boundary.satisfied for boundary in boundaries)
    gates = (
        (
            "t576_authority",
            criteria_by_id["t576_authority"].passed
            and source.selected_next_packet == t576.NEXT_PACKET,
            "T576 supplies source-law firebreak authority.",
            "T576 did not supply source-law firebreak authority.",
        ),
        (
            "firebreak_criteria_pass",
            all_criteria_pass,
            "Every firebreak criterion passed.",
            "One or more firebreak criteria failed.",
        ),
        (
            "package_boundaries_satisfied",
            all_boundaries_satisfied,
            "Every candidate-package boundary is satisfied.",
            "One or more candidate-package boundaries failed.",
        ),
        (
            "candidate_package_allowed_without_promotion",
            candidate_packaging_allowed
            and not source_law_earned
            and decisions["allow_internal_candidate_package"].selected
            and decisions["promote_source_law_now"].outcome
            == "BLOCKED_CANDIDATE_PACKAGE_ONLY",
            "Candidate packaging is allowed while source-law promotion stays blocked.",
            "Packaging moved too far or promotion was not blocked.",
        ),
        (
            "limitation_gate_selected_next",
            selected_next_packet == NEXT_PACKET
            and decisions["run_candidate_package_limitation_gate"].selected,
            "Candidate-package limitation gate is selected as the next burden.",
            "The expected limitation-gate next packet was not selected.",
        ),
        (
            "protected_boundaries_preserved",
            decisions["move_taf4_from_t577"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decisions["execute_taf8_from_t577"].outcome == "BLOCKED_TAF8_OVERREAD"
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
    criteria: tuple[FirebreakCriterion, ...],
    boundaries: tuple[PackageBoundary, ...],
    candidate_packaging_allowed: bool,
) -> tuple[ClaimLabel, ...]:
    passed_criteria = tuple(item.criterion_id for item in criteria if item.passed)
    satisfied_boundaries = tuple(
        item.boundary_id for item in boundaries if item.satisfied
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Firebreak criteria passed: " + ", ".join(passed_criteria) + ".",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Package boundaries satisfied: " + ", ".join(satisfied_boundaries) + ".",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Internal candidate packaging is allowed as review-only."
                if candidate_packaging_allowed
                else "Internal candidate packaging is not allowed."
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
        "# T577 Results: Domain-Native Sheaf Transport Source-Law Firebreak Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Firebreak status: `{payload['firebreak_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Package label: `{payload['package_label']}`",
        f"- Source T576 verdict: `{payload['source_t576_verdict']}`",
        f"- Source T576 selected next packet: `{payload['source_t576_selected_next_packet']}`",
        f"- Candidate packaging allowed: {payload['candidate_packaging_allowed']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Firebreak Criteria",
        "",
        "| criterion | passed? | evidence | package effect | residual risk |",
        "| --- | :---: | --- | --- | --- |",
    ]
    for criterion in payload["firebreak_criteria"]:
        evidence = ", ".join(f"`{item}`" for item in criterion["evidence"])
        lines.append(
            "| "
            f"`{criterion['criterion_id']}` | "
            f"{criterion['passed']} | "
            f"{evidence} | "
            f"{criterion['package_effect']} | "
            f"{criterion['residual_risk']} |"
        )
    lines.extend(
        [
            "",
            "## Package Boundaries",
            "",
            "| boundary | satisfied? | required label | protects | reason |",
            "| --- | :---: | --- | --- | --- |",
        ]
    )
    for boundary in payload["package_boundaries"]:
        protects = ", ".join(f"`{item}`" for item in boundary["protects"])
        lines.append(
            "| "
            f"`{boundary['boundary_id']}` | "
            f"{boundary['satisfied']} | "
            f"`{boundary['required_label']}` | "
            f"{protects} | "
            f"{boundary['reason']} |"
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


def write_results(result: T577Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t577_result_to_dict(result)
    json_path = (
        results_dir
        / "T577-domain-native-sheaf-transport-source-law-firebreak-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T577-domain-native-sheaf-transport-source-law-firebreak-gate-v0.1-results.md"
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

    result = run_t577_analysis()
    payload = t577_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
