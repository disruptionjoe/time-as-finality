"""T459 - policy-independent theorem-supply gate.

T456 left the integrated E3-region route with three blockers. T457 sharpened
description completion. T458 sharpened reference-policy invariance/preclusion.
This gate audits the remaining theorem-supply burden: whether the current
T454-style packet class has an independent theorem, beyond packet integration,
that makes the capability-deciding completion physically non-admissible and
handles or precludes reference-policy variants.

Run:

    python -m models.policy_independent_theorem_supply_gate --write-results
    python -m pytest tests/test_policy_independent_theorem_supply_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import description_completion_squeeze_gate as t457
from models import reference_policy_invariance_gate as t458


ARTIFACT = "T459-policy-independent-theorem-supply-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T454 = "results/T454-integrated-e3-region-packet-swing-v0.1-results.md"
SOURCE_T455 = "results/T455-t454-hostile-review-gate-v0.1-results.md"
SOURCE_T456 = "results/T456-policy-invariant-region-theorem-gate-v0.1-results.md"
SOURCE_T457 = "results/T457-description-completion-squeeze-gate-v0.1-results.md"
SOURCE_T458 = "results/T458-reference-policy-invariance-gate-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = (
    "POLICY_INDEPENDENT_THEOREM_SUPPLY_GATE_BUILT_CURRENT_ROUTE_DEMOTED_TO_NEGATIVE_GUARDRAIL"
)

HONEST_CEILING = (
    "Admission/demotion gate only. T459 closes the current integrated "
    "E3-region packet class as a route-level negative guardrail because it "
    "lacks an independent theorem beyond packet integration, still factors "
    "through admitted description, and remains reference-policy relative. It "
    "does not prove a region-indexed discriminator, real substrate law, quantum "
    "physics theorem, WAY theorem, GU/TaF adapter, claim support, public "
    "posture, or cross-repo support."
)


@dataclass(frozen=True)
class TheoremSupplyCandidate:
    candidate_id: str
    description: str
    source: str
    region_packet_present: bool
    mechanical_packet_review_survives: bool
    theorem_supplied: bool
    theorem_is_not_packet_integration: bool
    theorem_policy_independent: bool
    theorem_declared_before_pair: bool
    theorem_targets_named_completion: bool
    theorem_makes_completion_nonadmissible: bool
    description_nonfactorization_supplied: bool
    reference_variants_handled_or_precluded: bool
    operation_resource_class_frozen: bool = True
    a2_resource_lift_audited: bool = True
    negative_control_present: bool = True
    reads_hidden_label_or_case_id: bool = False
    requests_external_posture: bool = False
    synthetic_control_only: bool = False


def _candidate_to_dict(candidate: TheoremSupplyCandidate) -> dict[str, Any]:
    return asdict(candidate)


def _t457_current_summary() -> dict[str, Any]:
    result = t457.run()
    current = next(
        item
        for item in result["candidate_evaluations"]
        if item["candidate_id"] == "current_t454_boundary_resource_description"
    )
    return {
        "verdict": result["overall_verdict"]["verdict"],
        "current_label": current["gate_label"],
        "capability_factors_through_description": current[
            "factorization_audit"
        ]["capability_factors_through_description"],
        "current_artifacts_admitted_for_stronger_posture": result[
            "overall_verdict"
        ]["current_artifacts_admitted_for_stronger_posture"],
    }


def _t458_current_summary() -> dict[str, Any]:
    result = t458.run()
    current = next(
        item
        for item in result["candidate_evaluations"]
        if item["candidate_id"] == "current_t454_t455_t457_reference_policy_packet"
    )
    return {
        "verdict": result["overall_verdict"]["verdict"],
        "current_label": current["gate_label"],
        "unhandled_reference_policies": current["reference_policy_audit"][
            "unhandled_reference_policies"
        ],
        "current_artifacts_admitted_for_stronger_posture": result[
            "overall_verdict"
        ]["current_artifacts_admitted_for_stronger_posture"],
    }


def requirement_audit(candidate: TheoremSupplyCandidate) -> dict[str, bool]:
    return {
        "region_packet_present": candidate.region_packet_present,
        "mechanical_packet_review_survives": (
            candidate.mechanical_packet_review_survives
        ),
        "theorem_supplied": candidate.theorem_supplied,
        "theorem_not_packet_integration": (
            candidate.theorem_is_not_packet_integration
        ),
        "theorem_policy_independent": candidate.theorem_policy_independent,
        "theorem_declared_before_pair": candidate.theorem_declared_before_pair,
        "theorem_targets_named_completion": (
            candidate.theorem_targets_named_completion
        ),
        "theorem_makes_completion_nonadmissible": (
            candidate.theorem_makes_completion_nonadmissible
        ),
        "description_nonfactorization_supplied": (
            candidate.description_nonfactorization_supplied
        ),
        "reference_variants_handled_or_precluded": (
            candidate.reference_variants_handled_or_precluded
        ),
        "operation_resource_class_frozen": (
            candidate.operation_resource_class_frozen
        ),
        "a2_resource_lift_audited": candidate.a2_resource_lift_audited,
        "negative_control_present": candidate.negative_control_present,
        "no_hidden_label_or_case_id": (
            not candidate.reads_hidden_label_or_case_id
        ),
        "no_external_posture_request": not candidate.requests_external_posture,
    }


def evaluate_candidate(candidate: TheoremSupplyCandidate) -> dict[str, Any]:
    requirements = requirement_audit(candidate)
    missing = [key for key, value in requirements.items() if value is False]
    admitted = False

    if candidate.requests_external_posture:
        label = "BLOCKED_EXTERNAL_OR_PUBLIC_POSTURE_REQUEST"
        reason = "External/public posture movement is outside this repo-local gate."
    elif candidate.reads_hidden_label_or_case_id:
        label = "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
        reason = "The packet reads a hidden selector instead of theorem content."
    elif not candidate.theorem_declared_before_pair:
        label = "NOT_ADMITTED_POST_HOC_THEOREM"
        reason = "The theorem or theorem scope is declared after pair selection."
    elif not candidate.region_packet_present:
        label = "NOT_ADMITTED_NO_REGION_PACKET"
        reason = "A theorem without a region-indexed packet cannot move Direction A."
    elif not candidate.mechanical_packet_review_survives:
        label = "NOT_ADMITTED_PACKET_MECHANICS_FAIL"
        reason = "The packet fails the prior T455 mechanical review legs."
    elif not candidate.theorem_supplied:
        label = "NOT_ADMITTED_NO_THEOREM_SUPPLIED"
        reason = "No theorem is supplied beyond the finite packet."
    elif not candidate.theorem_is_not_packet_integration:
        label = "NOT_ADMITTED_PACKET_INTEGRATION_IS_NOT_THEOREM"
        reason = "Restating packet integration is not an independent theorem."
    elif not candidate.theorem_policy_independent:
        label = "NOT_ADMITTED_POLICY_DEPENDENT_THEOREM"
        reason = "The theorem depends on the same policy choice it must preclude."
    elif not candidate.theorem_targets_named_completion:
        label = "NOT_ADMITTED_THEOREM_NOT_TIED_TO_COMPLETION"
        reason = "The theorem does not target the named completion that restores factorization."
    elif not candidate.theorem_makes_completion_nonadmissible:
        label = "NOT_ADMITTED_THEOREM_DOES_NOT_PRECLUDE_COMPLETION"
        reason = "The theorem does not make the capability-deciding completion physically non-admissible."
    elif not candidate.description_nonfactorization_supplied:
        label = "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"
        reason = "The packet still factors through admitted description."
    elif not candidate.reference_variants_handled_or_precluded:
        label = "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
        reason = "Reference-policy variants still restore completion or route away."
    elif not candidate.operation_resource_class_frozen:
        label = "NOT_ADMITTED_OPERATION_RESOURCE_CLASS_UNFROZEN"
        reason = "The operation/resource class must be frozen before scoring."
    elif not candidate.a2_resource_lift_audited:
        label = "NOT_ADMITTED_A2_RESOURCE_LIFT_UNAUDITED"
        reason = "A2 reference/resource completion must be audited."
    elif not candidate.negative_control_present:
        label = "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
        reason = "The packet lacks a negative control."
    else:
        admitted = True
        label = "ADMITTED_POLICY_INDEPENDENT_THEOREM_TARGET_NO_PROMOTION"
        reason = "Synthetic future target clears the theorem-supply gate without claim promotion."

    return {
        "candidate_id": candidate.candidate_id,
        "candidate": _candidate_to_dict(candidate),
        "requirement_audit": requirements,
        "missing_requirements": missing,
        "gate_label": label,
        "admitted_future_target": admitted,
        "reason": reason,
    }


def candidates() -> tuple[TheoremSupplyCandidate, ...]:
    current_source = "; ".join((SOURCE_T454, SOURCE_T455, SOURCE_T457, SOURCE_T458))
    return (
        TheoremSupplyCandidate(
            candidate_id="current_t454_t455_t457_t458_integrated_route",
            description=(
                "The current integrated E3-region route after T457 and T458."
            ),
            source=current_source,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=False,
            theorem_is_not_packet_integration=False,
            theorem_policy_independent=False,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=False,
            theorem_makes_completion_nonadmissible=False,
            description_nonfactorization_supplied=False,
            reference_variants_handled_or_precluded=False,
        ),
        TheoremSupplyCandidate(
            candidate_id="packet_integration_as_theorem_control",
            description="A packet that treats the integrated finite toy as its theorem.",
            source=SOURCE_T454,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=False,
            theorem_policy_independent=False,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=False,
            description_nonfactorization_supplied=False,
            reference_variants_handled_or_precluded=False,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="description_factorization_control",
            description="A theorem-shaped packet that still admits description completion.",
            source=SOURCE_T457,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            description_nonfactorization_supplied=False,
            reference_variants_handled_or_precluded=True,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="reference_policy_relative_theorem_control",
            description="A theorem-shaped packet that leaves cyclic/consumed/ideal references unhandled.",
            source=SOURCE_T458,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            description_nonfactorization_supplied=True,
            reference_variants_handled_or_precluded=False,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="policy_dependent_theorem_control",
            description="A theorem-shaped packet that precludes variants only by policy choice.",
            source=ARTIFACT,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=False,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            description_nonfactorization_supplied=True,
            reference_variants_handled_or_precluded=True,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="post_hoc_theorem_control",
            description="A theorem-shaped packet whose theorem is selected after pair construction.",
            source=ARTIFACT,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=True,
            theorem_declared_before_pair=False,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            description_nonfactorization_supplied=True,
            reference_variants_handled_or_precluded=True,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="untargeted_theorem_control",
            description="A theorem-shaped packet unrelated to the named completion.",
            source=ARTIFACT,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=False,
            theorem_makes_completion_nonadmissible=True,
            description_nonfactorization_supplied=True,
            reference_variants_handled_or_precluded=True,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="completion_not_precluded_control",
            description="A theorem-shaped packet that names completion but does not make it non-admissible.",
            source=ARTIFACT,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=False,
            description_nonfactorization_supplied=True,
            reference_variants_handled_or_precluded=True,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="hidden_label_theorem_control",
            description="A packet that selects theorem treatment through a hidden case label.",
            source=ARTIFACT,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            description_nonfactorization_supplied=True,
            reference_variants_handled_or_precluded=True,
            reads_hidden_label_or_case_id=True,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="synthetic_policy_independent_theorem_target",
            description="A future-shaped packet with an independent theorem clearing all T456 blockers.",
            source=ARTIFACT,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            description_nonfactorization_supplied=True,
            reference_variants_handled_or_precluded=True,
            synthetic_control_only=True,
        ),
        TheoremSupplyCandidate(
            candidate_id="synthetic_missing_negative_control",
            description="A future-shaped theorem packet missing its negative control.",
            source=ARTIFACT,
            region_packet_present=True,
            mechanical_packet_review_survives=True,
            theorem_supplied=True,
            theorem_is_not_packet_integration=True,
            theorem_policy_independent=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            description_nonfactorization_supplied=True,
            reference_variants_handled_or_precluded=True,
            negative_control_present=False,
            synthetic_control_only=True,
        ),
    )


def run() -> dict[str, Any]:
    evaluations = [evaluate_candidate(candidate) for candidate in candidates()]
    admitted = [item for item in evaluations if item["admitted_future_target"]]
    current = next(
        item
        for item in evaluations
        if item["candidate_id"] == "current_t454_t455_t457_t458_integrated_route"
    )

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t454": SOURCE_T454,
            "t455": SOURCE_T455,
            "t456": SOURCE_T456,
            "t457": SOURCE_T457,
            "t458": SOURCE_T458,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Audit the last T456 blocker after T457 and T458: independent theorem "
            "supply for the integrated E3-region route."
        ),
        "t457_import_summary": _t457_current_summary(),
        "t458_import_summary": _t458_current_summary(),
        "candidate_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "current_route_label": current["gate_label"],
            "current_route_missing_requirements": current["missing_requirements"],
            "admitted_candidate_ids": [item["candidate_id"] for item in admitted],
            "admitted_candidates_are_synthetic_only": all(
                item["candidate"]["synthetic_control_only"] for item in admitted
            ),
            "current_artifacts_admitted_for_stronger_posture": False,
            "current_route_demoted_to_negative_guardrail": True,
            "route_demotion_scope": "current integrated E3-region packet class only",
            "region_discriminator_success": False,
            "claim_ledger_update": "none; no claim promotion or claim demotion",
            "reading": (
                "After T457 and T458, the current T454/T455/T457/T458 route still "
                "has no independent policy-invariant theorem beyond packet "
                "integration. Description completion and reference-policy "
                "fragility remain live, so the current integrated E3-region "
                "packet class is demoted to a useful negative guardrail rather "
                "than a stronger Direction-A route."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion or claim demotion",
        "recommended_next": [
            "Do not seek stronger posture from the current integrated E3-region packet class.",
            "Treat T454-T459 as negative guardrails for future Direction-A packets.",
            "A future Direction-A restart needs a new packet class with a predeclared independent theorem that clears T457, T458, and T459 together.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
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
            "# T459 - Policy-Independent Theorem-Supply Gate - v0.1 results",
            "",
            "> Admission/demotion gate only. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T459-policy-independent-theorem-supply-gate.md`",
            "- Model: `models/policy_independent_theorem_supply_gate.py`",
            "- Tests: `tests/test_policy_independent_theorem_supply_gate.py`",
            "- Artifact JSON: `results/T459-policy-independent-theorem-supply-gate-v0.1.json`",
            "- Sources: T454, T455, T456, T457, T458, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Candidate Evaluation",
            "",
            "| candidate | admitted? | gate label | missing requirements |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## Route Disposition",
            "",
            "- Current route status: `negative_guardrail_only`.",
            f"- Scope: `{verdict['route_demotion_scope']}`.",
            "- Claim ledger movement: none.",
            "- Public posture movement: none.",
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a sharper final guardrail for the integrated E3-region route. "
            "It records that the current packet class has exhausted the T456 "
            "blocker set: description nonfactorization, reference-policy "
            "invariance/preclusion, and independent theorem supply all remain "
            "uncleared.",
            "",
            "Does not earn: a region-indexed discriminator success, real "
            "substrate law, quantum physics theorem, WAY theorem, GU/TaF adapter, "
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
        json_path = results_dir / "T459-policy-independent-theorem-supply-gate-v0.1.json"
        md_path = (
            results_dir
            / "T459-policy-independent-theorem-supply-gate-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
