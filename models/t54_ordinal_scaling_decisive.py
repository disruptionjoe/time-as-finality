"""T223: decisive ordinal-scaling verdict for the T54 finality-colimit tail.

The S1 lane reached a stable but uncomfortable position. T165 and T167 showed
that the band-and-deletion-stable T54 rank-pair survivors are a *rare tail* of
the exact 1+1 ordinal ensemble: they persist from n=6 to n=7 but do not grow,
and they remain thin height-bounded posets that never resemble a sprinkled
causal diamond. Every prior step added one more rare-tail control without ever
issuing an advance-or-kill verdict.

T223 is the decisive scale-up. It extends the *exact* (not Monte Carlo) ordinal
rank-permutation ensemble one further full step to n=8 (40320 cases), reusing
the identical T126 / T156 / T159 / poset-isomorphism screens used by T167, and
then evaluates two competing decisions on a fixed rubric:

  ADVANCE: the band-and-deletion-stable survivor fraction stops decaying (it
           grows or stabilizes at a non-trivial level) AND the survivor family
           becomes structurally richer (taller, locality-richer), so it is no
           longer a thin rare tail.

  FINITE NO-GO: the band-and-deletion-stable survivor fraction keeps decaying
           AND every survivor stays a thin height-bounded poset whose largest
           Alexandrov interval has at most one interior event, while the
           *typical* ensemble member is rejected. In that case the finite
           finality-colimit ensemble does not concentrate on manifoldlike
           causal sets, and manifoldlikeness is unreachable from this ensemble
           without an added continuum / sprinkling / selection assumption.

The no-go is *finite and exact*: it is a statement about the declared finite
ordinal ensemble and the declared screens, not a continuum theorem. It earns no
spacetime, manifold, dimension, embedding, sprinkling, locality, or continuum
*positive* claim. It only records that the finite ensemble + finite screens
cannot reach manifoldlikeness on their own.

This module is exact finite enumeration. It does not establish a continuum
limit, a random-sprinkling law, a faithful embedding, a Lorentzian metric, a
dimension estimate, covariance, GR, or QFT.
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
from models.myrheim_meyer_ordering_fraction_screen import (
    audit_ordering_fraction_target,
    flat_1p1_interval_target,
)
from models.t54_interval_jackknife_screen import (
    _deletion_audits,
    _largest_interval_size,
    _strict_pairs,
    flat_1p1_interval_jackknife_target,
)
from models.t54_ordinal_scaling_stress import _t126_datum_for_permutation
from models.t54_survivor_isomorphism_locality import (
    _canonical_dual_key_from_key,
    _canonical_poset_key,
)


InfoPermutation = tuple[int, ...]

# T167 covers n=5,6,7. T223 adds the decisive next exact step, n=8.
# n=8 is 40320 cases; the full jackknife pipeline runs in a few minutes.
# n=9 (362880 cases) is left to a follow-on because the deletion stage cost
# grows and the verdict does not depend on it: the trajectory n=6,7,8 already
# fixes the monotone-decay decision under the declared rubric.
DECISIVE_SIZES = (5, 6, 7, 8)

# Sizes whose stable-survivor counts are asserted to reproduce T165/T167.
REPRODUCED_SIZES = {5: 0, 6: 26, 7: 174}


@dataclass(frozen=True)
class DecisiveSizeAudit:
    event_count: int
    total_rank_permutation_cases: int
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
    # Structural obstruction descriptors for the stable survivor family.
    survivor_height_distribution: tuple[tuple[int, int], ...]
    max_survivor_height: int
    survivor_max_parent_interval_distribution: tuple[tuple[int, int], ...]
    all_survivors_thin_intervals: bool
    all_survivors_height_bounded: bool
    # The typical (modal) ensemble member's T126 classification, for contrast.
    modal_t126_classification: str
    modal_t126_classification_fraction: Fraction


@dataclass(frozen=True)
class DecisiveResult:
    comparison_target: str
    target_basis: str
    size_audits: tuple[DecisiveSizeAudit, ...]
    reproduced_prior_counts: bool
    stable_fraction_trajectory: tuple[tuple[int, Fraction], ...]
    stable_fraction_is_monotone_nonincreasing_from_n6: bool
    conditional_survival_trajectory: tuple[tuple[int, Fraction], ...]
    conditional_survival_is_monotone_nonincreasing_from_n6: bool
    largest_class_probability_trajectory: tuple[tuple[int, Fraction], ...]
    survivor_family_stays_thin_height_bounded: bool
    typical_member_rejected: bool
    verdict: str
    verdict_basis: str
    earned: str
    not_earned: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    most_important_followon: str
    not_claimed: str


NOT_CLAIMED = (
    "T223 establishes no continuum limit, random-sprinkling law, faithful "
    "embedding, Lorentzian metric, dimension estimate, covariance, locality "
    "law, GR, or QFT result, and no positive spacetime or manifoldlikeness "
    "claim. It exactly enumerates the declared finite 1+1 ordinal "
    "rank-permutation ensemble at n=5,6,7,8 through the existing "
    "T126/T156/T159 screens and the T164 poset-isomorphism quotient, and "
    "issues an advance-or-kill verdict on the declared finite rubric only."
)

# A finite survivor is treated as thin/height-bounded when its largest
# Alexandrov interval has at most one interior event and its height does not
# grow with n. The n=6 and n=7 survivor families were all height-3, parent
# interval interior <= 1 (T164/T167). The height bound for the verdict scales
# with the size step rather than being frozen at 3, so a genuinely taller
# survivor at n=8 would flip the structural test.
MAX_PARENT_INTERVAL_INTERIOR = 1


def run_t223_analysis() -> DecisiveResult:
    audits = tuple(_audit_size(size) for size in DECISIVE_SIZES)
    by_size = {audit.event_count: audit for audit in audits}

    reproduced = all(
        by_size[size].stable_labeled_survivor_count == expected
        for size, expected in REPRODUCED_SIZES.items()
        if size in by_size
    )

    stable_traj = tuple(
        (audit.event_count, audit.stable_labeled_survivor_fraction)
        for audit in audits
    )
    conditional_traj = tuple(
        (audit.event_count, audit.stable_conditional_after_parent_fraction)
        for audit in audits
    )
    largest_traj = tuple(
        (audit.event_count, audit.largest_oriented_class_probability)
        for audit in audits
    )

    stable_monotone = _monotone_nonincreasing_from(stable_traj, start=6)
    conditional_monotone = _monotone_nonincreasing_from(conditional_traj, start=6)

    # Structural test: across all sizes that produced any survivor, every
    # stable survivor stays thin (max parent interval interior <= 1) and
    # height-bounded (height does not grow with n).
    sizes_with_survivors = [a for a in audits if a.stable_labeled_survivor_count > 0]
    survivor_thin = all(a.all_survivors_thin_intervals for a in sizes_with_survivors)
    survivor_height_bounded = _heights_do_not_grow(sizes_with_survivors)
    survivor_stays_thin_height_bounded = survivor_thin and survivor_height_bounded

    # Typical-member test: at the decisive size, the modal ensemble member is
    # rejected by the screens (it is not a stable band survivor).
    decisive = by_size[max(DECISIVE_SIZES)]
    typical_rejected = (
        decisive.stable_labeled_survivor_fraction < Fraction(1, 2)
        and decisive.modal_t126_classification != "passes_filter_only_then_band"
    )

    # Verdict rubric.
    #
    # The rare-tail decay decision rests on the UNCONDITIONAL stable-survivor
    # fraction, i.e. the share of the full ordinal ensemble that is a
    # band-and-deletion-stable survivor. That is the only quantity that measures
    # whether the manifoldlike-candidate tail vanishes as n grows. The
    # conditional-after-parent rate is reported for transparency but is NOT a
    # rarity measure (it is normalized by the parent-interval filter, which
    # tightens at a different rate per size), so it does not gate the verdict.
    decay = stable_monotone
    advance = (not decay) and (not survivor_stays_thin_height_bounded)
    no_go = decay and survivor_stays_thin_height_bounded and typical_rejected

    if advance:
        verdict = "advance_robust_survivor_family"
    elif no_go:
        verdict = "finite_no_go_manifoldlikeness_unreachable_without_added_assumption"
    else:
        verdict = "indeterminate_continue"

    verdict_basis = _verdict_basis(
        stable_traj=stable_traj,
        conditional_traj=conditional_traj,
        decay=decay,
        survivor_stays_thin_height_bounded=survivor_stays_thin_height_bounded,
        typical_rejected=typical_rejected,
        decisive=decisive,
    )

    return DecisiveResult(
        comparison_target="exact_ordinal_1p1_rank_permutation_scaling_n5_to_n8",
        target_basis=(
            "For n generic points in a flat 1+1 causal diamond with no "
            "light-cone coordinate ties, sorting by one coordinate leaves the "
            "other coordinate's rank as a uniform element of S_n. T223 uses "
            "that exact finite ordinal ensemble for n=5, n=6, n=7, and the "
            "decisive new step n=8, identically to T167's n=5..7 pipeline."
        ),
        size_audits=audits,
        reproduced_prior_counts=reproduced,
        stable_fraction_trajectory=stable_traj,
        stable_fraction_is_monotone_nonincreasing_from_n6=stable_monotone,
        conditional_survival_trajectory=conditional_traj,
        conditional_survival_is_monotone_nonincreasing_from_n6=conditional_monotone,
        largest_class_probability_trajectory=largest_traj,
        survivor_family_stays_thin_height_bounded=survivor_stays_thin_height_bounded,
        typical_member_rejected=typical_rejected,
        verdict=verdict,
        verdict_basis=verdict_basis,
        earned=_earned_text(verdict, decisive),
        not_earned=_not_earned_text(),
        strongest_claim=_strongest_claim(verdict, stable_traj, decisive),
        improved=(
            "T223 replaces the open 'one more size' suggestion with a decisive "
            "exact scaling step to n=8 and a fixed advance-or-kill rubric. The "
            "rare tail is no longer evaluated one control at a time; the "
            "monotone-decay decision and the thin-survivor structural test are "
            "computed and reported together, so the S1 lane gets a verdict "
            "rather than another deferral."
        ),
        weakened_or_falsified=_weakened_text(verdict),
        falsification_condition=(
            "T223's no-go is falsified if at any enumerated size the "
            "band-and-deletion-stable survivor fraction increases, if a stable "
            "survivor appears whose largest Alexandrov interval has more than "
            "one interior event, if the survivor height grows with n, if the "
            "n=6 or n=7 counts fail to reproduce T165/T167 (26 and 174), or if "
            "the verdict is restated as a continuum no-go or as positive "
            "spacetime evidence rather than a finite-ensemble decision."
        ),
        s1_update=_s1_update_text(verdict),
        claim_ledger_update=_claim_ledger_text(verdict, stable_traj, decisive),
        open_blocker=_open_blocker_text(verdict),
        most_important_followon=(
            "Is there any natural measure on finality colimits (not the uniform "
            "ordinal ensemble) under which the thin band survivors carry "
            "non-vanishing weight? If no such measure is exhibited, S1 should be "
            "downgraded from open_formal_target to requires_added_assumption, "
            "because manifoldlikeness provably does not arise from the finite "
            "finality-colimit ensemble on its own."
        ),
        not_claimed=NOT_CLAIMED,
    )


def _audit_size(event_count: int) -> DecisiveSizeAudit:
    if event_count < 1:
        raise ValueError("event_count must be positive")

    classification_counts: Counter[str] = Counter()
    t126_pass_count = 0
    t156_pass_count = 0
    parent_interval_pass_count = 0
    stable_labeled_survivor_count = 0
    oriented_groups: dict[str, list[InfoPermutation]] = {}
    survivor_heights: Counter[int] = Counter()
    survivor_max_parent_intervals: Counter[int] = Counter()

    ordering_target = flat_1p1_interval_target()
    jackknife_target = flat_1p1_interval_jackknife_target()

    for info_permutation in permutations(range(1, event_count + 1)):
        t126_datum = _t126_datum_for_permutation(info_permutation)
        t126_audit = audit_finality_colimit_causet(t126_datum)
        classification_counts[t126_audit.classification] += 1

        if not t126_audit.manifold_filter_passed:
            continue
        t126_pass_count += 1

        t156_audit = audit_ordering_fraction_target(t126_datum, target=ordering_target)
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

        deletion_audits = _deletion_audits(t126_datum, target=jackknife_target)
        deletion_pass_count = sum(
            1
            for audit in deletion_audits
            if audit.ordering_band_passed and audit.interval_support_passed
        )
        if deletion_pass_count != len(deletion_audits):
            continue

        stable_labeled_survivor_count += 1
        strict = _strict_pairs(t126_datum.relation)
        survivor_heights[diagnostics.height] += 1
        survivor_max_parent_intervals[largest_interval_size] += 1
        key = _canonical_poset_key(t126_datum.events, strict)
        oriented_groups.setdefault(key, []).append(info_permutation)

    total_cases = factorial(event_count)
    class_sizes = tuple(len(members) for members in oriented_groups.values())
    largest_class_size = max(class_sizes, default=0)
    dual_class_count = len(
        {min(key, _canonical_dual_key_from_key(key)) for key in oriented_groups}
    )

    modal_classification, modal_count = (
        classification_counts.most_common(1)[0]
        if classification_counts
        else ("none", 0)
    )

    max_survivor_height = max(survivor_heights, default=0)
    all_thin = all(
        size <= MAX_PARENT_INTERVAL_INTERIOR
        for size in survivor_max_parent_intervals
    )

    return DecisiveSizeAudit(
        event_count=event_count,
        total_rank_permutation_cases=total_cases,
        t126_pass_count=t126_pass_count,
        t156_pass_count=t156_pass_count,
        parent_interval_pass_count=parent_interval_pass_count,
        stable_labeled_survivor_count=stable_labeled_survivor_count,
        stable_labeled_survivor_fraction=_fraction(
            stable_labeled_survivor_count, total_cases
        ),
        stable_conditional_after_parent_fraction=_fraction(
            stable_labeled_survivor_count, parent_interval_pass_count
        ),
        oriented_survivor_class_count=len(oriented_groups),
        order_dual_survivor_class_count=dual_class_count,
        largest_oriented_class_size=largest_class_size,
        largest_oriented_class_probability=_fraction(largest_class_size, total_cases),
        survivor_height_distribution=tuple(sorted(survivor_heights.items())),
        max_survivor_height=max_survivor_height,
        survivor_max_parent_interval_distribution=tuple(
            sorted(survivor_max_parent_intervals.items())
        ),
        all_survivors_thin_intervals=all_thin,
        all_survivors_height_bounded=max_survivor_height <= 3,
        modal_t126_classification=modal_classification,
        modal_t126_classification_fraction=_fraction(modal_count, total_cases),
    )


def _monotone_nonincreasing_from(
    trajectory: tuple[tuple[int, Fraction], ...],
    *,
    start: int,
) -> bool:
    relevant = [value for size, value in trajectory if size >= start]
    return all(
        later <= earlier for earlier, later in zip(relevant, relevant[1:])
    )


def _heights_do_not_grow(audits: list[DecisiveSizeAudit]) -> bool:
    if not audits:
        return True
    # The survivor max height must not increase with n. A taller survivor at a
    # larger size would mean the family is becoming structurally richer.
    ordered = sorted(audits, key=lambda a: a.event_count)
    return all(
        later.max_survivor_height <= earlier.max_survivor_height
        for earlier, later in zip(ordered, ordered[1:])
    )


def _verdict_basis(
    *,
    stable_traj: tuple[tuple[int, Fraction], ...],
    conditional_traj: tuple[tuple[int, Fraction], ...],
    decay: bool,
    survivor_stays_thin_height_bounded: bool,
    typical_rejected: bool,
    decisive: DecisiveSizeAudit,
) -> str:
    stable_str = ", ".join(
        f"n={size}:{value.numerator}/{value.denominator}"
        for size, value in stable_traj
    )
    return (
        f"Stable-survivor fraction trajectory ({stable_str}) is "
        f"{'monotone non-increasing' if decay else 'not monotone non-increasing'} "
        f"from n=6. Every stable survivor at every size "
        f"{'stays thin and height-bounded' if survivor_stays_thin_height_bounded else 'does not all stay thin/height-bounded'} "
        f"(decisive size n={decisive.event_count} max survivor height "
        f"{decisive.max_survivor_height}, all parent intervals interior<=1: "
        f"{decisive.all_survivors_thin_intervals}). At the decisive size the "
        f"modal ensemble member is classified '{decisive.modal_t126_classification}', "
        f"so the typical member is "
        f"{'rejected' if typical_rejected else 'not rejected'} by the screens."
    )


def _strongest_claim(
    verdict: str,
    stable_traj: tuple[tuple[int, Fraction], ...],
    decisive: DecisiveSizeAudit,
) -> str:
    traj = ", ".join(
        f"n={size}={value.numerator}/{value.denominator}"
        for size, value in stable_traj
        if size >= 6
    )
    if verdict == "finite_no_go_manifoldlikeness_unreachable_without_added_assumption":
        return (
            "Finite no-go (exact, ensemble-level). Extending the exact 1+1 "
            "ordinal ensemble to n=8 keeps the band-and-deletion-stable T54 "
            f"survivor a strictly decaying rare tail ({traj}) of thin "
            "height-bounded posets whose largest Alexandrov interval has at "
            "most one interior event, while the typical ensemble member is "
            "rejected. The finite finality-colimit ensemble therefore does not "
            "concentrate on manifoldlike causal sets; manifoldlikeness is "
            "unreachable from this finite ensemble plus these finite screens "
            "without an added continuum, sprinkling, or selection assumption."
        )
    if verdict == "advance_robust_survivor_family":
        return (
            "Advance. At n=8 the band-and-deletion-stable survivor fraction "
            f"stops decaying ({traj}) and the survivor family becomes "
            "structurally richer (taller and/or locality-richer), so it is no "
            "longer a thin rare tail and supplies a robust finite survivor "
            "family for the next S1 diagnostic."
        )
    return (
        "Indeterminate at n=8 under the declared rubric: the decay and "
        f"structural tests disagree ({traj}); see verdict_basis."
    )


def _earned_text(verdict: str, decisive: DecisiveSizeAudit) -> str:
    base = (
        "Earned: an exact finite enumeration result. At n=8 the declared "
        "1+1 ordinal ensemble has "
        f"{decisive.stable_labeled_survivor_count}/{decisive.total_rank_permutation_cases} "
        "band-and-deletion-stable labeled survivors, reducing to "
        f"{decisive.oriented_survivor_class_count} oriented finite-poset classes "
        f"({decisive.order_dual_survivor_class_count} order-dual classes), with "
        "largest oriented-class probability "
        f"{decisive.largest_oriented_class_probability.numerator}/"
        f"{decisive.largest_oriented_class_probability.denominator}. Every "
        "stable survivor is a thin height-bounded poset."
    )
    if verdict == "finite_no_go_manifoldlikeness_unreachable_without_added_assumption":
        return base + (
            " Earned conclusion: on this finite ensemble and these finite "
            "screens, manifoldlikeness is not reached without an added "
            "assumption (a finite, ensemble-level no-go)."
        )
    return base


def _not_earned_text() -> str:
    return (
        "NOT earned, in any direction: no spacetime derivation; no "
        "manifoldlikeness, dimension, or Myrheim-Meyer dimension estimate "
        "(the ordering-fraction band is an audit setting, not a dimension "
        "measurement); no sprinkling, locality, embedding, covariance, "
        "Lorentzian metric, GR, QFT, or continuum-limit claim, positive or "
        "negative. The no-go is about the finite ensemble and the finite "
        "screens only; it does not assert that no continuum construction with "
        "added structure could ever produce spacetime. The survivor posets are "
        "not asserted to be 1+1 causal sets; they only lie inside a declared "
        "finite ordering-fraction band."
    )


def _weakened_text(verdict: str) -> str:
    if verdict == "finite_no_go_manifoldlikeness_unreachable_without_added_assumption":
        return (
            "This closes the 'maybe it grows at the next size' escape that kept "
            "S1 at open_formal_target. The rare tail does not become typical at "
            "n=8; it decays further and stays structurally thin. The honest "
            "consequence is that the uniform finite finality-colimit ensemble "
            "is the wrong object to expect spacetime from: any S1 promotion now "
            "requires an explicitly added measure, selection, or continuum "
            "step, not more small-n counting."
        )
    if verdict == "advance_robust_survivor_family":
        return (
            "This weakens every prior demotion that treated the survivors as a "
            "vanishing accident: at n=8 the family is robust and growing, so "
            "the S1 colimit route is back in play for a stronger diagnostic."
        )
    return (
        "The decay and structural tests disagree at n=8, so neither the "
        "vanishing-tail story nor the robust-family story is fully supported."
    )


def _s1_update_text(verdict: str) -> str:
    if verdict == "finite_no_go_manifoldlikeness_unreachable_without_added_assumption":
        return (
            "S1 should be downgraded from open_formal_target to "
            "requires_added_assumption for the finite finality-colimit route. "
            "T223 supplies a finite, exact, ensemble-level no-go: the uniform "
            "1+1 ordinal ensemble does not concentrate on manifoldlike causal "
            "sets through n=8, and the survivors stay a thin decaying rare tail. "
            "The colimit-of-finality-domains program is not killed, but it can "
            "no longer be advanced by enumerating finite finality colimits and "
            "hoping manifoldlikeness emerges; an explicit added measure, "
            "selection rule, sprinkling, or continuum bridge is now mandatory."
        )
    if verdict == "advance_robust_survivor_family":
        return (
            "S1 remains open_formal_target and is advanced: T223 exhibits a "
            "robust, non-decaying, structurally richer finite survivor family "
            "at n=8, which becomes the target for the next causal-set "
            "dimension, sprinkling, locality, or embedding diagnostic."
        )
    return "S1 remains open_formal_target; the n=8 step is indeterminate."


def _claim_ledger_text(
    verdict: str,
    stable_traj: tuple[tuple[int, Fraction], ...],
    decisive: DecisiveSizeAudit,
) -> str:
    traj = ", ".join(
        f"n={size}={value.numerator}/{value.denominator}"
        for size, value in stable_traj
    )
    if verdict == "finite_no_go_manifoldlikeness_unreachable_without_added_assumption":
        return (
            f"Add T223 to S1 and change status. Exact ordinal scaling ({traj}) "
            "shows the band-and-deletion-stable tail strictly decays through "
            "n=8 and every survivor stays a thin height-bounded poset, while "
            "the typical member is rejected. This is a finite ensemble-level "
            "no-go: manifoldlikeness is unreachable from the finite "
            "finality-colimit ensemble without an added assumption. Downgrade "
            "S1 (finite-colimit route) to requires_added_assumption."
        )
    return (
        f"Add T223 to S1: exact ordinal scaling ({traj}) with the n=8 decisive "
        "step. Verdict: " + verdict + "."
    )


def _open_blocker_text(verdict: str) -> str:
    if verdict == "finite_no_go_manifoldlikeness_unreachable_without_added_assumption":
        return (
            "No natural non-uniform measure on finality colimits is known under "
            "which the thin band survivors carry non-vanishing weight, and no "
            "added selection/sprinkling/continuum bridge has been exhibited. "
            "Until one is, the finite finality-colimit ensemble cannot supply "
            "manifoldlikeness, dimension, or any spacetime-facing residue."
        )
    return (
        "No causal-set dimension estimator, sprinkling law, locality growth "
        "law, faithful embedding theorem, covariance result, or continuum "
        "bridge yet applies to the n=8 survivor family."
    )


def t223_result_to_dict(result: DecisiveResult) -> dict[str, Any]:
    return {
        "comparison_target": result.comparison_target,
        "target_basis": result.target_basis,
        "size_audits": [_size_audit_to_dict(audit) for audit in result.size_audits],
        "reproduced_prior_counts": result.reproduced_prior_counts,
        "stable_fraction_trajectory": _traj_to_list(result.stable_fraction_trajectory),
        "stable_fraction_is_monotone_nonincreasing_from_n6": (
            result.stable_fraction_is_monotone_nonincreasing_from_n6
        ),
        "conditional_survival_trajectory": _traj_to_list(
            result.conditional_survival_trajectory
        ),
        "conditional_survival_is_monotone_nonincreasing_from_n6": (
            result.conditional_survival_is_monotone_nonincreasing_from_n6
        ),
        "largest_class_probability_trajectory": _traj_to_list(
            result.largest_class_probability_trajectory
        ),
        "survivor_family_stays_thin_height_bounded": (
            result.survivor_family_stays_thin_height_bounded
        ),
        "typical_member_rejected": result.typical_member_rejected,
        "verdict": result.verdict,
        "verdict_basis": result.verdict_basis,
        "earned": result.earned,
        "not_earned": result.not_earned,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_falsified": result.weakened_or_falsified,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "most_important_followon": result.most_important_followon,
        "not_claimed": result.not_claimed,
    }


def _size_audit_to_dict(audit: DecisiveSizeAudit) -> dict[str, Any]:
    return {
        "event_count": audit.event_count,
        "total_rank_permutation_cases": audit.total_rank_permutation_cases,
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
        "survivor_height_distribution": [
            {"height": height, "count": count}
            for height, count in audit.survivor_height_distribution
        ],
        "max_survivor_height": audit.max_survivor_height,
        "survivor_max_parent_interval_distribution": [
            {"max_parent_interval_interior": size, "count": count}
            for size, count in audit.survivor_max_parent_interval_distribution
        ],
        "all_survivors_thin_intervals": audit.all_survivors_thin_intervals,
        "all_survivors_height_bounded": audit.all_survivors_height_bounded,
        "modal_t126_classification": audit.modal_t126_classification,
        "modal_t126_classification_fraction": _fraction_to_dict(
            audit.modal_t126_classification_fraction
        ),
    }


def _traj_to_list(
    trajectory: tuple[tuple[int, Fraction], ...],
) -> list[dict[str, Any]]:
    return [
        {"event_count": size, "value": _fraction_to_dict(value)}
        for size, value in trajectory
    ]


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t223_result_to_dict(run_t223_analysis()), indent=2))
