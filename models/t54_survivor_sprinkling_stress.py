"""T165: exact ordinal-sprinkling stress test for T54 survivor classes.

T164 reduced the T163 stable survivors to 15 oriented finite-poset classes.
This module asks a sharper comparison question: how large is that survivor
set inside the exact six-point 1+1 ordinal sprinkling ensemble?

For six independent points in a flat 1+1 causal diamond with no coordinate
ties, sorting by one light-cone coordinate leaves the second coordinate as a
uniform permutation. That is exactly the T163 rank-pair family. This is still
finite control work, not spacetime evidence.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.t54_rank_pair_family_census import T163CaseAudit, audit_t163_family
from models.t54_survivor_isomorphism_locality import run_t164_analysis


@dataclass(frozen=True)
class T165ConditioningStage:
    stage: str
    pass_count: int
    universe_count: int
    unconditional_fraction: Fraction
    conditional_denominator: int
    conditional_fraction: Fraction
    interpretation: str


@dataclass(frozen=True)
class T165Result:
    comparison_target: str
    target_basis: str
    total_rank_permutation_cases: int
    t126_pass_count: int
    t156_pass_count: int
    parent_interval_pass_count: int
    stable_labeled_survivor_count: int
    stable_labeled_survivor_fraction: Fraction
    oriented_survivor_class_count: int
    order_dual_survivor_class_count: int
    largest_oriented_class_size: int
    largest_oriented_class_probability: Fraction
    all_oriented_classes_below_one_percent: bool
    conditioning_stages: tuple[T165ConditioningStage, ...]
    all_strict_pair_distribution: tuple[tuple[int, int], ...]
    stable_labeled_strict_pair_distribution: tuple[tuple[int, int], ...]
    stable_oriented_strict_pair_distribution: tuple[tuple[int, int], ...]
    parent_deletion_pass_distribution: tuple[tuple[int, int], ...]
    stable_oriented_rank_profile_distribution: tuple[tuple[tuple[int, ...], int], ...]
    stable_oriented_width_distribution: tuple[tuple[int, int], ...]
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
    "T165 does not validate a random sprinkling law, faithful embedding, "
    "Lorentzian metric reconstruction, covariance, GR, QFT, or a continuum "
    "limit. It only compares the six-event T54 survivors against the exact "
    "finite ordinal 1+1 permutation ensemble."
)


def run_t165_analysis() -> T165Result:
    audits = audit_t163_family()
    total = len(audits)
    t126_pass = tuple(audit for audit in audits if audit.t126_filter_passed)
    t156_pass = tuple(
        audit
        for audit in audits
        if audit.t156_verdict == "passes_ordering_fraction_control_only"
    )
    parent_pass = tuple(audit for audit in audits if audit.parent_interval_support_passed)
    stable = tuple(
        audit for audit in audits if audit.outcome_bucket == "t159_stable_survivor"
    )
    t164 = run_t164_analysis()
    largest_class = max(
        (audit.labeled_member_count for audit in t164.class_audits),
        default=0,
    )

    return T165Result(
        comparison_target="exact_six_point_ordinal_1p1_sprinkling",
        target_basis=(
            "For a flat 1+1 causal diamond in light-cone coordinates, six "
            "generic sampled points have no coordinate ties. After sorting by "
            "one coordinate, the other coordinate's rank is a uniform element "
            "of S_6, giving exactly the 720 T163 rank-pair cases."
        ),
        total_rank_permutation_cases=total,
        t126_pass_count=len(t126_pass),
        t156_pass_count=len(t156_pass),
        parent_interval_pass_count=len(parent_pass),
        stable_labeled_survivor_count=len(stable),
        stable_labeled_survivor_fraction=_fraction(len(stable), total),
        oriented_survivor_class_count=t164.oriented_isomorphism_class_count,
        order_dual_survivor_class_count=t164.order_dual_quotient_class_count,
        largest_oriented_class_size=largest_class,
        largest_oriented_class_probability=_fraction(largest_class, total),
        all_oriented_classes_below_one_percent=all(
            _fraction(audit.labeled_member_count, total) < Fraction(1, 100)
            for audit in t164.class_audits
        ),
        conditioning_stages=(
            _stage(
                "T126 finite causal-set filter",
                len(t126_pass),
                total,
                total,
                "Most ordinal 1+1 samples clear the coarse T126 filter.",
            ),
            _stage(
                "T156 ordering-fraction band",
                len(t156_pass),
                total,
                len(t126_pass),
                "The declared 1+1 ordering band removes almost half of the T126 passers.",
            ),
            _stage(
                "T159 parent-interval support",
                len(parent_pass),
                total,
                len(t156_pass),
                "Parent interval-thinness is a further strong finite conditioning step.",
            ),
            _stage(
                "T159 all single deletions stable",
                len(stable),
                total,
                len(parent_pass),
                "Only a small tail remains after every single-event deletion must also pass.",
            ),
        ),
        all_strict_pair_distribution=_counter_rows(
            audit.strict_pair_count for audit in audits if audit.strict_pair_count is not None
        ),
        stable_labeled_strict_pair_distribution=_counter_rows(
            audit.strict_pair_count for audit in stable if audit.strict_pair_count is not None
        ),
        stable_oriented_strict_pair_distribution=_counter_rows(
            audit.strict_pair_count for audit in t164.class_audits
        ),
        parent_deletion_pass_distribution=_counter_rows(
            audit.deletion_pass_count for audit in parent_pass
        ),
        stable_oriented_rank_profile_distribution=_tuple_counter_rows(
            audit.rank_profile for audit in t164.class_audits
        ),
        stable_oriented_width_distribution=_counter_rows(
            audit.width for audit in t164.class_audits
        ),
        strongest_claim=(
            "The T164 survivor classes are compatible with the exact six-point "
            "ordinal 1+1 sprinkling comparison, but only as a heavily "
            "conditioned rare tail: 26 of 720 labeled rank-permutation cases "
            "survive all current screens, a fraction of 13/360. Each oriented "
            "survivor class has uniform-ensemble probability at most 1/360."
        ),
        improved=(
            "T165 replaces loose 'random sprinkling' language with an exact "
            "finite comparison ensemble. It reports the unconditional and "
            "conditional narrowing caused by T126, T156, parent-interval, and "
            "single-deletion screens, plus the abundance of each T164 class."
        ),
        weakened_or_falsified=(
            "This weakens any optimistic reading that the 15 T164 classes are "
            "typical small sprinkling outputs or evidence of a generative "
            "spacetime law. They are a selected 3.6 percent tail of the exact "
            "six-point ordinal ensemble, not a broad or natural continuum "
            "family by themselves."
        ),
        falsification_condition=(
            "T165 fails if the T163 rank-pair family is not the correct exact "
            "ordinal model for six no-tie 1+1 interval samples, if the T163 "
            "and T164 pipelines disagree about stable survivors, or if rare "
            "finite abundance is described as continuum evidence rather than "
            "a new generative-law burden."
        ),
        s1_update=(
            "S1 remains open_formal_target. The current six-event boundary is "
            "finite-compatible with an ordinal 1+1 comparison, but only after "
            "strong conditioning; it is not yet a sprinkling law or spacetime "
            "reconstruction."
        ),
        claim_ledger_update=(
            "Add T165 to S1: the 15 oriented T164 survivor classes occupy only "
            "26/720 labeled cases in the exact six-point ordinal 1+1 "
            "sprinkling ensemble, and no oriented class has probability above "
            "1/360. Treat them as a rare finite tail needing a generative "
            "explanation, not as spacetime evidence."
        ),
        open_blocker=(
            "No T54 generative law, larger-n scaling result, faithful embedding "
            "theorem, Lorentzian metric reconstruction, covariance result, "
            "or continuum bridge explains why these rare finite classes should "
            "be selected physically."
        ),
        suggested_next=(
            "Either derive a T54 generative mechanism that predicts the rare "
            "survivor tail under a declared measure, or run the same exact "
            "ordinal comparison at n=7 with bounded computational scope."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t165_result_to_dict(result: T165Result) -> dict[str, Any]:
    return {
        "comparison_target": result.comparison_target,
        "target_basis": result.target_basis,
        "total_rank_permutation_cases": result.total_rank_permutation_cases,
        "t126_pass_count": result.t126_pass_count,
        "t156_pass_count": result.t156_pass_count,
        "parent_interval_pass_count": result.parent_interval_pass_count,
        "stable_labeled_survivor_count": result.stable_labeled_survivor_count,
        "stable_labeled_survivor_fraction": _fraction_to_dict(
            result.stable_labeled_survivor_fraction
        ),
        "oriented_survivor_class_count": result.oriented_survivor_class_count,
        "order_dual_survivor_class_count": result.order_dual_survivor_class_count,
        "largest_oriented_class_size": result.largest_oriented_class_size,
        "largest_oriented_class_probability": _fraction_to_dict(
            result.largest_oriented_class_probability
        ),
        "all_oriented_classes_below_one_percent": (
            result.all_oriented_classes_below_one_percent
        ),
        "conditioning_stages": [
            _stage_to_dict(stage) for stage in result.conditioning_stages
        ],
        "all_strict_pair_distribution": _rows_to_dict(
            result.all_strict_pair_distribution,
            "strict_pair_count",
        ),
        "stable_labeled_strict_pair_distribution": _rows_to_dict(
            result.stable_labeled_strict_pair_distribution,
            "strict_pair_count",
        ),
        "stable_oriented_strict_pair_distribution": _rows_to_dict(
            result.stable_oriented_strict_pair_distribution,
            "strict_pair_count",
        ),
        "parent_deletion_pass_distribution": _rows_to_dict(
            result.parent_deletion_pass_distribution,
            "deletion_pass_count",
        ),
        "stable_oriented_rank_profile_distribution": [
            {"rank_profile": list(profile), "class_count": count}
            for profile, count in result.stable_oriented_rank_profile_distribution
        ],
        "stable_oriented_width_distribution": _rows_to_dict(
            result.stable_oriented_width_distribution,
            "width",
        ),
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


def _stage(
    stage: str,
    pass_count: int,
    universe_count: int,
    conditional_denominator: int,
    interpretation: str,
) -> T165ConditioningStage:
    return T165ConditioningStage(
        stage=stage,
        pass_count=pass_count,
        universe_count=universe_count,
        unconditional_fraction=_fraction(pass_count, universe_count),
        conditional_denominator=conditional_denominator,
        conditional_fraction=_fraction(pass_count, conditional_denominator),
        interpretation=interpretation,
    )


def _counter_rows(values: Any) -> tuple[tuple[int, int], ...]:
    counts = Counter(values)
    return tuple(sorted((int(value), count) for value, count in counts.items()))


def _tuple_counter_rows(values: Any) -> tuple[tuple[tuple[int, ...], int], ...]:
    counts = Counter(values)
    return tuple(sorted(counts.items()))


def _rows_to_dict(rows: tuple[tuple[int, int], ...], key_name: str) -> list[dict[str, int]]:
    return [{key_name: value, "count": count} for value, count in rows]


def _stage_to_dict(stage: T165ConditioningStage) -> dict[str, Any]:
    return {
        "stage": stage.stage,
        "pass_count": stage.pass_count,
        "universe_count": stage.universe_count,
        "unconditional_fraction": _fraction_to_dict(stage.unconditional_fraction),
        "conditional_denominator": stage.conditional_denominator,
        "conditional_fraction": _fraction_to_dict(stage.conditional_fraction),
        "interpretation": stage.interpretation,
    }


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t165_result_to_dict(run_t165_analysis()), indent=2))
