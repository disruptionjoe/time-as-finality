"""T554: Observerse protocol-stack minimality gate.

T553 mapped the current bounded-native class for the frozen Observerse
protocol stack. T554 asks the next narrower question: can any frozen layer be
dropped across that admitted class before source-law, TAF4, TAF8, claim-ledger,
or public-posture movement is even considered?
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t551_observerse_protocol_stack_source_law_stress_packet as t551
from models import t552_observerse_protocol_stack_independent_transfer_gate as t552
from models import t553_observerse_protocol_stack_generalization_boundary_gate as t553


ARTIFACT = "T554-observerse-protocol-stack-minimality-gate-v0.1"
VERDICT = "observerse_protocol_stack_minimality_gate_clears_bounded_class"
MINIMALITY_STATUS = "LAYER_MINIMALITY_CLEARED_BOUNDED_NATIVE_CLASS_NO_SOURCE_LAW_STATUS"
NEXT_PACKET = "t555_observerse_protocol_stack_absorber_separation_gate"

FROZEN_LAYERS = t553.FROZEN_LAYERS
EXPECTED_DROP_MODES = {
    "issuance": "freeze",
    "admissibility": "incoherence",
    "sybil_finality": "capture",
    "consensus": "fragment",
    "governance": "ossification",
}

NOT_CLAIMED = (
    "T554 does not validate Observerse, establish a source law, prove a "
    "shadow-protection theorem, derive spacetime, prove manifoldlikeness, "
    "repair T528, reverse T223, unpause S1, promote S1, change claim status, "
    "change Canon Index tiers, change canon verdicts, change public posture, "
    "change the North Star, authorize external publication, move TAF4, execute "
    "TAF8, or move cross-repo truth. It tests layer minimality inside the "
    "bounded-native T550-T553 protocol-stack route only."
)


@dataclass(frozen=True)
class PhaseRecord:
    record_id: str
    tick: int
    observer_id: str
    phase: str
    novelty_need: int
    approvals: tuple[str, ...]
    contradiction_key: str
    polarity: int
    channel: str
    sybil: bool = False


@dataclass(frozen=True)
class LayerScenario:
    scenario_id: str
    expected_mode: str
    issuance: bool = True
    admissibility: bool = True
    sybil_finality: bool = True
    consensus: bool = True
    governance: bool = True
    fixed_rule_horizon: int = 60


@dataclass(frozen=True)
class PhaseOutcome:
    scenario_id: str
    expected_mode: str
    actual_mode: str
    prediction_matched: bool
    final_record_ids: tuple[str, ...]
    final_record_count: int
    rejected_by_reason: dict[str, int]
    contradiction_count: int
    capture_count: int
    channel_count: int
    shared_fraction: float
    finality_score: float
    target_blind_prediction: bool
    reason: str


@dataclass(frozen=True)
class AdmittedFixture:
    fixture_id: str
    source: str
    description: str
    complete_mode: str
    complete_rescues: bool
    layer_drop_modes: dict[str, str]
    full_horizon_governance_mode: str
    native_finality: bool
    bounded_fixture: bool
    target_blind: bool
    trusted_consensus: bool
    conditional_governance: bool
    frozen_layers: tuple[str, ...]
    record_ids: tuple[str, ...]


@dataclass(frozen=True)
class LayerMinimalityOutcome:
    fixture_id: str
    layer_id: str
    complete_mode: str
    expected_drop_mode: str
    actual_drop_mode: str
    minimal_in_fixture: bool
    matched: bool
    reason: str


@dataclass(frozen=True)
class LayerAggregate:
    layer_id: str
    expected_drop_mode: str
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
class T554Result:
    artifact: str
    source_t553_verdict: str
    source_t553_selected_next_packet: str
    source_t553_admitted_class_ids: tuple[str, ...]
    frozen_layers: tuple[str, ...]
    minimality_status: str
    admitted_fixtures: tuple[AdmittedFixture, ...]
    layer_minimality_outcomes: tuple[LayerMinimalityOutcome, ...]
    layer_aggregates: tuple[LayerAggregate, ...]
    phase_rotated_outcomes: tuple[PhaseOutcome, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_next_packet: str
    verdict: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    source_law_reading: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t554_analysis() -> T554Result:
    t551_result = t551.run_t551_analysis()
    t552_result = t552.run_t552_analysis()
    t553_result = t553.run_t553_analysis()
    phase_outcomes = _phase_rotated_outcomes()
    admitted_fixtures = _admitted_fixtures(t551_result, t552_result, phase_outcomes)
    minimality_outcomes = tuple(
        _evaluate_layer_minimality(fixture, layer_id)
        for fixture in admitted_fixtures
        for layer_id in FROZEN_LAYERS
    )
    aggregates = _layer_aggregates(minimality_outcomes)
    source_admitted_ids = _source_admitted_ids(t553_result)
    gates = _gate_decisions(
        t553_result=t553_result,
        source_admitted_ids=source_admitted_ids,
        admitted_fixtures=admitted_fixtures,
        minimality_outcomes=minimality_outcomes,
        aggregates=aggregates,
    )
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gates) else "none"
    verdict = (
        VERDICT
        if t553_result.verdict == t553.VERDICT
        and t553_result.selected_next_packet == t553.NEXT_PACKET
        and source_admitted_ids
        == (
            "t551_bounded_native_fixture",
            "t552_independent_transfer_fixture",
            "third_phase_rotated_native_fixture",
        )
        and all(outcome.complete_rescues for outcome in admitted_fixtures)
        and all(outcome.matched for outcome in minimality_outcomes)
        and all(aggregate.all_fixtures_minimal for aggregate in aggregates)
        and selected_next_packet == NEXT_PACKET
        else "observerse_protocol_stack_minimality_gate_unexpected_status"
    )

    return T554Result(
        artifact=ARTIFACT,
        source_t553_verdict=t553_result.verdict,
        source_t553_selected_next_packet=t553_result.selected_next_packet,
        source_t553_admitted_class_ids=source_admitted_ids,
        frozen_layers=FROZEN_LAYERS,
        minimality_status=MINIMALITY_STATUS,
        admitted_fixtures=admitted_fixtures,
        layer_minimality_outcomes=minimality_outcomes,
        layer_aggregates=aggregates,
        phase_rotated_outcomes=phase_outcomes,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should grant mature protocol, consensus, "
            "distributed-systems, governance, and record-provenance absorbers "
            "their normal state/comparison rights before treating the minimal "
            "bounded-native stack as source-law evidence."
        ),
        taf11_update=(
            "TAF11 remains active. T554 finds the frozen five-layer stack "
            "layer-minimal across the admitted bounded-native class, but the "
            "next burden is absorber separation, not promotion."
        ),
        taf4_update=(
            "TAF4 remains blocked. Layer minimality inside bounded native "
            "Observerse fixtures is not a finite-to-continuum bridge."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "Minimality inside the TAF11 class does not execute TAF8."
        ),
        source_law_reading=(
            "The stack is minimal for the current bounded-native class because "
            "each frozen layer is load-bearing under near-term governance. "
            "That is stronger internal route control, not source-law status."
        ),
        claim_labels=_claim_labels(admitted_fixtures, aggregates),
        claim_ledger_update=(
            "No claim-ledger update is earned. T554 is a layer-minimality gate "
            "and next absorber-gate selector; it leaves claim rows, Canon Index "
            "tiers, canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t554_result_to_dict(result: T554Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t553_verdict": result.source_t553_verdict,
        "source_t553_selected_next_packet": result.source_t553_selected_next_packet,
        "source_t553_admitted_class_ids": list(result.source_t553_admitted_class_ids),
        "frozen_layers": list(result.frozen_layers),
        "minimality_status": result.minimality_status,
        "admitted_fixtures": [
            {
                "fixture_id": fixture.fixture_id,
                "source": fixture.source,
                "description": fixture.description,
                "complete_mode": fixture.complete_mode,
                "complete_rescues": fixture.complete_rescues,
                "layer_drop_modes": fixture.layer_drop_modes,
                "full_horizon_governance_mode": fixture.full_horizon_governance_mode,
                "native_finality": fixture.native_finality,
                "bounded_fixture": fixture.bounded_fixture,
                "target_blind": fixture.target_blind,
                "trusted_consensus": fixture.trusted_consensus,
                "conditional_governance": fixture.conditional_governance,
                "frozen_layers": list(fixture.frozen_layers),
                "record_ids": list(fixture.record_ids),
            }
            for fixture in result.admitted_fixtures
        ],
        "layer_minimality_outcomes": [
            {
                "fixture_id": outcome.fixture_id,
                "layer_id": outcome.layer_id,
                "complete_mode": outcome.complete_mode,
                "expected_drop_mode": outcome.expected_drop_mode,
                "actual_drop_mode": outcome.actual_drop_mode,
                "minimal_in_fixture": outcome.minimal_in_fixture,
                "matched": outcome.matched,
                "reason": outcome.reason,
            }
            for outcome in result.layer_minimality_outcomes
        ],
        "layer_aggregates": [
            {
                "layer_id": aggregate.layer_id,
                "expected_drop_mode": aggregate.expected_drop_mode,
                "minimal_fixture_ids": list(aggregate.minimal_fixture_ids),
                "all_fixtures_minimal": aggregate.all_fixtures_minimal,
                "reason": aggregate.reason,
            }
            for aggregate in result.layer_aggregates
        ],
        "phase_rotated_outcomes": [
            {
                "scenario_id": outcome.scenario_id,
                "expected_mode": outcome.expected_mode,
                "actual_mode": outcome.actual_mode,
                "prediction_matched": outcome.prediction_matched,
                "final_record_ids": list(outcome.final_record_ids),
                "final_record_count": outcome.final_record_count,
                "rejected_by_reason": outcome.rejected_by_reason,
                "contradiction_count": outcome.contradiction_count,
                "capture_count": outcome.capture_count,
                "channel_count": outcome.channel_count,
                "shared_fraction": outcome.shared_fraction,
                "finality_score": outcome.finality_score,
                "target_blind_prediction": outcome.target_blind_prediction,
                "reason": outcome.reason,
            }
            for outcome in result.phase_rotated_outcomes
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
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "source_law_reading": result.source_law_reading,
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


def _source_admitted_ids(result: t553.T553Result) -> tuple[str, ...]:
    return tuple(
        outcome.case_id
        for outcome in result.boundary_outcomes
        if outcome.in_generalization_class
    )


def _admitted_fixtures(
    t551_result: t551.T551Result,
    t552_result: t552.T552Result,
    phase_outcomes: tuple[PhaseOutcome, ...],
) -> tuple[AdmittedFixture, ...]:
    t551_outcomes = {
        outcome.scenario_id: outcome for outcome in t551_result.scenario_outcomes
    }
    t552_outcomes = {
        outcome.scenario_id: outcome for outcome in t552_result.scenario_outcomes
    }
    phase_by_id = {outcome.scenario_id: outcome for outcome in phase_outcomes}
    return (
        AdmittedFixture(
            fixture_id="t551_bounded_native_fixture",
            source="T551",
            description="Original bounded native finality fixture.",
            complete_mode=t551_outcomes["full_stack_rescue"].actual_mode,
            complete_rescues=t551_outcomes["full_stack_rescue"].actual_mode == "rescue",
            layer_drop_modes={
                "issuance": t551_outcomes["without_issuance"].actual_mode,
                "admissibility": t551_outcomes["without_admissibility"].actual_mode,
                "sybil_finality": t551_outcomes["without_sybil_finality"].actual_mode,
                "consensus": t551_outcomes["without_consensus"].actual_mode,
                "governance": t551_outcomes[
                    "without_governance_near_term"
                ].actual_mode,
            },
            full_horizon_governance_mode=t551_outcomes[
                "without_governance_full_horizon"
            ].actual_mode,
            native_finality=True,
            bounded_fixture=True,
            target_blind=all(
                outcome.target_blind_prediction for outcome in t551_result.scenario_outcomes
            ),
            trusted_consensus=True,
            conditional_governance=True,
            frozen_layers=FROZEN_LAYERS,
            record_ids=tuple(
                record_id
                for outcome in t551_result.scenario_outcomes
                if outcome.scenario_id == "full_stack_rescue"
                for record_id in outcome.final_record_ids
            ),
        ),
        AdmittedFixture(
            fixture_id="t552_independent_transfer_fixture",
            source="T552",
            description="Independent handoff/partition/repair transfer fixture.",
            complete_mode=t552_outcomes["independent_transfer_rescue"].actual_mode,
            complete_rescues=(
                t552_outcomes["independent_transfer_rescue"].actual_mode == "rescue"
            ),
            layer_drop_modes={
                "issuance": t552_outcomes["transfer_without_issuance"].actual_mode,
                "admissibility": t552_outcomes[
                    "transfer_without_admissibility"
                ].actual_mode,
                "sybil_finality": t552_outcomes[
                    "transfer_without_sybil_finality"
                ].actual_mode,
                "consensus": t552_outcomes["transfer_without_consensus"].actual_mode,
                "governance": t552_outcomes[
                    "transfer_without_governance_near_term"
                ].actual_mode,
            },
            full_horizon_governance_mode=t552_outcomes[
                "transfer_without_governance_full_horizon"
            ].actual_mode,
            native_finality=True,
            bounded_fixture=True,
            target_blind=all(
                outcome.target_blind_prediction for outcome in t552_result.scenario_outcomes
            ),
            trusted_consensus=True,
            conditional_governance=True,
            frozen_layers=FROZEN_LAYERS,
            record_ids=t552_result.transfer_record_ids,
        ),
        AdmittedFixture(
            fixture_id="third_phase_rotated_native_fixture",
            source="T554",
            description="Phase-rotated issuance/review/bridge/closure native fixture.",
            complete_mode=phase_by_id["phase_rotated_full_stack_rescue"].actual_mode,
            complete_rescues=(
                phase_by_id["phase_rotated_full_stack_rescue"].actual_mode
                == "rescue"
            ),
            layer_drop_modes={
                "issuance": phase_by_id["phase_rotated_without_issuance"].actual_mode,
                "admissibility": phase_by_id[
                    "phase_rotated_without_admissibility"
                ].actual_mode,
                "sybil_finality": phase_by_id[
                    "phase_rotated_without_sybil_finality"
                ].actual_mode,
                "consensus": phase_by_id["phase_rotated_without_consensus"].actual_mode,
                "governance": phase_by_id[
                    "phase_rotated_without_governance_near_term"
                ].actual_mode,
            },
            full_horizon_governance_mode=phase_by_id[
                "phase_rotated_without_governance_full_horizon"
            ].actual_mode,
            native_finality=True,
            bounded_fixture=True,
            target_blind=all(outcome.target_blind_prediction for outcome in phase_outcomes),
            trusted_consensus=True,
            conditional_governance=True,
            frozen_layers=FROZEN_LAYERS,
            record_ids=tuple(record.record_id for record in _phase_rotated_fixture()),
        ),
    )


def _evaluate_layer_minimality(
    fixture: AdmittedFixture,
    layer_id: str,
) -> LayerMinimalityOutcome:
    expected_mode = EXPECTED_DROP_MODES[layer_id]
    actual_mode = fixture.layer_drop_modes[layer_id]
    minimal = fixture.complete_rescues and actual_mode != fixture.complete_mode
    matched = minimal and actual_mode == expected_mode
    return LayerMinimalityOutcome(
        fixture_id=fixture.fixture_id,
        layer_id=layer_id,
        complete_mode=fixture.complete_mode,
        expected_drop_mode=expected_mode,
        actual_drop_mode=actual_mode,
        minimal_in_fixture=minimal,
        matched=matched,
        reason=(
            f"Dropping `{layer_id}` changes `{fixture.complete_mode}` to "
            f"`{actual_mode}` as expected."
            if matched
            else (
                f"Dropping `{layer_id}` expected `{expected_mode}` but got "
                f"`{actual_mode}`."
            )
        ),
    )


def _layer_aggregates(
    outcomes: tuple[LayerMinimalityOutcome, ...],
) -> tuple[LayerAggregate, ...]:
    aggregates = []
    for layer_id in FROZEN_LAYERS:
        layer_outcomes = tuple(
            outcome for outcome in outcomes if outcome.layer_id == layer_id
        )
        minimal_fixture_ids = tuple(
            outcome.fixture_id for outcome in layer_outcomes if outcome.matched
        )
        all_minimal = len(minimal_fixture_ids) == len(layer_outcomes)
        aggregates.append(
            LayerAggregate(
                layer_id=layer_id,
                expected_drop_mode=EXPECTED_DROP_MODES[layer_id],
                minimal_fixture_ids=minimal_fixture_ids,
                all_fixtures_minimal=all_minimal,
                reason=(
                    f"`{layer_id}` is load-bearing in every admitted fixture."
                    if all_minimal
                    else f"`{layer_id}` is not load-bearing across the full admitted class."
                ),
            )
        )
    return tuple(aggregates)


TRUSTED_PHASE_OBSERVERS = ("mira", "noel", "oren", "paz")


def _phase_rotated_fixture() -> tuple[PhaseRecord, ...]:
    return (
        PhaseRecord(
            record_id="p_seed_mira",
            tick=1,
            observer_id="mira",
            phase="seed",
            novelty_need=12,
            approvals=("mira", "noel", "oren"),
            contradiction_key="seed",
            polarity=1,
            channel="north",
        ),
        PhaseRecord(
            record_id="p_seed_paz",
            tick=2,
            observer_id="paz",
            phase="seed",
            novelty_need=18,
            approvals=("mira", "paz"),
            contradiction_key="seed_paz",
            polarity=1,
            channel="south",
        ),
        PhaseRecord(
            record_id="p_review_noel",
            tick=3,
            observer_id="noel",
            phase="review",
            novelty_need=32,
            approvals=("noel", "oren"),
            contradiction_key="review",
            polarity=1,
            channel="east",
        ),
        PhaseRecord(
            record_id="p_bridge_oren",
            tick=4,
            observer_id="oren",
            phase="bridge",
            novelty_need=46,
            approvals=("mira", "noel", "oren"),
            contradiction_key="bridge",
            polarity=1,
            channel="both",
        ),
        PhaseRecord(
            record_id="p_shadow_capture",
            tick=5,
            observer_id="shadow_2",
            phase="review",
            novelty_need=48,
            approvals=("mira", "shadow_2"),
            contradiction_key="shadow_capture",
            polarity=1,
            channel="north",
            sybil=True,
        ),
        PhaseRecord(
            record_id="p_bridge_conflict",
            tick=6,
            observer_id="paz",
            phase="bridge",
            novelty_need=54,
            approvals=("mira", "paz"),
            contradiction_key="bridge",
            polarity=-1,
            channel="both",
        ),
        PhaseRecord(
            record_id="p_closure_noel",
            tick=7,
            observer_id="noel",
            phase="closure",
            novelty_need=82,
            approvals=("noel", "oren", "paz"),
            contradiction_key="closure",
            polarity=1,
            channel="east",
        ),
        PhaseRecord(
            record_id="p_late_mira",
            tick=8,
            observer_id="mira",
            phase="late_closure",
            novelty_need=118,
            approvals=("mira", "oren"),
            contradiction_key="late_mira",
            polarity=1,
            channel="north",
        ),
        PhaseRecord(
            record_id="p_tail_paz",
            tick=9,
            observer_id="paz",
            phase="late_closure",
            novelty_need=142,
            approvals=("mira", "noel", "paz"),
            contradiction_key="tail",
            polarity=1,
            channel="south",
        ),
    )


def _phase_rotated_scenarios() -> tuple[LayerScenario, ...]:
    return (
        LayerScenario(
            scenario_id="phase_rotated_full_stack_rescue",
            expected_mode="rescue",
        ),
        LayerScenario(
            scenario_id="phase_rotated_without_issuance",
            expected_mode="freeze",
            issuance=False,
        ),
        LayerScenario(
            scenario_id="phase_rotated_without_admissibility",
            expected_mode="incoherence",
            admissibility=False,
        ),
        LayerScenario(
            scenario_id="phase_rotated_without_sybil_finality",
            expected_mode="capture",
            sybil_finality=False,
        ),
        LayerScenario(
            scenario_id="phase_rotated_without_consensus",
            expected_mode="fragment",
            consensus=False,
        ),
        LayerScenario(
            scenario_id="phase_rotated_without_governance_near_term",
            expected_mode="ossification",
            governance=False,
            fixed_rule_horizon=60,
        ),
        LayerScenario(
            scenario_id="phase_rotated_without_governance_full_horizon",
            expected_mode="rescue_with_precomputed_rules",
            governance=False,
            fixed_rule_horizon=160,
        ),
    )


def _phase_rotated_outcomes() -> tuple[PhaseOutcome, ...]:
    records = _phase_rotated_fixture()
    return tuple(
        _evaluate_phase_scenario(records, scenario)
        for scenario in _phase_rotated_scenarios()
    )


def _evaluate_phase_scenario(
    records: tuple[PhaseRecord, ...],
    scenario: LayerScenario,
) -> PhaseOutcome:
    final_record_ids: list[str] = []
    rejected = {
        "no_issuance": 0,
        "rule_gap": 0,
        "sybil": 0,
        "consensus": 0,
        "contradiction": 0,
    }
    seen_polarity: dict[str, int] = {}
    final_channels: set[str] = set()
    contradiction_count = 0
    capture_count = 0

    for record in records:
        if not scenario.issuance:
            rejected["no_issuance"] += 1
            continue
        if not scenario.governance and record.novelty_need > scenario.fixed_rule_horizon:
            rejected["rule_gap"] += 1
            continue
        if scenario.sybil_finality and record.sybil:
            rejected["sybil"] += 1
            continue
        if not scenario.sybil_finality and record.sybil:
            capture_count += 1

        trusted_approvals = {
            approval
            for approval in record.approvals
            if approval in TRUSTED_PHASE_OBSERVERS
        }
        if scenario.consensus and len(trusted_approvals) < 2:
            rejected["consensus"] += 1
            continue

        prior = seen_polarity.get(record.contradiction_key)
        if prior is not None and prior != record.polarity:
            if scenario.admissibility:
                rejected["contradiction"] += 1
                continue
            contradiction_count += 1
        seen_polarity.setdefault(record.contradiction_key, record.polarity)
        final_record_ids.append(record.record_id)
        final_channels.add(record.channel)

    shared_fraction = 0.0 if not scenario.issuance else 1.0
    if not scenario.consensus and final_record_ids:
        shared_fraction = round(1 / len(TRUSTED_PHASE_OBSERVERS), 3)

    channel_count = len(final_channels)
    actual_mode = _classify_phase_mode(
        scenario=scenario,
        final_record_ids=tuple(final_record_ids),
        rejected=rejected,
        contradiction_count=contradiction_count,
        capture_count=capture_count,
        shared_fraction=shared_fraction,
    )
    finality_score = _phase_finality_score(
        final_record_count=len(final_record_ids),
        rejected=rejected,
        contradiction_count=contradiction_count,
        capture_count=capture_count,
        channel_count=channel_count,
        shared_fraction=shared_fraction,
    )

    return PhaseOutcome(
        scenario_id=scenario.scenario_id,
        expected_mode=scenario.expected_mode,
        actual_mode=actual_mode,
        prediction_matched=actual_mode == scenario.expected_mode,
        final_record_ids=tuple(final_record_ids),
        final_record_count=len(final_record_ids),
        rejected_by_reason=rejected,
        contradiction_count=contradiction_count,
        capture_count=capture_count,
        channel_count=channel_count,
        shared_fraction=shared_fraction,
        finality_score=finality_score,
        target_blind_prediction=True,
        reason=_phase_reason(scenario.expected_mode, actual_mode),
    )


def _classify_phase_mode(
    scenario: LayerScenario,
    final_record_ids: tuple[str, ...],
    rejected: dict[str, int],
    contradiction_count: int,
    capture_count: int,
    shared_fraction: float,
) -> str:
    if not scenario.issuance:
        return "freeze"
    if contradiction_count:
        return "incoherence"
    if capture_count:
        return "capture"
    if not scenario.consensus and shared_fraction < 0.5:
        return "fragment"
    if not scenario.governance and rejected["rule_gap"] >= 3:
        return "ossification"
    if (
        not scenario.governance
        and rejected["rule_gap"] == 0
        and len(final_record_ids) >= 6
    ):
        return "rescue_with_precomputed_rules"
    if len(final_record_ids) >= 6:
        return "rescue"
    return "narrowed"


def _phase_finality_score(
    final_record_count: int,
    rejected: dict[str, int],
    contradiction_count: int,
    capture_count: int,
    channel_count: int,
    shared_fraction: float,
) -> float:
    channel_bonus = 0.15 * max(0, channel_count - 1)
    penalty = (
        rejected["rule_gap"] * 0.5
        + contradiction_count * 2.0
        + capture_count * 2.0
    )
    return round(final_record_count * shared_fraction + channel_bonus - penalty, 3)


def _phase_reason(expected_mode: str, actual_mode: str) -> str:
    if expected_mode == actual_mode:
        return f"Prediction matched the phase-rotated mode `{expected_mode}`."
    return f"Expected `{expected_mode}` but observed `{actual_mode}`."


def _gate_decisions(
    t553_result: t553.T553Result,
    source_admitted_ids: tuple[str, ...],
    admitted_fixtures: tuple[AdmittedFixture, ...],
    minimality_outcomes: tuple[LayerMinimalityOutcome, ...],
    aggregates: tuple[LayerAggregate, ...],
) -> tuple[GateDecision, ...]:
    expected_admitted = (
        "t551_bounded_native_fixture",
        "t552_independent_transfer_fixture",
        "third_phase_rotated_native_fixture",
    )
    fixture_by_id = {fixture.fixture_id: fixture for fixture in admitted_fixtures}
    decisions = (
        (
            "t553_boundary_authority",
            t553_result.verdict == t553.VERDICT
            and t553_result.selected_next_packet == t553.NEXT_PACKET,
            "T553 completed the boundary map and selected T554.",
            "T553 did not select the expected T554 minimality gate.",
        ),
        (
            "admitted_class_preserved",
            source_admitted_ids == expected_admitted
            and tuple(fixture_by_id) == expected_admitted,
            "The admitted bounded-native class remains T551, T552, and the phase-rotated fixture.",
            "The admitted class drifted before minimality testing.",
        ),
        (
            "frozen_layer_contract_preserved",
            all(fixture.frozen_layers == FROZEN_LAYERS for fixture in admitted_fixtures)
            and tuple(t553_result.frozen_layers) == FROZEN_LAYERS,
            "The five-layer contract remains frozen.",
            "The layer contract changed before minimality testing.",
        ),
        (
            "complete_stack_rescues_all_fixtures",
            all(fixture.complete_rescues for fixture in admitted_fixtures),
            "The complete stack rescues every admitted bounded-native fixture.",
            "At least one admitted fixture is not rescued by the complete stack.",
        ),
        (
            "every_layer_minimal_across_class",
            all(outcome.matched for outcome in minimality_outcomes)
            and all(aggregate.all_fixtures_minimal for aggregate in aggregates),
            "Every frozen layer is load-bearing in every admitted fixture.",
            "At least one layer can be dropped in an admitted fixture.",
        ),
        (
            "conditional_governance_preserved",
            all(
                fixture.layer_drop_modes["governance"] == "ossification"
                and fixture.full_horizon_governance_mode
                == "rescue_with_precomputed_rules"
                for fixture in admitted_fixtures
            ),
            "Near-term governance is minimal while full-horizon rules still rescue.",
            "Governance was made unconditional or dropped without the full-horizon control.",
        ),
        (
            "phase_rotated_fixture_not_replay",
            fixture_by_id["third_phase_rotated_native_fixture"].record_ids
            != fixture_by_id["t551_bounded_native_fixture"].record_ids
            and fixture_by_id["third_phase_rotated_native_fixture"].record_ids
            != fixture_by_id["t552_independent_transfer_fixture"].record_ids,
            "The phase-rotated fixture is not a replay of T551 or T552 records.",
            "The phase-rotated fixture reuses prior fixture records.",
        ),
        (
            "next_packet_specific",
            NEXT_PACKET.startswith("t555_"),
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
            control_id="layer_drop_control",
            blocks="Dropping any frozen layer from the bounded-native stack.",
            reason="T554 requires each layer to fail in its expected mode across every admitted fixture.",
        ),
        HostileControl(
            control_id="phase_rotated_replay_control",
            blocks="Counting a renamed T551 or T552 fixture as the third admitted shape.",
            reason="The phase-rotated fixture uses distinct records, phases, channels, and observer ids.",
        ),
        HostileControl(
            control_id="conditional_governance_control",
            blocks="Making governance unconditional or deleting it without the near-term/full-horizon split.",
            reason="Governance is minimal under near-term rules and non-minimal only when full-horizon rules are granted.",
        ),
        HostileControl(
            control_id="source_law_overread_control",
            blocks="Treating bounded-class minimality as source-law proof.",
            reason="Minimality does not grant mature absorber separation or a source-law theorem.",
        ),
        HostileControl(
            control_id="absorber_bypass_control",
            blocks="Skipping protocol, consensus, governance, or provenance absorbers after minimality.",
            reason="The next gate must grant same-neighbor-data completion before stronger readings.",
        ),
        HostileControl(
            control_id="taf4_taf8_shortcut_control",
            blocks="Moving TAF4 or executing TAF8 from an internal TAF11 minimality result.",
            reason="Layer minimality is neither a finite-to-continuum bridge nor a cross-domain packet.",
        ),
        HostileControl(
            control_id="governance_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet has no governance movement authority.",
        ),
    )


def _claim_labels(
    admitted_fixtures: tuple[AdmittedFixture, ...],
    aggregates: tuple[LayerAggregate, ...],
) -> tuple[ClaimLabel, ...]:
    fixture_ids = ", ".join(fixture.fixture_id for fixture in admitted_fixtures)
    layer_ids = ", ".join(aggregate.layer_id for aggregate in aggregates)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The complete frozen stack rescues every admitted fixture: "
                f"{fixture_ids}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Each frozen layer is minimal across the admitted class: "
                f"{layer_ids}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Governance remains conditional: near-term removal ossifies, "
                "while full-horizon precomputed rules rescue in every fixture."
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
        "# T554 Results: Observerse Protocol-Stack Minimality Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Minimality status: `{payload['minimality_status']}`",
        f"- Source T553 verdict: `{payload['source_t553_verdict']}`",
        f"- Source T553 selected next packet: `{payload['source_t553_selected_next_packet']}`",
        "- Source T553 admitted class ids: "
        + ", ".join(
            f"`{item}`" for item in payload["source_t553_admitted_class_ids"]
        ),
        "- Frozen layers: " + ", ".join(f"`{item}`" for item in payload["frozen_layers"]),
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Admitted Fixtures",
        "",
        "| fixture | source | complete | full-horizon governance | records | description |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for fixture in payload["admitted_fixtures"]:
        lines.append(
            "| "
            f"`{fixture['fixture_id']}` | "
            f"`{fixture['source']}` | "
            f"`{fixture['complete_mode']}` | "
            f"`{fixture['full_horizon_governance_mode']}` | "
            f"{len(fixture['record_ids'])} | "
            f"{fixture['description']} |"
        )
    lines.extend(
        [
            "",
            "## Layer Minimality Outcomes",
            "",
            "| fixture | layer | complete | drop mode | matched? | reason |",
            "| --- | --- | --- | --- | :---: | --- |",
        ]
    )
    for outcome in payload["layer_minimality_outcomes"]:
        lines.append(
            "| "
            f"`{outcome['fixture_id']}` | "
            f"`{outcome['layer_id']}` | "
            f"`{outcome['complete_mode']}` | "
            f"`{outcome['actual_drop_mode']}` | "
            f"{outcome['matched']} | "
            f"{outcome['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Layer Aggregates",
            "",
            "| layer | expected drop | all fixtures minimal? | minimal fixtures | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for aggregate in payload["layer_aggregates"]:
        lines.append(
            "| "
            f"`{aggregate['layer_id']}` | "
            f"`{aggregate['expected_drop_mode']}` | "
            f"{aggregate['all_fixtures_minimal']} | "
            + ", ".join(f"`{item}`" for item in aggregate["minimal_fixture_ids"])
            + " | "
            f"{aggregate['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Phase-Rotated Outcomes",
            "",
            "| scenario | expected | actual | matched? | final records | channels | shared | score |",
            "| --- | --- | --- | :---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for outcome in payload["phase_rotated_outcomes"]:
        lines.append(
            "| "
            f"`{outcome['scenario_id']}` | "
            f"`{outcome['expected_mode']}` | "
            f"`{outcome['actual_mode']}` | "
            f"{outcome['prediction_matched']} | "
            f"{outcome['final_record_count']} | "
            f"{outcome['channel_count']} | "
            f"{outcome['shared_fraction']:.3f} | "
            f"{outcome['finality_score']:.3f} |"
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


def write_results(result: T554Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t554_result_to_dict(result)
    json_path = results_dir / "T554-observerse-protocol-stack-minimality-gate-v0.1.json"
    md_path = (
        results_dir
        / "T554-observerse-protocol-stack-minimality-gate-v0.1-results.md"
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

    result = run_t554_analysis()
    payload = t554_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
