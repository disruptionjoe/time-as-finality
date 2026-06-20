"""T123: same-payload detector packet FOA witness.

This audit asks a narrower question than T121. Hold fixed:

- raw measurement payload;
- immediate measurement result;
- coarse detector summary.

Then vary only packet-level evidence fields and ask whether admissibility,
reconstruction, challenge, certification, or future operation availability
changes. This is detector evidence infrastructure only; it does not score D1
or promote Q1.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from models.real_detector_packet_schema_audit import (
    ChallengeStatus,
    DetectorEvidencePacket,
    KeyState,
    PacketVerdict,
    PublicationStatus,
    RevocationStatus,
    REQUIRED_ADMISSIBILITY_TOKENS,
    valid_packet,
    validate_packet,
)


RAW_PAYLOAD = ("event:e1:+", "event:e2:-", "event:e3:+", "event:e4:-")
FULL_FOA = frozenset(
    {
        "read_immediate_result",
        "retain_raw_payload",
        "score_admissibility",
        "verify_lineage",
        "reconstruct_event",
        "challenge_packet",
        "certify_packet",
        "publish_packet",
        "bind_calibration",
        "audit_authority",
        "use_for_detector_claim_review",
    }
)
WITHHELD_FOA = frozenset(
    {
        "read_immediate_result",
        "retain_raw_payload",
        "inspect_dispute",
        "preserve_evidence",
    }
)
RAW_ONLY_FOA = frozenset({"read_immediate_result", "retain_raw_payload"})


@dataclass(frozen=True)
class ImmediateMeasurementView:
    raw_payload: tuple[str, ...]
    measurement_result: str
    coarse_detector_summary: tuple[tuple[str, object], ...]


@dataclass(frozen=True)
class PacketFOAAudit:
    packet_id: str
    changed_packet_fields: tuple[str, ...]
    same_raw_payload: bool
    same_measurement_result: bool
    same_coarse_detector_summary: bool
    packet_verdict: PacketVerdict
    signature_valid: bool
    admissibility_failures: tuple[str, ...]
    future_operations: frozenset[str]
    operations_removed_vs_reference: frozenset[str]
    operations_added_vs_reference: frozenset[str]
    immediate_result_unchanged_but_foa_changed: bool
    explanation: str


@dataclass(frozen=True)
class T123Result:
    reference_packet_id: str
    reference_view: ImmediateMeasurementView
    audits: tuple[PacketFOAAudit, ...]
    strongest_claim: str
    what_changed: str
    what_did_not_change: str
    claim_impact_note: str
    falsification_condition: str
    open_blocker: str
    recommended_next: str
    claim_ledger_update: str


def reference_packet() -> DetectorEvidencePacket:
    base = valid_packet()
    return replace(
        base,
        packet_id="same_payload_reference_packet",
        raw_measurement_payload=RAW_PAYLOAD,
        purpose="Reference packet: same raw payload, complete packet wrapper.",
    )


def same_payload_packet_variants() -> tuple[DetectorEvidencePacket, ...]:
    base = reference_packet()
    return (
        base,
        replace(
            base,
            packet_id="missing_provenance_same_payload",
            provenance_chain=(),
            admissibility_tokens=base.admissibility_tokens - {"signature_verified"},
            purpose="Same raw payload, but provenance chain is missing.",
        ),
        replace(
            base,
            packet_id="authority_collapsed_same_payload",
            authority_domains=frozenset({"single_lab_authority"}),
            admissibility_tokens=base.admissibility_tokens - {"authority_separation"},
            purpose="Same raw payload, but authority separation collapses.",
        ),
        replace(
            base,
            packet_id="invalid_signature_same_payload",
            signatures=("sig:invalid",),
            admissibility_tokens=base.admissibility_tokens - {"signature_verified"},
            purpose="Same raw payload, but signature verification fails.",
        ),
        replace(
            base,
            packet_id="key_compromised_same_payload",
            key_state=KeyState.COMPROMISED,
            purpose="Same raw payload, but signing key is compromised.",
        ),
        replace(
            base,
            packet_id="revoked_authority_same_payload",
            revocation_status=RevocationStatus.REVOKED,
            purpose="Same raw payload, but authority or packet is revoked.",
        ),
        replace(
            base,
            packet_id="publication_delayed_same_payload",
            publication_status=PublicationStatus.DELAYED,
            admissibility_tokens=base.admissibility_tokens - {"published_before_analysis"},
            purpose="Same raw payload, but publication is delayed.",
        ),
        replace(
            base,
            packet_id="missing_witnesses_same_payload",
            witness_references=(),
            purpose="Same raw payload, but witness references are missing.",
        ),
        replace(
            base,
            packet_id="missing_reconstruction_same_payload",
            reconstruction_paths=(),
            purpose="Same raw payload, but reconstruction paths are missing.",
        ),
        replace(
            base,
            packet_id="open_challenge_same_payload",
            challenge_status=ChallengeStatus.OPEN,
            admissibility_tokens=base.admissibility_tokens - {"challenge_window_declared"},
            purpose="Same raw payload, but challenge/dispute state is open.",
        ),
    )


def immediate_measurement_view(packet: DetectorEvidencePacket) -> ImmediateMeasurementView:
    plus_count = sum(1 for row in packet.raw_measurement_payload if row.endswith(":+"))
    minus_count = sum(1 for row in packet.raw_measurement_payload if row.endswith(":-"))
    result = f"plus={plus_count};minus={minus_count};balance={plus_count - minus_count}"
    summary = (
        ("detector_identity", packet.detector_identity),
        ("run_session_id", packet.run_session_id),
        ("calibration_reference", packet.calibration_reference),
        ("event_count", len(packet.raw_measurement_payload)),
        ("plus_count", plus_count),
        ("minus_count", minus_count),
    )
    return ImmediateMeasurementView(
        raw_payload=packet.raw_measurement_payload,
        measurement_result=result,
        coarse_detector_summary=summary,
    )


def audit_packet_against_reference(
    packet: DetectorEvidencePacket,
    reference: DetectorEvidencePacket,
) -> PacketFOAAudit:
    reference_view = immediate_measurement_view(reference)
    view = immediate_measurement_view(packet)
    schema_audit = validate_packet(packet)
    signature_valid = _signature_valid(packet)
    failures = list(schema_audit.admissibility_failures)
    if not signature_valid and "invalid_signature" not in failures:
        failures.append("invalid_signature")

    verdict = schema_audit.packet_verdict
    if not signature_valid and verdict == PacketVerdict.ADMISSIBLE:
        verdict = PacketVerdict.INADMISSIBLE
    future_operations = _future_operations(verdict)
    removed = FULL_FOA - future_operations
    added = future_operations - FULL_FOA
    same_immediate_view = (
        view.raw_payload == reference_view.raw_payload
        and view.measurement_result == reference_view.measurement_result
        and view.coarse_detector_summary == reference_view.coarse_detector_summary
    )
    return PacketFOAAudit(
        packet_id=packet.packet_id,
        changed_packet_fields=_changed_packet_fields(packet, reference),
        same_raw_payload=view.raw_payload == reference_view.raw_payload,
        same_measurement_result=view.measurement_result == reference_view.measurement_result,
        same_coarse_detector_summary=(
            view.coarse_detector_summary == reference_view.coarse_detector_summary
        ),
        packet_verdict=verdict,
        signature_valid=signature_valid,
        admissibility_failures=tuple(failures),
        future_operations=future_operations,
        operations_removed_vs_reference=removed,
        operations_added_vs_reference=added,
        immediate_result_unchanged_but_foa_changed=(
            same_immediate_view and future_operations != FULL_FOA
        ),
        explanation=_explanation(packet.packet_id, verdict, future_operations, failures),
    )


def run_t123_analysis() -> T123Result:
    reference = reference_packet()
    audits = tuple(
        audit_packet_against_reference(packet, reference)
        for packet in same_payload_packet_variants()
    )
    reference_audit = audits[0]
    if reference_audit.future_operations != FULL_FOA:
        raise AssertionError("reference packet must expose full FOA")
    if not all(
        audit.same_raw_payload
        and audit.same_measurement_result
        and audit.same_coarse_detector_summary
        for audit in audits
    ):
        raise AssertionError("all T123 variants must keep raw/result/summary fixed")
    if not any(audit.immediate_result_unchanged_but_foa_changed for audit in audits[1:]):
        raise AssertionError("T123 must contain a same-result FOA split")

    return T123Result(
        reference_packet_id=reference.packet_id,
        reference_view=immediate_measurement_view(reference),
        audits=audits,
        strongest_claim=(
            "Yes. In the finite detector-packet audit, packet-level structure "
            "changes admissibility, reconstruction, challenge, certification, "
            "and future operation availability while raw payload, immediate "
            "measurement result, and coarse detector summary remain fixed."
        ),
        what_changed=(
            "Provenance completeness, authority separation, signature validity, "
            "key-compromise status, revocation status, publication timing, witness "
            "availability, reconstruction paths, and challenge state each remove "
            "future operations in at least one same-payload variant."
        ),
        what_did_not_change=(
            "The raw rows, plus/minus measurement result, detector identity, run "
            "identifier, calibration reference, event count, and coarse plus/minus "
            "summary are identical across all T123 packet variants."
        ),
        claim_impact_note=(
            "No Q1 or detector-physics promotion. T123 is detector evidence "
            "infrastructure: raw measurement sameness does not imply equal packet "
            "admissibility or equal future operation rights."
        ),
        falsification_condition=(
            "T123's same-payload FOA split is falsified if packet protocols declare "
            "that admissibility, reconstruction, challenge, certification, and "
            "claim-review rights are functions only of raw payload, immediate "
            "measurement result, and coarse detector summary. Such a protocol would "
            "also abandon the T78/T87/T97/T100/T121 evidence requirements."
        ),
        open_blocker=(
            "The audit is still schema-level. It must be integrated into the T97 "
            "dry-run packet and then populated by a real pre-registered detector "
            "deployment before any detector branch can be evaluated."
        ),
        recommended_next=(
            "Add a T97 packet fixture that emits the T123 same-payload variants "
            "with signed manifests, then require the real detector packet to report "
            "both immediate measurement results and FOA verdicts side by side."
        ),
        claim_ledger_update=(
            "Q1B remains externally blocked and receives no empirical upgrade. "
            "T123 adds detector evidence infrastructure: same raw payload, same "
            "measurement result, and same coarse detector summary can still yield "
            "different admissibility and future operation availability when packet "
            "provenance, authority, signature, key, revocation, publication, "
            "witness, reconstruction, or challenge fields differ."
        ),
    )


def t123_result_to_dict(result: T123Result) -> dict[str, object]:
    return {
        "reference_packet_id": result.reference_packet_id,
        "reference_view": {
            "raw_payload": list(result.reference_view.raw_payload),
            "measurement_result": result.reference_view.measurement_result,
            "coarse_detector_summary": [
                {"field": field, "value": value}
                for field, value in result.reference_view.coarse_detector_summary
            ],
        },
        "audits": [
            {
                "packet_id": audit.packet_id,
                "changed_packet_fields": list(audit.changed_packet_fields),
                "same_raw_payload": audit.same_raw_payload,
                "same_measurement_result": audit.same_measurement_result,
                "same_coarse_detector_summary": audit.same_coarse_detector_summary,
                "packet_verdict": audit.packet_verdict.value,
                "signature_valid": audit.signature_valid,
                "admissibility_failures": list(audit.admissibility_failures),
                "future_operations": sorted(audit.future_operations),
                "operations_removed_vs_reference": sorted(
                    audit.operations_removed_vs_reference
                ),
                "operations_added_vs_reference": sorted(
                    audit.operations_added_vs_reference
                ),
                "immediate_result_unchanged_but_foa_changed": (
                    audit.immediate_result_unchanged_but_foa_changed
                ),
                "explanation": audit.explanation,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "what_changed": result.what_changed,
        "what_did_not_change": result.what_did_not_change,
        "claim_impact_note": result.claim_impact_note,
        "falsification_condition": result.falsification_condition,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
        "claim_ledger_update": result.claim_ledger_update,
    }


def _future_operations(verdict: PacketVerdict) -> frozenset[str]:
    if verdict == PacketVerdict.ADMISSIBLE:
        return FULL_FOA
    if verdict == PacketVerdict.WITHHOLD:
        return WITHHELD_FOA
    return RAW_ONLY_FOA


def _signature_valid(packet: DetectorEvidencePacket) -> bool:
    return (
        bool(packet.signatures)
        and all(signature.startswith("sig:") for signature in packet.signatures)
        and "sig:invalid" not in packet.signatures
        and "signature_verified" in packet.admissibility_tokens
    )


def _changed_packet_fields(
    packet: DetectorEvidencePacket,
    reference: DetectorEvidencePacket,
) -> tuple[str, ...]:
    excluded = {"packet_id", "purpose"}
    fields = [
        field
        for field in DetectorEvidencePacket.__dataclass_fields__
        if field not in excluded and getattr(packet, field) != getattr(reference, field)
    ]
    return tuple(fields)


def _explanation(
    packet_id: str,
    verdict: PacketVerdict,
    operations: frozenset[str],
    failures: list[str],
) -> str:
    if verdict == PacketVerdict.ADMISSIBLE:
        return (
            f"{packet_id}: same raw result and complete packet wrapper preserve "
            "full detector evidence operations."
        )
    if verdict == PacketVerdict.WITHHOLD:
        return (
            f"{packet_id}: same raw result is readable, but dispute state withholds "
            "claim review and certification operations."
        )
    return (
        f"{packet_id}: same raw result is readable, but packet failures remove "
        f"future evidence operations: {', '.join(failures)}."
    )
