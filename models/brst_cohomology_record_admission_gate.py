"""T508: BRST cohomology record-admission gate.

T507 reduced the mirror-sector record reading to two finite gates:
admissible operation algebra and observer normalization. Its named future
burden was a third gate: BRST/exactness language must be typed by an actual
constraint or gauge structure before it can upgrade the record reading.

This module builds that admission gate without deciding any physics. It uses a
finite synthetic chain-complex fixture to check the packet shape:

* a nilpotent constraint operator Q is required;
* the mirror vector must be Q-closed before any cohomology reading is allowed;
* an exact mirror routes to redundancy;
* a nontrivial mirror cohomology class is admitted only as review material, and
  only when the T507 full-Krein plus self-normalized controls are also present.

No claim ledger, public posture, BRST exactness decision, Krein quantization
decision, source-action truth, or cross-repo truth is moved by this gate.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T508-brst-cohomology-record-admission-gate-v0.1"
VERDICT = "BRST_COHOMOLOGY_RECORD_GATE_BUILT_REVIEW_ONLY"
SOURCE_GATE = "tests/T507-finality-record-redundancy-double-gate.md"
BASIS = ("physical", "mirror", "gauge_seed", "auxiliary")
MIRROR = (0.0, 1.0, 0.0, 0.0)


@dataclass(frozen=True)
class ConstraintPacket:
    packet_id: str
    description: str
    q_kind: str
    operation_algebra: str
    normalization_rule: str
    q_predeclared: bool
    quotient_or_cohomology_declared: bool
    q_closed_observables_declared: bool
    includes_exact_control: bool
    includes_nontrivial_control: bool
    includes_t507_operation_controls: bool
    includes_t507_normalization_controls: bool
    brst_asserted_without_constraint_structure: bool = False
    requests_claim_or_public_posture: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class ConstraintDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    q_nilpotent: bool
    mirror_q_closed: bool
    mirror_q_exact: bool
    mirror_cohomology_nontrivial: bool
    t507_double_gate_paid: bool
    counts_as_claim_evidence: bool
    cohomology_dimension: int
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
            "Make T507's BRST/exactness burden executable as a finite "
            "admission gate. BRST language must supply a predeclared "
            "nilpotent constraint structure, cohomology quotient, observable "
            "discipline, exact/nontrivial controls, and the T507 operation/"
            "normalization controls before any hidden-record review target is "
            "admitted."
        ),
        "basis": BASIS,
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "constraint_summaries": {
            kind: summarize_constraint(kind)
            for kind in (
                "exact_mirror",
                "nontrivial_mirror",
                "non_nilpotent",
                "mirror_not_closed",
            )
        },
        "overall": {
            "exact_mirror_routes_to_redundancy": by_id[
                "exact_mirror_default"
            ].label
            == "BRST_EXACT_REDUNDANCY_RECORDED",
            "nontrivial_mirror_requires_t507_double_gate": True,
            "nontrivial_double_gate_admitted_review_only": by_id[
                "nontrivial_mirror_full_krein_selfnorm"
            ].admitted,
            "full_born_nontrivial_rejected_as_hidden_record": by_id[
                "nontrivial_mirror_full_born"
            ].label
            == "REJECTED_NONTRIVIAL_BUT_FULL_BORN_VISIBLE",
            "untyped_brst_rejected": by_id["untyped_brst_shortcut"].label
            == "REJECTED_UNTYPED_BRST_ASSERTION",
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
            "T508 makes the post-T507 BRST burden explicit. In the finite "
            "fixture, a Q-exact mirror vector routes to redundancy; a "
            "Q-closed but non-exact mirror vector can be admitted only as a "
            "review target when the packet also pays T507's full-Krein "
            "operation and self-normalized hiddenness gates. Non-nilpotent, "
            "not-closed, post-hoc, missing-control, full-Born, claim/public, "
            "external-publication, and cross-repo shortcuts are rejected or "
            "blocked. This builds an intake gate; it does not decide the real "
            "physics."
        ),
    }


def packet_fixtures() -> tuple[ConstraintPacket, ...]:
    return (
        ConstraintPacket(
            packet_id="exact_mirror_default",
            description=(
                "Synthetic exact-control packet: Q maps a gauge seed onto the "
                "mirror vector, so the mirror is closed and exact."
            ),
            q_kind="exact_mirror",
            operation_algebra="positivity_preserving",
            normalization_rule="full_born",
            q_predeclared=True,
            quotient_or_cohomology_declared=True,
            q_closed_observables_declared=True,
            includes_exact_control=True,
            includes_nontrivial_control=True,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
        ),
        ConstraintPacket(
            packet_id="nontrivial_mirror_full_krein_selfnorm",
            description=(
                "Synthetic review packet: the mirror is Q-closed and not "
                "Q-exact, with T507's full-Krein recovery and self-normalized "
                "hiddenness controls paid."
            ),
            q_kind="nontrivial_mirror",
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            q_predeclared=True,
            quotient_or_cohomology_declared=True,
            q_closed_observables_declared=True,
            includes_exact_control=True,
            includes_nontrivial_control=True,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
        ),
        ConstraintPacket(
            packet_id="nontrivial_mirror_full_born",
            description=(
                "The cohomology class is nontrivial, but the packet keeps "
                "full-space Born normalization, so T507's hiddenness gate is "
                "not paid."
            ),
            q_kind="nontrivial_mirror",
            operation_algebra="full_krein_collective",
            normalization_rule="full_born",
            q_predeclared=True,
            quotient_or_cohomology_declared=True,
            q_closed_observables_declared=True,
            includes_exact_control=True,
            includes_nontrivial_control=True,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
        ),
        ConstraintPacket(
            packet_id="nontrivial_mirror_no_recovery",
            description=(
                "The cohomology class is nontrivial, but the admissible "
                "operation algebra is still positivity-preserving."
            ),
            q_kind="nontrivial_mirror",
            operation_algebra="positivity_preserving",
            normalization_rule="self_normalized",
            q_predeclared=True,
            quotient_or_cohomology_declared=True,
            q_closed_observables_declared=True,
            includes_exact_control=True,
            includes_nontrivial_control=True,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
        ),
        ConstraintPacket(
            packet_id="non_nilpotent_control",
            description="Invalid packet: the declared Q is not nilpotent.",
            q_kind="non_nilpotent",
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            q_predeclared=True,
            quotient_or_cohomology_declared=True,
            q_closed_observables_declared=True,
            includes_exact_control=True,
            includes_nontrivial_control=True,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
        ),
        ConstraintPacket(
            packet_id="mirror_not_closed_control",
            description="Invalid packet: the mirror is not Q-closed.",
            q_kind="mirror_not_closed",
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            q_predeclared=True,
            quotient_or_cohomology_declared=True,
            q_closed_observables_declared=True,
            includes_exact_control=True,
            includes_nontrivial_control=True,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
        ),
        ConstraintPacket(
            packet_id="post_hoc_q_shortcut",
            description="The constraint operator is selected after the split.",
            q_kind="nontrivial_mirror",
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            q_predeclared=False,
            quotient_or_cohomology_declared=True,
            q_closed_observables_declared=True,
            includes_exact_control=True,
            includes_nontrivial_control=True,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
        ),
        ConstraintPacket(
            packet_id="missing_controls_shortcut",
            description="The packet declares a Q but omits control burdens.",
            q_kind="nontrivial_mirror",
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            q_predeclared=True,
            quotient_or_cohomology_declared=False,
            q_closed_observables_declared=False,
            includes_exact_control=False,
            includes_nontrivial_control=False,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
        ),
        ConstraintPacket(
            packet_id="untyped_brst_shortcut",
            description="The packet asserts BRST status without a Q structure.",
            q_kind="not_supplied",
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            q_predeclared=False,
            quotient_or_cohomology_declared=False,
            q_closed_observables_declared=False,
            includes_exact_control=False,
            includes_nontrivial_control=False,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
            brst_asserted_without_constraint_structure=True,
        ),
        ConstraintPacket(
            packet_id="claim_cross_repo_shortcut",
            description="The packet tries to move claims or cross-repo truth.",
            q_kind="nontrivial_mirror",
            operation_algebra="full_krein_collective",
            normalization_rule="self_normalized",
            q_predeclared=True,
            quotient_or_cohomology_declared=True,
            q_closed_observables_declared=True,
            includes_exact_control=True,
            includes_nontrivial_control=True,
            includes_t507_operation_controls=True,
            includes_t507_normalization_controls=True,
            requests_claim_or_public_posture=True,
            requests_external_publication=True,
            requests_cross_repo_truth=True,
        ),
    )


def evaluate_packet(packet: ConstraintPacket) -> ConstraintDecision:
    if packet.requests_claim_or_public_posture:
        return make_decision(
            packet,
            admitted=False,
            label="BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            action="stop",
            missing=(),
            strongest=(
                "A constraint packet cannot move claim status, public posture, "
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
            strongest=(
                "Non-GitHub external action and cross-repo truth movement are "
                "outside this repo-local admission gate."
            ),
        )

    if packet.brst_asserted_without_constraint_structure or packet.q_kind == "not_supplied":
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_UNTYPED_BRST_ASSERTION",
            action="reject",
            missing=("predeclared nilpotent constraint operator Q",),
            strongest=(
                "BRST/exactness language is only a placeholder until a typed "
                "constraint or gauge structure is supplied."
            ),
        )

    summary = summarize_constraint(packet.q_kind)
    missing = missing_requirements(packet, summary)

    if not summary["q_nilpotent"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_NON_NILPOTENT_CONSTRAINT",
            action="reject",
            missing=missing,
            strongest="A BRST-style packet needs Q^2 = 0 before cohomology exists.",
        )
    if not summary["mirror_q_closed"]:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_MIRROR_NOT_Q_CLOSED",
            action="reject",
            missing=missing,
            strongest=(
                "A mirror vector outside ker(Q) cannot define a cohomology "
                "class or exactness question."
            ),
        )
    if missing:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_INCOMPLETE_CONSTRAINT_PACKET",
            action="reject",
            missing=missing,
            strongest="The packet is structurally typed but has not paid its controls.",
        )
    if summary["mirror_q_exact"]:
        return make_decision(
            packet,
            admitted=False,
            label="BRST_EXACT_REDUNDANCY_RECORDED",
            action="record_negative",
            missing=(),
            strongest=(
                "In this finite fixture, an exact mirror vector routes to "
                "redundancy rather than hidden-record support."
            ),
        )

    t507_paid = t507_double_gate_paid(packet)
    if packet.operation_algebra != "full_krein_collective":
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_NONTRIVIAL_BUT_NO_RECORD_RECOVERY",
            action="demote_to_nonrecoverable_class",
            missing=(),
            strongest=(
                "A nontrivial cohomology class is not a record reading unless "
                "the declared operation algebra can recover the mirror split."
            ),
        )
    if packet.normalization_rule != "self_normalized":
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_NONTRIVIAL_BUT_FULL_BORN_VISIBLE",
            action="demote_to_visible_physical_dof",
            missing=(),
            strongest=(
                "A nontrivial mirror class under full-space Born normalization "
                "is visible by T507's leakage control, not hidden record support."
            ),
        )
    if not t507_paid:
        return make_decision(
            packet,
            admitted=False,
            label="REJECTED_T507_CONTROLS_NOT_PAID",
            action="reject",
            missing=("T507 operation and normalization controls",),
            strongest=(
                "The BRST/cohomology gate does not replace T507's operation "
                "and normalization gates."
            ),
        )

    return make_decision(
        packet,
        admitted=True,
        label="ADMITTED_NONTRIVIAL_COHOMOLOGY_REVIEW_TARGET",
        action="review_only",
        missing=(),
        strongest=(
            "A predeclared nilpotent Q with mirror in ker(Q) but not im(Q), "
            "plus the T507 double gate, is admitted only as a hidden-record "
            "review target."
        ),
    )


def missing_requirements(
    packet: ConstraintPacket, summary: dict[str, Any]
) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.q_predeclared:
        missing.append("predeclared constraint operator Q")
    if not packet.quotient_or_cohomology_declared:
        missing.append("declared quotient/cohomology object")
    if not packet.q_closed_observables_declared:
        missing.append("Q-closed observable discipline")
    if not packet.includes_exact_control:
        missing.append("exact-mirror redundancy control")
    if not packet.includes_nontrivial_control:
        missing.append("nontrivial-mirror review control")
    if not packet.includes_t507_operation_controls:
        missing.append("T507 operation-algebra controls")
    if not packet.includes_t507_normalization_controls:
        missing.append("T507 normalization controls")
    if not summary["q_nilpotent"]:
        missing.append("nilpotency Q^2 = 0")
    if not summary["mirror_q_closed"]:
        missing.append("mirror vector in ker(Q)")
    return tuple(missing)


def t507_double_gate_paid(packet: ConstraintPacket) -> bool:
    return (
        packet.operation_algebra == "full_krein_collective"
        and packet.normalization_rule == "self_normalized"
        and packet.includes_t507_operation_controls
        and packet.includes_t507_normalization_controls
    )


def make_decision(
    packet: ConstraintPacket,
    admitted: bool,
    label: str,
    action: str,
    missing: tuple[str, ...],
    strongest: str,
) -> ConstraintDecision:
    summary = summarize_constraint(packet.q_kind)
    return ConstraintDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        review_target_only=admitted,
        q_nilpotent=summary["q_nilpotent"],
        mirror_q_closed=summary["mirror_q_closed"],
        mirror_q_exact=summary["mirror_q_exact"],
        mirror_cohomology_nontrivial=summary["mirror_cohomology_nontrivial"],
        t507_double_gate_paid=t507_double_gate_paid(packet),
        counts_as_claim_evidence=False,
        cohomology_dimension=summary["cohomology_dimension"],
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
    rank_q2 = matrix_rank(q2)
    kernel_dimension = len(BASIS) - rank_q
    image_dimension = rank_q
    if q_nilpotent:
        cohomology_dimension = kernel_dimension - image_dimension
    else:
        cohomology_dimension = -1

    return {
        "kind": kind,
        "q_matrix": q,
        "q_squared_zero": q_nilpotent,
        "q_nilpotent": q_nilpotent,
        "mirror_q_closed": mirror_q_closed,
        "mirror_q_exact": mirror_q_exact,
        "mirror_cohomology_nontrivial": (
            q_nilpotent and mirror_q_closed and not mirror_q_exact
        ),
        "rank_q": rank_q,
        "rank_q_squared": rank_q2,
        "kernel_dimension": kernel_dimension,
        "image_dimension": image_dimension,
        "cohomology_dimension": cohomology_dimension,
    }


def constraint_matrix(kind: str) -> tuple[tuple[float, ...], ...]:
    zero = (
        (0.0, 0.0, 0.0, 0.0),
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
    if kind == "nontrivial_mirror":
        # Q(auxiliary) = physical; mirror is closed but not exact.
        return (
            (0.0, 0.0, 0.0, 1.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
        )
    if kind == "non_nilpotent":
        # Q(gauge_seed) = mirror and Q(mirror) = physical, so Q^2 != 0.
        return (
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
        )
    if kind == "mirror_not_closed":
        # Q(mirror) = physical.
        return (
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
        )
    return zero


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


def is_zero_vector(vector: tuple[float, ...], tolerance: float = 1e-9) -> bool:
    return all(abs(item) < tolerance for item in vector)


def is_zero_matrix(
    matrix: tuple[tuple[float, ...], ...], tolerance: float = 1e-9
) -> bool:
    return all(abs(item) < tolerance for row in matrix for item in row)


def in_column_span(
    vector: tuple[float, ...], matrix: tuple[tuple[float, ...], ...]
) -> bool:
    columns = tuple(zip(*matrix))
    augmented = tuple(tuple(row) + (vector[index],) for index, row in enumerate(matrix))
    return matrix_rank(tuple(tuple(col) for col in columns)) == matrix_rank(augmented)


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
        "predeclare the constraint or gauge operator Q before selecting the mirror pair",
        "prove Q is nilpotent with Q^2 = 0",
        "prove the mirror vector is Q-closed",
        "decide exactness by membership in im(Q), not by assertion",
        "declare the cohomology quotient or physical-state quotient",
        "declare the Q-closed observable discipline",
        "include exact-mirror redundancy and nontrivial-mirror review controls",
        "pay T507's operation-algebra recovery controls",
        "pay T507's full-Born leakage and self-normalized hiddenness controls",
        "keep any nontrivial class review-only until physics-side constraints are supplied",
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
        "| {packet_id} | {admitted} | {label} | {nilpotent} | {closed} | {exact} | {nontrivial} | {t507} | {cohom_dim} | {missing} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            nilpotent="yes" if decision["q_nilpotent"] else "no",
            closed="yes" if decision["mirror_q_closed"] else "no",
            exact="yes" if decision["mirror_q_exact"] else "no",
            nontrivial="yes" if decision["mirror_cohomology_nontrivial"] else "no",
            t507="yes" if decision["t507_double_gate_paid"] else "no",
            cohom_dim=decision["cohomology_dimension"],
            missing=", ".join(decision["missing_requirements"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    future = [f"- {item}" for item in payload["future_packet_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T508 - BRST Cohomology Record-Admission Gate - v0.1 results",
            "",
            "> TaF-side finite admission gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T508-brst-cohomology-record-admission-gate.md`",
            "- Model: `models/brst_cohomology_record_admission_gate.py`",
            "- Tests: `tests/test_brst_cohomology_record_admission_gate.py`",
            f"- Source gate: `{payload['source_gate']}`",
            f"- Artifact JSON: `results/{ARTIFACT}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Q^2=0? | Mirror closed? | Mirror exact? | Mirror nontrivial? | T507 double gate paid? | H dim | Missing requirements |",
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
