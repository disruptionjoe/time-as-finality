"""T3 spacelike commit-order sanity check.

The fixture keeps the physics deliberately small: 1+1 Minkowski events, Lorentz
transforms with c=1, and a common-future reconciliation event. It tests where
finality language is safe: records can reconcile in a common causal future, but
there is no invariant order between spacelike-separated source events.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import argparse
import json
import math
from pathlib import Path
from typing import Any


TOLERANCE = 1e-9


@dataclass(frozen=True)
class Event:
    name: str
    t: float
    x: float


@dataclass(frozen=True)
class FrameReport:
    frame: str
    velocity: float
    transformed_events: dict[str, tuple[float, float]]
    ab_order: str


@dataclass(frozen=True)
class T3Result:
    verdict: str
    events: dict[str, dict[str, float | str]]
    interval_ab: float
    interval_ac: float
    interval_bc: float
    frames: list[FrameReport]
    common_future_reconciliation: dict[str, bool]
    proper_time_check: dict[str, float]
    safe_finality_reading: str
    not_earned: tuple[str, ...]


def minkowski_interval_squared(left: Event, right: Event) -> float:
    dt = right.t - left.t
    dx = right.x - left.x
    return dt * dt - dx * dx


def lorentz_transform(event: Event, velocity: float) -> Event:
    if abs(velocity) >= 1:
        raise ValueError("velocity must satisfy |v| < 1")
    gamma = 1.0 / math.sqrt(1.0 - velocity * velocity)
    t_prime = gamma * (event.t - velocity * event.x)
    x_prime = gamma * (event.x - velocity * event.t)
    return Event(event.name, t_prime, x_prime)


def causal_relation(left: Event, right: Event) -> str:
    interval = minkowski_interval_squared(left, right)
    dt = right.t - left.t
    if abs(interval) <= TOLERANCE:
        return "null_future" if dt >= -TOLERANCE else "null_past"
    if interval < 0:
        return "spacelike"
    return "causal_future" if dt > 0 else "causal_past"


def event_order(left: Event, right: Event) -> str:
    if abs(left.t - right.t) <= TOLERANCE:
        return "simultaneous_in_frame"
    return f"{left.name}_before_{right.name}" if left.t < right.t else f"{right.name}_before_{left.name}"


def frame_report(name: str, velocity: float, events: tuple[Event, ...]) -> FrameReport:
    transformed = tuple(lorentz_transform(event, velocity) for event in events)
    by_name = {event.name: (event.t, event.x) for event in transformed}
    return FrameReport(
        frame=name,
        velocity=velocity,
        transformed_events=by_name,
        ab_order=event_order(by_name_event(transformed, "A"), by_name_event(transformed, "B")),
    )


def by_name_event(events: tuple[Event, ...], name: str) -> Event:
    for event in events:
        if event.name == name:
            return event
    raise KeyError(name)


def proper_time_between(left: Event, right: Event) -> float:
    interval = minkowski_interval_squared(left, right)
    if interval < -TOLERANCE:
        raise ValueError("proper time is not defined for spacelike-separated events")
    return math.sqrt(max(interval, 0.0))


def build_result() -> T3Result:
    source_a = Event("A", 0.0, -1.0)
    source_b = Event("B", 0.0, 1.0)
    common_future = Event("C", 3.0, 0.0)
    observer_start = Event("O0", 0.0, 0.0)
    observer_end = Event("O1", 2.0, 1.0)
    observer_velocity = 0.5

    events = (source_a, source_b, common_future)
    frames = [
        frame_report("lab", 0.0, events),
        frame_report("observer_plus_half_c", 0.5, events),
        frame_report("observer_minus_half_c", -0.5, events),
    ]

    transformed_start = lorentz_transform(observer_start, observer_velocity)
    transformed_end = lorentz_transform(observer_end, observer_velocity)
    proper_time_lab = proper_time_between(observer_start, observer_end)
    proper_time_rest_frame = proper_time_between(transformed_start, transformed_end)

    return T3Result(
        verdict="T3_SPACELIKE_SANITY_CHECK_BUILT_REVIEW_ONLY",
        events={event.name: asdict(event) for event in events},
        interval_ab=minkowski_interval_squared(source_a, source_b),
        interval_ac=minkowski_interval_squared(source_a, common_future),
        interval_bc=minkowski_interval_squared(source_b, common_future),
        frames=frames,
        common_future_reconciliation={
            "A_to_C": causal_relation(source_a, common_future) == "causal_future",
            "B_to_C": causal_relation(source_b, common_future) == "causal_future",
            "A_to_B_spacelike": causal_relation(source_a, source_b) == "spacelike",
        },
        proper_time_check={
            "lab_frame": proper_time_lab,
            "observer_rest_frame": proper_time_rest_frame,
            "absolute_difference": abs(proper_time_lab - proper_time_rest_frame),
        },
        safe_finality_reading=(
            "Finality language may track when records from A and B can be "
            "compared at C, but it must not add an invariant global commit order "
            "between spacelike-separated A and B."
        ),
        not_earned=(
            "R1 claim promotion",
            "replacement spacetime geometry",
            "hidden universal present",
            "global commit order for spacelike events",
            "proper-time replacement",
        ),
    )


def result_to_jsonable(result: T3Result) -> dict[str, Any]:
    payload = asdict(result)
    payload["frames"] = [asdict(frame) for frame in result.frames]
    return payload


def write_results(result: T3Result, repo_root: Path) -> None:
    json_path = repo_root / "results" / "T3-spacelike-commit-order-sanity-v0.1.json"
    md_path = repo_root / "results" / "T3-spacelike-commit-order-sanity-v0.1-results.md"
    json_path.write_text(json.dumps(result_to_jsonable(result), indent=2) + "\n", encoding="utf-8")

    frame_lines = [
        f"- `{frame.frame}` (`v={frame.velocity}`): `{frame.ab_order}`"
        for frame in result.frames
    ]
    blocked = [f"- {item}" for item in result.not_earned]
    md_path.write_text(
        "\n".join(
            [
                "# T3 Spacelike Commit-Order Sanity Results v0.1",
                "",
                f"Verdict: `{result.verdict}`",
                "",
                "## Fixture",
                "",
                "Events A and B are spacelike-separated in 1+1 Minkowski space. "
                "Event C lies in the common causal future of both.",
                "",
                "## Frame Orders",
                "",
                *frame_lines,
                "",
                "## Invariant Checks",
                "",
                f"- Interval A-B: `{result.interval_ab}` (spacelike)",
                f"- Interval A-C: `{result.interval_ac}` (causal future)",
                f"- Interval B-C: `{result.interval_bc}` (causal future)",
                "- Proper-time difference across frames: "
                f"`{result.proper_time_check['absolute_difference']}`",
                "",
                "## Safe Reading",
                "",
                result.safe_finality_reading,
                "",
                "## Not Earned",
                "",
                *blocked,
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = build_result()
    if args.write_results:
        write_results(result, Path(__file__).resolve().parents[1])
    print(json.dumps(result_to_jsonable(result), indent=2))


if __name__ == "__main__":
    main()
