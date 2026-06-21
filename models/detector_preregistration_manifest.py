"""T136: pre-registration manifest for the Q1B detector route.

T134 showed that T97 raw-log rows are necessary but not sufficient for detector
packet admission. The missing object is a pre-event manifest that binds the T97
table commitments, the T121/T133 wrapper commitments, the T100 authority
partition, and the claimed tier before the first detector event.

This module intentionally does not require detector outcomes before the run.
It requires pre-event commitments to schemas, export rules, hashes, authority
separation, and the claimed review tier. Actual event values remain future
payloads to be checked against the frozen commitments.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import hashlib

from models.detector_authority_domain_bound import (
    DOMAINS,
    AuthorityPartition,
    audit_partition,
)
from models.detector_dry_run_packet_skeleton import (
    DetectorDryRunPacket,
    audit_detector_dry_run_packet,
    locked_detector_dry_run_packet_skeleton,
)
from models.detector_packet_tiered_minimality import (
    CLAIM_REVIEW_EXTENSION_FIELDS,
    PROVISIONAL_ADMISSION_FIELDS,
)
from models.real_detector_packet_schema_audit import SCHEMA_FIELDS


ALLOWED_TIERS: tuple[str, ...] = (
    "raw_log_preservation",
    "provisional_admission",
    "claim_review",
)

TIER_RANK: dict[str, int] = {
    "none": 0,
    "raw_log_preservation": 1,
    "provisional_admission": 2,
    "claim_review": 3,
}


@dataclass(frozen=True)
class TableHashCommitment:
    table_name: str
    file_name: str
    schema_hash: str
    export_checksum: str
    join_keys: tuple[str, ...]


@dataclass(frozen=True)
class WrapperFieldCommitment:
    field_name: str
    commitment_kind: str
    commitment_hash: str


@dataclass(frozen=True)
class DetectorPreregistrationManifest:
    name: str
    run_id: str
    registered_at: str
    first_event_not_before: str
    claimed_tier: str
    t97_manifest_hash: str
    table_commitments: tuple[TableHashCommitment, ...]
    wrapper_field_commitments: tuple[WrapperFieldCommitment, ...]
    authority_partition: tuple[tuple[str, ...], ...]
    no_data_analyzed: bool
    manifest_hash: str
    purpose: str


@dataclass(frozen=True)
class PreregistrationManifestAudit:
    manifest_name: str
    claimed_tier: str
    max_certifiable_tier: str
    claimed_tier_admissible: bool
    t97_packet_verdict: str
    t97_table_commitments_valid: bool
    wrapper_commitments_valid: bool
    authority_partition_admissible: bool
    authority_profile_name: str | None
    authority_count: int | None
    predata_boundary_respected: bool
    manifest_hash_valid: bool
    committed_wrapper_fields: tuple[str, ...]
    missing_provisional_fields: tuple[str, ...]
    missing_claim_review_fields: tuple[str, ...]
    failure_reasons: tuple[str, ...]
    interpretation: str


@dataclass(frozen=True)
class T136Result:
    required_t97_tables: tuple[str, ...]
    provisional_commitment_fields: tuple[str, ...]
    claim_review_commitment_fields: tuple[str, ...]
    audits: tuple[PreregistrationManifestAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def complete_claim_review_manifest() -> DetectorPreregistrationManifest:
    packet = locked_detector_dry_run_packet_skeleton()
    return _manifest(
        name="complete_claim_review_manifest",
        packet=packet,
        claimed_tier="claim_review",
        wrapper_field_commitments=_field_commitments(SCHEMA_FIELDS),
        authority_partition=_fully_separated_authority_partition(),
        registered_at=packet.registered_at,
        first_event_not_before=packet.first_event_not_before,
        no_data_analyzed=True,
        purpose=(
            "A complete pre-event manifest for a future detector run. It freezes "
            "T97 table commitments, all T121/T133 wrapper-field commitments, "
            "the five-domain authority partition, and a claim-review tier before "
            "the first event."
        ),
    )


def provisional_only_manifest() -> DetectorPreregistrationManifest:
    packet = locked_detector_dry_run_packet_skeleton()
    return _manifest(
        name="provisional_only_manifest",
        packet=packet,
        claimed_tier="provisional_admission",
        wrapper_field_commitments=_field_commitments(PROVISIONAL_ADMISSION_FIELDS),
        authority_partition=_fully_separated_authority_partition(),
        registered_at=packet.registered_at,
        first_event_not_before=packet.first_event_not_before,
        no_data_analyzed=True,
        purpose=(
            "A manifest that honestly claims only provisional admission. It "
            "commits the provisional core but does not claim claim-review "
            "readiness."
        ),
    )


def raw_log_only_manifest() -> DetectorPreregistrationManifest:
    packet = locked_detector_dry_run_packet_skeleton()
    return _manifest(
        name="raw_log_only_manifest",
        packet=packet,
        claimed_tier="provisional_admission",
        wrapper_field_commitments=(),
        authority_partition=_fully_separated_authority_partition(),
        registered_at=packet.registered_at,
        first_event_not_before=packet.first_event_not_before,
        no_data_analyzed=True,
        purpose=(
            "A hostile shortcut: the T97 raw-log scaffold is frozen, but the "
            "manifest tries to claim provisional admission without wrapper "
            "commitments."
        ),
    )


def claim_review_missing_witness_manifest() -> DetectorPreregistrationManifest:
    packet = locked_detector_dry_run_packet_skeleton()
    return _manifest(
        name="claim_review_missing_witness_manifest",
        packet=packet,
        claimed_tier="claim_review",
        wrapper_field_commitments=_field_commitments(PROVISIONAL_ADMISSION_FIELDS),
        authority_partition=_fully_separated_authority_partition(),
        registered_at=packet.registered_at,
        first_event_not_before=packet.first_event_not_before,
        no_data_analyzed=True,
        purpose=(
            "A tier overclaim: the provisional core is committed, but witness, "
            "reconstruction, and dispute commitments are missing."
        ),
    )


def posthoc_manifest() -> DetectorPreregistrationManifest:
    packet = locked_detector_dry_run_packet_skeleton()
    return _manifest(
        name="posthoc_claim_review_manifest",
        packet=packet,
        claimed_tier="claim_review",
        wrapper_field_commitments=_field_commitments(SCHEMA_FIELDS),
        authority_partition=_fully_separated_authority_partition(),
        registered_at="2026-06-22T00:00:00Z",
        first_event_not_before=packet.first_event_not_before,
        no_data_analyzed=False,
        purpose=(
            "A complete-looking manifest assembled after data access or after "
            "the first event boundary."
        ),
    )


def invalid_authority_manifest() -> DetectorPreregistrationManifest:
    packet = locked_detector_dry_run_packet_skeleton()
    return _manifest(
        name="three_domain_authority_manifest",
        packet=packet,
        claimed_tier="claim_review",
        wrapper_field_commitments=_field_commitments(SCHEMA_FIELDS),
        authority_partition=(
            ("analysis_governor", "control_designer"),
            ("instrument_operator",),
            ("archive_custodian", "trust_auditor"),
        ),
        registered_at=packet.registered_at,
        first_event_not_before=packet.first_event_not_before,
        no_data_analyzed=True,
        purpose=(
            "A complete-looking manifest with a three-domain authority partition "
            "that fails the T100 lower bound and trust-auditor independence."
        ),
    )


def deferred_tier_manifest() -> DetectorPreregistrationManifest:
    packet = locked_detector_dry_run_packet_skeleton()
    return _manifest(
        name="deferred_tier_manifest",
        packet=packet,
        claimed_tier="undeclared",
        wrapper_field_commitments=_field_commitments(SCHEMA_FIELDS),
        authority_partition=_fully_separated_authority_partition(),
        registered_at=packet.registered_at,
        first_event_not_before=packet.first_event_not_before,
        no_data_analyzed=True,
        purpose=(
            "A manifest that freezes fields but refuses to state before the run "
            "which tier is being claimed."
        ),
    )


def manifest_hash_mismatch_case() -> DetectorPreregistrationManifest:
    base = complete_claim_review_manifest()
    return replace(
        base,
        name="manifest_hash_mismatch_case",
        manifest_hash="0" * 64,
        purpose="A complete-looking manifest whose top-level hash is corrupted.",
    )


def observed_payload_value_manifest() -> DetectorPreregistrationManifest:
    base = complete_claim_review_manifest()
    commitments = tuple(
        replace(field, commitment_kind="observed_value_commitment")
        if field.field_name == "raw_measurement_payload"
        else field
        for field in base.wrapper_field_commitments
    )
    return _manifest(
        name="observed_payload_value_manifest",
        packet=locked_detector_dry_run_packet_skeleton(),
        claimed_tier="claim_review",
        wrapper_field_commitments=commitments,
        authority_partition=base.authority_partition,
        registered_at=base.registered_at,
        first_event_not_before=base.first_event_not_before,
        no_data_analyzed=True,
        purpose=(
            "A manifest that appears to know detector outcome values before the "
            "run instead of freezing an export rule for future payloads."
        ),
    )


def preregistration_manifest_fixtures() -> tuple[DetectorPreregistrationManifest, ...]:
    return (
        complete_claim_review_manifest(),
        provisional_only_manifest(),
        raw_log_only_manifest(),
        claim_review_missing_witness_manifest(),
        posthoc_manifest(),
        invalid_authority_manifest(),
        deferred_tier_manifest(),
        manifest_hash_mismatch_case(),
        observed_payload_value_manifest(),
    )


def audit_preregistration_manifest(
    manifest: DetectorPreregistrationManifest,
) -> PreregistrationManifestAudit:
    packet = locked_detector_dry_run_packet_skeleton()
    t97_audit = audit_detector_dry_run_packet(packet)

    table_failures = _table_commitment_failures(manifest, packet)
    field_map = {field.field_name: field for field in manifest.wrapper_field_commitments}
    malformed_fields = tuple(
        field.field_name
        for field in manifest.wrapper_field_commitments
        if not _is_hash(field.commitment_hash) or not field.commitment_kind
    )
    duplicate_fields = _duplicates(
        field.field_name for field in manifest.wrapper_field_commitments
    )
    predata_failures = _predata_failures(manifest)
    authority_admissible, authority_profile, authority_count, authority_failures = (
        _authority_status(manifest.authority_partition)
    )
    manifest_hash_failures = _manifest_hash_failures(manifest)
    payload_boundary_failures = _payload_boundary_failures(field_map)

    missing_provisional = _missing_fields(
        PROVISIONAL_ADMISSION_FIELDS,
        field_map,
    )
    missing_claim_review = _missing_fields(
        CLAIM_REVIEW_EXTENSION_FIELDS,
        field_map,
    )

    failures: list[str] = []
    failures.extend(table_failures)
    if malformed_fields:
        failures.append("malformed_wrapper_field_commitments")
    if duplicate_fields:
        failures.append("duplicate_wrapper_field_commitments")
    failures.extend(predata_failures)
    failures.extend(authority_failures)
    failures.extend(manifest_hash_failures)
    failures.extend(payload_boundary_failures)

    if manifest.claimed_tier not in ALLOWED_TIERS:
        failures.append("invalid_or_undeclared_claimed_tier")
    elif manifest.claimed_tier == "provisional_admission" and missing_provisional:
        failures.append("missing_provisional_wrapper_commitments")
    elif manifest.claimed_tier == "claim_review":
        if missing_provisional:
            failures.append("missing_provisional_wrapper_commitments")
        if missing_claim_review:
            failures.append("missing_claim_review_wrapper_commitments")

    table_valid = not table_failures
    wrapper_valid = not (
        malformed_fields
        or duplicate_fields
        or payload_boundary_failures
        or (
            manifest.claimed_tier == "provisional_admission"
            and missing_provisional
        )
        or (
            manifest.claimed_tier == "claim_review"
            and (missing_provisional or missing_claim_review)
        )
    )
    predata_ok = not predata_failures
    hash_ok = not manifest_hash_failures
    base_valid = table_valid and authority_admissible and predata_ok and hash_ok
    max_tier = _max_certifiable_tier(
        base_valid=base_valid,
        malformed_fields=bool(malformed_fields or duplicate_fields),
        payload_boundary_ok=not payload_boundary_failures,
        missing_provisional=missing_provisional,
        missing_claim_review=missing_claim_review,
    )
    claimed_admissible = (
        manifest.claimed_tier in ALLOWED_TIERS
        and TIER_RANK[max_tier] >= TIER_RANK[manifest.claimed_tier]
        and not failures
    )

    return PreregistrationManifestAudit(
        manifest_name=manifest.name,
        claimed_tier=manifest.claimed_tier,
        max_certifiable_tier=max_tier,
        claimed_tier_admissible=claimed_admissible,
        t97_packet_verdict=t97_audit.verdict,
        t97_table_commitments_valid=table_valid,
        wrapper_commitments_valid=wrapper_valid,
        authority_partition_admissible=authority_admissible,
        authority_profile_name=authority_profile,
        authority_count=authority_count,
        predata_boundary_respected=predata_ok,
        manifest_hash_valid=hash_ok,
        committed_wrapper_fields=tuple(sorted(field_map)),
        missing_provisional_fields=missing_provisional,
        missing_claim_review_fields=missing_claim_review,
        failure_reasons=tuple(dict.fromkeys(failures)),
        interpretation=_interpretation(manifest, max_tier, claimed_admissible, failures),
    )


def run_t136_analysis() -> T136Result:
    audits = tuple(
        audit_preregistration_manifest(manifest)
        for manifest in preregistration_manifest_fixtures()
    )
    audit_map = {audit.manifest_name: audit for audit in audits}

    if not audit_map["complete_claim_review_manifest"].claimed_tier_admissible:
        raise AssertionError("complete claim-review manifest must pass")
    if audit_map["raw_log_only_manifest"].claimed_tier_admissible:
        raise AssertionError("T97-only manifest must not claim provisional admission")
    if not audit_map["provisional_only_manifest"].claimed_tier_admissible:
        raise AssertionError("honest provisional manifest must pass its claimed tier")
    if audit_map["claim_review_missing_witness_manifest"].claimed_tier_admissible:
        raise AssertionError("claim-review tier must require review-extension commitments")
    if audit_map["posthoc_claim_review_manifest"].claimed_tier_admissible:
        raise AssertionError("post hoc manifest must fail")
    if audit_map["three_domain_authority_manifest"].claimed_tier_admissible:
        raise AssertionError("invalid T100 authority partition must fail")
    if audit_map["deferred_tier_manifest"].claimed_tier_admissible:
        raise AssertionError("undeclared tier must fail")
    if audit_map["observed_payload_value_manifest"].claimed_tier_admissible:
        raise AssertionError("predata manifest must not claim observed payload values")

    return T136Result(
        required_t97_tables=tuple(
            table.table_name
            for table in locked_detector_dry_run_packet_skeleton().tables
        ),
        provisional_commitment_fields=PROVISIONAL_ADMISSION_FIELDS,
        claim_review_commitment_fields=(
            PROVISIONAL_ADMISSION_FIELDS + CLAIM_REVIEW_EXTENSION_FIELDS
        ),
        audits=audits,
        strongest_claim=(
            "Q1B now has a concrete pre-event manifest gate. A detector "
            "deployment may claim only the strongest tier whose T97 table "
            "hashes, T121/T133 wrapper-field commitments, T100 authority "
            "partition, top-level manifest hash, no-data boundary, and claimed "
            "tier were frozen before the first event."
        ),
        improved=(
            "T136 closes the T134 integration gap without requiring impossible "
            "pre-event detector outcomes. It freezes export rules and field "
            "commitments before data, then makes any later tier upgrade a "
            "manifest failure rather than a matter of interpretation."
        ),
        weakened=(
            "This weakens Q1B operationally. Filled T97 rows, a post hoc wrapper, "
            "or a deferred tier declaration cannot upgrade detector evidence. A "
            "lab that cannot name the manifest, authority partition, and claimed "
            "tier pre-data has no admissible detector-branch claim."
        ),
        falsification_condition=(
            "T136 fails if a real detector deployment can legitimately claim "
            "provisional or claim-review status without pre-event wrapper-field "
            "commitments and authority evidence, or if the manifest requires "
            "actual detector outcomes before events rather than export-rule "
            "commitments."
        ),
        q1b_update=(
            "Q1B remains externally blocked, but its blocker is now sharper: "
            "produce one signed T136 manifest before event collection, then fill "
            "the bound packet without schema, authority, tier, or wrapper-policy "
            "changes."
        ),
        claim_ledger_update=(
            "Add T136 to Q1B: detector packet admission now requires a pre-event "
            "manifest binding T97 table hashes, T121/T133 wrapper commitments, "
            "T100 authority separation, and the claimed tier. T97-only, post hoc, "
            "invalid-authority, deferred-tier, and pre-known-payload variants are "
            "null for the claimed tier."
        ),
        open_blocker=(
            "No real lab has signed and frozen a T136 manifest before detector "
            "event collection."
        ),
        recommended_next=(
            "Draft a human-fillable T136 manifest template and try to map one "
            "specific lab workflow onto it. If no plausible workflow can sign it "
            "pre-data, demote Q1B below active quantum-measurement work."
        ),
    )


def t136_result_to_dict(result: T136Result) -> dict[str, object]:
    return {
        "required_t97_tables": list(result.required_t97_tables),
        "provisional_commitment_fields": list(result.provisional_commitment_fields),
        "claim_review_commitment_fields": list(result.claim_review_commitment_fields),
        "audits": [
            {
                "manifest_name": audit.manifest_name,
                "claimed_tier": audit.claimed_tier,
                "max_certifiable_tier": audit.max_certifiable_tier,
                "claimed_tier_admissible": audit.claimed_tier_admissible,
                "t97_packet_verdict": audit.t97_packet_verdict,
                "t97_table_commitments_valid": audit.t97_table_commitments_valid,
                "wrapper_commitments_valid": audit.wrapper_commitments_valid,
                "authority_partition_admissible": (
                    audit.authority_partition_admissible
                ),
                "authority_profile_name": audit.authority_profile_name,
                "authority_count": audit.authority_count,
                "predata_boundary_respected": audit.predata_boundary_respected,
                "manifest_hash_valid": audit.manifest_hash_valid,
                "committed_wrapper_fields": list(audit.committed_wrapper_fields),
                "missing_provisional_fields": list(audit.missing_provisional_fields),
                "missing_claim_review_fields": list(audit.missing_claim_review_fields),
                "failure_reasons": list(audit.failure_reasons),
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


def _manifest(
    *,
    name: str,
    packet: DetectorDryRunPacket,
    claimed_tier: str,
    wrapper_field_commitments: tuple[WrapperFieldCommitment, ...],
    authority_partition: tuple[tuple[str, ...], ...],
    registered_at: str,
    first_event_not_before: str,
    no_data_analyzed: bool,
    purpose: str,
) -> DetectorPreregistrationManifest:
    table_commitments = _table_commitments(packet)
    manifest = DetectorPreregistrationManifest(
        name=name,
        run_id=packet.run_id,
        registered_at=registered_at,
        first_event_not_before=first_event_not_before,
        claimed_tier=claimed_tier,
        t97_manifest_hash=packet.manifest_hash,
        table_commitments=table_commitments,
        wrapper_field_commitments=wrapper_field_commitments,
        authority_partition=authority_partition,
        no_data_analyzed=no_data_analyzed,
        manifest_hash="",
        purpose=purpose,
    )
    return replace(manifest, manifest_hash=_expected_manifest_hash(manifest))


def _table_commitments(packet: DetectorDryRunPacket) -> tuple[TableHashCommitment, ...]:
    return tuple(
        TableHashCommitment(
            table_name=table.table_name,
            file_name=table.file_name,
            schema_hash=table.schema_hash,
            export_checksum=table.export_checksum,
            join_keys=table.join_keys,
        )
        for table in packet.tables
    )


def _field_commitments(fields: tuple[str, ...]) -> tuple[WrapperFieldCommitment, ...]:
    return tuple(
        WrapperFieldCommitment(
            field_name=field,
            commitment_kind=_commitment_kind(field),
            commitment_hash=_digest(f"t136|{field}|{_commitment_kind(field)}|v0.1"),
        )
        for field in fields
    )


def _commitment_kind(field: str) -> str:
    if field in {"raw_measurement_payload", "causal_ordering_data"}:
        return "export_rule_commitment"
    if field in {"publication_status", "revocation_status", "key_state", "challenge_status"}:
        return "state_commitment"
    return "schema_commitment"


def _fully_separated_authority_partition() -> tuple[tuple[str, ...], ...]:
    return tuple((domain,) for domain in DOMAINS)


def _table_commitment_failures(
    manifest: DetectorPreregistrationManifest,
    packet: DetectorDryRunPacket,
) -> tuple[str, ...]:
    expected = {table.table_name: table for table in _table_commitments(packet)}
    provided = {table.table_name: table for table in manifest.table_commitments}
    failures: list[str] = []
    if set(expected) - set(provided):
        failures.append("missing_t97_table_commitments")
    if _duplicates(table.table_name for table in manifest.table_commitments):
        failures.append("duplicate_t97_table_commitments")
    malformed = [
        table.table_name
        for table in manifest.table_commitments
        if not _is_hash(table.schema_hash) or not _is_hash(table.export_checksum)
    ]
    if malformed:
        failures.append("malformed_t97_table_hashes")
    mismatches = [
        table_name
        for table_name, expected_table in expected.items()
        if table_name in provided and provided[table_name] != expected_table
    ]
    if mismatches:
        failures.append("mismatched_t97_table_commitments")
    if manifest.t97_manifest_hash != packet.manifest_hash:
        failures.append("t97_manifest_hash_mismatch")
    return tuple(failures)


def _predata_failures(manifest: DetectorPreregistrationManifest) -> tuple[str, ...]:
    failures: list[str] = []
    if manifest.registered_at >= manifest.first_event_not_before:
        failures.append("manifest_not_registered_before_first_event")
    if not manifest.no_data_analyzed:
        failures.append("data_accessed_before_manifest_lock")
    return tuple(failures)


def _authority_status(
    partition: tuple[tuple[str, ...], ...],
) -> tuple[bool, str | None, int | None, tuple[str, ...]]:
    provided = {domain for group in partition for domain in group}
    expected = set(DOMAINS)
    failures: list[str] = []
    if provided != expected:
        failures.append("authority_partition_role_set_mismatch")
        return False, None, None, tuple(failures)
    audit = audit_partition(AuthorityPartition(groups=partition))
    if not audit.admissible:
        failures.append(f"authority_partition_inadmissible:{audit.reason}")
    if audit.authority_count < 4:
        failures.append("authority_partition_below_t100_lower_bound")
    return (
        not failures,
        audit.profile_name,
        audit.authority_count,
        tuple(failures),
    )


def _manifest_hash_failures(
    manifest: DetectorPreregistrationManifest,
) -> tuple[str, ...]:
    failures: list[str] = []
    if not _is_hash(manifest.manifest_hash):
        failures.append("malformed_manifest_hash")
    elif manifest.manifest_hash != _expected_manifest_hash(manifest):
        failures.append("manifest_hash_mismatch")
    return tuple(failures)


def _payload_boundary_failures(
    field_map: dict[str, WrapperFieldCommitment],
) -> tuple[str, ...]:
    payload = field_map.get("raw_measurement_payload")
    if payload and payload.commitment_kind == "observed_value_commitment":
        return ("predata_manifest_claims_observed_payload_values",)
    return ()


def _missing_fields(
    fields: tuple[str, ...],
    field_map: dict[str, WrapperFieldCommitment],
) -> tuple[str, ...]:
    return tuple(field for field in fields if field not in field_map)


def _max_certifiable_tier(
    *,
    base_valid: bool,
    malformed_fields: bool,
    payload_boundary_ok: bool,
    missing_provisional: tuple[str, ...],
    missing_claim_review: tuple[str, ...],
) -> str:
    if not base_valid or malformed_fields or not payload_boundary_ok:
        return "none"
    if not missing_provisional and not missing_claim_review:
        return "claim_review"
    if not missing_provisional:
        return "provisional_admission"
    return "raw_log_preservation"


def _interpretation(
    manifest: DetectorPreregistrationManifest,
    max_tier: str,
    claimed_admissible: bool,
    failures: list[str],
) -> str:
    if claimed_admissible:
        return (
            f"{manifest.name} validly claims {manifest.claimed_tier}; the "
            f"strongest certifiable pre-event tier is {max_tier}."
        )
    if manifest.claimed_tier not in ALLOWED_TIERS:
        return "No tier was declared before the run, so later upgrades are barred."
    if "predata_manifest_claims_observed_payload_values" in failures:
        return (
            "The manifest tries to commit observed detector values before the "
            "event boundary; it should commit export rules instead."
        )
    if max_tier != "none" and TIER_RANK[max_tier] < TIER_RANK.get(manifest.claimed_tier, 0):
        return (
            f"The manifest can certify at most {max_tier}, so its "
            f"{manifest.claimed_tier} claim is an overclaim."
        )
    return f"{manifest.name} fails the pre-registration gate: {', '.join(failures)}."


def _expected_manifest_hash(manifest: DetectorPreregistrationManifest) -> str:
    table_lines = [
        "|".join(
            (
                table.table_name,
                table.file_name,
                table.schema_hash,
                table.export_checksum,
                ",".join(table.join_keys),
            )
        )
        for table in sorted(manifest.table_commitments, key=lambda table: table.table_name)
    ]
    field_lines = [
        "|".join((field.field_name, field.commitment_kind, field.commitment_hash))
        for field in sorted(
            manifest.wrapper_field_commitments,
            key=lambda field: field.field_name,
        )
    ]
    authority_line = ";".join(
        "+".join(group) for group in manifest.authority_partition
    )
    payload = "\n".join(
        (
            manifest.name,
            manifest.run_id,
            manifest.registered_at,
            manifest.first_event_not_before,
            manifest.claimed_tier,
            manifest.t97_manifest_hash,
            str(manifest.no_data_analyzed),
            authority_line,
            *table_lines,
            *field_lines,
        )
    )
    return _digest(payload)


def _is_hash(value: str) -> bool:
    return len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _duplicates(values) -> tuple[str, ...]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for value in values:
        if value in seen and value not in duplicates:
            duplicates.append(value)
        seen.add(value)
    return tuple(duplicates)


def _digest(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    import json

    print(json.dumps(t136_result_to_dict(run_t136_analysis()), indent=2))
