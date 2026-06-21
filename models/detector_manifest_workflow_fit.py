"""T138: workflow-fit audit for the T136 detector manifest.

T136 made the detector preregistration manifest executable. T138 asks whether
that object can be filled by a concrete lab workflow without turning Q1B into
post hoc self-certification.

The positive case here is only a scaffold fit. It is not detector evidence,
does not score D1, and does not promote Q1B. Real event rows and signatures
remain absent.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from models.detector_authority_domain_bound import DOMAINS
from models.detector_dry_run_packet_skeleton import (
    locked_detector_dry_run_packet_skeleton,
)
from models.detector_packet_tiered_minimality import (
    CLAIM_REVIEW_EXTENSION_FIELDS,
    PROVISIONAL_ADMISSION_FIELDS,
)
from models.detector_preregistration_manifest import (
    DetectorPreregistrationManifest,
    PreregistrationManifestAudit,
    WrapperFieldCommitment,
    _field_commitments,
    _manifest,
    audit_preregistration_manifest,
)
from models.real_detector_packet_schema_audit import SCHEMA_FIELDS


@dataclass(frozen=True)
class ManifestTemplateLine:
    section: str
    item: str
    required_for_tier: str
    fill_before_event: bool
    acceptable_fill: str
    null_if_missing: str


@dataclass(frozen=True)
class LabWorkflow:
    name: str
    workflow_kind: str
    claimed_tier: str
    wrapper_fields_available: tuple[str, ...]
    authority_partition: tuple[tuple[str, ...], ...]
    registered_before_first_event: bool
    no_data_analyzed_at_lock: bool
    raw_payload_commitment_kind: str
    manifest_hash_bound: bool
    purpose: str


@dataclass(frozen=True)
class WorkflowFitAudit:
    workflow_name: str
    workflow_kind: str
    claimed_tier: str
    max_certifiable_tier: str
    claimed_tier_admissible: bool
    verdict: str
    t136_failure_reasons: tuple[str, ...]
    missing_template_items: tuple[str, ...]
    authority_partition_admissible: bool
    predata_boundary_respected: bool
    wrapper_commitments_valid: bool
    manifest_hash_valid: bool
    interpretation: str


@dataclass(frozen=True)
class T138Result:
    template: tuple[ManifestTemplateLine, ...]
    audits: tuple[WorkflowFitAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def t136_human_fillable_template() -> tuple[ManifestTemplateLine, ...]:
    packet = locked_detector_dry_run_packet_skeleton()
    lines = [
        ManifestTemplateLine(
            section="run_identity",
            item="run_id",
            required_for_tier="raw_log_preservation",
            fill_before_event=True,
            acceptable_fill="Stable run/session identifier shared by every table.",
            null_if_missing="Rows cannot be joined to a frozen event collection.",
        ),
        ManifestTemplateLine(
            section="run_identity",
            item="claimed_tier",
            required_for_tier="raw_log_preservation",
            fill_before_event=True,
            acceptable_fill=(
                "One of raw_log_preservation, provisional_admission, claim_review."
            ),
            null_if_missing="Later tier upgrades are post hoc.",
        ),
        ManifestTemplateLine(
            section="run_identity",
            item="first_event_not_before",
            required_for_tier="raw_log_preservation",
            fill_before_event=True,
            acceptable_fill="Timestamp later than manifest registration.",
            null_if_missing="The manifest cannot prove it was locked pre-data.",
        ),
        ManifestTemplateLine(
            section="t97_tables",
            item="table_hashes",
            required_for_tier="raw_log_preservation",
            fill_before_event=True,
            acceptable_fill=(
                "Schema hash and empty-export checksum for "
                + ", ".join(table.table_name for table in packet.tables)
                + "."
            ),
            null_if_missing="The raw-log scaffold can drift during collection.",
        ),
        ManifestTemplateLine(
            section="authority",
            item="authority_partition",
            required_for_tier="provisional_admission",
            fill_before_event=True,
            acceptable_fill=(
                "At least four T100-compatible domains, with trust_auditor "
                "independent of analysis, instrument, control, and archive roles."
            ),
            null_if_missing="The packet collapses into self-certification.",
        ),
        ManifestTemplateLine(
            section="wrapper",
            item="provisional_fields",
            required_for_tier="provisional_admission",
            fill_before_event=True,
            acceptable_fill=", ".join(PROVISIONAL_ADMISSION_FIELDS),
            null_if_missing="The packet cannot enter provisional review.",
        ),
        ManifestTemplateLine(
            section="wrapper",
            item="claim_review_fields",
            required_for_tier="claim_review",
            fill_before_event=True,
            acceptable_fill=", ".join(CLAIM_REVIEW_EXTENSION_FIELDS),
            null_if_missing="The packet can at most be provisionally admitted.",
        ),
        ManifestTemplateLine(
            section="payload_boundary",
            item="raw_measurement_payload",
            required_for_tier="provisional_admission",
            fill_before_event=True,
            acceptable_fill="Export-rule commitment only; no observed payload values.",
            null_if_missing=(
                "Pre-known detector outcomes invalidate the preregistration boundary."
            ),
        ),
        ManifestTemplateLine(
            section="integrity",
            item="manifest_hash",
            required_for_tier="raw_log_preservation",
            fill_before_event=True,
            acceptable_fill="Top-level hash binding tables, wrappers, tier, and authority.",
            null_if_missing="The manifest contents are not fixed.",
        ),
    ]
    return tuple(lines)


def workflow_fixtures() -> tuple[LabWorkflow, ...]:
    return (
        LabWorkflow(
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
                "A concrete common workflow shape: one optical coincidence lab "
                "collects time tags, keeps calibration notes, signs exports, and "
                "assembles review material after seeing the run."
            ),
        ),
        LabWorkflow(
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
                "A repaired single-lab workflow that locks fields pre-data and "
                "uses a public archive, but still merges analysis with control "
                "design and archive custody with trust audit."
            ),
        ),
        LabWorkflow(
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
                "A minimal non-null scaffold: independent analysis governance, "
                "instrument operation, control design, archive custody, and trust "
                "audit all sign the manifest before event collection."
            ),
        ),
        LabWorkflow(
            name="federated_but_preknown_payload_workflow",
            workflow_kind="outcome_smuggling_control",
            claimed_tier="claim_review",
            wrapper_fields_available=SCHEMA_FIELDS,
            authority_partition=tuple((domain,) for domain in DOMAINS),
            registered_before_first_event=True,
            no_data_analyzed_at_lock=True,
            raw_payload_commitment_kind="observed_value_commitment",
            manifest_hash_bound=True,
            purpose=(
                "A hostile control: authority and timing are clean, but the "
                "manifest claims observed payload values instead of an export rule."
            ),
        ),
    )


def manifest_from_workflow(workflow: LabWorkflow) -> DetectorPreregistrationManifest:
    packet = locked_detector_dry_run_packet_skeleton()
    registered_at = (
        packet.registered_at
        if workflow.registered_before_first_event
        else "2026-06-22T00:00:00Z"
    )
    manifest = _manifest(
        name=workflow.name,
        packet=packet,
        claimed_tier=workflow.claimed_tier,
        wrapper_field_commitments=_workflow_field_commitments(workflow),
        authority_partition=workflow.authority_partition,
        registered_at=registered_at,
        first_event_not_before=packet.first_event_not_before,
        no_data_analyzed=workflow.no_data_analyzed_at_lock,
        purpose=workflow.purpose,
    )
    if not workflow.manifest_hash_bound:
        return replace(manifest, manifest_hash="0" * 64)
    return manifest


def audit_workflow_fit(workflow: LabWorkflow) -> WorkflowFitAudit:
    t136_audit = audit_preregistration_manifest(manifest_from_workflow(workflow))
    missing = _missing_template_items(t136_audit)
    verdict = _workflow_verdict(t136_audit)
    return WorkflowFitAudit(
        workflow_name=workflow.name,
        workflow_kind=workflow.workflow_kind,
        claimed_tier=workflow.claimed_tier,
        max_certifiable_tier=t136_audit.max_certifiable_tier,
        claimed_tier_admissible=t136_audit.claimed_tier_admissible,
        verdict=verdict,
        t136_failure_reasons=t136_audit.failure_reasons,
        missing_template_items=missing,
        authority_partition_admissible=t136_audit.authority_partition_admissible,
        predata_boundary_respected=t136_audit.predata_boundary_respected,
        wrapper_commitments_valid=t136_audit.wrapper_commitments_valid,
        manifest_hash_valid=t136_audit.manifest_hash_valid,
        interpretation=_workflow_interpretation(workflow, t136_audit, verdict),
    )


def run_t138_analysis() -> T138Result:
    audits = tuple(audit_workflow_fit(workflow) for workflow in workflow_fixtures())
    audit_map = {audit.workflow_name: audit for audit in audits}

    if audit_map["common_single_lab_photonic_coincidence_workflow"].claimed_tier_admissible:
        raise AssertionError("common single-lab workflow must not clear T136")
    if audit_map["predata_single_lab_with_public_archive_workflow"].claimed_tier_admissible:
        raise AssertionError("single-lab archive workflow must fail authority partition")
    if not audit_map["federated_predata_claim_review_workflow"].claimed_tier_admissible:
        raise AssertionError("federated predata scaffold must clear T136 as a scaffold")
    if audit_map["federated_but_preknown_payload_workflow"].claimed_tier_admissible:
        raise AssertionError("pre-known payload control must fail")

    return T138Result(
        template=t136_human_fillable_template(),
        audits=audits,
        strongest_claim=(
            "T138 converts T136 into a human-fillable workflow gate. A common "
            "single-lab photonic coincidence workflow is null for Q1B, even if "
            "it has time tags and signed exports, because it is post hoc and "
            "authority-collapsed. A federated pre-data workflow can clear the "
            "manifest only as an evidence scaffold, not as detector support."
        ),
        improved=(
            "The detector branch now has a reviewer-facing template and a "
            "workflow-fit audit. Review can reject concrete lab plans before "
            "event collection instead of debating detector interpretations after "
            "data are seen."
        ),
        weakened=(
            "This weakens Q1B against realistic small-lab deployment stories. "
            "Pre-data table hashes and signatures are not enough when analysis, "
            "control design, archive custody, and trust audit collapse into the "
            "same authority structure."
        ),
        falsification_condition=(
            "T138 fails if a common single-lab or three-domain workflow can "
            "legitimately claim provisional or claim-review status without the "
            "T100-compatible authority split, or if the federated scaffold cannot "
            "actually be signed before data despite satisfying the manifest fields."
        ),
        q1b_update=(
            "Q1B remains externally blocked. Its current non-null path is no "
            "longer 'a lab with time tags'; it is a federated preregistration "
            "scaffold with T136 fields and T100-compatible authorities fixed "
            "before the first event."
        ),
        claim_ledger_update=(
            "Add T138 to Q1B: the human-fillable manifest template rejects the "
            "common single-lab photonic workflow and a public-archive repair with "
            "merged authorities. Only a federated pre-data scaffold clears T136, "
            "and even that is not detector evidence until real rows populate the "
            "bound packet."
        ),
        open_blocker=(
            "No named real lab has agreed to fill and sign the federated T138/T136 "
            "template before detector event collection."
        ),
        recommended_next=(
            "Send the T138 template to one realistic detector group or map one "
            "named public experiment against it. If the group cannot provide "
            "independent archive and trust-audit roles pre-data, demote Q1B below "
            "active quantum-measurement work."
        ),
    )


def t138_result_to_dict(result: T138Result) -> dict[str, object]:
    return {
        "template": [
            {
                "section": line.section,
                "item": line.item,
                "required_for_tier": line.required_for_tier,
                "fill_before_event": line.fill_before_event,
                "acceptable_fill": line.acceptable_fill,
                "null_if_missing": line.null_if_missing,
            }
            for line in result.template
        ],
        "audits": [
            {
                "workflow_name": audit.workflow_name,
                "workflow_kind": audit.workflow_kind,
                "claimed_tier": audit.claimed_tier,
                "max_certifiable_tier": audit.max_certifiable_tier,
                "claimed_tier_admissible": audit.claimed_tier_admissible,
                "verdict": audit.verdict,
                "t136_failure_reasons": list(audit.t136_failure_reasons),
                "missing_template_items": list(audit.missing_template_items),
                "authority_partition_admissible": audit.authority_partition_admissible,
                "predata_boundary_respected": audit.predata_boundary_respected,
                "wrapper_commitments_valid": audit.wrapper_commitments_valid,
                "manifest_hash_valid": audit.manifest_hash_valid,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1b_update": result.q1b_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _workflow_field_commitments(
    workflow: LabWorkflow,
) -> tuple[WrapperFieldCommitment, ...]:
    commitments = _field_commitments(tuple(workflow.wrapper_fields_available))
    if workflow.raw_payload_commitment_kind == "export_rule_commitment":
        return commitments
    return tuple(
        replace(field, commitment_kind=workflow.raw_payload_commitment_kind)
        if field.field_name == "raw_measurement_payload"
        else field
        for field in commitments
    )


def _missing_template_items(
    audit: PreregistrationManifestAudit,
) -> tuple[str, ...]:
    missing: list[str] = []
    if not audit.t97_table_commitments_valid:
        missing.append("t97_tables:table_hashes")
    if not audit.authority_partition_admissible:
        missing.append("authority:authority_partition")
    if not audit.predata_boundary_respected:
        missing.append("run_identity:first_event_not_before")
    if not audit.manifest_hash_valid:
        missing.append("integrity:manifest_hash")
    for field in audit.missing_provisional_fields:
        missing.append(f"wrapper:{field}")
    if audit.claimed_tier == "claim_review":
        for field in audit.missing_claim_review_fields:
            missing.append(f"wrapper:{field}")
    if "predata_manifest_claims_observed_payload_values" in audit.failure_reasons:
        missing.append("payload_boundary:raw_measurement_payload_export_rule")
    if "invalid_or_undeclared_claimed_tier" in audit.failure_reasons:
        missing.append("run_identity:claimed_tier")
    return tuple(dict.fromkeys(missing))


def _workflow_verdict(audit: PreregistrationManifestAudit) -> str:
    if audit.claimed_tier_admissible and audit.max_certifiable_tier == "claim_review":
        return "claim_review_scaffold_fit"
    if audit.claimed_tier_admissible:
        return "provisional_scaffold_fit"
    if audit.max_certifiable_tier != "none":
        return "tier_overclaim_or_template_gap"
    return "workflow_null_for_q1b"


def _workflow_interpretation(
    workflow: LabWorkflow,
    audit: PreregistrationManifestAudit,
    verdict: str,
) -> str:
    if verdict == "claim_review_scaffold_fit":
        return (
            f"{workflow.name} clears the T136 claim-review manifest as a "
            "pre-data scaffold only. It still needs real event rows and signed "
            "packet population before it can count as detector evidence."
        )
    if verdict == "provisional_scaffold_fit":
        return (
            f"{workflow.name} clears provisional intake only; claim-review "
            "rights remain unavailable until witness, reconstruction, and "
            "challenge fields are frozen."
        )
    if not audit.predata_boundary_respected:
        return (
            f"{workflow.name} is null for Q1B because the manifest is not locked "
            "before the first event and data boundary."
        )
    if not audit.authority_partition_admissible:
        return (
            f"{workflow.name} is null for Q1B under T100: the authority split "
            "does not prevent self-certification."
        )
    if "predata_manifest_claims_observed_payload_values" in audit.failure_reasons:
        return (
            f"{workflow.name} is null because it tries to commit observed "
            "payload values before the event boundary."
        )
    return f"{workflow.name} fails T136: {', '.join(audit.failure_reasons)}."


if __name__ == "__main__":
    import json

    print(json.dumps(t138_result_to_dict(run_t138_analysis()), indent=2))
