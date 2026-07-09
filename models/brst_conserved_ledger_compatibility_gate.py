"""T510: BRST conserved-ledger compatibility gate.

T509 made the BRST quotient/readout burden executable: operations must descend
through the quotient and readouts must annihilate exact representative shifts.
This gate adds the next finite record/finality burden named by the unitarity
precondition open problem: a quotient-compatible readout is still only usable
as finality review material if it is conserved by the predeclared dynamics.

The model stays in finite record/ledger language. It does not assert a physical
BRST complex, unitarity theorem, Krein quantization decision, hidden mirror
record, source-action truth, mass-gap evidence, or claim movement.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T510-brst-conserved-ledger-compatibility-gate-v0.1"
VERDICT = "BRST_CONSERVED_LEDGER_GATE_BUILT_STABILITY_REVIEW_ONLY"
SOURCE_GATE = "tests/T509-brst-observable-compatibility-gate.md"
BASIS = ("physical_exact", "mirror", "gauge_seed", "auxiliary")
MIRROR = (0.0, 1.0, 0.0, 0.0)
STATE_A = (0.7, 0.5, 0.0, 0.0)
STATE_B = (0.7, -0.5, 0.0, 0.0)
SAMPLE_STATES = (
    STATE_A,
    STATE_B,
    (0.1, 0.25, 0.0, 0.6),
    (-0.2, -0.4, 0.0, 0.3),
)


@dataclass(frozen=True)
class LedgerPacket:
    packet_id: str
    description: str
    q_kind: str
    dynamics_kind: str
    readout_kind: str
    q_predeclared: bool
    quotient_declared: bool
    dynamics_predeclared: bool
    readout_predeclared: bool
    includes_t509_controls: bool
    includes_nondescending_dynamics_control: bool
    includes_ledger_drift_control: bool
    includes_exact_representative_noise_control: bool
    includes_exact_mirror_control: bool
    requests_claim_or_public_posture: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class LedgerDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    q_nilpotent: bool
    mirror_q_closed: bool
    mirror_q_exact: bool
    mirror_cohomology_nontrivial: bool
    dynamics_descends_to_cohomology: bool
    readout_descends_to_cohomology: bool
    ledger_conserved: bool
    ledger_drift_score: float
    cohomology_readout_delta: float
    exact_representative_noise_score: float
    exact_representative_noise_absorbed: bool
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
            "Make the post-T509 conserved-ledger burden finite and checkable. "
            "A direct cohomology readout can be review material only when the "
            "predeclared dynamics descends through the BRST quotient and "
            "conserves the readout across representative changes and time "
            "steps."
        ),
        "basis": BASIS,
        "states": {
            "state_a": STATE_A,
            "state_b": STATE_B,
            "share_wplus_before_dynamics": wplus_delta(STATE_A, STATE_B) < 1e-12,
            "mirror_delta_before_dynamics": abs(STATE_A[1] - STATE_B[1]),
            "sample_states": SAMPLE_STATES,
        },
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "constraint_summaries": {
            kind: summarize_constraint(kind)
            for kind in ("nontrivial_mirror", "exact_mirror", "non_nilpotent")
        },
        "dynamics_summaries": {
            kind: summarize_dynamics(kind, "nontrivial_mirror")
            for kind in (
                "identity",
                "exact_representative_noise",
                "cohomology_scaling_drift",
                "full_krein_boost",
            )
        },
        "readout_summaries": {
            kind: summarize_readout(kind, "nontrivial_mirror")
            for kind in ("mirror_cohomology_functional", "wplus_projector")
        },
        "overall": {
            "direct_cohomology_ledger_admitted_review_only": by_id[
                "conserved_direct_cohomology_ledger"
            ].admitted,
            "exact_representative_noise_absorbed": by_id[
                "exact_representative_noise_control"
            ].exact_representative_noise_absorbed,
            "cohomology_drift_rejected": by_id[
                "cohomology_scaling_drift_control"
            ].label
            == "REJECTED_NONCONSERVED_COHOMOLOGY_LEDGER",
            "nondescending_dynamics_rejected": by_id[
                "full_krein_dynamics_shortcut"
            ].label
            == "REJECTED_DYNAMICS_NOT_BRST_COMPATIBLE",
            "non_descending_readout_rejected": by_id[
                "wplus_ledger_shortcut"
            ].label
            == "REJECTED_NON_DESCENDING_LEDGER_READOUT",
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
            "unitarity_theorem_claimed": False,
            "physical_inner_product_chosen": False,
            "brst_exactness_decided_for_real_physics": False,
            "hidden_mirror_record_claim_earned": False,
            "physics_claim_earned": False,
        },
        "future_packet_minimum": future_packet_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T510 reprices T509's direct cohomology readout as a conserved "
            "ledger problem. A stable direct cohomology ledger and an "
            "exact-representative-noise control are admitted only as review "
            "targets. A quotient-descending dynamics that scales the mirror "
            "class is rejected because the ledger drifts; a full-Krein boost "
            "is rejected because it does not descend through the quotient; "
            "ordinary W+ ledger language is rejected because the readout is "
            "not exact-invariant."
        ),
    }


def packet_fixtures() -> tuple[LedgerPacket, ...]:
    return (
        LedgerPacket(
            packet_id="conserved_direct_cohomology_ledger",
            description=(
                "A direct exact-invariant mirror-class readout is paired with "
                "identity dynamics, so the quotient ledger is stable."
            ),
            q_kind="nontrivial_mirror",
            dynamics_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=True,
            includes_ledger_drift_control=True,
            includes_exact_representative_noise_control=True,
            includes_exact_mirror_control=True,
        ),
        LedgerPacket(
            packet_id="exact_representative_noise_control",
            description=(
                "The dynamics adds exact representative noise to the W+ "
                "coordinate while preserving the mirror cohomology ledger."
            ),
            q_kind="nontrivial_mirror",
            dynamics_kind="exact_representative_noise",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=True,
            includes_ledger_drift_control=True,
            includes_exact_representative_noise_control=True,
            includes_exact_mirror_control=True,
        ),
        LedgerPacket(
            packet_id="cohomology_scaling_drift_control",
            description=(
                "The dynamics descends to cohomology but scales the mirror "
                "class, so the ledger itself drifts."
            ),
            q_kind="nontrivial_mirror",
            dynamics_kind="cohomology_scaling_drift",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=True,
            includes_ledger_drift_control=True,
            includes_exact_representative_noise_control=True,
            includes_exact_mirror_control=True,
        ),
        LedgerPacket(
            packet_id="full_krein_dynamics_shortcut",
            description=(
                "A full-Krein boost tries to create a visible record but does "
                "not descend through the BRST quotient."
            ),
            q_kind="nontrivial_mirror",
            dynamics_kind="full_krein_boost",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=True,
            includes_ledger_drift_control=True,
            includes_exact_representative_noise_control=True,
            includes_exact_mirror_control=True,
        ),
        LedgerPacket(
            packet_id="wplus_ledger_shortcut",
            description=(
                "A W+-only ledger is conserved under identity dynamics but is "
                "not exact-invariant."
            ),
            q_kind="nontrivial_mirror",
            dynamics_kind="identity",
            readout_kind="wplus_projector",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=True,
            includes_ledger_drift_control=True,
            includes_exact_representative_noise_control=True,
            includes_exact_mirror_control=True,
        ),
        LedgerPacket(
            packet_id="exact_mirror_redundancy_control",
            description=(
                "Exact-control packet: the mirror is in im(Q), so no "
                "nontrivial conserved mirror ledger exists."
            ),
            q_kind="exact_mirror",
            dynamics_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=True,
            includes_ledger_drift_control=True,
            includes_exact_representative_noise_control=True,
            includes_exact_mirror_control=True,
        ),
        LedgerPacket(
            packet_id="non_nilpotent_constraint_control",
            description="The constraint operator is not nilpotent.",
            q_kind="non_nilpotent",
            dynamics_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=True,
            includes_ledger_drift_control=True,
            includes_exact_representative_noise_control=True,
            includes_exact_mirror_control=True,
        ),
        LedgerPacket(
            packet_id="missing_controls_shortcut",
            description="The packet omits the new T510 controls.",
            q_kind="nontrivial_mirror",
            dynamics_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=False,
            includes_ledger_drift_control=False,
            includes_exact_representative_noise_control=False,
            includes_exact_mirror_control=True,
        ),
        LedgerPacket(
            packet_id="claim_cross_repo_shortcut",
            description="The packet tries to move claim or cross-repo truth.",
            q_kind="nontrivial_mirror",
            dynamics_kind="identity",
            readout_kind="mirror_cohomology_functional",
            q_predeclared=True,
            quotient_declared=True,
            dynamics_predeclared=True,
            readout_predeclared=True,
            includes_t509_controls=True,
            includes_nondescending_dynamics_control=True,
            includes_ledger_drift_control=True,
            includes_exact_representative_noise_control=True,
            includes_exact_mirror_control=True,
            requests_claim_or_public_posture=True,
            requests_external_publication=True,
            requests_cross_repo_truth=True,
        ),
    )


def evaluate_packet(packet: LedgerPacket) -> LedgerDecision:
    if packet.requests_claim_or_public_posture:
        return make_decision(
            packet,
            admitted=False,
            label="BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            action="stop",
            missing=(),
            strongest=(
                "Conserved-ledger compatibility cannot move claims, public "
                "posture, external publication, or cross-repo truth."
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
            strongest="No BRST quotient ledger exists without Q^2 = 0.",
        )
    if not constraint["mirror_q_closed"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_MIRROR_NOT_Q_CLOSED",
            action="reject",
            missing=missing + ("mirror vector in ker(Q)",),
            strongest="The mirror must be closed before it can carry a ledger class.",
        )
    if constraint["mirror_q_exact"]:
        return make_decision(
            packet,
            admitted=False,
            label="BRST_EXACT_REDUNDANCY_RECORDED",
            action="record_negative",
            missing=missing,
            strongest=(
                "The mirror is exact in this packet, so a conserved "
                "cohomology ledger erases it rather than supporting a "
                "hidden-record reading."
            ),
        )
    if missing:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_INCOMPLETE_LEDGER_PACKET",
            action="reject",
            missing=missing,
            strongest="The packet has not paid the conserved-ledger controls.",
        )

    dynamics = summarize_dynamics(packet.dynamics_kind, packet.q_kind)
    readout = summarize_readout(packet.readout_kind, packet.q_kind)
    ledger_drift = ledger_drift_score(packet.dynamics_kind, packet.readout_kind)
    cohomology_delta = readout_delta("identity", packet.readout_kind)

    if not dynamics["dynamics_descends_to_cohomology"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_DYNAMICS_NOT_BRST_COMPATIBLE",
            action="reject",
            missing=(),
            strongest=(
                "The dynamics creates apparent ledger structure only by "
                "failing to descend through the BRST quotient."
            ),
        )
    if not readout["readout_descends_to_cohomology"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_NON_DESCENDING_LEDGER_READOUT",
            action="reject",
            missing=("exact-invariant ledger readout",),
            strongest=(
                "The proposed ledger changes under exact representative "
                "shifts and therefore is not a quotient ledger."
            ),
        )
    if ledger_drift > 1e-9:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_NONCONSERVED_COHOMOLOGY_LEDGER",
            action="reject",
            missing=("dynamics-conserved quotient ledger",),
            strongest=(
                "The dynamics descends through the quotient, but the "
                "cohomology readout itself drifts, so it cannot serve as a "
                "stable record/finality ledger."
            ),
        )
    if cohomology_delta > 1e-9:
        return make_decision(
            packet,
            admitted=True,
            label="ADMITTED_CONSERVED_COHOMOLOGY_LEDGER_REVIEW_TARGET",
            action="review_only",
            missing=(),
            strongest=(
                "A direct exact-invariant cohomology readout is conserved by "
                "the predeclared dynamics. This is review material only, not "
                "hidden-record, unitarity, or physics evidence."
            ),
        )

    return make_decision(
        packet,
        admitted=False,
        label="REJECTED_NO_COHOMOLOGY_LEDGER_SPREAD",
        action="reject",
        missing=(),
        strongest="No conserved quotient-compatible readout separates the tested pair.",
    )


def missing_requirements(packet: LedgerPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.q_predeclared:
        missing.append("predeclared nilpotent constraint operator Q")
    if not packet.quotient_declared:
        missing.append("declared BRST quotient/cohomology object")
    if not packet.dynamics_predeclared:
        missing.append("predeclared dynamics")
    if not packet.readout_predeclared:
        missing.append("predeclared exact-invariant readout")
    if not packet.includes_t509_controls:
        missing.append("T509 quotient/readout controls")
    if not packet.includes_nondescending_dynamics_control:
        missing.append("non-descending dynamics control")
    if not packet.includes_ledger_drift_control:
        missing.append("ledger drift control")
    if not packet.includes_exact_representative_noise_control:
        missing.append("exact-representative noise control")
    if not packet.includes_exact_mirror_control:
        missing.append("exact-mirror redundancy control")
    return tuple(missing)


def make_decision(
    packet: LedgerPacket,
    admitted: bool,
    label: str,
    action: str,
    missing: tuple[str, ...],
    strongest: str,
) -> LedgerDecision:
    constraint = summarize_constraint(packet.q_kind)
    dynamics = summarize_dynamics(packet.dynamics_kind, packet.q_kind)
    readout = summarize_readout(packet.readout_kind, packet.q_kind)
    ledger_drift = ledger_drift_score(packet.dynamics_kind, packet.readout_kind)
    exact_noise = exact_representative_noise_score(packet.dynamics_kind)

    return LedgerDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        review_target_only=admitted,
        q_nilpotent=constraint["q_nilpotent"],
        mirror_q_closed=constraint["mirror_q_closed"],
        mirror_q_exact=constraint["mirror_q_exact"],
        mirror_cohomology_nontrivial=constraint["mirror_cohomology_nontrivial"],
        dynamics_descends_to_cohomology=dynamics[
            "dynamics_descends_to_cohomology"
        ],
        readout_descends_to_cohomology=readout["readout_descends_to_cohomology"],
        ledger_conserved=ledger_drift < 1e-9,
        ledger_drift_score=ledger_drift,
        cohomology_readout_delta=readout_delta("identity", packet.readout_kind),
        exact_representative_noise_score=exact_noise,
        exact_representative_noise_absorbed=(
            admitted and exact_noise > 1e-9 and ledger_drift < 1e-9
        ),
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


def summarize_dynamics(kind: str, q_kind: str) -> dict[str, Any]:
    q = constraint_matrix(q_kind)
    dynamics = dynamics_matrix(kind)
    commutes = matrices_close(matmul(dynamics, q), matmul(q, dynamics))
    exact_preserved = all(
        in_column_span(matvec(dynamics, column), q) for column in columns(q)
    )
    descends = commutes and exact_preserved
    return {
        "kind": kind,
        "dynamics_matrix": dynamics,
        "commutes_with_q": commutes,
        "preserves_exact_subspace": exact_preserved,
        "dynamics_descends_to_cohomology": descends,
        "exact_representative_noise_score": exact_representative_noise_score(kind),
        "mirror_ledger_drift_score": ledger_drift_score(
            kind, "mirror_cohomology_functional"
        ),
        "wplus_ledger_drift_score": ledger_drift_score(kind, "wplus_projector"),
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


def ledger_drift_score(dynamics_kind: str, readout_kind: str) -> float:
    dynamics = dynamics_matrix(dynamics_kind)
    readout = readout_vector(readout_kind)
    return max(
        abs(dot(readout, matvec(dynamics, state)) - dot(readout, state))
        for state in SAMPLE_STATES
    )


def exact_representative_noise_score(dynamics_kind: str) -> float:
    dynamics = dynamics_matrix(dynamics_kind)
    return max(abs(matvec(dynamics, state)[0] - state[0]) for state in SAMPLE_STATES)


def readout_delta(dynamics_kind: str, readout_kind: str) -> float:
    dynamics = dynamics_matrix(dynamics_kind)
    readout = readout_vector(readout_kind)
    a = matvec(dynamics, STATE_A)
    b = matvec(dynamics, STATE_B)
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
    if kind == "non_nilpotent":
        # Q(auxiliary) = physical_exact and Q(physical_exact) = mirror.
        return (
            (0.0, 0.0, 0.0, 1.0),
            (1.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
        )
    raise ValueError(f"unknown q_kind: {kind}")


def dynamics_matrix(kind: str) -> tuple[tuple[float, ...], ...]:
    if kind == "identity":
        return identity_matrix(4)
    if kind == "exact_representative_noise":
        # mirror -> mirror + exact physical; direct cohomology readout is stable.
        return (
            (1.0, 1.0, 0.0, 0.0),
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        )
    if kind == "cohomology_scaling_drift":
        return (
            (1.0, 0.0, 0.0, 0.0),
            (0.0, 2.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        )
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
    raise ValueError(f"unknown dynamics_kind: {kind}")


def readout_vector(kind: str) -> tuple[float, ...]:
    if kind == "mirror_cohomology_functional":
        return (0.0, 1.0, 0.0, 0.0)
    if kind == "wplus_projector":
        return (1.0, 0.0, 0.0, 0.0)
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
    return tuple(
        tuple(matrix[row][col] for row in range(len(matrix)))
        for col in range(len(matrix[0]))
    )


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
        "predeclare Q, the quotient/cohomology object, dynamics, and readout",
        "prove the dynamics descends through the BRST quotient",
        "prove the readout annihilates exact representative shifts",
        "prove the quotient readout is conserved by the declared dynamics",
        "include non-descending dynamics and ledger-drift controls",
        "include exact-representative noise and exact-mirror redundancy controls",
        "treat conserved cohomology readout as review-only until physics-side constraints are supplied",
        "do not treat W+ representative leakage or drifting cohomology as a hidden physical record",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "unitarity theorem",
        "physical inner product selection",
        "real BRST exactness decision",
        "real BRST cohomology nontriviality decision",
        "Krein-retention quantization accepted as physical",
        "full-Krein collective operations accepted as physically admissible",
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
        "| {packet_id} | {admitted} | {label} | {dyn} | {readout} | {conserved} | {drift:.3e} | {cohom:.3e} | {noise:.3e} | {missing} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            dyn="yes" if decision["dynamics_descends_to_cohomology"] else "no",
            readout="yes" if decision["readout_descends_to_cohomology"] else "no",
            conserved="yes" if decision["ledger_conserved"] else "no",
            drift=decision["ledger_drift_score"],
            cohom=decision["cohomology_readout_delta"],
            noise=decision["exact_representative_noise_score"],
            missing=", ".join(decision["missing_requirements"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    future = [f"- {item}" for item in payload["future_packet_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T510 - BRST Conserved Ledger Compatibility Gate - v0.1 results",
            "",
            "> TaF-side finite record/ledger gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T510-brst-conserved-ledger-compatibility-gate.md`",
            "- Model: `models/brst_conserved_ledger_compatibility_gate.py`",
            "- Tests: `tests/test_brst_conserved_ledger_compatibility_gate.py`",
            f"- Source gate: `{payload['source_gate']}`",
            f"- Artifact JSON: `results/{ARTIFACT}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Dynamics descends? | Readout descends? | Ledger conserved? | Ledger drift | Cohomology readout delta | Exact representative noise | Missing requirements |",
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
