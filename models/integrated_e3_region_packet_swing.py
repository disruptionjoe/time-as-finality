"""T454 - integrated E3-region packet swing.

T453 left a precise target: a future Direction-A packet cannot merely cite the
T447 finite exact no-go. It must tie that exact witness to the same completion
that would otherwise restore factorization in the region-indexed packet.

T454 builds that finite toy integration. A region pair matches all declared
R-supported observations and interventions. A boundary menu splits revision
capability. The named completion that would repair the deficient side is an
exact charge-completion through a finite non-wrapping catalyst with exact return;
T447's nilpotent-shift certificate blocks that completion.

Recorded-tier review target only. This is not a region-indexed discriminator
success, not a quantum physics theorem, not a WAY theorem, not a GU/TaF adapter,
and not claim support.

Run:

    python -m models.integrated_e3_region_packet_swing --write-results
    python -m pytest tests/test_integrated_e3_region_packet_swing.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import quantum_e3_exact_no_go_big_swing as t447


ARTIFACT = "T454-integrated-e3-region-packet-swing-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T445 = "results/T445-region-capability-substrate-law-big-swing-v0.1-results.md"
SOURCE_T447 = "results/T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md"
SOURCE_T452 = "results/T452-law-sector-nonadmissibility-gate-v0.1-results.md"
SOURCE_T453 = (
    "results/T453-e3-to-region-nonadmissibility-adapter-gate-v0.1-results.md"
)
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "INTEGRATED_E3_REGION_PACKET_ADMITTED_REVIEW_TARGET_NO_PROMOTION"

HONEST_CEILING = (
    "Recorded-tier finite toy integration only. T454 admits one integrated "
    "E3-region packet as a review target because the exact no-go witness is tied "
    "to the named completion. The result remains below discriminator success: "
    "the policy is finite and declared, cyclic/consumed/ideal references route "
    "away, and law-sector description still explains which side has the boundary "
    "resource. It is not a quantum physics theorem, not a WAY theorem, not a "
    "GU/TaF adapter, not claim-ledger movement, and not public posture."
)

R_MENU = (
    "read_verdict",
    "append_neutral_annotation",
    "try_local_revise",
    "certify_verdict",
)
BOUNDARY_MENU = R_MENU + ("revise_with_boundary_charge",)
REVISION_CHARGE_DELTA = 1


@dataclass(frozen=True)
class RegionCase:
    case_id: str
    verdict_payload: str = "same"
    region_charge: int = 0
    correction_budget: int = 1
    boundary_charge_available: int = 0
    record_support: str = "matched_final_record_cell"
    provenance_state: str = "matched_valid_provenance"
    control_class: str = "charge_respecting_control"
    hidden_selector_label: str | None = None


@dataclass(frozen=True)
class CompletionPolicy:
    policy_id: str
    completion_kind: str
    declared_before_pair: bool = True
    exact_witness_predeclared: bool = True
    exact_witness_targets_named_completion: bool = True
    exact_catalyst_return_required: bool = True
    total_charge_conservation_required: bool = True
    reference_dimension: int | None = 5
    reads_hidden_label_or_case_id: bool = False
    negative_control_present: bool = True


@dataclass(frozen=True)
class IntegratedCandidate:
    candidate_id: str
    description: str
    source: str
    left: RegionCase
    right: RegionCase
    completion_policy: CompletionPolicy
    has_region_pair: bool = True
    frozen_operation_class: bool = True


def _case_to_dict(case: RegionCase) -> dict[str, Any]:
    return asdict(case)


def _policy_to_dict(policy: CompletionPolicy) -> dict[str, Any]:
    return asdict(policy)


def _charge_neutral(delta: int, boundary_charge: int) -> bool:
    return (delta + boundary_charge) % 2 == 0


def _r_visible_projection(case: RegionCase) -> dict[str, Any]:
    return {
        "verdict_payload": case.verdict_payload,
        "region_charge": case.region_charge,
        "correction_budget": case.correction_budget,
        "record_support": case.record_support,
        "provenance_state": case.provenance_state,
        "control_class": case.control_class,
        "operation_menu": list(R_MENU),
        "observable_algebra": "R_record_and_R_charge_only",
        "boundary_charge_available": "not_in_R_algebra",
    }


def _r_observation_signature(case: RegionCase) -> dict[str, Any]:
    return {
        "verdict_distribution": {case.verdict_payload: 1.0},
        "region_charge_distribution": {str(case.region_charge): 1.0},
        "visible_revision_budget": case.correction_budget,
        "boundary_charge_observable": "not_in_R_algebra",
    }


def _apply_r_intervention(case: RegionCase, intervention: str) -> dict[str, Any]:
    base = _r_observation_signature(case)
    if intervention == "read_verdict":
        return base | {"intervention_outcome": "read_same"}
    if intervention == "append_neutral_annotation":
        return base | {"intervention_outcome": "neutral_annotation_appended"}
    if intervention == "try_local_revise":
        allowed = _charge_neutral(REVISION_CHARGE_DELTA, 0)
        return base | {
            "intervention_outcome": "local_revision_allowed"
            if allowed
            else "local_revision_blocked",
            "failure_mode": "requires_boundary_charge" if not allowed else "none",
        }
    if intervention == "certify_verdict":
        return base | {"intervention_outcome": "certified_without_revision"}
    raise ValueError(f"unknown R intervention: {intervention}")


def _r_intervention_signature(case: RegionCase) -> dict[str, dict[str, Any]]:
    return {
        intervention: _apply_r_intervention(case, intervention)
        for intervention in R_MENU
    }


def region_equality_certificate(left: RegionCase, right: RegionCase) -> dict[str, Any]:
    left_projection = _r_visible_projection(left)
    right_projection = _r_visible_projection(right)
    left_observation = _r_observation_signature(left)
    right_observation = _r_observation_signature(right)
    left_interventions = _r_intervention_signature(left)
    right_interventions = _r_intervention_signature(right)

    return {
        "r_visible_projection_equal": left_projection == right_projection,
        "observational_statistics_equal": left_observation == right_observation,
        "interventional_statistics_equal": left_interventions == right_interventions,
        "tested_r_interventions": list(R_MENU),
        "left_r_projection": left_projection,
        "right_r_projection": right_projection,
        "left_r_interventions": left_interventions,
        "right_r_interventions": right_interventions,
    }


def _capability(case: RegionCase, menu: tuple[str, ...]) -> dict[str, Any]:
    admitted_boundary_charge = (
        case.boundary_charge_available
        if "revise_with_boundary_charge" in menu
        else 0
    )
    boundary_revise_allowed = (
        "revise_with_boundary_charge" in menu
        and _charge_neutral(REVISION_CHARGE_DELTA, admitted_boundary_charge)
    )
    can_revise = case.correction_budget > 0 and boundary_revise_allowed
    return {
        "can_read_verdict": "read_verdict" in menu,
        "can_append_neutral_annotation": "append_neutral_annotation" in menu,
        "can_certify_verdict": "certify_verdict" in menu,
        "can_revise_final_verdict": can_revise,
        "revision_blocked_reason": "none"
        if can_revise
        else "requires_admitted_boundary_charge",
        "available_boundary_charge": admitted_boundary_charge,
    }


def _differing_fields(left: dict[str, Any], right: dict[str, Any]) -> list[str]:
    return [key for key, value in left.items() if value != right.get(key)]


def _pair_audit(left: RegionCase, right: RegionCase) -> dict[str, Any]:
    r_only_left = _capability(left, R_MENU)
    r_only_right = _capability(right, R_MENU)
    boundary_left = _capability(left, BOUNDARY_MENU)
    boundary_right = _capability(right, BOUNDARY_MENU)
    return {
        "left": _case_to_dict(left),
        "right": _case_to_dict(right),
        "region_equality_certificate": region_equality_certificate(left, right),
        "r_only_capability": {
            "left": r_only_left,
            "right": r_only_right,
            "differs": r_only_left != r_only_right,
            "differing_fields": _differing_fields(r_only_left, r_only_right),
        },
        "boundary_capability": {
            "left": boundary_left,
            "right": boundary_right,
            "differs": boundary_left != boundary_right,
            "differing_fields": _differing_fields(boundary_left, boundary_right),
        },
    }


def _description_factorization_check() -> dict[str, Any]:
    cases = (
        RegionCase("boundary_charge_0", boundary_charge_available=0),
        RegionCase("boundary_charge_1", boundary_charge_available=1),
        RegionCase("boundary_charge_1_copy", boundary_charge_available=1),
    )
    violations: list[dict[str, str]] = []
    matched_description_pairs = 0
    checked_pairs = 0

    for index, left in enumerate(cases):
        for right in cases[index + 1 :]:
            checked_pairs += 1
            if left.boundary_charge_available != right.boundary_charge_available:
                continue
            matched_description_pairs += 1
            if _capability(left, BOUNDARY_MENU) != _capability(right, BOUNDARY_MENU):
                violations.append({"left": left.case_id, "right": right.case_id})

    return {
        "checked_pairs": checked_pairs,
        "matched_law_sector_description_pairs": matched_description_pairs,
        "violations": violations,
        "capability_factors_through_boundary_charge_description": not violations,
        "ceiling_reading": (
            "Admitting the boundary-charge descriptor still explains which side "
            "has the boundary resource. T454's positive result is therefore an "
            "operational nonadmissibility review target, not a claim that the "
            "state-description absorber has vanished."
        ),
    }


def _completion_audit(policy: CompletionPolicy) -> dict[str, Any]:
    certificate: dict[str, Any] | None = None
    completion_nonadmissible = False
    completion_restores = False

    if policy.completion_kind == "finite_nonwrapping_exact_catalyst":
        if policy.reference_dimension is None:
            label = "NOT_ADMITTED_REFERENCE_DIMENSION_MISSING"
            reason = "The finite reference dimension must be declared."
        elif not policy.exact_catalyst_return_required:
            label = "RESOURCE_COMPLETION_REFERENCE_MAY_CHANGE_NOT_EXACT_E3"
            reason = "Without exact catalyst return, the reference can be spent."
        elif not policy.total_charge_conservation_required:
            label = "NOT_STRUCTURAL_NO_CONSERVATION_RULE"
            reason = "The structural charge rule is missing."
        else:
            certificate = t447.finite_nonwrapping_shift_certificate(
                policy.reference_dimension
            )
            completion_nonadmissible = True
            label = "NAMED_COMPLETION_BLOCKED_BY_FINITE_NONWRAPPING_E3_NO_GO"
            reason = (
                "The named completion would require a nonzero unit-modulus "
                "eigenvector of a finite non-wrapping shift. T447's nilpotent "
                "certificate blocks that exact catalytic completion."
            )
    elif policy.completion_kind == "finite_cyclic_reference":
        if policy.reference_dimension is None:
            label = "NOT_ADMITTED_REFERENCE_DIMENSION_MISSING"
            reason = "The cyclic reference dimension must be declared."
        else:
            certificate = t447.cyclic_shift_control_certificate(policy.reference_dimension)
            completion_restores = True
            label = "COMPLETION_RESTORED_BY_CYCLIC_REFERENCE_CONTROL"
            reason = (
                "A cyclic reference has shift eigenvectors, so the non-wrapping "
                "nilpotent no-go does not apply."
            )
    elif policy.completion_kind == "consumed_charge_battery":
        completion_restores = True
        label = "RESOURCE_COMPLETION_ROUTES_AWAY_FROM_EXACT_CATALYTIC_E3"
        reason = "A consumed charge battery restores the task by changing resource state."
    elif policy.completion_kind == "ideal_phase_reference":
        completion_restores = True
        label = "IDEAL_REFERENCE_ROUTES_TO_IDEAL_OR_LIMIT_POLICY"
        reason = "An ideal reference is outside the finite exact-catalyst packet."
    elif policy.completion_kind == "description_only":
        label = "E0_DESCRIPTION_COMPLETION_ABSORBS_NO_E3_WITNESS"
        reason = (
            "Admitting the boundary-charge descriptor explains the split, but does "
            "not supply an exact operational no-go for changing the deficient side."
        )
    else:
        label = "UNKNOWN_COMPLETION_POLICY"
        reason = "The completion policy is not recognized."

    return {
        "policy": _policy_to_dict(policy),
        "certificate": certificate,
        "completion_physically_nonadmissible_under_declared_policy": (
            completion_nonadmissible
        ),
        "completion_restores_or_routes_away": completion_restores,
        "completion_label": label,
        "reason": reason,
    }


def _t452_requirement_check(
    candidate: IntegratedCandidate, pair_audit: dict[str, Any], completion: dict[str, Any]
) -> dict[str, Any]:
    policy = candidate.completion_policy
    checks = {
        "clear_t434_region_law_shape": candidate.has_region_pair,
        "match_r_statistics_and_interventions": bool(
            pair_audit["region_equality_certificate"]["observational_statistics_equal"]
            and pair_audit["region_equality_certificate"][
                "interventional_statistics_equal"
            ]
        ),
        "boundary_menu_splits_capability": pair_audit["boundary_capability"]["differs"],
        "law_sector_completion_named": bool(policy.policy_id),
        "allowed_operations_frozen": candidate.frozen_operation_class,
        "a2_resource_lift_audited": policy.completion_kind
        in {
            "finite_nonwrapping_exact_catalyst",
            "finite_cyclic_reference",
            "consumed_charge_battery",
            "ideal_phase_reference",
        },
        "exact_nonadmissibility_witness_predeclared": (
            policy.exact_witness_predeclared
        ),
        "exact_witness_targets_named_completion": (
            policy.exact_witness_targets_named_completion
        ),
        "negative_control_present": policy.negative_control_present,
        "completion_physically_nonadmissible": completion[
            "completion_physically_nonadmissible_under_declared_policy"
        ],
    }
    return {
        "checks": checks,
        "all_checks_pass": all(checks.values()),
    }


def evaluate_candidate(candidate: IntegratedCandidate) -> dict[str, Any]:
    pair = _pair_audit(candidate.left, candidate.right)
    completion = _completion_audit(candidate.completion_policy)
    requirements = _t452_requirement_check(candidate, pair, completion)
    admitted = False

    policy = candidate.completion_policy
    if policy.reads_hidden_label_or_case_id:
        label = "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
        reason = "The completion policy reads a hidden case label."
    elif not policy.declared_before_pair:
        label = "BLOCKED_POST_HOC_COMPLETION_POLICY"
        reason = "The completion policy is selected after the pair."
    elif not candidate.has_region_pair:
        label = "NOT_REGION_INDEXED_BASE_PACKET_MISSING"
        reason = "The candidate lacks the region-indexed equality and split packet."
    elif not pair["boundary_capability"]["differs"]:
        label = "NOT_ADMITTED_NO_BOUNDARY_CAPABILITY_SPLIT"
        reason = "The boundary menu does not separate the capability object."
    elif not policy.exact_witness_predeclared:
        label = "NOT_ADMITTED_NO_PREDECLARED_EXACT_WITNESS"
        reason = "The exact witness is not frozen before scoring the packet."
    elif not policy.exact_witness_targets_named_completion:
        label = "NOT_ADMITTED_EXACT_WITNESS_NOT_TIED_TO_COMPLETION"
        reason = "The exact witness does not forbid the named completion."
    elif not policy.negative_control_present:
        label = "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
        reason = "A nearby negative control is required."
    elif completion["completion_restores_or_routes_away"]:
        label = completion["completion_label"]
        reason = completion["reason"]
    elif not completion["completion_physically_nonadmissible_under_declared_policy"]:
        label = completion["completion_label"]
        reason = completion["reason"]
    elif not requirements["all_checks_pass"]:
        label = "NOT_ADMITTED_T452_REQUIREMENT_MISSING"
        missing = [
            key for key, value in requirements["checks"].items() if value is False
        ]
        reason = f"The packet misses T452 requirements: {', '.join(missing)}."
    else:
        admitted = True
        label = "ADMITTED_INTEGRATED_E3_REGION_REVIEW_TARGET_NO_PROMOTION"
        reason = (
            "The packet has matched R statistics/interventions, a boundary split, "
            "a named completion, a frozen operation class, A2 controls, and a "
            "T447-style exact no-go tied to that completion."
        )

    return {
        "candidate_id": candidate.candidate_id,
        "description": candidate.description,
        "source": candidate.source,
        "candidate": {
            "left": _case_to_dict(candidate.left),
            "right": _case_to_dict(candidate.right),
            "completion_policy": _policy_to_dict(policy),
            "has_region_pair": candidate.has_region_pair,
            "frozen_operation_class": candidate.frozen_operation_class,
        },
        "pair_audit": pair,
        "completion_audit": completion,
        "t452_requirement_check": requirements,
        "admitted_review_target": admitted,
        "integrated_label": label,
        "reason": reason,
    }


def _policy(
    policy_id: str,
    completion_kind: str = "finite_nonwrapping_exact_catalyst",
    declared_before_pair: bool = True,
    exact_witness_predeclared: bool = True,
    exact_witness_targets_named_completion: bool = True,
    exact_catalyst_return_required: bool = True,
    total_charge_conservation_required: bool = True,
    reference_dimension: int | None = 5,
    reads_hidden_label_or_case_id: bool = False,
    negative_control_present: bool = True,
) -> CompletionPolicy:
    return CompletionPolicy(
        policy_id=policy_id,
        completion_kind=completion_kind,
        declared_before_pair=declared_before_pair,
        exact_witness_predeclared=exact_witness_predeclared,
        exact_witness_targets_named_completion=exact_witness_targets_named_completion,
        exact_catalyst_return_required=exact_catalyst_return_required,
        total_charge_conservation_required=total_charge_conservation_required,
        reference_dimension=reference_dimension,
        reads_hidden_label_or_case_id=reads_hidden_label_or_case_id,
        negative_control_present=negative_control_present,
    )


def _cases() -> dict[str, RegionCase]:
    return {
        "compensator_available": RegionCase(
            case_id="compensator_available",
            boundary_charge_available=1,
        ),
        "compensator_deficit": RegionCase(
            case_id="compensator_deficit",
            boundary_charge_available=0,
        ),
        "matched_available_copy": RegionCase(
            case_id="matched_available_copy",
            boundary_charge_available=1,
        ),
        "hidden_alpha": RegionCase(
            case_id="hidden_alpha",
            boundary_charge_available=0,
            hidden_selector_label="alpha",
        ),
        "hidden_beta": RegionCase(
            case_id="hidden_beta",
            boundary_charge_available=0,
            hidden_selector_label="beta",
        ),
    }


def candidates() -> tuple[IntegratedCandidate, ...]:
    cases = _cases()
    main_left = cases["compensator_available"]
    main_right = cases["compensator_deficit"]

    return (
        IntegratedCandidate(
            candidate_id="main_integrated_nonwrapping_e3_region_packet",
            description=(
                "Finite integrated target: the deficient side can be repaired "
                "only by the named finite non-wrapping exact-catalyst completion, "
                "which T447 blocks."
            ),
            source=f"{SOURCE_T445}; {SOURCE_T447}; {SOURCE_T452}; {SOURCE_T453}",
            left=main_left,
            right=main_right,
            completion_policy=_policy("exact_charge_completion_nonwrapping"),
        ),
        IntegratedCandidate(
            candidate_id="cyclic_reference_completion_control",
            description="Cyclic reference control where the nilpotent no-go does not apply.",
            source=SOURCE_T447,
            left=main_left,
            right=main_right,
            completion_policy=_policy(
                "cyclic_reference_completion",
                completion_kind="finite_cyclic_reference",
            ),
        ),
        IntegratedCandidate(
            candidate_id="consumed_battery_completion_control",
            description="Consumed battery control routes to resource completion.",
            source=SOURCE_T447,
            left=main_left,
            right=main_right,
            completion_policy=_policy(
                "consumed_battery_completion",
                completion_kind="consumed_charge_battery",
                exact_catalyst_return_required=False,
                reference_dimension=None,
            ),
        ),
        IntegratedCandidate(
            candidate_id="ideal_reference_completion_control",
            description="Ideal reference control routes away from the finite packet.",
            source=SOURCE_T447,
            left=main_left,
            right=main_right,
            completion_policy=_policy(
                "ideal_reference_completion",
                completion_kind="ideal_phase_reference",
                reference_dimension=None,
            ),
        ),
        IntegratedCandidate(
            candidate_id="description_only_completion_control",
            description="Admitting the boundary-charge descriptor explains the split.",
            source=SOURCE_T445,
            left=main_left,
            right=main_right,
            completion_policy=_policy(
                "description_only_completion",
                completion_kind="description_only",
                reference_dimension=None,
            ),
        ),
        IntegratedCandidate(
            candidate_id="post_hoc_completion_policy_control",
            description="Post-hoc completion policy is blocked.",
            source=ARTIFACT,
            left=main_left,
            right=main_right,
            completion_policy=_policy(
                "post_hoc_completion",
                declared_before_pair=False,
            ),
        ),
        IntegratedCandidate(
            candidate_id="hidden_label_completion_policy_control",
            description="Hidden-label completion policy is blocked.",
            source=ARTIFACT,
            left=cases["hidden_alpha"],
            right=cases["hidden_beta"],
            completion_policy=_policy(
                "hidden_label_completion",
                reads_hidden_label_or_case_id=True,
            ),
        ),
        IntegratedCandidate(
            candidate_id="missing_region_pair_control",
            description="Bare exact witness with no region-indexed pair is blocked.",
            source=SOURCE_T447,
            left=main_left,
            right=main_right,
            completion_policy=_policy("missing_region_pair_completion"),
            has_region_pair=False,
        ),
        IntegratedCandidate(
            candidate_id="missing_negative_control",
            description="A nearby integrated packet with no negative control is blocked.",
            source=ARTIFACT,
            left=main_left,
            right=main_right,
            completion_policy=_policy(
                "missing_negative_control",
                negative_control_present=False,
            ),
        ),
        IntegratedCandidate(
            candidate_id="matched_boundary_no_split_control",
            description="Matched boundary sector proves the detector rejects no-split pairs.",
            source=ARTIFACT,
            left=main_left,
            right=cases["matched_available_copy"],
            completion_policy=_policy("matched_boundary_no_split"),
        ),
    )


def run() -> dict[str, Any]:
    evaluations = [evaluate_candidate(candidate) for candidate in candidates()]
    main = next(
        item
        for item in evaluations
        if item["candidate_id"] == "main_integrated_nonwrapping_e3_region_packet"
    )
    admitted = [item for item in evaluations if item["admitted_review_target"]]
    description_ceiling = _description_factorization_check()

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t445": SOURCE_T445,
            "t447": SOURCE_T447,
            "t452": SOURCE_T452,
            "t453": SOURCE_T453,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Execute T453's named next target: integrate a T447-style exact no-go "
            "with the same region-packet completion that would otherwise repair "
            "the deficient side."
        ),
        "declared_packet": {
            "region": "R sees final record payload, local charge, provenance, and R menu only",
            "capability_object": "availability of revise_final_verdict under the boundary menu",
            "boundary_split": "boundary charge 1 can revise; boundary charge 0 cannot",
            "named_completion": (
                "exact charge completion through a finite non-wrapping catalyst "
                "with exact return"
            ),
            "exact_witness": "T447 finite nilpotent shift has no nonzero unit-modulus eigenvector",
            "negative_controls": [
                "cyclic reference",
                "consumed battery",
                "ideal reference",
                "description-only completion",
                "post-hoc policy",
                "hidden label",
                "missing region pair",
                "missing negative control",
                "matched boundary no-split pair",
            ],
        },
        "candidate_evaluations": evaluations,
        "description_factorization_ceiling": description_ceiling,
        "overall_verdict": {
            "verdict": VERDICT,
            "main_candidate_admitted": main["admitted_review_target"],
            "main_candidate_label": main["integrated_label"],
            "admitted_candidate_ids": [item["candidate_id"] for item in admitted],
            "region_discriminator_success": False,
            "description_completion_still_explains_boundary_state": description_ceiling[
                "capability_factors_through_boundary_charge_description"
            ],
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T454 realizes T453's synthetic target as a finite toy review "
                "packet. The exact no-go witness is tied to the named completion "
                "that would repair the deficient region case. The result remains "
                "recorded-tier only: cyclic, consumed, and ideal references route "
                "away, and law-sector description still explains which side has "
                "the boundary resource."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Use T454 as the finite integrated review target, not as a theorem.",
            "Run hostile review before any stronger Direction-A posture movement.",
            "A stronger packet must make the boundary resource itself less declared and handle cyclic, consumed, and ideal reference policies.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    packet = result["declared_packet"]
    rows = [
        "| {candidate_id} | {admitted} | {label} |".format(
            candidate_id=item["candidate_id"],
            admitted="yes" if item["admitted_review_target"] else "no",
            label=item["integrated_label"],
        )
        for item in result["candidate_evaluations"]
    ]
    req_rows = [
        "| {name} | {value} |".format(name=name, value="yes" if value else "no")
        for name, value in next(
            item
            for item in result["candidate_evaluations"]
            if item["candidate_id"] == "main_integrated_nonwrapping_e3_region_packet"
        )["t452_requirement_check"]["checks"].items()
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T454 - Integrated E3 Region Packet Swing - v0.1 results",
            "",
            "> Recorded-tier finite toy integration. `CLAIM-LEDGER.md`, "
            "`TESTS.md`, `ROADMAP.md`, README, North Star files, public posture, "
            "hard policy, and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T454-integrated-e3-region-packet-swing.md`",
            "- Model: `models/integrated_e3_region_packet_swing.py`",
            "- Tests: `tests/test_integrated_e3_region_packet_swing.py`",
            "- Artifact JSON: `results/T454-integrated-e3-region-packet-swing-v0.1.json`",
            "- Sources: T445, T447, T452, T453, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Declared Packet",
            "",
            f"- Region: {packet['region']}",
            f"- Capability object: {packet['capability_object']}",
            f"- Boundary split: {packet['boundary_split']}",
            f"- Named completion: {packet['named_completion']}",
            f"- Exact witness: {packet['exact_witness']}",
            "",
            "## Main Packet T452 Checks",
            "",
            "| check | passes? |",
            "| --- | --- |",
            *req_rows,
            "",
            "## Candidate Evaluation",
            "",
            "| candidate | admitted? | integrated label |",
            "| --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a finite integrated E3-region review target. The main packet "
            "ties T447's nilpotent-shift no-go to the named completion that would "
            "otherwise repair the deficient side.",
            "",
            "Does not earn: a region-indexed discriminator success, a real "
            "substrate law, a quantum physics theorem, a WAY theorem, a GU/TaF "
            "adapter, claim-ledger movement, public posture, or cross-repo support.",
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
        json_path = results_dir / "T454-integrated-e3-region-packet-swing-v0.1.json"
        md_path = (
            results_dir / "T454-integrated-e3-region-packet-swing-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
