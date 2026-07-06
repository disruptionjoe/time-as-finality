"""T471: multi-valued fixture gate for coarse-graining packets.

T469 repaired the valid-coarse-graining fixture over binary holders. This
module checks whether that repaired packet survives transport to a ternary
record alphabet while retaining the task-naturalness and hostile-control
burdens.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any, Callable

from models.coarse_graining_task_naturalness_gate import (
    NaturalnessCandidate,
    TaskNaturalnessEvidence,
    evaluate_naturalness_candidate,
    evaluate_packet,
)
from models.valid_coarse_graining_admissibility_gate import (
    CertificationBudget,
    CoarseGrainingCandidate,
)


State = tuple[int, ...]
Labeler = Callable[[State], str]
Partition = tuple[tuple[str, ...], ...]

ARTIFACT_ID = "T471-coarse-graining-multivalued-fixture-gate-v0.1"
VERDICT = "MULTIVALUED_FIXTURE_GATE_BUILT_NO_PROMOTION"


@dataclass(frozen=True)
class AlphabetPacket:
    """Candidate identifiers for one alphabet-sized packet."""

    alphabet_size: int
    packet_id: str
    candidate_ids: tuple[str, ...]
    positive_control_ids: tuple[str, ...]
    hostile_control_ids: tuple[str, ...]


def default_budget() -> CertificationBudget:
    """Return the T471 three-holder observer budget."""

    return CertificationBudget(
        accessible_fields=(0, 1, 2),
        max_fields_read=3,
        max_predicate_cost=4,
        min_holder_redundancy=2,
        max_reversal_cost=2,
    )


def finite_record_states(
    *,
    width: int = 4,
    alphabet_size: int = 3,
) -> tuple[State, ...]:
    """Enumerate finite record states over a small alphabet."""

    if width < 1:
        raise ValueError("width must be positive")
    if alphabet_size < 2:
        raise ValueError("alphabet_size must be at least 2")
    return tuple(tuple(values) for values in product(range(alphabet_size), repeat=width))


def packet_candidates(alphabet_size: int) -> tuple[NaturalnessCandidate, ...]:
    """Return the T471 candidate catalogue for one alphabet size."""

    prefix = _prefix(alphabet_size)
    return (
        _candidate(
            candidate_id=f"{prefix}_finality_band",
            description=(
                "Accessible holders certify a single stable record value or an "
                "unsettled mixed-status class."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, width=3),
            evidence=TaskNaturalnessEvidence(
                task_family="multi_value_finality_status_band",
                certified_record_object=(
                    f"{prefix}_three_holder_finalized_value_status"
                ),
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="positive_control",
        ),
        _candidate(
            candidate_id=f"{prefix}_support_count",
            description=(
                "Accessible holders certify how many local records carry a "
                "nonzero finalized value."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=2,
            finality_native_task=True,
            labeler=lambda state: f"support_count_{sum(1 for value in state[:3] if value != 0)}",
            evidence=TaskNaturalnessEvidence(
                task_family="multi_value_support_multiplicity",
                certified_record_object=f"{prefix}_three_holder_support_count",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="positive_control",
        ),
        _candidate(
            candidate_id=f"{prefix}_mod_sum_with_task_label",
            description=(
                "A cheap accessible modular-sum partition with a finality-task "
                "label asserted."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: f"mod_sum_{sum(state[:3]) % alphabet_size}",
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
            candidate_id=f"{prefix}_label_restatement_lookup",
            description=(
                "A bounded lookup whose task account merely restates selected "
                "labels."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: (
                "favored_pattern"
                if state[:3] in _favored_patterns(alphabet_size)
                else "other_pattern"
            ),
            evidence=TaskNaturalnessEvidence(
                task_family="lookup_label_preference",
                certified_record_object=f"{prefix}_lookup_label_table",
                declared_before_relation=True,
                preserves_record_value_or_support=False,
                semantics_not_label_restatement=False,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id=f"{prefix}_hidden_fourth_field_task",
            description="A task account depending on a field outside access.",
            fields_read=(0, 3),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: f"hidden_{state[0]}_{state[3]}",
            evidence=TaskNaturalnessEvidence(
                task_family="hidden_field_status",
                certified_record_object=f"{prefix}_hidden_field_record",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id=f"{prefix}_microstate_identity",
            description="A full microstate identity relation over the fixture.",
            fields_read=(0, 1, 2, 3),
            predicate_cost=4,
            holder_redundancy=4,
            reversal_cost=4,
            finality_native_task=True,
            labeler=lambda state: "state_" + _state_label(state),
            evidence=TaskNaturalnessEvidence(
                task_family="microstate_identity",
                certified_record_object=f"{prefix}_full_microstate",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id=f"{prefix}_observer_creates_truth_overread",
            description=(
                "A forbidden packet that treats observer equivalencing as truth "
                "creation."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, width=3),
            evidence=TaskNaturalnessEvidence(
                task_family="observer_makes_truth",
                certified_record_object=f"{prefix}_three_holder_record",
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


def packet_shape(alphabet_size: int) -> AlphabetPacket:
    """Return the packet layout for one alphabet size."""

    prefix = _prefix(alphabet_size)
    positive_control_ids = (
        f"{prefix}_finality_band",
        f"{prefix}_support_count",
    )
    hostile_control_ids = (
        f"{prefix}_mod_sum_with_task_label",
        f"{prefix}_label_restatement_lookup",
        f"{prefix}_hidden_fourth_field_task",
        f"{prefix}_microstate_identity",
        f"{prefix}_observer_creates_truth_overread",
    )
    return AlphabetPacket(
        alphabet_size=alphabet_size,
        packet_id=f"{prefix}_three_holder_packet",
        candidate_ids=positive_control_ids + hostile_control_ids,
        positive_control_ids=positive_control_ids,
        hostile_control_ids=hostile_control_ids,
    )


def compare_positive_controls(
    *,
    alphabet_size: int,
    width: int = 3,
) -> dict[str, Any]:
    """Compare the finality-band and support-count partitions."""

    states = finite_record_states(width=width, alphabet_size=alphabet_size)
    finality_partition = _normalized_partition(
        states,
        lambda state: _finality_band_label(state, width=width),
    )
    support_partition = _normalized_partition(
        states,
        lambda state: f"support_count_{sum(1 for value in state[:width] if value != 0)}",
    )
    return {
        "alphabet_size": alphabet_size,
        "holder_width": width,
        "state_count": len(states),
        "finality_band_class_count": len(finality_partition),
        "support_count_class_count": len(support_partition),
        "partitions_identical": finality_partition == support_partition,
    }


def run() -> dict[str, Any]:
    """Run the T471 multi-valued fixture gate."""

    budget = default_budget()
    alphabet_sizes = (2, 3)
    candidates: dict[str, NaturalnessCandidate] = {}
    evaluations: dict[str, Any] = {}
    packets = []

    for alphabet_size in alphabet_sizes:
        states = finite_record_states(width=4, alphabet_size=alphabet_size)
        for candidate in packet_candidates(alphabet_size):
            candidate_id = candidate.base.candidate_id
            candidates[candidate_id] = candidate
            evaluations[candidate_id] = evaluate_naturalness_candidate(
                candidate,
                budget,
                states,
            )

        shape = packet_shape(alphabet_size)
        packet = evaluate_packet(
            packet_id=shape.packet_id,
            candidate_ids=shape.candidate_ids,
            positive_control_ids=shape.positive_control_ids,
            hostile_control_ids=shape.hostile_control_ids,
            candidates=candidates,
            evaluations=evaluations,
            states=states,
        )
        packets.append(packet)

    ternary_mod_sum = evaluations["ternary_mod_sum_with_task_label"]
    ternary_packet = next(
        packet for packet in packets if packet.packet_id == "ternary_three_holder_packet"
    )
    binary_packet = next(
        packet for packet in packets if packet.packet_id == "binary_three_holder_packet"
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Stress T469's repaired task-naturalness packet against a ternary "
            "record alphabet while retaining cheap non-finality, label "
            "restatement, hidden-field, microstate, and observer-creates-truth "
            "hostile controls."
        ),
        "budget": _budget_dict(budget),
        "alphabet_sizes": list(alphabet_sizes),
        "positive_control_comparisons": [
            compare_positive_controls(alphabet_size=alphabet_size)
            for alphabet_size in alphabet_sizes
        ],
        "candidate_evaluations": [
            _evaluation_dict(evaluation)
            for evaluation in evaluations.values()
        ],
        "packet_evaluations": [_packet_dict(packet) for packet in packets],
        "overall_verdict": {
            "verdict": VERDICT,
            "binary_reference_packet_admitted": binary_packet.admitted,
            "ternary_packet_admitted": ternary_packet.admitted,
            "ternary_positive_controls_independent": (
                ternary_packet.positive_controls_independent
            ),
            "ternary_hostile_controls_blocked": ternary_packet.hostile_controls_blocked,
            "ternary_mod_sum_base_gate_admitted": ternary_mod_sum.base_admitted,
            "ternary_mod_sum_t470_admitted": ternary_mod_sum.admitted,
            "claim_ledger_update": "none",
            "d1_promotion_earned": False,
            "t10_promotion_earned": False,
            "t29_promotion_earned": False,
            "observer_theory_identification_earned": False,
            "physics_claim_earned": False,
            "reading": (
                "The T469 packet shape survives the ternary holder alphabet: "
                "finality band and support count remain independent positive "
                "controls, while cheap modular sum, label restatement, hidden "
                "field, microstate identity, and observer-creates-truth controls "
                "are blocked. This is an alphabet-stress gate only, not an "
                "Observer Theory equivalence theorem or claim promotion."
            ),
        },
        "future_packet_minimum": [
            "stress constructive packets across at least one non-binary alphabet",
            "keep independent positive controls under alphabet transport",
            "include cheap accessible arithmetic partitions as hostile controls",
            "block label restatement and microstate identity before claim movement",
            "keep certified-record and observer-creates-truth guardrails active",
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
    """Render T471 results as Markdown."""

    verdict = result["overall_verdict"]
    comparison_rows = []
    for row in result["positive_control_comparisons"]:
        comparison_rows.append(
            "| {alphabet_size} | {holder_width} | {state_count} | "
            "{finality_band_class_count} | {support_count_class_count} | "
            "{partitions_identical} |".format(**row)
        )

    packet_rows = []
    for row in result["packet_evaluations"]:
        blockers = ", ".join(row["blockers"]) or "none"
        packet_rows.append(
            "| {packet_id} | {decision} | {route_label} | "
            "{positive_controls_independent} | {hostile_controls_blocked} | "
            "{blockers} |".format(
                packet_id=row["packet_id"],
                decision=row["decision"],
                route_label=row["route_label"],
                positive_controls_independent=row["positive_controls_independent"],
                hostile_controls_blocked=row["hostile_controls_blocked"],
                blockers=blockers,
            )
        )

    candidate_rows = []
    for row in result["candidate_evaluations"]:
        blockers = ", ".join(row["blockers"]) or "none"
        candidate_rows.append(
            "| {candidate_id} | {role} | {decision} | {route_label} | "
            "{base_route_label} | {blockers} |".format(
                candidate_id=row["candidate_id"],
                role=row["role"],
                decision=row["decision"],
                route_label=row["route_label"],
                base_route_label=row["base_route_label"],
                blockers=blockers,
            )
        )

    minimum = [f"- {item}" for item in result["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in result["not_earned"]]

    return "\n".join(
        [
            "# T471 - Coarse-Graining Multivalued Fixture Gate - v0.1 results",
            "",
            "> Alphabet-stress gate only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T471-coarse-graining-multivalued-fixture-gate.md`",
            "- Model: `models/coarse_graining_multivalued_fixture_gate.py`",
            "- Tests: `tests/test_coarse_graining_multivalued_fixture_gate.py`",
            "- Artifact JSON: `results/T471-coarse-graining-multivalued-fixture-gate-v0.1.json`",
            "- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`",
            "- Prior gates: T467, T468, T469",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Positive-Control Partition Comparison",
            "",
            "| alphabet size | holder width | state count | finality-band classes | support-count classes | identical? |",
            "| --- | --- | --- | --- | --- | --- |",
            *comparison_rows,
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
            expected_valid=role == "positive_control",
            labeler=labeler,
            observer_creates_truth_overread=observer_creates_truth_overread,
        ),
        evidence=evidence,
        role=role,
    )


def _prefix(alphabet_size: int) -> str:
    if alphabet_size == 2:
        return "binary"
    if alphabet_size == 3:
        return "ternary"
    return f"alphabet_{alphabet_size}"


def _finality_band_label(state: State, width: int) -> str:
    observed = state[:width]
    first = observed[0]
    if all(value == first for value in observed):
        return f"stable_value_{first}"
    return "unsettled"


def _favored_patterns(alphabet_size: int) -> frozenset[State]:
    ascending = tuple(range(min(alphabet_size, 3)))
    if len(ascending) < 3:
        ascending = ascending + (0,) * (3 - len(ascending))
    descending = tuple(reversed(ascending))
    return frozenset({ascending, descending})


def _normalized_partition(states: tuple[State, ...], labeler: Labeler) -> Partition:
    classes: dict[str, list[str]] = {}
    for state in states:
        classes.setdefault(labeler(state), []).append(_state_label(state))
    return tuple(sorted(tuple(sorted(members)) for members in classes.values()))


def _state_label(state: State) -> str:
    return "".join(str(value) for value in state)


def _budget_dict(budget: CertificationBudget) -> dict[str, Any]:
    return {
        "accessible_fields": list(budget.accessible_fields),
        "max_fields_read": budget.max_fields_read,
        "max_predicate_cost": budget.max_predicate_cost,
        "min_holder_redundancy": budget.min_holder_redundancy,
        "max_reversal_cost": budget.max_reversal_cost,
    }


def _evaluation_dict(evaluation: Any) -> dict[str, Any]:
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


def _packet_dict(packet: Any) -> dict[str, Any]:
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
