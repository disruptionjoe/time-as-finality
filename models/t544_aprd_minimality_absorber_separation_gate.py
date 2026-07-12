"""T544: APRD minimality and absorber separation gate.

T543 built accessible provenance reconstruction debt (APRD) as a set-valued
boundary object. T544 asks the narrower next question: does that object survive
minimality and native-absorber separation strongly enough to remain a live
TAF11 source-law feeder?

The answer here is deliberately finite and bounded. A non-detector survivor is
useful evidence for the route, not a source law.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t543_aprd_reconstruction_boundary_descent_packet as t543


ARTIFACT = "T544-aprd-minimality-absorber-separation-gate-v0.1"
VERDICT = "aprd_minimality_gate_finds_nonabsorbed_provenance_survivor"
APRD_GATE_STATUS = "FINITE_MINIMAL_SURVIVOR_FOUND_SOURCE_LAW_NOT_EARNED"
NEXT_PACKET = "t545_aprd_refinement_stability_packet"

NOT_CLAIMED = (
    "T544 does not establish a source law, prove a shadow-protection theorem, "
    "derive spacetime, prove manifoldlikeness, repair T528, reverse T223, "
    "unpause S1, promote S1, change claim status, change Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, or move cross-repo truth. It is a finite "
    "APRD minimality and absorber-separation gate only."
)


@dataclass(frozen=True)
class APRDGateCase:
    case_id: str
    source_test: str
    role: str
    domain: str
    debt_ids: tuple[str, ...]
    same_neighbor_completion_ids: tuple[str, ...]
    separation_requires: tuple[str, ...]
    expected_classification: str
    fixed_before_outcome: bool
    set_valued: bool
    native_absorber_available: bool
    detector_fixture: bool
    scalar_rank_only: bool
    outcome_leakage: bool


@dataclass(frozen=True)
class APRDGateEvaluation:
    case_id: str
    source_test: str
    role: str
    domain: str
    debt_ids: tuple[str, ...]
    same_neighbor_completion_ids: tuple[str, ...]
    residual_debt_ids: tuple[str, ...]
    separation_requires: tuple[str, ...]
    classification: str
    expected_classification: str
    classification_matches_expected: bool
    minimal: bool
    non_detector_survivor: bool
    absorbed_by_native_completion: bool
    scalar_rank_signature: int
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
class T544Result:
    artifact: str
    source_t543_verdict: str
    source_t543_status: str
    gate_definition: dict[str, Any]
    evaluations: tuple[APRDGateEvaluation, ...]
    controls: tuple[ControlEvaluation, ...]
    non_detector_survivors: tuple[str, ...]
    native_absorber_cases: tuple[str, ...]
    rejected_controls: tuple[str, ...]
    same_rank_distinct_debt_pair_found: bool
    aprd_gate_status: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    taf11_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t544_analysis() -> T544Result:
    t543_result = t543.run_t543_analysis()
    cases = _gate_cases()
    evaluations = tuple(evaluate_gate_case(case) for case in cases)
    non_detector_survivors = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.non_detector_survivor
    )
    native_absorber_cases = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.absorbed_by_native_completion
    )
    rejected_controls = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.classification.startswith("rejected_")
    )
    same_rank_distinct_debt_pair = _same_rank_distinct_debt_pair(evaluations)
    controls = _controls(
        evaluations,
        non_detector_survivors,
        native_absorber_cases,
        rejected_controls,
        same_rank_distinct_debt_pair,
    )
    verdict = (
        VERDICT
        if t543_result.verdict == t543.VERDICT
        and t543_result.aprd_status == t543.APRD_STATUS
        and non_detector_survivors
        and "t66_detector_threshold_absorber_control" in native_absorber_cases
        and same_rank_distinct_debt_pair
        and all(control.passed for control in controls)
        else "aprd_minimality_gate_unexpected_status"
    )

    return T544Result(
        artifact=ARTIFACT,
        source_t543_verdict=t543_result.verdict,
        source_t543_status=t543_result.aprd_status,
        gate_definition=_gate_definition(),
        evaluations=evaluations,
        controls=controls,
        non_detector_survivors=non_detector_survivors,
        native_absorber_cases=native_absorber_cases,
        rejected_controls=rejected_controls,
        same_rank_distinct_debt_pair_found=same_rank_distinct_debt_pair,
        aprd_gate_status=APRD_GATE_STATUS,
        verdict=verdict,
        strongest_reading=(
            "APRD survives the finite T544 gate as a predeclared, set-valued, "
            "minimal boundary object on non-detector record/provenance "
            "fixtures, while detector threshold/provenance cases remain "
            "absorbed by native completion. This keeps TAF11 alive as a "
            "source-law feeder but does not establish a source law."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should test whether the surviving APRD "
            "debt sets are stable under refinement, relabeling, and restriction "
            "maps. If the survivor changes under harmless presentation changes, "
            "the route should narrow or retire before any theorem reading."
        ),
        taf11_update=(
            "TAF11 remains the live Track-1 route. T544 finds a finite "
            "non-detector APRD survivor, but source-law status still waits on "
            "refinement stability and functorial behavior."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T544 supplies a cleaner APRD feeder, not a shadow-protection "
            "transfer theorem."
        ),
        claim_labels=_claim_labels(
            non_detector_survivors,
            native_absorber_cases,
            same_rank_distinct_debt_pair,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T544 leaves claim rows, Canon "
            "Index tiers, and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def evaluate_gate_case(case: APRDGateCase) -> APRDGateEvaluation:
    debt_set = set(case.debt_ids)
    completed = set(case.same_neighbor_completion_ids)
    residual = tuple(sorted(debt_set - completed))
    required = set(case.separation_requires)
    absorbed = bool(case.native_absorber_available and debt_set and not residual)
    minimal_core = bool(residual and set(residual) == required)

    if case.outcome_leakage or not case.fixed_before_outcome:
        classification = "rejected_post_hoc_outcome_leakage"
        reason = "The debt object was not fixed before outcome inspection."
    elif case.scalar_rank_only or not case.set_valued:
        classification = "rejected_scalar_rank_collapse"
        reason = "The fixture replaced the APRD debt set with a scalar count."
    elif set(residual) > required and required:
        classification = "rejected_nonminimal_padding"
        reason = "The APRD set contains debt atoms not needed for separation."
    elif absorbed:
        classification = "native_absorbed_after_same_neighbor_completion"
        reason = (
            "Same-neighbor-data completion supplies the missing detector "
            "threshold/provenance sections under the native absorber."
        )
    elif minimal_core and not case.detector_fixture:
        classification = "minimal_nonabsorbed_separator"
        reason = (
            "The predeclared debt set remains after allowed completion and each "
            "atom is load-bearing for the finite separation."
        )
    elif not debt_set:
        classification = "positive_control_no_debt"
        reason = "No reconstruction debt is present after declared access."
    elif residual:
        classification = "residual_debt_review_only"
        reason = "Residual debt remains, but the fixture does not clear minimality."
    else:
        classification = "unexpected_gate_state"
        reason = "The fixture did not match a declared T544 gate branch."

    return APRDGateEvaluation(
        case_id=case.case_id,
        source_test=case.source_test,
        role=case.role,
        domain=case.domain,
        debt_ids=tuple(sorted(case.debt_ids)),
        same_neighbor_completion_ids=tuple(sorted(case.same_neighbor_completion_ids)),
        residual_debt_ids=residual,
        separation_requires=tuple(sorted(case.separation_requires)),
        classification=classification,
        expected_classification=case.expected_classification,
        classification_matches_expected=classification == case.expected_classification,
        minimal=classification == "minimal_nonabsorbed_separator",
        non_detector_survivor=(
            classification == "minimal_nonabsorbed_separator"
            and not case.detector_fixture
        ),
        absorbed_by_native_completion=absorbed,
        scalar_rank_signature=len(case.debt_ids),
        reason=reason,
    )


def t544_result_to_dict(result: T544Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t543_verdict": result.source_t543_verdict,
        "source_t543_status": result.source_t543_status,
        "gate_definition": result.gate_definition,
        "evaluations": [
            {
                "case_id": evaluation.case_id,
                "source_test": evaluation.source_test,
                "role": evaluation.role,
                "domain": evaluation.domain,
                "debt_ids": list(evaluation.debt_ids),
                "same_neighbor_completion_ids": list(
                    evaluation.same_neighbor_completion_ids
                ),
                "residual_debt_ids": list(evaluation.residual_debt_ids),
                "separation_requires": list(evaluation.separation_requires),
                "classification": evaluation.classification,
                "expected_classification": evaluation.expected_classification,
                "classification_matches_expected": (
                    evaluation.classification_matches_expected
                ),
                "minimal": evaluation.minimal,
                "non_detector_survivor": evaluation.non_detector_survivor,
                "absorbed_by_native_completion": (
                    evaluation.absorbed_by_native_completion
                ),
                "scalar_rank_signature": evaluation.scalar_rank_signature,
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
        "non_detector_survivors": list(result.non_detector_survivors),
        "native_absorber_cases": list(result.native_absorber_cases),
        "rejected_controls": list(result.rejected_controls),
        "same_rank_distinct_debt_pair_found": (
            result.same_rank_distinct_debt_pair_found
        ),
        "aprd_gate_status": result.aprd_gate_status,
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


def _gate_definition() -> dict[str, Any]:
    return {
        "name": "aprd_minimality_and_absorber_separation_gate",
        "source": "T543 APRD object",
        "required_properties": [
            "debt_object_fixed_before_outcomes",
            "set_valued_debt_ids_not_scalar_rank",
            "same_neighbor_data_completion_tested",
            "native_absorber_cases_absorb_when_completion_is_legitimate",
            "at_least_one_non_detector_fixture_survives_completion",
            "every_surviving_debt_atom_is_load_bearing",
        ],
        "survivor_reading": (
            "A finite survivor keeps APRD alive as a feeder object. It is not "
            "a source law until the debt object is stable under refinement, "
            "restriction, relabeling, and native morphisms."
        ),
    }


def _gate_cases() -> tuple[APRDGateCase, ...]:
    return (
        APRDGateCase(
            case_id="t66_detector_threshold_absorber_control",
            source_test="T66",
            role="native_absorber_control",
            domain="detector_threshold_provenance",
            debt_ids=(
                "missing:information_threshold_rule",
                "underdeclared:threshold_rule",
            ),
            same_neighbor_completion_ids=(
                "missing:information_threshold_rule",
                "underdeclared:threshold_rule",
            ),
            separation_requires=(),
            expected_classification="native_absorbed_after_same_neighbor_completion",
            fixed_before_outcome=True,
            set_valued=True,
            native_absorber_available=True,
            detector_fixture=True,
            scalar_rank_only=False,
            outcome_leakage=False,
        ),
        APRDGateCase(
            case_id="t51_t58_observer_b_non_detector_separator",
            source_test="T51/T58",
            role="non_detector_survivor",
            domain="record_provenance_descent",
            debt_ids=(
                "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                "missing:provenance_record:r_A_locked",
            ),
            same_neighbor_completion_ids=("local_pair:e2_B_locking<=e3_composite_locking",),
            separation_requires=(
                "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                "missing:provenance_record:r_A_locked",
            ),
            expected_classification="minimal_nonabsorbed_separator",
            fixed_before_outcome=True,
            set_valued=True,
            native_absorber_available=False,
            detector_fixture=False,
            scalar_rank_only=False,
            outcome_leakage=False,
        ),
        APRDGateCase(
            case_id="t19_self_finality_external_witness_separator",
            source_test="T19",
            role="non_detector_survivor",
            domain="self_finality_record_access",
            debt_ids=("missing:R_self_finality_external_witness",),
            same_neighbor_completion_ids=("R_obs_internal_record",),
            separation_requires=("missing:R_self_finality_external_witness",),
            expected_classification="minimal_nonabsorbed_separator",
            fixed_before_outcome=True,
            set_valued=True,
            native_absorber_available=False,
            detector_fixture=False,
            scalar_rank_only=False,
            outcome_leakage=False,
        ),
        APRDGateCase(
            case_id="record_transport_same_rank_separator",
            source_test="finite_record_transport_control",
            role="scalar_rank_discriminator",
            domain="record_transport",
            debt_ids=(
                "missing:source_record_support",
                "missing:transport_compatibility_certificate",
            ),
            same_neighbor_completion_ids=("declared:local_transport_edge",),
            separation_requires=(
                "missing:source_record_support",
                "missing:transport_compatibility_certificate",
            ),
            expected_classification="minimal_nonabsorbed_separator",
            fixed_before_outcome=True,
            set_valued=True,
            native_absorber_available=False,
            detector_fixture=False,
            scalar_rank_only=False,
            outcome_leakage=False,
        ),
        APRDGateCase(
            case_id="padded_aprd_minimality_control",
            source_test="T51/T58",
            role="hostile_control",
            domain="record_provenance_descent",
            debt_ids=(
                "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                "missing:provenance_record:r_A_locked",
                "padding:rank_hint",
            ),
            same_neighbor_completion_ids=(),
            separation_requires=(
                "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                "missing:provenance_record:r_A_locked",
            ),
            expected_classification="rejected_nonminimal_padding",
            fixed_before_outcome=True,
            set_valued=True,
            native_absorber_available=False,
            detector_fixture=False,
            scalar_rank_only=False,
            outcome_leakage=False,
        ),
        APRDGateCase(
            case_id="scalar_rank_collapse_control",
            source_test="T542",
            role="hostile_control",
            domain="rank_proxy",
            debt_ids=("rank:2",),
            same_neighbor_completion_ids=(),
            separation_requires=("rank:2",),
            expected_classification="rejected_scalar_rank_collapse",
            fixed_before_outcome=True,
            set_valued=False,
            native_absorber_available=False,
            detector_fixture=False,
            scalar_rank_only=True,
            outcome_leakage=False,
        ),
        APRDGateCase(
            case_id="post_hoc_outcome_leakage_control",
            source_test="T544",
            role="hostile_control",
            domain="outcome_selected_debt",
            debt_ids=("missing:chosen_after_verdict",),
            same_neighbor_completion_ids=(),
            separation_requires=("missing:chosen_after_verdict",),
            expected_classification="rejected_post_hoc_outcome_leakage",
            fixed_before_outcome=False,
            set_valued=True,
            native_absorber_available=False,
            detector_fixture=False,
            scalar_rank_only=False,
            outcome_leakage=True,
        ),
        APRDGateCase(
            case_id="full_access_positive_control",
            source_test="T19",
            role="positive_control",
            domain="self_finality_record_access",
            debt_ids=(),
            same_neighbor_completion_ids=(),
            separation_requires=(),
            expected_classification="positive_control_no_debt",
            fixed_before_outcome=True,
            set_valued=True,
            native_absorber_available=False,
            detector_fixture=False,
            scalar_rank_only=False,
            outcome_leakage=False,
        ),
    )


def _controls(
    evaluations: tuple[APRDGateEvaluation, ...],
    non_detector_survivors: tuple[str, ...],
    native_absorber_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
    same_rank_distinct_debt_pair: bool,
) -> tuple[ControlEvaluation, ...]:
    by_id = {evaluation.case_id: evaluation for evaluation in evaluations}
    return (
        ControlEvaluation(
            control_id="source_t543_consumed",
            passed=t543.run_t543_analysis().verdict == t543.VERDICT,
            reason="T544 consumes the APRD object built by T543.",
        ),
        ControlEvaluation(
            control_id="expected_classifications_match",
            passed=all(
                evaluation.classification_matches_expected
                for evaluation in evaluations
            ),
            reason="Every fixture follows its predeclared gate branch.",
        ),
        ControlEvaluation(
            control_id="detector_absorber_still_absorbs",
            passed="t66_detector_threshold_absorber_control"
            in native_absorber_cases,
            reason="T66-style detector threshold debt is absorbed by native completion.",
        ),
        ControlEvaluation(
            control_id="non_detector_minimal_survivor_exists",
            passed=bool(non_detector_survivors),
            reason="At least one non-detector APRD fixture survives allowed completion.",
        ),
        ControlEvaluation(
            control_id="scalar_rank_not_sufficient",
            passed=same_rank_distinct_debt_pair
            and "scalar_rank_collapse_control" in rejected_controls,
            reason=(
                "Two survivor fixtures share scalar rank while carrying distinct "
                "debt labels, and scalar-only replacement rejects."
            ),
        ),
        ControlEvaluation(
            control_id="minimality_and_posthoc_controls_reject",
            passed={
                "padded_aprd_minimality_control",
                "post_hoc_outcome_leakage_control",
            }.issubset(set(rejected_controls)),
            reason="Padding and outcome-selected debt cannot clear the APRD gate.",
        ),
        ControlEvaluation(
            control_id="positive_control_has_no_debt",
            passed=by_id["full_access_positive_control"].classification
            == "positive_control_no_debt",
            reason="Full access produces no reconstruction debt.",
        ),
        ControlEvaluation(
            control_id="no_claim_or_posture_movement",
            passed=True,
            reason="T544 performs no claim, canon, public-posture, or external movement.",
        ),
    )


def _same_rank_distinct_debt_pair(
    evaluations: tuple[APRDGateEvaluation, ...]
) -> bool:
    survivors = [
        evaluation
        for evaluation in evaluations
        if evaluation.classification == "minimal_nonabsorbed_separator"
    ]
    for left_index, left in enumerate(survivors):
        for right in survivors[left_index + 1 :]:
            if (
                left.scalar_rank_signature == right.scalar_rank_signature
                and left.debt_ids != right.debt_ids
            ):
                return True
    return False


def _claim_labels(
    non_detector_survivors: tuple[str, ...],
    native_absorber_cases: tuple[str, ...],
    same_rank_distinct_debt_pair: bool,
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Non-detector APRD survivor fixtures cleared the finite gate: "
                + ", ".join(non_detector_survivors)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Native absorber completion still absorbs: "
                + ", ".join(native_absorber_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "APRD did not reduce to scalar rank."
                if same_rank_distinct_debt_pair
                else "No scalar-rank separation was found."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The finite survivor justifies a refinement-stability packet, "
                "not source-law, claim-ledger, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T544 Results: APRD Minimality And Absorber Separation Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- APRD gate status: `{payload['aprd_gate_status']}`",
        f"- Source T543 verdict: `{payload['source_t543_verdict']}`",
        f"- Source T543 status: `{payload['source_t543_status']}`",
        "- Non-detector survivors: "
        + ", ".join(f"`{item}`" for item in payload["non_detector_survivors"]),
        "- Native absorber cases: "
        + ", ".join(f"`{item}`" for item in payload["native_absorber_cases"]),
        f"- Same-rank distinct debt pair found: {payload['same_rank_distinct_debt_pair_found']}",
        "",
        "## Gate Definition",
        "",
        f"- Name: `{payload['gate_definition']['name']}`",
        f"- Source: {payload['gate_definition']['source']}",
        "- Required properties: "
        + ", ".join(
            f"`{item}`" for item in payload["gate_definition"]["required_properties"]
        ),
        f"- Survivor reading: {payload['gate_definition']['survivor_reading']}",
        "",
        "## Evaluations",
        "",
        "| case | source | role | domain | classification | residual debt | minimal? | survivor? |",
        "| --- | --- | --- | --- | --- | --- | :---: | :---: |",
    ]
    for evaluation in payload["evaluations"]:
        residual = (
            ", ".join(f"`{item}`" for item in evaluation["residual_debt_ids"])
            or "none"
        )
        lines.append(
            "| "
            f"`{evaluation['case_id']}` | "
            f"`{evaluation['source_test']}` | "
            f"`{evaluation['role']}` | "
            f"`{evaluation['domain']}` | "
            f"`{evaluation['classification']}` | "
            f"{residual} | "
            f"{evaluation['minimal']} | "
            f"{evaluation['non_detector_survivor']} |"
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


def write_results(result: T544Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t544_result_to_dict(result)
    json_path = results_dir / "T544-aprd-minimality-absorber-separation-gate-v0.1.json"
    md_path = (
        results_dir
        / "T544-aprd-minimality-absorber-separation-gate-v0.1-results.md"
    )
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t544_analysis()
    payload = t544_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
