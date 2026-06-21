"""T154: bridge T54/T58 finite colimits into the T126 causet screen.

This module connects existing finite-finality artifacts instead of creating
another synthetic spacetime fixture. It adapts T54 canonical quotient-union
completions into T126 causal-set candidate data, but only after T58 confirms
that the apparent/event gap is a well-formed phantom-gap extension case.

The expected result is allowed to be negative: if the actual T51/T52-derived
colimits are too small for manifoldlikeness or dimension diagnostics, then
they are not spacetime witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    CausetAudit,
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    non_strict_relation,
)
from models.finality_descent_theorem import CompletionResult, run_t54_analysis
from models.gap_phantom_equivalence import run_t58_audit


@dataclass(frozen=True)
class BridgeAudit:
    name: str
    source_completion: str
    t54_classification: str
    t54_theorem_applies: bool
    t58_gap_gate_passed: bool
    t126_classification: str
    causal_set_candidate: bool
    manifold_filter_passed: bool
    event_count: int
    strict_pair_count: int | None
    ordering_fraction: Fraction | None
    dimension_diagnostic: str
    verdict: str
    reason: str


@dataclass(frozen=True)
class T154Result:
    audits: tuple[BridgeAudit, ...]
    canonical_completions_audited: bool
    t58_gate_required: bool
    all_actual_canonical_colimits_blocked_before_manifold_claims: bool
    no_named_dimension_estimator_applied: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def run_t154_analysis() -> T154Result:
    """Run the direct T54/T58-to-T126 bridge audit."""

    completions = _selected_t54_completions()
    t58_gates = _t58_gap_gates()
    audits = tuple(
        _bridge_completion_to_t126(completion, t58_gates)
        for completion in completions
    )
    by_source = {audit.source_completion: audit for audit in audits}
    canonical_names = {"T51_phantom_repair", "T52_symmetric_reconstruction"}
    actual_canonical_audits = tuple(
        audit for audit in audits if audit.source_completion in canonical_names
    )

    canonical_completions_audited = canonical_names <= set(by_source)
    t58_gate_required = all(
        by_source[name].t58_gap_gate_passed for name in canonical_names
    )
    all_blocked = all(
        audit.causal_set_candidate
        and audit.t126_classification == "insufficient_scale"
        and not audit.manifold_filter_passed
        for audit in actual_canonical_audits
    )
    no_dimension_estimator = all(
        audit.dimension_diagnostic != "ready_for_named_dimension_estimator"
        for audit in audits
    )

    return T154Result(
        audits=audits,
        canonical_completions_audited=canonical_completions_audited,
        t58_gate_required=t58_gate_required,
        all_actual_canonical_colimits_blocked_before_manifold_claims=all_blocked,
        no_named_dimension_estimator_applied=no_dimension_estimator,
        strongest_claim=(
            "The actual T54 canonical T51/T52 quotient-union completions can be "
            "adapted into finite causal-set candidates only after the T58 "
            "phantom-gap gate passes, but both are too small for T126 "
            "manifoldlikeness or named dimension-estimator use."
        ),
        improved=(
            "T154 removes a placeholder in the S1/T126 chain: T126 now has a "
            "direct executable bridge from T54 completions and T58 gap checks, "
            "rather than only synthetic controls and prose dependencies."
        ),
        weakened=(
            "T51 and T52 are not current spacetime-reconstruction witnesses. "
            "They are three- and four-event finite causal-set candidates whose "
            "positive content stops at the causal-set gate."
        ),
        falsification_condition=(
            "T154 fails if the adapter changes the T54 event-finality order, "
            "if T58 exact-match extension is not required before phantom-gap "
            "resolution, or if a sub-scale finite colimit is legitimately "
            "promoted to manifoldlike evidence without a declared dimension, "
            "sprinkling, locality, or continuum-limit diagnostic."
        ),
        s1_update=(
            "S1 remains open_formal_target. Actual T54/T58 colimits now enter "
            "the T126 screen, but the current canonical examples are only "
            "small causal-set candidates and are blocked before manifold claims."
        ),
        claim_ledger_update=(
            "Add T154 to S1: T54 canonical T51/T52 completions pass through a "
            "T58 well-formed phantom-gap gate into T126, where both are "
            "classified insufficient_scale. This makes the finite-to-spacetime "
            "bridge more executable while weakening any T51/T52 spacetime read."
        ),
        open_blocker=(
            "No actual finality colimit in the current T54/T58 family is large "
            "enough to apply a named causal-set dimension estimator, sprinkling "
            "diagnostic, locality test, faithful embedding theorem, or "
            "continuum-limit argument."
        ),
        suggested_next=(
            "Construct a larger T54-style canonical colimit with at least the "
            "T126 minimum scale, then compare it to a declared Myrheim-Meyer "
            "ordering-fraction target or a named sprinkling/locality diagnostic."
        ),
    )


def _selected_t54_completions() -> tuple[CompletionResult, ...]:
    result = run_t54_analysis()
    names = {
        "T51_phantom_repair",
        "T52_symmetric_reconstruction",
        "T53_ambiguous_identity",
    }
    return tuple(
        completion
        for completion in result.completions
        if completion.datum_name in names
    )


def _t58_gap_gates() -> dict[str, bool]:
    result = run_t58_audit()
    gates: dict[str, bool] = {}
    for source in ("T51", "T52"):
        source_audits = tuple(
            audit for audit in result.observer_audits if audit.source_test == source
        )
        gates[source] = bool(source_audits) and all(
            audit.classification == "exact_match"
            and audit.local_is_suborder
            and audit.gap_equals_phantoms
            for audit in source_audits
        )
    return gates


def _bridge_completion_to_t126(
    completion: CompletionResult,
    t58_gates: dict[str, bool],
) -> BridgeAudit:
    source = _source_test_name(completion.datum_name)
    gate_passed = t58_gates.get(source, False)
    datum = _completion_to_t126_datum(completion, source, gate_passed)
    t126_audit = audit_finality_colimit_causet(datum)
    return _bridge_audit_from_t126(completion, gate_passed, t126_audit)


def _source_test_name(completion_name: str) -> str:
    if completion_name.startswith("T51"):
        return "T51"
    if completion_name.startswith("T52"):
        return "T52"
    if completion_name.startswith("T53"):
        return "T53"
    return "UNKNOWN"


def _completion_to_t126_datum(
    completion: CompletionResult,
    source: str,
    t58_gate_passed: bool,
) -> FinalityColimitCausetDatum:
    events = frozenset(event.name for event in completion.global_events)
    if completion.partial_order is None:
        relation = non_strict_relation(events, frozenset())
    else:
        relation = frozenset(completion.partial_order.order_pairs)

    descent_gate_passed = completion.theorem_applies and completion.partial_order is not None
    canonical_colimit = completion.classification == "canonical" and descent_gate_passed
    source_uses_phantom_gate = source in {"T51", "T52"}
    phantom_gap_resolved = (
        t58_gate_passed if canonical_colimit and source_uses_phantom_gate else False
    )

    return FinalityColimitCausetDatum(
        name=f"t154_{completion.datum_name}",
        events=events,
        relation=relation,
        descent_gate_passed=descent_gate_passed,
        canonical_colimit=canonical_colimit,
        phantom_gap_resolved=phantom_gap_resolved,
        observer_only_gap_changes_strict_order=not phantom_gap_resolved,
        source=f"T54 {completion.datum_name} with T58 {source} gate",
    )


def _bridge_audit_from_t126(
    completion: CompletionResult,
    t58_gate_passed: bool,
    t126_audit: CausetAudit,
) -> BridgeAudit:
    diagnostics = t126_audit.diagnostics
    if diagnostics is None:
        event_count = len(completion.global_events)
        strict_pair_count = None
        ordering_fraction = None
    else:
        event_count = diagnostics.event_count
        strict_pair_count = diagnostics.strict_pair_count
        ordering_fraction = diagnostics.comparable_fraction

    dimension_diagnostic = _dimension_diagnostic(t126_audit)
    if (
        t126_audit.causal_set_candidate
        and t126_audit.classification == "insufficient_scale"
    ):
        verdict = "causet_candidate_only"
    elif t126_audit.manifold_filter_passed:
        verdict = "passes_t126_filter_only"
    else:
        verdict = "blocked_before_spacetime_claim"

    return BridgeAudit(
        name=t126_audit.name,
        source_completion=completion.datum_name,
        t54_classification=completion.classification,
        t54_theorem_applies=completion.theorem_applies,
        t58_gap_gate_passed=t58_gate_passed,
        t126_classification=t126_audit.classification,
        causal_set_candidate=t126_audit.causal_set_candidate,
        manifold_filter_passed=t126_audit.manifold_filter_passed,
        event_count=event_count,
        strict_pair_count=strict_pair_count,
        ordering_fraction=ordering_fraction,
        dimension_diagnostic=dimension_diagnostic,
        verdict=verdict,
        reason=t126_audit.reason,
    )


def _dimension_diagnostic(audit: CausetAudit) -> str:
    diagnostics = audit.diagnostics
    if not audit.causal_set_candidate:
        return "not_reached"
    if diagnostics is None:
        return "not_reached"
    if audit.classification == "insufficient_scale":
        return "myrheim_meyer_ordering_fraction_not_applied_below_minimum_scale"
    if not audit.manifold_filter_passed:
        return "blocked_before_named_dimension_estimator"
    return "ready_for_named_dimension_estimator"


def t154_result_to_dict(result: T154Result) -> dict[str, Any]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "canonical_completions_audited": result.canonical_completions_audited,
        "t58_gate_required": result.t58_gate_required,
        "all_actual_canonical_colimits_blocked_before_manifold_claims": (
            result.all_actual_canonical_colimits_blocked_before_manifold_claims
        ),
        "no_named_dimension_estimator_applied": (
            result.no_named_dimension_estimator_applied
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


def _audit_to_dict(audit: BridgeAudit) -> dict[str, Any]:
    return {
        "name": audit.name,
        "source_completion": audit.source_completion,
        "t54_classification": audit.t54_classification,
        "t54_theorem_applies": audit.t54_theorem_applies,
        "t58_gap_gate_passed": audit.t58_gap_gate_passed,
        "t126_classification": audit.t126_classification,
        "causal_set_candidate": audit.causal_set_candidate,
        "manifold_filter_passed": audit.manifold_filter_passed,
        "event_count": audit.event_count,
        "strict_pair_count": audit.strict_pair_count,
        "ordering_fraction": (
            _fraction_to_dict(audit.ordering_fraction)
            if audit.ordering_fraction is not None
            else None
        ),
        "dimension_diagnostic": audit.dimension_diagnostic,
        "verdict": audit.verdict,
        "reason": audit.reason,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, Any]:
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "float": float(value),
    }
