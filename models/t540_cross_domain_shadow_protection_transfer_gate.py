"""T540: cross-domain shadow-protection transfer gate.

T539 routed the next swing to TAF8. T540 consumes the T492/T499/T501 ceilings
and asks whether the kappa and typed-gap catalogues already clear a reusable
cross-domain shadow-protection theorem burden without identity by construction.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import kappa_composite_residual_template_gate as t499
from models import typed_translation_object_identity_stack_gate as t501


ARTIFACT = "T540-cross-domain-shadow-protection-transfer-gate-v0.1"
VERDICT = "TAF8_TRANSFER_GATE_BUILT_CURRENT_CATALOGUES_SCAFFOLD_ONLY"
THEOREM_STATUS = "NOT_EARNED_CURRENT_CATALOGUES_NEED_NONIDENTITY_PACKET"
NEXT_PACKET = "T541_nonidentity_shadow_protection_witness_packet"

NOT_CLAIMED = (
    "T540 does not prove a cross-domain theorem, promote kappa, promote a "
    "typed-gap category theorem, move claim status, move Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, or move cross-repo truth. It is a TAF8 "
    "transfer-precondition gate only."
)


@dataclass(frozen=True)
class TransferCandidate:
    candidate_id: str
    description: str
    source_artifacts: tuple[str, ...]
    mature_lane_count: int
    shadow_capability_comparison_declared: bool
    same_proof_spine_declared: bool
    no_per_domain_retuning: bool
    positive_preservation_controls: bool
    negative_nonfactorization_fixtures: bool
    native_absorbers_granted: bool
    minimal_enrichment_or_demoter_named: bool
    kappa_nonidentity_burden_cleared: bool
    typed_gap_transfer_morphism_cleared: bool
    direct_spread_or_preservation_theorem: bool
    identity_by_construction: bool = False
    claim_movement_requested: bool = False
    public_posture_requested: bool = False
    external_publication_requested: bool = False
    cross_repo_truth_requested: bool = False


@dataclass(frozen=True)
class TransferDecision:
    candidate_id: str
    decision: str
    route_label: str
    scaffold_passes: bool
    theorem_preconditions_pass: bool
    blockers: tuple[str, ...]
    allowed_action: str


def evaluate_candidate(candidate: TransferCandidate) -> TransferDecision:
    blockers: list[str] = []

    if candidate.claim_movement_requested:
        blockers.append("claim_movement_requested")
    if candidate.public_posture_requested:
        blockers.append("public_posture_requested")
    if candidate.external_publication_requested:
        blockers.append("external_publication_requested")
    if candidate.cross_repo_truth_requested:
        blockers.append("cross_repo_truth_requested")

    if candidate.mature_lane_count < 2:
        blockers.append("fewer_than_two_mature_lanes")
    if not candidate.shadow_capability_comparison_declared:
        blockers.append("shadow_capability_comparison_missing")
    if not candidate.same_proof_spine_declared:
        blockers.append("same_proof_spine_missing")
    if not candidate.no_per_domain_retuning:
        blockers.append("per_domain_retuning")
    if not candidate.positive_preservation_controls:
        blockers.append("positive_preservation_controls_missing")
    if not candidate.negative_nonfactorization_fixtures:
        blockers.append("negative_nonfactorization_fixtures_missing")
    if not candidate.native_absorbers_granted:
        blockers.append("native_absorbers_not_granted")
    if not candidate.minimal_enrichment_or_demoter_named:
        blockers.append("minimal_enrichment_or_demoter_missing")

    if candidate.identity_by_construction:
        blockers.append("identity_by_construction")
    if not candidate.kappa_nonidentity_burden_cleared:
        blockers.append("kappa_nonidentity_burden_not_cleared")
    if not candidate.typed_gap_transfer_morphism_cleared:
        blockers.append("typed_gap_transfer_morphism_not_cleared")
    if not candidate.direct_spread_or_preservation_theorem:
        blockers.append("direct_spread_or_preservation_theorem_missing")

    forbidden = {
        "claim_movement_requested",
        "public_posture_requested",
        "external_publication_requested",
        "cross_repo_truth_requested",
    }
    scaffold_burden = {
        "fewer_than_two_mature_lanes",
        "shadow_capability_comparison_missing",
        "same_proof_spine_missing",
        "per_domain_retuning",
        "positive_preservation_controls_missing",
        "negative_nonfactorization_fixtures_missing",
        "native_absorbers_not_granted",
        "minimal_enrichment_or_demoter_missing",
    }
    blocker_set = set(blockers)
    scaffold_passes = not blocker_set.intersection(scaffold_burden)
    theorem_passes = scaffold_passes and not blockers

    if blocker_set.intersection(forbidden):
        return TransferDecision(
            candidate.candidate_id,
            "blocked",
            "FORBIDDEN_GOVERNANCE_OR_EXTERNAL_SHORTCUT",
            scaffold_passes,
            False,
            tuple(blockers),
            "record blocker only",
        )
    if "identity_by_construction" in blocker_set:
        return TransferDecision(
            candidate.candidate_id,
            "rejected",
            "IDENTITY_BY_CONSTRUCTION_BLOCKED",
            scaffold_passes,
            False,
            tuple(blockers),
            "reject same-object shortcut",
        )
    if theorem_passes:
        return TransferDecision(
            candidate.candidate_id,
            "admitted_future_review_target",
            "TAF8_THEOREM_PACKET_SHAPE_ONLY",
            True,
            True,
            (),
            "future review target only; no claim movement",
        )
    if scaffold_passes:
        return TransferDecision(
            candidate.candidate_id,
            "admitted_scaffold_only",
            "TRANSFER_SCAFFOLD_ONLY_THEOREM_BURDEN_OPEN",
            True,
            False,
            tuple(blockers),
            "use as TAF8 scaffold; build nonidentity packet next",
        )
    return TransferDecision(
        candidate.candidate_id,
        "not_admitted",
        "TRANSFER_SCAFFOLD_BURDEN_NOT_MET",
        False,
        False,
        tuple(blockers),
        "repair scaffold before theorem review",
    )


def source_summary(
    kappa_payload: dict[str, Any], typed_gap_payload: dict[str, Any]
) -> dict[str, Any]:
    current_typed_gap = typed_gap_payload["overall"]
    current_kappa = kappa_payload["overall"]
    return {
        "t499_verdict": kappa_payload["verdict"],
        "t501_verdict": typed_gap_payload["verdict"],
        "kappa_catalogue_method_template": current_kappa[
            "historical_kappa_catalogue_admitted_as_method_template"
        ],
        "kappa_synthetic_nonidentity_review_target": current_kappa[
            "synthetic_nonidentity_packet_admitted_for_review"
        ],
        "kappa_promotion_earned": current_kappa["kappa_promotion_earned"],
        "typed_gap_actual_interface_preserved": current_typed_gap[
            "actual_t92_t113_interface_preserved"
        ],
        "typed_gap_actual_object_identity_passes": current_typed_gap[
            "actual_t92_t113_object_identity_passes"
        ],
        "typed_gap_actual_direct_preservation_passes": current_typed_gap[
            "actual_t92_t113_direct_preservation_passes"
        ],
        "typed_gap_synthetic_exact_packet_review_target": current_typed_gap[
            "synthetic_exact_packet_admitted_for_review"
        ],
    }


def transfer_candidates(
    kappa_payload: dict[str, Any], typed_gap_payload: dict[str, Any]
) -> tuple[TransferCandidate, ...]:
    summary = source_summary(kappa_payload, typed_gap_payload)
    return (
        TransferCandidate(
            candidate_id="current_t499_t501_catalogue_pair",
            description=(
                "Current T499 kappa method-template lane plus current T501 "
                "typed-gap schema lane."
            ),
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT),
            mature_lane_count=2,
            shadow_capability_comparison_declared=True,
            same_proof_spine_declared=True,
            no_per_domain_retuning=True,
            positive_preservation_controls=True,
            negative_nonfactorization_fixtures=True,
            native_absorbers_granted=True,
            minimal_enrichment_or_demoter_named=True,
            kappa_nonidentity_burden_cleared=False,
            typed_gap_transfer_morphism_cleared=summary[
                "typed_gap_actual_object_identity_passes"
            ],
            direct_spread_or_preservation_theorem=summary[
                "typed_gap_actual_direct_preservation_passes"
            ],
        ),
        TransferCandidate(
            candidate_id="identity_by_construction_shortcut",
            description=(
                "A shortcut that treats shared schema or shared rank as same "
                "object identity."
            ),
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT),
            mature_lane_count=2,
            shadow_capability_comparison_declared=True,
            same_proof_spine_declared=True,
            no_per_domain_retuning=True,
            positive_preservation_controls=True,
            negative_nonfactorization_fixtures=True,
            native_absorbers_granted=True,
            minimal_enrichment_or_demoter_named=True,
            kappa_nonidentity_burden_cleared=True,
            typed_gap_transfer_morphism_cleared=True,
            direct_spread_or_preservation_theorem=True,
            identity_by_construction=True,
        ),
        TransferCandidate(
            candidate_id="retuned_domain_specific_pair",
            description=(
                "A pair that chooses a separate invariant or proof spine after "
                "seeing each domain."
            ),
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT),
            mature_lane_count=2,
            shadow_capability_comparison_declared=True,
            same_proof_spine_declared=False,
            no_per_domain_retuning=False,
            positive_preservation_controls=True,
            negative_nonfactorization_fixtures=True,
            native_absorbers_granted=True,
            minimal_enrichment_or_demoter_named=True,
            kappa_nonidentity_burden_cleared=True,
            typed_gap_transfer_morphism_cleared=True,
            direct_spread_or_preservation_theorem=True,
        ),
        TransferCandidate(
            candidate_id="missing_native_controls_pair",
            description=(
                "A pair that names two domains but omits positive controls, "
                "negative fixtures, or absorber completion."
            ),
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT),
            mature_lane_count=2,
            shadow_capability_comparison_declared=True,
            same_proof_spine_declared=True,
            no_per_domain_retuning=True,
            positive_preservation_controls=False,
            negative_nonfactorization_fixtures=False,
            native_absorbers_granted=False,
            minimal_enrichment_or_demoter_named=True,
            kappa_nonidentity_burden_cleared=True,
            typed_gap_transfer_morphism_cleared=True,
            direct_spread_or_preservation_theorem=True,
        ),
        TransferCandidate(
            candidate_id="synthetic_full_burden_pair",
            description=(
                "The future packet shape assembled from T499's synthetic "
                "nonidentity burden and T501's synthetic exact-object direct "
                "preservation burden."
            ),
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT),
            mature_lane_count=2,
            shadow_capability_comparison_declared=True,
            same_proof_spine_declared=True,
            no_per_domain_retuning=True,
            positive_preservation_controls=True,
            negative_nonfactorization_fixtures=True,
            native_absorbers_granted=True,
            minimal_enrichment_or_demoter_named=True,
            kappa_nonidentity_burden_cleared=summary[
                "kappa_synthetic_nonidentity_review_target"
            ],
            typed_gap_transfer_morphism_cleared=summary[
                "typed_gap_synthetic_exact_packet_review_target"
            ],
            direct_spread_or_preservation_theorem=True,
        ),
        TransferCandidate(
            candidate_id="claim_public_posture_shortcut",
            description=(
                "A structurally strong transfer packet that asks to move claims "
                "or public posture immediately."
            ),
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT),
            mature_lane_count=2,
            shadow_capability_comparison_declared=True,
            same_proof_spine_declared=True,
            no_per_domain_retuning=True,
            positive_preservation_controls=True,
            negative_nonfactorization_fixtures=True,
            native_absorbers_granted=True,
            minimal_enrichment_or_demoter_named=True,
            kappa_nonidentity_burden_cleared=True,
            typed_gap_transfer_morphism_cleared=True,
            direct_spread_or_preservation_theorem=True,
            claim_movement_requested=True,
            public_posture_requested=True,
        ),
    )


def run_t540_analysis() -> dict[str, Any]:
    kappa_payload = t499.run()
    typed_gap_payload = t501.run()
    candidates = transfer_candidates(kappa_payload, typed_gap_payload)
    decisions = tuple(evaluate_candidate(candidate) for candidate in candidates)
    current = next(
        decision
        for decision in decisions
        if decision.candidate_id == "current_t499_t501_catalogue_pair"
    )
    synthetic = next(
        decision
        for decision in decisions
        if decision.candidate_id == "synthetic_full_burden_pair"
    )
    source = source_summary(kappa_payload, typed_gap_payload)

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "theorem_status": THEOREM_STATUS,
        "sources": {
            "t492": "results/T492-typed-gap-category-bridge-v0.1-results.md",
            "t499": "results/T499-kappa-composite-residual-template-gate-v0.1-results.md",
            "t501": "results/T501-typed-translation-object-identity-stack-gate-v0.1-results.md",
            "taf8_open_problem": "open-problems/cross-domain-shadow-protection-theorem.md",
        },
        "source_summary": source,
        "transfer_preconditions": [
            "at least two mature lanes",
            "visible shadow, capability object, and native comparison declared",
            "same proof spine before domain-specific examples",
            "no per-domain retuning",
            "positive preservation controls and negative non-factorization fixtures",
            "native absorbers granted before residue is assigned",
            "minimal enrichment or honest demoter named",
            "no identity by construction",
            "kappa nonidentity burden cleared",
            "typed-gap transfer morphism or identity key cleared",
            "direct spread, factorization, or preservation theorem supplied",
            "no claim, canon, public-posture, external, or cross-repo movement",
        ],
        "candidates": [asdict(candidate) for candidate in candidates],
        "decisions": [asdict(decision) for decision in decisions],
        "overall": {
            "current_catalogue_scaffold_passes": current.scaffold_passes,
            "current_catalogue_theorem_preconditions_pass": (
                current.theorem_preconditions_pass
            ),
            "current_catalogue_blockers": list(current.blockers),
            "synthetic_full_burden_admitted_for_review": (
                synthetic.decision == "admitted_future_review_target"
            ),
            "claim_movement": False,
            "canon_movement": False,
            "public_posture_movement": False,
            "north_star_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "strongest_result": (
            "The kappa and typed-gap catalogues now share an executable TAF8 "
            "transfer scaffold: both can be read through shadow, capability "
            "comparison, native controls, absorber completion, and demotion "
            "discipline. The current catalogues still do not earn a theorem. "
            "T499 remains method-template only until nonidentity target "
            "burdens clear, and T501 remains schema-preservation only until a "
            "transfer morphism or identity key plus direct preservation theorem "
            "is supplied."
        ),
        "recommended_next": (
            f"Run {NEXT_PACKET}: instantiate one nonidentity kappa target and "
            "one typed-gap transfer target under the same predeclared "
            "shadow-protection spine, with native controls, absorber completion, "
            "and an explicit direct spread or preservation theorem. Keep it "
            "review-only unless the runnable artifact earns more."
        ),
        "claim_labels": [
            {
                "label": "COMPUTED",
                "confidence": "high",
                "text": (
                    "T499 and T501 are consumed as current ceilings: method "
                    "template and schema preservation, not theorem proof."
                ),
            },
            {
                "label": "COMPUTED",
                "confidence": "high",
                "text": (
                    "The current catalogue pair passes the TAF8 scaffold but "
                    "fails theorem preconditions on nonidentity and direct "
                    "preservation burdens."
                ),
            },
            {
                "label": "ARGUED",
                "confidence": "medium",
                "text": (
                    "TAF8 remains the best next lane because it now has a "
                    "specific executable burden rather than an open-ended "
                    "cross-domain aspiration."
                ),
            },
        ],
        "not_claimed": NOT_CLAIMED,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = [
        "# T540 Results: Cross-Domain Shadow-Protection Transfer Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Theorem status: `{payload['theorem_status']}`",
        "",
        "## Source Summary",
        "",
        "| Source fact | Value |",
        "| --- | --- |",
    ]
    for key, value in payload["source_summary"].items():
        lines.append(f"| `{key}` | `{value}` |")

    lines.extend(
        [
            "",
            "## Transfer Preconditions",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in payload["transfer_preconditions"])

    lines.extend(
        [
            "",
            "## Candidate Decisions",
            "",
            "| Candidate | Decision | Route | Scaffold? | Theorem preconditions? | Blockers | Allowed action |",
            "| --- | --- | --- | :---: | :---: | --- | --- |",
        ]
    )
    for decision in payload["decisions"]:
        blockers = ", ".join(decision["blockers"]) or "none"
        lines.append(
            "| `{candidate_id}` | `{decision}` | `{route_label}` | {scaffold} | "
            "{theorem} | {blockers} | {allowed_action} |".format(
                candidate_id=decision["candidate_id"],
                decision=decision["decision"],
                route_label=decision["route_label"],
                scaffold=decision["scaffold_passes"],
                theorem=decision["theorem_preconditions_pass"],
                blockers=blockers,
                allowed_action=decision["allowed_action"],
            )
        )

    lines.extend(
        [
            "",
            "## Strongest Result",
            "",
            payload["strongest_result"],
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
            "## Claim Labels",
            "",
        ]
    )
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    lines.extend(
        [
            "",
            "## Not Claimed",
            "",
            payload["not_claimed"],
            "",
        ]
    )
    return "\n".join(lines)


def write_results(
    payload: dict[str, Any], results_dir: Path = Path("results")
) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    json_path = results_dir / "T540-cross-domain-shadow-protection-transfer-gate-v0.1.json"
    md_path = (
        results_dir
        / "T540-cross-domain-shadow-protection-transfer-gate-v0.1-results.md"
    )
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    payload = run_t540_analysis()
    if args.write_results:
        write_results(payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
