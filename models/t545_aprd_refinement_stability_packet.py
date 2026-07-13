"""T545: APRD refinement stability packet.

T544 kept accessible provenance reconstruction debt (APRD) alive as a finite
source-law feeder. T545 asks the next narrow question: do the surviving APRD
debt sets remain the same under harmless refinement, relabeling, and
support-preserving restriction maps?

The answer remains bounded. Stability under these finite presentation changes
does not establish a source law; it only earns the next functoriality check.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t544_aprd_minimality_absorber_separation_gate as t544


ARTIFACT = "T545-aprd-refinement-stability-packet-v0.1"
VERDICT = "aprd_refinement_stability_gate_clears_harmless_changes"
APRD_STABILITY_STATUS = "STABLE_PRESENTATION_SOURCE_LAW_NOT_EARNED"
NEXT_PACKET = "t546_aprd_functoriality_naturality_packet"

NOT_CLAIMED = (
    "T545 does not establish a source law, prove a shadow-protection theorem, "
    "derive spacetime, prove manifoldlikeness, repair T528, reverse T223, "
    "unpause S1, promote S1, change claim status, change Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, or move cross-repo truth. It is a finite "
    "APRD refinement-stability gate only."
)


@dataclass(frozen=True)
class APRDStabilityCase:
    case_id: str
    source_t544_case_id: str
    transform_kind: str
    role: str
    debt_ids: tuple[str, ...]
    alias_map: tuple[tuple[str, str], ...]
    completion_ids: tuple[str, ...]
    expected_canonical_debt_ids: tuple[str, ...]
    expected_classification: str
    harmless_presentation_change: bool
    support_preserving: bool
    restriction_map_declared: bool
    hidden_support_change: bool
    set_valued: bool


@dataclass(frozen=True)
class APRDStabilityEvaluation:
    case_id: str
    source_t544_case_id: str
    transform_kind: str
    role: str
    source_debt_ids: tuple[str, ...]
    transformed_debt_ids: tuple[str, ...]
    canonical_debt_ids: tuple[str, ...]
    expected_canonical_debt_ids: tuple[str, ...]
    classification: str
    expected_classification: str
    classification_matches_expected: bool
    stable: bool
    narrowed_by_nonharmless_restriction: bool
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
class T545Result:
    artifact: str
    source_t544_verdict: str
    source_t544_status: str
    stability_definition: dict[str, Any]
    evaluations: tuple[APRDStabilityEvaluation, ...]
    controls: tuple[ControlEvaluation, ...]
    stable_cases: tuple[str, ...]
    narrowed_cases: tuple[str, ...]
    rejected_controls: tuple[str, ...]
    aprd_stability_status: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t545_analysis() -> T545Result:
    t544_result = t544.run_t544_analysis()
    cases = _stability_cases()
    evaluations = tuple(evaluate_stability_case(case, t544_result) for case in cases)
    stable_cases = tuple(
        evaluation.case_id for evaluation in evaluations if evaluation.stable
    )
    narrowed_cases = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.narrowed_by_nonharmless_restriction
    )
    rejected_controls = tuple(
        evaluation.case_id for evaluation in evaluations if evaluation.rejected
    )
    controls = _controls(evaluations, stable_cases, narrowed_cases, rejected_controls)
    verdict = (
        VERDICT
        if t544_result.verdict == t544.VERDICT
        and t544_result.aprd_gate_status == t544.APRD_GATE_STATUS
        and all(control.passed for control in controls)
        else "aprd_refinement_stability_gate_unexpected_status"
    )

    return T545Result(
        artifact=ARTIFACT,
        source_t544_verdict=t544_result.verdict,
        source_t544_status=t544_result.aprd_gate_status,
        stability_definition=_stability_definition(),
        evaluations=evaluations,
        controls=controls,
        stable_cases=stable_cases,
        narrowed_cases=narrowed_cases,
        rejected_controls=rejected_controls,
        aprd_stability_status=APRD_STABILITY_STATUS,
        verdict=verdict,
        strongest_reading=(
            "The T544 non-detector APRD survivors are stable under finite "
            "harmless refinement, relabeling, and declared support-preserving "
            "restriction maps in this packet. Non-harmless support loss narrows "
            "the object rather than promoting it, and hostile controls reject "
            "hidden support changes, padding, and scalar replacement."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should test whether APRD assignments behave "
            "naturally across native morphisms and composites, not merely under "
            "finite presentation changes."
        ),
        taf11_update=(
            "TAF11 remains the live Track-1 route. T545 clears finite "
            "refinement-stability controls for APRD, but source-law status "
            "still waits on functorial naturality across native morphisms."
        ),
        taf4_update=(
            "TAF4 remains blocked. T545 gives APRD a cleaner finite feeder, but "
            "finite-to-continuum movement still needs functorial behavior before "
            "restriction-map stability can be read geometrically."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T545 strengthens APRD as a typed-gap feeder, not as a "
            "shadow-protection transfer theorem."
        ),
        claim_labels=_claim_labels(stable_cases, narrowed_cases, rejected_controls),
        claim_ledger_update=(
            "No claim-ledger update is earned. T545 leaves claim rows, Canon "
            "Index tiers, and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def evaluate_stability_case(
    case: APRDStabilityCase, source_result: t544.T544Result
) -> APRDStabilityEvaluation:
    source = _source_evaluation(case.source_t544_case_id, source_result)
    source_debt = tuple(source.residual_debt_ids)
    canonical = _canonical_debt_ids(case.debt_ids, case.alias_map, case.completion_ids)
    expected = tuple(sorted(case.expected_canonical_debt_ids))
    source_set = set(source_debt)
    canonical_set = set(canonical)

    if not case.set_valued:
        classification = "rejected_scalar_rank_collapse"
        reason = "The transform replaced the APRD debt set with a scalar value."
    elif case.hidden_support_change and case.harmless_presentation_change:
        classification = "rejected_hidden_support_change"
        reason = (
            "The transform claimed to be harmless while changing the support "
            "needed to interpret the debt set."
        )
    elif canonical_set > source_set:
        classification = "rejected_nonminimal_padding"
        reason = "The transform added debt atoms beyond the T544 survivor set."
    elif case.harmless_presentation_change and canonical == source_debt:
        classification = "stable_harmless_presentation"
        reason = (
            "Canonical APRD debt labels are unchanged by the declared "
            "presentation transform."
        )
    elif (
        case.transform_kind == "restriction"
        and case.support_preserving
        and case.restriction_map_declared
        and canonical == source_debt
    ):
        classification = "stable_support_preserving_restriction"
        reason = (
            "The declared restriction map preserves the support carrying the "
            "APRD debt set."
        )
    elif (
        case.transform_kind == "restriction"
        and not case.support_preserving
        and case.restriction_map_declared
        and canonical_set < source_set
    ):
        classification = "narrowed_by_nonharmless_restriction"
        reason = (
            "The restriction removes support needed by the source APRD object, "
            "so the result narrows rather than counts as harmless stability."
        )
    elif case.harmless_presentation_change and canonical != source_debt:
        classification = "rejected_unstable_harmless_transform"
        reason = (
            "A transform declared harmless changed the canonical APRD debt set."
        )
    elif canonical != expected:
        classification = "rejected_unexpected_debt_mutation"
        reason = "The transform produced an unexpected canonical debt set."
    else:
        classification = "unexpected_stability_state"
        reason = "The case did not match a declared T545 branch."

    stable = classification in {
        "stable_harmless_presentation",
        "stable_support_preserving_restriction",
    }
    narrowed = classification == "narrowed_by_nonharmless_restriction"
    rejected = classification.startswith("rejected_")
    return APRDStabilityEvaluation(
        case_id=case.case_id,
        source_t544_case_id=case.source_t544_case_id,
        transform_kind=case.transform_kind,
        role=case.role,
        source_debt_ids=source_debt,
        transformed_debt_ids=tuple(sorted(case.debt_ids)),
        canonical_debt_ids=canonical,
        expected_canonical_debt_ids=expected,
        classification=classification,
        expected_classification=case.expected_classification,
        classification_matches_expected=classification == case.expected_classification,
        stable=stable,
        narrowed_by_nonharmless_restriction=narrowed,
        rejected=rejected,
        reason=reason,
    )


def t545_result_to_dict(result: T545Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t544_verdict": result.source_t544_verdict,
        "source_t544_status": result.source_t544_status,
        "stability_definition": result.stability_definition,
        "evaluations": [
            {
                "case_id": evaluation.case_id,
                "source_t544_case_id": evaluation.source_t544_case_id,
                "transform_kind": evaluation.transform_kind,
                "role": evaluation.role,
                "source_debt_ids": list(evaluation.source_debt_ids),
                "transformed_debt_ids": list(evaluation.transformed_debt_ids),
                "canonical_debt_ids": list(evaluation.canonical_debt_ids),
                "expected_canonical_debt_ids": list(
                    evaluation.expected_canonical_debt_ids
                ),
                "classification": evaluation.classification,
                "expected_classification": evaluation.expected_classification,
                "classification_matches_expected": (
                    evaluation.classification_matches_expected
                ),
                "stable": evaluation.stable,
                "narrowed_by_nonharmless_restriction": (
                    evaluation.narrowed_by_nonharmless_restriction
                ),
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
        "stable_cases": list(result.stable_cases),
        "narrowed_cases": list(result.narrowed_cases),
        "rejected_controls": list(result.rejected_controls),
        "aprd_stability_status": result.aprd_stability_status,
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


def _stability_definition() -> dict[str, Any]:
    return {
        "name": "aprd_refinement_stability_packet",
        "source": "T544 APRD minimal non-detector survivors",
        "stable_when": [
            "canonical_debt_set_preserved_by_harmless_refinement",
            "canonical_debt_set_preserved_by_harmless_relabeling",
            "canonical_debt_set_preserved_by_declared_support_preserving_restriction",
        ],
        "not_stability": [
            "support_loss_hidden_as_relabeling",
            "padding_extra_debt_atoms",
            "scalar_rank_replacement",
            "nonharmless_restriction_read_as_theorem_evidence",
        ],
        "survivor_reading": (
            "Finite stability keeps APRD alive as a source-law feeder. Source-law "
            "reading still waits on functorial naturality across native morphisms."
        ),
    }


def _stability_cases() -> tuple[APRDStabilityCase, ...]:
    t51_base = (
        "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
        "missing:provenance_record:r_A_locked",
    )
    t19_base = ("missing:R_self_finality_external_witness",)
    transport_base = (
        "missing:source_record_support",
        "missing:transport_compatibility_certificate",
    )
    return (
        APRDStabilityCase(
            case_id="t51_refinement_splits_ambient_debt",
            source_t544_case_id="t51_t58_observer_b_non_detector_separator",
            transform_kind="refinement",
            role="stable_presentation_control",
            debt_ids=(
                "refined:e1_A_locking_source",
                "refined:e3_composite_locking_target",
                "missing:provenance_record:r_A_locked",
            ),
            alias_map=(
                (
                    "refined:e1_A_locking_source",
                    "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                ),
                (
                    "refined:e3_composite_locking_target",
                    "missing:ambient_pair:e1_A_locking<=e3_composite_locking",
                ),
            ),
            completion_ids=(),
            expected_canonical_debt_ids=t51_base,
            expected_classification="stable_harmless_presentation",
            harmless_presentation_change=True,
            support_preserving=True,
            restriction_map_declared=False,
            hidden_support_change=False,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="t51_relabeling_renames_events",
            source_t544_case_id="t51_t58_observer_b_non_detector_separator",
            transform_kind="relabeling",
            role="stable_presentation_control",
            debt_ids=(
                "missing:ambient_pair:a_lock<=c_lock",
                "missing:provenance_record:rho_A_locked",
            ),
            alias_map=(
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
            expected_canonical_debt_ids=t51_base,
            expected_classification="stable_harmless_presentation",
            harmless_presentation_change=True,
            support_preserving=True,
            restriction_map_declared=False,
            hidden_support_change=False,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="t19_refinement_external_witness_cover",
            source_t544_case_id="t19_self_finality_external_witness_separator",
            transform_kind="refinement",
            role="stable_presentation_control",
            debt_ids=(
                "missing:R_self_finality_external_witness.left_patch",
                "missing:R_self_finality_external_witness.right_patch",
            ),
            alias_map=(
                (
                    "missing:R_self_finality_external_witness.left_patch",
                    "missing:R_self_finality_external_witness",
                ),
                (
                    "missing:R_self_finality_external_witness.right_patch",
                    "missing:R_self_finality_external_witness",
                ),
            ),
            completion_ids=(),
            expected_canonical_debt_ids=t19_base,
            expected_classification="stable_harmless_presentation",
            harmless_presentation_change=True,
            support_preserving=True,
            restriction_map_declared=False,
            hidden_support_change=False,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="record_transport_relabeling_certificate",
            source_t544_case_id="record_transport_same_rank_separator",
            transform_kind="relabeling",
            role="stable_presentation_control",
            debt_ids=("missing:src_record_support", "missing:transport_cert"),
            alias_map=(
                ("missing:src_record_support", "missing:source_record_support"),
                (
                    "missing:transport_cert",
                    "missing:transport_compatibility_certificate",
                ),
            ),
            completion_ids=(),
            expected_canonical_debt_ids=transport_base,
            expected_classification="stable_harmless_presentation",
            harmless_presentation_change=True,
            support_preserving=True,
            restriction_map_declared=False,
            hidden_support_change=False,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="record_transport_support_preserving_restriction",
            source_t544_case_id="record_transport_same_rank_separator",
            transform_kind="restriction",
            role="support_preserving_restriction_control",
            debt_ids=transport_base,
            alias_map=(),
            completion_ids=(),
            expected_canonical_debt_ids=transport_base,
            expected_classification="stable_support_preserving_restriction",
            harmless_presentation_change=False,
            support_preserving=True,
            restriction_map_declared=True,
            hidden_support_change=False,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="t19_support_losing_restriction_narrows",
            source_t544_case_id="t19_self_finality_external_witness_separator",
            transform_kind="restriction",
            role="nonharmless_restriction_control",
            debt_ids=(),
            alias_map=(),
            completion_ids=(),
            expected_canonical_debt_ids=(),
            expected_classification="narrowed_by_nonharmless_restriction",
            harmless_presentation_change=False,
            support_preserving=False,
            restriction_map_declared=True,
            hidden_support_change=False,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="hostile_harmless_relabel_changes_debt",
            source_t544_case_id="t19_self_finality_external_witness_separator",
            transform_kind="relabeling",
            role="hostile_control",
            debt_ids=("missing:R_self_finality_private_witness",),
            alias_map=(),
            completion_ids=(),
            expected_canonical_debt_ids=t19_base,
            expected_classification="rejected_unstable_harmless_transform",
            harmless_presentation_change=True,
            support_preserving=True,
            restriction_map_declared=False,
            hidden_support_change=False,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="hostile_refinement_adds_padding",
            source_t544_case_id="t51_t58_observer_b_non_detector_separator",
            transform_kind="refinement",
            role="hostile_control",
            debt_ids=t51_base + ("padding:rank_hint",),
            alias_map=(),
            completion_ids=(),
            expected_canonical_debt_ids=t51_base,
            expected_classification="rejected_nonminimal_padding",
            harmless_presentation_change=True,
            support_preserving=True,
            restriction_map_declared=False,
            hidden_support_change=False,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="hostile_hidden_support_change",
            source_t544_case_id="record_transport_same_rank_separator",
            transform_kind="relabeling",
            role="hostile_control",
            debt_ids=("missing:source_record_support",),
            alias_map=(),
            completion_ids=(),
            expected_canonical_debt_ids=transport_base,
            expected_classification="rejected_hidden_support_change",
            harmless_presentation_change=True,
            support_preserving=False,
            restriction_map_declared=False,
            hidden_support_change=True,
            set_valued=True,
        ),
        APRDStabilityCase(
            case_id="hostile_scalar_rank_replacement",
            source_t544_case_id="record_transport_same_rank_separator",
            transform_kind="rank_proxy",
            role="hostile_control",
            debt_ids=("rank:2",),
            alias_map=(),
            completion_ids=(),
            expected_canonical_debt_ids=transport_base,
            expected_classification="rejected_scalar_rank_collapse",
            harmless_presentation_change=True,
            support_preserving=True,
            restriction_map_declared=False,
            hidden_support_change=False,
            set_valued=False,
        ),
    )


def _controls(
    evaluations: tuple[APRDStabilityEvaluation, ...],
    stable_cases: tuple[str, ...],
    narrowed_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
) -> tuple[ControlEvaluation, ...]:
    by_id = {evaluation.case_id: evaluation for evaluation in evaluations}
    stable_presentation = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.role == "stable_presentation_control"
    )
    hostile = tuple(
        evaluation.case_id
        for evaluation in evaluations
        if evaluation.role == "hostile_control"
    )
    return (
        ControlEvaluation(
            control_id="source_t544_consumed",
            passed=t544.run_t544_analysis().verdict == t544.VERDICT,
            reason="T545 consumes the APRD survivors built by T544.",
        ),
        ControlEvaluation(
            control_id="expected_classifications_match",
            passed=all(
                evaluation.classification_matches_expected
                for evaluation in evaluations
            ),
            reason="Every fixture follows its predeclared stability branch.",
        ),
        ControlEvaluation(
            control_id="harmless_refinement_and_relabeling_stable",
            passed=set(stable_presentation).issubset(set(stable_cases)),
            reason=(
                "Canonical APRD debt sets survive declared harmless refinement "
                "and relabeling."
            ),
        ),
        ControlEvaluation(
            control_id="support_preserving_restriction_stable",
            passed=by_id[
                "record_transport_support_preserving_restriction"
            ].classification
            == "stable_support_preserving_restriction",
            reason="Declared support-preserving restriction keeps the debt set fixed.",
        ),
        ControlEvaluation(
            control_id="nonharmless_restriction_narrows_not_promotes",
            passed=narrowed_cases == ("t19_support_losing_restriction_narrows",),
            reason=(
                "A restriction that removes needed support is treated as a "
                "narrowing, not theorem evidence."
            ),
        ),
        ControlEvaluation(
            control_id="hostile_controls_reject",
            passed=set(hostile).issubset(set(rejected_controls)),
            reason=(
                "Hidden support change, padding, unstable harmless relabeling, "
                "and scalar replacement all reject."
            ),
        ),
        ControlEvaluation(
            control_id="no_claim_or_posture_movement",
            passed=True,
            reason="T545 performs no claim, canon, public-posture, or external movement.",
        ),
    )


def _source_evaluation(
    source_case_id: str, source_result: t544.T544Result
) -> t544.APRDGateEvaluation:
    for evaluation in source_result.evaluations:
        if evaluation.case_id == source_case_id:
            return evaluation
    raise KeyError(source_case_id)


def _canonical_debt_ids(
    debt_ids: tuple[str, ...],
    alias_map: tuple[tuple[str, str], ...],
    completion_ids: tuple[str, ...],
) -> tuple[str, ...]:
    aliases = dict(alias_map)
    completions = set(completion_ids)
    canonical = set()
    for debt_id in debt_ids:
        current = debt_id
        seen = set()
        while current in aliases:
            if current in seen:
                raise ValueError(f"Alias cycle detected at {current}")
            seen.add(current)
            current = aliases[current]
        if current not in completions:
            canonical.add(current)
    return tuple(sorted(canonical))


def _claim_labels(
    stable_cases: tuple[str, ...],
    narrowed_cases: tuple[str, ...],
    rejected_controls: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "APRD survivor debt sets stayed canonical under finite harmless "
                "presentation changes: " + ", ".join(stable_cases) + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Non-harmless restriction narrowed rather than promoted: "
                + ", ".join(narrowed_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Hostile stability controls rejected: " + ", ".join(rejected_controls) + ".",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Finite presentation stability justifies a functoriality packet, "
                "not source-law, claim-ledger, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T545 Results: APRD Refinement Stability Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- APRD stability status: `{payload['aprd_stability_status']}`",
        f"- Source T544 verdict: `{payload['source_t544_verdict']}`",
        f"- Source T544 status: `{payload['source_t544_status']}`",
        "- Stable cases: " + ", ".join(f"`{item}`" for item in payload["stable_cases"]),
        "- Narrowed cases: "
        + ", ".join(f"`{item}`" for item in payload["narrowed_cases"]),
        "- Rejected controls: "
        + ", ".join(f"`{item}`" for item in payload["rejected_controls"]),
        "",
        "## Stability Definition",
        "",
        f"- Name: `{payload['stability_definition']['name']}`",
        f"- Source: {payload['stability_definition']['source']}",
        "- Stable when: "
        + ", ".join(
            f"`{item}`" for item in payload["stability_definition"]["stable_when"]
        ),
        "- Not stability: "
        + ", ".join(
            f"`{item}`" for item in payload["stability_definition"]["not_stability"]
        ),
        f"- Survivor reading: {payload['stability_definition']['survivor_reading']}",
        "",
        "## Evaluations",
        "",
        "| case | source | transform | classification | canonical debt | stable? | rejected? |",
        "| --- | --- | --- | --- | --- | :---: | :---: |",
    ]
    for evaluation in payload["evaluations"]:
        debt = (
            ", ".join(f"`{item}`" for item in evaluation["canonical_debt_ids"])
            or "none"
        )
        lines.append(
            "| "
            f"`{evaluation['case_id']}` | "
            f"`{evaluation['source_t544_case_id']}` | "
            f"`{evaluation['transform_kind']}` | "
            f"`{evaluation['classification']}` | "
            f"{debt} | "
            f"{evaluation['stable']} | "
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


def write_results(result: T545Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t545_result_to_dict(result)
    json_path = results_dir / "T545-aprd-refinement-stability-packet-v0.1.json"
    md_path = results_dir / "T545-aprd-refinement-stability-packet-v0.1-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t545_analysis()
    payload = t545_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
