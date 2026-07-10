"""T513: Cap_TI reconciliation protocol gate.

The Cap_TI capability-object spec selected reconciliation rounds R(beta) as
the operative capability, but left the continuous formula needing protocol
grounding. This module makes the grounding requirement executable.

The fixture is review machinery only. It does not promote Cap_TI, H7, Temporal
Issuance source truth, claim status, public posture, or cross-repo truth.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T513-cap-ti-reconciliation-protocol-gate-v0.1"
VERDICT = "CAP_TI_RECONCILIATION_PROTOCOL_GATE_BUILT_REVIEW_ONLY"
SOURCE_SPEC = "open-problems/cap-ti-capability-object-spec.md"


@dataclass(frozen=True)
class ReconciliationPacket:
    packet_id: str
    event_count: int
    beta: float
    protocol_declared: bool
    beta_predeclared: bool
    reconciliation_unit_declared: bool
    observer_pair_schedule_declared: bool
    hierarchy_capacity_declared: bool
    timing_metric_declared: bool
    continuous_formula_declared: bool
    measured_rounds: int
    causal_order_matched: bool
    entropy_matched: bool
    gluing_topology_matched: bool
    positive_control_included: bool
    null_control_included: bool
    formula_only: bool = False
    topology_only: bool = False
    posthoc_beta: bool = False
    hidden_timing_shortcut: bool = False
    requests_claim_movement: bool = False
    requests_h7_promotion: bool = False
    requests_ti_source_truth: bool = False
    requests_cross_repo_truth_movement: bool = False
    requests_external_publication: bool = False


@dataclass(frozen=True)
class ReconciliationDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    expected_rounds: int
    measured_rounds: int
    hierarchy_capacity: int
    protocol_grounded: bool
    formula_only_rejected: bool
    topology_only_absorbed: bool
    posthoc_beta_rejected: bool
    hidden_timing_rejected: bool
    missing_requirements: tuple[str, ...]
    blocked_shortcuts: tuple[str, ...]
    strongest_allowed_reading: str


def expected_protocol_rounds(event_count: int, beta: float) -> int:
    """Discretize the Cap_TI continuous R = n^(1 - beta) formula."""

    if event_count <= 0:
        raise ValueError("event_count must be positive")
    if not 0.0 <= beta <= 1.0:
        raise ValueError("beta must be in [0, 1]")
    return max(1, math.ceil(event_count ** (1.0 - beta)))


def hierarchy_capacity(event_count: int, beta: float) -> int:
    """Finite packet interpretation: one round reconciles a beta-sized batch."""

    if event_count <= 0:
        raise ValueError("event_count must be positive")
    if not 0.0 <= beta <= 1.0:
        raise ValueError("beta must be in [0, 1]")
    return max(1, math.ceil(event_count**beta))


def run() -> dict[str, Any]:
    packets = fixture_packets()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    by_id = {decision.packet_id: decision for decision in decisions}

    high = by_id["hierarchical_protocol_high_beta"]
    low = by_id["hierarchical_protocol_low_beta"]
    null_a = by_id["same_beta_null_control_a"]
    null_b = by_id["same_beta_null_control_b"]

    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": VERDICT,
        "source_spec": SOURCE_SPEC,
        "objective": (
            "Ground the Cap_TI reconciliation-round capability in an explicit "
            "finite protocol packet. A packet must predeclare the beta metric, "
            "observer-pair schedule, hierarchy capacity, reconciliation unit, "
            "and controls before using R(beta) as review material."
        ),
        "protocol_interpretation": {
            "continuous_formula": "R_continuous(n, beta) = n^(1 - beta)",
            "finite_rounds": "ceil(n^(1 - beta))",
            "hierarchy_capacity": "ceil(n^beta)",
            "round_reading": (
                "One round may reconcile at most one hierarchy-capacity batch "
                "of observer disagreements under the predeclared schedule."
            ),
        },
        "packets": [asdict(packet) for packet in packets],
        "decisions": [decision_dict(decision) for decision in decisions],
        "admitted_packet_ids": [
            decision.packet_id for decision in decisions if decision.admitted
        ],
        "rejected_packet_ids": [
            decision.packet_id for decision in decisions if not decision.admitted
        ],
        "overall": {
            "review_target_admitted": high.admitted and low.admitted,
            "high_beta_rounds": high.measured_rounds,
            "low_beta_rounds": low.measured_rounds,
            "high_beta_fewer_rounds": high.measured_rounds < low.measured_rounds,
            "same_beta_null_same_rounds": (
                null_a.measured_rounds == null_b.measured_rounds
            ),
            "formula_only_rejected": by_id[
                "formula_only_shortcut"
            ].formula_only_rejected,
            "topology_only_absorbed": by_id[
                "topology_only_shortcut"
            ].topology_only_absorbed,
            "posthoc_beta_rejected": by_id[
                "posthoc_beta_shortcut"
            ].posthoc_beta_rejected,
            "hidden_timing_rejected": by_id[
                "hidden_timing_shortcut"
            ].hidden_timing_rejected,
            "round_mismatch_rejected": by_id[
                "round_mismatch_control"
            ].label
            == "REJECTED_PROTOCOL_ROUND_MISMATCH",
            "governance_shortcut_blocked": by_id[
                "promotion_or_cross_repo_shortcut"
            ].label
            == "BLOCKED_GOVERNANCE_OR_CROSS_REPO_SHORTCUT",
            "claim_movement": False,
            "h7_promotion": False,
            "temporal_issuance_source_truth": False,
            "cross_repo_truth_movement": False,
            "external_publication": False,
            "public_posture_movement": False,
            "north_star_movement": False,
            "roadmap_movement": False,
            "hard_policy_movement": False,
        },
        "future_packet_minimum": future_packet_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T513 turns the Cap_TI reconciliation-round formula into a finite "
            "review packet shape: beta, timing metric, observer-pair schedule, "
            "hierarchy capacity, reconciliation unit, and controls must be "
            "predeclared, and measured rounds must match ceil(n^(1 - beta)). "
            "The synthetic high-beta packet requires fewer rounds than the "
            "matched low-beta packet, while same-beta controls match. This is "
            "protocol grounding only, not Cap_TI promotion or Temporal Issuance "
            "source truth."
        ),
    }


def fixture_packets() -> tuple[ReconciliationPacket, ...]:
    base = {
        "event_count": 64,
        "protocol_declared": True,
        "beta_predeclared": True,
        "reconciliation_unit_declared": True,
        "observer_pair_schedule_declared": True,
        "hierarchy_capacity_declared": True,
        "timing_metric_declared": True,
        "continuous_formula_declared": True,
        "causal_order_matched": True,
        "entropy_matched": True,
        "gluing_topology_matched": True,
        "positive_control_included": True,
        "null_control_included": True,
    }
    return (
        ReconciliationPacket(
            packet_id="hierarchical_protocol_high_beta",
            beta=0.75,
            measured_rounds=expected_protocol_rounds(64, 0.75),
            **base,
        ),
        ReconciliationPacket(
            packet_id="hierarchical_protocol_low_beta",
            beta=0.50,
            measured_rounds=expected_protocol_rounds(64, 0.50),
            **base,
        ),
        ReconciliationPacket(
            packet_id="same_beta_null_control_a",
            beta=0.60,
            measured_rounds=expected_protocol_rounds(64, 0.60),
            **base,
        ),
        ReconciliationPacket(
            packet_id="same_beta_null_control_b",
            beta=0.60,
            measured_rounds=expected_protocol_rounds(64, 0.60),
            **base,
        ),
        ReconciliationPacket(
            packet_id="formula_only_shortcut",
            beta=0.75,
            protocol_declared=False,
            beta_predeclared=True,
            reconciliation_unit_declared=False,
            observer_pair_schedule_declared=False,
            hierarchy_capacity_declared=False,
            timing_metric_declared=True,
            continuous_formula_declared=True,
            measured_rounds=expected_protocol_rounds(64, 0.75),
            formula_only=True,
            **{k: v for k, v in base.items() if k not in {
                "protocol_declared",
                "beta_predeclared",
                "reconciliation_unit_declared",
                "observer_pair_schedule_declared",
                "hierarchy_capacity_declared",
                "timing_metric_declared",
                "continuous_formula_declared",
            }},
        ),
        ReconciliationPacket(
            packet_id="topology_only_shortcut",
            beta=0.75,
            protocol_declared=True,
            beta_predeclared=True,
            reconciliation_unit_declared=True,
            observer_pair_schedule_declared=True,
            hierarchy_capacity_declared=True,
            timing_metric_declared=False,
            continuous_formula_declared=True,
            measured_rounds=expected_protocol_rounds(64, 0.75),
            topology_only=True,
            **{k: v for k, v in base.items() if k not in {
                "protocol_declared",
                "beta_predeclared",
                "reconciliation_unit_declared",
                "observer_pair_schedule_declared",
                "hierarchy_capacity_declared",
                "timing_metric_declared",
                "continuous_formula_declared",
            }},
        ),
        ReconciliationPacket(
            packet_id="posthoc_beta_shortcut",
            beta=0.75,
            beta_predeclared=False,
            measured_rounds=expected_protocol_rounds(64, 0.75),
            posthoc_beta=True,
            **{k: v for k, v in base.items() if k not in {"beta_predeclared"}},
        ),
        ReconciliationPacket(
            packet_id="hidden_timing_shortcut",
            beta=0.75,
            timing_metric_declared=False,
            measured_rounds=expected_protocol_rounds(64, 0.75),
            hidden_timing_shortcut=True,
            **{k: v for k, v in base.items() if k not in {"timing_metric_declared"}},
        ),
        ReconciliationPacket(
            packet_id="round_mismatch_control",
            beta=0.75,
            measured_rounds=expected_protocol_rounds(64, 0.75) + 1,
            **base,
        ),
        ReconciliationPacket(
            packet_id="promotion_or_cross_repo_shortcut",
            beta=0.75,
            measured_rounds=expected_protocol_rounds(64, 0.75),
            requests_claim_movement=True,
            requests_h7_promotion=True,
            requests_ti_source_truth=True,
            requests_cross_repo_truth_movement=True,
            requests_external_publication=True,
            **base,
        ),
    )


def evaluate_packet(packet: ReconciliationPacket) -> ReconciliationDecision:
    expected = expected_protocol_rounds(packet.event_count, packet.beta)
    capacity = hierarchy_capacity(packet.event_count, packet.beta)
    missing = missing_requirements(packet)
    blocked = blocked_shortcuts(packet)

    if blocked:
        return decision(
            packet,
            admitted=False,
            label="BLOCKED_GOVERNANCE_OR_CROSS_REPO_SHORTCUT",
            action="stop",
            expected=expected,
            capacity=capacity,
            missing=missing,
            blocked=blocked,
            strongest=(
                "Protocol grounding cannot move claims, H7, Temporal Issuance "
                "source truth, public posture, external publication, or cross-repo truth."
            ),
        )
    if packet.formula_only:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_FORMULA_ONLY_NOT_PROTOCOL",
            action="reject",
            expected=expected,
            capacity=capacity,
            missing=missing,
            blocked=(),
            formula_only_rejected=True,
            strongest=(
                "The continuous formula alone is not a reconciliation protocol."
            ),
        )
    if packet.topology_only:
        return decision(
            packet,
            admitted=False,
            label="ABSORBED_BY_TOPOLOGY_ONLY_NO_TIMING_METRIC",
            action="record_absorption",
            expected=expected,
            capacity=capacity,
            missing=missing,
            blocked=(),
            topology_only_absorbed=True,
            strongest=(
                "Gluing topology alone is absorbed unless the timing metric and "
                "round schedule are independently declared."
            ),
        )
    if packet.posthoc_beta or not packet.beta_predeclared:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_POSTHOC_BETA",
            action="reject",
            expected=expected,
            capacity=capacity,
            missing=missing,
            blocked=(),
            posthoc_beta_rejected=True,
            strongest=(
                "A beta chosen after the pair or transcript is selected cannot "
                "ground the Cap_TI capability."
            ),
        )
    if packet.hidden_timing_shortcut:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_HIDDEN_TIMING_SHORTCUT",
            action="reject",
            expected=expected,
            capacity=capacity,
            missing=missing,
            blocked=(),
            hidden_timing_rejected=True,
            strongest=(
                "Hidden timing cannot be added after the same-neighbor freeze "
                "as an unexplained capability separator."
            ),
        )
    if missing:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_INCOMPLETE_PROTOCOL_PACKET",
            action="reject",
            expected=expected,
            capacity=capacity,
            missing=missing,
            blocked=(),
            strongest="The packet has not paid the T513 protocol minimum.",
        )
    if packet.measured_rounds != expected:
        return decision(
            packet,
            admitted=False,
            label="REJECTED_PROTOCOL_ROUND_MISMATCH",
            action="reject",
            expected=expected,
            capacity=capacity,
            missing=missing,
            blocked=(),
            strongest=(
                "The declared protocol transcript does not match the finite "
                "ceil(n^(1 - beta)) round interpretation."
            ),
        )
    return decision(
        packet,
        admitted=True,
        label="ADMITTED_PROTOCOL_GROUNDING_REVIEW_TARGET",
        action="review_only",
        expected=expected,
        capacity=capacity,
        missing=(),
        blocked=(),
        strongest=(
            "The packet grounds R(beta) as a finite reconciliation protocol "
            "review target only. It does not promote Cap_TI or source truth."
        ),
    )


def missing_requirements(packet: ReconciliationPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.protocol_declared:
        missing.append("finite reconciliation protocol")
    if not packet.beta_predeclared:
        missing.append("predeclared beta metric")
    if not packet.reconciliation_unit_declared:
        missing.append("reconciliation unit")
    if not packet.observer_pair_schedule_declared:
        missing.append("observer-pair schedule")
    if not packet.hierarchy_capacity_declared:
        missing.append("hierarchy capacity")
    if not packet.timing_metric_declared:
        missing.append("timing metric")
    if not packet.continuous_formula_declared:
        missing.append("continuous R(beta) formula")
    if not packet.positive_control_included:
        missing.append("positive control")
    if not packet.null_control_included:
        missing.append("null control")
    if not packet.causal_order_matched:
        missing.append("matched causal order")
    if not packet.entropy_matched:
        missing.append("matched entropy")
    if not packet.gluing_topology_matched:
        missing.append("matched gluing topology")
    return tuple(missing)


def blocked_shortcuts(packet: ReconciliationPacket) -> tuple[str, ...]:
    blocked: list[str] = []
    if packet.requests_claim_movement:
        blocked.append("claim_movement")
    if packet.requests_h7_promotion:
        blocked.append("h7_promotion")
    if packet.requests_ti_source_truth:
        blocked.append("temporal_issuance_source_truth")
    if packet.requests_cross_repo_truth_movement:
        blocked.append("cross_repo_truth_movement")
    if packet.requests_external_publication:
        blocked.append("external_publication")
    return tuple(blocked)


def decision(
    packet: ReconciliationPacket,
    admitted: bool,
    label: str,
    action: str,
    expected: int,
    capacity: int,
    missing: tuple[str, ...],
    blocked: tuple[str, ...],
    strongest: str,
    formula_only_rejected: bool = False,
    topology_only_absorbed: bool = False,
    posthoc_beta_rejected: bool = False,
    hidden_timing_rejected: bool = False,
) -> ReconciliationDecision:
    return ReconciliationDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        review_target_only=admitted,
        expected_rounds=expected,
        measured_rounds=packet.measured_rounds,
        hierarchy_capacity=capacity,
        protocol_grounded=admitted,
        formula_only_rejected=formula_only_rejected,
        topology_only_absorbed=topology_only_absorbed,
        posthoc_beta_rejected=posthoc_beta_rejected,
        hidden_timing_rejected=hidden_timing_rejected,
        missing_requirements=missing,
        blocked_shortcuts=blocked,
        strongest_allowed_reading=strongest,
    )


def decision_dict(item: ReconciliationDecision) -> dict[str, Any]:
    return {
        "packet_id": item.packet_id,
        "admitted": item.admitted,
        "label": item.label,
        "action": item.action,
        "review_target_only": item.review_target_only,
        "expected_rounds": item.expected_rounds,
        "measured_rounds": item.measured_rounds,
        "hierarchy_capacity": item.hierarchy_capacity,
        "protocol_grounded": item.protocol_grounded,
        "formula_only_rejected": item.formula_only_rejected,
        "topology_only_absorbed": item.topology_only_absorbed,
        "posthoc_beta_rejected": item.posthoc_beta_rejected,
        "hidden_timing_rejected": item.hidden_timing_rejected,
        "missing_requirements": list(item.missing_requirements),
        "blocked_shortcuts": list(item.blocked_shortcuts),
        "strongest_allowed_reading": item.strongest_allowed_reading,
    }


def future_packet_minimum() -> tuple[str, ...]:
    return (
        "predeclare beta and its timing metric before pair selection",
        "declare the finite reconciliation unit and observer-pair schedule",
        "declare hierarchy capacity as ceil(n^beta)",
        "map continuous R(beta) to integer protocol rounds as ceil(n^(1 - beta))",
        "include high-beta and low-beta positive controls under matched freeze data",
        "include same-beta null controls",
        "match causal order, entropy, and gluing topology before scoring beta",
        "reject formula-only, topology-only, post-hoc beta, and hidden-timing shortcuts",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "Cap_TI promotion",
        "Temporal Issuance source truth",
        "H7 support",
        "physical-substrate theorem",
        "source-object contract completion",
        "claim-ledger movement",
        "canon verdict movement",
        "roadmap movement",
        "README movement",
        "North Star movement",
        "public-posture movement",
        "hard-policy movement",
        "external publication",
        "cross-repo truth movement",
    )


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {packet_id} | {admitted} | {label} | {expected} | {measured} | {capacity} | {missing} | {blocked} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            expected=decision["expected_rounds"],
            measured=decision["measured_rounds"],
            capacity=decision["hierarchy_capacity"],
            missing=", ".join(decision["missing_requirements"]) or "none",
            blocked=", ".join(decision["blocked_shortcuts"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    future = [f"- {item}" for item in payload["future_packet_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]
    protocol = payload["protocol_interpretation"]

    return "\n".join(
        [
            "# T513 - Cap_TI Reconciliation Protocol Gate - v0.1 results",
            "",
            "> TaF-side protocol-grounding gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T513-cap-ti-reconciliation-protocol-gate.md`",
            "- Model: `models/cap_ti_reconciliation_protocol_gate.py`",
            "- Tests: `tests/test_cap_ti_reconciliation_protocol_gate.py`",
            f"- Source spec: `{payload['source_spec']}`",
            f"- Artifact JSON: `results/{ARTIFACT_ID}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Protocol Interpretation",
            "",
            f"- Continuous formula: `{protocol['continuous_formula']}`",
            f"- Finite rounds: `{protocol['finite_rounds']}`",
            f"- Hierarchy capacity: `{protocol['hierarchy_capacity']}`",
            f"- Round reading: {protocol['round_reading']}",
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Expected rounds | Measured rounds | Hierarchy capacity | Missing requirements | Blocked shortcuts |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Future Packet Minimum",
            "",
            *future,
            "",
            "## What This Does Not Earn",
            "",
            *blocked,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
