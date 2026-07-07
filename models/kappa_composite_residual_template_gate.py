"""T499 - kappa composite-residual template gate.

The kappa catalogue is useful as a method template: one fixed invariant is
carried through several unrelated absorber genres without retuning, with native
target checks and falsifying controls. T465 and T466 also make the ceiling
explicit: this is not yet prediction-language, a genre-agnostic theorem, or
claim movement unless a future packet clears a non-identity target burden.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T499-kappa-composite-residual-template-gate-v0.1"
VERDICT = "KAPPA_COMPOSITE_TEMPLATE_GATE_BUILT_METHOD_ONLY_NO_PROMOTION"
SOURCE_PROGRESS_LANES = "open-problems/composite-absorber-stack-progress-lanes.md"
SOURCE_KAPPA_OPEN_PROBLEM = "open-problems/typed-loss-transport-test.md"
SOURCE_T465 = "tests/T465-ab-contextuality-kappa-absorber.md"
SOURCE_T466 = "tests/T466-post-t465-kappa-nonidentity-router.md"

HONEST_CEILING = (
    "T499 extracts a method template from the kappa line: fixed invariant, "
    "unrelated absorber genres, no retuning, native witnesses, falsifying "
    "controls, and rank load-bearing. It does not promote kappa, does not "
    "upgrade T224, does not assert prediction-language, and does not move "
    "claim ledger, roadmap, README, North Star, public posture, hard policy, "
    "external publication, or cross-repo truth."
)


@dataclass(frozen=True)
class KappaTemplatePacket:
    packet_id: str
    description: str
    same_invariant_fixed: bool
    absorber_count: int
    unrelated_genre_count: int
    no_per_domain_retuning: bool
    native_witnesses_declared: bool
    native_witnesses_independent: bool
    mismatch_or_negative_control: bool
    rank_load_bearing: bool
    source_rank_fixed_before_target: bool
    transport_map_predeclared: bool
    target_witness_nonidentity: bool
    synthetic_nu_not_written_from_native_rank: bool
    same_support_global_section_reencoding: bool
    claim_movement_requested: bool = False
    public_posture_requested: bool = False
    external_publication_requested: bool = False
    cross_repo_truth_requested: bool = False


@dataclass(frozen=True)
class PacketDecision:
    packet_id: str
    decision: str
    route_label: str
    core_template_passes: bool
    nonidentity_burden_passes: bool
    blockers: tuple[str, ...]
    allowed_action: str


def evaluate_packet(packet: KappaTemplatePacket) -> PacketDecision:
    blockers: list[str] = []

    if packet.claim_movement_requested:
        blockers.append("claim_movement_requested")
    if packet.public_posture_requested:
        blockers.append("public_posture_requested")
    if packet.external_publication_requested:
        blockers.append("external_publication_requested")
    if packet.cross_repo_truth_requested:
        blockers.append("cross_repo_truth_requested")

    if not packet.same_invariant_fixed:
        blockers.append("same_invariant_not_fixed")
    if packet.absorber_count < 2:
        blockers.append("fewer_than_two_absorbers")
    if packet.unrelated_genre_count < 2:
        blockers.append("fewer_than_two_unrelated_genres")
    if not packet.no_per_domain_retuning:
        blockers.append("per_domain_retuning")
    if not packet.native_witnesses_declared:
        blockers.append("native_witnesses_not_declared")
    if not packet.native_witnesses_independent:
        blockers.append("native_witnesses_not_independent")
    if not packet.mismatch_or_negative_control:
        blockers.append("no_falsifying_control")
    if not packet.rank_load_bearing:
        blockers.append("rank_not_load_bearing")

    if not packet.source_rank_fixed_before_target:
        blockers.append("source_rank_not_fixed_before_target")
    if not packet.transport_map_predeclared:
        blockers.append("transport_map_not_predeclared")
    if not packet.target_witness_nonidentity:
        blockers.append("target_witness_not_nonidentity")
    if not packet.synthetic_nu_not_written_from_native_rank:
        blockers.append("synthetic_nu_written_from_native_rank")
    if packet.same_support_global_section_reencoding:
        blockers.append("same_support_global_section_reencoding")

    forbidden = {
        "claim_movement_requested",
        "public_posture_requested",
        "external_publication_requested",
        "cross_repo_truth_requested",
    }
    core_burden = {
        "same_invariant_not_fixed",
        "fewer_than_two_absorbers",
        "fewer_than_two_unrelated_genres",
        "per_domain_retuning",
        "native_witnesses_not_declared",
        "native_witnesses_not_independent",
        "no_falsifying_control",
        "rank_not_load_bearing",
    }
    nonidentity_burden = {
        "source_rank_not_fixed_before_target",
        "transport_map_not_predeclared",
        "target_witness_not_nonidentity",
        "synthetic_nu_written_from_native_rank",
        "same_support_global_section_reencoding",
    }

    blocker_set = set(blockers)
    core_passes = not blocker_set.intersection(core_burden)
    nonidentity_passes = core_passes and not blocker_set.intersection(nonidentity_burden)

    if blocker_set.intersection(forbidden):
        decision = "blocked"
        route = "FORBIDDEN_GOVERNANCE_OR_EXTERNAL_SHORTCUT"
        allowed = "record blocker only"
    elif not core_passes:
        decision = "not_admitted"
        route = "CORE_KAPPA_TEMPLATE_BURDEN_NOT_MET"
        allowed = "repair method-template packet before review"
    elif nonidentity_passes:
        decision = "admitted_future_review_target"
        route = "NONIDENTITY_REVIEW_TARGET_ONLY"
        allowed = "future review target only; no claim movement"
    else:
        decision = "admitted_method_template_only"
        route = "STRUCTURAL_TEMPLATE_ONLY_T465_T466_CEILING"
        allowed = "use as method template; no prediction or promotion"

    return PacketDecision(
        packet_id=packet.packet_id,
        decision=decision,
        route_label=route,
        core_template_passes=core_passes,
        nonidentity_burden_passes=nonidentity_passes,
        blockers=tuple(blockers),
        allowed_action=allowed,
    )


def example_packets() -> tuple[KappaTemplatePacket, ...]:
    return (
        KappaTemplatePacket(
            packet_id="t224_t244_historical_kappa_catalogue",
            description=(
                "Historical kappa line across T224/T229/T234/T239/T244: fixed "
                "kappa object, multiple unrelated absorber genres, no retuning, "
                "native witnesses, controls, and rank load-bearing."
            ),
            same_invariant_fixed=True,
            absorber_count=5,
            unrelated_genre_count=4,
            no_per_domain_retuning=True,
            native_witnesses_declared=True,
            native_witnesses_independent=True,
            mismatch_or_negative_control=True,
            rank_load_bearing=True,
            source_rank_fixed_before_target=False,
            transport_map_predeclared=True,
            target_witness_nonidentity=False,
            synthetic_nu_not_written_from_native_rank=False,
            same_support_global_section_reencoding=False,
        ),
        KappaTemplatePacket(
            packet_id="t465_ab_contextuality_same_support",
            description=(
                "AB contextuality after T465: useful absorber, but native AB "
                "rank and kappa read the same support/global-section data."
            ),
            same_invariant_fixed=True,
            absorber_count=1,
            unrelated_genre_count=1,
            no_per_domain_retuning=True,
            native_witnesses_declared=True,
            native_witnesses_independent=True,
            mismatch_or_negative_control=True,
            rank_load_bearing=True,
            source_rank_fixed_before_target=True,
            transport_map_predeclared=True,
            target_witness_nonidentity=False,
            synthetic_nu_not_written_from_native_rank=True,
            same_support_global_section_reencoding=True,
        ),
        KappaTemplatePacket(
            packet_id="retuned_per_domain_packet",
            description="A packet that chooses a different invariant per absorber.",
            same_invariant_fixed=False,
            absorber_count=3,
            unrelated_genre_count=3,
            no_per_domain_retuning=False,
            native_witnesses_declared=True,
            native_witnesses_independent=True,
            mismatch_or_negative_control=True,
            rank_load_bearing=True,
            source_rank_fixed_before_target=True,
            transport_map_predeclared=True,
            target_witness_nonidentity=True,
            synthetic_nu_not_written_from_native_rank=True,
            same_support_global_section_reencoding=False,
        ),
        KappaTemplatePacket(
            packet_id="native_witness_missing_packet",
            description="A packet with absorber names but no native target witness checks.",
            same_invariant_fixed=True,
            absorber_count=3,
            unrelated_genre_count=3,
            no_per_domain_retuning=True,
            native_witnesses_declared=False,
            native_witnesses_independent=False,
            mismatch_or_negative_control=False,
            rank_load_bearing=True,
            source_rank_fixed_before_target=True,
            transport_map_predeclared=True,
            target_witness_nonidentity=True,
            synthetic_nu_not_written_from_native_rank=True,
            same_support_global_section_reencoding=False,
        ),
        KappaTemplatePacket(
            packet_id="t466_synthetic_nonidentity_packet",
            description=(
                "Synthetic future packet shape named by T466: independent source "
                "rank, predeclared map, independent non-identity native target "
                "witness, falsifying control, and rank load-bearing."
            ),
            same_invariant_fixed=True,
            absorber_count=3,
            unrelated_genre_count=3,
            no_per_domain_retuning=True,
            native_witnesses_declared=True,
            native_witnesses_independent=True,
            mismatch_or_negative_control=True,
            rank_load_bearing=True,
            source_rank_fixed_before_target=True,
            transport_map_predeclared=True,
            target_witness_nonidentity=True,
            synthetic_nu_not_written_from_native_rank=True,
            same_support_global_section_reencoding=False,
        ),
        KappaTemplatePacket(
            packet_id="claim_promotion_shortcut",
            description="A structurally strong packet that asks to promote kappa now.",
            same_invariant_fixed=True,
            absorber_count=3,
            unrelated_genre_count=3,
            no_per_domain_retuning=True,
            native_witnesses_declared=True,
            native_witnesses_independent=True,
            mismatch_or_negative_control=True,
            rank_load_bearing=True,
            source_rank_fixed_before_target=True,
            transport_map_predeclared=True,
            target_witness_nonidentity=True,
            synthetic_nu_not_written_from_native_rank=True,
            same_support_global_section_reencoding=False,
            claim_movement_requested=True,
        ),
    )


def template_minimum() -> tuple[str, ...]:
    return (
        "same invariant fixed across absorbers",
        "at least two unrelated absorber genres",
        "no per-domain retuning",
        "native target witnesses declared",
        "native target witnesses independent of the invariant implementation",
        "mismatch or negative control included",
        "rank, not only presence, is load-bearing",
        "T465/T466 ceiling retained: method template does not equal prediction",
        "non-identity promotion burden requires independent source rank and predeclared map",
        "review only; no claim movement from packet shape alone",
    )


def run() -> dict[str, Any]:
    packets = example_packets()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    admitted_method = [
        decision.packet_id
        for decision in decisions
        if decision.decision == "admitted_method_template_only"
    ]
    admitted_review = [
        decision.packet_id
        for decision in decisions
        if decision.decision == "admitted_future_review_target"
    ]

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "source_progress_lanes": SOURCE_PROGRESS_LANES,
        "source_kappa_open_problem": SOURCE_KAPPA_OPEN_PROBLEM,
        "source_t465": SOURCE_T465,
        "source_t466": SOURCE_T466,
        "honest_ceiling": HONEST_CEILING,
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "template_minimum": list(template_minimum()),
        "overall": {
            "historical_kappa_catalogue_admitted_as_method_template": (
                "t224_t244_historical_kappa_catalogue" in admitted_method
            ),
            "synthetic_nonidentity_packet_admitted_for_review": (
                "t466_synthetic_nonidentity_packet" in admitted_review
            ),
            "kappa_promotion_earned": False,
            "t224_upgrade_earned": False,
            "prediction_language_earned": False,
            "genre_agnostic_theorem_earned": False,
            "claim_movement": False,
            "roadmap_movement": False,
            "readme_movement": False,
            "north_star_movement": False,
            "public_posture_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "strongest_result": (
            "The T224-T244 kappa catalogue clears the core structural template "
            "for composite residual work: one invariant, multiple unrelated "
            "absorber genres, no retuning, native witnesses, controls, and "
            "rank load-bearing. T465/T466 still cap it at method-template "
            "status unless a future non-identity target witness clears the "
            "independent source-rank and predeclared-map burden."
        ),
        "recommended_next": (
            "Use T499 as a checklist when drafting future composite absorber "
            "packets. Do not cite the kappa line as prediction or a theorem "
            "unless the packet also clears the T466 non-identity burden."
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {packet_id} | {decision} | {route_label} | {core} | {nonidentity} | {blockers} |".format(
            packet_id=decision["packet_id"],
            decision=decision["decision"],
            route_label=decision["route_label"],
            core="yes" if decision["core_template_passes"] else "no",
            nonidentity="yes" if decision["nonidentity_burden_passes"] else "no",
            blockers=", ".join(decision["blockers"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    minimum = [f"- {item}" for item in payload["template_minimum"]]

    return "\n".join(
        [
            "# T499 - Kappa Composite Residual Template Gate - v0.1 results",
            "",
            "> Method-template result only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T499-kappa-composite-residual-template-gate.md`",
            "- Model: `models/kappa_composite_residual_template_gate.py`",
            "- Tests: `tests/test_kappa_composite_residual_template_gate.py`",
            "- Progress lanes: `open-problems/composite-absorber-stack-progress-lanes.md`",
            "- Kappa open problem: `open-problems/typed-loss-transport-test.md`",
            "- T465 absorber: `tests/T465-ab-contextuality-kappa-absorber.md`",
            "- T466 router: `tests/T466-post-t465-kappa-nonidentity-router.md`",
            "- Artifact JSON: `results/T499-kappa-composite-residual-template-gate-v0.1.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Packet Decisions",
            "",
            "| Packet | Decision | Route | Core template? | Nonidentity burden? | Blockers |",
            "| --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Template Minimum",
            "",
            *minimum,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable method-template gate for future composite absorber packets, using the kappa line as the structural model.",
            "",
            "Does not earn: kappa promotion, T224 upgrade, prediction-language, a genre-agnostic theorem, claim-ledger movement, roadmap movement, README movement, North Star movement, public-posture movement, external-publication permission, or cross-repo truth movement.",
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
        json_path = results_dir / "T499-kappa-composite-residual-template-gate-v0.1.json"
        md_path = results_dir / "T499-kappa-composite-residual-template-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
