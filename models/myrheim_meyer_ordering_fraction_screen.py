"""T156: Myrheim-Meyer ordering-fraction screen for T126 survivors.

T126 can say that a finite finality colimit survived selected causal-set
necessary-condition filters. T156 adds a narrower named diagnostic: for a
declared 1+1 flat-interval comparison target, does the candidate's ordering
fraction sit near the Myrheim-Meyer ordering-fraction value 1/2?

This is not a dimension estimator, embedding theorem, or continuum result. It
is a guardrail against treating a T126 `passes_filter_only` verdict as even
weak evidence for a 1+1 Lorentzian causal-set approximation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    CausetAudit,
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    grid_filter_pass_control,
    non_strict_relation,
)


@dataclass(frozen=True)
class OrderingFractionTarget:
    name: str
    target_fraction: Fraction
    tolerance: Fraction
    basis: str

    def accepts(self, value: Fraction) -> bool:
        return abs(value - self.target_fraction) <= self.tolerance


@dataclass(frozen=True)
class T156Audit:
    name: str
    source: str
    t126_classification: str
    causal_set_candidate: bool
    t126_filter_passed: bool
    event_count: int
    strict_pair_count: int | None
    ordering_fraction: Fraction | None
    target_name: str
    target_fraction: Fraction
    tolerance: Fraction
    absolute_gap: Fraction | None
    target_verdict: str
    verdict: str
    reason: str
    required_next: str


@dataclass(frozen=True)
class T156Result:
    target: OrderingFractionTarget
    audits: tuple[T156Audit, ...]
    positive_target_control_passes: bool
    t126_pass_can_fail_ordering_fraction_target: bool
    all_product_grid_survivors_fail_target: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


NOT_CLAIMED = (
    "T156 does not estimate continuum dimension, prove faithful embedding, "
    "derive a Lorentzian metric, or validate spacetime reconstruction."
)


def flat_1p1_interval_target() -> OrderingFractionTarget:
    return OrderingFractionTarget(
        name="flat_1p1_interval_ordering_fraction",
        target_fraction=Fraction(1, 2),
        tolerance=Fraction(1, 10),
        basis=(
            "In light-cone coordinates on a flat 1+1 causal diamond, two "
            "independent points are causally related exactly when their two "
            "coordinate orderings agree, giving ordering fraction 1/2. The "
            "1/10 tolerance is a finite-audit band, not a continuum theorem."
        ),
    )


def deterministic_flat_interval_control() -> FinalityColimitCausetDatum:
    """A six-event light-cone coordinate control near the 1+1 target."""

    coordinates = {
        "p0": (Fraction(134, 1000), Fraction(847, 1000)),
        "p1": (Fraction(764, 1000), Fraction(255, 1000)),
        "p2": (Fraction(495, 1000), Fraction(449, 1000)),
        "p3": (Fraction(652, 1000), Fraction(789, 1000)),
        "p4": (Fraction(94, 1000), Fraction(28, 1000)),
        "p5": (Fraction(836, 1000), Fraction(433, 1000)),
    }
    events = frozenset(coordinates)
    strict = frozenset(
        (left, right)
        for left, left_uv in coordinates.items()
        for right, right_uv in coordinates.items()
        if left != right and left_uv[0] < right_uv[0] and left_uv[1] < right_uv[1]
    )
    return FinalityColimitCausetDatum(
        name="flat_1p1_target_control",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="deterministic light-cone coordinate control, not a TaF derivation",
    )


def product_grid_colimit_control(rows: int, cols: int) -> FinalityColimitCausetDatum:
    """Build a small product-order finality-colimit control."""

    if rows < 2 or cols < 2:
        raise ValueError("product grid controls require at least two rows and columns")
    events = frozenset(f"p{i}_{j}" for i in range(rows) for j in range(cols))
    strict = frozenset(
        (f"p{i}_{j}", f"p{k}_{l}")
        for i in range(rows)
        for j in range(cols)
        for k in range(rows)
        for l in range(cols)
        if (i, j) != (k, l) and i <= k and j <= l
    )
    return FinalityColimitCausetDatum(
        name=f"t54_style_product_grid_{rows}x{cols}",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source=(
            "synthetic T54-style canonical product-order finality colimit; "
            "not an actual T54 quotient-union output"
        ),
    )


def canonical_t156_datums() -> tuple[FinalityColimitCausetDatum, ...]:
    return (
        deterministic_flat_interval_control(),
        product_grid_colimit_control(2, 3),
        grid_filter_pass_control(),
    )


def audit_ordering_fraction_target(
    datum: FinalityColimitCausetDatum,
    *,
    target: OrderingFractionTarget,
) -> T156Audit:
    t126_audit = audit_finality_colimit_causet(datum)
    diagnostics = t126_audit.diagnostics
    if diagnostics is None:
        ordering_fraction = None
        strict_pair_count = None
        absolute_gap = None
    else:
        ordering_fraction = diagnostics.comparable_fraction
        strict_pair_count = diagnostics.strict_pair_count
        absolute_gap = abs(ordering_fraction - target.target_fraction)

    if not t126_audit.causal_set_candidate or not t126_audit.manifold_filter_passed:
        target_verdict = "not_reached_t126_blocked"
        verdict = "blocked_before_ordering_fraction_target"
        reason = (
            "The candidate did not clear the T126 causal-set filter, so the "
            "ordering-fraction target should not be interpreted."
        )
        required_next = t126_audit.required_next
    elif ordering_fraction is not None and target.accepts(ordering_fraction):
        target_verdict = "inside_declared_ordering_fraction_band"
        verdict = "passes_ordering_fraction_control_only"
        reason = (
            "The candidate's ordering fraction lies inside the declared finite "
            "1+1 target band. This is only a calibration/control pass."
        )
        required_next = (
            "Apply stronger dimension, abundance, sprinkling, locality, and "
            "continuum diagnostics before any spacetime-facing claim."
        )
    else:
        target_verdict = "outside_declared_ordering_fraction_band"
        verdict = "t126_pass_but_ordering_fraction_fail"
        reason = (
            "The candidate survived T126's selected finite filter but is too "
            "highly ordered relative to the declared 1+1 flat-interval "
            "ordering-fraction target."
        )
        required_next = (
            "Do not treat this T126 survivor as dimension evidence; either "
            "change the declared comparison target or build a less lattice-"
            "ordered finality colimit."
        )

    return _audit_from_t126(
        datum=datum,
        t126_audit=t126_audit,
        strict_pair_count=strict_pair_count,
        ordering_fraction=ordering_fraction,
        target=target,
        absolute_gap=absolute_gap,
        target_verdict=target_verdict,
        verdict=verdict,
        reason=reason,
        required_next=required_next,
    )


def run_t156_analysis() -> T156Result:
    target = flat_1p1_interval_target()
    audits = tuple(
        audit_ordering_fraction_target(datum, target=target)
        for datum in canonical_t156_datums()
    )
    by_name = {audit.name: audit for audit in audits}
    grid_audits = tuple(
        audit
        for audit in audits
        if audit.name.startswith("t54_style_product_grid")
        or audit.name == "grid_filter_pass_control"
    )

    positive_target_control_passes = (
        by_name["flat_1p1_target_control"].verdict
        == "passes_ordering_fraction_control_only"
    )
    grid_failures = all(
        audit.t126_filter_passed
        and audit.verdict == "t126_pass_but_ordering_fraction_fail"
        for audit in grid_audits
    )
    t126_pass_can_fail = any(
        audit.t126_filter_passed
        and audit.verdict == "t126_pass_but_ordering_fraction_fail"
        for audit in audits
    )

    return T156Result(
        target=target,
        audits=audits,
        positive_target_control_passes=positive_target_control_passes,
        t126_pass_can_fail_ordering_fraction_target=t126_pass_can_fail,
        all_product_grid_survivors_fail_target=grid_failures,
        strongest_claim=(
            "A T126 `passes_filter_only` result is not even a 1+1 "
            "Myrheim-Meyer ordering-fraction pass. The 2x3 and 3x3 product-"
            "order finality-colimit controls clear T126 but fail the declared "
            "flat 1+1 ordering-fraction band."
        ),
        improved=(
            "T156 connects the finite finality-colimit bridge to a named "
            "causal-set diagnostic and supplies a deterministic positive "
            "target control, making the S1 scale-up path more reviewable."
        ),
        weakened=(
            "This weakens the current S1 positive boundary: T126 survivors "
            "can be too lattice-ordered to resemble the declared 1+1 flat "
            "causal interval, so T126 passing is only a pre-diagnostic filter."
        ),
        falsification_condition=(
            "T156 fails if the ordering-fraction calculation is not computed "
            "from the same strict relation used by T126, if the deterministic "
            "target control is rejected by the declared band, or if product "
            "grid survivors are promoted as 1+1 dimension evidence despite "
            "falling outside that band."
        ),
        s1_update=(
            "S1 remains open_formal_target. A future spacetime-colimit witness "
            "must clear T126 and then match a declared causal-set diagnostic; "
            "T126 alone is insufficient."
        ),
        claim_ledger_update=(
            "Add T156 to S1: scale-cleared T126 product-grid survivors can fail "
            "a declared Myrheim-Meyer 1+1 ordering-fraction target. This turns "
            "the T126 pass into a stricter pre-diagnostic gate rather than "
            "dimension or manifoldlikeness evidence."
        ),
        open_blocker=(
            "No actual T54/T58 finality colimit both reaches T126 scale and "
            "matches a named causal-set dimension, sprinkling, locality, or "
            "continuum diagnostic."
        ),
        suggested_next=(
            "Generate a genuine T54 quotient-union family with at least six "
            "events whose ordering fraction falls inside the declared target "
            "band, then test whether stronger interval and locality diagnostics "
            "still reject it."
        ),
    )


def t156_result_to_dict(result: T156Result) -> dict[str, Any]:
    return {
        "target": {
            "name": result.target.name,
            "target_fraction": _fraction_to_dict(result.target.target_fraction),
            "tolerance": _fraction_to_dict(result.target.tolerance),
            "basis": result.target.basis,
        },
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "positive_target_control_passes": result.positive_target_control_passes,
        "t126_pass_can_fail_ordering_fraction_target": (
            result.t126_pass_can_fail_ordering_fraction_target
        ),
        "all_product_grid_survivors_fail_target": (
            result.all_product_grid_survivors_fail_target
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": NOT_CLAIMED,
    }


def _audit_from_t126(
    *,
    datum: FinalityColimitCausetDatum,
    t126_audit: CausetAudit,
    strict_pair_count: int | None,
    ordering_fraction: Fraction | None,
    target: OrderingFractionTarget,
    absolute_gap: Fraction | None,
    target_verdict: str,
    verdict: str,
    reason: str,
    required_next: str,
) -> T156Audit:
    diagnostics = t126_audit.diagnostics
    return T156Audit(
        name=t126_audit.name,
        source=datum.source,
        t126_classification=t126_audit.classification,
        causal_set_candidate=t126_audit.causal_set_candidate,
        t126_filter_passed=t126_audit.manifold_filter_passed,
        event_count=diagnostics.event_count if diagnostics is not None else len(datum.events),
        strict_pair_count=strict_pair_count,
        ordering_fraction=ordering_fraction,
        target_name=target.name,
        target_fraction=target.target_fraction,
        tolerance=target.tolerance,
        absolute_gap=absolute_gap,
        target_verdict=target_verdict,
        verdict=verdict,
        reason=reason,
        required_next=required_next,
    )


def _audit_to_dict(audit: T156Audit) -> dict[str, Any]:
    return {
        "name": audit.name,
        "source": audit.source,
        "t126_classification": audit.t126_classification,
        "causal_set_candidate": audit.causal_set_candidate,
        "t126_filter_passed": audit.t126_filter_passed,
        "event_count": audit.event_count,
        "strict_pair_count": audit.strict_pair_count,
        "ordering_fraction": (
            _fraction_to_dict(audit.ordering_fraction)
            if audit.ordering_fraction is not None
            else None
        ),
        "target_name": audit.target_name,
        "target_fraction": _fraction_to_dict(audit.target_fraction),
        "tolerance": _fraction_to_dict(audit.tolerance),
        "absolute_gap": (
            _fraction_to_dict(audit.absolute_gap)
            if audit.absolute_gap is not None
            else None
        ),
        "target_verdict": audit.target_verdict,
        "verdict": audit.verdict,
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t156_result_to_dict(run_t156_analysis()), indent=2))
