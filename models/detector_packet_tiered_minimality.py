"""T133: tiered minimality audit for detector evidence packets.

T121 and T123 established that raw payload validity is weaker than packet
admissibility and that same-payload packets can differ in future operation
availability. T133 asks a sharper question: does the current detector packet
need one flat "all fields or nothing" burden, or is the burden tiered?

The audit separates three tiers:

- raw evidence preservation;
- provisional packet admission for review;
- full detector-claim review and reconstruction readiness.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.real_detector_packet_schema_audit import (
    ChallengeStatus,
    KeyState,
    PacketVerdict,
    PublicationStatus,
    REQUIRED_ADMISSIBILITY_TOKENS,
    RevocationStatus,
)
from models.same_payload_packet_foa_witness import (
    PacketFOAAudit,
    audit_packet_against_reference,
    reference_packet,
    same_payload_packet_variants,
)


RAW_IDENTITY_FIELDS: tuple[str, ...] = (
    "detector_identity",
    "run_session_id",
    "causal_ordering_data",
    "raw_measurement_payload",
    "calibration_reference",
)

PROVISIONAL_ADMISSION_FIELDS: tuple[str, ...] = RAW_IDENTITY_FIELDS + (
    "provenance_chain",
    "signatures",
    "authority_domains",
    "publication_status",
    "revocation_status",
    "key_state",
    "admissibility_tokens",
)

CLAIM_REVIEW_EXTENSION_FIELDS: tuple[str, ...] = (
    "witness_references",
    "reconstruction_paths",
    "challenge_status",
)

PROVISIONAL_REQUIRED_TOKENS = frozenset(
    token for token in REQUIRED_ADMISSIBILITY_TOKENS if token != "challenge_window_declared"
)


@dataclass(frozen=True)
class TieredPacketAudit:
    packet_id: str
    changed_packet_fields: tuple[str, ...]
    raw_evidence_preserved: bool
    provisionally_admissible: bool
    claim_review_ready: bool
    strict_t121_verdict: PacketVerdict
    provisional_failures: tuple[str, ...]
    claim_review_failures: tuple[str, ...]
    strict_only_fields_triggered: tuple[str, ...]
    interpretation: str


@dataclass(frozen=True)
class T133Result:
    raw_identity_fields: tuple[str, ...]
    provisional_admission_fields: tuple[str, ...]
    claim_review_extension_fields: tuple[str, ...]
    audits: tuple[TieredPacketAudit, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    open_blocker: str
    recommended_next: str
    claim_ledger_update: str


def run_t133_analysis() -> T133Result:
    reference = reference_packet()
    audits = tuple(
        audit_packet_tiers(packet_foa_audit, reference.packet_id)
        for packet_foa_audit in (
            audit_packet_against_reference(packet, reference)
            for packet in same_payload_packet_variants()
        )
    )
    audit_map = {audit.packet_id: audit for audit in audits}

    if not audit_map["same_payload_reference_packet"].claim_review_ready:
        raise AssertionError("reference packet must be claim-review ready")
    if audit_map["missing_witnesses_same_payload"].claim_review_ready:
        raise AssertionError("missing witnesses must fail claim-review readiness")
    if not audit_map["missing_witnesses_same_payload"].provisionally_admissible:
        raise AssertionError("missing witnesses should remain provisionally admissible")
    if audit_map["missing_provenance_same_payload"].provisionally_admissible:
        raise AssertionError("missing provenance must fail provisional admission")
    if not audit_map["open_challenge_same_payload"].provisionally_admissible:
        raise AssertionError("open challenge should preserve provisional admission")
    if audit_map["open_challenge_same_payload"].claim_review_ready:
        raise AssertionError("open challenge must withhold claim-review readiness")

    return T133Result(
        raw_identity_fields=RAW_IDENTITY_FIELDS,
        provisional_admission_fields=PROVISIONAL_ADMISSION_FIELDS,
        claim_review_extension_fields=CLAIM_REVIEW_EXTENSION_FIELDS,
        audits=audits,
        strongest_claim=(
            "The current detector packet burden is tiered, not flat. Under the "
            "same-payload witness family, provenance/signature/authority/"
            "publication/revocation/key-state fields form the provisional "
            "admission core, while witness references, reconstruction paths, "
            "and dispute state are additional claim-review requirements."
        ),
        weakened_claim=(
            "T121's packet-wide strictness is too coarse as a description of "
            "what each field does. The current executable route should not say "
            "that every packet field is equally needed for the first admission "
            "decision. Some fields gate stronger review and future operations, "
            "not raw evidence preservation or provisional intake."
        ),
        falsification_condition=(
            "T133 fails if witness references, reconstruction paths, and "
            "challenge state can be removed while keeping full detector-claim "
            "review rights, or if provenance, signature, authority, "
            "publication, revocation, and key-state failures no longer block "
            "even provisional packet admission."
        ),
        open_blocker=(
            "The tier split is still a schema audit over synthetic same-payload "
            "packets. A real T97 dry-run packet must publish both provisional "
            "admission and claim-review readiness before the detector branch "
            "can present itself as a reproducible evidence protocol."
        ),
        recommended_next=(
            "Refactor the T97 dry-run packet into explicit tier outputs: raw "
            "evidence preserved, provisionally admitted, and claim-review "
            "ready. Then require any real deployment to freeze which tier is "
            "being claimed before event collection."
        ),
        claim_ledger_update=(
            "Q1B remains externally blocked. T133 sharpens the packet burden: "
            "detector evidence now has a smaller provisional-admission core "
            "plus a stricter claim-review extension. This weakens any flat "
            "reading that treats every packet field as equally necessary at the "
            "first admissibility step."
        ),
    )


def t133_result_to_dict(result: T133Result) -> dict[str, object]:
    return {
        "raw_identity_fields": list(result.raw_identity_fields),
        "provisional_admission_fields": list(result.provisional_admission_fields),
        "claim_review_extension_fields": list(result.claim_review_extension_fields),
        "audits": [
            {
                "packet_id": audit.packet_id,
                "changed_packet_fields": list(audit.changed_packet_fields),
                "raw_evidence_preserved": audit.raw_evidence_preserved,
                "provisionally_admissible": audit.provisionally_admissible,
                "claim_review_ready": audit.claim_review_ready,
                "strict_t121_verdict": audit.strict_t121_verdict.value,
                "provisional_failures": list(audit.provisional_failures),
                "claim_review_failures": list(audit.claim_review_failures),
                "strict_only_fields_triggered": list(audit.strict_only_fields_triggered),
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
        "claim_ledger_update": result.claim_ledger_update,
    }


def audit_packet_tiers(packet_audit: PacketFOAAudit, reference_packet_id: str) -> TieredPacketAudit:
    provisional_failures = _provisional_failures(packet_audit)
    claim_review_failures = _claim_review_failures(packet_audit, provisional_failures)
    strict_only = tuple(
        field
        for field in CLAIM_REVIEW_EXTENSION_FIELDS
        if field in packet_audit.changed_packet_fields and field not in provisional_failures
    )
    raw_evidence_preserved = (
        packet_audit.same_raw_payload
        and packet_audit.same_measurement_result
        and packet_audit.same_coarse_detector_summary
    )
    provisionally_admissible = not provisional_failures
    claim_review_ready = not claim_review_failures

    return TieredPacketAudit(
        packet_id=packet_audit.packet_id,
        changed_packet_fields=packet_audit.changed_packet_fields,
        raw_evidence_preserved=raw_evidence_preserved,
        provisionally_admissible=provisionally_admissible,
        claim_review_ready=claim_review_ready,
        strict_t121_verdict=packet_audit.packet_verdict,
        provisional_failures=tuple(provisional_failures),
        claim_review_failures=tuple(claim_review_failures),
        strict_only_fields_triggered=strict_only,
        interpretation=_interpretation(
            packet_audit.packet_id,
            packet_audit.changed_packet_fields,
            provisionally_admissible,
            claim_review_ready,
            strict_only,
            reference_packet_id,
        ),
    )


def _provisional_failures(packet_audit: PacketFOAAudit) -> list[str]:
    provisional: list[str] = []
    changed = set(packet_audit.changed_packet_fields)

    if not packet_audit.same_raw_payload:
        provisional.append("raw_measurement_payload")
    if "provenance_chain" in changed:
        provisional.append("provenance_chain")
    if "signatures" in changed or not packet_audit.signature_valid:
        provisional.append("signatures")
    if "authority_domains" in changed:
        provisional.append("authority_domains")
    if "publication_status" in changed:
        provisional.append("publication_status")
    if "revocation_status" in changed:
        provisional.append("revocation_status")
    if "key_state" in changed:
        provisional.append("key_state")
    if _missing_provisional_tokens(packet_audit):
        provisional.append("admissibility_tokens")
    return provisional


def _claim_review_failures(
    packet_audit: PacketFOAAudit,
    provisional_failures: list[str],
) -> list[str]:
    claim_review = list(provisional_failures)
    changed = set(packet_audit.changed_packet_fields)

    if "witness_references" in changed:
        claim_review.append("witness_references")
    if "reconstruction_paths" in changed:
        claim_review.append("reconstruction_paths")
    if "challenge_status" in changed:
        claim_review.append("challenge_status")
    if _missing_full_tokens(packet_audit):
        claim_review.append("admissibility_tokens")
    return claim_review


def _missing_provisional_tokens(packet_audit: PacketFOAAudit) -> bool:
    return (
        "published_before_analysis" in packet_audit.admissibility_failures
        or "missing_admissibility_tokens" in packet_audit.admissibility_failures
        and packet_audit.packet_id != "open_challenge_same_payload"
    )


def _missing_full_tokens(packet_audit: PacketFOAAudit) -> bool:
    return "missing_admissibility_tokens" in packet_audit.admissibility_failures


def _interpretation(
    packet_id: str,
    changed_packet_fields: tuple[str, ...],
    provisionally_admissible: bool,
    claim_review_ready: bool,
    strict_only: tuple[str, ...],
    reference_packet_id: str,
) -> str:
    if packet_id == reference_packet_id:
        return "Reference packet clears raw, provisional-admission, and claim-review tiers."
    if not provisionally_admissible:
        return (
            "Changed fields hit the provisional-admission core, so the packet "
            "cannot even enter claim review."
        )
    if not claim_review_ready and strict_only:
        return (
            "Changed fields preserve provisional admission but remove full "
            f"claim-review rights through {', '.join(strict_only)}."
        )
    if not claim_review_ready:
        return (
            "Packet survives provisional admission but fails full claim review "
            "under the stricter tier policy."
        )
    return (
        "Packet keeps both provisional admission and claim-review rights under "
        f"the current tier split despite changes to {', '.join(changed_packet_fields)}."
    )
