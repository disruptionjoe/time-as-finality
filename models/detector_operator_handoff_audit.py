"""T98: operator-handoff audit for the locked T97 detector packet.

T97 showed that detector-side Q1 currently survives only as a locked pre-data
packet. The next pressure test is operational rather than physical: can a real
lab freeze and populate that packet without role-merging that turns the trust
audit, control declaration, and demotion rules into self-certification?

This module does not create evidence and does not score D1. It checks whether
the T97 packet admits a conflict-free staffing pattern.
"""

from __future__ import annotations

from dataclasses import dataclass


TABLE_OWNER_BY_DOMAIN: dict[str, tuple[str, ...]] = {
    "analysis_governor": (
        "preregistration_manifest",
        "demotion_decision_log",
    ),
    "instrument_operator": ("event_time_tag_stream",),
    "control_designer": (
        "control_pair_manifest",
        "tag_ambiguity_challenge_log",
        "perturbation_trial_log",
    ),
    "archive_custodian": (
        "signature_verification_log",
        "ancestry_dag_edge_export",
    ),
    "trust_auditor": ("trust_boundary_audit_log",),
}

SELF_AUDIT_DOMAINS: tuple[str, ...] = (
    "analysis_governor",
    "instrument_operator",
    "control_designer",
    "archive_custodian",
)

GOVERNANCE_SEPARATION_PAIRS: tuple[tuple[str, str], ...] = (
    ("analysis_governor", "control_designer"),
    ("analysis_governor", "archive_custodian"),
    ("control_designer", "archive_custodian"),
)


@dataclass(frozen=True)
class HandoffProfile:
    name: str
    staff_assignments: dict[str, str]
    purpose: str


@dataclass(frozen=True)
class HandoffAudit:
    profile_name: str
    verdict: str
    distinct_operator_count: int
    independent_trust_auditor: bool
    self_audit_conflicts: tuple[str, ...]
    governance_conflicts: tuple[str, ...]
    owner_by_table: dict[str, str]
    failure_reasons: tuple[str, ...]
    next_allowed_step: str


