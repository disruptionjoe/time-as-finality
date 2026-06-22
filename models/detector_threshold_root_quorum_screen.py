"""T175: threshold-root quorum screen for the surviving Q1B claim-review route.

T161 rejects nominally separate detector authorities when critical packet roots
are simply shared. A realistic collaboration could reply that it uses threshold
keys or multisig release rather than one shared HSM. This module tests whether
that rescues Q1B's surviving T171/T173 route.

The screen is intentionally narrow. It audits only the claim-review phase where
full event rows must remain reviewable during the challenge window with
independent escrow and trust audit. The question is whether quorum-controlled
release and revocation still preserve those independent challenge rights.
"""

from __future__ import annotations

from dataclasses import dataclass


RELEASE_REQUIRED_DOMAINS = frozenset({"archive_custodian", "escrow_custodian"})
REVOCATION_REQUIRED_DOMAINS = frozenset({"trust_auditor", "escrow_custodian"})
AUDIT_REQUIRED_DOMAINS = frozenset({"trust_auditor"})


@dataclass(frozen=True)
class ThresholdRootPolicy:
    policy_id: str
    release_quorums: tuple[frozenset[str], ...]
    revocation_quorums: tuple[frozenset[str], ...]
    audit_quorums: tuple[frozenset[str], ...]
    purpose: str


@dataclass(frozen=True)
class ThresholdRootAudit:
    policy_id: str
    release_guardians_preserved: bool
    revocation_guardians_preserved: bool
    audit_guardians_preserved: bool
    release_bypass_domains: tuple[str, ...]
    revocation_bypass_domains: tuple[str, ...]
    audit_bypass_domains: tuple[str, ...]
    classification: str
    required_next: str
    interpretation: str


@dataclass(frozen=True)
class T175Result:
    audits: tuple[ThresholdRootAudit, ...]
    live_threshold_policies: tuple[str, ...]
    null_release_bypass_policies: tuple[str, ...]
    null_revocation_bypass_policies: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def threshold_root_policies() -> tuple[ThresholdRootPolicy, ...]:
    return (
        ThresholdRootPolicy(
            policy_id="mandatory_archive_and_escrow_release",
            release_quorums=(
                frozenset({"archive_custodian", "escrow_custodian"}),
                frozenset(
                    {"archive_custodian", "escrow_custodian", "trust_auditor"}
                ),
            ),
            revocation_quorums=(
                frozenset({"trust_auditor", "escrow_custodian"}),
                frozenset(
                    {"analysis_governor", "trust_auditor", "escrow_custodian"}
                ),
            ),
            audit_quorums=(
                frozenset({"trust_auditor"}),
                frozenset({"trust_auditor", "analysis_governor"}),
            ),
            purpose=(
                "Every authorized row-release coalition contains archive custody "
                "and escrow, and every revocation coalition contains trust audit "
                "and escrow."
            ),
        ),
        ThresholdRootPolicy(
            policy_id="optional_escrow_two_of_three_release",
            release_quorums=(
                frozenset({"analysis_governor", "archive_custodian"}),
                frozenset({"archive_custodian", "escrow_custodian"}),
                frozenset({"analysis_governor", "escrow_custodian"}),
            ),
            revocation_quorums=(frozenset({"trust_auditor", "escrow_custodian"}),),
            audit_quorums=(frozenset({"trust_auditor"}),),
            purpose=(
                "Escrow is named as one possible release signer, but governance "
                "and archive can authorize challenge-window row release without it."
            ),
        ),
        ThresholdRootPolicy(
            policy_id="optional_archive_three_of_four_release",
            release_quorums=(
                frozenset(
                    {"analysis_governor", "trust_auditor", "escrow_custodian"}
                ),
                frozenset(
                    {"archive_custodian", "trust_auditor", "escrow_custodian"}
                ),
            ),
            revocation_quorums=(frozenset({"trust_auditor", "escrow_custodian"}),),
            audit_quorums=(frozenset({"trust_auditor"}),),
            purpose=(
                "Escrow is mandatory for release, but archive custody is only "
                "optional because another quorum can publish rows without it."
            ),
        ),
        ThresholdRootPolicy(
            policy_id="optional_trust_two_of_three_revocation",
            release_quorums=(frozenset({"archive_custodian", "escrow_custodian"}),),
            revocation_quorums=(
                frozenset({"analysis_governor", "escrow_custodian"}),
                frozenset({"trust_auditor", "escrow_custodian"}),
            ),
            audit_quorums=(frozenset({"trust_auditor"}),),
            purpose=(
                "Escrow exists, but a governance-plus-escrow coalition can close "
                "challenge rights without trust-auditor participation."
            ),
        ),
        ThresholdRootPolicy(
            policy_id="global_three_of_five_multisig",
            release_quorums=(
                frozenset(
                    {"analysis_governor", "archive_custodian", "trust_auditor"}
                ),
                frozenset(
                    {"analysis_governor", "control_designer", "escrow_custodian"}
                ),
            ),
            revocation_quorums=(
                frozenset(
                    {"analysis_governor", "archive_custodian", "escrow_custodian"}
                ),
                frozenset(
                    {"control_designer", "trust_auditor", "escrow_custodian"}
                ),
            ),
            audit_quorums=(
                frozenset({"analysis_governor", "archive_custodian"}),
                frozenset({"trust_auditor", "control_designer"}),
            ),
            purpose=(
                "A generic multisig looks distributed, but different critical "
                "actions can still be authorized by coalitions that bypass the "
                "guardians Q1B needs."
            ),
        ),
    )


