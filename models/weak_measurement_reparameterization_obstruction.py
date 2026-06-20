"""T90: weak-measurement reparameterization obstruction.

The model asks whether a proposed weak-measurement finalization time is
independent of standard monitored-record statistics, or whether it is only a
new threshold on coherence decay, redundancy, and access.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose


STANDARD = "standard_statistic"
ACCESS = "access_window"
INDEPENDENT = "independent_intervention"
POST_HOC = "post_hoc"


@dataclass(frozen=True)
class TrajectoryPoint:
    time: float
    coherence: float
    redundancy: int
    access: int
    holder_redundancy: int
    branch_support: int
    reversal_cost: int


@dataclass(frozen=True)
class WeakMeasurementTrajectory:
    name: str
    points: tuple[TrajectoryPoint, ...]

    def standard_signature(self) -> tuple[tuple[float, float, int, int], ...]:
        return tuple(
            (point.time, point.coherence, point.redundancy, point.access)
            for point in self.points
        )


@dataclass(frozen=True)
class FinalityProtocol:
    coherence_epsilon: float
    redundancy_threshold: int
    access_threshold: int
    holder_threshold: int
    branch_threshold: int
    reversal_threshold: int
    holder_source: str
    branch_source: str
    reversal_source: str

    def decisive_sources(self) -> tuple[str, ...]:
        return (self.holder_source, self.branch_source, self.reversal_source)


@dataclass(frozen=True)
class FinalityTimes:
    decoherence_time: float | None
    redundancy_time: float | None
    access_time: float | None
    taf_finality_time: float | None


@dataclass(frozen=True)
class PairAudit:
    standard_timelines_equal: bool
    standard_verdict_equal: bool
    taf_verdict_changes: bool
    has_independent_source: bool
    rejected_for_post_hoc_source: bool
    verdict: str


@dataclass(frozen=True)
class T90Result:
    null_times: FinalityTimes
    null_verdict: str
    independent_pair: PairAudit
    post_hoc_pair: PairAudit
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    blocker: str
    recommended_next: str


def first_time(points: tuple[TrajectoryPoint, ...], predicate) -> float | None:
    for point in points:
        if predicate(point):
            return point.time
    return None


def compute_finality_times(
    trajectory: WeakMeasurementTrajectory,
    protocol: FinalityProtocol,
) -> FinalityTimes:
    points = trajectory.points
    return FinalityTimes(
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
                point.access >= protocol.access_threshold
                and point.holder_redundancy >= protocol.holder_threshold
                and point.branch_support >= protocol.branch_threshold
                and point.reversal_cost >= protocol.reversal_threshold
            ),
        ),
    )


def classify_single_protocol(protocol: FinalityProtocol) -> str:
    sources = protocol.decisive_sources()
    if POST_HOC in sources:
        return "null_post_hoc"
    if INDEPENDENT not in sources:
        return "null_reparameterization"
    return "candidate_non_null"


def audit_pair(
    left: WeakMeasurementTrajectory,
    right: WeakMeasurementTrajectory,
    protocol: FinalityProtocol,
) -> PairAudit:
    left_times = compute_finality_times(left, protocol)
    right_times = compute_finality_times(right, protocol)
    standard_timelines_equal = left.standard_signature() == right.standard_signature()
    standard_verdict_equal = _same_time(left_times.decoherence_time, right_times.decoherence_time) and _same_time(
        left_times.redundancy_time,
        right_times.redundancy_time,
    )
    taf_verdict_changes = not _same_time(left_times.taf_finality_time, right_times.taf_finality_time)
    has_independent_source = INDEPENDENT in protocol.decisive_sources()
    rejected_for_post_hoc_source = POST_HOC in protocol.decisive_sources()

    if rejected_for_post_hoc_source:
        verdict = "null_post_hoc"
    elif standard_timelines_equal and standard_verdict_equal and taf_verdict_changes and has_independent_source:
        verdict = "candidate_non_null_witness"
    elif standard_timelines_equal and not taf_verdict_changes:
        verdict = "no_taf_separation"
    else:
        verdict = "not_an_isolated_witness"

    return PairAudit(
        standard_timelines_equal=standard_timelines_equal,
        standard_verdict_equal=standard_verdict_equal,
        taf_verdict_changes=taf_verdict_changes,
        has_independent_source=has_independent_source,
        rejected_for_post_hoc_source=rejected_for_post_hoc_source,
        verdict=verdict,
    )


def null_reparameterization_fixture() -> WeakMeasurementTrajectory:
    """All D1 axes are standard-statistic or access-window transforms."""

    return WeakMeasurementTrajectory(
        name="null_standard_threshold",
        points=(
            TrajectoryPoint(0.0, 1.00, 0, 0, 0, 0, 0),
            TrajectoryPoint(1.0, 0.70, 0, 0, 0, 0, 0),
            TrajectoryPoint(2.0, 0.40, 1, 1, 1, 1, 1),
            TrajectoryPoint(3.0, 0.18, 2, 2, 2, 1, 2),
            TrajectoryPoint(4.0, 0.08, 3, 3, 3, 1, 3),
            TrajectoryPoint(5.0, 0.03, 3, 3, 3, 1, 3),
        ),
    )


def independent_branch_fixture_pair() -> tuple[WeakMeasurementTrajectory, WeakMeasurementTrajectory]:
    base = (
        (0.0, 1.00, 0, 0),
        (1.0, 0.70, 0, 0),
        (2.0, 0.40, 1, 1),
        (3.0, 0.18, 2, 2),
        (4.0, 0.08, 3, 3),
        (5.0, 0.03, 3, 3),
    )

    early_branch = WeakMeasurementTrajectory(
        name="independent_branch_early",
        points=tuple(
            TrajectoryPoint(time, coherence, redundancy, access, redundancy, branch, redundancy)
            for (time, coherence, redundancy, access), branch in zip(base, (0, 0, 1, 1, 1, 1))
        ),
    )
    late_branch = WeakMeasurementTrajectory(
        name="independent_branch_late",
        points=tuple(
            TrajectoryPoint(time, coherence, redundancy, access, redundancy, branch, redundancy)
            for (time, coherence, redundancy, access), branch in zip(base, (0, 0, 0, 0, 1, 1))
        ),
    )
    return early_branch, late_branch


def null_protocol() -> FinalityProtocol:
    return FinalityProtocol(
        coherence_epsilon=0.10,
        redundancy_threshold=2,
        access_threshold=2,
        holder_threshold=2,
        branch_threshold=1,
        reversal_threshold=2,
        holder_source=STANDARD,
        branch_source=STANDARD,
        reversal_source=STANDARD,
    )


def independent_branch_protocol() -> FinalityProtocol:
    return FinalityProtocol(
        coherence_epsilon=0.10,
        redundancy_threshold=2,
        access_threshold=2,
        holder_threshold=2,
        branch_threshold=1,
        reversal_threshold=2,
        holder_source=STANDARD,
        branch_source=INDEPENDENT,
        reversal_source=STANDARD,
    )


def post_hoc_branch_protocol() -> FinalityProtocol:
    protocol = independent_branch_protocol()
    return FinalityProtocol(
        coherence_epsilon=protocol.coherence_epsilon,
        redundancy_threshold=protocol.redundancy_threshold,
        access_threshold=protocol.access_threshold,
        holder_threshold=protocol.holder_threshold,
        branch_threshold=protocol.branch_threshold,
        reversal_threshold=protocol.reversal_threshold,
        holder_source=protocol.holder_source,
        branch_source=POST_HOC,
        reversal_source=protocol.reversal_source,
    )


def run_t90_analysis() -> T90Result:
    null = null_reparameterization_fixture()
    early, late = independent_branch_fixture_pair()

    null_times = compute_finality_times(null, null_protocol())
    null_verdict = classify_single_protocol(null_protocol())
    independent_pair = audit_pair(early, late, independent_branch_protocol())
    post_hoc_pair = audit_pair(early, late, post_hoc_branch_protocol())

    strongest_claim = (
        "A weak-measurement finalization time is null when every D1 coordinate "
        "is fixed by coherence, redundancy, access windows, or post hoc "
        "threshold choices. It becomes only a candidate discriminator when an "
        "independent pre-registered observable changes the TaF verdict while "
        "the standard monitored-record statistics are unchanged."
    )
    weakened_claim = (
        "The current TaF weak-measurement route does not yet predict new "
        "measurement dynamics. At most, T90 gives a required separation test "
        "for any future monitored-qubit or detector-trajectory proposal."
    )
    falsification_condition = (
        "T90 fails if a protocol with only standard coherence/redundancy/access "
        "statistics yields a TaF verdict that cannot be expressed as a "
        "thresholded standard-statistic rule, or if a post hoc branch label is "
        "accepted as an independent observable."
    )
    q1_update = (
        "Keep Q1 partially supported, but state the weak-measurement branch as "
        "an obstruction result: T12 is non-null only after a pre-registered "
        "branch, provenance, or reversal-cost observable produces a verdict "
        "change between trajectories with identical standard monitored-record "
        "statistics."
    )
    blocker = (
        "No concrete platform currently supplies a pre-registered branch-live "
        "or reversal-cost observable that is independent of coherence decay, "
        "fragment redundancy, and access thresholds."
    )
    recommended_next = (
        "Instantiate the independent-axis test on a superconducting-qubit "
        "homodyne trajectory or a trapped-ion/cavity-QED undo protocol; if no "
        "independent axis can be named before data analysis, demote T12."
    )

    return T90Result(
        null_times=null_times,
        null_verdict=null_verdict,
        independent_pair=independent_pair,
        post_hoc_pair=post_hoc_pair,
        strongest_claim=strongest_claim,
        weakened_claim=weakened_claim,
        falsification_condition=falsification_condition,
        q1_update=q1_update,
        blocker=blocker,
        recommended_next=recommended_next,
    )


def t90_result_to_dict(result: T90Result) -> dict[str, object]:
    return {
        "null_times": _times_to_dict(result.null_times),
        "null_verdict": result.null_verdict,
        "independent_pair": _pair_to_dict(result.independent_pair),
        "post_hoc_pair": _pair_to_dict(result.post_hoc_pair),
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def _same_time(left: float | None, right: float | None) -> bool:
    if left is None or right is None:
        return left is right
    return isclose(left, right)


def _times_to_dict(times: FinalityTimes) -> dict[str, float | None]:
    return {
        "decoherence_time": times.decoherence_time,
        "redundancy_time": times.redundancy_time,
        "access_time": times.access_time,
        "taf_finality_time": times.taf_finality_time,
    }


def _pair_to_dict(audit: PairAudit) -> dict[str, object]:
    return {
        "standard_timelines_equal": audit.standard_timelines_equal,
        "standard_verdict_equal": audit.standard_verdict_equal,
        "taf_verdict_changes": audit.taf_verdict_changes,
        "has_independent_source": audit.has_independent_source,
        "rejected_for_post_hoc_source": audit.rejected_for_post_hoc_source,
        "verdict": audit.verdict,
    }
