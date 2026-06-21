"""T94: priority audit between detector provenance and weak measurement.

This model does not add physics. It codifies the current evidence state after
T83/T85/T86/T91/T93 so the roadmap can demote weak measurement honestly until
it names a real independent axis.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RouteState:
    route: str
    has_real_platform: bool
    has_preregistered_raw_log_protocol: bool
    survives_current_null_criterion: bool
    has_independent_axis_named_before_analysis: bool
    has_source_anchored_candidate: bool
    isolated_positive_witness_exists: bool
    empirical_deployment_present: bool
    key_blocker: str


@dataclass(frozen=True)
class RoutePriorityAudit:
    preferred_route: str
    weak_measurement_status: str
    detector_status: str
    justification: str


@dataclass(frozen=True)
class T94Result:
    detector_state: RouteState
    weak_measurement_state: RouteState
    audit: RoutePriorityAudit
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    blocker: str
    recommended_next: str


def detector_provenance_state() -> RouteState:
    return RouteState(
        route="detector_provenance",
        has_real_platform=True,
        has_preregistered_raw_log_protocol=True,
        survives_current_null_criterion=True,
        has_independent_axis_named_before_analysis=True,
        has_source_anchored_candidate=True,
        isolated_positive_witness_exists=True,
        empirical_deployment_present=False,
        key_blocker=(
            "no actual T78-style deployment with published event-level raw logs is present"
        ),
    )


def weak_measurement_state() -> RouteState:
    return RouteState(
        route="weak_measurement",
        has_real_platform=False,
        has_preregistered_raw_log_protocol=False,
        survives_current_null_criterion=False,
        has_independent_axis_named_before_analysis=False,
        has_source_anchored_candidate=False,
        isolated_positive_witness_exists=False,
        empirical_deployment_present=False,
        key_blocker=(
            "no named platform supplies a pre-registered independent branch, provenance, "
            "or undo-cost axis distinct from the standard monitored record"
        ),
    )


def audit_priority(
    detector: RouteState,
    weak_measurement: RouteState,
) -> RoutePriorityAudit:
    if (
        detector.survives_current_null_criterion
        and detector.has_preregistered_raw_log_protocol
        and detector.has_source_anchored_candidate
        and not weak_measurement.has_independent_axis_named_before_analysis
    ):
        return RoutePriorityAudit(
            preferred_route="detector_provenance",
            weak_measurement_status="demoted_below_detector_provenance",
            detector_status="active_but_not_empirically_upgraded",
            justification=(
                "Detector provenance retains a source-anchored, pre-registered, "
                "raw-log admissibility route that survives current null tests, while "
                "weak measurement has no named independent axis on a real platform."
            ),
        )

    if weak_measurement.has_independent_axis_named_before_analysis:
        return RoutePriorityAudit(
            preferred_route="weak_measurement",
            weak_measurement_status="reinstated_candidate",
            detector_status="still_active",
            justification=(
                "Weak measurement supplied the missing independent axis and can be "
                "compared directly against detector provenance again."
            ),
        )

    return RoutePriorityAudit(
        preferred_route="undecided",
        weak_measurement_status="blocked",
        detector_status="blocked",
        justification="Neither route currently clears its own admission gate.",
    )


def run_t94_analysis() -> T94Result:
    detector = detector_provenance_state()
    weak = weak_measurement_state()
    audit = audit_priority(detector, weak)

    strongest_claim = (
        "Weak measurement should be demoted below detector provenance in the "
        "active Q1 roadmap. The detector route still has a source-anchored, "
        "pre-registered raw-log path that survives the current null criteria; "
        "the weak-measurement route has no real platform with an independent "
        "branch, provenance, or undo-cost axis."
    )
    improved = (
        "T94 converts repeated prose demotion warnings into an explicit route-"
        "selection rule. Future runs can stop reopening null weak-measurement "
        "platforms unless they first satisfy the independent-axis gate."
    )
    weakened = (
        "This weakens T12 strategically, not just locally. Weak measurement is "
        "no longer the default lead experimental route on the basis of promise "
        "alone."
    )
    falsification_condition = (
        "T94 fails if a concrete weak-measurement platform names a pre-registered "
        "independent branch/provenance/undo-cost observable, not derived from the "
        "standard monitored record and not postselected, and that axis changes the "
        "TaF verdict while standard monitored statistics stay fixed."
    )
    q1_update = (
        "Keep Q1 partially supported, but demote T12 below detector provenance in "
        "the active roadmap until a monitored weak-measurement platform clears T90 "
        "and T93 with a real independent axis."
    )
    blocker = (
        "The repo still lacks the single object weak measurement needs most: a "
        "named platform with a pre-registered independent axis that survives same-"
        "record and postselection collapse."
    )
    recommended_next = (
        "Advance detector provenance toward one real T78-style deployment, or "
        "reinstate weak measurement only after naming a concrete independent-axis "
        "platform with a raw-log schema."
    )

    return T94Result(
        detector_state=detector,
        weak_measurement_state=weak,
        audit=audit,
        strongest_claim=strongest_claim,
        improved=improved,
        weakened=weakened,
        falsification_condition=falsification_condition,
        q1_update=q1_update,
        blocker=blocker,
        recommended_next=recommended_next,
    )


def t94_result_to_dict(result: T94Result) -> dict[str, object]:
    return {
        "detector_state": result.detector_state.__dict__,
        "weak_measurement_state": result.weak_measurement_state.__dict__,
        "audit": result.audit.__dict__,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }
