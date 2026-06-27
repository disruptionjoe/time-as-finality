"""T280-T311: finite selection-measure audit for the T252-style n=9 tail.

T264-T279 answered the uniform exact n=9 question: the T252-style
deletion-stable tail exists, but it has only 10 labeled cases. T278/T279 then
made the next task explicit: stop adding uniform-count evidence and test whether
any non-uniform finite selection rule actually concentrates weight on that
tail.

This module audits a small, declared family of hard gates and soft integer
weights over the exact n=9 ordinal ensemble. It is a finite process diagnostic,
not a physical measure, continuum limit, sprinkling result, or S1 upgrade.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from typing import Any

from models.t256_t263_ordinal_neighborhood_diagnostics import _mutation_shapes
from models.t264_t279_nine_event_ordinal_exact_count import (
    SELECTED_T252_RANK_PERMUTATION,
    T252_COVER_HUB_CAP,
    T252_INTERVAL_CAP,
    DeletionSummary,
    FastOrdinalDiagnostics,
    InfoPermutation,
    _deletion_summary,
    _diagnostics_for_permutation,
    _fraction,
    _ordering_band_passed,
    _passes_t252_parent_cap,
)


NINE_EVENT_COUNT = 9
TARGET_TAIL_COUNT = 10

NOT_CLAIMED = (
    "These finite selection audits do not define a physical measure, estimate "
    "dimension, prove faithful embedding, validate random sprinkling, derive "
    "metric structure, establish a continuum limit, or settle S1."
)


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


@dataclass(frozen=True)
class CaseFlags:
    t126_band_passed: bool
    interval3_parent: bool
    low_cover_parent: bool
    t253_deletion_band_stable: bool
    relaxed_interval3_deletion_stable: bool
    t252_parent_cap: bool
    t252_style_deletion_stable: bool


@dataclass(frozen=True)
class MeasureSummary:
    name: str
    description: str
    total_weight: int
    tail_weight: int
    parent_cap_weight: int
    selected_t252_weight: int
    tail_probability: Fraction
    parent_cap_probability: Fraction
    selected_t252_probability: Fraction
    tail_lift_vs_uniform: Fraction
    tautological: bool


@dataclass(frozen=True)
class SelectionAudit:
    total_cases: int
    feature_counts: tuple[tuple[str, int], ...]
    intersection_counts: tuple[tuple[str, int], ...]
    t252_parent_deletion_pass_distribution: tuple[tuple[int, int], ...]
    t252_parent_signature_distribution: tuple[tuple[tuple[Any, ...], int], ...]
    t252_tail_signature_distribution: tuple[tuple[tuple[Any, ...], int], ...]
    t252_tail_permutations: tuple[InfoPermutation, ...]
    selected_t252_flags: CaseFlags
    selected_t252_diagnostics: FastOrdinalDiagnostics
    selected_t252_deletion_summary: DeletionSummary
    measure_summaries: tuple[MeasureSummary, ...]
    tail_symmetry_counts: tuple[tuple[str, int], ...]
    t255_t252_style_neighbor_count: int


def run_t280_t311_analyses() -> tuple[TaskResult, ...]:
    audit = _selection_audit()
    measures = {summary.name: summary for summary in audit.measure_summaries}
    features = dict(audit.feature_counts)
    intersections = dict(audit.intersection_counts)

    tasks = [
        _task(
            "T280",
            "Selection Target Declaration",
            (
                Metric("total_cases", audit.total_cases),
                Metric("target_tail_count", features["t252_style_tail"]),
                Metric("selected_t252_in_tail", audit.selected_t252_flags.t252_style_deletion_stable),
                Metric("target_definition", "T126+T156, parent interval<=3, cover hub<=2/7, and every deletion satisfies the same gate"),
            ),
            "t252_style_tail_declared_for_selection_audit",
            "The selection target is the exact 10-case T252-style deletion-stable tail from T272.",
            "T280 turns the next route into an explicit target rather than a vague request for a better measure.",
            "It weakens any hidden-target analysis: the target is declared before comparing measures.",
            "T280 fails if the target differs from the T272 tail definition.",
            "S1 is unchanged; declaring a finite target is not a physical measure.",
            "Do not update the claim ledger from T280 alone.",
            "No natural weighting rule has been supplied yet.",
            "Audit hard gates and soft weights against the declared tail.",
        ),
        _task(
            "T281",
            "T279 Count Reproduction",
            (
                Metric("t126_band_count", features["t126_band"]),
                Metric("t253_deletion_band_stable_count", features["t253_deletion_band_stable"]),
                Metric("t252_parent_cap_count", features["t252_parent_cap"]),
                Metric("t252_style_tail_count", features["t252_style_tail"]),
            ),
            "selection_audit_reproduces_t279_tail_counts",
            "The selection audit reproduces the T279 spine: 143435 band positives, 8339 T253-style stable cases, 66 T252-style parents, and 10 T252-style stable cases.",
            "This validates that the measure audit is using the same exact n=9 denominator.",
            "It weakens concern that selection results come from a shifted target.",
            "T281 fails if any count disagrees with T264-T279 under the same gates.",
            "S1 is unchanged; this is a regression guard.",
            "Do not update the claim ledger from T281 alone.",
            "Matching prior counts still does not define a physical measure.",
            "Use the reproduced counts as the baseline for measure lift.",
        ),
        _measure_task("T282", "Uniform Baseline", measures["uniform"], "uniform_tail_baseline_is_tiny"),
        _measure_task("T283", "T126 Plus T156 Conditioning", measures["band"], "band_conditioning_barely_lifts_tail"),
        _measure_task("T284", "T253 Deletion-Band Conditioning", measures["t253"], "deletion_band_conditioning_lifts_but_stays_broad"),
        _measure_task("T285", "Interval-3 Conditioning", measures["interval3"], "interval3_conditioning_stays_too_broad"),
        _measure_task("T286", "Low-Cover Conditioning", measures["lowcover"], "low_cover_is_best_single_hard_gate"),
        _measure_task("T287", "T252 Parent-Cap Conditioning", measures["parentcap"], "parent_cap_concentrates_but_does_not_isolate_tail"),
        _measure_task("T288", "Tautological Tail Conditioning", measures["tail"], "tail_conditioning_is_upper_bound_only"),
        _task(
            "T289",
            "Interval Feature Ablation",
            (
                Metric("interval3_parent_count", features["interval3_parent"]),
                Metric("tail_count_inside_interval3", features["t252_style_tail"]),
                Metric("tail_probability_after_interval3", measures["interval3"].tail_probability),
            ),
            "interval_feature_alone_is_too_permissive",
            "The interval<=3 parent feature admits 91350 cases, so it cannot explain the 10-case tail by itself.",
            "T289 separates T252's interval behavior from its cover and deletion behavior.",
            "It weakens interval-only selection stories.",
            "T289 fails if interval<=3 is not evaluated after T126+T156.",
            "S1 is unchanged; interval caps are finite screens.",
            "Do not update the claim ledger from T289 alone.",
            "Interval caps alone are far from a natural measure.",
            "Pair interval caps with cover and deletion features.",
        ),
        _task(
            "T290",
            "Cover Feature Ablation",
            (
                Metric("low_cover_parent_count", features["low_cover_parent"]),
                Metric("tail_count_inside_low_cover", features["t252_style_tail"]),
                Metric("tail_probability_after_low_cover", measures["lowcover"].tail_probability),
            ),
            "cover_feature_is_strong_but_not_sufficient",
            "The low-cover parent feature leaves 185 cases and is the strongest single hard gate, but it still contains many non-tail cases.",
            "T290 identifies cover sparsity as the main non-tautological selection signal.",
            "It weakens pure ordering-fraction or interval-only routes.",
            "T290 fails if the cover threshold differs from T257's cap.",
            "S1 is unchanged; cover sparsity is not a physical law.",
            "Do not update the claim ledger from T290 alone.",
            "Cover sparsity needs a reason, not just a threshold.",
            "Combine cover with interval and deletion gates.",
        ),
        _task(
            "T291",
            "Deletion-Band Ablation",
            (
                Metric("t253_deletion_band_stable_count", features["t253_deletion_band_stable"]),
                Metric("tail_probability_after_t253", measures["t253"].tail_probability),
            ),
            "deletion_band_stability_is_broad",
            "T253-style deletion-band stability leaves 8339 cases, so deletion-band stability alone does not recover the T252-style shape.",
            "T291 locates T253 as a robustness filter, not a locality selector.",
            "It weakens deletion-stability-only optimism.",
            "T291 fails if deletion suborders are not rank-normalized restrictions.",
            "S1 remains guarded.",
            "Do not update the claim ledger from T291 alone.",
            "Deletion-band stability needs shape constraints to become selective.",
            "Add interval and cover features.",
        ),
        _task(
            "T292",
            "Interval Plus Cover Pair",
            (
                Metric("interval_and_cover_count", intersections["interval3_and_lowcover"]),
                Metric("tail_probability_after_interval_cover", measures["parentcap"].tail_probability),
            ),
            "interval_cover_pair_is_the_best_parent_gate",
            "The interval<=3 plus low-cover pair is exactly the 66-case T252 parent cap.",
            "T292 shows that T252's parent rarity is a two-feature effect.",
            "It weakens any single-feature account of the selected witness.",
            "T292 fails if the pair count differs from the T271 parent cap.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T292 alone.",
            "The parent gate still has 56 false positives before deletion stability.",
            "Apply deletion stability to the parent gate.",
        ),
        _task(
            "T293",
            "Interval Plus Deletion Pair",
            (
                Metric("interval_and_t253_count", intersections["interval3_and_t253"]),
                Metric("target_tail_count", features["t252_style_tail"]),
            ),
            "interval_deletion_pair_remains_broad",
            "Interval<=3 plus T253 deletion-band stability leaves 7901 cases.",
            "T293 shows that deletion stability mostly tracks the interval-relaxed population, not the tiny T252 tail.",
            "It weakens interval+deletion selection stories without cover sparsity.",
            "T293 fails if the pair uses the wrong deletion target.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T293 alone.",
            "The cover feature is still required.",
            "Compare cover+deletion next.",
        ),
        _task(
            "T294",
            "Cover Plus Deletion Pair",
            (
                Metric("cover_and_t253_count", intersections["lowcover_and_t253"]),
                Metric("target_tail_count", features["t252_style_tail"]),
            ),
            "cover_deletion_pair_nearly_isolates_tail",
            "Low-cover plus T253 deletion-band stability leaves 16 cases, much closer to the 10-case tail.",
            "T294 identifies cover+deletion as the strongest non-parent pair.",
            "It weakens interval-first narratives: cover plus deletion does most of the work.",
            "T294 fails if cover and deletion are not evaluated on the same parent/deletion relations.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T294 alone.",
            "Six false positives remain without the interval cap.",
            "Use the full interval+cover+deletion gate as the target boundary.",
        ),
        _task(
            "T295",
            "Interval Cover Deletion Triple",
            (
                Metric("interval_cover_t253_count", intersections["interval3_lowcover_t253"]),
                Metric("t252_style_tail_count", features["t252_style_tail"]),
            ),
            "interval_cover_deletion_triple_matches_t252_tail",
            "The interval+cover+deletion triple leaves exactly the 10 T252-style stable cases.",
            "T295 shows which finite ingredients isolate the selected tail.",
            "It weakens broader finite-gate optimism: isolating the tail requires all three ingredients.",
            "T295 fails if the triple no longer equals the T272 tail.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T295 alone.",
            "The triple is still a target definition, not a derived measure.",
            "Test soft weights that use these features without hard-targeting the tail.",
        ),
        _measure_task("T296", "Parent Soft Score", measures["parent_soft"], "parent_soft_score_lifts_tail_weakly"),
        _measure_task("T297", "Deletion Soft Score", measures["deletion_soft"], "deletion_soft_score_lifts_tail_more_but_not_enough"),
        _measure_task("T298", "Anti-Parent Control Score", measures["anti_parent"], "anti_parent_control_suppresses_tail"),
        _measure_task("T299", "Selected Shape Soft Score", measures["shape_soft"], "shape_soft_score_enriches_selected_tail_but_stays_broad"),
        _task(
            "T300",
            "Selected T252 Singleton Probabilities",
            tuple(
                Metric(summary.name, summary.selected_t252_probability)
                for summary in audit.measure_summaries
                if summary.name in {"uniform", "lowcover", "parentcap", "deletion_soft", "shape_soft"}
            ),
            "selected_singleton_remains_measure_sensitive",
            "The selected T252 permutation remains a singleton inside every non-tautological measure; even parent-cap conditioning gives it probability only 1/66.",
            "T300 keeps the analysis from mistaking a tail measure for a selected-witness measure.",
            "It weakens over-reading of the specific T252 permutation.",
            "T300 fails if selected probabilities are computed outside the same n=9 denominator.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T300 alone.",
            "No rule selects the specific T252 witness rather than the tail.",
            "Audit tail symmetry and shape structure.",
        ),
        _task(
            "T301",
            "Tail Symmetry Audit",
            (
                Metric("tail_symmetry_counts", audit.tail_symmetry_counts),
                Metric("tail_count", features["t252_style_tail"]),
            ),
            "tail_closed_under_inverse_and_reverse_complement",
            "The 10-case tail is closed under inverse and reverse-complement transforms, but not under reverse or complement alone.",
            "T301 adds invariant structure to the target tail.",
            "It weakens a purely accidental-list reading of the 10 cases.",
            "T301 fails if transform definitions are changed after seeing the result.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T301 alone.",
            "Finite symmetry is not a physical selection rule.",
            "Inspect shape signatures next.",
        ),
        _task(
            "T302",
            "Tail Shape Signature Distribution",
            (
                Metric("tail_signature_distribution", audit.t252_tail_signature_distribution),
                Metric("parent_signature_distribution", audit.t252_parent_signature_distribution),
            ),
            "tail_has_five_shape_signatures",
            "The 10-case tail occupies five parent shape signatures, so it is narrow but not a single shape.",
            "T302 prevents treating the tail as one rigid poset.",
            "It weakens both singleton and broad-family readings.",
            "T302 fails if signatures do not include strict pairs, covers, height, width, rank profile, interval cap, and cover hub.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T302 alone.",
            "The shape signatures still lack a generative explanation.",
            "Record representatives for future measure proposals.",
        ),
        _task(
            "T303",
            "Tail Representative List",
            (
                Metric("t252_tail_permutations", audit.t252_tail_permutations),
                Metric("selected_t252_rank_permutation", SELECTED_T252_RANK_PERMUTATION),
            ),
            "tail_representatives_recorded",
            "All 10 T252-style stable permutations are recorded for future selection-measure work.",
            "T303 makes the target tail inspectable rather than just counted.",
            "It weakens ambiguity about which cases a later measure must support.",
            "T303 fails if the representative list length differs from 10.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T303 alone.",
            "A list of finite representatives is not a measure.",
            "Analyze false positives at the parent cap.",
        ),
        _task(
            "T304",
            "Parent-Cap False Positive Burden",
            (
                Metric("parent_cap_count", features["t252_parent_cap"]),
                Metric("tail_count", features["t252_style_tail"]),
                Metric("false_positive_count", features["t252_parent_cap"] - features["t252_style_tail"]),
                Metric("t252_parent_deletion_pass_distribution", audit.t252_parent_deletion_pass_distribution),
            ),
            "parent_cap_has_fifty_six_false_positives",
            "The 66-case parent cap contains 56 cases that fail full T252-style deletion stability.",
            "T304 shows the parent gate is not enough; deletion behavior is decisive.",
            "It weakens parent-shape-only selection proposals.",
            "T304 fails if deletion pass counts are not computed for every parent-cap case.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T304 alone.",
            "The false positives need either a principled exclusion or a broader target.",
            "Rank hard gates and soft measures.",
        ),
        _task(
            "T305",
            "Low-Cover Bottleneck",
            (
                Metric("low_cover_parent_count", features["low_cover_parent"]),
                Metric("parent_cap_count", features["t252_parent_cap"]),
                Metric("tail_count", features["t252_style_tail"]),
            ),
            "low_cover_is_the_main_bottleneck_before_deletion",
            "Low cover reduces the band-positive set to 185 cases; interval then reduces it to 66, and deletion to 10.",
            "T305 identifies the sequence of bottlenecks in the finite target.",
            "It weakens stories centered only on ordering fraction or interval size.",
            "T305 fails if the bottleneck counts use different parent filters.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T305 alone.",
            "The bottleneck still needs a non-ad hoc source.",
            "Compare local T255 behavior against the global bottleneck.",
        ),
        _task(
            "T306",
            "T255 Local Vs Selection Tail",
            (
                Metric("t255_t252_style_neighbor_count", audit.t255_t252_style_neighbor_count),
                Metric("global_t252_parent_cap_count", features["t252_parent_cap"]),
                Metric("global_t252_style_tail_count", features["t252_style_tail"]),
            ),
            "t255_neighbors_do_not_preserve_t252_style_cap",
            "None of the 36 one-swap T255 neighbors satisfy the T252-style parent cap, even though the global ensemble has 66 parent-cap cases.",
            "T306 explains why local mutation abundance did not become a selection measure.",
            "It weakens local-neighborhood optimism.",
            "T306 fails if the T255 neighborhood is not the one-transposition neighborhood of T252.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T306 alone.",
            "The target tail is locally fragile under one-swap moves.",
            "Rank the hard and soft candidates.",
        ),
        _task(
            "T307",
            "Hard Gate Ranking",
            (
                Metric("hard_gate_ranking", _hard_gate_ranking(audit)),
            ),
            "best_non_tautological_hard_gate_is_parent_cap",
            "Among non-tautological hard gates, the T252 parent cap is best, raising tail probability to 5/33.",
            "T307 makes the finite hard-gate tradeoff explicit.",
            "It weakens weaker hard gates as serious selection candidates.",
            "T307 fails if tautological tail conditioning is ranked as acceptable.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T307 alone.",
            "The best non-tautological hard gate still leaves 56 false positives.",
            "Compare soft scores.",
        ),
        _task(
            "T308",
            "Soft Score Ranking",
            (
                Metric("soft_score_ranking", _soft_score_ranking(audit)),
            ),
            "soft_scores_enrich_but_do_not_concentrate_tail",
            "The tested soft integer scores enrich the target tail but stay far below the parent-cap hard gate.",
            "T308 separates smooth enrichment from actual concentration.",
            "It weakens soft-score optimism without a sharper derivation.",
            "T308 fails if soft scores include the target label while being reported as non-tautological.",
            "S1 is unchanged.",
            "Do not update the claim ledger from T308 alone.",
            "No tested soft score supplies a convincing added measure.",
            "Set a concentration threshold.",
        ),
        _task(
            "T309",
            "Concentration Threshold Audit",
            (
                Metric("best_non_tautological_tail_probability", measures["parentcap"].tail_probability),
                Metric("threshold", Fraction(1, 2)),
                Metric("passes_threshold", measures["parentcap"].tail_probability >= Fraction(1, 2)),
            ),
            "no_non_tautological_candidate_reaches_half_mass",
            "No non-tautological candidate tested here puts even half its mass on the 10-case tail.",
            "T309 gives a clear stop condition for this finite measure family.",
            "It weakens the current candidate family as an S1 rescue.",
            "T309 fails if a non-tautological candidate exceeds the declared threshold.",
            "S1 remains requires_added_assumption.",
            "Do not update the claim ledger from T309 alone.",
            "A stronger, principled measure is still missing.",
            "Reject tautological tail conditioning as a physical answer.",
        ),
        _task(
            "T310",
            "Tautology Guardrail",
            (
                Metric("tail_conditioned_probability", measures["tail"].tail_probability),
                Metric("tail_conditioned_tautological", measures["tail"].tautological),
            ),
            "tail_conditioning_rejected_as_measure_answer",
            "Conditioning directly on the target tail gives probability 1, but it is tautological and not a selection explanation.",
            "T310 keeps the added-assumption route honest.",
            "It weakens any attempt to relabel the target definition as a measure.",
            "T310 fails if target-conditioned weighting is treated as a physical or explanatory measure.",
            "S1 remains requires_added_assumption.",
            "Do not update the claim ledger from T310 alone.",
            "The actual non-uniform finality-colimit measure remains unbuilt.",
            "State the synthesis and next task.",
        ),
        _task(
            "T311",
            "Thirty-Two Task Selection Audit Synthesis",
            (
                Metric("completed_task_count", 32),
                Metric("target_tail_count", features["t252_style_tail"]),
                Metric("best_non_tautological_hard_gate", "parentcap"),
                Metric("best_non_tautological_tail_probability", measures["parentcap"].tail_probability),
                Metric("round_verdict", "selection_measure_candidates_insufficient_without_new_principle"),
            ),
            "selection_measure_candidates_insufficient_without_new_principle",
            "T280-T311 complete a 32-task finite selection audit: current hard and soft candidates can enrich the T252-style tail, but none gives a non-tautological physical selection measure.",
            "The round turns the post-n=9 open blocker into concrete evidence about which finite gates matter.",
            "It weakens the idea that the T252-style tail can be rescued by obvious finite reweighting alone.",
            "T311 fails if a tested non-tautological measure actually concentrates most mass on the tail.",
            "S1 remains requires_added_assumption for the finite ordinal route.",
            "Safe future wording: finite selection probes identify cover sparsity plus deletion stability as necessary bottlenecks, but no natural non-uniform measure has been derived.",
            "The missing object is still a principled finality-colimit measure or a different continuum bridge.",
            "Next build or reject a principled non-uniform measure from finality-domain data rather than from post-hoc tail labels.",
        ),
    ]
    if len(tasks) != 32:
        raise AssertionError("T280-T311 should contain exactly 32 tasks")
    return tuple(tasks)


@lru_cache(maxsize=1)
def _selection_audit() -> SelectionAudit:
    feature_counts: Counter[str] = Counter()
    intersection_counts: Counter[str] = Counter()
    parent_deletion_pass_distribution: Counter[int] = Counter()
    parent_signature_distribution: Counter[tuple[Any, ...]] = Counter()
    tail_signature_distribution: Counter[tuple[Any, ...]] = Counter()
    tail_permutations: list[InfoPermutation] = []
    measure_accumulators = {
        name: {"total": 0, "tail": 0, "parent": 0, "selected": 0}
        for name in _measure_descriptions()
    }

    selected_flags: CaseFlags | None = None
    selected_diagnostics: FastOrdinalDiagnostics | None = None
    selected_deletion_summary: DeletionSummary | None = None

    for info_permutation in permutations(range(1, NINE_EVENT_COUNT + 1)):
        diagnostics = _diagnostics_for_permutation(info_permutation)
        flags, deletion_summary = _case_flags(info_permutation, diagnostics)
        feature_counts["total"] += 1
        feature_counts["t126_band"] += flags.t126_band_passed
        feature_counts["interval3_parent"] += flags.interval3_parent
        feature_counts["low_cover_parent"] += flags.low_cover_parent
        feature_counts["t253_deletion_band_stable"] += flags.t253_deletion_band_stable
        feature_counts["relaxed_interval3_deletion_stable"] += (
            flags.relaxed_interval3_deletion_stable
        )
        feature_counts["t252_parent_cap"] += flags.t252_parent_cap
        feature_counts["t252_style_tail"] += flags.t252_style_deletion_stable

        intersection_counts["interval3_and_lowcover"] += (
            flags.interval3_parent and flags.low_cover_parent
        )
        intersection_counts["interval3_and_t253"] += (
            flags.interval3_parent and flags.t253_deletion_band_stable
        )
        intersection_counts["lowcover_and_t253"] += (
            flags.low_cover_parent and flags.t253_deletion_band_stable
        )
        intersection_counts["interval3_lowcover_t253"] += (
            flags.interval3_parent
            and flags.low_cover_parent
            and flags.t253_deletion_band_stable
        )

        if flags.t252_parent_cap and deletion_summary is not None:
            signature = _shape_signature(diagnostics)
            parent_signature_distribution[signature] += 1
            parent_deletion_pass_distribution[
                deletion_summary.t252_style_deletion_pass_count
            ] += 1
            if flags.t252_style_deletion_stable:
                tail_signature_distribution[signature] += 1
                tail_permutations.append(info_permutation)

        if info_permutation == SELECTED_T252_RANK_PERMUTATION:
            selected_flags = flags
            selected_diagnostics = diagnostics
            if deletion_summary is None:
                raise AssertionError("selected T252 should have a deletion summary")
            selected_deletion_summary = deletion_summary

        weights = _measure_weights(flags, diagnostics)
        for name, weight in weights.items():
            acc = measure_accumulators[name]
            acc["total"] += weight
            if flags.t252_style_deletion_stable:
                acc["tail"] += weight
            if flags.t252_parent_cap:
                acc["parent"] += weight
            if info_permutation == SELECTED_T252_RANK_PERMUTATION:
                acc["selected"] += weight

    if selected_flags is None or selected_diagnostics is None or selected_deletion_summary is None:
        raise AssertionError("selected T252 permutation was not found")

    tail_tuple = tuple(tail_permutations)
    tail_count = len(tail_tuple)
    descriptions = _measure_descriptions()
    measure_summaries = tuple(
        _measure_summary(
            name=name,
            description=descriptions[name],
            total_cases=feature_counts["total"],
            tail_count=tail_count,
            tautological=(name == "tail"),
            **measure_accumulators[name],
        )
        for name in descriptions
    )
    return SelectionAudit(
        total_cases=feature_counts["total"],
        feature_counts=tuple(sorted(feature_counts.items())),
        intersection_counts=tuple(sorted(intersection_counts.items())),
        t252_parent_deletion_pass_distribution=tuple(
            sorted(parent_deletion_pass_distribution.items())
        ),
        t252_parent_signature_distribution=tuple(
            sorted(parent_signature_distribution.items(), key=lambda item: repr(item[0]))
        ),
        t252_tail_signature_distribution=tuple(
            sorted(tail_signature_distribution.items(), key=lambda item: repr(item[0]))
        ),
        t252_tail_permutations=tail_tuple,
        selected_t252_flags=selected_flags,
        selected_t252_diagnostics=selected_diagnostics,
        selected_t252_deletion_summary=selected_deletion_summary,
        measure_summaries=measure_summaries,
        tail_symmetry_counts=_tail_symmetry_counts(tail_tuple),
        t255_t252_style_neighbor_count=_t255_t252_style_neighbor_count(),
    )


def _case_flags(
    info_permutation: InfoPermutation,
    diagnostics: FastOrdinalDiagnostics | None = None,
) -> tuple[CaseFlags, DeletionSummary | None]:
    if diagnostics is None:
        diagnostics = _diagnostics_for_permutation(info_permutation)
    band = diagnostics.t126_filter_passed and _ordering_band_passed(
        diagnostics.strict_pair_count,
        diagnostics.event_count,
    )
    interval3_parent = band and diagnostics.largest_interval_size <= T252_INTERVAL_CAP
    low_cover_parent = (
        band and diagnostics.largest_cover_hub_fraction <= T252_COVER_HUB_CAP
    )
    deletion_summary = _deletion_summary(info_permutation) if band else None
    t253_stable = (
        deletion_summary is not None
        and deletion_summary.t253_t126_band_deletion_pass_count
        == diagnostics.event_count
    )
    relaxed_interval3_stable = (
        deletion_summary is not None
        and deletion_summary.relaxed_interval3_deletion_pass_count
        == diagnostics.event_count
    )
    parent_cap = _passes_t252_parent_cap(diagnostics)
    tail = (
        parent_cap
        and deletion_summary is not None
        and deletion_summary.t252_style_deletion_pass_count == diagnostics.event_count
    )
    return (
        CaseFlags(
            t126_band_passed=band,
            interval3_parent=interval3_parent,
            low_cover_parent=low_cover_parent,
            t253_deletion_band_stable=t253_stable,
            relaxed_interval3_deletion_stable=relaxed_interval3_stable,
            t252_parent_cap=parent_cap,
            t252_style_deletion_stable=tail,
        ),
        deletion_summary,
    )


def _measure_weights(
    flags: CaseFlags,
    diagnostics: FastOrdinalDiagnostics,
) -> dict[str, int]:
    return {
        "uniform": 1,
        "band": 1 if flags.t126_band_passed else 0,
        "t253": 1 if flags.t253_deletion_band_stable else 0,
        "interval3": 1 if flags.interval3_parent else 0,
        "lowcover": 1 if flags.low_cover_parent else 0,
        "parentcap": 1 if flags.t252_parent_cap else 0,
        "tail": 1 if flags.t252_style_deletion_stable else 0,
        "parent_soft": 2
        ** (
            int(flags.t126_band_passed)
            + int(flags.interval3_parent)
            + int(flags.low_cover_parent)
        ),
        "deletion_soft": 2
        ** (
            int(flags.t126_band_passed)
            + int(flags.interval3_parent)
            + int(flags.low_cover_parent)
            + int(flags.t253_deletion_band_stable)
            + int(flags.relaxed_interval3_deletion_stable)
        ),
        "anti_parent": 2
        ** (
            int(flags.t126_band_passed)
            + int(not flags.interval3_parent)
            + int(not flags.low_cover_parent)
        ),
        "shape_soft": 2
        ** (
            int(flags.t126_band_passed)
            + int(flags.interval3_parent)
            + int(flags.low_cover_parent)
            + int(diagnostics.height == 5)
            + int(diagnostics.width == 2)
            + int(diagnostics.cover_relation_count == 8)
            + int(diagnostics.strict_pair_count == 20)
        ),
    }


def _measure_descriptions() -> dict[str, str]:
    return {
        "uniform": "Uniform ordinal ensemble over all 9! permutations.",
        "band": "Hard conditioning on T126 plus the declared T156 ordering band.",
        "t253": "Hard conditioning on T253-style deletion-band stability.",
        "interval3": "Hard conditioning on T126+band and parent largest interval <= 3.",
        "lowcover": "Hard conditioning on T126+band and parent cover hub <= 2/7.",
        "parentcap": "Hard conditioning on the T252-style parent interval and cover cap.",
        "tail": "Hard conditioning directly on the T252-style deletion-stable target tail.",
        "parent_soft": "Soft integer score 2^(band + interval3 + lowcover).",
        "deletion_soft": "Soft integer score 2^(band + interval3 + lowcover + t253 + relaxed deletion interval3).",
        "anti_parent": "Control score 2^(band + not-interval3 + not-lowcover).",
        "shape_soft": "Soft score for T252-like parent shape labels without using the tail label.",
    }


def _measure_summary(
    *,
    name: str,
    description: str,
    total: int,
    tail: int,
    parent: int,
    selected: int,
    total_cases: int,
    tail_count: int,
    tautological: bool,
) -> MeasureSummary:
    return MeasureSummary(
        name=name,
        description=description,
        total_weight=total,
        tail_weight=tail,
        parent_cap_weight=parent,
        selected_t252_weight=selected,
        tail_probability=_fraction(tail, total),
        parent_cap_probability=_fraction(parent, total),
        selected_t252_probability=_fraction(selected, total),
        tail_lift_vs_uniform=_fraction(tail * total_cases, total * tail_count),
        tautological=tautological,
    )


def _measure_task(
    task_id: str,
    title: str,
    summary: MeasureSummary,
    verdict: str,
) -> TaskResult:
    return _task(
        task_id,
        title,
        (
            Metric("measure", summary.name),
            Metric("description", summary.description),
            Metric("total_weight", summary.total_weight),
            Metric("tail_weight", summary.tail_weight),
            Metric("tail_probability", summary.tail_probability),
            Metric("parent_cap_probability", summary.parent_cap_probability),
            Metric("selected_t252_probability", summary.selected_t252_probability),
            Metric("tail_lift_vs_uniform", summary.tail_lift_vs_uniform),
            Metric("tautological", summary.tautological),
        ),
        verdict,
        f"The `{summary.name}` measure gives the 10-case T252-style tail probability {summary.tail_probability}.",
        "This quantifies selection pressure as an exact finite weighted probability.",
        "It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.",
        f"{task_id} fails if the `{summary.name}` weights are changed without renaming the measure.",
        "S1 is unchanged; this is a finite selection audit only.",
        f"Do not update the claim ledger from {task_id} alone.",
        "A finite weighting rule is not yet a physical finality-colimit measure.",
        "Compare this measure against the hard-gate and soft-score rankings.",
    )


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


def _tail_symmetry_counts(
    tail_permutations: tuple[InfoPermutation, ...],
) -> tuple[tuple[str, int], ...]:
    tail = set(tail_permutations)
    transforms = {
        "reverse": _reverse_positions,
        "complement": _complement_values,
        "reverse_complement": lambda p: _complement_values(_reverse_positions(p)),
        "inverse": _inverse_permutation,
    }
    return tuple(
        (name, sum(1 for permutation in tail_permutations if transform(permutation) in tail))
        for name, transform in transforms.items()
    )


def _reverse_positions(permutation: InfoPermutation) -> InfoPermutation:
    return tuple(reversed(permutation))


def _complement_values(permutation: InfoPermutation) -> InfoPermutation:
    size = len(permutation)
    return tuple(size + 1 - value for value in permutation)


def _inverse_permutation(permutation: InfoPermutation) -> InfoPermutation:
    inverse = [0] * len(permutation)
    for index, value in enumerate(permutation, start=1):
        inverse[value - 1] = index
    return tuple(inverse)


def _t255_t252_style_neighbor_count() -> int:
    return sum(
        1
        for mutation in _mutation_shapes()
        if mutation.shape.t126_filter_passed
        and mutation.ordering_band_passed
        and mutation.shape.largest_interval_size <= T252_INTERVAL_CAP
        and mutation.shape.largest_cover_hub_fraction <= T252_COVER_HUB_CAP
    )


def _hard_gate_ranking(audit: SelectionAudit) -> tuple[MeasureSummary, ...]:
    hard_names = ("parentcap", "lowcover", "t253", "interval3", "band", "uniform")
    summaries = {
        summary.name: summary
        for summary in audit.measure_summaries
    }
    return tuple(
        sorted(
            (summaries[name] for name in hard_names),
            key=lambda summary: summary.tail_probability,
            reverse=True,
        )
    )


def _soft_score_ranking(audit: SelectionAudit) -> tuple[MeasureSummary, ...]:
    soft_names = ("shape_soft", "deletion_soft", "parent_soft", "anti_parent")
    summaries = {
        summary.name: summary
        for summary in audit.measure_summaries
    }
    return tuple(
        sorted(
            (summaries[name] for name in soft_names),
            key=lambda summary: summary.tail_probability,
            reverse=True,
        )
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


def _value_to_json(value: Any) -> Any:
    if isinstance(value, Fraction):
        return _fraction_to_dict(value)
    if isinstance(value, MeasureSummary):
        return _measure_summary_to_dict(value)
    if isinstance(value, FastOrdinalDiagnostics):
        return {
            "classification": value.classification,
            "strict_pair_count": value.strict_pair_count,
            "cover_relation_count": value.cover_relation_count,
            "height": value.height,
            "width": value.width,
            "rank_profile": list(value.rank_profile),
            "largest_interval_size": value.largest_interval_size,
            "largest_cover_hub_fraction": _fraction_to_dict(
                value.largest_cover_hub_fraction
            ),
        }
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


def _measure_summary_to_dict(summary: MeasureSummary) -> dict[str, Any]:
    return {
        "name": summary.name,
        "description": summary.description,
        "total_weight": summary.total_weight,
        "tail_weight": summary.tail_weight,
        "parent_cap_weight": summary.parent_cap_weight,
        "selected_t252_weight": summary.selected_t252_weight,
        "tail_probability": _fraction_to_dict(summary.tail_probability),
        "parent_cap_probability": _fraction_to_dict(summary.parent_cap_probability),
        "selected_t252_probability": _fraction_to_dict(
            summary.selected_t252_probability
        ),
        "tail_lift_vs_uniform": _fraction_to_dict(summary.tail_lift_vs_uniform),
        "tautological": summary.tautological,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}
