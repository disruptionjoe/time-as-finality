"""T383: falsification suite for the relativity adapter pattern.

T382 identified the two-null-channel adapter as the clean external interface
candidate. T383 tries to break it by perturbing the assumptions that T379/T380
needed: invariant signal speed, reciprocal scaling, channel completeness,
minimality, and exact access.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.generated_compatibility_substrate import derived_ranks, landmark_ids
from models.lorentz_pattern_from_propagation import (
    canonical_substrate,
)


@dataclass(frozen=True)
class Perturbation:
    perturbation_id: str
    left_scale: Fraction
    right_scale: Fraction
    left_time_delay: Fraction = Fraction(0)
    right_time_delay: Fraction = Fraction(0)
    missing_right_channel: bool = False
    extra_primitive_channel: bool = False
    deterministic_noise: bool = False
    coarse_grained_access: bool = False
    description: str = ""


@dataclass(frozen=True)
class PerturbationVerdict:
    perturbation_id: str
    status: str
    classification: str
    interval_preserved: bool
    signal_speed_invariant: bool
    two_channel_complete: bool
    minimal_basis: bool
    exact_access: bool
    reason: str


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T383Result:
    baseline_survives: bool
    anisotropic_speed_falsifies: bool
    nonreciprocal_scaling_falsifies: bool
    delayed_channel_falsifies: bool
    noisy_channel_falsifies_exact_invariance: bool
    missing_channel_falsifies: bool
    extra_primitive_channel_falsifies_minimality: bool
    coarse_graining_is_partial: bool
    survivor_ids: tuple[str, ...]
    partial_ids: tuple[str, ...]
    falsifier_ids: tuple[str, ...]
    verdicts: tuple[PerturbationVerdict, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str


def perturbations() -> tuple[Perturbation, ...]:
    return (
        Perturbation(
            "baseline_two_null",
            left_scale=Fraction(2),
            right_scale=Fraction(1, 2),
            description="reciprocal two-null-channel adapter",
        ),
        Perturbation(
            "anisotropic_signal_speed",
            left_scale=Fraction(2),
            right_scale=Fraction(1, 3),
            description="left/right signal units are not reciprocal",
        ),
        Perturbation(
            "nonreciprocal_scaling",
            left_scale=Fraction(2),
            right_scale=Fraction(2),
            description="observer rescales both channels in same direction",
        ),
        Perturbation(
            "delayed_left_channel",
            left_scale=Fraction(2),
            right_scale=Fraction(1, 2),
            left_time_delay=Fraction(1, 3),
            description="left signal has per-step delay",
        ),
        Perturbation(
            "deterministic_noise",
            left_scale=Fraction(2),
            right_scale=Fraction(1, 2),
            deterministic_noise=True,
            description="records receive parity-dependent time jitter",
        ),
        Perturbation(
            "missing_right_channel",
            left_scale=Fraction(2),
            right_scale=Fraction(0),
            missing_right_channel=True,
            description="adapter exposes only one signal direction",
        ),
        Perturbation(
            "extra_primitive_channel",
            left_scale=Fraction(2),
            right_scale=Fraction(1, 2),
            extra_primitive_channel=True,
            description="adapter adds a third primitive noncollinear signal direction",
        ),
        Perturbation(
            "coarse_grained_access",
            left_scale=Fraction(2),
            right_scale=Fraction(1, 2),
            coarse_grained_access=True,
            description="adapter preserves invariant only on a sampled coarse subset",
        ),
    )


def rendered_coordinates(
    left: int,
    right: int,
    perturbation: Perturbation,
) -> tuple[Fraction, Fraction] | None:
    if perturbation.missing_right_channel:
        return None
    scaled_left = perturbation.left_scale * left
    scaled_right = perturbation.right_scale * right
    signal_time = (
        (scaled_left + scaled_right) / 2
        + perturbation.left_time_delay * left
        + perturbation.right_time_delay * right
    )
    signal_space = (scaled_left - scaled_right) / 2
    if perturbation.deterministic_noise:
        signal_time += Fraction((left + 2 * right) % 3, 5)
    return signal_time, signal_space


def interval_for_pair(
    first: tuple[int, int],
    second: tuple[int, int],
    perturbation: Perturbation,
) -> Fraction | None:
    first_rendered = rendered_coordinates(first[0], first[1], perturbation)
    second_rendered = rendered_coordinates(second[0], second[1], perturbation)
    if first_rendered is None or second_rendered is None:
        return None
    delta_time = second_rendered[0] - first_rendered[0]
    delta_space = second_rendered[1] - first_rendered[1]
    return delta_time * delta_time - delta_space * delta_space


def expected_interval(first: tuple[int, int], second: tuple[int, int]) -> Fraction:
    return Fraction((second[0] - first[0]) * (second[1] - first[1]), 1)


def check_interval_preservation(perturbation: Perturbation) -> bool:
    if perturbation.coarse_grained_access:
        pairs = [((0, 0), (2, 2)), ((1, 1), (3, 3)), ((2, 0), (0, 2))]
    else:
        substrate = canonical_substrate()
        ranks = derived_ranks(substrate)
        landmarks = landmark_ids(substrate)
        ids = [landmarks[label] for label in ("origin", "near", "left_only", "right_only", "future", "far")]
        pairs = [(ranks[left], ranks[right]) for index, left in enumerate(ids) for right in ids[index + 1 :]]
    for first, second in pairs:
        interval = interval_for_pair(first, second, perturbation)
        if interval != expected_interval(first, second):
            return False
    return True


def signal_speed_invariant(perturbation: Perturbation) -> bool:
    if perturbation.missing_right_channel or perturbation.right_scale == 0:
        return False
    if perturbation.left_scale * perturbation.right_scale != 1:
        return False
    left_dt = perturbation.left_scale / 2 + perturbation.left_time_delay
    left_dx = perturbation.left_scale / 2
    right_dt = perturbation.right_scale / 2 + perturbation.right_time_delay
    right_dx = -perturbation.right_scale / 2
    if left_dt == 0 or right_dt == 0:
        return False
    return left_dx / left_dt == 1 and right_dx / right_dt == -1


def exact_access(perturbation: Perturbation) -> bool:
    return not perturbation.deterministic_noise and not perturbation.coarse_grained_access


def evaluate_perturbation(perturbation: Perturbation) -> PerturbationVerdict:
    interval_ok = check_interval_preservation(perturbation)
    speed_ok = signal_speed_invariant(perturbation)
    complete = not perturbation.missing_right_channel
    minimal = not perturbation.extra_primitive_channel
    access_ok = exact_access(perturbation)
    if all((interval_ok, speed_ok, complete, minimal, access_ok)):
        status = "survives"
        classification = "survivor"
        reason = "baseline reciprocal two-null-channel adapter preserves all checked requirements"
    elif perturbation.coarse_grained_access and interval_ok and speed_ok and complete and minimal:
        status = "partial_subset_only"
        classification = "partial"
        reason = "coarse-grained access preserves the sampled subset but is not exact full-substrate access"
    elif not complete:
        status = "falsifies_channel_completeness"
        classification = "falsifier"
        reason = "missing one primitive direction destroys two-sided observer relativity"
    elif not minimal:
        status = "falsifies_minimality"
        classification = "falsifier"
        reason = "extra primitive direction violates the minimal two-null-channel interface"
    elif not speed_ok:
        status = "falsifies_signal_speed"
        classification = "falsifier"
        reason = "primitive signal speed is no longer invariant"
    elif not interval_ok:
        status = "falsifies_interval"
        classification = "falsifier"
        reason = "rendered intervals no longer match the substrate product interval"
    elif not access_ok:
        status = "falsifies_exact_access"
        classification = "falsifier"
        reason = "deterministic noise breaks exact record-level invariance"
    else:
        status = "failed"
        classification = "falsifier"
        reason = "perturbation misses a declared requirement"
    return PerturbationVerdict(
        perturbation_id=perturbation.perturbation_id,
        status=status,
        classification=classification,
        interval_preserved=interval_ok,
        signal_speed_invariant=speed_ok,
        two_channel_complete=complete,
        minimal_basis=minimal,
        exact_access=access_ok,
        reason=reason,
    )


def evaluate_perturbations() -> tuple[PerturbationVerdict, ...]:
    return tuple(evaluate_perturbation(perturbation) for perturbation in perturbations())


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            "robustness",
            "fragile_but_informative",
            False,
            "the pattern breaks under targeted violations, which clarifies the necessary assumptions",
        ),
        ComparatorVerdict(
            "finite_perturbation_catalog",
            "still_absorbs",
            True,
            "the suite tests declared perturbations, not all possible deformations",
        ),
        ComparatorVerdict(
            "exact_invariance_requirement",
            "strict",
            False,
            "noise and coarse access are intentionally demoted under exact record-level invariance",
        ),
    )


def run_t383_analysis() -> T383Result:
    verdicts = evaluate_perturbations()
    by_id = {verdict.perturbation_id: verdict for verdict in verdicts}
    survivors = tuple(verdict.perturbation_id for verdict in verdicts if verdict.classification == "survivor")
    partials = tuple(verdict.perturbation_id for verdict in verdicts if verdict.classification == "partial")
    falsifiers = tuple(verdict.perturbation_id for verdict in verdicts if verdict.classification == "falsifier")
    return T383Result(
        baseline_survives=by_id["baseline_two_null"].classification == "survivor",
        anisotropic_speed_falsifies=by_id["anisotropic_signal_speed"].status
        == "falsifies_signal_speed",
        nonreciprocal_scaling_falsifies=by_id["nonreciprocal_scaling"].status
        == "falsifies_signal_speed",
        delayed_channel_falsifies=by_id["delayed_left_channel"].status
        == "falsifies_signal_speed",
        noisy_channel_falsifies_exact_invariance=(
            by_id["deterministic_noise"].classification == "falsifier"
        ),
        missing_channel_falsifies=by_id["missing_right_channel"].status
        == "falsifies_channel_completeness",
        extra_primitive_channel_falsifies_minimality=(
            by_id["extra_primitive_channel"].status == "falsifies_minimality"
        ),
        coarse_graining_is_partial=by_id["coarse_grained_access"].status
        == "partial_subset_only",
        survivor_ids=survivors,
        partial_ids=partials,
        falsifier_ids=falsifiers,
        verdicts=verdicts,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict="two_null_pattern_survives_baseline_and_fails_targeted_perturbations",
        strongest_claim=(
            "The two-null-channel relativity pattern is robust only when invariant signal speed, "
            "reciprocal scaling, channel completeness, minimality, and exact access are preserved. "
            "Targeted perturbations break the pattern in specific, interpretable ways."
        ),
        claim_ledger_update=(
            "Register T383 as falsification evidence: the clean adapter is not arbitrary, but it is "
            "premise-sensitive; the next synthesis should state the exact premise bundle."
        ),
    )


def t383_result_to_dict(result: T383Result) -> dict[str, object]:
    return {
        "baseline_survives": result.baseline_survives,
        "anisotropic_speed_falsifies": result.anisotropic_speed_falsifies,
        "nonreciprocal_scaling_falsifies": result.nonreciprocal_scaling_falsifies,
        "delayed_channel_falsifies": result.delayed_channel_falsifies,
        "noisy_channel_falsifies_exact_invariance": (
            result.noisy_channel_falsifies_exact_invariance
        ),
        "missing_channel_falsifies": result.missing_channel_falsifies,
        "extra_primitive_channel_falsifies_minimality": (
            result.extra_primitive_channel_falsifies_minimality
        ),
        "coarse_graining_is_partial": result.coarse_graining_is_partial,
        "survivor_ids": list(result.survivor_ids),
        "partial_ids": list(result.partial_ids),
        "falsifier_ids": list(result.falsifier_ids),
        "verdicts": [
            {
                "perturbation_id": verdict.perturbation_id,
                "status": verdict.status,
                "classification": verdict.classification,
                "interval_preserved": verdict.interval_preserved,
                "signal_speed_invariant": verdict.signal_speed_invariant,
                "two_channel_complete": verdict.two_channel_complete,
                "minimal_basis": verdict.minimal_basis,
                "exact_access": verdict.exact_access,
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

    print(json.dumps(t383_result_to_dict(run_t383_analysis()), indent=2))
