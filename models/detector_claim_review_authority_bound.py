"""T173: authority lower bound for the T171 claim-review detector route.

T100 proved that the pre-data T97/T98 detector packet needs at least four
authority domains. T171 then sharpened the only surviving Q1B route: claim
review requires full reviewable event rows during the challenge window with
independent escrow.

This module asks whether that stronger T171 burden changes the exact authority
lower bound. It stays at detector evidence infrastructure only.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.detector_authority_domain_bound import (
    AuthorityPartition,
    enumerate_partitions,
)
from models.detector_operator_handoff_audit import (
    GOVERNANCE_SEPARATION_PAIRS,
    SELF_AUDIT_DOMAINS,
)


CLAIM_REVIEW_DOMAINS: tuple[str, ...] = (
    "analysis_governor",
    "instrument_operator",
    "control_designer",
    "archive_custodian",
    "trust_auditor",
    "escrow_custodian",
)

ESCROW_SEPARATION_DOMAINS: tuple[str, ...] = (
    "analysis_governor",
    "instrument_operator",
    "control_designer",
    "archive_custodian",
    "trust_auditor",
)


@dataclass(frozen=True)
class ClaimReviewPartitionAudit:
    profile_name: str
    authority_count: int
    partition: tuple[tuple[str, ...], ...]
    admissible: bool
    trust_auditor_independent: bool
    governance_conflicts: tuple[str, ...]
    escrow_conflicts: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class T173Result:
    audits: tuple[ClaimReviewPartitionAudit, ...]
    minimum_admissible_authority_count: int
    no_four_domain_profile_survives: bool
    admissible_five_domain_profiles: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def audit_claim_review_partition(
    partition: AuthorityPartition,
) -> ClaimReviewPartitionAudit:
    owner_by_domain = {
        domain: index
        for index, group in enumerate(partition.groups)
        for domain in group
    }

    trust_auditor_independent = all(
        owner_by_domain["trust_auditor"] != owner_by_domain[domain]
        for domain in SELF_AUDIT_DOMAINS + ("escrow_custodian",)
    )
    governance_conflicts = tuple(
        f"{left}={right}"
        for left, right in GOVERNANCE_SEPARATION_PAIRS
        if owner_by_domain[left] == owner_by_domain[right]
    )
    escrow_conflicts = tuple(
        domain
        for domain in ESCROW_SEPARATION_DOMAINS
        if owner_by_domain["escrow_custodian"] == owner_by_domain[domain]
    )

    admissible = (
        trust_auditor_independent
        and not governance_conflicts
        and not escrow_conflicts
    )
    if admissible:
        reason = "conflict_free_claim_review_partition"
    elif not trust_auditor_independent:
        reason = "trust_auditor_not_independent"
    elif governance_conflicts:
        reason = "governance_control_archive_role_merge"
    else:
        reason = "escrow_not_independent"

    return ClaimReviewPartitionAudit(
        profile_name=partition.profile_name,
        authority_count=partition.authority_count,
        partition=partition.groups,
        admissible=admissible,
        trust_auditor_independent=trust_auditor_independent,
        governance_conflicts=governance_conflicts,
        escrow_conflicts=escrow_conflicts,
        reason=reason,
    )


def run_t173_analysis() -> T173Result:
    audits = tuple(
        audit_claim_review_partition(partition)
        for partition in enumerate_partitions(CLAIM_REVIEW_DOMAINS)
    )
    admissible = tuple(audit for audit in audits if audit.admissible)
    minimum = min(audit.authority_count for audit in admissible)
    admissible_five_domain_profiles = tuple(
        audit.profile_name for audit in admissible if audit.authority_count == minimum
    )
    no_four_domain_profile_survives = not any(
        audit.admissible and audit.authority_count <= 4 for audit in audits
    )

    return T173Result(
        audits=audits,
        minimum_admissible_authority_count=minimum,
        no_four_domain_profile_survives=no_four_domain_profile_survives,
        admissible_five_domain_profiles=admissible_five_domain_profiles,
        strongest_claim=(
            "T173 upgrades the T100 lower bound for the only surviving T171 "
            "claim-review route. Once full reviewable rows with independent "
            "escrow are treated as a real authority burden, no four-domain "
            "profile survives. The exact minimum becomes five authority domains, "
            "with only three minimal merge classes: instrument operation merged "
            "with exactly one of governance, control design, or archive custody."
        ),
        improved=(
            "T173 removes another ambiguity from Q1B. The repo no longer has to "
            "talk loosely about a reviewable-row federation. It can state the "
            "exact operational lower bound for the surviving claim-review path."
        ),
        weakened=(
            "This weakens Q1B again. T100's four-domain lower bound still covers "
            "weaker pre-data packet or scaffold talk, but it is no longer enough "
            "for the lone T171 live route. Any claim-review deployment that lacks "
            "a separate escrow authority should be rejected before detector "
            "evidence is discussed."
        ),
        falsification_condition=(
            "T173 fails if T171-level independent escrow can be implemented "
            "without a separate escrow authority while preserving outside "
            "challenge rights, or if a four-domain claim-review partition "
            "survives once escrow independence is stated operationally."
        ),
        q1b_update=(
            "Q1B remains externally blocked. For the only surviving T171 "
            "claim-review route, the detector packet now has a hard five-domain "
            "lower bound: governance, control, archive, trust audit, and "
            "independent escrow must remain conflict-free, with instrument "
            "operation mergeable into only one of governance, control, or archive."
        ),
        claim_ledger_update=(
            "Add T173 to Q1B: the T171 reviewable-row route is stricter than "
            "the older T100 packet. Once independent escrow is included, no "
            "four-domain claim-review profile survives; the exact minimum is "
            "five authority domains."
        ),
        open_blocker=(
            "The repo still has no named workflow that can supply both a "
            "T161-valid control-root map and the extra independent escrow "
            "authority demanded by T171 claim review."
        ),
        recommended_next=(
            "Update the Q1B deployment handoff to require a named escrow "
            "authority and then map one realistic collaboration onto one of the "
            "three surviving five-domain claim-review profiles. If none fits, "
            "demote Q1B below the active frontier."
        ),
    )


def t173_result_to_dict(result: T173Result) -> dict[str, object]:
    return {
        "claim_review_domains": list(CLAIM_REVIEW_DOMAINS),
        "escrow_separation_domains": list(ESCROW_SEPARATION_DOMAINS),
        "audits": [
            {
                "profile_name": audit.profile_name,
                "authority_count": audit.authority_count,
                "partition": [list(group) for group in audit.partition],
                "admissible": audit.admissible,
                "trust_auditor_independent": audit.trust_auditor_independent,
                "governance_conflicts": list(audit.governance_conflicts),
                "escrow_conflicts": list(audit.escrow_conflicts),
                "reason": audit.reason,
            }
            for audit in result.audits
        ],
        "minimum_admissible_authority_count": result.minimum_admissible_authority_count,
        "no_four_domain_profile_survives": result.no_four_domain_profile_survives,
        "admissible_five_domain_profiles": list(result.admissible_five_domain_profiles),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1b_update": result.q1b_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }
