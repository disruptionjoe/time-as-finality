"""T121: real detector evidence packet schema audit.

This module defines the minimal evidence object that must exist before the
detector raw-log route can reason about admissibility. It deliberately does not
score D1, upgrade Q1, or claim detector dynamics. The audit separates:

- raw measurement payload validity;
- packet admissibility for detector-branch evidence;
- future operation availability over the packet.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum


MIN_AUTHORITY_DOMAINS = 4


class PublicationStatus(Enum):
    PUBLISHED = "published"
    DELAYED = "delayed"
    WITHHELD = "withheld"


class RevocationStatus(Enum):
    ACTIVE = "active"
    REVOKED = "revoked"


class KeyState(Enum):
    CURRENT = "current"
    ROTATED_WITH_CONTINUITY_PROOF = "rotated_with_continuity_proof"
    COMPROMISED = "compromised"


class ChallengeStatus(Enum):
    NONE = "none"
    OPEN = "open"
    RESOLVED_UPHELD = "resolved_upheld"
    RESOLVED_REJECTED = "resolved_rejected"


class PacketVerdict(Enum):
    ADMISSIBLE = "admissible"
    INADMISSIBLE = "inadmissible"
    WITHHOLD = "withhold"


@dataclass(frozen=True)
class DetectorEvidencePacket:
    packet_id: str
    detector_identity: str | None
    run_session_id: str | None
    causal_ordering_data: tuple[str, ...]
    raw_measurement_payload: tuple[str, ...]
    calibration_reference: str | None
    provenance_chain: tuple[str, ...]
    signatures: tuple[str, ...]
    authority_domains: frozenset[str]
    publication_status: PublicationStatus
    revocation_status: RevocationStatus
    key_state: KeyState
    witness_references: tuple[str, ...]
    reconstruction_paths: tuple[str, ...]
    admissibility_tokens: frozenset[str]
    challenge_status: ChallengeStatus
    purpose: str


@dataclass(frozen=True)
class PacketAudit:
    packet_id: str
    raw_payload_valid: bool
    packet_verdict: PacketVerdict
    admissibility_failures: tuple[str, ...]
    future_operations: frozenset[str]
    missing_strict_fields: tuple[str, ...]
    failures_change_admissibility: tuple[str, ...]
    failures_change_future_operation_availability: tuple[str, ...]
    handled_by_existing_protocol_artifacts: tuple[str, ...]
    missing_schema_requirements_revealed: tuple[str, ...]
    explanation: str


@dataclass(frozen=True)
class T121Result:
    schema_fields: tuple[str, ...]
    strict_necessary_fields: tuple[str, ...]
    audits: tuple[PacketAudit, ...]
    strongest_claim: str
    fields_strictly_necessary: str
    failures_change_admissibility: str
    failures_change_future_operation_availability: str
    handled_by_existing_protocol_artifacts: str
    missing_schema_requirements: str
    claim_impact_recommendation: str
    recommended_next: str


SCHEMA_FIELDS: tuple[str, ...] = (
    "detector_identity",
    "run_session_id",
    "causal_ordering_data",
    "raw_measurement_payload",
    "calibration_reference",
    "provenance_chain",
    "signatures",
    "authority_domains",
    "publication_status",
    "revocation_status",
    "key_state",
    "witness_references",
    "reconstruction_paths",
    "admissibility_tokens",
    "challenge_status",
)

STRICT_NECESSARY_FIELDS: tuple[str, ...] = SCHEMA_FIELDS

REQUIRED_ADMISSIBILITY_TOKENS = frozenset(
    {
        "pre_registered_packet",
        "immutable_raw_export",
        "calibration_bound",
        "authority_separation",
        "signature_verified",
        "published_before_analysis",
        "revocation_checked",
        "key_continuity_checked",
        "challenge_window_declared",
    }
)

BASE_OPERATIONS = frozenset({"retain_raw_payload"})

ADMISSIBLE_OPERATIONS = frozenset(
    {
        "score_admissibility",
        "publish_packet",
        "verify_lineage",
        "reconstruct_event",
        "challenge_packet",
        "bind_calibration",
        "audit_authority",
        "use_for_detector_claim_review",
    }
)


def valid_packet() -> DetectorEvidencePacket:
    return DetectorEvidencePacket(
        packet_id="valid_packet",
        detector_identity="detector:hbt-stack-a",
        run_session_id="run:2026-06-20:001",
        causal_ordering_data=("event_time_tags", "white_rabbit_epoch", "sequence_counter"),
        raw_measurement_payload=("event:e1:+", "event:e2:-"),
        calibration_reference="calibration:cal-2026-06-20:signed",
        provenance_chain=("detector", "timing_export", "signed_archive", "public_mirror"),
        signatures=("sig:detector", "sig:timing", "sig:archive", "sig:auditor"),
        authority_domains=frozenset(
            {
                "instrument_operator",
                "control_designer",
                "archive_custodian",
                "trust_auditor",
            }
        ),
        publication_status=PublicationStatus.PUBLISHED,
        revocation_status=RevocationStatus.ACTIVE,
        key_state=KeyState.CURRENT,
        witness_references=("witness:control-pair", "witness:dag-edge", "witness:signature-log"),
        reconstruction_paths=("path:event-replay", "path:calibration-bind"),
        admissibility_tokens=REQUIRED_ADMISSIBILITY_TOKENS,
        challenge_status=ChallengeStatus.NONE,
        purpose="Complete minimal detector evidence packet.",
    )


def finite_packet_cases() -> tuple[DetectorEvidencePacket, ...]:
    base = valid_packet()
    return (
        base,
        replace(
            base,
            packet_id="missing_provenance",
            provenance_chain=(),
            admissibility_tokens=base.admissibility_tokens - {"signature_verified"},
            purpose="Raw data and signatures exist, but provenance chain is absent.",
        ),
        replace(
            base,
            packet_id="key_compromised",
            key_state=KeyState.COMPROMISED,
            purpose="Packet has raw data and signatures, but signing key is compromised.",
        ),
        replace(
            base,
            packet_id="revoked_authority",
            revocation_status=RevocationStatus.REVOKED,
            purpose="Authority domain was revoked after packet creation.",
        ),
        replace(
            base,
            packet_id="publication_delayed",
            publication_status=PublicationStatus.DELAYED,
            admissibility_tokens=base.admissibility_tokens - {"published_before_analysis"},
            purpose="Packet is complete but not published before analysis.",
        ),
        replace(
            base,
            packet_id="authority_domains_collapsed",
            authority_domains=frozenset({"single_lab_authority"}),
            admissibility_tokens=base.admissibility_tokens - {"authority_separation"},
            purpose="All packet roles collapse into one authority domain.",
        ),
        replace(
            base,
            packet_id="valid_raw_data_inadmissible_packet",
            signatures=(),
            witness_references=(),
            reconstruction_paths=(),
            admissibility_tokens=frozenset({"immutable_raw_export"}),
            purpose="Raw payload is valid but packet evidence wrappers are missing.",
        ),
        replace(
            base,
            packet_id="same_raw_data_reduced_future_rights",
            challenge_status=ChallengeStatus.OPEN,
            admissibility_tokens=base.admissibility_tokens - {"challenge_window_declared"},
            purpose=(
                "Same raw data and mostly admissible packet, but open dispute removes "
                "future claim-review operations."
            ),
        ),
    )


def validate_packet(packet: DetectorEvidencePacket) -> PacketAudit:
    missing = _missing_strict_fields(packet)
    raw_payload_valid = bool(
        packet.detector_identity
        and packet.run_session_id
        and packet.causal_ordering_data
        and packet.raw_measurement_payload
        and packet.calibration_reference
    )

    failures: list[str] = []
    handled: list[str] = []
    missing_schema: list[str] = []

    if missing:
        failures.append("missing_strict_packet_fields")
        missing_schema.append("strict_packet_fields_must_be_present")
    if not packet.provenance_chain:
        failures.append("missing_provenance_chain")
        handled.append("T87/T97 raw-log provenance contract")
    if not packet.signatures:
        failures.append("missing_signatures")
        handled.append("T87 signature verification log")
    if len(packet.authority_domains) < MIN_AUTHORITY_DOMAINS:
        failures.append("authority_domains_collapsed")
        handled.append("T100 authority-domain lower bound")
    if packet.publication_status != PublicationStatus.PUBLISHED:
        failures.append("packet_not_published_before_analysis")
        handled.append("T87/T97 preregistration and immutable export gate")
    if packet.revocation_status != RevocationStatus.ACTIVE:
        failures.append("authority_or_packet_revoked")
        missing_schema.append("revocation registry and check time must be part of packet")
    if packet.key_state == KeyState.COMPROMISED:
        failures.append("signing_key_compromised")
        missing_schema.append("key-compromise and rotation-continuity state must be explicit")
    if not packet.witness_references:
        failures.append("missing_witness_references")
        handled.append("T97 control and witness packet skeleton")
    if not packet.reconstruction_paths:
        failures.append("missing_reconstruction_paths")
        handled.append("T117/T119 future-operation and reconstruction-path audit")
    missing_tokens = REQUIRED_ADMISSIBILITY_TOKENS - packet.admissibility_tokens
    if missing_tokens:
        failures.append("missing_admissibility_tokens")
        handled.append("T78/T87/T97 admissibility gates")
    if packet.challenge_status == ChallengeStatus.OPEN:
        failures.append("open_challenge_or_dispute")
        missing_schema.append("challenge/dispute lifecycle must gate future use")

    if not raw_payload_valid:
        verdict = PacketVerdict.INADMISSIBLE
    elif packet.challenge_status == ChallengeStatus.OPEN:
        verdict = PacketVerdict.WITHHOLD
    elif failures:
        verdict = PacketVerdict.INADMISSIBLE
    else:
        verdict = PacketVerdict.ADMISSIBLE

    operations = _future_operations(packet, raw_payload_valid, verdict)
    return PacketAudit(
        packet_id=packet.packet_id,
        raw_payload_valid=raw_payload_valid,
        packet_verdict=verdict,
        admissibility_failures=tuple(failures),
        future_operations=operations,
        missing_strict_fields=missing,
        failures_change_admissibility=tuple(failures),
        failures_change_future_operation_availability=tuple(
            sorted(_foa_failure_labels(packet, failures, operations))
        ),
        handled_by_existing_protocol_artifacts=tuple(dict.fromkeys(handled)),
        missing_schema_requirements_revealed=tuple(dict.fromkeys(missing_schema)),
        explanation=_explain_packet(packet, verdict, operations, failures),
    )


def run_t121_analysis() -> T121Result:
    audits = tuple(validate_packet(packet) for packet in finite_packet_cases())
    valid = audits[0]
    if valid.packet_verdict != PacketVerdict.ADMISSIBLE:
        raise AssertionError("valid packet must be admissible")
    if not all(audit.raw_payload_valid for audit in audits):
        raise AssertionError("all finite cases intentionally keep raw payload valid")

    return T121Result(
        schema_fields=SCHEMA_FIELDS,
        strict_necessary_fields=STRICT_NECESSARY_FIELDS,
        audits=audits,
        strongest_claim=(
            "Before detector admissibility can be reasoned about, the evidence "
            "object must include raw payload plus provenance, authority, "
            "publication, revocation, key-state, witness, reconstruction, token, "
            "and dispute fields. Valid raw data alone is insufficient."
        ),
        fields_strictly_necessary=(
            "All declared schema fields are strictly necessary for this minimal "
            "packet because each supports either raw-payload identity/order, "
            "evidence admissibility, or future operations over the packet."
        ),
        failures_change_admissibility=(
            "Missing provenance, compromised key, revoked authority, delayed "
            "publication, collapsed authority domains, missing signatures, "
            "missing witnesses, missing reconstruction paths, missing tokens, "
            "and open disputes all block or withhold admissibility."
        ),
        failures_change_future_operation_availability=(
            "Every negative case reduces future operations. The clearest split is "
            "same raw data with open dispute: raw retention remains available, "
            "but claim review, lineage verification, challenge closure, and "
            "detector-claim use are withheld."
        ),
        handled_by_existing_protocol_artifacts=(
            "Provenance, signatures, publication, authority separation, witness "
            "references, reconstruction paths, and admissibility tokens are mostly "
            "handled by T78/T87/T97/T100. Revocation status, key-compromise state, "
            "and challenge lifecycle need explicit packet-level fields."
        ),
        missing_schema_requirements=(
            "The audit reveals three schema requirements not cleanly owned by the "
            "older raw-log artifacts: revocation registry/check time, key rotation "
            "and compromise continuity, and challenge/dispute lifecycle state."
        ),
        claim_impact_recommendation=(
            "No Q1 or detector-physics promotion. Treat T121 as infrastructure: "
            "a minimal detector evidence packet object required before D1 scoring "
            "or detector-branch admissibility claims."
        ),
        recommended_next=(
            "Integrate this packet schema with the T97 dry-run packet and require "
            "revocation, key-continuity, and dispute-state checks before any future "
            "real detector packet is scored."
        ),
    )


def t121_result_to_dict(result: T121Result) -> dict[str, object]:
    return {
        "schema_fields": list(result.schema_fields),
        "strict_necessary_fields": list(result.strict_necessary_fields),
        "audits": [
            {
                "packet_id": audit.packet_id,
                "raw_payload_valid": audit.raw_payload_valid,
                "packet_verdict": audit.packet_verdict.value,
                "admissibility_failures": list(audit.admissibility_failures),
                "future_operations": sorted(audit.future_operations),
                "missing_strict_fields": list(audit.missing_strict_fields),
                "failures_change_admissibility": list(
                    audit.failures_change_admissibility
                ),
                "failures_change_future_operation_availability": list(
                    audit.failures_change_future_operation_availability
                ),
                "handled_by_existing_protocol_artifacts": list(
                    audit.handled_by_existing_protocol_artifacts
                ),
                "missing_schema_requirements_revealed": list(
                    audit.missing_schema_requirements_revealed
                ),
                "explanation": audit.explanation,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "fields_strictly_necessary": result.fields_strictly_necessary,
        "failures_change_admissibility": result.failures_change_admissibility,
        "failures_change_future_operation_availability": (
            result.failures_change_future_operation_availability
        ),
        "handled_by_existing_protocol_artifacts": (
            result.handled_by_existing_protocol_artifacts
        ),
        "missing_schema_requirements": result.missing_schema_requirements,
        "claim_impact_recommendation": result.claim_impact_recommendation,
        "recommended_next": result.recommended_next,
    }


def _missing_strict_fields(packet: DetectorEvidencePacket) -> tuple[str, ...]:
    missing: list[str] = []
    for field in SCHEMA_FIELDS:
        value = getattr(packet, field)
        if value is None or value == () or value == frozenset():
            missing.append(field)
    return tuple(missing)


def _future_operations(
    packet: DetectorEvidencePacket,
    raw_payload_valid: bool,
    verdict: PacketVerdict,
) -> frozenset[str]:
    if not raw_payload_valid:
        return frozenset()
    if verdict == PacketVerdict.ADMISSIBLE:
        return BASE_OPERATIONS | ADMISSIBLE_OPERATIONS
    if verdict == PacketVerdict.WITHHOLD:
        return BASE_OPERATIONS | frozenset({"inspect_dispute", "preserve_evidence"})
    return BASE_OPERATIONS


def _foa_failure_labels(
    packet: DetectorEvidencePacket,
    failures: list[str],
    operations: frozenset[str],
) -> frozenset[str]:
    labels = set(failures)
    if operations == BASE_OPERATIONS:
        labels.add("future_claim_operations_removed")
    if packet.challenge_status == ChallengeStatus.OPEN:
        labels.add("future_operations_withheld_pending_dispute")
    return frozenset(labels)


def _explain_packet(
    packet: DetectorEvidencePacket,
    verdict: PacketVerdict,
    operations: frozenset[str],
    failures: list[str],
) -> str:
    if verdict == PacketVerdict.ADMISSIBLE:
        return "Packet is schema-complete, admissible, and preserves detector review operations."
    if verdict == PacketVerdict.WITHHOLD:
        return (
            "Raw payload is preserved, but dispute state withholds detector-claim "
            f"operations: {', '.join(sorted(operations))}."
        )
    return (
        f"Raw payload remains valid for {packet.packet_id}, but packet-level "
        f"failures block admissibility: {', '.join(failures)}."
    )


if __name__ == "__main__":
    import json

    print(json.dumps(t121_result_to_dict(run_t121_analysis()), indent=2))
