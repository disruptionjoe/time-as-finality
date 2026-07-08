"""T507: finality record-redundancy double gate.

The unnumbered finality discriminator isolated the mirror-sector record
reading to an admissible-operation question. The follow-up ghost-parity probe
then found that hiddenness also depends on the observer normalization rule.

This module turns those two exploratory scripts into a governed gate. It does
not decide BRST exactness, real Krein quantization, or physics truth. It only
checks the finite carrier consequence:

* positivity-preserving operations recover no mirror difference: redundancy;
* full-Krein collective operations can recover the difference: record-like;
* full-space Born normalization leaks mirror weight: not hidden;
* self-normalized/projector Born hides the mirror: hidden only in that frame.

The hidden-record reading is therefore admitted only as review material in the
double-special corner: Krein retention plus self-normalized observation.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T507-finality-record-redundancy-double-gate-v0.1"
VERDICT = "FINALITY_RECORD_REDUNDANCY_DOUBLE_GATE_BUILT_DEFAULT_REDUNDANCY"
SOURCE_DISCRIMINATOR = "models/finality_records_vs_redundancy_discriminator.py"
SOURCE_PROBE = "models/ghost_parity_physicality_probe.py"


@dataclass(frozen=True)
class GatePacket:
    packet_id: str
    description: str
    operation_algebra: str
    normalization_rule: str
    mirror_difference_present: bool
    full_space_positive_inner_product: bool
    quantization_leg_typed_by_constraint_structure: bool
    includes_individual_control: bool
    includes_collective_control: bool
    includes_full_born_control: bool
    includes_selfnorm_control: bool
    declares_brst_status_without_constraint_structure: bool = False
    requests_claim_or_public_posture: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class GateDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    mirror_recoverable_by_declared_algebra: bool
    hidden_under_declared_normalization: bool
    full_born_leakage_present: bool
    self_normalized_hiddenness_present: bool
    double_special_corner: bool
    counts_as_claim_evidence: bool
    recovery_score: float
    full_born_max_delta: float
    selfnorm_max_delta: float
    missing_requirements: tuple[str, ...]
    strongest_allowed_reading: str


def run() -> dict[str, Any]:
    carrier = evaluate_carrier()
    packets = packet_fixtures()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    by_id = {decision.packet_id: decision for decision in decisions}

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "source_discriminator": SOURCE_DISCRIMINATOR,
        "source_probe": SOURCE_PROBE,
        "objective": (
            "Make the finality records-vs-redundancy discriminator and "
            "ghost-parity hiddenness probe into a numbered TaF gate. The "
            "standard positivity/BRST route is recorded as redundancy; the "
            "hidden-record reading is admitted only as a double-gated review "
            "target requiring Krein retention and self-normalized observation."
        ),
        "carrier": carrier,
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "overall": {
            "standard_default_redundancy": (
                by_id["standard_positivity_default"].label
                == "REDUNDANCY_UNDER_STANDARD_POSITIVITY"
            ),
            "full_krein_collective_recovers_mirror_difference": carrier[
                "collective_recovery_score"
            ]
            > 0.1,
            "positivity_preserving_recovers_no_mirror_difference": carrier[
                "individual_recovery_score"
            ]
            < 1e-9,
            "full_born_leaks_hiddenness": carrier["full_born_max_delta"] > 1e-6,
            "self_normalized_hides_mirror": carrier["selfnorm_max_delta"] < 1e-9,
            "hidden_record_corner_admitted_review_only": by_id[
                "krein_retention_selfnorm_corner"
            ].admitted,
            "record_reading_requires_two_special_bets": True,
            "default_corner": "redundancy",
            "claim_movement": False,
            "roadmap_movement": False,
            "readme_movement": False,
            "north_star_movement": False,
            "public_posture_movement": False,
            "hard_policy_movement": False,
            "protected_license_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
            "sibling_repo_inspection": False,
            "brst_exactness_decided": False,
            "krein_quantization_decided": False,
            "physics_claim_earned": False,
        },
        "future_packet_minimum": future_packet_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T507 turns the finality residual into a two-stage finite gate. "
            "First, the admissible operation algebra decides whether the "
            "mirror difference is recoverable: positivity-preserving/block-"
            "diagonal operations recover nothing, while full-Krein collective "
            "boosts recover a mirror difference. Second, the normalization "
            "rule decides whether a recovered physical mirror can still be "
            "hidden: full-space Born normalization leaks mirror weight into "
            "W+-restricted statistics, while self-normalized/projector Born "
            "hides it. The hidden-record reading is therefore only a review "
            "target in the double-special Krein-retention plus self-normalized "
            "corner; the default positivity/BRST plus full-Born corner remains "
            "redundancy."
        ),
    }


def evaluate_carrier() -> dict[str, Any]:
    psi, psip = states(mirror_difference_present=True)
    individual_recovery = max(
        recovery(individual_operation(theta_p, theta_m), psi, psip)
        for theta_p in [i * math.pi / 8 for i in range(8)]
        for theta_m in [i * math.pi / 8 for i in range(8)]
    )
    collective_recovery = max(
        recovery(collective_boost(eta), psi, psip)
        for eta in [0.2 * i for i in range(1, 8)]
    )
    full_born = visibility_deltas(psi, psip, "full_born")
    selfnorm = visibility_deltas(psi, psip, "self_normalized")

    return {
        "carrier": "minimal_real_krein_space_dim_4",
        "krein_signature": "(+,+,-,-)",
        "states_share_wplus": wplus_distance(psi, psip) < 1e-12,
        "states_differ_in_wminus": wminus_distance(psi, psip) > 0.1,
        "mirror_negative_under_krein_form": ip_k([0, 0, 1, 0], [0, 0, 1, 0]) < 0,
        "mirror_positive_under_standard_inner_product": ip_i(
            [0, 0, 1, 0], [0, 0, 1, 0]
        )
        > 0,
        "individual_recovery_score": individual_recovery,
        "collective_recovery_score": collective_recovery,
        "physical_recovery_score": individual_recovery,
        "full_born_deltas": full_born,
        "selfnorm_deltas": selfnorm,
        "full_born_max_delta": max(full_born.values()),
        "selfnorm_max_delta": max(selfnorm.values()),
        "full_space_observer_mirror_number_delta": full_space_mirror_number_delta(
            psi, psip
        ),
    }


def packet_fixtures() -> tuple[GatePacket, ...]:
    return (
        GatePacket(
            packet_id="standard_positivity_default",
            description=(
                "Default packet: physical operations preserve positivity and "
                "therefore do not move the negative mirror sector into W+."
            ),
            operation_algebra="positivity_preserving",
            normalization_rule="full_born",
            mirror_difference_present=True,
            full_space_positive_inner_product=False,
            quantization_leg_typed_by_constraint_structure=False,
            includes_individual_control=True,
            includes_collective_control=True,
            includes_full_born_control=True,
            includes_selfnorm_control=True,
        ),
        GatePacket(
            packet_id="krein_retention_full_born",
            description=(
                "Krein-retention packet with full-space Born normalization: "
                "the mirror is recoverable, but W+-restricted normalized "
                "statistics leak mirror weight."
            ),
            operation_algebra="full_krein_collective",
            normalization_rule="full_born",
            mirror_difference_present=True,
            full_space_positive_inner_product=True,
            quantization_leg_typed_by_constraint_structure=False,
            includes_individual_control=True,
            includes_collective_control=True,
            includes_full_born_control=True,
            includes_selfnorm_control=True,
        ),
        GatePacket(
            packet_id="krein_retention_selfnorm_corner",
            description=(
                "The only hidden-record review corner: full-Krein recovery "
                "plus self-normalized/projector Born observation."
            ),
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            mirror_difference_present=True,
            full_space_positive_inner_product=True,
            quantization_leg_typed_by_constraint_structure=False,
            includes_individual_control=True,
            includes_collective_control=True,
            includes_full_born_control=True,
            includes_selfnorm_control=True,
        ),
        GatePacket(
            packet_id="positivity_selfnorm_no_recovery",
            description=(
                "Self-normalization alone does not create a record if the "
                "admissible algebra still cannot recover the mirror sector."
            ),
            operation_algebra="positivity_preserving",
            normalization_rule="self_normalized",
            mirror_difference_present=True,
            full_space_positive_inner_product=False,
            quantization_leg_typed_by_constraint_structure=False,
            includes_individual_control=True,
            includes_collective_control=True,
            includes_full_born_control=True,
            includes_selfnorm_control=True,
        ),
        GatePacket(
            packet_id="degenerate_no_mirror_spread_control",
            description=(
                "Control with no W- difference: any hidden-record reading is "
                "degenerate because there is no mirror spread to recover."
            ),
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            mirror_difference_present=False,
            full_space_positive_inner_product=True,
            quantization_leg_typed_by_constraint_structure=False,
            includes_individual_control=True,
            includes_collective_control=True,
            includes_full_born_control=True,
            includes_selfnorm_control=True,
        ),
        GatePacket(
            packet_id="untyped_brst_assertion_shortcut",
            description=(
                "Asserts BRST exactness or nontriviality without supplying "
                "the constraint/gauge structure that would decide it."
            ),
            operation_algebra="positivity_preserving",
            normalization_rule="full_born",
            mirror_difference_present=True,
            full_space_positive_inner_product=False,
            quantization_leg_typed_by_constraint_structure=False,
            includes_individual_control=True,
            includes_collective_control=True,
            includes_full_born_control=True,
            includes_selfnorm_control=True,
            declares_brst_status_without_constraint_structure=True,
        ),
        GatePacket(
            packet_id="claim_cross_repo_shortcut",
            description=(
                "Treats the finite gate as permission to move claims, public "
                "posture, external publication, or sibling-repo truth."
            ),
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            mirror_difference_present=True,
            full_space_positive_inner_product=True,
            quantization_leg_typed_by_constraint_structure=False,
            includes_individual_control=True,
            includes_collective_control=True,
            includes_full_born_control=True,
            includes_selfnorm_control=True,
            requests_claim_or_public_posture=True,
            requests_external_publication=True,
            requests_cross_repo_truth=True,
        ),
    )


def evaluate_packet(packet: GatePacket) -> GateDecision:
    psi, psip = states(packet.mirror_difference_present)
    recovery_score = recovery_for_algebra(packet.operation_algebra, psi, psip)
    full_born_max_delta = max(visibility_deltas(psi, psip, "full_born").values())
    selfnorm_max_delta = max(
        visibility_deltas(psi, psip, "self_normalized").values()
    )
    declared_delta = (
        full_born_max_delta
        if packet.normalization_rule == "full_born"
        else selfnorm_max_delta
    )
    recoverable = recovery_score > 0.1
    hidden = declared_delta < 1e-9
    full_born_leaks = full_born_max_delta > 1e-6
    selfnorm_hides = selfnorm_max_delta < 1e-9
    double_special = (
        packet.operation_algebra == "full_krein_collective"
        and packet.normalization_rule == "self_normalized"
        and packet.full_space_positive_inner_product
        and recoverable
        and hidden
    )
    missing = missing_requirements(packet)

    if packet.requests_claim_or_public_posture:
        return decision(
            packet,
            False,
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            "stop",
            recoverable,
            hidden,
            full_born_leaks,
            selfnorm_hides,
            double_special,
            recovery_score,
            full_born_max_delta,
            selfnorm_max_delta,
            missing,
            "The finite gate cannot move claims, public posture, or hard policy.",
        )
    if packet.requests_external_publication or packet.requests_cross_repo_truth:
        return decision(
            packet,
            False,
            "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT",
            "stop",
            recoverable,
            hidden,
            full_born_leaks,
            selfnorm_hides,
            double_special,
            recovery_score,
            full_born_max_delta,
            selfnorm_max_delta,
            missing,
            "External publication and sibling-repo truth movement are outside this run.",
        )
    if packet.declares_brst_status_without_constraint_structure:
        return decision(
            packet,
            False,
            "REJECTED_UNTYPED_BRST_STATUS_ASSERTION",
            "reject",
            recoverable,
            hidden,
            full_born_leaks,
            selfnorm_hides,
            double_special,
            recovery_score,
            full_born_max_delta,
            selfnorm_max_delta,
            missing,
            "BRST exactness or nontriviality must be decided by a typed constraint/gauge structure.",
        )
    if not packet.mirror_difference_present:
        return decision(
            packet,
            False,
            "REJECTED_DEGENERATE_NO_MIRROR_SPREAD",
            "reject",
            recoverable,
            hidden,
            full_born_leaks,
            selfnorm_hides,
            double_special,
            recovery_score,
            full_born_max_delta,
            selfnorm_max_delta,
            missing,
            "No hidden-record reading is available without a mirror-sector difference.",
        )
    if missing:
        return decision(
            packet,
            False,
            "REJECTED_INCOMPLETE_DOUBLE_GATE_PACKET",
            "reject",
            recoverable,
            hidden,
            full_born_leaks,
            selfnorm_hides,
            double_special,
            recovery_score,
            full_born_max_delta,
            selfnorm_max_delta,
            missing,
            "The packet lacks the paired algebra and normalization controls.",
        )
    if not recoverable:
        label = (
            "REDUNDANCY_UNDER_STANDARD_POSITIVITY"
            if packet.operation_algebra == "positivity_preserving"
            else "REDUNDANCY_UNDER_DECLARED_ALGEBRA"
        )
        return decision(
            packet,
            False,
            label,
            "record_negative",
            recoverable,
            hidden,
            full_born_leaks,
            selfnorm_hides,
            double_special,
            recovery_score,
            full_born_max_delta,
            selfnorm_max_delta,
            missing,
            "The declared operation algebra recovers no mirror difference; classify as redundancy.",
        )
    if recoverable and not hidden:
        return decision(
            packet,
            False,
            "REJECTED_AS_HIDDEN_RECORD_FULL_BORN_LEAKAGE",
            "demote_to_visible_physical_dof",
            recoverable,
            hidden,
            full_born_leaks,
            selfnorm_hides,
            double_special,
            recovery_score,
            full_born_max_delta,
            selfnorm_max_delta,
            missing,
            "Full-space Born normalization makes the physicalized mirror visible, not hidden.",
        )
    if double_special:
        return decision(
            packet,
            True,
            "ADMITTED_HIDDEN_RECORD_REVIEW_TARGET_DOUBLE_GATED",
            "review_only",
            recoverable,
            hidden,
            full_born_leaks,
            selfnorm_hides,
            double_special,
            recovery_score,
            full_born_max_delta,
            selfnorm_max_delta,
            missing,
            "Review target only: hidden-record reading requires both Krein retention and self-normalized observation.",
        )

    return decision(
        packet,
        False,
        "REJECTED_UNPRICED_RECORD_READING",
        "reject",
        recoverable,
        hidden,
        full_born_leaks,
        selfnorm_hides,
        double_special,
        recovery_score,
        full_born_max_delta,
        selfnorm_max_delta,
        missing,
        "The packet does not pay both gates required by the hidden-record reading.",
    )


def missing_requirements(packet: GatePacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.includes_individual_control:
        missing.append("individual_or_positivity_control")
    if not packet.includes_collective_control:
        missing.append("full_krein_collective_control")
    if not packet.includes_full_born_control:
        missing.append("full_born_leakage_control")
    if not packet.includes_selfnorm_control:
        missing.append("self_normalized_hiddenness_control")
    if (
        packet.operation_algebra == "full_krein_collective"
        and not packet.full_space_positive_inner_product
    ):
        missing.append("positive_full_space_inner_product")
    return tuple(missing)


def recovery_for_algebra(algebra: str, psi: list[float], psip: list[float]) -> float:
    if algebra in {"positivity_preserving", "individual_block_diagonal"}:
        return max(
            recovery(individual_operation(theta_p, theta_m), psi, psip)
            for theta_p in [i * math.pi / 8 for i in range(8)]
            for theta_m in [i * math.pi / 8 for i in range(8)]
        )
    if algebra == "full_krein_collective":
        return max(
            recovery(collective_boost(eta), psi, psip)
            for eta in [0.2 * i for i in range(1, 8)]
        )
    raise ValueError(f"unknown algebra: {algebra}")


def states(mirror_difference_present: bool) -> tuple[list[float], list[float]]:
    psi = [0.7, -0.3, 0.5, 0.2]
    if mirror_difference_present:
        return psi, [0.7, -0.3, 0.1, -0.4]
    return psi, [0.7, -0.3, 0.5, 0.2]


def individual_operation(theta_p: float, theta_m: float) -> list[list[float]]:
    cp, sp = math.cos(theta_p), math.sin(theta_p)
    cm, sm = math.cos(theta_m), math.sin(theta_m)
    return [
        [cp, -sp, 0.0, 0.0],
        [sp, cp, 0.0, 0.0],
        [0.0, 0.0, cm, -sm],
        [0.0, 0.0, sm, cm],
    ]


def collective_boost(eta: float) -> list[list[float]]:
    ch, sh = math.cosh(eta), math.sinh(eta)
    return [
        [ch, 0.0, sh, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [sh, 0.0, ch, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def recovery(matrix: list[list[float]], psi: list[float], psip: list[float]) -> float:
    a = wplus(matvec(matrix, psi))
    b = wplus(matvec(matrix, psip))
    return vector_norm([a[0] - b[0], a[1] - b[1]])


def visibility_deltas(
    psi: list[float], psip: list[float], normalization_rule: str
) -> dict[str, float]:
    observables = {
        "projector_a": [[1.0, 0.0], [0.0, 0.0]],
        "mixed_b": [[0.3, 0.4], [0.4, -0.2]],
    }
    if normalization_rule == "full_born":
        fn = wplus_expect_full
    elif normalization_rule == "self_normalized":
        fn = wplus_expect_selfnorm
    else:
        raise ValueError(f"unknown normalization rule: {normalization_rule}")
    return {
        name: abs(fn(psi, observable) - fn(psip, observable))
        for name, observable in observables.items()
    }


def wplus_expect_full(state: list[float], observable: list[list[float]]) -> float:
    component = [state[0], state[1]]
    numerator = sum(
        component[i] * observable[i][j] * component[j]
        for i in range(2)
        for j in range(2)
    )
    return numerator / ip_i(state, state)


def wplus_expect_selfnorm(state: list[float], observable: list[list[float]]) -> float:
    component = [state[0], state[1]]
    numerator = sum(
        component[i] * observable[i][j] * component[j]
        for i in range(2)
        for j in range(2)
    )
    denominator = component[0] * component[0] + component[1] * component[1]
    return numerator / denominator


def full_space_mirror_number_delta(psi: list[float], psip: list[float]) -> float:
    mirror_number = [0.0, 0.0, 1.0, 1.0]
    return abs(
        sum(psi[i] * mirror_number[i] * psi[i] for i in range(4)) / ip_i(psi, psi)
        - sum(psip[i] * mirror_number[i] * psip[i] for i in range(4))
        / ip_i(psip, psip)
    )


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    ]


def vector_norm(vector: list[float]) -> float:
    return math.sqrt(sum(item * item for item in vector))


def wplus(vector: list[float]) -> list[float]:
    return [vector[0], vector[1]]


def wplus_distance(psi: list[float], psip: list[float]) -> float:
    return vector_norm([psi[0] - psip[0], psi[1] - psip[1]])


def wminus_distance(psi: list[float], psip: list[float]) -> float:
    return vector_norm([psi[2] - psip[2], psi[3] - psip[3]])


def ip_i(left: list[float], right: list[float]) -> float:
    return sum(left[i] * right[i] for i in range(4))


def ip_k(left: list[float], right: list[float]) -> float:
    signature = [1.0, 1.0, -1.0, -1.0]
    return sum(left[i] * signature[i] * right[i] for i in range(4))


def future_packet_minimum() -> tuple[str, ...]:
    return (
        "declare the admissible operation algebra before the record/redundancy verdict",
        "include a positivity-preserving or individual-access control",
        "include a full-Krein collective recovery control",
        "declare the observer normalization rule before checking hiddenness",
        "include a full-space Born leakage control",
        "include a self-normalized/projector Born hiddenness control",
        "show a nondegenerate mirror-sector spread rather than a zero-difference pair",
        "type BRST exactness or nontriviality through a constraint/gauge structure before asserting it",
        "keep any Krein-retention plus self-normalized success review-only until physics-side constraints are supplied",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "BRST exactness decision",
        "BRST cohomology nontriviality decision",
        "Krein-retention quantization accepted as physical",
        "full-Krein collective operations accepted as physically admissible",
        "self-normalized observer convention accepted as physical",
        "hidden mirror record claim",
        "source-action truth",
        "mass-gap evidence",
        "claim-ledger movement",
        "roadmap movement",
        "README movement",
        "North Star movement",
        "public-posture movement",
        "hard-policy movement",
        "external publication",
        "cross-repo truth movement",
    )


def decision(
    packet: GatePacket,
    admitted: bool,
    label: str,
    action: str,
    recoverable: bool,
    hidden: bool,
    full_born_leaks: bool,
    selfnorm_hides: bool,
    double_special: bool,
    recovery_score: float,
    full_born_max_delta: float,
    selfnorm_max_delta: float,
    missing: tuple[str, ...],
    strongest_allowed_reading: str,
) -> GateDecision:
    return GateDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        review_target_only=admitted,
        mirror_recoverable_by_declared_algebra=recoverable,
        hidden_under_declared_normalization=hidden,
        full_born_leakage_present=full_born_leaks,
        self_normalized_hiddenness_present=selfnorm_hides,
        double_special_corner=double_special,
        counts_as_claim_evidence=False,
        recovery_score=recovery_score,
        full_born_max_delta=full_born_max_delta,
        selfnorm_max_delta=selfnorm_max_delta,
        missing_requirements=missing,
        strongest_allowed_reading=strongest_allowed_reading,
    )


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {packet_id} | {admitted} | {label} | {recoverable} | {hidden} | {double} | {recovery:.3e} | {full:.3e} | {selfnorm:.3e} | {missing} |".format(
            packet_id=decision_item["packet_id"],
            admitted="yes" if decision_item["admitted"] else "no",
            label=decision_item["label"],
            recoverable=(
                "yes"
                if decision_item["mirror_recoverable_by_declared_algebra"]
                else "no"
            ),
            hidden=(
                "yes" if decision_item["hidden_under_declared_normalization"] else "no"
            ),
            double="yes" if decision_item["double_special_corner"] else "no",
            recovery=decision_item["recovery_score"],
            full=decision_item["full_born_max_delta"],
            selfnorm=decision_item["selfnorm_max_delta"],
            missing=", ".join(decision_item["missing_requirements"]) or "none",
        )
        for decision_item in payload["decisions"]
    ]
    future = [f"- {item}" for item in payload["future_packet_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T507 - Finality Record-Redundancy Double Gate - v0.1 results",
            "",
            "> TaF-side finite review gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T507-finality-record-redundancy-double-gate.md`",
            "- Model: `models/finality_record_redundancy_double_gate.py`",
            "- Tests: `tests/test_finality_record_redundancy_double_gate.py`",
            f"- Source discriminator: `{payload['source_discriminator']}`",
            f"- Source probe: `{payload['source_probe']}`",
            f"- Artifact JSON: `results/{ARTIFACT}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Carrier Checks",
            "",
            f"- Individual/positivity recovery: `{payload['carrier']['individual_recovery_score']:.3e}`",
            f"- Full-Krein collective recovery: `{payload['carrier']['collective_recovery_score']:.3e}`",
            f"- Full-Born maximum W+ leakage: `{payload['carrier']['full_born_max_delta']:.3e}`",
            f"- Self-normalized maximum W+ leakage: `{payload['carrier']['selfnorm_max_delta']:.3e}`",
            f"- Full-space mirror-number delta: `{payload['carrier']['full_space_observer_mirror_number_delta']:.3e}`",
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Recoverable? | Hidden? | Double-special corner? | Recovery | Full-Born delta | Selfnorm delta | Missing requirements |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
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
        json_path = results_dir / f"{ARTIFACT}.json"
        md_path = results_dir / f"{ARTIFACT}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
