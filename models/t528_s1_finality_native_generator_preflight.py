"""T528: S1 finality-native generator preflight.

T526 sharpened the S1 burden: the repaired S1 diagnostic suite is passable,
but the passing reference law imports Lorentzian light-cone coordinates. T528
tests the next smallest packet shape without upgrading S1: a predeclared
two-receipt record generator that creates finite causets from local receipt
orders rather than from target spacetime coordinates.

The result is intentionally pre-promotional. Passing the repaired finite suite
would only admit a packet for review; failing it rejects the packet. Neither
outcome counts as S1 evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import random
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    CausetAudit,
    CausetDiagnostics,
    FinalityColimitCausetDatum,
    hub_order_control,
    non_strict_relation,
    audit_finality_colimit_causet,
)
from models.t525_repaired_s1_manifoldlikeness_suite import (
    HARD_REJECTION_CLASSIFICATIONS,
    run_t525_analysis,
)


SAMPLE_SIZES = (8, 12, 16, 20)
SAMPLE_SEEDS = tuple(range(8))

VERDICT = "s1_finality_native_generator_preflight_rejects_first_packet"
NOT_CLAIMED = (
    "T528 does not derive spacetime, prove manifoldlikeness, establish a "
    "TaF-native sprinkling law, reconstruct a Lorentzian metric, prove an "
    "embedding or continuum theorem, reverse T223, or promote S1. It is a "
    "finite generator-preflight packet only."
)


@dataclass(frozen=True)
class GeneratedSampleAudit:
    packet_id: str
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
class SizePassSummary:
    event_count: int
    sample_count: int
    pass_count: int
    pass_rate: Fraction


@dataclass(frozen=True)
class HostileControlAudit:
    control_id: str
    event_count: int
    t126_classification: str
    repaired_suite_passed: bool
    reason: str


@dataclass(frozen=True)
class GeneratorPacket:
    packet_id: str
    description: str
    sample_count: int
    pass_count: int
    predeclared_generator: bool
    descends_from_finality_domain_data: bool
    imports_lorentzian_coordinates: bool
    conditions_on_repaired_suite_success: bool
    supplies_hostile_controls: bool
    hostile_controls_rejected: bool
    names_later_lorentzian_constraints: bool
    independent_naturality_justified: bool
    no_overclaim_language: bool
    requests_s1_promotion: bool = False
    synthetic_control_only: bool = False


@dataclass(frozen=True)
class PacketDecision:
    packet_id: str
    classification: str
    admitted_as_future_review_target: bool
    counts_as_s1_evidence: bool
    missing_requirements: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class T528Result:
    generator_id: str
    generator_basis: str
    sample_audits: tuple[GeneratedSampleAudit, ...]
    sample_count: int
    pass_count: int
    pass_rate: Fraction
    pass_summary_by_size: tuple[SizePassSummary, ...]
    hostile_control_audits: tuple[HostileControlAudit, ...]
    hostile_controls_rejected: bool
    packet_decisions: tuple[PacketDecision, ...]
    main_packet_classification: str
    main_packet_counts_as_s1_evidence: bool
    verdict: str
    strongest_reading: str
    improved: str
    missing_object: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    suggested_next: str
    not_claimed: str


def run_t528_analysis() -> T528Result:
    bands = {band.event_count: band for band in run_t525_analysis().calibration_bands}
    sample_audits = tuple(
        _audit_generated_sample(event_count=size, seed=seed, bands=bands)
        for size in SAMPLE_SIZES
        for seed in SAMPLE_SEEDS
    )
    pass_count = sum(audit.repaired_suite_passed for audit in sample_audits)
    sample_count = len(sample_audits)
    pass_rate = Fraction(pass_count, sample_count)
    pass_summary = tuple(_size_summary(size, sample_audits) for size in SAMPLE_SIZES)
    hostile_controls = tuple(_hostile_controls(bands))
    hostile_controls_rejected = all(
        not audit.repaired_suite_passed for audit in hostile_controls
    )
    packets = _packet_inputs(
        sample_count=sample_count,
        pass_count=pass_count,
        hostile_controls_rejected=hostile_controls_rejected,
    )
    decisions = tuple(_evaluate_packet(packet) for packet in packets)
    decisions_by_id = {decision.packet_id: decision for decision in decisions}
    main_decision = decisions_by_id["two_receipt_finality_generator"]

    verdict = (
        VERDICT
        if main_decision.classification == "rejected_repaired_suite_incomplete"
        and pass_count < sample_count
        and hostile_controls_rejected
        and not main_decision.counts_as_s1_evidence
        else "s1_finality_native_generator_preflight_unexpected_status"
    )

    return T528Result(
        generator_id="two_receipt_finality_generator",
        generator_basis=(
            "Generate record events with two independent local receipt orders. "
            "Declare x<y only when both receipt orders place x before y. The "
            "packet uses local receipt comparability, not imported Lorentzian "
            "light-cone coordinates, and is audited against the T525 repaired "
            "suite."
        ),
        sample_audits=sample_audits,
        sample_count=sample_count,
        pass_count=pass_count,
        pass_rate=pass_rate,
        pass_summary_by_size=pass_summary,
        hostile_control_audits=hostile_controls,
        hostile_controls_rejected=hostile_controls_rejected,
        packet_decisions=decisions,
        main_packet_classification=main_decision.classification,
        main_packet_counts_as_s1_evidence=main_decision.counts_as_s1_evidence,
        verdict=verdict,
        strongest_reading=(
            "The first TaF-native-looking two-receipt packet is not enough. It "
            "avoids explicit target-spacetime coordinates, but only 25 of 32 "
            "multi-size samples pass the repaired S1 suite, so it is rejected "
            "before S1 evidence or posture movement."
        ),
        improved=(
            "T528 converts T526's suggested next step into an executable intake "
            "screen. Future generator packets now need all repaired-suite "
            "samples to pass, independent naturality or neighbor-theory support, "
            "hostile controls, and no imported Lorentzian coordinate shortcut."
        ),
        missing_object=(
            "A predeclared finality-native generator, measure law, or continuum "
            "bridge whose samples pass the repaired suite across sizes, whose "
            "naturality is justified independently of the diagnostic, and whose "
            "later Lorentzian causal, metric, covariance, locality, and embedding "
            "constraints are named before promotion pressure."
        ),
        falsification_condition=(
            "T528 fails if the packet counts an incomplete repaired-suite pass as "
            "S1 evidence, admits a screen-conditioned generator, imports "
            "Lorentzian coordinates as the source law, or changes S1/claim/canon "
            "posture from a preflight result."
        ),
        s1_update=(
            "S1 remains `requires_added_assumption`. T528 rejects the first "
            "two-receipt finality-native generator packet as incomplete and "
            "therefore does not reverse T223 or promote S1."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T528 is a test-registry preflight "
            "only: no claim row, no S1 status movement, and no T223 reversal."
        ),
        suggested_next=(
            "Try a stronger predeclared generator or bridge with independent "
            "naturality support and all T525 repaired-suite samples passing, or "
            "route S1 effort to a separate formal entry point."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t528_result_to_dict(result: T528Result) -> dict[str, Any]:
    return {
        "generator_id": result.generator_id,
        "generator_basis": result.generator_basis,
        "sample_audits": [_sample_to_dict(audit) for audit in result.sample_audits],
        "sample_count": result.sample_count,
        "pass_count": result.pass_count,
        "pass_rate": _fraction_to_dict(result.pass_rate),
        "pass_summary_by_size": [
            _summary_to_dict(summary) for summary in result.pass_summary_by_size
        ],
        "hostile_control_audits": [
            _control_to_dict(audit) for audit in result.hostile_control_audits
        ],
        "hostile_controls_rejected": result.hostile_controls_rejected,
        "packet_decisions": [
            _decision_to_dict(decision) for decision in result.packet_decisions
        ],
        "main_packet_classification": result.main_packet_classification,
        "main_packet_counts_as_s1_evidence": result.main_packet_counts_as_s1_evidence,
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


def two_receipt_finality_datum(event_count: int, seed: int) -> FinalityColimitCausetDatum:
    rng = random.Random(seed)
    events = tuple(f"r{seed}_{index:02d}" for index in range(event_count))
    left_order = list(range(event_count))
    right_order = list(range(event_count))
    rng.shuffle(left_order)
    rng.shuffle(right_order)
    receipt_ranks = dict(zip(events, zip(left_order, right_order)))
    strict = {
        (left, right)
        for left in events
        for right in events
        if left != right
        and receipt_ranks[left][0] < receipt_ranks[right][0]
        and receipt_ranks[left][1] < receipt_ranks[right][1]
    }
    event_set = frozenset(events)
    return FinalityColimitCausetDatum(
        name=f"two_receipt_finality_generator_n{event_count}_seed{seed}",
        events=event_set,
        relation=non_strict_relation(event_set, frozenset(strict)),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="predeclared two-local-receipt finality generator",
    )


def _one_channel_chain_control(event_count: int = 8) -> FinalityColimitCausetDatum:
    events = tuple(f"c{index:02d}" for index in range(event_count))
    strict = {
        (left, right)
        for left_index, left in enumerate(events)
        for right_index, right in enumerate(events)
        if left_index < right_index
    }
    event_set = frozenset(events)
    return FinalityColimitCausetDatum(
        name="one_channel_chain_control",
        events=event_set,
        relation=non_strict_relation(event_set, frozenset(strict)),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="single receipt order hostile control",
    )


def _audit_generated_sample(
    *,
    event_count: int,
    seed: int,
    bands: dict[int, Any],
) -> GeneratedSampleAudit:
    audit = audit_finality_colimit_causet(two_receipt_finality_datum(event_count, seed))
    screen = _screen_against_band(audit, bands[event_count])
    return GeneratedSampleAudit(
        packet_id="two_receipt_finality_generator",
        event_count=event_count,
        seed=seed,
        **screen,
    )


def _hostile_controls(bands: dict[int, Any]) -> tuple[HostileControlAudit, ...]:
    controls = (
        _one_channel_chain_control(),
        hub_order_control(),
    )
    audits: list[HostileControlAudit] = []
    for datum in controls:
        audit = audit_finality_colimit_causet(datum)
        diagnostics = _diagnostics(audit)
        screen = _screen_against_band(audit, bands[diagnostics.event_count])
        audits.append(
            HostileControlAudit(
                control_id=datum.name,
                event_count=diagnostics.event_count,
                t126_classification=screen["t126_classification"],
                repaired_suite_passed=screen["repaired_suite_passed"],
                reason=screen["reason"],
            )
        )
    return tuple(audits)


def _screen_against_band(audit: CausetAudit, band: Any) -> dict[str, Any]:
    diagnostics = _diagnostics(audit)
    largest_interval = _largest_interval_size(diagnostics)
    hard_gate_passed = audit.classification not in HARD_REJECTION_CLASSIFICATIONS
    order_dimension_quarantined = audit.classification == "order_dimension_obstruction"
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
    return {
        "t126_classification": audit.classification,
        "order_dimension_quarantined": order_dimension_quarantined,
        "ordering_fraction": diagnostics.comparable_fraction,
        "height": diagnostics.height,
        "width": diagnostics.width,
        "largest_interval_size": largest_interval,
        "hard_gate_passed": hard_gate_passed,
        "ordering_fraction_in_band": ordering_ok,
        "height_in_band": height_ok,
        "width_in_band": width_ok,
        "largest_interval_in_band": interval_ok,
        "repaired_suite_passed": repaired_passed,
        "reason": _screen_reason(
            audit=audit,
            hard_gate_passed=hard_gate_passed,
            ordering_ok=ordering_ok,
            height_ok=height_ok,
            width_ok=width_ok,
            interval_ok=interval_ok,
            order_dimension_quarantined=order_dimension_quarantined,
        ),
    }


def _screen_reason(
    *,
    audit: CausetAudit,
    hard_gate_passed: bool,
    ordering_ok: bool,
    height_ok: bool,
    width_ok: bool,
    interval_ok: bool,
    order_dimension_quarantined: bool,
) -> str:
    if not hard_gate_passed:
        return f"hard T126 gate rejected: {audit.classification}"
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
        prefix = "order-dimension quarantined, but " if order_dimension_quarantined else ""
        return prefix + ", ".join(failures)
    if order_dimension_quarantined:
        return "order-dimension/profile-spread leg quarantined; T525 calibrated statistics pass"
    return "T525 hard gates and calibrated statistics pass"


def _size_summary(
    event_count: int,
    sample_audits: tuple[GeneratedSampleAudit, ...],
) -> SizePassSummary:
    subset = tuple(audit for audit in sample_audits if audit.event_count == event_count)
    pass_count = sum(audit.repaired_suite_passed for audit in subset)
    return SizePassSummary(
        event_count=event_count,
        sample_count=len(subset),
        pass_count=pass_count,
        pass_rate=Fraction(pass_count, len(subset)),
    )


def _packet_inputs(
    *,
    sample_count: int,
    pass_count: int,
    hostile_controls_rejected: bool,
) -> tuple[GeneratorPacket, ...]:
    return (
        GeneratorPacket(
            packet_id="two_receipt_finality_generator",
            description=(
                "Executed packet: two local receipt orders generate a finite "
                "causet by mutual-before comparability."
            ),
            sample_count=sample_count,
            pass_count=pass_count,
            predeclared_generator=True,
            descends_from_finality_domain_data=True,
            imports_lorentzian_coordinates=False,
            conditions_on_repaired_suite_success=False,
            supplies_hostile_controls=True,
            hostile_controls_rejected=hostile_controls_rejected,
            names_later_lorentzian_constraints=True,
            independent_naturality_justified=False,
            no_overclaim_language=True,
        ),
        GeneratorPacket(
            packet_id="screen_conditioned_survivor_law",
            description=(
                "Shortcut packet: define the source law as whichever samples "
                "pass the repaired suite."
            ),
            sample_count=0,
            pass_count=0,
            predeclared_generator=False,
            descends_from_finality_domain_data=False,
            imports_lorentzian_coordinates=False,
            conditions_on_repaired_suite_success=True,
            supplies_hostile_controls=False,
            hostile_controls_rejected=False,
            names_later_lorentzian_constraints=False,
            independent_naturality_justified=False,
            no_overclaim_language=True,
            synthetic_control_only=True,
        ),
        GeneratorPacket(
            packet_id="lorentzian_import_promotion_shortcut",
            description=(
                "Shortcut packet: import the T526 external reference law and "
                "treat its pass as an S1 promotion reason."
            ),
            sample_count=sample_count,
            pass_count=sample_count,
            predeclared_generator=True,
            descends_from_finality_domain_data=False,
            imports_lorentzian_coordinates=True,
            conditions_on_repaired_suite_success=False,
            supplies_hostile_controls=True,
            hostile_controls_rejected=True,
            names_later_lorentzian_constraints=True,
            independent_naturality_justified=False,
            no_overclaim_language=False,
            requests_s1_promotion=True,
            synthetic_control_only=True,
        ),
        GeneratorPacket(
            packet_id="future_full_burden_generator_packet",
            description=(
                "Synthetic future target with finality-native descent, hostile "
                "controls, independent naturality, and later Lorentzian burdens "
                "declared before execution."
            ),
            sample_count=0,
            pass_count=0,
            predeclared_generator=True,
            descends_from_finality_domain_data=True,
            imports_lorentzian_coordinates=False,
            conditions_on_repaired_suite_success=False,
            supplies_hostile_controls=True,
            hostile_controls_rejected=True,
            names_later_lorentzian_constraints=True,
            independent_naturality_justified=True,
            no_overclaim_language=True,
            synthetic_control_only=True,
        ),
    )


def _evaluate_packet(packet: GeneratorPacket) -> PacketDecision:
    missing = _missing_requirements(packet)
    if packet.requests_s1_promotion:
        classification = "blocked_s1_promotion_shortcut"
        admitted = False
        reason = "A preflight or imported reference law cannot promote S1."
    elif packet.conditions_on_repaired_suite_success:
        classification = "rejected_screen_conditioned_generator"
        admitted = False
        reason = "Conditioning the law on diagnostic success is circular."
    elif packet.imports_lorentzian_coordinates:
        classification = "rejected_lorentzian_coordinate_import"
        admitted = False
        reason = "The packet imports the target spacetime structure."
    elif packet.sample_count == 0 and not missing:
        classification = "admitted_future_full_burden_review_target"
        admitted = True
        reason = "The shape is admissible for future review, but no samples exist yet."
    elif packet.pass_count < packet.sample_count:
        classification = "rejected_repaired_suite_incomplete"
        admitted = False
        reason = "Not all executed samples pass the repaired S1 suite."
    elif missing:
        classification = "rejected_missing_generator_requirements"
        admitted = False
        reason = "The packet lacks one or more T528 generator requirements."
    else:
        classification = "admitted_executed_review_target"
        admitted = True
        reason = (
            "The packet would be review-only; later Lorentzian and continuum "
            "burdens would still remain before any S1 movement."
        )

    return PacketDecision(
        packet_id=packet.packet_id,
        classification=classification,
        admitted_as_future_review_target=admitted,
        counts_as_s1_evidence=False,
        missing_requirements=missing,
        reason=reason,
    )


def _missing_requirements(packet: GeneratorPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.predeclared_generator:
        missing.append("predeclared_generator")
    if packet.sample_count > 0 and packet.pass_count < packet.sample_count:
        missing.append("repaired_suite_all_samples_pass")
    if not packet.descends_from_finality_domain_data:
        missing.append("finality_domain_descent")
    if packet.imports_lorentzian_coordinates:
        missing.append("no_imported_lorentzian_coordinates")
    if packet.conditions_on_repaired_suite_success:
        missing.append("not_conditioned_on_repaired_suite_success")
    if not packet.supplies_hostile_controls:
        missing.append("hostile_controls")
    if packet.supplies_hostile_controls and not packet.hostile_controls_rejected:
        missing.append("hostile_controls_rejected")
    if not packet.names_later_lorentzian_constraints:
        missing.append("later_lorentzian_constraints_named")
    if not packet.independent_naturality_justified:
        missing.append("independent_naturality_or_neighbor_theory")
    if not packet.no_overclaim_language:
        missing.append("no_overclaim_language")
    if packet.requests_s1_promotion:
        missing.append("no_s1_promotion_request")
    return tuple(missing)


def _diagnostics(audit: CausetAudit) -> CausetDiagnostics:
    if audit.diagnostics is None:
        raise RuntimeError(f"{audit.name} unexpectedly has no diagnostics")
    return audit.diagnostics


def _largest_interval_size(diagnostics: CausetDiagnostics) -> int:
    return max((size for size, count in diagnostics.interval_counts_by_size if count), default=0)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


def _sample_to_dict(audit: GeneratedSampleAudit) -> dict[str, Any]:
    return {
        "packet_id": audit.packet_id,
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


def _summary_to_dict(summary: SizePassSummary) -> dict[str, Any]:
    return {
        "event_count": summary.event_count,
        "sample_count": summary.sample_count,
        "pass_count": summary.pass_count,
        "pass_rate": _fraction_to_dict(summary.pass_rate),
    }


def _control_to_dict(audit: HostileControlAudit) -> dict[str, Any]:
    return {
        "control_id": audit.control_id,
        "event_count": audit.event_count,
        "t126_classification": audit.t126_classification,
        "repaired_suite_passed": audit.repaired_suite_passed,
        "reason": audit.reason,
    }


def _decision_to_dict(decision: PacketDecision) -> dict[str, Any]:
    return {
        "packet_id": decision.packet_id,
        "classification": decision.classification,
        "admitted_as_future_review_target": decision.admitted_as_future_review_target,
        "counts_as_s1_evidence": decision.counts_as_s1_evidence,
        "missing_requirements": list(decision.missing_requirements),
        "reason": decision.reason,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t528_result_to_dict(run_t528_analysis()), indent=2))
