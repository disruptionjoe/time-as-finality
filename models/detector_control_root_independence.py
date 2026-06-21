"""T161: control-root independence screen for detector authority domains.

T100 and T138 made Q1B depend on a nominal authority partition and a
pre-data manifest. The remaining loophole is nominal federation without
operational independence: labeled authority domains can still collapse if
critical signing, archive, publication, or revocation roots are shared.

This module turns that loophole into an executable screen by quotienting
nominal authority domains by shared critical control roots, then reusing
the T100 authority-partition audit on the effective partition.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.detector_authority_domain_bound import AuthorityPartition, audit_partition


CRITICAL_CONTROL_KINDS: tuple[str, ...] = (
    "manifest_registration",
    "archive_write",
    "audit_attestation",
    "publication_release",
    "revocation_registry",
)


@dataclass(frozen=True)
class ControlRootAssignment:
    domain: str
    capability_kind: str
    root_id: str
    critical: bool


@dataclass(frozen=True)
class ControlRootProfile:
    name: str
    nominal_partition: tuple[tuple[str, ...], ...]
    assignments: tuple[ControlRootAssignment, ...]
    purpose: str


@dataclass(frozen=True)
class ControlRootAudit:
    profile_name: str
    nominal_profile_name: str
    effective_profile_name: str
    nominal_authority_count: int
    effective_authority_count: int
    nominal_admissible: bool
    effective_admissible: bool
    verdict: str
    shared_critical_roots: tuple[str, ...]
    ignored_noncritical_roots: tuple[str, ...]
    effective_partition: tuple[tuple[str, ...], ...]
    failure_reasons: tuple[str, ...]
    interpretation: str


@dataclass(frozen=True)
class T161Result:
    audits: tuple[ControlRootAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def control_root_fixtures() -> tuple[ControlRootProfile, ...]:
    return (
        ControlRootProfile(
            name="four_domain_distinct_critical_roots",
            nominal_partition=(
                ("analysis_governor", "instrument_operator"),
                ("archive_custodian",),
                ("control_designer",),
                ("trust_auditor",),
            ),
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
                    "revocation_registry",
                    "root_revoke_archive",
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
                "A minimal nominally admissible four-domain profile whose "
                "critical control roots stay distinct."
            ),
        ),
        ControlRootProfile(
            name="five_domain_shared_archive_audit_hsm",
            nominal_partition=(
                ("analysis_governor",),
                ("archive_custodian",),
                ("control_designer",),
                ("instrument_operator",),
                ("trust_auditor",),
            ),
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
                "A nominal five-domain federation where archive custody and "
                "trust audit share the same critical signing root."
            ),
        ),
        ControlRootProfile(
            name="five_domain_shared_governance_archive_release_root",
            nominal_partition=(
                ("analysis_governor",),
                ("archive_custodian",),
                ("control_designer",),
                ("instrument_operator",),
                ("trust_auditor",),
            ),
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
                "A nominal five-domain layout where governance and archive "
                "share the same critical release root."
            ),
        ),
        ControlRootProfile(
            name="five_domain_shared_noncritical_dashboard",
            nominal_partition=(
                ("analysis_governor",),
                ("archive_custodian",),
                ("control_designer",),
                ("instrument_operator",),
                ("trust_auditor",),
            ),
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
                "A nominal five-domain workflow that shares only a noncritical "
                "observability dashboard."
            ),
        ),
    )


def audit_control_root_profile(profile: ControlRootProfile) -> ControlRootAudit:
    nominal_audit = audit_partition(AuthorityPartition(groups=profile.nominal_partition))
    effective_partition = _effective_partition(profile)
    effective_audit = audit_partition(AuthorityPartition(groups=effective_partition))
    shared_critical = _shared_root_descriptions(profile, critical_only=True)
    ignored_noncritical = _shared_root_descriptions(profile, critical_only=False)

    if not nominal_audit.admissible:
        verdict = "nominal_partition_already_inadmissible"
        failures = ("nominal_t100_failure",)
    elif effective_audit.admissible:
        verdict = "control_roots_preserve_nominal_independence"
        failures = ()
    else:
        verdict = "hidden_control_root_merge"
        failures = ("shared_critical_control_root_collapses_authority_partition",)

    return ControlRootAudit(
        profile_name=profile.name,
        nominal_profile_name=nominal_audit.profile_name,
        effective_profile_name=effective_audit.profile_name,
        nominal_authority_count=nominal_audit.authority_count,
        effective_authority_count=effective_audit.authority_count,
        nominal_admissible=nominal_audit.admissible,
        effective_admissible=effective_audit.admissible,
        verdict=verdict,
        shared_critical_roots=shared_critical,
        ignored_noncritical_roots=ignored_noncritical,
        effective_partition=effective_partition,
        failure_reasons=failures,
        interpretation=_interpretation(profile, nominal_audit.admissible, effective_audit.admissible, shared_critical),
    )


def run_t161_analysis() -> T161Result:
    audits = tuple(audit_control_root_profile(profile) for profile in control_root_fixtures())
    audit_map = {audit.profile_name: audit for audit in audits}

    if not audit_map["four_domain_distinct_critical_roots"].effective_admissible:
        raise AssertionError("distinct critical roots should preserve admissibility")
    if audit_map["five_domain_shared_archive_audit_hsm"].effective_admissible:
        raise AssertionError("shared archive/audit HSM must collapse admissibility")
    if audit_map["five_domain_shared_governance_archive_release_root"].effective_admissible:
        raise AssertionError("shared governance/archive release root must collapse admissibility")
    if not audit_map["five_domain_shared_noncritical_dashboard"].effective_admissible:
        raise AssertionError("shared noncritical dashboard should not collapse admissibility")

    return T161Result(
        audits=audits,
        strongest_claim=(
            "Nominal authority labels are insufficient for Q1B. A T100/T138-valid "
            "role partition is null if critical control roots are shared, because "
            "the effective authority partition collapses back into self-certifying "
            "governance, archive, or audit control."
        ),
        improved=(
            "T161 converts an implicit governance loophole into an executable "
            "screen. Detector proposals can now be rejected before data if their "
            "archive, audit, publication, manifest, or revocation control roots "
            "quietly merge nominally separate authorities."
        ),
        weakened=(
            "This weakens Q1B again. A workflow does not clear the detector "
            "handoff merely by naming four or five roles; it must also show that "
            "critical packet-control roots do not collapse those roles in practice."
        ),
        falsification_condition=(
            "T161 fails if shared critical control roots can coexist with an "
            "honest detector packet while preserving independent archive and trust "
            "audit powers, or if only noncritical shared services are sufficient "
            "to collapse the effective authority partition."
        ),
        q1b_update=(
            "Q1B remains externally blocked. A future detector deployment must "
            "freeze not only a T100-compatible nominal authority partition but "
            "also evidence that manifest registration, archive mutation, audit "
            "attestation, publication release, and revocation roots are not "
            "shared in a way that collapses the effective partition."
        ),
        claim_ledger_update=(
            "Add T161 to Q1B: nominal four- or five-domain staffing is null when "
            "critical control roots are shared. The operative object is the "
            "effective authority partition after quotienting by shared critical "
            "packet-control roots."
        ),
        open_blocker=(
            "No named detector workflow in the repo currently exposes its critical "
            "control-root map well enough to prove that nominal authority "
            "separation is operationally real."
        ),
        recommended_next=(
            "Extend the Q1B handoff so a proposed deployment must disclose its "
            "manifest-registration, archive-write, audit-attestation, publication, "
            "and revocation control roots alongside the nominal authority roles."
        ),
    )


def t161_result_to_dict(result: T161Result) -> dict[str, object]:
    return {
        "critical_control_kinds": list(CRITICAL_CONTROL_KINDS),
        "audits": [
            {
                "profile_name": audit.profile_name,
                "nominal_profile_name": audit.nominal_profile_name,
                "effective_profile_name": audit.effective_profile_name,
                "nominal_authority_count": audit.nominal_authority_count,
                "effective_authority_count": audit.effective_authority_count,
                "nominal_admissible": audit.nominal_admissible,
                "effective_admissible": audit.effective_admissible,
                "verdict": audit.verdict,
                "shared_critical_roots": list(audit.shared_critical_roots),
                "ignored_noncritical_roots": list(audit.ignored_noncritical_roots),
                "effective_partition": [list(group) for group in audit.effective_partition],
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


def _effective_partition(
    profile: ControlRootProfile,
) -> tuple[tuple[str, ...], ...]:
    domains = sorted({domain for group in profile.nominal_partition for domain in group})
    parent = {domain: domain for domain in domains}

    def find(domain: str) -> str:
        while parent[domain] != domain:
            parent[domain] = parent[parent[domain]]
            domain = parent[domain]
        return domain

    def union(left: str, right: str) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for group in profile.nominal_partition:
        anchor = group[0]
        for domain in group[1:]:
            union(anchor, domain)

    by_root: dict[str, list[str]] = {}
    for assignment in profile.assignments:
        if not assignment.critical:
            continue
        by_root.setdefault(assignment.root_id, []).append(assignment.domain)
    for attached_domains in by_root.values():
        anchor = attached_domains[0]
        for domain in attached_domains[1:]:
            union(anchor, domain)

    grouped: dict[str, list[str]] = {}
    for domain in domains:
        grouped.setdefault(find(domain), []).append(domain)
    return tuple(
        sorted(
            (tuple(sorted(group)) for group in grouped.values()),
            key=lambda group: (len(group), group),
        )
    )


def _shared_root_descriptions(
    profile: ControlRootProfile,
    *,
    critical_only: bool,
) -> tuple[str, ...]:
    by_root: dict[str, list[ControlRootAssignment]] = {}
    for assignment in profile.assignments:
        if assignment.critical != critical_only:
            continue
        by_root.setdefault(assignment.root_id, []).append(assignment)

    descriptions: list[str] = []
    for root_id, assignments in sorted(by_root.items()):
        domains = sorted({assignment.domain for assignment in assignments})
        if len(domains) <= 1:
            continue
        kinds = sorted({assignment.capability_kind for assignment in assignments})
        descriptions.append(
            f"{root_id}:{'+'.join(domains)}:{'+'.join(kinds)}"
        )
    return tuple(descriptions)


def _interpretation(
    profile: ControlRootProfile,
    nominal_admissible: bool,
    effective_admissible: bool,
    shared_critical: tuple[str, ...],
) -> str:
    if not nominal_admissible:
        return f"{profile.name} already fails the nominal T100 authority screen."
    if effective_admissible:
        if shared_critical:
            return (
                f"{profile.name} survives despite shared critical roots, which "
                "would contradict the intended T161 screen."
            )
        return (
            f"{profile.name} preserves its nominal authority split because no "
            "critical control root merges distinct domains."
        )
    return (
        f"{profile.name} is null for Q1B because shared critical roots "
        f"collapse the effective authority partition: {', '.join(shared_critical)}."
    )


if __name__ == "__main__":
    import json

    print(json.dumps(t161_result_to_dict(run_t161_analysis()), indent=2))
