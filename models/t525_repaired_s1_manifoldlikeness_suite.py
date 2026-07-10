"""T525: repaired S1 manifoldlikeness diagnostic suite.

T524 showed that T126's `order_dimension_obstruction` rejects genuine random
1+1 sprinkles as their finite interval profiles fluctuate. T525 therefore
quarantines that profile-spread leg and replaces it, for finite audit purposes,
with simple statistics calibrated on seeded random 1+1 light-cone sprinkles:

* ordering fraction;
* height and width;
* largest Alexandrov interval interior size.

This is still only a finite diagnostic suite. It does not prove embedding,
dimension, locality, covariance, metric reconstruction, or a continuum limit.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    CausetAudit,
    CausetDiagnostics,
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    complete_bipartite_layer_control,
    degenerate_chain_control,
    grid_filter_pass_control,
    hub_order_control,
)
from models.t249_larger_t54_t126_colimit import run_t249_analysis
from models.t252_t255_nine_event_ordinal_controls import run_t252_analysis
from models.t524_t126_random_sprinkle_diagnostic_repair import (
    DEFAULT_SEEDS,
    random_lightcone_sprinkle_datum,
)


RANDOM_CONTROL_SIZES = (8, 12, 16, 20)
RANDOM_REPRESENTATIVE_SEED = 0

HARD_REJECTION_CLASSIFICATIONS = frozenset(
    {
        "not_descent_datum",
        "noncanonical_colimit",
        "not_poset",
        "phantom_gap_unresolved",
        "insufficient_scale",
        "hub_nonlocality_obstruction",
        "rank_width_obstruction",
        "interval_profile_obstruction",
    }
)

VERDICT_NO_SURVIVOR = "repaired_s1_suite_no_current_finite_colimit_survivor"
NOT_CLAIMED = (
    "T525 does not derive spacetime, prove manifoldlikeness, estimate continuum "
    "dimension, establish a random-sprinkling law, reconstruct a Lorentzian "
    "metric, prove locality/covariance, derive GR/QFT, or promote S1. It is a "
    "finite repaired diagnostic suite calibrated on seeded controls."
)


@dataclass(frozen=True)
class CalibrationBand:
    event_count: int
    sample_count: int
    ordering_fraction_min: Fraction
    ordering_fraction_max: Fraction
    height_min: int
    height_max: int
    width_min: int
    width_max: int
    largest_interval_min: int
    largest_interval_max: int
    order_dimension_obstruction_count: int


@dataclass(frozen=True)
class CandidateInput:
    name: str
    group: str
    audit: CausetAudit


@dataclass(frozen=True)
class RepairedCandidateAudit:
    name: str
    group: str
    event_count: int
    original_t126_classification: str
    original_t126_filter_passed: bool
    order_dimension_quarantined: bool
    hard_gate_passed: bool
    ordering_fraction: Fraction
    height: int
    width: int
    largest_interval_size: int
    ordering_fraction_in_band: bool
    height_in_band: bool
    width_in_band: bool
    largest_interval_in_band: bool
    repaired_filter_passed: bool
    verdict: str
    reason: str


@dataclass(frozen=True)
class T525Result:
    comparison_target: str
    target_basis: str
    calibration_bands: tuple[CalibrationBand, ...]
    candidate_audits: tuple[RepairedCandidateAudit, ...]
    random_controls_pass_repaired_suite: bool
    hard_negative_controls_rejected: bool
    current_finite_colimit_survivor_count: int
    current_finite_colimits_survive_repaired_suite: bool
    t249_grid_rejected_by_repaired_suite: bool
    t252_ordinal_rejected_by_repaired_suite: bool
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_rescoped: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


def run_t525_analysis() -> T525Result:
    candidates = _candidate_inputs()
    calibration_sizes = tuple(
        sorted(
            set(RANDOM_CONTROL_SIZES)
            | {
                _diagnostics(candidate.audit).event_count
                for candidate in candidates
            }
        )
    )
    calibration_map = {
        size: _calibration_band(size)
        for size in calibration_sizes
    }
    audited = tuple(
        _audit_candidate(candidate, calibration_map[_diagnostics(candidate.audit).event_count])
        for candidate in candidates
    )

    random_controls_pass = all(
        audit.repaired_filter_passed
        for audit in audited
        if audit.group == "random_sprinkle_control"
    )
    hard_controls_rejected = all(
        not audit.repaired_filter_passed
        for audit in audited
        if audit.group == "hard_negative_control"
    )
    finite_colimit_audits = tuple(
        audit for audit in audited if audit.group == "current_finite_colimit"
    )
    finite_colimit_survivor_count = sum(
        audit.repaired_filter_passed for audit in finite_colimit_audits
    )
    finite_colimits_survive = finite_colimit_survivor_count > 0
    by_name = {audit.name: audit for audit in audited}
    t249_rejected = not by_name["t249_grid_colimit"].repaired_filter_passed
    t252_rejected = not by_name["t252_ordinal_band_control"].repaired_filter_passed
    verdict = (
        VERDICT_NO_SURVIVOR
        if random_controls_pass
        and hard_controls_rejected
        and not finite_colimits_survive
        and t249_rejected
        and t252_rejected
        else "repaired_s1_suite_mixed_or_unexpected_status"
    )

    return T525Result(
        comparison_target="seeded_1p1_sprinkle_calibrated_repaired_s1_suite",
        target_basis=(
            "The suite treats seeded random 1+1 light-cone sprinkles as finite "
            "calibration controls at each event count. It keeps T126's hard "
            "causal-set gates, quarantines profile-spread/order-dimension as "
            "finite regularity, and asks whether candidate diagnostics fall "
            "inside the observed random-control envelope."
        ),
        calibration_bands=tuple(calibration_map[size] for size in calibration_sizes),
        candidate_audits=audited,
        random_controls_pass_repaired_suite=random_controls_pass,
        hard_negative_controls_rejected=hard_controls_rejected,
        current_finite_colimit_survivor_count=finite_colimit_survivor_count,
        current_finite_colimits_survive_repaired_suite=finite_colimits_survive,
        t249_grid_rejected_by_repaired_suite=t249_rejected,
        t252_ordinal_rejected_by_repaired_suite=t252_rejected,
        verdict=verdict,
        strongest_claim=(
            "A repaired finite S1 suite can pass true random 1+1 controls while "
            "rejecting the current finite colimit witnesses. T249's grid is "
            "outside the calibrated interval-abundance envelope, and T252's "
            "selected ordinal witness is outside the calibrated width envelope."
        ),
        improved=(
            "T525 removes the known T126 profile-spread artifact from the wall "
            "set and replaces it with explicit random-control calibration. This "
            "keeps the S1 closure honest: current witnesses still fail, but not "
            "because genuine random sprinkles are punished for fluctuating."
        ),
        weakened_or_rescoped=(
            "This rescopes T223/T126 language away from the bad "
            "`order_dimension_obstruction` leg while preserving the practical "
            "S1 conclusion: no current finite finality colimit survives a "
            "repaired finite manifoldlikeness screen."
        ),
        falsification_condition=(
            "T525 fails if seeded random controls do not pass the repaired "
            "suite, if hard negative controls pass, if the T249/T252 verdicts "
            "are not computed against event-count-matched calibration bands, or "
            "if the finite repaired screen is promoted into a continuum theorem."
        ),
        s1_update=(
            "S1 remains `requires_added_assumption`. T525 strengthens the "
            "diagnostic basis for that status after T524: the known bad leg is "
            "quarantined, but no current finite colimit survives the repaired "
            "suite. The live paths remain an independent measure law, a "
            "separate formal entry point, or a continuum/embedding bridge."
        ),
        claim_ledger_update=(
            "Record T525 as S1 claim-history only: repaired finite diagnostic "
            "suite, no current finite colimit survivor, no S1 promotion, and no "
            "T223 reversal. Add T525 to the S1 test list and sync the S1 claim file."
        ),
        open_blocker=(
            "No finality-native measure, locality law, abundance theorem, "
            "embedding theorem, covariance result, Lorentzian metric "
            "reconstruction, or continuum bridge selects a repaired-suite "
            "survivor."
        ),
        suggested_next=(
            "Either build an independent generative measure that produces "
            "repaired-suite survivors without tail tuning, or leave the finite "
            "S1 colimit route closed and move to a separate formal entry point."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t525_result_to_dict(result: T525Result) -> dict[str, Any]:
    return {
        "comparison_target": result.comparison_target,
        "target_basis": result.target_basis,
        "calibration_bands": [_band_to_dict(band) for band in result.calibration_bands],
        "candidate_audits": [_candidate_to_dict(audit) for audit in result.candidate_audits],
        "random_controls_pass_repaired_suite": result.random_controls_pass_repaired_suite,
        "hard_negative_controls_rejected": result.hard_negative_controls_rejected,
        "current_finite_colimit_survivor_count": result.current_finite_colimit_survivor_count,
        "current_finite_colimits_survive_repaired_suite": (
            result.current_finite_colimits_survive_repaired_suite
        ),
        "t249_grid_rejected_by_repaired_suite": result.t249_grid_rejected_by_repaired_suite,
        "t252_ordinal_rejected_by_repaired_suite": (
            result.t252_ordinal_rejected_by_repaired_suite
        ),
        "verdict": result.verdict,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_rescoped": result.weakened_or_rescoped,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _candidate_inputs() -> tuple[CandidateInput, ...]:
    random_controls = tuple(
        CandidateInput(
            name=f"random_1p1_sprinkle_n{size}_seed{RANDOM_REPRESENTATIVE_SEED}",
            group="random_sprinkle_control",
            audit=audit_finality_colimit_causet(
                random_lightcone_sprinkle_datum(size, RANDOM_REPRESENTATIVE_SEED)
            ),
        )
        for size in RANDOM_CONTROL_SIZES
    )

    t249 = run_t249_analysis()
    t252 = run_t252_analysis()
    finite_colimits = (
        CandidateInput("t249_grid_colimit", "current_finite_colimit", t249.t126_audit),
        CandidateInput("t252_ordinal_band_control", "current_finite_colimit", t252.t126_audit),
    )

    hard_controls: list[CandidateInput] = []
    for datum in (
        hub_order_control(),
        complete_bipartite_layer_control(),
        degenerate_chain_control(),
        grid_filter_pass_control(),
    ):
        group = (
            "current_finite_colimit"
            if datum.name == "grid_filter_pass_control"
            else "hard_negative_control"
        )
        name = (
            "synthetic_3x3_grid_control"
            if datum.name == "grid_filter_pass_control"
            else datum.name
        )
        hard_controls.append(
            CandidateInput(
                name=name,
                group=group,
                audit=audit_finality_colimit_causet(datum),
            )
        )

    return random_controls + finite_colimits + tuple(hard_controls)


def _calibration_band(event_count: int) -> CalibrationBand:
    audits = tuple(
        audit_finality_colimit_causet(random_lightcone_sprinkle_datum(event_count, seed))
        for seed in DEFAULT_SEEDS
    )
    diagnostics = tuple(_diagnostics(audit) for audit in audits)
    largest_intervals = tuple(_largest_interval_size(d) for d in diagnostics)
    classification_counts = Counter(audit.classification for audit in audits)
    return CalibrationBand(
        event_count=event_count,
        sample_count=len(audits),
        ordering_fraction_min=min(d.comparable_fraction for d in diagnostics),
        ordering_fraction_max=max(d.comparable_fraction for d in diagnostics),
        height_min=min(d.height for d in diagnostics),
        height_max=max(d.height for d in diagnostics),
        width_min=min(d.width for d in diagnostics),
        width_max=max(d.width for d in diagnostics),
        largest_interval_min=min(largest_intervals),
        largest_interval_max=max(largest_intervals),
        order_dimension_obstruction_count=classification_counts[
            "order_dimension_obstruction"
        ],
    )


def _audit_candidate(
    candidate: CandidateInput,
    band: CalibrationBand,
) -> RepairedCandidateAudit:
    audit = candidate.audit
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
        hard_gate_passed
        and ordering_ok
        and height_ok
        and width_ok
        and interval_ok
    )
    verdict = "passes_repaired_suite" if repaired_passed else "fails_repaired_suite"
    reason = _candidate_reason(
        audit=audit,
        hard_gate_passed=hard_gate_passed,
        ordering_ok=ordering_ok,
        height_ok=height_ok,
        width_ok=width_ok,
        interval_ok=interval_ok,
        order_dimension_quarantined=order_dimension_quarantined,
    )
    return RepairedCandidateAudit(
        name=candidate.name,
        group=candidate.group,
        event_count=diagnostics.event_count,
        original_t126_classification=audit.classification,
        original_t126_filter_passed=audit.manifold_filter_passed,
        order_dimension_quarantined=order_dimension_quarantined,
        hard_gate_passed=hard_gate_passed,
        ordering_fraction=diagnostics.comparable_fraction,
        height=diagnostics.height,
        width=diagnostics.width,
        largest_interval_size=largest_interval,
        ordering_fraction_in_band=ordering_ok,
        height_in_band=height_ok,
        width_in_band=width_ok,
        largest_interval_in_band=interval_ok,
        repaired_filter_passed=repaired_passed,
        verdict=verdict,
        reason=reason,
    )


def _candidate_reason(
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
        failures.append("ordering_fraction_outside_random_band")
    if not height_ok:
        failures.append("height_outside_random_band")
    if not width_ok:
        failures.append("width_outside_random_band")
    if not interval_ok:
        failures.append("largest_interval_outside_random_band")
    if failures:
        prefix = (
            "profile-spread was quarantined, but "
            if order_dimension_quarantined
            else ""
        )
        return prefix + ", ".join(failures)
    if order_dimension_quarantined:
        return "profile-spread/order-dimension leg quarantined; calibrated statistics pass"
    return "hard gates and calibrated statistics pass"


def _diagnostics(audit: CausetAudit) -> CausetDiagnostics:
    if audit.diagnostics is None:
        raise RuntimeError(f"{audit.name} unexpectedly has no diagnostics")
    return audit.diagnostics


def _largest_interval_size(diagnostics: CausetDiagnostics) -> int:
    return max((size for size, count in diagnostics.interval_counts_by_size if count), default=0)


def _band_to_dict(band: CalibrationBand) -> dict[str, Any]:
    return {
        "event_count": band.event_count,
        "sample_count": band.sample_count,
        "ordering_fraction_min": _fraction_to_dict(band.ordering_fraction_min),
        "ordering_fraction_max": _fraction_to_dict(band.ordering_fraction_max),
        "height_min": band.height_min,
        "height_max": band.height_max,
        "width_min": band.width_min,
        "width_max": band.width_max,
        "largest_interval_min": band.largest_interval_min,
        "largest_interval_max": band.largest_interval_max,
        "order_dimension_obstruction_count": band.order_dimension_obstruction_count,
    }


def _candidate_to_dict(audit: RepairedCandidateAudit) -> dict[str, Any]:
    return {
        "name": audit.name,
        "group": audit.group,
        "event_count": audit.event_count,
        "original_t126_classification": audit.original_t126_classification,
        "original_t126_filter_passed": audit.original_t126_filter_passed,
        "order_dimension_quarantined": audit.order_dimension_quarantined,
        "hard_gate_passed": audit.hard_gate_passed,
        "ordering_fraction": _fraction_to_dict(audit.ordering_fraction),
        "height": audit.height,
        "width": audit.width,
        "largest_interval_size": audit.largest_interval_size,
        "ordering_fraction_in_band": audit.ordering_fraction_in_band,
        "height_in_band": audit.height_in_band,
        "width_in_band": audit.width_in_band,
        "largest_interval_in_band": audit.largest_interval_in_band,
        "repaired_filter_passed": audit.repaired_filter_passed,
        "verdict": audit.verdict,
        "reason": audit.reason,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t525_result_to_dict(run_t525_analysis()), indent=2))
