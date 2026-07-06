"""T455 - T454 hostile-review gate.

T454 built the first integrated E3-region review target after T453. This file
audits that packet as a hostile reviewer would before any stronger Direction-A
posture movement.

The result is intentionally conservative: T454 survives as a finite integrated
review target, but the hostile objections that T454 itself named still fire.
Law-sector description explains which side has the boundary resource, cyclic /
consumed / ideal reference policies route away from the finite exact packet, and
the artifact does not yet supply a new region theorem beyond the T454 bookkeeping
plus the T447 finite no-go.

Run:

    python -m models.t454_hostile_review_gate --write-results
    python -m pytest tests/test_t454_hostile_review_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import integrated_e3_region_packet_swing as t454


ARTIFACT = "T455-t454-hostile-review-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T447 = "results/T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md"
SOURCE_T452 = "results/T452-law-sector-nonadmissibility-gate-v0.1-results.md"
SOURCE_T453 = "results/T453-e3-to-region-nonadmissibility-adapter-gate-v0.1-results.md"
SOURCE_T454 = "results/T454-integrated-e3-region-packet-swing-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "T454_SURVIVES_HOSTILE_REVIEW_AS_REVIEW_TARGET_PROMOTION_BLOCKED"

HONEST_CEILING = (
    "Hostile-review gate only. T455 preserves T454 as a finite integrated "
    "review target while blocking any stronger Direction-A posture movement. "
    "It does not prove a region-indexed discriminator, real substrate law, "
    "quantum physics theorem, WAY theorem, GU/TaF adapter, claim support, or "
    "public posture."
)


@dataclass(frozen=True)
class ReviewCheck:
    check_id: str
    question: str
    status: str
    passed: bool
    evidence: tuple[str, ...]
    residual_risk: str
    gate_class: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["evidence"] = list(self.evidence)
        return data


def _artifact() -> dict[str, Any]:
    return t454.run()


def _candidate(result: dict[str, Any], candidate_id: str) -> dict[str, Any]:
    return next(
        item
        for item in result["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def _main_packet(result: dict[str, Any]) -> dict[str, Any]:
    return _candidate(result, "main_integrated_nonwrapping_e3_region_packet")


def _region_packet_check(result: dict[str, Any]) -> ReviewCheck:
    main = _main_packet(result)
    cert = main["pair_audit"]["region_equality_certificate"]
    r_only = main["pair_audit"]["r_only_capability"]
    boundary = main["pair_audit"]["boundary_capability"]

    passed = (
        cert["r_visible_projection_equal"] is True
        and cert["observational_statistics_equal"] is True
        and cert["interventional_statistics_equal"] is True
        and r_only["differs"] is False
        and boundary["differs"] is True
        and boundary["left"]["can_revise_final_verdict"] is True
        and boundary["right"]["can_revise_final_verdict"] is False
    )
    return ReviewCheck(
        check_id="region_packet_mechanical_correctness",
        question=(
            "Does T454 actually match R-supported data while splitting only under "
            "the boundary menu?"
        ),
        status="PASS" if passed else "FAIL",
        passed=passed,
        evidence=(
            "T454 main pair has equal R visible projection.",
            "T454 main pair has equal observational and R-interventional signatures.",
            "R-only capability does not split; boundary menu splits can_revise_final_verdict.",
        ),
        residual_risk=(
            "This is correctness of the finite packet, not evidence that the "
            "boundary resource is physically non-declared."
        ),
        gate_class="survival",
    )


def _exact_witness_integration_check(result: dict[str, Any]) -> ReviewCheck:
    main = _main_packet(result)
    completion = main["completion_audit"]
    certificate = completion["certificate"] or {}
    checks = main["t452_requirement_check"]["checks"]

    passed = (
        main["admitted_review_target"] is True
        and main["integrated_label"]
        == "ADMITTED_INTEGRATED_E3_REGION_REVIEW_TARGET_NO_PROMOTION"
        and checks["exact_witness_targets_named_completion"] is True
        and checks["completion_physically_nonadmissible"] is True
        and completion["completion_label"]
        == "NAMED_COMPLETION_BLOCKED_BY_FINITE_NONWRAPPING_E3_NO_GO"
        and certificate.get("reference_model") == "finite_nonwrapping_charge_ladder"
        and certificate.get("has_nonzero_unit_modulus_eigenvector") is False
    )
    return ReviewCheck(
        check_id="exact_witness_tied_to_named_completion",
        question=(
            "Is the T447-style exact no-go tied to the same completion that "
            "would repair the deficient side?"
        ),
        status="PASS" if passed else "FAIL",
        passed=passed,
        evidence=(
            "T454 main packet names exact charge completion through a finite non-wrapping catalyst.",
            "T454 imports the T447 nilpotent-shift certificate for that completion.",
            "T452 exact-witness and completion-nonadmissibility checks pass for the main packet.",
        ),
        residual_risk=(
            "The witness is tied to a declared finite non-wrapping exact-catalyst "
            "policy only; it does not cover cyclic, consumed, or ideal references."
        ),
        gate_class="survival",
    )


def _control_discipline_check(result: dict[str, Any]) -> ReviewCheck:
    expected_labels = {
        "cyclic_reference_completion_control": "COMPLETION_RESTORED_BY_CYCLIC_REFERENCE_CONTROL",
        "consumed_battery_completion_control": "RESOURCE_COMPLETION_ROUTES_AWAY_FROM_EXACT_CATALYTIC_E3",
        "ideal_reference_completion_control": "IDEAL_REFERENCE_ROUTES_TO_IDEAL_OR_LIMIT_POLICY",
        "description_only_completion_control": "E0_DESCRIPTION_COMPLETION_ABSORBS_NO_E3_WITNESS",
        "post_hoc_completion_policy_control": "BLOCKED_POST_HOC_COMPLETION_POLICY",
        "hidden_label_completion_policy_control": "BLOCKED_HIDDEN_LABEL_OR_CASE_ID",
        "missing_region_pair_control": "NOT_REGION_INDEXED_BASE_PACKET_MISSING",
        "missing_negative_control": "NOT_ADMITTED_NO_NEGATIVE_CONTROL",
        "matched_boundary_no_split_control": "NOT_ADMITTED_NO_BOUNDARY_CAPABILITY_SPLIT",
    }
    actual = {
        item["candidate_id"]: item["integrated_label"]
        for item in result["candidate_evaluations"]
        if item["candidate_id"] in expected_labels
    }
    admitted = result["overall_verdict"]["admitted_candidate_ids"]
    passed = actual == expected_labels and admitted == [
        "main_integrated_nonwrapping_e3_region_packet"
    ]
    return ReviewCheck(
        check_id="negative_controls_keep_scope_narrow",
        question="Do T454 controls reject nearby overreads?",
        status="PASS" if passed else "FAIL",
        passed=passed,
        evidence=(
            "Cyclic, consumed, ideal, and description-only completions are not admitted as the main result.",
            "Post-hoc, hidden-label, missing-region, missing-control, and no-split packets are rejected.",
            "Only the main integrated packet is admitted as a review target.",
        ),
        residual_risk=(
            "The controls narrow T454; they also expose why the result cannot be "
            "read as a stable Direction-A success."
        ),
        gate_class="survival",
    )


def _description_absorber_objection(result: dict[str, Any]) -> ReviewCheck:
    ceiling = result["description_factorization_ceiling"]
    fires = (
        ceiling["capability_factors_through_boundary_charge_description"] is True
        and ceiling["violations"] == []
    )
    return ReviewCheck(
        check_id="law_sector_description_absorber_still_fires",
        question=(
            "Does admitting the boundary-charge description still explain the "
            "capability split?"
        ),
        status="FIRES" if fires else "CLEARED",
        passed=not fires,
        evidence=(
            "T454 description-factorization check reports no violations.",
            "Capability factors through the boundary-charge description once that descriptor is admitted.",
            "T454 itself records this as the honest ceiling below discriminator success.",
        ),
        residual_risk=(
            "The packet remains below region-indexed discriminator success because "
            "a lawful description still says which side has the boundary resource."
        ),
        gate_class="promotion_block",
    )


def _reference_policy_fragility_objection(result: dict[str, Any]) -> ReviewCheck:
    cyclic = _candidate(result, "cyclic_reference_completion_control")
    consumed = _candidate(result, "consumed_battery_completion_control")
    ideal = _candidate(result, "ideal_reference_completion_control")
    fires = (
        cyclic["integrated_label"] == "COMPLETION_RESTORED_BY_CYCLIC_REFERENCE_CONTROL"
        and consumed["integrated_label"]
        == "RESOURCE_COMPLETION_ROUTES_AWAY_FROM_EXACT_CATALYTIC_E3"
        and ideal["integrated_label"] == "IDEAL_REFERENCE_ROUTES_TO_IDEAL_OR_LIMIT_POLICY"
    )
    return ReviewCheck(
        check_id="reference_policy_fragility_still_fires",
        question=(
            "Does the positive packet depend on the declared finite non-wrapping "
            "exact-catalyst policy?"
        ),
        status="FIRES" if fires else "CLEARED",
        passed=not fires,
        evidence=(
            "Cyclic reference control restores completion.",
            "Consumed battery control routes to resource completion.",
            "Ideal reference control routes away from the finite exact packet.",
        ),
        residual_risk=(
            "The T447 witness remains policy-relative. A stronger packet must "
            "preclude, not merely exclude, these reference policies."
        ),
        gate_class="promotion_block",
    )


def _product_decomposition_objection(result: dict[str, Any]) -> ReviewCheck:
    main = _main_packet(result)
    cert = main["pair_audit"]["region_equality_certificate"]
    certificate = main["completion_audit"]["certificate"] or {}
    has_region_part = (
        cert["observational_statistics_equal"] is True
        and cert["interventional_statistics_equal"] is True
        and main["pair_audit"]["boundary_capability"]["differs"] is True
    )
    has_t447_part = (
        certificate.get("reference_model") == "finite_nonwrapping_charge_ladder"
        and certificate.get("has_nonzero_unit_modulus_eigenvector") is False
    )
    no_extra_coupling_theorem = (
        result["overall_verdict"]["region_discriminator_success"] is False
        and result["claim_ledger_update"] == "none; no claim promotion"
    )
    fires = has_region_part and has_t447_part and no_extra_coupling_theorem
    return ReviewCheck(
        check_id="no_new_region_theorem_beyond_integration",
        question=(
            "Does T454 prove a new coupling theorem beyond the region packet plus "
            "the T447 no-go?"
        ),
        status="FIRES" if fires else "CLEARED",
        passed=not fires,
        evidence=(
            "T454 combines a correct finite region packet with the T447 finite non-wrapping certificate.",
            "T454 records region_discriminator_success as false.",
            "No minimality, uniqueness, or policy-independent coupling theorem is claimed or supplied.",
        ),
        residual_risk=(
            "This is acceptable for a review target, but it blocks a stronger "
            "Direction-A posture move."
        ),
        gate_class="promotion_block",
    )


def _promotion_posture_objection() -> ReviewCheck:
    return ReviewCheck(
        check_id="stronger_direction_a_posture_blocked",
        question="Does T455 authorize claim, roadmap, public, or cross-repo movement?",
        status="BLOCKED",
        passed=False,
        evidence=(
            "T454 is recorded-tier only.",
            "The hostile objections above still fire.",
            "Repo governance forbids changing public posture or cross-repo truth here.",
        ),
        residual_risk=(
            "Any future promotion requires a new artifact that clears the "
            "description-completion and reference-policy objections."
        ),
        gate_class="promotion_block",
    )


def run() -> dict[str, Any]:
    result = _artifact()
    survival_checks = (
        _region_packet_check(result),
        _exact_witness_integration_check(result),
        _control_discipline_check(result),
    )
    hostile_objections = (
        _description_absorber_objection(result),
        _reference_policy_fragility_objection(result),
        _product_decomposition_objection(result),
        _promotion_posture_objection(),
    )
    fired_objections = [
        check.check_id
        for check in hostile_objections
        if check.status in {"FIRES", "BLOCKED"}
    ]
    survives_as_review_target = all(check.passed for check in survival_checks)
    stronger_posture_earned = survives_as_review_target and not fired_objections

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t447": SOURCE_T447,
            "t452": SOURCE_T452,
            "t453": SOURCE_T453,
            "t454": SOURCE_T454,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Run hostile review on T454 before any stronger Direction-A posture "
            "movement."
        ),
        "survival_checks": [check.to_dict() for check in survival_checks],
        "hostile_objections": [check.to_dict() for check in hostile_objections],
        "overall_verdict": {
            "verdict": VERDICT,
            "t454_survives_as_review_target": survives_as_review_target,
            "fired_objection_ids": fired_objections,
            "stronger_direction_a_posture_earned": stronger_posture_earned,
            "region_discriminator_success": False,
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T454 survives hostile review only at the level it claimed: a "
                "finite integrated review target. Its region equality, boundary "
                "split, exact-witness integration, and negative controls check "
                "out. Promotion remains blocked because law-sector description "
                "still explains the boundary resource, cyclic/consumed/ideal "
                "reference policies route away, and no new policy-independent "
                "region theorem is supplied."
            ),
        },
        "recommended_next": [
            "Keep T454 as a recorded-tier review target, not a Direction-A success.",
            "Do not move claim ledger, TESTS, roadmap, North Star, public posture, or cross-repo truth from T454/T455.",
            "A stronger packet must make the boundary resource less descriptive and handle cyclic, consumed, and ideal reference policies.",
            "If no such packet can be typed, demote the integrated E3-region route to a useful negative/guardrail lane.",
        ],
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    survival_rows = [
        "| {check_id} | {status} | {risk} |".format(
            check_id=item["check_id"],
            status=item["status"],
            risk=item["residual_risk"],
        )
        for item in result["survival_checks"]
    ]
    objection_rows = [
        "| {check_id} | {status} | {risk} |".format(
            check_id=item["check_id"],
            status=item["status"],
            risk=item["residual_risk"],
        )
        for item in result["hostile_objections"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T455 - T454 Hostile Review Gate - v0.1 results",
            "",
            "> Recorded-tier hostile-review gate. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T455-t454-hostile-review-gate.md`",
            "- Model: `models/t454_hostile_review_gate.py`",
            "- Tests: `tests/test_t454_hostile_review_gate.py`",
            "- Artifact JSON: `results/T455-t454-hostile-review-gate-v0.1.json`",
            "- Sources: T447, T452, T453, T454, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Survival Checks",
            "",
            "| check | status | residual risk |",
            "| --- | --- | --- |",
            *survival_rows,
            "",
            "## Hostile Objections",
            "",
            "| objection | status | residual risk |",
            "| --- | --- | --- |",
            *objection_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: local hostile-review clearance for preserving T454 as a finite "
            "integrated review target.",
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
        json_path = results_dir / "T455-t454-hostile-review-gate-v0.1.json"
        md_path = results_dir / "T455-t454-hostile-review-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
