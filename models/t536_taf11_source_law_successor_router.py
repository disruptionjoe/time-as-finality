"""T536: TAF11 source-law successor router.

T534 paused the S1 finite-generator route because no finality-domain source law
cleared. T535 found no real C(R) packet to unblock the Track-2 branch. T536
turns the TAF11 successor choice into an executable router: pick the next
source-law swing without demoting the North Star, repeating spent finite-generator
screens, or moving claims.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t534_new_finality_domain_law_pause_router as t534
from models import t535_real_taf10_packet_screen as t535


ARTIFACT = "T536-taf11-source-law-successor-router-v0.1"
VERDICT = "taf11_successor_route_selected_source_law_family_and_falsifier_packet"
SELECTED_ROUTE = "t537_source_law_family_and_falsifier_packet"

FORBIDDEN_REPEAT_SHAPES = (
    "two_channel_receipt_product_order",
    "three_channel_receipt_product_order",
    "record_window_separation_order",
    "external_lorentzian_uv_reference_law",
    "t528_screen_conditioned_receipt_mixture",
    "posthoc_repaired_band_fit",
)

NOT_CLAIMED = (
    "T536 does not derive spacetime, prove manifoldlikeness, repair T528, "
    "reverse T223, unpause the S1 finite-generator route, promote S1, change "
    "claim status, change canon, change public posture, authorize external "
    "publication, or move cross-repo truth. It is a TAF11 work-selection router."
)


@dataclass(frozen=True)
class SuccessorRoute:
    route_id: str
    description: str
    preserves_north_star: bool
    directed_source_law_route: bool
    supplies_or_requires_independent_naturality: bool
    states_falsifier_before_execution: bool
    repeats_spent_finite_generator_shape: bool
    changes_target_statistic_before_law: bool
    imports_lorentzian_reference: bool
    depends_on_real_data_packet: bool
    replaces_track_1_with_track_2: bool
    requests_claim_canon_public_or_external_movement: bool
    produces_executable_next_packet: bool


@dataclass(frozen=True)
class RouteDecision:
    route_id: str
    outcome: str
    selected_as_next: bool
    track_role: str
    missing_requirements: tuple[str, ...]
    reason: str
    next_packet: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T536Result:
    artifact: str
    source_t534_verdict: str
    source_t534_route_outcome: str
    source_t534_cleared_laws: tuple[str, ...]
    source_t535_verdict: str
    source_t535_real_packet_in_hand: bool
    forbidden_repeat_shapes: tuple[str, ...]
    route_decisions: tuple[RouteDecision, ...]
    selected_route_ids: tuple[str, ...]
    verdict: str
    recommended_next: str
    claim_labels: tuple[ClaimLabel, ...]
    s1_update: str
    claim_ledger_update: str
    not_claimed: str


def run_t536_analysis() -> T536Result:
    t534_result = t534.run_t534_analysis()
    t535_payload = t535.run()
    decisions = tuple(_evaluate_route(route) for route in _successor_routes())
    selected = tuple(
        decision.route_id for decision in decisions if decision.selected_as_next
    )
    verdict = (
        VERDICT
        if t534_result.route_outcome == "PAUSE"
        and t534_result.cleared_candidate_ids == ()
        and not t535_payload["overall"]["real_taf10_packet_in_hand"]
        and selected == (SELECTED_ROUTE,)
        else "taf11_successor_router_unexpected_status"
    )
    return T536Result(
        artifact=ARTIFACT,
        source_t534_verdict=t534_result.verdict,
        source_t534_route_outcome=t534_result.route_outcome,
        source_t534_cleared_laws=t534_result.cleared_candidate_ids,
        source_t535_verdict=t535_payload["verdict"],
        source_t535_real_packet_in_hand=t535_payload["overall"][
            "real_taf10_packet_in_hand"
        ],
        forbidden_repeat_shapes=FORBIDDEN_REPEAT_SHAPES,
        route_decisions=decisions,
        selected_route_ids=selected,
        verdict=verdict,
        recommended_next=(
            "Run T537 as a source-law family and falsifier packet. It should "
            "generate a small menu of genuinely new finality-domain law families, "
            "exclude spent finite-generator shapes, require independent "
            "naturality and a predeclared falsifier for each family, and select "
            "only a law family that can later be computed without target import."
        ),
        claim_labels=_claim_labels(decisions),
        s1_update=(
            "S1 remains `requires_added_assumption`. T536 selects the next "
            "source-law router and supplies no S1 evidence."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T536 is work-selection for "
            "TAF11 only and leaves claim rows, Canon Index tiers, and verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t536_result_to_dict(result: T536Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t534_verdict": result.source_t534_verdict,
        "source_t534_route_outcome": result.source_t534_route_outcome,
        "source_t534_cleared_laws": list(result.source_t534_cleared_laws),
        "source_t535_verdict": result.source_t535_verdict,
        "source_t535_real_packet_in_hand": result.source_t535_real_packet_in_hand,
        "forbidden_repeat_shapes": list(result.forbidden_repeat_shapes),
        "route_decisions": [
            {
                "route_id": decision.route_id,
                "outcome": decision.outcome,
                "selected_as_next": decision.selected_as_next,
                "track_role": decision.track_role,
                "missing_requirements": list(decision.missing_requirements),
                "reason": decision.reason,
                "next_packet": decision.next_packet,
            }
            for decision in result.route_decisions
        ],
        "selected_route_ids": list(result.selected_route_ids),
        "verdict": result.verdict,
        "recommended_next": result.recommended_next,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _successor_routes() -> tuple[SuccessorRoute, ...]:
    return (
        SuccessorRoute(
            route_id=SELECTED_ROUTE,
            description=(
                "Create a successor packet that generates new finality-domain "
                "law families and attaches a falsifier to each before any "
                "computation reads target outcomes."
            ),
            preserves_north_star=True,
            directed_source_law_route=True,
            supplies_or_requires_independent_naturality=True,
            states_falsifier_before_execution=True,
            repeats_spent_finite_generator_shape=False,
            changes_target_statistic_before_law=False,
            imports_lorentzian_reference=False,
            depends_on_real_data_packet=False,
            replaces_track_1_with_track_2=False,
            requests_claim_canon_public_or_external_movement=False,
            produces_executable_next_packet=True,
        ),
        SuccessorRoute(
            route_id="taf8_shadow_protection_feeder_packet",
            description=(
                "Move to a higher-level cross-domain shadow-protection theorem "
                "before a new source law exists."
            ),
            preserves_north_star=True,
            directed_source_law_route=False,
            supplies_or_requires_independent_naturality=True,
            states_falsifier_before_execution=True,
            repeats_spent_finite_generator_shape=False,
            changes_target_statistic_before_law=False,
            imports_lorentzian_reference=False,
            depends_on_real_data_packet=False,
            replaces_track_1_with_track_2=False,
            requests_claim_canon_public_or_external_movement=False,
            produces_executable_next_packet=True,
        ),
        SuccessorRoute(
            route_id="changed_target_statistic_first",
            description=(
                "Change the ordering-fraction target statistic before naming a "
                "new law or falsifier."
            ),
            preserves_north_star=False,
            directed_source_law_route=False,
            supplies_or_requires_independent_naturality=False,
            states_falsifier_before_execution=False,
            repeats_spent_finite_generator_shape=False,
            changes_target_statistic_before_law=True,
            imports_lorentzian_reference=False,
            depends_on_real_data_packet=False,
            replaces_track_1_with_track_2=False,
            requests_claim_canon_public_or_external_movement=False,
            produces_executable_next_packet=False,
        ),
        SuccessorRoute(
            route_id="taf12_data_packet_wait",
            description=(
                "Wait for a real data-bearing C(R) packet to replace the Track-1 "
                "source-law question."
            ),
            preserves_north_star=False,
            directed_source_law_route=False,
            supplies_or_requires_independent_naturality=False,
            states_falsifier_before_execution=False,
            repeats_spent_finite_generator_shape=False,
            changes_target_statistic_before_law=False,
            imports_lorentzian_reference=False,
            depends_on_real_data_packet=True,
            replaces_track_1_with_track_2=True,
            requests_claim_canon_public_or_external_movement=False,
            produces_executable_next_packet=False,
        ),
        SuccessorRoute(
            route_id="repeat_record_window_or_receipt_product",
            description=(
                "Rerun two-channel, three-channel, or record-window finite-generator shapes."
            ),
            preserves_north_star=False,
            directed_source_law_route=True,
            supplies_or_requires_independent_naturality=True,
            states_falsifier_before_execution=True,
            repeats_spent_finite_generator_shape=True,
            changes_target_statistic_before_law=False,
            imports_lorentzian_reference=False,
            depends_on_real_data_packet=False,
            replaces_track_1_with_track_2=False,
            requests_claim_canon_public_or_external_movement=False,
            produces_executable_next_packet=False,
        ),
        SuccessorRoute(
            route_id="s1_posture_move_from_pause",
            description=(
                "Treat the T534 pause as reason to move S1, claims, canon, or public posture."
            ),
            preserves_north_star=False,
            directed_source_law_route=False,
            supplies_or_requires_independent_naturality=False,
            states_falsifier_before_execution=False,
            repeats_spent_finite_generator_shape=False,
            changes_target_statistic_before_law=False,
            imports_lorentzian_reference=False,
            depends_on_real_data_packet=False,
            replaces_track_1_with_track_2=False,
            requests_claim_canon_public_or_external_movement=True,
            produces_executable_next_packet=False,
        ),
    )


def _evaluate_route(route: SuccessorRoute) -> RouteDecision:
    missing = _missing_requirements(route)
    if route.requests_claim_canon_public_or_external_movement:
        outcome = "BLOCKED_GOVERNANCE"
        selected = False
        track_role = "forbidden"
        reason = "A pause or router cannot move claims, canon, public posture, or external state."
        next_packet = "none"
    elif route.repeats_spent_finite_generator_shape:
        outcome = "REJECTED_DUPLICATE"
        selected = False
        track_role = "spent"
        reason = "The route repeats shapes already spent by T532/T534."
        next_packet = "none"
    elif route.changes_target_statistic_before_law:
        outcome = "BLOCKED_TARGET_DRIFT"
        selected = False
        track_role = "blocked"
        reason = "Target statistics can change only after a law or falsifier earns the change."
        next_packet = "none"
    elif route.depends_on_real_data_packet and route.replaces_track_1_with_track_2:
        outcome = "PAUSED_TRACK_2"
        selected = False
        track_role = "track_2_waiting"
        reason = "T535 found no real data-bearing packet, and Track 2 cannot replace Track 1."
        next_packet = "none"
    elif missing:
        outcome = "NOT_SELECTED"
        selected = False
        track_role = "feeder_or_incomplete"
        reason = "The route lacks one or more TAF11 source-law successor requirements."
        next_packet = "none"
    elif route.directed_source_law_route:
        outcome = "SELECTED"
        selected = True
        track_role = "track_1_next"
        reason = (
            "The route preserves the North Star, requires new source-law families, "
            "requires independent naturality and falsifiers, and avoids spent shapes."
        )
        next_packet = SELECTED_ROUTE
    else:
        outcome = "FEEDER_REVIEW_ONLY"
        selected = False
        track_role = "track_1_adjacent"
        reason = "Useful feeder work, but not the next directed source-law route."
        next_packet = "none"
    return RouteDecision(
        route_id=route.route_id,
        outcome=outcome,
        selected_as_next=selected,
        track_role=track_role,
        missing_requirements=missing,
        reason=reason,
        next_packet=next_packet,
    )


def _missing_requirements(route: SuccessorRoute) -> tuple[str, ...]:
    missing: list[str] = []
    if not route.preserves_north_star:
        missing.append("preserves_north_star")
    if not route.directed_source_law_route:
        missing.append("directed_source_law_route")
    if not route.supplies_or_requires_independent_naturality:
        missing.append("independent_naturality_requirement")
    if not route.states_falsifier_before_execution:
        missing.append("predeclared_falsifier")
    if route.repeats_spent_finite_generator_shape:
        missing.append("no_spent_finite_generator_repeat")
    if route.changes_target_statistic_before_law:
        missing.append("no_target_statistic_change_before_law")
    if route.imports_lorentzian_reference:
        missing.append("no_lorentzian_reference_import")
    if route.depends_on_real_data_packet:
        missing.append("not_blocked_on_real_data_packet")
    if route.replaces_track_1_with_track_2:
        missing.append("track_2_does_not_replace_track_1")
    if route.requests_claim_canon_public_or_external_movement:
        missing.append("no_claim_canon_public_or_external_movement")
    if not route.produces_executable_next_packet:
        missing.append("produces_executable_next_packet")
    return tuple(missing)


def _claim_labels(decisions: tuple[RouteDecision, ...]) -> tuple[ClaimLabel, ...]:
    selected = tuple(decision for decision in decisions if decision.selected_as_next)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T534 is consumed as a pause state with no cleared new source law, "
                "and T535 is consumed as no real TAF10 packet in hand."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Exactly one successor route is selected: {selected[0].route_id}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Spent finite-generator shapes, target drift, Track-2 replacement, "
                "and posture movement are rejected or blocked."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "A source-law family and falsifier packet is the next honest Track-1 "
                "move because it seeks new directed source-law routes without "
                "demoting the North Star for difficulty."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T536 Results: TAF11 Source-Law Successor Router",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source T534 route outcome: `{payload['source_t534_route_outcome']}`",
        f"- Source T534 cleared laws: {', '.join(payload['source_t534_cleared_laws']) or 'none'}",
        f"- Source T535 verdict: `{payload['source_t535_verdict']}`",
        f"- T535 real packet in hand: {payload['source_t535_real_packet_in_hand']}",
        "- Selected route ids: "
        + (", ".join(f"`{item}`" for item in payload["selected_route_ids"]) or "none"),
        "",
        "## Forbidden Repeat Shapes",
        "",
    ]
    lines.extend(f"- `{shape}`" for shape in payload["forbidden_repeat_shapes"])
    lines.extend(
        [
            "",
            "## Route Decisions",
            "",
            "| route | outcome | selected? | role | missing requirements | reason | next packet |",
            "| --- | --- | :---: | --- | --- | --- | --- |",
        ]
    )
    for decision in payload["route_decisions"]:
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['route_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected_as_next']} | "
            f"`{decision['track_role']}` | "
            f"{missing} | "
            f"{decision['reason']} | "
            f"`{decision['next_packet']}` |"
        )
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Recommended Next", "recommended_next"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = t536_result_to_dict(run_t536_analysis())
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T536-taf11-source-law-successor-router-v0.1.json"
        md_path = results_dir / "T536-taf11-source-law-successor-router-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
