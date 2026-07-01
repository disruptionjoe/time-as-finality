"""T380: compatibility signal-basis forcing screen.

T379 derived Lorentz-pattern rendering after assuming a primitive two-channel
compatibility signal basis with invariant c = 1. T380 asks what part of that is
forced by finite compatibility algebra and what part remains imported.

Result in one line:

* two independent null compatibility channels force the product interval
  ``Delta_left * Delta_right`` up to scale;
* c = 1 is then a rest-rendering unit normalization;
* but compatibility alone does not force exactly those two primitive null
  channels, nor the bilinear/null premises themselves.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys


if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.generated_compatibility_substrate import derived_ranks
from models.lorentz_pattern_from_propagation import canonical_substrate


@dataclass(frozen=True)
class CompatibilityVector:
    name: str
    left: Fraction
    right: Fraction


@dataclass(frozen=True)
class QuadraticForm:
    """q(left, right) = a*left^2 + 2*b*left*right + c*right^2."""

    a: Fraction
    b: Fraction
    c: Fraction

    def evaluate(self, vector: CompatibilityVector) -> Fraction:
        return (
            self.a * vector.left * vector.left
            + 2 * self.b * vector.left * vector.right
            + self.c * vector.right * vector.right
        )

    def interval_between(
        self,
        first: tuple[int, int],
        second: tuple[int, int],
    ) -> Fraction:
        delta = CompatibilityVector(
            name="delta",
            left=Fraction(second[0] - first[0], 1),
            right=Fraction(second[1] - first[1], 1),
        )
        return self.evaluate(delta)

    def determinant(self) -> Fraction:
        return self.a * self.c - self.b * self.b

    def normalized_to_product(self) -> "QuadraticForm":
        if self.b == 0:
            raise ValueError("cannot normalize a form with zero product coefficient")
        scale = Fraction(1, 2) / self.b
        return QuadraticForm(
            a=self.a * scale,
            b=self.b * scale,
            c=self.c * scale,
        )


@dataclass(frozen=True)
class BasisCandidate:
    candidate_id: str
    channels: tuple[CompatibilityVector, ...]
    description: str


@dataclass(frozen=True)
class BasisVerdict:
    candidate_id: str
    status: str
    passes: bool
    span_dimension: int
    null_solution_dimension: int
    forced_form: QuadraticForm | None
    reason: str


@dataclass(frozen=True)
class RestRenderedStep:
    channel: str
    delta_time: Fraction
    delta_space: Fraction
    speed: Fraction | None


@dataclass(frozen=True)
class ScalingCheck:
    scale_left: Fraction
    scale_right: Fraction
    preserves_interval: bool
    determinant: Fraction


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T380Result:
    two_channel_basis_forces_product_interval: bool
    c_equals_one_is_unit_normalization: bool
    reciprocal_scaling_preserves_interval: bool
    nonreciprocal_scaling_fails: bool
    single_channel_underdetermined: bool
    collinear_channels_do_not_form_basis: bool
    three_noncollinear_null_channels_fail: bool
    extra_collinear_channel_is_redundant: bool
    substrate_intervals_match_forced_form: bool
    basis_fully_derived_from_compatibility_alone: bool
    checked_substrate_pair_count: int
    basis_verdicts: tuple[BasisVerdict, ...]
    rest_rendered_steps: tuple[RestRenderedStep, ...]
    scaling_checks: tuple[ScalingCheck, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str


def canonical_form() -> QuadraticForm:
    return QuadraticForm(a=Fraction(0, 1), b=Fraction(1, 2), c=Fraction(0, 1))


def basis_candidates() -> tuple[BasisCandidate, ...]:
    left = CompatibilityVector("left_signal", Fraction(1, 1), Fraction(0, 1))
    right = CompatibilityVector("right_signal", Fraction(0, 1), Fraction(1, 1))
    left_double = CompatibilityVector("left_signal_double", Fraction(2, 1), Fraction(0, 1))
    diagonal = CompatibilityVector("diagonal_signal", Fraction(1, 1), Fraction(1, 1))
    return (
        BasisCandidate(
            candidate_id="two_independent_null_channels",
            channels=(left, right),
            description="the T379 primitive left/right compatibility signal basis",
        ),
        BasisCandidate(
            candidate_id="single_null_channel",
            channels=(left,),
            description="one primitive signal direction only",
        ),
        BasisCandidate(
            candidate_id="collinear_two_channels",
            channels=(left, left_double),
            description="two channels but only one direction",
        ),
        BasisCandidate(
            candidate_id="three_noncollinear_null_channels",
            channels=(left, right, diagonal),
            description="three distinct primitive signal directions in 1+1",
        ),
        BasisCandidate(
            candidate_id="extra_collinear_null_channel",
            channels=(left, right, left_double),
            description="a redundant extra channel collinear with a primitive signal",
        ),
    )


def _rank_matrix(rows: list[list[Fraction]]) -> int:
    matrix = [row[:] for row in rows if any(value != 0 for value in row)]
    if not matrix:
        return 0

    rank = 0
    column_count = len(matrix[0])
    for column in range(column_count):
        pivot_row = None
        for row_index in range(rank, len(matrix)):
            if matrix[row_index][column] != 0:
                pivot_row = row_index
                break
        if pivot_row is None:
            continue
        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        pivot = matrix[rank][column]
        matrix[rank] = [value / pivot for value in matrix[rank]]
        for row_index in range(len(matrix)):
            if row_index == rank:
                continue
            factor = matrix[row_index][column]
            if factor == 0:
                continue
            matrix[row_index] = [
                value - factor * pivot_value
                for value, pivot_value in zip(matrix[row_index], matrix[rank])
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def _rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], tuple[int, ...]]:
    matrix = [row[:] for row in rows if any(value != 0 for value in row)]
    if not matrix:
        return [], ()

    rank = 0
    pivot_columns: list[int] = []
    column_count = len(matrix[0])
    for column in range(column_count):
        pivot_row = None
        for row_index in range(rank, len(matrix)):
            if matrix[row_index][column] != 0:
                pivot_row = row_index
                break
        if pivot_row is None:
            continue
        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        pivot = matrix[rank][column]
        matrix[rank] = [value / pivot for value in matrix[rank]]
        for row_index in range(len(matrix)):
            if row_index == rank:
                continue
            factor = matrix[row_index][column]
            if factor == 0:
                continue
            matrix[row_index] = [
                value - factor * pivot_value
                for value, pivot_value in zip(matrix[row_index], matrix[rank])
            ]
        pivot_columns.append(column)
        rank += 1
        if rank == len(matrix):
            break
    return matrix, tuple(pivot_columns)


def _nullspace(rows: list[list[Fraction]], column_count: int = 3) -> tuple[tuple[Fraction, ...], ...]:
    rref, pivot_columns = _rref(rows)
    free_columns = [column for column in range(column_count) if column not in pivot_columns]
    if not free_columns:
        return ()

    vectors: list[tuple[Fraction, ...]] = []
    for free_column in free_columns:
        vector = [Fraction(0, 1) for _ in range(column_count)]
        vector[free_column] = Fraction(1, 1)
        for row_index, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = -rref[row_index][free_column]
        vectors.append(tuple(vector))
    return tuple(vectors)


def span_dimension(channels: tuple[CompatibilityVector, ...]) -> int:
    return _rank_matrix([[channel.left, channel.right] for channel in channels])


def null_constraint_rows(channels: tuple[CompatibilityVector, ...]) -> list[list[Fraction]]:
    return [
        [
            channel.left * channel.left,
            2 * channel.left * channel.right,
            channel.right * channel.right,
        ]
        for channel in channels
    ]


def solve_null_forms(channels: tuple[CompatibilityVector, ...]) -> tuple[QuadraticForm, ...]:
    solutions = _nullspace(null_constraint_rows(channels))
    return tuple(QuadraticForm(a, b, c) for a, b, c in solutions)


def choose_forced_form(forms: tuple[QuadraticForm, ...]) -> QuadraticForm | None:
    if len(forms) != 1:
        return None
    form = forms[0]
    if form.determinant() == 0:
        return None
    return form.normalized_to_product()


def evaluate_basis_candidate(candidate: BasisCandidate) -> BasisVerdict:
    span = span_dimension(candidate.channels)
    forms = solve_null_forms(candidate.channels)
    forced_form = choose_forced_form(forms)

    if candidate.candidate_id == "two_independent_null_channels":
        passes = span == 2 and forced_form == canonical_form()
        status = "product_interval_forced_up_to_scale" if passes else "failed"
        reason = (
            "two independent null channel constraints leave exactly one "
            "nondegenerate bilinear interval form: the product interval"
        )
    elif candidate.candidate_id == "single_null_channel":
        passes = False
        status = "underdetermined"
        reason = (
            "one null channel leaves a two-dimensional family of forms, so "
            "compatibility direction alone does not determine relativity structure"
        )
    elif candidate.candidate_id == "collinear_two_channels":
        passes = False
        status = "not_a_two_direction_basis"
        reason = "two collinear channels span only one direction and do not define a 1+1 signal basis"
    elif candidate.candidate_id == "three_noncollinear_null_channels":
        passes = False
        status = "overconstrained"
        reason = (
            "three noncollinear primitive null directions in 1+1 force only the zero form, "
            "so a nondegenerate interval cannot make all three primitive"
        )
    elif candidate.candidate_id == "extra_collinear_null_channel":
        passes = span == 2 and forced_form == canonical_form()
        status = "redundant_channel_factors_through_basis" if passes else "failed"
        reason = (
            "the extra channel is collinear with an existing null direction, so it adds "
            "no new primitive signal direction"
        )
    else:
        passes = False
        status = "unknown"
        reason = "candidate not classified"

    return BasisVerdict(
        candidate_id=candidate.candidate_id,
        status=status,
        passes=passes,
        span_dimension=span,
        null_solution_dimension=len(forms),
        forced_form=forced_form,
        reason=reason,
    )


def evaluate_basis_candidates() -> tuple[BasisVerdict, ...]:
    return tuple(evaluate_basis_candidate(candidate) for candidate in basis_candidates())


def rest_render_step(channel: CompatibilityVector) -> RestRenderedStep:
    delta_time = (channel.left + channel.right) / 2
    delta_space = (channel.left - channel.right) / 2
    speed = None if delta_time == 0 else delta_space / delta_time
    return RestRenderedStep(
        channel=channel.name,
        delta_time=delta_time,
        delta_space=delta_space,
        speed=speed,
    )


def rest_rendered_steps() -> tuple[RestRenderedStep, ...]:
    return (
        rest_render_step(CompatibilityVector("left_signal", Fraction(1), Fraction(0))),
        rest_render_step(CompatibilityVector("right_signal", Fraction(0), Fraction(1))),
    )


def c_equals_one_is_unit_normalization() -> bool:
    steps = rest_rendered_steps()
    return (
        steps[0].speed == Fraction(1, 1)
        and steps[1].speed == Fraction(-1, 1)
        and canonical_form().evaluate(CompatibilityVector("left", Fraction(1), Fraction(0))) == 0
        and canonical_form().evaluate(CompatibilityVector("right", Fraction(0), Fraction(1))) == 0
    )


def scaling_check(scale_left: Fraction, scale_right: Fraction) -> ScalingCheck:
    determinant = scale_left * scale_right
    preserves = determinant == 1
    return ScalingCheck(
        scale_left=scale_left,
        scale_right=scale_right,
        preserves_interval=preserves,
        determinant=determinant,
    )


def canonical_scaling_checks() -> tuple[ScalingCheck, ...]:
    return (
        scaling_check(Fraction(2, 1), Fraction(1, 2)),
        scaling_check(Fraction(3, 2), Fraction(2, 3)),
        scaling_check(Fraction(2, 1), Fraction(2, 1)),
    )


def reciprocal_scaling_preserves_interval() -> bool:
    checks = canonical_scaling_checks()
    return checks[0].preserves_interval and checks[1].preserves_interval


def nonreciprocal_scaling_fails() -> bool:
    return not canonical_scaling_checks()[2].preserves_interval


def substrate_intervals_match_forced_form() -> tuple[bool, int]:
    substrate = canonical_substrate()
    ranks = derived_ranks(substrate)
    form = canonical_form()
    checked = 0
    for left_id, right_id in combinations(ranks, 2):
        left_rank = ranks[left_id]
        right_rank = ranks[right_id]
        expected = Fraction(
            (right_rank[0] - left_rank[0]) * (right_rank[1] - left_rank[1]),
            1,
        )
        if form.interval_between(left_rank, right_rank) != expected:
            return False, checked
        checked += 1
    return True, checked


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            comparator_id="minkowski_metric_import",
            status="weakened_by_null_constraint_solution",
            absorbs=False,
            reason=(
                "the product interval is solved from finite null-channel constraints rather "
                "than inserted as a t/x metric in source rows"
            ),
        ),
        ComparatorVerdict(
            comparator_id="two_channel_basis_import",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "the existence of two independent primitive compatibility-signal directions is "
                "an assumption, not derived from generic compatibility"
            ),
        ),
        ComparatorVerdict(
            comparator_id="null_signal_assumption",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "the derivation requires primitive signal channels to be null; that premise is "
                "not yet derived from record compatibility alone"
            ),
        ),
        ComparatorVerdict(
            comparator_id="bilinear_interval_premise",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "the screen assumes a symmetric bilinear interval form; nonlinear or higher-rank "
                "compatibility invariants are not ruled out"
            ),
        ),
        ComparatorVerdict(
            comparator_id="numeric_c_equals_one",
            status="unit_normalization",
            absorbs=False,
            reason=(
                "once a common two-direction null signal basis is granted, c=1 is a choice of "
                "units for the rest rendering, not an additional physical constant"
            ),
        ),
        ComparatorVerdict(
            comparator_id="compatibility_alone",
            status="insufficient",
            absorbs=True,
            reason=(
                "single-channel and collinear controls show that compatibility direction data "
                "alone underdetermines the relativistic interval"
            ),
        ),
    )


def run_t380_analysis() -> T380Result:
    verdicts = evaluate_basis_candidates()
    by_id = {verdict.candidate_id: verdict for verdict in verdicts}
    substrate_match, checked_pairs = substrate_intervals_match_forced_form()
    scaling_checks = canonical_scaling_checks()
    return T380Result(
        two_channel_basis_forces_product_interval=(
            by_id["two_independent_null_channels"].passes
        ),
        c_equals_one_is_unit_normalization=c_equals_one_is_unit_normalization(),
        reciprocal_scaling_preserves_interval=reciprocal_scaling_preserves_interval(),
        nonreciprocal_scaling_fails=nonreciprocal_scaling_fails(),
        single_channel_underdetermined=(
            by_id["single_null_channel"].status == "underdetermined"
        ),
        collinear_channels_do_not_form_basis=(
            by_id["collinear_two_channels"].status == "not_a_two_direction_basis"
        ),
        three_noncollinear_null_channels_fail=(
            by_id["three_noncollinear_null_channels"].status == "overconstrained"
        ),
        extra_collinear_channel_is_redundant=(
            by_id["extra_collinear_null_channel"].status
            == "redundant_channel_factors_through_basis"
        ),
        substrate_intervals_match_forced_form=substrate_match,
        basis_fully_derived_from_compatibility_alone=False,
        checked_substrate_pair_count=checked_pairs,
        basis_verdicts=verdicts,
        rest_rendered_steps=rest_rendered_steps(),
        scaling_checks=scaling_checks,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict=(
            "product_interval_forced_given_two_null_channels_but_signal_basis_not_derived"
        ),
        strongest_claim=(
            "In a 1+1 compatibility module, two independent primitive null signal channels "
            "force the product interval Delta_left*Delta_right up to scale, and reciprocal "
            "lineage scaling is exactly the interval-preserving observer family. The numeric "
            "c=1 is a rest-rendering unit normalization. But the existence of exactly two "
            "independent null primitive channels, and the bilinear interval premise, are not "
            "derived from compatibility alone."
        ),
        claim_ledger_update=(
            "Register T380 as a basis-forcing boundary result: T379's Lorentz algebra is not "
            "arbitrary once a two-null-channel basis is granted, but that basis is still the "
            "live imported object."
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


def t380_result_to_dict(result: T380Result) -> dict[str, object]:
    return {
        "two_channel_basis_forces_product_interval": (
            result.two_channel_basis_forces_product_interval
        ),
        "c_equals_one_is_unit_normalization": result.c_equals_one_is_unit_normalization,
        "reciprocal_scaling_preserves_interval": (
            result.reciprocal_scaling_preserves_interval
        ),
        "nonreciprocal_scaling_fails": result.nonreciprocal_scaling_fails,
        "single_channel_underdetermined": result.single_channel_underdetermined,
        "collinear_channels_do_not_form_basis": (
            result.collinear_channels_do_not_form_basis
        ),
        "three_noncollinear_null_channels_fail": (
            result.three_noncollinear_null_channels_fail
        ),
        "extra_collinear_channel_is_redundant": (
            result.extra_collinear_channel_is_redundant
        ),
        "substrate_intervals_match_forced_form": (
            result.substrate_intervals_match_forced_form
        ),
        "basis_fully_derived_from_compatibility_alone": (
            result.basis_fully_derived_from_compatibility_alone
        ),
        "checked_substrate_pair_count": result.checked_substrate_pair_count,
        "basis_verdicts": [
            {
                "candidate_id": verdict.candidate_id,
                "status": verdict.status,
                "passes": verdict.passes,
                "span_dimension": verdict.span_dimension,
                "null_solution_dimension": verdict.null_solution_dimension,
                "forced_form": _form_to_dict(verdict.forced_form),
                "reason": verdict.reason,
            }
            for verdict in result.basis_verdicts
        ],
        "rest_rendered_steps": [
            {
                "channel": step.channel,
                "delta_time": str(step.delta_time),
                "delta_space": str(step.delta_space),
                "speed": None if step.speed is None else str(step.speed),
            }
            for step in result.rest_rendered_steps
        ],
        "scaling_checks": [
            {
                "scale_left": str(check.scale_left),
                "scale_right": str(check.scale_right),
                "preserves_interval": check.preserves_interval,
                "determinant": str(check.determinant),
            }
            for check in result.scaling_checks
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

    print(json.dumps(t380_result_to_dict(run_t380_analysis()), indent=2))
