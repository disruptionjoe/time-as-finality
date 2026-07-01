"""T379: Lorentz-pattern rendering from propagation constraints.

T378 recovered observer-relative rendering from a generated shared
compatibility substrate. T379 asks whether the relativity pattern can be derived
from propagation constraints over that substrate rather than choosing observer
scales by hand.

The derivation is intentionally narrow:

* primitive compatibility signals define the shared speed unit c = 1;
* an observer rest calibration is a pair of outbound/return signal counts;
* the observer's own rest line must balance those two signal counts;
* reciprocal signal scaling preserves the round-trip product.

From those constraints, the light-channel scale, beta, gamma, time dilation,
simultaneity disagreement, and interval preservation are computed. The result is
still a finite pattern match, not a physical derivation of special relativity.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import isqrt
from pathlib import Path
import sys


if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.generated_compatibility_substrate import (
    FORBIDDEN_SOURCE_COLUMNS,
    GeneratedCompatibilitySubstrate,
    generate_compatibility_substrate,
    landmark_ids,
    source_rows,
    derived_ranks,
)


COMPATIBILITY_SIGNAL_SPEED = Fraction(1, 1)


@dataclass(frozen=True)
class SignalCalibration:
    observer_id: str
    outbound_left_ticks: int
    return_right_ticks: int


@dataclass(frozen=True)
class DerivedRenderMap:
    observer_id: str
    outbound_left_ticks: int
    return_right_ticks: int
    signal_scale: Fraction
    beta: Fraction
    gamma: Fraction
    rest_tick: Fraction
    dilation_against_rest_observer: Fraction
    derivation_steps: tuple[str, ...]


@dataclass(frozen=True)
class RenderedRecord:
    observer_id: str
    record_id: str
    left_lineage: int
    right_lineage: int
    signal_time: Fraction
    signal_space: Fraction


@dataclass(frozen=True)
class TransformCoefficients:
    observer_id: str
    gamma: Fraction
    beta: Fraction
    time_from_rest_time: Fraction
    time_from_rest_space: Fraction
    space_from_rest_time: Fraction
    space_from_rest_space: Fraction
    determinant: Fraction


@dataclass(frozen=True)
class SignalSpeedCheck:
    observer_id: str
    left_channel_speed: Fraction
    right_channel_speed: Fraction
    speed_unit: Fraction


@dataclass(frozen=True)
class TimeDilationCheck:
    observer_id: str
    calibration_record_rank: tuple[int, int]
    own_space: Fraction
    own_time: Fraction
    rest_observer_time: Fraction
    dilation_ratio: Fraction
    expected_gamma: Fraction


@dataclass(frozen=True)
class PairInvariant:
    left_id: str
    right_id: str
    substrate_interval: int
    rendered_intervals: tuple[tuple[str, Fraction], ...]


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T379Result:
    source_has_no_minkowski_columns: bool
    render_maps_derived_from_signal_calibration: bool
    primitive_signal_speed_invariant: bool
    round_trip_balance_satisfied: bool
    lorentz_pattern_coefficients_recovered: bool
    time_dilation_recovered: bool
    simultaneity_disagreement: bool
    simultaneity_pair: tuple[str, str]
    interval_invariant: bool
    checked_pair_count: int
    observer_count: int
    signal_speed_unit: Fraction
    render_maps: tuple[DerivedRenderMap, ...]
    transform_coefficients: tuple[TransformCoefficients, ...]
    time_dilation_checks: tuple[TimeDilationCheck, ...]
    sample_pair_invariants: tuple[PairInvariant, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str


def canonical_substrate() -> GeneratedCompatibilitySubstrate:
    return generate_compatibility_substrate(left_steps=9, right_steps=9)


def canonical_calibrations() -> tuple[SignalCalibration, ...]:
    return (
        SignalCalibration("A_rest", 1, 1),
        SignalCalibration("B_fast_outbound", 1, 4),
        SignalCalibration("C_fast_return", 4, 1),
        SignalCalibration("D_mild_outbound", 4, 9),
    )


def sqrt_fraction(value: Fraction) -> Fraction:
    numerator_root = isqrt(value.numerator)
    denominator_root = isqrt(value.denominator)
    if (
        numerator_root * numerator_root != value.numerator
        or denominator_root * denominator_root != value.denominator
    ):
        raise ValueError(f"ratio is not an exact rational square: {value}")
    return Fraction(numerator_root, denominator_root)


def source_has_no_minkowski_columns(
    substrate: GeneratedCompatibilitySubstrate,
) -> bool:
    if set(substrate.source_columns) & FORBIDDEN_SOURCE_COLUMNS:
        return False
    return all(not (set(row) & FORBIDDEN_SOURCE_COLUMNS) for row in source_rows(substrate))


def derive_render_map(calibration: SignalCalibration) -> DerivedRenderMap:
    if calibration.outbound_left_ticks <= 0 or calibration.return_right_ticks <= 0:
        raise ValueError("signal calibration counts must be positive")

    left_ticks = calibration.outbound_left_ticks
    right_ticks = calibration.return_right_ticks
    signal_scale = sqrt_fraction(Fraction(right_ticks, left_ticks))
    reciprocal_scale = Fraction(1, 1) / signal_scale
    rest_tick = signal_scale * left_ticks
    return_tick = Fraction(right_ticks, 1) * reciprocal_scale
    if rest_tick != return_tick:
        raise ValueError("round-trip calibration does not balance")

    scale_squared = signal_scale * signal_scale
    beta = (scale_squared - 1) / (scale_squared + 1)
    gamma = (signal_scale + reciprocal_scale) / 2
    rest_observer_time = Fraction(left_ticks + right_ticks, 2)
    dilation = rest_observer_time / rest_tick

    return DerivedRenderMap(
        observer_id=calibration.observer_id,
        outbound_left_ticks=left_ticks,
        return_right_ticks=right_ticks,
        signal_scale=signal_scale,
        beta=beta,
        gamma=gamma,
        rest_tick=rest_tick,
        dilation_against_rest_observer=dilation,
        derivation_steps=(
            "rest calibration supplies outbound and return compatibility signal counts",
            "own rest line requires scaled outbound count to equal scaled return count",
            "reciprocal scaling preserves round-trip signal product",
            "therefore scale^2 = return_right_ticks / outbound_left_ticks",
            "beta and gamma are computed from the derived reciprocal signal scale",
        ),
    )


def derive_render_maps(
    calibrations: tuple[SignalCalibration, ...],
) -> tuple[DerivedRenderMap, ...]:
    return tuple(derive_render_map(calibration) for calibration in calibrations)


def round_trip_balance_satisfied(render_maps: tuple[DerivedRenderMap, ...]) -> bool:
    return all(
        render_map.signal_scale * render_map.outbound_left_ticks
        == Fraction(render_map.return_right_ticks, 1) / render_map.signal_scale
        == render_map.rest_tick
        for render_map in render_maps
    )


def render_record(
    record_id: str,
    ranks: dict[str, tuple[int, int]],
    render_map: DerivedRenderMap,
) -> RenderedRecord:
    left_lineage, right_lineage = ranks[record_id]
    scaled_left = render_map.signal_scale * left_lineage
    scaled_right = Fraction(right_lineage, 1) / render_map.signal_scale
    return RenderedRecord(
        observer_id=render_map.observer_id,
        record_id=record_id,
        left_lineage=left_lineage,
        right_lineage=right_lineage,
        signal_time=(scaled_left + scaled_right) / 2,
        signal_space=(scaled_left - scaled_right) / 2,
    )


def substrate_interval(
    left_id: str,
    right_id: str,
    ranks: dict[str, tuple[int, int]],
) -> int:
    left_left, left_right = ranks[left_id]
    right_left, right_right = ranks[right_id]
    return (right_left - left_left) * (right_right - left_right)


def rendered_interval(
    left_id: str,
    right_id: str,
    ranks: dict[str, tuple[int, int]],
    render_map: DerivedRenderMap,
) -> Fraction:
    left_rendered = render_record(left_id, ranks, render_map)
    right_rendered = render_record(right_id, ranks, render_map)
    delta_time = right_rendered.signal_time - left_rendered.signal_time
    delta_space = right_rendered.signal_space - left_rendered.signal_space
    return delta_time * delta_time - delta_space * delta_space


def pair_invariants(
    substrate: GeneratedCompatibilitySubstrate,
    render_maps: tuple[DerivedRenderMap, ...],
    record_ids: tuple[str, ...] | None = None,
) -> tuple[PairInvariant, ...]:
    ranks = derived_ranks(substrate)
    ids = record_ids if record_ids is not None else tuple(record.record_id for record in substrate.records)
    rows: list[PairInvariant] = []
    for left_id, right_id in combinations(ids, 2):
        rows.append(
            PairInvariant(
                left_id=left_id,
                right_id=right_id,
                substrate_interval=substrate_interval(left_id, right_id, ranks),
                rendered_intervals=tuple(
                    (
                        render_map.observer_id,
                        rendered_interval(left_id, right_id, ranks, render_map),
                    )
                    for render_map in render_maps
                ),
            )
        )
    return tuple(rows)


def intervals_are_invariant(rows: tuple[PairInvariant, ...]) -> bool:
    return all(
        all(
            interval == Fraction(row.substrate_interval, 1)
            for _, interval in row.rendered_intervals
        )
        for row in rows
    )


def primitive_signal_speed_checks(
    render_maps: tuple[DerivedRenderMap, ...],
) -> tuple[SignalSpeedCheck, ...]:
    checks: list[SignalSpeedCheck] = []
    for render_map in render_maps:
        left_dt = render_map.signal_scale / 2
        left_dx = render_map.signal_scale / 2
        right_dt = Fraction(1, 1) / (2 * render_map.signal_scale)
        right_dx = -Fraction(1, 1) / (2 * render_map.signal_scale)
        checks.append(
            SignalSpeedCheck(
                observer_id=render_map.observer_id,
                left_channel_speed=left_dx / left_dt,
                right_channel_speed=right_dx / right_dt,
                speed_unit=COMPATIBILITY_SIGNAL_SPEED,
            )
        )
    return tuple(checks)


def primitive_signal_speed_invariant(
    checks: tuple[SignalSpeedCheck, ...],
) -> bool:
    return all(
        check.left_channel_speed == check.speed_unit
        and check.right_channel_speed == -check.speed_unit
        for check in checks
    )


def transform_coefficients(
    render_map: DerivedRenderMap,
) -> TransformCoefficients:
    signal_scale = render_map.signal_scale
    reciprocal_scale = Fraction(1, 1) / signal_scale
    gamma = (signal_scale + reciprocal_scale) / 2
    delta = (signal_scale - reciprocal_scale) / 2
    return TransformCoefficients(
        observer_id=render_map.observer_id,
        gamma=gamma,
        beta=delta / gamma,
        time_from_rest_time=gamma,
        time_from_rest_space=delta,
        space_from_rest_time=delta,
        space_from_rest_space=gamma,
        determinant=gamma * gamma - delta * delta,
    )


def transform_matches_rendering(
    substrate: GeneratedCompatibilitySubstrate,
    render_maps: tuple[DerivedRenderMap, ...],
) -> bool:
    ranks = derived_ranks(substrate)
    rest_map = render_maps[0]
    for render_map in render_maps:
        coefficients = transform_coefficients(render_map)
        for record in substrate.records:
            rest_rendered = render_record(record.record_id, ranks, rest_map)
            rendered = render_record(record.record_id, ranks, render_map)
            transformed_time = (
                coefficients.time_from_rest_time * rest_rendered.signal_time
                + coefficients.time_from_rest_space * rest_rendered.signal_space
            )
            transformed_space = (
                coefficients.space_from_rest_time * rest_rendered.signal_time
                + coefficients.space_from_rest_space * rest_rendered.signal_space
            )
            if (
                transformed_time != rendered.signal_time
                or transformed_space != rendered.signal_space
            ):
                return False
    return True


def lorentz_pattern_coefficients_recovered(
    substrate: GeneratedCompatibilitySubstrate,
    render_maps: tuple[DerivedRenderMap, ...],
) -> bool:
    coefficients = tuple(transform_coefficients(render_map) for render_map in render_maps)
    return all(
        item.determinant == 1 and item.beta == render_map.beta
        for item, render_map in zip(coefficients, render_maps)
    ) and transform_matches_rendering(substrate, render_maps)


def time_dilation_checks(
    substrate: GeneratedCompatibilitySubstrate,
    render_maps: tuple[DerivedRenderMap, ...],
) -> tuple[TimeDilationCheck, ...]:
    ranks = derived_ranks(substrate)
    rank_to_id = {rank: record_id for record_id, rank in ranks.items()}
    rest_map = render_maps[0]
    checks: list[TimeDilationCheck] = []
    for render_map in render_maps:
        calibration_rank = (
            render_map.outbound_left_ticks,
            render_map.return_right_ticks,
        )
        record_id = rank_to_id[calibration_rank]
        own_rendered = render_record(record_id, ranks, render_map)
        rest_rendered = render_record(record_id, ranks, rest_map)
        checks.append(
            TimeDilationCheck(
                observer_id=render_map.observer_id,
                calibration_record_rank=calibration_rank,
                own_space=own_rendered.signal_space,
                own_time=own_rendered.signal_time,
                rest_observer_time=rest_rendered.signal_time,
                dilation_ratio=rest_rendered.signal_time / own_rendered.signal_time,
                expected_gamma=render_map.gamma,
            )
        )
    return tuple(checks)


def time_dilation_recovered(checks: tuple[TimeDilationCheck, ...]) -> bool:
    return all(
        check.own_space == 0 and check.dilation_ratio == check.expected_gamma
        for check in checks
    )


def simultaneity_disagreement(
    substrate: GeneratedCompatibilitySubstrate,
    render_maps: tuple[DerivedRenderMap, ...],
) -> tuple[bool, tuple[str, str]]:
    ranks = derived_ranks(substrate)
    landmarks = landmark_ids(substrate)
    left_only = landmarks["left_only"]
    right_only = landmarks["right_only"]
    rendered_pairs = [
        (
            render_map.observer_id,
            render_record(left_only, ranks, render_map).signal_time,
            render_record(right_only, ranks, render_map).signal_time,
        )
        for render_map in render_maps
    ]
    same = [observer_id for observer_id, left_time, right_time in rendered_pairs if left_time == right_time]
    different = [
        observer_id
        for observer_id, left_time, right_time in rendered_pairs
        if left_time != right_time
    ]
    return bool(same and different), (left_only, right_only)


def render_maps_are_derived(
    render_maps: tuple[DerivedRenderMap, ...],
) -> bool:
    return all(
        render_map.signal_scale
        == sqrt_fraction(
            Fraction(render_map.return_right_ticks, render_map.outbound_left_ticks)
        )
        and render_map.beta
        == (
            render_map.signal_scale * render_map.signal_scale - 1
        )
        / (
            render_map.signal_scale * render_map.signal_scale + 1
        )
        for render_map in render_maps
    )


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            comparator_id="minkowski_coordinate_import",
            status="not_imported_as_source",
            absorbs=False,
            reason=(
                "source rows contain only generated compatibility records, parents, and local "
                "channels; time, space, metric, and interval values are derived render outputs"
            ),
        ),
        ComparatorVerdict(
            comparator_id="hand_chosen_observer_scale",
            status="weakened_by_round_trip_derivation",
            absorbs=False,
            reason=(
                "observer scales are computed from reciprocal round-trip signal counts rather "
                "than supplied directly as render-map parameters"
            ),
        ),
        ComparatorVerdict(
            comparator_id="fixed_light_channel_basis",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "the two primitive compatibility channels and c=1 signal-speed convention are "
                "fixed assumptions, not derived from a deeper substrate"
            ),
        ),
        ComparatorVerdict(
            comparator_id="linear_reciprocal_rendering",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "linearity and reciprocal scaling are derivation premises; the fixture does not "
                "prove them from arbitrary compatibility data"
            ),
        ),
        ComparatorVerdict(
            comparator_id="finite_generated_closure",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "the finite generated substrate can still be expanded into a completed table "
                "after the derivation"
            ),
        ),
        ComparatorVerdict(
            comparator_id="causal_order_only",
            status="insufficient",
            absorbs=False,
            reason=(
                "the invariant uses signal-count products; causal comparability alone does not "
                "supply the interval magnitudes"
            ),
        ),
    )


def run_t379_analysis() -> T379Result:
    substrate = canonical_substrate()
    render_maps = derive_render_maps(canonical_calibrations())
    all_rows = pair_invariants(substrate, render_maps)
    landmarks = landmark_ids(substrate)
    sample_ids = tuple(landmarks[label] for label in ("origin", "near", "left_only", "right_only", "future", "far"))
    sample_rows = pair_invariants(substrate, render_maps, sample_ids)
    speed_checks = primitive_signal_speed_checks(render_maps)
    dilation_checks = time_dilation_checks(substrate, render_maps)
    simultaneity_ok, simultaneity_pair = simultaneity_disagreement(substrate, render_maps)

    result_bits = {
        "source_has_no_minkowski_columns": source_has_no_minkowski_columns(substrate),
        "render_maps_derived_from_signal_calibration": render_maps_are_derived(render_maps),
        "primitive_signal_speed_invariant": primitive_signal_speed_invariant(speed_checks),
        "round_trip_balance_satisfied": round_trip_balance_satisfied(render_maps),
        "lorentz_pattern_coefficients_recovered": lorentz_pattern_coefficients_recovered(
            substrate, render_maps
        ),
        "time_dilation_recovered": time_dilation_recovered(dilation_checks),
        "simultaneity_disagreement": simultaneity_ok,
        "interval_invariant": intervals_are_invariant(all_rows),
    }
    rendered_success = all(result_bits.values())
    return T379Result(
        source_has_no_minkowski_columns=result_bits["source_has_no_minkowski_columns"],
        render_maps_derived_from_signal_calibration=result_bits[
            "render_maps_derived_from_signal_calibration"
        ],
        primitive_signal_speed_invariant=result_bits[
            "primitive_signal_speed_invariant"
        ],
        round_trip_balance_satisfied=result_bits["round_trip_balance_satisfied"],
        lorentz_pattern_coefficients_recovered=result_bits[
            "lorentz_pattern_coefficients_recovered"
        ],
        time_dilation_recovered=result_bits["time_dilation_recovered"],
        simultaneity_disagreement=result_bits["simultaneity_disagreement"],
        simultaneity_pair=simultaneity_pair,
        interval_invariant=result_bits["interval_invariant"],
        checked_pair_count=len(all_rows),
        observer_count=len(render_maps),
        signal_speed_unit=COMPATIBILITY_SIGNAL_SPEED,
        render_maps=render_maps,
        transform_coefficients=tuple(
            transform_coefficients(render_map) for render_map in render_maps
        ),
        time_dilation_checks=dilation_checks,
        sample_pair_invariants=sample_rows,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict=(
            "lorentz_pattern_recovered_from_signal_constraints_but_channel_premises_absorb"
            if rendered_success
            else "fixture_failed"
        ),
        strongest_claim=(
            "Given a generated shared compatibility substrate, invariant primitive signal speed, "
            "round-trip rest calibration, and reciprocal signal scaling, Lorentz-pattern render "
            "maps are derived rather than hand-chosen: beta, gamma, time dilation, simultaneity "
            "disagreement, and interval preservation all follow in the finite fixture. This is "
            "not a physical derivation of relativity because the light-channel and linearity "
            "premises are still assumed."
        ),
        claim_ledger_update=(
            "Register T379 as a Lorentz-pattern propagation calibration. It supports the idea "
            "that perceived time differences can arise from invariant compatibility-signal "
            "transfer constraints, but fixed light-channel and linear reciprocal-scaling premises "
            "remain live absorbers."
        ),
    )


def _fraction(value: Fraction) -> str:
    return str(value)


def _render_map_to_dict(render_map: DerivedRenderMap) -> dict[str, object]:
    return {
        "observer_id": render_map.observer_id,
        "outbound_left_ticks": render_map.outbound_left_ticks,
        "return_right_ticks": render_map.return_right_ticks,
        "signal_scale": _fraction(render_map.signal_scale),
        "beta": _fraction(render_map.beta),
        "gamma": _fraction(render_map.gamma),
        "rest_tick": _fraction(render_map.rest_tick),
        "dilation_against_rest_observer": _fraction(
            render_map.dilation_against_rest_observer
        ),
        "derivation_steps": list(render_map.derivation_steps),
    }


def _transform_to_dict(coefficients: TransformCoefficients) -> dict[str, object]:
    return {
        "observer_id": coefficients.observer_id,
        "gamma": _fraction(coefficients.gamma),
        "beta": _fraction(coefficients.beta),
        "time_from_rest_time": _fraction(coefficients.time_from_rest_time),
        "time_from_rest_space": _fraction(coefficients.time_from_rest_space),
        "space_from_rest_time": _fraction(coefficients.space_from_rest_time),
        "space_from_rest_space": _fraction(coefficients.space_from_rest_space),
        "determinant": _fraction(coefficients.determinant),
    }


def _dilation_to_dict(check: TimeDilationCheck) -> dict[str, object]:
    return {
        "observer_id": check.observer_id,
        "calibration_record_rank": list(check.calibration_record_rank),
        "own_space": _fraction(check.own_space),
        "own_time": _fraction(check.own_time),
        "rest_observer_time": _fraction(check.rest_observer_time),
        "dilation_ratio": _fraction(check.dilation_ratio),
        "expected_gamma": _fraction(check.expected_gamma),
    }


def _pair_to_dict(row: PairInvariant) -> dict[str, object]:
    return {
        "left_id": row.left_id,
        "right_id": row.right_id,
        "substrate_interval": row.substrate_interval,
        "rendered_intervals": [
            {"observer_id": observer_id, "interval": _fraction(interval)}
            for observer_id, interval in row.rendered_intervals
        ],
    }


def t379_result_to_dict(result: T379Result) -> dict[str, object]:
    return {
        "source_has_no_minkowski_columns": result.source_has_no_minkowski_columns,
        "render_maps_derived_from_signal_calibration": (
            result.render_maps_derived_from_signal_calibration
        ),
        "primitive_signal_speed_invariant": result.primitive_signal_speed_invariant,
        "round_trip_balance_satisfied": result.round_trip_balance_satisfied,
        "lorentz_pattern_coefficients_recovered": (
            result.lorentz_pattern_coefficients_recovered
        ),
        "time_dilation_recovered": result.time_dilation_recovered,
        "simultaneity_disagreement": result.simultaneity_disagreement,
        "simultaneity_pair": list(result.simultaneity_pair),
        "interval_invariant": result.interval_invariant,
        "checked_pair_count": result.checked_pair_count,
        "observer_count": result.observer_count,
        "signal_speed_unit": _fraction(result.signal_speed_unit),
        "render_maps": [_render_map_to_dict(render_map) for render_map in result.render_maps],
        "transform_coefficients": [
            _transform_to_dict(coefficients)
            for coefficients in result.transform_coefficients
        ],
        "time_dilation_checks": [
            _dilation_to_dict(check) for check in result.time_dilation_checks
        ],
        "sample_pair_invariants": [
            _pair_to_dict(row) for row in result.sample_pair_invariants
        ],
        "comparator_verdicts": [
            {
                "comparator_id": verdict.comparator_id,
                "status": verdict.status,
                "absorbs": verdict.absorbs,
                "reason": verdict.reason,
            }
            for verdict in result.comparator_verdicts
        ],
        "overall_verdict": result.overall_verdict,
        "strongest_claim": result.strongest_claim,
        "claim_ledger_update": result.claim_ledger_update,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t379_result_to_dict(run_t379_analysis()), indent=2))
