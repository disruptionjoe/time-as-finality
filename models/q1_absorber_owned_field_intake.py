"""T177: Q1 absorber-owned field intake screen.

The Q1 child branches now have strong local gates. This module adds one
pre-branch intake screen: a proposal does not reopen quantum measurement work
merely by changing fields already owned by decoherence, Quantum Darwinism,
Spectrum Broadcast Structure, detector provenance, ordinary monitored records,
or no-signalling/contextuality guardrails.

The screen is not a no-go theorem. It includes hypothetical positive controls
for the exact proposal shapes that would deserve further work.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.weak_measurement_platform_packet_gate import (
    Q1CPlatformPacketInput,
    classify_platform_packet,
)


Q1_BRANCHES = frozenset({"Q1A", "Q1B", "Q1C", "Q1D"})


@dataclass(frozen=True)
class Q1Proposal:
    proposal_id: str
    branch: str
    description: str
    changes_absorber_owned_fields: bool = False
    fixes_child_branch_closure_data: bool = False
    predeclares_new_physical_dimension: bool = False
    neighbor_can_import_dimension: bool = True
    changes_d1_or_taf_verdict: bool = False
    real_deployment_named: bool = False
    signed_predata_manifest: bool = False
    full_reviewable_rows_during_challenge: bool = False
    five_domain_claim_review_authority: bool = False
    mandatory_guardian_quorums: bool = False
    challenge_window_policy_frozen: bool = False
    q1c_packet: Q1CPlatformPacketInput | None = None
    positive_predeclared_verdict_lift: bool = False
    lift_source_physically_typed: bool = False
    preserves_no_signalling: bool = True
    exports_joint_record_before_causal_comparison: bool = False
    claims_hidden_variable_repair: bool = False
    names_nonredundant_theorem_target: bool = False


@dataclass(frozen=True)
class Q1IntakeAudit:
    proposal_id: str
    branch: str
    classification: str
    should_reopen_branch: bool
    required_next: str
    reason: str


@dataclass(frozen=True)
class T177Result:
    audits: tuple[Q1IntakeAudit, ...]
    null_controls_rejected: bool
    hypothetical_reopen_controls_admitted: bool
    q1_remains_roadmap_umbrella: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _reject(
    proposal: Q1Proposal,
    classification: str,
    reason: str,
    required_next: str,
) -> Q1IntakeAudit:
    return Q1IntakeAudit(
        proposal_id=proposal.proposal_id,
        branch=proposal.branch,
        classification=classification,
        should_reopen_branch=False,
        required_next=required_next,
        reason=reason,
    )


def _admit(
    proposal: Q1Proposal,
    classification: str,
    reason: str,
    required_next: str,
) -> Q1IntakeAudit:
    return Q1IntakeAudit(
        proposal_id=proposal.proposal_id,
        branch=proposal.branch,
        classification=classification,
        should_reopen_branch=True,
        required_next=required_next,
        reason=reason,
    )


def classify_q1_proposal(proposal: Q1Proposal) -> Q1IntakeAudit:
    if proposal.branch not in Q1_BRANCHES:
        return _reject(
            proposal,
            "null_unknown_q1_branch",
            "The proposal does not name one of the four current Q1 child branches.",
            "Route through Q1A, Q1B, Q1C, or Q1D before adding work.",
        )

    if proposal.branch == "Q1A":
        return _classify_q1a(proposal)
    if proposal.branch == "Q1B":
        return _classify_q1b(proposal)
    if proposal.branch == "Q1C":
        return _classify_q1c(proposal)
    return _classify_q1d(proposal)


def _classify_q1a(proposal: Q1Proposal) -> Q1IntakeAudit:
    if proposal.changes_absorber_owned_fields:
        return _reject(
            proposal,
            "absorbed_q1a_changes_sbs_or_qd_data",
            (
                "The proposal changes objectivity, access, provenance partition, "
                "partition visibility, audited support, or another field already "
                "importable by SBS, strong Quantum Darwinism, or provenance-aware "
                "redundancy accounting."
            ),
            "Hold the SBS/strong-QD closure key fixed before claiming a Q1A split.",
        )
    if not proposal.fixes_child_branch_closure_data:
        return _reject(
            proposal,
            "blocked_q1a_closure_key_not_fixed",
            "The proposal does not freeze the T162 SBS-importable closure data.",
            "Freeze full SBS/objectivity, access, partition, visibility, and support data.",
        )
    if not proposal.predeclares_new_physical_dimension:
        return _reject(
            proposal,
            "blocked_q1a_no_predeclared_physical_dimension",
            "A same-closure-key proposal must name the verdict-splitting dimension before scoring.",
            "Predeclare a physical dimension that is not the D1 verdict in disguise.",
        )
    if proposal.neighbor_can_import_dimension:
        return _reject(
            proposal,
            "absorbed_q1a_neighbor_imports_dimension",
            "The proposed dimension is still ordinary objectivity, access, provenance, or support data.",
            "Show why the neighbor cannot import the dimension without adding new physics.",
        )
    if not proposal.changes_d1_or_taf_verdict:
        return _reject(
            proposal,
            "null_q1a_no_verdict_split",
            "The closure key is fixed, but the proposed physical dimension does not change the verdict.",
            "Demonstrate a same-closure-key D1 split before reopening Q1A.",
        )
    return _admit(
        proposal,
        "provisional_q1a_same_sbs_key_split",
        "This is the exact post-T162 Q1A positive-control shape.",
        "Run the hostile same-SBS-data witness and attempt SBS/strong-QD absorption.",
    )


def _classify_q1b(proposal: Q1Proposal) -> Q1IntakeAudit:
    if not proposal.real_deployment_named:
        return _reject(
            proposal,
            "blocked_q1b_no_named_deployment",
            "Q1B is external now; synthetic governance prose is not detector evidence.",
            "Name a real detector deployment willing to sign the pre-data packet.",
        )
    required = (
        proposal.signed_predata_manifest,
        proposal.full_reviewable_rows_during_challenge,
        proposal.five_domain_claim_review_authority,
        proposal.mandatory_guardian_quorums,
        proposal.challenge_window_policy_frozen,
    )
    if not all(required):
        missing = []
        if not proposal.signed_predata_manifest:
            missing.append("signed pre-data manifest")
        if not proposal.full_reviewable_rows_during_challenge:
            missing.append("full reviewable rows during challenge")
        if not proposal.five_domain_claim_review_authority:
            missing.append("five authority domains")
        if not proposal.mandatory_guardian_quorums:
            missing.append("mandatory archive/escrow/trust quorums")
        if not proposal.challenge_window_policy_frozen:
            missing.append("frozen challenge-window policy")
        return _reject(
            proposal,
            "scaffold_only_q1b_incomplete_external_packet",
            "The deployment is missing: " + ", ".join(missing) + ".",
            "Complete the T136/T171/T173/T175/T176 external packet before scoring.",
        )
    return _admit(
        proposal,
        "provisional_q1b_reviewable_deployment_packet",
        "This clears the current Q1B intake burden but is still not evidence until rows are audited.",
        "Run the event-level packet through the detector null criterion and D1 scoring.",
    )


def _classify_q1c(proposal: Q1Proposal) -> Q1IntakeAudit:
    if proposal.q1c_packet is None:
        return _reject(
            proposal,
            "blocked_q1c_no_platform_packet",
            "Q1C cannot reopen without a frozen T166 platform packet.",
            "Supply R, A, architecture, H, V, support floor, loss, controls, and event-level burden.",
        )

    packet_audit = classify_platform_packet(
        proposal.q1c_packet,
        name=proposal.proposal_id,
    )
    if not packet_audit.admissible_packet:
        return _reject(
            proposal,
            packet_audit.classification,
            packet_audit.reason,
            packet_audit.required_next,
        )
    if not proposal.positive_predeclared_verdict_lift:
        return _reject(
            proposal,
            "scaffold_only_q1c_packet_without_verdict_lift",
            "The packet is admissible, but no positive predeclared verdict-risk lift is shown.",
            "Show that (R,A) improves the declared verdict risk over R alone.",
        )
    if not proposal.lift_source_physically_typed:
        return _reject(
            proposal,
            "blocked_q1c_untyped_lift_source",
            "Positive lift is not enough unless the source is extra environment structure or honest enlargement.",
            "Type the source of the lift before reopening Q1C.",
        )
    return _admit(
        proposal,
        "provisional_q1c_packet_plus_lift",
        "This is the post-T166 positive-control shape for Q1C.",
        "Run T149/T150/T158 event-level screens and same-neighbor-data absorbers.",
    )


def _classify_q1d(proposal: Q1Proposal) -> Q1IntakeAudit:
    if not proposal.preserves_no_signalling:
        return _reject(
            proposal,
            "null_q1d_signalling_language",
            "The proposal allows local signalling through finality language.",
            "Restore no-signalling before using Q1D.",
        )
    if proposal.claims_hidden_variable_repair:
        return _reject(
            proposal,
            "null_q1d_hidden_variable_retrofit",
            "The proposal treats Q1D as a hidden-variable repair.",
            "Keep contextuality as a guardrail unless a new theorem target is named.",
        )
    if proposal.exports_joint_record_before_causal_comparison:
        return _reject(
            proposal,
            "null_q1d_premature_joint_record_export",
            "The proposal exports a joint correlation record before causal comparison.",
            "Separate local records from later reconciled correlation records.",
        )
    if not proposal.names_nonredundant_theorem_target:
        return _reject(
            proposal,
            "guardrail_only_q1d_no_new_theorem_target",
            "The proposal is admissible language discipline but not a Q1D upgrade.",
            "Name a nonredundant contextuality or detector-record theorem target.",
        )
    return _admit(
        proposal,
        "provisional_q1d_theorem_target",
        "The proposal names a theorem target while preserving no-signalling and record staging.",
        "Compare against standard contextuality, decoherent histories, and local-algebra absorbers.",
    )


def _valid_q1c_packet() -> Q1CPlatformPacketInput:
    return Q1CPlatformPacketInput(
        ordinary_record_frozen=True,
        ordinary_record_is_full_event_level=True,
        auxiliary_channel_frozen=True,
        architecture_class="extra_environment",
        taf_axis_independently_typed=True,
        verdict_map_predeclared=True,
        class_support_floor_declared=True,
        loss_rule_declared=True,
        null_control_plan_declared=True,
        event_level_audit_data_promised=True,
    )


def _coarse_q1c_packet() -> Q1CPlatformPacketInput:
    return Q1CPlatformPacketInput(
        ordinary_record_frozen=True,
        ordinary_record_is_full_event_level=False,
        auxiliary_channel_frozen=True,
        architecture_class="extra_environment",
        taf_axis_independently_typed=True,
        verdict_map_predeclared=True,
        class_support_floor_declared=True,
        loss_rule_declared=True,
        null_control_plan_declared=True,
        event_level_audit_data_promised=True,
    )


def canonical_q1_intake_proposals() -> tuple[Q1Proposal, ...]:
    return (
        Q1Proposal(
            proposal_id="q1a_partition_relabel",
            branch="Q1A",
            description="Changes the provenance partition and calls the new verdict a Q1A split.",
            changes_absorber_owned_fields=True,
        ),
        Q1Proposal(
            proposal_id="q1a_same_sbs_key_physical_split_candidate",
            branch="Q1A",
            description="Hypothetical same-SBS-key physical dimension that changes D1.",
            fixes_child_branch_closure_data=True,
            predeclares_new_physical_dimension=True,
            neighbor_can_import_dimension=False,
            changes_d1_or_taf_verdict=True,
        ),
        Q1Proposal(
            proposal_id="q1b_nominal_federation",
            branch="Q1B",
            description="Named deployment, but no full challenge-window rights freeze.",
            real_deployment_named=True,
            signed_predata_manifest=True,
            full_reviewable_rows_during_challenge=False,
            five_domain_claim_review_authority=True,
            mandatory_guardian_quorums=True,
            challenge_window_policy_frozen=False,
        ),
        Q1Proposal(
            proposal_id="q1b_reviewable_packet_candidate",
            branch="Q1B",
            description="Hypothetical complete reviewable-row deployment packet.",
            real_deployment_named=True,
            signed_predata_manifest=True,
            full_reviewable_rows_during_challenge=True,
            five_domain_claim_review_authority=True,
            mandatory_guardian_quorums=True,
            challenge_window_policy_frozen=True,
        ),
        Q1Proposal(
            proposal_id="q1c_coarse_record_second_meter",
            branch="Q1C",
            description="Second meter with only coarse standard record fixed.",
            q1c_packet=_coarse_q1c_packet(),
        ),
        Q1Proposal(
            proposal_id="q1c_packet_without_lift",
            branch="Q1C",
            description="Complete packet but no verdict-risk lift over R.",
            q1c_packet=_valid_q1c_packet(),
            positive_predeclared_verdict_lift=False,
            lift_source_physically_typed=True,
        ),
        Q1Proposal(
            proposal_id="q1c_packet_plus_typed_lift_candidate",
            branch="Q1C",
            description="Hypothetical valid packet with typed positive verdict lift.",
            q1c_packet=_valid_q1c_packet(),
            positive_predeclared_verdict_lift=True,
            lift_source_physically_typed=True,
        ),
        Q1Proposal(
            proposal_id="q1d_hidden_variable_story",
            branch="Q1D",
            description="Turns later correlation records into hidden variables.",
            claims_hidden_variable_repair=True,
        ),
        Q1Proposal(
            proposal_id="q1d_guardrail_only_language",
            branch="Q1D",
            description="Preserves no-signalling but names no new theorem.",
        ),
    )


def run_t177_analysis() -> T177Result:
    audits = tuple(
        classify_q1_proposal(proposal)
        for proposal in canonical_q1_intake_proposals()
    )
    reopen_ids = {audit.proposal_id for audit in audits if audit.should_reopen_branch}
    expected_reopen_ids = {
        "q1a_same_sbs_key_physical_split_candidate",
        "q1b_reviewable_packet_candidate",
        "q1c_packet_plus_typed_lift_candidate",
    }
    null_controls_rejected = all(
        not audit.should_reopen_branch
        for audit in audits
        if audit.proposal_id not in expected_reopen_ids
    )
    hypothetical_reopen_controls_admitted = reopen_ids == expected_reopen_ids

    return T177Result(
        audits=audits,
        null_controls_rejected=null_controls_rejected,
        hypothetical_reopen_controls_admitted=hypothetical_reopen_controls_admitted,
        q1_remains_roadmap_umbrella=(
            null_controls_rejected and hypothetical_reopen_controls_admitted
        ),
        strongest_claim=(
            "Q1 should be reopened only by a proposal that clears a child-branch "
            "escape gate while holding absorber-owned fields fixed. Changing SBS, "
            "Quantum-Darwinism, provenance, ordinary-record, governance, or "
            "no-signalling data is absorption, not a quantum measurement upgrade."
        ),
        improved=(
            "T177 gives Q1 a single intake screen before branch-local work starts. "
            "It admits exact positive-control shapes for Q1A, Q1B, and Q1C, while "
            "rejecting partition relabels, nominal federations, coarse second "
            "meters, no-lift platform packets, and hidden-variable language."
        ),
        weakened=(
            "This weakens Q1 as an autonomous research route. Most plausible "
            "proposal motions are now classified as absorber-owned field changes "
            "or scaffold-only until they clear a stricter branch gate."
        ),
        falsification_condition=(
            "T177 fails if a serious Q1 proposal should reopen a branch despite "
            "changing only absorber-owned fields, omitting the child-branch closure "
            "data, lacking a real Q1B deployment packet, lacking a T166/T149-style "
            "Q1C packet-plus-lift, or violating Q1D no-signalling/staging rules."
        ),
        q1_update=(
            "Q1 remains a roadmap umbrella. Future quantum-measurement work must "
            "first pass the T177 intake screen, then the relevant child-branch gate."
        ),
        claim_ledger_update=(
            "Add T177 to Q1: absorber-owned field changes do not reopen Q1. Only "
            "a same-SBS-key Q1A physical split, a complete reviewable Q1B deployment "
            "packet, or a T166-valid Q1C packet with typed positive verdict lift "
            "passes the intake screen; Q1D remains guardrail-only absent a theorem."
        ),
        open_blocker=(
            "No current repo proposal supplies one of the admitted positive-control "
            "shapes. The screen is ready, but the frontier remains externally or "
            "physically blocked."
        ),
        recommended_next=(
            "Use T177 as the first check for any future Q1 proposal. Without a "
            "passing intake classification, shift the hourly run away from Q1."
        ),
    )


def _audit_to_dict(audit: Q1IntakeAudit) -> dict[str, object]:
    return {
        "proposal_id": audit.proposal_id,
        "branch": audit.branch,
        "classification": audit.classification,
        "should_reopen_branch": audit.should_reopen_branch,
        "required_next": audit.required_next,
        "reason": audit.reason,
    }


def t177_result_to_dict(result: T177Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "null_controls_rejected": result.null_controls_rejected,
        "hypothetical_reopen_controls_admitted": (
            result.hypothetical_reopen_controls_admitted
        ),
        "q1_remains_roadmap_umbrella": result.q1_remains_roadmap_umbrella,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t177_result_to_dict(run_t177_analysis()), indent=2))
