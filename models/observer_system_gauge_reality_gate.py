"""T505: observer/system gauge reality gate.

The CT-3 correction in the boundary-adapter lane warns against a verificationist
overread: unobservability alone does not make a distinction mere gauge. This
module makes that guard executable. It separates proven equivalence/gauge from
unobservable-but-explanatory distinctions, and it routes the current
two-adapter de-correlation state as review material only.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T505-observer-system-gauge-reality-gate-v0.1"
VERDICT = "OBSERVER_SYSTEM_GAUGE_REALITY_GATE_BUILT_DINOSAUR_GUARD_REVIEW_ONLY"
SOURCE_EXPLORATION = (
    "explorations/physics-from-a-finite-observer-and-the-observer-system-gauge-2026-07-07.md"
)
SOURCE_OPEN_PROBLEM = "open-problems/boundary-adapter-as-functor-spec-2026-07-07.md"


@dataclass(frozen=True)
class RealityPacket:
    packet_id: str
    description: str
    packet_kind: str
    same_observable_total: bool
    proven_total_equivalence: bool
    reversible_translation_proved: bool
    explanation_requires_distinction: bool
    hard_to_vary_explanation: bool
    independent_forcing_count: int
    de_correlated_processes: bool
    shared_encoding_or_brief: bool
    shared_tunable_knob_found: bool
    falsifiable_disagreement_control: bool
    capability_bound_declared: bool
    constant_or_trivial_map: bool = False
    requests_claim_or_public_posture: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class RealityDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    genuine_gauge: bool
    unobservable_but_real_candidate: bool
    de_correlation_requirement_met: bool
    de_correlation_pending: bool
    current_adapter_state: bool
    counts_as_claim_evidence: bool
    missing_requirements: tuple[str, ...]
    reason: str


def run() -> dict[str, Any]:
    packets = packet_fixtures()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    by_id = {decision.packet_id: decision for decision in decisions}

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "source_exploration": SOURCE_EXPLORATION,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "objective": (
            "Turn the CT-3 dinosaur correction into a repo-local gate: proven "
            "equivalence may be treated as gauge, but mere unobservability may "
            "not. Boundary-adapter agreement remains review-only until the "
            "observer/system split is independently fixed without a shared "
            "manufactured-convergence knob."
        ),
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "overall": {
            "genuine_gauge_packets": [
                decision.packet_id for decision in decisions if decision.genuine_gauge
            ],
            "unobservable_but_real_candidates": [
                decision.packet_id
                for decision in decisions
                if decision.unobservable_but_real_candidate
            ],
            "verificationist_gauge_shortcut_rejected": (
                by_id["no_difference_only_gauge_shortcut"].label
                == "REJECTED_VERIFICATIONIST_GAUGE_SHORTCUT"
            ),
            "manufactured_convergence_rejected": (
                by_id["shared_knob_manufactured_convergence"].label
                == "REJECTED_MANUFACTURED_CONVERGENCE_RISK"
            ),
            "current_two_adapter_gate_closed": False,
            "current_two_adapter_state": by_id[
                "current_two_adapter_single_process"
            ].label,
            "de_correlation_pending": by_id[
                "current_two_adapter_single_process"
            ].de_correlation_pending,
            "future_decorrelated_packet_admitted_for_review": by_id[
                "future_decorrelated_two_adapter_packet"
            ].admitted,
            "review_target_only": True,
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
        },
        "future_decorrelation_minimum": future_decorrelation_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T505 builds a dinosaur guard for CT-3: a distinction may be "
            "gauge only after equivalence is proved, not merely because it is "
            "unobservable. Hidden or observer/system structure may be admitted "
            "as a review target when it is hard to vary and falsifiable. The "
            "current GU/TI/TaF two-adapter state is stronger than one adapter "
            "because two different forcing sources cohere, but it remains "
            "single-process, shared-encoding review material. De-correlation is "
            "pending; no identity, claim, public posture, or cross-repo truth "
            "movement is earned."
        ),
    }


def packet_fixtures() -> tuple[RealityPacket, ...]:
    return (
        RealityPacket(
            packet_id="coordinate_relabeling_equivalence",
            description=(
                "A calibration packet where all consequences are identical and "
                "a reversible translation is proved."
            ),
            packet_kind="gauge_calibration",
            same_observable_total=True,
            proven_total_equivalence=True,
            reversible_translation_proved=True,
            explanation_requires_distinction=False,
            hard_to_vary_explanation=False,
            independent_forcing_count=0,
            de_correlated_processes=False,
            shared_encoding_or_brief=False,
            shared_tunable_knob_found=False,
            falsifiable_disagreement_control=False,
            capability_bound_declared=False,
        ),
        RealityPacket(
            packet_id="no_difference_only_gauge_shortcut",
            description=(
                "Treats lack of direct observation as enough to call a split gauge."
            ),
            packet_kind="ct3_overread",
            same_observable_total=True,
            proven_total_equivalence=False,
            reversible_translation_proved=False,
            explanation_requires_distinction=False,
            hard_to_vary_explanation=False,
            independent_forcing_count=0,
            de_correlated_processes=False,
            shared_encoding_or_brief=True,
            shared_tunable_knob_found=False,
            falsifiable_disagreement_control=False,
            capability_bound_declared=False,
        ),
        RealityPacket(
            packet_id="dinosaur_hidden_cause_calibration",
            description=(
                "A hidden-cause calibration: direct perception is absent, but "
                "the explanation is hard to vary and has disagreement controls."
            ),
            packet_kind="hidden_reality_calibration",
            same_observable_total=True,
            proven_total_equivalence=False,
            reversible_translation_proved=False,
            explanation_requires_distinction=True,
            hard_to_vary_explanation=True,
            independent_forcing_count=1,
            de_correlated_processes=False,
            shared_encoding_or_brief=False,
            shared_tunable_knob_found=False,
            falsifiable_disagreement_control=True,
            capability_bound_declared=False,
        ),
        RealityPacket(
            packet_id="current_two_adapter_single_process",
            description=(
                "Current F/S adapter state: two source-forced signatures cohere, "
                "but they were built in one process and one D1 encoding."
            ),
            packet_kind="adapter_decorrelation",
            same_observable_total=True,
            proven_total_equivalence=False,
            reversible_translation_proved=False,
            explanation_requires_distinction=True,
            hard_to_vary_explanation=True,
            independent_forcing_count=2,
            de_correlated_processes=False,
            shared_encoding_or_brief=True,
            shared_tunable_knob_found=False,
            falsifiable_disagreement_control=True,
            capability_bound_declared=True,
        ),
        RealityPacket(
            packet_id="future_decorrelated_two_adapter_packet",
            description=(
                "Future target: the two adapters are fixed by separate processes "
                "with no shared brief or tunable observer/system split."
            ),
            packet_kind="adapter_decorrelation",
            same_observable_total=True,
            proven_total_equivalence=False,
            reversible_translation_proved=False,
            explanation_requires_distinction=True,
            hard_to_vary_explanation=True,
            independent_forcing_count=2,
            de_correlated_processes=True,
            shared_encoding_or_brief=False,
            shared_tunable_knob_found=False,
            falsifiable_disagreement_control=True,
            capability_bound_declared=True,
        ),
        RealityPacket(
            packet_id="constant_functor_convergence",
            description=(
                "A constant or trivial map that makes all adapters agree by collapse."
            ),
            packet_kind="adapter_decorrelation",
            same_observable_total=True,
            proven_total_equivalence=False,
            reversible_translation_proved=False,
            explanation_requires_distinction=False,
            hard_to_vary_explanation=False,
            independent_forcing_count=2,
            de_correlated_processes=False,
            shared_encoding_or_brief=True,
            shared_tunable_knob_found=True,
            falsifiable_disagreement_control=False,
            capability_bound_declared=False,
            constant_or_trivial_map=True,
        ),
        RealityPacket(
            packet_id="shared_knob_manufactured_convergence",
            description=(
                "Both sides agree only because a shared observer/system split knob "
                "was tuned after seeing the target."
            ),
            packet_kind="adapter_decorrelation",
            same_observable_total=True,
            proven_total_equivalence=False,
            reversible_translation_proved=False,
            explanation_requires_distinction=True,
            hard_to_vary_explanation=False,
            independent_forcing_count=2,
            de_correlated_processes=False,
            shared_encoding_or_brief=True,
            shared_tunable_knob_found=True,
            falsifiable_disagreement_control=False,
            capability_bound_declared=True,
        ),
        RealityPacket(
            packet_id="missing_hard_to_vary_burden",
            description=(
                "Claims hidden reality without a hard-to-vary explanation or a "
                "falsifiable disagreement control."
            ),
            packet_kind="hidden_reality_calibration",
            same_observable_total=True,
            proven_total_equivalence=False,
            reversible_translation_proved=False,
            explanation_requires_distinction=True,
            hard_to_vary_explanation=False,
            independent_forcing_count=1,
            de_correlated_processes=False,
            shared_encoding_or_brief=False,
            shared_tunable_knob_found=False,
            falsifiable_disagreement_control=False,
            capability_bound_declared=False,
        ),
        RealityPacket(
            packet_id="external_cross_repo_shortcut",
            description=(
                "Uses the gate to move public posture or cross-repo truth."
            ),
            packet_kind="adapter_decorrelation",
            same_observable_total=True,
            proven_total_equivalence=False,
            reversible_translation_proved=False,
            explanation_requires_distinction=True,
            hard_to_vary_explanation=True,
            independent_forcing_count=2,
            de_correlated_processes=True,
            shared_encoding_or_brief=False,
            shared_tunable_knob_found=False,
            falsifiable_disagreement_control=True,
            capability_bound_declared=True,
            requests_claim_or_public_posture=True,
            requests_external_publication=True,
            requests_cross_repo_truth=True,
        ),
    )


def evaluate_packet(packet: RealityPacket) -> RealityDecision:
    missing = missing_requirements(packet)

    if packet.requests_claim_or_public_posture:
        return _decision(
            packet,
            False,
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            "stop",
            False,
            False,
            False,
            False,
            missing,
            "This gate cannot move claims, public posture, or hard policy.",
        )
    if packet.requests_external_publication or packet.requests_cross_repo_truth:
        return _decision(
            packet,
            False,
            "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT",
            "stop",
            False,
            False,
            False,
            False,
            missing,
            "External publication and cross-repo truth movement are outside this run.",
        )
    if packet.constant_or_trivial_map:
        return _decision(
            packet,
            False,
            "REJECTED_TRIVIAL_OR_CONSTANT_CONVERGENCE",
            "reject",
            False,
            False,
            False,
            False,
            missing,
            "A constant or trivial map manufactures agreement and proves nothing.",
        )
    if packet.shared_tunable_knob_found:
        return _decision(
            packet,
            False,
            "REJECTED_MANUFACTURED_CONVERGENCE_RISK",
            "reject",
            False,
            False,
            False,
            False,
            missing,
            "A shared tunable observer/system split can manufacture the agreement.",
        )
    if packet.proven_total_equivalence and packet.reversible_translation_proved:
        return _decision(
            packet,
            False,
            "GENUINE_GAUGE_EQUIVALENCE_INVARIANT_ONLY",
            "treat_as_invariant",
            True,
            False,
            False,
            False,
            (),
            "Equivalence is proved; only invariant content may move.",
        )
    if packet.same_observable_total and not packet.explanation_requires_distinction:
        return _decision(
            packet,
            False,
            "REJECTED_VERIFICATIONIST_GAUGE_SHORTCUT",
            "reject",
            False,
            False,
            False,
            False,
            missing,
            "No observed difference is not enough to prove gauge equivalence.",
        )
    if missing:
        return _decision(
            packet,
            False,
            "REJECTED_MISSING_HARD_TO_VARY_BURDEN",
            "reject",
            False,
            False,
            False,
            False,
            missing,
            "The packet lacks the explanation, controls, or adapter de-correlation burden.",
        )
    if packet.packet_kind == "adapter_decorrelation" and not packet.de_correlated_processes:
        return _decision(
            packet,
            True,
            "ADMITTED_SINGLE_PROCESS_INDEPENDENT_FORCING_DECORRELATION_PENDING",
            "review_only",
            False,
            True,
            False,
            True,
            (),
            "Two forcing sources cohere, but shared process/encoding keeps de-correlation open.",
        )
    if packet.packet_kind == "adapter_decorrelation" and packet.de_correlated_processes:
        return _decision(
            packet,
            True,
            "ADMITTED_DECORRELATED_HARD_TO_VARY_REVIEW_TARGET",
            "review_only",
            False,
            True,
            True,
            False,
            (),
            "A future de-correlated packet may be reviewed, still without claim movement.",
        )
    return _decision(
        packet,
        True,
        "ADMITTED_UNOBSERVABLE_BUT_HARD_TO_VARY_REVIEW_TARGET",
        "review_only",
        False,
        True,
        False,
        False,
        (),
        "Unobservability is not gauge when a hard-to-vary explanation is load-bearing.",
    )


def missing_requirements(packet: RealityPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if packet.explanation_requires_distinction and not packet.hard_to_vary_explanation:
        missing.append("hard_to_vary_explanation")
    if packet.explanation_requires_distinction and not packet.falsifiable_disagreement_control:
        missing.append("falsifiable_disagreement_control")
    if packet.packet_kind == "adapter_decorrelation":
        if packet.independent_forcing_count < 2:
            missing.append("two_independent_forcing_sources")
        if not packet.capability_bound_declared:
            missing.append("capability_bound")
        if packet.de_correlated_processes and packet.shared_encoding_or_brief:
            missing.append("no_shared_encoding_or_brief")
    return tuple(missing)


def future_decorrelation_minimum() -> tuple[str, ...]:
    return (
        "prove equivalence before treating a distinction as gauge",
        "do not infer gauge from lack of direct observability",
        "name the hidden or observer/system distinction the explanation requires",
        "show the explanation is hard to vary rather than fitted after the fact",
        "include a falsifiable disagreement control",
        "for adapter closure, supply at least two independent forcing sources",
        "fix the observer/system split independently on each adapter",
        "exclude a shared tunable knob, shared brief, or trivial constant map",
        "declare the finite capability bound that fences observer-side burden",
        "keep admitted packets review-only until a runnable artifact earns a narrower update",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "observer/system split proved to be gauge",
        "observer/system split proved to be real",
        "GU/TI/TaF adapter identity",
        "two-adapter gate closure for the current single-process build",
        "real GU source category",
        "real TI source-category truth",
        "hard promotion",
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
    decision_rows = [
        "| {packet_id} | {admitted} | {label} | {gauge} | {real} | {met} | {pending} | {missing} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            gauge="yes" if decision["genuine_gauge"] else "no",
            real="yes" if decision["unobservable_but_real_candidate"] else "no",
            met="yes" if decision["de_correlation_requirement_met"] else "no",
            pending="yes" if decision["de_correlation_pending"] else "no",
            missing=", ".join(decision["missing_requirements"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    minimum = [f"- {item}" for item in payload["future_decorrelation_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T505 - Observer/System Gauge Reality Gate - v0.1 results",
            "",
            "> CT-3 dinosaur guard only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T505-observer-system-gauge-reality-gate.md`",
            "- Model: `models/observer_system_gauge_reality_gate.py`",
            "- Tests: `tests/test_observer_system_gauge_reality_gate.py`",
            f"- Source exploration: `{payload['source_exploration']}`",
            f"- Source open problem: `{payload['source_open_problem']}`",
            f"- Artifact JSON: `results/{ARTIFACT}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Genuine gauge? | Hidden/reality review? | De-correlation met? | De-correlation pending? | Missing requirements |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *decision_rows,
            "",
            "## Future De-correlation Minimum",
            "",
            *minimum,
            "",
            "## What This Does Not Earn",
            "",
            *blocked,
            "",
        ]
    )


def _decision(
    packet: RealityPacket,
    admitted: bool,
    label: str,
    action: str,
    genuine_gauge: bool,
    unobservable_but_real_candidate: bool,
    de_correlation_requirement_met: bool,
    de_correlation_pending: bool,
    missing_requirements: tuple[str, ...],
    reason: str,
) -> RealityDecision:
    return RealityDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        genuine_gauge=genuine_gauge,
        unobservable_but_real_candidate=unobservable_but_real_candidate,
        de_correlation_requirement_met=de_correlation_requirement_met,
        de_correlation_pending=de_correlation_pending,
        current_adapter_state=packet.packet_id == "current_two_adapter_single_process",
        counts_as_claim_evidence=False,
        missing_requirements=missing_requirements,
        reason=reason,
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
