"""T543: APRD reconstruction-boundary descent packet.

T542 selected APRD / reconstruction-boundary descent as the next non-rank
TAF11 packet after T539 retired the programmable rank route. This module makes
APRD executable as a set-valued access/provenance reconstruction-debt object.

APRD is deliberately not a scalar score. It records which typed sections are
needed for reconstruction and which of those sections are inaccessible,
underdeclared, or only supplied by a native absorber.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import gap_phantom_equivalence as t58
from models import povm_detector_calibration_obstruction as t66
from models import t542_post_retirement_source_law_reassessment_router as t542


ARTIFACT = "T543-aprd-reconstruction-boundary-descent-packet-v0.1"
VERDICT = "aprd_boundary_object_built_source_law_not_earned"
APRD_STATUS = "SUPPORTED_FEEDER_NATIVE_ABSORBER_BOUNDARY"
NEXT_PACKET = "t544_aprd_minimality_and_absorber_separation_gate"

NOT_CLAIMED = (
    "T543 does not establish a source law, prove a shadow-protection theorem, "
    "derive spacetime, prove manifoldlikeness, repair T528, reverse T223, "
    "unpause S1, promote S1, change claim status, change Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, or move cross-repo truth. It defines and "
    "stress-tests an APRD boundary object only."
)


@dataclass(frozen=True)
class APRDCase:
    case_id: str
    source_test: str
    role: str
    required_sections: tuple[str, ...]
    accessible_sections: tuple[str, ...]
    expected_debt_ids: tuple[str, ...]
    expected_classification: str
    native_absorber_available: bool = False
    threshold_rule_declared: bool = True
    provenance_rule_declared: bool = True
    local_is_suborder: bool = True
    scalar_rank_proxy_used: bool = False
    target_statistic_import_used: bool = False
    lorentzian_reference_import_used: bool = False


@dataclass(frozen=True)
class APRDEvaluation:
    case_id: str
    source_test: str
    role: str
    debt_ids: tuple[str, ...]
    missing_sections: tuple[str, ...]
    reconstruction_complete: bool
    classification: str
    reproduces_reference_burden: bool
    native_absorber_available: bool
    counts_as_source_law_evidence: bool
    reason: str


@dataclass(frozen=True)
class ControlEvaluation:
    control_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T543Result:
    artifact: str
    source_t542_verdict: str
    source_t542_selected_family: str
    source_t58_t51_gap_equals_phantoms: bool
    source_t58_extension_condition_necessary: bool
    source_t66_threshold_verdict_flips: bool
    source_t66_independence_verdict_flips: bool
    aprd_definition: dict[str, Any]
    evaluations: tuple[APRDEvaluation, ...]
    controls: tuple[ControlEvaluation, ...]
    reproduced_reference_burdens: tuple[str, ...]
    native_absorber_collapse_found: bool
    aprd_status: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    taf11_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t543_analysis() -> T543Result:
    t542_result = t542.run_t542_analysis()
    t58_result = t58.run_t58_audit()
    t66_result = t66.run_t66_analysis()

    cases = _reference_cases(t58_result, t66_result)
    evaluations = tuple(evaluate_aprd_case(case) for case in cases)
    controls = _controls(evaluations)
    reproduced = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.role == "reference_burden"
        and evaluation.reproduces_reference_burden
    )
    native_absorber_collapse = any(
        evaluation.native_absorber_available
        and evaluation.classification == "reproduced_but_native_absorbed"
        for evaluation in evaluations
    )
    source_law_evidence_count = sum(
        1 for evaluation in evaluations if evaluation.counts_as_source_law_evidence
    )
    verdict = (
        VERDICT
        if t542_result.verdict == t542.VERDICT
        and t542_result.selected_family_ids == (t542.SELECTED_FAMILY,)
        and t58_result.t51_gap_equals_phantoms
        and t58_result.extension_condition_necessary
        and t66_result.threshold_obstruction.verdict_flips
        and t66_result.independence_obstruction.verdict_flips
        and len(reproduced) == 4
        and native_absorber_collapse
        and source_law_evidence_count < len(reproduced)
        and all(control.passed for control in controls)
        else "aprd_packet_unexpected_status"
    )

    return T543Result(
        artifact=ARTIFACT,
        source_t542_verdict=t542_result.verdict,
        source_t542_selected_family=t542_result.selected_family_ids[0],
        source_t58_t51_gap_equals_phantoms=t58_result.t51_gap_equals_phantoms,
        source_t58_extension_condition_necessary=(
            t58_result.extension_condition_necessary
        ),
        source_t66_threshold_verdict_flips=(
            t66_result.threshold_obstruction.verdict_flips
        ),
        source_t66_independence_verdict_flips=(
            t66_result.independence_obstruction.verdict_flips
        ),
        aprd_definition=_aprd_definition(),
        evaluations=evaluations,
        controls=controls,
        reproduced_reference_burdens=reproduced,
        native_absorber_collapse_found=native_absorber_collapse,
        aprd_status=APRD_STATUS,
        verdict=verdict,
        strongest_reading=(
            "APRD is a coherent set-valued reconstruction-boundary object for "
            "the declared fixtures: it reproduces T19 access-boundary debt, "
            "T66 threshold/provenance debt, and T51/T58 phantom-gap descent "
            "debt without scalar rank, target statistics, or Lorentzian "
            "reference import. It does not yet earn a source law because the "
            "T66 splits are explicitly absorbed by native detector threshold "
            "and provenance completion."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should test whether APRD has a minimal "
            "non-absorbed enrichment theorem: the debt object must be fixed "
            "before outcomes, remain set-valued, survive same-neighbor-data "
            "completion, and separate at least one non-detector native fixture "
            "without reducing to scalar rank."
        ),
        taf11_update=(
            "TAF11 remains open. T543 gives APRD a real executable object, but "
            "source-law status waits on a minimality and native-absorber "
            "separation gate."
        ),
        taf8_update=(
            "TAF8 remains waiting for a domain-native packet. APRD is a "
            "possible feeder because it supplies typed-gap and reconstruction "
            "boundary objects, but it does not prove cross-domain shadow "
            "protection."
        ),
        claim_labels=_claim_labels(reproduced, native_absorber_collapse),
        claim_ledger_update=(
            "No claim-ledger update is earned. T543 leaves claim rows, Canon "
            "Index tiers, and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def evaluate_aprd_case(case: APRDCase) -> APRDEvaluation:
    missing = tuple(
        section
        for section in case.required_sections
        if section not in case.accessible_sections
    )
    debt_ids = tuple(f"missing:{section}" for section in missing)
    if not case.threshold_rule_declared:
        debt_ids += ("underdeclared:threshold_rule",)
    if not case.provenance_rule_declared:
        debt_ids += ("underdeclared:provenance_rule",)

    forbidden_import = (
        case.scalar_rank_proxy_used
        or case.target_statistic_import_used
        or case.lorentzian_reference_import_used
    )
    if forbidden_import:
        classification = "rejected_forbidden_rank_or_import"
        reason = (
            "The packet used scalar rank, target statistics, or Lorentzian "
            "reference import, which T542 excluded before execution."
        )
    elif not case.local_is_suborder:
        classification = "invalid_extension_boundary"
        reason = (
            "Local apparent order is not a suborder of the ambient order, so "
            "the gap is a conflict boundary rather than phantom descent debt."
        )
    elif case.native_absorber_available and debt_ids:
        classification = "reproduced_but_native_absorbed"
        reason = (
            "APRD detects the debt, but a native completion explains the split "
            "under the same access/provenance data."
        )
    elif debt_ids:
        classification = "aprd_reconstruction_boundary_detected"
        reason = (
            "The required reconstruction sections are typed and missing from "
            "the declared access profile."
        )
    else:
        classification = "positive_control_no_debt"
        reason = "All declared reconstruction sections are accessible."

    reproduces = (
        tuple(sorted(debt_ids)) == tuple(sorted(case.expected_debt_ids))
        and classification == case.expected_classification
    )
    counts_as_source_law_evidence = (
        reproduces
        and case.role == "reference_burden"
        and classification == "aprd_reconstruction_boundary_detected"
        and not case.native_absorber_available
    )
    return APRDEvaluation(
        case_id=case.case_id,
        source_test=case.source_test,
        role=case.role,
        debt_ids=tuple(sorted(debt_ids)),
        missing_sections=tuple(sorted(missing)),
        reconstruction_complete=not debt_ids,
        classification=classification,
        reproduces_reference_burden=reproduces,
        native_absorber_available=case.native_absorber_available,
        counts_as_source_law_evidence=counts_as_source_law_evidence,
        reason=reason,
    )


def t543_result_to_dict(result: T543Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t542_verdict": result.source_t542_verdict,
        "source_t542_selected_family": result.source_t542_selected_family,
        "source_t58_t51_gap_equals_phantoms": (
            result.source_t58_t51_gap_equals_phantoms
        ),
        "source_t58_extension_condition_necessary": (
            result.source_t58_extension_condition_necessary
        ),
        "source_t66_threshold_verdict_flips": (
            result.source_t66_threshold_verdict_flips
        ),
        "source_t66_independence_verdict_flips": (
            result.source_t66_independence_verdict_flips
        ),
        "aprd_definition": result.aprd_definition,
        "evaluations": [
            {
                "case_id": evaluation.case_id,
                "source_test": evaluation.source_test,
                "role": evaluation.role,
                "debt_ids": list(evaluation.debt_ids),
                "missing_sections": list(evaluation.missing_sections),
                "reconstruction_complete": evaluation.reconstruction_complete,
                "classification": evaluation.classification,
                "reproduces_reference_burden": (
                    evaluation.reproduces_reference_burden
                ),
                "native_absorber_available": evaluation.native_absorber_available,
                "counts_as_source_law_evidence": (
                    evaluation.counts_as_source_law_evidence
                ),
                "reason": evaluation.reason,
            }
            for evaluation in result.evaluations
        ],
        "controls": [
            {
                "control_id": control.control_id,
                "passed": control.passed,
                "reason": control.reason,
            }
            for control in result.controls
        ],
        "reproduced_reference_burdens": list(result.reproduced_reference_burdens),
        "native_absorber_collapse_found": result.native_absorber_collapse_found,
        "aprd_status": result.aprd_status,
        "verdict": result.verdict,
        "strongest_reading": result.strongest_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _aprd_definition() -> dict[str, Any]:
    return {
        "name": "accessible_provenance_reconstruction_debt",
        "abbreviation": "APRD",
        "kind": "set_valued_boundary_object",
        "inputs": [
            "access_profile",
            "provenance_axis",
            "required_reconstruction_sections",
            "accessible_sections",
            "threshold_rule",
            "local_apparent_order",
            "ambient_descent_order",
            "native_absorber_outcome",
        ],
        "rule": (
            "APRD is the typed set of required reconstruction sections that "
            "are absent from the observer-accessible sections, plus explicit "
            "underdeclared threshold/provenance obligations. It is evaluated "
            "only when the local apparent order is a suborder of the ambient "
            "descent order."
        ),
        "not_a_scalar": True,
        "forbidden_shortcuts": [
            "scalar_rank_proxy",
            "target_statistic_import",
            "lorentzian_reference_import",
            "post_hoc_threshold_or_provenance_choice",
        ],
    }


def _reference_cases(
    t58_result: t58.T58Result, t66_result: t66.T66Result
) -> tuple[APRDCase, ...]:
    t51_observer_b = next(
        audit
        for audit in t58_result.observer_audits
        if audit.source_test == "T51" and audit.observer == "Observer_B"
    )
    if t51_observer_b.gap_pairs != t51_observer_b.phantom_pairs:
        t51_expected_gap = ("ambient_pair:t51_gap_mismatch",)
    else:
        t51_expected_gap = tuple(
            f"ambient_pair:{left}<={right}"
            for left, right in sorted(t51_observer_b.gap_pairs)
        )

    if not t66_result.threshold_obstruction.verdict_flips:
        threshold_expected = ("t66_threshold_no_flip",)
    else:
        threshold_expected = ("information_threshold_rule",)

    if not t66_result.independence_obstruction.verdict_flips:
        provenance_expected = ("t66_provenance_no_flip",)
    else:
        provenance_expected = ("provenance_partition",)

    return (
        APRDCase(
            case_id="t19_internal_self_finality_boundary",
            source_test="T19",
            role="reference_burden",
            required_sections=(
                "R_obs_internal_record",
                "R_self_finality_external_witness",
            ),
            accessible_sections=("R_obs_internal_record",),
            expected_debt_ids=("missing:R_self_finality_external_witness",),
            expected_classification="aprd_reconstruction_boundary_detected",
        ),
        APRDCase(
            case_id="t66_threshold_rule_boundary",
            source_test="T66",
            role="reference_burden",
            required_sections=(
                "povm_response_matrix",
                threshold_expected[0],
                "access_window",
                "provenance_partition",
            ),
            accessible_sections=(
                "povm_response_matrix",
                "access_window",
                "provenance_partition",
            ),
            expected_debt_ids=(
                f"missing:{threshold_expected[0]}",
                "underdeclared:threshold_rule",
            ),
            expected_classification="reproduced_but_native_absorbed",
            native_absorber_available=True,
            threshold_rule_declared=False,
        ),
        APRDCase(
            case_id="t66_provenance_partition_boundary",
            source_test="T66",
            role="reference_burden",
            required_sections=(
                "povm_response_matrix",
                "access_window",
                provenance_expected[0],
            ),
            accessible_sections=("povm_response_matrix", "access_window"),
            expected_debt_ids=(
                f"missing:{provenance_expected[0]}",
                "underdeclared:provenance_rule",
            ),
            expected_classification="reproduced_but_native_absorbed",
            native_absorber_available=True,
            provenance_rule_declared=False,
        ),
        APRDCase(
            case_id="t51_t58_observer_b_phantom_gap",
            source_test="T51/T58",
            role="reference_burden",
            required_sections=(
                t51_expected_gap[0],
                "provenance_record:r_A_locked",
            ),
            accessible_sections=("local_pair:e2_B_locking<=e3_composite_locking",),
            expected_debt_ids=(
                f"missing:{t51_expected_gap[0]}",
                "missing:provenance_record:r_A_locked",
            ),
            expected_classification="aprd_reconstruction_boundary_detected",
        ),
        APRDCase(
            case_id="t19_external_meta_positive_control",
            source_test="T19",
            role="positive_control",
            required_sections=(
                "R_obs_internal_record",
                "R_self_finality_external_witness",
            ),
            accessible_sections=(
                "R_obs_internal_record",
                "R_self_finality_external_witness",
            ),
            expected_debt_ids=(),
            expected_classification="positive_control_no_debt",
        ),
        APRDCase(
            case_id="t58_local_reversal_control",
            source_test="T58",
            role="hostile_control",
            required_sections=("ambient_pair:a<=b",),
            accessible_sections=("local_pair:b<=a",),
            expected_debt_ids=("missing:ambient_pair:a<=b",),
            expected_classification="invalid_extension_boundary",
            local_is_suborder=False,
        ),
        APRDCase(
            case_id="scalar_rank_proxy_control",
            source_test="T542",
            role="hostile_control",
            required_sections=("rank_depth_value",),
            accessible_sections=("rank_depth_value",),
            expected_debt_ids=(),
            expected_classification="rejected_forbidden_rank_or_import",
            scalar_rank_proxy_used=True,
        ),
        APRDCase(
            case_id="target_statistic_import_control",
            source_test="T542",
            role="hostile_control",
            required_sections=("target_ordering_fraction_band",),
            accessible_sections=("target_ordering_fraction_band",),
            expected_debt_ids=(),
            expected_classification="rejected_forbidden_rank_or_import",
            target_statistic_import_used=True,
        ),
        APRDCase(
            case_id="lorentzian_reference_import_control",
            source_test="T542",
            role="hostile_control",
            required_sections=("lorentzian_reference_coordinates",),
            accessible_sections=("lorentzian_reference_coordinates",),
            expected_debt_ids=(),
            expected_classification="rejected_forbidden_rank_or_import",
            lorentzian_reference_import_used=True,
        ),
    )


def _controls(evaluations: tuple[APRDEvaluation, ...]) -> tuple[ControlEvaluation, ...]:
    by_id = {evaluation.case_id: evaluation for evaluation in evaluations}
    return (
        ControlEvaluation(
            control_id="t542_source_family_consumed",
            passed=t542.run_t542_analysis().selected_family_ids
            == (t542.SELECTED_FAMILY,),
            reason="T543 consumes the APRD successor selected by T542.",
        ),
        ControlEvaluation(
            control_id="reference_burdens_reproduced",
            passed=all(
                evaluation.reproduces_reference_burden
                for evaluation in evaluations
                if evaluation.role == "reference_burden"
            ),
            reason="T19, T66, and T51/T58 burdens reproduce under APRD.",
        ),
        ControlEvaluation(
            control_id="positive_control_has_no_debt",
            passed=by_id["t19_external_meta_positive_control"].classification
            == "positive_control_no_debt",
            reason="The external T19 observer has all required sections.",
        ),
        ControlEvaluation(
            control_id="local_reversal_not_phantom",
            passed=by_id["t58_local_reversal_control"].classification
            == "invalid_extension_boundary",
            reason="T58's local-reversal control is blocked as conflict, not APRD.",
        ),
        ControlEvaluation(
            control_id="scalar_rank_target_lorentzian_shortcuts_reject",
            passed=all(
                by_id[case_id].classification == "rejected_forbidden_rank_or_import"
                for case_id in (
                    "scalar_rank_proxy_control",
                    "target_statistic_import_control",
                    "lorentzian_reference_import_control",
                )
            ),
            reason="T542-forbidden shortcuts reject before source-law reading.",
        ),
        ControlEvaluation(
            control_id="no_claim_or_posture_movement",
            passed=True,
            reason="T543 performs no claim, canon, public-posture, or external movement.",
        ),
    )


def _claim_labels(
    reproduced: tuple[str, ...], native_absorber_collapse: bool
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "APRD reproduces the declared reference burdens: "
                + ", ".join(reproduced)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "APRD rejects scalar-rank, target-statistic, and Lorentzian "
                "reference shortcuts in the hostile controls."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "A native absorber boundary is present."
                if native_absorber_collapse
                else "No native absorber boundary was detected."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "APRD is now a useful Track-1 feeder object, but source-law "
                "status requires a minimality and absorber-separation theorem."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T543 Results: APRD Reconstruction-Boundary Descent Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- APRD status: `{payload['aprd_status']}`",
        f"- Source T542 verdict: `{payload['source_t542_verdict']}`",
        f"- Source T542 selected family: `{payload['source_t542_selected_family']}`",
        f"- Native absorber boundary found: {payload['native_absorber_collapse_found']}",
        "",
        "## APRD Definition",
        "",
        f"- Kind: `{payload['aprd_definition']['kind']}`",
        f"- Rule: {payload['aprd_definition']['rule']}",
        "- Inputs: "
        + ", ".join(f"`{item}`" for item in payload["aprd_definition"]["inputs"]),
        "- Forbidden shortcuts: "
        + ", ".join(
            f"`{item}`" for item in payload["aprd_definition"]["forbidden_shortcuts"]
        ),
        "",
        "## Evaluations",
        "",
        "| case | source | role | classification | debt ids | reproduces? | source-law evidence? |",
        "| --- | --- | --- | --- | --- | :---: | :---: |",
    ]
    for evaluation in payload["evaluations"]:
        debt = ", ".join(f"`{item}`" for item in evaluation["debt_ids"]) or "none"
        lines.append(
            "| "
            f"`{evaluation['case_id']}` | "
            f"`{evaluation['source_test']}` | "
            f"`{evaluation['role']}` | "
            f"`{evaluation['classification']}` | "
            f"{debt} | "
            f"{evaluation['reproduces_reference_burden']} | "
            f"{evaluation['counts_as_source_law_evidence']} |"
        )
    lines.extend(["", "## Controls", ""])
    for control in payload["controls"]:
        lines.append(
            f"- `{control['control_id']}`: {control['passed']}. {control['reason']}"
        )
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Strongest Reading", "strongest_reading"),
        ("Recommended Next", "recommended_next"),
        ("TAF11 Update", "taf11_update"),
        ("TAF8 Update", "taf8_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def write_results(result: T543Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t543_result_to_dict(result)
    json_path = results_dir / "T543-aprd-reconstruction-boundary-descent-packet-v0.1.json"
    md_path = results_dir / "T543-aprd-reconstruction-boundary-descent-packet-v0.1-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t543_analysis()
    payload = t543_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
