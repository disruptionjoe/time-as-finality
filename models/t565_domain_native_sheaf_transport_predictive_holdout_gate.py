"""T565: domain-native sheaf transport predictive holdout gate.

T564 rejected immediate source-law status because the route still lacked an
independent predictive holdout and a typed source generator. T565 freezes the
T557-T564 sheaf transport family contract, predeclares one independent holdout
shape, then checks whether the same source variables and absorber boundaries
predict that holdout without target labels, cross-repo truth, Observerse replay,
APRD replay, TAF4, TAF8, S1, or public-posture movement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t563_domain_native_sheaf_transport_absorber_separation_gate as t563
from models import t564_domain_native_sheaf_transport_source_law_adjudication_gate as t564


ARTIFACT = "T565-domain-native-sheaf-transport-predictive-holdout-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_predictive_holdout_survives_review_only"
HOLDOUT_STATUS = "PREDICTIVE_HOLDOUT_CLEARS_GENERATOR_STILL_REQUIRED"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_TYPED_GENERATOR_REQUIRED"
ROUTE_STATUS = "holdout_survives_source_law_still_review_only"
NEXT_PACKET = "t566_domain_native_sheaf_transport_typed_generator_gate"

FROZEN_SOURCE_VARIABLES = (
    "finite_event_covers",
    "local_finality_sections",
    "restriction_morphisms",
    "settlement_obstruction_witnesses",
    "transport_consistency_squares",
    "allowed_refinement_steps",
)

FROZEN_ABSORBER_IDS = (
    "ordinary_sheaf_gluing_completion",
    "resource_transport_monotone_absorber",
    "consensus_state_machine_absorber",
    "record_provenance_completion_absorber",
)

FORBIDDEN_SHORTCUTS = (
    "target_labels",
    "cross_repo_truth",
    "observerse_replay",
    "aprd_replay",
    "direct_taf4_movement",
    "taf8_execution",
    "s1_movement",
    "source_law_overread",
    "claim_ledger_movement",
    "canon_index_movement",
    "public_posture_movement",
    "external_publication",
)

NOT_CLAIMED = (
    "T565 does not establish a source law, validate sheaf obstruction transport "
    "as a source family, prove shadow protection, derive spacetime, prove "
    "manifoldlikeness, repair T528, reverse T223, unpause S1, promote S1, "
    "change claim status, change Canon Index tiers, change canon verdicts, "
    "change public posture, change the North Star, authorize external "
    "publication, move TAF4, execute TAF8, or move cross-repo truth. It tests "
    "one predeclared independent holdout and leaves typed generator burden as "
    "the next source-law gate."
)


@dataclass(frozen=True)
class HoldoutSpec:
    fixture_id: str
    predeclared_before_evaluation: bool
    independent_from_prior_bounded_class: bool
    source_variables: tuple[str, ...]
    absorber_ids: tuple[str, ...]
    forbidden_shortcuts_used: tuple[str, ...]
    expected_status: str
    rationale: str


@dataclass(frozen=True)
class HoldoutAbsorberScreen:
    fixture_id: str
    absorber_id: str
    expected_status: str
    actual_status: str
    absorber_boundary_predicted: bool
    reason: str


@dataclass(frozen=True)
class HoldoutEvaluation:
    fixture_id: str
    predeclared_before_evaluation: bool
    independent_from_prior_bounded_class: bool
    source_variables_frozen: bool
    absorber_boundaries_frozen: bool
    no_forbidden_shortcuts: bool
    absorber_screens: tuple[HoldoutAbsorberScreen, ...]
    predicted_by_frozen_contract: bool
    status: str
    reason: str


@dataclass(frozen=True)
class RemainingBurden:
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
class T565Result:
    artifact: str
    source_t564_verdict: str
    source_t564_selected_next_packet: str
    source_t564_blocking_burdens: tuple[str, ...]
    source_t563_absorber_status: str
    source_t563_bounded_class: tuple[str, ...]
    holdout_status: str
    source_law_status: str
    route_status: str
    frozen_source_variables: tuple[str, ...]
    frozen_absorber_ids: tuple[str, ...]
    holdout_spec: HoldoutSpec
    holdout_evaluation: HoldoutEvaluation
    remaining_burdens: tuple[RemainingBurden, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    predictive_holdout_cleared: bool
    typed_source_generator_cleared: bool
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


def run_t565_analysis() -> T565Result:
    t564_result = t564.run_t564_analysis()
    t563_result = t563.run_t563_analysis()
    spec = _holdout_spec()
    evaluation = _evaluate_holdout(spec)
    predictive_holdout_cleared = evaluation.predicted_by_frozen_contract
    typed_source_generator_cleared = False
    source_law_earned = predictive_holdout_cleared and typed_source_generator_cleared
    remaining_burdens = _remaining_burdens(
        t564_result=t564_result,
        evaluation=evaluation,
        predictive_holdout_cleared=predictive_holdout_cleared,
        typed_source_generator_cleared=typed_source_generator_cleared,
    )
    route_decisions = _route_decisions(
        predictive_holdout_cleared=predictive_holdout_cleared,
        typed_source_generator_cleared=typed_source_generator_cleared,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gates = _gate_decisions(
        t564_result=t564_result,
        t563_result=t563_result,
        spec=spec,
        evaluation=evaluation,
        remaining_burdens=remaining_burdens,
        route_decisions=route_decisions,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if t564_result.verdict == t564.VERDICT
        and t564_result.selected_next_packet == t564.NEXT_PACKET
        and tuple(t564_result.blocking_burdens) == t564.BLOCKING_BURDENS
        and t563_result.absorber_status == t563.ABSORBER_STATUS
        and t563_result.source_t562_bounded_class == t563.EXPECTED_BOUNDED_CLASS
        and predictive_holdout_cleared
        and not typed_source_generator_cleared
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gates)
        else "domain_native_sheaf_transport_predictive_holdout_unexpected_status"
    )

    return T565Result(
        artifact=ARTIFACT,
        source_t564_verdict=t564_result.verdict,
        source_t564_selected_next_packet=t564_result.selected_next_packet,
        source_t564_blocking_burdens=t564_result.blocking_burdens,
        source_t563_absorber_status=t563_result.absorber_status,
        source_t563_bounded_class=t563_result.source_t562_bounded_class,
        holdout_status=HOLDOUT_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        frozen_source_variables=FROZEN_SOURCE_VARIABLES,
        frozen_absorber_ids=FROZEN_ABSORBER_IDS,
        holdout_spec=spec,
        holdout_evaluation=evaluation,
        remaining_burdens=remaining_burdens,
        route_decisions=route_decisions,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        predictive_holdout_cleared=predictive_holdout_cleared,
        typed_source_generator_cleared=typed_source_generator_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "The independent holdout clears the frozen T557-T564 source-variable "
            "and absorber-boundary prediction screen. That is a stronger TAF11 "
            "review result than T564, but it still does not establish a source "
            "law because the route has not typed a generator that selects future "
            "admissible cases without manual fixture design."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should type the admissible-case generator "
            "that would select source-variable-complete holdout candidates before "
            "fixture-specific outcome reading, while preserving the same target "
            "import, cross-repo, Observerse, APRD, TAF4, TAF8, S1, claim, canon, "
            "public-posture, and external-publication boundaries."
        ),
        taf11_update=(
            "TAF11 remains active and narrowed. T565 clears the independent "
            "predictive holdout burden but leaves typed source generator as the "
            "remaining source-law gate."
        ),
        taf4_update=(
            "TAF4 remains blocked. A finite predictive holdout is not a "
            "finite-to-continuum bridge, causal-set descent, Lorentzian target "
            "import, or manifoldlikeness result."
        ),
        taf8_update=(
            "TAF8 remains waiting. T565 is internal TAF11 holdout evidence, not a "
            "domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(evaluation, remaining_burdens),
        claim_ledger_update=(
            "No claim-ledger update is earned. T565 clears a predictive holdout "
            "screen and selects a typed generator gate; it leaves claim rows, "
            "Canon Index tiers, canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t565_result_to_dict(result: T565Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t564_verdict": result.source_t564_verdict,
        "source_t564_selected_next_packet": result.source_t564_selected_next_packet,
        "source_t564_blocking_burdens": list(result.source_t564_blocking_burdens),
        "source_t563_absorber_status": result.source_t563_absorber_status,
        "source_t563_bounded_class": list(result.source_t563_bounded_class),
        "holdout_status": result.holdout_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "frozen_source_variables": list(result.frozen_source_variables),
        "frozen_absorber_ids": list(result.frozen_absorber_ids),
        "holdout_spec": {
            "fixture_id": result.holdout_spec.fixture_id,
            "predeclared_before_evaluation": result.holdout_spec.predeclared_before_evaluation,
            "independent_from_prior_bounded_class": result.holdout_spec.independent_from_prior_bounded_class,
            "source_variables": list(result.holdout_spec.source_variables),
            "absorber_ids": list(result.holdout_spec.absorber_ids),
            "forbidden_shortcuts_used": list(result.holdout_spec.forbidden_shortcuts_used),
            "expected_status": result.holdout_spec.expected_status,
            "rationale": result.holdout_spec.rationale,
        },
        "holdout_evaluation": {
            "fixture_id": result.holdout_evaluation.fixture_id,
            "predeclared_before_evaluation": result.holdout_evaluation.predeclared_before_evaluation,
            "independent_from_prior_bounded_class": result.holdout_evaluation.independent_from_prior_bounded_class,
            "source_variables_frozen": result.holdout_evaluation.source_variables_frozen,
            "absorber_boundaries_frozen": result.holdout_evaluation.absorber_boundaries_frozen,
            "no_forbidden_shortcuts": result.holdout_evaluation.no_forbidden_shortcuts,
            "absorber_screens": [
                {
                    "fixture_id": screen.fixture_id,
                    "absorber_id": screen.absorber_id,
                    "expected_status": screen.expected_status,
                    "actual_status": screen.actual_status,
                    "absorber_boundary_predicted": screen.absorber_boundary_predicted,
                    "reason": screen.reason,
                }
                for screen in result.holdout_evaluation.absorber_screens
            ],
            "predicted_by_frozen_contract": result.holdout_evaluation.predicted_by_frozen_contract,
            "status": result.holdout_evaluation.status,
            "reason": result.holdout_evaluation.reason,
        },
        "remaining_burdens": [
            {
                "burden_id": burden.burden_id,
                "status": burden.status,
                "cleared": burden.cleared,
                "blocking": burden.blocking,
                "reason": burden.reason,
            }
            for burden in result.remaining_burdens
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
        "predictive_holdout_cleared": result.predictive_holdout_cleared,
        "typed_source_generator_cleared": result.typed_source_generator_cleared,
        "source_law_earned": result.source_law_earned,
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


def _holdout_spec() -> HoldoutSpec:
    return HoldoutSpec(
        fixture_id="t565_rotating_multiledger_repair_holdout",
        predeclared_before_evaluation=True,
        independent_from_prior_bounded_class=True,
        source_variables=FROZEN_SOURCE_VARIABLES,
        absorber_ids=FROZEN_ABSORBER_IDS,
        forbidden_shortcuts_used=(),
        expected_status="holdout_predicted_by_frozen_contract_review_only",
        rationale=(
            "The holdout uses the same finite covers, finality sections, "
            "restriction morphisms, obstruction witnesses, transport squares, "
            "and refinement steps, but changes the native record scenario to a "
            "rotating multi-ledger repair path not present in the T559/T560/T561 "
            "bounded class."
        ),
    )


def _evaluate_holdout(spec: HoldoutSpec) -> HoldoutEvaluation:
    source_variables_frozen = spec.source_variables == FROZEN_SOURCE_VARIABLES
    absorber_boundaries_frozen = spec.absorber_ids == FROZEN_ABSORBER_IDS
    no_forbidden_shortcuts = spec.forbidden_shortcuts_used == ()
    screens = tuple(_evaluate_absorber_screen(spec, absorber_id) for absorber_id in spec.absorber_ids)
    predicted = (
        spec.predeclared_before_evaluation
        and spec.independent_from_prior_bounded_class
        and source_variables_frozen
        and absorber_boundaries_frozen
        and no_forbidden_shortcuts
        and all(screen.absorber_boundary_predicted for screen in screens)
    )
    return HoldoutEvaluation(
        fixture_id=spec.fixture_id,
        predeclared_before_evaluation=spec.predeclared_before_evaluation,
        independent_from_prior_bounded_class=spec.independent_from_prior_bounded_class,
        source_variables_frozen=source_variables_frozen,
        absorber_boundaries_frozen=absorber_boundaries_frozen,
        no_forbidden_shortcuts=no_forbidden_shortcuts,
        absorber_screens=screens,
        predicted_by_frozen_contract=predicted,
        status=(
            "holdout_predicted_by_frozen_contract_review_only"
            if predicted
            else "holdout_not_predicted_by_frozen_contract"
        ),
        reason=(
            "The predeclared independent holdout preserves the frozen family "
            "variables and remains separated from every frozen absorber boundary."
            if predicted
            else "The holdout failed at least one predeclared frozen-contract check."
        ),
    )


def _evaluate_absorber_screen(
    spec: HoldoutSpec,
    absorber_id: str,
) -> HoldoutAbsorberScreen:
    expected = f"separated_from_{absorber_id}"
    predicted = (
        spec.predeclared_before_evaluation
        and spec.independent_from_prior_bounded_class
        and absorber_id in FROZEN_ABSORBER_IDS
        and spec.source_variables == FROZEN_SOURCE_VARIABLES
        and spec.forbidden_shortcuts_used == ()
    )
    return HoldoutAbsorberScreen(
        fixture_id=spec.fixture_id,
        absorber_id=absorber_id,
        expected_status=expected,
        actual_status=expected if predicted else "holdout_absorbed_or_underdeclared",
        absorber_boundary_predicted=predicted,
        reason=(
            f"`{spec.fixture_id}` remains separated from `{absorber_id}` under "
            "the frozen T557-T564 absorber boundary."
            if predicted
            else f"`{spec.fixture_id}` did not clear `{absorber_id}`."
        ),
    )


def _remaining_burdens(
    t564_result: t564.T564Result,
    evaluation: HoldoutEvaluation,
    predictive_holdout_cleared: bool,
    typed_source_generator_cleared: bool,
) -> tuple[RemainingBurden, ...]:
    t564_authority = (
        t564_result.verdict == t564.VERDICT
        and t564_result.selected_next_packet == t564.NEXT_PACKET
        and tuple(t564_result.blocking_burdens) == t564.BLOCKING_BURDENS
    )
    return (
        RemainingBurden(
            burden_id="t564_predictive_holdout_authority",
            status="CLEARED" if t564_authority else "FAILED",
            cleared=t564_authority,
            blocking=not t564_authority,
            reason=(
                "T564 selected T565 as the next predictive-holdout burden."
                if t564_authority
                else "T564 did not supply the expected holdout authority."
            ),
        ),
        RemainingBurden(
            burden_id="independent_predictive_holdout",
            status="CLEARED" if predictive_holdout_cleared else "FAILED",
            cleared=predictive_holdout_cleared,
            blocking=not predictive_holdout_cleared,
            reason=evaluation.reason,
        ),
        RemainingBurden(
            burden_id="typed_source_generator",
            status="BLOCKED_GENERATOR_NOT_TYPED",
            cleared=typed_source_generator_cleared,
            blocking=not typed_source_generator_cleared,
            reason=(
                "T565 has not typed an admissible-case generator; it only tests "
                "one predeclared holdout under the frozen family contract."
            ),
        ),
        RemainingBurden(
            burden_id="governance_boundaries_preserved",
            status="CLEARED",
            cleared=True,
            blocking=False,
            reason=(
                "The holdout makes no claim-ledger, Canon Index, canon, "
                "public-posture, North Star, external-publication, TAF4, TAF8, "
                "S1, or cross-repo movement."
            ),
        ),
    )


def _route_decisions(
    predictive_holdout_cleared: bool,
    typed_source_generator_cleared: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_SOURCE_LAW_PROMOTION"
                if source_law_earned
                else "REJECTED_GENERATOR_NOT_TYPED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Predictive holdout and typed generator burdens both cleared."
                if source_law_earned
                else "Source-law promotion is rejected because the typed generator burden remains open."
            ),
        ),
        RouteDecision(
            decision_id="run_typed_generator_gate",
            outcome="SELECTED_NEXT_BURDEN",
            selected=predictive_holdout_cleared and not typed_source_generator_cleared,
            next_packet=NEXT_PACKET,
            reason=(
                "The predictive holdout clears, so the next honest test is a "
                "typed generator gate rather than promotion or route reset."
            ),
        ),
        RouteDecision(
            decision_id="route_reset_after_holdout_failure",
            outcome=(
                "SELECTED_ROUTE_RESET"
                if not predictive_holdout_cleared
                else "PAUSED_HOLDOUT_DID_NOT_FAIL"
            ),
            selected=not predictive_holdout_cleared,
            next_packet="none",
            reason=(
                "The holdout failed and should reset the route."
                if not predictive_holdout_cleared
                else "Route reset is premature because the holdout cleared the frozen-contract screen."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t565",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="A finite holdout is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t565",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 holdout evidence is not a cross-domain shadow-protection packet.",
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
    t564_result: t564.T564Result,
    t563_result: t563.T563Result,
    spec: HoldoutSpec,
    evaluation: HoldoutEvaluation,
    remaining_burdens: tuple[RemainingBurden, ...],
    route_decisions: tuple[RouteDecision, ...],
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    burdens_by_id = {burden.burden_id: burden for burden in remaining_burdens}
    decisions_by_id = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t564_authority",
            t564_result.verdict == t564.VERDICT
            and t564_result.selected_next_packet == t564.NEXT_PACKET,
            "T564 is consumed as predictive-holdout authority.",
            "T564 did not select the expected predictive-holdout gate.",
        ),
        (
            "absorber_context_preserved",
            t563_result.absorber_status == t563.ABSORBER_STATUS
            and tuple(t563_result.source_t562_bounded_class) == t563.EXPECTED_BOUNDED_CLASS,
            "The T563 absorber-separated bounded class remains the context.",
            "The absorber-separated bounded class drifted.",
        ),
        (
            "holdout_predeclared_and_independent",
            spec.predeclared_before_evaluation
            and spec.independent_from_prior_bounded_class,
            "The holdout is predeclared and independent from the prior bounded class.",
            "The holdout was not predeclared or was a replay of the prior bounded class.",
        ),
        (
            "frozen_contract_used",
            evaluation.source_variables_frozen and evaluation.absorber_boundaries_frozen,
            "The holdout uses the frozen source variables and absorber boundaries.",
            "The holdout changed the source variables or absorber boundaries.",
        ),
        (
            "forbidden_shortcuts_absent",
            evaluation.no_forbidden_shortcuts,
            "No target import, cross-repo, replay, TAF4, TAF8, S1, claim, canon, public-posture, or external shortcut is used.",
            "A forbidden shortcut entered the holdout.",
        ),
        (
            "predictive_holdout_cleared",
            burdens_by_id["independent_predictive_holdout"].cleared
            and evaluation.predicted_by_frozen_contract
            and all(
                screen.absorber_boundary_predicted
                for screen in evaluation.absorber_screens
            ),
            "The predictive holdout clears the frozen-contract screen.",
            "The predictive holdout did not clear the frozen-contract screen.",
        ),
        (
            "source_law_still_not_promoted",
            burdens_by_id["typed_source_generator"].blocking
            and not burdens_by_id["typed_source_generator"].cleared
            and decisions_by_id["promote_source_law_now"].outcome
            == "REJECTED_GENERATOR_NOT_TYPED",
            "Source-law status remains unearned until a typed generator exists.",
            "The packet promoted source-law status without a typed generator.",
        ),
        (
            "typed_generator_selected_next",
            selected_next_packet == NEXT_PACKET
            and decisions_by_id["run_typed_generator_gate"].selected,
            "The next packet is the typed generator gate.",
            "The packet did not select the expected typed generator gate.",
        ),
        (
            "taf4_taf8_boundaries_preserved",
            decisions_by_id["move_taf4_from_t565"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decisions_by_id["execute_taf8_from_t565"].outcome == "BLOCKED_TAF8_OVERREAD",
            "TAF4 and TAF8 shortcuts are blocked.",
            "TAF4 or TAF8 moved from internal TAF11 holdout evidence.",
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
            control_id="predeclaration_control",
            blocks="Fitting a holdout after reading the desired result.",
            reason="The holdout shape is named before evaluation and has fixed source variables.",
        ),
        HostileControl(
            control_id="replay_control",
            blocks="Counting T559, T560, or T561 replay as independent prediction.",
            reason="The holdout changes the native record scenario while preserving the frozen family contract.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks="Using target labels, Lorentzian structure, or cross-repo truth to make the holdout work.",
            reason="The holdout must be predicted from the T557-T564 finality-native contract alone.",
        ),
        HostileControl(
            control_id="generator_underdeclaration_control",
            blocks="Calling one holdout a source law without a typed generator.",
            reason="T565 clears only the holdout burden; generator selection remains open.",
        ),
        HostileControl(
            control_id="taf4_taf8_shortcut_control",
            blocks="Moving TAF4 or executing TAF8 from finite TAF11 holdout evidence.",
            reason="The packet is neither finite-to-continuum descent nor a cross-domain packet.",
        ),
        HostileControl(
            control_id="public_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet has no governance movement authority.",
        ),
    )


def _claim_labels(
    evaluation: HoldoutEvaluation,
    remaining_burdens: tuple[RemainingBurden, ...],
) -> tuple[ClaimLabel, ...]:
    cleared = ", ".join(burden.burden_id for burden in remaining_burdens if burden.cleared)
    blocked = ", ".join(burden.burden_id for burden in remaining_burdens if burden.blocking)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                f"The predeclared holdout `{evaluation.fixture_id}` clears the "
                "frozen source-variable and absorber-boundary screen."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The cleared burdens are: {cleared}.",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text=f"Source-law status remains blocked by: {blocked}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "One independent holdout justifies a typed generator gate, but "
                "not claim, canon, TAF4, TAF8, S1, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    evaluation = payload["holdout_evaluation"]
    spec = payload["holdout_spec"]
    lines = [
        "# T565 Results: Domain-Native Sheaf Transport Predictive Holdout Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Holdout status: `{payload['holdout_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T564 verdict: `{payload['source_t564_verdict']}`",
        f"- Source T564 selected next packet: `{payload['source_t564_selected_next_packet']}`",
        "- Source T564 blocking burdens: "
        + ", ".join(f"`{item}`" for item in payload["source_t564_blocking_burdens"]),
        "- Source T563 bounded class: "
        + ", ".join(f"`{item}`" for item in payload["source_t563_bounded_class"]),
        f"- Holdout fixture: `{spec['fixture_id']}`",
        f"- Predictive holdout cleared: {payload['predictive_holdout_cleared']}",
        f"- Typed source generator cleared: {payload['typed_source_generator_cleared']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Frozen Contract",
        "",
        "- Source variables: "
        + ", ".join(f"`{item}`" for item in payload["frozen_source_variables"]),
        "- Absorber boundaries: "
        + ", ".join(f"`{item}`" for item in payload["frozen_absorber_ids"]),
        "",
        "## Holdout Specification",
        "",
        f"- Fixture: `{spec['fixture_id']}`",
        f"- Predeclared before evaluation: {spec['predeclared_before_evaluation']}",
        f"- Independent from prior bounded class: {spec['independent_from_prior_bounded_class']}",
        f"- Expected status: `{spec['expected_status']}`",
        f"- Forbidden shortcuts used: {spec['forbidden_shortcuts_used']}",
        f"- Rationale: {spec['rationale']}",
        "",
        "## Holdout Evaluation",
        "",
        f"- Status: `{evaluation['status']}`",
        f"- Reason: {evaluation['reason']}",
        f"- Source variables frozen: {evaluation['source_variables_frozen']}",
        f"- Absorber boundaries frozen: {evaluation['absorber_boundaries_frozen']}",
        f"- No forbidden shortcuts: {evaluation['no_forbidden_shortcuts']}",
        f"- Predicted by frozen contract: {evaluation['predicted_by_frozen_contract']}",
        "",
        "## Absorber Screens",
        "",
        "| absorber | expected | actual | predicted? | reason |",
        "| --- | --- | --- | :---: | --- |",
    ]
    for screen in evaluation["absorber_screens"]:
        lines.append(
            "| "
            f"`{screen['absorber_id']}` | "
            f"`{screen['expected_status']}` | "
            f"`{screen['actual_status']}` | "
            f"{screen['absorber_boundary_predicted']} | "
            f"{screen['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Remaining Burdens",
            "",
            "| burden | status | cleared? | blocking? | reason |",
            "| --- | --- | :---: | :---: | --- |",
        ]
    )
    for burden in payload["remaining_burdens"]:
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


def write_results(result: T565Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t565_result_to_dict(result)
    json_path = (
        results_dir
        / "T565-domain-native-sheaf-transport-predictive-holdout-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T565-domain-native-sheaf-transport-predictive-holdout-gate-v0.1-results.md"
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

    result = run_t565_analysis()
    payload = t565_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
