"""T576: hostile-search scope closure for the TAF11 semantic generator.

T575 found no true route-breaking hostile counterfamily, but it explicitly
left a scope-closure burden before any source-law, claim, canon, public-posture,
TAF4, TAF8, S1, publication, or cross-repo movement. T576 checks whether that
finite hostile panel was broad enough for the declared review scope. It closes
the finite hostile-search scope only as review pressure and selects a promotion
firebreak rather than promoting the route.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t575_domain_native_sheaf_transport_hostile_counterfamily_search_gate as t575,
)


ARTIFACT = "T576-domain-native-sheaf-transport-hostile-search-scope-closure-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_hostile_search_scope_closed_review_only"
SCOPE_STATUS = "FINITE_HOSTILE_SCOPE_CLOSED_REVIEW_ONLY"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_PROMOTION_FIREBREAK_REQUIRED"
NEXT_PACKET = "t577_domain_native_sheaf_transport_source_law_firebreak_gate"

NOT_CLAIMED = (
    "T576 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It closes the declared "
    "finite hostile-search scope as review-only and requires a promotion "
    "firebreak before any stronger reading."
)


@dataclass(frozen=True)
class ScopeAxis:
    axis_id: str
    required: tuple[str, ...]
    observed: tuple[str, ...]
    passed: bool
    evidence: str
    residual_risk: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["required"] = list(self.required)
        data["observed"] = list(self.observed)
        return data


@dataclass(frozen=True)
class ClosureCheck:
    check_id: str
    passed: bool
    evidence: tuple[str, ...]
    residual_risk: str

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
class T576Result:
    artifact: str
    source_t575_verdict: str
    source_t575_selected_next_packet: str
    scope_status: str
    source_law_status: str
    scope_axes: tuple[ScopeAxis, ...]
    closure_checks: tuple[ClosureCheck, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    finite_scope_closed: bool
    hostile_search_completed: bool
    true_counterfamily_found: bool
    route_breaks: bool
    route_kept_open: bool
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


def run_t576_analysis() -> T576Result:
    source = t575.run_t575_analysis()
    scope_axes = _scope_axes(source)
    closure_checks = _closure_checks(source=source, scope_axes=scope_axes)
    finite_scope_closed = all(axis.passed for axis in scope_axes) and all(
        check.passed for check in closure_checks
    )
    hostile_search_completed = source.hostile_search_completed
    true_counterfamily_found = source.true_counterfamily_found
    route_breaks = source.route_breaks
    route_kept_open = finite_scope_closed and source.route_kept_open
    source_law_earned = False
    route_decisions = _route_decisions(
        finite_scope_closed=finite_scope_closed,
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        source=source,
        scope_axes=scope_axes,
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        finite_scope_closed=finite_scope_closed,
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if finite_scope_closed
        and hostile_search_completed
        and not true_counterfamily_found
        and route_kept_open
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_hostile_scope_closure_unexpected_status"
    )

    return T576Result(
        artifact=ARTIFACT,
        source_t575_verdict=source.verdict,
        source_t575_selected_next_packet=source.selected_next_packet,
        scope_status=SCOPE_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        scope_axes=scope_axes,
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        finite_scope_closed=finite_scope_closed,
        hostile_search_completed=hostile_search_completed,
        true_counterfamily_found=true_counterfamily_found,
        route_breaks=route_breaks,
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T576 closes only the declared finite hostile-search scope. The "
            "scope covers the frozen source roles, absorber boundaries, "
            "semantic requirements, six shortcut classes, two independent "
            "survivor families, and the T574/T575 route history. That is enough "
            "to stop repeating the same hostile-search panel, but not enough "
            "to promote a public source law."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should be a promotion "
            "firebreak: it should decide whether the T559-T576 review-only "
            "route deserves any source-law candidate packaging, and it must "
            "still preserve claim, canon, public-posture, TAF4, TAF8, S1, "
            "publication, and cross-repo boundaries unless separately earned."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. T576 closes the hostile-search "
            "scope as finite review-only pressure and selects a promotion "
            "firebreak rather than source-law promotion."
        ),
        taf4_update=(
            "TAF4 remains blocked. Scope closure over a finite hostile panel is "
            "not continuum descent, causal-set recovery, Lorentzian target "
            "import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. Scope closure is internal TAF11 audit work, "
            "not a cross-domain shadow-protection theorem packet."
        ),
        claim_labels=_claim_labels(
            scope_axes=scope_axes,
            closure_checks=closure_checks,
            finite_scope_closed=finite_scope_closed,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T576 closes the declared finite "
            "hostile-search scope as review-only and selects a promotion "
            "firebreak; claim rows, Canon Index tiers, canon verdicts, and "
            "public posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t576_result_to_dict(result: T576Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t575_verdict": result.source_t575_verdict,
        "source_t575_selected_next_packet": result.source_t575_selected_next_packet,
        "scope_status": result.scope_status,
        "source_law_status": result.source_law_status,
        "scope_axes": [axis.to_dict() for axis in result.scope_axes],
        "closure_checks": [check.to_dict() for check in result.closure_checks],
        "route_decisions": [decision.to_dict() for decision in result.route_decisions],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "finite_scope_closed": result.finite_scope_closed,
        "hostile_search_completed": result.hostile_search_completed,
        "true_counterfamily_found": result.true_counterfamily_found,
        "route_breaks": result.route_breaks,
        "route_kept_open": result.route_kept_open,
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


def _scope_axes(source: t575.T575Result) -> tuple[ScopeAxis, ...]:
    candidates = source.candidates
    evaluations = {item.candidate_id: item for item in source.evaluations}
    contract = source.search_contract
    required_shortcuts = (
        "same_neighbor_trivial_gluing",
        "target_geometry_import",
        "optional_payload",
        "commuting_square_replacement",
        "foreign_truth_import",
        "incomplete_source_role",
    )
    observed_shortcuts = (
        "same_neighbor_trivial_gluing"
        if evaluations["trivial_same_neighbor_gluing_control"].status
        == "REJECTED_NOT_A_TRUE_COUNTERFAMILY"
        else "",
        "target_geometry_import"
        if evaluations["target_geometry_language_import_control"].status
        == "REJECTED_NOT_A_TRUE_COUNTERFAMILY"
        else "",
        "optional_payload"
        if evaluations["optional_payload_counterfamily_control"].status
        == "REJECTED_NOT_A_TRUE_COUNTERFAMILY"
        else "",
        "commuting_square_replacement"
        if evaluations["commuting_square_replacement_control"].status
        == "REJECTED_NOT_A_TRUE_COUNTERFAMILY"
        else "",
        "foreign_truth_import"
        if evaluations["foreign_truth_replay_control"].status
        == "REJECTED_NOT_A_TRUE_COUNTERFAMILY"
        else "",
        "incomplete_source_role"
        if evaluations["incomplete_source_role_collision_control"].status
        == "REJECTED_NOT_A_TRUE_COUNTERFAMILY"
        else "",
    )
    observed_shortcuts = tuple(item for item in observed_shortcuts if item)
    survivor_families = tuple(
        candidate.family_id
        for candidate in candidates
        if candidate.candidate_id in source.survivor_candidate_ids
    )
    return (
        _axis(
            axis_id="frozen_source_roles",
            required=contract.frozen_source_roles,
            observed=_union_tuple(candidate.frozen_source_roles for candidate in candidates),
            evidence="T575 candidates collectively covered every frozen source role.",
            residual_risk="Role coverage is finite and synthetic, not a source-law theorem.",
        ),
        _axis(
            axis_id="absorber_boundaries",
            required=contract.absorber_boundaries,
            observed=_union_tuple(candidate.absorber_boundaries for candidate in candidates),
            evidence="T575 covered sheaf, resource, consensus, and provenance absorbers.",
            residual_risk="Other mature absorbers may still exist.",
        ),
        _axis(
            axis_id="semantic_requirements",
            required=contract.semantic_requirements,
            observed=_union_tuple(candidate.semantic_requirements for candidate in candidates),
            evidence="T575 included nontrivial obstruction, noncommuting transport, payload, target-blind, role-projection, and independent-surface requirements.",
            residual_risk="Semantic coverage is by declared finite requirements.",
        ),
        _axis(
            axis_id="rejected_shortcut_classes",
            required=required_shortcuts,
            observed=observed_shortcuts,
            evidence="T575 rejected the six shortcut classes that would create false counterfamilies.",
            residual_risk="The rejected class list is not exhaustive for all mathematics.",
        ),
        _axis(
            axis_id="independent_survivor_families",
            required=("escrow_epoch_repair_family", "quorum_manifest_repair_family"),
            observed=survivor_families,
            evidence="T575 included two independent finality-native survivor families.",
            residual_risk="Survivors keep the route open but do not prove uniqueness.",
        ),
        _axis(
            axis_id="route_history_pressure",
            required=(
                source.source_t574_verdict,
                source.verdict,
                source.selected_next_packet,
            ),
            observed=(
                source.source_t574_verdict,
                source.verdict,
                source.selected_next_packet,
            ),
            evidence="T576 consumes the T574 route-adjudication and T575 hostile-search chain.",
            residual_risk="The T559-T576 route remains a finite review route.",
        ),
    )


def _axis(
    axis_id: str,
    required: tuple[str, ...],
    observed: tuple[str, ...],
    evidence: str,
    residual_risk: str,
) -> ScopeAxis:
    required_set = set(required)
    observed_set = set(observed)
    return ScopeAxis(
        axis_id=axis_id,
        required=required,
        observed=observed,
        passed=required_set <= observed_set,
        evidence=evidence,
        residual_risk=residual_risk,
    )


def _union_tuple(groups: tuple[str, ...] | list[tuple[str, ...]] | Any) -> tuple[str, ...]:
    seen: list[str] = []
    for group in groups:
        for item in group:
            if item not in seen:
                seen.append(item)
    return tuple(seen)


def _closure_checks(
    source: t575.T575Result,
    scope_axes: tuple[ScopeAxis, ...],
) -> tuple[ClosureCheck, ...]:
    axis_map = {axis.axis_id: axis for axis in scope_axes}
    passed_axes = tuple(axis.axis_id for axis in scope_axes if axis.passed)
    return (
        ClosureCheck(
            check_id="t575_authority",
            passed=(
                source.verdict == t575.VERDICT
                and source.selected_next_packet == t575.NEXT_PACKET
                and source.hostile_search_completed
                and not source.true_counterfamily_found
            ),
            evidence=(source.verdict, source.selected_next_packet),
            residual_risk="T575 is hostile search, not source-law status.",
        ),
        ClosureCheck(
            check_id="all_scope_axes_pass",
            passed=len(passed_axes) == len(scope_axes),
            evidence=passed_axes,
            residual_risk="Axis closure only covers the declared finite panel.",
        ),
        ClosureCheck(
            check_id="survivors_and_rejections_balanced",
            passed=(
                len(source.survivor_candidate_ids) >= 2
                and len(source.rejected_candidate_ids) >= 6
                and axis_map["independent_survivor_families"].passed
                and axis_map["rejected_shortcut_classes"].passed
            ),
            evidence=source.survivor_candidate_ids + source.rejected_candidate_ids,
            residual_risk="Balanced panels still do not exhaust all future hostile families.",
        ),
        ClosureCheck(
            check_id="residual_risks_explicit",
            passed=all(axis.residual_risk for axis in scope_axes),
            evidence=tuple(axis.residual_risk for axis in scope_axes),
            residual_risk="Explicit risk language prevents closure from becoming promotion.",
        ),
        ClosureCheck(
            check_id="protected_boundaries_need_firebreak",
            passed=not source.source_law_earned,
            evidence=("source_law_not_earned", NEXT_PACKET),
            residual_risk="The next packet must still prevent promotion by inertia.",
        ),
    )


def _route_decisions(
    finite_scope_closed: bool,
    route_kept_open: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "BLOCKED_FIREBREAK_REQUIRED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "Scope closure is not public source-law status."
            ),
        ),
        RouteDecision(
            decision_id="close_hostile_search_scope",
            outcome=(
                "SELECTED_SCOPE_CLOSED_REVIEW_ONLY"
                if finite_scope_closed and route_kept_open
                else "PAUSED_SCOPE_NOT_CLOSED"
            ),
            selected=finite_scope_closed and route_kept_open,
            next_packet="none",
            reason=(
                "The declared finite hostile-search scope is closed as review-only."
                if finite_scope_closed and route_kept_open
                else "The hostile-search scope needs more coverage."
            ),
        ),
        RouteDecision(
            decision_id="run_source_law_firebreak",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if finite_scope_closed and route_kept_open and not source_law_earned
                else "PAUSED_UNTIL_SCOPE_CLOSED"
            ),
            selected=finite_scope_closed and route_kept_open and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "After finite scope closure, the honest next step is a promotion firebreak."
                if finite_scope_closed and route_kept_open
                else "The firebreak waits for scope closure."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_scope_closure",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Scope closure is not continuum descent or target-spacetime recovery.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_scope_closure",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Scope closure is not a cross-domain shadow-protection theorem.",
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
    selected = tuple(decision for decision in decisions if decision.selected)
    next_packets = tuple(
        decision.next_packet for decision in selected if decision.next_packet != "none"
    )
    if len(next_packets) != 1:
        return "none"
    return next_packets[0]


def _gate_decisions(
    source: t575.T575Result,
    scope_axes: tuple[ScopeAxis, ...],
    closure_checks: tuple[ClosureCheck, ...],
    route_decisions: tuple[RouteDecision, ...],
    finite_scope_closed: bool,
    route_kept_open: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    decisions = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t575_authority",
            source.verdict == t575.VERDICT
            and source.selected_next_packet == t575.NEXT_PACKET,
            "T575 supplies hostile-search scope-closure authority.",
            "T575 did not supply scope-closure authority.",
        ),
        (
            "scope_axes_pass",
            all(axis.passed for axis in scope_axes),
            "Every declared scope axis passed.",
            "One or more scope axes failed.",
        ),
        (
            "closure_checks_pass",
            all(check.passed for check in closure_checks),
            "Every closure check passed.",
            "One or more closure checks failed.",
        ),
        (
            "finite_scope_closed_review_only",
            finite_scope_closed and route_kept_open and not source_law_earned,
            "Finite hostile scope is closed as review-only.",
            "Scope closure moved too far or failed.",
        ),
        (
            "source_law_firebreak_selected_next",
            selected_next_packet == NEXT_PACKET
            and decisions["run_source_law_firebreak"].selected,
            "Source-law firebreak is selected as the next burden.",
            "The expected firebreak next packet was not selected.",
        ),
        (
            "protected_boundaries_preserved",
            decisions["promote_source_law_now"].outcome == "BLOCKED_FIREBREAK_REQUIRED"
            and decisions["move_taf4_from_scope_closure"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decisions["execute_taf8_from_scope_closure"].outcome == "BLOCKED_TAF8_OVERREAD"
            and decisions["move_s1_or_cross_repo_truth"].outcome == "BLOCKED_GOVERNANCE",
            "Source-law, TAF4, TAF8, S1, cross-repo, publication, claim, canon, and public-posture shortcuts are blocked.",
            "A protected route movement was allowed.",
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
    scope_axes: tuple[ScopeAxis, ...],
    closure_checks: tuple[ClosureCheck, ...],
    finite_scope_closed: bool,
) -> tuple[ClaimLabel, ...]:
    passed_axes = ", ".join(axis.axis_id for axis in scope_axes if axis.passed)
    passed_checks = ", ".join(
        check.check_id for check in closure_checks if check.passed
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Scope axes passed: {passed_axes}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Closure checks passed: {passed_checks}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Finite hostile-search scope is closed as review-only."
                if finite_scope_closed
                else "Finite hostile-search scope is not closed."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law promotion remains blocked until a separate firebreak packet earns it.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T576 Results: Domain-Native Sheaf Transport Hostile Search Scope Closure Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Scope status: `{payload['scope_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Source T575 verdict: `{payload['source_t575_verdict']}`",
        f"- Source T575 selected next packet: `{payload['source_t575_selected_next_packet']}`",
        f"- Finite scope closed: {payload['finite_scope_closed']}",
        f"- Hostile search completed: {payload['hostile_search_completed']}",
        f"- True counterfamily found: {payload['true_counterfamily_found']}",
        f"- Route breaks: {payload['route_breaks']}",
        f"- Route kept open: {payload['route_kept_open']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Scope Axes",
        "",
        "| axis | passed? | observed | residual risk |",
        "| --- | :---: | --- | --- |",
    ]
    for axis in payload["scope_axes"]:
        observed = ", ".join(f"`{item}`" for item in axis["observed"])
        lines.append(
            "| "
            f"`{axis['axis_id']}` | "
            f"{axis['passed']} | "
            f"{observed} | "
            f"{axis['residual_risk']} |"
        )
    lines.extend(
        [
            "",
            "## Closure Checks",
            "",
            "| check | passed? | evidence | residual risk |",
            "| --- | :---: | --- | --- |",
        ]
    )
    for check in payload["closure_checks"]:
        evidence = ", ".join(f"`{item}`" for item in check["evidence"])
        lines.append(
            "| "
            f"`{check['check_id']}` | "
            f"{check['passed']} | "
            f"{evidence} | "
            f"{check['residual_risk']} |"
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


def write_results(result: T576Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t576_result_to_dict(result)
    json_path = (
        results_dir
        / "T576-domain-native-sheaf-transport-hostile-search-scope-closure-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T576-domain-native-sheaf-transport-hostile-search-scope-closure-gate-v0.1-results.md"
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

    result = run_t576_analysis()
    payload = t576_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
