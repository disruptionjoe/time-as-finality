"""T388: mutual-attestability semantics origin screen.

T386 derived a bidirectional handshake from local mutual attestability. T387
flagged the remaining question: why should compatibility mean mutual local
attestability at all?

T388 tests semantics for "compatible." Raw compatibility still does not force
mutuality. But if compatibility is record-finalizable shared state, with local,
durable, source-owned, authentic receipts at both endpoints and no global
reconciler, then mutual local attestability follows in the finite screen.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompatibilitySemantics:
    semantics_id: str
    local_pairwise_relation: bool
    shared_record_state: bool
    symmetric_label_only: bool
    scalar_token_only: bool
    two_endpoint_attestation: bool
    durable_both_sides: bool
    source_owned_receipts: bool
    authentic_receipts: bool
    one_sided_readout: bool
    imports_global_reconciler: bool
    hidden_foliation: bool
    nonnegative_source_counts: bool
    finality_closure: bool
    description: str


@dataclass(frozen=True)
class SemanticsCriterion:
    criterion_id: str
    passes: bool
    reason: str


@dataclass(frozen=True)
class SemanticsVerdict:
    semantics_id: str
    status: str
    classification: str
    derives_mutual_attestability: bool
    criteria: tuple[SemanticsCriterion, ...]
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
class T388Result:
    finalizable_shared_state_unique_survivor: bool
    raw_compatibility_derives_mutual_attestability: bool
    record_finality_semantics_derives_mutual_attestability: bool
    symmetric_label_partial: bool
    scalar_token_rejected: bool
    one_sided_readout_rejected: bool
    global_reconciler_rejected: bool
    spoofed_receipt_rejected: bool
    asymmetric_persistence_partial: bool
    conditional_chain_to_two_null_basis: bool
    surviving_semantics_ids: tuple[str, ...]
    partial_semantics_ids: tuple[str, ...]
    rejected_semantics_ids: tuple[str, ...]
    derivation_steps: tuple[DerivationStep, ...]
    semantics_verdicts: tuple[SemanticsVerdict, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str
    next_open_object: str


def compatibility_semantics_catalog() -> tuple[CompatibilitySemantics, ...]:
    return (
        CompatibilitySemantics(
            semantics_id="raw_predicate_compatibility",
            local_pairwise_relation=True,
            shared_record_state=False,
            symmetric_label_only=False,
            scalar_token_only=False,
            two_endpoint_attestation=False,
            durable_both_sides=False,
            source_owned_receipts=False,
            authentic_receipts=False,
            one_sided_readout=False,
            imports_global_reconciler=False,
            hidden_foliation=False,
            nonnegative_source_counts=True,
            finality_closure=False,
            description="bare compatible/incompatible predicate with no witness semantics",
        ),
        CompatibilitySemantics(
            semantics_id="symmetric_label_compatibility",
            local_pairwise_relation=True,
            shared_record_state=False,
            symmetric_label_only=True,
            scalar_token_only=False,
            two_endpoint_attestation=False,
            durable_both_sides=False,
            source_owned_receipts=False,
            authentic_receipts=False,
            one_sided_readout=False,
            imports_global_reconciler=False,
            hidden_foliation=False,
            nonnegative_source_counts=True,
            finality_closure=False,
            description="A and B share a symmetric compatibility label but no endpoint-owned receipt",
        ),
        CompatibilitySemantics(
            semantics_id="shared_scalar_token_compatibility",
            local_pairwise_relation=True,
            shared_record_state=False,
            symmetric_label_only=False,
            scalar_token_only=True,
            two_endpoint_attestation=True,
            durable_both_sides=True,
            source_owned_receipts=True,
            authentic_receipts=True,
            one_sided_readout=False,
            imports_global_reconciler=False,
            hidden_foliation=False,
            nonnegative_source_counts=True,
            finality_closure=False,
            description="both endpoints share one scalar token without a finalizable relation record",
        ),
        CompatibilitySemantics(
            semantics_id="one_sided_readout_compatibility",
            local_pairwise_relation=True,
            shared_record_state=True,
            symmetric_label_only=False,
            scalar_token_only=False,
            two_endpoint_attestation=False,
            durable_both_sides=False,
            source_owned_receipts=True,
            authentic_receipts=True,
            one_sided_readout=True,
            imports_global_reconciler=False,
            hidden_foliation=False,
            nonnegative_source_counts=True,
            finality_closure=False,
            description="one endpoint records compatibility while the other has no durable receipt",
        ),
        CompatibilitySemantics(
            semantics_id="global_reconciled_compatibility",
            local_pairwise_relation=False,
            shared_record_state=True,
            symmetric_label_only=False,
            scalar_token_only=False,
            two_endpoint_attestation=True,
            durable_both_sides=True,
            source_owned_receipts=True,
            authentic_receipts=True,
            one_sided_readout=False,
            imports_global_reconciler=True,
            hidden_foliation=True,
            nonnegative_source_counts=True,
            finality_closure=True,
            description="a global reconciler issues compatibility receipts to both endpoints",
        ),
        CompatibilitySemantics(
            semantics_id="spoofed_receipt_compatibility",
            local_pairwise_relation=True,
            shared_record_state=True,
            symmetric_label_only=False,
            scalar_token_only=False,
            two_endpoint_attestation=True,
            durable_both_sides=True,
            source_owned_receipts=False,
            authentic_receipts=False,
            one_sided_readout=False,
            imports_global_reconciler=False,
            hidden_foliation=False,
            nonnegative_source_counts=True,
            finality_closure=False,
            description="two receipts exist but can be spoofed, replayed, or equivocated",
        ),
        CompatibilitySemantics(
            semantics_id="asymmetric_persistence_compatibility",
            local_pairwise_relation=True,
            shared_record_state=True,
            symmetric_label_only=False,
            scalar_token_only=False,
            two_endpoint_attestation=True,
            durable_both_sides=False,
            source_owned_receipts=True,
            authentic_receipts=True,
            one_sided_readout=False,
            imports_global_reconciler=False,
            hidden_foliation=False,
            nonnegative_source_counts=True,
            finality_closure=False,
            description="both endpoints can attest once, but only one side has durable persistence",
        ),
        CompatibilitySemantics(
            semantics_id="finalizable_shared_state_compatibility",
            local_pairwise_relation=True,
            shared_record_state=True,
            symmetric_label_only=False,
            scalar_token_only=False,
            two_endpoint_attestation=True,
            durable_both_sides=True,
            source_owned_receipts=True,
            authentic_receipts=True,
            one_sided_readout=False,
            imports_global_reconciler=False,
            hidden_foliation=False,
            nonnegative_source_counts=True,
            finality_closure=True,
            description=(
                "local pairwise shared state with durable, source-owned, authentic "
                "receipts at both endpoints"
            ),
        ),
    )


def evaluate_semantics(semantics: CompatibilitySemantics) -> SemanticsVerdict:
    criteria = (
        SemanticsCriterion(
            "no_global_reconciler",
            not semantics.imports_global_reconciler,
            "compatibility semantics must not be certified by a global reconciler",
        ),
        SemanticsCriterion(
            "no_hidden_foliation",
            not semantics.hidden_foliation,
            "compatibility must not smuggle in a global ordering layer",
        ),
        SemanticsCriterion(
            "local_pairwise_relation",
            semantics.local_pairwise_relation,
            "compatibility should be witnessed as a local pair relation",
        ),
        SemanticsCriterion(
            "shared_record_state",
            semantics.shared_record_state,
            "compatibility must be a finalizable relation record, not only a label or token",
        ),
        SemanticsCriterion(
            "not_label_or_scalar_only",
            not semantics.symmetric_label_only and not semantics.scalar_token_only,
            "symmetric labels and scalar tokens do not establish record-finality mutuality",
        ),
        SemanticsCriterion(
            "two_endpoint_attestation",
            semantics.two_endpoint_attestation,
            "both endpoints must be able to attest the compatibility relation",
        ),
        SemanticsCriterion(
            "durable_both_sides",
            semantics.durable_both_sides,
            "mutual attestability must persist at both endpoints",
        ),
        SemanticsCriterion(
            "source_owned_authentic_receipts",
            semantics.source_owned_receipts and semantics.authentic_receipts,
            "receipts must be source-owned and resistant to spoof/replay/equivocation",
        ),
        SemanticsCriterion(
            "not_one_sided_readout",
            not semantics.one_sided_readout,
            "one-sided observation is not mutual local attestability",
        ),
        SemanticsCriterion(
            "nonnegative_source_counts",
            semantics.nonnegative_source_counts,
            "source-level compatibility uses nonnegative primitive counts",
        ),
        SemanticsCriterion(
            "finality_closure",
            semantics.finality_closure,
            "after finalization, the pair relation should not diverge without a record conflict",
        ),
    )
    derives = all(criterion.passes for criterion in criteria)

    if derives:
        status = "record_finality_mutual_attestability_survivor"
        classification = "survivor"
        reason = (
            "record-finalizable shared state requires durable, authentic endpoint receipts, "
            "so mutual local attestability follows"
        )
    elif semantics.imports_global_reconciler or semantics.hidden_foliation:
        status = "rejected_global_reconciliation"
        classification = "rejected"
        reason = "global reconciliation imports certification/order rather than local mutuality"
    elif semantics.semantics_id == "raw_predicate_compatibility":
        status = "underdetermined_raw_predicate"
        classification = "rejected"
        reason = "a bare predicate does not specify witness, receipt, persistence, or finality semantics"
    elif semantics.symmetric_label_only:
        status = "partial_symmetry_not_attestation"
        classification = "partial"
        reason = "symmetry says the label is mirrored, not that endpoints own durable receipts"
    elif semantics.scalar_token_only:
        status = "rejected_scalar_token_not_record_state"
        classification = "rejected"
        reason = "a scalar token can be shared without finalizing a pairwise relation record"
    elif semantics.one_sided_readout:
        status = "rejected_one_sided_readout"
        classification = "rejected"
        reason = "one-sided readout leaves one endpoint unable to attest the relation"
    elif not semantics.source_owned_receipts or not semantics.authentic_receipts:
        status = "rejected_spoofed_or_unowned_receipts"
        classification = "rejected"
        reason = "apparent receipts do not count if they can be spoofed, replayed, or equivocated"
    elif not semantics.durable_both_sides:
        status = "partial_asymmetric_persistence"
        classification = "partial"
        reason = "temporary or one-sided persistence cannot support finalizable mutuality"
    elif not semantics.shared_record_state:
        status = "rejected_no_shared_record_state"
        classification = "rejected"
        reason = "without shared record state, compatibility is not a finalizable relation"
    else:
        status = "failed_semantics_screen"
        classification = "rejected"
        reason = "semantics misses at least one mutual-attestability requirement"

    return SemanticsVerdict(
        semantics_id=semantics.semantics_id,
        status=status,
        classification=classification,
        derives_mutual_attestability=derives,
        criteria=criteria,
        reason=reason,
    )


def evaluate_semantics_catalog() -> tuple[SemanticsVerdict, ...]:
    return tuple(evaluate_semantics(semantics) for semantics in compatibility_semantics_catalog())


def derivation_steps() -> tuple[DerivationStep, ...]:
    return (
        DerivationStep(
            "raw_compatibility_underdetermined",
            "A bare compatible/incompatible predicate does not decide witness semantics.",
            "none",
        ),
        DerivationStep(
            "record_finality_requires_persistent_relation",
            "If compatibility is record-finalizable shared state, the pair relation must persist.",
            "record_finality_semantics",
        ),
        DerivationStep(
            "local_no_global_requires_endpoint_receipts",
            "Without global reconciliation, persistence must be carried by endpoint-owned receipts.",
            "no_global_reconciler",
        ),
        DerivationStep(
            "authentic_two_endpoint_receipts_force_mutuality",
            "Durable authentic receipts at both endpoints force mutual local attestability.",
            "source_owned_authentic_receipts",
        ),
        DerivationStep(
            "mutuality_feeds_t386_t385_chain",
            "T386 turns mutual local attestability into a bidirectional handshake, and T385 turns that into the two-null basis motivation.",
            "T386_and_T385",
        ),
    )


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            "raw_compatibility_semantics",
            "still_not_enough",
            True,
            "raw compatibility alone does not force mutual local attestability",
        ),
        ComparatorVerdict(
            "record_finality_semantics",
            "conditional_derivation_supported",
            False,
            "record-finalizable shared state forces mutual local attestability in this screen",
        ),
        ComparatorVerdict(
            "symmetric_label_shortcut",
            "rejected_as_insufficient",
            False,
            "a symmetric label can mirror a predicate without endpoint-owned receipts",
        ),
        ComparatorVerdict(
            "receipt_authenticity",
            "explicit_requirement",
            False,
            "spoofed or replayed receipts are rejected rather than counted as mutuality",
        ),
        ComparatorVerdict(
            "two_leg_to_null_signal_bridge",
            "still_absorbs",
            True,
            "this screen derives mutuality, not the nullness or bilinear geometry of signal legs",
        ),
        ComparatorVerdict(
            "minimality_principle_origin",
            "still_absorbs",
            True,
            "T386 still uses minimality to select the two-leg handshake from mutuality",
        ),
    )


def run_t388_analysis() -> T388Result:
    verdicts = evaluate_semantics_catalog()
    by_id = {verdict.semantics_id: verdict for verdict in verdicts}
    survivors = tuple(
        verdict.semantics_id for verdict in verdicts if verdict.classification == "survivor"
    )
    partials = tuple(
        verdict.semantics_id for verdict in verdicts if verdict.classification == "partial"
    )
    rejected = tuple(
        verdict.semantics_id for verdict in verdicts if verdict.classification == "rejected"
    )
    return T388Result(
        finalizable_shared_state_unique_survivor=(
            survivors == ("finalizable_shared_state_compatibility",)
        ),
        raw_compatibility_derives_mutual_attestability=False,
        record_finality_semantics_derives_mutual_attestability=True,
        symmetric_label_partial=(
            by_id["symmetric_label_compatibility"].status == "partial_symmetry_not_attestation"
        ),
        scalar_token_rejected=(
            by_id["shared_scalar_token_compatibility"].status
            == "rejected_scalar_token_not_record_state"
        ),
        one_sided_readout_rejected=(
            by_id["one_sided_readout_compatibility"].status == "rejected_one_sided_readout"
        ),
        global_reconciler_rejected=(
            by_id["global_reconciled_compatibility"].status == "rejected_global_reconciliation"
        ),
        spoofed_receipt_rejected=(
            by_id["spoofed_receipt_compatibility"].status
            == "rejected_spoofed_or_unowned_receipts"
        ),
        asymmetric_persistence_partial=(
            by_id["asymmetric_persistence_compatibility"].status
            == "partial_asymmetric_persistence"
        ),
        conditional_chain_to_two_null_basis=True,
        surviving_semantics_ids=survivors,
        partial_semantics_ids=partials,
        rejected_semantics_ids=rejected,
        derivation_steps=derivation_steps(),
        semantics_verdicts=verdicts,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict=(
            "mutual_attestability_derived_from_record_finalizable_shared_state_not_raw_compatibility"
        ),
        strongest_claim=(
            "Raw compatibility still does not derive mutual local attestability. But if "
            "compatibility means local record-finalizable shared state, with durable "
            "source-owned authentic receipts at both endpoints and no global reconciler, "
            "then mutual local attestability follows. Through T386 and T385 this gives a "
            "conditional path to the bidirectional handshake and two-null basis motivation."
        ),
        claim_ledger_update=(
            "Register T388 as a semantics-origin screen: mutual_attestability_semantics_origin "
            "is resolved under record-finality semantics, while raw compatibility remains "
            "insufficient and two_leg_to_null_signal_bridge remains open."
        ),
        next_open_object="two_leg_to_null_signal_bridge",
    )


def t388_result_to_dict(result: T388Result) -> dict[str, object]:
    return {
        "finalizable_shared_state_unique_survivor": (
            result.finalizable_shared_state_unique_survivor
        ),
        "raw_compatibility_derives_mutual_attestability": (
            result.raw_compatibility_derives_mutual_attestability
        ),
        "record_finality_semantics_derives_mutual_attestability": (
            result.record_finality_semantics_derives_mutual_attestability
        ),
        "symmetric_label_partial": result.symmetric_label_partial,
        "scalar_token_rejected": result.scalar_token_rejected,
        "one_sided_readout_rejected": result.one_sided_readout_rejected,
        "global_reconciler_rejected": result.global_reconciler_rejected,
        "spoofed_receipt_rejected": result.spoofed_receipt_rejected,
        "asymmetric_persistence_partial": result.asymmetric_persistence_partial,
        "conditional_chain_to_two_null_basis": result.conditional_chain_to_two_null_basis,
        "surviving_semantics_ids": list(result.surviving_semantics_ids),
        "partial_semantics_ids": list(result.partial_semantics_ids),
        "rejected_semantics_ids": list(result.rejected_semantics_ids),
        "derivation_steps": [
            {
                "step_id": step.step_id,
                "statement": step.statement,
                "dependency": step.dependency,
            }
            for step in result.derivation_steps
        ],
        "semantics_verdicts": [
            {
                "semantics_id": verdict.semantics_id,
                "status": verdict.status,
                "classification": verdict.classification,
                "derives_mutual_attestability": verdict.derives_mutual_attestability,
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
            for verdict in result.semantics_verdicts
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

    print(json.dumps(t388_result_to_dict(run_t388_analysis()), indent=2))
