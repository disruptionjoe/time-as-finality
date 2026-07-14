"""T574: source-law route adjudication for the TAF11 semantic generator.

T573 selected route adjudication after the adversarial blind-family holdout
survived. T574 asks whether the T559-T573 route should be promoted, retired,
or kept open under a further non-promotion burden. The adjudication keeps the
route open, blocks promotion, and selects hostile counterfamily search.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t573_domain_native_sheaf_transport_adversarial_blind_family_holdout_gate
    as t573,
)


ARTIFACT = "T574-domain-native-sheaf-transport-source-law-route-adjudication-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_route_kept_open_counterfamily_required_review_only"
ADJUDICATION_STATUS = "ROUTE_KEPT_OPEN_SOURCE_LAW_NOT_PROMOTED"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_COUNTERFAMILY_SEARCH_REQUIRED"
NEXT_PACKET = "t575_domain_native_sheaf_transport_hostile_counterfamily_search_gate"

NOT_CLAIMED = (
    "T574 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It adjudicates the T559-T573 "
    "route as review-only and names a further hostile counterfamily burden."
)


@dataclass(frozen=True)
class RouteCriterion:
    criterion_id: str
    source_span: str
    passed: bool
    weight: str
    evidence: tuple[str, ...]
    route_effect: str
    residual_risk: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["evidence"] = list(self.evidence)
        return data


@dataclass(frozen=True)
class PromotionBlocker:
    blocker_id: str
    active: bool
    reason: str
    required_next: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


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
class T574Result:
    artifact: str
    source_t573_verdict: str
    source_t573_selected_next_packet: str
    source_t573_adversarial_holdout_cleared: bool
    adjudication_status: str
    source_law_status: str
    route_criteria: tuple[RouteCriterion, ...]
    promotion_blockers: tuple[PromotionBlocker, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
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


def run_t574_analysis() -> T574Result:
    source = t573.run_t573_analysis()
    criteria = _route_criteria(source)
    promotion_blockers = _promotion_blockers()
    route_kept_open = all(
        criterion.passed for criterion in criteria if criterion.weight == "required"
    )
    source_law_earned = False
    route_decisions = _route_decisions(
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        criteria=criteria,
        promotion_blockers=promotion_blockers,
        route_decisions=route_decisions,
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if route_kept_open
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_route_adjudication_unexpected_status"
    )

    return T574Result(
        artifact=ARTIFACT,
        source_t573_verdict=source.verdict,
        source_t573_selected_next_packet=source.selected_next_packet,
        source_t573_adversarial_holdout_cleared=source.adversarial_holdout_cleared,
        adjudication_status=ADJUDICATION_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_criteria=criteria,
        promotion_blockers=promotion_blockers,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T574 adjudicates the T559-T573 route as strong enough to keep "
            "open but still insufficient for public source-law status. The "
            "route has bounded-class, minimality, absorber-separation, "
            "predictive, typed-generator, hostile-review, semantic-strengthening, "
            "independent-reimplementation, fresh-family, falsifier-rotation, "
            "blind-family, and adversarial blind-family pressure. It still lacks "
            "hostile counterfamily search and any public law, continuum, "
            "cross-domain, or external evidence."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should search for a hostile "
            "domain-native counterfamily under the frozen source roles, absorber "
            "boundaries, and semantic requirements before any source-law, claim, "
            "canon, public-posture, TAF4, TAF8, S1, publication, or cross-repo "
            "movement."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. T574 keeps the semantic-generator "
            "route open, blocks promotion, and turns the next burden toward "
            "hostile counterfamily search."
        ),
        taf4_update=(
            "TAF4 remains blocked. Route adjudication is not finite-to-continuum "
            "descent, causal-set recovery, Lorentzian target import, or "
            "manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T574 is internal TAF11 route adjudication, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(criteria, promotion_blockers),
        claim_ledger_update=(
            "No claim-ledger update is earned. T574 keeps the TAF11 route open "
            "as review-only, blocks promotion, and selects hostile counterfamily "
            "search; claim rows, Canon Index tiers, canon verdicts, and public "
            "posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t574_result_to_dict(result: T574Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t573_verdict": result.source_t573_verdict,
        "source_t573_selected_next_packet": result.source_t573_selected_next_packet,
        "source_t573_adversarial_holdout_cleared": (
            result.source_t573_adversarial_holdout_cleared
        ),
        "adjudication_status": result.adjudication_status,
        "source_law_status": result.source_law_status,
        "route_criteria": [criterion.to_dict() for criterion in result.route_criteria],
        "promotion_blockers": [
            blocker.to_dict() for blocker in result.promotion_blockers
        ],
        "route_decisions": [decision.to_dict() for decision in result.route_decisions],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
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


def _route_criteria(source: t573.T573Result) -> tuple[RouteCriterion, ...]:
    t573_authority = (
        source.verdict == t573.VERDICT
        and source.selected_next_packet == t573.NEXT_PACKET
        and source.adversarial_holdout_cleared
        and not source.source_law_earned
    )
    return (
        RouteCriterion(
            criterion_id="t573_authority",
            source_span="T573",
            passed=t573_authority,
            weight="required",
            evidence=(
                source.verdict,
                source.selected_next_packet,
                "adversarial_holdout_cleared",
            ),
            route_effect="Supplies route-adjudication authority without promotion.",
            residual_risk="T573 is finite synthetic review pressure, not a public law.",
        ),
        RouteCriterion(
            criterion_id="bounded_class_minimality_and_absorber_separation",
            source_span="T559-T564",
            passed=True,
            weight="required",
            evidence=(
                "bounded class mapped",
                "minimality cleared",
                "absorber separation cleared",
                "predictive and typed-generator burdens named at T564",
            ),
            route_effect="The route has a bounded class and survived native absorbers.",
            residual_risk="This still does not establish a law beyond the synthetic class.",
        ),
        RouteCriterion(
            criterion_id="predictive_and_typed_generator_burdens_cleared",
            source_span="T565-T566",
            passed=True,
            weight="required",
            evidence=(
                "predictive holdout survived",
                "typed generator selected future admissible cases",
            ),
            route_effect="The route moved beyond manual fixture reading.",
            residual_risk="The generator still needed hostile review and semantic hardening.",
        ),
        RouteCriterion(
            criterion_id="hostile_review_and_semantic_strengthening_cleared",
            source_span="T567-T568",
            passed=True,
            weight="required",
            evidence=(
                "same-field alternates survived hostile review",
                "semantic screens reject trivial completion and target import",
            ),
            route_effect="The route corrected field-name overbreadth.",
            residual_risk="Semantic strengthening may still overfit the tested families.",
        ),
        RouteCriterion(
            criterion_id="independent_reimplementation_and_fresh_family_stress_cleared",
            source_span="T569-T570",
            passed=True,
            weight="required",
            evidence=(
                "independent reimplementation matched",
                "fresh family stress survived",
            ),
            route_effect="The route is not merely fixture-label replay.",
            residual_risk="Fresh family stress remains finite and synthetic.",
        ),
        RouteCriterion(
            criterion_id="rotation_blind_and_adversarial_holdouts_cleared",
            source_span="T571-T573",
            passed=source.adversarial_holdout_cleared,
            weight="required",
            evidence=(
                "multi-family falsifier rotation survived",
                "blind-family holdout survived",
                "adversarial blind-family holdout survived",
            ),
            route_effect="The route has enough pressure to stay open.",
            residual_risk="No hostile counterfamily search has tried to break the route.",
        ),
    )


def _promotion_blockers() -> tuple[PromotionBlocker, ...]:
    return (
        PromotionBlocker(
            blocker_id="finite_synthetic_route_only",
            active=True,
            reason="The evidence is finite synthetic route pressure, not a public source law.",
            required_next=NEXT_PACKET,
        ),
        PromotionBlocker(
            blocker_id="hostile_counterfamily_search_missing",
            active=True,
            reason="The route has not searched for an independent hostile counterfamily.",
            required_next=NEXT_PACKET,
        ),
        PromotionBlocker(
            blocker_id="no_taf4_continuum_descent",
            active=True,
            reason="The route supplies no finite-to-continuum descent or Lorentzian bridge.",
            required_next="keep_taf4_blocked",
        ),
        PromotionBlocker(
            blocker_id="no_taf8_cross_domain_packet",
            active=True,
            reason="The route is internal TAF11 generator stress, not TAF8 shadow protection.",
            required_next="keep_taf8_waiting",
        ),
        PromotionBlocker(
            blocker_id="protected_governance_surfaces",
            active=True,
            reason="Claim rows, Canon Index tiers, canon verdicts, public posture, S1, publication, and cross-repo truth remain protected.",
            required_next="no_governance_movement",
        ),
    )


def _route_decisions(
    route_kept_open: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "BLOCKED_PROMOTION_BAR_NOT_MET"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "Route evidence is strong enough to continue but still review-only."
            ),
        ),
        RouteDecision(
            decision_id="retire_semantic_generator_route",
            outcome=(
                "PAUSED_ROUTE_STILL_OPEN"
                if route_kept_open
                else "SELECTED_ROUTE_RETIREMENT"
            ),
            selected=not route_kept_open,
            next_packet="none",
            reason=(
                "Retirement is premature because required route criteria passed."
                if route_kept_open
                else "The route failed required adjudication criteria."
            ),
        ),
        RouteDecision(
            decision_id="run_hostile_counterfamily_search_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if route_kept_open and not source_law_earned
                else "PAUSED_UNTIL_ROUTE_IS_OPEN_AND_UNPROMOTED"
            ),
            selected=route_kept_open and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The route should be kept open by trying to break it with a hostile counterfamily before any promotion."
                if route_kept_open
                else "Counterfamily search waits for a live route."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t574",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Route adjudication is not continuum descent or target-spacetime recovery.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t574",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 route adjudication is not a cross-domain shadow-protection packet.",
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
    if len(selected) != 1:
        return "none"
    return selected[0].next_packet


def _gate_decisions(
    criteria: tuple[RouteCriterion, ...],
    promotion_blockers: tuple[PromotionBlocker, ...],
    route_decisions: tuple[RouteDecision, ...],
    route_kept_open: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    criteria_by_id = {criterion.criterion_id: criterion for criterion in criteria}
    decisions = {decision.decision_id: decision for decision in route_decisions}
    blockers_active = all(blocker.active for blocker in promotion_blockers)
    required_criteria_pass = all(
        criterion.passed for criterion in criteria if criterion.weight == "required"
    )
    gates = (
        (
            "t573_authority",
            criteria_by_id["t573_authority"].passed,
            "T573 supplies route-adjudication authority.",
            "T573 did not supply route-adjudication authority.",
        ),
        (
            "route_evidence_keeps_route_open",
            route_kept_open and required_criteria_pass,
            "Required T559-T573 route criteria passed.",
            "Required route criteria did not pass.",
        ),
        (
            "promotion_blockers_active",
            blockers_active and not source_law_earned,
            "Promotion blockers remain active and source-law status is not earned.",
            "A promotion blocker was missing or source-law status moved too early.",
        ),
        (
            "hostile_counterfamily_search_selected_next",
            selected_next_packet == NEXT_PACKET
            and decisions["run_hostile_counterfamily_search_gate"].selected,
            "Hostile counterfamily search is selected as the next burden.",
            "The expected hostile counterfamily search next packet was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            decisions["move_taf4_from_t574"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decisions["execute_taf8_from_t574"].outcome == "BLOCKED_TAF8_OVERREAD"
            and decisions["move_s1_or_cross_repo_truth"].outcome == "BLOCKED_GOVERNANCE",
            "TAF4, TAF8, S1, cross-repo, publication, claim, canon, and public-posture shortcuts are blocked.",
            "A forbidden route movement was allowed.",
        ),
        (
            "source_law_not_promoted",
            decisions["promote_source_law_now"].outcome == "BLOCKED_PROMOTION_BAR_NOT_MET"
            and not source_law_earned,
            "Source-law promotion is blocked.",
            "Source-law promotion moved too early.",
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
    criteria: tuple[RouteCriterion, ...],
    blockers: tuple[PromotionBlocker, ...],
) -> tuple[ClaimLabel, ...]:
    passed_criteria = tuple(
        criterion.criterion_id for criterion in criteria if criterion.passed
    )
    active_blockers = tuple(blocker.blocker_id for blocker in blockers if blocker.active)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Route adjudication passed required criteria: " + ", ".join(passed_criteria) + ".",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law promotion remains blocked by: " + ", ".join(active_blockers) + ".",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="The route is worth keeping open only through hostile counterfamily search.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T574 Results: Domain-Native Sheaf Transport Source-Law Route Adjudication Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Adjudication status: `{payload['adjudication_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Source T573 verdict: `{payload['source_t573_verdict']}`",
        f"- Source T573 selected next packet: `{payload['source_t573_selected_next_packet']}`",
        f"- Source T573 adversarial holdout cleared: {payload['source_t573_adversarial_holdout_cleared']}",
        f"- Route kept open: {payload['route_kept_open']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Route Criteria",
        "",
        "| criterion | source span | passed? | weight | route effect | residual risk |",
        "| --- | --- | :---: | --- | --- | --- |",
    ]
    for criterion in payload["route_criteria"]:
        lines.append(
            "| "
            f"`{criterion['criterion_id']}` | "
            f"`{criterion['source_span']}` | "
            f"{criterion['passed']} | "
            f"`{criterion['weight']}` | "
            f"{criterion['route_effect']} | "
            f"{criterion['residual_risk']} |"
        )
    lines.extend(
        [
            "",
            "## Promotion Blockers",
            "",
            "| blocker | active? | required next | reason |",
            "| --- | :---: | --- | --- |",
        ]
    )
    for blocker in payload["promotion_blockers"]:
        lines.append(
            "| "
            f"`{blocker['blocker_id']}` | "
            f"{blocker['active']} | "
            f"`{blocker['required_next']}` | "
            f"{blocker['reason']} |"
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


def write_results(result: T574Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t574_result_to_dict(result)
    json_path = (
        results_dir
        / "T574-domain-native-sheaf-transport-source-law-route-adjudication-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T574-domain-native-sheaf-transport-source-law-route-adjudication-gate-v0.1-results.md"
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

    result = run_t574_analysis()
    payload = t574_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
