"""T532: starter router for finality-native ordering-fraction laws.

T531 admitted a future packet shape: a predeclared finality-native
ordering-fraction measure law with independent naturality and hostile controls.
T532 instantiates the smallest honest router for that lane. It does not try to
solve S1. It distinguishes independently motivated finality-receipt candidates
from target imports, screen conditioning, and post-hoc band fitting, while
preserving the current negative evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.t528_s1_finality_native_generator_preflight import run_t528_analysis
from models.t530_t528_generator_failure_router import run_t530_analysis
from models.t531_ordering_fraction_measure_law_contract import (
    ADMITTED_PACKET_ID as T531_ADMITTED_PACKET_ID,
    VERDICT as T531_VERDICT,
    run_t531_analysis,
)


ARTIFACT = "T532-finality-native-ordering-fraction-law-starter-v0.1"
VERDICT = "no_real_ordering_fraction_law_candidate_clears_starter_router"

NOT_CLAIMED = (
    "T532 does not derive spacetime, prove manifoldlikeness, establish a "
    "finality-native sprinkling law, repair T528, reverse T223, promote S1, "
    "change claim status, change canon, change public posture, authorize "
    "external publication, or support cross-repo truth. It is only a starter "
    "router for T531 candidate law shapes."
)


@dataclass(frozen=True)
class CandidateLaw:
    law_id: str
    description: str
    law_declared_before_sampling: bool
    finality_native_observable: bool
    directly_targets_ordering_fraction: bool
    independent_naturality: bool
    hostile_controls_named: bool
    hostile_controls_independent_of_screen: bool
    sample_family_predeclared: bool
    later_burdens_named: bool
    imports_lorentzian_reference: bool = False
    conditions_on_t528_screen: bool = False
    post_hoc_band_fit: bool = False
    requests_s1_or_claim_movement: bool = False
    receipt_channel_count: int | None = None
    executed_t528_packet: bool = False


@dataclass(frozen=True)
class CandidateDecision:
    law_id: str
    classification: str
    action: str
    independent_naturality_candidate: bool
    clears_t531_contract_terms: bool
    clears_as_real_candidate: bool
    counts_as_s1_evidence: bool
    expected_ordering_fraction: Fraction | None
    deterministic_evidence: str
    missing_requirements: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    status: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T532Result:
    artifact: str
    source_t531_verdict: str
    source_t531_admitted_packet_ids: tuple[str, ...]
    source_t530_primary_failure_axis: str
    source_t528_pass_count: int
    source_t528_sample_count: int
    source_t528_ordering_failure_count: int
    candidate_decisions: tuple[CandidateDecision, ...]
    independent_naturality_candidate_ids: tuple[str, ...]
    cleared_candidate_ids: tuple[str, ...]
    rejected_or_negative_candidate_ids: tuple[str, ...]
    verdict: str
    strongest_reading: str
    recommended_next: str
    claim_labels: tuple[ClaimLabel, ...]
    s1_update: str
    claim_ledger_update: str
    not_claimed: str


def run_t532_analysis() -> T532Result:
    t528 = run_t528_analysis()
    t530 = run_t530_analysis()
    t531 = run_t531_analysis()
    ordering_failure_count = _ordering_failure_count(t528)
    decisions = tuple(
        _evaluate_candidate(
            candidate,
            t528_pass_count=t528.pass_count,
            t528_sample_count=t528.sample_count,
            ordering_failure_count=ordering_failure_count,
        )
        for candidate in _candidate_laws()
    )
    independent_ids = tuple(
        decision.law_id
        for decision in decisions
        if decision.independent_naturality_candidate
    )
    cleared = tuple(
        decision.law_id for decision in decisions if decision.clears_as_real_candidate
    )
    negative = tuple(
        decision.law_id for decision in decisions if not decision.clears_as_real_candidate
    )
    verdict = (
        VERDICT
        if t531.verdict == T531_VERDICT
        and t531.admitted_packet_ids == (T531_ADMITTED_PACKET_ID,)
        and t530.primary_failure_axis == "ordering_fraction"
        and t528.pass_count == 25
        and t528.sample_count == 32
        and ordering_failure_count == 6
        and not cleared
        and all(not decision.counts_as_s1_evidence for decision in decisions)
        else "ordering_fraction_law_starter_router_unexpected_status"
    )
    result = T532Result(
        artifact=ARTIFACT,
        source_t531_verdict=t531.verdict,
        source_t531_admitted_packet_ids=t531.admitted_packet_ids,
        source_t530_primary_failure_axis=t530.primary_failure_axis,
        source_t528_pass_count=t528.pass_count,
        source_t528_sample_count=t528.sample_count,
        source_t528_ordering_failure_count=ordering_failure_count,
        candidate_decisions=decisions,
        independent_naturality_candidate_ids=independent_ids,
        cleared_candidate_ids=cleared,
        rejected_or_negative_candidate_ids=negative,
        verdict=verdict,
        strongest_reading=(
            "The first TAF1 starter screen distinguishes independently natural "
            "receipt-product laws from bad shortcuts, but none currently clears "
            "as a real finality-native ordering-fraction law. The two-channel "
            "receipt law is the only executed finality-native candidate, and "
            "T528/T530 already record its negative ordering-fraction evidence."
        ),
        recommended_next=(
            "A next swing should either predeclare a new finality-domain law "
            "with an independent reason for its comparability density, or stop "
            "the S1 finite-generator route until such a law exists. Do not tune "
            "from the T525/T528 screen and do not import the Lorentzian reference "
            "as the source law."
        ),
        claim_labels=_claim_labels(decisions, ordering_failure_count),
        s1_update=(
            "S1 remains `requires_added_assumption`. T532 reports no real "
            "candidate clearing the T531 starter router."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T532 is a starter artifact with "
            "negative routing evidence only: no claim row, no S1 status movement, "
            "and no T223 reversal."
        ),
        not_claimed=NOT_CLAIMED,
    )
    return result


def t532_result_to_dict(result: T532Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t531_verdict": result.source_t531_verdict,
        "source_t531_admitted_packet_ids": list(result.source_t531_admitted_packet_ids),
        "source_t530_primary_failure_axis": result.source_t530_primary_failure_axis,
        "source_t528_pass_count": result.source_t528_pass_count,
        "source_t528_sample_count": result.source_t528_sample_count,
        "source_t528_ordering_failure_count": result.source_t528_ordering_failure_count,
        "candidate_decisions": [
            _decision_to_dict(decision) for decision in result.candidate_decisions
        ],
        "independent_naturality_candidate_ids": list(
            result.independent_naturality_candidate_ids
        ),
        "cleared_candidate_ids": list(result.cleared_candidate_ids),
        "rejected_or_negative_candidate_ids": list(
            result.rejected_or_negative_candidate_ids
        ),
        "verdict": result.verdict,
        "strongest_reading": result.strongest_reading,
        "recommended_next": result.recommended_next,
        "claim_labels": [_claim_to_dict(claim) for claim in result.claim_labels],
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _candidate_laws() -> tuple[CandidateLaw, ...]:
    return (
        CandidateLaw(
            law_id="two_channel_receipt_product_order",
            description=(
                "Use two independent local finality receipt streams. Declare "
                "x<y iff both streams place x before y."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=True,
            directly_targets_ordering_fraction=True,
            independent_naturality=True,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
            receipt_channel_count=2,
            executed_t528_packet=True,
        ),
        CandidateLaw(
            law_id="three_channel_receipt_product_order",
            description=(
                "Use three independent local finality receipt streams and "
                "require unanimous receipt-order agreement."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=True,
            directly_targets_ordering_fraction=True,
            independent_naturality=True,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
            receipt_channel_count=3,
        ),
        CandidateLaw(
            law_id="external_lorentzian_uv_reference_law",
            description=(
                "Use independent u/v light-cone coordinates as the ordering "
                "law, as in the T526 calibration reference."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=False,
            directly_targets_ordering_fraction=True,
            independent_naturality=True,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
            imports_lorentzian_reference=True,
        ),
        CandidateLaw(
            law_id="t528_screen_conditioned_receipt_mixture",
            description=(
                "Choose receipt-channel mixtures after reading which T528 "
                "samples missed the repaired ordering-fraction band."
            ),
            law_declared_before_sampling=False,
            finality_native_observable=True,
            directly_targets_ordering_fraction=True,
            independent_naturality=False,
            hostile_controls_named=False,
            hostile_controls_independent_of_screen=False,
            sample_family_predeclared=False,
            later_burdens_named=True,
            conditions_on_t528_screen=True,
        ),
        CandidateLaw(
            law_id="posthoc_repaired_band_fit",
            description=(
                "Define the law as the empirical repaired-suite ordering band "
                "and then sample only survivors."
            ),
            law_declared_before_sampling=False,
            finality_native_observable=False,
            directly_targets_ordering_fraction=True,
            independent_naturality=False,
            hostile_controls_named=False,
            hostile_controls_independent_of_screen=False,
            sample_family_predeclared=False,
            later_burdens_named=False,
            conditions_on_t528_screen=True,
            post_hoc_band_fit=True,
        ),
        CandidateLaw(
            law_id="s1_promotion_from_starter_screen",
            description=(
                "Treat a starter-router pass as a reason to move S1, claims, "
                "canon, or public posture."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=True,
            directly_targets_ordering_fraction=True,
            independent_naturality=True,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
            requests_s1_or_claim_movement=True,
        ),
    )


def _evaluate_candidate(
    candidate: CandidateLaw,
    *,
    t528_pass_count: int,
    t528_sample_count: int,
    ordering_failure_count: int,
) -> CandidateDecision:
    missing = _missing_requirements(candidate)
    clears_contract = not missing
    expected = _expected_ordering_fraction(candidate.receipt_channel_count)

    if candidate.requests_s1_or_claim_movement:
        classification = "blocked_governance_or_posture_shortcut"
        action = "stop"
        clears_real = False
        reason = "A starter router cannot move S1, claims, canon, public posture, or external state."
    elif candidate.imports_lorentzian_reference:
        classification = "rejected_target_import"
        action = "reject"
        clears_real = False
        reason = "The candidate imports the target Lorentzian reference law."
    elif candidate.post_hoc_band_fit:
        classification = "rejected_post_hoc_band_fit"
        action = "reject"
        clears_real = False
        reason = "The candidate defines the law from the repaired-screen band."
    elif candidate.conditions_on_t528_screen:
        classification = "rejected_screen_conditioned_law"
        action = "reject"
        clears_real = False
        reason = "The candidate is tuned from the diagnostic it must clear."
    elif not clears_contract:
        classification = "rejected_missing_t531_requirements"
        action = "revise_before_review"
        clears_real = False
        reason = "The candidate lacks one or more T531 starter requirements."
    elif candidate.executed_t528_packet and t528_pass_count < t528_sample_count:
        classification = "negative_independent_naturality_candidate"
        action = "preserve_negative_result"
        clears_real = False
        reason = (
            "The law is independently motivated, but the executed T528 packet "
            f"passed only {t528_pass_count}/{t528_sample_count} samples and "
            f"had {ordering_failure_count} ordering-fraction failures."
        )
    elif expected is not None and expected != Fraction(1, 2):
        classification = "negative_expected_density_mismatch"
        action = "preserve_negative_result"
        clears_real = False
        reason = (
            "The law is independently motivated, but its exchangeable receipt "
            f"model has expected ordering fraction {expected}, not the "
            "T530 primary ordering-fraction target neighborhood."
        )
    else:
        classification = "review_only_unexecuted_candidate"
        action = "future_execution_required"
        clears_real = False
        reason = (
            "The candidate clears the starter contract but has no sufficient "
            "deterministic execution evidence in this artifact."
        )

    return CandidateDecision(
        law_id=candidate.law_id,
        classification=classification,
        action=action,
        independent_naturality_candidate=(
            candidate.independent_naturality
            and candidate.finality_native_observable
            and not candidate.imports_lorentzian_reference
            and not candidate.conditions_on_t528_screen
            and not candidate.post_hoc_band_fit
            and not candidate.requests_s1_or_claim_movement
        ),
        clears_t531_contract_terms=clears_contract,
        clears_as_real_candidate=clears_real,
        counts_as_s1_evidence=False,
        expected_ordering_fraction=expected,
        deterministic_evidence=_deterministic_evidence(
            candidate,
            expected=expected,
            t528_pass_count=t528_pass_count,
            t528_sample_count=t528_sample_count,
            ordering_failure_count=ordering_failure_count,
        ),
        missing_requirements=missing,
        reason=reason,
    )


def _missing_requirements(candidate: CandidateLaw) -> tuple[str, ...]:
    missing: list[str] = []
    if not candidate.law_declared_before_sampling:
        missing.append("law_declared_before_sampling")
    if not candidate.finality_native_observable:
        missing.append("finality_native_observable")
    if not candidate.directly_targets_ordering_fraction:
        missing.append("directly_targets_ordering_fraction")
    if not candidate.independent_naturality:
        missing.append("independent_naturality_or_neighbor_theory")
    if not candidate.hostile_controls_named:
        missing.append("hostile_controls_named")
    if not candidate.hostile_controls_independent_of_screen:
        missing.append("hostile_controls_independent_of_screen")
    if not candidate.sample_family_predeclared:
        missing.append("sample_family_predeclared")
    if not candidate.later_burdens_named:
        missing.append("later_lorentzian_locality_covariance_embedding_burdens_named")
    if candidate.imports_lorentzian_reference:
        missing.append("no_lorentzian_reference_import")
    if candidate.conditions_on_t528_screen:
        missing.append("no_t528_screen_conditioning")
    if candidate.post_hoc_band_fit:
        missing.append("no_post_hoc_band_fit")
    if candidate.requests_s1_or_claim_movement:
        missing.append("no_s1_claim_canon_public_or_external_movement")
    return tuple(missing)


def _expected_ordering_fraction(receipt_channel_count: int | None) -> Fraction | None:
    if receipt_channel_count is None:
        return None
    if receipt_channel_count < 1:
        raise ValueError("receipt_channel_count must be positive")
    return Fraction(1, 2 ** (receipt_channel_count - 1))


def _ordering_failure_count(t528: Any) -> int:
    return sum(
        not audit.ordering_fraction_in_band
        for audit in t528.sample_audits
        if not audit.repaired_suite_passed
    )


def _deterministic_evidence(
    candidate: CandidateLaw,
    *,
    expected: Fraction | None,
    t528_pass_count: int,
    t528_sample_count: int,
    ordering_failure_count: int,
) -> str:
    if candidate.executed_t528_packet:
        return (
            f"T528 executed this law shape: {t528_pass_count}/{t528_sample_count} "
            f"samples passed, with {ordering_failure_count} failed samples "
            "missing the ordering-fraction band."
        )
    if expected is not None:
        return (
            "Exchangeable receipt-product calculation gives expected ordering "
            f"fraction {expected}."
        )
    if candidate.imports_lorentzian_reference:
        return "T526 identifies this as an external Lorentzian calibration law."
    if candidate.conditions_on_t528_screen or candidate.post_hoc_band_fit:
        return "The candidate is defined from the repaired diagnostic screen."
    if candidate.requests_s1_or_claim_movement:
        return "The candidate requests forbidden posture movement."
    return "No deterministic execution evidence is supplied by T532."


def _claim_labels(
    decisions: tuple[CandidateDecision, ...],
    ordering_failure_count: int,
) -> tuple[ClaimLabel, ...]:
    cleared = tuple(decision for decision in decisions if decision.clears_as_real_candidate)
    independent = tuple(
        decision for decision in decisions if decision.independent_naturality_candidate
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            status="high",
            confidence="high",
            text=(
                "T531's admitted route is preserved and T530's primary failure "
                "axis remains ordering_fraction."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            status="high",
            confidence="high",
            text=(
                "The executed two-channel receipt candidate preserves T528's "
                f"negative result, including {ordering_failure_count} failed "
                "samples on the ordering-fraction axis."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            status="high",
            confidence="high",
            text=(
                "Target-import, screen-conditioned, post-hoc band-fit, and "
                "posture-movement candidates are rejected or blocked."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            status="high",
            confidence="high",
            text=(
                "No candidate clears as a real finality-native ordering-fraction "
                f"law candidate in this starter router: {len(cleared)} cleared."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            status="medium",
            confidence="medium",
            text=(
                "Receipt-product laws are independently natural starter "
                "candidates because they are stated in local finality-receipt "
                "order data and are invariant under event relabeling and "
                "monotone receipt-rank renaming."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            status="medium",
            confidence="medium",
            text=(
                "Independent naturality is not enough for S1-facing progress; "
                f"{len(independent)} independently natural starter candidates "
                "remain negative or review-only here."
            ),
        ),
    )


def _decision_to_dict(decision: CandidateDecision) -> dict[str, Any]:
    expected = decision.expected_ordering_fraction
    return {
        "law_id": decision.law_id,
        "classification": decision.classification,
        "action": decision.action,
        "independent_naturality_candidate": decision.independent_naturality_candidate,
        "clears_t531_contract_terms": decision.clears_t531_contract_terms,
        "clears_as_real_candidate": decision.clears_as_real_candidate,
        "counts_as_s1_evidence": decision.counts_as_s1_evidence,
        "expected_ordering_fraction": (
            None
            if expected is None
            else {"fraction": f"{expected.numerator}/{expected.denominator}", "float": float(expected)}
        ),
        "deterministic_evidence": decision.deterministic_evidence,
        "missing_requirements": list(decision.missing_requirements),
        "reason": decision.reason,
    }


def _claim_to_dict(claim: ClaimLabel) -> dict[str, str]:
    return {
        "label": claim.label,
        "status": claim.status,
        "confidence": claim.confidence,
        "text": claim.text,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t532_result_to_dict(run_t532_analysis()), indent=2))
