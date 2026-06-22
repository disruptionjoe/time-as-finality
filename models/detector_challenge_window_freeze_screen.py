"""T176: challenge-window freeze screen for the surviving Q1B route.

T175 showed that a static threshold or multisig map can preserve the required
guardians on release, revocation, and audit actions. That still leaves one
practical loophole: the guardian roster or critical policy can be changed
during the challenge window itself.

This module asks whether the surviving T171/T173/T175 claim-review route
remains live when challenge-window rights are mutable after data collection.
The answer in this finite audit is no: Q1B needs a frozen challenge-window
policy, not merely a good initial quorum map.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ChallengeWindowMutation:
    mutation_id: str
    target: str
    authorized_by: frozenset[str]
    effect: str
    enabled_during_challenge_window: bool


@dataclass(frozen=True)
class ChallengeWindowFreezeProfile:
    profile_id: str
    base_t175_valid: bool
    mutations: tuple[ChallengeWindowMutation, ...]
    purpose: str


@dataclass(frozen=True)
class ChallengeWindowFreezeAudit:
    profile_id: str
    base_t175_valid: bool
    challenge_window_mutable: bool
    mutable_targets: tuple[str, ...]
    mutable_effects: tuple[str, ...]
    mutable_authorities: tuple[str, ...]
    classification: str
    required_next: str
    interpretation: str


@dataclass(frozen=True)
class T176Result:
    audits: tuple[ChallengeWindowFreezeAudit, ...]
    live_frozen_profiles: tuple[str, ...]
    null_mutable_profiles: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def challenge_window_freeze_profiles() -> tuple[ChallengeWindowFreezeProfile, ...]:
    return (
        ChallengeWindowFreezeProfile(
            profile_id="fully_frozen_challenge_window_policy",
            base_t175_valid=True,
            mutations=(),
            purpose=(
                "The T175-valid guardian and quorum map is frozen until the "
                "challenge window closes."
            ),
        ),
        ChallengeWindowFreezeProfile(
            profile_id="governance_break_glass_release_override",
            base_t175_valid=True,
            mutations=(
                ChallengeWindowMutation(
                    mutation_id="temporary_release_override",
                    target="release_quorums",
                    authorized_by=frozenset(
                        {"analysis_governor", "control_designer"}
                    ),
                    effect="temporary_override_bypassing_archive_and_escrow",
                    enabled_during_challenge_window=True,
                ),
            ),
            purpose=(
                "An emergency governance path can authorize release without the "
                "predeclared archive and escrow guardians."
            ),
        ),
        ChallengeWindowFreezeProfile(
            profile_id="midwindow_escrow_replacement",
            base_t175_valid=True,
            mutations=(
                ChallengeWindowMutation(
                    mutation_id="replace_escrow_custodian",
                    target="guardian_roster",
                    authorized_by=frozenset(
                        {"analysis_governor", "trust_auditor"}
                    ),
                    effect="replace_escrow_before_row_review",
                    enabled_during_challenge_window=True,
                ),
            ),
            purpose=(
                "The named escrow authority can be replaced after data "
                "collection but before challenge-window review completes."
            ),
        ),
        ChallengeWindowFreezeProfile(
            profile_id="trust_suspension_before_revocation",
            base_t175_valid=True,
            mutations=(
                ChallengeWindowMutation(
                    mutation_id="suspend_trust_for_revocation",
                    target="revocation_quorums",
                    authorized_by=frozenset(
                        {"analysis_governor", "archive_custodian"}
                    ),
                    effect="temporary_trust_suspension",
                    enabled_during_challenge_window=True,
                ),
            ),
            purpose=(
                "A dispute process can suspend the trust auditor and then close "
                "challenge rights under a modified revocation rule."
            ),
        ),
        ChallengeWindowFreezeProfile(
            profile_id="postdispute_guardian_addition",
            base_t175_valid=True,
            mutations=(
                ChallengeWindowMutation(
                    mutation_id="add_substitute_auditor_after_dispute",
                    target="audit_quorums",
                    authorized_by=frozenset(
                        {"analysis_governor", "archive_custodian"}
                    ),
                    effect="add_substitute_guardian_postdispute",
                    enabled_during_challenge_window=True,
                ),
            ),
            purpose=(
                "A new guardian can be inserted after a dispute starts, so the "
                "pre-data guardian map no longer determines who controls review."
            ),
        ),
    )


def audit_challenge_window_freeze_profile(
    profile: ChallengeWindowFreezeProfile,
) -> ChallengeWindowFreezeAudit:
    mutable = tuple(
        mutation
        for mutation in profile.mutations
        if mutation.enabled_during_challenge_window
    )
    mutable_targets = tuple(sorted({mutation.target for mutation in mutable}))
    mutable_effects = tuple(sorted({mutation.effect for mutation in mutable}))
    mutable_authorities = tuple(
        sorted(
            {
                authority
                for mutation in mutable
                for authority in mutation.authorized_by
            }
        )
    )

    if not profile.base_t175_valid:
        classification = "null_base_quorum_policy_invalid"
    elif mutable:
        classification = "null_mutable_challenge_window_rights"
    else:
        classification = "live_frozen_challenge_window_policy"

    return ChallengeWindowFreezeAudit(
        profile_id=profile.profile_id,
        base_t175_valid=profile.base_t175_valid,
        challenge_window_mutable=bool(mutable),
        mutable_targets=mutable_targets,
        mutable_effects=mutable_effects,
        mutable_authorities=mutable_authorities,
        classification=classification,
        required_next=_required_next(classification),
        interpretation=_interpretation(profile, classification, mutable),
    )


def run_t176_analysis() -> T176Result:
    audits = tuple(
        audit_challenge_window_freeze_profile(profile)
        for profile in challenge_window_freeze_profiles()
    )
    live = tuple(
        audit.profile_id
        for audit in audits
        if audit.classification == "live_frozen_challenge_window_policy"
    )
    null_mutable = tuple(
        audit.profile_id
        for audit in audits
        if audit.classification == "null_mutable_challenge_window_rights"
    )

    if live != ("fully_frozen_challenge_window_policy",):
        raise AssertionError("exactly one frozen challenge-window profile should survive")
    if "governance_break_glass_release_override" not in null_mutable:
        raise AssertionError("break-glass release override must remain null")
    if "midwindow_escrow_replacement" not in null_mutable:
        raise AssertionError("mid-window escrow replacement must remain null")

    return T176Result(
        audits=audits,
        live_frozen_profiles=live,
        null_mutable_profiles=null_mutable,
        strongest_claim=(
            "A T175-valid static quorum map is still insufficient for Q1B if "
            "challenge-window rights can be changed after data collection. The "
            "surviving T171/T173/T175 route stays live only when the guardian "
            "roster and critical release, revocation, and audit policies are "
            "frozen until challenge-window expiry."
        ),
        improved=(
            "T176 removes a policy-layer loophole from Q1B. The repo can now "
            "distinguish a genuinely precommitted claim-review process from one "
            "that merely starts with good guardians and then rewrites them under "
            "pressure."
        ),
        weakened=(
            "This weakens Q1B again. A detector workflow does not clear the "
            "current frontier just by publishing an admissible initial quorum "
            "map. Break-glass overrides, mid-window guardian replacement, or "
            "temporary suspension of trust or escrow make the challenge rights "
            "contingent rather than fixed."
        ),
        falsification_condition=(
            "T176 fails if a detector workflow should still count for Q1B even "
            "though it can change guardian identity or critical release, "
            "revocation, or audit rules during the challenge window after data "
            "collection begins."
        ),
        q1b_update=(
            "Q1B remains externally blocked. A T175-valid quorum map counts "
            "only if the guardian roster and critical challenge-window action "
            "policies are frozen until the review window closes."
        ),
        claim_ledger_update=(
            "Add T176 to Q1B: static guardian quorums are scaffold-only if "
            "release, revocation, audit, or guardian-identity rules can be "
            "rewritten during the challenge window. The surviving route now "
            "requires a pre-data challenge-window freeze."
        ),
        open_blocker=(
            "No named detector workflow in the repo currently exposes a "
            "pre-data freeze policy proving that challenge-window guardians and "
            "critical rights cannot be changed after data collection."
        ),
        recommended_next=(
            "Update the Q1B handoff to require a signed challenge-window freeze "
            "policy in addition to the T175 quorum map. If a realistic group "
            "needs break-glass override or mid-window guardian rotation, "
            "demote Q1B below the active frontier."
        ),
    )


def t176_result_to_dict(result: T176Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "profile_id": audit.profile_id,
                "base_t175_valid": audit.base_t175_valid,
                "challenge_window_mutable": audit.challenge_window_mutable,
                "mutable_targets": list(audit.mutable_targets),
                "mutable_effects": list(audit.mutable_effects),
                "mutable_authorities": list(audit.mutable_authorities),
                "classification": audit.classification,
                "required_next": audit.required_next,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "live_frozen_profiles": list(result.live_frozen_profiles),
        "null_mutable_profiles": list(result.null_mutable_profiles),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1b_update": result.q1b_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _required_next(classification: str) -> str:
    if classification == "null_base_quorum_policy_invalid":
        return "Repair the base T175 guardian quorum map before challenge-window freeze matters."
    if classification == "null_mutable_challenge_window_rights":
        return (
            "Freeze guardian identity and critical release, revocation, and "
            "audit policies until challenge-window expiry."
        )
    return "Publish the signed challenge-window freeze policy pre-data."


def _interpretation(
    profile: ChallengeWindowFreezeProfile,
    classification: str,
    mutable: tuple[ChallengeWindowMutation, ...],
) -> str:
    if classification == "live_frozen_challenge_window_policy":
        return (
            f"{profile.profile_id} is the only live finite profile because the "
            "pre-data guardian and action map cannot be changed during review."
        )
    if classification == "null_base_quorum_policy_invalid":
        return (
            f"{profile.profile_id} is already null because its base T175 quorum "
            "policy fails before mutation questions matter."
        )
    effects = ", ".join(mutation.effect for mutation in mutable)
    return (
        f"{profile.profile_id} is null because challenge-window rights remain "
        f"mutable after data collection: {effects}."
    )


if __name__ == "__main__":
    import json

    print(json.dumps(t176_result_to_dict(run_t176_analysis()), indent=2))
