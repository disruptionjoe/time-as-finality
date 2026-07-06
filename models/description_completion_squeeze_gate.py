"""T457 - description-completion squeeze gate.

T456 left the integrated E3-region route with three blockers. This gate focuses
on the first one: description nonfactorization. For the current T454-style
boundary-resource packet class, once the admitted description includes the
boundary resource that decides revision capability, the capability object factors
through that description.

Run:

    python -m models.description_completion_squeeze_gate --write-results
    python -m pytest tests/test_description_completion_squeeze_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path
from typing import Any

from models import policy_invariant_region_theorem_gate as t456


ARTIFACT = "T457-description-completion-squeeze-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T454 = "results/T454-integrated-e3-region-packet-swing-v0.1-results.md"
SOURCE_T455 = "results/T455-t454-hostile-review-gate-v0.1-results.md"
SOURCE_T456 = "results/T456-policy-invariant-region-theorem-gate-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "DESCRIPTION_COMPLETION_SQUEEZE_GATE_BUILT_T454_CLASS_FACTORS_THROUGH_DESCRIPTION"

HONEST_CEILING = (
    "Admission/guardrail gate only. T457 shows that the current T454-style "
    "boundary-resource packet class cannot clear T456's description-"
    "nonfactorization requirement while the boundary-resource descriptor remains "
    "admitted and capability-deciding. It does not prove a region-indexed "
    "discriminator, real substrate law, quantum physics theorem, WAY theorem, "
    "GU/TaF adapter, claim support, public posture, or cross-repo support."
)

CAPABILITY_DECIDING_FIELDS = (
    "correction_budget",
    "boundary_charge_available",
    "operation_resource_class",
)


@dataclass(frozen=True)
class BoundaryCase:
    case_id: str
    verdict_payload: str = "same"
    region_charge: int = 0
    correction_budget: int = 1
    boundary_charge_available: int = 0
    operation_resource_class: str = "charge_respecting_control"
    reference_policy: str = "finite_nonwrapping_exact_catalyst"
    hidden_selector_label: str | None = None


@dataclass(frozen=True)
class DescriptionPacketCandidate:
    candidate_id: str
    description: str
    source: str
    cases: tuple[BoundaryCase, ...]
    description_fields: tuple[str, ...]
    descriptor_admitted: bool = True
    omitted_capability_field_has_theorem: bool = False
    theorem_policy_independent: bool = False
    reference_policy_variants_invariant_or_precluded: bool = False
    operation_resource_class_frozen: bool = True
    a2_resource_lift_audited: bool = True
    negative_control_present: bool = True
    declared_before_pair: bool = True
    reads_hidden_label_or_case_id: bool = False
    requests_external_posture: bool = False
    synthetic_control_only: bool = False


def _case_to_dict(case: BoundaryCase) -> dict[str, Any]:
    return asdict(case)


def _candidate_to_dict(candidate: DescriptionPacketCandidate) -> dict[str, Any]:
    data = asdict(candidate)
    data["cases"] = [_case_to_dict(case) for case in candidate.cases]
    return data


def _capability(case: BoundaryCase) -> dict[str, Any]:
    can_revise = (
        case.correction_budget > 0
        and case.boundary_charge_available == 1
        and case.operation_resource_class == "charge_respecting_control"
    )
    return {
        "can_revise_final_verdict": can_revise,
        "revision_blocked_reason": "none"
        if can_revise
        else "requires_admitted_boundary_resource",
    }


def _description(case: BoundaryCase, fields: tuple[str, ...]) -> dict[str, Any]:
    return {field: getattr(case, field) for field in fields}


def factorization_audit(candidate: DescriptionPacketCandidate) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    split_pairs: list[dict[str, Any]] = []
    same_description_pairs = 0

    for left, right in combinations(candidate.cases, 2):
        left_description = _description(left, candidate.description_fields)
        right_description = _description(right, candidate.description_fields)
        left_capability = _capability(left)
        right_capability = _capability(right)
        same_description = left_description == right_description
        capability_split = left_capability != right_capability
        if same_description:
            same_description_pairs += 1
        if same_description and capability_split:
            split_pairs.append(
                {
                    "left": left.case_id,
                    "right": right.case_id,
                    "description": left_description,
                    "left_capability": left_capability,
                    "right_capability": right_capability,
                }
            )
        rows.append(
            {
                "left": left.case_id,
                "right": right.case_id,
                "same_description": same_description,
                "capability_split": capability_split,
            }
        )

    omitted_deciding_fields = [
        field
        for field in CAPABILITY_DECIDING_FIELDS
        if field not in candidate.description_fields
    ]

    return {
        "description_fields": list(candidate.description_fields),
        "capability_deciding_fields": list(CAPABILITY_DECIDING_FIELDS),
        "omitted_capability_deciding_fields": omitted_deciding_fields,
        "same_description_pairs": same_description_pairs,
        "split_pairs": split_pairs,
        "pair_rows": rows,
        "capability_factors_through_description": not split_pairs,
        "description_nonfactorization_witnessed": bool(split_pairs),
    }


def requirement_audit(candidate: DescriptionPacketCandidate) -> dict[str, bool]:
    factorization = factorization_audit(candidate)
    omitted_deciding = bool(factorization["omitted_capability_deciding_fields"])
    return {
        "descriptor_admitted": candidate.descriptor_admitted,
        "description_nonfactorization_witnessed": factorization[
            "description_nonfactorization_witnessed"
        ],
        "omitted_deciding_fields_theorem_supported": (
            not omitted_deciding or candidate.omitted_capability_field_has_theorem
        ),
        "theorem_policy_independent": candidate.theorem_policy_independent,
        "reference_policy_invariant_or_precluded": (
            candidate.reference_policy_variants_invariant_or_precluded
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


def evaluate_candidate(candidate: DescriptionPacketCandidate) -> dict[str, Any]:
    factorization = factorization_audit(candidate)
    requirements = requirement_audit(candidate)
    missing = [key for key, value in requirements.items() if value is False]
    omitted_deciding = bool(factorization["omitted_capability_deciding_fields"])
    admitted = False

    if candidate.requests_external_posture:
        label = "BLOCKED_EXTERNAL_OR_PUBLIC_POSTURE_REQUEST"
        reason = "External/public posture movement is outside this repo-local gate."
    elif candidate.reads_hidden_label_or_case_id:
        label = "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
        reason = "The packet reads a hidden selector rather than a description theorem."
    elif not candidate.declared_before_pair:
        label = "BLOCKED_POST_HOC_DESCRIPTION_PACKET"
        reason = "The description packet must be declared before pair selection."
    elif not candidate.descriptor_admitted:
        label = "NOT_ADMITTED_DESCRIPTOR_NOT_ADMITTED"
        reason = "The descriptor itself is not admitted as a stable comparison object."
    elif factorization["capability_factors_through_description"]:
        label = "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"
        reason = (
            "Within this packet class, admitted description already decides the "
            "boundary-menu capability, so description completion restores "
            "factorization."
        )
    elif omitted_deciding and not candidate.omitted_capability_field_has_theorem:
        label = "NOT_ADMITTED_UNDERDESCRIBED_BOUNDARY_RESOURCE"
        reason = (
            "The apparent split is created by omitting a capability-deciding "
            "boundary-resource field without an independent theorem that makes "
            "that field physically non-admissible."
        )
    elif not candidate.theorem_policy_independent:
        label = "NOT_ADMITTED_NO_POLICY_INDEPENDENT_THEOREM"
        reason = "The packet supplies a split but not a policy-independent theorem."
    elif not candidate.reference_policy_variants_invariant_or_precluded:
        label = "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
        reason = (
            "Cyclic, consumed, or ideal reference variants are not invariantly "
            "handled or independently precluded."
        )
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
        label = "ADMITTED_NON_DESCRIPTIVE_THEOREM_TARGET_NO_PROMOTION"
        reason = (
            "The candidate has the future target shape: nonfactorization under "
            "the declared description, a theorem supporting omission of the "
            "capability-deciding field, policy independence, reference-policy "
            "invariance or preclusion, frozen operations, A2 audit, and controls."
        )

    return {
        "candidate_id": candidate.candidate_id,
        "description": candidate.description,
        "source": candidate.source,
        "candidate": _candidate_to_dict(candidate),
        "factorization_audit": factorization,
        "requirement_audit": requirements,
        "missing_requirements": missing,
        "admitted_future_target": admitted,
        "gate_label": label,
        "reason": reason,
    }


def _cases() -> dict[str, BoundaryCase]:
    return {
        "available": BoundaryCase(
            case_id="boundary_resource_available",
            boundary_charge_available=1,
        ),
        "deficient": BoundaryCase(
            case_id="boundary_resource_deficient",
            boundary_charge_available=0,
        ),
        "available_copy": BoundaryCase(
            case_id="boundary_resource_available_copy",
            boundary_charge_available=1,
        ),
        "hidden_alpha": BoundaryCase(
            case_id="hidden_alpha",
            boundary_charge_available=0,
            hidden_selector_label="alpha",
        ),
        "hidden_beta": BoundaryCase(
            case_id="hidden_beta",
            boundary_charge_available=1,
            hidden_selector_label="beta",
        ),
    }


def candidates() -> tuple[DescriptionPacketCandidate, ...]:
    cases = _cases()
    main_cases = (cases["available"], cases["deficient"], cases["available_copy"])
    complete_fields = (
        "verdict_payload",
        "region_charge",
        "correction_budget",
        "boundary_charge_available",
        "operation_resource_class",
        "reference_policy",
    )
    underdescribed_fields = (
        "verdict_payload",
        "region_charge",
        "correction_budget",
        "operation_resource_class",
        "reference_policy",
    )

    return (
        DescriptionPacketCandidate(
            candidate_id="current_t454_boundary_resource_description",
            description=(
                "The current T454/T455 class after admitting the boundary "
                "resource descriptor that decides revision capability."
            ),
            source=f"{SOURCE_T454}; {SOURCE_T455}; {SOURCE_T456}",
            cases=main_cases,
            description_fields=complete_fields,
            theorem_policy_independent=False,
            reference_policy_variants_invariant_or_precluded=False,
        ),
        DescriptionPacketCandidate(
            candidate_id="omitted_boundary_resource_control",
            description=(
                "A same-description split created by omitting the boundary "
                "resource field from the descriptor."
            ),
            source=ARTIFACT,
            cases=main_cases,
            description_fields=underdescribed_fields,
            theorem_policy_independent=False,
            reference_policy_variants_invariant_or_precluded=False,
        ),
        DescriptionPacketCandidate(
            candidate_id="description_complete_synthetic_control",
            description=(
                "Synthetic control proving that once the capability-deciding "
                "field is included, the split disappears into description completion."
            ),
            source=ARTIFACT,
            cases=main_cases,
            description_fields=complete_fields,
            omitted_capability_field_has_theorem=True,
            theorem_policy_independent=True,
            reference_policy_variants_invariant_or_precluded=True,
            synthetic_control_only=True,
        ),
        DescriptionPacketCandidate(
            candidate_id="synthetic_non_descriptive_theorem_target",
            description=(
                "Future target shape: the descriptor omits the boundary resource, "
                "but a policy-independent theorem makes that field physically "
                "non-admissible while reference variants are handled."
            ),
            source=ARTIFACT,
            cases=main_cases,
            description_fields=underdescribed_fields,
            omitted_capability_field_has_theorem=True,
            theorem_policy_independent=True,
            reference_policy_variants_invariant_or_precluded=True,
            synthetic_control_only=True,
        ),
        DescriptionPacketCandidate(
            candidate_id="synthetic_no_policy_independence",
            description="A nonfactorizing packet with no policy-independent theorem.",
            source=ARTIFACT,
            cases=main_cases,
            description_fields=underdescribed_fields,
            omitted_capability_field_has_theorem=True,
            theorem_policy_independent=False,
            reference_policy_variants_invariant_or_precluded=True,
            synthetic_control_only=True,
        ),
        DescriptionPacketCandidate(
            candidate_id="synthetic_reference_policy_fragile",
            description="A nonfactorizing packet whose reference variants are still fragile.",
            source=ARTIFACT,
            cases=main_cases,
            description_fields=underdescribed_fields,
            omitted_capability_field_has_theorem=True,
            theorem_policy_independent=True,
            reference_policy_variants_invariant_or_precluded=False,
            synthetic_control_only=True,
        ),
        DescriptionPacketCandidate(
            candidate_id="hidden_label_shortcut_control",
            description="A shortcut that reads hidden case labels.",
            source=ARTIFACT,
            cases=(cases["hidden_alpha"], cases["hidden_beta"]),
            description_fields=underdescribed_fields,
            omitted_capability_field_has_theorem=True,
            theorem_policy_independent=True,
            reference_policy_variants_invariant_or_precluded=True,
            reads_hidden_label_or_case_id=True,
            synthetic_control_only=True,
        ),
        DescriptionPacketCandidate(
            candidate_id="synthetic_missing_negative_control",
            description="A future-shaped packet missing its negative control.",
            source=ARTIFACT,
            cases=main_cases,
            description_fields=underdescribed_fields,
            omitted_capability_field_has_theorem=True,
            theorem_policy_independent=True,
            reference_policy_variants_invariant_or_precluded=True,
            negative_control_present=False,
            synthetic_control_only=True,
        ),
    )


def _t456_current_summary() -> dict[str, Any]:
    result = t456.run()
    current = next(
        item
        for item in result["candidate_evaluations"]
        if item["candidate_id"] == "current_t454_t455_review_target"
    )
    return {
        "verdict": result["overall_verdict"]["verdict"],
        "current_t454_t455_label": current["gate_label"],
        "current_t454_t455_missing_requirements": current[
            "missing_requirements"
        ],
        "admitted_candidates_are_synthetic_only": result["overall_verdict"][
            "admitted_candidates_are_synthetic_only"
        ],
    }


def run() -> dict[str, Any]:
    evaluations = [evaluate_candidate(candidate) for candidate in candidates()]
    admitted = [item for item in evaluations if item["admitted_future_target"]]
    current = next(
        item
        for item in evaluations
        if item["candidate_id"] == "current_t454_boundary_resource_description"
    )

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t454": SOURCE_T454,
            "t455": SOURCE_T455,
            "t456": SOURCE_T456,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Sharpen T456's description-nonfactorization blocker for the current "
            "T454-style boundary-resource packet class."
        ),
        "t456_import_summary": _t456_current_summary(),
        "capability_deciding_fields": list(CAPABILITY_DECIDING_FIELDS),
        "candidate_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "current_t454_class_label": current["gate_label"],
            "current_t454_class_factors_through_description": current[
                "factorization_audit"
            ]["capability_factors_through_description"],
            "admitted_candidate_ids": [item["candidate_id"] for item in admitted],
            "admitted_candidates_are_synthetic_only": all(
                item["candidate"]["synthetic_control_only"] for item in admitted
            ),
            "current_artifacts_admitted_for_stronger_posture": False,
            "region_discriminator_success": False,
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "The current T454/T455 packet class cannot clear T456's "
                "description-nonfactorization requirement while the "
                "boundary-resource descriptor remains admitted and "
                "capability-deciding. Omitting that descriptor creates only an "
                "underdescription split unless a future policy-independent "
                "theorem makes the omitted field physically non-admissible."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Do not seek stronger posture inside the current T454 boundary-resource-description class.",
            "Future Direction-A packets must change class by supplying a policy-independent nonadmissibility theorem for the omitted capability-deciding field.",
            "If no such theorem packet can be supplied, demote the integrated E3-region route to a useful negative guardrail.",
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
            "# T457 - Description-Completion Squeeze Gate - v0.1 results",
            "",
            "> Admission/guardrail gate only. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T457-description-completion-squeeze-gate.md`",
            "- Model: `models/description_completion_squeeze_gate.py`",
            "- Tests: `tests/test_description_completion_squeeze_gate.py`",
            "- Artifact JSON: `results/T457-description-completion-squeeze-gate-v0.1.json`",
            "- Sources: T454, T455, T456, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Capability-Deciding Fields",
            "",
            *[f"- `{field}`" for field in result["capability_deciding_fields"]],
            "",
            "## Candidate Evaluation",
            "",
            "| candidate | admitted? | gate label | missing requirements |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a sharper guardrail for T456's description-nonfactorization "
            "blocker. It shows the current T454-style boundary-resource packet "
            "class factors through admitted description.",
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
        json_path = results_dir / "T457-description-completion-squeeze-gate-v0.1.json"
        md_path = (
            results_dir / "T457-description-completion-squeeze-gate-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
