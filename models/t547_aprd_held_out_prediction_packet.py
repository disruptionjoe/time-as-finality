"""T547: APRD held-out prediction packet.

T546 kept accessible provenance reconstruction debt (APRD) alive under finite
native functoriality and composite checks. T547 asks the stricter predictive
question: can the frozen APRD object predict held-out native fixture debt before
target-outcome labels are read or the predictor is retuned?

The answer remains bounded. Held-out prediction pressure strengthens APRD as a
source-law feeder. It still does not establish a source law or move governance
surfaces.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t546_aprd_functoriality_naturality_packet as t546


ARTIFACT = "T547-aprd-held-out-prediction-packet-v0.1"
VERDICT = "aprd_held_out_prediction_gate_clears_native_fixtures"
APRD_PREDICTION_STATUS = "HELD_OUT_PREDICTION_PRESSURE_SOURCE_LAW_NOT_EARNED"
NEXT_PACKET = "t548_aprd_cross_family_prediction_stress_packet"

NOT_CLAIMED = (
    "T547 does not establish a source law, prove a shadow-protection theorem, "
    "derive spacetime, prove manifoldlikeness, repair T528, reverse T223, "
    "unpause S1, promote S1, change claim status, change Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, or move cross-repo truth. It is a finite "
    "held-out APRD prediction gate only."
)


@dataclass(frozen=True)
class HeldOutFixture:
    case_id: str
    family: str
    role: str
    required_support_ids: tuple[str, ...]
    observed_support_ids: tuple[str, ...]
    actual_debt_ids: tuple[str, ...]
    expected_classification: str
    native_fixture: bool
    outcome_label_visible: bool
    proxy_outcome_hint_visible: bool
    retune_requested: bool
    hidden_support_change: bool
    source_law_claim_requested: bool


@dataclass(frozen=True)
class HeldOutEvaluation:
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
    accepted_prediction: bool
    clear_prediction: bool
    debt_prediction: bool
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
class T547Result:
    artifact: str
    source_t546_verdict: str
    source_t546_status: str
    prediction_definition: dict[str, Any]
    evaluations: tuple[HeldOutEvaluation, ...]
    controls: tuple[ControlEvaluation, ...]
    accepted_prediction_cases: tuple[str, ...]
    clear_prediction_cases: tuple[str, ...]
    debt_prediction_cases: tuple[str, ...]
    rejected_controls: tuple[str, ...]
    aprd_prediction_status: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t547_analysis() -> T547Result:
    t546_result = t546.run_t546_analysis()
    fixtures = _held_out_fixtures()
    evaluations = tuple(evaluate_held_out_fixture(fixture) for fixture in fixtures)
    accepted_prediction_cases = tuple(
        evaluation.case_id for evaluation in evaluations if evaluation.accepted_prediction
    )
    clear_prediction_cases = tuple(
        evaluation.case_id for evaluation in evaluations if evaluation.clear_prediction
    )
    debt_prediction_cases = tuple(
        evaluation.case_id for evaluation in evaluations if evaluation.debt_prediction
    )
    rejected_controls = tuple(
        evaluation.case_id for evaluation in evaluations if evaluation.rejected
    )
    controls = _controls(
        t546_result,
        evaluations,
        accepted_prediction_cases,
        clear_prediction_cases,
        debt_prediction_cases,
        rejected_controls,
    )
    verdict = (
        VERDICT
        if t546_result.verdict == t546.VERDICT
        and t546_result.aprd_functoriality_status == t546.APRD_FUNCTORIALITY_STATUS
        and all(control.passed for control in controls)
        else "aprd_held_out_prediction_gate_unexpected_status"
    )

    return T547Result(
        artifact=ARTIFACT,
        source_t546_verdict=t546_result.verdict,
        source_t546_status=t546_result.aprd_functoriality_status,
        prediction_definition=_prediction_definition(),
        evaluations=evaluations,
        controls=controls,
        accepted_prediction_cases=accepted_prediction_cases,
        clear_prediction_cases=clear_prediction_cases,
        debt_prediction_cases=debt_prediction_cases,
        rejected_controls=rejected_controls,
        aprd_prediction_status=APRD_PREDICTION_STATUS,
        verdict=verdict,
        strongest_reading=(
            "The frozen T546 APRD object predicts held-out native fixture debt "
            "for clear, record-transport, T51/T58, and T19 cases before outcome "
            "labels are read. Leakage, proxy-label reading, retuning, hidden "
            "support change, non-native fixtures, and source-law overclaiming "
            "reject. This is predictive pressure, not source-law status."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should stress the frozen APRD predictor on "
            "a distinct native family or adversarial cross-family fixture before "
            "any finite-to-continuum or source-law reading."
        ),
        taf11_update=(
            "TAF11 remains the live Track-1 route. T547 clears bounded held-out "
            "APRD prediction pressure, but source-law status still waits on "
            "cross-family stress without retuning."
        ),
        taf4_update=(
            "TAF4 remains blocked. T547 gives APRD a stronger finite predictor, "
            "but finite-to-continuum movement still needs cross-family or "
            "adversarial predictive pressure before geometric reading."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T547 strengthens APRD as a typed-gap predictor, not as a "
            "shadow-protection transfer theorem."
        ),
        claim_labels=_claim_labels(
            accepted_prediction_cases,
            clear_prediction_cases,
            debt_prediction_cases,
            rejected_controls,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T547 leaves claim rows, Canon "
            "Index tiers, and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def evaluate_held_out_fixture(fixture: HeldOutFixture) -> HeldOutEvaluation:
    predicted = ()
    actual = tuple(sorted(fixture.actual_debt_ids))

    if fixture.source_law_claim_requested:
        classification = "rejected_source_law_overclaim"
        reason = "The fixture requests source-law status from finite prediction."
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
    elif not fixture.native_fixture:
        classification = "rejected_non_native_heldout_fixture"
        reason = "The fixture is not native to the frozen APRD predictor family."
    else:
        predicted = predict_debt_ids(fixture)
        if predicted == actual and not predicted:
            classification = "held_out_clear_prediction_matched"
            reason = "The frozen predictor correctly predicted no APRD debt."
        elif predicted == actual:
            classification = "held_out_debt_prediction_matched"
            reason = "The frozen predictor correctly predicted APRD debt."
        else:
            classification = "failed_held_out_prediction"
            reason = "Predicted APRD debt did not match the revealed held-out label."

    prediction_matched = predicted == actual
    accepted_prediction = classification in {
        "held_out_clear_prediction_matched",
        "held_out_debt_prediction_matched",
    }
    clear_prediction = classification == "held_out_clear_prediction_matched"
    debt_prediction = classification == "held_out_debt_prediction_matched"
    rejected = classification.startswith("rejected_") or classification.startswith(
        "failed_"
    )
    return HeldOutEvaluation(
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
        accepted_prediction=accepted_prediction,
        clear_prediction=clear_prediction,
        debt_prediction=debt_prediction,
        rejected=rejected,
        reason=reason,
    )


def predict_debt_ids(fixture: HeldOutFixture) -> tuple[str, ...]:
    """Frozen APRD predictor inherited from T546's debt-object families."""

    rules = _debt_rules()
    if fixture.family not in rules:
        return ("missing:unknown_native_family_rule",)
    observed = set(fixture.observed_support_ids)
    debt_ids = {
        debt_id
        for support_id, debt_id in rules[fixture.family].items()
        if support_id in fixture.required_support_ids and support_id not in observed
    }
    return tuple(sorted(debt_ids))


