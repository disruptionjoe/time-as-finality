"""T264-T279: exact nine-event ordinal count with shape labels.

T262 recommended a bounded exact n=9 class count with the existing T126/T156
screens plus the interval and cover labels introduced around T252. This module
does that count directly on ordinal rank permutations.

The direct counter is intentionally relation-level: for a permutation p, the
strict order is i < j and p_i < p_j. T264 validates this optimized path by
reproducing the published T223 n=6, n=7, and n=8 counts. The n=9 results remain
finite enumeration diagnostics only; they do not upgrade S1 or establish a
continuum, sprinkling, dimension, or embedding result.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from math import factorial
from typing import Any, Iterable


InfoPermutation = tuple[int, ...]

SELECTED_T252_RANK_PERMUTATION: InfoPermutation = (1, 6, 7, 8, 9, 2, 3, 4, 5)
T252_INTERVAL_CAP = 3
T252_COVER_HUB_CAP = Fraction(2, 7)
THIN_INTERVAL_CAP = 1

NOT_CLAIMED = (
    "These exact counts do not estimate dimension, prove faithful embedding, "
    "validate random sprinkling, derive metric structure, establish a continuum "
    "limit, or settle S1."
)


@dataclass(frozen=True)
class FastOrdinalDiagnostics:
    event_count: int
    classification: str
    t126_filter_passed: bool
    strict_pair_count: int
    cover_relation_count: int
    height: int
    width: int
    rank_profile: tuple[int, ...]
    interval_counts_by_size: tuple[tuple[int, int], ...]
    largest_interval_size: int
    largest_cover_hub_fraction: Fraction
    link_density: Fraction
    profile_spread_obstruction: bool


@dataclass(frozen=True)
class DeletionSummary:
    deletion_count: int
    t159_thin_deletion_pass_count: int
    relaxed_interval3_deletion_pass_count: int
    t253_t126_band_deletion_pass_count: int
    t252_style_deletion_pass_count: int


@dataclass(frozen=True)
class ExactOrdinalSizeAudit:
    event_count: int
    total_rank_permutation_cases: int
    t126_classification_counts: tuple[tuple[str, int], ...]
    t126_pass_count: int
    t156_pass_count: int
    t156_fraction: Fraction
    parent_interval_cap1_count: int
    t159_thin_deletion_stable_count: int
    parent_interval_cap3_count: int
    relaxed_interval3_deletion_stable_count: int
    t252_parent_cap_count: int
    t252_deletion_stable_count: int
    t253_all_deletions_t126_band_stable_count: int
    strict_pair_distribution: tuple[tuple[int, int], ...]
    t126_pass_strict_pair_distribution: tuple[tuple[int, int], ...]
    t156_height_distribution: tuple[tuple[int, int], ...]
    t156_width_distribution: tuple[tuple[int, int], ...]
    t156_largest_interval_distribution: tuple[tuple[int, int], ...]
    t156_cover_count_distribution: tuple[tuple[int, int], ...]
    t156_cover_hub_distribution: tuple[tuple[Fraction, int], ...]
    t156_rank_profile_top: tuple[tuple[tuple[int, ...], int], ...]
    thin_stable_strict_pair_distribution: tuple[tuple[int, int], ...]
    t253_stable_parent_max_interval_distribution: tuple[tuple[int, int], ...]
    t253_stable_parent_cover_hub_distribution: tuple[tuple[Fraction, int], ...]
    t252_parent_signature_distribution: tuple[tuple[tuple[Any, ...], int], ...]
    t252_deletion_stable_signature_distribution: tuple[tuple[tuple[Any, ...], int], ...]
    representative_t156_permutations: tuple[InfoPermutation, ...]
    representative_thin_stable_permutations: tuple[InfoPermutation, ...]
    representative_t252_parent_cap_permutations: tuple[InfoPermutation, ...]
    representative_t252_deletion_stable_permutations: tuple[InfoPermutation, ...]
    selected_t252_diagnostics: FastOrdinalDiagnostics | None
    selected_t252_deletion_summary: DeletionSummary | None


@dataclass(frozen=True)
class Metric:
    name: str
    value: Any


@dataclass(frozen=True)
class TaskResult:
    task_id: str
    title: str
    metrics: tuple[Metric, ...]
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


def run_t264_analysis() -> TaskResult:
    n6 = _audit_size(6)
    n7 = _audit_size(7)
    n8 = _audit_size(8)
    reproduced = (
        n6.t126_pass_count == 578
        and n6.t156_pass_count == 305
        and n6.t159_thin_deletion_stable_count == 26
        and n7.t126_pass_count == 4456
        and n7.t156_pass_count == 2051
        and n7.t159_thin_deletion_stable_count == 174
        and n8.t126_pass_count == 34044
        and n8.t156_pass_count == 16261
        and n8.t159_thin_deletion_stable_count == 361
    )
    return _task(
        "T264",
        "Optimized Ordinal Counter Validation",
        (
            Metric("n6_t126_t156_stable", (n6.t126_pass_count, n6.t156_pass_count, n6.t159_thin_deletion_stable_count)),
            Metric("n7_t126_t156_stable", (n7.t126_pass_count, n7.t156_pass_count, n7.t159_thin_deletion_stable_count)),
            Metric("n8_t126_t156_stable", (n8.t126_pass_count, n8.t156_pass_count, n8.t159_thin_deletion_stable_count)),
            Metric("reproduces_t223_counts", reproduced),
        ),
        "optimized_counter_reproduces_t223_n6_to_n8_counts" if reproduced else "optimized_counter_validation_failed",
        "The optimized relation-level ordinal counter reproduces the published T223 n=6, n=7, and n=8 counts.",
        "This makes the n=9 count feasible without rerunning T54 completion for every permutation.",
        "It weakens concern that the n=9 sweep is a new, incompatible pipeline.",
        "T264 fails if any reproduced T223 count differs from the published values.",
        "S1 is unchanged; this is validation of a finite counting implementation.",
        "Do not update the claim ledger from T264 alone.",
        "The validation says the counter matches prior finite counts; it does not pick a physical measure.",
        "Use the optimized counter for the exact n=9 sweep.",
    )


def run_t265_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T265",
        "Exact n=9 T126 Census",
        (
            Metric("total_cases", audit.total_rank_permutation_cases),
            Metric("t126_pass_count", audit.t126_pass_count),
            Metric("t126_classification_counts", audit.t126_classification_counts),
        ),
        "n9_t126_census_complete",
        "At n=9, 263047 of 362880 ordinal permutations pass T126; the rest are rejected by named finite obstructions.",
        "This gives the first exact n=9 T126 denominator for the ordinal ensemble.",
        "It weakens any reading that T126 alone is highly selective at n=9; most cases still pass that filter.",
        "T265 fails if the sweep does not exhaust all 9! ordinal permutations.",
        "S1 is unchanged; T126 passing remains filter-only.",
        "Do not update the claim ledger from T265 alone.",
        "T126 alone does not identify the rare stable tail or a continuum-facing family.",
        "Apply the declared ordering band and shape/deletion gates.",
    )


def run_t266_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T266",
        "Exact n=9 Ordering-Band Census",
        (
            Metric("t156_pass_count_after_t126", audit.t156_pass_count),
            Metric("t156_pass_fraction_of_total", audit.t156_fraction),
            Metric("t126_pass_strict_pair_distribution", audit.t126_pass_strict_pair_distribution),
        ),
        "n9_t126_t156_band_census_complete",
        "At n=9, 143435 permutations pass both T126 and the declared T156 ordering band.",
        "This separates broad T126 passing from the smaller ordering-band subset.",
        "It weakens any claim that ordering fraction alone is a strong locality or manifoldlikeness screen.",
        "T266 fails if T156 is not applied to the same strict-pair counts as T126.",
        "S1 is unchanged; the ordering band is an audit target, not a dimension estimate.",
        "Do not update the claim ledger from T266 alone.",
        "The band-positive set is still large and structurally mixed.",
        "Apply interval, cover, and deletion labels to the band-positive set.",
    )


def run_t267_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T267",
        "Exact n=9 Thin Parent-Interval Gate",
        (
            Metric("parent_interval_cap1_count", audit.parent_interval_cap1_count),
            Metric("parent_interval_cap1_fraction", _fraction(audit.parent_interval_cap1_count, audit.total_rank_permutation_cases)),
            Metric("t156_largest_interval_distribution", audit.t156_largest_interval_distribution),
        ),
        "n9_thin_parent_interval_gate_complete",
        "Only 7813 n=9 T126+T156 cases have largest parent interval size at most 1.",
        "This extends the T159/T223 thin-parent gate to the n=9 denominator.",
        "It weakens the selected T252 route under the older thin gate: T252 has largest interval size 3, not 1.",
        "T267 fails if largest interval sizes are not computed from the audited strict relation.",
        "S1 is unchanged; thin parent intervals are finite diagnostics only.",
        "Do not update the claim ledger from T267 alone.",
        "Thinness is still a hostile finite screen, not a continuum theorem.",
        "Check deletion stability for the thin-parent cases.",
    )


def run_t268_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T268",
        "Exact n=9 Thin Deletion Stability",
        (
            Metric("thin_parent_count", audit.parent_interval_cap1_count),
            Metric("thin_deletion_stable_count", audit.t159_thin_deletion_stable_count),
            Metric("thin_stable_fraction", _fraction(audit.t159_thin_deletion_stable_count, audit.total_rank_permutation_cases)),
            Metric("thin_stable_strict_pair_distribution", audit.thin_stable_strict_pair_distribution),
        ),
        "n9_t159_thin_stable_survivor_count_complete",
        "At n=9, the T159/T223 thin deletion-stable tail has 1583 labeled survivors.",
        "This gives the exact next-size count that T223 deliberately left as follow-on work.",
        "It weakens any hope that the thin tail becomes common at n=9; the count rises but the fraction continues to fall.",
        "T268 fails if deletion suborders are not rank-normalized restrictions of the parent permutation.",
        "S1 remains requires_added_assumption for the finite ordinal route.",
        "Do not update the claim ledger from T268 alone; combine with the trajectory result.",
        "Thin deletion stability still gives a rare finite tail, not spacetime evidence.",
        "Compare the n=9 stable fraction to n=6..8.",
    )


def run_t269_analysis() -> TaskResult:
    n6 = _audit_size(6)
    n7 = _audit_size(7)
    n8 = _audit_size(8)
    n9 = _audit_size(9)
    trajectory = tuple(
        (
            audit.event_count,
            _fraction(audit.t159_thin_deletion_stable_count, audit.total_rank_permutation_cases),
        )
        for audit in (n6, n7, n8, n9)
    )
    relevant = tuple(value for size, value in trajectory if size >= 6)
    monotone = all(
        later <= earlier
        for earlier, later in zip(relevant, relevant[1:])
    )
    return _task(
        "T269",
        "n=6..9 Thin Survivor Trajectory",
        (
            Metric("thin_stable_fraction_trajectory", trajectory),
            Metric("monotone_nonincreasing_from_n6", monotone),
        ),
        "n9_strengthens_t223_decay_trajectory" if monotone else "n9_breaks_t223_decay_trajectory",
        "Adding n=9 keeps the thin survivor fraction monotone non-increasing from n=6 through n=9.",
        "T269 turns the T223 follow-on into an exact next-size trajectory point.",
        "It weakens the 'maybe n=9 rebounds' escape for the uniform ordinal ensemble.",
        "T269 fails if the n=9 survivor fraction exceeds the n=8 fraction under the same thin gate.",
        "S1 remains requires_added_assumption for this finite route.",
        "Safe future wording: the exact n=9 thin-tail count strengthens the T223 finite no-go trajectory.",
        "The result still concerns the declared finite ordinal ensemble only.",
        "Stop expecting uniform ordinal counting alone to produce manifoldlikeness; look for a non-uniform selection principle.",
    )


def run_t270_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T270",
        "n=9 Relaxed Interval-3 Gate",
        (
            Metric("parent_interval_cap3_count", audit.parent_interval_cap3_count),
            Metric("relaxed_interval3_deletion_stable_count", audit.relaxed_interval3_deletion_stable_count),
            Metric("parent_interval_cap3_fraction", _fraction(audit.parent_interval_cap3_count, audit.total_rank_permutation_cases)),
        ),
        "n9_relaxed_interval3_gate_complete",
        "Relaxing the parent interval cap from 1 to 3 admits 91350 parents and 9176 deletion-stable cases.",
        "This quantifies how much of T252's interval behavior is excluded by the older thin gate.",
        "It weakens a binary reading of interval size: cap 3 is much less rare than T252's full cover-local shape.",
        "T270 fails if the relaxed cap is mixed with the older T159 thin cap.",
        "S1 is unchanged; relaxing a finite cap does not establish locality.",
        "Do not update the claim ledger from T270 alone.",
        "Interval cap 3 alone is too permissive to explain T252's selected shape.",
        "Add the cover-hub cap from T257.",
    )


def run_t271_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T271",
        "n=9 T252-Style Parent Cap",
        (
            Metric("t252_parent_cap_count", audit.t252_parent_cap_count),
            Metric("t252_parent_cap_fraction", _fraction(audit.t252_parent_cap_count, audit.total_rank_permutation_cases)),
            Metric("t252_parent_signature_distribution", audit.t252_parent_signature_distribution),
        ),
        "n9_t252_style_parent_cap_is_rare",
        "Only 66 n=9 permutations match the T252-style parent cap: T126+band, largest interval <=3, and cover hub <=2/7.",
        "This makes T252's parent shape a genuinely rare global feature, not just another band-positive case.",
        "It weakens the local-neighborhood optimism from T255: the stricter T252-style parent cap is globally tiny.",
        "T271 fails if the cover cap differs from the T257 deletion-stable cap.",
        "S1 is unchanged; rarity under one finite ensemble is not a physical selection law.",
        "Do not update the claim ledger from T271 alone.",
        "The 66 parents still need deletion stability and a selection explanation.",
        "Apply the same cap to every single-event deletion.",
    )


def run_t272_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T272",
        "n=9 T252-Style Deletion Stability",
        (
            Metric("t252_parent_cap_count", audit.t252_parent_cap_count),
            Metric("t252_deletion_stable_count", audit.t252_deletion_stable_count),
            Metric("t252_deletion_stable_fraction", _fraction(audit.t252_deletion_stable_count, audit.total_rank_permutation_cases)),
            Metric("t252_deletion_stable_signature_distribution", audit.t252_deletion_stable_signature_distribution),
            Metric("representative_t252_deletion_stable_permutations", audit.representative_t252_deletion_stable_permutations),
        ),
        "n9_t252_style_deletion_stable_tail_has_ten_cases",
        "Only 10 n=9 permutations pass the T252-style parent cap and keep every deletion inside the same T126/band/interval/cover gate.",
        "This gives a precise global answer to the T252/T253/T257 route: it exists, but it is a very small tail.",
        "It weakens both extremes: T252 is not unique, but T252-style deletion stability is far from typical.",
        "T272 fails if deletions are not rank-normalized suborders of the same parent permutation.",
        "S1 remains guarded; ten finite cases are not a continuum mechanism.",
        "Do not update the claim ledger from T272 alone.",
        "The ten-case tail has no natural measure or generative law attached.",
        "Inspect where the selected T252 witness sits inside this tail.",
    )


def run_t273_analysis() -> TaskResult:
    audit = _audit_size(9)
    selected = audit.selected_t252_diagnostics
    deletion = audit.selected_t252_deletion_summary
    if selected is None or deletion is None:
        raise AssertionError("T252 selected permutation should be present in n=9 audit")
    return _task(
        "T273",
        "Selected T252 Global Placement",
        (
            Metric("selected_t252_rank_permutation", SELECTED_T252_RANK_PERMUTATION),
            Metric("selected_t252_strict_pairs", selected.strict_pair_count),
            Metric("selected_t252_largest_interval", selected.largest_interval_size),
            Metric("selected_t252_cover_hub", selected.largest_cover_hub_fraction),
            Metric("selected_t252_deletion_summary", deletion),
            Metric("selected_is_t252_style_deletion_stable", deletion.t252_style_deletion_pass_count == selected.event_count),
        ),
        "selected_t252_is_one_of_the_ten_t252_style_stable_cases",
        "The selected T252 permutation is one of the 10 exact n=9 T252-style deletion-stable cases.",
        "This anchors the selected witness inside the global count instead of leaving it as a hand-picked orphan.",
        "It weakens overclaiming: T252 fails the older thin cap, so its support depends on the relaxed interval/cover gate.",
        "T273 fails if the selected permutation is not audited as the same rank order used in T252.",
        "S1 remains guarded; global placement is not physical selection.",
        "Do not update the claim ledger from T273 alone.",
        "Being one of ten finite cases does not explain why nature would select that tail.",
        "Compare the local T255 neighborhood against global rates.",
    )


def run_t274_analysis() -> TaskResult:
    audit = _audit_size(9)
    global_band_rate = _fraction(audit.t156_pass_count, audit.total_rank_permutation_cases)
    global_t252_parent_rate = _fraction(audit.t252_parent_cap_count, audit.total_rank_permutation_cases)
    global_t252_stable_rate = _fraction(audit.t252_deletion_stable_count, audit.total_rank_permutation_cases)
    return _task(
        "T274",
        "T255 Local Neighborhood Vs Global n=9 Rates",
        (
            Metric("t255_t126_band_neighbor_rate", Fraction(21, 36)),
            Metric("global_t126_band_rate", global_band_rate),
            Metric("t255_t252_style_neighbor_count", 0),
            Metric("global_t252_parent_cap_count", audit.t252_parent_cap_count),
            Metric("global_t252_deletion_stable_count", audit.t252_deletion_stable_count),
            Metric("global_t252_parent_rate", global_t252_parent_rate),
            Metric("global_t252_deletion_stable_rate", global_t252_stable_rate),
        ),
        "t255_neighborhood_enriched_for_band_but_not_t252_style_cap",
        "The T255 one-swap neighborhood is enriched for T126+band passes, but none of the 36 neighbors match the stricter T252-style cap.",
        "This explains the mixed T255 result: local band positives do not preserve the full T252 interval/cover shape.",
        "It weakens the idea that one-swap abundance is enough to support the selected witness.",
        "T274 fails if the local T255 rates are compared against a different n=9 ensemble.",
        "S1 is unchanged; local enrichment is not a global measure.",
        "Do not update the claim ledger from T274 alone.",
        "The selected shape is locally fragile under one-swap mutations.",
        "Use shape distributions to see what the broader band-positive set looks like.",
    )


def run_t275_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T275",
        "n=9 Band-Positive Shape Distributions",
        (
            Metric("t156_height_distribution", audit.t156_height_distribution),
            Metric("t156_width_distribution", audit.t156_width_distribution),
            Metric("t156_largest_interval_distribution", audit.t156_largest_interval_distribution),
            Metric("t156_cover_count_distribution", audit.t156_cover_count_distribution),
            Metric("t156_cover_hub_distribution", audit.t156_cover_hub_distribution),
            Metric("t156_rank_profile_top", audit.t156_rank_profile_top),
        ),
        "n9_band_positive_shapes_are_broad",
        "The 143435 band-positive n=9 cases span broad height, width, interval, cover-count, and cover-hub profiles.",
        "This turns the band-positive set into a structural distribution rather than a single count.",
        "It weakens ordering-fraction-only interpretations: equal band status hides very different finite shapes.",
        "T275 fails if shape labels are computed before applying the T126+T156 filters.",
        "S1 is unchanged; distributions are finite audit data.",
        "Do not update the claim ledger from T275 alone.",
        "The broad distribution still needs a principled selection rule.",
        "Separate deletion-stable band cases from the broad parent band.",
    )


def run_t276_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T276",
        "n=9 T253-Style Deletion-Band Stability",
        (
            Metric("t253_all_deletions_t126_band_stable_count", audit.t253_all_deletions_t126_band_stable_count),
            Metric("t253_all_deletions_t126_band_stable_fraction", _fraction(audit.t253_all_deletions_t126_band_stable_count, audit.total_rank_permutation_cases)),
            Metric("t253_stable_parent_max_interval_distribution", audit.t253_stable_parent_max_interval_distribution),
            Metric("t253_stable_parent_cover_hub_distribution", audit.t253_stable_parent_cover_hub_distribution),
        ),
        "n9_t253_style_deletion_band_stability_has_8339_cases",
        "8339 n=9 permutations pass T126+band and keep every deletion inside T126+band, but most do not satisfy the stricter T252 cover shape.",
        "This locates T253-style stability between the broad band-positive set and the tiny T252-style tail.",
        "It weakens any assumption that deletion-band stability alone recovers T252-like locality.",
        "T276 fails if deletion T126+band checks use a different target from the parent.",
        "S1 remains guarded; deletion-band stability is still finite control evidence.",
        "Do not update the claim ledger from T276 alone.",
        "Many deletion-stable band cases have larger cover hubs or intervals.",
        "Use obstruction anatomy and route selection to decide what to do next.",
    )


def run_t277_analysis() -> TaskResult:
    audit = _audit_size(9)
    blocked_total = audit.total_rank_permutation_cases - audit.t126_pass_count
    blocked_counts = tuple(
        (classification, count)
        for classification, count in audit.t126_classification_counts
        if classification != "passes_filter_only"
    )
    return _task(
        "T277",
        "n=9 T126 Obstruction Anatomy",
        (
            Metric("t126_blocked_total", blocked_total),
            Metric("t126_blocked_classification_counts", blocked_counts),
            Metric("dominant_blocker", max(blocked_counts, key=lambda item: item[1])[0]),
        ),
        "n9_t126_blockers_dominated_by_profile_spread",
        "Among n=9 T126 rejections, the dominant obstruction is order-dimension/profile-spread instability.",
        "This matches the T259 local-neighborhood lesson at global scale.",
        "It weakens the value of the ordering band without the T126 profile-spread gate.",
        "T277 fails if obstruction labels are not the same labels used by T126.",
        "S1 is unchanged; obstruction anatomy is diagnostic.",
        "Do not update the claim ledger from T277 alone.",
        "The obstruction labels do not derive a physical dimension estimator.",
        "Carry the profile-spread gate into any future selection measure.",
    )


def run_t278_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T278",
        "Post-n=9 Route Selection",
        (
            Metric("thin_stable_count", audit.t159_thin_deletion_stable_count),
            Metric("t252_style_stable_count", audit.t252_deletion_stable_count),
            Metric("selected_next_route", "non_uniform_selection_measure_for_t252_style_tail"),
            Metric("rejected_route", "more_uniform_ordinal_counting_without_new_measure"),
        ),
        "post_n9_route_requires_non_uniform_selection_or_new_bridge",
        "After exact n=9 counting, the meaningful next route is a non-uniform selection measure or a different bridge, not more uniform ordinal counting alone.",
        "T278 converts the 16-task data into an actionable research decision.",
        "It weakens further hand-picked or uniform-count-only rounds: the exact count already says the relevant tails are rare.",
        "T278 fails if the n=9 count is incomplete or if route selection ignores the tiny T252-style tail.",
        "S1 remains requires_added_assumption for the finite ordinal route.",
        "Safe future wording: exact n=9 counting strengthens the need for an added selection assumption.",
        "The actual added measure or continuum bridge remains unbuilt.",
        "Next, define and test a non-uniform finality-colimit measure against the 10 T252-style cases.",
    )


def run_t279_analysis() -> TaskResult:
    audit = _audit_size(9)
    return _task(
        "T279",
        "Sixteen-Task n=9 Exact Count Synthesis",
        (
            Metric("completed_task_count", 16),
            Metric("total_n9_cases", audit.total_rank_permutation_cases),
            Metric("t126_pass_count", audit.t126_pass_count),
            Metric("t126_t156_pass_count", audit.t156_pass_count),
            Metric("thin_stable_count", audit.t159_thin_deletion_stable_count),
            Metric("t252_style_parent_count", audit.t252_parent_cap_count),
            Metric("t252_style_stable_count", audit.t252_deletion_stable_count),
            Metric("round_verdict", "sixteen_task_n9_exact_count_round_complete"),
        ),
        "sixteen_task_n9_exact_count_round_complete",
        "T264-T279 complete the exact n=9 ordinal-count round: the uniform ordinal ensemble remains a rare-tail story, while the T252-style deletion-stable tail has exactly 10 labeled cases.",
        "The round replaces local T252/T255 evidence with global n=9 denominators.",
        "It weakens optimistic readings of local mutation abundance and further weakens uniform ordinal counting as an S1 route without added structure.",
        "T279 fails if any T264-T278 constituent result changes under the same screens.",
        "S1 remains requires_added_assumption for the finite ordinal route.",
        "Do not update the claim ledger from T279 alone unless recording the exact n=9 follow-on as strengthening T223.",
        "No non-uniform measure, embedding theorem, or continuum bridge has been supplied.",
        "Build the selection-measure task next, using the 10 T252-style stable cases as the target tail.",
    )


TASK_RUNNERS = (
    run_t264_analysis,
    run_t265_analysis,
    run_t266_analysis,
    run_t267_analysis,
    run_t268_analysis,
    run_t269_analysis,
    run_t270_analysis,
    run_t271_analysis,
    run_t272_analysis,
    run_t273_analysis,
    run_t274_analysis,
    run_t275_analysis,
    run_t276_analysis,
    run_t277_analysis,
    run_t278_analysis,
    run_t279_analysis,
)


@lru_cache(maxsize=None)
def _audit_size(event_count: int) -> ExactOrdinalSizeAudit:
    if event_count < 1:
        raise ValueError("event_count must be positive")

    classification_counts: Counter[str] = Counter()
    strict_pair_distribution: Counter[int] = Counter()
    t126_pass_strict_pair_distribution: Counter[int] = Counter()
    t156_height_distribution: Counter[int] = Counter()
    t156_width_distribution: Counter[int] = Counter()
    t156_largest_interval_distribution: Counter[int] = Counter()
    t156_cover_count_distribution: Counter[int] = Counter()
    t156_cover_hub_distribution: Counter[Fraction] = Counter()
    t156_rank_profile_distribution: Counter[tuple[int, ...]] = Counter()
    thin_stable_strict_pair_distribution: Counter[int] = Counter()
    t253_stable_parent_max_interval_distribution: Counter[int] = Counter()
    t253_stable_parent_cover_hub_distribution: Counter[Fraction] = Counter()
    t252_parent_signature_distribution: Counter[tuple[Any, ...]] = Counter()
    t252_deletion_stable_signature_distribution: Counter[tuple[Any, ...]] = Counter()

    t126_pass_count = 0
    t156_pass_count = 0
    parent_interval_cap1_count = 0
    thin_deletion_stable_count = 0
    parent_interval_cap3_count = 0
    relaxed_interval3_deletion_stable_count = 0
    t252_parent_cap_count = 0
    t252_deletion_stable_count = 0
    t253_stable_count = 0

    representative_t156: list[InfoPermutation] = []
    representative_thin_stable: list[InfoPermutation] = []
    representative_t252_parent: list[InfoPermutation] = []
    representative_t252_stable: list[InfoPermutation] = []
    selected_t252_diagnostics: FastOrdinalDiagnostics | None = None
    selected_t252_deletion_summary: DeletionSummary | None = None

    for info_permutation in permutations(range(1, event_count + 1)):
        diagnostics = _diagnostics_for_permutation(info_permutation)
        classification_counts[diagnostics.classification] += 1
        strict_pair_distribution[diagnostics.strict_pair_count] += 1

        if info_permutation == SELECTED_T252_RANK_PERMUTATION:
            selected_t252_diagnostics = diagnostics

        if not diagnostics.t126_filter_passed:
            continue
        t126_pass_count += 1
        t126_pass_strict_pair_distribution[diagnostics.strict_pair_count] += 1

        if not _ordering_band_passed(diagnostics.strict_pair_count, event_count):
            continue
        t156_pass_count += 1
        _append_representative(representative_t156, info_permutation)
        t156_height_distribution[diagnostics.height] += 1
        t156_width_distribution[diagnostics.width] += 1
        t156_largest_interval_distribution[diagnostics.largest_interval_size] += 1
        t156_cover_count_distribution[diagnostics.cover_relation_count] += 1
        t156_cover_hub_distribution[diagnostics.largest_cover_hub_fraction] += 1
        t156_rank_profile_distribution[diagnostics.rank_profile] += 1

        deletion_summary = _deletion_summary(info_permutation)
        if info_permutation == SELECTED_T252_RANK_PERMUTATION:
            selected_t252_deletion_summary = deletion_summary

        if deletion_summary.t253_t126_band_deletion_pass_count == event_count:
            t253_stable_count += 1
            t253_stable_parent_max_interval_distribution[
                diagnostics.largest_interval_size
            ] += 1
            t253_stable_parent_cover_hub_distribution[
                diagnostics.largest_cover_hub_fraction
            ] += 1

        if diagnostics.largest_interval_size <= THIN_INTERVAL_CAP:
            parent_interval_cap1_count += 1
            if deletion_summary.t159_thin_deletion_pass_count == event_count:
                thin_deletion_stable_count += 1
                thin_stable_strict_pair_distribution[
                    diagnostics.strict_pair_count
                ] += 1
                _append_representative(representative_thin_stable, info_permutation)

        if diagnostics.largest_interval_size <= T252_INTERVAL_CAP:
            parent_interval_cap3_count += 1
            if deletion_summary.relaxed_interval3_deletion_pass_count == event_count:
                relaxed_interval3_deletion_stable_count += 1

        if _passes_t252_parent_cap(diagnostics):
            t252_parent_cap_count += 1
            signature = _shape_signature(diagnostics)
            t252_parent_signature_distribution[signature] += 1
            _append_representative(representative_t252_parent, info_permutation, limit=10)
            if deletion_summary.t252_style_deletion_pass_count == event_count:
                t252_deletion_stable_count += 1
                t252_deletion_stable_signature_distribution[signature] += 1
                _append_representative(
                    representative_t252_stable,
                    info_permutation,
                    limit=10,
                )

    total_cases = factorial(event_count)
    return ExactOrdinalSizeAudit(
        event_count=event_count,
        total_rank_permutation_cases=total_cases,
        t126_classification_counts=tuple(sorted(classification_counts.items())),
        t126_pass_count=t126_pass_count,
        t156_pass_count=t156_pass_count,
        t156_fraction=_fraction(t156_pass_count, total_cases),
        parent_interval_cap1_count=parent_interval_cap1_count,
        t159_thin_deletion_stable_count=thin_deletion_stable_count,
        parent_interval_cap3_count=parent_interval_cap3_count,
        relaxed_interval3_deletion_stable_count=relaxed_interval3_deletion_stable_count,
        t252_parent_cap_count=t252_parent_cap_count,
        t252_deletion_stable_count=t252_deletion_stable_count,
        t253_all_deletions_t126_band_stable_count=t253_stable_count,
        strict_pair_distribution=tuple(sorted(strict_pair_distribution.items())),
        t126_pass_strict_pair_distribution=tuple(
            sorted(t126_pass_strict_pair_distribution.items())
        ),
        t156_height_distribution=tuple(sorted(t156_height_distribution.items())),
        t156_width_distribution=tuple(sorted(t156_width_distribution.items())),
        t156_largest_interval_distribution=tuple(
            sorted(t156_largest_interval_distribution.items())
        ),
        t156_cover_count_distribution=tuple(
            sorted(t156_cover_count_distribution.items())
        ),
        t156_cover_hub_distribution=tuple(sorted(t156_cover_hub_distribution.items())),
        t156_rank_profile_top=tuple(t156_rank_profile_distribution.most_common(10)),
        thin_stable_strict_pair_distribution=tuple(
            sorted(thin_stable_strict_pair_distribution.items())
        ),
        t253_stable_parent_max_interval_distribution=tuple(
            sorted(t253_stable_parent_max_interval_distribution.items())
        ),
        t253_stable_parent_cover_hub_distribution=tuple(
            sorted(t253_stable_parent_cover_hub_distribution.items())
        ),
        t252_parent_signature_distribution=tuple(
            sorted(t252_parent_signature_distribution.items(), key=lambda item: repr(item[0]))
        ),
        t252_deletion_stable_signature_distribution=tuple(
            sorted(
                t252_deletion_stable_signature_distribution.items(),
                key=lambda item: repr(item[0]),
            )
        ),
        representative_t156_permutations=tuple(representative_t156),
        representative_thin_stable_permutations=tuple(representative_thin_stable),
        representative_t252_parent_cap_permutations=tuple(representative_t252_parent),
        representative_t252_deletion_stable_permutations=tuple(
            representative_t252_stable
        ),
        selected_t252_diagnostics=selected_t252_diagnostics,
        selected_t252_deletion_summary=selected_t252_deletion_summary,
    )


@lru_cache(maxsize=None)
def _diagnostics_for_permutation(
    info_permutation: InfoPermutation,
) -> FastOrdinalDiagnostics:
    event_count = len(info_permutation)
    strict: list[tuple[int, int]] = []
    relation = [[False] * event_count for _ in range(event_count)]
    for left, left_value in enumerate(info_permutation):
        for right in range(left + 1, event_count):
            if left_value < info_permutation[right]:
                relation[left][right] = True
                strict.append((left, right))

    cover_relations: list[tuple[int, int]] = []
    for left, right in strict:
        if not any(
            relation[left][middle] and relation[middle][right]
            for middle in range(left + 1, right)
        ):
            cover_relations.append((left, right))

    ranks = [1] * event_count
    for right in range(event_count):
        ranks[right] = 1 + max(
            (
                ranks[left]
                for left in range(right)
                if relation[left][right]
            ),
            default=0,
        )
    height = max(ranks, default=0)
    width = _longest_decreasing_subsequence_length(info_permutation)
    rank_profile = tuple(
        sum(1 for rank in ranks if rank == level)
        for level in range(1, height + 1)
    )

    interval_counts: Counter[int] = Counter()
    profiles_by_size: dict[int, set[tuple[int, int]]] = {}
    for left, right in strict:
        interior = tuple(
            middle
            for middle in range(left + 1, right)
            if relation[left][middle] and relation[middle][right]
        )
        size = len(interior)
        interval_counts[size] += 1
        if not interior:
            profile = (0, 0)
        else:
            interior_values = tuple(info_permutation[index] for index in interior)
            profile = (
                _longest_increasing_subsequence_length(interior_values),
                _longest_decreasing_subsequence_length(interior_values),
            )
        profiles_by_size.setdefault(size, set()).add(profile)

    profile_spread = any(
        size >= 2 and len(profiles) > 1
        for size, profiles in profiles_by_size.items()
    )
    cover_degree = [0] * event_count
    for left, right in cover_relations:
        cover_degree[left] += 1
        cover_degree[right] += 1

    strict_pair_count = len(strict)
    cover_relation_count = len(cover_relations)
    cover_hub = (
        Fraction(max(cover_degree, default=0), event_count - 1)
        if event_count > 1
        else Fraction(0, 1)
    )
    link_density = _fraction(cover_relation_count, strict_pair_count)

    classification, passed = _t126_classification(
        event_count=event_count,
        strict_pair_count=strict_pair_count,
        cover_hub=cover_hub,
        link_density=link_density,
        height=height,
        width=width,
        profile_spread=profile_spread,
    )

    return FastOrdinalDiagnostics(
        event_count=event_count,
        classification=classification,
        t126_filter_passed=passed,
        strict_pair_count=strict_pair_count,
        cover_relation_count=cover_relation_count,
        height=height,
        width=width,
        rank_profile=rank_profile,
        interval_counts_by_size=tuple(sorted(interval_counts.items())),
        largest_interval_size=max(interval_counts, default=0),
        largest_cover_hub_fraction=cover_hub,
        link_density=link_density,
        profile_spread_obstruction=profile_spread,
    )


@lru_cache(maxsize=None)
def _deletion_summary(info_permutation: InfoPermutation) -> DeletionSummary:
    event_count = len(info_permutation)
    thin_count = 0
    relaxed_interval3_count = 0
    t253_t126_band_count = 0
    t252_style_count = 0
    for removed_index in range(event_count):
        sub_permutation = _normalize(
            info_permutation[:removed_index] + info_permutation[removed_index + 1 :]
        )
        diagnostics = _diagnostics_for_permutation(sub_permutation)
        band_passed = _ordering_band_passed(
            diagnostics.strict_pair_count,
            event_count - 1,
        )
        if band_passed and diagnostics.largest_interval_size <= THIN_INTERVAL_CAP:
            thin_count += 1
        if band_passed and diagnostics.largest_interval_size <= T252_INTERVAL_CAP:
            relaxed_interval3_count += 1
        if diagnostics.t126_filter_passed and band_passed:
            t253_t126_band_count += 1
            if _passes_t252_parent_cap(diagnostics):
                t252_style_count += 1
    return DeletionSummary(
        deletion_count=event_count,
        t159_thin_deletion_pass_count=thin_count,
        relaxed_interval3_deletion_pass_count=relaxed_interval3_count,
        t253_t126_band_deletion_pass_count=t253_t126_band_count,
        t252_style_deletion_pass_count=t252_style_count,
    )


def task_result_to_dict(result: TaskResult) -> dict[str, Any]:
    return {
        "task_id": result.task_id,
        "title": result.title,
        "metrics": [
            {"name": metric.name, "value": _value_to_json(metric.value)}
            for metric in result.metrics
        ],
        "verdict": result.verdict,
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


def _task(
    task_id: str,
    title: str,
    metrics: tuple[Metric, ...],
    verdict: str,
    strongest_claim: str,
    improved: str,
    weakened_or_falsified: str,
    falsification_condition: str,
    s1_update: str,
    claim_ledger_update: str,
    open_blocker: str,
    suggested_next: str,
) -> TaskResult:
    return TaskResult(
        task_id=task_id,
        title=title,
        metrics=metrics,
        verdict=verdict,
        strongest_claim=strongest_claim,
        improved=improved,
        weakened_or_falsified=weakened_or_falsified,
        falsification_condition=falsification_condition,
        s1_update=s1_update,
        claim_ledger_update=claim_ledger_update,
        open_blocker=open_blocker,
        suggested_next=suggested_next,
        not_claimed=NOT_CLAIMED,
    )


def _passes_t252_parent_cap(diagnostics: FastOrdinalDiagnostics) -> bool:
    return (
        diagnostics.t126_filter_passed
        and _ordering_band_passed(
            diagnostics.strict_pair_count,
            diagnostics.event_count,
        )
        and diagnostics.largest_interval_size <= T252_INTERVAL_CAP
        and diagnostics.largest_cover_hub_fraction <= T252_COVER_HUB_CAP
    )


def _shape_signature(diagnostics: FastOrdinalDiagnostics) -> tuple[Any, ...]:
    return (
        diagnostics.strict_pair_count,
        diagnostics.cover_relation_count,
        diagnostics.height,
        diagnostics.width,
        diagnostics.rank_profile,
        diagnostics.largest_interval_size,
        diagnostics.largest_cover_hub_fraction,
    )


def _t126_classification(
    *,
    event_count: int,
    strict_pair_count: int,
    cover_hub: Fraction,
    link_density: Fraction,
    height: int,
    width: int,
    profile_spread: bool,
) -> tuple[str, bool]:
    if cover_hub >= Fraction(3, 4):
        return "hub_nonlocality_obstruction", False
    if height == event_count or width == event_count:
        return "rank_width_obstruction", False
    if profile_spread:
        return "order_dimension_obstruction", False
    if height <= 2 and strict_pair_count >= event_count and link_density >= Fraction(9, 10):
        return "interval_profile_obstruction", False
    return "passes_filter_only", True


def _ordering_band_passed(strict_pair_count: int, event_count: int) -> bool:
    pair_limit = event_count * (event_count - 1) // 2
    return abs(_fraction(strict_pair_count, pair_limit) - Fraction(1, 2)) <= Fraction(1, 10)


@lru_cache(maxsize=None)
def _longest_increasing_subsequence_length(values: InfoPermutation) -> int:
    lengths = [1] * len(values)
    for right, right_value in enumerate(values):
        best = 1
        for left in range(right):
            if values[left] < right_value and lengths[left] + 1 > best:
                best = lengths[left] + 1
        lengths[right] = best
    return max(lengths, default=0)


@lru_cache(maxsize=None)
def _longest_decreasing_subsequence_length(values: InfoPermutation) -> int:
    lengths = [1] * len(values)
    for right, right_value in enumerate(values):
        best = 1
        for left in range(right):
            if values[left] > right_value and lengths[left] + 1 > best:
                best = lengths[left] + 1
        lengths[right] = best
    return max(lengths, default=0)


def _normalize(values: InfoPermutation) -> InfoPermutation:
    ranks = {value: rank for rank, value in enumerate(sorted(values), start=1)}
    return tuple(ranks[value] for value in values)


def _append_representative(
    representatives: list[InfoPermutation],
    info_permutation: InfoPermutation,
    *,
    limit: int = 5,
) -> None:
    if len(representatives) < limit:
        representatives.append(info_permutation)


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _value_to_json(value: Any) -> Any:
    if isinstance(value, Fraction):
        return _fraction_to_dict(value)
    if isinstance(value, FastOrdinalDiagnostics):
        return _diagnostics_to_dict(value)
    if isinstance(value, DeletionSummary):
        return {
            "deletion_count": value.deletion_count,
            "t159_thin_deletion_pass_count": value.t159_thin_deletion_pass_count,
            "relaxed_interval3_deletion_pass_count": (
                value.relaxed_interval3_deletion_pass_count
            ),
            "t253_t126_band_deletion_pass_count": (
                value.t253_t126_band_deletion_pass_count
            ),
            "t252_style_deletion_pass_count": value.t252_style_deletion_pass_count,
        }
    if isinstance(value, tuple):
        if _looks_like_distribution(value):
            return _distribution_to_json(value)
        return [_value_to_json(item) for item in value]
    if isinstance(value, list):
        return [_value_to_json(item) for item in value]
    return value


def _looks_like_distribution(value: tuple[Any, ...]) -> bool:
    return bool(value) and all(
        isinstance(item, tuple) and len(item) == 2 and isinstance(item[1], int)
        for item in value
    )


def _distribution_to_json(distribution: tuple[tuple[Any, int], ...]) -> list[dict[str, Any]]:
    return [
        {"value": _value_to_json(value), "count": count}
        for value, count in distribution
    ]


def _diagnostics_to_dict(diagnostics: FastOrdinalDiagnostics) -> dict[str, Any]:
    return {
        "event_count": diagnostics.event_count,
        "classification": diagnostics.classification,
        "t126_filter_passed": diagnostics.t126_filter_passed,
        "strict_pair_count": diagnostics.strict_pair_count,
        "cover_relation_count": diagnostics.cover_relation_count,
        "height": diagnostics.height,
        "width": diagnostics.width,
        "rank_profile": list(diagnostics.rank_profile),
        "interval_counts_by_size": [
            {"size": size, "count": count}
            for size, count in diagnostics.interval_counts_by_size
        ],
        "largest_interval_size": diagnostics.largest_interval_size,
        "largest_cover_hub_fraction": _fraction_to_dict(
            diagnostics.largest_cover_hub_fraction
        ),
        "link_density": _fraction_to_dict(diagnostics.link_density),
        "profile_spread_obstruction": diagnostics.profile_spread_obstruction,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}
