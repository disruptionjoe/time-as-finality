"""T57: Finality Reflection Property.

Phase 21 introduced a precise obligation for the T56 gap-presheaf move:
G(U) = A(U) - F(U) is not automatically closed under restriction just because
A is a presheaf. The complement of a subassignment can fail to restrict.

This module checks the specific TaF apparent-order construction:

    F(U) = record-dependency transitive closure over U-accessible events.

For nested record-access patches V <= U, every F(V) witness also exists in
F(U), because the events and direct dependencies visible at V are included in
those visible at U. Equivalently:

    (a, b) not in F(U) implies (a, b) not in F(V).

That is the Finality Reflection Property (FRP). FRP is exactly what is needed
for gaps at a larger patch to restrict to gaps at a smaller patch.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any

from models.sheaf_cohomology_apparent_finality import (
    EventNode,
    FiniteObserverCover,
    ObserverPatch,
    compute_apparent_order,
    compute_global_order,
    restrict_order,
)


Pair = tuple[str, str]


def _nonreflexive(order: frozenset[Pair]) -> frozenset[Pair]:
    return frozenset((a, b) for (a, b) in order if a != b)


def _ordered_pairs(names: frozenset[str]) -> frozenset[Pair]:
    return frozenset((a, b) for a in names for b in names if a != b)


def _proper_nested_patch_pairs(
    cover: FiniteObserverCover,
) -> tuple[tuple[ObserverPatch, ObserverPatch], ...]:
    """Return (larger, smaller) patch pairs with smaller records < larger records."""
    pairs: list[tuple[ObserverPatch, ObserverPatch]] = []
    for larger in cover.patches:
        for smaller in cover.patches:
            if larger.name == smaller.name:
                continue
            if smaller.accessible_records < larger.accessible_records:
                pairs.append((larger, smaller))
    return tuple(pairs)


def gap_pairs(
    cover: FiniteObserverCover,
    patch: ObserverPatch,
    global_order: frozenset[Pair] | None = None,
) -> frozenset[Pair]:
    """Return G(U) = A(U) - F(U), excluding reflexive pairs."""
    if global_order is None:
        global_order = compute_global_order(cover)
    accessible = cover.accessible_event_names(patch)
    ambient = _nonreflexive(restrict_order(global_order, accessible))
    apparent = _nonreflexive(compute_apparent_order(cover, patch))
    return frozenset(ambient - apparent)


@dataclass(frozen=True)
class ReflectionViolation:
    larger_patch: str
    smaller_patch: str
    pair: Pair
    explanation: str


@dataclass(frozen=True)
class ReflectionCheck:
    cover_name: str
    comparable_patch_pairs: int
    checked_event_pairs: int
    holds: bool
    violations: tuple[ReflectionViolation, ...]
    explanation: str


def check_finality_reflection(cover: FiniteObserverCover) -> ReflectionCheck:
    """
    Check FRP over all nested patch pairs in a finite cover.

    For V < U, FRP is checked in its witness form:

        F(V) subset rho_{U->V}(F(U)).

    This is equivalent to absence reflection over V-accessible pairs:

        (a,b) not in F(U) => (a,b) not in F(V).
    """
    violations: list[ReflectionViolation] = []
    checked_event_pairs = 0
    nested_pairs = _proper_nested_patch_pairs(cover)

    for larger, smaller in nested_pairs:
        smaller_events = cover.accessible_event_names(smaller)
        larger_apparent_on_smaller = _nonreflexive(
            restrict_order(compute_apparent_order(cover, larger), smaller_events)
        )
        smaller_apparent = _nonreflexive(compute_apparent_order(cover, smaller))
        checked_event_pairs += len(_ordered_pairs(smaller_events))

        for pair in sorted(smaller_apparent - larger_apparent_on_smaller):
            violations.append(
                ReflectionViolation(
                    larger_patch=larger.name,
                    smaller_patch=smaller.name,
                    pair=pair,
                    explanation=(
                        "Smaller patch computes an apparent order pair that "
                        "the larger patch does not compute after restriction."
                    ),
                )
            )

    holds = len(violations) == 0
    if holds:
        explanation = (
            "FRP holds: every apparent-order witness at a smaller record-access "
            "patch is preserved at every larger patch. Apparent order is "
            "covariantly monotone under record-access inclusion, even though "
            "it is not a contravariant presheaf."
        )
    else:
        explanation = (
            "FRP fails: some smaller patch computes an apparent-order pair "
            "not computed by a larger patch. The gap assignment is not licensed."
        )

    return ReflectionCheck(
        cover_name=cover.name,
        comparable_patch_pairs=len(nested_pairs),
        checked_event_pairs=checked_event_pairs,
        holds=holds,
        violations=tuple(violations),
        explanation=explanation,
    )


@dataclass(frozen=True)
class GapRestrictionViolation:
    larger_patch: str
    smaller_patch: str
    pair: Pair
    explanation: str


@dataclass(frozen=True)
class NonLiftingGapExample:
    larger_patch: str
    smaller_patch: str
    pair: Pair
    explanation: str


@dataclass(frozen=True)
class GapRestrictionCheck:
    cover_name: str
    comparable_patch_pairs: int
    holds: bool
    violations: tuple[GapRestrictionViolation, ...]
    non_lifting_examples: tuple[NonLiftingGapExample, ...]
    explanation: str


def check_gap_restriction_closure(cover: FiniteObserverCover) -> GapRestrictionCheck:
    """
    Check that G(U) restricts into G(V) for V < U.

    This is closure, not surjectivity. A smaller patch can have extra gaps that
    disappear at a larger patch once hidden intermediaries become visible.
    """
    global_order = compute_global_order(cover)
    violations: list[GapRestrictionViolation] = []
    non_lifting: list[NonLiftingGapExample] = []
    nested_pairs = _proper_nested_patch_pairs(cover)

    for larger, smaller in nested_pairs:
        smaller_events = cover.accessible_event_names(smaller)
        larger_gap = gap_pairs(cover, larger, global_order)
        smaller_gap = gap_pairs(cover, smaller, global_order)

        restricted_larger_gap = _nonreflexive(restrict_order(larger_gap, smaller_events))
        for pair in sorted(restricted_larger_gap - smaller_gap):
            violations.append(
                GapRestrictionViolation(
                    larger_patch=larger.name,
                    smaller_patch=smaller.name,
                    pair=pair,
                    explanation=(
                        "A larger-patch gap restricts to a pair that is not a "
                        "gap at the smaller patch."
                    ),
                )
            )

        for pair in sorted(smaller_gap - restricted_larger_gap):
            non_lifting.append(
                NonLiftingGapExample(
                    larger_patch=larger.name,
                    smaller_patch=smaller.name,
                    pair=pair,
                    explanation=(
                        "The smaller patch has a gap that does not lift from "
                        "the larger patch. This is expected: restriction "
                        "closure is not a lifting or surjectivity claim."
                    ),
                )
            )

    holds = len(violations) == 0
    if holds:
        explanation = (
            "Gap restriction closure holds: every larger-patch gap restricts "
            "to a smaller-patch gap. Smaller patches may still have additional "
            "phantom gaps that vanish when larger patches expose hidden "
            "intermediaries."
        )
    else:
        explanation = (
            "Gap restriction closure fails. FRP is insufficient or violated "
            "for this cover."
        )

    return GapRestrictionCheck(
        cover_name=cover.name,
        comparable_patch_pairs=len(nested_pairs),
        holds=holds,
        violations=tuple(violations),
        non_lifting_examples=tuple(non_lifting),
        explanation=explanation,
    )


@dataclass(frozen=True)
class ComplementCounterexample:
    ambient_larger: frozenset[Pair]
    ambient_smaller: frozenset[Pair]
    sub_larger: frozenset[Pair]
    sub_smaller: frozenset[Pair]
    complement_larger: frozenset[Pair]
    complement_smaller: frozenset[Pair]
    frp_holds: bool
    complement_restriction_closed: bool
    witness_pair: Pair
    explanation: str


def build_generic_complement_counterexample() -> ComplementCounterexample:
    """
    Show why FRP is a real obligation, not a formal freebie.

    Let A(U) = A(V) = {(x,y)}. Let F(U) be empty but F(V) contain (x,y).
    Then the complement G(U) contains (x,y), but G(V) is empty. Restricting
    G(U) to V exits G(V).
    """
    pair = ("x", "y")
    ambient_larger = frozenset({pair})
    ambient_smaller = frozenset({pair})
    sub_larger = frozenset()
    sub_smaller = frozenset({pair})
    complement_larger = ambient_larger - sub_larger
    complement_smaller = ambient_smaller - sub_smaller
    frp_holds = not (pair not in sub_larger and pair in sub_smaller)
    complement_closed = complement_larger <= complement_smaller

    return ComplementCounterexample(
        ambient_larger=ambient_larger,
        ambient_smaller=ambient_smaller,
        sub_larger=sub_larger,
        sub_smaller=sub_smaller,
        complement_larger=complement_larger,
        complement_smaller=complement_smaller,
        frp_holds=frp_holds,
        complement_restriction_closed=complement_closed,
        witness_pair=pair,
        explanation=(
            "The ambient assignment is stable, but the chosen subassignment "
            "violates FRP: the smaller patch has (x,y) while the larger patch "
            "does not. Therefore the complement of the larger patch restricts "
            "outside the smaller complement."
        ),
    )


def _record_lattice_patches(records: tuple[str, ...]) -> tuple[ObserverPatch, ...]:
    patches: list[ObserverPatch] = []
    for size in range(len(records) + 1):
        for subset in combinations(records, size):
            name = "U_empty" if not subset else "U_" + "_".join(subset)
            patches.append(
                ObserverPatch(name=name, accessible_records=frozenset(subset))
            )
    return tuple(patches)


def build_hidden_intermediary_lattice_cover() -> FiniteObserverCover:
    """T56 hidden-intermediary witness expanded to the full record lattice."""
    events = (
        EventNode(
            name="e_j",
            source_records=frozenset(),
            target_records=frozenset({"r1"}),
            causal=1,
            info=1,
        ),
        EventNode(
            name="e_k",
            source_records=frozenset({"r1"}),
            target_records=frozenset({"r2"}),
            causal=2,
            info=2,
        ),
        EventNode(
            name="e_i",
            source_records=frozenset({"r2"}),
            target_records=frozenset({"r3"}),
            causal=3,
            info=3,
        ),
    )
    return FiniteObserverCover(
        name="hidden_intermediary_record_lattice",
        events=events,
        patches=_record_lattice_patches(("r1", "r2", "r3")),
    )


def build_branching_dependency_lattice_cover() -> FiniteObserverCover:
    """A non-chain witness: two root records jointly enable a later event."""
    events = (
        EventNode(
            name="e_a",
            source_records=frozenset(),
            target_records=frozenset({"ra"}),
            causal=1,
            info=1,
        ),
        EventNode(
            name="e_b",
            source_records=frozenset(),
            target_records=frozenset({"rb"}),
            causal=1,
            info=1,
        ),
        EventNode(
            name="e_c",
            source_records=frozenset({"ra", "rb"}),
            target_records=frozenset({"rc"}),
            causal=2,
            info=2,
        ),
        EventNode(
            name="e_d",
            source_records=frozenset({"rc"}),
            target_records=frozenset({"rd"}),
            causal=3,
            info=3,
        ),
    )
    return FiniteObserverCover(
        name="branching_dependency_record_lattice",
        events=events,
        patches=_record_lattice_patches(("ra", "rb", "rc", "rd")),
    )


@dataclass(frozen=True)
class HypothesisEvaluation:
    hypothesis_id: str
    status: str
    claim: str
    evidence: str


@dataclass(frozen=True)
class T57Result:
    theorem_statement: str
    reflection_checks: tuple[ReflectionCheck, ...]
    gap_checks: tuple[GapRestrictionCheck, ...]
    complement_counterexample: ComplementCounterexample
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    best_supported: str
    limits: tuple[str, ...]
    next_questions: tuple[str, ...]


def run_t57_analysis() -> T57Result:
    covers = (
        build_hidden_intermediary_lattice_cover(),
        build_branching_dependency_lattice_cover(),
    )
    reflection_checks = tuple(check_finality_reflection(c) for c in covers)
    gap_checks = tuple(check_gap_restriction_closure(c) for c in covers)
    counterexample = build_generic_complement_counterexample()

    all_frp = all(check.holds for check in reflection_checks)
    all_gap = all(check.holds for check in gap_checks)
    has_non_lifting = any(check.non_lifting_examples for check in gap_checks)

    theorem_statement = (
        "Finality Reflection Property (v0.1): for the T56 apparent-order "
        "construction, if V is a proper subpatch of U in record-access order, "
        "then every non-reflexive pair in F(V) appears in the restriction of "
        "F(U) to V-accessible events. Equivalently, absence from F(U) reflects "
        "downward to absence from F(V). Therefore G(U)=A(U)-F(U) is closed "
        "under restriction. This closure is conditional on the TaF apparent-order "
        "definition and is not true for arbitrary complements."
    )

    hypotheses = (
        HypothesisEvaluation(
            hypothesis_id="H0",
            status="refuted" if all_frp else "supported",
            claim="The T56 apparent-order construction need not satisfy FRP.",
            evidence=(
                "FRP held across both record-lattice witnesses."
                if all_frp
                else "At least one reflection violation was found."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H1",
            status="supported" if all_frp else "refuted",
            claim="Apparent order is monotone under record-access inclusion.",
            evidence=(
                "For every nested patch pair V<U, F(V) was included in "
                "rho(F(U))."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H2",
            status="supported" if all_gap else "refuted",
            claim="The T56 gap assignment is restriction-closed once FRP holds.",
            evidence=(
                "Every larger-patch gap restricted into the smaller-patch gap."
                if all_gap
                else "A larger-patch gap failed to restrict into a smaller gap."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H3",
            status="refuted",
            claim="Complement restriction closure is automatic for any subassignment.",
            evidence=(
                "The generic complement counterexample violates FRP and its "
                "larger complement restricts outside the smaller complement."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H4",
            status="left_open",
            claim="FRP resolves the T56 medium circular risk on arrow direction.",
            evidence=(
                "FRP only proves monotonicity after directed source/target "
                "records are given. It does not derive that direction from "
                "substrate-free task composability."
            ),
        ),
    )

    best_supported = (
        "T57 supports FRP for the T56 apparent-order model and licenses the "
        "gap-presheaf restriction step as a finite theorem. It also rejects "
        "the stronger idea that complements are automatically presheaves and "
        "leaves the arrow-origin circularity question open."
    )

    limits = (
        "The executable witnesses are finite record lattices, not an arbitrary "
        "machine-checked proof over all finite covers.",
        "The proof assumes the T56 event-access rule and record-dependency "
        "source/target relation.",
        "FRP gives restriction closure only; smaller-patch phantom gaps need "
        "not lift to larger patches.",
        "FRP does not derive the direction of finality arrows.",
    )

    next_questions = (
        "Turn the proof sketch into a short formal lemma in FORMALISM with "
        "explicit quantifiers over finite covers.",
        "Use FRP to test whether H0(G) is exactly the T51-T52 phantom-pair set.",
        "Attack T56 Q4 separately: derive or reject arrow direction from "
        "constructor-style task composability.",
    )

    if not has_non_lifting:
        limits = limits + (
            "No non-lifting gap was observed, so the closure-vs-lifting "
            "boundary needs another witness.",
        )

    return T57Result(
        theorem_statement=theorem_statement,
        reflection_checks=reflection_checks,
        gap_checks=gap_checks,
        complement_counterexample=counterexample,
        hypothesis_evaluations=hypotheses,
        best_supported=best_supported,
        limits=limits,
        next_questions=next_questions,
    )


def _pairs_to_lists(pairs: frozenset[Pair]) -> list[list[str]]:
    return [[a, b] for (a, b) in sorted(pairs)]


def t57_result_to_dict(result: T57Result) -> dict[str, Any]:
    return {
        "theorem_statement": result.theorem_statement,
        "reflection_checks": [
            {
                "cover_name": check.cover_name,
                "comparable_patch_pairs": check.comparable_patch_pairs,
                "checked_event_pairs": check.checked_event_pairs,
                "holds": check.holds,
                "violations": [
                    {
                        "larger_patch": v.larger_patch,
                        "smaller_patch": v.smaller_patch,
                        "pair": list(v.pair),
                        "explanation": v.explanation,
                    }
                    for v in check.violations
                ],
                "explanation": check.explanation,
            }
            for check in result.reflection_checks
        ],
        "gap_checks": [
            {
                "cover_name": check.cover_name,
                "comparable_patch_pairs": check.comparable_patch_pairs,
                "holds": check.holds,
                "violations": [
                    {
                        "larger_patch": v.larger_patch,
                        "smaller_patch": v.smaller_patch,
                        "pair": list(v.pair),
                        "explanation": v.explanation,
                    }
                    for v in check.violations
                ],
                "non_lifting_examples": [
                    {
                        "larger_patch": ex.larger_patch,
                        "smaller_patch": ex.smaller_patch,
                        "pair": list(ex.pair),
                        "explanation": ex.explanation,
                    }
                    for ex in check.non_lifting_examples
                ],
                "explanation": check.explanation,
            }
            for check in result.gap_checks
        ],
        "complement_counterexample": {
            "ambient_larger": _pairs_to_lists(
                result.complement_counterexample.ambient_larger
            ),
            "ambient_smaller": _pairs_to_lists(
                result.complement_counterexample.ambient_smaller
            ),
            "sub_larger": _pairs_to_lists(result.complement_counterexample.sub_larger),
            "sub_smaller": _pairs_to_lists(
                result.complement_counterexample.sub_smaller
            ),
            "complement_larger": _pairs_to_lists(
                result.complement_counterexample.complement_larger
            ),
            "complement_smaller": _pairs_to_lists(
                result.complement_counterexample.complement_smaller
            ),
            "frp_holds": result.complement_counterexample.frp_holds,
            "complement_restriction_closed": (
                result.complement_counterexample.complement_restriction_closed
            ),
            "witness_pair": list(result.complement_counterexample.witness_pair),
            "explanation": result.complement_counterexample.explanation,
        },
        "hypothesis_evaluations": [
            {
                "id": h.hypothesis_id,
                "status": h.status,
                "claim": h.claim,
                "evidence": h.evidence,
            }
            for h in result.hypothesis_evaluations
        ],
        "best_supported": result.best_supported,
        "limits": list(result.limits),
        "next_questions": list(result.next_questions),
    }
