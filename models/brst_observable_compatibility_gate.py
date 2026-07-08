"""T509: BRST observable-compatibility gate.

T508 made the BRST/exactness burden executable, but it treated the Q-closed
observable discipline as a declared packet field. This gate makes that field
finite and checkable.

The key distinction is quotient compatibility. A nontrivial mirror class is
not enough for a hidden-record reading if the recovery operation or readout is
not well-defined after quotienting by exact states:

* operations must descend through the BRST quotient;
* observables/readouts must be exact-invariant;
* W+ representative leakage is not a cohomology observable;
* direct cohomology observables are review targets only, not claim evidence.

No claim ledger, public posture, BRST physics decision, Krein quantization
decision, source-action truth, or cross-repo truth is moved by this gate.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T509-brst-observable-compatibility-gate-v0.1"
VERDICT = "BRST_OBSERVABLE_COMPATIBILITY_GATE_BUILT_RECOVERY_BLOCKED"
SOURCE_GATE = "tests/T508-brst-cohomology-record-admission-gate.md"
BASIS = ("physical_exact", "mirror", "gauge_seed", "auxiliary")
MIRROR = (0.0, 1.0, 0.0, 0.0)
STATE_A = (0.7, 0.5, 0.0, 0.0)
STATE_B = (0.7, -0.5, 0.0, 0.0)


@dataclass(frozen=True)
class ObservablePacket:
    packet_id: str
    description: str
    q_kind: str
    operation_kind: str
    readout_kind: str
    q_predeclared: bool
    quotient_declared: bool
    operation_predeclared: bool
    readout_predeclared: bool
    includes_exact_mirror_control: bool
    includes_nondescending_operation_control: bool
    includes_representative_leakage_control: bool
    includes_cohomology_observable_control: bool
    includes_t507_t508_controls: bool
    requests_claim_or_public_posture: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class ObservableDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    q_nilpotent: bool
    mirror_q_closed: bool
    mirror_q_exact: bool
    mirror_cohomology_nontrivial: bool
    operation_descends_to_cohomology: bool
    readout_descends_to_cohomology: bool
    wplus_recovery_score: float
    cohomology_readout_delta: float
    representative_leakage: bool
    counts_as_claim_evidence: bool
    missing_requirements: tuple[str, ...]
    strongest_allowed_reading: str


def run() -> dict[str, Any]:
    packets = packet_fixtures()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    by_id = {decision.packet_id: decision for decision in decisions}

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "source_gate": SOURCE_GATE,
        "objective": (
            "Make T508's Q-closed observable discipline executable. A "
            "nontrivial mirror cohomology class is reviewable only through "
            "operations that descend through the BRST quotient and readouts "
            "that annihilate exact representative changes."
        ),
        "basis": BASIS,
        "states": {
            "state_a": STATE_A,
            "state_b": STATE_B,
            "share_wplus_before_operation": wplus_delta(STATE_A, STATE_B) < 1e-12,
            "mirror_delta_before_operation": abs(STATE_A[1] - STATE_B[1]),
        },
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "constraint_summaries": {
            kind: summarize_constraint(kind)
            for kind in ("nontrivial_mirror", "exact_mirror")
        },
        "operation_summaries": {
            kind: summarize_operation(kind, "nontrivial_mirror")
            for kind in (
                "full_krein_boost",
                "representative_leakage_chain_map",
                "cohomology_scaling",
                "identity",
            )
        },
        "readout_summaries": {
            kind: summarize_readout(kind, "nontrivial_mirror")
            for kind in ("wplus_projector", "mirror_cohomology_functional")
        },
        "overall": {
            "t508_full_krein_recovery_rejected_by_quotient_discipline": by_id[
                "t508_full_krein_recovery"
            ].label
            == "REJECTED_RECOVERY_OPERATION_NOT_BRST_COMPATIBLE",
            "representative_leakage_rejected": by_id[
                "chain_map_representative_leakage"
            ].label
            == "REJECTED_EXACT_REPRESENTATIVE_LEAKAGE",
            "direct_cohomology_observable_admitted_review_only": by_id[
                "direct_cohomology_observable"
            ].admitted,
            "exact_mirror_routes_to_redundancy": by_id[
                "exact_mirror_redundancy_control"
            ].label
            == "BRST_EXACT_REDUNDANCY_RECORDED",
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
            "brst_exactness_decided_for_real_physics": False,
            "brst_nontriviality_decided_for_real_physics": False,
            "krein_quantization_decided": False,
            "hidden_mirror_record_claim_earned": False,
            "physics_claim_earned": False,
        },
        "future_packet_minimum": future_packet_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T509 makes the T508 observable/readout burden explicit. The "
            "T507-style full-Krein recovery of a mirror difference is rejected "
            "in the finite BRST fixture because it does not descend through "
            "the quotient. A chain-map operation can create W+ representative "
            "leakage, but W+ readout is not exact-invariant, so that leakage "
            "is rejected as gauge-representative dependence. Only a direct "
            "exact-invariant cohomology readout is admitted, and only as a "
            "review target rather than hidden-record or physics evidence."
        ),
    }


def packet_fixtures() -> tuple[ObservablePacket, ...]:
    return (
        ObservablePacket(
            packet_id="t508_full_krein_recovery",
            description=(
                "T508's admitted corner tries to use a full-Krein boost to "
                "recover the mirror difference into W+."
            ),
            q_kind="nontrivial_mirror",
            operation_kind="full_krein_boost",
            readout_kind="wplus_projector",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=True,
            includes_exact_mirror_control=True,
            includes_nondescending_operation_control=True,
            includes_representative_leakage_control=True,
            includes_cohomology_observable_control=True,
            includes_t507_t508_controls=True,
        ),
        ObservablePacket(
            packet_id="chain_map_representative_leakage",
            description=(
                "A chain-map operation sends mirror to mirror plus an exact "
                "physical representative, creating W+ leakage without a "
                "cohomology readout."
            ),
            q_kind="nontrivial_mirror",
            operation_kind="representative_leakage_chain_map",
            readout_kind="wplus_projector",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=True,
            includes_exact_mirror_control=True,
            includes_nondescending_operation_control=True,
            includes_representative_leakage_control=True,
            includes_cohomology_observable_control=True,
            includes_t507_t508_controls=True,
        ),
        ObservablePacket(
            packet_id="direct_cohomology_observable",
            description=(
                "A direct mirror-class functional annihilates exact states and "
                "separates the nontrivial cohomology class."
            ),
            q_kind="nontrivial_mirror",
            operation_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=True,
            includes_exact_mirror_control=True,
            includes_nondescending_operation_control=True,
            includes_representative_leakage_control=True,
            includes_cohomology_observable_control=True,
            includes_t507_t508_controls=True,
        ),
        ObservablePacket(
            packet_id="cohomology_scaling_control",
            description=(
                "A quotient-descending operation scales the mirror class; it "
                "is observable only by a direct cohomology readout."
            ),
            q_kind="nontrivial_mirror",
            operation_kind="cohomology_scaling",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=True,
            includes_exact_mirror_control=True,
            includes_nondescending_operation_control=True,
            includes_representative_leakage_control=True,
            includes_cohomology_observable_control=True,
            includes_t507_t508_controls=True,
        ),
        ObservablePacket(
            packet_id="exact_mirror_redundancy_control",
            description=(
                "Exact-control packet: the mirror lies in im(Q), so mirror "
                "readout does not descend and the class routes to redundancy."
            ),
            q_kind="exact_mirror",
            operation_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=True,
            includes_exact_mirror_control=True,
            includes_nondescending_operation_control=True,
            includes_representative_leakage_control=True,
            includes_cohomology_observable_control=True,
            includes_t507_t508_controls=True,
        ),
        ObservablePacket(
            packet_id="wplus_observable_shortcut",
            description=(
                "A packet declares ordinary W+ readout as physical without "
                "checking exact-invariance."
            ),
            q_kind="nontrivial_mirror",
            operation_kind="identity",
            readout_kind="wplus_projector",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=True,
            includes_exact_mirror_control=True,
            includes_nondescending_operation_control=True,
            includes_representative_leakage_control=True,
            includes_cohomology_observable_control=True,
            includes_t507_t508_controls=True,
        ),
        ObservablePacket(
            packet_id="post_hoc_readout_shortcut",
            description=(
                "The packet selects the readout after seeing the mirror split."
            ),
            q_kind="nontrivial_mirror",
            operation_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=False,
            includes_exact_mirror_control=True,
            includes_nondescending_operation_control=True,
            includes_representative_leakage_control=True,
            includes_cohomology_observable_control=True,
            includes_t507_t508_controls=True,
        ),
        ObservablePacket(
            packet_id="missing_controls_shortcut",
            description="The packet omits the new T509 controls.",
            q_kind="nontrivial_mirror",
            operation_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=True,
            includes_exact_mirror_control=False,
            includes_nondescending_operation_control=False,
            includes_representative_leakage_control=False,
            includes_cohomology_observable_control=False,
            includes_t507_t508_controls=True,
        ),
        ObservablePacket(
            packet_id="claim_cross_repo_shortcut",
            description="The packet tries to move claim or cross-repo truth.",
            q_kind="nontrivial_mirror",
            operation_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            operation_predeclared=True,
            readout_predeclared=True,
            includes_exact_mirror_control=True,
            includes_nondescending_operation_control=True,
            includes_representative_leakage_control=True,
            includes_cohomology_observable_control=True,
            includes_t507_t508_controls=True,
            requests_claim_or_public_posture=True,
            requests_external_publication=True,
            requests_cross_repo_truth=True,
        ),
    )


def evaluate_packet(packet: ObservablePacket) -> ObservableDecision:
    if packet.requests_claim_or_public_posture:
        return make_decision(
            packet,
            admitted=False,
            label="BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            action="stop",
            missing=(),
            strongest=(
                "Observable compatibility cannot move claims, public posture, "
                "external publication, or cross-repo truth."
            ),
        )
    if packet.requests_external_publication or packet.requests_cross_repo_truth:
        return make_decision(
            packet,
            admitted=False,
            label="BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT",
            action="stop",
            missing=(),
            strongest="External and cross-repo actions are outside this gate.",
        )

    constraint = summarize_constraint(packet.q_kind)
    missing = missing_requirements(packet)

    if not constraint["q_nilpotent"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_NON_NILPOTENT_CONSTRAINT",
            action="reject",
            missing=missing + ("nilpotency Q^2 = 0",),
            strongest="No BRST/cohomology observable exists without Q^2 = 0.",
        )
    if not constraint["mirror_q_closed"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_MIRROR_NOT_Q_CLOSED",
            action="reject",
            missing=missing + ("mirror vector in ker(Q)",),
            strongest="The mirror must be closed before an observable can read its class.",
        )
    if constraint["mirror_q_exact"]:
        return make_decision(
            packet,
            admitted=False,
            label="BRST_EXACT_REDUNDANCY_RECORDED",
            action="record_negative",
            missing=missing,
            strongest=(
                "The mirror is exact in this packet, so exact-invariant "
                "readouts erase it rather than support a hidden-record reading."
            ),
        )
    if missing:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_INCOMPLETE_OBSERVABLE_PACKET",
            action="reject",
            missing=missing,
            strongest="The packet has not paid the quotient/readout controls.",
        )

    operation = summarize_operation(packet.operation_kind, packet.q_kind)
    readout = summarize_readout(packet.readout_kind, packet.q_kind)
    wplus_recovery = operation["wplus_recovery_score"]
    cohomology_delta = readout_delta(packet.operation_kind, packet.readout_kind)
    representative_leakage = (
        operation["operation_descends_to_cohomology"]
        and wplus_recovery > 1e-9
        and not summarize_readout("wplus_projector", packet.q_kind)[
            "readout_descends_to_cohomology"
        ]
    )

    if wplus_recovery > 1e-9 and not operation["operation_descends_to_cohomology"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_RECOVERY_OPERATION_NOT_BRST_COMPATIBLE",
            action="reject",
            missing=(),
            strongest=(
                "The recovery operation exposes W+ differences only by failing "
                "to descend through the BRST quotient."
            ),
        )
    if representative_leakage and not readout["readout_descends_to_cohomology"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_EXACT_REPRESENTATIVE_LEAKAGE",
            action="demote_to_representative_artifact",
            missing=(),
            strongest=(
                "The operation is a chain map, but the W+ signal is exact "
                "representative leakage; it is not a quotient-level observable."
            ),
        )
    if not readout["readout_descends_to_cohomology"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_NON_DESCENDING_READOUT",
            action="reject",
            missing=("exact-invariant readout",),
            strongest=(
                "The declared readout changes under exact representative "
                "shifts and therefore does not define a cohomology observable."
            ),
        )
    if cohomology_delta > 1e-9:
        return make_decision(
            packet,
            admitted=True,
            label="ADMITTED_COHOMOLOGY_OBSERVABLE_REVIEW_TARGET",
            action="review_only",
            missing=(),
            strongest=(
                "A direct exact-invariant cohomology readout separates the "
                "mirror class. This is a review target only, not hidden-record "
                "or physics evidence."
            ),
        )

    return make_decision(
        packet,
        admitted=False,
        label="REJECTED_NO_OBSERVABLE_COHOMOLOGY_SPREAD",
        action="reject",
        missing=(),
        strongest="No quotient-compatible readout separates the tested pair.",
    )


def missing_requirements(packet: ObservablePacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.q_predeclared:
        missing.append("predeclared nilpotent constraint operator Q")
    if not packet.quotient_declared:
        missing.append("declared BRST quotient/cohomology object")
    if not packet.operation_predeclared:
        missing.append("predeclared operation algebra")
    if not packet.readout_predeclared:
        missing.append("predeclared exact-invariant readout")
    if not packet.includes_exact_mirror_control:
        missing.append("exact-mirror redundancy control")
    if not packet.includes_nondescending_operation_control:
        missing.append("non-descending recovery-operation control")
    if not packet.includes_representative_leakage_control:
        missing.append("exact-representative leakage control")
    if not packet.includes_cohomology_observable_control:
        missing.append("direct cohomology-observable control")
    if not packet.includes_t507_t508_controls:
        missing.append("T507/T508 prior controls")
    return tuple(missing)


def make_decision(
    packet: ObservablePacket,
    admitted: bool,
    label: str,
    action: str,
    missing: tuple[str, ...],
    strongest: str,
) -> ObservableDecision:
    constraint = summarize_constraint(packet.q_kind)
    operation = summarize_operation(packet.operation_kind, packet.q_kind)
    readout = summarize_readout(packet.readout_kind, packet.q_kind)
    wplus_recovery = operation["wplus_recovery_score"]
    cohomology_delta = readout_delta(packet.operation_kind, packet.readout_kind)
    representative_leakage = (
        operation["operation_descends_to_cohomology"]
        and wplus_recovery > 1e-9
        and not summarize_readout("wplus_projector", packet.q_kind)[
            "readout_descends_to_cohomology"
        ]
    )

    return ObservableDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        review_target_only=admitted,
        q_nilpotent=constraint["q_nilpotent"],
        mirror_q_closed=constraint["mirror_q_closed"],
        mirror_q_exact=constraint["mirror_q_exact"],
        mirror_cohomology_nontrivial=constraint["mirror_cohomology_nontrivial"],
        operation_descends_to_cohomology=operation[
            "operation_descends_to_cohomology"
        ],
        readout_descends_to_cohomology=readout["readout_descends_to_cohomology"],
        wplus_recovery_score=wplus_recovery,
        cohomology_readout_delta=cohomology_delta,
        representative_leakage=representative_leakage,
        counts_as_claim_evidence=False,
        missing_requirements=missing,
        strongest_allowed_reading=strongest,
    )


def summarize_constraint(kind: str) -> dict[str, Any]:
    q = constraint_matrix(kind)
    q2 = matmul(q, q)
    q_nilpotent = is_zero_matrix(q2)
    mirror_q_closed = is_zero_vector(matvec(q, MIRROR))
    mirror_q_exact = in_column_span(MIRROR, q)
    rank_q = matrix_rank(q)
    kernel_dimension = len(BASIS) - rank_q
    image_dimension = rank_q
    cohomology_dimension = kernel_dimension - image_dimension if q_nilpotent else -1

    return {
        "kind": kind,
        "q_matrix": q,
        "q_nilpotent": q_nilpotent,
        "mirror_q_closed": mirror_q_closed,
        "mirror_q_exact": mirror_q_exact,
        "mirror_cohomology_nontrivial": (
            q_nilpotent and mirror_q_closed and not mirror_q_exact
        ),
        "rank_q": rank_q,
        "kernel_dimension": kernel_dimension,
        "image_dimension": image_dimension,
        "cohomology_dimension": cohomology_dimension,
    }


def summarize_operation(kind: str, q_kind: str) -> dict[str, Any]:
    q = constraint_matrix(q_kind)
    operation = operation_matrix(kind)
    commutes = matrices_close(matmul(operation, q), matmul(q, operation))
    exact_preserved = all(
        in_column_span(matvec(operation, column), q) for column in columns(q)
    )
    descends = commutes and exact_preserved
    wplus_recovery = wplus_delta(
        matvec(operation, STATE_A), matvec(operation, STATE_B)
    )

    return {
        "kind": kind,
        "operation_matrix": operation,
        "commutes_with_q": commutes,
        "preserves_exact_subspace": exact_preserved,
        "operation_descends_to_cohomology": descends,
        "wplus_recovery_score": wplus_recovery,
    }


def summarize_readout(kind: str, q_kind: str) -> dict[str, Any]:
    q = constraint_matrix(q_kind)
    readout = readout_vector(kind)
    exact_values = tuple(dot(readout, column) for column in columns(q))
    descends = all(abs(item) < 1e-9 for item in exact_values)
    return {
        "kind": kind,
        "readout_vector": readout,
        "values_on_exact_generators": exact_values,
        "readout_descends_to_cohomology": descends,
    }


def readout_delta(operation_kind: str, readout_kind: str) -> float:
    operation = operation_matrix(operation_kind)
    readout = readout_vector(readout_kind)
    a = matvec(operation, STATE_A)
    b = matvec(operation, STATE_B)
    return abs(dot(readout, a) - dot(readout, b))


def constraint_matrix(kind: str) -> tuple[tuple[float, ...], ...]:
    if kind == "nontrivial_mirror":
        # Q(auxiliary) = physical_exact; mirror is closed and not exact.
        return (
            (0.0, 0.0, 0.0, 1.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
        )
    if kind == "exact_mirror":
        # Q(gauge_seed) = mirror.
        return (
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
        )
    raise ValueError(f"unknown q_kind: {kind}")


def operation_matrix(kind: str) -> tuple[tuple[float, ...], ...]:
    if kind == "identity":
        return identity_matrix(4)
    if kind == "full_krein_boost":
        eta = 0.7
        ch = math.cosh(eta)
        sh = math.sinh(eta)
        return (
            (ch, sh, 0.0, 0.0),
            (sh, ch, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        )
    if kind == "representative_leakage_chain_map":
        # mirror -> mirror + exact physical; physical exact remains exact.
        return (
            (1.0, 1.0, 0.0, 0.0),
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        )
    if kind == "cohomology_scaling":
        return (
            (1.0, 0.0, 0.0, 0.0),
            (0.0, 2.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        )
    raise ValueError(f"unknown operation_kind: {kind}")


def readout_vector(kind: str) -> tuple[float, ...]:
    if kind == "wplus_projector":
        return (1.0, 0.0, 0.0, 0.0)
    if kind == "mirror_cohomology_functional":
        return (0.0, 1.0, 0.0, 0.0)
    raise ValueError(f"unknown readout_kind: {kind}")


def identity_matrix(size: int) -> tuple[tuple[float, ...], ...]:
    return tuple(
        tuple(1.0 if row == col else 0.0 for col in range(size))
        for row in range(size)
    )


def matvec(
    matrix: tuple[tuple[float, ...], ...], vector: tuple[float, ...]
) -> tuple[float, ...]:
    return tuple(
        sum(matrix[row][col] * vector[col] for col in range(len(vector)))
        for row in range(len(matrix))
    )


def matmul(
    left: tuple[tuple[float, ...], ...],
    right: tuple[tuple[float, ...], ...],
) -> tuple[tuple[float, ...], ...]:
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][k] * right[k][col] for k in range(size))
            for col in range(size)
        )
        for row in range(size)
    )


def matrices_close(
    left: tuple[tuple[float, ...], ...],
    right: tuple[tuple[float, ...], ...],
    tolerance: float = 1e-9,
) -> bool:
    return all(
        abs(left[row][col] - right[row][col]) < tolerance
        for row in range(len(left))
        for col in range(len(left[row]))
    )


def columns(matrix: tuple[tuple[float, ...], ...]) -> tuple[tuple[float, ...], ...]:
    return tuple(tuple(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0])))


def dot(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    return sum(a * b for a, b in zip(left, right))


def wplus_delta(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    return abs(left[0] - right[0])


def is_zero_vector(vector: tuple[float, ...], tolerance: float = 1e-9) -> bool:
    return all(abs(item) < tolerance for item in vector)


def is_zero_matrix(
    matrix: tuple[tuple[float, ...], ...], tolerance: float = 1e-9
) -> bool:
    return all(abs(item) < tolerance for row in matrix for item in row)


def in_column_span(
    vector: tuple[float, ...], matrix: tuple[tuple[float, ...], ...]
) -> bool:
    augmented = tuple(tuple(row) + (vector[index],) for index, row in enumerate(matrix))
    return matrix_rank(matrix) == matrix_rank(augmented)


def matrix_rank(
    matrix: tuple[tuple[float, ...], ...], tolerance: float = 1e-9
) -> int:
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    rank = 0
    for col in range(col_count):
        pivot = None
        for row in range(rank, row_count):
            if abs(rows[row][col]) > tolerance:
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [item / pivot_value for item in rows[rank]]
        for row in range(row_count):
            if row == rank:
                continue
            factor = rows[row][col]
            if abs(factor) <= tolerance:
                continue
            rows[row] = [
                item - factor * pivot_item
                for item, pivot_item in zip(rows[row], rows[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def future_packet_minimum() -> tuple[str, ...]:
    return (
        "predeclare Q, the quotient/cohomology object, operation algebra, and readout",
        "prove the recovery operation descends through the BRST quotient",
        "prove the readout annihilates exact representative shifts",
        "include a non-descending full-Krein recovery control",
        "include an exact-representative leakage control",
        "include exact-mirror redundancy and direct cohomology-observable controls",
        "treat direct cohomology readout as review-only until physics-side constraints are supplied",
        "do not treat W+ representative leakage as a hidden physical record",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "real BRST exactness decision",
        "real BRST cohomology nontriviality decision",
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


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {packet_id} | {admitted} | {label} | {op} | {readout} | {wplus:.3e} | {cohom:.3e} | {leakage} | {missing} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            op="yes" if decision["operation_descends_to_cohomology"] else "no",
            readout="yes" if decision["readout_descends_to_cohomology"] else "no",
            wplus=decision["wplus_recovery_score"],
            cohom=decision["cohomology_readout_delta"],
            leakage="yes" if decision["representative_leakage"] else "no",
            missing=", ".join(decision["missing_requirements"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    future = [f"- {item}" for item in payload["future_packet_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T509 - BRST Observable Compatibility Gate - v0.1 results",
            "",
            "> TaF-side finite quotient/readout gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T509-brst-observable-compatibility-gate.md`",
            "- Model: `models/brst_observable_compatibility_gate.py`",
            "- Tests: `tests/test_brst_observable_compatibility_gate.py`",
            f"- Source gate: `{payload['source_gate']}`",
            f"- Artifact JSON: `results/{ARTIFACT}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Operation descends? | Readout descends? | W+ recovery | Cohomology readout delta | Representative leakage? | Missing requirements |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
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
