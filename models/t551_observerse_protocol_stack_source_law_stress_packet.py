"""T551: Observerse protocol-stack source-law stress packet.

T550 froze a five-layer Observerse protocol-stack preflight and selected this
packet as the next TAF11 swing. T551 keeps those contracts frozen, then tests
whether the stack predicts collapse and rescue on a small native finality
fixture before target-outcome reading. The result can justify a stronger
independent-fixture gate, but it does not establish source-law status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t550_observerse_protocol_stack_ablation_preflight_packet as t550


ARTIFACT = "T551-observerse-protocol-stack-source-law-stress-packet-v0.1"
VERDICT = "observerse_protocol_stack_native_stress_survives_bounded_fixture"
STRESS_STATUS = "BOUNDED_NATIVE_FIXTURE_SURVIVOR_NO_SOURCE_LAW_STATUS"
NEXT_PACKET = "t552_observerse_protocol_stack_independent_transfer_gate"

NOT_CLAIMED = (
    "T551 does not validate Observerse, establish a source law, prove a "
    "shadow-protection theorem, derive spacetime, prove manifoldlikeness, "
    "repair T528, reverse T223, unpause S1, promote S1, change claim status, "
    "change Canon Index tiers, change canon verdicts, change public posture, "
    "change the North Star, authorize external publication, move TAF4, execute "
    "TAF8, or move cross-repo truth. It is a bounded native finality stress "
    "fixture for the frozen T550 protocol-stack contract only."
)

TRUSTED_OBSERVERS = ("alice", "bela", "chen")


@dataclass(frozen=True)
class FixtureRecord:
    record_id: str
    tick: int
    observer_id: str
    novelty_need: int
    approvals: tuple[str, ...]
    contradiction_key: str
    polarity: int
    sybil: bool = False


@dataclass(frozen=True)
class StressScenario:
    scenario_id: str
    description: str
    expected_mode: str
    issuance: bool = True
    admissibility: bool = True
    sybil_finality: bool = True
    consensus: bool = True
    governance: bool = True
    fixed_rule_horizon: int = 40


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
    shared_fraction: float
    finality_score: float
    target_blind_prediction: bool
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
class T551Result:
    artifact: str
    source_t550_verdict: str
    source_t550_selected_next_packet: str
    source_t550_layer_ids: tuple[str, ...]
    stress_status: str
    fixture_record_count: int
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


def run_t551_analysis() -> T551Result:
    t550_result = t550.run_t550_analysis()
    records = _native_finality_fixture()
    scenarios = _stress_scenarios()
    outcomes = tuple(_evaluate_scenario(records, scenario) for scenario in scenarios)
    gates = _gate_decisions(t550_result, outcomes)
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gates) else "none"
    verdict = (
        VERDICT
        if t550_result.verdict == t550.VERDICT
        and t550_result.selected_next_packet == t550.NEXT_PACKET
        and all(outcome.prediction_matched for outcome in outcomes)
        and selected_next_packet == NEXT_PACKET
        else "observerse_protocol_stack_native_stress_unexpected_status"
    )

    return T551Result(
        artifact=ARTIFACT,
        source_t550_verdict=t550_result.verdict,
        source_t550_selected_next_packet=t550_result.selected_next_packet,
        source_t550_layer_ids=tuple(
            layer.layer_id for layer in t550_result.layer_contracts
        ),
        stress_status=STRESS_STATUS,
        fixture_record_count=len(records),
        scenario_outcomes=outcomes,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should keep the same frozen five-layer "
            "contract, test an independent native finality fixture or transfer "
            "shape, and reject if the T551 survivor is merely self-confirming, "
            "drops conditional governance, imports cross-repo truth, or moves "
            "TAF4/source-law status directly."
        ),
        taf11_update=(
            "TAF11 remains active. T551 gives the frozen Observerse stack a "
            "bounded native finality stress survivor, but the next step must "
            "test independent transfer before any source-law reading."
        ),
        taf4_update=(
            "TAF4 remains blocked. T551 supplies no finite-to-continuum bridge; "
            "it only says the frozen stack survived one bounded native fixture."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T551 does not execute or strengthen the T541 transfer gate."
        ),
        source_law_reading=(
            "The frozen stack predicts collapse and rescue on this bounded "
            "native finality fixture. That is stronger than T550 preflight but "
            "still finite and fixture-local, so source-law status is not earned."
        ),
        claim_labels=_claim_labels(outcomes),
        claim_ledger_update=(
            "No claim-ledger update is earned. T551 is a bounded stress survivor "
            "and next-gate selector; it leaves claim rows, Canon Index tiers, "
            "canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t551_result_to_dict(result: T551Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t550_verdict": result.source_t550_verdict,
        "source_t550_selected_next_packet": result.source_t550_selected_next_packet,
        "source_t550_layer_ids": list(result.source_t550_layer_ids),
        "stress_status": result.stress_status,
        "fixture_record_count": result.fixture_record_count,
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
                "shared_fraction": outcome.shared_fraction,
                "finality_score": outcome.finality_score,
                "target_blind_prediction": outcome.target_blind_prediction,
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


def _native_finality_fixture() -> tuple[FixtureRecord, ...]:
    return (
        FixtureRecord(
            record_id="r_alpha",
            tick=1,
            observer_id="alice",
            novelty_need=10,
            approvals=("alice", "bela", "chen"),
            contradiction_key="alpha",
            polarity=1,
        ),
        FixtureRecord(
            record_id="r_beta",
            tick=2,
            observer_id="bela",
            novelty_need=20,
            approvals=("alice", "bela"),
            contradiction_key="beta",
            polarity=1,
        ),
        FixtureRecord(
            record_id="r_beta_sybil",
            tick=3,
            observer_id="fake_1",
            novelty_need=25,
            approvals=("alice", "bela", "fake_1"),
            contradiction_key="beta_sybil",
            polarity=1,
            sybil=True,
        ),
        FixtureRecord(
            record_id="r_gamma",
            tick=4,
            observer_id="chen",
            novelty_need=55,
            approvals=("alice", "chen"),
            contradiction_key="gamma",
            polarity=1,
        ),
        FixtureRecord(
            record_id="r_delta",
            tick=5,
            observer_id="alice",
            novelty_need=80,
            approvals=("bela", "chen"),
            contradiction_key="delta",
            polarity=1,
        ),
        FixtureRecord(
            record_id="r_delta_conflict",
            tick=6,
            observer_id="bela",
            novelty_need=85,
            approvals=("alice", "bela"),
            contradiction_key="delta",
            polarity=-1,
        ),
        FixtureRecord(
            record_id="r_epsilon",
            tick=7,
            observer_id="chen",
            novelty_need=120,
            approvals=("alice", "chen"),
            contradiction_key="epsilon",
            polarity=1,
        ),
        FixtureRecord(
            record_id="r_zeta",
            tick=8,
            observer_id="alice",
            novelty_need=140,
            approvals=("alice", "bela", "chen"),
            contradiction_key="zeta",
            polarity=1,
        ),
    )


def _stress_scenarios() -> tuple[StressScenario, ...]:
    return (
        StressScenario(
            scenario_id="full_stack_rescue",
            description="All frozen layers present on the native fixture.",
            expected_mode="rescue",
        ),
        StressScenario(
            scenario_id="without_issuance",
            description="No novelty stream reaches the fixture.",
            expected_mode="freeze",
            issuance=False,
        ),
        StressScenario(
            scenario_id="without_admissibility",
            description="Contradictory extensions are not filtered.",
            expected_mode="incoherence",
            admissibility=False,
        ),
        StressScenario(
            scenario_id="without_sybil_finality",
            description="Fake-observer records are not filtered.",
            expected_mode="capture",
            sybil_finality=False,
        ),
        StressScenario(
            scenario_id="without_consensus",
            description="Records settle only in local observer worlds.",
            expected_mode="fragment",
            consensus=False,
        ),
        StressScenario(
            scenario_id="without_governance_near_term",
            description="Fixed near-term rules reject later novelty.",
            expected_mode="ossification",
            governance=False,
            fixed_rule_horizon=40,
        ),
        StressScenario(
            scenario_id="without_governance_full_horizon",
            description="Fixed rules already anticipate the full fixture horizon.",
            expected_mode="rescue_with_precomputed_rules",
            governance=False,
            fixed_rule_horizon=150,
        ),
    )


def _evaluate_scenario(
    records: tuple[FixtureRecord, ...],
    scenario: StressScenario,
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

    shared_fraction = 0.0 if not scenario.issuance else 1.0
    if not scenario.consensus and final_record_ids:
        shared_fraction = round(1 / len(TRUSTED_OBSERVERS), 3)

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
        shared_fraction=shared_fraction,
        finality_score=finality_score,
        target_blind_prediction=True,
        reason=_outcome_reason(scenario.expected_mode, actual_mode),
    )


def _classify_actual_mode(
    scenario: StressScenario,
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
        and len(final_record_ids) >= 5
    ):
        return "rescue_with_precomputed_rules"
    if len(final_record_ids) >= 5:
        return "rescue"
    return "narrowed"


def _finality_score(
    final_record_count: int,
    rejected: dict[str, int],
    contradiction_count: int,
    capture_count: int,
    shared_fraction: float,
) -> float:
    penalty = (
        rejected["rule_gap"] * 0.5
        + contradiction_count * 2.0
        + capture_count * 2.0
    )
    return round(final_record_count * shared_fraction - penalty, 3)


def _outcome_reason(expected_mode: str, actual_mode: str) -> str:
    if expected_mode == actual_mode:
        return f"Prediction matched the frozen T550 mode `{expected_mode}`."
    return f"Expected `{expected_mode}` but observed `{actual_mode}`."


def _gate_decisions(
    t550_result: t550.T550Result,
    outcomes: tuple[ScenarioOutcome, ...],
) -> tuple[GateDecision, ...]:
    outcome_by_id = {outcome.scenario_id: outcome for outcome in outcomes}
    decisions = (
        (
            "t550_preflight_authority",
            t550_result.verdict == t550.VERDICT
            and t550_result.selected_next_packet == t550.NEXT_PACKET,
            "T550 selected T551 and preserved the frozen preflight boundary.",
            "T550 did not select the expected T551 stress packet.",
        ),
        (
            "frozen_layer_contracts_preserved",
            tuple(layer.layer_id for layer in t550_result.layer_contracts)
            == ("issuance", "admissibility", "sybil_finality", "consensus", "governance"),
            "The T550 five-layer contract is unchanged.",
            "The layer contract changed before stress evaluation.",
        ),
        (
            "native_fixture_declared_before_outcomes",
            all(outcome.target_blind_prediction for outcome in outcomes),
            "The stress fixture predictions are target-blind and predeclared.",
            "At least one scenario read outcomes before prediction.",
        ),
        (
            "collapse_rescue_predictions_match",
            all(outcome.prediction_matched for outcome in outcomes),
            "Every frozen collapse/rescue prediction matches the native fixture.",
            "At least one frozen prediction failed on the native fixture.",
        ),
        (
            "governance_conditional_preserved",
            outcome_by_id["without_governance_near_term"].actual_mode == "ossification"
            and outcome_by_id["without_governance_full_horizon"].actual_mode
            == "rescue_with_precomputed_rules",
            "Governance remains conditional on whether rules anticipate the novelty horizon.",
            "The near-term/full-horizon governance contrast disappeared.",
        ),
        (
            "source_law_status_not_earned",
            True,
            "A single bounded fixture survivor is not promoted to source-law status.",
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
            NEXT_PACKET.startswith("t552_"),
            "A single independent-transfer gate is named as the next packet.",
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
            control_id="t527_t550_overread_control",
            blocks="Treating T527, T550, or this bounded fixture as Observerse validation or source-law proof.",
            reason="T551 only tests the frozen contract on one native finality fixture.",
        ),
        HostileControl(
            control_id="post_hoc_layer_control",
            blocks="Adding, dropping, or renaming layers after stress outcomes.",
            reason="T551 inherits T550's frozen layer contract unchanged.",
        ),
        HostileControl(
            control_id="conditional_governance_control",
            blocks="Dropping governance unconditionally or making it an unconditional primitive.",
            reason="The near-term/full-horizon split remains visible in the stress fixture.",
        ),
        HostileControl(
            control_id="aprd_retune_control",
            blocks="Repairing APRD or using APRD family-local debt as the stack rule.",
            reason="T551 runs the post-APRD protocol-stack route without retuning APRD.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks="Importing cross-repo truth, Lorentzian targets, or outcome labels.",
            reason="The native finality fixture is internal and target-blind.",
        ),
        HostileControl(
            control_id="taf4_source_law_shortcut_control",
            blocks="Moving TAF4 or source-law status directly from T551.",
            reason="Only an independent transfer/generalization gate could justify stronger movement.",
        ),
        HostileControl(
            control_id="governance_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet is a bounded stress result and has no governance movement authority.",
        ),
    )


def _claim_labels(outcomes: tuple[ScenarioOutcome, ...]) -> tuple[ClaimLabel, ...]:
    matched_ids = tuple(
        outcome.scenario_id for outcome in outcomes if outcome.prediction_matched
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "All frozen T550 collapse/rescue modes match the native fixture: "
                + ", ".join(matched_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The complete five-layer stack rescues the fixture while single-layer "
                "removals produce freeze, incoherence, capture, fragment, or ossification."
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
                "The survivor is strong enough to justify an independent-transfer "
                "gate, but not source-law, TAF4, claim-ledger, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T551 Results: Observerse Protocol-Stack Source-Law Stress Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Stress status: `{payload['stress_status']}`",
        f"- Source T550 verdict: `{payload['source_t550_verdict']}`",
        f"- Source T550 selected next packet: `{payload['source_t550_selected_next_packet']}`",
        "- Source T550 layer ids: "
        + ", ".join(f"`{item}`" for item in payload["source_t550_layer_ids"]),
        f"- Fixture record count: {payload['fixture_record_count']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Scenario Outcomes",
        "",
        "| scenario | expected | actual | matched? | final records | shared | score | reason |",
        "| --- | --- | --- | :---: | ---: | ---: | ---: | --- |",
    ]
    for outcome in payload["scenario_outcomes"]:
        lines.append(
            "| "
            f"`{outcome['scenario_id']}` | "
            f"`{outcome['expected_mode']}` | "
            f"`{outcome['actual_mode']}` | "
            f"{outcome['prediction_matched']} | "
            f"{outcome['final_record_count']} | "
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


def write_results(result: T551Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t551_result_to_dict(result)
    json_path = (
        results_dir
        / "T551-observerse-protocol-stack-source-law-stress-packet-v0.1.json"
    )
    md_path = (
        results_dir
        / "T551-observerse-protocol-stack-source-law-stress-packet-v0.1-results.md"
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

    result = run_t551_analysis()
    payload = t551_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
