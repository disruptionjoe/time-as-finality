"""T456 - policy-invariant region theorem gate.

T455 preserved T454 only as a finite integrated review target. This gate turns
T455's blockers into an executable admission screen for any future stronger
Direction-A packet.

The result is intentionally conservative: current T454/T455 is not admitted for
stronger posture because description completion, reference-policy fragility, and
the no-new-theorem objection still fire. Only a synthetic future theorem packet
passes, and that pass is a target shape rather than a claim promotion.

Run:

    python -m models.policy_invariant_region_theorem_gate --write-results
    python -m pytest tests/test_policy_invariant_region_theorem_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import t454_hostile_review_gate as t455


ARTIFACT = "T456-policy-invariant-region-theorem-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T447 = "results/T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md"
SOURCE_T452 = "results/T452-law-sector-nonadmissibility-gate-v0.1-results.md"
SOURCE_T453 = "results/T453-e3-to-region-nonadmissibility-adapter-gate-v0.1-results.md"
SOURCE_T454 = "results/T454-integrated-e3-region-packet-swing-v0.1-results.md"
SOURCE_T455 = "results/T455-t454-hostile-review-gate-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "POLICY_INVARIANT_REGION_THEOREM_GATE_BUILT_CURRENT_T454_NOT_ADMITTED"

HONEST_CEILING = (
    "Admission gate only. T456 converts T455's hostile objections into the next "
    "Direction-A screen: a stronger packet must make the boundary resource fail "
    "description completion, remain invariant under or independently preclude "
    "cyclic/consumed/ideal reference policies, and supply a policy-independent "
    "region theorem. It does not prove a region-indexed discriminator, real "
    "substrate law, quantum physics theorem, WAY theorem, GU/TaF adapter, claim "
    "support, or public posture."
)


@dataclass(frozen=True)
class TheoremPacketCandidate:
    candidate_id: str
    description: str
    source: str
    has_region_packet: bool
    t455_mechanical_review_survives: bool
    exact_witness_tied_to_named_completion: bool
    law_sector_description_factorizes: bool
    reference_policy_variants_precluded: bool
    reference_policy_variants_preserve_split: bool
    policy_independent_region_theorem_supplied: bool
    operation_resource_class_frozen: bool = True
    a2_resource_lift_audited: bool = True
    negative_control_present: bool = True
    declared_before_pair: bool = True
    reads_hidden_label_or_case_id: bool = False
    requests_external_posture: bool = False
    synthetic_control_only: bool = False


def _candidate_to_dict(candidate: TheoremPacketCandidate) -> dict[str, Any]:
    return asdict(candidate)


def _hostile_objection(review: dict[str, Any], check_id: str) -> dict[str, Any]:
    return next(
        item for item in review["hostile_objections"] if item["check_id"] == check_id
    )


def _survival_check(review: dict[str, Any], check_id: str) -> dict[str, Any]:
    return next(
        item for item in review["survival_checks"] if item["check_id"] == check_id
    )


def _t455_summary() -> dict[str, Any]:
    review = t455.run()
    return {
        "verdict": review["overall_verdict"]["verdict"],
        "t454_survives_as_review_target": review["overall_verdict"][
            "t454_survives_as_review_target"
        ],
        "region_packet_mechanical_correctness": _survival_check(
            review, "region_packet_mechanical_correctness"
        )["passed"],
        "exact_witness_tied_to_named_completion": _survival_check(
            review, "exact_witness_tied_to_named_completion"
        )["passed"],
        "controls_keep_scope_narrow": _survival_check(
            review, "negative_controls_keep_scope_narrow"
        )["passed"],
        "description_objection_fires": _hostile_objection(
            review, "law_sector_description_absorber_still_fires"
        )["status"]
        == "FIRES",
        "reference_policy_objection_fires": _hostile_objection(
            review, "reference_policy_fragility_still_fires"
        )["status"]
        == "FIRES",
        "no_new_theorem_objection_fires": _hostile_objection(
            review, "no_new_region_theorem_beyond_integration"
        )["status"]
        == "FIRES",
        "stronger_posture_earned": review["overall_verdict"][
            "stronger_direction_a_posture_earned"
        ],
    }


def _reference_policy_invariant(candidate: TheoremPacketCandidate) -> bool:
    return (
        candidate.reference_policy_variants_precluded
        or candidate.reference_policy_variants_preserve_split
    )


def requirement_audit(candidate: TheoremPacketCandidate) -> dict[str, bool]:
    return {
        "region_packet_present": candidate.has_region_packet,
        "t455_mechanical_review_survives": candidate.t455_mechanical_review_survives,
        "exact_witness_tied_to_named_completion": (
            candidate.exact_witness_tied_to_named_completion
        ),
        "description_nonfactorization": (
            not candidate.law_sector_description_factorizes
        ),
        "reference_policy_invariance": _reference_policy_invariant(candidate),
        "policy_independent_region_theorem": (
            candidate.policy_independent_region_theorem_supplied
        ),
        "operation_resource_class_frozen": (
            candidate.operation_resource_class_frozen
        ),
        "a2_resource_lift_audited": candidate.a2_resource_lift_audited,
        "negative_control_present": candidate.negative_control_present,
        "declared_before_pair": candidate.declared_before_pair,
        "no_hidden_label_or_case_id": (
            not candidate.reads_hidden_label_or_case_id
        ),
        "no_external_posture_request": not candidate.requests_external_posture,
    }


def evaluate_candidate(candidate: TheoremPacketCandidate) -> dict[str, Any]:
    requirements = requirement_audit(candidate)
    missing = [key for key, value in requirements.items() if value is False]
    admitted = False

    if candidate.requests_external_posture:
        label = "BLOCKED_EXTERNAL_OR_PUBLIC_POSTURE_REQUEST"
        reason = "External/public posture movement is outside this repo-local gate."
    elif candidate.reads_hidden_label_or_case_id:
        label = "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
        reason = "The packet reads a hidden selector instead of a region theorem."
    elif not candidate.declared_before_pair:
        label = "BLOCKED_POST_HOC_PACKET"
        reason = "The theorem packet must be declared before pair selection."
    elif not candidate.has_region_packet:
        label = "NOT_ADMITTED_NO_REGION_PACKET"
        reason = "An exact no-go alone is not a region-indexed packet."
    elif not candidate.t455_mechanical_review_survives:
        label = "NOT_ADMITTED_T455_MECHANICAL_REVIEW_FAILED"
        reason = "The packet must first survive T455-style mechanical review."
    elif {
        "description_nonfactorization",
        "reference_policy_invariance",
        "policy_independent_region_theorem",
    }.issubset(set(missing)):
        label = "NOT_ADMITTED_DESCRIPTION_POLICY_THEOREM_BLOCKS"
        reason = (
            "Current T454/T455 still factors through law-sector description, "
            "depends on the finite non-wrapping reference policy, and supplies no "
            "policy-independent region theorem."
        )
    elif not requirements["description_nonfactorization"]:
        label = "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"
        reason = "Capability still factors through an admitted boundary-resource description."
    elif not requirements["reference_policy_invariance"]:
        label = "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
        reason = (
            "Cyclic, consumed, or ideal reference variants restore completion or "
            "route away from the declared finite exact packet."
        )
    elif not requirements["policy_independent_region_theorem"]:
        label = "NOT_ADMITTED_NO_POLICY_INDEPENDENT_REGION_THEOREM"
        reason = "The packet integrates existing pieces but supplies no new region theorem."
    elif not candidate.operation_resource_class_frozen:
        label = "NOT_ADMITTED_OPERATION_RESOURCE_CLASS_UNFROZEN"
        reason = "The operation/resource class must be frozen before scoring."
    elif not candidate.a2_resource_lift_audited:
        label = "NOT_ADMITTED_A2_RESOURCE_LIFT_UNAUDITED"
        reason = "A2 reference/resource completion must be audited."
    elif not candidate.negative_control_present:
        label = "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
        reason = "A nearby negative control is required."
    else:
        admitted = True
        label = "ADMITTED_POLICY_INVARIANT_REGION_THEOREM_TARGET_NO_PROMOTION"
        reason = (
            "The candidate supplies the future target shape: T455-style survival, "
            "description nonfactorization, reference-policy invariance or "
            "preclusion, a policy-independent region theorem, frozen operations, "
            "A2 audit, and controls."
        )

    return {
        "candidate_id": candidate.candidate_id,
        "description": candidate.description,
        "source": candidate.source,
        "candidate": _candidate_to_dict(candidate),
        "requirement_audit": requirements,
        "missing_requirements": missing,
        "admitted_future_target": admitted,
        "gate_label": label,
        "reason": reason,
    }


def candidates() -> tuple[TheoremPacketCandidate, ...]:
    summary = _t455_summary()
    t455_survives = bool(summary["t454_survives_as_review_target"])
    exact_tied = bool(summary["exact_witness_tied_to_named_completion"])

    return (
        TheoremPacketCandidate(
            candidate_id="current_t454_t455_review_target",
            description=(
                "The currently landed T454 packet after T455 hostile review, "
                "considered for a stronger Direction-A posture move."
            ),
            source=SOURCE_T455,
            has_region_packet=True,
            t455_mechanical_review_survives=t455_survives,
            exact_witness_tied_to_named_completion=exact_tied,
            law_sector_description_factorizes=summary[
                "description_objection_fires"
            ],
            reference_policy_variants_precluded=False,
            reference_policy_variants_preserve_split=False,
            policy_independent_region_theorem_supplied=not summary[
                "no_new_theorem_objection_fires"
            ],
        ),
        TheoremPacketCandidate(
            candidate_id="bare_t447_exact_no_go_control",
            description=(
                "T447's finite non-wrapping exact no-go without any region packet."
            ),
            source=SOURCE_T447,
            has_region_packet=False,
            t455_mechanical_review_survives=False,
            exact_witness_tied_to_named_completion=True,
            law_sector_description_factorizes=False,
            reference_policy_variants_precluded=False,
            reference_policy_variants_preserve_split=False,
            policy_independent_region_theorem_supplied=False,
        ),
        TheoremPacketCandidate(
            candidate_id="description_completion_control",
            description=(
                "A packet whose boundary descriptor is admitted and therefore "
                "explains the capability split."
            ),
            source=SOURCE_T454,
            has_region_packet=True,
            t455_mechanical_review_survives=True,
            exact_witness_tied_to_named_completion=False,
            law_sector_description_factorizes=True,
            reference_policy_variants_precluded=True,
            reference_policy_variants_preserve_split=False,
            policy_independent_region_theorem_supplied=False,
        ),
        TheoremPacketCandidate(
            candidate_id="reference_policy_variant_control",
            description=(
                "A packet that works only for finite non-wrapping references while "
                "cyclic, consumed, or ideal variants restore or reroute completion."
            ),
            source=SOURCE_T455,
            has_region_packet=True,
            t455_mechanical_review_survives=True,
            exact_witness_tied_to_named_completion=True,
            law_sector_description_factorizes=False,
            reference_policy_variants_precluded=False,
            reference_policy_variants_preserve_split=False,
            policy_independent_region_theorem_supplied=True,
        ),
        TheoremPacketCandidate(
            candidate_id="integration_without_region_theorem_control",
            description=(
                "A packet that correctly integrates a region pair with an exact "
                "witness but supplies no policy-independent theorem."
            ),
            source=SOURCE_T454,
            has_region_packet=True,
            t455_mechanical_review_survives=True,
            exact_witness_tied_to_named_completion=True,
            law_sector_description_factorizes=False,
            reference_policy_variants_precluded=True,
            reference_policy_variants_preserve_split=False,
            policy_independent_region_theorem_supplied=False,
        ),
        TheoremPacketCandidate(
            candidate_id="synthetic_policy_invariant_region_theorem_packet",
            description=(
                "Synthetic calibration target: a future packet with a region pair, "
                "description nonfactorization, reference-policy invariance or "
                "independent preclusion, and a policy-independent theorem."
            ),
            source=ARTIFACT,
            has_region_packet=True,
            t455_mechanical_review_survives=True,
            exact_witness_tied_to_named_completion=True,
            law_sector_description_factorizes=False,
            reference_policy_variants_precluded=True,
            reference_policy_variants_preserve_split=True,
            policy_independent_region_theorem_supplied=True,
            synthetic_control_only=True,
        ),
        TheoremPacketCandidate(
            candidate_id="synthetic_missing_negative_control",
            description="A nearby synthetic future packet missing its negative control.",
            source=ARTIFACT,
            has_region_packet=True,
            t455_mechanical_review_survives=True,
            exact_witness_tied_to_named_completion=True,
            law_sector_description_factorizes=False,
            reference_policy_variants_precluded=True,
            reference_policy_variants_preserve_split=True,
            policy_independent_region_theorem_supplied=True,
            negative_control_present=False,
            synthetic_control_only=True,
        ),
    )


def run() -> dict[str, Any]:
    summary = _t455_summary()
    evaluations = [evaluate_candidate(candidate) for candidate in candidates()]
    admitted = [item for item in evaluations if item["admitted_future_target"]]
    current = next(
        item
        for item in evaluations
        if item["candidate_id"] == "current_t454_t455_review_target"
    )

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t447": SOURCE_T447,
            "t452": SOURCE_T452,
            "t453": SOURCE_T453,
            "t454": SOURCE_T454,
            "t455": SOURCE_T455,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Convert T455's hostile objections into an admission gate for any "
            "future policy-invariant region theorem packet."
        ),
        "t455_import_summary": summary,
        "admission_requirements": [
            "survive T455-style mechanical review",
            "tie the exact witness to the named completion",
            "make the boundary-resource completion fail description factorization",
            "remain invariant under or independently preclude cyclic, consumed, and ideal reference policies",
            "supply a policy-independent region theorem beyond packet integration",
            "freeze operation/resource class before pair selection",
            "audit A2 reference/resource lift",
            "include a nearby negative control",
            "avoid hidden labels, post-hoc selectors, external posture movement, and cross-repo truth",
        ],
        "candidate_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "current_t454_t455_label": current["gate_label"],
            "current_t454_t455_missing_requirements": current[
                "missing_requirements"
            ],
            "admitted_candidate_ids": [item["candidate_id"] for item in admitted],
            "admitted_candidates_are_synthetic_only": all(
                item["candidate"]["synthetic_control_only"] for item in admitted
            ),
            "current_artifacts_admitted_for_stronger_posture": False,
            "region_discriminator_success": False,
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "Current T454/T455 is not admitted for stronger Direction-A "
                "posture. It remains a recorded-tier review target because the "
                "law-sector description absorber, reference-policy fragility, and "
                "no-policy-independent-theorem objection still fire. T456 admits "
                "only a synthetic future target shape."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Do not promote T454/T455 beyond recorded-tier review target.",
            "Future Direction-A packets must clear T456 before any stronger posture movement.",
            "If no packet can clear description nonfactorization, reference-policy invariance, and theorem supply, demote the integrated E3-region route to a useful negative guardrail.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["admission_requirements"]]
    rows = [
        "| {candidate_id} | {admitted} | {label} | {missing} |".format(
            candidate_id=item["candidate_id"],
            admitted="yes" if item["admitted_future_target"] else "no",
            label=item["gate_label"],
            missing=", ".join(item["missing_requirements"]) or "none",
        )
        for item in result["candidate_evaluations"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T456 - Policy-Invariant Region Theorem Gate - v0.1 results",
            "",
            "> Admission gate only. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T456-policy-invariant-region-theorem-gate.md`",
            "- Model: `models/policy_invariant_region_theorem_gate.py`",
            "- Tests: `tests/test_policy_invariant_region_theorem_gate.py`",
            "- Artifact JSON: `results/T456-policy-invariant-region-theorem-gate-v0.1.json`",
            "- Sources: T447, T452, T453, T454, T455, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Admission Requirements",
            "",
            *requirements,
            "",
            "## Candidate Evaluation",
            "",
            "| candidate | admitted? | gate label | missing requirements |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a sharper admission gate for future Direction-A packets after "
            "T455. It makes the next burden executable and rejects current "
            "T454/T455 for stronger posture.",
            "",
            "Does not earn: a region-indexed discriminator success, real substrate "
            "law, quantum physics theorem, WAY theorem, GU/TaF adapter, "
            "claim-ledger movement, TESTS or roadmap movement, public posture, "
            "hard-policy movement, or cross-repo support.",
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_steps,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T456-policy-invariant-region-theorem-gate-v0.1.json"
        md_path = (
            results_dir
            / "T456-policy-invariant-region-theorem-gate-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
