"""T497 - source-checked bounded retrieval composite stack gate.

This extends T495 only in the bounded computation lane. It adds primary-source
status for copying/retrieval workloads and checks finite length scaling for
bounded summaries. The admitted outcome is a composite absorber explanation or
review target, not a theorem, physics mechanism, or claim movement.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Iterable


ARTIFACT = "T497-bounded-retrieval-source-checked-stack-gate-v0.1"
VERDICT = "BOUNDED_RETRIEVAL_SOURCE_CHECKED_STACK_BUILT_COMPOSITE_EXPLANATION"
SOURCE_T495 = "tests/T495-bounded-record-retrieval-bottleneck-gate.md"
SOURCE_T496 = "tests/T496-bridge-functor-admission-packet-gate.md"
SOURCE_N18 = "literature/N18-bounded-retrieval-copying-lower-bound-sources.md"
SOURCE_PROGRESS_LANES = "open-problems/composite-absorber-stack-progress-lanes.md"

ALPHABET = (0, 1)
LENGTHS = tuple(range(2, 9))

HONEST_CEILING = (
    "T497 is a source-checked computation-lane composite explanation and finite "
    "review target. It does not prove an SSM/Transformer theorem, does not "
    "claim physics mechanism, does not assert attention equals quantum "
    "copyability, and does not move claim ledger, roadmap, README, North Star, "
    "public posture, hard policy, external publication, or cross-repo truth."
)


BitStream = tuple[int, ...]
Projection = Callable[[BitStream], tuple[Any, ...]]
Capability = Callable[[BitStream], tuple[Any, ...]]


@dataclass(frozen=True)
class SourceCheck:
    source_id: str
    citation: str
    checked: bool
    supports_copying_retrieval_workload: bool
    supports_fixed_state_caveat: bool
    blocks_overread: str
    allowed_use: str


@dataclass(frozen=True)
class StackAbsorber:
    absorber_id: str
    status: str
    granted_form: str
    effect: str


@dataclass(frozen=True)
class LengthEvaluation:
    length: int
    projection_label: str
    capability_label: str
    factorizes: bool
    expected_factorizes: bool
    projection_class_count: int
    capability_class_count: int
    max_capability_spread: int
    expected_max_spread: int
    non_singleton_fiber_count: int
    label: str


@dataclass(frozen=True)
class Reading:
    reading_id: str
    description: str
    uses_source_checked_retrieval_workload: bool = False
    admits_composite_explanation: bool = False
    claims_complexity_theorem: bool = False
    claims_physics_mechanism: bool = False
    claims_naive_attention_quantum_copyability: bool = False
    claims_public_or_cross_repo_movement: bool = False


@dataclass(frozen=True)
class ReadingDecision:
    reading_id: str
    admitted: bool
    label: str
    action: str
    reason: str


def source_space(length: int) -> tuple[BitStream, ...]:
    return tuple(itertools.product(ALPHABET, repeat=length))


def project_full(stream: BitStream) -> tuple[Any, ...]:
    return ("full", len(stream)) + stream


def project_last(k: int) -> Projection:
    def _project(stream: BitStream) -> tuple[Any, ...]:
        return ("last", len(stream), k) + stream[-k:]

    return _project


def cap_arbitrary(stream: BitStream) -> tuple[Any, ...]:
    return tuple(enumerate(stream))


def cap_suffix(k: int) -> Capability:
    def _cap(stream: BitStream) -> tuple[Any, ...]:
        start = len(stream) - k
        return tuple((index, stream[index]) for index in range(start, len(stream)))

    return _cap


def source_checks() -> tuple[SourceCheck, ...]:
    return (
        SourceCheck(
            source_id="jelassi_2024_copying",
            citation=(
                "Jelassi, Brandfonbrener, Kakade, and Malach, 'Repeat After Me: "
                "Transformers are Better than State Space Models at Copying,' ICML 2024."
            ),
            checked=True,
            supports_copying_retrieval_workload=True,
            supports_fixed_state_caveat=True,
            blocks_overread="Does not imply physics or TaF novelty; scope is copying/retrieval workloads.",
            allowed_use="Primary support for source-checked bounded retrieval workload language.",
        ),
        SourceCheck(
            source_id="gu_dao_2023_mamba",
            citation="Gu and Dao, 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces,' arXiv:2312.00752.",
            checked=True,
            supports_copying_retrieval_workload=False,
            supports_fixed_state_caveat=True,
            blocks_overread="Blocks simplistic SSM-bad readings; selective/input-dependent state matters.",
            allowed_use="Architecture caveat for any SSM comparison.",
        ),
        SourceCheck(
            source_id="schlag_2021_fast_weights",
            citation="Schlag, Irie, and Schmidhuber, 'Linear Transformers Are Secretly Fast Weight Programmers,' ICML 2021.",
            checked=True,
            supports_copying_retrieval_workload=True,
            supports_fixed_state_caveat=True,
            blocks_overread="Blocks naive full-attention-is-unbounded-history readings; fast-weight memory has capacity structure.",
            allowed_use="Memory-programming caveat for attention/linear-attention comparisons.",
        ),
    )


def absorber_stack() -> tuple[StackAbsorber, ...]:
    return (
        StackAbsorber(
            absorber_id="full_history_access",
            status="granted_and_tested",
            granted_form="The full stream is visible.",
            effect="Arbitrary indexed retrieval factors through visibility.",
        ),
        StackAbsorber(
            absorber_id="bounded_retained_state_summary",
            status="granted_and_tested",
            granted_form="Only the last k bits are visible as committed state.",
            effect="Arbitrary indexed retrieval has non-singleton spread for n > k.",
        ),
        StackAbsorber(
            absorber_id="native_retained_task_control",
            status="granted_and_tested",
            granted_form="The task asks only for the retained suffix.",
            effect="The bounded summary factors its native task.",
        ),
        StackAbsorber(
            absorber_id="source_checked_copying_retrieval_workload",
            status="source_checked",
            granted_form="N18 sources permit computation-side copying/retrieval workload language.",
            effect="The lane can use lower-bound-source status as review scaffolding, not as theorem import.",
        ),
        StackAbsorber(
            absorber_id="architecture_caveat_stack",
            status="granted",
            granted_form="Fixed latent state, selective state, and fast-weight memory distinctions are not collapsed.",
            effect="Naive SSM/attention polarity and physics overreads are blocked.",
        ),
    )


def evaluate_factorization(
    streams: Iterable[BitStream],
    projection: Projection,
    capability: Capability,
) -> tuple[bool, int, int, int, int]:
    fibers: dict[tuple[Any, ...], set[tuple[Any, ...]]] = defaultdict(set)
    capability_values: set[tuple[Any, ...]] = set()
    for stream in streams:
        p_value = projection(stream)
        c_value = capability(stream)
        fibers[p_value].add(c_value)
        capability_values.add(c_value)
    spreads = [len(values) for values in fibers.values()]
    return (
        all(spread == 1 for spread in spreads),
        len(fibers),
        len(capability_values),
        max(spreads),
        sum(1 for spread in spreads if spread > 1),
    )


def length_evaluations(k: int = 2) -> tuple[LengthEvaluation, ...]:
    evaluations: list[LengthEvaluation] = []
    for length in LENGTHS:
        streams = source_space(length)
        scenarios = (
            ("full_history", "arbitrary_retrieval", project_full, cap_arbitrary, True, 1),
            (
                f"last_{k}_state",
                "arbitrary_retrieval",
                project_last(k),
                cap_arbitrary,
                length <= k,
                1 if length <= k else 2 ** (length - k),
            ),
            (
                f"last_{k}_state",
                f"last_{k}_suffix_retrieval",
                project_last(k),
                cap_suffix(k),
                True,
                1,
            ),
        )
        for projection_label, capability_label, projection, capability, expected, spread in scenarios:
            factorizes, p_count, c_count, max_spread, non_singleton = evaluate_factorization(
                streams, projection, capability
            )
            if factorizes == expected and max_spread == spread:
                label = "EXPECTED_STACK_BEHAVIOR"
            elif factorizes == expected:
                label = "EXPECTED_FACTORING_UNEXPECTED_SPREAD"
            else:
                label = "UNEXPECTED_FACTORING_BEHAVIOR"
            evaluations.append(
                LengthEvaluation(
                    length=length,
                    projection_label=projection_label,
                    capability_label=capability_label,
                    factorizes=factorizes,
                    expected_factorizes=expected,
                    projection_class_count=p_count,
                    capability_class_count=c_count,
                    max_capability_spread=max_spread,
                    expected_max_spread=spread,
                    non_singleton_fiber_count=non_singleton,
                    label=label,
                )
            )
    return tuple(evaluations)


def readings() -> tuple[Reading, ...]:
    return (
        Reading(
            reading_id="bounded_retrieval_composite_explanation",
            description="Bounded committed state explains native retention success plus arbitrary retrieval failure.",
            uses_source_checked_retrieval_workload=True,
            admits_composite_explanation=True,
        ),
        Reading(
            reading_id="complexity_theorem_import",
            description="Treat finite spread checks as an SSM/Transformer lower-bound theorem.",
            uses_source_checked_retrieval_workload=True,
            claims_complexity_theorem=True,
        ),
        Reading(
            reading_id="physics_mechanism_import",
            description="Treat bounded retrieval as decoherence, Standard Model, or physical finality mechanism.",
            claims_physics_mechanism=True,
        ),
        Reading(
            reading_id="attention_quantum_copyability_revival",
            description="Revive the naive attention equals quantum copyability polarity.",
            claims_naive_attention_quantum_copyability=True,
        ),
        Reading(
            reading_id="public_or_cross_repo_shortcut",
            description="Move public posture or cross-repo truth from the source-checked computation lane.",
            claims_public_or_cross_repo_movement=True,
        ),
    )


def decide_reading(reading: Reading) -> ReadingDecision:
    if reading.claims_public_or_cross_repo_movement:
        return ReadingDecision(
            reading.reading_id,
            False,
            "BLOCKED_PUBLIC_OR_CROSS_REPO_SHORTCUT",
            "stop",
            "Source checking a computation-side workload does not authorize public posture or cross-repo truth movement.",
        )
    if reading.claims_physics_mechanism:
        return ReadingDecision(
            reading.reading_id,
            False,
            "REJECTED_PHYSICS_MECHANISM_IMPORT",
            "reject",
            "N18 supports a computation-side retrieval workload only, not a physics mechanism.",
        )
    if reading.claims_naive_attention_quantum_copyability:
        return ReadingDecision(
            reading.reading_id,
            False,
            "REJECTED_NAIVE_COPYABILITY_REVIVAL",
            "reject",
            "Architecture retrieval/copying comparisons do not map to unknown quantum-state copyability.",
        )
    if reading.claims_complexity_theorem:
        return ReadingDecision(
            reading.reading_id,
            False,
            "REJECTED_THEOREM_IMPORT_SHORTCUT",
            "reject",
            "T497 source-checks theorem neighborhood but does not reproduce or prove the source theorem.",
        )
    if reading.uses_source_checked_retrieval_workload and reading.admits_composite_explanation:
        return ReadingDecision(
            reading.reading_id,
            True,
            "ADMITTED_COMPOSITE_ABSORBER_EXPLANATION",
            "record",
            "The stack explains native retention success plus arbitrary retrieval failure under bounded committed state.",
        )
    return ReadingDecision(
        reading.reading_id,
        False,
        "REJECTED_UNTYPED_READING",
        "reject",
        "The reading is outside the source-checked bounded retrieval stack.",
    )


def run() -> dict[str, Any]:
    evaluations = length_evaluations()
    decisions = tuple(decide_reading(reading) for reading in readings())
    all_expected = all(
        evaluation.factorizes == evaluation.expected_factorizes
        and evaluation.max_capability_spread == evaluation.expected_max_spread
        for evaluation in evaluations
    )
    source_payload = source_checks()
    direct_sources = tuple(
        source.source_id
        for source in source_payload
        if source.checked and source.supports_copying_retrieval_workload
    )

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "source_t495": SOURCE_T495,
        "source_t496": SOURCE_T496,
        "source_n18": SOURCE_N18,
        "source_progress_lanes": SOURCE_PROGRESS_LANES,
        "honest_ceiling": HONEST_CEILING,
        "source_checks": [asdict(source) for source in source_payload],
        "direct_copying_retrieval_sources": list(direct_sources),
        "absorber_stack": [asdict(absorber) for absorber in absorber_stack()],
        "length_evaluations": [asdict(evaluation) for evaluation in evaluations],
        "reading_decisions": [asdict(decision) for decision in decisions],
        "overall": {
            "all_length_checks_expected": all_expected,
            "source_checked_retrieval_workload": bool(direct_sources),
            "outcome": "COMPOSITE_ABSORBER_EXPLANATION",
            "review_target_only": True,
            "claim_movement": False,
            "public_posture_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "strongest_result": (
            "Across finite binary streams of length 2 through 8, full-history "
            "visibility factors arbitrary indexed retrieval, while last-2 "
            "committed state has growing arbitrary-retrieval spread once length "
            "exceeds 2 and still factors its native retained-suffix task. N18 "
            "source-checks copying/retrieval workload language for this "
            "computation lane, but T497 admits only composite absorber "
            "explanation and review-target status."
        ),
        "recommended_next": (
            "If the lane continues, build a theorem-facing packet that restates "
            "one checked copying/retrieval lower-bound theorem with its exact "
            "assumptions, then compare that theorem's state model to the T497 "
            "finite capability-spread fixture."
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    source_rows = [
        "| {source_id} | {checked} | {workload} | {caveat} | {allowed} |".format(
            source_id=source["source_id"],
            checked="yes" if source["checked"] else "no",
            workload="yes" if source["supports_copying_retrieval_workload"] else "no",
            caveat=source["blocks_overread"],
            allowed=source["allowed_use"],
        )
        for source in payload["source_checks"]
    ]
    absorber_rows = [
        "| {absorber_id} | {status} | {granted} | {effect} |".format(
            absorber_id=absorber["absorber_id"],
            status=absorber["status"],
            granted=absorber["granted_form"],
            effect=absorber["effect"],
        )
        for absorber in payload["absorber_stack"]
    ]
    length_rows = [
        "| {length} | {projection} | {capability} | {factorizes} | {spread} | {expected} | {label} |".format(
            length=evaluation["length"],
            projection=evaluation["projection_label"],
            capability=evaluation["capability_label"],
            factorizes="yes" if evaluation["factorizes"] else "no",
            spread=evaluation["max_capability_spread"],
            expected=evaluation["expected_max_spread"],
            label=evaluation["label"],
        )
        for evaluation in payload["length_evaluations"]
    ]
    reading_rows = [
        "| {reading_id} | {admitted} | {label} | {action} | {reason} |".format(
            reading_id=decision["reading_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            action=decision["action"],
            reason=decision["reason"],
        )
        for decision in payload["reading_decisions"]
    ]

    return "\n".join(
        [
            "# T497 - Bounded Retrieval Source-Checked Stack Gate - v0.1 results",
            "",
            "> Computation-lane composite explanation only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T497-bounded-retrieval-source-checked-stack-gate.md`",
            "- Model: `models/bounded_retrieval_source_checked_stack_gate.py`",
            "- Tests: `tests/test_bounded_retrieval_source_checked_stack_gate.py`",
            "- Source note: `literature/N18-bounded-retrieval-copying-lower-bound-sources.md`",
            "- Progress lanes: `open-problems/composite-absorber-stack-progress-lanes.md`",
            "- Artifact JSON: `results/T497-bounded-retrieval-source-checked-stack-gate-v0.1.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Source Checks",
            "",
            "| Source | Checked? | Supports retrieval workload? | Blocks overread | Allowed use |",
            "| --- | --- | --- | --- | --- |",
            *source_rows,
            "",
            "## Absorber Stack",
            "",
            "| Absorber | Status | Granted form | Effect |",
            "| --- | --- | --- | --- |",
            *absorber_rows,
            "",
            "## Finite Length Checks",
            "",
            "| Length | Projection | Capability | Factors? | Max spread | Expected spread | Label |",
            "| ---: | --- | --- | --- | ---: | ---: | --- |",
            *length_rows,
            "",
            "## Reading Decisions",
            "",
            "| Reading | Admitted? | Label | Action | Reason |",
            "| --- | --- | --- | --- | --- |",
            *reading_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: source-backed computation-lane composite explanation for why bounded committed summaries can preserve native retained tasks while losing arbitrary indexed retrieval.",
            "",
            "Does not earn: SSM/Transformer theorem proof, quantum copyability, physics mechanism, claim-ledger movement, public-posture movement, or cross-repo truth movement.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
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
        json_path = results_dir / "T497-bounded-retrieval-source-checked-stack-gate-v0.1.json"
        md_path = results_dir / "T497-bounded-retrieval-source-checked-stack-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
