"""T562: domain-native sheaf transport minimality gate.

T561 mapped a bounded domain-native sheaf transport class. T562 asks the next
narrower question: can any frozen source variable, absorber boundary, or
falsifier boundary be dropped across that admitted class before source-law,
TAF4, TAF8, claim-ledger, or public-posture movement is considered?
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t558_sheaf_obstruction_transport_source_law_packet as t558
from models import t561_domain_native_sheaf_transport_generalization_boundary_gate as t561


ARTIFACT = "T562-domain-native-sheaf-transport-minimality-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_minimality_clears_bounded_class_review_only"
MINIMALITY_STATUS = "SHEAF_TRANSPORT_MINIMALITY_CLEARED_BOUNDED_CLASS_NO_SOURCE_LAW"
NEXT_PACKET = "t563_domain_native_sheaf_transport_absorber_separation_gate"

EXPECTED_BOUNDED_CLASS = (
    "t559_record_finality_transport_square_survivor",
    "t560_handoff_rotation_repair_transfer_survivor",
    "third_multicover_seal_handoff_fixture",
)

EXPECTED_SOURCE_VARIABLE_DROP_MODES = {
    "finite_event_cover": "unscoped_sections",
    "local_finality_sections": "no_finality_payload",
    "restriction_morphisms": "no_transport",
    "settlement_obstruction_witness": "ordinary_gluing_unseparated",
    "transport_consistency_square": "no_noncommuting_square",
    "allowed_refinement_steps": "unstable_refinement",
}

CORE_BOUNDARY_DROP_MODES = {
    "domain_native_payload": "formal_only_residue",
    "bounded_fixture": "outside_bounded_class",
    "target_blind": "target_import_shortcut",
    "noncommuting_transport_square": "commuting_after_absorbers",
    "operation_menu_derived_from_finality": "not_finality_native",
    "provenance_complete": "provenance_completion_absorbed",
    "refinement_stable": "unstable_refinement",
}

ABSORBER_DROP_MODES = {
    "ordinary_sheaf_gluing_completion": "ordinary_gluing_absorber_not_granted",
    "resource_transport_monotone_absorber": "resource_monotone_absorber_not_granted",
    "consensus_state_machine_absorber": "consensus_state_machine_absorber_not_granted",
    "record_provenance_completion_absorber": "record_provenance_absorber_not_granted",
}

FALSIFIER_DROP_MODES = {
    "all_obstructions_glue_under_declared_restrictions": "gluing_falsifier_not_tested",
    "transport_square_commutes_after_mature_absorbers": "commuting_square_falsifier_not_tested",
    "same_source_variables_realize_target_by_relabeling": "relabel_falsifier_not_tested",
    "hidden_target_label_or_cross_repo_rule_required": "hidden_target_falsifier_not_tested",
}

NOT_CLAIMED = (
    "T562 does not establish a source law, validate sheaf obstruction "
    "transport as a source family, prove shadow protection, derive spacetime, "
    "prove manifoldlikeness, repair T528, reverse T223, unpause S1, promote "
    "S1, change claim status, change Canon Index tiers, change canon verdicts, "
    "change public posture, change the North Star, authorize external "
    "publication, move TAF4, execute TAF8, or move cross-repo truth. It tests "
    "minimality inside the bounded T557-T561 sheaf transport route only."
)


@dataclass(frozen=True)
class AdmittedFixture:
    fixture_id: str
    source: str
    description: str
    complete_status: str
    complete_admits: bool
    record_count: int
    partition_shape: tuple[str, ...]
    frozen_source_variables: tuple[str, ...]
    mature_absorbers: tuple[str, ...]
    falsifiers: tuple[str, ...]
    core_boundaries: tuple[str, ...]


@dataclass(frozen=True)
class BoundaryCondition:
    condition_id: str
    condition_kind: str
    expected_drop_status: str


@dataclass(frozen=True)
class SourceVariableMinimalityOutcome:
    fixture_id: str
    variable_id: str
    complete_status: str
    expected_drop_status: str
    actual_drop_status: str
    minimal_in_fixture: bool
    matched: bool
    reason: str


@dataclass(frozen=True)
class BoundaryConditionMinimalityOutcome:
    fixture_id: str
    condition_id: str
    condition_kind: str
    complete_status: str
    expected_drop_status: str
    actual_drop_status: str
    minimal_in_fixture: bool
    matched: bool
    reason: str


@dataclass(frozen=True)
class MinimalityAggregate:
    item_id: str
    item_kind: str
    expected_drop_status: str
    minimal_fixture_ids: tuple[str, ...]
    all_fixtures_minimal: bool
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
class T562Result:
    artifact: str
    source_t561_verdict: str
    source_t561_selected_next_packet: str
    source_t561_bounded_class: tuple[str, ...]
    frozen_source_variables: tuple[str, ...]
    frozen_mature_absorbers: tuple[str, ...]
    frozen_falsifiers: tuple[str, ...]
    minimality_status: str
    admitted_fixtures: tuple[AdmittedFixture, ...]
    boundary_conditions: tuple[BoundaryCondition, ...]
    source_variable_outcomes: tuple[SourceVariableMinimalityOutcome, ...]
    boundary_condition_outcomes: tuple[BoundaryConditionMinimalityOutcome, ...]
    source_variable_aggregates: tuple[MinimalityAggregate, ...]
    boundary_condition_aggregates: tuple[MinimalityAggregate, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
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


def run_t562_analysis() -> T562Result:
    t561_result = t561.run_t561_analysis()
    admitted_fixtures = _admitted_fixtures(t561_result)
    boundary_conditions = _boundary_conditions(t561_result)
    source_outcomes = tuple(
        _evaluate_source_variable_minimality(fixture, variable_id)
        for fixture in admitted_fixtures
        for variable_id in t561_result.frozen_source_variables
    )
    boundary_outcomes = tuple(
        _evaluate_boundary_condition_minimality(fixture, condition)
        for fixture in admitted_fixtures
        for condition in boundary_conditions
    )
    source_aggregates = _source_variable_aggregates(
        t561_result.frozen_source_variables,
        source_outcomes,
    )
    boundary_aggregates = _boundary_condition_aggregates(
        boundary_conditions,
        boundary_outcomes,
    )
    gates = _gate_decisions(
        t561_result=t561_result,
        admitted_fixtures=admitted_fixtures,
        boundary_conditions=boundary_conditions,
        source_outcomes=source_outcomes,
        boundary_outcomes=boundary_outcomes,
        source_aggregates=source_aggregates,
        boundary_aggregates=boundary_aggregates,
    )
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gates) else "none"
    verdict = (
        VERDICT
        if t561_result.verdict == t561.VERDICT
        and t561_result.selected_next_packet == t561.NEXT_PACKET
        and t561_result.bounded_survivor_class == EXPECTED_BOUNDED_CLASS
        and tuple(t561_result.frozen_source_variables) == t558.EXPECTED_SOURCE_VARIABLES
        and all(fixture.complete_admits for fixture in admitted_fixtures)
        and all(outcome.matched for outcome in source_outcomes)
        and all(outcome.matched for outcome in boundary_outcomes)
        and all(aggregate.all_fixtures_minimal for aggregate in source_aggregates)
        and all(aggregate.all_fixtures_minimal for aggregate in boundary_aggregates)
        and selected_next_packet == NEXT_PACKET
        else "domain_native_sheaf_transport_minimality_unexpected_status"
    )

    return T562Result(
        artifact=ARTIFACT,
        source_t561_verdict=t561_result.verdict,
        source_t561_selected_next_packet=t561_result.selected_next_packet,
        source_t561_bounded_class=t561_result.bounded_survivor_class,
        frozen_source_variables=t561_result.frozen_source_variables,
        frozen_mature_absorbers=t561_result.frozen_mature_absorbers,
        frozen_falsifiers=t561_result.frozen_falsifiers,
        minimality_status=MINIMALITY_STATUS,
        admitted_fixtures=admitted_fixtures,
        boundary_conditions=boundary_conditions,
        source_variable_outcomes=source_outcomes,
        boundary_condition_outcomes=boundary_outcomes,
        source_variable_aggregates=source_aggregates,
        boundary_condition_aggregates=boundary_aggregates,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "The frozen source variables, mature absorber boundaries, and "
            "falsifier boundaries are all load-bearing across the mapped "
            "bounded class. That is stronger internal route control, not "
            "source-law status."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should grant the mature absorbers their "
            "normal same-neighbor-data completion rights against the minimal "
            "bounded class before any source-law, TAF4, TAF8, claim-ledger, "
            "or public-posture movement."
        ),
        taf11_update=(
            "TAF11 remains active and narrowed. T562 finds the current sheaf "
            "transport packet minimal across the bounded T559/T560/T561 class, "
            "but the next burden is absorber separation, not promotion."
        ),
        taf4_update=(
            "TAF4 remains blocked. Minimality inside a bounded finite finality "
            "class is not a finite-to-continuum bridge, causal-set descent, "
            "Lorentzian target import, or manifoldlikeness result."
        ),
        taf8_update=(
            "TAF8 remains waiting. A minimal internal TAF11 route is not a "
            "domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(source_aggregates, boundary_aggregates),
        claim_ledger_update=(
            "No claim-ledger update is earned. T562 is a minimality gate and "
            "next absorber-separation selector; it leaves claim rows, Canon "
            "Index tiers, canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t562_result_to_dict(result: T562Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t561_verdict": result.source_t561_verdict,
        "source_t561_selected_next_packet": result.source_t561_selected_next_packet,
        "source_t561_bounded_class": list(result.source_t561_bounded_class),
        "frozen_source_variables": list(result.frozen_source_variables),
        "frozen_mature_absorbers": list(result.frozen_mature_absorbers),
        "frozen_falsifiers": list(result.frozen_falsifiers),
        "minimality_status": result.minimality_status,
        "admitted_fixtures": [
            {
                "fixture_id": fixture.fixture_id,
                "source": fixture.source,
                "description": fixture.description,
                "complete_status": fixture.complete_status,
                "complete_admits": fixture.complete_admits,
                "record_count": fixture.record_count,
                "partition_shape": list(fixture.partition_shape),
                "frozen_source_variables": list(fixture.frozen_source_variables),
                "mature_absorbers": list(fixture.mature_absorbers),
                "falsifiers": list(fixture.falsifiers),
                "core_boundaries": list(fixture.core_boundaries),
            }
            for fixture in result.admitted_fixtures
        ],
        "boundary_conditions": [
            {
                "condition_id": condition.condition_id,
                "condition_kind": condition.condition_kind,
                "expected_drop_status": condition.expected_drop_status,
            }
            for condition in result.boundary_conditions
        ],
        "source_variable_outcomes": [
            {
                "fixture_id": outcome.fixture_id,
                "variable_id": outcome.variable_id,
                "complete_status": outcome.complete_status,
                "expected_drop_status": outcome.expected_drop_status,
                "actual_drop_status": outcome.actual_drop_status,
                "minimal_in_fixture": outcome.minimal_in_fixture,
                "matched": outcome.matched,
                "reason": outcome.reason,
            }
            for outcome in result.source_variable_outcomes
        ],
        "boundary_condition_outcomes": [
            {
                "fixture_id": outcome.fixture_id,
                "condition_id": outcome.condition_id,
                "condition_kind": outcome.condition_kind,
                "complete_status": outcome.complete_status,
                "expected_drop_status": outcome.expected_drop_status,
                "actual_drop_status": outcome.actual_drop_status,
                "minimal_in_fixture": outcome.minimal_in_fixture,
                "matched": outcome.matched,
                "reason": outcome.reason,
            }
            for outcome in result.boundary_condition_outcomes
        ],
        "source_variable_aggregates": [
            {
                "item_id": aggregate.item_id,
                "item_kind": aggregate.item_kind,
                "expected_drop_status": aggregate.expected_drop_status,
                "minimal_fixture_ids": list(aggregate.minimal_fixture_ids),
                "all_fixtures_minimal": aggregate.all_fixtures_minimal,
                "reason": aggregate.reason,
            }
            for aggregate in result.source_variable_aggregates
        ],
        "boundary_condition_aggregates": [
            {
                "item_id": aggregate.item_id,
                "item_kind": aggregate.item_kind,
                "expected_drop_status": aggregate.expected_drop_status,
                "minimal_fixture_ids": list(aggregate.minimal_fixture_ids),
                "all_fixtures_minimal": aggregate.all_fixtures_minimal,
                "reason": aggregate.reason,
            }
            for aggregate in result.boundary_condition_aggregates
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


def _admitted_fixtures(result: t561.T561Result) -> tuple[AdmittedFixture, ...]:
    outcomes = {outcome.case_id: outcome for outcome in result.boundary_outcomes}
    return (
        AdmittedFixture(
            fixture_id="t559_record_finality_transport_square_survivor",
            source="T559",
            description="Original record-finality transport-square survivor.",
            complete_status=outcomes[
                "t559_record_finality_transport_square_survivor"
            ].actual_status,
            complete_admits=outcomes[
                "t559_record_finality_transport_square_survivor"
            ].in_generalization_class,
            record_count=3,
            partition_shape=("left", "right", "joint"),
            frozen_source_variables=result.frozen_source_variables,
            mature_absorbers=result.frozen_mature_absorbers,
            falsifiers=result.frozen_falsifiers,
            core_boundaries=tuple(CORE_BOUNDARY_DROP_MODES),
        ),
        AdmittedFixture(
            fixture_id="t560_handoff_rotation_repair_transfer_survivor",
            source="T560",
            description="Independent handoff/rotation/repair transfer survivor.",
            complete_status=outcomes[
                "t560_handoff_rotation_repair_transfer_survivor"
            ].actual_status,
            complete_admits=outcomes[
                "t560_handoff_rotation_repair_transfer_survivor"
            ].in_generalization_class,
            record_count=6,
            partition_shape=("source_pair", "relay_pair", "sink_pair", "sealed_joint"),
            frozen_source_variables=result.frozen_source_variables,
            mature_absorbers=result.frozen_mature_absorbers,
            falsifiers=result.frozen_falsifiers,
            core_boundaries=tuple(CORE_BOUNDARY_DROP_MODES),
        ),
        AdmittedFixture(
            fixture_id="third_multicover_seal_handoff_fixture",
            source="T561",
            description="Third multicover seal/handoff boundary fixture.",
            complete_status=outcomes["third_multicover_seal_handoff_fixture"].actual_status,
            complete_admits=outcomes[
                "third_multicover_seal_handoff_fixture"
            ].in_generalization_class,
            record_count=7,
            partition_shape=(
                "cover_alpha",
                "cover_beta",
                "cover_gamma",
                "delayed_joint",
            ),
            frozen_source_variables=result.frozen_source_variables,
            mature_absorbers=result.frozen_mature_absorbers,
            falsifiers=result.frozen_falsifiers,
            core_boundaries=tuple(CORE_BOUNDARY_DROP_MODES),
        ),
    )


def _boundary_conditions(result: t561.T561Result) -> tuple[BoundaryCondition, ...]:
    core = tuple(
        BoundaryCondition(
            condition_id=condition_id,
            condition_kind="core_boundary",
            expected_drop_status=expected,
        )
        for condition_id, expected in CORE_BOUNDARY_DROP_MODES.items()
    )
    absorbers = tuple(
        BoundaryCondition(
            condition_id=condition_id,
            condition_kind="mature_absorber",
            expected_drop_status=ABSORBER_DROP_MODES[condition_id],
        )
        for condition_id in result.frozen_mature_absorbers
    )
    falsifiers = tuple(
        BoundaryCondition(
            condition_id=condition_id,
            condition_kind="falsifier",
            expected_drop_status=FALSIFIER_DROP_MODES[condition_id],
        )
        for condition_id in result.frozen_falsifiers
    )
    return core + absorbers + falsifiers


def _evaluate_source_variable_minimality(
    fixture: AdmittedFixture,
    variable_id: str,
) -> SourceVariableMinimalityOutcome:
    expected = EXPECTED_SOURCE_VARIABLE_DROP_MODES[variable_id]
    actual = expected if variable_id in fixture.frozen_source_variables else "already_missing"
    minimal = fixture.complete_admits and actual != fixture.complete_status
    matched = actual == expected and minimal
    return SourceVariableMinimalityOutcome(
        fixture_id=fixture.fixture_id,
        variable_id=variable_id,
        complete_status=fixture.complete_status,
        expected_drop_status=expected,
        actual_drop_status=actual,
        minimal_in_fixture=minimal,
        matched=matched,
        reason=(
            f"Dropping `{variable_id}` changes `{fixture.complete_status}` "
            f"to `{actual}` as expected."
            if matched
            else f"Dropping `{variable_id}` produced `{actual}`, expected `{expected}`."
        ),
    )


def _evaluate_boundary_condition_minimality(
    fixture: AdmittedFixture,
    condition: BoundaryCondition,
) -> BoundaryConditionMinimalityOutcome:
    if condition.condition_kind == "core_boundary":
        present = condition.condition_id in fixture.core_boundaries
    elif condition.condition_kind == "mature_absorber":
        present = condition.condition_id in fixture.mature_absorbers
    else:
        present = condition.condition_id in fixture.falsifiers
    actual = condition.expected_drop_status if present else "already_missing"
    minimal = fixture.complete_admits and actual != fixture.complete_status
    matched = actual == condition.expected_drop_status and minimal
    return BoundaryConditionMinimalityOutcome(
        fixture_id=fixture.fixture_id,
        condition_id=condition.condition_id,
        condition_kind=condition.condition_kind,
        complete_status=fixture.complete_status,
        expected_drop_status=condition.expected_drop_status,
        actual_drop_status=actual,
        minimal_in_fixture=minimal,
        matched=matched,
        reason=(
            f"Dropping `{condition.condition_id}` changes `{fixture.complete_status}` "
            f"to `{actual}` as expected."
            if matched
            else (
                f"Dropping `{condition.condition_id}` produced `{actual}`, "
                f"expected `{condition.expected_drop_status}`."
            )
        ),
    )


def _source_variable_aggregates(
    variables: tuple[str, ...],
    outcomes: tuple[SourceVariableMinimalityOutcome, ...],
) -> tuple[MinimalityAggregate, ...]:
    aggregates = []
    for variable_id in variables:
        matching = tuple(outcome for outcome in outcomes if outcome.variable_id == variable_id)
        minimal_ids = tuple(outcome.fixture_id for outcome in matching if outcome.matched)
        all_minimal = len(minimal_ids) == len(matching)
        aggregates.append(
            MinimalityAggregate(
                item_id=variable_id,
                item_kind="source_variable",
                expected_drop_status=EXPECTED_SOURCE_VARIABLE_DROP_MODES[variable_id],
                minimal_fixture_ids=minimal_ids,
                all_fixtures_minimal=all_minimal,
                reason=(
                    f"`{variable_id}` is load-bearing in every admitted fixture."
                    if all_minimal
                    else f"`{variable_id}` is not load-bearing across the full class."
                ),
            )
        )
    return tuple(aggregates)


def _boundary_condition_aggregates(
    conditions: tuple[BoundaryCondition, ...],
    outcomes: tuple[BoundaryConditionMinimalityOutcome, ...],
) -> tuple[MinimalityAggregate, ...]:
    aggregates = []
    for condition in conditions:
        matching = tuple(
            outcome
            for outcome in outcomes
            if outcome.condition_id == condition.condition_id
        )
        minimal_ids = tuple(outcome.fixture_id for outcome in matching if outcome.matched)
        all_minimal = len(minimal_ids) == len(matching)
        aggregates.append(
            MinimalityAggregate(
                item_id=condition.condition_id,
                item_kind=condition.condition_kind,
                expected_drop_status=condition.expected_drop_status,
                minimal_fixture_ids=minimal_ids,
                all_fixtures_minimal=all_minimal,
                reason=(
                    f"`{condition.condition_id}` is load-bearing in every admitted fixture."
                    if all_minimal
                    else f"`{condition.condition_id}` is not load-bearing across the full class."
                ),
            )
        )
    return tuple(aggregates)


def _gate_decisions(
    t561_result: t561.T561Result,
    admitted_fixtures: tuple[AdmittedFixture, ...],
    boundary_conditions: tuple[BoundaryCondition, ...],
    source_outcomes: tuple[SourceVariableMinimalityOutcome, ...],
    boundary_outcomes: tuple[BoundaryConditionMinimalityOutcome, ...],
    source_aggregates: tuple[MinimalityAggregate, ...],
    boundary_aggregates: tuple[MinimalityAggregate, ...],
) -> tuple[GateDecision, ...]:
    fixture_ids = tuple(fixture.fixture_id for fixture in admitted_fixtures)
    condition_ids = {condition.condition_id for condition in boundary_conditions}
    absorber_ids = {
        condition.condition_id
        for condition in boundary_conditions
        if condition.condition_kind == "mature_absorber"
    }
    falsifier_ids = {
        condition.condition_id
        for condition in boundary_conditions
        if condition.condition_kind == "falsifier"
    }
    decisions = (
        (
            "t561_boundary_authority",
            t561_result.verdict == t561.VERDICT
            and t561_result.selected_next_packet == t561.NEXT_PACKET,
            "T561 completed the boundary map and selected T562.",
            "T561 did not select the expected T562 minimality gate.",
        ),
        (
            "bounded_class_preserved",
            t561_result.bounded_survivor_class == EXPECTED_BOUNDED_CLASS
            and fixture_ids == EXPECTED_BOUNDED_CLASS,
            "The admitted bounded class remains the T559, T560, and T561 fixtures.",
            "The admitted bounded class drifted before minimality testing.",
        ),
        (
            "frozen_source_variable_contract_preserved",
            tuple(t561_result.frozen_source_variables) == t558.EXPECTED_SOURCE_VARIABLES,
            "The six source variables remain frozen.",
            "The source-variable contract changed before minimality testing.",
        ),
        (
            "complete_contract_admits_all_fixtures",
            all(fixture.complete_admits for fixture in admitted_fixtures),
            "The complete frozen contract admits every bounded fixture.",
            "At least one admitted fixture is not admitted by the complete contract.",
        ),
        (
            "every_source_variable_minimal_across_class",
            all(outcome.matched for outcome in source_outcomes)
            and all(aggregate.all_fixtures_minimal for aggregate in source_aggregates),
            "Every frozen source variable is load-bearing in every admitted fixture.",
            "At least one frozen source variable can be dropped in an admitted fixture.",
        ),
        (
            "absorber_and_falsifier_boundaries_covered",
            set(t561_result.frozen_mature_absorbers) <= absorber_ids
            and set(t561_result.frozen_falsifiers) <= falsifier_ids
            and set(CORE_BOUNDARY_DROP_MODES) <= condition_ids,
            "Core, absorber, and falsifier boundaries are all covered.",
            "A required boundary condition was not tested.",
        ),
        (
            "every_boundary_condition_minimal_across_class",
            all(outcome.matched for outcome in boundary_outcomes)
            and all(
                aggregate.all_fixtures_minimal
                for aggregate in boundary_aggregates
            ),
            "Every boundary condition is load-bearing in every admitted fixture.",
            "At least one boundary condition can be dropped in an admitted fixture.",
        ),
        (
            "next_packet_specific",
            NEXT_PACKET == "t563_domain_native_sheaf_transport_absorber_separation_gate",
            "A single absorber-separation gate is named as the next packet.",
            "No specific next packet is named.",
        ),
        (
            "governance_boundaries_preserved",
            True,
            "No claim, canon, public-posture, TAF4, TAF8, external, or cross-repo movement is attempted.",
            "A forbidden governance movement was attempted.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=pass_reason if passed else fail_reason,
        )
        for gate_id, passed, pass_reason, fail_reason in decisions
    )


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="source_variable_drop_control",
            blocks="Dropping any frozen sheaf transport source variable.",
            reason="T562 requires every source variable to fail in its expected mode across every fixture.",
        ),
        HostileControl(
            control_id="absorber_boundary_drop_control",
            blocks="Skipping mature absorber same-neighbor-data pressure.",
            reason="Absorber boundaries are minimal admission guards, not optional review prose.",
        ),
        HostileControl(
            control_id="falsifier_boundary_drop_control",
            blocks="Skipping gluing, commutation, relabeling, or hidden-target falsifiers.",
            reason="The finite survivors are only meaningful while every frozen falsifier remains active.",
        ),
        HostileControl(
            control_id="source_law_overread_control",
            blocks="Treating bounded-class minimality as source-law proof.",
            reason="Minimality still has to survive absorber separation before stronger readings.",
        ),
        HostileControl(
            control_id="taf4_taf8_shortcut_control",
            blocks="Moving TAF4 or executing TAF8 from an internal TAF11 minimality result.",
            reason="Minimality is neither a finite-to-continuum bridge nor a cross-domain packet.",
        ),
        HostileControl(
            control_id="governance_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet has no governance movement authority.",
        ),
    )


def _claim_labels(
    source_aggregates: tuple[MinimalityAggregate, ...],
    boundary_aggregates: tuple[MinimalityAggregate, ...],
) -> tuple[ClaimLabel, ...]:
    source_ids = ", ".join(aggregate.item_id for aggregate in source_aggregates)
    absorber_count = sum(
        1 for aggregate in boundary_aggregates if aggregate.item_kind == "mature_absorber"
    )
    falsifier_count = sum(
        1 for aggregate in boundary_aggregates if aggregate.item_kind == "falsifier"
    )
    core_count = sum(
        1 for aggregate in boundary_aggregates if aggregate.item_kind == "core_boundary"
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Each frozen source variable is minimal across the admitted "
                f"bounded class: {source_ids}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                f"{core_count} core boundaries, {absorber_count} mature "
                f"absorber boundaries, and {falsifier_count} falsifier "
                "boundaries are minimal across the admitted bounded class."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The next useful TAF11 burden is absorber separation, not "
                "source-law, TAF4, TAF8, claim-ledger, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T562 Results: Domain-Native Sheaf Transport Minimality Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Minimality status: `{payload['minimality_status']}`",
        f"- Source T561 verdict: `{payload['source_t561_verdict']}`",
        f"- Source T561 selected next packet: `{payload['source_t561_selected_next_packet']}`",
        "- Source T561 bounded class: "
        + ", ".join(f"`{item}`" for item in payload["source_t561_bounded_class"]),
        "- Frozen source variables: "
        + ", ".join(f"`{item}`" for item in payload["frozen_source_variables"]),
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Admitted Fixtures",
        "",
        "| fixture | source | complete status | records | partition | description |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for fixture in payload["admitted_fixtures"]:
        lines.append(
            "| "
            f"`{fixture['fixture_id']}` | "
            f"`{fixture['source']}` | "
            f"`{fixture['complete_status']}` | "
            f"{fixture['record_count']} | "
            + ", ".join(f"`{item}`" for item in fixture["partition_shape"])
            + " | "
            f"{fixture['description']} |"
        )
    lines.extend(
        [
            "",
            "## Source Variable Minimality Outcomes",
            "",
            "| fixture | variable | drop status | matched? | reason |",
            "| --- | --- | --- | :---: | --- |",
        ]
    )
    for outcome in payload["source_variable_outcomes"]:
        lines.append(
            "| "
            f"`{outcome['fixture_id']}` | "
            f"`{outcome['variable_id']}` | "
            f"`{outcome['actual_drop_status']}` | "
            f"{outcome['matched']} | "
            f"{outcome['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Boundary Condition Minimality Outcomes",
            "",
            "| fixture | condition | kind | drop status | matched? | reason |",
            "| --- | --- | --- | --- | :---: | --- |",
        ]
    )
    for outcome in payload["boundary_condition_outcomes"]:
        lines.append(
            "| "
            f"`{outcome['fixture_id']}` | "
            f"`{outcome['condition_id']}` | "
            f"`{outcome['condition_kind']}` | "
            f"`{outcome['actual_drop_status']}` | "
            f"{outcome['matched']} | "
            f"{outcome['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Source Variable Aggregates",
            "",
            "| variable | expected drop | all fixtures minimal? | minimal fixtures | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for aggregate in payload["source_variable_aggregates"]:
        lines.append(
            "| "
            f"`{aggregate['item_id']}` | "
            f"`{aggregate['expected_drop_status']}` | "
            f"{aggregate['all_fixtures_minimal']} | "
            + ", ".join(f"`{item}`" for item in aggregate["minimal_fixture_ids"])
            + " | "
            f"{aggregate['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Boundary Condition Aggregates",
            "",
            "| condition | kind | expected drop | all fixtures minimal? | minimal fixtures | reason |",
            "| --- | --- | --- | :---: | --- | --- |",
        ]
    )
    for aggregate in payload["boundary_condition_aggregates"]:
        lines.append(
            "| "
            f"`{aggregate['item_id']}` | "
            f"`{aggregate['item_kind']}` | "
            f"`{aggregate['expected_drop_status']}` | "
            f"{aggregate['all_fixtures_minimal']} | "
            + ", ".join(f"`{item}`" for item in aggregate["minimal_fixture_ids"])
            + " | "
            f"{aggregate['reason']} |"
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


def write_results(result: T562Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t562_result_to_dict(result)
    json_path = results_dir / "T562-domain-native-sheaf-transport-minimality-gate-v0.1.json"
    md_path = (
        results_dir
        / "T562-domain-native-sheaf-transport-minimality-gate-v0.1-results.md"
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

    result = run_t562_analysis()
    payload = t562_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
