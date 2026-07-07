"""T495 - bounded-record retrieval bottleneck gate.

This turns the finality-as-computation exploration into a finite capability
screen. It tests the retention axis only: a full-history record determines
arbitrary indexed retrieval, while bounded committed summaries do not.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Iterable


ARTIFACT = "T495-bounded-record-retrieval-bottleneck-gate-v0.1"
VERDICT = "BOUNDED_RETRIEVAL_BOTTLENECK_BUILT_RETENTION_AXIS_ONLY"
STREAM_LENGTH = 5
ALPHABET = (0, 1)

SOURCE_EXPLORATION = "explorations/finality-as-computation-state-vs-attention-2026-07-07.md"

HONEST_CEILING = (
    "Finite capability-audit toy only. T495 supports the information-retention "
    "axis named by the computation exploration: full-history access determines "
    "arbitrary retrieval while bounded committed summaries do not. It does not "
    "prove a quantum, Standard Model, decoherence, or complexity-theorem claim; "
    "does not assert that physics is literally a Transformer or SSM; and does "
    "not move claim ledger, roadmap, README, North Star, public posture, hard "
    "policy, external publication, or cross-repo truth."
)


BitStream = tuple[int, ...]
Projection = Callable[[BitStream], tuple[Any, ...]]
Capability = Callable[[BitStream], tuple[Any, ...]]


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    description: str
    projection_label: str
    capability_label: str
    expected_factorizes: bool
    interpretation: str


@dataclass(frozen=True)
class ScenarioEvaluation:
    scenario_id: str
    factorizes: bool
    label: str
    projection_class_count: int
    capability_class_count: int
    max_capability_spread: int
    non_singleton_fiber_count: int
    example_collision: dict[str, Any] | None
    interpretation: str


@dataclass(frozen=True)
class CandidateReading:
    reading_id: str
    description: str
    uses_retention_axis: bool = False
    claims_naive_attention_quantum_copyability: bool = False
    claims_physics_mechanism: bool = False
    claims_complexity_theorem: bool = False
    treats_as_capability_review_target: bool = False
    claims_public_or_cross_repo_update: bool = False


@dataclass(frozen=True)
class ReadingEvaluation:
    reading_id: str
    admitted: bool
    label: str
    action: str
    reason: str
    reading: CandidateReading


def source_space(length: int = STREAM_LENGTH) -> tuple[BitStream, ...]:
    return tuple(itertools.product(ALPHABET, repeat=length))


def project_full_history(stream: BitStream) -> tuple[Any, ...]:
    return ("full_history",) + stream


def project_last_k(k: int) -> Projection:
    def _project(stream: BitStream) -> tuple[Any, ...]:
        return ("last_k", len(stream), k) + stream[-k:]

    return _project


def project_parity(stream: BitStream) -> tuple[Any, ...]:
    return ("parity", len(stream), sum(stream) % 2)


def cap_arbitrary_indexed_retrieval(stream: BitStream) -> tuple[Any, ...]:
    return tuple((index, bit) for index, bit in enumerate(stream))


def cap_suffix_retrieval(k: int) -> Capability:
    def _cap(stream: BitStream) -> tuple[Any, ...]:
        start = len(stream) - k
        return tuple((index, stream[index]) for index in range(start, len(stream)))

    return _cap


def cap_parity(stream: BitStream) -> tuple[Any, ...]:
    return (("parity", sum(stream) % 2),)


PROJECTIONS: dict[str, Projection] = {
    "full_history": project_full_history,
    "last_2_committed_state": project_last_k(2),
    "parity_committed_state": project_parity,
}

CAPABILITIES: dict[str, Capability] = {
    "arbitrary_indexed_retrieval": cap_arbitrary_indexed_retrieval,
    "last_2_indexed_retrieval": cap_suffix_retrieval(2),
    "parity_query": cap_parity,
}


def scenarios() -> tuple[Scenario, ...]:
    return (
        Scenario(
            scenario_id="full_history_arbitrary_retrieval_control",
            description="Full-history access over five bits answers every indexed retrieval query.",
            projection_label="full_history",
            capability_label="arbitrary_indexed_retrieval",
            expected_factorizes=True,
            interpretation="Full retention is the positive preservation control.",
        ),
        Scenario(
            scenario_id="last2_state_arbitrary_retrieval_bottleneck",
            description="A committed last-2 state is asked to answer every indexed retrieval query.",
            projection_label="last_2_committed_state",
            capability_label="arbitrary_indexed_retrieval",
            expected_factorizes=False,
            interpretation=(
                "The bounded state loses arbitrary retrieval capability: old "
                "bits vary across a fixed visible committed state."
            ),
        ),
        Scenario(
            scenario_id="last2_state_suffix_retrieval_control",
            description="The same last-2 state is asked only for the retained suffix.",
            projection_label="last_2_committed_state",
            capability_label="last_2_indexed_retrieval",
            expected_factorizes=True,
            interpretation="Bounded state is sufficient for the task it explicitly retains.",
        ),
        Scenario(
            scenario_id="parity_state_parity_task_control",
            description="A parity summary is asked for the parity task it was built to preserve.",
            projection_label="parity_committed_state",
            capability_label="parity_query",
            expected_factorizes=True,
            interpretation="A summary can preserve its native declared task.",
        ),
        Scenario(
            scenario_id="parity_state_arbitrary_retrieval_bottleneck",
            description="A parity summary is asked for arbitrary indexed retrieval.",
            projection_label="parity_committed_state",
            capability_label="arbitrary_indexed_retrieval",
            expected_factorizes=False,
            interpretation="Parity retention is not arbitrary record retrieval.",
        ),
    )


def _to_jsonable_tuple(value: tuple[Any, ...]) -> list[Any]:
    converted: list[Any] = []
    for item in value:
        if isinstance(item, tuple):
            converted.append(_to_jsonable_tuple(item))
        else:
            converted.append(item)
    return converted


def evaluate_scenario(scenario: Scenario, streams: Iterable[BitStream]) -> ScenarioEvaluation:
    projection = PROJECTIONS[scenario.projection_label]
    capability = CAPABILITIES[scenario.capability_label]
    fibers: dict[tuple[Any, ...], set[tuple[Any, ...]]] = defaultdict(set)
    examples: dict[tuple[Any, ...], dict[tuple[Any, ...], BitStream]] = defaultdict(dict)

    capability_values: set[tuple[Any, ...]] = set()
    for stream in streams:
        p_value = projection(stream)
        c_value = capability(stream)
        fibers[p_value].add(c_value)
        capability_values.add(c_value)
        examples[p_value].setdefault(c_value, stream)

    spreads = {p_value: len(c_values) for p_value, c_values in fibers.items()}
    factorizes = all(spread == 1 for spread in spreads.values())
    non_singleton = sum(1 for spread in spreads.values() if spread > 1)
    max_spread = max(spreads.values())
    collision = None
    for p_value, c_values in fibers.items():
        if len(c_values) > 1:
            ordered_caps = sorted(c_values, key=repr)
            first_cap, second_cap = ordered_caps[0], ordered_caps[1]
            collision = {
                "visible_state": _to_jsonable_tuple(p_value),
                "first_stream": list(examples[p_value][first_cap]),
                "first_capability": _to_jsonable_tuple(first_cap),
                "second_stream": list(examples[p_value][second_cap]),
                "second_capability": _to_jsonable_tuple(second_cap),
            }
            break

    if factorizes and scenario.expected_factorizes:
        label = "PRESERVATION_CONTROL_PASSED"
    elif (not factorizes) and (not scenario.expected_factorizes):
        label = "BOTTLENECK_DETECTED_AS_EXPECTED"
    elif factorizes:
        label = "UNEXPECTED_FACTORING"
    else:
        label = "UNEXPECTED_NONFACTORING"

    return ScenarioEvaluation(
        scenario_id=scenario.scenario_id,
        factorizes=factorizes,
        label=label,
        projection_class_count=len(fibers),
        capability_class_count=len(capability_values),
        max_capability_spread=max_spread,
        non_singleton_fiber_count=non_singleton,
        example_collision=collision,
        interpretation=scenario.interpretation,
    )


def candidate_readings() -> tuple[CandidateReading, ...]:
    return (
        CandidateReading(
            reading_id="retention_axis_capability_probe",
            description=(
                "Treat full-history versus bounded committed-state access as a "
                "finite capability probe for arbitrary retrieval."
            ),
            uses_retention_axis=True,
            treats_as_capability_review_target=True,
        ),
        CandidateReading(
            reading_id="naive_attention_quantum_copyability_mapping",
            description=(
                "Infer from full-history retrieval that the attention side maps "
                "directly to copyable quantum states."
            ),
            claims_naive_attention_quantum_copyability=True,
        ),
        CandidateReading(
            reading_id="physics_mechanism_import",
            description="Treat the finite gate as a decoherence or Standard Model mechanism.",
            uses_retention_axis=True,
            claims_physics_mechanism=True,
        ),
        CandidateReading(
            reading_id="complexity_theorem_shortcut",
            description=(
                "Treat this finite enumeration as if it proved an SSM/Transformer "
                "complexity lower bound."
            ),
            uses_retention_axis=True,
            claims_complexity_theorem=True,
        ),
        CandidateReading(
            reading_id="public_or_cross_repo_update_shortcut",
            description="Use the computation analogy to move public posture or cross-repo truth.",
            claims_public_or_cross_repo_update=True,
        ),
    )


def evaluate_reading(reading: CandidateReading) -> ReadingEvaluation:
    if reading.claims_public_or_cross_repo_update:
        return ReadingEvaluation(
            reading.reading_id,
            False,
            "BLOCKED_PUBLIC_OR_CROSS_REPO_UPDATE",
            "stop",
            "A repo-local finite screen does not authorize public posture or cross-repo truth movement.",
            reading,
        )
    if reading.claims_naive_attention_quantum_copyability:
        return ReadingEvaluation(
            reading.reading_id,
            False,
            "REJECTED_NAIVE_COPYABILITY_MAPPING",
            "reject",
            "The gate preserves retrieval for stored classical records; it does not map unknown quantum states to copyable records.",
            reading,
        )
    if reading.claims_physics_mechanism:
        return ReadingEvaluation(
            reading.reading_id,
            False,
            "REJECTED_PHYSICS_MECHANISM_IMPORT",
            "reject",
            "The finite retention-axis fixture is not a decoherence, Standard Model, or physical mechanism result.",
            reading,
        )
    if reading.claims_complexity_theorem:
        return ReadingEvaluation(
            reading.reading_id,
            False,
            "REJECTED_COMPLEXITY_THEOREM_SHORTCUT",
            "reject",
            "Finite enumeration can motivate a lower-bound target, but it is not itself an SSM/Transformer theorem.",
            reading,
        )
    if reading.uses_retention_axis and reading.treats_as_capability_review_target:
        return ReadingEvaluation(
            reading.reading_id,
            True,
            "ADMITTED_RETENTION_AXIS_CAPABILITY_PROBE",
            "record",
            "The bounded-state retrieval bottleneck is admitted as a finite review target for C(R)-style capability language.",
            reading,
        )
    return ReadingEvaluation(
        reading.reading_id,
        False,
        "REJECTED_UNTYPED_READING",
        "reject",
        "The reading does not stay within the typed finite capability probe.",
        reading,
    )


def run() -> dict[str, Any]:
    streams = source_space()
    scenario_evaluations = [evaluate_scenario(scenario, streams) for scenario in scenarios()]
    reading_evaluations = [evaluate_reading(reading) for reading in candidate_readings()]
    all_expected = all(
        evaluation.factorizes == scenario.expected_factorizes
        for scenario, evaluation in zip(scenarios(), scenario_evaluations)
    )
    admitted_readings = [
        evaluation.reading_id for evaluation in reading_evaluations if evaluation.admitted
    ]

    return {
        "artifact": ARTIFACT,
        "source_exploration": SOURCE_EXPLORATION,
        "stream_space": {
            "alphabet": list(ALPHABET),
            "length": STREAM_LENGTH,
            "stream_count": len(streams),
        },
        "scenario_evaluations": [asdict(evaluation) for evaluation in scenario_evaluations],
        "reading_evaluations": [
            {
                "reading_id": evaluation.reading_id,
                "admitted": evaluation.admitted,
                "label": evaluation.label,
                "action": evaluation.action,
                "reason": evaluation.reason,
                "reading": asdict(evaluation.reading),
            }
            for evaluation in reading_evaluations
        ],
        "overall_verdict": {
            "verdict": VERDICT,
            "all_scenarios_matched_expected": all_expected,
            "admitted_reading_ids": admitted_readings,
            "retention_axis_only": True,
            "claim_movement": False,
            "public_or_cross_repo_movement": False,
        },
        "strongest_result": (
            "In the finite five-bit stream space, full-history visibility factors "
            "arbitrary indexed retrieval, but last-2 and parity committed states "
            "have non-singleton arbitrary-retrieval spreads. The same bounded "
            "states pass native positive controls for retained suffix or parity "
            "queries. The useful computation analogy is therefore a typed "
            "retention bottleneck, not the failed copyability mapping."
        ),
        "recommended_next": [
            "If this lane continues, cite real SSM/attention lower-bound sources before importing any theorem language.",
            "Use T495 as a finite C(R)-style review target for bounded-record retrieval, not as physics support.",
            "Keep the naive attention/quantum copyability mapping demoted unless a separate typed packet repairs it.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    scenario_rows = [
        "| {scenario_id} | {factorizes} | {label} | {spread} | {interp} |".format(
            scenario_id=item["scenario_id"],
            factorizes="yes" if item["factorizes"] else "no",
            label=item["label"],
            spread=item["max_capability_spread"],
            interp=item["interpretation"],
        )
        for item in payload["scenario_evaluations"]
    ]
    reading_rows = [
        "| {reading_id} | {admitted} | {label} | {action} | {reason} |".format(
            reading_id=item["reading_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["label"],
            action=item["action"],
            reason=item["reason"],
        )
        for item in payload["reading_evaluations"]
    ]
    next_lines = [f"- {item}" for item in payload["recommended_next"]]

    return "\n".join(
        [
            "# T495 - Bounded-Record Retrieval Bottleneck Gate - v0.1 results",
            "",
            "> Finite capability-audit toy only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T495-bounded-record-retrieval-bottleneck-gate.md`",
            "- Model: `models/bounded_record_retrieval_bottleneck_gate.py`",
            "- Tests: `tests/test_bounded_record_retrieval_bottleneck_gate.py`",
            "- Source exploration: `explorations/finality-as-computation-state-vs-attention-2026-07-07.md`",
            "- Artifact JSON: `results/T495-bounded-record-retrieval-bottleneck-gate-v0.1.json`",
            "",
            f"## Overall verdict: {payload['overall_verdict']['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Scenario Evaluation",
            "",
            "| Scenario | Factors? | Label | Max spread | Interpretation |",
            "| --- | --- | --- | --- | --- |",
            *scenario_rows,
            "",
            "## Reading Evaluation",
            "",
            "| Reading | Admitted? | Label | Action | Reason |",
            "| --- | --- | --- | --- | --- |",
            *reading_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a finite capability bottleneck for arbitrary retrieval under bounded committed records, with positive controls for retained suffix and parity tasks.",
            "",
            "Does not earn: a quantum, Standard Model, decoherence, physics-mechanism, SSM/Transformer lower-bound, claim-ledger, public-posture, or cross-repo result.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_lines,
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
        json_path = results_dir / "T495-bounded-record-retrieval-bottleneck-gate-v0.1.json"
        md_path = results_dir / "T495-bounded-record-retrieval-bottleneck-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