def t547_result_to_dict(result: T547Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t546_verdict": result.source_t546_verdict,
        "source_t546_status": result.source_t546_status,
        "prediction_definition": result.prediction_definition,
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
                "accepted_prediction": evaluation.accepted_prediction,
                "clear_prediction": evaluation.clear_prediction,
                "debt_prediction": evaluation.debt_prediction,
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
        "accepted_prediction_cases": list(result.accepted_prediction_cases),
        "clear_prediction_cases": list(result.clear_prediction_cases),
        "debt_prediction_cases": list(result.debt_prediction_cases),
        "rejected_controls": list(result.rejected_controls),
        "aprd_prediction_status": result.aprd_prediction_status,
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


def _prediction_definition() -> dict[str, Any]:
    return {
        "name": "aprd_held_out_prediction_packet",
        "source": "T546 finite native APRD functoriality object",
        "frozen_rule": [
            "read_required_support_before_target_label",
            "map_absent_native_support_to_predeclared_aprd_debt_atoms",
            "do_not_read_actual_debt_ids_until_validation",
            "do_not_retune_rules_after_target_fixture_selection",
        ],
        "prediction_acceptance": [
            "native_fixture",
            "outcome_label_hidden_before_prediction",
            "no_proxy_outcome_hint",
            "no_posthoc_retuning",
            "no_hidden_support_change",
            "predicted_debt_set_equals_revealed_debt_set",
        ],
        "rejected_shortcuts": [
            "outcome_label_leakage",
            "proxy_label_reading",
            "posthoc_retuning",
            "hidden_support_change",
            "non_native_fixture",
            "finite_prediction_read_as_source_law",
        ],
        "survivor_reading": (
            "Held-out prediction pressure keeps APRD alive as a source-law "
            "feeder. Source-law reading still waits on cross-family stress."
        ),
    }


def _held_out_fixtures() -> tuple[HeldOutFixture, ...]:
    return (
        HeldOutFixture(
            case_id="heldout_record_transport_complete_clear",
            family="record_transport",
            role="native_clear_control",
            required_support_ids=(
                "source_record_support",
                "transport_compatibility_certificate",
            ),
            observed_support_ids=(
                "source_record_support",
                "transport_compatibility_certificate",
            ),
            actual_debt_ids=(),
            expected_classification="held_out_clear_prediction_matched",
            native_fixture=True,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=False,
            retune_requested=False,
            hidden_support_change=False,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="heldout_record_transport_missing_certificate",
            family="record_transport",
            role="native_debt_control",
            required_support_ids=(
                "source_record_support",
                "transport_compatibility_certificate",
            ),
            observed_support_ids=("source_record_support",),
            actual_debt_ids=("missing:transport_compatibility_certificate",),
            expected_classification="held_out_debt_prediction_matched",
            native_fixture=True,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=False,
            retune_requested=False,
            hidden_support_change=False,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="heldout_t51_missing_provenance_record",
            family="t51_t58_locking",
            role="native_debt_control",
            required_support_ids=(
                "ambient_pair:e1_A_locking<=e3_composite_locking",
                "provenance_record:r_A_locked",
            ),
            observed_support_ids=("ambient_pair:e1_A_locking<=e3_composite_locking",),
            actual_debt_ids=("missing:provenance_record:r_A_locked",),
            expected_classification="held_out_debt_prediction_matched",
            native_fixture=True,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=False,
            retune_requested=False,
            hidden_support_change=False,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="heldout_t19_missing_external_witness",
            family="t19_external_witness",
            role="native_debt_control",
            required_support_ids=("R_self_finality_external_witness",),
            observed_support_ids=(),
            actual_debt_ids=("missing:R_self_finality_external_witness",),
            expected_classification="held_out_debt_prediction_matched",
            native_fixture=True,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=False,
            retune_requested=False,
            hidden_support_change=False,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="control_outcome_label_leakage",
            family="record_transport",
            role="hostile_control",
            required_support_ids=("transport_compatibility_certificate",),
            observed_support_ids=(),
            actual_debt_ids=("missing:transport_compatibility_certificate",),
            expected_classification="rejected_outcome_label_leakage",
            native_fixture=True,
            outcome_label_visible=True,
            proxy_outcome_hint_visible=False,
            retune_requested=False,
            hidden_support_change=False,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="control_proxy_label_reading",
            family="t51_t58_locking",
            role="hostile_control",
            required_support_ids=("provenance_record:r_A_locked",),
            observed_support_ids=(),
            actual_debt_ids=("missing:provenance_record:r_A_locked",),
            expected_classification="rejected_proxy_label_reading",
            native_fixture=True,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=True,
            retune_requested=False,
            hidden_support_change=False,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="control_posthoc_retuning",
            family="record_transport",
            role="hostile_control",
            required_support_ids=("transport_compatibility_certificate",),
            observed_support_ids=(),
            actual_debt_ids=("missing:transport_compatibility_certificate",),
            expected_classification="rejected_posthoc_retuning",
            native_fixture=True,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=False,
            retune_requested=True,
            hidden_support_change=False,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="control_hidden_support_change",
            family="record_transport",
            role="hostile_control",
            required_support_ids=("source_record_support",),
            observed_support_ids=("source_record_support",),
            actual_debt_ids=("missing:source_record_support",),
            expected_classification="rejected_hidden_support_change",
            native_fixture=True,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=False,
            retune_requested=False,
            hidden_support_change=True,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="control_non_native_cross_family_fixture",
            family="cross_domain_quorum_fixture",
            role="hostile_control",
            required_support_ids=("quorum_intersection_certificate",),
            observed_support_ids=(),
            actual_debt_ids=("missing:quorum_intersection_certificate",),
            expected_classification="rejected_non_native_heldout_fixture",
            native_fixture=False,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=False,
            retune_requested=False,
            hidden_support_change=False,
            source_law_claim_requested=False,
        ),
        HeldOutFixture(
            case_id="control_source_law_overclaim",
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
            expected_classification="rejected_source_law_overclaim",
            native_fixture=True,
            outcome_label_visible=False,
            proxy_outcome_hint_visible=False,
            retune_requested=False,
            hidden_support_change=False,
            source_law_claim_requested=True,
        ),
    )


def _debt_rules() -> dict[str, dict[str, str]]:
    return {
        "record_transport": {
            "source_record_support": "missing:source_record_support",
            "transport_compatibility_certificate": (
                "missing:transport_compatibility_certificate"
            ),
        },
        "t51_t58_locking": {
            "ambient_pair:e1_A_locking<=e3_composite_locking": (
                "missing:ambient_pair:e1_A_locking<=e3_composite_locking"
            ),
            "provenance_record:r_A_locked": "missing:provenance_record:r_A_locked",
        },
        "t19_external_witness": {
            "R_self_finality_external_witness": (
                "missing:R_self_finality_external_witness"
            ),
        },
    }


def _controls(
    t546_result: t546.T546Result,
    evaluations: tuple[HeldOutEvaluation, ...],
    accepted_prediction_cases: tuple[str, ...],
    clear_prediction_cases: tuple[str, ...],
    debt_prediction_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
) -> tuple[ControlEvaluation, ...]:
    by_id = {evaluation.case_id: evaluation for evaluation in evaluations}
    hostile_cases = {
        "control_outcome_label_leakage",
        "control_proxy_label_reading",
        "control_posthoc_retuning",
        "control_hidden_support_change",
        "control_non_native_cross_family_fixture",
        "control_source_law_overclaim",
    }
    expected_debt_cases = {
        "heldout_record_transport_missing_certificate",
        "heldout_t51_missing_provenance_record",
        "heldout_t19_missing_external_witness",
    }
    return (
        ControlEvaluation(
            control_id="source_t546_consumed",
            passed=t546_result.verdict == t546.VERDICT
            and t546_result.aprd_functoriality_status
            == t546.APRD_FUNCTORIALITY_STATUS,
            reason="T547 consumes the APRD functoriality object built by T546.",
        ),
        ControlEvaluation(
            control_id="expected_classifications_match",
            passed=all(
                evaluation.classification_matches_expected
                for evaluation in evaluations
            ),
            reason="Every fixture follows its predeclared prediction branch.",
        ),
        ControlEvaluation(
            control_id="clear_native_case_predicted",
            passed=clear_prediction_cases
            == ("heldout_record_transport_complete_clear",),
            reason="A held-out complete native fixture predicts no APRD debt.",
        ),
        ControlEvaluation(
            control_id="debt_bearing_native_cases_predicted",
            passed=expected_debt_cases.issubset(set(debt_prediction_cases)),
            reason=(
                "Held-out record-transport, T51/T58, and T19 native debt "
                "fixtures are predicted before target label reveal."
            ),
        ),
        ControlEvaluation(
            control_id="accepted_predictions_match_revealed_labels",
            passed=all(
                by_id[case_id].prediction_matched
                for case_id in accepted_prediction_cases
            ),
            reason="Every accepted held-out prediction matches the revealed label.",
        ),
        ControlEvaluation(
            control_id="hostile_prediction_shortcuts_reject",
            passed=hostile_cases.issubset(set(rejected_controls)),
            reason=(
                "Outcome leakage, proxy labels, retuning, hidden support, "
                "non-native fixtures, and source-law overclaiming all reject."
            ),
        ),
        ControlEvaluation(
            control_id="source_law_status_not_earned",
            passed=APRD_PREDICTION_STATUS.endswith("SOURCE_LAW_NOT_EARNED")
            and by_id["control_source_law_overclaim"].rejected,
            reason="Finite held-out prediction pressure is not promoted to source-law status.",
        ),
        ControlEvaluation(
            control_id="no_claim_or_posture_movement",
            passed=True,
            reason="T547 performs no claim, canon, public-posture, or external movement.",
        ),
    )


def _claim_labels(
    accepted_prediction_cases: tuple[str, ...],
    clear_prediction_cases: tuple[str, ...],
    debt_prediction_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Frozen APRD predictor matched held-out native fixtures: "
                + ", ".join(accepted_prediction_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Clear held-out fixture predicted no debt: "
                + ", ".join(clear_prediction_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Debt-bearing held-out fixtures predicted APRD debt: "
                + ", ".join(debt_prediction_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Prediction shortcut controls rejected: " + ", ".join(rejected_controls) + ".",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Held-out finite prediction justifies cross-family stress, not "
                "source-law, claim-ledger, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T547 Results: APRD Held-Out Prediction Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- APRD prediction status: `{payload['aprd_prediction_status']}`",
        f"- Source T546 verdict: `{payload['source_t546_verdict']}`",
        f"- Source T546 status: `{payload['source_t546_status']}`",
        "- Accepted prediction cases: "
        + ", ".join(f"`{item}`" for item in payload["accepted_prediction_cases"]),
        "- Clear prediction cases: "
        + ", ".join(f"`{item}`" for item in payload["clear_prediction_cases"]),
        "- Debt prediction cases: "
        + ", ".join(f"`{item}`" for item in payload["debt_prediction_cases"]),
        "- Rejected controls: "
        + ", ".join(f"`{item}`" for item in payload["rejected_controls"]),
        "",
        "## Prediction Definition",
        "",
        f"- Name: `{payload['prediction_definition']['name']}`",
        f"- Source: {payload['prediction_definition']['source']}",
        "- Frozen rule: "
        + ", ".join(
            f"`{item}`" for item in payload["prediction_definition"]["frozen_rule"]
        ),
        "- Prediction acceptance: "
        + ", ".join(
            f"`{item}`"
            for item in payload["prediction_definition"]["prediction_acceptance"]
        ),
        "- Rejected shortcuts: "
        + ", ".join(
            f"`{item}`"
            for item in payload["prediction_definition"]["rejected_shortcuts"]
        ),
        f"- Survivor reading: {payload['prediction_definition']['survivor_reading']}",
        "",
        "## Held-Out Evaluations",
        "",
        "| case | family | classification | predicted debt | actual debt | matched? | rejected? |",
        "| --- | --- | --- | --- | --- | :---: | :---: |",
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


def write_results(result: T547Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t547_result_to_dict(result)
    json_path = results_dir / "T547-aprd-held-out-prediction-packet-v0.1.json"
    md_path = results_dir / "T547-aprd-held-out-prediction-packet-v0.1-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t547_analysis()
    payload = t547_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
