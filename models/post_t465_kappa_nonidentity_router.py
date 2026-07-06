"""T466: Post-T465 kappa non-identity router.

T465 made the strongest AB contextuality objection executable: when the target
native witness is already the same support/global-section obstruction that
kappa reads, the result is re-encoding rather than prediction.

This module turns that lesson into a small admission router for future kappa
packets. It deliberately does not promote T224, CSP-PO1, or any kappa claim.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T466-post-t465-kappa-nonidentity-router-v0.1"
VERDICT = "POST_T465_KAPPA_NONIDENTITY_ROUTER_BUILT_NO_PROMOTION"


@dataclass(frozen=True)
class KappaPacketProposal:
    """A proposed post-T465 kappa packet shape."""

    proposal_id: str
    description: str
    source_kappa: int | None
    native_target_rank: int | None
    nu_kappa: int | None
    native_witness_kind: str
    target_witness_is_same_support_global_section_rank: bool = False
    synthetic_nu_written_from_native_rank: bool = False
    source_rank_independent_of_target_construction: bool = False
    native_witness_independent_of_compute_kappa: bool = True
    predeclared_mapping_before_target_measurement: bool = False
    has_mismatch_or_negative_control: bool = False
    no_shared_derivation_with_source: bool = True
    rank_load_bearing: bool = False
    claim_promotion_requested: bool = False
    public_posture_move_requested: bool = False
    cross_repo_truth_move_requested: bool = False


@dataclass(frozen=True)
class PacketEvaluation:
    """Router decision for one proposal."""

    proposal_id: str
    admitted_future_target: bool
    decision: str
    route_label: str
    blockers: tuple[str, ...]
    allowed_action: str


def evaluate_packet(proposal: KappaPacketProposal) -> PacketEvaluation:
    """Classify a proposed kappa packet under the post-T465 burden."""

    blockers: list[str] = []

    if proposal.claim_promotion_requested:
        blockers.append("claim_promotion_requested")
    if proposal.public_posture_move_requested:
        blockers.append("public_posture_move_requested")
    if proposal.cross_repo_truth_move_requested:
        blockers.append("cross_repo_truth_move_requested")
    if not proposal.no_shared_derivation_with_source:
        blockers.append("shared_derivation_with_source")
    if not proposal.native_witness_independent_of_compute_kappa:
        blockers.append("native_witness_calls_or_depends_on_compute_kappa")
    if proposal.target_witness_is_same_support_global_section_rank:
        blockers.append("same_support_global_section_rank_reencoding")
    if proposal.synthetic_nu_written_from_native_rank:
        blockers.append("synthetic_nu_written_from_native_rank")
    if not proposal.source_rank_independent_of_target_construction:
        blockers.append("source_rank_not_independent_of_target_construction")
    if not proposal.predeclared_mapping_before_target_measurement:
        blockers.append("mapping_not_predeclared_before_target_measurement")
    if not proposal.has_mismatch_or_negative_control:
        blockers.append("no_mismatch_or_negative_control")
    if not proposal.rank_load_bearing:
        blockers.append("rank_not_load_bearing")

    forbidden = {
        "claim_promotion_requested",
        "public_posture_move_requested",
        "cross_repo_truth_move_requested",
    }
    if forbidden.intersection(blockers):
        decision = "blocked"
        route = "FORBIDDEN_POSTURE_OR_CLAIM_MOVE"
        allowed = "record blocker only"
    elif "same_support_global_section_rank_reencoding" in blockers:
        decision = "not_admitted"
        route = "T465_ABSORBER_REENCODING_NOT_PREDICTION"
        allowed = "use as absorber or guardrail only"
    elif "synthetic_nu_written_from_native_rank" in blockers:
        decision = "not_admitted"
        route = "FINITE_REENCODING_CATALOGUE_HELD_NO_PROMOTION"
        allowed = "catalogue evidence only"
    elif "shared_derivation_with_source" in blockers:
        decision = "not_admitted"
        route = "SHARED_DERIVATION_SHORTCUT"
        allowed = "route away before kappa review"
    elif "native_witness_calls_or_depends_on_compute_kappa" in blockers:
        decision = "not_admitted"
        route = "NATIVE_WITNESS_NOT_INDEPENDENT"
        allowed = "repair native witness before review"
    elif blockers:
        decision = "not_admitted"
        route = "NONIDENTITY_BURDEN_NOT_MET"
        allowed = "repair packet shape before review"
    else:
        decision = "admitted_for_review"
        route = "SYNTHETIC_NONIDENTITY_REVIEW_TARGET_ONLY"
        allowed = "future review target only; no claim movement"

    return PacketEvaluation(
        proposal_id=proposal.proposal_id,
        admitted_future_target=decision == "admitted_for_review",
        decision=decision,
        route_label=route,
        blockers=tuple(blockers),
        allowed_action=allowed,
    )


def example_proposals() -> tuple[KappaPacketProposal, ...]:
    """Representative current and synthetic packet classes."""

    return (
        KappaPacketProposal(
            proposal_id="current_t224_t244_catalogue",
            description=(
                "Existing finite kappa catalogue where source k, native target "
                "rank, and synthetic nu rank are paired by construction."
            ),
            source_kappa=3,
            native_target_rank=3,
            nu_kappa=3,
            native_witness_kind="finite re-encoding catalogue",
            synthetic_nu_written_from_native_rank=True,
            native_witness_independent_of_compute_kappa=True,
            has_mismatch_or_negative_control=True,
            no_shared_derivation_with_source=True,
            rank_load_bearing=True,
            predeclared_mapping_before_target_measurement=True,
        ),
        KappaPacketProposal(
            proposal_id="ab_contextuality_after_t465",
            description=(
                "AB support-table contextuality where the native target witness "
                "is already the same local-section/global-section obstruction."
            ),
            source_kappa=2,
            native_target_rank=2,
            nu_kappa=2,
            native_witness_kind="AB support/global-section rank",
            target_witness_is_same_support_global_section_rank=True,
            native_witness_independent_of_compute_kappa=True,
            source_rank_independent_of_target_construction=True,
            predeclared_mapping_before_target_measurement=True,
            has_mismatch_or_negative_control=True,
            no_shared_derivation_with_source=True,
            rank_load_bearing=True,
        ),
        KappaPacketProposal(
            proposal_id="integer_echo_without_falsifier",
            description=(
                "A paired fixture that writes the same integer into source, "
                "native target, and nu, but has no mismatch branch."
            ),
            source_kappa=1,
            native_target_rank=1,
            nu_kappa=1,
            native_witness_kind="paired integer echo",
            synthetic_nu_written_from_native_rank=True,
            source_rank_independent_of_target_construction=False,
            predeclared_mapping_before_target_measurement=True,
            has_mismatch_or_negative_control=False,
            no_shared_derivation_with_source=True,
            rank_load_bearing=False,
        ),
        KappaPacketProposal(
            proposal_id="shared_derivation_cap_shortcut",
            description="A CAP-shaped shortcut that routes through the source engine.",
            source_kappa=1,
            native_target_rank=1,
            nu_kappa=1,
            native_witness_kind="shared source-derived witness",
            source_rank_independent_of_target_construction=True,
            predeclared_mapping_before_target_measurement=True,
            has_mismatch_or_negative_control=True,
            no_shared_derivation_with_source=False,
            rank_load_bearing=True,
        ),
        KappaPacketProposal(
            proposal_id="native_witness_calls_kappa",
            description="A target whose native witness directly calls kappa.",
            source_kappa=1,
            native_target_rank=1,
            nu_kappa=1,
            native_witness_kind="native witness dependent on compute_kappa",
            source_rank_independent_of_target_construction=True,
            native_witness_independent_of_compute_kappa=False,
            predeclared_mapping_before_target_measurement=True,
            has_mismatch_or_negative_control=True,
            no_shared_derivation_with_source=True,
            rank_load_bearing=True,
        ),
        KappaPacketProposal(
            proposal_id="presence_only_packet",
            description="A packet that only distinguishes obstruction presence.",
            source_kappa=1,
            native_target_rank=1,
            nu_kappa=1,
            native_witness_kind="presence-only target",
            source_rank_independent_of_target_construction=True,
            predeclared_mapping_before_target_measurement=True,
            has_mismatch_or_negative_control=True,
            no_shared_derivation_with_source=True,
            rank_load_bearing=False,
        ),
        KappaPacketProposal(
            proposal_id="claim_promotion_shortcut",
            description="A packet that asks to promote T224 immediately.",
            source_kappa=2,
            native_target_rank=2,
            nu_kappa=2,
            native_witness_kind="promotion shortcut",
            source_rank_independent_of_target_construction=True,
            predeclared_mapping_before_target_measurement=True,
            has_mismatch_or_negative_control=True,
            no_shared_derivation_with_source=True,
            rank_load_bearing=True,
            claim_promotion_requested=True,
        ),
        KappaPacketProposal(
            proposal_id="synthetic_future_nonidentity_packet",
            description=(
                "A future-review packet shape with an independently fixed source "
                "rank, a predeclared transport map, an independent native target "
                "witness not identical to support/global-section rank, mismatch "
                "controls, no shared derivation, and rank load-bearing."
            ),
            source_kappa=2,
            native_target_rank=2,
            nu_kappa=2,
            native_witness_kind="non-identity target-side witness",
            target_witness_is_same_support_global_section_rank=False,
            synthetic_nu_written_from_native_rank=False,
            source_rank_independent_of_target_construction=True,
            native_witness_independent_of_compute_kappa=True,
            predeclared_mapping_before_target_measurement=True,
            has_mismatch_or_negative_control=True,
            no_shared_derivation_with_source=True,
            rank_load_bearing=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T466 admission router."""

    proposals = example_proposals()
    evaluations = tuple(evaluate_packet(proposal) for proposal in proposals)
    admitted = tuple(
        evaluation.proposal_id
        for evaluation in evaluations
        if evaluation.admitted_future_target
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Make the post-T465 kappa non-identity burden executable without "
            "claim movement."
        ),
        "proposals": [_proposal_dict(proposal) for proposal in proposals],
        "evaluations": [_evaluation_dict(evaluation) for evaluation in evaluations],
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_future_target_ids": list(admitted),
            "admitted_targets_are_synthetic_only": True,
            "current_catalogue_promoted": False,
            "t224_promotion_earned": False,
            "genre_agnostic_theorem_earned": False,
            "claim_ledger_update": "none",
            "reading": (
                "T224/T229/T234/T239/T244 remain a finite re-encoding catalogue; "
                "T465 blocks AB prediction-language; future kappa promotion "
                "requires a non-identity native target witness with a falsifying "
                "branch and independent source rank."
            ),
        },
        "not_earned": [
            "T224 promotion",
            "CSP-PO1 promotion",
            "prediction-language",
            "genre-agnostic theorem",
            "physics or quantum prediction",
            "claim-ledger movement",
            "public-posture movement",
        ],
        "future_packet_minimum": [
            "source rank fixed independently before target construction",
            "transport map predeclared before target measurement",
            "target native witness independent of compute_kappa",
            "target native witness not identical to same support/global-section rank",
            "synthetic nu not written from the native rank by construction",
            "mismatch or negative control included",
            "rank, not only presence, load-bearing",
            "no shared derivation with the source engine",
            "review only; no claim movement from packet shape alone",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Render the result as a compact Markdown artifact."""

    verdict = result["overall_verdict"]
    rows = []
    for evaluation in result["evaluations"]:
        blockers = ", ".join(evaluation["blockers"]) or "none"
        rows.append(
            "| {proposal_id} | {decision} | {route_label} | {blockers} |".format(
                proposal_id=evaluation["proposal_id"],
                decision=evaluation["decision"],
                route_label=evaluation["route_label"],
                blockers=blockers,
            )
        )

    not_earned = [f"- {item}" for item in result["not_earned"]]
    minimum = [f"- {item}" for item in result["future_packet_minimum"]]

    return "\n".join(
        [
            "# T466 - Post-T465 Kappa Non-Identity Router - v0.1 results",
            "",
            "> Admission/router guard only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T466-post-t465-kappa-nonidentity-router.md`",
            "- Model: `models/post_t465_kappa_nonidentity_router.py`",
            "- Tests: `tests/test_post_t465_kappa_nonidentity_router.py`",
            "- Artifact JSON: `results/T466-post-t465-kappa-nonidentity-router-v0.1.json`",
            "- Sources: T224/T229/T234/T239/T244 finite kappa catalogue and T465 AB absorber",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Router Table",
            "",
            "| proposal | decision | route | blockers |",
            "| --- | --- | --- | --- |",
            *rows,
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


def _proposal_dict(proposal: KappaPacketProposal) -> dict[str, Any]:
    return {
        "proposal_id": proposal.proposal_id,
        "description": proposal.description,
        "source_kappa": proposal.source_kappa,
        "native_target_rank": proposal.native_target_rank,
        "nu_kappa": proposal.nu_kappa,
        "native_witness_kind": proposal.native_witness_kind,
        "target_witness_is_same_support_global_section_rank": (
            proposal.target_witness_is_same_support_global_section_rank
        ),
        "synthetic_nu_written_from_native_rank": (
            proposal.synthetic_nu_written_from_native_rank
        ),
        "source_rank_independent_of_target_construction": (
            proposal.source_rank_independent_of_target_construction
        ),
        "native_witness_independent_of_compute_kappa": (
            proposal.native_witness_independent_of_compute_kappa
        ),
        "predeclared_mapping_before_target_measurement": (
            proposal.predeclared_mapping_before_target_measurement
        ),
        "has_mismatch_or_negative_control": proposal.has_mismatch_or_negative_control,
        "no_shared_derivation_with_source": proposal.no_shared_derivation_with_source,
        "rank_load_bearing": proposal.rank_load_bearing,
        "claim_promotion_requested": proposal.claim_promotion_requested,
        "public_posture_move_requested": proposal.public_posture_move_requested,
        "cross_repo_truth_move_requested": proposal.cross_repo_truth_move_requested,
    }


def _evaluation_dict(evaluation: PacketEvaluation) -> dict[str, Any]:
    return {
        "proposal_id": evaluation.proposal_id,
        "admitted_future_target": evaluation.admitted_future_target,
        "decision": evaluation.decision,
        "route_label": evaluation.route_label,
        "blockers": list(evaluation.blockers),
        "allowed_action": evaluation.allowed_action,
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
