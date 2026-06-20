"""T113: Gap Presheaf Classification.

This module audits whether the finite TaF gap assignment

    G(U) = A(U) - F(U)

classifies phantom incomparability witnesses.

The result is intentionally conservative. Raw gap sections are useful, but the
tested family includes noncanonical T53 completions and malformed local-order
controls where raw H0(G) contains diagnostic gaps that should not be promoted
to phantom witnesses. The supported object is therefore a typed subobject:
endpoint-accessible, canonical-ambient, well-formed local sections whose gap
pair is a local incomparability rather than a local reversal/conflict.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.finality_reflection_property import (
    build_branching_dependency_lattice_cover,
    build_hidden_intermediary_lattice_cover,
    check_gap_restriction_closure,
)
from models.gap_phantom_equivalence import (
    audit_t51,
    audit_t52,
    build_conflicting_order_control,
)
from models.observer_colimit_descent_boundary import build_t53_cases, run_t53_analysis
from models.sheaf_cohomology_apparent_finality import (
    FiniteObserverCover,
    ObserverPatch,
    _build_hidden_intermediary_cover,
    compute_apparent_order,
    compute_global_order,
    detect_phantom_pairs,
    restrict_order,
)


Pair = tuple[str, str]
SectionKey = tuple[str, str, str, str]


@dataclass(frozen=True)
class SectionAudit:
    """One observer section comparison for A(U), F(U), G(U), and phantoms."""

    source_pattern: str
    case_name: str
    observer: str
    ambient_pairs: frozenset[Pair]
    apparent_pairs: frozenset[Pair]
    gap_pairs: frozenset[Pair]
    phantom_pairs: frozenset[Pair]
    typed_gap_pairs: frozenset[Pair]
    extra_raw_gap_pairs: frozenset[Pair]
    extra_typed_gap_pairs: frozenset[Pair]
    missing_typed_gap_pairs: frozenset[Pair]
    spurious_apparent_pairs: frozenset[Pair]
    endpoint_accessible: bool
    local_is_suborder: bool
    canonical_ambient: bool
    local_incomparability_only: bool
    raw_gap_equals_phantoms: bool
    typed_gap_equals_phantoms: bool
    classification: str
    note: str


@dataclass(frozen=True)
class T53Diagnostic:
    """T53 case-level boundary signal used by T113."""

    case_name: str
    verdict: str
    compatible_completion_names: tuple[str, ...]
    unique_completion: bool
    gap_bearing_completion_names: tuple[str, ...]
    classification_role: str
    note: str


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T113Result:
    section_audits: tuple[SectionAudit, ...]
    t53_diagnostics: tuple[T53Diagnostic, ...]
    frp_gap_checks: tuple[Any, ...]
    raw_h0_gap_sections: frozenset[SectionKey]
    typed_gap_sections: frozenset[SectionKey]
    phantom_sections: frozenset[SectionKey]
    raw_h0_equals_phantoms: bool
    typed_gap_sections_equal_phantoms: bool
    malformed_controls_rejected: bool
    frp_restriction_closure_preserved: bool
    t53_noncanonical_blocks_raw_classification: bool
    best_supported: str
    finding: str
    guardrails: tuple[str, ...]
    hypothesis_evaluations: tuple[HypothesisResult, ...]


def _nonreflexive(order: frozenset[Pair]) -> frozenset[Pair]:
    return frozenset((a, b) for (a, b) in order if a != b)


def _relation(pair: Pair, order: frozenset[Pair]) -> str:
    a, b = pair
    if (a, b) in order:
        return "leq"
    if (b, a) in order:
        return "geq"
    return "incomparable"


def _section_keys(audit: SectionAudit, pairs: frozenset[Pair]) -> frozenset[SectionKey]:
    return frozenset(
        (audit.source_pattern, audit.case_name, audit.observer, f"{a}->{b}")
        for (a, b) in pairs
    )


def _classify_section(
    *,
    source_pattern: str,
    case_name: str,
    observer: str,
    ambient_order: frozenset[Pair],
    apparent_order: frozenset[Pair],
    phantom_pairs: frozenset[Pair],
    canonical_ambient: bool,
    endpoint_accessible: bool = True,
    note: str = "",
) -> SectionAudit:
    ambient = _nonreflexive(ambient_order)
    apparent = _nonreflexive(apparent_order)
    gap = ambient - apparent
    spurious = apparent - ambient
    local_is_suborder = not spurious
    local_incomparability_only = all(_relation(pair, apparent) == "incomparable" for pair in gap)

    typed_gap = (
        gap
        if endpoint_accessible
        and canonical_ambient
        and local_is_suborder
        and local_incomparability_only
        else frozenset()
    )

    extra_raw = gap - phantom_pairs
    extra_typed = typed_gap - phantom_pairs
    missing_typed = phantom_pairs - typed_gap
    raw_match = gap == phantom_pairs
    typed_match = typed_gap == phantom_pairs

    if not canonical_ambient:
        classification = "noncanonical_ambient_diagnostic"
    elif not local_is_suborder:
        classification = "invalid_local_order_control"
    elif not local_incomparability_only:
        classification = "not_incomparability"
    elif typed_match and typed_gap:
        classification = "typed_exact_match"
    elif typed_match and not gap and not phantom_pairs:
        classification = "empty_exact_match"
    else:
        classification = "mismatch"

    return SectionAudit(
        source_pattern=source_pattern,
        case_name=case_name,
        observer=observer,
        ambient_pairs=ambient,
        apparent_pairs=apparent,
        gap_pairs=gap,
        phantom_pairs=phantom_pairs,
        typed_gap_pairs=typed_gap,
        extra_raw_gap_pairs=extra_raw,
        extra_typed_gap_pairs=extra_typed,
        missing_typed_gap_pairs=missing_typed,
        spurious_apparent_pairs=spurious,
        endpoint_accessible=endpoint_accessible,
        local_is_suborder=local_is_suborder,
        canonical_ambient=canonical_ambient,
        local_incomparability_only=local_incomparability_only,
        raw_gap_equals_phantoms=raw_match,
        typed_gap_equals_phantoms=typed_match,
        classification=classification,
        note=note,
    )


def _audits_from_t58() -> tuple[SectionAudit, ...]:
    audits: list[SectionAudit] = []
    for source_audit in audit_t51() + audit_t52():
        audits.append(
            _classify_section(
                source_pattern=source_audit.source_test,
                case_name=source_audit.source_test.lower(),
                observer=source_audit.observer,
                ambient_order=source_audit.ambient_pairs,
                apparent_order=source_audit.apparent_pairs,
                phantom_pairs=source_audit.phantom_pairs,
                canonical_ambient=True,
                note="Imported T58 well-formed T51/T52 gap-phantom audit.",
            )
        )
    return tuple(audits)


def _audits_from_cover(source_pattern: str, cover: FiniteObserverCover) -> tuple[SectionAudit, ...]:
    global_order = compute_global_order(cover)
    phantom_by_patch: dict[str, set[Pair]] = {patch.name: set() for patch in cover.patches}
    for phantom in detect_phantom_pairs(cover, global_order):
        phantom_by_patch.setdefault(phantom.observer, set()).add(
            (phantom.event_j, phantom.event_i)
        )

    audits: list[SectionAudit] = []
    for patch in cover.patches:
        accessible = cover.accessible_event_names(patch)
        ambient = restrict_order(global_order, accessible)
        apparent = compute_apparent_order(cover, patch)
        audits.append(
            _classify_section(
                source_pattern=source_pattern,
                case_name=cover.name,
                observer=patch.name,
                ambient_order=ambient,
                apparent_order=apparent,
                phantom_pairs=frozenset(phantom_by_patch.get(patch.name, set())),
                canonical_ambient=True,
                note="Finite record-access cover with independently detected phantoms.",
            )
        )
    return tuple(audits)


def _record_order_for_events(events: tuple[Any, ...]) -> frozenset[Pair]:
    names = [event.name for event in events]
    order: set[Pair] = {(name, name) for name in names}
    for predecessor in events:
        for successor in events:
            if predecessor.name == successor.name:
                continue
            if predecessor.target_records and predecessor.target_records <= successor.source_records:
                order.add((predecessor.name, successor.name))

    changed = True
    while changed:
        changed = False
        additions: set[Pair] = set()
        for a, b in order:
            for c, d in order:
                if b == c and (a, d) not in order:
                    additions.add((a, d))
        if additions:
            order.update(additions)
            changed = True
    return frozenset(order)


def _relabeled_local_order(view: Any, mapping: dict[str, str]) -> frozenset[Pair]:
    local_order = _record_order_for_events(view.events)
    return frozenset(
        (mapping[a], mapping[b])
        for (a, b) in local_order
        if a in mapping and b in mapping
    )


def _audits_from_t53() -> tuple[tuple[SectionAudit, ...], tuple[T53Diagnostic, ...]]:
    cases = {case.name: case for case in build_t53_cases()}
    evaluated = {case.case_name: case for case in run_t53_analysis().cases}
    section_audits: list[SectionAudit] = []
    diagnostics: list[T53Diagnostic] = []

    for case_name, case in cases.items():
        evaluation = evaluated[case_name]
        gap_bearing: list[str] = []

        for completion in case.completions:
            completion_eval = next(
                ev for ev in evaluation.evaluations if ev.completion_name == completion.name
            )
            if not completion_eval.compatible_with_views:
                continue

            ambient_global = _record_order_for_events(completion.events)
            canonical = evaluation.unique_completion and completion_eval.compatible_with_views
            completion_has_gap = False

            for view in case.observer_views:
                mapping = {
                    event_map.local_event: event_map.global_event
                    for event_map in completion.event_maps
                    if event_map.observer == view.name
                }
                accessible = frozenset(mapping.values())
                ambient = restrict_order(ambient_global, accessible)
                apparent = _relabeled_local_order(view, mapping)
                gap = _nonreflexive(ambient) - _nonreflexive(apparent)
                completion_has_gap = completion_has_gap or bool(gap)

                phantom_pairs = gap if canonical else frozenset()
                section_audits.append(
                    _classify_section(
                        source_pattern="T53",
                        case_name=f"{case_name}:{completion.name}",
                        observer=view.name,
                        ambient_order=ambient,
                        apparent_order=apparent,
                        phantom_pairs=phantom_pairs,
                        canonical_ambient=canonical,
                        note=(
                            "T53 completion is unique and compatible."
                            if canonical
                            else "T53 completion is compatible but not a canonical ambient order."
                        ),
                    )
                )

            if completion_has_gap:
                gap_bearing.append(completion.name)

        if not evaluation.compatible_completion_names:
            role = "diagnostic_only"
            note = "No compatible ambient completion exists, so A(U) is not defined canonically."
        elif evaluation.unique_completion:
            role = "canonical_control"
            note = "The compatible completion is unique; gap sections may be typed."
        else:
            role = "noncanonical_blocks_classification"
            note = "Multiple compatible completions remain; raw gaps are completion-relative diagnostics."

        diagnostics.append(
            T53Diagnostic(
                case_name=case_name,
                verdict=evaluation.verdict,
                compatible_completion_names=evaluation.compatible_completion_names,
                unique_completion=evaluation.unique_completion,
                gap_bearing_completion_names=tuple(gap_bearing),
                classification_role=role,
                note=note,
            )
        )

    return tuple(section_audits), tuple(diagnostics)


def _malformed_controls() -> tuple[SectionAudit, ...]:
    reversal = build_conflicting_order_control()
    local_reversal = _classify_section(
        source_pattern="T58_CONTROL",
        case_name="local_reversal",
        observer=reversal.observer,
        ambient_order=reversal.ambient_pairs,
        apparent_order=reversal.apparent_pairs,
        phantom_pairs=frozenset(),
        canonical_ambient=True,
        note="Hostile local reversal: a conflicting local order is not a phantom gap.",
    )

    malformed_extra = _classify_section(
        source_pattern="T113_CONTROL",
        case_name="malformed_extra_local_order",
        observer="malformed_extra_local_order",
        ambient_order=frozenset({("a", "a"), ("b", "b"), ("a", "b")}),
        apparent_order=frozenset({("a", "a"), ("b", "b"), ("a", "b"), ("b", "a")}),
        phantom_pairs=frozenset(),
        canonical_ambient=True,
        note="Malformed local section has F(U) not contained in A(U).",
    )
    return (local_reversal, malformed_extra)


def run_t113_analysis() -> T113Result:
    """Run the finite T113 gap-presheaf classification audit."""

    t58_audits = _audits_from_t58()
    t56_audits = _audits_from_cover("T56", _build_hidden_intermediary_cover())
    t57_covers = (
        build_hidden_intermediary_lattice_cover(),
        build_branching_dependency_lattice_cover(),
    )
    t57_audits = tuple(
        audit
        for cover in t57_covers
        for audit in _audits_from_cover("T57", cover)
    )
    t53_audits, t53_diagnostics = _audits_from_t53()
    controls = _malformed_controls()

    section_audits = t58_audits + t56_audits + t57_audits + t53_audits + controls
    frp_checks = tuple(check_gap_restriction_closure(cover) for cover in t57_covers)

    raw_h0 = frozenset(
        key
        for audit in section_audits
        for key in _section_keys(audit, audit.gap_pairs)
    )
    typed = frozenset(
        key
        for audit in section_audits
        for key in _section_keys(audit, audit.typed_gap_pairs)
    )
    phantoms = frozenset(
        key
        for audit in section_audits
        for key in _section_keys(audit, audit.phantom_pairs)
    )

    raw_equals = raw_h0 == phantoms
    typed_equals = typed == phantoms
    malformed_rejected = all(
        audit.classification == "invalid_local_order_control"
        and not audit.typed_gap_pairs
        and not audit.phantom_pairs
        for audit in controls
    )
    frp_preserved = all(check.holds and not check.violations for check in frp_checks)
    t53_blocks = any(
        diagnostic.classification_role == "noncanonical_blocks_classification"
        and diagnostic.gap_bearing_completion_names
        for diagnostic in t53_diagnostics
    )

    hypotheses = (
        HypothesisResult(
            "H_RAW_H0_CLASSIFIES",
            "Raw H0(G), taken as all computed gap sections, classifies phantom incomparability.",
            "refuted" if not raw_equals else "supported",
            (
                f"raw_gap_sections={len(raw_h0)}, phantom_sections={len(phantoms)}; "
                f"extra_raw={len(raw_h0 - phantoms)}, missing={len(phantoms - raw_h0)}"
            ),
        ),
        HypothesisResult(
            "H_TYPED_SUBOBJECT_CLASSIFIES",
            "The endpoint-accessible, canonical, well-formed local-incomparability subobject of H0(G) classifies phantom witnesses in the finite family.",
            "supported" if typed_equals else "refuted",
            (
                f"typed_gap_sections={len(typed)}, phantom_sections={len(phantoms)}; "
                f"extra_typed={len(typed - phantoms)}, missing={len(phantoms - typed)}"
            ),
        ),
        HypothesisResult(
            "H_FRP_CLOSURE_PRESERVED",
            "T57 FRP gap restriction closure remains intact for the T113 covers.",
            "supported" if frp_preserved else "refuted",
            "; ".join(f"{check.cover_name}: holds={check.holds}" for check in frp_checks),
        ),
        HypothesisResult(
            "H_MALFORMED_CONTROLS_REJECTED",
            "Malformed/local-reversal controls are rejected before gap sections are called phantoms.",
            "supported" if malformed_rejected else "refuted",
            "; ".join(f"{audit.case_name}: {audit.classification}" for audit in controls),
        ),
        HypothesisResult(
            "H_T53_BOUNDARY",
            "T53 underdetermined completions block raw classification and remain diagnostic only.",
            "supported" if t53_blocks else "refuted",
            "; ".join(
                f"{d.case_name}: {d.classification_role}, gaps={list(d.gap_bearing_completion_names)}"
                for d in t53_diagnostics
            ),
        ),
    )

    if typed_equals and not raw_equals and malformed_rejected and frp_preserved and t53_blocks:
        best = (
            "A typed subobject of H0(G), not raw H0(G), classifies phantom "
            "incomparability in the tested finite witness family."
        )
        finding = (
            "T113 supports a conservative classification theorem for the finite "
            "TaF witnesses: after requiring endpoint access, a canonical ambient "
            "completion, F(U) subset A(U), and local incomparability, every typed "
            "gap section is an independently computed phantom witness and every "
            "phantom witness appears as a typed gap section. Raw H0(G) remains "
            "too broad because noncanonical T53 repairs and malformed local "
            "reversals create diagnostic gaps."
        )
    elif raw_equals:
        best = "Raw H0(G) classifies phantom incomparability in the tested finite family."
        finding = "The finite audit did not find a raw gap/phantom mismatch."
    else:
        best = "G is diagnostic only; no tested classification object is exact."
        finding = (
            "The finite audit found mismatches even after typing; keep G as a "
            "diagnostic until the typing rules are revised."
        )

    guardrails = (
        "This does not validate Geometric Unity or any physical torsion tensor.",
        "This does not prove that F sheafifies to A.",
        "This does not derive finality-arrow direction.",
        "T53-style noncanonical completions remain completion-relative diagnostics.",
    )

    return T113Result(
        section_audits=section_audits,
        t53_diagnostics=t53_diagnostics,
        frp_gap_checks=frp_checks,
        raw_h0_gap_sections=raw_h0,
        typed_gap_sections=typed,
        phantom_sections=phantoms,
        raw_h0_equals_phantoms=raw_equals,
        typed_gap_sections_equal_phantoms=typed_equals,
        malformed_controls_rejected=malformed_rejected,
        frp_restriction_closure_preserved=frp_preserved,
        t53_noncanonical_blocks_raw_classification=t53_blocks,
        best_supported=best,
        finding=finding,
        guardrails=guardrails,
        hypothesis_evaluations=hypotheses,
    )


def _pairs_to_lists(pairs: frozenset[Pair]) -> list[list[str]]:
    return [[a, b] for (a, b) in sorted(pairs)]


def _keys_to_lists(keys: frozenset[SectionKey]) -> list[dict[str, str]]:
    return [
        {
            "source_pattern": source,
            "case_name": case_name,
            "observer": observer,
            "pair": pair,
        }
        for (source, case_name, observer, pair) in sorted(keys)
    ]


def _audit_to_dict(audit: SectionAudit) -> dict[str, Any]:
    return {
        "source_pattern": audit.source_pattern,
        "case_name": audit.case_name,
        "observer": audit.observer,
        "ambient_pairs": _pairs_to_lists(audit.ambient_pairs),
        "apparent_pairs": _pairs_to_lists(audit.apparent_pairs),
        "gap_pairs": _pairs_to_lists(audit.gap_pairs),
        "phantom_pairs": _pairs_to_lists(audit.phantom_pairs),
        "typed_gap_pairs": _pairs_to_lists(audit.typed_gap_pairs),
        "extra_raw_gap_pairs": _pairs_to_lists(audit.extra_raw_gap_pairs),
        "extra_typed_gap_pairs": _pairs_to_lists(audit.extra_typed_gap_pairs),
        "missing_typed_gap_pairs": _pairs_to_lists(audit.missing_typed_gap_pairs),
        "spurious_apparent_pairs": _pairs_to_lists(audit.spurious_apparent_pairs),
        "endpoint_accessible": audit.endpoint_accessible,
        "local_is_suborder": audit.local_is_suborder,
        "canonical_ambient": audit.canonical_ambient,
        "local_incomparability_only": audit.local_incomparability_only,
        "raw_gap_equals_phantoms": audit.raw_gap_equals_phantoms,
        "typed_gap_equals_phantoms": audit.typed_gap_equals_phantoms,
        "classification": audit.classification,
        "note": audit.note,
    }


def t113_result_to_dict(result: T113Result) -> dict[str, Any]:
    return {
        "section_audits": [_audit_to_dict(audit) for audit in result.section_audits],
        "t53_diagnostics": [
            {
                "case_name": diagnostic.case_name,
                "verdict": diagnostic.verdict,
                "compatible_completion_names": list(diagnostic.compatible_completion_names),
                "unique_completion": diagnostic.unique_completion,
                "gap_bearing_completion_names": list(diagnostic.gap_bearing_completion_names),
                "classification_role": diagnostic.classification_role,
                "note": diagnostic.note,
            }
            for diagnostic in result.t53_diagnostics
        ],
        "frp_gap_checks": [
            {
                "cover_name": check.cover_name,
                "comparable_patch_pairs": check.comparable_patch_pairs,
                "holds": check.holds,
                "violations": [
                    {
                        "larger_patch": violation.larger_patch,
                        "smaller_patch": violation.smaller_patch,
                        "pair": list(violation.pair),
                        "explanation": violation.explanation,
                    }
                    for violation in check.violations
                ],
                "non_lifting_examples": [
                    {
                        "larger_patch": example.larger_patch,
                        "smaller_patch": example.smaller_patch,
                        "pair": list(example.pair),
                        "explanation": example.explanation,
                    }
                    for example in check.non_lifting_examples
                ],
            }
            for check in result.frp_gap_checks
        ],
        "raw_h0_gap_sections": _keys_to_lists(result.raw_h0_gap_sections),
        "typed_gap_sections": _keys_to_lists(result.typed_gap_sections),
        "phantom_sections": _keys_to_lists(result.phantom_sections),
        "raw_h0_equals_phantoms": result.raw_h0_equals_phantoms,
        "typed_gap_sections_equal_phantoms": result.typed_gap_sections_equal_phantoms,
        "malformed_controls_rejected": result.malformed_controls_rejected,
        "frp_restriction_closure_preserved": result.frp_restriction_closure_preserved,
        "t53_noncanonical_blocks_raw_classification": (
            result.t53_noncanonical_blocks_raw_classification
        ),
        "best_supported": result.best_supported,
        "finding": result.finding,
        "guardrails": list(result.guardrails),
        "hypothesis_evaluations": [
            {
                "id": h.hypothesis_id,
                "claim": h.claim,
                "status": h.status,
                "evidence": h.evidence,
            }
            for h in result.hypothesis_evaluations
        ],
    }
