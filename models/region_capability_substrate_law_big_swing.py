"""T445 - region capability substrate-law big swing.

T434 defined the admission burden left by T406: a future substrate-law packet
must force operation availability without restating a transition table. T445
tries a finite Z2 charge-conservation packet against the region-indexed
capability discriminator lane.

The result is deliberately conservative. The packet clears the T434 admission
shape and is not transition-table underdescription, but the split still factors
through explicit law-sector completion once the boundary compensator sector is
admitted. Recorded-tier only; no claim promotion follows.

Run:

    python -m models.region_capability_substrate_law_big_swing --write-results
    python -m pytest tests/test_region_capability_substrate_law_big_swing.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import substrate_law_admission_gate as t434


ARTIFACT = "T445-region-capability-substrate-law-big-swing-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T434 = "T434-substrate-law-admission-gate-v0.1"
SOURCE_T406 = "T406-transition-system-operation-unavailability-gate-v0.1"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = (
    "SUBSTRATE_LAW_PACKET_CLEARS_T434_NOT_TRANSITION_TABLE_UNDERDESCRIPTION_"
    "BUT_FACTORS_THROUGH_LAW_SECTOR_COMPLETION"
)

HONEST_CEILING = (
    "Recorded-tier finite substrate-law pressure test only. The packet clears "
    "T434 as a law-forced transition shape and avoids transition-table "
    "underdescription, but it is still absorbed by explicit law-sector "
    "completion. It is not a real physics law, not a WAY theorem, not a "
    "region-indexed discriminator success, and not claim-ledger movement."
)

R_MENU = (
    "read_verdict",
    "append_neutral_annotation",
    "try_local_revise",
    "certify_verdict",
)
BOUNDARY_MENU = R_MENU + ("revise_with_boundary_compensator",)
REFERENCE_MENU = BOUNDARY_MENU + ("borrow_reference_compensator",)

START_STATE = "final_verdict_same"
REVISED_STATE = "revised_verdict_same"
ANNOTATED_STATE = "neutral_annotation_appended"
CERTIFIED_STATE = "certified_verdict_same"
REVISION_CHARGE_DELTA = 1


@dataclass(frozen=True)
class RegionCase:
    case_id: str
    verdict_payload: str = "same"
    region_charge: int = 0
    correction_budget: int = 1
    complement_compensator_charge: int = 0
    record_support: str = "matched_final_record_cell"
    provenance_state: str = "matched_valid_provenance"
    control_class: str = "charge_respecting_control"
    hidden_selector_label: str | None = None


@dataclass(frozen=True)
class TransitionEdge:
    operation: str
    source: str
    target: str


def _charge_preserved(region_delta: int, compensator_charge: int) -> bool:
    return (region_delta + compensator_charge) % 2 == 0


def _available_compensator_charge(case: RegionCase, menu_policy: str) -> int:
    if menu_policy == "R_only":
        return 0
    if menu_policy == "boundary":
        return case.complement_compensator_charge
    if menu_policy == "reference_resource":
        return 1
    raise ValueError(f"unknown menu policy: {menu_policy}")


def _menu(menu_policy: str) -> tuple[str, ...]:
    if menu_policy == "R_only":
        return R_MENU
    if menu_policy == "boundary":
        return BOUNDARY_MENU
    if menu_policy == "reference_resource":
        return REFERENCE_MENU
    raise ValueError(f"unknown menu policy: {menu_policy}")


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
        "boundary_access": "not_admitted",
    }


def _fixed_accounting_projection(case: RegionCase) -> dict[str, Any]:
    projection = _r_visible_projection(case)
    projection["law_accounting"] = {
        "revision_charge_delta": REVISION_CHARGE_DELTA,
        "conservation_rule": "Z2 total charge must be preserved",
        "local_reference_resource": "not_admitted",
    }
    return projection


def _law_sector_completion(case: RegionCase, menu_policy: str) -> dict[str, Any]:
    completion = _fixed_accounting_projection(case)
    completion["menu_policy"] = menu_policy
    completion["admitted_compensator_charge"] = _available_compensator_charge(
        case, menu_policy
    )
    return completion


def _r_observation_signature(case: RegionCase) -> dict[str, Any]:
    return {
        "verdict_distribution": {case.verdict_payload: 1.0},
        "region_charge_distribution": {str(case.region_charge): 1.0},
        "visible_revision_budget": case.correction_budget,
        "boundary_compensator_observable": "not_in_R_algebra",
    }


def _apply_r_intervention(case: RegionCase, intervention: str) -> dict[str, Any]:
    base = _r_observation_signature(case)
    if intervention == "read_verdict":
        return base | {"intervention_outcome": "read_same"}
    if intervention == "append_neutral_annotation":
        return base | {"intervention_outcome": "neutral_annotation_appended"}
    if intervention == "try_local_revise":
        local_allowed = _charge_preserved(REVISION_CHARGE_DELTA, 0)
        return base | {
            "intervention_outcome": "local_revision_allowed"
            if local_allowed
            else "local_revision_blocked",
            "failure_mode": "requires_admitted_compensator"
            if not local_allowed
            else "none",
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


def _capability(case: RegionCase, menu_policy: str) -> dict[str, Any]:
    available_compensator = _available_compensator_charge(case, menu_policy)
    local_revise_allowed = (
        "try_local_revise" in _menu(menu_policy)
        and _charge_preserved(REVISION_CHARGE_DELTA, 0)
    )
    boundary_revise_allowed = (
        "revise_with_boundary_compensator" in _menu(menu_policy)
        and _charge_preserved(REVISION_CHARGE_DELTA, available_compensator)
    )
    reference_revise_allowed = (
        "borrow_reference_compensator" in _menu(menu_policy)
        and _charge_preserved(REVISION_CHARGE_DELTA, 1)
    )
    can_revise = (
        case.correction_budget > 0
        and (local_revise_allowed or boundary_revise_allowed or reference_revise_allowed)
    )
    return {
        "can_read_verdict": "read_verdict" in _menu(menu_policy),
        "can_append_neutral_annotation": "append_neutral_annotation" in _menu(menu_policy),
        "can_certify_verdict": "certify_verdict" in _menu(menu_policy),
        "can_revise_final_verdict": can_revise,
        "revision_blocked_reason": "none"
        if can_revise
        else "Z2_charge_conservation_without_admitted_compensator",
        "available_compensator_charge": available_compensator,
        "menu_policy": menu_policy,
    }


def _transition_edges(case: RegionCase, menu_policy: str) -> tuple[TransitionEdge, ...]:
    edges = [
        TransitionEdge("read_verdict", START_STATE, START_STATE),
        TransitionEdge("append_neutral_annotation", START_STATE, ANNOTATED_STATE),
        TransitionEdge("certify_verdict", START_STATE, CERTIFIED_STATE),
    ]
    if _capability(case, menu_policy)["can_revise_final_verdict"]:
        edges.append(TransitionEdge("revise_final_verdict", START_STATE, REVISED_STATE))
    return tuple(edges)


def _edge_key(edge: TransitionEdge) -> tuple[str, str, str]:
    return (edge.operation, edge.source, edge.target)


def _edges_to_dict(edges: tuple[TransitionEdge, ...]) -> list[dict[str, str]]:
    return [asdict(edge) for edge in sorted(edges, key=_edge_key)]


def _differing_fields(left: dict[str, Any], right: dict[str, Any]) -> list[str]:
    return [key for key, value in left.items() if value != right.get(key)]


def _case_to_dict(case: RegionCase) -> dict[str, Any]:
    return asdict(case)


def _pair_audit(
    pair_id: str, left: RegionCase, right: RegionCase, menu_policy: str
) -> dict[str, Any]:
    equality = region_equality_certificate(left, right)
    left_fixed = _fixed_accounting_projection(left)
    right_fixed = _fixed_accounting_projection(right)
    left_sector = _law_sector_completion(left, menu_policy)
    right_sector = _law_sector_completion(right, menu_policy)
    left_capability = _capability(left, menu_policy)
    right_capability = _capability(right, menu_policy)
    left_edges = _transition_edges(left, menu_policy)
    right_edges = _transition_edges(right, menu_policy)
    capability_differences = _differing_fields(left_capability, right_capability)
    hidden_selector_attempt = (
        left.hidden_selector_label is not None
        or right.hidden_selector_label is not None
    ) and left.hidden_selector_label != right.hidden_selector_label

    return {
        "pair_id": pair_id,
        "menu_policy": menu_policy,
        "left": _case_to_dict(left),
        "right": _case_to_dict(right),
        "region_equality_certificate": equality,
        "fixed_accounting_projection_equal": left_fixed == right_fixed,
        "law_sector_completion_equal": left_sector == right_sector,
        "transition_system_completion_equal": left_edges == right_edges,
        "left_derived_transition_edges": _edges_to_dict(left_edges),
        "right_derived_transition_edges": _edges_to_dict(right_edges),
        "capability": {
            "left": left_capability,
            "right": right_capability,
            "differs": bool(capability_differences),
            "differing_fields": capability_differences,
        },
        "hidden_selector_shortcut_attempt": hidden_selector_attempt,
    }


def _cases() -> dict[str, RegionCase]:
    return {
        "compensator_available": RegionCase(
            case_id="compensator_available",
            complement_compensator_charge=1,
        ),
        "no_compensator": RegionCase(
            case_id="no_compensator",
            complement_compensator_charge=0,
        ),
        "compensator_available_copy": RegionCase(
            case_id="compensator_available_copy",
            complement_compensator_charge=1,
        ),
        "visible_region_charge_control": RegionCase(
            case_id="visible_region_charge_control",
            region_charge=1,
            complement_compensator_charge=1,
        ),
        "hidden_alpha": RegionCase(
            case_id="hidden_alpha",
            complement_compensator_charge=1,
            hidden_selector_label="alpha",
        ),
        "hidden_beta": RegionCase(
            case_id="hidden_beta",
            complement_compensator_charge=1,
            hidden_selector_label="beta",
        ),
    }


def _law_package(
    package_id: str = "z2_charge_conservation_boundary_packet",
    source_kind: str = "conservation_law",
    declared_before_pair: bool = True,
    shared_formula_across_pair: bool = True,
    reads_transition_relation: bool = False,
    reads_case_id_or_hidden_label: bool = False,
    uses_allowed_substrate_observables: bool = True,
    preserves_fixed_accounting: bool = True,
    derives_declared_transition_relation: bool = True,
) -> t434.LawPackage:
    return t434.LawPackage(
        package_id=package_id,
        source_kind=source_kind,
        declared_before_pair=declared_before_pair,
        shared_formula_across_pair=shared_formula_across_pair,
        reads_transition_relation=reads_transition_relation,
        reads_case_id_or_hidden_label=reads_case_id_or_hidden_label,
        uses_allowed_substrate_observables=uses_allowed_substrate_observables,
        preserves_fixed_accounting=preserves_fixed_accounting,
        derives_declared_transition_relation=derives_declared_transition_relation,
        has_negative_control=True,
        formula=(
            "revise_final_verdict is admitted iff the local revision charge "
            "delta plus an admitted compensator charge is neutral mod 2"
        ),
        substrate_observables=(
            "revision_charge_delta",
            "admitted_compensator_charge",
            "total_Z2_charge_neutrality",
        ),
    )


def _t434_candidate(
    candidate_id: str,
    law_package: t434.LawPackage,
    fixed_accounting_projection_equal: bool = True,
    transition_system_completion_equal: bool = False,
) -> dict[str, Any]:
    candidate = t434.Candidate(
        candidate_id=candidate_id,
        description=(
            "T445 finite Z2 conservation-law packet deriving revision "
            "availability from admitted compensator charge."
        ),
        capability_split=True,
        fixed_accounting_projection_equal=fixed_accounting_projection_equal,
        transition_system_completion_equal=transition_system_completion_equal,
        law_package=law_package,
        synthetic_positive_control=False,
    )
    return t434.evaluate_candidate(candidate)


def _t434_admission_audits() -> dict[str, Any]:
    return {
        "main_z2_conservation_packet": _t434_candidate(
            "main_z2_conservation_packet", _law_package()
        ),
        "transition_table_restatement_control": _t434_candidate(
            "transition_table_restatement_control",
            _law_package(
                package_id="transition_table_restatement_control",
                source_kind="transition_table",
                reads_transition_relation=True,
                derives_declared_transition_relation=True,
            ),
        ),
        "post_hoc_law_control": _t434_candidate(
            "post_hoc_law_control",
            _law_package(
                package_id="post_hoc_law_control",
                declared_before_pair=False,
            ),
        ),
        "hidden_label_law_control": _t434_candidate(
            "hidden_label_law_control",
            _law_package(
                package_id="hidden_label_law_control",
                reads_case_id_or_hidden_label=True,
            ),
        ),
    }


def _pair_audits() -> list[dict[str, Any]]:
    cases = _cases()
    return [
        _pair_audit(
            "main_boundary_compensator_pair",
            cases["compensator_available"],
            cases["no_compensator"],
            "boundary",
        ),
        _pair_audit(
            "r_only_no_split_control",
            cases["compensator_available"],
            cases["no_compensator"],
            "R_only",
        ),
        _pair_audit(
            "reference_resource_lift_control",
            cases["compensator_available"],
            cases["no_compensator"],
            "reference_resource",
        ),
        _pair_audit(
            "matched_compensator_control",
            cases["compensator_available"],
            cases["compensator_available_copy"],
            "boundary",
        ),
        _pair_audit(
            "r_visible_charge_control",
            cases["compensator_available"],
            cases["visible_region_charge_control"],
            "boundary",
        ),
        _pair_audit(
            "hidden_selector_control",
            cases["hidden_alpha"],
            cases["hidden_beta"],
            "boundary",
        ),
    ]


def _completion_factorization_check() -> dict[str, Any]:
    cases = [
        _cases()["compensator_available"],
        _cases()["no_compensator"],
        _cases()["compensator_available_copy"],
    ]
    menu_policies = ("R_only", "boundary", "reference_resource")
    items = [(case, menu_policy) for case in cases for menu_policy in menu_policies]
    violations: list[dict[str, str]] = []
    matched_completion_pairs = 0
    checked_pairs = 0

    for index, (left_case, left_policy) in enumerate(items):
        for right_case, right_policy in items[index + 1 :]:
            checked_pairs += 1
            left_completion = _law_sector_completion(left_case, left_policy)
            right_completion = _law_sector_completion(right_case, right_policy)
            if left_completion != right_completion:
                continue
            matched_completion_pairs += 1
            if _capability(left_case, left_policy) != _capability(
                right_case, right_policy
            ):
                violations.append(
                    {
                        "left": left_case.case_id,
                        "left_policy": left_policy,
                        "right": right_case.case_id,
                        "right_policy": right_policy,
                    }
                )

    return {
        "checked_pairs": checked_pairs,
        "matched_law_sector_completion_pairs": matched_completion_pairs,
        "violations": violations,
        "capability_factors_through_law_sector_completion": not violations,
    }


def _absorber_audit(
    main_pair: dict[str, Any], t434_audits: dict[str, Any]
) -> dict[str, Any]:
    main_t434 = t434_audits["main_z2_conservation_packet"]
    restatement = t434_audits["transition_table_restatement_control"]
    reference = next(
        item for item in _pair_audits() if item["pair_id"] == "reference_resource_lift_control"
    )
    return {
        "t434_substrate_law_admission": {
            "status": "passes",
            "residue_label": main_t434["residue_label"],
            "reason": (
                "The Z2 packet is predeclared, shared, substrate-native, and "
                "derives boundary revision availability without reading edges."
            ),
        },
        "transition_table_underdescription": {
            "status": "does_not_fire_for_main_packet",
            "transition_table_restatement_admitted": restatement["admitted"],
            "reason": (
                "The main packet derives the revise edge from the conservation "
                "formula; the explicit transition-table restatement control is "
                "rejected by T434."
            ),
        },
        "r_supported_statistics_and_interventions": {
            "status": "matched_for_main_pair",
            "reason": (
                "The main pair has identical R-visible projections, observations, "
                "and all tested R-supported intervention signatures."
            ),
        },
        "forced_boundary_task_shape": {
            "status": "passes_shape_only",
            "reason": (
                "R-only local revision is blocked in both cases. Boundary revision "
                "is forced by the declared conservation formula because it needs "
                "an admitted compensator charge."
            ),
        },
        "ordinary_joint_record_or_law_sector_completion": {
            "status": "absorbs_recorded_result",
            "main_pair_law_sector_completion_equal": main_pair[
                "law_sector_completion_equal"
            ],
            "factorization_check": _completion_factorization_check(),
            "reason": (
                "Once the admitted compensator sector is added to the state "
                "description, capability factors. The result is not a new "
                "region-indexed discriminator success."
            ),
        },
        "resource_reference_lift": {
            "status": "relative_only",
            "reference_resource_pair_split": reference["capability"]["differs"],
            "reason": (
                "If a reference compensator resource is admitted, both sides can "
                "revise; the boundary split is relative to the declared A-class."
            ),
        },
        "causal_domain_and_latch_absorbers": {
            "status": "not_the_explaining_difference_here",
            "reason": (
                "The finite packet holds record payload, provenance, control, and "
                "local operation menu fixed. The live explaining difference is the "
                "law-sector compensator, not causal reachability or latch topology."
            ),
        },
        "claim_promotion": {
            "status": "blocked",
            "reason": "Recorded-tier pressure test only; no ledger or public posture move.",
        },
    }


def run() -> dict[str, Any]:
    pair_audits = _pair_audits()
    main_pair = next(
        item for item in pair_audits if item["pair_id"] == "main_boundary_compensator_pair"
    )
    r_only = next(
        item for item in pair_audits if item["pair_id"] == "r_only_no_split_control"
    )
    reference = next(
        item for item in pair_audits if item["pair_id"] == "reference_resource_lift_control"
    )
    t434_audits = _t434_admission_audits()
    main_t434 = t434_audits["main_z2_conservation_packet"]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t434": SOURCE_T434,
            "t406": SOURCE_T406,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Pressure-test whether a substrate-law packet can clear the post-T434 "
            "burden without becoming transition-table underdescription."
        ),
        "setup": {
            "law": "finite Z2 charge conservation",
            "region": "R observes only final-record payload and R charge sector",
            "capability_object": (
                "availability of revise_final_verdict under R-only, boundary, "
                "and reference-resource menus"
            ),
            "revision_charge_delta": REVISION_CHARGE_DELTA,
            "r_menu": list(R_MENU),
            "boundary_menu": list(BOUNDARY_MENU),
            "reference_menu": list(REFERENCE_MENU),
            "declared_before_pair": True,
        },
        "t434_admission_audits": t434_audits,
        "pair_audits": pair_audits,
        "absorber_audit": _absorber_audit(main_pair, t434_audits),
        "overall_verdict": {
            "verdict": VERDICT,
            "t434_main_packet_admitted": main_t434["admitted"],
            "main_pair_r_statistics_equal": main_pair[
                "region_equality_certificate"
            ]["observational_statistics_equal"],
            "main_pair_r_interventions_equal": main_pair[
                "region_equality_certificate"
            ]["interventional_statistics_equal"],
            "r_only_pair_splits": r_only["capability"]["differs"],
            "boundary_pair_splits": main_pair["capability"]["differs"],
            "reference_resource_pair_splits": reference["capability"]["differs"],
            "transition_table_restatement_rejected": not t434_audits[
                "transition_table_restatement_control"
            ]["admitted"],
            "law_sector_completion_absorbs": _completion_factorization_check()[
                "capability_factors_through_law_sector_completion"
            ],
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "The Z2 conservation packet is a real post-T434 shape in the "
                "finite model: it derives the revise edge from a predeclared law "
                "rather than from a transition table, while R-supported statistics "
                "and interventions remain equal. The honest ceiling is still "
                "absorptive: admitting the compensator sector restores ordinary "
                "law-sector factorization, and a reference resource removes the "
                "split."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Treat this as a recorded finite law-packet calibration, not a discriminator success.",
            "A stronger packet must make the law-sector completion itself physically non-admissible, not merely hidden from R.",
            "Keep future attempts paired with T434 admission and T436-style resource-lift reporting.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    rows = [
        "| {pair_id} | {menu_policy} | {r_equal} | {split} | {sector_equal} |".format(
            pair_id=item["pair_id"],
            menu_policy=item["menu_policy"],
            r_equal="yes"
            if item["region_equality_certificate"]["r_visible_projection_equal"]
            else "no",
            split="yes" if item["capability"]["differs"] else "no",
            sector_equal="yes" if item["law_sector_completion_equal"] else "no",
        )
        for item in result["pair_audits"]
    ]
    t434_rows = [
        "| {candidate} | {admitted} | {label} |".format(
            candidate=item["candidate_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["residue_label"],
        )
        for item in result["t434_admission_audits"].values()
    ]
    absorber_rows = [
        "| {name} | {status} |".format(name=name, status=audit["status"])
        for name, audit in result["absorber_audit"].items()
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T445 - Region Capability Substrate-Law Big Swing - v0.1 results",
            "",
            "> Recorded-tier pressure test. `TESTS.md`, `ROADMAP.md`, "
            "`CLAIM-LEDGER.md`, North Star, public posture, hard policy, and "
            "shared context are untouched.",
            "",
            "- Spec: `tests/T445-region-capability-substrate-law-big-swing.md`",
            "- Model: `models/region_capability_substrate_law_big_swing.py`",
            "- Tests: `tests/test_region_capability_substrate_law_big_swing.py`",
            "- Artifact JSON: `results/T445-region-capability-substrate-law-big-swing-v0.1.json`",
            "- Sources: T406, T434, T436 guardrail posture, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## T434 Admission Audit",
            "",
            "| candidate | admitted? | residue label |",
            "| --- | --- | --- |",
            *t434_rows,
            "",
            "## Pair Audit",
            "",
            "| pair | menu | R projection equal? | capability split? | law-sector completion equal? |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Absorber Audit",
            "",
            "| absorber | status |",
            "| --- | --- |",
            *absorber_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a finite packet showing that the post-T434 shape can clear "
            "the law-admission gate without merely restating a transition table.",
            "",
            "Does not earn: a region-indexed discriminator success, a real "
            "substrate law, a physics theorem, a WAY result, a claim-ledger "
            "update, public posture, or cross-repo support. The split is still "
            "absorbed by explicit law-sector completion.",
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
        json_path = results_dir / "T445-region-capability-substrate-law-big-swing-v0.1.json"
        md_path = results_dir / "T445-region-capability-substrate-law-big-swing-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
