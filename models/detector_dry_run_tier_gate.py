"""T134: T97 dry-run packet integration with T133 packet tiers.

T97 froze the raw-log scaffold for a future detector deployment. T133 then
showed that detector packets have three tiers: raw evidence preservation,
provisional admission, and claim-review readiness. This audit composes those
results and asks whether a T97 packet can honestly emit the T133 tier verdicts.

The main boundary is intentional: a row-filled T97 raw-log packet is necessary
but not sufficient. It still needs the T121/T123 packet wrapper fields before
it can clear provisional admission or claim-review readiness.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from models.detector_dry_run_packet_skeleton import (
    DetectorDryRunPacket,
    audit_detector_dry_run_packet,
    locked_detector_dry_run_packet_skeleton,
)
from models.detector_packet_tiered_minimality import (
    CLAIM_REVIEW_EXTENSION_FIELDS,
    PROVISIONAL_ADMISSION_FIELDS,
    RAW_IDENTITY_FIELDS,
    TieredPacketAudit,
    audit_packet_tiers,
)
from models.real_detector_packet_schema_audit import DetectorEvidencePacket
from models.real_run_raw_log_contract import REQUIRED_TABLE_COLUMNS
from models.same_payload_packet_foa_witness import (
    audit_packet_against_reference,
    reference_packet,
    same_payload_packet_variants,
)


FIELD_COVERAGE_BY_T97: dict[str, str] = {
    "detector_identity": "covered_by_event_time_tag_stream.detector_id",
    "run_session_id": "covered_by_preregistration_manifest.run_id",
    "causal_ordering_data": "covered_by_event_time_tag_stream_and_control_pair_manifest",
    "raw_measurement_payload": "missing_from_t97_raw_log_scaffold",
    "calibration_reference": "missing_from_t97_raw_log_scaffold",
    "provenance_chain": "partial_via_signature_log_ancestry_dag_and_trust_audit",
    "signatures": "covered_by_signature_verification_log",
    "authority_domains": "missing_from_t97_raw_log_scaffold",
    "publication_status": "missing_from_t97_raw_log_scaffold",
    "revocation_status": "missing_from_t97_raw_log_scaffold",
    "key_state": "missing_from_t97_raw_log_scaffold",
    "witness_references": "partial_via_control_and_challenge_tables",
    "reconstruction_paths": "missing_from_t97_raw_log_scaffold",
    "admissibility_tokens": "partial_via_policy_schema_and_demotion_hashes",
    "challenge_status": "missing_from_t97_raw_log_scaffold",
}


@dataclass(frozen=True)
class IntegratedDetectorTierCase:
    name: str
    t97_packet: DetectorDryRunPacket
    wrapper_packet: DetectorEvidencePacket | None
    claimed_tier_before_event: str
    purpose: str


@dataclass(frozen=True)
class IntegratedTierAudit:
    case_name: str
    claimed_tier_before_event: str
    t97_packet_name: str
    wrapper_packet_id: str | None
    t97_verdict: str
    t97_evidence_verdict: str
    t87_verdict_if_scored_now: str
    real_t97_rows_present: bool
    raw_log_scaffold_ready: bool
    raw_evidence_preserved: bool
    provisionally_admissible: bool
    claim_review_ready: bool
    missing_native_provisional_fields: tuple[str, ...]
    missing_native_claim_review_fields: tuple[str, ...]
    wrapper_changed_fields: tuple[str, ...]
    wrapper_provisional_failures: tuple[str, ...]
    wrapper_claim_review_failures: tuple[str, ...]
    blocking_reasons: tuple[str, ...]
    interpretation: str


@dataclass(frozen=True)
class T134Result:
    field_coverage_by_t97: dict[str, str]
    raw_identity_fields: tuple[str, ...]
    provisional_admission_fields: tuple[str, ...]
    claim_review_extension_fields: tuple[str, ...]
    audits: tuple[IntegratedTierAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def filled_t97_raw_log_packet() -> DetectorDryRunPacket:
    """T97-shaped packet after real rows have filled every locked table."""

    base = locked_detector_dry_run_packet_skeleton()
    filled_tables = tuple(
        replace(
            table,
            row_state="real_event_rows_present",
            real_rows_present=True,
        )
        for table in base.tables
    )
    return replace(
        base,
        tables=filled_tables,
        purpose=(
            "A T97 packet with real rows in every raw-log table, but without "
            "the T121/T133 evidence-wrapper fields."
        ),
    )


def integrated_detector_tier_cases() -> tuple[IntegratedDetectorTierCase, ...]:
    filled = filled_t97_raw_log_packet()
    variants = {packet.packet_id: packet for packet in same_payload_packet_variants()}
    return (
        IntegratedDetectorTierCase(
            name="locked_t97_predata_scaffold_only",
            t97_packet=locked_detector_dry_run_packet_skeleton(),
            wrapper_packet=None,
            claimed_tier_before_event="raw_log_scaffold",
            purpose="A locked T97 scaffold with no detector rows yet.",
        ),
        IntegratedDetectorTierCase(
            name="filled_t97_raw_log_only",
            t97_packet=filled,
            wrapper_packet=None,
            claimed_tier_before_event="provisional_admission",
            purpose=(
                "A hostile shortcut: real T97 rows exist, but the packet has "
                "no T121/T133 wrapper."
            ),
        ),
        IntegratedDetectorTierCase(
            name="filled_t97_with_reference_wrapper",
            t97_packet=filled,
            wrapper_packet=reference_packet(),
            claimed_tier_before_event="claim_review",
            purpose=(
                "Schema-integration target: real T97 rows plus a complete "
                "T121/T123 reference wrapper."
            ),
        ),
        IntegratedDetectorTierCase(
            name="filled_t97_missing_provenance_wrapper",
            t97_packet=filled,
            wrapper_packet=variants["missing_provenance_same_payload"],
            claimed_tier_before_event="provisional_admission",
            purpose="Same T97 rows, but the wrapper lacks packet provenance.",
        ),
        IntegratedDetectorTierCase(
            name="filled_t97_missing_witnesses_wrapper",
            t97_packet=filled,
            wrapper_packet=variants["missing_witnesses_same_payload"],
            claimed_tier_before_event="claim_review",
            purpose=(
                "Same T97 rows, wrapper clears provisional intake but lacks "
                "claim-review witnesses."
            ),
        ),
        IntegratedDetectorTierCase(
            name="filled_t97_open_challenge_wrapper",
            t97_packet=filled,
            wrapper_packet=variants["open_challenge_same_payload"],
            claimed_tier_before_event="claim_review",
            purpose=(
                "Same T97 rows, wrapper clears provisional intake but leaves "
                "the dispute state open."
            ),
        ),
    )


def audit_integrated_tier_case(case: IntegratedDetectorTierCase) -> IntegratedTierAudit:
    t97_audit = audit_detector_dry_run_packet(case.t97_packet)
    real_t97_rows_present = set(t97_audit.real_row_tables) == set(REQUIRED_TABLE_COLUMNS)
    raw_log_scaffold_ready = t97_audit.failure_reasons == ()
    wrapper_audit = _wrapper_tier_audit(case.wrapper_packet)

    raw_wrapper_ready = wrapper_audit.raw_evidence_preserved if wrapper_audit else False
    provisional_wrapper_ready = (
        wrapper_audit.provisionally_admissible if wrapper_audit else False
    )
    claim_wrapper_ready = wrapper_audit.claim_review_ready if wrapper_audit else False

    raw_evidence_preserved = (
        raw_log_scaffold_ready and real_t97_rows_present and raw_wrapper_ready
    )
    provisionally_admissible = raw_evidence_preserved and provisional_wrapper_ready
    claim_review_ready = provisionally_admissible and claim_wrapper_ready
    native_provisional_gaps = _native_t97_gaps(PROVISIONAL_ADMISSION_FIELDS)
    native_review_gaps = _native_t97_gaps(CLAIM_REVIEW_EXTENSION_FIELDS)
    blocking_reasons = _blocking_reasons(
        real_t97_rows_present=real_t97_rows_present,
        raw_log_scaffold_ready=raw_log_scaffold_ready,
        t97_failure_reasons=t97_audit.failure_reasons,
        wrapper_audit=wrapper_audit,
        has_wrapper=case.wrapper_packet is not None,
    )

    return IntegratedTierAudit(
        case_name=case.name,
        claimed_tier_before_event=case.claimed_tier_before_event,
        t97_packet_name=case.t97_packet.name,
        wrapper_packet_id=case.wrapper_packet.packet_id if case.wrapper_packet else None,
        t97_verdict=t97_audit.verdict,
        t97_evidence_verdict=t97_audit.evidence_verdict,
        t87_verdict_if_scored_now=t97_audit.t87_verdict_if_scored_now,
        real_t97_rows_present=real_t97_rows_present,
        raw_log_scaffold_ready=raw_log_scaffold_ready,
        raw_evidence_preserved=raw_evidence_preserved,
        provisionally_admissible=provisionally_admissible,
        claim_review_ready=claim_review_ready,
        missing_native_provisional_fields=native_provisional_gaps,
        missing_native_claim_review_fields=native_review_gaps,
        wrapper_changed_fields=(
            wrapper_audit.changed_packet_fields if wrapper_audit else ()
        ),
        wrapper_provisional_failures=(
            wrapper_audit.provisional_failures if wrapper_audit else ()
        ),
        wrapper_claim_review_failures=(
            wrapper_audit.claim_review_failures if wrapper_audit else ()
        ),
        blocking_reasons=blocking_reasons,
        interpretation=_interpretation(
            case,
            real_t97_rows_present,
            raw_log_scaffold_ready,
            wrapper_audit,
            provisionally_admissible,
            claim_review_ready,
            blocking_reasons,
        ),
    )


def run_t134_analysis() -> T134Result:
    audits = tuple(audit_integrated_tier_case(case) for case in integrated_detector_tier_cases())
    audit_map = {audit.case_name: audit for audit in audits}

    if audit_map["locked_t97_predata_scaffold_only"].provisionally_admissible:
        raise AssertionError("predata T97 scaffold must not be provisionally admitted")
    if audit_map["filled_t97_raw_log_only"].provisionally_admissible:
        raise AssertionError("T97 raw rows alone must not clear T133 provisional admission")
    if not audit_map["filled_t97_with_reference_wrapper"].claim_review_ready:
        raise AssertionError("complete wrapper integration target must clear all tiers")
    if audit_map["filled_t97_missing_provenance_wrapper"].provisionally_admissible:
        raise AssertionError("missing provenance must block provisional admission")
    if not audit_map["filled_t97_missing_witnesses_wrapper"].provisionally_admissible:
        raise AssertionError("missing witnesses should still clear provisional intake")
    if audit_map["filled_t97_missing_witnesses_wrapper"].claim_review_ready:
        raise AssertionError("missing witnesses must block claim-review readiness")
    if audit_map["filled_t97_open_challenge_wrapper"].claim_review_ready:
        raise AssertionError("open challenge must block claim-review readiness")

    return T134Result(
        field_coverage_by_t97=FIELD_COVERAGE_BY_T97,
        raw_identity_fields=RAW_IDENTITY_FIELDS,
        provisional_admission_fields=PROVISIONAL_ADMISSION_FIELDS,
        claim_review_extension_fields=CLAIM_REVIEW_EXTENSION_FIELDS,
        audits=audits,
        strongest_claim=(
            "T97 is necessary but not sufficient for Q1B tier admission. A "
            "schema-complete raw-log packet, even after real rows populate all "
            "T97 tables, cannot be treated as provisionally admissible or "
            "claim-review ready until a T121/T133 wrapper supplies raw payload, "
            "calibration, authority, publication, revocation, key-state, "
            "admissibility-token, reconstruction, and dispute fields."
        ),
        improved=(
            "T134 turns the T133 recommendation into an executable integration "
            "gate. Future detector packets now report three explicit tier "
            "outputs instead of one flat verdict: raw evidence preserved, "
            "provisionally admissible, and claim-review ready."
        ),
        weakened=(
            "This weakens the apparent sufficiency of the T97 dry-run scaffold. "
            "T97 raw-log readiness is only a lower layer; it must not be used "
            "as detector evidence admission or as a Q1B upgrade by itself."
        ),
        falsification_condition=(
            "T134 fails if real T97 rows alone are enough for provisional "
            "admission under the packet policy, or if a complete T121/T123 "
            "wrapper plus real T97 rows still cannot clear the three declared "
            "tiers without adding post hoc fields."
        ),
        q1b_update=(
            "Q1B remains externally blocked. The next admissible detector "
            "deployment must pre-register both the T97 raw-log scaffold and "
            "the T121/T133 wrapper, then state before events whether it claims "
            "only raw-log preservation, provisional admission, or full "
            "claim-review readiness."
        ),
        claim_ledger_update=(
            "Add T134 to Q1B: T97 raw-log packets now feed an explicit tier "
            "gate. Filled T97 rows are necessary but not sufficient; missing "
            "T121/T133 wrapper fields block provisional admission, while "
            "missing witnesses or open challenges preserve intake but block "
            "claim review."
        ),
        open_blocker=(
            "No real deployment has frozen the combined T97 raw-log packet and "
            "T121/T133 wrapper before data collection."
        ),
        recommended_next=(
            "Build a single pre-registration manifest that binds T97 table "
            "hashes, T121 packet-wrapper fields, T100 authority-domain evidence, "
            "and the claimed tier before the first detector event."
        ),
    )


def t134_result_to_dict(result: T134Result) -> dict[str, object]:
    return {
        "field_coverage_by_t97": result.field_coverage_by_t97,
        "raw_identity_fields": list(result.raw_identity_fields),
        "provisional_admission_fields": list(result.provisional_admission_fields),
        "claim_review_extension_fields": list(result.claim_review_extension_fields),
        "audits": [
            {
                "case_name": audit.case_name,
                "claimed_tier_before_event": audit.claimed_tier_before_event,
                "t97_packet_name": audit.t97_packet_name,
                "wrapper_packet_id": audit.wrapper_packet_id,
                "t97_verdict": audit.t97_verdict,
                "t97_evidence_verdict": audit.t97_evidence_verdict,
                "t87_verdict_if_scored_now": audit.t87_verdict_if_scored_now,
                "real_t97_rows_present": audit.real_t97_rows_present,
                "raw_log_scaffold_ready": audit.raw_log_scaffold_ready,
                "raw_evidence_preserved": audit.raw_evidence_preserved,
                "provisionally_admissible": audit.provisionally_admissible,
                "claim_review_ready": audit.claim_review_ready,
                "missing_native_provisional_fields": list(
                    audit.missing_native_provisional_fields
                ),
                "missing_native_claim_review_fields": list(
                    audit.missing_native_claim_review_fields
                ),
                "wrapper_changed_fields": list(audit.wrapper_changed_fields),
                "wrapper_provisional_failures": list(
                    audit.wrapper_provisional_failures
                ),
                "wrapper_claim_review_failures": list(
                    audit.wrapper_claim_review_failures
                ),
                "blocking_reasons": list(audit.blocking_reasons),
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


def _wrapper_tier_audit(packet: DetectorEvidencePacket | None) -> TieredPacketAudit | None:
    if packet is None:
        return None
    reference = reference_packet()
    packet_audit = audit_packet_against_reference(packet, reference)
    return audit_packet_tiers(packet_audit, reference.packet_id)


def _native_t97_gaps(fields: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(
        field
        for field in fields
        if not FIELD_COVERAGE_BY_T97[field].startswith("covered_by_")
    )


def _blocking_reasons(
    *,
    real_t97_rows_present: bool,
    raw_log_scaffold_ready: bool,
    t97_failure_reasons: tuple[str, ...],
    wrapper_audit: TieredPacketAudit | None,
    has_wrapper: bool,
) -> tuple[str, ...]:
    reasons: list[str] = []
    if not raw_log_scaffold_ready:
        reasons.extend(f"t97_failure:{reason}" for reason in t97_failure_reasons)
    if not real_t97_rows_present:
        reasons.append("no_real_t97_rows")
    if not has_wrapper:
        reasons.append("missing_t121_t133_packet_wrapper")
        reasons.extend(
            f"t97_native_gap:{field}"
            for field in _native_t97_gaps(PROVISIONAL_ADMISSION_FIELDS)
        )
        reasons.extend(
            f"t97_native_claim_review_gap:{field}"
            for field in _native_t97_gaps(CLAIM_REVIEW_EXTENSION_FIELDS)
        )
    elif wrapper_audit is not None:
        if not wrapper_audit.raw_evidence_preserved:
            reasons.append("wrapper_raw_evidence_not_preserved")
        if not wrapper_audit.provisionally_admissible:
            reasons.extend(
                f"wrapper_provisional_failure:{failure}"
                for failure in wrapper_audit.provisional_failures
            )
        if wrapper_audit.provisionally_admissible and not wrapper_audit.claim_review_ready:
            reasons.extend(
                f"wrapper_claim_review_failure:{failure}"
                for failure in wrapper_audit.claim_review_failures
            )
    return tuple(dict.fromkeys(reasons))


def _interpretation(
    case: IntegratedDetectorTierCase,
    real_t97_rows_present: bool,
    raw_log_scaffold_ready: bool,
    wrapper_audit: TieredPacketAudit | None,
    provisionally_admissible: bool,
    claim_review_ready: bool,
    blocking_reasons: tuple[str, ...],
) -> str:
    if claim_review_ready:
        return (
            "Real T97 rows plus the complete T121/T133 wrapper clear raw, "
            "provisional, and claim-review tiers as a schema-integration target."
        )
    if provisionally_admissible:
        return (
            "Real T97 rows plus this wrapper clear provisional intake, but "
            "claim-review readiness is withheld."
        )
    if wrapper_audit is None and real_t97_rows_present and raw_log_scaffold_ready:
        return (
            "The raw-log packet is filled, but T97 alone lacks the packet-wrapper "
            "fields required by T133; it is necessary but not sufficient."
        )
    if wrapper_audit is None:
        return (
            "The T97 scaffold is still pre-data and has no T121/T133 wrapper. "
            "It remains a packet-freezing artifact, not evidence admission."
        )
    return (
        f"{case.name} is blocked before provisional admission: "
        f"{', '.join(blocking_reasons)}."
    )