def audit_threshold_root_policy(policy: ThresholdRootPolicy) -> ThresholdRootAudit:
    release_bypass = _guardian_bypass(policy.release_quorums, RELEASE_REQUIRED_DOMAINS)
    revocation_bypass = _guardian_bypass(
        policy.revocation_quorums,
        REVOCATION_REQUIRED_DOMAINS,
    )
    audit_bypass = _guardian_bypass(policy.audit_quorums, AUDIT_REQUIRED_DOMAINS)

    release_ok = not release_bypass
    revocation_ok = not revocation_bypass
    audit_ok = not audit_bypass

    classification = _classification(release_bypass, revocation_bypass, audit_bypass)
    return ThresholdRootAudit(
        policy_id=policy.policy_id,
        release_guardians_preserved=release_ok,
        revocation_guardians_preserved=revocation_ok,
        audit_guardians_preserved=audit_ok,
        release_bypass_domains=release_bypass,
        revocation_bypass_domains=revocation_bypass,
        audit_bypass_domains=audit_bypass,
        classification=classification,
        required_next=_required_next(classification),
        interpretation=_interpretation(
            policy,
            classification,
            release_bypass,
            revocation_bypass,
            audit_bypass,
        ),
    )


def run_t175_analysis() -> T175Result:
    audits = tuple(
        audit_threshold_root_policy(policy) for policy in threshold_root_policies()
    )
    live = tuple(
        audit.policy_id
        for audit in audits
        if audit.classification == "live_threshold_claim_review_policy"
    )
    null_release = tuple(
        audit.policy_id
        for audit in audits
        if audit.classification == "null_release_quorum_bypasses_required_guardian"
    )
    null_revocation = tuple(
        audit.policy_id
        for audit in audits
        if audit.classification == "null_revocation_or_audit_quorum_bypasses_required_guardian"
    )

    if live != ("mandatory_archive_and_escrow_release",):
        raise AssertionError("exactly one threshold-root policy should preserve Q1B rights")
    if "optional_escrow_two_of_three_release" not in null_release:
        raise AssertionError("optional-escrow release must remain null")
    if "optional_trust_two_of_three_revocation" not in null_revocation:
        raise AssertionError("optional-trust revocation must remain null")

    return T175Result(
        audits=audits,
        live_threshold_policies=live,
        null_release_bypass_policies=null_release,
        null_revocation_bypass_policies=null_revocation,
        strongest_claim=(
            "Threshold or multisig root control does not rescue Q1B merely by "
            "naming escrow or trust audit as possible signers. For the "
            "surviving T171/T173 claim-review route, every authorized "
            "challenge-window row-release quorum must include both archive "
            "custody and escrow, and every authorized revocation quorum must "
            "include both trust audit and escrow."
        ),
        improved=(
            "T175 removes a realistic governance loophole from T161/T173. The "
            "repo can now evaluate threshold-key or multisig stories without "
            "collapsing them either into naive shared-root failure or into "
            "unexamined 'distributed control' optimism."
        ),
        weakened=(
            "This weakens Q1B again. A collaboration does not clear the "
            "claim-review route by putting escrow or trust on one branch of a "
            "quorum tree. If any authorized release or revocation coalition can "
            "bypass those guardians, independent challenge rights are only "
            "rhetorical."
        ),
        falsification_condition=(
            "T175 fails if a threshold-controlled row-release or revocation "
            "policy should still count for Q1B even though some authorized "
            "coalition omits archive custody, escrow, or trust audit from the "
            "critical challenge-window actions they are meant to guard."
        ),
        q1b_update=(
            "Q1B remains externally blocked. A threshold-key or multisig "
            "workflow is admissible only when escrow is a mandatory signer in "
            "every authorized challenge-window release and revocation quorum, "
            "archive custody is mandatory in every release quorum, and trust "
            "audit is mandatory in every revocation or audit quorum."
        ),
        claim_ledger_update=(
            "Add T175 to Q1B: threshold or multisig control is null whenever "
            "challenge-window release or revocation can be authorized by a "
            "coalition that bypasses archive custody, escrow, or trust audit. "
            "Those guardians must be mandatory members of every authorized "
            "critical quorum, not optional signers."
        ),
        open_blocker=(
            "No named detector workflow in the repo currently publishes the "
            "critical release and revocation quorum map needed to show that "
            "escrow and trust are mandatory rather than optional guardians."
        ),
        recommended_next=(
            "Update the Q1B handoff to require a pre-data quorum map for "
            "challenge-window row release, audit attestation, and revocation. "
            "If a realistic collaboration can only offer optional-escrow or "
            "optional-trust multisig, demote Q1B below the active frontier."
        ),
    )


