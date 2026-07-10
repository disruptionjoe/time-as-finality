"""T526: S1 reference-law gap audit.

T525 showed that the repaired finite S1 diagnostic suite can pass seeded
random 1+1 causal-diamond controls while rejecting the current finite colimit
witnesses. T526 turns that into a sharper research diagnosis: the repaired
suite is not the blocker; the blocker is the missing TaF-native source law.

The audit treats the 1+1 causal-diamond random law as an external reference
law. It is useful calibration because it clears the repaired suite, but it is
not S1 evidence because it imports Lorentzian light-cone coordinates instead
of descending from finality-domain colimits.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    CausetAudit,
    CausetDiagnostics,
    audit_finality_colimit_causet,
)
from models.t524_t126_random_sprinkle_diagnostic_repair import (
    DEFAULT_SEEDS,
    random_lightcone_sprinkle_datum,
)
from models.t525_repaired_s1_manifoldlikeness_suite import (
    HARD_REJECTION_CLASSIFICATIONS,
    run_t525_analysis,
)


REFERENCE_SIZES = (8, 12, 16, 20)
REFERENCE_SEEDS = DEFAULT_SEEDS

VERDICT = "s1_reference_law_calibrates_suite_but_taf_descent_missing"
NOT_CLAIMED = (
    "T526 does not derive spacetime, prove manifoldlikeness, establish a "
    "TaF-native sprinkling law, reconstruct a Lorentzian metric, prove an "
    "embedding or continuum theorem, reverse T223, or promote S1. It separates "
    "external reference-law calibration from S1 evidence."
)


@dataclass(frozen=True)
class ReferenceSampleAudit:
    law_id: str
    event_count: int
    seed: int
    t126_classification: str
    order_dimension_quarantined: bool
    ordering_fraction: Fraction
    height: int
    width: int
    largest_interval_size: int
    hard_gate_passed: bool
    ordering_fraction_in_band: bool
    height_in_band: bool
    width_in_band: bool
    largest_interval_in_band: bool
    repaired_suite_passed: bool
    reason: str


@dataclass(frozen=True)
class LawPacket:
    packet_id: str
    description: str
    repaired_suite_passed: bool | None
    has_executed_samples: bool
    predeclared_generator: bool
    generator_source: str
    descends_from_finality_colimit: bool
    imports_lorentzian_coordinates: bool
    conditions_on_repaired_suite_success: bool
    names_later_lorentzian_constraints: bool
    supplies_hostile_controls: bool
    no_overclaim_language: bool
    requests_s1_promotion: bool = False
    synthetic_control_only: bool = False


@dataclass(frozen=True)
class LawPacketDecision:
    packet_id: str
    classification: str
    admitted_as_future_review_target: bool
    counts_as_s1_evidence: bool
    missing_requirements: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class T526Result:
    reference_law: str
    reference_basis: str
    sample_audits: tuple[ReferenceSampleAudit, ...]
    reference_sample_count: int
    reference_pass_count: int
    reference_pass_rate: Fraction
    reference_law_passes_repaired_suite: bool
    current_finite_colimit_survivor_count: int
    current_finite_colimits_survive_repaired_suite: bool
    law_packet_decisions: tuple[LawPacketDecision, ...]
    external_reference_counts_as_s1_evidence: bool
    taf_native_future_target_admitted: bool
    verdict: str
    strongest_reading: str
    improved: str
    missing_object: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    suggested_next: str
    not_claimed: str


def run_t526_analysis() -> T526Result:
    t525 = run_t525_analysis()
    bands = {band.event_count: band for band in t525.calibration_bands}
    sample_audits = tuple(
        _audit_reference_sample(event_count=size, seed=seed, band=bands[size])
        for size in REFERENCE_SIZES
        for seed in REFERENCE_SEEDS
    )
    reference_pass_count = sum(audit.repaired_suite_passed for audit in sample_audits)
    reference_sample_count = len(sample_audits)
    reference_pass_rate = Fraction(reference_pass_count, reference_sample_count)
    reference_all_pass = reference_pass_count == reference_sample_count

    packets = _law_packets(
        reference_law_passed=reference_all_pass,
        current_finite_colimits_passed=t525.current_finite_colimits_survive_repaired_suite,
    )
    decisions = tuple(_evaluate_packet(packet) for packet in packets)
    decisions_by_id = {decision.packet_id: decision for decision in decisions}
    external_counts_as_evidence = decisions_by_id[
        "external_1p1_causal_diamond_reference_law"
    ].counts_as_s1_evidence
    taf_target_admitted = decisions_by_id[
        "future_taf_native_generator_bridge_target"
    ].admitted_as_future_review_target

    verdict = (
        VERDICT
        if reference_all_pass
        and t525.current_finite_colimit_survivor_count == 0
        and not external_counts_as_evidence
        and taf_target_admitted
        else "s1_reference_law_gap_audit_unexpected_status"
    )

    return T526Result(
        reference_law="external_seeded_1p1_causal_diamond_random_law",
        reference_basis=(
            "Sample independent u,v light-cone coordinates and order p<q iff "
            "u_p<u_q and v_p<v_q. This is a standard external Lorentzian "
            "causal-diamond reference law, not a finality-colimit generator."
        ),
        sample_audits=sample_audits,
        reference_sample_count=reference_sample_count,
        reference_pass_count=reference_pass_count,
        reference_pass_rate=reference_pass_rate,
        reference_law_passes_repaired_suite=reference_all_pass,
        current_finite_colimit_survivor_count=(
            t525.current_finite_colimit_survivor_count
        ),
        current_finite_colimits_survive_repaired_suite=(
            t525.current_finite_colimits_survive_repaired_suite
        ),
        law_packet_decisions=decisions,
        external_reference_counts_as_s1_evidence=external_counts_as_evidence,
        taf_native_future_target_admitted=taf_target_admitted,
        verdict=verdict,
        strongest_reading=(
            "The repaired S1 suite is passable: the predeclared external 1+1 "
            "causal-diamond reference law clears it on every calibrated sample. "
            "The current TaF finite colimits still do not. Therefore the live "
            "S1 blocker is not the repaired manifoldlikeness screen itself; it "
            "is the missing finality-native generator or bridge that produces "
            "such a law without importing Lorentzian coordinates."
        ),
        improved=(
            "T526 turns T525's negative result into a constructive calibration "
            "target. Future S1 work can now be asked to match a concrete "
            "reference-law packet while also paying the descent burden that the "
            "reference law deliberately does not pay."
        ),
        missing_object=(
            "A predeclared finality-native generator, measure law, or continuum "
            "bridge whose finite samples descend from finality-domain colimit "
            "data, pass the repaired suite, include hostile controls, and name "
            "later Lorentzian causal/metric/covariance/embedding constraints."
        ),
        falsification_condition=(
            "T526 fails if the external reference law does not pass the repaired "
            "suite, if current finite colimits survive T525 after all, if an "
            "imported Lorentzian coordinate law is counted as S1 evidence, or "
            "if the result is used to promote S1 before a TaF-native descent law "
            "exists."
        ),
        s1_update=(
            "S1 remains `requires_added_assumption`. T526 narrows the next "
            "positive burden: not merely 'pass repaired manifoldlikeness', but "
            "produce a finality-native source law or bridge that passes it "
            "without importing the target spacetime structure."
        ),
        claim_ledger_update=(
            "Record T526 as S1 claim-history only: external reference law "
            "calibration passes the repaired suite, current finite colimits do "
            "not, and the missing object is finality-native generator descent. "
            "No claim row, S1 status movement, or T223 reversal."
        ),
        suggested_next=(
            "Attempt the smallest TaF-native generator descent packet: declare "
            "record-domain data and local compatibility rules first, generate "
            "finite causets without u/v coordinates as primitives, then compare "
            "against the T526 reference-law diagnostics and T525 repaired suite."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t526_result_to_dict(result: T526Result) -> dict[str, Any]:
    return {
        "reference_law": result.reference_law,
        "reference_basis": result.reference_basis,
        "sample_audits": [_sample_to_dict(audit) for audit in result.sample_audits],
        "reference_sample_count": result.reference_sample_count,
        "reference_pass_count": result.reference_pass_count,
        "reference_pass_rate": _fraction_to_dict(result.reference_pass_rate),
        "reference_law_passes_repaired_suite": (
            result.reference_law_passes_repaired_suite
        ),
        "current_finite_colimit_survivor_count": (
            result.current_finite_colimit_survivor_count
        ),
        "current_finite_colimits_survive_repaired_suite": (
            result.current_finite_colimits_survive_repaired_suite
        ),
        "law_packet_decisions": [
            _decision_to_dict(decision) for decision in result.law_packet_decisions
        ],
        "external_reference_counts_as_s1_evidence": (
            result.external_reference_counts_as_s1_evidence
        ),
        "taf_native_future_target_admitted": result.taf_native_future_target_admitted,
        "verdict": result.verdict,
        "strongest_reading": result.strongest_reading,
        "improved": result.improved,
        "missing_object": result.missing_object,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _audit_reference_sample(
    *,
    event_count: int,
    seed: int,
    band: Any,
) -> ReferenceSampleAudit:
    audit = audit_finality_colimit_causet(
        random_lightcone_sprinkle_datum(event_count, seed)
    )
    diagnostics = _diagnostics(audit)
    largest_interval = _largest_interval_size(diagnostics)
    hard_gate_passed = audit.classification not in HARD_REJECTION_CLASSIFICATIONS
    ordering_ok = (
        band.ordering_fraction_min
        <= diagnostics.comparable_fraction
        <= band.ordering_fraction_max
    )
    height_ok = band.height_min <= diagnostics.height <= band.height_max
    width_ok = band.width_min <= diagnostics.width <= band.width_max
    interval_ok = (
        band.largest_interval_min
        <= largest_interval
        <= band.largest_interval_max
    )
    repaired_passed = (
        hard_gate_passed and ordering_ok and height_ok and width_ok and interval_ok
    )
    return ReferenceSampleAudit(
        law_id="external_1p1_causal_diamond_reference_law",
        event_count=event_count,
        seed=seed,
        t126_classification=audit.classification,
        order_dimension_quarantined=(
            audit.classification == "order_dimension_obstruction"
        ),
        ordering_fraction=diagnostics.comparable_fraction,
        height=diagnostics.height,
        width=diagnostics.width,
        largest_interval_size=largest_interval,
        hard_gate_passed=hard_gate_passed,
        ordering_fraction_in_band=ordering_ok,
        height_in_band=height_ok,
        width_in_band=width_ok,
        largest_interval_in_band=interval_ok,
        repaired_suite_passed=repaired_passed,
        reason=_sample_reason(
            hard_gate_passed=hard_gate_passed,
            ordering_ok=ordering_ok,
            height_ok=height_ok,
            width_ok=width_ok,
            interval_ok=interval_ok,
            classification=audit.classification,
        ),
    )


def _law_packets(
    *,
    reference_law_passed: bool,
    current_finite_colimits_passed: bool,
) -> tuple[LawPacket, ...]:
    return (
        LawPacket(
            packet_id="external_1p1_causal_diamond_reference_law",
            description=(
                "Predeclared random u,v light-cone coordinate law used as a "
                "calibration reference for the repaired finite suite."
            ),
            repaired_suite_passed=reference_law_passed,
            has_executed_samples=True,
            predeclared_generator=True,
            generator_source="external Lorentzian causal-diamond coordinates",
            descends_from_finality_colimit=False,
            imports_lorentzian_coordinates=True,
            conditions_on_repaired_suite_success=False,
            names_later_lorentzian_constraints=True,
            supplies_hostile_controls=True,
            no_overclaim_language=True,
        ),
        LawPacket(
            packet_id="current_t249_t252_finite_colimit_route",
            description=(
                "Current finite finality-colimit candidates after T525 repair."
            ),
            repaired_suite_passed=current_finite_colimits_passed,
            has_executed_samples=True,
            predeclared_generator=True,
            generator_source="current T249/T252 finite finality-colimit route",
            descends_from_finality_colimit=True,
            imports_lorentzian_coordinates=False,
            conditions_on_repaired_suite_success=False,
            names_later_lorentzian_constraints=True,
            supplies_hostile_controls=True,
            no_overclaim_language=True,
        ),
        LawPacket(
            packet_id="screen_conditioned_survivor_law",
            description=(
                "Declare the law to be 'whatever passes the repaired suite' and "
                "then count the survivor set as S1 progress."
            ),
            repaired_suite_passed=True,
            has_executed_samples=True,
            predeclared_generator=False,
            generator_source="post-hoc repaired-suite success predicate",
            descends_from_finality_colimit=False,
            imports_lorentzian_coordinates=False,
            conditions_on_repaired_suite_success=True,
            names_later_lorentzian_constraints=False,
            supplies_hostile_controls=False,
            no_overclaim_language=True,
        ),
        LawPacket(
            packet_id="lorentzian_import_promotion_shortcut",
            description=(
                "Use the external reference law's pass as a reason to promote "
                "S1 immediately."
            ),
            repaired_suite_passed=reference_law_passed,
            has_executed_samples=True,
            predeclared_generator=True,
            generator_source="external Lorentzian causal-diamond coordinates",
            descends_from_finality_colimit=False,
            imports_lorentzian_coordinates=True,
            conditions_on_repaired_suite_success=False,
            names_later_lorentzian_constraints=True,
            supplies_hostile_controls=True,
            no_overclaim_language=False,
            requests_s1_promotion=True,
            synthetic_control_only=True,
        ),
        LawPacket(
            packet_id="future_taf_native_generator_bridge_target",
            description=(
                "Synthetic future target: a predeclared generator descending "
                "from finality-domain data, not from u/v coordinates, with "
                "fixed repaired-suite and hostile controls."
            ),
            repaired_suite_passed=None,
            has_executed_samples=False,
            predeclared_generator=True,
            generator_source="future finality-domain colimit generator",
            descends_from_finality_colimit=True,
            imports_lorentzian_coordinates=False,
            conditions_on_repaired_suite_success=False,
            names_later_lorentzian_constraints=True,
            supplies_hostile_controls=True,
            no_overclaim_language=True,
            synthetic_control_only=True,
        ),
    )


def _evaluate_packet(packet: LawPacket) -> LawPacketDecision:
    missing = _missing_requirements(packet)
    if packet.requests_s1_promotion:
        classification = "blocked_s1_promotion_shortcut"
        admitted = False
        evidence = False
        reason = "Passing an imported reference law cannot promote S1."
    elif not packet.no_overclaim_language:
        classification = "blocked_spacetime_or_lorentzian_overclaim"
        admitted = False
        evidence = False
        reason = "The packet overclaims beyond finite repaired-suite calibration."
    elif packet.conditions_on_repaired_suite_success:
        classification = "rejected_screen_conditioned_generator"
        admitted = False
        evidence = False
        reason = "Conditioning the law on passing the diagnostic is circular."
    elif packet.repaired_suite_passed is False:
        classification = "rejected_repaired_suite_failure"
        admitted = False
        evidence = False
        reason = "The packet does not pass the repaired finite suite."
    elif packet.imports_lorentzian_coordinates and not packet.descends_from_finality_colimit:
        classification = "calibration_only_external_reference_law"
        admitted = False
        evidence = False
        reason = (
            "The law is a useful external calibration target, but it imports "
            "the target Lorentzian structure and supplies no TaF descent."
        )
    elif not packet.has_executed_samples and not missing:
        classification = "admitted_future_taf_native_generator_review_target"
        admitted = True
        evidence = False
        reason = (
            "This is the right future packet shape, but it has no executed law "
            "yet and therefore counts as no S1 evidence."
        )
    elif missing:
        classification = "rejected_missing_reference_law_requirements"
        admitted = False
        evidence = False
        reason = "The packet lacks one or more T526 source-law requirements."
    else:
        classification = "admitted_executed_taf_native_generator_review_target"
        admitted = True
        evidence = False
        reason = (
            "The packet would be admitted for S1 review only; promotion would "
            "require later embedding, locality, covariance, and continuum work."
        )

    return LawPacketDecision(
        packet_id=packet.packet_id,
        classification=classification,
        admitted_as_future_review_target=admitted,
        counts_as_s1_evidence=evidence,
        missing_requirements=missing,
        reason=reason,
    )


def _missing_requirements(packet: LawPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.predeclared_generator:
        missing.append("predeclared_generator")
    if packet.repaired_suite_passed is False:
        missing.append("repaired_suite_pass")
    if packet.conditions_on_repaired_suite_success:
        missing.append("not_conditioned_on_repaired_suite_success")
    if not packet.descends_from_finality_colimit:
        missing.append("finality_colimit_descent")
    if packet.imports_lorentzian_coordinates:
        missing.append("no_imported_lorentzian_coordinates")
    if not packet.names_later_lorentzian_constraints:
        missing.append("later_lorentzian_constraints_named")
    if not packet.supplies_hostile_controls:
        missing.append("hostile_controls")
    if not packet.no_overclaim_language:
        missing.append("no_overclaim_language")
    if packet.requests_s1_promotion:
        missing.append("no_s1_promotion_request")
    return tuple(missing)


def _sample_reason(
    *,
    hard_gate_passed: bool,
    ordering_ok: bool,
    height_ok: bool,
    width_ok: bool,
    interval_ok: bool,
    classification: str,
) -> str:
    if not hard_gate_passed:
        return f"hard T126 gate rejected: {classification}"
    failures: list[str] = []
    if not ordering_ok:
        failures.append("ordering_fraction_outside_t525_band")
    if not height_ok:
        failures.append("height_outside_t525_band")
    if not width_ok:
        failures.append("width_outside_t525_band")
    if not interval_ok:
        failures.append("largest_interval_outside_t525_band")
    if failures:
        return ", ".join(failures)
    if classification == "order_dimension_obstruction":
        return "order-dimension/profile-spread leg quarantined; T525 calibrated statistics pass"
    return "T525 hard gates and calibrated statistics pass"


def _diagnostics(audit: CausetAudit) -> CausetDiagnostics:
    if audit.diagnostics is None:
        raise RuntimeError(f"{audit.name} unexpectedly has no diagnostics")
    return audit.diagnostics


def _largest_interval_size(diagnostics: CausetDiagnostics) -> int:
    return max((size for size, count in diagnostics.interval_counts_by_size if count), default=0)


def _sample_to_dict(audit: ReferenceSampleAudit) -> dict[str, Any]:
    return {
        "law_id": audit.law_id,
        "event_count": audit.event_count,
        "seed": audit.seed,
        "t126_classification": audit.t126_classification,
        "order_dimension_quarantined": audit.order_dimension_quarantined,
        "ordering_fraction": _fraction_to_dict(audit.ordering_fraction),
        "height": audit.height,
        "width": audit.width,
        "largest_interval_size": audit.largest_interval_size,
        "hard_gate_passed": audit.hard_gate_passed,
        "ordering_fraction_in_band": audit.ordering_fraction_in_band,
        "height_in_band": audit.height_in_band,
        "width_in_band": audit.width_in_band,
        "largest_interval_in_band": audit.largest_interval_in_band,
        "repaired_suite_passed": audit.repaired_suite_passed,
        "reason": audit.reason,
    }


def _decision_to_dict(decision: LawPacketDecision) -> dict[str, Any]:
    return {
        "packet_id": decision.packet_id,
        "classification": decision.classification,
        "admitted_as_future_review_target": decision.admitted_as_future_review_target,
        "counts_as_s1_evidence": decision.counts_as_s1_evidence,
        "missing_requirements": list(decision.missing_requirements),
        "reason": decision.reason,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t526_result_to_dict(run_t526_analysis()), indent=2))
