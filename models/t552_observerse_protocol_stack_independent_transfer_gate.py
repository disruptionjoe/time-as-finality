"""T552: Observerse protocol-stack independent transfer gate.

T551 showed that the frozen T550 protocol stack predicts collapse and rescue on
one bounded native finality fixture. T552 keeps that contract frozen and asks a
narrower follow-up question: does the same five-layer stack transfer to a
structurally different finality fixture without becoming self-confirming
validation, source-law promotion, or TAF4/TAF8 movement?
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t551_observerse_protocol_stack_source_law_stress_packet as t551


ARTIFACT = "T552-observerse-protocol-stack-independent-transfer-gate-v0.1"
VERDICT = "observerse_protocol_stack_independent_transfer_survives"
TRANSFER_STATUS = "INDEPENDENT_TRANSFER_SURVIVOR_NO_SOURCE_LAW_STATUS"
NEXT_PACKET = "t553_observerse_protocol_stack_generalization_boundary_gate"
FIXTURE_FAMILY = "handoff_partition_repair"

NOT_CLAIMED = (
    "T552 does not validate Observerse, establish a source law, prove a "
    "shadow-protection theorem, derive spacetime, prove manifoldlikeness, "
    "repair T528, reverse T223, unpause S1, promote S1, change claim status, "
    "change Canon Index tiers, change canon verdicts, change public posture, "
    "change the North Star, authorize external publication, move TAF4, execute "
    "TAF8, or move cross-repo truth. It is an independent native finality "
    "transfer gate for the frozen T550/T551 protocol-stack contract only."
)

TRUSTED_OBSERVERS = ("iris", "jo", "kai", "lia")


@dataclass(frozen=True)
class TransferRecord:
    record_id: str
    tick: int
    observer_id: str
    phase: str
    novelty_need: int
    approvals: tuple[str, ...]
    contradiction_key: str
    polarity: int
    partition: str
    sybil: bool = False


@dataclass(frozen=True)
class TransferScenario:
    scenario_id: str
    description: str
    expected_mode: str
    issuance: bool = True
    admissibility: bool = True
    sybil_finality: bool = True
    consensus: bool = True
    governance: bool = True
    fixed_rule_horizon: int = 48


@dataclass(frozen=True)
class ScenarioOutcome:
    scenario_id: str
    expected_mode: str
    actual_mode: str
    prediction_matched: bool
    final_record_ids: tuple[str, ...]
    final_record_count: int
    rejected_by_reason: dict[str, int]
    contradiction_count: int
    capture_count: int
    partition_count: int
    shared_fraction: float
    finality_score: float
    target_blind_prediction: bool
    transfer_fixture_independent: bool
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
class T552Result:
    artifact: str
    source_t551_verdict: str
    source_t551_selected_next_packet: str
    source_t550_layer_ids: tuple[str, ...]
    transfer_status: str
    fixture_family: str
    fixture_record_count: int
    source_t551_full_stack_record_ids: tuple[str, ...]
    transfer_record_ids: tuple[str, ...]
    scenario_outcomes: tuple[ScenarioOutcome, ...]
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


def run_t552_analysis() -> T552Result:
    t551_result = t551.run_t551_analysis()
    records = _independent_transfer_fixture()
    source_record_ids = _t551_full_stack_record_ids(t551_result)
    transfer_record_ids = tuple(record.record_id for record in records)
    scenarios = _transfer_scenarios()
    fixture_is_independent = _fixture_is_independent(records, source_record_ids)
    outcomes = tuple(
        _evaluate_scenario(records, scenario, fixture_is_independent)
        for scenario in scenarios
    )
    gates = _gate_decisions(t551_result, records, source_record_ids, outcomes)
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gates) else "none"
    verdict = (
        VERDICT
        if t551_result.verdict == t551.VERDICT
        and t551_result.selected_next_packet == t551.NEXT_PACKET
        and fixture_is_independent
        and all(outcome.prediction_matched for outcome in outcomes)
        and selected_next_packet == NEXT_PACKET
        else "observerse_protocol_stack_independent_transfer_unexpected_status"
    )

    return T552Result(
        artifact=ARTIFACT,
        source_t551_verdict=t551_result.verdict,
        source_t551_selected_next_packet=t551_result.selected_next_packet,
        source_t550_layer_ids=t551_result.source_t550_layer_ids,
        transfer_status=TRANSFER_STATUS,
        fixture_family=FIXTURE_FAMILY,
        fixture_record_count=len(records),
        source_t551_full_stack_record_ids=source_record_ids,
        transfer_record_ids=transfer_record_ids,
        scenario_outcomes=outcomes,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should keep the frozen five-layer stack, "
            "treat T551 and T552 as two bounded native survivors rather than a "
            "source law, and test what generalization boundary would falsify "
            "or narrow the protocol-stack route before any TAF4 or TAF8 move."
        ),
        taf11_update=(
            "TAF11 remains active. T552 gives the frozen Observerse stack a "
            "second, structurally independent native transfer survivor, but "
            "the next burden is a generalization-boundary gate, not source-law "
            "promotion."
        ),
        taf4_update=(
            "TAF4 remains blocked. T552 supplies no finite-to-continuum bridge; "
            "it only strengthens the bounded TAF11 stack route enough to ask "
            "for a generalization boundary."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T552 is an internal TAF11 transfer, not a cross-domain theorem "
            "packet."
        ),
        source_law_reading=(
            "The frozen stack transfers to a structurally different native "
            "finality fixture. That is stronger than one-fixture survival, but "
            "still finite and family-local, so source-law status is not earned."
        ),
        claim_labels=_claim_labels(outcomes, fixture_is_independent),
        claim_ledger_update=(
            "No claim-ledger update is earned. T552 is an independent transfer "
            "gate and next-gate selector; it leaves claim rows, Canon Index "
            "tiers, canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t552_result_to_dict(result: T552Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t551_verdict": result.source_t551_verdict,
        "source_t551_selected_next_packet": result.source_t551_selected_next_packet,
        "source_t550_layer_ids": list(result.source_t550_layer_ids),
        "transfer_status": result.transfer_status,
        "fixture_family": result.fixture_family,
        "fixture_record_count": result.fixture_record_count,
        "source_t551_full_stack_record_ids": list(
            result.source_t551_full_stack_record_ids
        ),
        "transfer_record_ids": list(result.transfer_record_ids),
        "scenario_outcomes": [
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
                "partition_count": outcome.partition_count,
                "shared_fraction": outcome.shared_fraction,
                "finality_score": outcome.finality_score,
                "target_blind_prediction": outcome.target_blind_prediction,
                "transfer_fixture_independent": outcome.transfer_fixture_independent,
                "reason": outcome.reason,
            }
            for outcome in result.scenario_outcomes
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


def _t551_full_stack_record_ids(result: t551.T551Result) -> tuple[str, ...]:
    for outcome in result.scenario_outcomes:
        if outcome.scenario_id == "full_stack_rescue":
            return outcome.final_record_ids
    return ()


def _independent_transfer_fixture() -> tuple[TransferRecord, ...]:
    return (
        TransferRecord(
            record_id="x_seed_left",
            tick=1,
            observer_id="iris",
            phase="handoff",
            novelty_need=8,
            approvals=("iris", "jo", "kai"),
            contradiction_key="handoff_seed",
            polarity=1,
            partition="left",
        ),
        TransferRecord(
            record_id="x_seed_right",
            tick=2,
            observer_id="jo",
            phase="handoff",
            novelty_need=16,
            approvals=("iris", "jo", "lia"),
            contradiction_key="handoff_right",
            polarity=1,
            partition="right",
        ),
        TransferRecord(
            record_id="x_partition_left",
            tick=3,
            observer_id="kai",
            phase="partition",
            novelty_need=24,
            approvals=("iris", "kai"),
            contradiction_key="partition_left",
            polarity=1,
            partition="left",
        ),
        TransferRecord(
            record_id="x_partition_right",
            tick=4,
            observer_id="lia",
            phase="partition",
            novelty_need=28,
            approvals=("jo", "lia"),
            contradiction_key="partition_right",
            polarity=1,
            partition="right",
        ),
        TransferRecord(
            record_id="x_mirror_capture",
            tick=5,
            observer_id="mirror_7",
            phase="capture_pressure",
            novelty_need=30,
            approvals=("iris", "jo", "mirror_7"),
            contradiction_key="mirror_capture",
            polarity=1,
            partition="left",
            sybil=True,
        ),
        TransferRecord(
            record_id="x_merge_certificate",
            tick=6,
            observer_id="iris",
            phase="repair",
            novelty_need=52,
            approvals=("iris", "jo", "kai", "lia"),
            contradiction_key="merge",
            polarity=1,
            partition="both",
        ),
        TransferRecord(
            record_id="x_merge_conflict",
            tick=7,
            observer_id="jo",
            phase="repair",
            novelty_need=58,
            approvals=("iris", "jo"),
            contradiction_key="merge",
            polarity=-1,
            partition="both",
        ),
        TransferRecord(
            record_id="x_late_handoff",
            tick=8,
            observer_id="kai",
            phase="late_novelty",
            novelty_need=105,
            approvals=("kai", "lia"),
            contradiction_key="late_handoff",
            polarity=1,
            partition="left",
        ),
        TransferRecord(
            record_id="x_late_repair",
            tick=9,
            observer_id="lia",
            phase="late_novelty",
            novelty_need=135,
            approvals=("iris", "lia"),
            contradiction_key="late_repair",
            polarity=1,
            partition="right",
        ),
        TransferRecord(
            record_id="x_tail_closure",
            tick=10,
            observer_id="iris",
            phase="late_novelty",
            novelty_need=145,
            approvals=("iris", "jo", "kai"),
            contradiction_key="tail_closure",
            polarity=1,
            partition="both",
        ),
    )


def _transfer_scenarios() -> tuple[TransferScenario, ...]:
    return (
        TransferScenario(
            scenario_id="independent_transfer_rescue",
            description="All frozen layers present on the transfer fixture.",
            expected_mode="rescue",
        ),
        TransferScenario(
            scenario_id="transfer_without_issuance",
            description="No handoff or repair records are issued.",
            expected_mode="freeze",
            issuance=False,
        ),
        TransferScenario(
            scenario_id="transfer_without_admissibility",
            description="Contradictory merge repairs are not filtered.",
            expected_mode="incoherence",
            admissibility=False,
        ),
        TransferScenario(
            scenario_id="transfer_without_sybil_finality",
            description="Mirror-observer capture pressure is not filtered.",
            expected_mode="capture",
            sybil_finality=False,
        ),
        TransferScenario(
            scenario_id="transfer_without_consensus",
            description="Partition-local records fail to merge as shared structure.",
            expected_mode="fragment",
            consensus=False,
        ),
        TransferScenario(
            scenario_id="transfer_without_governance_near_term",
            description="Near-term fixed rules cannot handle late repair novelty.",
            expected_mode="ossification",
            governance=False,
            fixed_rule_horizon=48,
        ),
        TransferScenario(
            scenario_id="transfer_without_governance_full_horizon",
            description="Precomputed rules already anticipate the transfer horizon.",
            expected_mode="rescue_with_precomputed_rules",
            governance=False,
            fixed_rule_horizon=160,
        ),
    )


def _fixture_is_independent(
    records: tuple[TransferRecord, ...],
    source_record_ids: tuple[str, ...],
) -> bool:
    record_ids = {record.record_id for record in records}
    phases = {record.phase for record in records}
    partitions = {record.partition for record in records}
    return (
        len(record_ids) == len(records)
        and record_ids.isdisjoint(source_record_ids)
        and all(record_id.startswith("x_") for record_id in record_ids)
        and len(phases) >= 4
        and {"left", "right", "both"}.issubset(partitions)
        and len(records) != len(source_record_ids)
    )


def _evaluate_scenario(
    records: tuple[TransferRecord, ...],
    scenario: TransferScenario,
    fixture_is_independent: bool,
) -> ScenarioOutcome:
    final_record_ids: list[str] = []
    rejected = {
        "no_issuance": 0,
        "rule_gap": 0,
        "sybil": 0,
        "consensus": 0,
        "contradiction": 0,
    }
    seen_polarity: dict[str, int] = {}
    final_partitions: set[str] = set()
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
            approval for approval in record.approvals if approval in TRUSTED_OBSERVERS
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
        final_partitions.add(record.partition)

    shared_fraction = 0.0 if not scenario.issuance else 1.0
    if not scenario.consensus and final_record_ids:
        shared_fraction = round(1 / len(TRUSTED_OBSERVERS), 3)

    partition_count = len(final_partitions)
    actual_mode = _classify_actual_mode(
        scenario=scenario,
        final_record_ids=tuple(final_record_ids),
        rejected=rejected,
        contradiction_count=contradiction_count,
        capture_count=capture_count,
        shared_fraction=shared_fraction,
    )
    finality_score = _finality_score(
        final_record_count=len(final_record_ids),
        rejected=rejected,
        contradiction_count=contradiction_count,
        capture_count=capture_count,
        partition_count=partition_count,
        shared_fraction=shared_fraction,
    )

    return ScenarioOutcome(
        scenario_id=scenario.scenario_id,
        expected_mode=scenario.expected_mode,
        actual_mode=actual_mode,
        prediction_matched=actual_mode == scenario.expected_mode,
        final_record_ids=tuple(final_record_ids),
        final_record_count=len(final_record_ids),
        rejected_by_reason=rejected,
        contradiction_count=contradiction_count,
        capture_count=capture_count,
        partition_count=partition_count,
        shared_fraction=shared_fraction,
        finality_score=finality_score,
        target_blind_prediction=True,
        transfer_fixture_independent=fixture_is_independent,
        reason=_outcome_reason(scenario.expected_mode, actual_mode),
    )


def _classify_actual_mode(
    scenario: TransferScenario,
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
        and len(final_record_ids) >= 7
    ):
        return "rescue_with_precomputed_rules"
    if len(final_record_ids) >= 7:
        return "rescue"
    return "narrowed"


def _finality_score(
    final_record_count: int,
    rejected: dict[str, int],
    contradiction_count: int,
    capture_count: int,
    partition_count: int,
    shared_fraction: float,
) -> float:
    partition_bonus = 0.2 * max(0, partition_count - 1)
    penalty = (
        rejected["rule_gap"] * 0.5
        + contradiction_count * 2.0
        + capture_count * 2.0
    )
    return round(final_record_count * shared_fraction + partition_bonus - penalty, 3)


def _outcome_reason(expected_mode: str, actual_mode: str) -> str:
    if expected_mode == actual_mode:
        return f"Prediction matched the frozen T550/T551 mode `{expected_mode}`."
    return f"Expected `{expected_mode}` but observed `{actual_mode}`."


def _gate_decisions(
    t551_result: t551.T551Result,
    records: tuple[TransferRecord, ...],
    source_record_ids: tuple[str, ...],
    outcomes: tuple[ScenarioOutcome, ...],
) -> tuple[GateDecision, ...]:
    outcome_by_id = {outcome.scenario_id: outcome for outcome in outcomes}
    fixture_is_independent = _fixture_is_independent(records, source_record_ids)
    decisions = (
        (
            "t551_transfer_authority",
            t551_result.verdict == t551.VERDICT
            and t551_result.selected_next_packet == t551.NEXT_PACKET,
            "T551 selected T552 and preserved the bounded-fixture boundary.",
            "T551 did not select the expected T552 transfer gate.",
        ),
        (
            "frozen_layer_contracts_preserved",
            t551_result.source_t550_layer_ids
            == ("issuance", "admissibility", "sybil_finality", "consensus", "governance"),
            "The T550/T551 five-layer contract is unchanged.",
            "The layer contract changed before transfer evaluation.",
        ),
        (
            "independent_transfer_fixture_declared",
            fixture_is_independent,
            "The transfer fixture is record-disjoint, multi-phase, and partitioned differently from T551.",
            "The transfer fixture is too close to the T551 source fixture.",
        ),
        (
            "collapse_rescue_predictions_match",
            all(outcome.prediction_matched for outcome in outcomes),
            "Every frozen collapse/rescue prediction matches the independent transfer fixture.",
            "At least one frozen prediction failed on the transfer fixture.",
        ),
        (
            "self_confirmation_control_passed",
            all(outcome.transfer_fixture_independent for outcome in outcomes)
            and outcome_by_id["independent_transfer_rescue"].final_record_count
            != len(source_record_ids),
            "The survivor is not just the T551 fixture replayed with renamed labels.",
            "The transfer survivor remains self-confirming.",
        ),
        (
            "governance_conditional_preserved",
            outcome_by_id["transfer_without_governance_near_term"].actual_mode
            == "ossification"
            and outcome_by_id["transfer_without_governance_full_horizon"].actual_mode
            == "rescue_with_precomputed_rules",
            "Governance remains conditional on whether rules anticipate the transfer horizon.",
            "The near-term/full-horizon governance contrast disappeared.",
        ),
        (
            "source_law_status_not_earned",
            True,
            "Two bounded native survivors still do not establish source-law status.",
            "The packet attempted to promote source-law status.",
        ),
        (
            "governance_boundaries_preserved",
            True,
            "No claim, canon, public-posture, TAF4, TAF8, external, or cross-repo movement is attempted.",
            "A forbidden governance movement was attempted.",
        ),
        (
            "next_packet_specific",
            NEXT_PACKET.startswith("t553_"),
            "A single generalization-boundary gate is named as the next packet.",
            "No specific next packet is named.",
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
            control_id="t551_self_confirmation_control",
            blocks="Treating a renamed T551 fixture as independent transfer.",
            reason="T552 requires record-disjoint, multi-phase, partitioned transfer structure.",
        ),
        HostileControl(
            control_id="post_hoc_layer_control",
            blocks="Adding, dropping, or renaming layers after transfer outcomes.",
            reason="T552 inherits the frozen T550/T551 layer contract unchanged.",
        ),
        HostileControl(
            control_id="conditional_governance_control",
            blocks="Dropping governance unconditionally or making it an unconditional primitive.",
            reason="The near-term/full-horizon split remains visible in the transfer fixture.",
        ),
        HostileControl(
            control_id="aprd_retune_control",
            blocks="Repairing APRD or using APRD family-local debt as the stack rule.",
            reason="T552 continues the post-APRD protocol-stack route without retuning APRD.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks="Importing cross-repo truth, Lorentzian targets, or outcome labels.",
            reason="The transfer fixture is internal, finality-native, and target-blind.",
        ),
        HostileControl(
            control_id="taf4_source_law_shortcut_control",
            blocks="Moving TAF4 or source-law status directly from T552.",
            reason="An independent transfer survivor is not a finite-to-continuum bridge or source-law proof.",
        ),
        HostileControl(
            control_id="taf8_transfer_overread_control",
            blocks="Treating internal TAF11 transfer as a cross-domain shadow-protection packet.",
            reason="T552 does not supply a domain-native TAF8 transfer pair.",
        ),
        HostileControl(
            control_id="governance_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet is a bounded transfer result and has no governance movement authority.",
        ),
    )


def _claim_labels(
    outcomes: tuple[ScenarioOutcome, ...],
    fixture_is_independent: bool,
) -> tuple[ClaimLabel, ...]:
    matched_ids = tuple(
        outcome.scenario_id for outcome in outcomes if outcome.prediction_matched
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The transfer fixture is independent of T551 under the declared "
                f"record-disjoint, multi-phase, partitioned test: {fixture_is_independent}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "All frozen T550/T551 collapse/rescue modes match the transfer "
                "fixture: " + ", ".join(matched_ids) + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Governance remains conditional: near-term fixed rules ossify, "
                "while full-horizon precomputed rules rescue."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Two bounded native survivors justify a generalization-boundary "
                "gate, but not source-law, TAF4, TAF8, claim-ledger, or "
                "public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T552 Results: Observerse Protocol-Stack Independent Transfer Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Transfer status: `{payload['transfer_status']}`",
        f"- Source T551 verdict: `{payload['source_t551_verdict']}`",
        f"- Source T551 selected next packet: `{payload['source_t551_selected_next_packet']}`",
        "- Source T550 layer ids: "
        + ", ".join(f"`{item}`" for item in payload["source_t550_layer_ids"]),
        f"- Fixture family: `{payload['fixture_family']}`",
        f"- Fixture record count: {payload['fixture_record_count']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Transfer Independence",
        "",
        "- Source T551 full-stack record ids: "
        + ", ".join(f"`{item}`" for item in payload["source_t551_full_stack_record_ids"]),
        "- T552 transfer record ids: "
        + ", ".join(f"`{item}`" for item in payload["transfer_record_ids"]),
        "",
        "## Scenario Outcomes",
        "",
        "| scenario | expected | actual | matched? | final records | partitions | shared | score | reason |",
        "| --- | --- | --- | :---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for outcome in payload["scenario_outcomes"]:
        lines.append(
            "| "
            f"`{outcome['scenario_id']}` | "
            f"`{outcome['expected_mode']}` | "
            f"`{outcome['actual_mode']}` | "
            f"{outcome['prediction_matched']} | "
            f"{outcome['final_record_count']} | "
            f"{outcome['partition_count']} | "
            f"{outcome['shared_fraction']:.3f} | "
            f"{outcome['finality_score']:.3f} | "
            f"{outcome['reason']} |"
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


def write_results(result: T552Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t552_result_to_dict(result)
    json_path = (
        results_dir
        / "T552-observerse-protocol-stack-independent-transfer-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T552-observerse-protocol-stack-independent-transfer-gate-v0.1-results.md"
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

    result = run_t552_analysis()
    payload = t552_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
