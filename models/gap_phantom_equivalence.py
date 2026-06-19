"""T58: Gap-Phantom Equivalence Audit.

This model tests T56 open question Q1 on the already-built T51 and T52
finite colimit witnesses:

    Is H0(G), with G(U) = A(U) - F(U), exactly the set of phantom
    incomparability witnesses?

Here A(U) is the event-finality/colimit order restricted to the observer's
event domain, and F(U) is that observer's apparent order. In T51 and T52 every
observer sees the same event labels, so the restriction is the non-reflexive
colimit order over those labels.

The audit deliberately does not promote a universal theorem. It verifies the
equivalence for the well-formed T51/T52 extension cases and includes a
conflicting-order control showing that the equivalence requires local apparent
orders to be suborders of the ambient event-finality order.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.multi_observer_apparent_finality_colimit import run_t51_analysis
from models.symmetric_colimit_theorem import run_t52_analysis


Pair = tuple[str, str]


@dataclass(frozen=True)
class ObserverGapAudit:
    """Gap-vs-phantom comparison for one observer in one finite witness."""

    source_test: str
    observer: str
    ambient_pairs: frozenset[Pair]
    apparent_pairs: frozenset[Pair]
    gap_pairs: frozenset[Pair]
    phantom_pairs: frozenset[Pair]
    extra_gap_pairs: frozenset[Pair]
    missing_gap_pairs: frozenset[Pair]
    spurious_apparent_pairs: frozenset[Pair]
    local_is_suborder: bool
    gap_equals_phantoms: bool
    classification: str


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T58Result:
    observer_audits: tuple[ObserverGapAudit, ...]
    control_audit: ObserverGapAudit
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    t51_gap_equals_phantoms: bool
    t52_gap_equals_phantoms: bool
    extension_condition_necessary: bool
    best_supported: str
    finding: str
    boundary: str


def _nonreflexive(order: frozenset[Pair]) -> frozenset[Pair]:
    return frozenset((a, b) for (a, b) in order if a != b)


def _phantom_pairs_from_t51(result: Any, observer_name: str) -> frozenset[Pair]:
    return frozenset(
        (p.event_j, p.event_i)
        for p in result.phantom_results
        if p.is_phantom and p.observer_name == observer_name
    )


def _phantom_pairs_from_t52(result: Any, observer_name: str) -> frozenset[Pair]:
    return frozenset(
        (p.event_j, p.event_i)
        for p in result.phantoms
        if p.is_phantom and p.observer == observer_name
    )


def _classify_audit(
    source_test: str,
    observer: str,
    ambient_order: frozenset[Pair],
    apparent_order: frozenset[Pair],
    phantom_pairs: frozenset[Pair],
) -> ObserverGapAudit:
    ambient = _nonreflexive(ambient_order)
    apparent = _nonreflexive(apparent_order)
    gap = ambient - apparent
    spurious = apparent - ambient
    extra_gap = gap - phantom_pairs
    missing_gap = phantom_pairs - gap
    local_is_suborder = not spurious
    gap_equals_phantoms = gap == phantom_pairs

    if gap_equals_phantoms and local_is_suborder:
        classification = "exact_match"
    elif not local_is_suborder:
        classification = "invalid_extension_boundary"
    else:
        classification = "mismatch"

    return ObserverGapAudit(
        source_test=source_test,
        observer=observer,
        ambient_pairs=ambient,
        apparent_pairs=apparent,
        gap_pairs=gap,
        phantom_pairs=phantom_pairs,
        extra_gap_pairs=extra_gap,
        missing_gap_pairs=missing_gap,
        spurious_apparent_pairs=spurious,
        local_is_suborder=local_is_suborder,
        gap_equals_phantoms=gap_equals_phantoms,
        classification=classification,
    )


def audit_t51() -> tuple[ObserverGapAudit, ...]:
    """Compare G(U) and phantom witnesses in T51."""
    result = run_t51_analysis()
    ambient = result.colimit.colimit_order
    return (
        _classify_audit(
            "T51",
            result.observer_a.name,
            ambient,
            result.observer_a.apparent_order,
            _phantom_pairs_from_t51(result, result.observer_a.name),
        ),
        _classify_audit(
            "T51",
            result.observer_b.name,
            ambient,
            result.observer_b.apparent_order,
            _phantom_pairs_from_t51(result, result.observer_b.name),
        ),
    )


def audit_t52() -> tuple[ObserverGapAudit, ...]:
    """Compare G(U) and phantom witnesses in T52."""
    result = run_t52_analysis()
    ambient = result.colimit.colimit_order
    return (
        _classify_audit(
            "T52",
            result.observer_a.name,
            ambient,
            result.observer_a.apparent_order,
            _phantom_pairs_from_t52(result, result.observer_a.name),
        ),
        _classify_audit(
            "T52",
            result.observer_b.name,
            ambient,
            result.observer_b.apparent_order,
            _phantom_pairs_from_t52(result, result.observer_b.name),
        ),
    )


def build_conflicting_order_control() -> ObserverGapAudit:
    """Hostile control: a reversed local comparison is not a phantom gap."""
    ambient = frozenset({("a", "a"), ("b", "b"), ("a", "b")})
    apparent = frozenset({("a", "a"), ("b", "b"), ("b", "a")})

    # Phantom incomparability requires local incomparability, not local conflict.
    phantoms = frozenset()
    return _classify_audit(
        "CONTROL",
        "local_reversal",
        ambient,
        apparent,
        phantoms,
    )


def run_t58_audit() -> T58Result:
    """Run the bounded T58 gap-phantom equivalence audit."""
    t51_audits = audit_t51()
    t52_audits = audit_t52()
    all_witness_audits = t51_audits + t52_audits
    control = build_conflicting_order_control()

    t51_ok = all(a.gap_equals_phantoms and a.local_is_suborder for a in t51_audits)
    t52_ok = all(a.gap_equals_phantoms and a.local_is_suborder for a in t52_audits)
    control_blocks_universal = (
        not control.local_is_suborder
        and not control.gap_equals_phantoms
        and control.classification == "invalid_extension_boundary"
    )

    total_gap_pairs = sum(len(a.gap_pairs) for a in all_witness_audits)
    total_phantom_pairs = sum(len(a.phantom_pairs) for a in all_witness_audits)
    mismatches = [
        f"{a.source_test}:{a.observer}"
        for a in all_witness_audits
        if not (a.gap_equals_phantoms and a.local_is_suborder)
    ]

    hypotheses = (
        HypothesisResult(
            "H_T51_GAP_PHANTOM",
            "In T51, each observer's gap section equals its phantom incomparability witnesses.",
            "supported" if t51_ok else "refuted",
            "; ".join(
                f"{a.observer}: gap={sorted(a.gap_pairs)}, phantoms={sorted(a.phantom_pairs)}"
                for a in t51_audits
            ),
        ),
        HypothesisResult(
            "H_T52_GAP_PHANTOM",
            "In T52, each observer's gap section equals its phantom incomparability witnesses.",
            "supported" if t52_ok else "refuted",
            "; ".join(
                f"{a.observer}: gap={sorted(a.gap_pairs)}, phantoms={sorted(a.phantom_pairs)}"
                for a in t52_audits
            ),
        ),
        HypothesisResult(
            "H_EXTENSION_BOUNDARY",
            "The equivalence requires F(U) to be a suborder of A(U); conflicting local order is a different failure mode.",
            "supported" if control_blocks_universal else "refuted",
            (
                f"control gap={sorted(control.gap_pairs)}, "
                f"phantoms={sorted(control.phantom_pairs)}, "
                f"spurious_local={sorted(control.spurious_apparent_pairs)}"
            ),
        ),
    )

    if t51_ok and t52_ok and control_blocks_universal:
        best = (
            "H0(G) matches phantom witnesses for the tested T51/T52 well-formed "
            "extension cases; the extension condition is necessary."
        )
        finding = (
            "T58 supports the refined T56 Q1 claim in the bounded witness class: "
            "across T51 and T52, every gap pair A(U)-F(U) is exactly a phantom "
            "incomparability witness, and every phantom witness appears in the "
            "gap. The hostile reversal control blocks a universal reading."
        )
    else:
        best = "partial: " + ", ".join(h.hypothesis_id for h in hypotheses if h.status == "supported")
        finding = (
            "T58 found a mismatch between gap sections and phantom witnesses in "
            f"{mismatches}. The H0(G) reformulation needs further weakening."
        )

    boundary = (
        "Do not read this as a theorem for arbitrary observer assignments. "
        "If F(U) contains local order pairs absent from A(U), then A(U)-F(U) "
        "mixes missing ambient order with local conflict. Such cases require a "
        "conflict/compatibility diagnostic before calling a gap pair phantom."
    )

    return T58Result(
        observer_audits=all_witness_audits,
        control_audit=control,
        hypothesis_evaluations=hypotheses,
        t51_gap_equals_phantoms=t51_ok,
        t52_gap_equals_phantoms=t52_ok,
        extension_condition_necessary=control_blocks_universal,
        best_supported=best,
        finding=finding,
        boundary=boundary,
    )


def _audit_to_dict(audit: ObserverGapAudit) -> dict[str, Any]:
    return {
        "source_test": audit.source_test,
        "observer": audit.observer,
        "ambient_pairs": sorted([list(p) for p in audit.ambient_pairs]),
        "apparent_pairs": sorted([list(p) for p in audit.apparent_pairs]),
        "gap_pairs": sorted([list(p) for p in audit.gap_pairs]),
        "phantom_pairs": sorted([list(p) for p in audit.phantom_pairs]),
        "extra_gap_pairs": sorted([list(p) for p in audit.extra_gap_pairs]),
        "missing_gap_pairs": sorted([list(p) for p in audit.missing_gap_pairs]),
        "spurious_apparent_pairs": sorted([list(p) for p in audit.spurious_apparent_pairs]),
        "local_is_suborder": audit.local_is_suborder,
        "gap_equals_phantoms": audit.gap_equals_phantoms,
        "classification": audit.classification,
    }


def t58_result_to_dict(result: T58Result) -> dict[str, Any]:
    return {
        "observer_audits": [_audit_to_dict(a) for a in result.observer_audits],
        "control_audit": _audit_to_dict(result.control_audit),
        "hypothesis_evaluations": [
            {
                "id": h.hypothesis_id,
                "claim": h.claim,
                "status": h.status,
                "evidence": h.evidence,
            }
            for h in result.hypothesis_evaluations
        ],
        "t51_gap_equals_phantoms": result.t51_gap_equals_phantoms,
        "t52_gap_equals_phantoms": result.t52_gap_equals_phantoms,
        "extension_condition_necessary": result.extension_condition_necessary,
        "best_supported": result.best_supported,
        "finding": result.finding,
        "boundary": result.boundary,
    }
