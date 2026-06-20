"""T100: exact authority-domain lower bound for the T97/T98 detector route.

T98 showed by example that some staffing profiles keep the detector packet
operationally admissible while common small-lab merges collapse it into
self-certification. T100 upgrades that example-level result into a finite
enumeration over all role partitions of the T97 authority domains.

This module does not produce detector evidence. It computes the exact minimal
number of authority domains compatible with the current governance and trust
separation constraints.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.detector_operator_handoff_audit import (
    GOVERNANCE_SEPARATION_PAIRS,
    SELF_AUDIT_DOMAINS,
    TABLE_OWNER_BY_DOMAIN,
)


DOMAINS: tuple[str, ...] = tuple(TABLE_OWNER_BY_DOMAIN)


@dataclass(frozen=True)
class AuthorityPartition:
    groups: tuple[tuple[str, ...], ...]

    @property
    def authority_count(self) -> int:
        return len(self.groups)

    @property
    def profile_name(self) -> str:
        merged = ["+".join(group) for group in self.groups if len(group) > 1]
        if not merged:
            return "fully_separated_five_domain_profile"
        return "merge_" + "__".join(merged)


@dataclass(frozen=True)
class PartitionAudit:
    profile_name: str
    authority_count: int
    partition: tuple[tuple[str, ...], ...]
    admissible: bool
    trust_auditor_independent: bool
    governance_conflicts: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class T100Result:
    audits: tuple[PartitionAudit, ...]
    admissible_four_domain_profiles: tuple[str, ...]
    minimum_admissible_authority_count: int
    no_three_domain_profile_survives: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def enumerate_partitions(items: tuple[str, ...]) -> tuple[AuthorityPartition, ...]:
    groups: list[list[list[str]]] = []

    def backtrack(index: int, current: list[list[str]]) -> None:
        if index == len(items):
            canonical = sorted(tuple(sorted(group)) for group in current)
            groups.append([list(group) for group in canonical])
            return

        item = items[index]
        for position in range(len(current)):
            current[position].append(item)
            backtrack(index + 1, current)
            current[position].pop()

        current.append([item])
        backtrack(index + 1, current)
        current.pop()

    backtrack(0, [])

    unique: dict[tuple[tuple[str, ...], ...], AuthorityPartition] = {}
    for grouping in groups:
        key = tuple(tuple(group) for group in grouping)
        unique.setdefault(key, AuthorityPartition(groups=key))
    return tuple(sorted(unique.values(), key=lambda part: (part.authority_count, part.groups)))


def audit_partition(partition: AuthorityPartition) -> PartitionAudit:
    owner_by_domain = {
        domain: index
        for index, group in enumerate(partition.groups)
        for domain in group
    }

    trust_auditor_independent = all(
        owner_by_domain["trust_auditor"] != owner_by_domain[domain]
        for domain in SELF_AUDIT_DOMAINS
    )
    governance_conflicts = tuple(
        f"{left}={right}"
        for left, right in GOVERNANCE_SEPARATION_PAIRS
        if owner_by_domain[left] == owner_by_domain[right]
    )

    admissible = trust_auditor_independent and not governance_conflicts
    if admissible:
        reason = "conflict_free_partition"
    elif not trust_auditor_independent:
        reason = "trust_auditor_not_independent"
    else:
        reason = "governance_control_archive_role_merge"

    return PartitionAudit(
        profile_name=partition.profile_name,
        authority_count=partition.authority_count,
        partition=partition.groups,
        admissible=admissible,
        trust_auditor_independent=trust_auditor_independent,
        governance_conflicts=governance_conflicts,
        reason=reason,
    )


def run_t100_analysis() -> T100Result:
    audits = tuple(audit_partition(partition) for partition in enumerate_partitions(DOMAINS))
    admissible = tuple(audit for audit in audits if audit.admissible)
    minimum = min(audit.authority_count for audit in admissible)
    admissible_four_domain_profiles = tuple(
        audit.profile_name
        for audit in admissible
        if audit.authority_count == minimum
    )
    no_three_domain_profile_survives = not any(
        audit.admissible and audit.authority_count <= 3 for audit in audits
    )

    strongest_claim = (
        "T100 proves that the current T97/T98 detector route requires at least "
        "four non-conflicting authority domains. The lower bound is exact: "
        "there are exactly three admissible four-domain merge classes, each "
        "merging instrument operation with exactly one of governance, control "
        "design, or archive custody while keeping trust auditing separate."
    )

    return T100Result(
        audits=audits,
        admissible_four_domain_profiles=admissible_four_domain_profiles,
        minimum_admissible_authority_count=minimum,
        no_three_domain_profile_survives=no_three_domain_profile_survives,
        strongest_claim=strongest_claim,
        improved=(
            "T100 replaces T98's example-level staffing judgment with a finite "
            "combinatorial audit over every partition of the five T97 "
            "authority domains. The detector branch now has an exact "
            "operational lower bound rather than a suggestive staffing story."
        ),
        weakened=(
            "This narrows detector-side Q1 again. Any two- or three-person "
            "deployment is ruled out by structure, not pessimism: the trust "
            "auditor must be independent, and governance, control design, and "
            "archive custody cannot collapse into one authority. Small-lab "
            "future-deployment narratives should therefore be treated as null "
            "unless they change the packet itself."
        ),
        falsification_condition=(
            "T100 fails if the T97 packet can be redefined so that an "
            "admissible partition with three or fewer authority domains "
            "exists without allowing trust self-audit or governance/control/"
            "archive self-certification, or if a real deployment shows that "
            "one of T98's current separation constraints is unnecessary."
        ),
        q1_update=(
            "Q1 remains partially supported only as a detector-record "
            "admissibility protocol. T100 strengthens the operational "
            "narrowing: under the current packet, detector-side Q1 has a hard "
            "four-authority lower bound and should be demoted for any proposed "
            "deployment that cannot meet it pre-data."
        ),
        claim_ledger_update=(
            "Add T100 to Q1 as an exact combinatorial obstruction: the current "
            "T97/T98 packet admits no admissible staffing profile with fewer "
            "than four authority domains, and the only minimal surviving "
            "profiles merge instrument operation with exactly one other "
            "non-auditing role."
        ),
        open_blocker=(
            "The repo still lacks a named real lab organization that fits one "
            "of T100's three minimal four-domain patterns while also freezing "
            "the T97 packet before first event."
        ),
        recommended_next=(
            "Map one concrete lab onto each of the three minimal four-domain "
            "profiles and reject the detector route unless at least one can be "
            "staffed, signed, and frozen pre-data without hidden role merges."
        ),
    )


def t100_result_to_dict(result: T100Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "profile_name": audit.profile_name,
                "authority_count": audit.authority_count,
                "partition": [list(group) for group in audit.partition],
                "admissible": audit.admissible,
                "trust_auditor_independent": audit.trust_auditor_independent,
                "governance_conflicts": list(audit.governance_conflicts),
                "reason": audit.reason,
            }
            for audit in result.audits
        ],
        "admissible_four_domain_profiles": list(result.admissible_four_domain_profiles),
        "minimum_admissible_authority_count": result.minimum_admissible_authority_count,
        "no_three_domain_profile_survives": result.no_three_domain_profile_survives,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }
