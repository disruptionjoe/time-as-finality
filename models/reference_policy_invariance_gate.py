"""T458 - reference-policy invariance/preclusion gate.

T456 left the integrated E3-region route with three blockers. T457 sharpened
the description-completion blocker. This gate focuses on the second blocker:
reference-policy invariance or independent preclusion.

For the current T454-style packet, the positive finite non-wrapping exact
catalyst policy remains policy-relative. Cyclic, consumed, and ideal-reference
variants either restore completion or route away. A stronger Direction-A packet
must make the split invariant across the admitted reference-policy family, or
preclude the variants by a policy-independent theorem declared before pair
selection.

Run:

    python -m models.reference_policy_invariance_gate --write-results
    python -m pytest tests/test_reference_policy_invariance_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import description_completion_squeeze_gate as t457
from models import integrated_e3_region_packet_swing as t454


ARTIFACT = "T458-reference-policy-invariance-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T454 = "results/T454-integrated-e3-region-packet-swing-v0.1-results.md"
SOURCE_T455 = "results/T455-t454-hostile-review-gate-v0.1-results.md"
SOURCE_T456 = "results/T456-policy-invariant-region-theorem-gate-v0.1-results.md"
SOURCE_T457 = "results/T457-description-completion-squeeze-gate-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = (
    "REFERENCE_POLICY_INVARIANCE_GATE_BUILT_CURRENT_T454_POLICY_RELATIVE_NOT_ADMITTED"
)

HONEST_CEILING = (
    "Admission/guardrail gate only. T458 shows that the current integrated "
    "E3-region packet remains relative to the finite non-wrapping exact-catalyst "
    "policy. It does not prove a region-indexed discriminator, real substrate "
    "law, quantum physics theorem, WAY theorem, GU/TaF adapter, claim support, "
    "public posture, or cross-repo support."
)

REQUIRED_REFERENCE_POLICIES = (
    "finite_nonwrapping_exact_catalyst",
    "finite_cyclic_reference",
    "consumed_charge_battery",
    "ideal_phase_reference",
)


@dataclass(frozen=True)
class ReferencePolicyVariant:
    policy_id: str
    completion_label: str
    preserves_boundary_split: bool
    completion_restores_or_routes_away: bool
    precluded_by_independent_theorem: bool = False
    preclusion_theorem_policy_independent: bool = False
    preclusion_declared_before_pair: bool = True
    note: str = ""


@dataclass(frozen=True)
class ReferencePolicyCandidate:
    candidate_id: str
    description: str
    source: str
    variants: tuple[ReferencePolicyVariant, ...]
    reference_scope_declared_before_pair: bool = True
    exact_witness_tied_to_named_completion: bool = True
    operation_resource_class_frozen: bool = True
    a2_resource_lift_audited: bool = True
    negative_control_present: bool = True
    reads_hidden_label_or_case_id: bool = False
    requests_external_posture: bool = False
    synthetic_control_only: bool = False


def _variant_to_dict(variant: ReferencePolicyVariant) -> dict[str, Any]:
    return asdict(variant)


def _candidate_to_dict(candidate: ReferencePolicyCandidate) -> dict[str, Any]:
    data = asdict(candidate)
    data["variants"] = [_variant_to_dict(variant) for variant in candidate.variants]
    return data


def _variant_handled(variant: ReferencePolicyVariant) -> bool:
    if variant.preserves_boundary_split:
        return True
    return (
        variant.precluded_by_independent_theorem
        and variant.preclusion_theorem_policy_independent
        and variant.preclusion_declared_before_pair
    )


def _variant_failure_reason(variant: ReferencePolicyVariant) -> str:
    if variant.preserves_boundary_split:
        return "handled_by_invariant_split"
    if not variant.precluded_by_independent_theorem:
        return "not_precluded_and_does_not_preserve_split"
    if not variant.preclusion_declared_before_pair:
        return "preclusion_is_post_hoc"
    if not variant.preclusion_theorem_policy_independent:
        return "preclusion_not_policy_independent"
    return "handled_by_independent_preclusion"


def reference_policy_audit(candidate: ReferencePolicyCandidate) -> dict[str, Any]:
    variant_by_policy = {variant.policy_id: variant for variant in candidate.variants}
    present = tuple(sorted(variant_by_policy))
    missing = [
        policy for policy in REQUIRED_REFERENCE_POLICIES if policy not in variant_by_policy
    ]
    extra = [
        policy for policy in present if policy not in set(REQUIRED_REFERENCE_POLICIES)
    ]
    unhandled = [
        variant.policy_id for variant in candidate.variants if not _variant_handled(variant)
    ]
    post_hoc_preclusions = [
        variant.policy_id
        for variant in candidate.variants
        if variant.precluded_by_independent_theorem
        and not variant.preclusion_declared_before_pair
    ]
    policy_dependent_preclusions = [
        variant.policy_id
        for variant in candidate.variants
        if variant.precluded_by_independent_theorem
        and not variant.preclusion_theorem_policy_independent
    ]

    return {
        "required_reference_policies": list(REQUIRED_REFERENCE_POLICIES),
        "present_reference_policies": list(present),
        "missing_reference_policies": missing,
        "extra_reference_policies": extra,
        "variant_rows": [
            {
                "policy_id": variant.policy_id,
                "completion_label": variant.completion_label,
                "preserves_boundary_split": variant.preserves_boundary_split,
                "completion_restores_or_routes_away": (
                    variant.completion_restores_or_routes_away
                ),
                "precluded_by_independent_theorem": (
                    variant.precluded_by_independent_theorem
                ),
                "preclusion_theorem_policy_independent": (
                    variant.preclusion_theorem_policy_independent
                ),
                "preclusion_declared_before_pair": (
                    variant.preclusion_declared_before_pair
                ),
                "handled": _variant_handled(variant),
                "failure_reason": _variant_failure_reason(variant),
                "note": variant.note,
            }
            for variant in candidate.variants
        ],
        "unhandled_reference_policies": unhandled,
        "post_hoc_preclusions": post_hoc_preclusions,
        "policy_dependent_preclusions": policy_dependent_preclusions,
        "reference_scope_complete": not missing and not extra,
        "all_required_policies_handled": not missing and not extra and not unhandled,
        "all_preclusions_declared_before_pair": not post_hoc_preclusions,
        "all_preclusions_policy_independent": not policy_dependent_preclusions,
    }


def requirement_audit(candidate: ReferencePolicyCandidate) -> dict[str, bool]:
    audit = reference_policy_audit(candidate)
    return {
        "reference_scope_declared_before_pair": (
            candidate.reference_scope_declared_before_pair
        ),
        "reference_scope_complete": audit["reference_scope_complete"],
        "all_required_reference_policies_handled": audit[
            "all_required_policies_handled"
        ],
        "all_preclusions_declared_before_pair": audit[
            "all_preclusions_declared_before_pair"
        ],
        "all_preclusions_policy_independent": audit[
            "all_preclusions_policy_independent"
        ],
        "exact_witness_tied_to_named_completion": (
            candidate.exact_witness_tied_to_named_completion
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


def evaluate_candidate(candidate: ReferencePolicyCandidate) -> dict[str, Any]:
    audit = reference_policy_audit(candidate)
    requirements = requirement_audit(candidate)
    missing = [key for key, value in requirements.items() if value is False]
    admitted = False

    if candidate.requests_external_posture:
        label = "BLOCKED_EXTERNAL_OR_PUBLIC_POSTURE_REQUEST"
        reason = "External/public posture movement is outside this repo-local gate."
    elif candidate.reads_hidden_label_or_case_id:
        label = "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
        reason = "The packet reads a hidden selector rather than a policy theorem."
    elif not candidate.reference_scope_declared_before_pair:
        label = "BLOCKED_POST_HOC_REFERENCE_SCOPE"
        reason = "The reference-policy scope must be declared before pair selection."
    elif audit["post_hoc_preclusions"]:
        label = "NOT_ADMITTED_POST_HOC_POLICY_PRECLUSION"
        reason = (
            "A reference-policy variant is precluded only after seeing the packet."
        )
    elif audit["policy_dependent_preclusions"]:
        label = "NOT_ADMITTED_POLICY_DEPENDENT_PRECLUSION"
        reason = (
            "A variant is excluded by a policy-relative rule, not by an independent "
            "preclusion theorem."
        )
    elif not audit["reference_scope_complete"]:
        label = "NOT_ADMITTED_REFERENCE_SCOPE_INCOMPLETE"
        reason = (
            "Finite non-wrapping, cyclic, consumed, and ideal reference policies "
            "must all be handled or independently precluded."
        )
    elif audit["unhandled_reference_policies"]:
        label = "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
        reason = (
            "At least one admitted reference-policy variant restores completion "
            "or routes away without an independent preclusion theorem."
        )
    elif not candidate.exact_witness_tied_to_named_completion:
        label = "NOT_ADMITTED_EXACT_WITNESS_NOT_TIED_TO_COMPLETION"
        reason = "The exact witness must target the named completion."
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
        label = "ADMITTED_REFERENCE_POLICY_INVARIANT_OR_PRECLUDED_TARGET_NO_PROMOTION"
        reason = (
            "The candidate has the future target shape: all required reference "
            "policies either preserve the boundary split or are precluded by a "
            "policy-independent theorem declared before pair selection."
        )

    return {
        "candidate_id": candidate.candidate_id,
        "description": candidate.description,
        "source": candidate.source,
        "candidate": _candidate_to_dict(candidate),
        "reference_policy_audit": audit,
        "requirement_audit": requirements,
        "missing_requirements": missing,
        "admitted_future_target": admitted,
        "gate_label": label,
        "reason": reason,
    }


def _variant(
    policy_id: str,
    completion_label: str,
    preserves_boundary_split: bool,
    completion_restores_or_routes_away: bool,
    precluded_by_independent_theorem: bool = False,
    preclusion_theorem_policy_independent: bool = False,
    preclusion_declared_before_pair: bool = True,
    note: str = "",
) -> ReferencePolicyVariant:
    return ReferencePolicyVariant(
        policy_id=policy_id,
        completion_label=completion_label,
        preserves_boundary_split=preserves_boundary_split,
        completion_restores_or_routes_away=completion_restores_or_routes_away,
        precluded_by_independent_theorem=precluded_by_independent_theorem,
        preclusion_theorem_policy_independent=preclusion_theorem_policy_independent,
        preclusion_declared_before_pair=preclusion_declared_before_pair,
        note=note,
    )


def _current_t454_variant_labels() -> dict[str, str]:
    result = t454.run()
    mapping = {
        "finite_nonwrapping_exact_catalyst": "main_integrated_nonwrapping_e3_region_packet",
        "finite_cyclic_reference": "cyclic_reference_completion_control",
        "consumed_charge_battery": "consumed_battery_completion_control",
        "ideal_phase_reference": "ideal_reference_completion_control",
    }
    labels: dict[str, str] = {}
    for policy_id, candidate_id in mapping.items():
        item = next(
            row
            for row in result["candidate_evaluations"]
            if row["candidate_id"] == candidate_id
        )
        labels[policy_id] = item["integrated_label"]
    return labels


def _current_policy_variants() -> tuple[ReferencePolicyVariant, ...]:
    labels = _current_t454_variant_labels()
    return (
        _variant(
            "finite_nonwrapping_exact_catalyst",
            labels["finite_nonwrapping_exact_catalyst"],
            preserves_boundary_split=True,
            completion_restores_or_routes_away=False,
            note="T454 main finite exact-catalyst packet survives as review target.",
        ),
        _variant(
            "finite_cyclic_reference",
            labels["finite_cyclic_reference"],
            preserves_boundary_split=False,
            completion_restores_or_routes_away=True,
            note="Cyclic shift has exact eigenvectors, so the nilpotent no-go does not apply.",
        ),
        _variant(
            "consumed_charge_battery",
            labels["consumed_charge_battery"],
            preserves_boundary_split=False,
            completion_restores_or_routes_away=True,
            note="Consumed reference routes to resource completion.",
        ),
        _variant(
            "ideal_phase_reference",
            labels["ideal_phase_reference"],
            preserves_boundary_split=False,
            completion_restores_or_routes_away=True,
            note="Ideal reference routes away from the finite exact packet.",
        ),
    )


def _invariant_variants() -> tuple[ReferencePolicyVariant, ...]:
    return tuple(
        _variant(
            policy_id,
            "SYNTHETIC_POLICY_INVARIANT_SPLIT",
            preserves_boundary_split=True,
            completion_restores_or_routes_away=False,
            note="Synthetic target: the boundary split survives this policy variant.",
        )
        for policy_id in REQUIRED_REFERENCE_POLICIES
    )


def _precluded_variants(
    policy_independent: bool = True,
    declared_before_pair: bool = True,
) -> tuple[ReferencePolicyVariant, ...]:
    variants = [
        _variant(
            "finite_nonwrapping_exact_catalyst",
            "SYNTHETIC_FINITE_NONWRAPPING_SPLIT",
            preserves_boundary_split=True,
            completion_restores_or_routes_away=False,
            note="Synthetic target: finite non-wrapping split remains.",
        )
    ]
    for policy_id in REQUIRED_REFERENCE_POLICIES[1:]:
        variants.append(
            _variant(
                policy_id,
                "SYNTHETIC_INDEPENDENTLY_PRECLUDED_REFERENCE_VARIANT",
                preserves_boundary_split=False,
                completion_restores_or_routes_away=False,
                precluded_by_independent_theorem=True,
                preclusion_theorem_policy_independent=policy_independent,
                preclusion_declared_before_pair=declared_before_pair,
                note=(
                    "Synthetic target: this policy variant is not in the "
                    "admissible physical class by an independent theorem."
                ),
            )
        )
    return tuple(variants)


def candidates() -> tuple[ReferencePolicyCandidate, ...]:
    finite_only = (
        _variant(
            "finite_nonwrapping_exact_catalyst",
            "FINITE_ONLY_DECLARED_POLICY",
            preserves_boundary_split=True,
            completion_restores_or_routes_away=False,
            note="Finite policy selected without handling other reference variants.",
        ),
    )

    return (
        ReferencePolicyCandidate(
            candidate_id="current_t454_t455_t457_reference_policy_packet",
            description=(
                "The current integrated E3-region packet after T455 hostile review "
                "and T457 description-completion squeeze."
            ),
            source=f"{SOURCE_T454}; {SOURCE_T455}; {SOURCE_T457}",
            variants=_current_policy_variants(),
        ),
        ReferencePolicyCandidate(
            candidate_id="finite_policy_only_selection_control",
            description=(
                "A packet that declares only the finite non-wrapping policy and "
                "does not handle cyclic, consumed, or ideal references."
            ),
            source=ARTIFACT,
            variants=finite_only,
        ),
        ReferencePolicyCandidate(
            candidate_id="synthetic_reference_policy_invariant_target",
            description=(
                "Synthetic target: the boundary split survives finite non-wrapping, "
                "cyclic, consumed, and ideal reference policies."
            ),
            source=ARTIFACT,
            variants=_invariant_variants(),
            synthetic_control_only=True,
        ),
        ReferencePolicyCandidate(
            candidate_id="synthetic_reference_policy_preclusion_target",
            description=(
                "Synthetic target: non-finite variants are precluded by a "
                "policy-independent theorem declared before pair selection."
            ),
            source=ARTIFACT,
            variants=_precluded_variants(),
            synthetic_control_only=True,
        ),
        ReferencePolicyCandidate(
            candidate_id="synthetic_policy_dependent_preclusion_control",
            description="A preclusion packet whose exclusions are policy-relative.",
            source=ARTIFACT,
            variants=_precluded_variants(policy_independent=False),
            synthetic_control_only=True,
        ),
        ReferencePolicyCandidate(
            candidate_id="synthetic_post_hoc_preclusion_control",
            description="A preclusion packet whose exclusions are post-hoc.",
            source=ARTIFACT,
            variants=_precluded_variants(declared_before_pair=False),
            synthetic_control_only=True,
        ),
        ReferencePolicyCandidate(
            candidate_id="hidden_label_policy_control",
            description="A policy gate that reads hidden case labels.",
            source=ARTIFACT,
            variants=_invariant_variants(),
            reads_hidden_label_or_case_id=True,
            synthetic_control_only=True,
        ),
        ReferencePolicyCandidate(
            candidate_id="post_hoc_reference_scope_control",
            description="A packet that chooses the reference scope after the pair.",
            source=ARTIFACT,
            variants=_invariant_variants(),
            reference_scope_declared_before_pair=False,
            synthetic_control_only=True,
        ),
        ReferencePolicyCandidate(
            candidate_id="synthetic_missing_negative_control",
            description="A future-shaped packet missing its negative control.",
            source=ARTIFACT,
            variants=_invariant_variants(),
            negative_control_present=False,
            synthetic_control_only=True,
        ),
    )


def _t457_current_summary() -> dict[str, Any]:
    result = t457.run()
    current = next(
        item
        for item in result["candidate_evaluations"]
        if item["candidate_id"] == "current_t454_boundary_resource_description"
    )
    return {
        "verdict": result["overall_verdict"]["verdict"],
        "current_t454_class_label": current["gate_label"],
        "current_t454_class_factors_through_description": current[
            "factorization_audit"
        ]["capability_factors_through_description"],
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
        if item["candidate_id"] == "current_t454_t455_t457_reference_policy_packet"
    )

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t454": SOURCE_T454,
            "t455": SOURCE_T455,
            "t456": SOURCE_T456,
            "t457": SOURCE_T457,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Sharpen T456's reference-policy invariance/preclusion blocker for "
            "the current integrated E3-region route."
        ),
        "t457_import_summary": _t457_current_summary(),
        "required_reference_policies": list(REQUIRED_REFERENCE_POLICIES),
        "candidate_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "current_packet_label": current["gate_label"],
            "current_packet_unhandled_reference_policies": current[
                "reference_policy_audit"
            ]["unhandled_reference_policies"],
            "admitted_candidate_ids": [item["candidate_id"] for item in admitted],
            "admitted_candidates_are_synthetic_only": all(
                item["candidate"]["synthetic_control_only"] for item in admitted
            ),
            "current_artifacts_admitted_for_stronger_posture": False,
            "region_discriminator_success": False,
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "The current T454/T455/T457 packet remains reference-policy "
                "relative. It preserves the split only for the finite "
                "non-wrapping exact-catalyst policy; cyclic, consumed, and ideal "
                "reference variants are unhandled because they restore completion "
                "or route away and have not been independently precluded."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Do not seek stronger posture from the current finite non-wrapping policy packet.",
            "Future Direction-A packets must either make the split invariant across cyclic, consumed, and ideal reference policies or preclude those policies by an independent theorem.",
            "If the reference-policy gate cannot be cleared, demote the integrated E3-region route to a useful negative guardrail after the theorem-supply blocker is also audited.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    rows = [
        "| {candidate_id} | {admitted} | {label} | {missing} | {unhandled} |".format(
            candidate_id=item["candidate_id"],
            admitted="yes" if item["admitted_future_target"] else "no",
            label=item["gate_label"],
            missing=", ".join(item["missing_requirements"]) or "none",
            unhandled=", ".join(
                item["reference_policy_audit"]["unhandled_reference_policies"]
            )
            or "none",
        )
        for item in result["candidate_evaluations"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T458 - Reference-Policy Invariance Gate - v0.1 results",
            "",
            "> Admission/guardrail gate only. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T458-reference-policy-invariance-gate.md`",
            "- Model: `models/reference_policy_invariance_gate.py`",
            "- Tests: `tests/test_reference_policy_invariance_gate.py`",
            "- Artifact JSON: `results/T458-reference-policy-invariance-gate-v0.1.json`",
            "- Sources: T454, T455, T456, T457, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Required Reference Policies",
            "",
            *[f"- `{policy}`" for policy in result["required_reference_policies"]],
            "",
            "## Candidate Evaluation",
            "",
            "| candidate | admitted? | gate label | missing requirements | unhandled policies |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a sharper guardrail for T456's reference-policy blocker. It "
            "shows the current integrated E3-region route remains finite-policy "
            "relative rather than invariant or independently precluded.",
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
        json_path = results_dir / "T458-reference-policy-invariance-gate-v0.1.json"
        md_path = (
            results_dir / "T458-reference-policy-invariance-gate-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
