"""T250: apply the T156 ordering-fraction screen to T249.

T249 built a nine-event T54-native grid colimit that clears the T126 finite
filter. T250 asks the next named diagnostic question: does that same witness
also match the declared flat 1+1 Myrheim-Meyer ordering-fraction band?

The answer is negative. The T249 grid has ordering fraction 3/4, outside the
declared 1/2 +/- 1/10 band. This is a demotion of the T249 positive boundary,
not a new spacetime claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    FinalityColimitCausetDatum,
    non_strict_relation,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    T156Audit,
    audit_ordering_fraction_target,
    flat_1p1_interval_target,
)
from models.t249_larger_t54_t126_colimit import run_t249_analysis


@dataclass(frozen=True)
class T250Result:
    t249_t54_classification: str
    t249_t54_theorem_applies: bool
    t249_t126_classification: str
    t249_t126_filter_passed: bool
    t156_audit: T156Audit
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


NOT_CLAIMED = (
    "T250 does not estimate dimension, prove a faithful embedding, validate "
    "sprinkling behavior, derive a metric, or support a continuum claim."
)


def run_t250_analysis() -> T250Result:
    t249 = run_t249_analysis()
    target = flat_1p1_interval_target()
    t156_audit = audit_ordering_fraction_target(
        _t249_to_t156_datum(),
        target=target,
    )
    verdict = (
        "t249_t126_pass_but_ordering_fraction_fail"
        if t249.t126_audit.manifold_filter_passed
        and t156_audit.verdict == "t126_pass_but_ordering_fraction_fail"
        else "unexpected_t249_ordering_fraction_status"
    )

    return T250Result(
        t249_t54_classification=t249.completion.classification,
        t249_t54_theorem_applies=t249.completion.theorem_applies,
        t249_t126_classification=t249.t126_audit.classification,
        t249_t126_filter_passed=t249.t126_audit.manifold_filter_passed,
        t156_audit=t156_audit,
        verdict=verdict,
        strongest_claim=(
            "The T249 nine-event T54-native grid colimit clears T126 but fails "
            "the declared flat 1+1 Myrheim-Meyer ordering-fraction band: its "
            "ordering fraction is 3/4, not within 1/2 +/- 1/10."
        ),
        improved=(
            "T250 removes ambiguity from the T249 next step by applying the "
            "existing named T156 diagnostic to the actual T249 T54-native "
            "witness, not to a synthetic product-grid control."
        ),
        weakened_or_falsified=(
            "This weakens the positive reading of T249. The larger canonical "
            "grid is a useful T54/T126 bridge control, but it is too ordered "
            "for the declared flat 1+1 ordering-fraction target."
        ),
        falsification_condition=(
            "T250 fails if the relation sent to T156 is not the same T249 "
            "quotient-union relation audited by T126, if the target band is "
            "changed after seeing the result, or if a failed ordering-fraction "
            "screen is described as spacetime evidence."
        ),
        s1_update=(
            "S1 remains open_formal_target. T249 now has a named-diagnostic "
            "demotion: T126 passing alone is not enough."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T250 alone. Safe future "
            "wording: the T249 T54-native grid passes T126 but fails the "
            "declared T156 flat 1+1 ordering-fraction band."
        ),
        open_blocker=(
            "No T54-native nine-event witness currently both clears T126 and "
            "matches the declared flat 1+1 ordering-fraction target."
        ),
        suggested_next=(
            "Search for a T54-native scale-cleared witness with ordering "
            "fraction inside the declared band, then apply deletion, interval, "
            "locality, and sprinkling screens before any S1 upgrade."
        ),
        not_claimed=NOT_CLAIMED,
    )


def _t249_to_t156_datum() -> FinalityColimitCausetDatum:
    t249 = run_t249_analysis()
    completion = t249.completion
    events = frozenset(event.name for event in completion.global_events)
    strict = frozenset(
        (left, right)
        for left, right in completion.partial_order.order_pairs
        if left != right
    )
    return FinalityColimitCausetDatum(
        name="t250_t249_larger_grid_t54_colimit",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=completion.theorem_applies,
        canonical_colimit=completion.classification == "canonical",
        phantom_gap_resolved=all(
            summary.local_is_suborder and summary.gap_count == 0
            for summary in t249.local_gap_summaries
        ),
        observer_only_gap_changes_strict_order=False,
        source="T250 reuse of the T249 T54-native 3x3 grid colimit",
    )


def t250_result_to_dict(result: T250Result) -> dict[str, Any]:
    return {
        "t249_t54_classification": result.t249_t54_classification,
        "t249_t54_theorem_applies": result.t249_t54_theorem_applies,
        "t249_t126_classification": result.t249_t126_classification,
        "t249_t126_filter_passed": result.t249_t126_filter_passed,
        "t156_audit": _audit_to_dict(result.t156_audit),
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
