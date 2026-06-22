"""T169: deployment-archetype screen for the Q1B detector route.

T138 reduced Q1B to a pre-data manifest scaffold, and T161 showed that nominal
federation can still collapse through shared critical control roots. The
remaining ambiguity is practical rather than formal: what deployment
archetypes are still alive once both gates are applied together?

This module answers that question with a bounded finite audit. It does not
produce detector evidence and does not claim a real lab currently satisfies
the surviving archetype.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.detector_authority_domain_bound import DOMAINS
from models.detector_control_root_independence import (
    ControlRootAssignment,
    ControlRootAudit,
    ControlRootProfile,
    audit_control_root_profile,
)
from models.detector_manifest_workflow_fit import (
    LabWorkflow,
    WorkflowFitAudit,
    audit_workflow_fit,
)
from models.detector_packet_tiered_minimality import PROVISIONAL_ADMISSION_FIELDS
from models.real_detector_packet_schema_audit import SCHEMA_FIELDS


@dataclass(frozen=True)
class RowReviewCommitment:
    commitment_kind: str
    event_rows_reviewable: bool
    independently_escrowed: bool
    schema_bound_after_collection: bool
    purpose: str


@dataclass(frozen=True)
class DeploymentArchetype:
    archetype_id: str
    workflow: LabWorkflow
    control_profile: ControlRootProfile
    row_commitment: RowReviewCommitment
    purpose: str


@dataclass(frozen=True)
class DeploymentArchetypeAudit:
    archetype_id: str
    workflow_verdict: str
    control_verdict: str
    row_commitment_kind: str
    manifest_claim_review_ready: bool
    effective_root_partition_admissible: bool
    event_rows_reviewable: bool
    independently_escrowed: bool
    schema_bound_after_collection: bool
    classification: str
    required_next: str
    interpretation: str


@dataclass(frozen=True)
class T169Result:
    audits: tuple[DeploymentArchetypeAudit, ...]
    null_predata_or_authority_archetypes: tuple[str, ...]
    null_hidden_root_merge_archetypes: tuple[str, ...]
    scaffold_only_archetypes: tuple[str, ...]
    live_external_candidate_archetypes: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def deployment_archetypes() -> tuple[DeploymentArchetype, ...]:
    federated_claim_review = LabWorkflow(
        name="federated_predata_claim_review_workflow",
        workflow_kind="federated_preregistration_scaffold",
        claimed_tier="claim_review",
        wrapper_fields_available=SCHEMA_FIELDS,
        authority_partition=tuple((domain,) for domain in DOMAINS),
        registered_before_first_event=True,
        no_data_analyzed_at_lock=True,
        raw_payload_commitment_kind="export_rule_commitment",
        manifest_hash_bound=True,
        purpose=(
            "Independent governance, instrument, control, archive, and trust "
            "roles sign a claim-review manifest before event collection."
        ),
    )
    return (
        DeploymentArchetype(
            archetype_id="single_lab_posthoc_internal_pki",
            workflow=LabWorkflow(
                name="common_single_lab_photonic_coincidence_workflow",
                workflow_kind="single_lab_photon_counter",
                claimed_tier="claim_review",
                wrapper_fields_available=(
                    "detector_identity",
                    "run_session_id",
                    "causal_ordering_data",
                    "raw_measurement_payload",
                    "calibration_reference",
                    "provenance_chain",
                    "signatures",
                ),
                authority_partition=(tuple(DOMAINS),),
                registered_before_first_event=False,
                no_data_analyzed_at_lock=False,
                raw_payload_commitment_kind="export_rule_commitment",
                manifest_hash_bound=True,
                purpose=(
                    "One lab collects data, signs exports, and assembles the "
                    "review packet after seeing the run."
                ),
            ),
            control_profile=ControlRootProfile(
                name="single_domain_internal_pki",
                nominal_partition=(tuple(DOMAINS),),
                assignments=tuple(
                    ControlRootAssignment(
                        domain=domain,
                        capability_kind=kind,
                        root_id="root_single_lab_internal_pki",
                        critical=True,
                    )
                    for domain, kind in zip(
                        DOMAINS,
                        (
                            "manifest_registration",
                            "archive_write",
                            "audit_attestation",
                            "publication_release",
                            "revocation_registry",
                        ),
                        strict=True,
                    )
                ),
                purpose=(
                    "A single internal PKI signs manifest, archive, audit, "
                    "publication, and revocation operations."
                ),
            ),
            row_commitment=RowReviewCommitment(
                commitment_kind="summary_only_after_run",
                event_rows_reviewable=False,
                independently_escrowed=False,
                schema_bound_after_collection=False,
                purpose="Only dashboard summaries are promised after the run.",
            ),
            purpose=(
                "The common small-lab story: accurate hardware, signed exports, "
                "but no pre-data separation."
            ),
        ),
        DeploymentArchetype(
            archetype_id="predata_single_lab_public_archive_repair",
            workflow=LabWorkflow(
                name="predata_single_lab_with_public_archive_workflow",
                workflow_kind="single_lab_plus_archive",
                claimed_tier="provisional_admission",
                wrapper_fields_available=PROVISIONAL_ADMISSION_FIELDS,
                authority_partition=(
                    ("analysis_governor", "control_designer"),
                    ("instrument_operator",),
                    ("archive_custodian", "trust_auditor"),
                ),
                registered_before_first_event=True,
                no_data_analyzed_at_lock=True,
                raw_payload_commitment_kind="export_rule_commitment",
                manifest_hash_bound=True,
                purpose=(
                    "A repaired single-lab workflow that locks fields pre-data "
                    "and writes into a public archive."
                ),
            ),
            control_profile=ControlRootProfile(
                name="three_domain_public_archive_repair_roots",
                nominal_partition=(
                    ("analysis_governor", "control_designer"),
                    ("instrument_operator",),
                    ("archive_custodian", "trust_auditor"),
                ),
                assignments=(
                    ControlRootAssignment(
                        "analysis_governor",
                        "manifest_registration",
                        "root_manifest_governance",
                        True,
                    ),
                    ControlRootAssignment(
                        "control_designer",
                        "publication_release",
                        "root_manifest_governance",
                        True,
                    ),
                    ControlRootAssignment(
                        "instrument_operator",
                        "archive_write",
                        "root_archive_instrument",
                        True,
                    ),
                    ControlRootAssignment(
                        "archive_custodian",
                        "revocation_registry",
                        "root_shared_archive_audit_hsm",
                        True,
                    ),
                    ControlRootAssignment(
                        "trust_auditor",
                        "audit_attestation",
                        "root_shared_archive_audit_hsm",
                        True,
                    ),
                ),
                purpose=(
                    "A public-archive repair where archive custody and trust "
                    "audit still collapse operationally."
                ),
            ),
            row_commitment=RowReviewCommitment(
                commitment_kind="public_archive_summary_and_selected_rows",
                event_rows_reviewable=False,
                independently_escrowed=True,
                schema_bound_after_collection=True,
                purpose=(
                    "The archive promises immutable exports, but not full "
                    "reviewable event rows."
                ),
            ),
            purpose=(
                "A common attempted repair: add pre-data locking and a public "
                "archive without creating a real trust-audit split."
            ),
        ),
        DeploymentArchetype(
            archetype_id="nominal_federation_shared_archive_audit_hsm",
            workflow=federated_claim_review,
            control_profile=ControlRootProfile(
                name="five_domain_shared_archive_audit_hsm",
                nominal_partition=tuple((domain,) for domain in DOMAINS),
                assignments=(
                    ControlRootAssignment(
                        "analysis_governor",
                        "manifest_registration",
                        "root_manifest_governance",
                        True,
                    ),
                    ControlRootAssignment(
                        "instrument_operator",
                        "archive_write",
                        "root_archive_instrument",
                        True,
                    ),
                    ControlRootAssignment(
                        "control_designer",
                        "publication_release",
                        "root_publish_control",
                        True,
                    ),
                    ControlRootAssignment(
                        "archive_custodian",
                        "archive_write",
                        "root_shared_archive_audit_hsm",
                        True,
                    ),
                    ControlRootAssignment(
                        "trust_auditor",
                        "audit_attestation",
                        "root_shared_archive_audit_hsm",
                        True,
                    ),
                ),
                purpose=(
                    "A nominal federation that shares the archive/audit HSM "
                    "despite separate role labels."
                ),
            ),
            row_commitment=RowReviewCommitment(
                commitment_kind="reviewable_event_rows_promised",
                event_rows_reviewable=True,
                independently_escrowed=True,
                schema_bound_after_collection=True,
                purpose="Event rows would be reviewable if the root split were real.",
            ),
            purpose=(
                "A role-clean collaboration that still hides a critical "
                "archive/audit merge."
            ),
        ),
        DeploymentArchetype(
            archetype_id="nominal_federation_shared_release_root",
            workflow=federated_claim_review,
            control_profile=ControlRootProfile(
                name="five_domain_shared_governance_archive_release_root",
                nominal_partition=tuple((domain,) for domain in DOMAINS),
                assignments=(
                    ControlRootAssignment(
                        "analysis_governor",
                        "manifest_registration",
                        "root_shared_release_gate",
                        True,
                    ),
                    ControlRootAssignment(
                        "archive_custodian",
                        "publication_release",
                        "root_shared_release_gate",
                        True,
                    ),
                    ControlRootAssignment(
                        "control_designer",
                        "archive_write",
                        "root_archive_control",
                        True,
                    ),
                    ControlRootAssignment(
                        "instrument_operator",
                        "archive_write",
                        "root_archive_instrument",
                        True,
                    ),
                    ControlRootAssignment(
                        "trust_auditor",
                        "audit_attestation",
                        "root_audit_external",
                        True,
                    ),
                ),
                purpose=(
                    "A consortium where governance and archive publication share "
                    "the same critical release root."
                ),
            ),
            row_commitment=RowReviewCommitment(
                commitment_kind="reviewable_event_rows_promised",
                event_rows_reviewable=True,
                independently_escrowed=True,
                schema_bound_after_collection=True,
                purpose="Rows are promised, but the release root is shared.",
            ),
            purpose=(
                "A realistic collaboration-management loophole: nominally "
                "separate roles but one release gate."
            ),
        ),
        DeploymentArchetype(
            archetype_id="federated_independent_roots_private_escrow",
            workflow=federated_claim_review,
            control_profile=ControlRootProfile(
                name="five_domain_distinct_critical_roots_with_shared_dashboard",
                nominal_partition=tuple((domain,) for domain in DOMAINS),
                assignments=(
                    ControlRootAssignment(
                        "analysis_governor",
                        "manifest_registration",
                        "root_manifest_governance",
                        True,
                    ),
                    ControlRootAssignment(
                        "archive_custodian",
                        "archive_write",
                        "root_archive_custodian",
                        True,
                    ),
                    ControlRootAssignment(
                        "control_designer",
                        "publication_release",
                        "root_publish_control",
                        True,
                    ),
                    ControlRootAssignment(
                        "instrument_operator",
                        "revocation_registry",
                        "root_revocation_instrument",
                        True,
                    ),
                    ControlRootAssignment(
                        "trust_auditor",
                        "audit_attestation",
                        "root_audit_external",
                        True,
                    ),
                    ControlRootAssignment(
                        "analysis_governor",
                        "dashboard_observability",
                        "root_shared_dashboard",
                        False,
                    ),
                    ControlRootAssignment(
                        "trust_auditor",
                        "dashboard_observability",
                        "root_shared_dashboard",
                        False,
                    ),
                ),
                purpose=(
                    "A clean critical-root split that still shares a "
                    "noncritical status dashboard."
                ),
            ),
            row_commitment=RowReviewCommitment(
                commitment_kind="immutable_private_escrow_only",
                event_rows_reviewable=False,
                independently_escrowed=True,
                schema_bound_after_collection=True,
                purpose=(
                    "Event rows are escrowed immutably, but outside review is "
                    "limited to proofs or summaries."
                ),
            ),
            purpose=(
                "A near-miss archetype: the pre-data packet and root split are "
                "honest, but the post-data row commitment is too weak."
            ),
        ),
        DeploymentArchetype(
            archetype_id="federated_independent_roots_reviewable_rows",
            workflow=federated_claim_review,
            control_profile=ControlRootProfile(
                name="five_domain_distinct_critical_roots_reviewable_rows",
                nominal_partition=tuple((domain,) for domain in DOMAINS),
                assignments=(
                    ControlRootAssignment(
                        "analysis_governor",
                        "manifest_registration",
                        "root_manifest_governance",
                        True,
                    ),
                    ControlRootAssignment(
                        "archive_custodian",
                        "archive_write",
                        "root_archive_custodian",
                        True,
                    ),
                    ControlRootAssignment(
                        "control_designer",
                        "publication_release",
                        "root_publish_control",
                        True,
                    ),
                    ControlRootAssignment(
                        "instrument_operator",
                        "revocation_registry",
                        "root_revocation_instrument",
                        True,
                    ),
                    ControlRootAssignment(
                        "trust_auditor",
                        "audit_attestation",
                        "root_audit_external",
                        True,
                    ),
                ),
                purpose=(
                    "A clean five-domain critical-root split with no hidden "
                    "critical merges."
                ),
            ),
            row_commitment=RowReviewCommitment(
                commitment_kind="reviewable_event_rows_with_independent_escrow",
                event_rows_reviewable=True,
                independently_escrowed=True,
                schema_bound_after_collection=True,
                purpose=(
                    "The bound packet is reviewable at event level after "
                    "collection without schema drift."
                ),
            ),
            purpose=(
                "The narrow surviving external candidate class for Q1B."
            ),
        ),
    )


def audit_deployment_archetype(
    archetype: DeploymentArchetype,
) -> DeploymentArchetypeAudit:
    workflow_audit = audit_workflow_fit(archetype.workflow)
    control_audit = audit_control_root_profile(archetype.control_profile)
    classification = _classification(archetype, workflow_audit, control_audit)
    return DeploymentArchetypeAudit(
        archetype_id=archetype.archetype_id,
        workflow_verdict=workflow_audit.verdict,
        control_verdict=control_audit.verdict,
        row_commitment_kind=archetype.row_commitment.commitment_kind,
        manifest_claim_review_ready=workflow_audit.claimed_tier_admissible,
        effective_root_partition_admissible=control_audit.effective_admissible,
        event_rows_reviewable=archetype.row_commitment.event_rows_reviewable,
        independently_escrowed=archetype.row_commitment.independently_escrowed,
        schema_bound_after_collection=archetype.row_commitment.schema_bound_after_collection,
        classification=classification,
        required_next=_required_next(classification),
        interpretation=_interpretation(
            archetype,
            workflow_audit,
            control_audit,
            classification,
        ),
    )


def run_t169_analysis() -> T169Result:
    audits = tuple(
        audit_deployment_archetype(archetype) for archetype in deployment_archetypes()
    )
    null_predata = tuple(
        audit.archetype_id
        for audit in audits
        if audit.classification == "null_predata_manifest_or_nominal_authority_failure"
    )
    null_hidden_root = tuple(
        audit.archetype_id
        for audit in audits
        if audit.classification == "null_hidden_control_root_merge"
    )
    scaffold_only = tuple(
        audit.archetype_id
        for audit in audits
        if audit.classification.startswith("scaffold_only_")
    )
    live_candidates = tuple(
        audit.archetype_id
        for audit in audits
        if audit.classification == "live_external_q1b_candidate"
    )

    if "federated_independent_roots_reviewable_rows" not in live_candidates:
        raise AssertionError("one narrow live external candidate class should remain")
    if "single_lab_posthoc_internal_pki" not in null_predata:
        raise AssertionError("single-lab post hoc workflow must remain null")
    if "nominal_federation_shared_archive_audit_hsm" not in null_hidden_root:
        raise AssertionError("shared archive/audit root must remain null")
    if "federated_independent_roots_private_escrow" not in scaffold_only:
        raise AssertionError("private escrow without reviewable rows must be scaffold-only")

    return T169Result(
        audits=audits,
        null_predata_or_authority_archetypes=null_predata,
        null_hidden_root_merge_archetypes=null_hidden_root,
        scaffold_only_archetypes=scaffold_only,
        live_external_candidate_archetypes=live_candidates,
        strongest_claim=(
            "After T138 and T161 are composed, Q1B has only one surviving "
            "deployment archetype family: a pre-data claim-review federation "
            "with an admissible effective authority partition, distinct critical "
            "control roots, and a binding commitment to reviewable event-level "
            "rows. Single-lab, public-archive-repair, and nominal-federation "
            "stories are null; private escrow without reviewable rows is only "
            "scaffold."
        ),
        improved=(
            "T169 turns the detector handoff from an abstract federation ask "
            "into a concrete archetype census. Future Q1B discussions can now "
            "say exactly which organizational shapes are dead, which are "
            "scaffold-only, and which narrow class is still worth asking a lab "
            "to sign."
        ),
        weakened=(
            "This weakens Q1B further as an autonomous internal program. Most "
            "plausible workflow stories fail before detector physics is even "
            "relevant, and even a clean pre-data federation is null unless it "
            "also commits to later reviewable event rows."
        ),
        falsification_condition=(
            "T169 fails if a workflow lacking either a T138-valid pre-data "
            "manifest, a T161-valid effective authority partition, or a "
            "reviewable event-level row commitment should nevertheless count as "
            "a live Q1B deployment archetype."
        ),
        q1b_update=(
            "Q1B remains externally blocked. T169 narrows the surviving route "
            "to one external candidate class: pre-data claim-review manifest, "
            "independent effective control roots, and later reviewable "
            "event-level packet rows without schema drift."
        ),
        claim_ledger_update=(
            "Add T169 to Q1B: the deployment frontier is no longer generic "
            "'federated detector provenance'. Single-lab, public-archive "
            "repair, and hidden-root federation archetypes are null; private "
            "escrow is scaffold-only; only a reviewable-row federation remains "
            "live as an external candidate."
        ),
        open_blocker=(
            "No named real detector group in the repo currently instantiates "
            "the lone surviving T169 archetype with a signed pre-data packet "
            "and a commitment to later reviewable event rows."
        ),
        recommended_next=(
            "Either map one named collaboration onto the surviving T169 "
            "archetype and ask for a signed pre-data manifest, or demote Q1B "
            "below the active frontier if no realistic group can accept the "
            "reviewable-row burden."
        ),
    )


def t169_result_to_dict(result: T169Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "archetype_id": audit.archetype_id,
                "workflow_verdict": audit.workflow_verdict,
                "control_verdict": audit.control_verdict,
                "row_commitment_kind": audit.row_commitment_kind,
                "manifest_claim_review_ready": audit.manifest_claim_review_ready,
                "effective_root_partition_admissible": audit.effective_root_partition_admissible,
                "event_rows_reviewable": audit.event_rows_reviewable,
                "independently_escrowed": audit.independently_escrowed,
                "schema_bound_after_collection": audit.schema_bound_after_collection,
                "classification": audit.classification,
                "required_next": audit.required_next,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "null_predata_or_authority_archetypes": list(
            result.null_predata_or_authority_archetypes
        ),
        "null_hidden_root_merge_archetypes": list(
            result.null_hidden_root_merge_archetypes
        ),
        "scaffold_only_archetypes": list(result.scaffold_only_archetypes),
        "live_external_candidate_archetypes": list(
            result.live_external_candidate_archetypes
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1b_update": result.q1b_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _classification(
    archetype: DeploymentArchetype,
    workflow_audit: WorkflowFitAudit,
    control_audit: ControlRootAudit,
) -> str:
    if not workflow_audit.claimed_tier_admissible:
        return "null_predata_manifest_or_nominal_authority_failure"
    if not control_audit.effective_admissible:
        return "null_hidden_control_root_merge"
    if not archetype.row_commitment.schema_bound_after_collection:
        return "scaffold_only_unbound_postdata_packet"
    if not archetype.row_commitment.event_rows_reviewable:
        return "scaffold_only_no_reviewable_event_rows"
    if not archetype.row_commitment.independently_escrowed:
        return "scaffold_only_self_certified_row_access"
    return "live_external_q1b_candidate"


def _required_next(classification: str) -> str:
    if classification == "null_predata_manifest_or_nominal_authority_failure":
        return "Repair the pre-data manifest and nominal authority partition before detector events."
    if classification == "null_hidden_control_root_merge":
        return "Separate the shared critical control roots or treat the workflow as self-certifying."
    if classification == "scaffold_only_unbound_postdata_packet":
        return "Bind the post-data packet to the precommitted schema and export rule."
    if classification == "scaffold_only_no_reviewable_event_rows":
        return "Commit to reviewable event-level rows rather than proofs, summaries, or private escrow."
    if classification == "scaffold_only_self_certified_row_access":
        return "Add independent escrow or external review rights over the event-level rows."
    return "Obtain a named signatory and actual pre-data manifest; no further internal toy model is needed."


def _interpretation(
    archetype: DeploymentArchetype,
    workflow_audit: WorkflowFitAudit,
    control_audit: ControlRootAudit,
    classification: str,
) -> str:
    if classification == "null_predata_manifest_or_nominal_authority_failure":
        return (
            f"{archetype.archetype_id} is null before root or detector-detail "
            f"questions matter: {workflow_audit.interpretation}"
        )
    if classification == "null_hidden_control_root_merge":
        return (
            f"{archetype.archetype_id} clears T138 only nominally, then fails "
            f"T161 because {control_audit.interpretation}"
        )
    if classification == "scaffold_only_unbound_postdata_packet":
        return (
            f"{archetype.archetype_id} has an honest pre-data packet and root "
            "split, but the post-data row object can still drift."
        )
    if classification == "scaffold_only_no_reviewable_event_rows":
        return (
            f"{archetype.archetype_id} remains scaffold-only because the event "
            "rows stay private or summary-level after collection."
        )
    if classification == "scaffold_only_self_certified_row_access":
        return (
            f"{archetype.archetype_id} keeps the row review path inside the same "
            "authority structure that claims admissibility."
        )
    return (
        f"{archetype.archetype_id} is the narrow surviving external candidate "
        "class. It still provides no evidence until a real group signs and "
        "populates the packet."
    )


if __name__ == "__main__":
    import json

    print(json.dumps(t169_result_to_dict(run_t169_analysis()), indent=2))
