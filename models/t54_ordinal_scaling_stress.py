"""T167: bounded ordinal-scaling stress test for T54 rank-pair survivors.

T165 showed that the six-event T54 survivor classes are a rare tail of the
exact ordinal 1+1 rank-permutation ensemble. This module asks the next bounded
question: does that rare-tail status immediately disappear, become typical, or
persist when the exact ensemble is extended one step to seven events?

The comparison is still finite control work. It is not a continuum limit,
sprinkling law, Lorentzian embedding, or spacetime reconstruction.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from math import factorial
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    audit_finality_colimit_causet,
)
from models.finality_descent_theorem import (
    AxisProfile,
    EventIdentityMap,
    LocalEvent,
    ObserverDescentDatum,
    ObserverView,
    complete_observer_descent_datum,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    audit_ordering_fraction_target,
    flat_1p1_interval_target,
)
from models.t54_interval_jackknife_screen import (
    _deletion_audits,
    _largest_interval_size,
    flat_1p1_interval_jackknife_target,
)
from models.t54_ordering_fraction_bridge import _completion_to_t126_datum
from models.t54_survivor_isomorphism_locality import (
    _canonical_dual_key_from_key,
    _canonical_poset_key,
    _strict_pairs,
)


Event = str
InfoPermutation = tuple[int, ...]

SUPPORTED_SIZES = (5, 6, 7)


@dataclass(frozen=True)
class T167SizeAudit:
    event_count: int
    total_rank_permutation_cases: int
    t126_classification_counts: tuple[tuple[str, int], ...]
    t126_pass_count: int
    t156_pass_count: int
    parent_interval_pass_count: int
    stable_labeled_survivor_count: int
    stable_labeled_survivor_fraction: Fraction
    stable_conditional_after_parent_fraction: Fraction
    oriented_survivor_class_count: int
    order_dual_survivor_class_count: int
    largest_oriented_class_size: int
    largest_oriented_class_probability: Fraction
    singleton_oriented_class_count: int
    deletion_pass_distribution: tuple[tuple[int, int], ...]
    stable_strict_pair_distribution: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class T167Result:
    comparison_target: str
    target_basis: str
    size_audits: tuple[T167SizeAudit, ...]
    n6_stable_fraction: Fraction
    n7_stable_fraction: Fraction
    one_step_fraction_delta: Fraction
    n7_oriented_class_count: int
    n7_order_dual_class_count: int
    n7_largest_class_probability: Fraction
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
    "T167 does not establish a continuum limit, random sprinkling law, "
    "faithful embedding, Lorentzian metric reconstruction, covariance, GR, "
    "QFT, or a generative spacetime mechanism. It only runs exact finite "
    "ordinal rank-permutation ensembles through the existing T54/T126/T156/"
    "T159 screens at n=5, n=6, and n=7."
)


def run_t167_analysis() -> T167Result:
    audits = tuple(_audit_size(size) for size in SUPPORTED_SIZES)
    by_size = {audit.event_count: audit for audit in audits}
    n6 = by_size[6]
    n7 = by_size[7]
    delta = n7.stable_labeled_survivor_fraction - n6.stable_labeled_survivor_fraction

    return T167Result(
        comparison_target="exact_ordinal_1p1_rank_permutation_scaling_n5_to_n7",
        target_basis=(
            "For n generic points in a flat 1+1 causal diamond with no "
            "light-cone coordinate ties, sorting by one coordinate leaves the "
            "other coordinate's rank as a uniform element of S_n. T167 uses "
            "that exact finite ordinal ensemble for n=5, n=6, and n=7."
        ),
        size_audits=audits,
        n6_stable_fraction=n6.stable_labeled_survivor_fraction,
        n7_stable_fraction=n7.stable_labeled_survivor_fraction,
        one_step_fraction_delta=delta,
        n7_oriented_class_count=n7.oriented_survivor_class_count,
        n7_order_dual_class_count=n7.order_dual_survivor_class_count,
        n7_largest_class_probability=n7.largest_oriented_class_probability,
        strongest_claim=(
            "The T165 rare-tail boundary survives one exact ordinal scaling "
            "step. At n=5 every case is blocked by the T126 scale floor. At "
            "n=6, 26/720 cases survive all current screens. At n=7, 174/5040 "
            "survive, a reduced fraction of 29/840, and those labels collapse "
            "to 86 oriented finite-poset classes or 45 order-dual classes."
        ),
        improved=(
            "T167 replaces the open 'try n=7' suggestion with an exact bounded "
            "scaling audit. It checks the same T126, T156, parent-interval, "
            "single-deletion, and finite-poset isomorphism stages at n=5, n=6, "
            "and n=7, so the six-event result is no longer a one-size-only "
            "comparison."
        ),
        weakened_or_falsified=(
            "This weakens two premature readings at once. The stable T54 tail "
            "does not vanish at n=7, so T165 was not merely a six-event "
            "accident. But it also does not become typical: the stable fraction "
            "slightly decreases from 13/360 to 29/840, and the largest n=7 "
            "oriented class has probability only 1/1260."
        ),
        falsification_condition=(
            "T167 fails if the ordinal S_n ensemble is not the intended exact "
            "finite model for no-tie 1+1 interval samples, if the n=6 result "
            "does not reproduce T165, if the n=7 audit changes any screen "
            "relative to T126/T156/T159, or if one-step scaling is described "
            "as a continuum-limit or generative-law result."
        ),
        s1_update=(
            "S1 remains open_formal_target. The T54 survivor tail persists "
            "from n=6 to n=7 under the declared exact ordinal comparison, but "
            "only as a rare finite tail requiring a generative mechanism, "
            "larger-n scaling law, embedding theorem, or continuum bridge."
        ),
        claim_ledger_update=(
            "Add T167 to S1: exact ordinal scaling gives n=5 scale-blocked, "
            "n=6 stable fraction 13/360, and n=7 stable fraction 29/840 with "
            "86 oriented survivor classes and largest class probability "
            "1/1260. Treat this as one-step persistence of a rare finite tail, "
            "not as spacetime evidence."
        ),
        open_blocker=(
            "No T54 generative law, asymptotic scaling theorem, natural "
            "measure over finality colimits, faithful embedding theorem, "
            "Lorentzian metric reconstruction, covariance result, or continuum "
            "bridge explains why the rare tail should be physically selected."
        ),
        suggested_next=(
            "Do not repeat small-n counting alone. Either derive a T54 "
            "generative measure that predicts the rare tail, add an efficient "
            "sampling/asymptotic argument for n>=8, or switch to a different "
            "S1 bridge such as embedding/covariance/metric reconstruction."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t167_result_to_dict(result: T167Result) -> dict[str, Any]:
    return {
        "comparison_target": result.comparison_target,
        "target_basis": result.target_basis,
        "size_audits": [_size_audit_to_dict(audit) for audit in result.size_audits],
        "n6_stable_fraction": _fraction_to_dict(result.n6_stable_fraction),
        "n7_stable_fraction": _fraction_to_dict(result.n7_stable_fraction),
        "one_step_fraction_delta": _fraction_to_dict(result.one_step_fraction_delta),
        "n7_oriented_class_count": result.n7_oriented_class_count,
        "n7_order_dual_class_count": result.n7_order_dual_class_count,
        "n7_largest_class_probability": _fraction_to_dict(
            result.n7_largest_class_probability
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


def _audit_size(event_count: int) -> T167SizeAudit:
    if event_count not in SUPPORTED_SIZES:
        raise ValueError(f"T167 supports only bounded sizes {SUPPORTED_SIZES}")

    classification_counts: Counter[str] = Counter()
    deletion_pass_distribution: Counter[int] = Counter()
    stable_strict_pair_distribution: Counter[int] = Counter()
    oriented_groups: dict[str, list[InfoPermutation]] = {}
    t126_pass_count = 0
    t156_pass_count = 0
    parent_interval_pass_count = 0
    stable_labeled_survivor_count = 0

    for info_permutation in permutations(range(1, event_count + 1)):
        t126_datum = _t126_datum_for_permutation(info_permutation)
        t126_audit = audit_finality_colimit_causet(t126_datum)
        classification_counts[t126_audit.classification] += 1

        if not t126_audit.manifold_filter_passed:
            continue
        t126_pass_count += 1

        t156_audit = audit_ordering_fraction_target(
            t126_datum,
            target=flat_1p1_interval_target(),
        )
        if t156_audit.verdict != "passes_ordering_fraction_control_only":
            continue
        t156_pass_count += 1

        diagnostics = t126_audit.diagnostics
        if diagnostics is None:
            continue
        largest_interval_size = _largest_interval_size(
            diagnostics.interval_counts_by_size
        )
        if largest_interval_size is None or largest_interval_size > 1:
            continue
        parent_interval_pass_count += 1

        deletion_audits = _deletion_audits(
            t126_datum,
            target=flat_1p1_interval_jackknife_target(),
        )
        deletion_pass_count = sum(
            1
            for audit in deletion_audits
            if audit.ordering_band_passed and audit.interval_support_passed
        )
        deletion_pass_distribution[deletion_pass_count] += 1
        if deletion_pass_count != len(deletion_audits):
            continue

        stable_labeled_survivor_count += 1
        stable_strict_pair_distribution[diagnostics.strict_pair_count] += 1
        key = _canonical_poset_key(t126_datum.events, _strict_pairs(t126_datum.relation))
        oriented_groups.setdefault(key, []).append(info_permutation)

    total_cases = factorial(event_count)
    class_sizes = tuple(len(members) for members in oriented_groups.values())
    largest_class_size = max(class_sizes, default=0)
    dual_class_count = len(
        {
            min(key, _canonical_dual_key_from_key(key))
            for key in oriented_groups
        }
    )

    return T167SizeAudit(
        event_count=event_count,
        total_rank_permutation_cases=total_cases,
        t126_classification_counts=tuple(sorted(classification_counts.items())),
        t126_pass_count=t126_pass_count,
        t156_pass_count=t156_pass_count,
        parent_interval_pass_count=parent_interval_pass_count,
        stable_labeled_survivor_count=stable_labeled_survivor_count,
        stable_labeled_survivor_fraction=_fraction(
            stable_labeled_survivor_count,
            total_cases,
        ),
        stable_conditional_after_parent_fraction=_fraction(
            stable_labeled_survivor_count,
            parent_interval_pass_count,
        ),
        oriented_survivor_class_count=len(oriented_groups),
        order_dual_survivor_class_count=dual_class_count,
        largest_oriented_class_size=largest_class_size,
        largest_oriented_class_probability=_fraction(largest_class_size, total_cases),
        singleton_oriented_class_count=sum(1 for size in class_sizes if size == 1),
        deletion_pass_distribution=tuple(sorted(deletion_pass_distribution.items())),
        stable_strict_pair_distribution=tuple(
            sorted(stable_strict_pair_distribution.items())
        ),
    )


def _t126_datum_for_permutation(info_permutation: InfoPermutation):
    completion = complete_observer_descent_datum(_rank_pair_datum(info_permutation))
    return _completion_to_t126_datum(completion)


def _rank_pair_datum(info_permutation: InfoPermutation) -> ObserverDescentDatum:
    profiles = {
        f"e{index}": AxisProfile(causal=index, info=info_permutation[index - 1])
        for index in range(1, len(info_permutation) + 1)
    }
    strict_pairs = frozenset(
        (left, right)
        for left, left_profile in profiles.items()
        for right, right_profile in profiles.items()
        if left != right and left_profile.leq(right_profile)
    )
    observers = ("A", "B")
    observer_views = tuple(
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
        name=f"t167_rank_pair_{'-'.join(str(value) for value in info_permutation)}",
        description="Bounded n-event ordinal rank-pair T54 family member.",
        observer_views=observer_views,
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
        source_records=frozenset(
            {f"raw_{event}"} | {f"locked_{predecessor}" for predecessor in predecessors}
        ),
        target_records=frozenset({f"locked_{event}"}),
        profile=profile,
    )


def _size_audit_to_dict(audit: T167SizeAudit) -> dict[str, Any]:
    return {
        "event_count": audit.event_count,
        "total_rank_permutation_cases": audit.total_rank_permutation_cases,
        "t126_classification_counts": [
            {"classification": classification, "count": count}
            for classification, count in audit.t126_classification_counts
        ],
        "t126_pass_count": audit.t126_pass_count,
        "t156_pass_count": audit.t156_pass_count,
        "parent_interval_pass_count": audit.parent_interval_pass_count,
        "stable_labeled_survivor_count": audit.stable_labeled_survivor_count,
        "stable_labeled_survivor_fraction": _fraction_to_dict(
            audit.stable_labeled_survivor_fraction
        ),
        "stable_conditional_after_parent_fraction": _fraction_to_dict(
            audit.stable_conditional_after_parent_fraction
        ),
        "oriented_survivor_class_count": audit.oriented_survivor_class_count,
        "order_dual_survivor_class_count": audit.order_dual_survivor_class_count,
        "largest_oriented_class_size": audit.largest_oriented_class_size,
        "largest_oriented_class_probability": _fraction_to_dict(
            audit.largest_oriented_class_probability
        ),
        "singleton_oriented_class_count": audit.singleton_oriented_class_count,
        "deletion_pass_distribution": [
            {"deletion_pass_count": pass_count, "case_count": case_count}
            for pass_count, case_count in audit.deletion_pass_distribution
        ],
        "stable_strict_pair_distribution": [
            {"strict_pair_count": strict_pair_count, "case_count": case_count}
            for strict_pair_count, case_count in audit.stable_strict_pair_distribution
        ],
    }


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t167_result_to_dict(run_t167_analysis()), indent=2))
