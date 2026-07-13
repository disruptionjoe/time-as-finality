"""T546: APRD functoriality and naturality packet.

T545 kept accessible provenance reconstruction debt (APRD) alive under finite
presentation stability. T546 asks the stricter next question: do APRD
assignments behave naturally across native morphisms and composites, instead of
only surviving isolated relabeling or restriction checks?

The answer remains bounded. Finite functorial behavior keeps APRD alive as a
source-law feeder. It does not establish a source law or move governance
surfaces.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t545_aprd_refinement_stability_packet as t545


ARTIFACT = "T546-aprd-functoriality-naturality-packet-v0.1"
VERDICT = "aprd_finite_functoriality_gate_clears_native_composites"
APRD_FUNCTORIALITY_STATUS = "FINITE_FUNCTORIAL_SOURCE_LAW_NOT_EARNED"
NEXT_PACKET = "t547_aprd_held_out_prediction_packet"

NOT_CLAIMED = (
    "T546 does not establish a source law, prove a shadow-protection theorem, "
    "derive spacetime, prove manifoldlikeness, repair T528, reverse T223, "
    "unpause S1, promote S1, change claim status, change Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, or move cross-repo truth. It is a finite "
    "APRD functoriality and naturality gate only."
)


@dataclass(frozen=True)
class APRDObject:
    object_id: str
    source_t545_case_id: str
    canonical_debt_ids: tuple[str, ...]


@dataclass(frozen=True)
class APRDMorphismCase:
    case_id: str
    source_object_id: str
    target_object_id: str
    role: str
    morphism_kind: str
    source_debt_ids: tuple[str, ...]
    target_debt_ids: tuple[str, ...]
    pullback_map: tuple[tuple[str, str], ...]
    completion_ids: tuple[str, ...]
    expected_pullback_debt_ids: tuple[str, ...]
    expected_classification: str
    native_morphism: bool
    support_preserving: bool
    hidden_support_change: bool
    outcome_selected_repair: bool


@dataclass(frozen=True)
class APRDMorphismEvaluation:
    case_id: str
    source_object_id: str
    target_object_id: str
    role: str
    morphism_kind: str
    source_debt_ids: tuple[str, ...]
    target_debt_ids: tuple[str, ...]
    pulled_back_debt_ids: tuple[str, ...]
    unmapped_target_debt_ids: tuple[str, ...]
    expected_pullback_debt_ids: tuple[str, ...]
    classification: str
    expected_classification: str
    classification_matches_expected: bool
    natural: bool
    narrowed: bool
    rejected: bool
    reason: str


@dataclass(frozen=True)
class APRDCompositeCase:
    case_id: str
    role: str
    source_object_id: str
    target_object_id: str
    source_debt_ids: tuple[str, ...]
    middle_debt_ids: tuple[str, ...]
    target_debt_ids: tuple[str, ...]
    first_pullback_map: tuple[tuple[str, str], ...]
    second_pullback_map: tuple[tuple[str, str], ...]
    direct_pullback_map: tuple[tuple[str, str], ...]
    expected_classification: str
    native_morphisms: bool
    support_preserving: bool
    outcome_selected_repair: bool


@dataclass(frozen=True)
class APRDCompositeEvaluation:
    case_id: str
    role: str
    source_object_id: str
    target_object_id: str
    source_debt_ids: tuple[str, ...]
    composed_pullback_debt_ids: tuple[str, ...]
    direct_pullback_debt_ids: tuple[str, ...]
    unmapped_target_debt_ids: tuple[str, ...]
    classification: str
    expected_classification: str
    classification_matches_expected: bool
    functorial: bool
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
class T546Result:
    artifact: str
    source_t545_verdict: str
    source_t545_status: str
    functoriality_definition: dict[str, Any]
    morphism_evaluations: tuple[APRDMorphismEvaluation, ...]
    composite_evaluations: tuple[APRDCompositeEvaluation, ...]
    controls: tuple[ControlEvaluation, ...]
    natural_morphism_cases: tuple[str, ...]
    functorial_composite_cases: tuple[str, ...]
    narrowed_cases: tuple[str, ...]
    rejected_controls: tuple[str, ...]
    aprd_functoriality_status: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t546_analysis() -> T546Result:
    t545_result = t545.run_t545_analysis()
    objects = _objects(t545_result)
    morphism_cases = _morphism_cases(objects)
    composite_cases = _composite_cases(objects)
    morphism_evaluations = tuple(
        evaluate_morphism_case(case) for case in morphism_cases
    )
    composite_evaluations = tuple(
        evaluate_composite_case(case) for case in composite_cases
    )
    natural_morphism_cases = tuple(
        evaluation.case_id
        for evaluation in morphism_evaluations
        if evaluation.natural
    )
    functorial_composite_cases = tuple(
        evaluation.case_id
        for evaluation in composite_evaluations
        if evaluation.functorial
    )
    narrowed_cases = tuple(
        evaluation.case_id
        for evaluation in (*morphism_evaluations, *composite_evaluations)
        if evaluation.narrowed
    )
    rejected_controls = tuple(
        evaluation.case_id
        for evaluation in (*morphism_evaluations, *composite_evaluations)
        if evaluation.rejected
    )
    controls = _controls(
        t545_result,
        morphism_evaluations,
        composite_evaluations,
        natural_morphism_cases,
        functorial_composite_cases,
        narrowed_cases,
        rejected_controls,
    )
    verdict = (
        VERDICT
        if t545_result.verdict == t545.VERDICT
        and t545_result.aprd_stability_status == t545.APRD_STABILITY_STATUS
        and natural_morphism_cases
        and functorial_composite_cases
        and all(control.passed for control in controls)
        else "aprd_finite_functoriality_gate_unexpected_status"
    )

    return T546Result(
        artifact=ARTIFACT,
        source_t545_verdict=t545_result.verdict,
        source_t545_status=t545_result.aprd_stability_status,
        functoriality_definition=_functoriality_definition(),
        morphism_evaluations=morphism_evaluations,
        composite_evaluations=composite_evaluations,
        controls=controls,
        natural_morphism_cases=natural_morphism_cases,
        functorial_composite_cases=functorial_composite_cases,
        narrowed_cases=narrowed_cases,
        rejected_controls=rejected_controls,
        aprd_functoriality_status=APRD_FUNCTORIALITY_STATUS,
        verdict=verdict,
        strongest_reading=(
            "The T545 APRD survivors clear a finite native functoriality gate: "
            "identity, native pullback, support-preserving restriction, and "
            "declared composites preserve the APRD assignment in this packet. "
            "Support loss narrows rather than promotes, and hostile controls "
            "reject non-native, unmapped, composite-mismatch, and "
            "outcome-selected repairs."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should test whether the functorial APRD "
            "object predicts a held-out native fixture's reconstruction debt "
            "before target-outcome reading. If it cannot predict a held-out "
            "case without retuning, retire or narrow the source-law route "
            "before finite-to-continuum movement."
        ),
        taf11_update=(
            "TAF11 remains the live Track-1 route. T546 clears finite native "
            "morphism and composite controls for APRD, but source-law status "
            "still waits on held-out predictive pressure."
        ),
        taf4_update=(
            "TAF4 remains blocked. APRD is now cleaner as a finite functorial "
            "feeder, but finite-to-continuum movement still needs predictive "
            "source-law pressure before geometric reading."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T546 strengthens APRD as a typed-gap feeder, not as a "
            "shadow-protection transfer theorem."
        ),
        claim_labels=_claim_labels(
            natural_morphism_cases,
            functorial_composite_cases,
            narrowed_cases,
            rejected_controls,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T546 leaves claim rows, Canon "
            "Index tiers, and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def evaluate_morphism_case(case: APRDMorphismCase) -> APRDMorphismEvaluation:
    pulled_back, unmapped = _pullback_assignment(
        case.target_debt_ids, case.pullback_map, case.completion_ids
    )
    expected = tuple(sorted(case.expected_pullback_debt_ids))
    source = tuple(sorted(case.source_debt_ids))

    if case.outcome_selected_repair:
        classification = "rejected_outcome_selected_target_repair"
        reason = "The target repair was selected after reading the desired outcome."
    elif not case.native_morphism:
        classification = "rejected_non_native_morphism"
        reason = "The proposed morphism is not native to the declared APRD objects."
    elif case.hidden_support_change:
        classification = "rejected_hidden_support_change"
        reason = "The morphism hides a support change while presenting as natural."
    elif not case.support_preserving:
        classification = "narrowed_by_support_losing_morphism"
        reason = (
            "The morphism removes support needed by the source APRD assignment, "
            "so it narrows rather than promotes."
        )
    elif unmapped:
        classification = "rejected_unmapped_target_debt"
        reason = "Target debt atoms lack a declared native pullback."
    elif pulled_back == source and pulled_back == expected:
        classification = "natural_aprd_morphism"
        reason = "The native pullback preserves the APRD debt assignment."
    elif pulled_back != expected:
        classification = "rejected_unexpected_pullback"
        reason = "The pullback does not match the predeclared expected APRD debt."
    else:
        classification = "failed_naturality_mismatch"
        reason = "The native pullback changes the source APRD assignment."

    natural = classification == "natural_aprd_morphism"
    narrowed = classification == "narrowed_by_support_losing_morphism"
    rejected = classification.startswith("rejected_") or classification.startswith(
        "failed_"
    )
    return APRDMorphismEvaluation(
        case_id=case.case_id,
        source_object_id=case.source_object_id,
        target_object_id=case.target_object_id,
        role=case.role,
        morphism_kind=case.morphism_kind,
        source_debt_ids=source,
        target_debt_ids=tuple(sorted(case.target_debt_ids)),
        pulled_back_debt_ids=pulled_back,
        unmapped_target_debt_ids=unmapped,
        expected_pullback_debt_ids=expected,
        classification=classification,
        expected_classification=case.expected_classification,
        classification_matches_expected=classification == case.expected_classification,
        natural=natural,
        narrowed=narrowed,
        rejected=rejected,
        reason=reason,
    )


def evaluate_composite_case(case: APRDCompositeCase) -> APRDCompositeEvaluation:
    composed_map, composition_unmapped = _compose_pullback_maps(
        case.first_pullback_map, case.second_pullback_map, case.target_debt_ids
    )
    composed, composed_unmapped = _pullback_assignment(
        case.target_debt_ids, composed_map, ()
    )
    direct, direct_unmapped = _pullback_assignment(
        case.target_debt_ids, case.direct_pullback_map, ()
    )
    unmapped = tuple(
        sorted(set(composition_unmapped) | set(composed_unmapped) | set(direct_unmapped))
    )
    source = tuple(sorted(case.source_debt_ids))

    if case.outcome_selected_repair:
        classification = "rejected_outcome_selected_composite_repair"
        reason = "The composite was repaired after reading the desired outcome."
    elif not case.native_morphisms:
        classification = "rejected_non_native_composite"
        reason = "At least one leg of the composite is not native."
    elif not case.support_preserving:
        classification = "narrowed_by_support_losing_composite"
        reason = (
            "The composite removes required support, so it narrows rather than "
            "promotes."
        )
    elif unmapped:
        classification = "rejected_unmapped_composite_debt"
        reason = "A target debt atom lacks a declared pullback through the composite."
    elif composed != direct:
        classification = "rejected_composite_mismatch"
        reason = "The two-step pullback does not equal the direct pullback."
    elif direct == source:
        classification = "functorial_composite_preserved"
        reason = "The two-step and direct APRD pullbacks agree with source debt."
    else:
        classification = "failed_composite_naturality"
        reason = "The composite agrees with itself but changes the source APRD debt."

    functorial = classification == "functorial_composite_preserved"
    narrowed = classification == "narrowed_by_support_losing_composite"
    rejected = classification.startswith("rejected_") or classification.startswith(
        "failed_"
    )
    return APRDCompositeEvaluation(
        case_id=case.case_id,
        role=case.role,
        source_object_id=case.source_object_id,
        target_object_id=case.target_object_id,
        source_debt_ids=source,
        composed_pullback_debt_ids=composed,
        direct_pullback_debt_ids=direct,
        unmapped_target_debt_ids=unmapped,
        classification=classification,
        expected_classification=case.expected_classification,
        classification_matches_expected=classification == case.expected_classification,
        functorial=functorial,
        narrowed=narrowed,
        rejected=rejected,
        reason=reason,
    )


def t546_result_to_dict(result: T546Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t545_verdict": result.source_t545_verdict,
        "source_t545_status": result.source_t545_status,
        "functoriality_definition": result.functoriality_definition,
        "morphism_evaluations": [
            {
                "case_id": evaluation.case_id,
                "source_object_id": evaluation.source_object_id,
                "target_object_id": evaluation.target_object_id,
                "role": evaluation.role,
                "morphism_kind": evaluation.morphism_kind,
                "source_debt_ids": list(evaluation.source_debt_ids),
                "target_debt_ids": list(evaluation.target_debt_ids),
                "pulled_back_debt_ids": list(evaluation.pulled_back_debt_ids),
                "unmapped_target_debt_ids": list(
                    evaluation.unmapped_target_debt_ids
                ),
                "expected_pullback_debt_ids": list(
                    evaluation.expected_pullback_debt_ids
                ),
                "classification": evaluation.classification,
                "expected_classification": evaluation.expected_classification,
                "classification_matches_expected": (
                    evaluation.classification_matches_expected
                ),
                "natural": evaluation.natural,
                "narrowed": evaluation.narrowed,
                "rejected": evaluation.rejected,
                "reason": evaluation.reason,
            }
            for evaluation in result.morphism_evaluations
        ],
        "composite_evaluations": [
            {
                "case_id": evaluation.case_id,
                "role": evaluation.role,
                "source_object_id": evaluation.source_object_id,
                "target_object_id": evaluation.target_object_id,
                "source_debt_ids": list(evaluation.source_debt_ids),
                "composed_pullback_debt_ids": list(
                    evaluation.composed_pullback_debt_ids
                ),
                "direct_pullback_debt_ids": list(
                    evaluation.direct_pullback_debt_ids
                ),
                "unmapped_target_debt_ids": list(
                    evaluation.unmapped_target_debt_ids
                ),
                "classification": evaluation.classification,
                "expected_classification": evaluation.expected_classification,
                "classification_matches_expected": (
                    evaluation.classification_matches_expected
                ),
                "functorial": evaluation.functorial,
                "narrowed": evaluation.narrowed,
                "rejected": evaluation.rejected,
                "reason": evaluation.reason,
            }
            for evaluation in result.composite_evaluations
        ],
        "controls": [
            {
                "control_id": control.control_id,
                "passed": control.passed,
                "reason": control.reason,
            }
            for control in result.controls
        ],
        "natural_morphism_cases": list(result.natural_morphism_cases),
        "functorial_composite_cases": list(result.functorial_composite_cases),
        "narrowed_cases": list(result.narrowed_cases),
        "rejected_controls": list(result.rejected_controls),
        "aprd_functoriality_status": result.aprd_functoriality_status,
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


def _functoriality_definition() -> dict[str, Any]:
    return {
        "name": "aprd_functoriality_naturality_packet",
        "source": "T545 APRD refinement-stable survivors",
        "natural_when": [
            "identity_morphisms_preserve_aprd_assignment",
            "native_pullback_preserves_source_debt_set",
            "support_preserving_restrictions_preserve_debt_set",
            "declared_composites_equal_direct_pullback",
        ],
        "not_natural": [
            "support_loss_hidden_as_native_morphism",
            "non_native_cross_domain_morphism",
            "unmapped_target_debt",
            "composite_pullback_mismatch",
            "outcome_selected_target_repair",
        ],
        "survivor_reading": (
            "Finite functoriality keeps APRD alive as a source-law feeder. "
            "Source-law reading still waits on held-out predictive pressure."
        ),
    }


def _objects(source_result: t545.T545Result) -> dict[str, APRDObject]:
    return {
        "t51_t58_observer_b": APRDObject(
            object_id="t51_t58_observer_b",
            source_t545_case_id="t51_refinement_splits_ambient_debt",
            canonical_debt_ids=_evaluation_debt(
                source_result, "t51_refinement_splits_ambient_debt"
            ),
        ),
        "t19_external_witness": APRDObject(
            object_id="t19_external_witness",
            source_t545_case_id="t19_refinement_external_witness_cover",
            canonical_debt_ids=_evaluation_debt(
                source_result, "t19_refinement_external_witness_cover"
            ),
        ),
        "record_transport": APRDObject(
            object_id="record_transport",
            source_t545_case_id="record_transport_support_preserving_restriction",
            canonical_debt_ids=_evaluation_debt(
                source_result, "record_transport_support_preserving_restriction"
            ),
        ),
    }


def _evaluation_debt(result: t545.T545Result, case_id: str) -> tuple[str, ...]:
    for evaluation in result.evaluations:
        if evaluation.case_id == case_id:
            return tuple(sorted(evaluation.canonical_debt_ids))
    raise KeyError(case_id)


def _morphism_cases(objects: dict[str, APRDObject]) -> tuple[APRDMorphismCase, ...]:
    t51 = objects["t51_t58_observer_b"].canonical_debt_ids
    t19 = objects["t19_external_witness"].canonical_debt_ids
    transport = objects["record_transport"].canonical_debt_ids
    t51_relabel = (
        "missing:ambient_pair:a_lock<=c_lock",
        "missing:provenance_record:rho_A_locked",
    )
    transport_relabel = ("missing:src_record_support", "missing:transport_cert")
    return (
        APRDMorphismCase(
            case_id="identity_t51_t58_debt_object",
            source_object_id="t51_t58_observer_b",
            target_object_id="t51_t58_observer_b",
            role="identity_control",
            morphism_kind="identity",
            source_debt_ids=t51,
            target_debt_ids=t51,
            pullback_map=_identity_map(t51),
            completion_ids=(),
            expected_pullback_debt_ids=t51,
            expected_classification="natural_aprd_morphism",
            native_morphism=True,
            support_preserving=True,
            hidden_support_change=False,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="identity_t19_external_witness",
            source_object_id="t19_external_witness",
            target_object_id="t19_external_witness",
            role="identity_control",
            morphism_kind="identity",
            source_debt_ids=t19,
            target_debt_ids=t19,
            pullback_map=_identity_map(t19),
            completion_ids=(),
            expected_pullback_debt_ids=t19,
            expected_classification="natural_aprd_morphism",
            native_morphism=True,
            support_preserving=True,
            hidden_support_change=False,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="t51_native_relabel_pullback_natural",
            source_object_id="t51_t58_observer_b",
            target_object_id="t51_t58_observer_b_relabel",
            role="native_pullback_control",
            morphism_kind="native_relabeling",
            source_debt_ids=t51,
            target_debt_ids=t51_relabel,
            pullback_map=(
                (
                    "missing:ambient_pair:a_lock<=c_lock",
                    "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                ),
                (
                    "missing:provenance_record:rho_A_locked",
                    "missing:provenance_record:r_A_locked",
                ),
            ),
            completion_ids=(),
            expected_pullback_debt_ids=t51,
            expected_classification="natural_aprd_morphism",
            native_morphism=True,
            support_preserving=True,
            hidden_support_change=False,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="record_transport_relabel_pullback_natural",
            source_object_id="record_transport",
            target_object_id="record_transport_relabel",
            role="native_pullback_control",
            morphism_kind="native_relabeling",
            source_debt_ids=transport,
            target_debt_ids=transport_relabel,
            pullback_map=(
                ("missing:src_record_support", "missing:source_record_support"),
                (
                    "missing:transport_cert",
                    "missing:transport_compatibility_certificate",
                ),
            ),
            completion_ids=(),
            expected_pullback_debt_ids=transport,
            expected_classification="natural_aprd_morphism",
            native_morphism=True,
            support_preserving=True,
            hidden_support_change=False,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="record_transport_support_preserving_restriction_natural",
            source_object_id="record_transport",
            target_object_id="record_transport_restricted_support",
            role="support_preserving_restriction_control",
            morphism_kind="restriction",
            source_debt_ids=transport,
            target_debt_ids=transport,
            pullback_map=_identity_map(transport),
            completion_ids=(),
            expected_pullback_debt_ids=transport,
            expected_classification="natural_aprd_morphism",
            native_morphism=True,
            support_preserving=True,
            hidden_support_change=False,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="t19_support_losing_morphism_narrows",
            source_object_id="t19_external_witness",
            target_object_id="t19_support_lost",
            role="support_loss_control",
            morphism_kind="restriction",
            source_debt_ids=t19,
            target_debt_ids=(),
            pullback_map=(),
            completion_ids=(),
            expected_pullback_debt_ids=(),
            expected_classification="narrowed_by_support_losing_morphism",
            native_morphism=True,
            support_preserving=False,
            hidden_support_change=False,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="hostile_non_native_t19_to_transport_map",
            source_object_id="t19_external_witness",
            target_object_id="record_transport",
            role="hostile_control",
            morphism_kind="cross_domain_shortcut",
            source_debt_ids=t19,
            target_debt_ids=transport,
            pullback_map=(
                (
                    "missing:source_record_support",
                    "missing:R_self_finality_external_witness",
                ),
                (
                    "missing:transport_compatibility_certificate",
                    "missing:R_self_finality_external_witness",
                ),
            ),
            completion_ids=(),
            expected_pullback_debt_ids=t19,
            expected_classification="rejected_non_native_morphism",
            native_morphism=False,
            support_preserving=True,
            hidden_support_change=False,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="hostile_hidden_support_change_as_natural",
            source_object_id="record_transport",
            target_object_id="record_transport_hidden_support_change",
            role="hostile_control",
            morphism_kind="hidden_support_change",
            source_debt_ids=transport,
            target_debt_ids=("missing:source_record_support",),
            pullback_map=(("missing:source_record_support", "missing:source_record_support"),),
            completion_ids=(),
            expected_pullback_debt_ids=("missing:source_record_support",),
            expected_classification="rejected_hidden_support_change",
            native_morphism=True,
            support_preserving=True,
            hidden_support_change=True,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="hostile_unmapped_target_debt",
            source_object_id="t51_t58_observer_b",
            target_object_id="t51_extra_target_debt",
            role="hostile_control",
            morphism_kind="unmapped_target_extension",
            source_debt_ids=t51,
            target_debt_ids=t51 + ("missing:secret_repair_channel",),
            pullback_map=_identity_map(t51),
            completion_ids=(),
            expected_pullback_debt_ids=t51,
            expected_classification="rejected_unmapped_target_debt",
            native_morphism=True,
            support_preserving=True,
            hidden_support_change=False,
            outcome_selected_repair=False,
        ),
        APRDMorphismCase(
            case_id="hostile_outcome_selected_target_repair",
            source_object_id="t19_external_witness",
            target_object_id="t19_repaired_after_outcome",
            role="hostile_control",
            morphism_kind="outcome_selected_repair",
            source_debt_ids=t19,
            target_debt_ids=t19,
            pullback_map=_identity_map(t19),
            completion_ids=t19,
            expected_pullback_debt_ids=(),
            expected_classification="rejected_outcome_selected_target_repair",
            native_morphism=True,
            support_preserving=True,
            hidden_support_change=False,
            outcome_selected_repair=True,
        ),
    )


def _composite_cases(objects: dict[str, APRDObject]) -> tuple[APRDCompositeCase, ...]:
    t51 = objects["t51_t58_observer_b"].canonical_debt_ids
    transport = objects["record_transport"].canonical_debt_ids
    t51_relabel = (
        "missing:ambient_pair:a_lock<=c_lock",
        "missing:provenance_record:rho_A_locked",
    )
    first_t51_relabel = (
        (
            "missing:ambient_pair:a_lock<=c_lock",
            "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
        ),
        (
            "missing:provenance_record:rho_A_locked",
            "missing:provenance_record:r_A_locked",
        ),
    )
    return (
        APRDCompositeCase(
            case_id="record_transport_two_step_restriction_composite",
            role="native_composite_control",
            source_object_id="record_transport",
            target_object_id="record_transport_twice_restricted",
            source_debt_ids=transport,
            middle_debt_ids=transport,
            target_debt_ids=transport,
            first_pullback_map=_identity_map(transport),
            second_pullback_map=_identity_map(transport),
            direct_pullback_map=_identity_map(transport),
            expected_classification="functorial_composite_preserved",
            native_morphisms=True,
            support_preserving=True,
            outcome_selected_repair=False,
        ),
        APRDCompositeCase(
            case_id="t51_relabel_then_identity_composite",
            role="native_composite_control",
            source_object_id="t51_t58_observer_b",
            target_object_id="t51_t58_observer_b_relabel",
            source_debt_ids=t51,
            middle_debt_ids=t51_relabel,
            target_debt_ids=t51_relabel,
            first_pullback_map=first_t51_relabel,
            second_pullback_map=_identity_map(t51_relabel),
            direct_pullback_map=first_t51_relabel,
            expected_classification="functorial_composite_preserved",
            native_morphisms=True,
            support_preserving=True,
            outcome_selected_repair=False,
        ),
        APRDCompositeCase(
            case_id="hostile_composite_drops_provenance",
            role="hostile_control",
            source_object_id="t51_t58_observer_b",
            target_object_id="t51_bad_composite",
            source_debt_ids=t51,
            middle_debt_ids=t51,
            target_debt_ids=t51,
            first_pullback_map=_identity_map(t51),
            second_pullback_map=(
                (
                    "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                    "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                ),
                (
                    "missing:provenance_record:r_A_locked",
                    "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                ),
            ),
            direct_pullback_map=_identity_map(t51),
            expected_classification="rejected_composite_mismatch",
            native_morphisms=True,
            support_preserving=True,
            outcome_selected_repair=False,
        ),
    )


def _controls(
    t545_result: t545.T545Result,
    morphism_evaluations: tuple[APRDMorphismEvaluation, ...],
    composite_evaluations: tuple[APRDCompositeEvaluation, ...],
    natural_morphism_cases: tuple[str, ...],
    functorial_composite_cases: tuple[str, ...],
    narrowed_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
) -> tuple[ControlEvaluation, ...]:
    by_morphism_id = {evaluation.case_id: evaluation for evaluation in morphism_evaluations}
    by_composite_id = {evaluation.case_id: evaluation for evaluation in composite_evaluations}
    identity_cases = {
        "identity_t51_t58_debt_object",
        "identity_t19_external_witness",
    }
    native_non_identity = {
        "t51_native_relabel_pullback_natural",
        "record_transport_relabel_pullback_natural",
        "record_transport_support_preserving_restriction_natural",
    }
    hostile_cases = {
        "hostile_non_native_t19_to_transport_map",
        "hostile_hidden_support_change_as_natural",
        "hostile_unmapped_target_debt",
        "hostile_outcome_selected_target_repair",
        "hostile_composite_drops_provenance",
    }
    return (
        ControlEvaluation(
            control_id="source_t545_consumed",
            passed=t545_result.verdict == t545.VERDICT,
            reason="T546 consumes the APRD stability survivors built by T545.",
        ),
        ControlEvaluation(
            control_id="expected_classifications_match",
            passed=all(
                evaluation.classification_matches_expected
                for evaluation in (*morphism_evaluations, *composite_evaluations)
            ),
            reason="Every fixture follows its predeclared functoriality branch.",
        ),
        ControlEvaluation(
            control_id="identity_morphisms_natural",
            passed=identity_cases.issubset(set(natural_morphism_cases)),
            reason="Identity morphisms preserve APRD assignments.",
        ),
        ControlEvaluation(
            control_id="native_morphism_naturality",
            passed=native_non_identity.issubset(set(natural_morphism_cases)),
            reason="Native relabeling and support-preserving restriction preserve APRD pullbacks.",
        ),
        ControlEvaluation(
            control_id="composite_functoriality",
            passed={
                "record_transport_two_step_restriction_composite",
                "t51_relabel_then_identity_composite",
            }.issubset(set(functorial_composite_cases)),
            reason="Declared two-step pullbacks equal direct pullbacks.",
        ),
        ControlEvaluation(
            control_id="support_loss_narrows_not_promotes",
            passed=narrowed_cases == ("t19_support_losing_morphism_narrows",),
            reason="Support-losing morphisms narrow rather than count as theorem evidence.",
        ),
        ControlEvaluation(
            control_id="hostile_controls_reject",
            passed=hostile_cases.issubset(set(rejected_controls))
            and by_composite_id["hostile_composite_drops_provenance"].rejected
            and by_morphism_id["hostile_unmapped_target_debt"].rejected,
            reason=(
                "Non-native maps, hidden support change, unmapped debt, "
                "outcome-selected repairs, and composite mismatch all reject."
            ),
        ),
        ControlEvaluation(
            control_id="no_claim_or_posture_movement",
            passed=True,
            reason="T546 performs no claim, canon, public-posture, or external movement.",
        ),
    )


def _claim_labels(
    natural_morphism_cases: tuple[str, ...],
    functorial_composite_cases: tuple[str, ...],
    narrowed_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Native APRD morphism cases preserved debt assignments: "
                + ", ".join(natural_morphism_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Declared APRD composites agreed with direct pullback: "
                + ", ".join(functorial_composite_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Support-losing morphisms narrowed rather than promoted: "
                + ", ".join(narrowed_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Hostile functoriality controls rejected: " + ", ".join(rejected_controls) + ".",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Finite native functoriality justifies a held-out prediction "
                "packet, not source-law, claim-ledger, or public-posture movement."
            ),
        ),
    )


def _identity_map(debt_ids: tuple[str, ...]) -> tuple[tuple[str, str], ...]:
    return tuple((debt_id, debt_id) for debt_id in debt_ids)


def _pullback_assignment(
    target_debt_ids: tuple[str, ...],
    pullback_map: tuple[tuple[str, str], ...],
    completion_ids: tuple[str, ...],
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    pullback = dict(pullback_map)
    completed = set(completion_ids)
    pulled = set()
    unmapped = set()
    for debt_id in target_debt_ids:
        if debt_id in completed:
            continue
        if debt_id not in pullback:
            unmapped.add(debt_id)
        else:
            pulled.add(pullback[debt_id])
    return tuple(sorted(pulled)), tuple(sorted(unmapped))


def _compose_pullback_maps(
    first_pullback_map: tuple[tuple[str, str], ...],
    second_pullback_map: tuple[tuple[str, str], ...],
    target_debt_ids: tuple[str, ...],
) -> tuple[tuple[tuple[str, str], ...], tuple[str, ...]]:
    first = dict(first_pullback_map)
    second = dict(second_pullback_map)
    composed = []
    unmapped = []
    for target_debt_id in target_debt_ids:
        if target_debt_id not in second:
            unmapped.append(target_debt_id)
            continue
        middle_debt_id = second[target_debt_id]
        if middle_debt_id not in first:
            unmapped.append(target_debt_id)
            continue
        composed.append((target_debt_id, first[middle_debt_id]))
    return tuple(composed), tuple(sorted(unmapped))


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T546 Results: APRD Functoriality Naturality Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- APRD functoriality status: `{payload['aprd_functoriality_status']}`",
        f"- Source T545 verdict: `{payload['source_t545_verdict']}`",
        f"- Source T545 status: `{payload['source_t545_status']}`",
        "- Natural morphism cases: "
        + ", ".join(f"`{item}`" for item in payload["natural_morphism_cases"]),
        "- Functorial composite cases: "
        + ", ".join(f"`{item}`" for item in payload["functorial_composite_cases"]),
        "- Narrowed cases: "
        + ", ".join(f"`{item}`" for item in payload["narrowed_cases"]),
        "- Rejected controls: "
        + ", ".join(f"`{item}`" for item in payload["rejected_controls"]),
        "",
        "## Functoriality Definition",
        "",
        f"- Name: `{payload['functoriality_definition']['name']}`",
        f"- Source: {payload['functoriality_definition']['source']}",
        "- Natural when: "
        + ", ".join(
            f"`{item}`" for item in payload["functoriality_definition"]["natural_when"]
        ),
        "- Not natural: "
        + ", ".join(
            f"`{item}`" for item in payload["functoriality_definition"]["not_natural"]
        ),
        f"- Survivor reading: {payload['functoriality_definition']['survivor_reading']}",
        "",
        "## Morphism Evaluations",
        "",
        "| case | source | target | kind | classification | pullback debt | natural? | rejected? |",
        "| --- | --- | --- | --- | --- | --- | :---: | :---: |",
    ]
    for evaluation in payload["morphism_evaluations"]:
        pullback = (
            ", ".join(f"`{item}`" for item in evaluation["pulled_back_debt_ids"])
            or "none"
        )
        lines.append(
            "| "
            f"`{evaluation['case_id']}` | "
            f"`{evaluation['source_object_id']}` | "
            f"`{evaluation['target_object_id']}` | "
            f"`{evaluation['morphism_kind']}` | "
            f"`{evaluation['classification']}` | "
            f"{pullback} | "
            f"{evaluation['natural']} | "
            f"{evaluation['rejected']} |"
        )
    lines.extend(
        [
            "",
            "## Composite Evaluations",
            "",
            "| case | source | target | classification | composed debt | direct debt | functorial? | rejected? |",
            "| --- | --- | --- | --- | --- | --- | :---: | :---: |",
        ]
    )
    for evaluation in payload["composite_evaluations"]:
        composed = (
            ", ".join(f"`{item}`" for item in evaluation["composed_pullback_debt_ids"])
            or "none"
        )
        direct = (
            ", ".join(f"`{item}`" for item in evaluation["direct_pullback_debt_ids"])
            or "none"
        )
        lines.append(
            "| "
            f"`{evaluation['case_id']}` | "
            f"`{evaluation['source_object_id']}` | "
            f"`{evaluation['target_object_id']}` | "
            f"`{evaluation['classification']}` | "
            f"{composed} | "
            f"{direct} | "
            f"{evaluation['functorial']} | "
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


def write_results(result: T546Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t546_result_to_dict(result)
    json_path = results_dir / "T546-aprd-functoriality-naturality-packet-v0.1.json"
    md_path = results_dir / "T546-aprd-functoriality-naturality-packet-v0.1-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t546_analysis()
    payload = t546_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
