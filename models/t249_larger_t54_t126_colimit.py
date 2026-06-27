"""T249: larger T54-style canonical colimit for the T126 screen.

T154 showed that the actual T51/T52 canonical colimits reach T126 only as
three- and four-event causal-set candidates, then stop at insufficient scale.
This module builds the next necessary control: a nine-event observer-descent
datum whose T54 quotient-union order is the 3x3 product order already used by
T126 as a small filter-pass control.

The result is intentionally modest. Passing T126 here is only a finite
necessary-condition pass, not a spacetime, embedding, or continuum claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    CausetAudit,
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


GridPoint = tuple[int, int]


@dataclass(frozen=True)
class LocalGapSummary:
    observer: str
    local_event_count: int
    ambient_pair_count: int
    local_pair_count: int
    gap_count: int
    local_is_suborder: bool


@dataclass(frozen=True)
class T249Result:
    completion: CompletionResult
    local_gap_summaries: tuple[LocalGapSummary, ...]
    t126_audit: CausetAudit
    product_order_exact: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


PATCHES: tuple[tuple[str, tuple[GridPoint, ...]], ...] = (
    ("NW", ((0, 0), (0, 1), (1, 0), (1, 1))),
    ("NE", ((0, 1), (0, 2), (1, 1), (1, 2))),
    ("SW", ((1, 0), (1, 1), (2, 0), (2, 1))),
    ("SE", ((1, 1), (1, 2), (2, 1), (2, 2))),
)


def build_grid_observer_descent_datum() -> ObserverDescentDatum:
    """Build four overlapping observer patches over a 3x3 product order."""

    views = tuple(
        ObserverView(
            name=observer,
            events=tuple(_grid_event(observer, point) for point in points),
        )
        for observer, points in PATCHES
    )
    identity_maps = tuple(
        EventIdentityMap(view.name, event.name, event.name)
        for view in views
        for event in view.events
    )
    overlap_witnesses = frozenset(_event_name(point) for point in _grid_points())
    return ObserverDescentDatum(
        name="T249_larger_grid_colimit",
        description=(
            "Four overlapping 2x2 observer patches reconstruct a nine-event "
            "3x3 product-order finality colimit."
        ),
        observer_views=views,
        identity_maps=identity_maps,
        overlap_witnesses=overlap_witnesses,
        expected_classification="canonical",
    )


def run_t249_analysis() -> T249Result:
    datum = build_grid_observer_descent_datum()
    completion = complete_observer_descent_datum(datum)
    gap_summaries = _local_gap_summaries(datum, completion)
    product_exact = _completion_strict_pairs(completion) == _product_order_pairs()
    t126_audit = audit_finality_colimit_causet(
        _completion_to_t126_datum(completion, gap_summaries)
    )

    return T249Result(
        completion=completion,
        local_gap_summaries=gap_summaries,
        t126_audit=t126_audit,
        product_order_exact=product_exact,
        strongest_claim=(
            "A nine-event T54-native observer descent datum can reconstruct the "
            "3x3 product order and reach T126 above the minimum scale floor, "
            "where it receives only the verdict passes_filter_only."
        ),
        improved=(
            "This closes the T154 immediate blocker at the finite-control level: "
            "the larger T126 grid is no longer merely a synthetic causet control, "
            "because it now has an explicit T54 observer-descent source."
        ),
        weakened=(
            "The result weakens any broad S1 reading. Clearing the selected "
            "finite T126 filter is not an embedding theorem and does not supply "
            "sprinkling, locality, covariance, metric, or continuum evidence."
        ),
        falsification_condition=(
            "T249 fails if the quotient-union order differs from the 3x3 product "
            "order, if any observer-local patch has a non-suborder gap relative "
            "to the ambient order, or if T126 is read as stronger than a finite "
            "necessary-condition filter."
        ),
        s1_update=(
            "S1 remains open_formal_target. The finite bridge now has a larger "
            "T54-native control, but no continuum-facing claim follows."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T249 alone. If recorded later, "
            "the safe wording is: a nine-event T54-native grid colimit passes "
            "the current T126 finite filter only."
        ),
        open_blocker=(
            "No named causal-set dimension estimator, random sprinkling test, "
            "locality diagnostic, faithful embedding theorem, or continuum-limit "
            "argument has been applied to this T54-native witness."
        ),
        suggested_next=(
            "Compare this grid-derived finality colimit against a declared "
            "Myrheim-Meyer, sprinkling, or locality diagnostic, with tolerance "
            "chosen before seeing the verdict."
        ),
    )


def _grid_points() -> tuple[GridPoint, ...]:
    return tuple((i, j) for i in range(3) for j in range(3))


def _event_name(point: GridPoint) -> str:
    i, j = point
    return f"p{i}{j}"


def _record_name(point: GridPoint) -> str:
    i, j = point
    return f"r{i}{j}"


def _source_records(point: GridPoint) -> frozenset[str]:
    i, j = point
    records: set[str] = set()
    if i == 0 and j == 0:
        records.add("raw_origin")
    if i > 0:
        records.add(_record_name((i - 1, j)))
    if j > 0:
        records.add(_record_name((i, j - 1)))
    return frozenset(records)


def _grid_event(observer: str, point: GridPoint) -> LocalEvent:
    i, j = point
    return LocalEvent(
        observer=observer,
        name=_event_name(point),
        source_records=_source_records(point),
        target_records=frozenset({_record_name(point)}),
        profile=AxisProfile(causal=i, info=j),
    )


def _completion_strict_pairs(completion: CompletionResult) -> frozenset[tuple[str, str]]:
    if completion.partial_order is None:
        return frozenset()
    return frozenset(
        (left, right)
        for left, right in completion.partial_order.order_pairs
        if left != right
    )


def _product_order_pairs() -> frozenset[tuple[str, str]]:
    return frozenset(
        (_event_name((i, j)), _event_name((k, l)))
        for (i, j), (k, l) in product(_grid_points(), repeat=2)
        if (i, j) != (k, l) and i <= k and j <= l
    )


def _local_strict_pairs(view: ObserverView) -> frozenset[tuple[str, str]]:
    events = frozenset(event.name for event in view.events)
    generators = frozenset(
        (left.name, right.name)
        for left, right in product(view.events, repeat=2)
        if left.name != right.name
        and left.target_records
        and left.target_records <= right.source_records
    )
    relation = non_strict_relation(events, generators)
    return frozenset((left, right) for left, right in relation if left != right)


def _local_gap_summaries(
    datum: ObserverDescentDatum,
    completion: CompletionResult,
) -> tuple[LocalGapSummary, ...]:
    ambient = _completion_strict_pairs(completion)
    summaries: list[LocalGapSummary] = []
    for view in datum.observer_views:
        names = frozenset(event.name for event in view.events)
        ambient_restricted = frozenset(
            (left, right)
            for left, right in ambient
            if left in names and right in names
        )
        local = _local_strict_pairs(view)
        summaries.append(
            LocalGapSummary(
                observer=view.name,
                local_event_count=len(names),
                ambient_pair_count=len(ambient_restricted),
                local_pair_count=len(local),
                gap_count=len(ambient_restricted - local),
                local_is_suborder=local <= ambient_restricted,
            )
        )
    return tuple(summaries)


def _completion_to_t126_datum(
    completion: CompletionResult,
    gap_summaries: tuple[LocalGapSummary, ...],
) -> FinalityColimitCausetDatum:
    events = frozenset(event.name for event in completion.global_events)
    relation = (
        frozenset(completion.partial_order.order_pairs)
        if completion.partial_order is not None
        else non_strict_relation(events, frozenset())
    )
    local_gate_passed = all(
        summary.local_is_suborder and summary.gap_count == 0
        for summary in gap_summaries
    )
    return FinalityColimitCausetDatum(
        name="t249_larger_grid_t54_colimit",
        events=events,
        relation=relation,
        descent_gate_passed=completion.theorem_applies,
        canonical_colimit=completion.classification == "canonical",
        phantom_gap_resolved=local_gate_passed,
        observer_only_gap_changes_strict_order=not local_gate_passed,
        source="T249 T54-native 3x3 grid observer descent datum",
    )


def t249_result_to_dict(result: T249Result) -> dict[str, Any]:
    return {
        "completion": {
            "datum_name": result.completion.datum_name,
            "classification": result.completion.classification,
            "theorem_applies": result.completion.theorem_applies,
            "condition_failures": list(result.completion.condition_failures),
            "global_event_count": len(result.completion.global_events),
            "strict_pair_count": len(_completion_strict_pairs(result.completion)),
            "product_order_exact": result.product_order_exact,
        },
        "local_gap_summaries": [
            {
                "observer": summary.observer,
                "local_event_count": summary.local_event_count,
                "ambient_pair_count": summary.ambient_pair_count,
                "local_pair_count": summary.local_pair_count,
                "gap_count": summary.gap_count,
                "local_is_suborder": summary.local_is_suborder,
            }
            for summary in result.local_gap_summaries
        ],
        "t126_audit": _audit_to_dict(result.t126_audit),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


def _audit_to_dict(audit: CausetAudit) -> dict[str, Any]:
    diagnostics = audit.diagnostics
    return {
        "name": audit.name,
        "classification": audit.classification,
        "causal_set_candidate": audit.causal_set_candidate,
        "manifold_filter_passed": audit.manifold_filter_passed,
        "reason": audit.reason,
        "required_next": audit.required_next,
        "not_claimed": audit.not_claimed,
        "diagnostics": None
        if diagnostics is None
        else {
            "event_count": diagnostics.event_count,
            "strict_pair_count": diagnostics.strict_pair_count,
            "comparable_fraction": _fraction_to_dict(diagnostics.comparable_fraction),
            "cover_relation_count": diagnostics.cover_relation_count,
            "link_density": _fraction_to_dict(diagnostics.link_density),
            "height": diagnostics.height,
            "width": diagnostics.width,
            "rank_profile": list(diagnostics.rank_profile),
            "interval_counts_by_size": [
                list(item) for item in diagnostics.interval_counts_by_size
            ],
            "largest_cover_hub_fraction": _fraction_to_dict(
                diagnostics.largest_cover_hub_fraction
            ),
            "profile_spread_obstruction": diagnostics.profile_spread_obstruction,
        },
    }


def _fraction_to_dict(value: Fraction) -> dict[str, Any]:
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "float": float(value),
    }
