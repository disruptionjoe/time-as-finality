"""T534: route TAF9 after the first finality-law candidates fail.

T532 found no cleared finality-native ordering-fraction law candidate. T534
tests one genuinely new finality-domain source-law shape with an independent
comparability-density calculation, while excluding the receipt-product,
target-import, screen-conditioned, and repaired-band routes that are already
negative or forbidden.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

from models.t532_finality_native_ordering_fraction_law_starter import (
    run_t532_analysis,
)


ARTIFACT = "T534-new-finality-domain-law-pause-router-v0.1"
VERDICT = "pause_s1_finite_generator_route_no_cleared_new_source_law"
TARGET_COMPARABILITY_DENSITY = Fraction(1, 2)

ALLOWED_OUTCOMES = ("CLEARED", "NARROWED", "FALSIFIED", "PAUSE", "REVIEW_ONLY")

EXCLUDED_LAW_IDS = (
    "two_channel_receipt_product_order",
    "three_channel_receipt_product_order",
    "external_lorentzian_uv_reference_law",
    "t528_screen_conditioned_receipt_mixture",
    "posthoc_repaired_band_fit",
)

NOT_CLAIMED = (
    "T534 does not derive spacetime, prove manifoldlikeness, establish a "
    "finality-native sprinkling law, repair T528, reverse T223, promote S1, "
    "change claim status, change canon, change public posture, authorize "
    "external publication, or support cross-repo truth. It is a TAF9 source-law "
    "router only."
)

PAUSE_READING = (
    "Difficulty alone is not falsification. The North Star is not demoted "
    "because a source law is hard to find. But the S1 finite-generator route "
    "should pause until a new finality-domain source law exists with an "
    "independent comparability-density reason that clears the T531/T532 burden."
)


@dataclass(frozen=True)
class EndpointPattern:
    pattern_id: str
    a_positions: tuple[int, int]
    b_positions: tuple[int, int]
    relation: str


@dataclass(frozen=True)
class CandidateLaw:
    law_id: str
    description: str
    finality_domain_law: bool
    new_relative_to_t532: bool
    law_declared_before_sampling: bool
    independent_density_reason: bool
    sample_family_predeclared: bool
    hostile_controls_named: bool
    later_burdens_named: bool
    uses_receipt_product_order: bool = False
    imports_lorentzian_reference: bool = False
    conditions_on_t528_or_t530_screen: bool = False
    post_hoc_band_fit: bool = False
    requests_s1_claim_canon_public_or_external_movement: bool = False


@dataclass(frozen=True)
class HostileControl:
    control_id: str
    comparability_density: Fraction
    clears_source_law_gate: bool
    reason: str


@dataclass(frozen=True)
class CandidateDecision:
    law_id: str
    outcome: str
    clears_source_law_gate: bool
    counts_as_s1_evidence: bool
    expected_comparability_density: Fraction | None
    target_comparability_density: Fraction
    missing_requirements: tuple[str, ...]
    reason: str
    deterministic_evidence: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T534Result:
    artifact: str
    source_t532_verdict: str
    source_t532_cleared_candidate_ids: tuple[str, ...]
    excluded_law_ids: tuple[str, ...]
    candidate_menu_ids: tuple[str, ...]
    endpoint_patterns: tuple[EndpointPattern, ...]
    exact_pair_pattern_count: int
    exact_comparable_pattern_count: int
    target_comparability_density: Fraction
    candidate_decisions: tuple[CandidateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    cleared_candidate_ids: tuple[str, ...]
    route_outcome: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    claim_labels: tuple[ClaimLabel, ...]
    s1_update: str
    claim_ledger_update: str
    not_claimed: str


def run_t534_analysis() -> T534Result:
    t532 = run_t532_analysis()
    candidates = _candidate_laws()
    patterns = tuple(record_window_endpoint_patterns())
    decisions = tuple(
        _evaluate_candidate(candidate, endpoint_patterns=patterns)
        for candidate in candidates
    )
    hostile_controls = _hostile_controls()
    cleared = tuple(
        decision.law_id for decision in decisions if decision.clears_source_law_gate
    )
    route_outcome = "REVIEW_ONLY" if cleared else "PAUSE"
    verdict = (
        VERDICT
        if t532.cleared_candidate_ids == ()
        and _candidate_menu_excludes_forbidden(candidates)
        and not cleared
        and route_outcome == "PAUSE"
        and all(not decision.counts_as_s1_evidence for decision in decisions)
        else "new_finality_domain_law_pause_router_unexpected_status"
    )
    return T534Result(
        artifact=ARTIFACT,
        source_t532_verdict=t532.verdict,
        source_t532_cleared_candidate_ids=t532.cleared_candidate_ids,
        excluded_law_ids=EXCLUDED_LAW_IDS,
        candidate_menu_ids=tuple(candidate.law_id for candidate in candidates),
        endpoint_patterns=patterns,
        exact_pair_pattern_count=len(patterns),
        exact_comparable_pattern_count=sum(
            pattern.relation != "incomparable" for pattern in patterns
        ),
        target_comparability_density=TARGET_COMPARABILITY_DENSITY,
        candidate_decisions=decisions,
        hostile_controls=hostile_controls,
        cleared_candidate_ids=cleared,
        route_outcome=route_outcome,
        verdict=verdict,
        strongest_reading=(
            "The record-window separation law is a genuine new finality-domain "
            "candidate, but its exact independent comparability density is 1/3, "
            "not the T532 target density 1/2. It narrows the search by showing "
            "that a natural finalization-window law does not rescue the S1 "
            "finite-generator route."
        ),
        recommended_next=PAUSE_READING,
        claim_labels=_claim_labels(decisions, patterns),
        s1_update=(
            "S1 remains `requires_added_assumption`. T534 supplies no cleared "
            "source law and no S1 evidence."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T534 is a TAF9 routing artifact "
            "only: no claim row, no S1 status movement, and no T223 reversal."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t534_result_to_dict(result: T534Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t532_verdict": result.source_t532_verdict,
        "source_t532_cleared_candidate_ids": list(
            result.source_t532_cleared_candidate_ids
        ),
        "excluded_law_ids": list(result.excluded_law_ids),
        "candidate_menu_ids": list(result.candidate_menu_ids),
        "endpoint_patterns": [
            {
                "pattern_id": pattern.pattern_id,
                "a_positions": list(pattern.a_positions),
                "b_positions": list(pattern.b_positions),
                "relation": pattern.relation,
            }
            for pattern in result.endpoint_patterns
        ],
        "exact_pair_pattern_count": result.exact_pair_pattern_count,
        "exact_comparable_pattern_count": result.exact_comparable_pattern_count,
        "target_comparability_density": _fraction_to_dict(
            result.target_comparability_density
        ),
        "candidate_decisions": [
            _decision_to_dict(decision) for decision in result.candidate_decisions
        ],
        "hostile_controls": [
            {
                "control_id": control.control_id,
                "comparability_density": _fraction_to_dict(
                    control.comparability_density
                ),
                "clears_source_law_gate": control.clears_source_law_gate,
                "reason": control.reason,
            }
            for control in result.hostile_controls
        ],
        "cleared_candidate_ids": list(result.cleared_candidate_ids),
        "route_outcome": result.route_outcome,
        "verdict": result.verdict,
        "strongest_reading": result.strongest_reading,
        "recommended_next": result.recommended_next,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def record_window_endpoint_patterns() -> tuple[EndpointPattern, ...]:
    """Enumerate exact two-record endpoint orders for the window law."""
    patterns: list[EndpointPattern] = []
    all_positions = (1, 2, 3, 4)
    for index, a_positions in enumerate(combinations(all_positions, 2), start=1):
        b_positions = tuple(position for position in all_positions if position not in a_positions)
        if max(a_positions) < min(b_positions):
            relation = "a_before_b"
        elif max(b_positions) < min(a_positions):
            relation = "b_before_a"
        else:
            relation = "incomparable"
        patterns.append(
            EndpointPattern(
                pattern_id=f"endpoint_pattern_{index}",
                a_positions=tuple(a_positions),
                b_positions=b_positions,
                relation=relation,
            )
        )
    return tuple(patterns)


def record_window_expected_density() -> Fraction:
    patterns = record_window_endpoint_patterns()
    comparable = sum(pattern.relation != "incomparable" for pattern in patterns)
    return Fraction(comparable, len(patterns))


def _candidate_laws() -> tuple[CandidateLaw, ...]:
    return (
        CandidateLaw(
            law_id="record_window_separation_order",
            description=(
                "Each record has an open endpoint and a finalized endpoint in a "
                "finality-domain window. Declare x<y only when x finalizes "
                "before y opens."
            ),
            finality_domain_law=True,
            new_relative_to_t532=True,
            law_declared_before_sampling=True,
            independent_density_reason=True,
            sample_family_predeclared=True,
            hostile_controls_named=True,
            later_burdens_named=True,
        ),
    )


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="all_windows_overlap_control",
            comparability_density=Fraction(0, 1),
            clears_source_law_gate=False,
            reason="If every record window overlaps, the law yields no comparabilities.",
        ),
        HostileControl(
            control_id="zero_duration_chain_control",
            comparability_density=Fraction(1, 1),
            clears_source_law_gate=False,
            reason=(
                "If every window collapses to a point in one stream, the law "
                "collapses to a one-channel chain control."
            ),
        ),
    )


def _evaluate_candidate(
    candidate: CandidateLaw,
    *,
    endpoint_patterns: tuple[EndpointPattern, ...],
) -> CandidateDecision:
    missing = _missing_requirements(candidate)
    expected = (
        record_window_expected_density()
        if candidate.law_id == "record_window_separation_order"
        else None
    )
    if candidate.requests_s1_claim_canon_public_or_external_movement:
        outcome = "FALSIFIED"
        clears = False
        reason = "Posture or external movement is forbidden for a TAF9 router."
    elif (
        candidate.imports_lorentzian_reference
        or candidate.conditions_on_t528_or_t530_screen
        or candidate.post_hoc_band_fit
        or candidate.uses_receipt_product_order
    ):
        outcome = "FALSIFIED"
        clears = False
        reason = "The candidate uses a route T534 explicitly excludes."
    elif missing:
        outcome = "FALSIFIED"
        clears = False
        reason = "The candidate lacks one or more source-law requirements."
    elif expected != TARGET_COMPARABILITY_DENSITY:
        outcome = "NARROWED"
        clears = False
        reason = (
            "The candidate is new and finality-domain native, but its exact "
            f"comparability density is {expected}, not the target "
            f"{TARGET_COMPARABILITY_DENSITY}."
        )
    else:
        outcome = "CLEARED"
        clears = True
        reason = (
            "The candidate clears the T534 source-law density gate. This is not "
            "S1 evidence, and later execution, locality, covariance, embedding, "
            "and continuum burdens still remain."
        )
    return CandidateDecision(
        law_id=candidate.law_id,
        outcome=outcome,
        clears_source_law_gate=clears,
        counts_as_s1_evidence=False,
        expected_comparability_density=expected,
        target_comparability_density=TARGET_COMPARABILITY_DENSITY,
        missing_requirements=missing,
        reason=reason,
        deterministic_evidence=_deterministic_evidence(endpoint_patterns, expected),
    )


def _missing_requirements(candidate: CandidateLaw) -> tuple[str, ...]:
    missing: list[str] = []
    if not candidate.finality_domain_law:
        missing.append("finality_domain_law")
    if not candidate.new_relative_to_t532:
        missing.append("new_relative_to_t532")
    if not candidate.law_declared_before_sampling:
        missing.append("law_declared_before_sampling")
    if not candidate.independent_density_reason:
        missing.append("independent_comparability_density_reason")
    if not candidate.sample_family_predeclared:
        missing.append("sample_family_predeclared")
    if not candidate.hostile_controls_named:
        missing.append("hostile_controls_named")
    if not candidate.later_burdens_named:
        missing.append("later_lorentzian_locality_covariance_embedding_burdens_named")
    if candidate.uses_receipt_product_order:
        missing.append("no_receipt_product_order")
    if candidate.imports_lorentzian_reference:
        missing.append("no_lorentzian_reference_import")
    if candidate.conditions_on_t528_or_t530_screen:
        missing.append("no_t528_or_t530_screen_conditioning")
    if candidate.post_hoc_band_fit:
        missing.append("no_post_hoc_band_fit")
    if candidate.requests_s1_claim_canon_public_or_external_movement:
        missing.append("no_s1_claim_canon_public_or_external_movement")
    return tuple(missing)


def _candidate_menu_excludes_forbidden(candidates: tuple[CandidateLaw, ...]) -> bool:
    candidate_ids = {candidate.law_id for candidate in candidates}
    return not (candidate_ids & set(EXCLUDED_LAW_IDS)) and all(
        not candidate.uses_receipt_product_order
        and not candidate.imports_lorentzian_reference
        and not candidate.conditions_on_t528_or_t530_screen
        and not candidate.post_hoc_band_fit
        for candidate in candidates
    )


def _deterministic_evidence(
    endpoint_patterns: tuple[EndpointPattern, ...],
    expected: Fraction | None,
) -> str:
    comparable = sum(pattern.relation != "incomparable" for pattern in endpoint_patterns)
    return (
        "Exact endpoint-order enumeration for two finality windows gives "
        f"{comparable}/{len(endpoint_patterns)} comparable patterns, so the "
        f"expected comparability density is {expected}."
    )


def _claim_labels(
    decisions: tuple[CandidateDecision, ...],
    endpoint_patterns: tuple[EndpointPattern, ...],
) -> tuple[ClaimLabel, ...]:
    cleared = tuple(decision for decision in decisions if decision.clears_source_law_gate)
    comparable = sum(pattern.relation != "incomparable" for pattern in endpoint_patterns)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The T534 candidate menu excludes the T532-negative receipt "
                "products, Lorentzian target import, T528/T530 screen "
                "conditioning, and post-hoc band fitting."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The record-window separation law has exact endpoint-pattern "
                f"density {comparable}/{len(endpoint_patterns)} = "
                f"{record_window_expected_density()}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"No new source law clears in T534: {len(cleared)} cleared.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The record-window separation law is finality-domain native "
                "because it uses only record opening and finalization endpoints, "
                "not target spacetime coordinates."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=PAUSE_READING,
        ),
    )


def _fraction_to_dict(value: Fraction | None) -> dict[str, object] | None:
    if value is None:
        return None
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


def _decision_to_dict(decision: CandidateDecision) -> dict[str, Any]:
    return {
        "law_id": decision.law_id,
        "outcome": decision.outcome,
        "clears_source_law_gate": decision.clears_source_law_gate,
        "counts_as_s1_evidence": decision.counts_as_s1_evidence,
        "expected_comparability_density": _fraction_to_dict(
            decision.expected_comparability_density
        ),
        "target_comparability_density": _fraction_to_dict(
            decision.target_comparability_density
        ),
        "missing_requirements": list(decision.missing_requirements),
        "reason": decision.reason,
        "deterministic_evidence": decision.deterministic_evidence,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T534 Results: New Finality-Domain Law Pause Router",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Route outcome: `{payload['route_outcome']}`",
        f"- Source T532 verdict: `{payload['source_t532_verdict']}`",
        "- Source T532 cleared candidate ids: "
        + (", ".join(f"`{item}`" for item in payload["source_t532_cleared_candidate_ids"]) or "none"),
        "- Candidate menu ids: "
        + (", ".join(f"`{item}`" for item in payload["candidate_menu_ids"]) or "none"),
        "- Cleared new source-law ids: "
        + (", ".join(f"`{item}`" for item in payload["cleared_candidate_ids"]) or "none"),
        "- Target comparability density: "
        f"{payload['target_comparability_density']['fraction']}",
        "",
        "## Excluded From Candidate Menu",
        "",
    ]
    lines.extend(f"- `{law_id}`" for law_id in payload["excluded_law_ids"])
    lines.extend(
        [
            "",
            "## Candidate Decisions",
            "",
            "| candidate | outcome | clears source-law gate? | S1 evidence? | expected density | missing requirements | reason |",
            "| --- | --- | :---: | :---: | --- | --- | --- |",
        ]
    )
    for decision in payload["candidate_decisions"]:
        expected = decision["expected_comparability_density"]
        expected_text = "none" if expected is None else expected["fraction"]
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['law_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['clears_source_law_gate']} | "
            f"{decision['counts_as_s1_evidence']} | "
            f"{expected_text} | "
            f"{missing} | "
            f"{decision['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Exact Endpoint Enumeration",
            "",
            "| pattern | A endpoints | B endpoints | relation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for pattern in payload["endpoint_patterns"]:
        lines.append(
            "| "
            f"`{pattern['pattern_id']}` | "
            f"{tuple(pattern['a_positions'])} | "
            f"{tuple(pattern['b_positions'])} | "
            f"`{pattern['relation']}` |"
        )
    lines.extend(
        [
            "",
            "## Hostile Controls",
            "",
            "| control | density | clears? | reason |",
            "| --- | ---: | :---: | --- |",
        ]
    )
    for control in payload["hostile_controls"]:
        lines.append(
            "| "
            f"`{control['control_id']}` | "
            f"{control['comparability_density']['fraction']} | "
            f"{control['clears_source_law_gate']} | "
            f"{control['reason']} |"
        )
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Strongest Reading", "strongest_reading"),
        ("Recommended Next", "recommended_next"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = t534_result_to_dict(run_t534_analysis())
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T534-new-finality-domain-law-pause-router-v0.1.json"
        md_path = results_dir / "T534-new-finality-domain-law-pause-router-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
