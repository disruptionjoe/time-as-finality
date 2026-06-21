"""T140: Q1 branch frontier and escape-matrix audit.

The Q1 branch has been narrowed by T101, T104, T105, T109, T118,
T138, and T139. T140 turns the remaining branch prose into an executable
decision matrix: what would count as a non-null Q1A, Q1B, Q1C, or Q1D
next move, and what is merely another absorbed internal witness?
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Q1AInput:
    fixed_standard_quantum_summaries: bool
    provenance_partition_shared: bool
    same_audited_accessible_support: bool
    verdict_split_at_same_support: bool
    physical_dimension_beyond_support: bool
    partition_rule_nonimportable_by_neighbor: bool


@dataclass(frozen=True)
class Q1BInput:
    t138_workflow_fit: bool
    pre_event_manifest_signed: bool
    real_event_rows_published: bool
    packet_schema_unchanged_after_manifest: bool
    passes_packet_and_authority_gates: bool
    survives_t83_null_criterion: bool


@dataclass(frozen=True)
class Q1CInput:
    full_event_standard_record_fixed: bool
    auxiliary_axis_independent_after_full_record: bool
    verdict_changes: bool
    postselected_or_schedule_proxy: bool


@dataclass(frozen=True)
class Q1DInput:
    no_signalling_preserved: bool
    avoids_hidden_variable_reading: bool
    nonredundant_theorem_named: bool
    already_standard_contextuality: bool


@dataclass(frozen=True)
class BranchAudit:
    branch: str
    classification: str
    active_internal_route: bool
    live_evidence: bool
    reason: str
    required_next: str


@dataclass(frozen=True)
class T140Result:
    audits: tuple[BranchAudit, ...]
    internal_q1_upgrade_available: bool
    q1b_is_only_external_experimental_path: bool
    overall_recommendation: str
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def classify_q1a(case: Q1AInput) -> BranchAudit:
    if not case.fixed_standard_quantum_summaries:
        return BranchAudit(
            branch="Q1A",
            classification="inadmissible_standard_data_changed",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The proposed witness changes ordinary quantum-side summaries, "
                "so it does not test the post-T102 fixed-data gate."
            ),
            required_next="Hold decoherence, fragment information, redundancy, and branch/history data fixed.",
        )
    if not case.provenance_partition_shared:
        return BranchAudit(
            branch="Q1A",
            classification="underdescribed_partition",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The witness has not granted the neighbor the same audited "
                "provenance-aware fragment partition, so T104 absorption has "
                "not been tested."
            ),
            required_next="Share the access cut and provenance partition before scoring D1.",
        )
    if not case.same_audited_accessible_support:
        return BranchAudit(
            branch="Q1A",
            classification="bookkeeping_accessible_support_count",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The split is still explained by the T105 audited accessible "
                "support count, not by nonredundant measurement structure."
            ),
            required_next="Match audited accessible support, then ask whether the D1 verdict still splits.",
        )
    if case.verdict_split_at_same_support and (
        case.physical_dimension_beyond_support
        or case.partition_rule_nonimportable_by_neighbor
    ):
        return BranchAudit(
            branch="Q1A",
            classification="candidate_nonredundant_q1a_escape",
            active_internal_route=True,
            live_evidence=False,
            reason=(
                "This is the minimal internal Q1A escape class: fixed standard "
                "summaries, shared provenance partition, same audited support, "
                "and a verdict split carried by a physically justified "
                "dimension or a nonimportable partition rule."
            ),
            required_next="Build the witness and run the same-neighbor-data absorption pass.",
        )
    if case.verdict_split_at_same_support:
        return BranchAudit(
            branch="Q1A",
            classification="underjustified_same_support_split",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The witness claims a same-support verdict split, but the "
                "load-bearing dimension has not been physically justified."
            ),
            required_next="Name the physical D1 dimension or the nonimportable partition rule.",
        )
    return BranchAudit(
        branch="Q1A",
        classification="bookkeeping_only",
        active_internal_route=False,
        live_evidence=False,
        reason=(
            "Current Q1A evidence is exhausted by audited accessible support "
            "plus partition visibility after T105, T109, and T118."
        ),
        required_next="Do not add another Q1A toy witness unless it targets the same-support escape gate.",
    )


def classify_q1b(case: Q1BInput) -> BranchAudit:
    if not case.t138_workflow_fit:
        return BranchAudit(
            branch="Q1B",
            classification="null_workflow_fit_failure",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The workflow is post hoc or authority-collapsed under T138, "
                "so it cannot supply detector-branch evidence."
            ),
            required_next="Use a federated pre-data workflow with separated authority domains.",
        )
    if not case.pre_event_manifest_signed:
        return BranchAudit(
            branch="Q1B",
            classification="externally_blocked_no_signed_manifest",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The only non-null detector path requires a T136/T138 manifest "
                "signed before event collection; no such concrete deployment "
                "is present."
            ),
            required_next="Find a named lab or team willing to sign the federated manifest pre-data.",
        )
    if not case.real_event_rows_published:
        return BranchAudit(
            branch="Q1B",
            classification="externally_blocked_no_event_rows",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "A signed manifest without real event-level rows is still only "
                "a scaffold, not detector evidence."
            ),
            required_next="Publish the bound event-level packet without changing schema, authority, or tier.",
        )
    if not case.packet_schema_unchanged_after_manifest:
        return BranchAudit(
            branch="Q1B",
            classification="null_schema_changed_after_manifest",
            active_internal_route=False,
            live_evidence=False,
            reason="The packet changed after the pre-event freeze, invalidating the manifest.",
            required_next="Freeze the schema, authorities, and tier before the first event.",
        )
    if not case.passes_packet_and_authority_gates:
        return BranchAudit(
            branch="Q1B",
            classification="null_packet_or_authority_gate_failure",
            active_internal_route=False,
            live_evidence=False,
            reason="The event packet fails the T87/T97/T100/T121/T133 admission gates.",
            required_next="Repair the packet before treating detector records as D1 evidence.",
        )
    if not case.survives_t83_null_criterion:
        return BranchAudit(
            branch="Q1B",
            classification="null_reduces_to_existing_summary",
            active_internal_route=False,
            live_evidence=False,
            reason="The detector verdict reduces to passive statistics, dashboards, or post hoc labels.",
            required_next="Produce a verdict that survives the T83 null criterion.",
        )
    return BranchAudit(
        branch="Q1B",
        classification="candidate_detector_evidence_packet",
        active_internal_route=False,
        live_evidence=True,
        reason=(
            "This is the minimum detector-branch live-evidence class: manifest "
            "fit, pre-event signature, real rows, unchanged packet policy, "
            "packet-gate success, and T83 survival."
        ),
        required_next="Review the raw packet and only then compute D1 scores.",
    )


def classify_q1c(case: Q1CInput) -> BranchAudit:
    if not case.full_event_standard_record_fixed:
        return BranchAudit(
            branch="Q1C",
            classification="null_coarse_standard_record",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The proposed split fixes only a coarse ordinary record, so it "
                "falls to the T139 coarse-summary loophole."
            ),
            required_next="Condition on the full pre-registered event-level standard monitored record.",
        )
    if not case.auxiliary_axis_independent_after_full_record:
        return BranchAudit(
            branch="Q1C",
            classification="null_screened_off_by_full_record",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The auxiliary axis is conditionally determined by the full "
                "ordinary monitored record."
            ),
            required_next="Name an auxiliary channel that remains verdict-changing after full-record conditioning.",
        )
    if case.postselected_or_schedule_proxy:
        return BranchAudit(
            branch="Q1C",
            classification="null_proxy_or_postselection",
            active_internal_route=False,
            live_evidence=False,
            reason="The axis is a control-schedule proxy or success-conditioned reversal.",
            required_next="Use a calibrated meter fixed before analysis and not conditioned on success.",
        )
    if not case.verdict_changes:
        return BranchAudit(
            branch="Q1C",
            classification="independent_but_not_decisive",
            active_internal_route=False,
            live_evidence=False,
            reason="The auxiliary channel is independent but does not change the TaF verdict.",
            required_next="Show a verdict split under fixed full standard record and fixed standard summaries.",
        )
    return BranchAudit(
        branch="Q1C",
        classification="candidate_full_record_escape",
        active_internal_route=True,
        live_evidence=False,
        reason=(
            "This is the minimum Q1C reopening class: a calibrated auxiliary "
            "axis remains verdict-changing after conditioning on the full "
            "ordinary monitored record."
        ),
        required_next="Tie the logical escape to a named monitored-qubit platform.",
    )


def classify_q1d(case: Q1DInput) -> BranchAudit:
    if not case.no_signalling_preserved or not case.avoids_hidden_variable_reading:
        return BranchAudit(
            branch="Q1D",
            classification="invalid_guardrail_violation",
            active_internal_route=False,
            live_evidence=False,
            reason=(
                "The proposal violates the contextuality/no-signalling guardrail "
                "or turns finality language into hidden-variable language."
            ),
            required_next="Reject or rewrite the claim before any model work.",
        )
    if not case.nonredundant_theorem_named:
        return BranchAudit(
            branch="Q1D",
            classification="guardrail_only",
            active_internal_route=False,
            live_evidence=False,
            reason="Q1D constrains language but does not yet name a nonredundant theorem target.",
            required_next="Name a theorem not already covered by standard contextuality or no-signalling.",
        )
    if case.already_standard_contextuality:
        return BranchAudit(
            branch="Q1D",
            classification="absorbed_by_standard_contextuality",
            active_internal_route=False,
            live_evidence=False,
            reason="The theorem target is already supplied by standard contextuality/no-signalling frameworks.",
            required_next="Record absorption rather than promoting a Q1D result.",
        )
    return BranchAudit(
        branch="Q1D",
        classification="candidate_nonredundant_guardrail_theorem",
        active_internal_route=True,
        live_evidence=False,
        reason="A theorem target survives the guardrails and is not already standard.",
        required_next="Formalize the theorem and run a native absorber pass.",
    )


def current_frontier_inputs() -> tuple[Q1AInput, Q1BInput, Q1CInput, Q1DInput]:
    return (
        Q1AInput(
            fixed_standard_quantum_summaries=True,
            provenance_partition_shared=True,
            same_audited_accessible_support=True,
            verdict_split_at_same_support=False,
            physical_dimension_beyond_support=False,
            partition_rule_nonimportable_by_neighbor=False,
        ),
        Q1BInput(
            t138_workflow_fit=True,
            pre_event_manifest_signed=False,
            real_event_rows_published=False,
            packet_schema_unchanged_after_manifest=False,
            passes_packet_and_authority_gates=False,
            survives_t83_null_criterion=False,
        ),
        Q1CInput(
            full_event_standard_record_fixed=True,
            auxiliary_axis_independent_after_full_record=False,
            verdict_changes=False,
            postselected_or_schedule_proxy=False,
        ),
        Q1DInput(
            no_signalling_preserved=True,
            avoids_hidden_variable_reading=True,
            nonredundant_theorem_named=False,
            already_standard_contextuality=True,
        ),
    )


def run_t140_analysis(
    inputs: tuple[Q1AInput, Q1BInput, Q1CInput, Q1DInput] | None = None,
) -> T140Result:
    if inputs is None:
        inputs = current_frontier_inputs()
    q1a, q1b, q1c, q1d = inputs
    audits = (
        classify_q1a(q1a),
        classify_q1b(q1b),
        classify_q1c(q1c),
        classify_q1d(q1d),
    )
    internal_q1_upgrade_available = any(audit.active_internal_route for audit in audits)
    q1b_is_only_external_experimental_path = (
        audits[1].classification.startswith("externally_blocked")
        and not internal_q1_upgrade_available
    )

    if internal_q1_upgrade_available:
        overall_recommendation = (
            "Run only the branch whose escape gate is explicitly satisfied; do "
            "not broaden Q1."
        )
    elif q1b_is_only_external_experimental_path:
        overall_recommendation = (
            "Do not spend the next internal research run on another Q1 toy "
            "witness. The quantum branch is waiting on an external Q1B "
            "manifest or event packet; absent that, move the next autonomous "
            "run to thermodynamic arrow, spacetime reconstruction, or another "
            "non-Q1 route."
        )
    else:
        overall_recommendation = (
            "Treat Q1 as inactive until a branch-specific escape condition is "
            "met."
        )

    return T140Result(
        audits=audits,
        internal_q1_upgrade_available=internal_q1_upgrade_available,
        q1b_is_only_external_experimental_path=q1b_is_only_external_experimental_path,
        overall_recommendation=overall_recommendation,
        strongest_claim=(
            "The current Q1 frontier has no active internal upgrade route. Q1A "
            "is bookkeeping-only after accessible-support, branch-support, and "
            "reversal-cost collapse; Q1C is dormant unless a full-record "
            "auxiliary-meter escape is tied to a real platform; Q1D is a "
            "guardrail. Q1B is the only non-null experimental direction, but "
            "it is externally blocked until a real pre-event manifest and "
            "event-level packet exist."
        ),
        improved=(
            "T140 converts scattered branch-specific demotion prose into an "
            "executable route-selection matrix. Future Q1 work now has to "
            "name which escape gate it satisfies before adding another model."
        ),
        weakened=(
            "This weakens Q1 as an autonomous internal research route. Without "
            "a same-support Q1A split, a real Q1B packet, a full-record Q1C "
            "meter, or a nonredundant Q1D theorem, more internal Q1 artifacts "
            "are expected to be absorbed."
        ),
        falsification_condition=(
            "T140 fails if one current branch already satisfies its listed "
            "escape gate, or if a future branch-specific artifact satisfies an "
            "escape gate and is still classified here as inactive."
        ),
        claim_ledger_update=(
            "Add T140 to Q1: no current Q1 child branch has an active internal "
            "upgrade route; Q1B remains the only non-null experimental path "
            "but is externally blocked pending a signed pre-event manifest and "
            "real event-level packet."
        ),
        open_blocker=(
            "No named detector deployment has signed the T136/T138 manifest "
            "pre-data, and no Q1A/Q1C/Q1D escape artifact currently clears its "
            "branch gate."
        ),
        recommended_next=(
            "Unless a Q1B deployment appears, the next autonomous run should "
            "leave Q1 and attack thermodynamic arrow or spacetime "
            "reconstruction with the same absorber discipline."
        ),
    )


def branch_audit_to_dict(audit: BranchAudit) -> dict[str, object]:
    return {
        "branch": audit.branch,
        "classification": audit.classification,
        "active_internal_route": audit.active_internal_route,
        "live_evidence": audit.live_evidence,
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def t140_result_to_dict(result: T140Result) -> dict[str, object]:
    return {
        "audits": [branch_audit_to_dict(audit) for audit in result.audits],
        "internal_q1_upgrade_available": result.internal_q1_upgrade_available,
        "q1b_is_only_external_experimental_path": (
            result.q1b_is_only_external_experimental_path
        ),
        "overall_recommendation": result.overall_recommendation,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t140_result_to_dict(run_t140_analysis()), indent=2))
