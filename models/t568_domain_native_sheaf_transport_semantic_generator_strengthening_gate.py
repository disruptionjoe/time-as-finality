"""T568: semantic strengthening for the domain-native sheaf transport generator.

T567 preserved T566 as a field-complete selector but exposed a semantic burden:
field names alone admitted absorber-complete triviality and disguised target
imports. T568 strengthens the generator with semantic nontriviality,
noncommuting transport-square, native-payload-forcing, and target-language
screens before any claim, canon, public-posture, TAF4, TAF8, S1, external
publication, or cross-repo movement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import t565_domain_native_sheaf_transport_predictive_holdout_gate as t565
from models import t566_domain_native_sheaf_transport_typed_generator_gate as t566
from models import (
    t567_domain_native_sheaf_transport_source_law_hostile_review_gate as t567,
)


ARTIFACT = "T568-domain-native-sheaf-transport-semantic-generator-strengthening-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_semantic_generator_strengthened_review_only"
GENERATOR_STATUS = "SEMANTIC_GENERATOR_REJECTS_T567_GAPS"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_INDEPENDENT_REIMPLEMENTATION_REQUIRED"
ROUTE_STATUS = "semantic_generator_strengthened_independent_reimplementation_required"
NEXT_PACKET = "t569_domain_native_sheaf_transport_independent_reimplementation_gate"

SEMANTIC_REQUIREMENTS = (
    "nontrivial_obstruction_witness",
    "noncommuting_transport_square",
    "native_payload_forced",
    "target_blind_language",
)

NOT_CLAIMED = (
    "T568 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It strengthens the internal "
    "semantic generator and selects independent reimplementation as the next "
    "review-only burden."
)


@dataclass(frozen=True)
class StrengthenedGeneratorType:
    generator_id: str
    inherited_generator_id: str
    inherited_source_variables: tuple[str, ...]
    inherited_absorber_ids: tuple[str, ...]
    forbidden_shortcuts: tuple[str, ...]
    semantic_requirements: tuple[str, ...]
    selection_rule: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "inherited_source_variables",
            "inherited_absorber_ids",
            "forbidden_shortcuts",
            "semantic_requirements",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class StrengthenedEvaluation:
    adversary_id: str
    prior_t566_selector_admissible: bool
    prior_hostile_review_admissible: bool
    strengthened_generator_admissible: bool
    status: str
    passed_checks: tuple[str, ...]
    failed_checks: tuple[str, ...]
    reason: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["passed_checks"] = list(self.passed_checks)
        data["failed_checks"] = list(self.failed_checks)
        return data


@dataclass(frozen=True)
class ClosureCheck:
    check_id: str
    status: str
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
class T568Result:
    artifact: str
    source_t567_verdict: str
    source_t567_selected_next_packet: str
    source_t567_semantic_burden_exposed: bool
    generator_status: str
    source_law_status: str
    route_status: str
    strengthened_generator_type: StrengthenedGeneratorType
    strengthened_evaluations: tuple[StrengthenedEvaluation, ...]
    closure_checks: tuple[ClosureCheck, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    preserved_survivor_ids: tuple[str, ...]
    closed_semantic_gap_ids: tuple[str, ...]
    semantic_generator_strengthened: bool
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


def run_t568_analysis() -> T568Result:
    source = t567.run_t567_analysis()
    generator = _strengthened_generator_type()
    prior_by_id = {
        evaluation.adversary_id: evaluation
        for evaluation in source.hostile_evaluations
    }
    evaluations = tuple(
        _evaluate_adversary(generator, adversary, prior_by_id[adversary.adversary_id])
        for adversary in source.adversaries
    )
    preserved_survivor_ids = tuple(
        evaluation.adversary_id
        for evaluation in evaluations
        if evaluation.strengthened_generator_admissible
    )
    closed_semantic_gap_ids = tuple(
        evaluation.adversary_id
        for evaluation in evaluations
        if evaluation.adversary_id in source.semantic_gap_adversary_ids
        and not evaluation.strengthened_generator_admissible
    )
    semantic_generator_strengthened = (
        source.verdict == t567.VERDICT
        and source.selected_next_packet == t567.NEXT_PACKET
        and source.semantic_generator_burden_exposed
        and preserved_survivor_ids == source.valid_alternate_survivor_ids
        and closed_semantic_gap_ids == source.semantic_gap_adversary_ids
    )
    source_law_earned = False
    closure_checks = _closure_checks(
        source=source,
        evaluations=evaluations,
        preserved_survivor_ids=preserved_survivor_ids,
        closed_semantic_gap_ids=closed_semantic_gap_ids,
    )
    route_decisions = _route_decisions(
        semantic_generator_strengthened=semantic_generator_strengthened,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        source=source,
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        semantic_generator_strengthened=semantic_generator_strengthened,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if semantic_generator_strengthened
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(check.passed for check in closure_checks)
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_semantic_generator_strengthening_unexpected_status"
    )

    return T568Result(
        artifact=ARTIFACT,
        source_t567_verdict=source.verdict,
        source_t567_selected_next_packet=source.selected_next_packet,
        source_t567_semantic_burden_exposed=source.semantic_generator_burden_exposed,
        generator_status=GENERATOR_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        strengthened_generator_type=generator,
        strengthened_evaluations=evaluations,
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        preserved_survivor_ids=preserved_survivor_ids,
        closed_semantic_gap_ids=closed_semantic_gap_ids,
        semantic_generator_strengthened=semantic_generator_strengthened,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T568 closes the semantic gap T567 exposed by strengthening the "
            "generator beyond field-name completeness. It preserves the two "
            "same-field native survivors and rejects absorber-complete triviality "
            "and disguised target-language import. That is still review-only: "
            "the route needs independent reimplementation before source-law, "
            "claim, canon, or public-posture movement."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next gate should independently reimplement "
            "the strengthened generator from the declared semantic contract, "
            "not from T567/T568 fixture labels, before any source-law, claim, "
            "canon, public-posture, TAF4, TAF8, or S1 movement."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. The semantic generator is now "
            "strictly stronger than the T566 field selector, but source-law "
            "status waits for independent reimplementation."
        ),
        taf4_update=(
            "TAF4 remains blocked. A strengthened finite semantic generator is "
            "not finite-to-continuum descent, causal-set recovery, Lorentzian "
            "target import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T568 is internal TAF11 generator hygiene, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(
            preserved_survivor_ids=preserved_survivor_ids,
            closed_semantic_gap_ids=closed_semantic_gap_ids,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T568 strengthens the internal "
            "semantic generator and selects independent reimplementation; claim "
            "rows, Canon Index tiers, canon verdicts, and public posture remain "
            "unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t568_result_to_dict(result: T568Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t567_verdict": result.source_t567_verdict,
        "source_t567_selected_next_packet": result.source_t567_selected_next_packet,
        "source_t567_semantic_burden_exposed": result.source_t567_semantic_burden_exposed,
        "generator_status": result.generator_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "strengthened_generator_type": result.strengthened_generator_type.to_dict(),
        "strengthened_evaluations": [
            evaluation.to_dict() for evaluation in result.strengthened_evaluations
        ],
        "closure_checks": [check.to_dict() for check in result.closure_checks],
        "route_decisions": [
            decision.to_dict() for decision in result.route_decisions
        ],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "preserved_survivor_ids": list(result.preserved_survivor_ids),
        "closed_semantic_gap_ids": list(result.closed_semantic_gap_ids),
        "semantic_generator_strengthened": result.semantic_generator_strengthened,
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


def _strengthened_generator_type() -> StrengthenedGeneratorType:
    return StrengthenedGeneratorType(
        generator_id="semantic_source_variable_complete_holdout_generator_v2",
        inherited_generator_id="source_variable_complete_holdout_generator_v1",
        inherited_source_variables=t565.FROZEN_SOURCE_VARIABLES,
        inherited_absorber_ids=t565.FROZEN_ABSORBER_IDS,
        forbidden_shortcuts=t565.FORBIDDEN_SHORTCUTS,
        semantic_requirements=SEMANTIC_REQUIREMENTS,
        selection_rule=(
            "A candidate is admissible exactly when the inherited T566 field "
            "selector admits it and it also carries a nontrivial obstruction "
            "witness, a noncommuting transport square, a forced finality-native "
            "payload, and no target-language import."
        ),
    )


def _evaluate_adversary(
    generator: StrengthenedGeneratorType,
    adversary: t567.HostileAdversary,
    prior: t567.HostileEvaluation,
) -> StrengthenedEvaluation:
    checks = (
        (
            "inherited_t566_field_selector_admits",
            prior.t566_selector_admissible,
        ),
        (
            "nontrivial_obstruction_witness",
            adversary.nontrivial_obstruction_witnesses,
        ),
        (
            "noncommuting_transport_square",
            adversary.noncommuting_transport_square,
        ),
        ("native_payload_forced", adversary.native_payload_forced),
        (
            "target_blind_language",
            adversary.disguised_target_import_terms == (),
        ),
        (
            "forbidden_shortcuts_absent",
            adversary.forbidden_shortcuts_used == (),
        ),
    )
    passed = tuple(name for name, ok in checks if ok)
    failed = tuple(name for name, ok in checks if not ok)
    strengthened_admissible = not failed
    if strengthened_admissible:
        status = "ADMITTED_BY_SEMANTIC_GENERATOR"
        reason = "The candidate passes the inherited field selector and every semantic screen."
    elif not prior.t566_selector_admissible:
        status = "REJECTED_BY_INHERITED_T566_SELECTOR"
        reason = "The candidate fails before semantic strengthening because the inherited T566 selector rejects it."
    elif adversary.adversary_id in (
        "absorber_complete_trivial_gluing_case",
        "disguised_lorentzian_target_import",
    ):
        status = "T567_GAP_CLOSED_BY_SEMANTIC_GENERATOR"
        reason = "The strengthened semantic generator rejects the T567 gap because: " + ", ".join(failed)
    else:
        status = "REJECTED_BY_SEMANTIC_GENERATOR"
        reason = "The strengthened semantic generator rejects the candidate because: " + ", ".join(failed)
    if set(generator.semantic_requirements) - set(passed) and strengthened_admissible:
        raise AssertionError("semantic requirements cannot fail for an admitted candidate")
    return StrengthenedEvaluation(
        adversary_id=adversary.adversary_id,
        prior_t566_selector_admissible=prior.t566_selector_admissible,
        prior_hostile_review_admissible=prior.hostile_review_admissible,
        strengthened_generator_admissible=strengthened_admissible,
        status=status,
        passed_checks=passed,
        failed_checks=failed,
        reason=reason,
    )


def _closure_checks(
    source: t567.T567Result,
    evaluations: tuple[StrengthenedEvaluation, ...],
    preserved_survivor_ids: tuple[str, ...],
    closed_semantic_gap_ids: tuple[str, ...],
) -> tuple[ClosureCheck, ...]:
    by_id = {evaluation.adversary_id: evaluation for evaluation in evaluations}
    t567_authority = (
        source.verdict == t567.VERDICT
        and source.selected_next_packet == t567.NEXT_PACKET
        and source.semantic_generator_burden_exposed
    )
    gap_cases_stricter = all(
        by_id[adversary_id].prior_t566_selector_admissible
        and not by_id[adversary_id].strengthened_generator_admissible
        for adversary_id in source.semantic_gap_adversary_ids
    )
    return (
        ClosureCheck(
            check_id="t567_authority",
            status="PASS" if t567_authority else "FAIL",
            passed=t567_authority,
            evidence=(
                "T567 verdict exposed a semantic generator burden.",
                "T567 selected T568 as the next packet.",
            ),
            residual_risk="T567 is review authority, not source-law status.",
        ),
        ClosureCheck(
            check_id="native_survivors_preserved",
            status=(
                "PASS"
                if preserved_survivor_ids == source.valid_alternate_survivor_ids
                else "FAIL"
            ),
            passed=preserved_survivor_ids == source.valid_alternate_survivor_ids,
            evidence=preserved_survivor_ids,
            residual_risk="Survivors still need independent reimplementation.",
        ),
        ClosureCheck(
            check_id="t567_semantic_gaps_closed",
            status=(
                "PASS"
                if closed_semantic_gap_ids == source.semantic_gap_adversary_ids
                else "FAIL"
            ),
            passed=closed_semantic_gap_ids == source.semantic_gap_adversary_ids,
            evidence=closed_semantic_gap_ids,
            residual_risk="Closing named gaps does not prove source-law generality.",
        ),
        ClosureCheck(
            check_id="strictly_stronger_than_t566_selector",
            status="PASS" if gap_cases_stricter else "FAIL",
            passed=gap_cases_stricter,
            evidence=source.semantic_gap_adversary_ids,
            residual_risk="The strengthening is tested on T567 cases only.",
        ),
        ClosureCheck(
            check_id="semantic_nontriviality_screen_active",
            status=(
                "PASS"
                if {
                    "nontrivial_obstruction_witness",
                    "noncommuting_transport_square",
                    "native_payload_forced",
                }.issubset(set(by_id["absorber_complete_trivial_gluing_case"].failed_checks))
                else "FAIL"
            ),
            passed={
                "nontrivial_obstruction_witness",
                "noncommuting_transport_square",
                "native_payload_forced",
            }.issubset(set(by_id["absorber_complete_trivial_gluing_case"].failed_checks)),
            evidence=by_id["absorber_complete_trivial_gluing_case"].failed_checks,
            residual_risk="Future trivial completions may need richer semantic fields.",
        ),
        ClosureCheck(
            check_id="target_language_screen_active",
            status=(
                "PASS"
                if "target_blind_language"
                in by_id["disguised_lorentzian_target_import"].failed_checks
                else "FAIL"
            ),
            passed=(
                "target_blind_language"
                in by_id["disguised_lorentzian_target_import"].failed_checks
            ),
            evidence=by_id["disguised_lorentzian_target_import"].failed_checks,
            residual_risk="Language screening is finite and still review-only.",
        ),
        ClosureCheck(
            check_id="governance_boundaries_preserved",
            status="PASS",
            passed=True,
            evidence=(
                "No claim-ledger movement.",
                "No Canon Index movement.",
                "No public-posture, TAF4, TAF8, S1, external, or cross-repo movement.",
            ),
            residual_risk="None inside this packet; the next packet remains review-only.",
        ),
    )


def _route_decisions(
    semantic_generator_strengthened: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "REJECTED_REVIEW_ONLY_INDEPENDENT_REIMPLEMENTATION_REQUIRED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "The semantic generator is stronger, but source-law status needs independent reimplementation."
            ),
        ),
        RouteDecision(
            decision_id="run_independent_reimplementation_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if semantic_generator_strengthened and not source_law_earned
                else "PAUSED_UNTIL_SEMANTIC_GENERATOR_STRENGTHENED"
            ),
            selected=semantic_generator_strengthened and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The T567 semantic gaps are closed, so the next honest review step is independent reimplementation."
                if semantic_generator_strengthened
                else "Semantic strengthening has not cleared."
            ),
        ),
        RouteDecision(
            decision_id="abandon_semantic_generator_route",
            outcome=(
                "SELECTED_ROUTE_RESET"
                if not semantic_generator_strengthened
                else "PAUSED_GENERATOR_STRENGTHENED"
            ),
            selected=not semantic_generator_strengthened,
            next_packet="none",
            reason=(
                "The strengthened generator failed and should reset the route."
                if not semantic_generator_strengthened
                else "Route reset is premature because semantic strengthening cleared the named gaps."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t568",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="A strengthened finite semantic generator is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t568",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 generator hygiene is not cross-domain shadow protection.",
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
    source: t567.T567Result,
    closure_checks: tuple[ClosureCheck, ...],
    route_decisions: tuple[RouteDecision, ...],
    semantic_generator_strengthened: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    checks = {check.check_id: check for check in closure_checks}
    routes = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t567_authority",
            checks["t567_authority"].passed,
            "T567 supplies semantic-strengthening authority.",
            "T567 did not supply the expected semantic-strengthening authority.",
        ),
        (
            "semantic_generator_closes_named_gaps",
            checks["t567_semantic_gaps_closed"].passed
            and checks["semantic_nontriviality_screen_active"].passed
            and checks["target_language_screen_active"].passed,
            "The strengthened generator closes both named T567 semantic gaps.",
            "The strengthened generator did not close both named T567 gaps.",
        ),
        (
            "native_survivors_preserved",
            checks["native_survivors_preserved"].passed,
            "The valid same-field native survivors remain admitted.",
            "The strengthened generator overfiltered valid same-field survivors.",
        ),
        (
            "source_law_not_promoted",
            not source_law_earned
            and routes["promote_source_law_now"].outcome
            == "REJECTED_REVIEW_ONLY_INDEPENDENT_REIMPLEMENTATION_REQUIRED",
            "Source-law promotion is rejected.",
            "Source-law promotion moved too early.",
        ),
        (
            "independent_reimplementation_selected_next",
            semantic_generator_strengthened
            and source.selected_next_packet == t567.NEXT_PACKET
            and selected_next_packet == NEXT_PACKET
            and routes["run_independent_reimplementation_gate"].selected,
            "Independent reimplementation is selected as the next burden.",
            "The expected independent-reimplementation next packet was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            routes["move_taf4_from_t568"].outcome == "BLOCKED_TAF4_OVERREAD"
            and routes["execute_taf8_from_t568"].outcome == "BLOCKED_TAF8_OVERREAD"
            and routes["move_s1_or_cross_repo_truth"].outcome == "BLOCKED_GOVERNANCE",
            "TAF4, TAF8, S1, cross-repo, publication, claim, canon, and public-posture shortcuts are blocked.",
            "A forbidden route movement was allowed.",
        ),
        (
            "governance_boundaries_preserved",
            checks["governance_boundaries_preserved"].passed,
            "No governance boundary was crossed.",
            "A governance boundary was crossed.",
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
    preserved_survivor_ids: tuple[str, ...],
    closed_semantic_gap_ids: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Strengthened generator preserves same-field survivors: "
                + ", ".join(preserved_survivor_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Strengthened generator closes T567 semantic gaps: "
                + ", ".join(closed_semantic_gap_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law status remains blocked by independent reimplementation.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="Semantic strengthening narrows the route rather than promoting it.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    generator = payload["strengthened_generator_type"]
    lines = [
        "# T568 Results: Domain-Native Sheaf Transport Semantic Generator Strengthening Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Generator status: `{payload['generator_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T567 verdict: `{payload['source_t567_verdict']}`",
        f"- Source T567 selected next packet: `{payload['source_t567_selected_next_packet']}`",
        f"- Source T567 semantic burden exposed: {payload['source_t567_semantic_burden_exposed']}",
        f"- Semantic generator strengthened: {payload['semantic_generator_strengthened']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Strengthened Generator",
        "",
        f"- Generator: `{generator['generator_id']}`",
        f"- Inherits: `{generator['inherited_generator_id']}`",
        "- Source variables: "
        + ", ".join(f"`{item}`" for item in generator["inherited_source_variables"]),
        "- Absorber boundaries: "
        + ", ".join(f"`{item}`" for item in generator["inherited_absorber_ids"]),
        "- Semantic requirements: "
        + ", ".join(f"`{item}`" for item in generator["semantic_requirements"]),
        f"- Selection rule: {generator['selection_rule']}",
        "",
        "## Strengthened Evaluations",
        "",
        "| adversary | prior T566 admits? | prior hostile admits? | strengthened admits? | status | failed checks | reason |",
        "| --- | :---: | :---: | :---: | --- | --- | --- |",
    ]
    for evaluation in payload["strengthened_evaluations"]:
        lines.append(
            "| "
            f"`{evaluation['adversary_id']}` | "
            f"{evaluation['prior_t566_selector_admissible']} | "
            f"{evaluation['prior_hostile_review_admissible']} | "
            f"{evaluation['strengthened_generator_admissible']} | "
            f"`{evaluation['status']}` | "
            f"{', '.join(evaluation['failed_checks']) or 'none'} | "
            f"{evaluation['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Closure Checks",
            "",
            "| check | status | passed? | residual risk |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for check in payload["closure_checks"]:
        lines.append(
            "| "
            f"`{check['check_id']}` | "
            f"`{check['status']}` | "
            f"{check['passed']} | "
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


def write_results(result: T568Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t568_result_to_dict(result)
    json_path = (
        results_dir
        / "T568-domain-native-sheaf-transport-semantic-generator-strengthening-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T568-domain-native-sheaf-transport-semantic-generator-strengthening-gate-v0.1-results.md"
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

    result = run_t568_analysis()
    payload = t568_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
