from __future__ import annotations

import math

from models.t3_spacelike_commit_order_sanity import (
    Event,
    build_result,
    causal_relation,
    lorentz_transform,
    minkowski_interval_squared,
    proper_time_between,
)


def test_spacelike_interval_has_no_invariant_commit_order() -> None:
    source_a = Event("A", 0.0, -1.0)
    source_b = Event("B", 0.0, 1.0)

    assert minkowski_interval_squared(source_a, source_b) < 0
    assert causal_relation(source_a, source_b) == "spacelike"


def test_frame_order_flips_without_changing_interval() -> None:
    source_a = Event("A", 0.0, -1.0)
    source_b = Event("B", 0.0, 1.0)
    plus_a = lorentz_transform(source_a, 0.5)
    plus_b = lorentz_transform(source_b, 0.5)
    minus_a = lorentz_transform(source_a, -0.5)
    minus_b = lorentz_transform(source_b, -0.5)

    assert plus_b.t < plus_a.t
    assert minus_a.t < minus_b.t
    assert math.isclose(
        minkowski_interval_squared(plus_a, plus_b),
        minkowski_interval_squared(source_a, source_b),
    )
    assert math.isclose(
        minkowski_interval_squared(minus_a, minus_b),
        minkowski_interval_squared(source_a, source_b),
    )


def test_common_future_reconciliation_is_causal_for_both_records() -> None:
    source_a = Event("A", 0.0, -1.0)
    source_b = Event("B", 0.0, 1.0)
    common_future = Event("C", 3.0, 0.0)

    assert causal_relation(source_a, common_future) == "causal_future"
    assert causal_relation(source_b, common_future) == "causal_future"


def test_proper_time_remains_invariant_for_observer_worldline() -> None:
    observer_start = Event("O0", 0.0, 0.0)
    observer_end = Event("O1", 2.0, 1.0)
    rest_start = lorentz_transform(observer_start, 0.5)
    rest_end = lorentz_transform(observer_end, 0.5)

    assert math.isclose(
        proper_time_between(observer_start, observer_end),
        proper_time_between(rest_start, rest_end),
    )


def test_result_blocks_replacement_geometry_and_claim_upgrade() -> None:
    result = build_result()
    orders = {frame.frame: frame.ab_order for frame in result.frames}

    assert result.verdict == "T3_SPACELIKE_SANITY_CHECK_BUILT_REVIEW_ONLY"
    assert orders["lab"] == "simultaneous_in_frame"
    assert orders["observer_plus_half_c"] == "B_before_A"
    assert orders["observer_minus_half_c"] == "A_before_B"
    assert result.common_future_reconciliation == {
        "A_to_C": True,
        "B_to_C": True,
        "A_to_B_spacelike": True,
    }
    assert "R1 claim promotion" in result.not_earned
    assert "hidden universal present" in result.not_earned
