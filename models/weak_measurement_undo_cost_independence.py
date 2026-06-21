"""T93: weak-measurement undo-cost independence audit.

This model tests the remaining T91 escape hatch: a hardware-defined undo-cost
meter. It asks whether an undo-cost coordinate is independent of the standard
monitored record and postselection, and whether it can change a TaF verdict
while standard weak-measurement statistics are held fixed.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose


STANDARD_RECORD = "standard_monitoring_record"
CONTROL_SCHEDULE = "control_schedule"
POSTSELECTED_SUCCESS = "postselected_success"
INDEPENDENT_METER = "independent_cost_meter"


@dataclass(frozen=True)
class UndoCostPoint:
    time: float
    coherence: float
    redundancy: int
    access: int
    reversal_success_probability: float
    undo_cost: float


@dataclass(frozen=True)
class UndoCostTrajectory:
    name: str
    points: tuple[UndoCostPoint, ...]

    def standard_signature(self) -> tuple[tuple[float, float, int, int, float], ...]:
        return tuple(
            (
                point.time,
                point.coherence,
                point.redundancy,
                point.access,
                point.reversal_success_probability,
            )
            for point in self.points
        )


@dataclass(frozen=True)
class UndoCostProtocol:
    coherence_epsilon: float
    redundancy_threshold: int
    access_threshold: int
    undo_cost_threshold: float
    cost_source: str
    pre_registered: bool
    independent_of_standard_record: bool
    requires_postselection: bool
    cost_meter_calibrated: bool


@dataclass(frozen=True)
class UndoCostTimes:
    decoherence_time: float | None
    redundancy_time: float | None
    access_time: float | None
    taf_finality_time: float | None


@dataclass(frozen=True)
class UndoCostAudit:
    case: str
    standard_timelines_equal: bool
    undo_cost_differs: bool
    taf_verdict_changes: bool
    classification: str
    blocker: str


@dataclass(frozen=True)
class T93Result:
    audits: tuple[UndoCostAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    blocker: str
    recommended_next: str


def first_time(points: tuple[UndoCostPoint, ...], predicate) -> float | None:
    for point in points:
        if predicate(point):
            return point.time
    return None


def compute_times(trajectory: UndoCostTrajectory, protocol: UndoCostProtocol) -> UndoCostTimes:
    points = trajectory.points
    return UndoCostTimes(
        decoherence_time=first_time(
            points,
            lambda point: point.coherence <= protocol.coherence_epsilon,
        ),
        redundancy_time=first_time(
            points,
            lambda point: point.redundancy >= protocol.redundancy_threshold,
        ),
        access_time=first_time(
            points,
            lambda point: point.access >= protocol.access_threshold,
        ),
        taf_finality_time=first_time(
            points,
            lambda point: (
                point.redundancy >= protocol.redundancy_threshold
                and point.access >= protocol.access_threshold
                and point.undo_cost >= protocol.undo_cost_threshold
            ),
        ),
    )


def audit_pair(
    case: str,
    left: UndoCostTrajectory,
    right: UndoCostTrajectory,
    protocol: UndoCostProtocol,
) -> UndoCostAudit:
    left_times = compute_times(left, protocol)
    right_times = compute_times(right, protocol)
    standard_timelines_equal = left.standard_signature() == right.standard_signature()
    undo_cost_differs = tuple(point.undo_cost for point in left.points) != tuple(
        point.undo_cost for point in right.points
    )
    taf_verdict_changes = not _same_time(
        left_times.taf_finality_time,
        right_times.taf_finality_time,
    )

    classification, blocker = _classify_pair(
        protocol,
        standard_timelines_equal,
        undo_cost_differs,
        taf_verdict_changes,
    )

    return UndoCostAudit(
        case=case,
        standard_timelines_equal=standard_timelines_equal,
        undo_cost_differs=undo_cost_differs,
        taf_verdict_changes=taf_verdict_changes,
        classification=classification,
        blocker=blocker,
    )


def _classify_pair(
    protocol: UndoCostProtocol,
    standard_timelines_equal: bool,
    undo_cost_differs: bool,
    taf_verdict_changes: bool,
) -> tuple[str, str]:
    if not protocol.pre_registered:
        return "null_not_preregistered", "undo-cost rule is fixed after analysis"
    if protocol.requires_postselection or protocol.cost_source == POSTSELECTED_SUCCESS:
        return "null_postselected_cost", "cost coordinate depends on success-conditioned recovery"
    if not protocol.independent_of_standard_record or protocol.cost_source in {
        STANDARD_RECORD,
        CONTROL_SCHEDULE,
    }:
        return "null_proxy_cost", "cost coordinate is a proxy for the monitored record or control schedule"
    if not protocol.cost_meter_calibrated:
        return "null_uncalibrated_meter", "meter has no calibration tying readout to physical undo cost"
    if not standard_timelines_equal:
        return "not_isolated_standard_record_changes", "standard monitored statistics changed too"
    if not undo_cost_differs:
        return "no_independent_variation", "independent meter does not vary across the witness pair"
    if taf_verdict_changes:
        return "candidate_non_null_undo_cost_axis", "independent meter changes the TaF verdict with standard statistics fixed"
    return "independent_but_not_decisive", "meter varies but does not change the TaF verdict"


def control_energy_proxy_pair() -> tuple[UndoCostTrajectory, UndoCostTrajectory]:
    costs = (0.0, 0.0, 1.0, 2.0, 3.0, 3.0)
    return (
        _trajectory("control_proxy_left", costs),
        _trajectory("control_proxy_right", costs),
    )


def postselected_cost_pair() -> tuple[UndoCostTrajectory, UndoCostTrajectory]:
    return (
        _trajectory("postselected_early", (0.0, 0.0, 1.0, 2.0, 2.5, 3.0)),
        _trajectory("postselected_late", (0.0, 0.0, 0.0, 1.0, 2.5, 3.0)),
    )


def independent_meter_pair() -> tuple[UndoCostTrajectory, UndoCostTrajectory]:
    return (
        _trajectory("meter_early", (0.0, 0.0, 0.5, 2.0, 3.0, 3.0)),
        _trajectory("meter_late", (0.0, 0.0, 0.5, 1.0, 2.0, 3.0)),
    )


def independent_but_nondecisive_pair() -> tuple[UndoCostTrajectory, UndoCostTrajectory]:
    return (
        _trajectory("meter_varies_left", (0.0, 0.0, 0.5, 2.0, 2.5, 3.0)),
        _trajectory("meter_varies_right", (0.0, 0.0, 0.5, 2.1, 2.6, 3.1)),
    )


def proxy_protocol() -> UndoCostProtocol:
    return UndoCostProtocol(
        coherence_epsilon=0.10,
        redundancy_threshold=2,
        access_threshold=2,
        undo_cost_threshold=2.0,
        cost_source=CONTROL_SCHEDULE,
        pre_registered=True,
        independent_of_standard_record=False,
        requires_postselection=False,
        cost_meter_calibrated=True,
    )


def postselected_protocol() -> UndoCostProtocol:
    return UndoCostProtocol(
        coherence_epsilon=0.10,
        redundancy_threshold=2,
        access_threshold=2,
        undo_cost_threshold=2.0,
        cost_source=POSTSELECTED_SUCCESS,
        pre_registered=True,
        independent_of_standard_record=False,
        requires_postselection=True,
        cost_meter_calibrated=True,
    )


def independent_meter_protocol() -> UndoCostProtocol:
    return UndoCostProtocol(
        coherence_epsilon=0.10,
        redundancy_threshold=2,
        access_threshold=2,
        undo_cost_threshold=2.0,
        cost_source=INDEPENDENT_METER,
        pre_registered=True,
        independent_of_standard_record=True,
        requires_postselection=False,
        cost_meter_calibrated=True,
    )


def run_t93_analysis() -> T93Result:
    proxy_left, proxy_right = control_energy_proxy_pair()
    post_left, post_right = postselected_cost_pair()
    meter_left, meter_right = independent_meter_pair()
    nond_left, nond_right = independent_but_nondecisive_pair()

    audits = (
        audit_pair("control_energy_proxy", proxy_left, proxy_right, proxy_protocol()),
        audit_pair("postselected_reversal_success", post_left, post_right, postselected_protocol()),
        audit_pair("independent_meter_candidate", meter_left, meter_right, independent_meter_protocol()),
        audit_pair("independent_meter_nondecisive", nond_left, nond_right, independent_meter_protocol()),
    )

    strongest_claim = (
        "A hardware undo-cost axis is non-null only if a calibrated, pre-registered "
        "meter changes the TaF verdict while coherence, redundancy, access, and "
        "reversal-success statistics are fixed. Control-pulse energy, trajectory-derived "
        "cost, and success-conditioned recovery are null."
    )
    improved = (
        "T93 turns T91's remaining undo-cost escape hatch into a concrete admission "
        "test with a positive witness shape and three failure modes."
    )
    weakened = (
        "The weak-measurement route is weakened again: naming an undo operation, "
        "feedback sequence, or reversal success event is not enough to make T12 non-null."
    )
    falsification_condition = (
        "T93 fails if control-schedule energy or success-conditioned reversal can be "
        "used as an independent D1 coordinate while standard monitored statistics are "
        "held fixed, or if a calibrated independent cost meter changes no TaF verdict "
        "yet still counts as a discriminator."
    )
    q1_update = (
        "Keep Q1 partially supported, but treat T12 as blocked except for a future "
        "platform with a calibrated pre-registered undo-cost meter that is independent "
        "of the monitored record and not postselected."
    )
    blocker = (
        "No real platform in the repo currently supplies the calibrated independent "
        "undo-cost meter instantiated by the candidate witness."
    )
    recommended_next = (
        "Either name an actual hardware meter and raw-log schema satisfying T93, or "
        "demote weak measurement below detector provenance in the active roadmap."
    )

    return T93Result(
        audits=audits,
        strongest_claim=strongest_claim,
        improved=improved,
        weakened=weakened,
        falsification_condition=falsification_condition,
        q1_update=q1_update,
        blocker=blocker,
        recommended_next=recommended_next,
    )


def t93_result_to_dict(result: T93Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "case": audit.case,
                "standard_timelines_equal": audit.standard_timelines_equal,
                "undo_cost_differs": audit.undo_cost_differs,
                "taf_verdict_changes": audit.taf_verdict_changes,
                "classification": audit.classification,
                "blocker": audit.blocker,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def _trajectory(name: str, costs: tuple[float, ...]) -> UndoCostTrajectory:
    base = (
        (0.0, 1.00, 0, 0, 0.00),
        (1.0, 0.70, 0, 0, 0.10),
        (2.0, 0.40, 1, 1, 0.30),
        (3.0, 0.18, 2, 2, 0.55),
        (4.0, 0.08, 3, 3, 0.75),
        (5.0, 0.03, 3, 3, 0.80),
    )
    return UndoCostTrajectory(
        name=name,
        points=tuple(
            UndoCostPoint(time, coherence, redundancy, access, success, cost)
            for (time, coherence, redundancy, access, success), cost in zip(base, costs)
        ),
    )


def _same_time(left: float | None, right: float | None) -> bool:
    if left is None or right is None:
        return left is right
    return isclose(left, right)
