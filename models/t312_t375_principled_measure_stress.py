"""T312-T375: principled finite-measure stress tests for the T252 tail.

T280-T311 showed that obvious hard gates and soft scores enrich the 10-case
T252-style n=9 tail, but did not yet supply a non-tautological measure. This
round expands the search to local-action style weights built from declared
finite diagnostics: ordering-band status, cover sparsity, interval depth,
deletion stability counts, and T252-like parent shape labels.

The result is still finite and diagnostic. A high finite concentration is not a
physical measure unless it is derived from finality-domain dynamics rather than
chosen after seeing the target tail.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from typing import Any

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
from models.t280_t311_selection_measure_audit import _tail_symmetry_counts


NINE_EVENT_COUNT = 9
TAIL_COUNT = 10
UNIFORM_TAIL_PROBABILITY = Fraction(1, 36288)

NOT_CLAIMED = (
    "These finite measure stress tests do not define a physical measure, "
    "estimate dimension, prove faithful embedding, validate random sprinkling, "
    "derive metric structure, establish a continuum limit, or settle S1."
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
    band: bool
    interval3: bool
    lowcover: bool
    parentcap: bool
    t253_stable: bool
    relaxed_interval3_stable: bool
    tail: bool
    deletion_band_pass_count: int
    deletion_interval3_pass_count: int
    deletion_t252_pass_count: int


@dataclass(frozen=True)
class MeasureSummary:
    name: str
    description: str
    total_weight: int
    tail_weight: int
    parentcap_weight: int
    selected_weight: int
    tail_probability: Fraction
    parentcap_probability: Fraction
    selected_probability: Fraction
    lift_vs_uniform: Fraction
    uses_tail_label: bool
    empirical_target_equivalent: bool
    uses_deletion_t252_count: bool


@dataclass(frozen=True)
class MeasureStressAudit:
    total_cases: int
    feature_counts: tuple[tuple[str, int], ...]
    intersection_counts: tuple[tuple[str, int], ...]
    deletion_t252_pass_distribution: tuple[tuple[int, int], ...]
    parentcap_deletion_t252_pass_distribution: tuple[tuple[int, int], ...]
    parentcap_signature_distribution: tuple[tuple[tuple[Any, ...], int], ...]
    tail_signature_distribution: tuple[tuple[tuple[Any, ...], int], ...]
    tail_permutations: tuple[InfoPermutation, ...]
    tail_symmetry_counts: tuple[tuple[str, int], ...]
    selected_diagnostics: FastOrdinalDiagnostics
    selected_deletion_summary: DeletionSummary
    measure_summaries: tuple[MeasureSummary, ...]


MEASURE_DESCRIPTIONS: dict[str, str] = {
    "uniform": "Uniform ordinal ensemble over all 9! permutations.",
    "hard_band": "Hard gate: T126 plus T156 band.",
    "hard_interval3": "Hard gate: T126+band and parent largest interval <= 3.",
    "hard_lowcover": "Hard gate: T126+band and parent cover hub <= 2/7.",
    "hard_t253": "Hard gate: every deletion remains T126+band.",
    "hard_parentcap": "Hard gate: T252-style parent interval+cover cap.",
    "hard_interval_deletion": "Hard gate: interval<=3 and deletion-band stability.",
    "hard_cover_deletion": "Hard gate: low cover and deletion-band stability.",
    "hard_interval_cover_deletion": "Hard gate: interval<=3, low cover, and deletion-band stability.",
    "hard_tail": "Hard gate: condition directly on the T252-style tail.",
    "soft_parent_v1": "Soft score 2^(band + interval3 + lowcover).",
    "soft_parent_v2": "Soft score 3^(band + interval3 + lowcover).",
    "soft_deletion_binary": "Soft score 2^(band + interval3 + lowcover + t253 + relaxed deletion interval3).",
    "soft_d_count": "Soft score 2^(number of deletion-band passes).",
    "soft_r_count": "Soft score 2^(number of deletion interval<=3 passes).",
    "soft_s_count": "Soft score 2^(number of deletion T252-style passes).",
    "soft_non_tail_local": "Soft score 2^(band + interval3 + lowcover + min(T252 deletion pass count,4)).",
    "soft_non_tail_local_strong": "Soft score 2^(band + interval3 + lowcover + min(T252 deletion pass count,6)).",
    "soft_s_count_squared": "Soft score 4^(number of deletion T252-style passes).",
    "soft_parent_s_squared": "Soft score 4^(T252 deletion pass count) with a parent-cap multiplier.",
    "soft_s_count_cubed": "Soft score 8^(number of deletion T252-style passes).",
    "soft_cover_s_count": "Soft score 2^(T252 deletion pass count) with a low-cover multiplier.",
    "soft_interval_cover_s_count": "Soft score 2^(T252 deletion pass count) with an interval+cover multiplier.",
    "soft_rank_shape": "Soft score for T252-like parent shape labels.",
    "soft_t252_exact_parent_shape": "Soft score for exact selected-parent shape labels.",
    "soft_coverhub_inverse": "Soft score giving an 8x bonus to cover hub <= 1/4 inside the band.",
    "soft_interval_inverse": "Soft score giving an 8x bonus to interval<=3 inside the band.",
    "soft_anti_parent": "Control score favoring band cases that fail interval and cover caps.",
}


def run_t312_t375_analyses() -> tuple[TaskResult, ...]:
    audit = _measure_stress_audit()
    measures = {summary.name: summary for summary in audit.measure_summaries}
    features = dict(audit.feature_counts)
    intersections = dict(audit.intersection_counts)
    tasks: list[TaskResult] = []

    manual_specs = [
        (
            "T312",
            "Measure Stress Target",
            (
                Metric("total_cases", audit.total_cases),
                Metric("target_tail_count", features["tail"]),
                Metric("uniform_tail_probability", UNIFORM_TAIL_PROBABILITY),
            ),
            "measure_stress_target_declared",
            "The finite measure stress target is the same 10-case T252-style tail, with uniform probability 1/36288.",
            "T312 fixes the target before evaluating a larger candidate-measure family.",
            "It weakens hidden-target risk in this round.",
            "T312 fails if the target is not the T272/T311 tail.",
        ),
        (
            "T313",
            "Prior Count Reproduction",
            (
                Metric("band_count", features["band"]),
                Metric("t253_stable_count", features["t253_stable"]),
                Metric("parentcap_count", features["parentcap"]),
                Metric("tail_count", features["tail"]),
            ),
            "measure_stress_reproduces_prior_counts",
            "The stress audit reproduces the prior n=9 counts: 143435 band cases, 8339 deletion-band stable cases, 66 parent-cap cases, and 10 tail cases.",
            "T313 validates that the expanded measure audit uses the same denominator.",
            "It weakens concern that the stronger measures are computed over a shifted ensemble.",
            "T313 fails if any reproduced count changes under the same definitions.",
        ),
        (
            "T314",
            "Feature Count Map",
            (
                Metric("feature_counts", audit.feature_counts),
            ),
            "feature_count_map_recorded",
            "The core finite features are recorded for the exact n=9 ensemble.",
            "T314 exposes the bottlenecks before measure weighting.",
            "It weakens qualitative discussion detached from exact feature counts.",
            "T314 fails if feature names are reused with different definitions.",
        ),
        (
            "T315",
            "Intersection Count Map",
            (
                Metric("intersection_counts", audit.intersection_counts),
            ),
            "intersection_count_map_recorded",
            "The key intersections show that low-cover plus deletion-band stability leaves 16 cases, while interval+cover+deletion leaves exactly 10.",
            "T315 identifies which feature combinations are doing the selection work.",
            "It weakens single-feature explanations.",
            "T315 fails if intersections are not computed from the same case flags.",
        ),
        (
            "T316",
            "Deletion T252-Pass Distribution",
            (
                Metric("deletion_t252_pass_distribution", audit.deletion_t252_pass_distribution),
                Metric("parentcap_deletion_t252_pass_distribution", audit.parentcap_deletion_t252_pass_distribution),
            ),
            "deletion_t252_pass_distribution_recorded",
            "Among band-positive cases, the number of deletion T252-style passes is highly concentrated near zero, while parent-cap cases split across 4, 7, 8, and 9 passes.",
            "T316 motivates deletion-count soft actions.",
            "It weakens parent-cap-only explanations.",
            "T316 fails if deletion counts are not rank-normalized suborders.",
        ),
        (
            "T317",
            "Selected T252 Placement",
            (
                Metric("selected_t252_diagnostics", audit.selected_diagnostics),
                Metric("selected_t252_deletion_summary", audit.selected_deletion_summary),
            ),
            "selected_t252_has_full_deletion_t252_count",
            "The selected T252 witness has all nine deletion suborders passing the T252-style deletion gate.",
            "T317 anchors the selected witness inside the expanded deletion-count audit.",
            "It weakens any account that ignores deletion substructure.",
            "T317 fails if the selected permutation is not the T252 rank order.",
        ),
        (
            "T318",
            "Tail Symmetry Check",
            (
                Metric("tail_symmetry_counts", audit.tail_symmetry_counts),
            ),
            "tail_symmetry_reproduced",
            "The tail remains closed under inverse and reverse-complement transforms, not under reverse or complement alone.",
            "T318 confirms the structural symmetry result from T301.",
            "It weakens accidental-list readings of the target tail.",
            "T318 fails if transform definitions change after seeing the tail.",
        ),
        (
            "T319",
            "Tail Shape Signature Check",
            (
                Metric("tail_signature_distribution", audit.tail_signature_distribution),
                Metric("parentcap_signature_distribution", audit.parentcap_signature_distribution),
            ),
            "tail_shape_signatures_reproduced",
            "The 10-case tail remains narrow but not shape-singleton: it occupies multiple parent signatures.",
            "T319 keeps selection-measure work from collapsing the target into one hand-picked shape.",
            "It weakens singleton-shape explanations.",
            "T319 fails if signatures omit the rank profile or cover/interval data.",
        ),
    ]
    for spec in manual_specs:
        tasks.append(_manual_task(*spec))

    measure_task_ids = [f"T{number}" for number in range(320, 348)]
    for task_id, measure_name in zip(measure_task_ids, MEASURE_DESCRIPTIONS):
        tasks.append(_measure_task(task_id, measures[measure_name]))

    more_specs = [
        (
            "T348",
            "Best Hard Gate",
            (
                Metric("best_hard_gate", _best_by_probability(measures, _hard_measure_names())),
            ),
            "best_hard_gate_is_interval_cover_deletion_but_target_equivalent",
            "The best hard gate is interval+cover+deletion, but it is empirically target-equivalent at n=9.",
            "T348 separates explanatory gates from target-equivalent gates.",
            "It weakens any claim that a perfect hard gate is automatically a physical measure.",
            "T348 fails if target-equivalent gates are not flagged.",
        ),
        (
            "T349",
            "Best Non-Target Hard Gate",
            (
                Metric("best_non_target_hard_gate", measures["hard_cover_deletion"]),
            ),
            "cover_deletion_hard_gate_puts_five_eighths_mass_on_tail",
            "The best non-target hard gate is low-cover plus deletion-band stability, with tail probability 5/8.",
            "T349 identifies a genuinely strong finite selection candidate.",
            "It weakens the T311 result that obvious finite reweighting was insufficient.",
            "T349 fails if the gate uses the tail label.",
        ),
        (
            "T350",
            "Best Soft Score",
            (
                Metric("best_soft_score", _best_by_probability(measures, _soft_measure_names())),
            ),
            "best_soft_score_is_cubic_deletion_t252_count",
            "The best tested soft score is 8^(T252-style deletion pass count), with tail probability above three quarters.",
            "T350 shows deletion-count temperature can concentrate on the tail without an explicit tail indicator.",
            "It weakens low-temperature soft-score pessimism.",
            "T350 fails if the soft score uses parent tail membership directly.",
        ),
        (
            "T351",
            "Half-Mass Threshold",
            (
                Metric("non_tautological_half_mass_measures", _half_mass_measures(audit)),
            ),
            "some_non_tautological_candidates_exceed_half_mass",
            "Several non-tail-labeled candidates exceed half mass on the 10-case tail, led by cover+deletion and high-temperature deletion-count scores.",
            "T351 updates the prior concentration threshold result with a stronger candidate family.",
            "It weakens the claim that no simple finite score can concentrate the tail.",
            "T351 fails if tail-conditioned measures are included as evidence.",
        ),
        (
            "T352",
            "Hard Cover-Deletion False Positives",
            (
                Metric("hard_cover_deletion_count", measures["hard_cover_deletion"].total_weight),
                Metric("tail_count_inside_gate", measures["hard_cover_deletion"].tail_weight),
                Metric("false_positive_count", measures["hard_cover_deletion"].total_weight - measures["hard_cover_deletion"].tail_weight),
            ),
            "cover_deletion_gate_has_six_false_positives",
            "The strongest non-target hard gate has 6 false positives outside the 10-case target tail.",
            "T352 makes the remaining burden explicit.",
            "It weakens treating cover+deletion as already identical to the target.",
            "T352 fails if false positives are not counted inside the hard gate.",
        ),
        (
            "T353",
            "Parent Cap False Positives Revisited",
            (
                Metric("parentcap_count", measures["hard_parentcap"].total_weight),
                Metric("tail_inside_parentcap", measures["hard_parentcap"].tail_weight),
                Metric("false_positive_count", measures["hard_parentcap"].total_weight - measures["hard_parentcap"].tail_weight),
            ),
            "parentcap_false_positive_burden_stays_large",
            "The parent cap still has 56 false positives before deletion stability.",
            "T353 confirms that parent shape alone is not the measure.",
            "It weakens parentcap-only selection proposals.",
            "T353 fails if it omits the deletion-stability requirement.",
        ),
        (
            "T354",
            "Deletion Temperature Ladder",
            (
                Metric("soft_s_count", measures["soft_s_count"].tail_probability),
                Metric("soft_s_count_squared", measures["soft_s_count_squared"].tail_probability),
                Metric("soft_s_count_cubed", measures["soft_s_count_cubed"].tail_probability),
            ),
            "deletion_temperature_has_threshold_behavior",
            "Tail probability rises from about 1.3 percent to 56.6 percent to 78.7 percent as the T252-deletion-count temperature increases.",
            "T354 shows that concentration depends strongly on temperature.",
            "It weakens treating one arbitrary temperature as principled.",
            "T354 fails if the temperature ladder changes after seeing probabilities.",
        ),
        (
            "T355",
            "Selected Singleton Under Strong Measures",
            (
                Metric("selected_under_cover_deletion", measures["hard_cover_deletion"].selected_probability),
                Metric("selected_under_s_squared", measures["soft_s_count_squared"].selected_probability),
                Metric("selected_under_s_cubed", measures["soft_s_count_cubed"].selected_probability),
            ),
            "selected_singleton_still_not_explained",
            "Even strong tail measures do not uniquely select the original T252 permutation.",
            "T355 separates tail selection from singleton selection.",
            "It weakens overreading of the specific selected witness.",
            "T355 fails if singleton probability is confused with tail probability.",
        ),
        (
            "T356",
            "Cover-Deletion Vs Cubic Soft Score",
            (
                Metric("cover_deletion_tail_probability", measures["hard_cover_deletion"].tail_probability),
                Metric("s_cubed_tail_probability", measures["soft_s_count_cubed"].tail_probability),
            ),
            "hard_and_soft_candidates_both_concentrate_tail",
            "A sparse hard gate and a high-temperature deletion-count soft score both concentrate the target tail.",
            "T356 gives two distinct finite routes for future derivation attempts.",
            "It weakens dependence on one arbitrary candidate.",
            "T356 fails if either candidate is relabeled as physical without derivation.",
        ),
        (
            "T357",
            "Target-Equivalent Gate Guardrail",
            (
                Metric("interval_cover_deletion_probability", measures["hard_interval_cover_deletion"].tail_probability),
                Metric("empirical_target_equivalent", measures["hard_interval_cover_deletion"].empirical_target_equivalent),
            ),
            "perfect_gate_is_guardrailed_as_target_equivalent",
            "The interval+cover+deletion hard gate has probability 1 because it is empirically target-equivalent at n=9.",
            "T357 prevents a perfect finite gate from being mistaken for an explanatory measure.",
            "It weakens post-hoc target-definition laundering.",
            "T357 fails if target-equivalent gates are ranked as physical explanations.",
        ),
        (
            "T358",
            "Tail-Label Tautology Guardrail",
            (
                Metric("tail_conditioned_probability", measures["hard_tail"].tail_probability),
                Metric("uses_tail_label", measures["hard_tail"].uses_tail_label),
            ),
            "tail_label_conditioning_rejected",
            "Direct tail conditioning still gives probability 1 and is rejected as tautological.",
            "T358 keeps the finite measure search honest.",
            "It weakens any attempt to call the target label a measure.",
            "T358 fails if tail-label conditioning is treated as non-tautological.",
        ),
        (
            "T359",
            "Anti-Parent Control",
            (
                Metric("anti_parent_tail_probability", measures["soft_anti_parent"].tail_probability),
                Metric("uniform_tail_probability", UNIFORM_TAIL_PROBABILITY),
            ),
            "anti_parent_control_suppresses_tail",
            "The anti-parent control suppresses the target tail below useful concentration.",
            "T359 checks that the scoring direction matters.",
            "It weakens claims that any reweighting will make the tail look good.",
            "T359 fails if control scores are omitted.",
        ),
        (
            "T360",
            "Cover Hub Primitive",
            (
                Metric("lowcover_tail_probability", measures["hard_lowcover"].tail_probability),
                Metric("cover_deletion_tail_probability", measures["hard_cover_deletion"].tail_probability),
            ),
            "cover_hub_needs_deletion_stability",
            "Low cover alone gives probability 2/37, but low cover plus deletion-band stability gives 5/8.",
            "T360 identifies deletion stability as the multiplier on cover sparsity.",
            "It weakens cover-only accounts.",
            "T360 fails if the cover threshold differs from T257.",
        ),
        (
            "T361",
            "Interval Primitive",
            (
                Metric("interval3_tail_probability", measures["hard_interval3"].tail_probability),
                Metric("interval_deletion_tail_probability", measures["hard_interval_deletion"].tail_probability),
            ),
            "interval_primitive_is_weak_without_cover",
            "Interval<=3 is weak alone and remains broad even with deletion-band stability.",
            "T361 demotes interval depth as the primary selection driver.",
            "It weakens interval-first interpretations.",
            "T361 fails if interval<=3 is evaluated before the band gate.",
        ),
        (
            "T362",
            "Rank Shape Primitive",
            (
                Metric("rank_shape_tail_probability", measures["soft_rank_shape"].tail_probability),
                Metric("exact_parent_shape_tail_probability", measures["soft_t252_exact_parent_shape"].tail_probability),
            ),
            "rank_shape_soft_scores_do_not_concentrate_tail",
            "T252-like rank and parent-shape bonuses enrich the tail only weakly.",
            "T362 keeps shape-label scores from being overread.",
            "It weakens parent-shape-only soft actions.",
            "T362 fails if shape scores include tail membership.",
        ),
        (
            "T363",
            "Lift Ranking",
            (
                Metric("lift_ranking", _top_lifts(audit, limit=10)),
            ),
            "lift_ranking_recorded",
            "The highest non-tail lift comes from high-temperature deletion-count and cover-deletion candidates.",
            "T363 records exact finite lifts relative to uniform.",
            "It weakens qualitative ranking by intuition.",
            "T363 fails if tautological tail conditioning is not marked.",
        ),
        (
            "T364",
            "Measure Family Winner",
            (
                Metric("winner", measures["soft_s_count_cubed"]),
            ),
            "cubic_deletion_count_is_finite_winner_but_underived",
            "Within this finite candidate family, the cubic deletion-count score has the highest non-tail-labeled tail probability.",
            "T364 identifies a concrete candidate for derivation or rejection.",
            "It weakens the need for more ad hoc grid searches before testing derivability.",
            "T364 fails if the winner uses the tail label.",
        ),
        (
            "T365",
            "Best Explainable Hard Candidate",
            (
                Metric("candidate", measures["hard_cover_deletion"]),
            ),
            "cover_deletion_is_best_simple_hard_candidate",
            "The best simple hard candidate is low-cover plus deletion-band stability.",
            "T365 separates an interpretable gate from high-temperature soft tuning.",
            "It weakens purely temperature-based optimism.",
            "T365 fails if target-equivalent gates are allowed to win.",
        ),
        (
            "T366",
            "New Falsification Target",
            (
                Metric("candidate_to_derive", "cover_deletion_or_cubic_deletion_count"),
                Metric("required_derivation", "from finality-domain dynamics, not post-hoc ordinal tail labels"),
            ),
            "next_target_is_derivation_not_more_counting",
            "The next task is to derive or reject the cover-deletion/cubic-deletion-count weights from finality-domain dynamics.",
            "T366 converts finite success into a falsifiable derivation target.",
            "It weakens more uniform counting as the next move.",
            "T366 fails if the candidate is accepted without derivation.",
        ),
        (
            "T367",
            "S1 Status Check",
            (
                Metric("tail_concentration_found", True),
                Metric("physical_measure_derived", False),
            ),
            "s1_still_requires_added_assumption_despite_finite_concentration",
            "Finite concentration exists, but no physical non-uniform measure has been derived.",
            "T367 keeps S1 status aligned with the evidence.",
            "It weakens premature S1 upgrades.",
            "T367 fails if finite concentration is treated as spacetime evidence.",
        ),
        (
            "T368",
            "Claim Ledger Guard",
            (
                Metric("safe_wording", "finite candidate measures can concentrate the T252-style tail, but remain underived"),
            ),
            "claim_ledger_guard_recorded",
            "Safe wording is finite and conditional: candidate measures concentrate the tail but are not physical measures.",
            "T368 prevents overclaiming from the strong finite scores.",
            "It weakens claim-ledger upgrades from this round alone.",
            "T368 fails if it claims a derived selection law.",
        ),
        (
            "T369",
            "Comparison To T311",
            (
                Metric("t311_best_non_tautological_probability", Fraction(5, 33)),
                Metric("t312_t375_best_simple_hard_probability", Fraction(5, 8)),
                Metric("t312_t375_best_soft_probability", measures["soft_s_count_cubed"].tail_probability),
            ),
            "expanded_measure_family_strengthens_tail_concentration",
            "The expanded family improves the best non-tail concentration from 5/33 to 5/8 for a hard gate and above 3/4 for a soft score.",
            "T369 updates the previous round with a stronger candidate family.",
            "It weakens the conclusion that all obvious finite weights are insufficient.",
            "T369 fails if the prior and current candidates are not compared on the same target tail.",
        ),
        (
            "T370",
            "Residual False Positive Target",
            (
                Metric("cover_deletion_false_positive_count", measures["hard_cover_deletion"].total_weight - measures["hard_cover_deletion"].tail_weight),
                Metric("target_next", "explain_or_exclude_the_six_cover_deletion_false_positives"),
            ),
            "six_false_positives_are_next_local_target",
            "The simple hard candidate's remaining problem is exactly six false positives.",
            "T370 turns the best hard candidate into a concrete local obstruction problem.",
            "It weakens vague measure-building next steps.",
            "T370 fails if false positives are not explicitly tracked.",
        ),
        (
            "T371",
            "Temperature Justification Target",
            (
                Metric("winning_temperature_base", 8),
                Metric("winning_soft_probability", measures["soft_s_count_cubed"].tail_probability),
            ),
            "temperature_requires_independent_justification",
            "The winning soft score depends on a high deletion-count temperature that has not been derived.",
            "T371 identifies the missing parameter principle.",
            "It weakens arbitrary-temperature selection claims.",
            "T371 fails if the base-8 temperature is treated as natural without evidence.",
        ),
        (
            "T372",
            "No Singleton Selection",
            (
                Metric("selected_under_best_soft", measures["soft_s_count_cubed"].selected_probability),
                Metric("selected_under_best_hard", measures["hard_cover_deletion"].selected_probability),
            ),
            "best_measures_select_tail_not_singleton",
            "The best measures select the tail, not the single chosen T252 permutation.",
            "T372 keeps singleton claims out of the result.",
            "It weakens hand-picked-witness interpretations.",
            "T372 fails if singleton selection is inferred from tail concentration.",
        ),
        (
            "T373",
            "Route Selection",
            (
                Metric("selected_next_route", "derive_or_reject_cover_deletion_action_from_finality_domain_dynamics"),
                Metric("secondary_route", "derive_or_reject_deletion_count_temperature"),
                Metric("rejected_route", "more_post_hoc_tail_conditioning"),
            ),
            "route_is_derivation_or_rejection_of_candidate_action",
            "The next meaningful route is derivation or rejection of the candidate action, not more post-hoc tail conditioning.",
            "T373 makes the next research move explicit.",
            "It weakens further brute-force task inflation.",
            "T373 fails if the route ignores the best finite candidates.",
        ),
        (
            "T374",
            "Open Blocker Restatement",
            (
                Metric("open_blocker", "no finality-domain derivation of cover-deletion or deletion-count weighting"),
            ),
            "open_blocker_is_now_derivability",
            "The blocker has narrowed from finding a concentrating finite score to deriving that score from finality-domain structure.",
            "T374 records the improved blocker.",
            "It weakens the older blocker that no finite candidate measure was known.",
            "T374 fails if derivability is not distinguished from finite performance.",
        ),
        (
            "T375",
            "Sixty-Four Task Measure Stress Synthesis",
            (
                Metric("completed_task_count", 64),
                Metric("best_simple_hard_tail_probability", measures["hard_cover_deletion"].tail_probability),
                Metric("best_soft_tail_probability", measures["soft_s_count_cubed"].tail_probability),
                Metric("round_verdict", "finite_candidate_measures_concentrate_tail_but_remain_underived"),
            ),
            "finite_candidate_measures_concentrate_tail_but_remain_underived",
            "T312-T375 complete a 64-task finite measure stress round: candidate measures can concentrate the T252-style tail, but the successful weights remain underived.",
            "The round upgrades the blocker from 'find any concentrating finite score' to 'derive the candidate action from finality-domain dynamics.'",
            "It weakens both pessimism about finite concentration and optimism about S1; concentration exists, but derivation is missing.",
            "T375 fails if the candidate scores are later shown to use the tail label or if a physical derivation is supplied and ignored.",
        ),
    ]
    for spec in more_specs:
        tasks.append(_manual_task(*spec))

    if len(tasks) != 64:
        raise AssertionError(f"expected 64 tasks, got {len(tasks)}")
    return tuple(tasks)


@lru_cache(maxsize=1)
def _measure_stress_audit() -> MeasureStressAudit:
    feature_counts: Counter[str] = Counter()
    intersection_counts: Counter[str] = Counter()
    deletion_t252_pass_distribution: Counter[int] = Counter()
    parentcap_deletion_t252_pass_distribution: Counter[int] = Counter()
    parentcap_signatures: Counter[tuple[Any, ...]] = Counter()
    tail_signatures: Counter[tuple[Any, ...]] = Counter()
    tail_permutations: list[InfoPermutation] = []
    measure_accumulators = {
        name: {"total": 0, "tail": 0, "parentcap": 0, "selected": 0}
        for name in MEASURE_DESCRIPTIONS
    }
    selected_diagnostics: FastOrdinalDiagnostics | None = None
    selected_deletion_summary: DeletionSummary | None = None

    for info_permutation in permutations(range(1, NINE_EVENT_COUNT + 1)):
        diagnostics = _diagnostics_for_permutation(info_permutation)
        flags, deletion_summary = _case_flags(info_permutation, diagnostics)
        feature_counts["total"] += 1
        feature_counts["band"] += flags.band
        feature_counts["interval3"] += flags.interval3
        feature_counts["lowcover"] += flags.lowcover
        feature_counts["t253_stable"] += flags.t253_stable
        feature_counts["relaxed_interval3_stable"] += flags.relaxed_interval3_stable
        feature_counts["parentcap"] += flags.parentcap
        feature_counts["tail"] += flags.tail

        if flags.band:
            deletion_t252_pass_distribution[flags.deletion_t252_pass_count] += 1
        if flags.parentcap:
            parentcap_deletion_t252_pass_distribution[
                flags.deletion_t252_pass_count
            ] += 1
            parentcap_signatures[_shape_signature(diagnostics)] += 1
        if flags.tail:
            tail_permutations.append(info_permutation)
            tail_signatures[_shape_signature(diagnostics)] += 1

        intersection_counts["interval_cover"] += flags.interval3 and flags.lowcover
        intersection_counts["interval_deletion"] += (
            flags.interval3 and flags.t253_stable
        )
        intersection_counts["cover_deletion"] += flags.lowcover and flags.t253_stable
        intersection_counts["interval_cover_deletion"] += (
            flags.interval3 and flags.lowcover and flags.t253_stable
        )

        if info_permutation == SELECTED_T252_RANK_PERMUTATION:
            selected_diagnostics = diagnostics
            selected_deletion_summary = deletion_summary

        weights = _measure_weights(flags, diagnostics)
        for name, weight in weights.items():
            accumulator = measure_accumulators[name]
            accumulator["total"] += weight
            if flags.tail:
                accumulator["tail"] += weight
            if flags.parentcap:
                accumulator["parentcap"] += weight
            if info_permutation == SELECTED_T252_RANK_PERMUTATION:
                accumulator["selected"] += weight

    if selected_diagnostics is None or selected_deletion_summary is None:
        raise AssertionError("selected T252 witness was not found")

    measure_summaries = tuple(
        _measure_summary(
            name=name,
            description=MEASURE_DESCRIPTIONS[name],
            total_cases=feature_counts["total"],
            tail_count=feature_counts["tail"],
            uses_tail_label=(name == "hard_tail"),
            empirical_target_equivalent=(name == "hard_interval_cover_deletion"),
            uses_deletion_t252_count=name
            in {
                "soft_s_count",
                "soft_non_tail_local",
                "soft_non_tail_local_strong",
                "soft_s_count_squared",
                "soft_parent_s_squared",
                "soft_s_count_cubed",
                "soft_cover_s_count",
                "soft_interval_cover_s_count",
            },
            **measure_accumulators[name],
        )
        for name in MEASURE_DESCRIPTIONS
    )
    tail_tuple = tuple(tail_permutations)
    return MeasureStressAudit(
        total_cases=feature_counts["total"],
        feature_counts=tuple(sorted(feature_counts.items())),
        intersection_counts=tuple(sorted(intersection_counts.items())),
        deletion_t252_pass_distribution=tuple(
            sorted(deletion_t252_pass_distribution.items())
        ),
        parentcap_deletion_t252_pass_distribution=tuple(
            sorted(parentcap_deletion_t252_pass_distribution.items())
        ),
        parentcap_signature_distribution=tuple(
            sorted(parentcap_signatures.items(), key=lambda item: repr(item[0]))
        ),
        tail_signature_distribution=tuple(
            sorted(tail_signatures.items(), key=lambda item: repr(item[0]))
        ),
        tail_permutations=tail_tuple,
        tail_symmetry_counts=_tail_symmetry_counts(tail_tuple),
        selected_diagnostics=selected_diagnostics,
        selected_deletion_summary=selected_deletion_summary,
        measure_summaries=measure_summaries,
    )


def _case_flags(
    info_permutation: InfoPermutation,
    diagnostics: FastOrdinalDiagnostics | None = None,
) -> tuple[CaseFlags, DeletionSummary]:
    if diagnostics is None:
        diagnostics = _diagnostics_for_permutation(info_permutation)
    band = diagnostics.t126_filter_passed and _ordering_band_passed(
        diagnostics.strict_pair_count,
        diagnostics.event_count,
    )
    deletion_summary = (
        _deletion_summary(info_permutation)
        if band
        else DeletionSummary(
            deletion_count=diagnostics.event_count,
            t159_thin_deletion_pass_count=0,
            relaxed_interval3_deletion_pass_count=0,
            t253_t126_band_deletion_pass_count=0,
            t252_style_deletion_pass_count=0,
        )
    )
    interval3 = band and diagnostics.largest_interval_size <= T252_INTERVAL_CAP
    lowcover = band and diagnostics.largest_cover_hub_fraction <= T252_COVER_HUB_CAP
    parentcap = _passes_t252_parent_cap(diagnostics)
    t253_stable = (
        deletion_summary.t253_t126_band_deletion_pass_count
        == diagnostics.event_count
    )
    relaxed_stable = (
        deletion_summary.relaxed_interval3_deletion_pass_count
        == diagnostics.event_count
    )
    tail = parentcap and (
        deletion_summary.t252_style_deletion_pass_count == diagnostics.event_count
    )
    return (
        CaseFlags(
            band=band,
            interval3=interval3,
            lowcover=lowcover,
            parentcap=parentcap,
            t253_stable=t253_stable,
            relaxed_interval3_stable=relaxed_stable,
            tail=tail,
            deletion_band_pass_count=deletion_summary.t253_t126_band_deletion_pass_count,
            deletion_interval3_pass_count=(
                deletion_summary.relaxed_interval3_deletion_pass_count
            ),
            deletion_t252_pass_count=deletion_summary.t252_style_deletion_pass_count,
        ),
        deletion_summary,
    )


def _measure_weights(
    flags: CaseFlags,
    diagnostics: FastOrdinalDiagnostics,
) -> dict[str, int]:
    band = int(flags.band)
    interval = int(flags.interval3)
    cover = int(flags.lowcover)
    t253 = int(flags.t253_stable)
    relaxed = int(flags.relaxed_interval3_stable)
    parentcap = int(flags.parentcap)
    tail = int(flags.tail)
    deletion_band_count = flags.deletion_band_pass_count
    deletion_interval_count = flags.deletion_interval3_pass_count
    deletion_t252_count = flags.deletion_t252_pass_count
    return {
        "uniform": 1,
        "hard_band": band,
        "hard_interval3": interval,
        "hard_lowcover": cover,
        "hard_t253": t253,
        "hard_parentcap": parentcap,
        "hard_interval_deletion": int(flags.interval3 and flags.t253_stable),
        "hard_cover_deletion": int(flags.lowcover and flags.t253_stable),
        "hard_interval_cover_deletion": int(
            flags.interval3 and flags.lowcover and flags.t253_stable
        ),
        "hard_tail": tail,
        "soft_parent_v1": 2 ** (band + interval + cover),
        "soft_parent_v2": 3 ** (band + interval + cover),
        "soft_deletion_binary": 2 ** (band + interval + cover + t253 + relaxed),
        "soft_d_count": 2 ** deletion_band_count,
        "soft_r_count": 2 ** deletion_interval_count,
        "soft_s_count": 2 ** deletion_t252_count,
        "soft_non_tail_local": 2
        ** (band + interval + cover + min(deletion_t252_count, 4)),
        "soft_non_tail_local_strong": 2
        ** (band + interval + cover + min(deletion_t252_count, 6)),
        "soft_s_count_squared": 4 ** deletion_t252_count,
        "soft_parent_s_squared": (4 ** deletion_t252_count)
        * (4 if flags.parentcap else 1),
        "soft_s_count_cubed": 8 ** deletion_t252_count,
        "soft_cover_s_count": (2 ** deletion_t252_count)
        * (4 if flags.lowcover else 1),
        "soft_interval_cover_s_count": (2 ** deletion_t252_count)
        * (4 if flags.interval3 and flags.lowcover else 1),
        "soft_rank_shape": 2
        ** (
            band
            + interval
            + cover
            + int(diagnostics.height == 5)
            + int(diagnostics.width == 2)
            + int(diagnostics.cover_relation_count == 8)
            + int(diagnostics.strict_pair_count == 20)
        ),
        "soft_t252_exact_parent_shape": 2
        ** (
            band
            + int(diagnostics.strict_pair_count == 20)
            + int(diagnostics.cover_relation_count == 8)
            + int(diagnostics.height == 5)
            + int(diagnostics.width == 2)
            + int(
                diagnostics.rank_profile
                in {
                    (1, 2, 2, 2, 2),
                    (2, 2, 2, 2, 1),
                }
            )
        ),
        "soft_coverhub_inverse": 8
        if flags.band and diagnostics.largest_cover_hub_fraction <= Fraction(1, 4)
        else 1,
        "soft_interval_inverse": 8 if flags.interval3 else 1,
        "soft_anti_parent": 2 ** (band + int(not flags.interval3) + int(not flags.lowcover)),
    }


def _measure_summary(
    *,
    name: str,
    description: str,
    total: int,
    tail: int,
    parentcap: int,
    selected: int,
    total_cases: int,
    tail_count: int,
    uses_tail_label: bool,
    empirical_target_equivalent: bool,
    uses_deletion_t252_count: bool,
) -> MeasureSummary:
    tail_probability = _fraction(tail, total)
    return MeasureSummary(
        name=name,
        description=description,
        total_weight=total,
        tail_weight=tail,
        parentcap_weight=parentcap,
        selected_weight=selected,
        tail_probability=tail_probability,
        parentcap_probability=_fraction(parentcap, total),
        selected_probability=_fraction(selected, total),
        lift_vs_uniform=_fraction(tail * total_cases, total * tail_count),
        uses_tail_label=uses_tail_label,
        empirical_target_equivalent=empirical_target_equivalent,
        uses_deletion_t252_count=uses_deletion_t252_count,
    )


def _manual_task(
    task_id: str,
    title: str,
    metrics: tuple[Metric, ...],
    verdict: str,
    strongest_claim: str,
    improved: str,
    weakened_or_falsified: str,
    falsification_condition: str,
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
        s1_update="S1 remains requires_added_assumption for the finite ordinal route.",
        claim_ledger_update=f"Do not update the claim ledger from {task_id} alone.",
        open_blocker=(
            "No finality-domain dynamics derive the successful finite weighting "
            "rule yet."
        ),
        suggested_next=(
            "Derive or reject the candidate action from finality-domain data "
            "rather than from post-hoc tail labels."
        ),
        not_claimed=NOT_CLAIMED,
    )


def _measure_task(task_id: str, summary: MeasureSummary) -> TaskResult:
    verdict = (
        f"{summary.name}_tail_probability_recorded"
        if not summary.uses_tail_label
        else "tail_label_conditioning_recorded_as_tautology"
    )
    return TaskResult(
        task_id=task_id,
        title=summary.name.replace("_", " ").title(),
        metrics=(
            Metric("description", summary.description),
            Metric("total_weight", summary.total_weight),
            Metric("tail_weight", summary.tail_weight),
            Metric("tail_probability", summary.tail_probability),
            Metric("parentcap_probability", summary.parentcap_probability),
            Metric("selected_probability", summary.selected_probability),
            Metric("lift_vs_uniform", summary.lift_vs_uniform),
            Metric("uses_tail_label", summary.uses_tail_label),
            Metric("empirical_target_equivalent", summary.empirical_target_equivalent),
            Metric("uses_deletion_t252_count", summary.uses_deletion_t252_count),
        ),
        verdict=verdict,
        strongest_claim=(
            f"The `{summary.name}` candidate assigns the 10-case tail "
            f"probability {summary.tail_probability}."
        ),
        improved=(
            "This records an exact finite probability for a declared candidate "
            "weighting rule."
        ),
        weakened_or_falsified=(
            "The candidate is weakened as an S1-relevant measure unless it is "
            "both non-tautological and independently derivable."
        ),
        falsification_condition=(
            f"{task_id} fails if the `{summary.name}` weights are changed "
            "without renaming the measure."
        ),
        s1_update="S1 remains requires_added_assumption for the finite ordinal route.",
        claim_ledger_update=f"Do not update the claim ledger from {task_id} alone.",
        open_blocker=(
            "A finite weighting rule is not a physical measure until derived "
            "from finality-domain dynamics."
        ),
        suggested_next=(
            "Compare this probability against the hard-gate and soft-score "
            "rankings, then derive or reject the leading candidate."
        ),
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


def _hard_measure_names() -> tuple[str, ...]:
    return tuple(name for name in MEASURE_DESCRIPTIONS if name.startswith("hard_") and name != "hard_tail")


def _soft_measure_names() -> tuple[str, ...]:
    return tuple(name for name in MEASURE_DESCRIPTIONS if name.startswith("soft_"))


def _best_by_probability(
    measures: dict[str, MeasureSummary],
    names: tuple[str, ...],
) -> MeasureSummary:
    return max((measures[name] for name in names), key=lambda item: item.tail_probability)


def _half_mass_measures(audit: MeasureStressAudit) -> tuple[MeasureSummary, ...]:
    return tuple(
        summary
        for summary in audit.measure_summaries
        if not summary.uses_tail_label
        and summary.tail_probability >= Fraction(1, 2)
    )


def _top_lifts(audit: MeasureStressAudit, *, limit: int) -> tuple[MeasureSummary, ...]:
    return tuple(
        sorted(
            (
                summary
                for summary in audit.measure_summaries
                if not summary.uses_tail_label
            ),
            key=lambda item: item.lift_vs_uniform,
            reverse=True,
        )[:limit]
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
        "parentcap_weight": summary.parentcap_weight,
        "selected_weight": summary.selected_weight,
        "tail_probability": _fraction_to_dict(summary.tail_probability),
        "parentcap_probability": _fraction_to_dict(summary.parentcap_probability),
        "selected_probability": _fraction_to_dict(summary.selected_probability),
        "lift_vs_uniform": _fraction_to_dict(summary.lift_vs_uniform),
        "uses_tail_label": summary.uses_tail_label,
        "empirical_target_equivalent": summary.empirical_target_equivalent,
        "uses_deletion_t252_count": summary.uses_deletion_t252_count,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}
