"""T531: pre-execution contract for the next S1 ordering-fraction packet.

T530 admitted one future packet shape: a predeclared finality-native
ordering-fraction measure law with independent naturality and hostile controls.
T531 makes that shape executable as an admission contract. It does not sample a
new generator, repair T528, or move S1.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


ARTIFACT = "T531-ordering-fraction-measure-law-contract-v0.1"
VERDICT = "ordering_fraction_measure_law_contract_built_review_only"
ADMITTED_PACKET_ID = "predeclared_finality_native_ordering_measure_law_contract"
SOURCE_ADMITTED_PACKET_ID = "predeclared_ordering_fraction_measure_law"
SOURCE_RESULTS_JSON = Path("results/T530-t528-generator-failure-router-v0.1.json")

REQUIRED_CONTRACT_TERMS = (
    "law_declared_before_sampling",
    "finality_native_observable",
    "directly_targets_ordering_fraction",
    "independent_naturality_or_neighbor_theory",
    "hostile_controls_named",
    "hostile_controls_independent_of_screen",
    "sample_family_predeclared",
    "later_lorentzian_locality_covariance_embedding_burdens_named",
    "no_lorentzian_reference_import",
    "no_t528_screen_conditioning",
    "no_s1_claim_canon_public_or_external_movement",
)

NOT_CLAIMED = (
    "T531 does not run a generator, produce S1 evidence, repair T528, reverse "
    "T223, establish a finality-native sprinkling law, derive spacetime, change "
    "claim status, change canon, change public posture, authorize external "
    "publication, or support cross-repo truth."
)


@dataclass(frozen=True)
class MeasureLawPacket:
    packet_id: str
    description: str
    law_declared_before_sampling: bool
    finality_native_observable: bool
    directly_targets_ordering_fraction: bool
    independent_naturality_or_neighbor_theory: bool
    hostile_controls_named: bool
    hostile_controls_independent_of_screen: bool
    sample_family_predeclared: bool
    later_burdens_named: bool
    imports_lorentzian_reference: bool = False
    conditions_on_t528_screen: bool = False
    requests_s1_claim_canon_public_or_external_movement: bool = False


@dataclass(frozen=True)
class PacketDecision:
    packet_id: str
    classification: str
    admitted_as_pre_execution_contract: bool
    counts_as_s1_evidence: bool
    action: str
    missing_requirements: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class SourceRoute:
    artifact: str
    verdict: str
    primary_failure_axis: str
    admitted_packet_ids: tuple[str, ...]


@dataclass(frozen=True)
class T531Result:
    artifact: str
    source_artifact: str
    source_verdict: str
    source_primary_failure_axis: str
    source_admitted_packet_id: str
    required_contract_terms: tuple[str, ...]
    packet_decisions: tuple[PacketDecision, ...]
    admitted_packet_ids: tuple[str, ...]
    rejected_or_blocked_packet_ids: tuple[str, ...]
    verdict: str
    strongest_reading: str
    recommended_next: str
    s1_update: str
    claim_ledger_update: str
    not_claimed: str


def run_t531_analysis() -> T531Result:
    source = _load_t530_route()
    decisions = tuple(_evaluate_packet(packet) for packet in _candidate_packets())
    admitted = tuple(
        decision.packet_id
        for decision in decisions
        if decision.admitted_as_pre_execution_contract
    )
    rejected_or_blocked = tuple(
        decision.packet_id
        for decision in decisions
        if not decision.admitted_as_pre_execution_contract
    )
    verdict = (
        VERDICT
        if source.primary_failure_axis == "ordering_fraction"
        and source.admitted_packet_ids == (SOURCE_ADMITTED_PACKET_ID,)
        and admitted == (ADMITTED_PACKET_ID,)
        and all(not decision.counts_as_s1_evidence for decision in decisions)
        else "ordering_fraction_measure_law_contract_unexpected_status"
    )
    return T531Result(
        artifact=ARTIFACT,
        source_artifact=source.artifact,
        source_verdict=source.verdict,
        source_primary_failure_axis=source.primary_failure_axis,
        source_admitted_packet_id=(
            source.admitted_packet_ids[0] if source.admitted_packet_ids else "none"
        ),
        required_contract_terms=REQUIRED_CONTRACT_TERMS,
        packet_decisions=decisions,
        admitted_packet_ids=admitted,
        rejected_or_blocked_packet_ids=rejected_or_blocked,
        verdict=verdict,
        strongest_reading=(
            "The next S1-facing packet cannot be a better-looking sample set. "
            "It must first be a declared law contract: the ordering-fraction "
            "observable, sampling family, naturality story, hostile controls, "
            "and later Lorentzian/locality/covariance/embedding burdens are "
            "fixed before any generator result is read."
        ),
        recommended_next=(
            "A later run may instantiate the admitted contract with an actual "
            "law and samples. That run should fail closed if the law is tuned "
            "from T528/T530 outcomes, imports a Lorentzian reference, lacks "
            "independent naturality, or requests S1/claim/canon/public-posture "
            "movement from the contract or a finite pass alone."
        ),
        s1_update=(
            "S1 remains `requires_added_assumption`. T531 only builds the "
            "pre-execution admission contract for the next review packet."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T531 is test-registry routing "
            "infrastructure only: no claim row, no S1 status movement, and no "
            "T223 reversal."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t531_result_to_dict(result: T531Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_artifact": result.source_artifact,
        "source_verdict": result.source_verdict,
        "source_primary_failure_axis": result.source_primary_failure_axis,
        "source_admitted_packet_id": result.source_admitted_packet_id,
        "required_contract_terms": list(result.required_contract_terms),
        "packet_decisions": [
            _decision_to_dict(decision) for decision in result.packet_decisions
        ],
        "admitted_packet_ids": list(result.admitted_packet_ids),
        "rejected_or_blocked_packet_ids": list(result.rejected_or_blocked_packet_ids),
        "verdict": result.verdict,
        "strongest_reading": result.strongest_reading,
        "recommended_next": result.recommended_next,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _load_t530_route() -> SourceRoute:
    payload = json.loads(SOURCE_RESULTS_JSON.read_text(encoding="utf-8"))
    admitted = tuple(
        decision["packet_id"]
        for decision in payload["packet_decisions"]
        if decision["admitted_as_future_review_target"]
    )
    return SourceRoute(
        artifact=payload["artifact"],
        verdict=payload["verdict"],
        primary_failure_axis=payload["primary_failure_axis"],
        admitted_packet_ids=admitted,
    )


def _candidate_packets() -> tuple[MeasureLawPacket, ...]:
    return (
        MeasureLawPacket(
            packet_id="posthoc_ordering_band_fit",
            description=(
                "Fit a measure law after inspecting which T528/T530 samples "
                "missed the repaired ordering-fraction band."
            ),
            law_declared_before_sampling=False,
            finality_native_observable=True,
            directly_targets_ordering_fraction=True,
            independent_naturality_or_neighbor_theory=False,
            hostile_controls_named=False,
            hostile_controls_independent_of_screen=False,
            sample_family_predeclared=False,
            later_burdens_named=True,
            conditions_on_t528_screen=True,
        ),
        MeasureLawPacket(
            packet_id="lorentzian_ordering_fraction_reference",
            description=(
                "Reuse an external 1+1 Lorentzian reference law as the source "
                "of the ordering-fraction target."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=False,
            directly_targets_ordering_fraction=True,
            independent_naturality_or_neighbor_theory=True,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
            imports_lorentzian_reference=True,
        ),
        MeasureLawPacket(
            packet_id="height_first_secondary_repair",
            description=(
                "Build a packet around T530's secondary height failures while "
                "leaving the primary ordering-fraction axis untreated."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=True,
            directly_targets_ordering_fraction=False,
            independent_naturality_or_neighbor_theory=True,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
        ),
        MeasureLawPacket(
            packet_id="ordering_fraction_no_naturality",
            description=(
                "Declare an ordering-fraction law but supply no independent "
                "reason it is natural outside the repaired-suite screen."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=True,
            directly_targets_ordering_fraction=True,
            independent_naturality_or_neighbor_theory=False,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
        ),
        MeasureLawPacket(
            packet_id=ADMITTED_PACKET_ID,
            description=(
                "Declare a finality-native ordering-fraction observable and "
                "measure law before sampling, with independent naturality, "
                "predeclared samples, hostile controls, and later burdens named."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=True,
            directly_targets_ordering_fraction=True,
            independent_naturality_or_neighbor_theory=True,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
        ),
        MeasureLawPacket(
            packet_id="s1_promotion_from_contract",
            description=(
                "Use a pre-execution contract, or a finite pass under it, as a "
                "request to move S1, claims, canon, or public posture."
            ),
            law_declared_before_sampling=True,
            finality_native_observable=True,
            directly_targets_ordering_fraction=True,
            independent_naturality_or_neighbor_theory=True,
            hostile_controls_named=True,
            hostile_controls_independent_of_screen=True,
            sample_family_predeclared=True,
            later_burdens_named=True,
            requests_s1_claim_canon_public_or_external_movement=True,
        ),
    )


def _evaluate_packet(packet: MeasureLawPacket) -> PacketDecision:
    missing = _missing_requirements(packet)
    if packet.requests_s1_claim_canon_public_or_external_movement:
        classification = "blocked_posture_or_external_movement_shortcut"
        admitted = False
        action = "stop"
        reason = "A pre-execution contract cannot move S1, claims, canon, public posture, or external state."
    elif packet.imports_lorentzian_reference:
        classification = "rejected_lorentzian_reference_import"
        admitted = False
        action = "reject"
        reason = "The packet imports the target spacetime reference law."
    elif packet.conditions_on_t528_screen or not packet.law_declared_before_sampling:
        classification = "rejected_screen_conditioned_measure_law"
        admitted = False
        action = "reject"
        reason = "The packet derives or tunes the law from the diagnostic screen."
    elif not packet.directly_targets_ordering_fraction:
        classification = "rejected_primary_axis_not_addressed"
        admitted = False
        action = "reject"
        reason = "The packet does not address T530's primary failure axis."
    elif missing:
        classification = "rejected_missing_contract_requirements"
        admitted = False
        action = "revise_before_execution"
        reason = "The packet targets the right axis but lacks the full contract."
    else:
        classification = "admitted_pre_execution_review_contract"
        admitted = True
        action = "future_execution_review_only"
        reason = (
            "The packet shape can be instantiated in a later run, but this "
            "contract creates no generator success or S1 evidence."
        )
    return PacketDecision(
        packet_id=packet.packet_id,
        classification=classification,
        admitted_as_pre_execution_contract=admitted,
        counts_as_s1_evidence=False,
        action=action,
        missing_requirements=missing,
        reason=reason,
    )


def _missing_requirements(packet: MeasureLawPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.law_declared_before_sampling:
        missing.append("law_declared_before_sampling")
    if not packet.finality_native_observable:
        missing.append("finality_native_observable")
    if not packet.directly_targets_ordering_fraction:
        missing.append("directly_targets_ordering_fraction")
    if not packet.independent_naturality_or_neighbor_theory:
        missing.append("independent_naturality_or_neighbor_theory")
    if not packet.hostile_controls_named:
        missing.append("hostile_controls_named")
    if not packet.hostile_controls_independent_of_screen:
        missing.append("hostile_controls_independent_of_screen")
    if not packet.sample_family_predeclared:
        missing.append("sample_family_predeclared")
    if not packet.later_burdens_named:
        missing.append("later_lorentzian_locality_covariance_embedding_burdens_named")
    if packet.imports_lorentzian_reference:
        missing.append("no_lorentzian_reference_import")
    if packet.conditions_on_t528_screen:
        missing.append("no_t528_screen_conditioning")
    if packet.requests_s1_claim_canon_public_or_external_movement:
        missing.append("no_s1_claim_canon_public_or_external_movement")
    return tuple(missing)


def _decision_to_dict(decision: PacketDecision) -> dict[str, Any]:
    return {
        "packet_id": decision.packet_id,
        "classification": decision.classification,
        "admitted_as_pre_execution_contract": decision.admitted_as_pre_execution_contract,
        "counts_as_s1_evidence": decision.counts_as_s1_evidence,
        "action": decision.action,
        "missing_requirements": list(decision.missing_requirements),
        "reason": decision.reason,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t531_result_to_dict(run_t531_analysis()), indent=2))
