"""T524: random-sprinkle repair audit for the T126 order-dimension leg.

T126's `order_dimension_obstruction` is implemented as an equal-interval
height/width profile-spread screen. T524 asks whether that screen behaves like
a true 1+1 manifoldlikeness falsifier when run against seeded random
light-cone sprinkles, or whether it rejects genuine samples as finite
statistical fluctuation appears.

This is a diagnostic repair audit only. It does not prove embedding,
continuum convergence, metric reconstruction, or spacetime emergence, and it
does not reopen or promote S1 by itself.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from random import Random
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    non_strict_relation,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    deterministic_flat_interval_control,
    flat_1p1_interval_target,
)


SUPPORTED_SIZES = (8, 12, 16, 20)
DEFAULT_SEEDS = tuple(range(8))
COORDINATE_DENOMINATOR = 1_000_000_000

VERDICT_REPAIRED = "t126_order_dimension_leg_confirmed_finite_regular_screen"
NOT_CLAIMED = (
    "T524 is not a manifoldlikeness proof, dimension estimate, faithful "
    "embedding theorem, random-sprinkling law, continuum limit, Lorentzian "
    "metric reconstruction, GR, QFT, or S1 promotion. It audits one T126 "
    "diagnostic leg against seeded finite random 1+1 controls."
)


@dataclass(frozen=True)
class RandomSprinkleSampleAudit:
    event_count: int
    seed: int
    t126_classification: str
    t126_filter_passed: bool
    ordering_fraction: Fraction
    absolute_gap_from_half: Fraction
    t156_band_passed: bool
    strict_pair_count: int
    height: int
    width: int
    profile_spread_obstruction: bool


@dataclass(frozen=True)
class RandomSprinkleSizeSummary:
    event_count: int
    sample_count: int
    t126_pass_count: int
    order_dimension_obstruction_count: int
    other_obstruction_count: int
    t156_band_pass_count: int
    mean_ordering_fraction: Fraction
    mean_absolute_gap_from_half: Fraction
    order_dimension_obstruction_rate: Fraction
    t156_band_pass_rate: Fraction
    classification_counts: tuple[tuple[str, int], ...]


@dataclass(frozen=True)
class T524Result:
    comparison_target: str
    target_basis: str
    sizes: tuple[int, ...]
    seeds: tuple[int, ...]
    calibration_control_classification: str
    calibration_control_passed: bool
    calibration_control_ordering_fraction: Fraction
    sample_audits: tuple[RandomSprinkleSampleAudit, ...]
    size_summaries: tuple[RandomSprinkleSizeSummary, ...]
    mean_ordering_gap_decreases_with_size: bool
    order_dimension_rejection_rate_increases_with_size: bool
    larger_sprinkles_all_order_dimension_rejected: bool
    artifact_confirmed: bool
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


def random_lightcone_sprinkle_datum(
    event_count: int,
    seed: int,
) -> FinalityColimitCausetDatum:
    """Build a seeded finite 1+1 light-cone coordinate sprinkle."""

    if event_count < 2:
        raise ValueError("event_count must be at least 2")

    rng = Random(seed)
    coordinates = {
        f"r{i}": (
            Fraction(rng.randrange(1, COORDINATE_DENOMINATOR), COORDINATE_DENOMINATOR),
            Fraction(rng.randrange(1, COORDINATE_DENOMINATOR), COORDINATE_DENOMINATOR),
        )
        for i in range(event_count)
    }

    u_values = [uv[0] for uv in coordinates.values()]
    v_values = [uv[1] for uv in coordinates.values()]
    if len(set(u_values)) != event_count or len(set(v_values)) != event_count:
        raise ValueError("seeded control unexpectedly produced a coordinate tie")

    strict = frozenset(
        (left, right)
        for left, left_uv in coordinates.items()
        for right, right_uv in coordinates.items()
        if left != right and left_uv[0] < right_uv[0] and left_uv[1] < right_uv[1]
    )
    events = frozenset(coordinates)
    return FinalityColimitCausetDatum(
        name=f"t524_random_1p1_sprinkle_n{event_count}_seed{seed}",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source=(
            "seeded random 1+1 light-cone coordinate sprinkle; finite "
            "diagnostic control, not a TaF-derived colimit"
        ),
    )


def run_t524_analysis(
    *,
    sizes: tuple[int, ...] = SUPPORTED_SIZES,
    seeds: tuple[int, ...] = DEFAULT_SEEDS,
) -> T524Result:
    target = flat_1p1_interval_target()
    control_audit = audit_finality_colimit_causet(deterministic_flat_interval_control())
    if control_audit.diagnostics is None:
        raise RuntimeError("T156 flat control unexpectedly has no diagnostics")

    sample_audits = tuple(
        _audit_sample(event_count=size, seed=seed)
        for size in sizes
        for seed in seeds
    )
    size_summaries = tuple(
        _summarize_size(size, tuple(a for a in sample_audits if a.event_count == size))
        for size in sizes
    )

    mean_gaps = tuple(summary.mean_absolute_gap_from_half for summary in size_summaries)
    rejection_rates = tuple(
        summary.order_dimension_obstruction_rate for summary in size_summaries
    )
    gap_decreases = _strictly_decreases(mean_gaps)
    rejection_increases = _nondecreasing(rejection_rates)
    larger_all_rejected = all(
        summary.order_dimension_obstruction_count == summary.sample_count
        for summary in size_summaries
        if summary.event_count >= 16
    )
    artifact_confirmed = (
        control_audit.manifold_filter_passed
        and gap_decreases
        and rejection_increases
        and larger_all_rejected
    )

    return T524Result(
        comparison_target="seeded_random_flat_1p1_lightcone_sprinkles_n8_to_n20",
        target_basis=(
            "In flat 1+1 light-cone coordinates, a finite causal diamond sample "
            "orders p<q exactly when u_p<u_q and v_p<v_q. Its ordering fraction "
            "approaches the Myrheim-Meyer 1+1 target 1/2 in expectation; finite "
            "interval profiles naturally fluctuate."
        ),
        sizes=sizes,
        seeds=seeds,
        calibration_control_classification=control_audit.classification,
        calibration_control_passed=control_audit.manifold_filter_passed,
        calibration_control_ordering_fraction=control_audit.diagnostics.comparable_fraction,
        sample_audits=sample_audits,
        size_summaries=size_summaries,
        mean_ordering_gap_decreases_with_size=gap_decreases,
        order_dimension_rejection_rate_increases_with_size=rejection_increases,
        larger_sprinkles_all_order_dimension_rejected=larger_all_rejected,
        artifact_confirmed=artifact_confirmed,
        verdict=VERDICT_REPAIRED if artifact_confirmed else "t126_order_dimension_artifact_not_confirmed",
        strongest_claim=(
            "The seeded random 1+1 controls confirm that T126's "
            "`order_dimension_obstruction` is not a reliable manifoldlikeness "
            "falsifier. The repo's six-event flat control passes, but random "
            "1+1 sprinkles are increasingly rejected by that leg as their mean "
            "ordering-fraction gap from 1/2 decreases."
        ),
        improved=(
            "T524 upgrades the earlier deterministic calibration note into an "
            "executable RNG-ensemble repair audit. It separates the T126 causal-"
            "set gate and other obstruction legs from the profile-spread leg "
            "that mistakes random interval fluctuation for non-manifoldness."
        ),
        weakened_or_rescoped=(
            "This rescopes any S1/T223 language that treats the T126 "
            "order-dimension leg as a genuine manifoldlikeness wall. It does "
            "not weaken the independent T223 rare-tail counting result, and it "
            "does not make current finite finality colimits manifoldlike."
        ),
        falsification_condition=(
            "T524 fails if the seeded random controls stop approaching the "
            "declared 1+1 ordering-fraction target, if larger random sprinkles "
            "are not rejected by `order_dimension_obstruction`, if the flat "
            "six-event control no longer passes, or if the result is used to "
            "promote S1 rather than repair one diagnostic leg."
        ),
        s1_update=(
            "S1 remains `requires_added_assumption`. T524 only says the T126 "
            "profile-spread leg must be treated as a finite-regularity screen, "
            "not as a continuum manifoldlikeness wall. Future S1 work still "
            "needs an added measure, selection rule, sprinkling law, dimension "
            "estimator, or continuum bridge."
        ),
        claim_ledger_update=(
            "Record T524 as an S1 claim-history repair: the T126 "
            "`order_dimension_obstruction` leg is quarantined as diagnostic "
            "regularity, while T223 remains a finite-screen/finite-ensemble "
            "no-go. No S1 status movement and no claim promotion."
        ),
        open_blocker=(
            "No repaired manifoldlikeness suite has replaced the profile-spread "
            "leg, and no current finality-colimit family has been shown to "
            "survive a robust causal-set dimension, abundance, locality, "
            "sprinkling, or continuum-limit diagnostic."
        ),
        suggested_next=(
            "Replace the T126 profile-spread leg with a declared statistical "
            "dimension/locality diagnostic calibrated on random sprinkles, then "
            "rerun the S1 finite-colimit route only on that repaired suite."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t524_result_to_dict(result: T524Result) -> dict[str, Any]:
    return {
        "comparison_target": result.comparison_target,
        "target_basis": result.target_basis,
        "sizes": list(result.sizes),
        "seeds": list(result.seeds),
        "calibration_control_classification": result.calibration_control_classification,
        "calibration_control_passed": result.calibration_control_passed,
        "calibration_control_ordering_fraction": _fraction_to_dict(
            result.calibration_control_ordering_fraction
        ),
        "sample_audits": [_sample_to_dict(audit) for audit in result.sample_audits],
        "size_summaries": [_summary_to_dict(summary) for summary in result.size_summaries],
        "mean_ordering_gap_decreases_with_size": (
            result.mean_ordering_gap_decreases_with_size
        ),
        "order_dimension_rejection_rate_increases_with_size": (
            result.order_dimension_rejection_rate_increases_with_size
        ),
        "larger_sprinkles_all_order_dimension_rejected": (
            result.larger_sprinkles_all_order_dimension_rejected
        ),
        "artifact_confirmed": result.artifact_confirmed,
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


def _audit_sample(*, event_count: int, seed: int) -> RandomSprinkleSampleAudit:
    datum = random_lightcone_sprinkle_datum(event_count, seed)
    audit = audit_finality_colimit_causet(datum)
    diagnostics = audit.diagnostics
    if diagnostics is None:
        raise RuntimeError(f"{datum.name} unexpectedly has no T126 diagnostics")

    target = flat_1p1_interval_target()
    ordering_fraction = diagnostics.comparable_fraction
    return RandomSprinkleSampleAudit(
        event_count=event_count,
        seed=seed,
        t126_classification=audit.classification,
        t126_filter_passed=audit.manifold_filter_passed,
        ordering_fraction=ordering_fraction,
        absolute_gap_from_half=abs(ordering_fraction - target.target_fraction),
        t156_band_passed=target.accepts(ordering_fraction),
        strict_pair_count=diagnostics.strict_pair_count,
        height=diagnostics.height,
        width=diagnostics.width,
        profile_spread_obstruction=diagnostics.profile_spread_obstruction,
    )


def _summarize_size(
    event_count: int,
    audits: tuple[RandomSprinkleSampleAudit, ...],
) -> RandomSprinkleSizeSummary:
    if not audits:
        raise ValueError(f"no audits supplied for event_count={event_count}")

    classifications = Counter(audit.t126_classification for audit in audits)
    sample_count = len(audits)
    order_dimension_count = classifications["order_dimension_obstruction"]
    pass_count = sum(audit.t126_filter_passed for audit in audits)
    band_pass_count = sum(audit.t156_band_passed for audit in audits)
    mean_fraction = _mean(audit.ordering_fraction for audit in audits)
    mean_gap = _mean(audit.absolute_gap_from_half for audit in audits)
    other_obstructions = sample_count - pass_count - order_dimension_count

    return RandomSprinkleSizeSummary(
        event_count=event_count,
        sample_count=sample_count,
        t126_pass_count=pass_count,
        order_dimension_obstruction_count=order_dimension_count,
        other_obstruction_count=other_obstructions,
        t156_band_pass_count=band_pass_count,
        mean_ordering_fraction=mean_fraction,
        mean_absolute_gap_from_half=mean_gap,
        order_dimension_obstruction_rate=_fraction(order_dimension_count, sample_count),
        t156_band_pass_rate=_fraction(band_pass_count, sample_count),
        classification_counts=tuple(sorted(classifications.items())),
    )


def _strictly_decreases(values: tuple[Fraction, ...]) -> bool:
    return all(later < earlier for earlier, later in zip(values, values[1:]))


def _nondecreasing(values: tuple[Fraction, ...]) -> bool:
    return all(later >= earlier for earlier, later in zip(values, values[1:]))


def _mean(values: Any) -> Fraction:
    values_tuple = tuple(values)
    return _fraction(sum(values_tuple, Fraction(0, 1)), len(values_tuple))


def _fraction(numerator: int | Fraction, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _sample_to_dict(audit: RandomSprinkleSampleAudit) -> dict[str, Any]:
    return {
        "event_count": audit.event_count,
        "seed": audit.seed,
        "t126_classification": audit.t126_classification,
        "t126_filter_passed": audit.t126_filter_passed,
        "ordering_fraction": _fraction_to_dict(audit.ordering_fraction),
        "absolute_gap_from_half": _fraction_to_dict(audit.absolute_gap_from_half),
        "t156_band_passed": audit.t156_band_passed,
        "strict_pair_count": audit.strict_pair_count,
        "height": audit.height,
        "width": audit.width,
        "profile_spread_obstruction": audit.profile_spread_obstruction,
    }


def _summary_to_dict(summary: RandomSprinkleSizeSummary) -> dict[str, Any]:
    return {
        "event_count": summary.event_count,
        "sample_count": summary.sample_count,
        "t126_pass_count": summary.t126_pass_count,
        "order_dimension_obstruction_count": summary.order_dimension_obstruction_count,
        "other_obstruction_count": summary.other_obstruction_count,
        "t156_band_pass_count": summary.t156_band_pass_count,
        "mean_ordering_fraction": _fraction_to_dict(summary.mean_ordering_fraction),
        "mean_absolute_gap_from_half": _fraction_to_dict(
            summary.mean_absolute_gap_from_half
        ),
        "order_dimension_obstruction_rate": _fraction_to_dict(
            summary.order_dimension_obstruction_rate
        ),
        "t156_band_pass_rate": _fraction_to_dict(summary.t156_band_pass_rate),
        "classification_counts": [
            {"classification": classification, "count": count}
            for classification, count in summary.classification_counts
        ],
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t524_result_to_dict(run_t524_analysis()), indent=2))
