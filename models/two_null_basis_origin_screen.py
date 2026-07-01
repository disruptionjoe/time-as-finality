"""T385: origin-principle screen for the two-null compatibility basis.

T384 left one central open object: why exactly two primitive null
compatibility-signal directions? This screen compares small origin principles
that could supply that basis without importing Minkowski spacetime or a global
clock first.

The honest result is deliberately modest. A minimal local round-trip handshake
is the unique survivor among the declared principles, but that does not derive
the handshake premise from compatibility alone. It moves the live object from
``basis_origin`` to ``handshake_origin``.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OriginPrinciple:
    origin_id: str
    imports_global_time: bool
    local_coupling: bool
    primitive_signal_directions: int
    directional_signal_geometry: bool
    round_trip_closure: bool
    nonnegative_source_counts: bool
    reciprocal_calibration: bool
    overcomplete: bool
    imports_acknowledgment_premise: bool
    description: str


@dataclass(frozen=True)
class OriginCriterion:
    criterion_id: str
    passes: bool
    reason: str


@dataclass(frozen=True)
class OriginVerdict:
    origin_id: str
    status: str
    classification: str
    passes: bool
    imports_acknowledgment_premise: bool
    criteria: tuple[OriginCriterion, ...]
    reason: str


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T385Result:
    minimal_handshake_unique_survivor: bool
    absolute_clock_rejected: bool
    scalar_source_action_rejected: bool
    one_way_signal_rejected: bool
    overcomplete_broadcast_demoted: bool
    signed_cancellation_rejected: bool
    gauge_relabel_partial: bool
    two_null_basis_derived_from_compatibility_alone: bool
    two_null_basis_minimally_motivated_by_handshake: bool
    handshake_premise_still_open: bool
    surviving_origin_ids: tuple[str, ...]
    partial_origin_ids: tuple[str, ...]
    rejected_origin_ids: tuple[str, ...]
    verdicts: tuple[OriginVerdict, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str
    next_open_object: str


def origin_principles() -> tuple[OriginPrinciple, ...]:
    return (
        OriginPrinciple(
            origin_id="absolute_clock_origin",
            imports_global_time=True,
            local_coupling=False,
            primitive_signal_directions=0,
            directional_signal_geometry=False,
            round_trip_closure=False,
            nonnegative_source_counts=True,
            reciprocal_calibration=False,
            overcomplete=False,
            imports_acknowledgment_premise=False,
            description="basis is replaced by an external universal clock",
        ),
        OriginPrinciple(
            origin_id="scalar_source_action_origin",
            imports_global_time=False,
            local_coupling=True,
            primitive_signal_directions=0,
            directional_signal_geometry=False,
            round_trip_closure=False,
            nonnegative_source_counts=True,
            reciprocal_calibration=False,
            overcomplete=False,
            imports_acknowledgment_premise=False,
            description="source action contributes one local scalar with no signal direction",
        ),
        OriginPrinciple(
            origin_id="one_way_signal_origin",
            imports_global_time=False,
            local_coupling=True,
            primitive_signal_directions=1,
            directional_signal_geometry=True,
            round_trip_closure=False,
            nonnegative_source_counts=True,
            reciprocal_calibration=False,
            overcomplete=False,
            imports_acknowledgment_premise=False,
            description="one primitive compatibility signal direction only",
        ),
        OriginPrinciple(
            origin_id="minimal_handshake_origin",
            imports_global_time=False,
            local_coupling=True,
            primitive_signal_directions=2,
            directional_signal_geometry=True,
            round_trip_closure=True,
            nonnegative_source_counts=True,
            reciprocal_calibration=True,
            overcomplete=False,
            imports_acknowledgment_premise=True,
            description="minimal request/return or send/ack round-trip interface",
        ),
        OriginPrinciple(
            origin_id="overcomplete_broadcast_origin",
            imports_global_time=False,
            local_coupling=True,
            primitive_signal_directions=3,
            directional_signal_geometry=True,
            round_trip_closure=True,
            nonnegative_source_counts=True,
            reciprocal_calibration=False,
            overcomplete=True,
            imports_acknowledgment_premise=True,
            description="broadcast adapter with more primitive directions than a 1+1 null basis",
        ),
        OriginPrinciple(
            origin_id="signed_cancellation_origin",
            imports_global_time=False,
            local_coupling=True,
            primitive_signal_directions=2,
            directional_signal_geometry=True,
            round_trip_closure=True,
            nonnegative_source_counts=False,
            reciprocal_calibration=True,
            overcomplete=False,
            imports_acknowledgment_premise=True,
            description="two directions obtained through signed cancellation of source counts",
        ),
        OriginPrinciple(
            origin_id="gauge_relabel_origin",
            imports_global_time=False,
            local_coupling=True,
            primitive_signal_directions=0,
            directional_signal_geometry=False,
            round_trip_closure=False,
            nonnegative_source_counts=True,
            reciprocal_calibration=False,
            overcomplete=False,
            imports_acknowledgment_premise=False,
            description="local label symmetry that preserves identity but supplies no calibrated signal basis",
        ),
    )


def evaluate_origin(principle: OriginPrinciple) -> OriginVerdict:
    criteria = (
        OriginCriterion(
            "no_global_time_import",
            not principle.imports_global_time,
            "origin must not solve relativity by supplying an absolute clock",
        ),
        OriginCriterion(
            "local_substrate_coupling",
            principle.local_coupling,
            "origin should touch local compatibility relations",
        ),
        OriginCriterion(
            "directional_signal_geometry",
            principle.directional_signal_geometry,
            "origin must supply signal directions, not only scalar or relabel data",
        ),
        OriginCriterion(
            "round_trip_closure",
            principle.round_trip_closure,
            "observer comparison needs a closed send/return calibration loop",
        ),
        OriginCriterion(
            "exactly_two_primitive_directions",
            principle.primitive_signal_directions == 2,
            "the T380-T384 ladder needs exactly two primitive null directions",
        ),
        OriginCriterion(
            "nonnegative_source_counts",
            principle.nonnegative_source_counts,
            "source compatibility directions cannot require negative count primitives",
        ),
        OriginCriterion(
            "reciprocal_calibration",
            principle.reciprocal_calibration,
            "the origin must support reciprocal calibration rather than one-way readout",
        ),
        OriginCriterion(
            "minimal_not_overcomplete",
            not principle.overcomplete and principle.primitive_signal_directions == 2,
            "extra primitive directions must be absent or factor through the two-direction basis",
        ),
    )
    passes = all(criterion.passes for criterion in criteria)

    if passes:
        status = "minimal_handshake_survivor"
        classification = "survivor"
        reason = (
            "a local request/return handshake supplies exactly two primitive directions, "
            "round-trip closure, reciprocal calibration, and no global clock"
        )
    elif principle.imports_global_time:
        status = "rejected_global_time_import"
        classification = "rejected"
        reason = "absolute clock origin imports the observer time structure the model should render"
    elif principle.origin_id == "gauge_relabel_origin":
        status = "partial_relabel_not_origin"
        classification = "partial"
        reason = "local relabeling may preserve substrate identity but does not originate calibrated signal rays"
    elif not principle.directional_signal_geometry:
        status = "rejected_no_signal_geometry"
        classification = "rejected"
        reason = "scalar coupling has no primitive direction geometry for null-channel relativity"
    elif principle.primitive_signal_directions < 2:
        status = "rejected_undercomplete_one_way"
        classification = "rejected"
        reason = "one-way signal direction cannot close a reciprocal observer comparison"
    elif not principle.round_trip_closure:
        status = "rejected_no_round_trip_closure"
        classification = "rejected"
        reason = "without round-trip closure, the two sides cannot recover an invariant interval"
    elif not principle.nonnegative_source_counts:
        status = "rejected_signed_source_counts"
        classification = "rejected"
        reason = "signed cancellation uses negative primitive counts unavailable to source compatibility rows"
    elif principle.overcomplete or principle.primitive_signal_directions > 2:
        status = "demoted_overcomplete"
        classification = "demoted"
        reason = "extra primitive directions overconstrain the null basis or reduce to redundant channels"
    elif not principle.reciprocal_calibration:
        status = "partial_no_reciprocal_calibration"
        classification = "partial"
        reason = "local direction data is present but does not calibrate reciprocal observers"
    else:
        status = "failed_origin_screen"
        classification = "rejected"
        reason = "principle misses at least one declared origin requirement"

    return OriginVerdict(
        origin_id=principle.origin_id,
        status=status,
        classification=classification,
        passes=passes,
        imports_acknowledgment_premise=principle.imports_acknowledgment_premise,
        criteria=criteria,
        reason=reason,
    )


def evaluate_origins() -> tuple[OriginVerdict, ...]:
    return tuple(evaluate_origin(principle) for principle in origin_principles())


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            comparator_id="compatibility_alone_derivation",
            status="not_earned",
            absorbs=True,
            reason=(
                "the survivor relies on the added premise that compatibility requires "
                "bidirectional acknowledgment or round-trip calibration"
            ),
        ),
        ComparatorVerdict(
            comparator_id="minimal_handshake_origin",
            status="supported_as_minimal_adapter",
            absorbs=False,
            reason=(
                "among declared origins, a local round-trip handshake is the only one "
                "that cleanly supplies the two primitive null directions"
            ),
        ),
        ComparatorVerdict(
            comparator_id="handshake_premise_origin",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "the screen does not derive why compatibility must be a bidirectional "
                "send/return relation rather than a scalar or one-way relation"
            ),
        ),
        ComparatorVerdict(
            comparator_id="scalar_or_clock_shortcut",
            status="rejected",
            absorbs=False,
            reason="global clock and scalar source-action origins fail the declared substrate criteria",
        ),
        ComparatorVerdict(
            comparator_id="catalog_completeness",
            status="still_absorbs",
            absorbs=True,
            reason="the screen covers the targeted origin principles, not every possible origin",
        ),
    )


def run_t385_analysis() -> T385Result:
    verdicts = evaluate_origins()
    by_id = {verdict.origin_id: verdict for verdict in verdicts}
    survivors = tuple(verdict.origin_id for verdict in verdicts if verdict.classification == "survivor")
    partials = tuple(verdict.origin_id for verdict in verdicts if verdict.classification == "partial")
    rejected = tuple(verdict.origin_id for verdict in verdicts if verdict.classification == "rejected")
    return T385Result(
        minimal_handshake_unique_survivor=survivors == ("minimal_handshake_origin",),
        absolute_clock_rejected=(
            by_id["absolute_clock_origin"].status == "rejected_global_time_import"
        ),
        scalar_source_action_rejected=(
            by_id["scalar_source_action_origin"].status == "rejected_no_signal_geometry"
        ),
        one_way_signal_rejected=(
            by_id["one_way_signal_origin"].status == "rejected_undercomplete_one_way"
        ),
        overcomplete_broadcast_demoted=(
            by_id["overcomplete_broadcast_origin"].status == "demoted_overcomplete"
        ),
        signed_cancellation_rejected=(
            by_id["signed_cancellation_origin"].status == "rejected_signed_source_counts"
        ),
        gauge_relabel_partial=(
            by_id["gauge_relabel_origin"].status == "partial_relabel_not_origin"
        ),
        two_null_basis_derived_from_compatibility_alone=False,
        two_null_basis_minimally_motivated_by_handshake=True,
        handshake_premise_still_open=True,
        surviving_origin_ids=survivors,
        partial_origin_ids=partials,
        rejected_origin_ids=rejected,
        verdicts=verdicts,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict=(
            "two_null_basis_minimally_motivated_by_round_trip_handshake_not_derived_from_compatibility_alone"
        ),
        strongest_claim=(
            "A compatibility-only scalar, global clock, or one-way origin fails. A minimal "
            "local round-trip handshake uniquely motivates exactly two primitive null "
            "compatibility-signal directions within the declared screen, but the need for "
            "bidirectional acknowledgment is still an imported premise, so the basis is "
            "not derived from compatibility alone."
        ),
        claim_ledger_update=(
            "Register T385 as an origin-principle screen: basis_origin is sharpened into "
            "handshake_origin. The two-null basis is minimally motivated by round-trip "
            "compatibility, not derived from compatibility alone."
        ),
        next_open_object="derive_or_falsify_bidirectional_handshake_origin",
    )


def t385_result_to_dict(result: T385Result) -> dict[str, object]:
    return {
        "minimal_handshake_unique_survivor": result.minimal_handshake_unique_survivor,
        "absolute_clock_rejected": result.absolute_clock_rejected,
        "scalar_source_action_rejected": result.scalar_source_action_rejected,
        "one_way_signal_rejected": result.one_way_signal_rejected,
        "overcomplete_broadcast_demoted": result.overcomplete_broadcast_demoted,
        "signed_cancellation_rejected": result.signed_cancellation_rejected,
        "gauge_relabel_partial": result.gauge_relabel_partial,
        "two_null_basis_derived_from_compatibility_alone": (
            result.two_null_basis_derived_from_compatibility_alone
        ),
        "two_null_basis_minimally_motivated_by_handshake": (
            result.two_null_basis_minimally_motivated_by_handshake
        ),
        "handshake_premise_still_open": result.handshake_premise_still_open,
        "surviving_origin_ids": list(result.surviving_origin_ids),
        "partial_origin_ids": list(result.partial_origin_ids),
        "rejected_origin_ids": list(result.rejected_origin_ids),
        "verdicts": [
            {
                "origin_id": verdict.origin_id,
                "status": verdict.status,
                "classification": verdict.classification,
                "passes": verdict.passes,
                "imports_acknowledgment_premise": verdict.imports_acknowledgment_premise,
                "criteria": [
                    {
                        "criterion_id": criterion.criterion_id,
                        "passes": criterion.passes,
                        "reason": criterion.reason,
                    }
                    for criterion in verdict.criteria
                ],
                "reason": verdict.reason,
            }
            for verdict in result.verdicts
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
        "next_open_object": result.next_open_object,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t385_result_to_dict(run_t385_analysis()), indent=2))
