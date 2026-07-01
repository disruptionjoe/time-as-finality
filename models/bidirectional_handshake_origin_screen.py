"""T386: bidirectional-handshake origin screen.

T385 showed that a minimal round-trip handshake is the cleanest origin story
for exactly two primitive null compatibility-signal directions, but it left the
handshake premise open. T386 asks whether that premise follows from a sharper
meaning of compatibility:

* raw compatibility alone is still too weak;
* local mutual attestability forces a two-leg send/return witness under the
  declared finite constraints.

So this is not a raw compatibility derivation. It is a conditional derivation
from mutual local attestability, which becomes the next open object.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolCandidate:
    protocol_id: str
    imports_global_coordinator: bool
    local_pairwise_relation: bool
    directed_signal_legs: int
    endpoint_receipts: int
    mutual_attestability: bool
    round_trip_closure: bool
    directional_signal_geometry: bool
    nonnegative_source_counts: bool
    hidden_foliation: bool
    overcomplete_phases: bool
    description: str


@dataclass(frozen=True)
class ProtocolCriterion:
    criterion_id: str
    passes: bool
    reason: str


@dataclass(frozen=True)
class ProtocolVerdict:
    protocol_id: str
    status: str
    classification: str
    passes: bool
    criteria: tuple[ProtocolCriterion, ...]
    reason: str


@dataclass(frozen=True)
class DerivationStep:
    step_id: str
    statement: str
    dependency: str


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T386Result:
    minimal_bidirectional_handshake_unique_survivor: bool
    raw_compatibility_derives_handshake: bool
    mutual_attestability_derives_handshake: bool
    one_sided_readout_rejected: bool
    broadcast_without_ack_rejected: bool
    shared_scalar_token_rejected: bool
    global_reconciler_rejected: bool
    signed_anti_handshake_rejected: bool
    three_phase_commit_demoted: bool
    asymmetric_receipt_partial: bool
    conditional_origin_chain_to_two_null_basis: bool
    surviving_protocol_ids: tuple[str, ...]
    partial_protocol_ids: tuple[str, ...]
    demoted_protocol_ids: tuple[str, ...]
    rejected_protocol_ids: tuple[str, ...]
    derivation_steps: tuple[DerivationStep, ...]
    protocol_verdicts: tuple[ProtocolVerdict, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str
    next_open_object: str


def protocol_candidates() -> tuple[ProtocolCandidate, ...]:
    return (
        ProtocolCandidate(
            protocol_id="one_sided_readout",
            imports_global_coordinator=False,
            local_pairwise_relation=True,
            directed_signal_legs=1,
            endpoint_receipts=1,
            mutual_attestability=False,
            round_trip_closure=False,
            directional_signal_geometry=True,
            nonnegative_source_counts=True,
            hidden_foliation=False,
            overcomplete_phases=False,
            description="A observes B or receives from B, but B has no reciprocal local receipt.",
        ),
        ProtocolCandidate(
            protocol_id="broadcast_without_ack",
            imports_global_coordinator=False,
            local_pairwise_relation=False,
            directed_signal_legs=1,
            endpoint_receipts=1,
            mutual_attestability=False,
            round_trip_closure=False,
            directional_signal_geometry=True,
            nonnegative_source_counts=True,
            hidden_foliation=False,
            overcomplete_phases=False,
            description="A source broadcasts outward without pair-specific acknowledgment.",
        ),
        ProtocolCandidate(
            protocol_id="shared_scalar_token",
            imports_global_coordinator=False,
            local_pairwise_relation=True,
            directed_signal_legs=0,
            endpoint_receipts=2,
            mutual_attestability=True,
            round_trip_closure=False,
            directional_signal_geometry=False,
            nonnegative_source_counts=True,
            hidden_foliation=False,
            overcomplete_phases=False,
            description="Both endpoints share a scalar token, but no directed signal trace.",
        ),
        ProtocolCandidate(
            protocol_id="global_reconciler_receipt",
            imports_global_coordinator=True,
            local_pairwise_relation=False,
            directed_signal_legs=0,
            endpoint_receipts=2,
            mutual_attestability=True,
            round_trip_closure=True,
            directional_signal_geometry=False,
            nonnegative_source_counts=True,
            hidden_foliation=True,
            overcomplete_phases=False,
            description="A central reconciler records compatibility and issues receipts.",
        ),
        ProtocolCandidate(
            protocol_id="minimal_bidirectional_handshake",
            imports_global_coordinator=False,
            local_pairwise_relation=True,
            directed_signal_legs=2,
            endpoint_receipts=2,
            mutual_attestability=True,
            round_trip_closure=True,
            directional_signal_geometry=True,
            nonnegative_source_counts=True,
            hidden_foliation=False,
            overcomplete_phases=False,
            description="A local send/return witness where each endpoint can attest the pair relation.",
        ),
        ProtocolCandidate(
            protocol_id="three_phase_commit_handshake",
            imports_global_coordinator=False,
            local_pairwise_relation=True,
            directed_signal_legs=3,
            endpoint_receipts=2,
            mutual_attestability=True,
            round_trip_closure=True,
            directional_signal_geometry=True,
            nonnegative_source_counts=True,
            hidden_foliation=False,
            overcomplete_phases=True,
            description="Prepare/commit/ack protocol with an extra primitive phase.",
        ),
        ProtocolCandidate(
            protocol_id="signed_anti_handshake",
            imports_global_coordinator=False,
            local_pairwise_relation=True,
            directed_signal_legs=2,
            endpoint_receipts=2,
            mutual_attestability=True,
            round_trip_closure=True,
            directional_signal_geometry=True,
            nonnegative_source_counts=False,
            hidden_foliation=False,
            overcomplete_phases=False,
            description="Two-leg handshake represented through signed cancellation.",
        ),
        ProtocolCandidate(
            protocol_id="asymmetric_receipt_handshake",
            imports_global_coordinator=False,
            local_pairwise_relation=True,
            directed_signal_legs=2,
            endpoint_receipts=1,
            mutual_attestability=False,
            round_trip_closure=True,
            directional_signal_geometry=True,
            nonnegative_source_counts=True,
            hidden_foliation=False,
            overcomplete_phases=False,
            description="Two directed legs exist, but only one endpoint keeps a local attestable receipt.",
        ),
    )


def evaluate_protocol(candidate: ProtocolCandidate) -> ProtocolVerdict:
    criteria = (
        ProtocolCriterion(
            "no_global_coordinator",
            not candidate.imports_global_coordinator,
            "compatibility should not be certified by a central clock or reconciler",
        ),
        ProtocolCriterion(
            "local_pairwise_relation",
            candidate.local_pairwise_relation,
            "compatibility must be witnessed as a local relation between endpoints",
        ),
        ProtocolCriterion(
            "two_endpoint_receipts",
            candidate.endpoint_receipts == 2,
            "each endpoint must have a local receipt of the relation",
        ),
        ProtocolCriterion(
            "mutual_attestability",
            candidate.mutual_attestability,
            "each endpoint must be able to attest that the other side participates",
        ),
        ProtocolCriterion(
            "directional_signal_geometry",
            candidate.directional_signal_geometry,
            "a scalar token is not enough to define null signal directions",
        ),
        ProtocolCriterion(
            "round_trip_closure",
            candidate.round_trip_closure,
            "the witness must close a send/return loop for observer calibration",
        ),
        ProtocolCriterion(
            "exactly_two_directed_legs",
            candidate.directed_signal_legs == 2,
            "minimal mutual attestability needs one outgoing and one returning leg",
        ),
        ProtocolCriterion(
            "nonnegative_source_counts",
            candidate.nonnegative_source_counts,
            "source compatibility cannot use negative primitive count directions",
        ),
        ProtocolCriterion(
            "no_hidden_foliation",
            not candidate.hidden_foliation,
            "the protocol must not smuggle in a hidden global ordering layer",
        ),
        ProtocolCriterion(
            "minimal_not_overcomplete",
            not candidate.overcomplete_phases and candidate.directed_signal_legs == 2,
            "extra primitive phases must be absent or reducible to the two-leg handshake",
        ),
    )
    passes = all(criterion.passes for criterion in criteria)

    if passes:
        status = "minimal_bidirectional_handshake_survivor"
        classification = "survivor"
        reason = (
            "local mutual attestability with no global coordinator has the minimal "
            "two-leg send/return witness needed for round-trip calibration"
        )
    elif candidate.imports_global_coordinator or candidate.hidden_foliation:
        status = "rejected_global_reconciler"
        classification = "rejected"
        reason = "global reconciliation imports a hidden ordering/certification layer"
    elif not candidate.directional_signal_geometry:
        status = "rejected_no_signal_geometry"
        classification = "rejected"
        reason = "scalar or reconciler receipts do not supply directed signal geometry"
    elif not candidate.local_pairwise_relation:
        status = "rejected_not_pairwise_local"
        classification = "rejected"
        reason = "broadcast without pair-specific acknowledgment is not a local compatibility witness"
    elif not candidate.mutual_attestability:
        if candidate.directed_signal_legs == 2 and candidate.round_trip_closure:
            status = "partial_asymmetric_receipt"
            classification = "partial"
            reason = "two legs exist, but only one endpoint can locally attest the relation"
        else:
            status = "rejected_one_sided_attestation"
            classification = "rejected"
            reason = "one-sided readout cannot certify compatibility as mutual participation"
    elif not candidate.nonnegative_source_counts:
        status = "rejected_signed_counts"
        classification = "rejected"
        reason = "signed cancellation is not available to source-level compatibility counts"
    elif candidate.overcomplete_phases or candidate.directed_signal_legs > 2:
        status = "demoted_overcomplete_protocol"
        classification = "demoted"
        reason = "extra primitive phases exceed the minimal two-leg handshake"
    elif not candidate.round_trip_closure:
        status = "rejected_no_round_trip"
        classification = "rejected"
        reason = "without closure, the relation cannot support reciprocal calibration"
    else:
        status = "failed_handshake_origin_screen"
        classification = "rejected"
        reason = "candidate misses at least one handshake-origin criterion"

    return ProtocolVerdict(
        protocol_id=candidate.protocol_id,
        status=status,
        classification=classification,
        passes=passes,
        criteria=criteria,
        reason=reason,
    )


def evaluate_protocols() -> tuple[ProtocolVerdict, ...]:
    return tuple(evaluate_protocol(candidate) for candidate in protocol_candidates())


def derivation_steps() -> tuple[DerivationStep, ...]:
    return (
        DerivationStep(
            step_id="raw_compatibility_insufficient",
            statement=(
                "A bare compatible/incompatible relation does not decide whether the witness "
                "is scalar, one-way, global, or mutual."
            ),
            dependency="none",
        ),
        DerivationStep(
            step_id="mutual_attestability_requires_two_receipts",
            statement=(
                "If compatibility means each endpoint can locally attest the relation, "
                "then both endpoints need local receipts."
            ),
            dependency="mutual_local_attestability_semantics",
        ),
        DerivationStep(
            step_id="local_pairwise_no_global_reconciler_requires_signal_exchange",
            statement=(
                "Without a global reconciler, pairwise mutual receipts must be carried "
                "by local signal exchange between the endpoints."
            ),
            dependency="no_global_coordinator",
        ),
        DerivationStep(
            step_id="minimal_exchange_has_two_directed_legs",
            statement=(
                "The minimal exchange that lets both sides attest participation is one "
                "outgoing leg and one returning leg."
            ),
            dependency="minimality_and_nonnegative_source_counts",
        ),
        DerivationStep(
            step_id="two_legs_feed_t385_two_null_basis",
            statement=(
                "Under T385, a minimal two-leg round-trip handshake is the origin story "
                "for the two primitive null compatibility-signal directions."
            ),
            dependency="T385",
        ),
    )


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            comparator_id="raw_compatibility_derivation",
            status="still_not_earned",
            absorbs=True,
            reason=(
                "raw compatibility alone does not force mutual attestability rather than "
                "one-way, scalar, or global certification"
            ),
        ),
        ComparatorVerdict(
            comparator_id="mutual_attestability_semantics",
            status="conditional_derivation_supported",
            absorbs=False,
            reason=(
                "once compatibility is sharpened to local mutual attestability, the "
                "minimal two-leg handshake follows in the finite screen"
            ),
        ),
        ComparatorVerdict(
            comparator_id="global_reconciler_shortcut",
            status="rejected",
            absorbs=False,
            reason="central reconciliation is explicitly rejected as hidden global structure",
        ),
        ComparatorVerdict(
            comparator_id="protocol_catalog_completeness",
            status="still_absorbs",
            absorbs=True,
            reason="the screen covers targeted protocol semantics, not every possible protocol",
        ),
        ComparatorVerdict(
            comparator_id="mutual_attestability_origin",
            status="new_open_object",
            absorbs=True,
            reason="the screen does not derive why compatibility must mean mutual attestability",
        ),
    )


def run_t386_analysis() -> T386Result:
    verdicts = evaluate_protocols()
    by_id = {verdict.protocol_id: verdict for verdict in verdicts}
    survivors = tuple(verdict.protocol_id for verdict in verdicts if verdict.classification == "survivor")
    partials = tuple(verdict.protocol_id for verdict in verdicts if verdict.classification == "partial")
    demoted = tuple(verdict.protocol_id for verdict in verdicts if verdict.classification == "demoted")
    rejected = tuple(verdict.protocol_id for verdict in verdicts if verdict.classification == "rejected")
    return T386Result(
        minimal_bidirectional_handshake_unique_survivor=(
            survivors == ("minimal_bidirectional_handshake",)
        ),
        raw_compatibility_derives_handshake=False,
        mutual_attestability_derives_handshake=True,
        one_sided_readout_rejected=(
            by_id["one_sided_readout"].status == "rejected_one_sided_attestation"
        ),
        broadcast_without_ack_rejected=(
            by_id["broadcast_without_ack"].status == "rejected_not_pairwise_local"
        ),
        shared_scalar_token_rejected=(
            by_id["shared_scalar_token"].status == "rejected_no_signal_geometry"
        ),
        global_reconciler_rejected=(
            by_id["global_reconciler_receipt"].status == "rejected_global_reconciler"
        ),
        signed_anti_handshake_rejected=(
            by_id["signed_anti_handshake"].status == "rejected_signed_counts"
        ),
        three_phase_commit_demoted=(
            by_id["three_phase_commit_handshake"].status == "demoted_overcomplete_protocol"
        ),
        asymmetric_receipt_partial=(
            by_id["asymmetric_receipt_handshake"].status == "partial_asymmetric_receipt"
        ),
        conditional_origin_chain_to_two_null_basis=True,
        surviving_protocol_ids=survivors,
        partial_protocol_ids=partials,
        demoted_protocol_ids=demoted,
        rejected_protocol_ids=rejected,
        derivation_steps=derivation_steps(),
        protocol_verdicts=verdicts,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict=(
            "bidirectional_handshake_derived_from_mutual_attestability_not_raw_compatibility"
        ),
        strongest_claim=(
            "Raw compatibility still does not derive the handshake. But if compatibility "
            "means local mutual attestability with no global reconciler, nonnegative source "
            "counts, and minimality, then the minimal witness is a two-leg bidirectional "
            "handshake. Combined with T385, that conditionally grounds the two-null basis."
        ),
        claim_ledger_update=(
            "Register T386 as a conditional handshake-origin screen: handshake_origin is "
            "derived from mutual local attestability, while mutual_attestability_origin "
            "becomes the next live object."
        ),
        next_open_object="derive_or_falsify_mutual_attestability_semantics",
    )


def t386_result_to_dict(result: T386Result) -> dict[str, object]:
    return {
        "minimal_bidirectional_handshake_unique_survivor": (
            result.minimal_bidirectional_handshake_unique_survivor
        ),
        "raw_compatibility_derives_handshake": result.raw_compatibility_derives_handshake,
        "mutual_attestability_derives_handshake": (
            result.mutual_attestability_derives_handshake
        ),
        "one_sided_readout_rejected": result.one_sided_readout_rejected,
        "broadcast_without_ack_rejected": result.broadcast_without_ack_rejected,
        "shared_scalar_token_rejected": result.shared_scalar_token_rejected,
        "global_reconciler_rejected": result.global_reconciler_rejected,
        "signed_anti_handshake_rejected": result.signed_anti_handshake_rejected,
        "three_phase_commit_demoted": result.three_phase_commit_demoted,
        "asymmetric_receipt_partial": result.asymmetric_receipt_partial,
        "conditional_origin_chain_to_two_null_basis": (
            result.conditional_origin_chain_to_two_null_basis
        ),
        "surviving_protocol_ids": list(result.surviving_protocol_ids),
        "partial_protocol_ids": list(result.partial_protocol_ids),
        "demoted_protocol_ids": list(result.demoted_protocol_ids),
        "rejected_protocol_ids": list(result.rejected_protocol_ids),
        "derivation_steps": [
            {
                "step_id": step.step_id,
                "statement": step.statement,
                "dependency": step.dependency,
            }
            for step in result.derivation_steps
        ],
        "protocol_verdicts": [
            {
                "protocol_id": verdict.protocol_id,
                "status": verdict.status,
                "classification": verdict.classification,
                "passes": verdict.passes,
                "criteria": [
                    {
                        "criterion_id": criterion.criterion_id,
                        "passes": criterion.passes,
                        "reason": criterion.reason,
                    }
                    for criterion in verdict.criteria
                ],
                "reason": verdict.reason,
            }
            for verdict in result.protocol_verdicts
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
        "next_open_object": result.next_open_object,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t386_result_to_dict(run_t386_analysis()), indent=2))