@dataclass(frozen=True)
class T98Result:
    audits: tuple[HandoffAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def independent_five_domain_profile() -> HandoffProfile:
    return HandoffProfile(
        name="independent_five_domain_profile",
        staff_assignments={
            "analysis_governor": "governance_pi",
            "instrument_operator": "detector_operator",
            "control_designer": "control_engineer",
            "archive_custodian": "archive_engineer",
            "trust_auditor": "external_auditor",
        },
        purpose=(
            "A maximal independence profile: each T97 authority domain has a "
            "distinct owner and the trust audit is external."
        ),
    )


def four_domain_cross_handoff_profile() -> HandoffProfile:
    return HandoffProfile(
        name="four_domain_cross_handoff_profile",
        staff_assignments={
            "analysis_governor": "governance_pi",
            "instrument_operator": "governance_pi",
            "control_designer": "control_engineer",
            "archive_custodian": "archive_engineer",
            "trust_auditor": "external_auditor",
        },
        purpose=(
            "A lean but still separated profile: governance and instrument "
            "operation are merged, but controls, archive custody, and trust "
            "auditing remain independent."
        ),
    )


def three_person_small_lab_profile() -> HandoffProfile:
    return HandoffProfile(
        name="three_person_small_lab_profile",
        staff_assignments={
            "analysis_governor": "pi",
            "instrument_operator": "student",
            "control_designer": "pi",
            "archive_custodian": "postdoc",
            "trust_auditor": "postdoc",
        },
        purpose=(
            "A common small-lab merge: the PI owns governance and control "
            "design, while the archive owner also signs off the trust audit."
        ),
    )


def two_person_pi_student_profile() -> HandoffProfile:
    return HandoffProfile(
        name="two_person_pi_student_profile",
        staff_assignments={
            "analysis_governor": "pi",
            "instrument_operator": "student",
            "control_designer": "pi",
            "archive_custodian": "pi",
            "trust_auditor": "pi",
        },
        purpose=(
            "An underspecified lab where one PI both defines, certifies, and "
            "audits most of the packet."
        ),
    )


def handoff_profile_fixtures() -> tuple[HandoffProfile, ...]:
    return (
        independent_five_domain_profile(),
        four_domain_cross_handoff_profile(),
        three_person_small_lab_profile(),
        two_person_pi_student_profile(),
    )


def audit_operator_handoff(profile: HandoffProfile) -> HandoffAudit:
    assignments = profile.staff_assignments
    missing_domains = set(TABLE_OWNER_BY_DOMAIN) - set(assignments)
    if missing_domains:
        raise ValueError(
            "Profile must assign every T97 authority domain: "
            + ", ".join(sorted(missing_domains))
        )

    owner_by_table = {
        table_name: assignments[domain]
        for domain, tables in TABLE_OWNER_BY_DOMAIN.items()
        for table_name in tables
    }

    auditor = assignments["trust_auditor"]
    self_audit_conflicts = tuple(
        domain
        for domain in SELF_AUDIT_DOMAINS
        if assignments[domain] == auditor
    )
    governance_conflicts = tuple(
        f"{left}={right}"
        for left, right in GOVERNANCE_SEPARATION_PAIRS
        if assignments[left] == assignments[right]
    )

    failure_reasons: list[str] = []
    if self_audit_conflicts:
        failure_reasons.append("trust_auditor_not_independent")
    if governance_conflicts:
        failure_reasons.append("governance_control_archive_role_merge")

    independent_trust_auditor = not self_audit_conflicts
    distinct_operator_count = len(set(assignments.values()))
    if failure_reasons:
        verdict = "inadmissible_due_role_conflicts"
        next_allowed = "split_conflicting_authority_domains_before_freeze"
    else:
        verdict = "admissible_predata_handoff_profile"
        next_allowed = "freeze_t97_packet_with_named_operator_handoffs"

    return HandoffAudit(
        profile_name=profile.name,
        verdict=verdict,
        distinct_operator_count=distinct_operator_count,
        independent_trust_auditor=independent_trust_auditor,
        self_audit_conflicts=self_audit_conflicts,
        governance_conflicts=governance_conflicts,
        owner_by_table=owner_by_table,
        failure_reasons=tuple(failure_reasons),
        next_allowed_step=next_allowed,
    )


def run_t98_analysis() -> T98Result:
    audits = tuple(audit_operator_handoff(profile) for profile in handoff_profile_fixtures())
    five_domain, four_domain, three_person, two_person = audits
    expected_shape = (
        five_domain.verdict == "admissible_predata_handoff_profile"
        and four_domain.verdict == "admissible_predata_handoff_profile"
        and three_person.verdict == "inadmissible_due_role_conflicts"
        and two_person.verdict == "inadmissible_due_role_conflicts"
    )
    strongest_claim = (
        "The surviving detector-side Q1 route is operationally admissible only "
        "if the T97 packet is carried by at least four non-conflicting "
        "authority domains, including an independent trust auditor. Common "
        "two- and three-person role merges collapse the route into "
        "self-certification before any detector evidence exists."
        if expected_shape
        else "The operator-handoff audit did not cleanly separate conflict-free "
        "packet staffing from self-audited or merged-governance profiles."
    )
    return T98Result(
        audits=audits,
        strongest_claim=strongest_claim,
        improved=(
            "T98 converts T97's vague 'operator handoff checks' into an "
            "executable staffing criterion. The detector route can now fail "
            "before data if the same authority both defines controls and "
            "audits them, or both owns the archive and sets demotion policy."
        ),
        weakened=(
            "This weakens detector-side Q1 again. The live bottleneck is not "
            "timing hardware or even schema design; it is conflict-free role "
            "separation. Small labs with merged governance, archive, and "
            "audit roles collapse back into self-certification and should not "
            "treat a filled packet as independent support."
        ),
        falsification_condition=(
            "Demote the detector branch if a realistic deployment cannot name "
            "at least four non-conflicting authority domains with an "
            "independent trust auditor before the first event, or if merged "
            "governance/control/archive roles are allowed to certify the "
            "packet without independent review."
        ),
        q1_update=(
            "Q1 remains partially supported only as a detector-record "
            "admissibility protocol. T98 adds that even the T97 dry-run packet "
            "counts only if its preregistration, control design, archive "
            "custody, instrument operation, and trust audit are separated "
            "enough to prevent self-certification."
        ),
        claim_ledger_update=(
            "Add T98 to Q1 as an operational narrowing: detector-side Q1 now "
            "requires at least four non-conflicting authority domains, "
            "including an independent trust auditor. Common two- and "
            "three-person role merges should demote the route before any "
            "event-level evidence is scored."
        ),
        open_blocker=(
            "No concrete lab deployment in the repo yet names independent "
            "operators for the T97 packet. The live blocker is organizational: "
            "identify a realistic authority split that survives trust-audit "
            "and governance-conflict checks."
        ),
        recommended_next=(
            "Instantiate one named lab staffing plan against the T97 packet "
            "with real operator roles, signed handoff points, and explicit "
            "external or functionally independent trust auditing. If no such "
            "plan is realistic, demote detector provenance below the active "
            "Q1 frontier."
        ),
    )


def t98_result_to_dict(result: T98Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "profile_name": audit.profile_name,
                "verdict": audit.verdict,
                "distinct_operator_count": audit.distinct_operator_count,
                "independent_trust_auditor": audit.independent_trust_auditor,
                "self_audit_conflicts": list(audit.self_audit_conflicts),
                "governance_conflicts": list(audit.governance_conflicts),
                "owner_by_table": audit.owner_by_table,
                "failure_reasons": list(audit.failure_reasons),
                "next_allowed_step": audit.next_allowed_step,
            }
            for audit in result.audits
        ],
        "table_owner_by_domain": {
            domain: list(tables) for domain, tables in TABLE_OWNER_BY_DOMAIN.items()
        },
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }
