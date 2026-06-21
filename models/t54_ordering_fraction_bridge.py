"""T157: bridge T54 canonical colimits into the T156 ordering-fraction gate.

T156 left a sharp executable blocker: no actual T54 finality colimit both
reached the T126 scale floor and matched the declared flat 1+1 ordering-
fraction band. This module constructs T54 descent datums directly, completes
them with the T54 quotient-union algorithm, and only then applies the T126 and
T156 screens.

The positive case is deliberately modest. It is a hand-built finite control
showing that the T54 machinery can realize a six-event 1+1-like causet. It is
not a spacetime derivation, a sprinkling theorem, or a continuum-limit result.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    non_strict_relation,
)
from models.finality_descent_theorem import (
    AxisProfile,
    CompletionResult,
    EventIdentityMap,
    LocalEvent,
    ObserverDescentDatum,
    ObserverView,
    complete_observer_descent_datum,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    OrderingFractionTarget,
    audit_ordering_fraction_target,
    flat_1p1_interval_target,
)


Event = str
StrictPair = tuple[Event, Event]


@dataclass(frozen=True)
class T157Audit:
    name: str
    t54_classification: str
    t54_theorem_applies: bool
    t126_classification: str
    t126_filter_passed: bool
    event_count: int
    strict_pair_count: int | None
    ordering_fraction: Fraction | None
    target_name: str
    target_fraction: Fraction
    tolerance: Fraction
    absolute_gap: Fraction | None
    target_verdict: str
    verdict: str
    reason: str
    required_next: str


@dataclass(frozen=True)
class T157Result:
    target: OrderingFractionTarget
    audits: tuple[T157Audit, ...]
    t54_flat_candidate_reaches_t126_scale: bool
    t54_flat_candidate_matches_target_band: bool
    t54_product_grid_control_fails_target_band: bool
    t54_chain_control_blocked_before_target: bool
    previous_t156_open_blocker_removed: bool
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


NOT_CLAIMED = (
    "T157 does not estimate dimension, prove a faithful embedding, derive a "
    "Lorentzian metric, validate sprinkling behavior, or derive spacetime."
)


def flat_1p1_t54_datum() -> ObserverDescentDatum:
    """A six-event T54 datum whose completed order matches the T156 control."""

    coordinates = {
        "p0": (Fraction(134, 1000), Fraction(847, 1000)),
        "p1": (Fraction(764, 1000), Fraction(255, 1000)),
        "p2": (Fraction(495, 1000), Fraction(449, 1000)),
        "p3": (Fraction(652, 1000), Fraction(789, 1000)),
        "p4": (Fraction(94, 1000), Fraction(28, 1000)),
        "p5": (Fraction(836, 1000), Fraction(433, 1000)),
    }
    profiles = _rank_profiles(coordinates)
    strict = frozenset(
        (left, right)
        for left, left_profile in profiles.items()
        for right, right_profile in profiles.items()
        if left != right and left_profile.leq(right_profile)
    )
    return _datum_from_profiles(
        name="t157_flat_1p1_t54_colimit",
        description=(
            "Two agreeing observer views whose T54 quotient-union realizes a "
            "six-event flat-1+1 ordering-fraction control."
        ),
        profiles=profiles,
        strict_pairs=strict,
    )


def product_grid_2x3_t54_datum() -> ObserverDescentDatum:
    """A T54 version of the T156 over-ordered product-grid control."""

    profiles = {
        f"p{i}_{j}": AxisProfile(causal=i + 1, info=j + 1)
        for i in range(2)
        for j in range(3)
    }
    strict = _strict_from_profiles(profiles)
    return _datum_from_profiles(
        name="t157_product_grid_2x3_t54_colimit",
        description=(
            "Two agreeing observer views whose T54 quotient-union realizes the "
            "six-event product-grid control."
        ),
        profiles=profiles,
        strict_pairs=strict,
    )


def chain_6_t54_datum() -> ObserverDescentDatum:
    """A T54 control that is canonical but rejected by the T126 filter."""

    profiles = {f"c{i}": AxisProfile(causal=i + 1, info=i + 1) for i in range(6)}
    strict = _strict_from_profiles(profiles)
    return _datum_from_profiles(
        name="t157_chain_6_t54_colimit",
        description=(
            "Two agreeing observer views whose T54 quotient-union realizes a "
            "degenerate six-event chain."
        ),
        profiles=profiles,
        strict_pairs=strict,
    )


def canonical_t157_datums() -> tuple[ObserverDescentDatum, ...]:
    return (
        flat_1p1_t54_datum(),
        product_grid_2x3_t54_datum(),
        chain_6_t54_datum(),
    )


def run_t157_analysis() -> T157Result:
    target = flat_1p1_interval_target()
    audits = tuple(_audit_t54_datum(datum, target=target) for datum in canonical_t157_datums())
    by_name = {audit.name: audit for audit in audits}

    flat = by_name["t157_flat_1p1_t54_colimit"]
    grid = by_name["t157_product_grid_2x3_t54_colimit"]
    chain = by_name["t157_chain_6_t54_colimit"]

    flat_reaches_scale = flat.t54_theorem_applies and flat.t126_filter_passed
    flat_matches = flat.verdict == "t54_colimit_matches_ordering_fraction_control_only"
    grid_fails = grid.verdict == "t54_colimit_fails_ordering_fraction_target"
    chain_blocked = chain.verdict == "blocked_at_t126"

    return T157Result(
        target=target,
        audits=audits,
        t54_flat_candidate_reaches_t126_scale=flat_reaches_scale,
        t54_flat_candidate_matches_target_band=flat_matches,
        t54_product_grid_control_fails_target_band=grid_fails,
        t54_chain_control_blocked_before_target=chain_blocked,
        previous_t156_open_blocker_removed=flat_matches,
        strongest_claim=(
            "A hand-built but genuine T54 canonical quotient-union datum can "
            "reach the T126 scale floor and land inside the declared flat 1+1 "
            "ordering-fraction band: the six-event T157 control has ordering "
            "fraction 7/15."
        ),
        improved=(
            "T157 replaces the previous synthetic-only positive ordering-"
            "fraction control with a T54-completed colimit, while preserving "
            "negative T54 controls for the over-ordered product grid and the "
            "degenerate chain."
        ),
        weakened_or_falsified=(
            "The narrow T156 blocker 'no actual T54 finality colimit reaches "
            "scale and matches the declared ordering-fraction band' is now "
            "false. This does not upgrade S1, because the survivor is a "
            "constructed finite control and has not faced interval-abundance, "
            "locality, sprinkling, covariance, or continuum diagnostics."
        ),
        falsification_condition=(
            "T157 fails if the T54 completion does not reproduce the audited "
            "strict relation, if the same relation is not used by T126 and "
            "T156, if the product-grid and chain controls stop blocking the "
            "claimed interpretation, or if the positive finite control is "
            "described as spacetime evidence."
        ),
        s1_update=(
            "S1 remains open_formal_target. The scale/order-fraction blocker "
            "has been cleared for one constructed T54 control, but the result "
            "is still only a pre-diagnostic finite colimit control."
        ),
        claim_ledger_update=(
            "Add T157 to S1: a constructed six-event T54 canonical "
            "quotient-union colimit reaches T126 and matches the declared "
            "1+1 ordering-fraction band, while T54 product-grid and chain "
            "controls remain rejected or demoted. This removes the immediate "
            "T156 scale/order-fraction blocker without upgrading S1."
        ),
        open_blocker=(
            "No non-hand-built observer-local family, interval-abundance "
            "diagnostic, locality/sprinkling screen, embedding theorem, "
            "continuum-limit bridge, covariance result, or Lorentzian metric "
            "reconstruction exists for the T157 survivor."
        ),
        suggested_next=(
            "Subject the T157 flat control and nearby T54-generated families "
            "to a stronger interval-abundance or locality diagnostic; require "
            "failure to demote the survivor back to a calibration artifact."
        ),
        not_claimed=NOT_CLAIMED,
    )


def _rank_profiles(
    coordinates: dict[Event, tuple[Fraction, Fraction]],
) -> dict[Event, AxisProfile]:
    u_rank = {
        event: rank
        for rank, event in enumerate(
            sorted(coordinates, key=lambda item: coordinates[item][0]),
            start=1,
        )
    }
    v_rank = {
        event: rank
        for rank, event in enumerate(
            sorted(coordinates, key=lambda item: coordinates[item][1]),
            start=1,
        )
    }
    return {
        event: AxisProfile(causal=u_rank[event], info=v_rank[event])
        for event in coordinates
    }


def _strict_from_profiles(
    profiles: dict[Event, AxisProfile],
) -> frozenset[StrictPair]:
    return frozenset(
        (left, right)
        for left, left_profile in profiles.items()
        for right, right_profile in profiles.items()
        if left != right and left_profile.leq(right_profile)
    )


def _datum_from_profiles(
    *,
    name: str,
    description: str,
    profiles: dict[Event, AxisProfile],
    strict_pairs: frozenset[StrictPair],
) -> ObserverDescentDatum:
    observers = ("A", "B")
    events_by_observer = tuple(
        ObserverView(
            observer,
            tuple(
                _local_event(
                    observer=observer,
                    event=event,
                    profile=profiles[event],
                    predecessors=frozenset(
                        left for left, right in strict_pairs if right == event
                    ),
                )
                for event in sorted(profiles)
            ),
        )
        for observer in observers
    )
    identity_maps = tuple(
        EventIdentityMap(observer=observer, local_event=event, global_event=event)
        for observer in observers
        for event in sorted(profiles)
    )
    return ObserverDescentDatum(
        name=name,
        description=description,
        observer_views=events_by_observer,
        identity_maps=identity_maps,
        overlap_witnesses=frozenset(profiles),
        expected_classification="canonical",
    )


def _local_event(
    *,
    observer: str,
    event: Event,
    profile: AxisProfile,
    predecessors: frozenset[Event],
) -> LocalEvent:
    return LocalEvent(
        observer=observer,
        name=event,
        source_records=frozenset({f"raw_{event}"} | {f"locked_{p}" for p in predecessors}),
        target_records=frozenset({f"locked_{event}"}),
        profile=profile,
    )


def _audit_t54_datum(
    datum: ObserverDescentDatum,
    *,
    target: OrderingFractionTarget,
) -> T157Audit:
    completion = complete_observer_descent_datum(datum)
    t126_datum = _completion_to_t126_datum(completion)
    t126_audit = audit_finality_colimit_causet(t126_datum)
    t156_audit = audit_ordering_fraction_target(t126_datum, target=target)

    if not completion.theorem_applies:
        verdict = "blocked_at_t54"
        reason = completion.evidence
        required_next = "Repair T54 descent data before causal-set screening."
    elif not t126_audit.manifold_filter_passed:
        verdict = "blocked_at_t126"
        reason = t126_audit.reason
        required_next = t126_audit.required_next
    elif t156_audit.verdict == "passes_ordering_fraction_control_only":
        verdict = "t54_colimit_matches_ordering_fraction_control_only"
        reason = (
            "The T54-completed colimit reaches the T126 filter and its "
            "ordering fraction lies inside the declared finite 1+1 band."
        )
        required_next = t156_audit.required_next
    else:
        verdict = "t54_colimit_fails_ordering_fraction_target"
        reason = t156_audit.reason
        required_next = t156_audit.required_next

    diagnostics = t126_audit.diagnostics
    return T157Audit(
        name=datum.name,
        t54_classification=completion.classification,
        t54_theorem_applies=completion.theorem_applies,
        t126_classification=t126_audit.classification,
        t126_filter_passed=t126_audit.manifold_filter_passed,
        event_count=diagnostics.event_count if diagnostics is not None else len(t126_datum.events),
        strict_pair_count=t156_audit.strict_pair_count,
        ordering_fraction=t156_audit.ordering_fraction,
        target_name=target.name,
        target_fraction=target.target_fraction,
        tolerance=target.tolerance,
        absolute_gap=t156_audit.absolute_gap,
        target_verdict=t156_audit.target_verdict,
        verdict=verdict,
        reason=reason,
        required_next=required_next,
    )


def _completion_to_t126_datum(completion: CompletionResult) -> FinalityColimitCausetDatum:
    events = frozenset(event.name for event in completion.global_events)
    relation = (
        frozenset(completion.partial_order.order_pairs)
        if completion.partial_order is not None
        else non_strict_relation(events, frozenset())
    )
    descent_gate_passed = completion.theorem_applies and completion.partial_order is not None
    canonical_colimit = completion.classification == "canonical" and descent_gate_passed
    return FinalityColimitCausetDatum(
        name=completion.datum_name,
        events=events,
        relation=relation,
        descent_gate_passed=descent_gate_passed,
        canonical_colimit=canonical_colimit,
        phantom_gap_resolved=canonical_colimit,
        observer_only_gap_changes_strict_order=False,
        source="T157 T54 quotient-union completion",
    )


def t157_result_to_dict(result: T157Result) -> dict[str, Any]:
    return {
        "target": {
            "name": result.target.name,
            "target_fraction": _fraction_to_dict(result.target.target_fraction),
            "tolerance": _fraction_to_dict(result.target.tolerance),
            "basis": result.target.basis,
        },
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "t54_flat_candidate_reaches_t126_scale": (
            result.t54_flat_candidate_reaches_t126_scale
        ),
        "t54_flat_candidate_matches_target_band": (
            result.t54_flat_candidate_matches_target_band
        ),
        "t54_product_grid_control_fails_target_band": (
            result.t54_product_grid_control_fails_target_band
        ),
        "t54_chain_control_blocked_before_target": (
            result.t54_chain_control_blocked_before_target
        ),
        "previous_t156_open_blocker_removed": result.previous_t156_open_blocker_removed,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_falsified": result.weakened_or_falsified,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _audit_to_dict(audit: T157Audit) -> dict[str, Any]:
    return {
        "name": audit.name,
        "t54_classification": audit.t54_classification,
        "t54_theorem_applies": audit.t54_theorem_applies,
        "t126_classification": audit.t126_classification,
        "t126_filter_passed": audit.t126_filter_passed,
        "event_count": audit.event_count,
        "strict_pair_count": audit.strict_pair_count,
        "ordering_fraction": (
            _fraction_to_dict(audit.ordering_fraction)
            if audit.ordering_fraction is not None
            else None
        ),
        "target_name": audit.target_name,
        "target_fraction": _fraction_to_dict(audit.target_fraction),
        "tolerance": _fraction_to_dict(audit.tolerance),
        "absolute_gap": (
            _fraction_to_dict(audit.absolute_gap)
            if audit.absolute_gap is not None
            else None
        ),
        "target_verdict": audit.target_verdict,
        "verdict": audit.verdict,
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t157_result_to_dict(run_t157_analysis()), indent=2))
