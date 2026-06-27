"""T256-T263: structural diagnostics around the T252 ordinal witness.

T252-T255 established a selected nine-event ordinal witness that clears the
current finite screens and has a mixed one-transposition neighborhood. This
module keeps the claim boundary fixed and asks what the nearby shapes look like:
interval profiles, cover/locality summaries, mutation-positive cases, mutation
obstructions, outside-band cases, and the next route-selection gate.

These are finite diagnostic tasks only. They do not upgrade S1 and do not turn a
selected witness into a typical or continuum-facing result.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from typing import Any, Iterable

from models.finality_colimit_causal_set_embeddability import (
    CausetAudit,
    CausetDiagnostics,
    audit_finality_colimit_causet,
)
from models.myrheim_meyer_ordering_fraction_screen import flat_1p1_interval_target
from models.t249_larger_t54_t126_colimit import run_t249_analysis
from models.t252_t255_nine_event_ordinal_controls import (
    NINE_EVENT_ORDINAL_PERMUTATION,
    _deletion_datum,
    _event_names,
    _mutation_audit,
    _permutation_to_t126_datum,
    run_t252_analysis,
)


NOT_CLAIMED = (
    "These diagnostics do not estimate dimension, prove faithful embedding, "
    "validate random sprinkling, derive metric structure, or settle S1."
)


@dataclass(frozen=True)
class ShapeSummary:
    name: str
    classification: str
    t126_filter_passed: bool
    event_count: int
    strict_pair_count: int
    ordering_fraction: Fraction
    cover_relation_count: int
    link_density: Fraction
    height: int
    width: int
    rank_profile: tuple[int, ...]
    interval_counts_by_size: tuple[tuple[int, int], ...]
    interval_profile_counts: tuple[tuple[str, int], ...]
    largest_interval_size: int
    largest_comparable_hub_fraction: Fraction
    largest_cover_hub_fraction: Fraction
    profile_spread_obstruction: bool


@dataclass(frozen=True)
class DeletionShapeSummary:
    removed_event: str
    shape: ShapeSummary


@dataclass(frozen=True)
class MutationShapeSummary:
    swapped_positions: tuple[int, int]
    permutation: tuple[int, ...]
    ordering_band_passed: bool
    shape: ShapeSummary


@dataclass(frozen=True)
class T256Result:
    parent_shape: ShapeSummary
    deletion_shapes: tuple[DeletionShapeSummary, ...]
    deletion_largest_interval_distribution: tuple[tuple[int, int], ...]
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T257Result:
    parent_shape: ShapeSummary
    deletion_shapes: tuple[DeletionShapeSummary, ...]
    deletion_cover_count_distribution: tuple[tuple[int, int], ...]
    deletion_cover_hub_distribution: tuple[tuple[Fraction, int], ...]
    deletion_link_density_distribution: tuple[tuple[Fraction, int], ...]
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T258Result:
    positive_neighbors: tuple[MutationShapeSummary, ...]
    positive_neighbor_count: int
    ordering_fraction_distribution: tuple[tuple[Fraction, int], ...]
    height_distribution: tuple[tuple[int, int], ...]
    width_distribution: tuple[tuple[int, int], ...]
    cover_count_distribution: tuple[tuple[int, int], ...]
    largest_interval_distribution: tuple[tuple[int, int], ...]
    cover_hub_distribution: tuple[tuple[Fraction, int], ...]
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T259Result:
    blocked_inside_band_neighbors: tuple[MutationShapeSummary, ...]
    blocked_inside_band_count: int
    classification_distribution: tuple[tuple[str, int], ...]
    profile_spread_obstruction_count: int
    ordering_fraction_distribution: tuple[tuple[Fraction, int], ...]
    rank_profile_distribution: tuple[tuple[tuple[int, ...], int], ...]
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T260Result:
    outside_band_neighbors: tuple[MutationShapeSummary, ...]
    outside_band_count: int
    outside_band_swaps: tuple[tuple[int, int], ...]
    ordering_fraction_distribution: tuple[tuple[Fraction, int], ...]
    cover_count_distribution: tuple[tuple[int, int], ...]
    cover_hub_distribution: tuple[tuple[Fraction, int], ...]
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T261Result:
    grid_shape: ShapeSummary
    ordinal_shape: ShapeSummary
    strict_pair_delta_grid_minus_ordinal: int
    ordering_fraction_gap_grid_minus_ordinal: Fraction
    cover_relation_delta_grid_minus_ordinal: int
    link_density_gap_grid_minus_ordinal: Fraction
    largest_interval_delta_grid_minus_ordinal: int
    cover_hub_gap_grid_minus_ordinal: Fraction
    width_delta_grid_minus_ordinal: int
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T262Result:
    parent_and_deletions_stay_inside_interval_cap: bool
    parent_and_deletions_stay_below_cover_hub_cap: bool
    mutation_count: int
    positive_neighbor_count: int
    blocked_inside_band_count: int
    outside_band_count: int
    positive_neighbor_rate: Fraction
    band_neighbor_rate: Fraction
    selected_next_route: str
    secondary_route: str
    rejected_route: str
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T263Result:
    t256_verdict: str
    t257_verdict: str
    t258_verdict: str
    t259_verdict: str
    t260_verdict: str
    t261_verdict: str
    t262_verdict: str
    completed_task_count: int
    round_verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


def run_t256_analysis() -> T256Result:
    parent = _t252_parent_shape()
    deletions = _t252_deletion_shapes()
    largest_interval_distribution = _distribution(
        deletion.shape.largest_interval_size for deletion in deletions
    )
    verdict = (
        "ordinal_interval_profiles_bounded_under_deletion"
        if parent.largest_interval_size == 3
        and largest_interval_distribution == ((2, 1), (3, 8))
        else "unexpected_ordinal_interval_profile_status"
    )
    return T256Result(
        parent_shape=parent,
        deletion_shapes=deletions,
        deletion_largest_interval_distribution=largest_interval_distribution,
        verdict=verdict,
        strongest_claim=(
            "The T252 parent has largest finite interval size 3, and all nine "
            "single-event deletions keep largest intervals at size 2 or 3."
        ),
        improved=(
            "T256 records interval shape rather than relying only on the "
            "ordering-fraction pass from T252/T253."
        ),
        weakened_or_falsified=(
            "This weakens the concern that the selected witness hides a deep "
            "finite interval like the T249 grid's size-7 interval."
        ),
        falsification_condition=(
            "T256 fails if interval counts are not computed from the same T252 "
            "strict relation, if deletion suborders are not restrictions, or if "
            "the bounded finite profile is promoted into a continuum locality "
            "claim."
        ),
        s1_update="S1 remains guarded; bounded finite intervals are diagnostic only.",
        claim_ledger_update=(
            "Do not update the claim ledger from T256 alone. Safe wording: the "
            "selected T252 witness has small interval profiles under all single "
            "deletions."
        ),
        open_blocker=(
            "No distributional abundance result or Lorentzian interval-volume "
            "comparison has been attached to these finite counts."
        ),
        suggested_next=(
            "Pair interval profiles with cover/locality summaries and then ask "
            "whether the pattern is common across the n=9 search space."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t257_analysis() -> T257Result:
    parent = _t252_parent_shape()
    deletions = _t252_deletion_shapes()
    cover_count_distribution = _distribution(
        deletion.shape.cover_relation_count for deletion in deletions
    )
    cover_hub_distribution = _distribution(
        deletion.shape.largest_cover_hub_fraction for deletion in deletions
    )
    link_density_distribution = _distribution(
        deletion.shape.link_density for deletion in deletions
    )
    verdict = (
        "ordinal_cover_locality_stable_under_deletion"
        if parent.cover_relation_count == 8
        and parent.largest_cover_hub_fraction == Fraction(1, 4)
        and cover_count_distribution == ((6, 1), (7, 8))
        and cover_hub_distribution == ((Fraction(2, 7), 9),)
        else "unexpected_ordinal_cover_locality_status"
    )
    return T257Result(
        parent_shape=parent,
        deletion_shapes=deletions,
        deletion_cover_count_distribution=cover_count_distribution,
        deletion_cover_hub_distribution=cover_hub_distribution,
        deletion_link_density_distribution=link_density_distribution,
        verdict=verdict,
        strongest_claim=(
            "The T252 parent has 8 cover relations and a largest cover hub "
            "fraction of 1/4; every deletion keeps the cover hub at 2/7."
        ),
        improved=(
            "T257 adds a cover/locality-style view to the T252 deletion story, "
            "separating sparse cover structure from mere ordering fraction."
        ),
        weakened_or_falsified=(
            "This further weakens the suspicion that the T252 control passes "
            "only because of a concentrated cover hub."
        ),
        falsification_condition=(
            "T257 fails if cover relations are not the transitive reductions of "
            "the audited strict orders, or if finite cover sparsity is treated "
            "as an embedding theorem."
        ),
        s1_update="S1 remains guarded; cover sparsity is still a finite filter.",
        claim_ledger_update=(
            "Do not update the claim ledger from T257 alone. Safe wording: the "
            "selected T252 witness has stable sparse cover summaries under "
            "single deletion."
        ),
        open_blocker=(
            "The repo still lacks a selection rule explaining why this cover "
            "shape should occur naturally."
        ),
        suggested_next=(
            "Use the same shape summaries on the T255 mutation neighborhood to "
            "separate positive neighbors from T126-obstructed cases."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t258_analysis() -> T258Result:
    positives = tuple(
        mutation
        for mutation in _mutation_shapes()
        if mutation.shape.t126_filter_passed and mutation.ordering_band_passed
    )
    verdict = (
        "positive_mutation_neighbors_keep_band_but_shape_varies"
        if len(positives) == 21
        else "unexpected_positive_mutation_neighbor_status"
    )
    return T258Result(
        positive_neighbors=positives,
        positive_neighbor_count=len(positives),
        ordering_fraction_distribution=_distribution(
            mutation.shape.ordering_fraction for mutation in positives
        ),
        height_distribution=_distribution(mutation.shape.height for mutation in positives),
        width_distribution=_distribution(mutation.shape.width for mutation in positives),
        cover_count_distribution=_distribution(
            mutation.shape.cover_relation_count for mutation in positives
        ),
        largest_interval_distribution=_distribution(
            mutation.shape.largest_interval_size for mutation in positives
        ),
        cover_hub_distribution=_distribution(
            mutation.shape.largest_cover_hub_fraction for mutation in positives
        ),
        verdict=verdict,
        strongest_claim=(
            "The 21 mutation-positive neighbors are not all copies of T252: "
            "they span multiple ordering fractions, widths, cover counts, and "
            "largest interval sizes."
        ),
        improved=(
            "T258 turns the T255 positive count into a structural catalog rather "
            "than a bare tally."
        ),
        weakened_or_falsified=(
            "This weakens the idea that one rigid shape explains every nearby "
            "positive case; the local positive region is heterogeneous."
        ),
        falsification_condition=(
            "T258 fails if the positives are not exactly T255 one-transposition "
            "neighbors that pass both T126 and the T156 band."
        ),
        s1_update="S1 remains guarded; local positive heterogeneity is not typicality.",
        claim_ledger_update=(
            "Do not update the claim ledger from T258 alone. Safe wording: 21 "
            "one-transposition neighbors pass the finite screens, with varied "
            "finite shape summaries."
        ),
        open_blocker=(
            "The positive-neighbor catalog has not been converted into an exact "
            "global abundance count or a generative law."
        ),
        suggested_next=(
            "Compare positive neighbors against the inside-band cases that fail "
            "T126 to identify the active obstruction."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t259_analysis() -> T259Result:
    blocked = tuple(
        mutation
        for mutation in _mutation_shapes()
        if not mutation.shape.t126_filter_passed and mutation.ordering_band_passed
    )
    obstruction_count = sum(
        1 for mutation in blocked if mutation.shape.profile_spread_obstruction
    )
    verdict = (
        "inside_band_neighbors_blocked_by_profile_spread"
        if len(blocked) == 13 and obstruction_count == 13
        else "unexpected_inside_band_obstruction_status"
    )
    return T259Result(
        blocked_inside_band_neighbors=blocked,
        blocked_inside_band_count=len(blocked),
        classification_distribution=_distribution(
            mutation.shape.classification for mutation in blocked
        ),
        profile_spread_obstruction_count=obstruction_count,
        ordering_fraction_distribution=_distribution(
            mutation.shape.ordering_fraction for mutation in blocked
        ),
        rank_profile_distribution=_distribution(
            mutation.shape.rank_profile for mutation in blocked
        ),
        verdict=verdict,
        strongest_claim=(
            "All 13 inside-band neighbors blocked by T126 are classified as "
            "order-dimension obstructions, and all 13 trip the profile-spread "
            "diagnostic."
        ),
        improved=(
            "T259 explains why the T156 band alone is too weak in the local "
            "neighborhood: it admits cases with unstable interval profiles."
        ),
        weakened_or_falsified=(
            "This weakens any plan to use the Myrheim-Meyer ordering-fraction "
            "band by itself as the next S1-facing filter."
        ),
        falsification_condition=(
            "T259 fails if any inside-band T255 blocked neighbor has a different "
            "T126 classification or lacks profile-spread obstruction."
        ),
        s1_update=(
            "S1 remains guarded; the obstruction confirms the need for multiple "
            "finite screens."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T259 alone. Safe wording: in "
            "the T255 neighborhood, every inside-band T126 failure is a "
            "profile-spread/order-dimension obstruction."
        ),
        open_blocker=(
            "The obstruction is diagnostic, not a theorem identifying the right "
            "continuum dimension or a selection measure."
        ),
        suggested_next=(
            "Keep the T126 profile-spread gate active in any exact n=9 count."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t260_analysis() -> T260Result:
    outside = tuple(
        mutation
        for mutation in _mutation_shapes()
        if mutation.shape.t126_filter_passed and not mutation.ordering_band_passed
    )
    swaps = tuple(mutation.swapped_positions for mutation in outside)
    verdict = (
        "outside_band_neighbors_are_two_low_fraction_edge_cases"
        if swaps == ((0, 4), (0, 8))
        and _distribution(mutation.shape.ordering_fraction for mutation in outside)
        == ((Fraction(13, 36), 2),)
        else "unexpected_outside_band_neighbor_status"
    )
    return T260Result(
        outside_band_neighbors=outside,
        outside_band_count=len(outside),
        outside_band_swaps=swaps,
        ordering_fraction_distribution=_distribution(
            mutation.shape.ordering_fraction for mutation in outside
        ),
        cover_count_distribution=_distribution(
            mutation.shape.cover_relation_count for mutation in outside
        ),
        cover_hub_distribution=_distribution(
            mutation.shape.largest_cover_hub_fraction for mutation in outside
        ),
        verdict=verdict,
        strongest_claim=(
            "Only two T255 neighbors pass T126 while missing the declared "
            "ordering band, and both miss low at ordering fraction 13/36."
        ),
        improved=(
            "T260 records the small outside-band tail so that the positive count "
            "is not mistaken for all T126-passing mutations."
        ),
        weakened_or_falsified=(
            "This weakens a uniform-neighborhood reading: even T126-passing "
            "one-transposition neighbors can fall below the target band."
        ),
        falsification_condition=(
            "T260 fails if outside-band status is computed from a different "
            "target band, or if swaps outside the T255 transposition list are "
            "included."
        ),
        s1_update="S1 remains guarded; two low-fraction edge cases are controls only.",
        claim_ledger_update=(
            "Do not update the claim ledger from T260 alone. Safe wording: two "
            "T126-passing T255 neighbors fall below the declared ordering band."
        ),
        open_blocker=(
            "No principle currently explains the boundary between low-fraction "
            "T126 passes and in-band positives."
        ),
        suggested_next=(
            "Use exact counting or a stricter local shape gate before adding "
            "more selected examples."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t261_analysis() -> T261Result:
    grid = _t249_grid_shape()
    ordinal = _t252_parent_shape()
    verdict = (
        "grid_is_more_ordered_and_interval_deeper_than_ordinal_control"
        if grid.strict_pair_count > ordinal.strict_pair_count
        and grid.largest_interval_size > ordinal.largest_interval_size
        and grid.largest_cover_hub_fraction > ordinal.largest_cover_hub_fraction
        else "unexpected_grid_ordinal_shape_comparison_status"
    )
    return T261Result(
        grid_shape=grid,
        ordinal_shape=ordinal,
        strict_pair_delta_grid_minus_ordinal=(
            grid.strict_pair_count - ordinal.strict_pair_count
        ),
        ordering_fraction_gap_grid_minus_ordinal=(
            grid.ordering_fraction - ordinal.ordering_fraction
        ),
        cover_relation_delta_grid_minus_ordinal=(
            grid.cover_relation_count - ordinal.cover_relation_count
        ),
        link_density_gap_grid_minus_ordinal=grid.link_density - ordinal.link_density,
        largest_interval_delta_grid_minus_ordinal=(
            grid.largest_interval_size - ordinal.largest_interval_size
        ),
        cover_hub_gap_grid_minus_ordinal=(
            grid.largest_cover_hub_fraction - ordinal.largest_cover_hub_fraction
        ),
        width_delta_grid_minus_ordinal=grid.width - ordinal.width,
        verdict=verdict,
        strongest_claim=(
            "At the same nine-event scale, the T249 grid is more ordered than "
            "the T252 ordinal witness: +7 strict pairs, +4 cover relations, "
            "and largest interval size 7 instead of 3."
        ),
        improved=(
            "T261 gives the T249/T252 contrast a structural explanation beyond "
            "the ordering-fraction pass/fail result."
        ),
        weakened_or_falsified=(
            "This weakens product-grid optimism: T249's failure aligns with "
            "deeper intervals and a larger cover hub, not just a marginal band "
            "miss."
        ),
        falsification_condition=(
            "T261 fails if the compared shapes are not the original T249 and "
            "T252 audited relations, or if a finite contrast is reported as a "
            "general theorem."
        ),
        s1_update="S1 remains guarded; same-scale contrast is not a continuum bridge.",
        claim_ledger_update=(
            "Do not update the claim ledger from T261 alone. Safe wording: the "
            "T249 grid and T252 ordinal control differ sharply in finite shape "
            "diagnostics."
        ),
        open_blocker=(
            "The comparison still does not say how often T252-like shapes occur "
            "under a principled ensemble."
        ),
        suggested_next=(
            "Prefer exact n=9 counting with these labels over more hand-picked "
            "grid-vs-ordinal examples."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t262_analysis() -> T262Result:
    t256 = run_t256_analysis()
    t257 = run_t257_analysis()
    t258 = run_t258_analysis()
    t259 = run_t259_analysis()
    t260 = run_t260_analysis()
    mutation_count = (
        t258.positive_neighbor_count
        + t259.blocked_inside_band_count
        + t260.outside_band_count
    )
    parent_and_deletions_stay_inside_interval_cap = (
        t256.parent_shape.largest_interval_size <= 3
        and all(
            deletion.shape.largest_interval_size <= 3
            for deletion in t256.deletion_shapes
        )
    )
    parent_and_deletions_stay_below_cover_hub_cap = (
        t257.parent_shape.largest_cover_hub_fraction <= Fraction(2, 7)
        and all(
            deletion.shape.largest_cover_hub_fraction <= Fraction(2, 7)
            for deletion in t257.deletion_shapes
        )
    )
    verdict = (
        "exact_nine_event_count_preferred_over_more_selected_examples"
        if mutation_count == 36
        and t258.positive_neighbor_count == 21
        and t259.blocked_inside_band_count == 13
        and t260.outside_band_count == 2
        else "route_selection_needs_reaudit"
    )
    return T262Result(
        parent_and_deletions_stay_inside_interval_cap=(
            parent_and_deletions_stay_inside_interval_cap
        ),
        parent_and_deletions_stay_below_cover_hub_cap=(
            parent_and_deletions_stay_below_cover_hub_cap
        ),
        mutation_count=mutation_count,
        positive_neighbor_count=t258.positive_neighbor_count,
        blocked_inside_band_count=t259.blocked_inside_band_count,
        outside_band_count=t260.outside_band_count,
        positive_neighbor_rate=_fraction(t258.positive_neighbor_count, 36),
        band_neighbor_rate=_fraction(
            t258.positive_neighbor_count + t259.blocked_inside_band_count,
            36,
        ),
        selected_next_route="bounded_exact_n9_class_count_with_shape_labels",
        secondary_route="turn_T256_T257_interval_cover_caps_into_a_stricter_gate",
        rejected_route="keep_adding_hand_picked_selected_examples",
        verdict=verdict,
        strongest_claim=(
            "The next meaningful route is a bounded exact n=9 count with the "
            "T126/T156/T256/T257 labels attached, not another selected example."
        ),
        improved=(
            "T262 converts the diagnostic batch into an orchestration choice "
            "for the next round."
        ),
        weakened_or_falsified=(
            "This weakens the value of more hand-picked witnesses: the local "
            "neighborhood already shows both positive abundance and active "
            "obstructions."
        ),
        falsification_condition=(
            "T262 fails if the mutation partition does not cover all 36 T255 "
            "neighbors or if exact counting is infeasible without an explicit "
            "bounded search plan."
        ),
        s1_update="S1 remains guarded; route selection is a research-process result.",
        claim_ledger_update=(
            "Do not update the claim ledger from T262 alone. Safe wording: the "
            "next recommended finite task is exact n=9 counting with shape "
            "labels."
        ),
        open_blocker=(
            "Exact global abundance for nine-event ordinal controls is still "
            "uncomputed."
        ),
        suggested_next=(
            "Run the bounded exact n=9 class count, then decide whether the "
            "interval/cover caps should become formal gates."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t263_analysis() -> T263Result:
    t256 = run_t256_analysis()
    t257 = run_t257_analysis()
    t258 = run_t258_analysis()
    t259 = run_t259_analysis()
    t260 = run_t260_analysis()
    t261 = run_t261_analysis()
    t262 = run_t262_analysis()
    return T263Result(
        t256_verdict=t256.verdict,
        t257_verdict=t257.verdict,
        t258_verdict=t258.verdict,
        t259_verdict=t259.verdict,
        t260_verdict=t260.verdict,
        t261_verdict=t261.verdict,
        t262_verdict=t262.verdict,
        completed_task_count=8,
        round_verdict="eight_task_ordinal_neighborhood_diagnostic_round_complete",
        strongest_claim=(
            "T256-T263 complete an eight-task finite diagnostic round around "
            "T252: the selected witness has bounded interval and cover profiles, "
            "its mutation neighborhood is mixed, and exact n=9 counting is the "
            "next meaningful route."
        ),
        improved=(
            "The round replaces a bare positive witness with a shape-aware "
            "neighborhood map and a concrete next-task recommendation."
        ),
        weakened_or_falsified=(
            "The round weakens both overconfident readings and dead-end "
            "readings: T252 is not isolated, but the local neighborhood is not "
            "uniformly S1-facing."
        ),
        falsification_condition=(
            "T263 fails if any constituent T256-T262 task is computed from a "
            "different relation family or target band."
        ),
        s1_update=(
            "S1 remains requires_added_assumption/open_formal_target. No claim "
            "ledger upgrade follows from this round."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T263 alone. Safe wording: "
            "T256-T263 add finite structural diagnostics and recommend exact "
            "n=9 counting."
        ),
        open_blocker=(
            "The open blocker is now global abundance under a declared finite "
            "ensemble, plus any later continuum-facing comparison."
        ),
        suggested_next=(
            "Run the bounded exact n=9 class count with T126, T156, interval, "
            "and cover labels."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t256_result_to_dict(result: T256Result) -> dict[str, Any]:
    return {
        "parent_shape": _shape_to_dict(result.parent_shape),
        "deletion_shapes": [
            _deletion_shape_to_dict(deletion) for deletion in result.deletion_shapes
        ],
        "deletion_largest_interval_distribution": _distribution_to_json(
            result.deletion_largest_interval_distribution
        ),
        **_common_to_dict(result),
    }


def t257_result_to_dict(result: T257Result) -> dict[str, Any]:
    return {
        "parent_shape": _shape_to_dict(result.parent_shape),
        "deletion_shapes": [
            _deletion_shape_to_dict(deletion) for deletion in result.deletion_shapes
        ],
        "deletion_cover_count_distribution": _distribution_to_json(
            result.deletion_cover_count_distribution
        ),
        "deletion_cover_hub_distribution": _distribution_to_json(
            result.deletion_cover_hub_distribution
        ),
        "deletion_link_density_distribution": _distribution_to_json(
            result.deletion_link_density_distribution
        ),
        **_common_to_dict(result),
    }


def t258_result_to_dict(result: T258Result) -> dict[str, Any]:
    return {
        "positive_neighbors": [
            _mutation_shape_to_dict(mutation) for mutation in result.positive_neighbors
        ],
        "positive_neighbor_count": result.positive_neighbor_count,
        "ordering_fraction_distribution": _distribution_to_json(
            result.ordering_fraction_distribution
        ),
        "height_distribution": _distribution_to_json(result.height_distribution),
        "width_distribution": _distribution_to_json(result.width_distribution),
        "cover_count_distribution": _distribution_to_json(
            result.cover_count_distribution
        ),
        "largest_interval_distribution": _distribution_to_json(
            result.largest_interval_distribution
        ),
        "cover_hub_distribution": _distribution_to_json(result.cover_hub_distribution),
        **_common_to_dict(result),
    }


def t259_result_to_dict(result: T259Result) -> dict[str, Any]:
    return {
        "blocked_inside_band_neighbors": [
            _mutation_shape_to_dict(mutation)
            for mutation in result.blocked_inside_band_neighbors
        ],
        "blocked_inside_band_count": result.blocked_inside_band_count,
        "classification_distribution": _distribution_to_json(
            result.classification_distribution
        ),
        "profile_spread_obstruction_count": result.profile_spread_obstruction_count,
        "ordering_fraction_distribution": _distribution_to_json(
            result.ordering_fraction_distribution
        ),
        "rank_profile_distribution": _distribution_to_json(
            result.rank_profile_distribution
        ),
        **_common_to_dict(result),
    }


def t260_result_to_dict(result: T260Result) -> dict[str, Any]:
    return {
        "outside_band_neighbors": [
            _mutation_shape_to_dict(mutation) for mutation in result.outside_band_neighbors
        ],
        "outside_band_count": result.outside_band_count,
        "outside_band_swaps": [list(swap) for swap in result.outside_band_swaps],
        "ordering_fraction_distribution": _distribution_to_json(
            result.ordering_fraction_distribution
        ),
        "cover_count_distribution": _distribution_to_json(
            result.cover_count_distribution
        ),
        "cover_hub_distribution": _distribution_to_json(result.cover_hub_distribution),
        **_common_to_dict(result),
    }


def t261_result_to_dict(result: T261Result) -> dict[str, Any]:
    return {
        "grid_shape": _shape_to_dict(result.grid_shape),
        "ordinal_shape": _shape_to_dict(result.ordinal_shape),
        "strict_pair_delta_grid_minus_ordinal": (
            result.strict_pair_delta_grid_minus_ordinal
        ),
        "ordering_fraction_gap_grid_minus_ordinal": _fraction_to_dict(
            result.ordering_fraction_gap_grid_minus_ordinal
        ),
        "cover_relation_delta_grid_minus_ordinal": (
            result.cover_relation_delta_grid_minus_ordinal
        ),
        "link_density_gap_grid_minus_ordinal": _fraction_to_dict(
            result.link_density_gap_grid_minus_ordinal
        ),
        "largest_interval_delta_grid_minus_ordinal": (
            result.largest_interval_delta_grid_minus_ordinal
        ),
        "cover_hub_gap_grid_minus_ordinal": _fraction_to_dict(
            result.cover_hub_gap_grid_minus_ordinal
        ),
        "width_delta_grid_minus_ordinal": result.width_delta_grid_minus_ordinal,
        **_common_to_dict(result),
    }


def t262_result_to_dict(result: T262Result) -> dict[str, Any]:
    return {
        "parent_and_deletions_stay_inside_interval_cap": (
            result.parent_and_deletions_stay_inside_interval_cap
        ),
        "parent_and_deletions_stay_below_cover_hub_cap": (
            result.parent_and_deletions_stay_below_cover_hub_cap
        ),
        "mutation_count": result.mutation_count,
        "positive_neighbor_count": result.positive_neighbor_count,
        "blocked_inside_band_count": result.blocked_inside_band_count,
        "outside_band_count": result.outside_band_count,
        "positive_neighbor_rate": _fraction_to_dict(result.positive_neighbor_rate),
        "band_neighbor_rate": _fraction_to_dict(result.band_neighbor_rate),
        "selected_next_route": result.selected_next_route,
        "secondary_route": result.secondary_route,
        "rejected_route": result.rejected_route,
        **_common_to_dict(result),
    }


def t263_result_to_dict(result: T263Result) -> dict[str, Any]:
    return {
        "t256_verdict": result.t256_verdict,
        "t257_verdict": result.t257_verdict,
        "t258_verdict": result.t258_verdict,
        "t259_verdict": result.t259_verdict,
        "t260_verdict": result.t260_verdict,
        "t261_verdict": result.t261_verdict,
        "t262_verdict": result.t262_verdict,
        "completed_task_count": result.completed_task_count,
        "round_verdict": result.round_verdict,
        **_common_to_dict(result, verdict_key="round_verdict"),
    }


@lru_cache(maxsize=1)
def _t252_parent_shape() -> ShapeSummary:
    return _shape_summary("t252_parent", run_t252_analysis().t126_audit)


@lru_cache(maxsize=1)
def _t249_grid_shape() -> ShapeSummary:
    return _shape_summary("t249_grid", run_t249_analysis().t126_audit)


@lru_cache(maxsize=1)
def _t252_deletion_shapes() -> tuple[DeletionShapeSummary, ...]:
    return tuple(
        DeletionShapeSummary(
            removed_event=event,
            shape=_shape_summary(
                f"t252_delete_{event}",
                audit_finality_colimit_causet(_deletion_datum(event)),
            ),
        )
        for event in _event_names(NINE_EVENT_ORDINAL_PERMUTATION)
    )


@lru_cache(maxsize=1)
def _mutation_shapes() -> tuple[MutationShapeSummary, ...]:
    target = flat_1p1_interval_target()
    mutations: list[MutationShapeSummary] = []
    for left, right in combinations(range(len(NINE_EVENT_ORDINAL_PERMUTATION)), 2):
        mutation = _mutation_audit(left, right, target)
        audit = audit_finality_colimit_causet(
            _permutation_to_t126_datum(
                mutation.permutation,
                name=f"t256_t263_swap_{left}_{right}",
            )
        )
        mutations.append(
            MutationShapeSummary(
                swapped_positions=mutation.swapped_positions,
                permutation=mutation.permutation,
                ordering_band_passed=mutation.ordering_band_passed,
                shape=_shape_summary(f"swap_{left}_{right}", audit),
            )
        )
    return tuple(mutations)


def _shape_summary(name: str, audit: CausetAudit) -> ShapeSummary:
    diagnostics = audit.diagnostics
    if diagnostics is None:
        raise AssertionError(f"{name} should produce finite causet diagnostics")
    return ShapeSummary(
        name=name,
        classification=audit.classification,
        t126_filter_passed=audit.manifold_filter_passed,
        event_count=diagnostics.event_count,
        strict_pair_count=diagnostics.strict_pair_count,
        ordering_fraction=diagnostics.comparable_fraction,
        cover_relation_count=diagnostics.cover_relation_count,
        link_density=diagnostics.link_density,
        height=diagnostics.height,
        width=diagnostics.width,
        rank_profile=diagnostics.rank_profile,
        interval_counts_by_size=diagnostics.interval_counts_by_size,
        interval_profile_counts=diagnostics.interval_profile_counts,
        largest_interval_size=_largest_interval_size(diagnostics),
        largest_comparable_hub_fraction=diagnostics.largest_comparable_hub_fraction,
        largest_cover_hub_fraction=diagnostics.largest_cover_hub_fraction,
        profile_spread_obstruction=diagnostics.profile_spread_obstruction,
    )


def _largest_interval_size(diagnostics: CausetDiagnostics) -> int:
    return max(
        (size for size, count in diagnostics.interval_counts_by_size if count > 0),
        default=0,
    )


def _distribution(values: Iterable[Any]) -> tuple[tuple[Any, int], ...]:
    return tuple(sorted(Counter(values).items(), key=lambda item: repr(item[0])))


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _common_to_dict(result: object, *, verdict_key: str = "verdict") -> dict[str, Any]:
    return {
        verdict_key: getattr(result, verdict_key),
        "strongest_claim": getattr(result, "strongest_claim"),
        "improved": getattr(result, "improved"),
        "weakened_or_falsified": getattr(result, "weakened_or_falsified"),
        "falsification_condition": getattr(result, "falsification_condition"),
        "s1_update": getattr(result, "s1_update"),
        "claim_ledger_update": getattr(result, "claim_ledger_update"),
        "open_blocker": getattr(result, "open_blocker"),
        "suggested_next": getattr(result, "suggested_next"),
        "not_claimed": getattr(result, "not_claimed"),
    }


def _shape_to_dict(shape: ShapeSummary) -> dict[str, Any]:
    return {
        "name": shape.name,
        "classification": shape.classification,
        "t126_filter_passed": shape.t126_filter_passed,
        "event_count": shape.event_count,
        "strict_pair_count": shape.strict_pair_count,
        "ordering_fraction": _fraction_to_dict(shape.ordering_fraction),
        "cover_relation_count": shape.cover_relation_count,
        "link_density": _fraction_to_dict(shape.link_density),
        "height": shape.height,
        "width": shape.width,
        "rank_profile": list(shape.rank_profile),
        "interval_counts_by_size": [
            {"size": size, "count": count}
            for size, count in shape.interval_counts_by_size
        ],
        "interval_profile_counts": [
            {"profile": profile, "count": count}
            for profile, count in shape.interval_profile_counts
        ],
        "largest_interval_size": shape.largest_interval_size,
        "largest_comparable_hub_fraction": _fraction_to_dict(
            shape.largest_comparable_hub_fraction
        ),
        "largest_cover_hub_fraction": _fraction_to_dict(
            shape.largest_cover_hub_fraction
        ),
        "profile_spread_obstruction": shape.profile_spread_obstruction,
    }


def _deletion_shape_to_dict(deletion: DeletionShapeSummary) -> dict[str, Any]:
    return {
        "removed_event": deletion.removed_event,
        "shape": _shape_to_dict(deletion.shape),
    }


def _mutation_shape_to_dict(mutation: MutationShapeSummary) -> dict[str, Any]:
    return {
        "swapped_positions": list(mutation.swapped_positions),
        "permutation": list(mutation.permutation),
        "ordering_band_passed": mutation.ordering_band_passed,
        "shape": _shape_to_dict(mutation.shape),
    }


def _distribution_to_json(distribution: tuple[tuple[Any, int], ...]) -> list[dict[str, Any]]:
    return [
        {"value": _value_to_json(value), "count": count}
        for value, count in distribution
    ]


def _value_to_json(value: Any) -> Any:
    if isinstance(value, Fraction):
        return _fraction_to_dict(value)
    if isinstance(value, tuple):
        return list(value)
    return value


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}
