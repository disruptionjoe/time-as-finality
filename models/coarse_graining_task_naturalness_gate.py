"""T469: task-naturalness gate for valid coarse-graining packets.

T467 made bounded-observer certification executable, and T468 showed that the
fixture still needed independent positive controls and a real task-naturalness
audit. This module turns that follow-up burden into a finite admission gate.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from models.valid_coarse_graining_admissibility_gate import (
    CertificationBudget,
    CoarseGrainingCandidate,
    evaluate_candidate as evaluate_base_candidate,
    finite_record_states,
)


State = tuple[int, ...]
Labeler = Callable[[State], str]
Partition = tuple[tuple[str, ...], ...]

ARTIFACT_ID = "T469-coarse-graining-task-naturalness-gate-v0.1"
VERDICT = "TASK_NATURALNESS_GATE_BUILT_FIXTURE_REPAIRED_NO_PROMOTION"


@dataclass(frozen=True)
class TaskNaturalnessEvidence:
    """Predeclared semantic burden for a finality-native coarse-graining task."""

    task_family: str
    certified_record_object: str
    declared_before_relation: bool
    preserves_record_value_or_support: bool
    semantics_not_label_restatement: bool
    demotion_condition_declared: bool
    observer_creates_truth_overread: bool = False


@dataclass(frozen=True)
class NaturalnessCandidate:
    """A coarse-graining candidate plus its task-naturalness evidence."""

    base: CoarseGrainingCandidate
    evidence: TaskNaturalnessEvidence
    role: str


@dataclass(frozen=True)
class NaturalnessEvaluation:
    """T469 decision for one candidate."""

    candidate_id: str
    admitted: bool
    decision: str
    route_label: str
    blockers: tuple[str, ...]
    base_route_label: str
    base_admitted: bool
    class_count: int
    role: str


@dataclass(frozen=True)
class PacketEvaluation:
    """Packet-level check for positive-control independence and hostile controls."""

    packet_id: str
    admitted: bool
    decision: str
    route_label: str
    blockers: tuple[str, ...]
    positive_control_ids: tuple[str, ...]
    positive_controls_independent: bool
    hostile_control_ids: tuple[str, ...]
    hostile_controls_blocked: bool


def default_budget() -> CertificationBudget:
    """Return the repaired three-holder finite observer budget."""

    return CertificationBudget(
        accessible_fields=(0, 1, 2),
        max_fields_read=3,
        max_predicate_cost=4,
        min_holder_redundancy=2,
        max_reversal_cost=2,
    )


def evaluate_naturalness_candidate(
    candidate: NaturalnessCandidate,
    budget: CertificationBudget,
    states: tuple[State, ...],
) -> NaturalnessEvaluation:
    """Evaluate one candidate under the T469 task-naturalness gate."""

    base_eval = evaluate_base_candidate(candidate.base, budget, states)
    blockers: list[str] = []
    evidence = candidate.evidence

    if not base_eval.admitted:
        blockers.append(f"base_gate:{base_eval.route_label}")
    if not evidence.declared_before_relation:
        blockers.append("task_not_predeclared")
    if not evidence.certified_record_object:
        blockers.append("certified_record_object_not_named")
    if not evidence.preserves_record_value_or_support:
        blockers.append("record_value_or_support_not_preserved")
    if not evidence.semantics_not_label_restatement:
        blockers.append("task_semantics_restates_label")
    if not evidence.demotion_condition_declared:
        blockers.append("demotion_condition_missing")
    if evidence.observer_creates_truth_overread:
        blockers.append("observer_creates_truth_overread")

    if "observer_creates_truth_overread" in blockers:
        decision = "blocked"
        route = "FORBIDDEN_POSTURE_OR_CREATION_OVERREAD"
    elif not base_eval.admitted:
        decision = "not_admitted"
        route = "BASE_CERTIFICATION_GATE_NOT_MET"
    elif blockers:
        decision = "not_admitted"
        route = "TASK_NATURALNESS_NOT_MET"
    else:
        decision = "admitted_for_review"
        route = "TASK_NATURALNESS_PACKET_CLEARED"

    return NaturalnessEvaluation(
        candidate_id=candidate.base.candidate_id,
        admitted=decision == "admitted_for_review",
        decision=decision,
        route_label=route,
        blockers=tuple(blockers),
        base_route_label=base_eval.route_label,
        base_admitted=base_eval.admitted,
        class_count=base_eval.class_count,
        role=candidate.role,
    )


def evaluate_packet(
    packet_id: str,
    candidate_ids: tuple[str, ...],
    positive_control_ids: tuple[str, ...],
    hostile_control_ids: tuple[str, ...],
    candidates: dict[str, NaturalnessCandidate],
    evaluations: dict[str, NaturalnessEvaluation],
    states: tuple[State, ...],
) -> PacketEvaluation:
    """Evaluate a finite packet, not just its individual candidates."""

    blockers: list[str] = []
    missing_ids = tuple(
        candidate_id
        for candidate_id in candidate_ids
        if candidate_id not in candidates
    )
    if missing_ids:
        blockers.append("candidate_id_missing")

    positive_controls_independent = _positive_controls_independent(
        positive_control_ids,
        candidates,
        states,
    )
    if not positive_controls_independent:
        blockers.append("positive_controls_not_independent")

    not_admitted_positive = tuple(
        candidate_id
        for candidate_id in positive_control_ids
        if candidate_id in evaluations and not evaluations[candidate_id].admitted
    )
    if not_admitted_positive:
        blockers.append("positive_control_not_admitted")

    hostile_controls_blocked = all(
        candidate_id in evaluations and not evaluations[candidate_id].admitted
        for candidate_id in hostile_control_ids
    )
    if not hostile_controls_blocked:
        blockers.append("hostile_control_admitted")

    if blockers:
        decision = "not_admitted"
        if "positive_controls_not_independent" in blockers:
            route = "POSITIVE_CONTROL_INDEPENDENCE_NOT_MET"
        elif "hostile_control_admitted" in blockers:
            route = "HOSTILE_CONTROL_NOT_BLOCKED"
        else:
            route = "PACKET_BURDEN_NOT_MET"
    else:
        decision = "admitted_for_review"
        route = "REPAIRED_TASK_NATURALNESS_PACKET_ADMITTED"

    return PacketEvaluation(
        packet_id=packet_id,
        admitted=decision == "admitted_for_review",
        decision=decision,
        route_label=route,
        blockers=tuple(blockers),
        positive_control_ids=positive_control_ids,
        positive_controls_independent=positive_controls_independent,
        hostile_control_ids=hostile_control_ids,
        hostile_controls_blocked=hostile_controls_blocked,
    )


def example_candidates() -> tuple[NaturalnessCandidate, ...]:
    """Return the finite candidate catalogue for T469."""

    return (
        _candidate(
            candidate_id="three_holder_finality_band",
            description=(
                "Three accessible holders certify stable-zero, stable-one, or "
                "unsettled finality status."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, width=3),
            evidence=TaskNaturalnessEvidence(
                task_family="finality_status_band",
                certified_record_object="three_holder_finalized_value_status",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="positive_control",
        ),
        _candidate(
            candidate_id="three_holder_support_count",
            description=(
                "Three accessible holders certify the local finalized-support "
                "multiplicity."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=2,
            finality_native_task=True,
            labeler=lambda state: f"support_count_{sum(state[:3])}",
            evidence=TaskNaturalnessEvidence(
                task_family="support_multiplicity",
                certified_record_object="three_holder_support_count_certificate",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="positive_control",
        ),
        _candidate(
            candidate_id="two_holder_finality_band",
            description=(
                "Legacy two-holder finality band from T467, retained to test "
                "packet-level independence."
            ),
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, width=2),
            evidence=TaskNaturalnessEvidence(
                task_family="finality_status_band",
                certified_record_object="two_holder_finalized_value_status",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="legacy_positive_control",
        ),
        _candidate(
            candidate_id="two_holder_support_count",
            description=(
                "Legacy two-holder support count from T467, retained to test "
                "packet-level independence."
            ),
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=2,
            finality_native_task=True,
            labeler=lambda state: f"support_count_{sum(state[:2])}",
            evidence=TaskNaturalnessEvidence(
                task_family="support_multiplicity",
                certified_record_object="two_holder_support_count_certificate",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="legacy_positive_control",
        ),
        _candidate(
            candidate_id="cheap_accessible_xor_with_task_label",
            description=(
                "A cheap accessible xor partition with a task label asserted; "
                "included as T468's hostile non-finality control."
            ),
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: f"xor_{state[0] ^ state[1]}",
            evidence=TaskNaturalnessEvidence(
                task_family="asserted_finality_task",
                certified_record_object="",
                declared_before_relation=True,
                preserves_record_value_or_support=False,
                semantics_not_label_restatement=False,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id="label_restatement_lookup",
            description=(
                "A bounded relation whose task account merely restates the "
                "chosen labels."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: "lookup_high" if state[:3] in {(1, 0, 1), (0, 1, 0)} else "lookup_low",
            evidence=TaskNaturalnessEvidence(
                task_family="lookup_label_preference",
                certified_record_object="lookup_label_table",
                declared_before_relation=True,
                preserves_record_value_or_support=False,
                semantics_not_label_restatement=False,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id="hidden_fourth_field_task",
            description="A task account depending on a field outside the access boundary.",
            fields_read=(0, 3),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: f"hidden_{state[0]}_{state[3]}",
            evidence=TaskNaturalnessEvidence(
                task_family="hidden_field_status",
                certified_record_object="hidden_field_record",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id="observer_creates_truth_overread",
            description=(
                "A forbidden packet that treats observer equivalencing as making "
                "the underlying fact true."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, width=3),
            evidence=TaskNaturalnessEvidence(
                task_family="observer_makes_truth",
                certified_record_object="three_holder_record",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
                observer_creates_truth_overread=True,
            ),
            role="forbidden_control",
            observer_creates_truth_overread=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T469 task-naturalness gate."""

    states = finite_record_states(width=4)
    budget = default_budget()
    candidates = {candidate.base.candidate_id: candidate for candidate in example_candidates()}
    evaluations = {
        candidate_id: evaluate_naturalness_candidate(candidate, budget, states)
        for candidate_id, candidate in candidates.items()
    }

    repaired_packet = evaluate_packet(
        packet_id="repaired_three_holder_packet",
        candidate_ids=(
            "three_holder_finality_band",
            "three_holder_support_count",
            "cheap_accessible_xor_with_task_label",
            "label_restatement_lookup",
            "hidden_fourth_field_task",
            "observer_creates_truth_overread",
        ),
        positive_control_ids=(
            "three_holder_finality_band",
            "three_holder_support_count",
        ),
        hostile_control_ids=(
            "cheap_accessible_xor_with_task_label",
            "label_restatement_lookup",
            "hidden_fourth_field_task",
            "observer_creates_truth_overread",
        ),
        candidates=candidates,
        evaluations=evaluations,
        states=states,
    )
    legacy_packet = evaluate_packet(
        packet_id="legacy_two_holder_packet",
        candidate_ids=(
            "two_holder_finality_band",
            "two_holder_support_count",
        ),
        positive_control_ids=(
            "two_holder_finality_band",
            "two_holder_support_count",
        ),
        hostile_control_ids=(),
        candidates=candidates,
        evaluations=evaluations,
        states=states,
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Make T468's future packet minimum executable: independent "
            "three-holder positive controls, cheap accessible non-finality "
            "hostile controls, and a predeclared task-naturalness account."
        ),
        "budget": _budget_dict(budget),
        "state_count": len(states),
        "candidate_evaluations": [
            _evaluation_dict(evaluation)
            for evaluation in evaluations.values()
        ],
        "packet_evaluations": [
            _packet_dict(repaired_packet),
            _packet_dict(legacy_packet),
        ],
        "overall_verdict": {
            "verdict": VERDICT,
            "repaired_three_holder_packet_admitted": repaired_packet.admitted,
            "legacy_two_holder_packet_admitted": legacy_packet.admitted,
            "legacy_two_holder_positive_controls_independent": (
                legacy_packet.positive_controls_independent
            ),
            "cheap_xor_base_gate_admitted": (
                evaluations["cheap_accessible_xor_with_task_label"].base_admitted
            ),
            "cheap_xor_t469_admitted": (
                evaluations["cheap_accessible_xor_with_task_label"].admitted
            ),
            "claim_ledger_update": "none",
            "d1_promotion_earned": False,
            "t10_promotion_earned": False,
            "t29_promotion_earned": False,
            "observer_theory_identification_earned": False,
            "physics_claim_earned": False,
            "reading": (
                "The repaired three-holder packet clears review admission with "
                "independent finality-band and support-count positives, while "
                "the legacy two-holder packet fails positive-control "
                "independence. The cheap accessible xor control still passes "
                "the old mechanical gate if a task label is asserted, but T469 "
                "blocks it because no certified record object or natural "
                "finality task is supplied."
            ),
        },
        "future_packet_minimum": [
            "use independent positive controls when claiming constructive support",
            "include cheap accessible non-finality hostile controls",
            "name a certified record object before selecting the relation",
            "show the task preserves record value, support, or finality status",
            "include a demotion condition for label-restatement or observer-creates-truth overread",
        ],
        "not_earned": [
            "D1 promotion",
            "T10 superselection result",
            "T29 projection-obstruction promotion",
            "observer-theory equivalence theorem",
            "physics or consciousness claim",
            "claim-ledger movement",
            "public-posture movement",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Render T469 results as Markdown."""

    verdict = result["overall_verdict"]
    candidate_rows = []
    for row in result["candidate_evaluations"]:
        blockers = ", ".join(row["blockers"]) or "none"
        candidate_rows.append(
            "| {candidate_id} | {role} | {decision} | {route_label} | {base_route_label} | {blockers} |".format(
                candidate_id=row["candidate_id"],
                role=row["role"],
                decision=row["decision"],
                route_label=row["route_label"],
                base_route_label=row["base_route_label"],
                blockers=blockers,
            )
        )

    packet_rows = []
    for row in result["packet_evaluations"]:
        blockers = ", ".join(row["blockers"]) or "none"
        packet_rows.append(
            "| {packet_id} | {decision} | {route_label} | {positive_controls_independent} | {hostile_controls_blocked} | {blockers} |".format(
                packet_id=row["packet_id"],
                decision=row["decision"],
                route_label=row["route_label"],
                positive_controls_independent=row["positive_controls_independent"],
                hostile_controls_blocked=row["hostile_controls_blocked"],
                blockers=blockers,
            )
        )

    minimum = [f"- {item}" for item in result["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in result["not_earned"]]

    return "\n".join(
        [
            "# T469 - Coarse-Graining Task-Naturalness Gate - v0.1 results",
            "",
            "> Fixture repair and admission gate only. No claim status, roadmap, "
            "README, North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T469-coarse-graining-task-naturalness-gate.md`",
            "- Model: `models/coarse_graining_task_naturalness_gate.py`",
            "- Tests: `tests/test_coarse_graining_task_naturalness_gate.py`",
            "- Artifact JSON: `results/T469-coarse-graining-task-naturalness-gate-v0.1.json`",
            "- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`",
            "- Prior audits: T467, T468",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Packet Decisions",
            "",
            "| packet | decision | route | positives independent? | hostile controls blocked? | blockers |",
            "| --- | --- | --- | --- | --- | --- |",
            *packet_rows,
            "",
            "## Candidate Decisions",
            "",
            "| candidate | role | decision | route | base route | blockers |",
            "| --- | --- | --- | --- | --- | --- |",
            *candidate_rows,
            "",
            "## Future Packet Minimum",
            "",
            *minimum,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _candidate(
    *,
    candidate_id: str,
    description: str,
    fields_read: tuple[int, ...],
    predicate_cost: int,
    holder_redundancy: int,
    reversal_cost: int,
    finality_native_task: bool,
    labeler: Labeler,
    evidence: TaskNaturalnessEvidence,
    role: str,
    observer_creates_truth_overread: bool = False,
) -> NaturalnessCandidate:
    return NaturalnessCandidate(
        base=CoarseGrainingCandidate(
            candidate_id=candidate_id,
            description=description,
            fields_read=fields_read,
            predicate_cost=predicate_cost,
            holder_redundancy=holder_redundancy,
            reversal_cost=reversal_cost,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=finality_native_task,
            expected_valid=role in {"positive_control", "legacy_positive_control"},
            labeler=labeler,
            observer_creates_truth_overread=observer_creates_truth_overread,
        ),
        evidence=evidence,
        role=role,
    )


def _finality_band_label(state: State, width: int) -> str:
    observed = state[:width]
    if all(bit == 0 for bit in observed):
        return "stable_zero"
    if all(bit == 1 for bit in observed):
        return "stable_one"
    return "unsettled"


def _positive_controls_independent(
    positive_control_ids: tuple[str, ...],
    candidates: dict[str, NaturalnessCandidate],
    states: tuple[State, ...],
) -> bool:
    if len(positive_control_ids) < 2:
        return False
    partitions = [
        _normalized_partition(states, candidates[candidate_id].base.labeler)
        for candidate_id in positive_control_ids
        if candidate_id in candidates
    ]
    return len(partitions) == len(positive_control_ids) and len(set(partitions)) > 1


def _normalized_partition(states: tuple[State, ...], labeler: Labeler) -> Partition:
    classes: dict[str, list[str]] = {}
    for state in states:
        classes.setdefault(labeler(state), []).append(_state_label(state))
    return tuple(sorted(tuple(sorted(members)) for members in classes.values()))


def _state_label(state: State) -> str:
    return "".join(str(bit) for bit in state)


def _budget_dict(budget: CertificationBudget) -> dict[str, Any]:
    return {
        "accessible_fields": list(budget.accessible_fields),
        "max_fields_read": budget.max_fields_read,
        "max_predicate_cost": budget.max_predicate_cost,
        "min_holder_redundancy": budget.min_holder_redundancy,
        "max_reversal_cost": budget.max_reversal_cost,
    }


def _evaluation_dict(evaluation: NaturalnessEvaluation) -> dict[str, Any]:
    return {
        "candidate_id": evaluation.candidate_id,
        "admitted": evaluation.admitted,
        "decision": evaluation.decision,
        "route_label": evaluation.route_label,
        "blockers": list(evaluation.blockers),
        "base_route_label": evaluation.base_route_label,
        "base_admitted": evaluation.base_admitted,
        "class_count": evaluation.class_count,
        "role": evaluation.role,
    }


def _packet_dict(packet: PacketEvaluation) -> dict[str, Any]:
    return {
        "packet_id": packet.packet_id,
        "admitted": packet.admitted,
        "decision": packet.decision,
        "route_label": packet.route_label,
        "blockers": list(packet.blockers),
        "positive_control_ids": list(packet.positive_control_ids),
        "positive_controls_independent": packet.positive_controls_independent,
        "hostile_control_ids": list(packet.hostile_control_ids),
        "hostile_controls_blocked": packet.hostile_controls_blocked,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
