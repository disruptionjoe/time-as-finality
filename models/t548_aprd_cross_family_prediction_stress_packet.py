"""T548: APRD cross-family prediction stress packet.

T547 kept APRD alive under held-out native fixture prediction. T548 applies the
stricter cross-family burden: can the frozen T547 predictor handle distinct
native-candidate families without adding a new family rule after seeing the
target?

The answer is a narrowing result. The known-family regression still works, but
new candidate families return the frozen predictor's unknown-family marker. That
is useful: APRD remains a family-local feeder object, not a cross-family source
law or finite-to-continuum bridge.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t547_aprd_held_out_prediction_packet as t547


ARTIFACT = "T548-aprd-cross-family-prediction-stress-packet-v0.1"
VERDICT = "aprd_cross_family_stress_narrows_to_family_local_feeder"
APRD_CROSS_FAMILY_STATUS = "CROSS_FAMILY_STRESS_FAILED_WITHOUT_RETUNING"
NEXT_PACKET = "t549_taf11_post_aprd_route_reset_router"

NOT_CLAIMED = (
    "T548 does not establish a source law, prove a shadow-protection theorem, "
    "derive spacetime, prove manifoldlikeness, repair T528, reverse T223, "
    "unpause S1, promote S1, change claim status, change Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, or move cross-repo truth. It is a finite "
    "cross-family APRD stress and narrowing packet only."
)


@dataclass(frozen=True)
class CrossFamilyFixture:
    case_id: str
    family: str
    role: str
    required_support_ids: tuple[str, ...]
    observed_support_ids: tuple[str, ...]
    actual_debt_ids: tuple[str, ...]
    expected_classification: str
    native_candidate: bool
    outcome_label_visible: bool = False
    proxy_outcome_hint_visible: bool = False
    retune_requested: bool = False
    hidden_support_change: bool = False
    manual_family_rule_injection: bool = False
    cross_repo_truth_import_requested: bool = False
    taf4_or_source_law_claim_requested: bool = False


@dataclass(frozen=True)
class CrossFamilyEvaluation:
    case_id: str
    family: str
    role: str
    required_support_ids: tuple[str, ...]
    observed_support_ids: tuple[str, ...]
    predicted_debt_ids: tuple[str, ...]
    actual_debt_ids: tuple[str, ...]
    classification: str
    expected_classification: str
    classification_matches_expected: bool
    prediction_matched: bool
    known_family_regression: bool
    cross_family_survivor: bool
    narrowed: bool
    rejected: bool
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
class T548Result:
    artifact: str
    source_t547_verdict: str
    source_t547_status: str
    stress_definition: dict[str, Any]
    evaluations: tuple[CrossFamilyEvaluation, ...]
    controls: tuple[ControlEvaluation, ...]
    known_family_regressions: tuple[str, ...]
    narrowed_cases: tuple[str, ...]
    rejected_controls: tuple[str, ...]
    cross_family_survivors: tuple[str, ...]
    aprd_cross_family_status: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t548_analysis() -> T548Result:
    t547_result = t547.run_t547_analysis()
    evaluations = tuple(evaluate_cross_family_fixture(case) for case in _fixtures())
    known_family_regressions = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.known_family_regression
    )
    narrowed_cases = tuple(
        evaluation.case_id for evaluation in evaluations if evaluation.narrowed
    )
    rejected_controls = tuple(
        evaluation.case_id for evaluation in evaluations if evaluation.rejected
    )
    cross_family_survivors = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.cross_family_survivor
    )
    controls = _controls(
        t547_result,
        evaluations,
        known_family_regressions,
        narrowed_cases,
        rejected_controls,
        cross_family_survivors,
    )
    verdict = (
        VERDICT
        if t547_result.verdict == t547.VERDICT
        and t547_result.aprd_prediction_status == t547.APRD_PREDICTION_STATUS
        and known_family_regressions
        and narrowed_cases
        and not cross_family_survivors
        and all(control.passed for control in controls)
        else "aprd_cross_family_stress_unexpected_status"
    )

    return T548Result(
        artifact=ARTIFACT,
        source_t547_verdict=t547_result.verdict,
        source_t547_status=t547_result.aprd_prediction_status,
        stress_definition=_stress_definition(),
        evaluations=evaluations,
        controls=controls,
        known_family_regressions=known_family_regressions,
        narrowed_cases=narrowed_cases,
        rejected_controls=rejected_controls,
        cross_family_survivors=cross_family_survivors,
        aprd_cross_family_status=APRD_CROSS_FAMILY_STATUS,
        verdict=verdict,
        strongest_reading=(
            "The frozen T547 APRD predictor still matches its known native "
            "record-transport family, but it does not predict distinct "
            "access-structure or protocol-stack candidate families without "
            "adding a new family rule. Manual rule injection, outcome leakage, "
            "proxy hints, hidden support change, cross-repo truth import, and "
            "TAF4/source-law overreading all reject. APRD narrows to a useful "
            "family-local feeder object."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should choose the next TAF11 route after "
            "APRD failed cross-family prediction without retuning: either a "
            "new source-law family with its own falsifier, a protocol-stack "
            "ablation preflight, or a deliberate pause behind TAF8 until a "
            "domain-native packet exists."
        ),
        taf11_update=(
            "TAF11 remains open but APRD is narrowed. T548 blocks reading the "
            "T543-T547 APRD line as a cross-family source law; the next move "
            "should reset route selection rather than deepen APRD toward TAF4."
        ),
        taf4_update=(
            "TAF4 remains blocked. T548 specifically rejects finite-to-continuum "
            "movement from APRD because the frozen predictor does not survive "
            "new-family stress without retuning."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T548 supplies a negative control: cross-family prediction cannot "
            "be obtained by injecting a family rule after target selection."
        ),
        claim_labels=_claim_labels(
            known_family_regressions,
            narrowed_cases,
            rejected_controls,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T548 leaves claim rows, Canon "
            "Index tiers, and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def evaluate_cross_family_fixture(
    fixture: CrossFamilyFixture,
) -> CrossFamilyEvaluation:
    predicted: tuple[str, ...] = ()
    actual = tuple(sorted(fixture.actual_debt_ids))

    if fixture.taf4_or_source_law_claim_requested:
        classification = "rejected_taf4_or_source_law_overread"
        reason = "The fixture tries to read finite stress as source-law or TAF4 movement."
    elif fixture.cross_repo_truth_import_requested:
        classification = "rejected_cross_repo_truth_import"
        reason = "The fixture asks TaF to import another repo's truth directly."
    elif fixture.manual_family_rule_injection:
        classification = "rejected_posthoc_family_rule_injection"
        reason = "A new family rule is injected after target selection."
    elif fixture.outcome_label_visible:
        classification = "rejected_outcome_label_leakage"
        reason = "The target outcome label is visible before prediction."
    elif fixture.proxy_outcome_hint_visible:
        classification = "rejected_proxy_label_reading"
        reason = "A proxy outcome hint is visible before prediction."
    elif fixture.retune_requested:
        classification = "rejected_posthoc_retuning"
        reason = "The predictor asks to retune after seeing a target fixture."
    elif fixture.hidden_support_change:
        classification = "rejected_hidden_support_change"
        reason = "The fixture hides a support change while presenting as native."
    elif not fixture.native_candidate:
        classification = "rejected_non_native_cross_family_fixture"
        reason = "The fixture is not native to the APRD stress target."
    else:
        predicted = frozen_t547_prediction(fixture)
        if predicted == ("missing:unknown_native_family_rule",):
            classification = "narrowed_unknown_family_requires_native_rule"
            reason = (
                "The frozen T547 predictor has no rule for this candidate "
                "family, so cross-family prediction would require retuning."
            )
        elif predicted == actual and fixture.family in _known_t547_families():
            classification = "known_family_regression_matched"
            reason = "The frozen predictor still works on its known native family."
        elif predicted == actual:
            classification = "cross_family_prediction_matched"
            reason = "The frozen predictor matched a distinct family without retuning."
        else:
            classification = "failed_cross_family_prediction"
            reason = "Predicted APRD debt did not match the revealed stress label."

    prediction_matched = predicted == actual
    known_family_regression = classification == "known_family_regression_matched"
    cross_family_survivor = classification == "cross_family_prediction_matched"
    narrowed = classification == "narrowed_unknown_family_requires_native_rule"
    rejected = classification.startswith("rejected_") or classification.startswith(
        "failed_"
    )
    return CrossFamilyEvaluation(
        case_id=fixture.case_id,
        family=fixture.family,
        role=fixture.role,
        required_support_ids=tuple(sorted(fixture.required_support_ids)),
        observed_support_ids=tuple(sorted(fixture.observed_support_ids)),
        predicted_debt_ids=predicted,
        actual_debt_ids=actual,
        classification=classification,
        expected_classification=fixture.expected_classification,
        classification_matches_expected=classification
        == fixture.expected_classification,
        prediction_matched=prediction_matched,
        known_family_regression=known_family_regression,
        cross_family_survivor=cross_family_survivor,
        narrowed=narrowed,
        rejected=rejected,
        reason=reason,
    )


def frozen_t547_prediction(fixture: CrossFamilyFixture) -> tuple[str, ...]:
    held_out = t547.HeldOutFixture(
        case_id=fixture.case_id,
        family=fixture.family,
        role=fixture.role,
        required_support_ids=fixture.required_support_ids,
        observed_support_ids=fixture.observed_support_ids,
        actual_debt_ids=fixture.actual_debt_ids,
        expected_classification=fixture.expected_classification,
        native_fixture=fixture.native_candidate,
        outcome_label_visible=False,
        proxy_outcome_hint_visible=False,
        retune_requested=False,
        hidden_support_change=False,
        source_law_claim_requested=False,
    )
    return t547.predict_debt_ids(held_out)


def t548_result_to_dict(result: T548Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t547_verdict": result.source_t547_verdict,
        "source_t547_status": result.source_t547_status,
        "stress_definition": result.stress_definition,
        "evaluations": [
            {
                "case_id": evaluation.case_id,
                "family": evaluation.family,
                "role": evaluation.role,
                "required_support_ids": list(evaluation.required_support_ids),
                "observed_support_ids": list(evaluation.observed_support_ids),
                "predicted_debt_ids": list(evaluation.predicted_debt_ids),
                "actual_debt_ids": list(evaluation.actual_debt_ids),
                "classification": evaluation.classification,
                "expected_classification": evaluation.expected_classification,
                "classification_matches_expected": (
                    evaluation.classification_matches_expected
                ),
                "prediction_matched": evaluation.prediction_matched,
                "known_family_regression": evaluation.known_family_regression,
                "cross_family_survivor": evaluation.cross_family_survivor,
                "narrowed": evaluation.narrowed,
                "rejected": evaluation.rejected,
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
        "known_family_regressions": list(result.known_family_regressions),
        "narrowed_cases": list(result.narrowed_cases),
        "rejected_controls": list(result.rejected_controls),
        "cross_family_survivors": list(result.cross_family_survivors),
        "aprd_cross_family_status": result.aprd_cross_family_status,
        "verdict": result.verdict,
        "strongest_reading": result.strongest_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
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


def _stress_definition() -> dict[str, Any]:
    return {
        "name": "aprd_cross_family_prediction_stress_packet",
        "source": "T547 frozen APRD held-out predictor",
        "stress_question": (
            "Can the frozen predictor assign APRD debt for a distinct "
            "native-candidate family before outcome labels and without adding "
            "a family-specific rule?"
        ),
        "success_requires": [
            "known_family_regression_still_matches",
            "distinct_family_prediction_matches_without_new_rule",
            "no_outcome_label_leakage",
            "no_proxy_outcome_hint",
            "no_posthoc_retuning",
            "no_manual_family_rule_injection",
            "no_cross_repo_truth_import",
            "no_taf4_or_source_law_overread",
        ],
        "narrowing_condition": (
            "If distinct native-candidate families return the frozen unknown-"
            "family marker, APRD remains family-local and must not feed TAF4 "
            "or source-law status without a new governed route."
        ),
    }


def _fixtures() -> tuple[CrossFamilyFixture, ...]:
    return (
        CrossFamilyFixture(
            case_id="regression_t547_record_transport_missing_certificate",
            family="record_transport",
            role="known_family_regression",
            required_support_ids=(
                "source_record_support",
                "transport_compatibility_certificate",
            ),
            observed_support_ids=("source_record_support",),
            actual_debt_ids=("missing:transport_compatibility_certificate",),
            expected_classification="known_family_regression_matched",
            native_candidate=True,
        ),
        CrossFamilyFixture(
            case_id="stress_quantum_access_missing_shareability_witness",
            family="quantum_access_structure",
            role="distinct_native_candidate",
            required_support_ids=(
                "access_structure_definition",
                "monogamy_shareability_witness",
            ),
            observed_support_ids=("access_structure_definition",),
            actual_debt_ids=("missing:monogamy_shareability_witness",),
            expected_classification="narrowed_unknown_family_requires_native_rule",
            native_candidate=True,
        ),
        CrossFamilyFixture(
            case_id="stress_protocol_stack_missing_sybil_layer",
            family="observerse_protocol_stack",
            role="distinct_native_candidate",
            required_support_ids=(
                "issuance_log",
                "fork_choice_rule",
                "sybil_resistance_layer",
            ),
            observed_support_ids=("issuance_log", "fork_choice_rule"),
            actual_debt_ids=("missing:sybil_resistance_layer",),
            expected_classification="narrowed_unknown_family_requires_native_rule",
            native_candidate=True,
        ),
        CrossFamilyFixture(
            case_id="control_manual_family_rule_injection",
            family="quantum_access_structure",
            role="hostile_control",
            required_support_ids=("monogamy_shareability_witness",),
            observed_support_ids=(),
            actual_debt_ids=("missing:monogamy_shareability_witness",),
            expected_classification="rejected_posthoc_family_rule_injection",
            native_candidate=True,
            manual_family_rule_injection=True,
        ),
        CrossFamilyFixture(
            case_id="control_outcome_label_leakage",
            family="quantum_access_structure",
            role="hostile_control",
            required_support_ids=("monogamy_shareability_witness",),
            observed_support_ids=(),
            actual_debt_ids=("missing:monogamy_shareability_witness",),
            expected_classification="rejected_outcome_label_leakage",
            native_candidate=True,
            outcome_label_visible=True,
        ),
        CrossFamilyFixture(
            case_id="control_proxy_label_reading",
            family="observerse_protocol_stack",
            role="hostile_control",
            required_support_ids=("sybil_resistance_layer",),
            observed_support_ids=(),
            actual_debt_ids=("missing:sybil_resistance_layer",),
            expected_classification="rejected_proxy_label_reading",
            native_candidate=True,
            proxy_outcome_hint_visible=True,
        ),
        CrossFamilyFixture(
            case_id="control_hidden_support_change",
            family="observerse_protocol_stack",
            role="hostile_control",
            required_support_ids=("sybil_resistance_layer",),
            observed_support_ids=("sybil_resistance_layer",),
            actual_debt_ids=("missing:sybil_resistance_layer",),
            expected_classification="rejected_hidden_support_change",
            native_candidate=True,
            hidden_support_change=True,
        ),
        CrossFamilyFixture(
            case_id="control_cross_repo_truth_import",
            family="gu_ti_taf_adapter",
            role="hostile_control",
            required_support_ids=("external_source_category_truth",),
            observed_support_ids=(),
            actual_debt_ids=("missing:external_source_category_truth",),
            expected_classification="rejected_cross_repo_truth_import",
            native_candidate=False,
            cross_repo_truth_import_requested=True,
        ),
        CrossFamilyFixture(
            case_id="control_taf4_source_law_overread",
            family="record_transport",
            role="hostile_control",
            required_support_ids=(
                "source_record_support",
                "transport_compatibility_certificate",
            ),
            observed_support_ids=(
                "source_record_support",
                "transport_compatibility_certificate",
            ),
            actual_debt_ids=(),
            expected_classification="rejected_taf4_or_source_law_overread",
            native_candidate=True,
            taf4_or_source_law_claim_requested=True,
        ),
    )


def _controls(
    t547_result: t547.T547Result,
    evaluations: tuple[CrossFamilyEvaluation, ...],
    known_family_regressions: tuple[str, ...],
    narrowed_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
    cross_family_survivors: tuple[str, ...],
) -> tuple[ControlEvaluation, ...]:
    expected_narrowed = {
        "stress_quantum_access_missing_shareability_witness",
        "stress_protocol_stack_missing_sybil_layer",
    }
    expected_rejections = {
        "control_manual_family_rule_injection",
        "control_outcome_label_leakage",
        "control_proxy_label_reading",
        "control_hidden_support_change",
        "control_cross_repo_truth_import",
        "control_taf4_source_law_overread",
    }
    return (
        ControlEvaluation(
            control_id="source_t547_consumed",
            passed=t547_result.verdict == t547.VERDICT
            and t547_result.aprd_prediction_status == t547.APRD_PREDICTION_STATUS,
            reason="T548 consumes the held-out APRD predictor built by T547.",
        ),
        ControlEvaluation(
            control_id="expected_classifications_match",
            passed=all(
                evaluation.classification_matches_expected
                for evaluation in evaluations
            ),
            reason="Every stress fixture follows its predeclared branch.",
        ),
        ControlEvaluation(
            control_id="known_family_regression_still_matches",
            passed=known_family_regressions
            == ("regression_t547_record_transport_missing_certificate",),
            reason="The frozen predictor still handles a known T547 native family.",
        ),
        ControlEvaluation(
            control_id="distinct_candidate_families_narrow",
            passed=expected_narrowed == set(narrowed_cases),
            reason=(
                "Distinct candidate families require a native family rule rather "
                "than cross-family prediction by the frozen APRD predictor."
            ),
        ),
        ControlEvaluation(
            control_id="no_cross_family_survivor_without_retuning",
            passed=cross_family_survivors == (),
            reason="No distinct candidate family clears without adding a rule.",
        ),
        ControlEvaluation(
            control_id="hostile_controls_reject",
            passed=expected_rejections.issubset(set(rejected_controls)),
            reason=(
                "Rule injection, leakage, proxy hints, hidden support, cross-repo "
                "truth import, and TAF4/source-law overread all reject."
            ),
        ),
        ControlEvaluation(
            control_id="no_claim_or_posture_movement",
            passed=True,
            reason="T548 performs no claim, canon, public-posture, or external movement.",
        ),
    )


def _claim_labels(
    known_family_regressions: tuple[str, ...],
    narrowed_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Known-family APRD regression still matches: "
                + ", ".join(known_family_regressions)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Distinct candidate families narrowed under the frozen predictor: "
                + ", ".join(narrowed_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Cross-family shortcut controls rejected: "
            + ", ".join(rejected_controls)
            + ".",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "T548 narrows APRD to a family-local feeder and blocks TAF4 or "
                "source-law movement from the APRD line."
            ),
        ),
    )


def _known_t547_families() -> set[str]:
    return set(t547._debt_rules())


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T548 Results: APRD Cross-Family Prediction Stress Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- APRD cross-family status: `{payload['aprd_cross_family_status']}`",
        f"- Source T547 verdict: `{payload['source_t547_verdict']}`",
        f"- Source T547 status: `{payload['source_t547_status']}`",
        "- Known-family regressions: "
        + ", ".join(f"`{item}`" for item in payload["known_family_regressions"]),
        "- Narrowed cases: "
        + ", ".join(f"`{item}`" for item in payload["narrowed_cases"]),
        "- Rejected controls: "
        + ", ".join(f"`{item}`" for item in payload["rejected_controls"]),
        "- Cross-family survivors: "
        + (
            ", ".join(f"`{item}`" for item in payload["cross_family_survivors"])
            or "none"
        ),
        "",
        "## Stress Definition",
        "",
        f"- Name: `{payload['stress_definition']['name']}`",
        f"- Source: {payload['stress_definition']['source']}",
        f"- Stress question: {payload['stress_definition']['stress_question']}",
        "- Success requires: "
        + ", ".join(
            f"`{item}`" for item in payload["stress_definition"]["success_requires"]
        ),
        f"- Narrowing condition: {payload['stress_definition']['narrowing_condition']}",
        "",
        "## Evaluations",
        "",
        "| case | family | classification | predicted debt | actual debt | matched? | narrowed? | rejected? |",
        "| --- | --- | --- | --- | --- | :---: | :---: | :---: |",
    ]
    for evaluation in payload["evaluations"]:
        predicted = (
            ", ".join(f"`{item}`" for item in evaluation["predicted_debt_ids"])
            or "none"
        )
        actual = (
            ", ".join(f"`{item}`" for item in evaluation["actual_debt_ids"])
            or "none"
        )
        lines.append(
            "| "
            f"`{evaluation['case_id']}` | "
            f"`{evaluation['family']}` | "
            f"`{evaluation['classification']}` | "
            f"{predicted} | "
            f"{actual} | "
            f"{evaluation['prediction_matched']} | "
            f"{evaluation['narrowed']} | "
            f"{evaluation['rejected']} |"
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
        ("TAF4 Update", "taf4_update"),
        ("TAF8 Update", "taf8_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def write_results(result: T548Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t548_result_to_dict(result)
    json_path = results_dir / "T548-aprd-cross-family-prediction-stress-packet-v0.1.json"
    md_path = (
        results_dir / "T548-aprd-cross-family-prediction-stress-packet-v0.1-results.md"
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

    result = run_t548_analysis()
    payload = t548_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
