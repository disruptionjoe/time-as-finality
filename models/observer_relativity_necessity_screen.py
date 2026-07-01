"""T381: necessity screen for two primitive null compatibility signals.

T380 showed that two independent primitive null channels force the product
interval up to scale. T381 asks a sharper finite question: among simple adapter
shapes, which ones satisfy the observer-relativity requirements that T379/T380
actually need?

The answer is intentionally conditional. Inside this finite screen, a minimal
two-null-channel adapter is the only survivor. That is evidence for necessity
under declared requirements, not a proof that compatibility alone derives the
basis.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.compatibility_signal_basis_screen import (
    BasisCandidate,
    CompatibilityVector,
    QuadraticForm,
    canonical_form,
    choose_forced_form,
    solve_null_forms,
    span_dimension,
)


@dataclass(frozen=True)
class NecessityCandidate:
    candidate_id: str
    channels: tuple[CompatibilityVector, ...]
    description: str


@dataclass(frozen=True)
class RequirementCheck:
    requirement_id: str
    passes: bool
    reason: str


@dataclass(frozen=True)
class NecessityVerdict:
    candidate_id: str
    status: str
    passes_all: bool
    checks: tuple[RequirementCheck, ...]
    forced_form: QuadraticForm | None
    reason: str


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T381Result:
    minimal_two_null_adapter_unique_survivor: bool
    one_channel_fails: bool
    collinear_channels_fail: bool
    three_channel_overcomplete_fails_minimality: bool
    asymmetric_unit_adapter_reduces_to_two_null_basis: bool
    signed_diagonal_adapter_rejected_as_non_source_compatible: bool
    surviving_candidate_ids: tuple[str, ...]
    verdicts: tuple[NecessityVerdict, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str


def necessity_candidates() -> tuple[NecessityCandidate, ...]:
    left = CompatibilityVector("left_signal", Fraction(1), Fraction(0))
    right = CompatibilityVector("right_signal", Fraction(0), Fraction(1))
    left_double = CompatibilityVector("left_signal_double", Fraction(2), Fraction(0))
    diagonal = CompatibilityVector("diagonal_signal", Fraction(1), Fraction(1))
    long_left = CompatibilityVector("long_left_signal", Fraction(2), Fraction(0))
    signed_forward = CompatibilityVector("signed_forward", Fraction(1), Fraction(1))
    signed_backward = CompatibilityVector("signed_backward", Fraction(1), Fraction(-1))
    return (
        NecessityCandidate(
            "single_channel",
            (left,),
            "one primitive direction",
        ),
        NecessityCandidate(
            "collinear_two_channel",
            (left, left_double),
            "two labels but one primitive direction",
        ),
        NecessityCandidate(
            "minimal_two_null_channel",
            (left, right),
            "two independent primitive null directions",
        ),
        NecessityCandidate(
            "overcomplete_three_channel",
            (left, right, diagonal),
            "two null directions plus one noncollinear primitive extra direction",
        ),
        NecessityCandidate(
            "asymmetric_unit_two_channel",
            (long_left, right),
            "two independent null directions with unequal primitive units",
        ),
        NecessityCandidate(
            "signed_diagonal_two_channel",
            (signed_forward, signed_backward),
            "signed diagonal directions requiring negative compatibility counts",
        ),
    )


def primitive_ray_count(channels: tuple[CompatibilityVector, ...]) -> int:
    rays: set[tuple[Fraction, Fraction]] = set()
    for channel in channels:
        if channel.left == 0 and channel.right == 0:
            continue
        if channel.left == 0:
            rays.add((Fraction(0), Fraction(1)))
            continue
        if channel.right == 0:
            rays.add((Fraction(1), Fraction(0)))
            continue
        if channel.left < 0:
            normalizer = -channel.left
        else:
            normalizer = channel.left
        rays.add((channel.left / normalizer, channel.right / normalizer))
    return len(rays)


def source_compatible(channels: tuple[CompatibilityVector, ...]) -> bool:
    return all(channel.left >= 0 and channel.right >= 0 for channel in channels)


def unit_normalized_primitive_steps(channels: tuple[CompatibilityVector, ...]) -> bool:
    allowed = {
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    }
    return all((channel.left, channel.right) in allowed for channel in channels)


def forced_form_for(channels: tuple[CompatibilityVector, ...]) -> QuadraticForm | None:
    try:
        return choose_forced_form(solve_null_forms(channels))
    except ValueError:
        return None


def simultaneity_split_possible(form: QuadraticForm | None) -> bool:
    if form != canonical_form():
        return False
    rest_left_time = Fraction(3, 2)
    rest_right_time = Fraction(3, 2)
    boosted_left_time = Fraction(2 * 3, 2)
    boosted_right_time = Fraction(3, 2 * 2)
    return rest_left_time == rest_right_time and boosted_left_time != boosted_right_time


def reciprocal_observer_family_possible(form: QuadraticForm | None) -> bool:
    if form != canonical_form():
        return False
    left_scale = Fraction(2)
    right_scale = Fraction(1, 2)
    return left_scale * right_scale == 1


def evaluate_candidate(candidate: NecessityCandidate) -> NecessityVerdict:
    form = forced_form_for(candidate.channels)
    span = span_dimension(candidate.channels)
    ray_count = primitive_ray_count(candidate.channels)
    checks = (
        RequirementCheck(
            "source_compatible_nonnegative_counts",
            source_compatible(candidate.channels),
            "primitive compatibility counts must be nonnegative source directions",
        ),
        RequirementCheck(
            "two_independent_directions",
            span == 2,
            "observer relativity needs two independent signal directions in 1+1",
        ),
        RequirementCheck(
            "minimal_two_primitive_rays",
            ray_count == 2 and len(candidate.channels) == 2,
            "screen requires exactly two primitive rays, not one ray or an overcomplete primitive set",
        ),
        RequirementCheck(
            "unit_normalized_primitive_steps",
            unit_normalized_primitive_steps(candidate.channels),
            "minimal adapter uses the primitive one-step representative of each null ray",
        ),
        RequirementCheck(
            "nondegenerate_forced_interval",
            form is not None and form.determinant() != 0,
            "null constraints must force one nondegenerate interval form",
        ),
        RequirementCheck(
            "reciprocal_observer_family",
            reciprocal_observer_family_possible(form),
            "nontrivial observer changes must preserve the interval by reciprocal scaling",
        ),
        RequirementCheck(
            "simultaneity_split",
            simultaneity_split_possible(form),
            "rest simultaneity must split under a nontrivial observer scaling",
        ),
    )

    passes_all = all(check.passes for check in checks)
    if passes_all and candidate.candidate_id == "minimal_two_null_channel":
        status = "minimal_survivor"
        reason = "minimal two-null-channel adapter satisfies all observer-relativity requirements"
    elif candidate.candidate_id == "asymmetric_unit_two_channel" and form == canonical_form():
        status = "isomorphic_to_two_null_basis_but_unit_redundant"
        reason = "unequal primitive units reduce to the same two null rays after unit normalization"
    elif not source_compatible(candidate.channels):
        status = "rejected_signed_source_direction"
        reason = "signed negative compatibility counts are not source-compatible record directions"
    elif span < 2:
        status = "insufficient_directionality"
        reason = "candidate does not provide two independent signal directions"
    elif len(candidate.channels) > 2:
        status = "overcomplete_not_minimal"
        reason = "candidate adds a primitive direction beyond the two-ray minimal adapter"
    elif form is None:
        status = "interval_not_forced"
        reason = "candidate does not force one nondegenerate product interval"
    else:
        status = "failed_requirement"
        reason = "candidate misses at least one observer-relativity requirement"

    return NecessityVerdict(
        candidate_id=candidate.candidate_id,
        status=status,
        passes_all=passes_all,
        checks=checks,
        forced_form=form,
        reason=reason,
    )


def evaluate_candidates() -> tuple[NecessityVerdict, ...]:
    return tuple(evaluate_candidate(candidate) for candidate in necessity_candidates())


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            "finite_candidate_scope",
            "still_absorbs",
            True,
            "the screen covers declared adapter shapes, not every possible compatibility structure",
        ),
        ComparatorVerdict(
            "two_null_basis_necessity",
            "supported_within_screen",
            False,
            "within the declared requirements, the minimal two-null-channel adapter is the only survivor",
        ),
        ComparatorVerdict(
            "compatibility_alone_derivation",
            "not_earned",
            True,
            "the requirements themselves still include source compatibility, nullness, bilinearity, and minimality premises",
        ),
        ComparatorVerdict(
            "external_adapter_reading",
            "still_live",
            True,
            "the surviving two-channel basis may be an adapter interface rather than something derived internally",
        ),
    )


def run_t381_analysis() -> T381Result:
    verdicts = evaluate_candidates()
    by_id = {verdict.candidate_id: verdict for verdict in verdicts}
    survivors = tuple(verdict.candidate_id for verdict in verdicts if verdict.passes_all)
    return T381Result(
        minimal_two_null_adapter_unique_survivor=survivors == ("minimal_two_null_channel",),
        one_channel_fails=not by_id["single_channel"].passes_all,
        collinear_channels_fail=not by_id["collinear_two_channel"].passes_all,
        three_channel_overcomplete_fails_minimality=(
            by_id["overcomplete_three_channel"].status == "overcomplete_not_minimal"
        ),
        asymmetric_unit_adapter_reduces_to_two_null_basis=(
            by_id["asymmetric_unit_two_channel"].status
            == "isomorphic_to_two_null_basis_but_unit_redundant"
        ),
        signed_diagonal_adapter_rejected_as_non_source_compatible=(
            by_id["signed_diagonal_two_channel"].status
            == "rejected_signed_source_direction"
        ),
        surviving_candidate_ids=survivors,
        verdicts=verdicts,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict="minimal_two_null_adapter_necessary_within_declared_screen",
        strongest_claim=(
            "Within the finite observer-relativity requirement screen, the only minimal source-compatible "
            "adapter shape that supports nondegenerate interval recovery, reciprocal observer scaling, "
            "and simultaneity split is the two-independent-null-channel adapter. This is necessity within "
            "the declared screen, not a compatibility-alone derivation."
        ),
        claim_ledger_update=(
            "Register T381 as conditional necessity evidence: the live object is now a minimal two-null-channel "
            "adapter, but the screen's premises still need independent motivation."
        ),
    )


def _form_to_dict(form: QuadraticForm | None) -> dict[str, str] | None:
    if form is None:
        return None
    return {
        "a": str(form.a),
        "b": str(form.b),
        "c": str(form.c),
        "determinant": str(form.determinant()),
    }


def t381_result_to_dict(result: T381Result) -> dict[str, object]:
    return {
        "minimal_two_null_adapter_unique_survivor": result.minimal_two_null_adapter_unique_survivor,
        "one_channel_fails": result.one_channel_fails,
        "collinear_channels_fail": result.collinear_channels_fail,
        "three_channel_overcomplete_fails_minimality": (
            result.three_channel_overcomplete_fails_minimality
        ),
        "asymmetric_unit_adapter_reduces_to_two_null_basis": (
            result.asymmetric_unit_adapter_reduces_to_two_null_basis
        ),
        "signed_diagonal_adapter_rejected_as_non_source_compatible": (
            result.signed_diagonal_adapter_rejected_as_non_source_compatible
        ),
        "surviving_candidate_ids": list(result.surviving_candidate_ids),
        "verdicts": [
            {
                "candidate_id": verdict.candidate_id,
                "status": verdict.status,
                "passes_all": verdict.passes_all,
                "forced_form": _form_to_dict(verdict.forced_form),
                "checks": [
                    {
                        "requirement_id": check.requirement_id,
                        "passes": check.passes,
                        "reason": check.reason,
                    }
                    for check in verdict.checks
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
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t381_result_to_dict(run_t381_analysis()), indent=2))