def t175_result_to_dict(result: T175Result) -> dict[str, object]:
    return {
        "release_required_domains": sorted(RELEASE_REQUIRED_DOMAINS),
        "revocation_required_domains": sorted(REVOCATION_REQUIRED_DOMAINS),
        "audit_required_domains": sorted(AUDIT_REQUIRED_DOMAINS),
        "audits": [
            {
                "policy_id": audit.policy_id,
                "release_guardians_preserved": audit.release_guardians_preserved,
                "revocation_guardians_preserved": audit.revocation_guardians_preserved,
                "audit_guardians_preserved": audit.audit_guardians_preserved,
                "release_bypass_domains": list(audit.release_bypass_domains),
                "revocation_bypass_domains": list(audit.revocation_bypass_domains),
                "audit_bypass_domains": list(audit.audit_bypass_domains),
                "classification": audit.classification,
                "required_next": audit.required_next,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "live_threshold_policies": list(result.live_threshold_policies),
        "null_release_bypass_policies": list(result.null_release_bypass_policies),
        "null_revocation_bypass_policies": list(result.null_revocation_bypass_policies),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1b_update": result.q1b_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _guardian_bypass(
    quorums: tuple[frozenset[str], ...],
    required_domains: frozenset[str],
) -> tuple[str, ...]:
    bypassed = {
        domain
        for quorum in quorums
        for domain in required_domains
        if domain not in quorum
    }
    return tuple(sorted(bypassed))


def _classification(
    release_bypass: tuple[str, ...],
    revocation_bypass: tuple[str, ...],
    audit_bypass: tuple[str, ...],
) -> str:
    if not release_bypass and not revocation_bypass and not audit_bypass:
        return "live_threshold_claim_review_policy"
    if release_bypass:
        return "null_release_quorum_bypasses_required_guardian"
    return "null_revocation_or_audit_quorum_bypasses_required_guardian"


def _required_next(classification: str) -> str:
    if classification == "null_release_quorum_bypasses_required_guardian":
        return (
            "Rewrite the release quorum so every authorized challenge-window "
            "row-release coalition includes both archive custody and escrow."
        )
    if classification == "null_revocation_or_audit_quorum_bypasses_required_guardian":
        return (
            "Rewrite the revocation and audit quorums so trust audit and escrow "
            "cannot be bypassed on critical challenge-window actions."
        )
    return "Publish the quorum map pre-data and obtain a named collaboration willing to sign it."


def _interpretation(
    policy: ThresholdRootPolicy,
    classification: str,
    release_bypass: tuple[str, ...],
    revocation_bypass: tuple[str, ...],
    audit_bypass: tuple[str, ...],
) -> str:
    if classification == "live_threshold_claim_review_policy":
        return (
            f"{policy.policy_id} preserves the full T171/T173 guardian set "
            "under threshold control and is the only live quorum policy in the "
            "current fixture family."
        )
    missing = release_bypass + revocation_bypass + audit_bypass
    return (
        f"{policy.policy_id} is null because its authorized coalitions can bypass "
        f"{', '.join(sorted(set(missing)))} on critical challenge-window actions."
    )


if __name__ == "__main__":
    import json

    print(json.dumps(t175_result_to_dict(run_t175_analysis()), indent=2))
