"""T178: preserved-rights successor policy screen for the surviving Q1B route.

T176 made the challenge-window freeze burden explicit, but it left one narrow
real-world caveat open: a collaboration may need a predeclared legal, safety,
or emergency successor procedure. This module tests whether any such successor
can preserve Q1B's surviving claim-review rights without collapsing back into
generic post-data override.

The finite answer is narrow. A successor policy can stay live only when it is
predeclared, preserves the same required guardians on every critical action,
preserves already-granted row-review access, preserves guardian identity, and
emits immutable transition logs.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SuccessorTransition:
    transition_id: str
    trigger: str
    predeclared: bool
    preserves_release_guardians: bool
    preserves_revocation_guardians: bool
    preserves_audit_guardians: bool
    preserves_review_access: bool
    preserves_guardian_identity: bool
    immutable_transition_log: bool
    effect: str


@dataclass(frozen=True)
class SuccessorPolicyProfile:
    profile_id: str
    base_t175_valid: bool
    base_t176_frozen: bool
    transitions: tuple[SuccessorTransition, ...]
    purpose: str


@dataclass(frozen=True)
class SuccessorPolicyAudit:
    profile_id: str
    successor_present: bool
    successor_predeclared: bool
    preserves_required_guardians: bool
    preserves_review_access: bool
    preserves_guardian_identity: bool
    immutable_transition_log: bool
    classification: str
    required_next: str
    interpretation: str


@dataclass(frozen=True)
class T178Result:
    audits: tuple[SuccessorPolicyAudit, ...]
    live_profiles: tuple[str, ...]
    null_profiles: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def successor_policy_profiles() -> tuple[SuccessorPolicyProfile, ...]:
    return (
        SuccessorPolicyProfile(
            profile_id="fully_frozen_no_successor_policy",
            base_t175_valid=True,
            base_t176_frozen=True,
            transitions=(),
            purpose=(
                "The challenge-window policy is frozen, with no successor path "
                "available after data collection begins."
            ),
        ),
        SuccessorPolicyProfile(
            profile_id="predeclared_preserved_rights_legal_hold_successor",
            base_t175_valid=True,
            base_t176_frozen=True,
            transitions=(
                SuccessorTransition(
                    transition_id="sealed_review_room_mirror",
                    trigger="predeclared_legal_hold_trigger",
                    predeclared=True,
                    preserves_release_guardians=True,
                    preserves_revocation_guardians=True,
                    preserves_audit_guardians=True,
                    preserves_review_access=True,
                    preserves_guardian_identity=True,
                    immutable_transition_log=True,
                    effect="switch_review_channel_without_changing_guardians",
                ),
            ),
            purpose=(
                "A predeclared legal-hold procedure mirrors the same full row "
                "review into a sealed room without changing guardians, rights, "
                "or immutable audit logs."
            ),
        ),
        SuccessorPolicyProfile(
            profile_id="undeclared_break_glass_successor",
            base_t175_valid=True,
            base_t176_frozen=True,
            transitions=(
                SuccessorTransition(
                    transition_id="unlogged_break_glass_override",
                    trigger="operator_declared_emergency",
                    predeclared=False,
                    preserves_release_guardians=False,
                    preserves_revocation_guardians=False,
                    preserves_audit_guardians=False,
                    preserves_review_access=False,
                    preserves_guardian_identity=False,
                    immutable_transition_log=False,
                    effect="postdata_override_without_precommitment",
                ),
            ),
            purpose=(
                "A break-glass path is available after data collection but was "
                "not frozen pre-data and does not guarantee preserved rights."
            ),
        ),
        SuccessorPolicyProfile(
            profile_id="predeclared_release_pause_pending_governance_clearance",
            base_t175_valid=True,
            base_t176_frozen=True,
            transitions=(
                SuccessorTransition(
                    transition_id="pause_external_row_review",
                    trigger="predeclared_safety_pause_trigger",
                    predeclared=True,
                    preserves_release_guardians=True,
                    preserves_revocation_guardians=True,
                    preserves_audit_guardians=True,
                    preserves_review_access=False,
                    preserves_guardian_identity=True,
                    immutable_transition_log=True,
                    effect="temporary_loss_of_full_row_review_access",
                ),
            ),
            purpose=(
                "A predeclared safety hold keeps the same guardians but pauses "
                "outside row review until governance later reauthorizes access."
            ),
        ),
        SuccessorPolicyProfile(
            profile_id="predeclared_escrow_rotation_successor",
            base_t175_valid=True,
            base_t176_frozen=True,
            transitions=(
                SuccessorTransition(
                    transition_id="replace_escrow_under_legal_order",
                    trigger="predeclared_escrow_rotation_trigger",
                    predeclared=True,
                    preserves_release_guardians=False,
                    preserves_revocation_guardians=False,
                    preserves_audit_guardians=True,
                    preserves_review_access=True,
                    preserves_guardian_identity=False,
                    immutable_transition_log=True,
                    effect="replace_named_escrow_custodian",
                ),
            ),
            purpose=(
                "A predeclared court-order path rotates the named escrow "
                "authority during the challenge window."
            ),
        ),
        SuccessorPolicyProfile(
            profile_id="predeclared_revocation_override_successor",
            base_t175_valid=True,
            base_t176_frozen=True,
            transitions=(
                SuccessorTransition(
                    transition_id="governance_revocation_override",
                    trigger="predeclared_legal_dispute_trigger",
                    predeclared=True,
                    preserves_release_guardians=True,
                    preserves_revocation_guardians=False,
                    preserves_audit_guardians=False,
                    preserves_review_access=True,
                    preserves_guardian_identity=True,
                    immutable_transition_log=True,
                    effect="close_challenge_rights_without_trust_or_escrow",
                ),
            ),
            purpose=(
                "A predeclared dispute path keeps release access but lets "
                "governance close challenge rights without the full guardian set."
            ),
        ),
    )


def audit_successor_policy_profile(
    profile: SuccessorPolicyProfile,
) -> SuccessorPolicyAudit:
    transitions = profile.transitions
    successor_present = bool(transitions)
    successor_predeclared = all(item.predeclared for item in transitions)
    preserves_required_guardians = all(
        item.preserves_release_guardians
        and item.preserves_revocation_guardians
        and item.preserves_audit_guardians
        for item in transitions
    )
    preserves_review_access = all(item.preserves_review_access for item in transitions)
    preserves_guardian_identity = all(
        item.preserves_guardian_identity for item in transitions
    )
    immutable_transition_log = all(
        item.immutable_transition_log for item in transitions
    )

    classification = _classification(
        profile=profile,
        successor_present=successor_present,
        successor_predeclared=successor_predeclared,
        preserves_required_guardians=preserves_required_guardians,
        preserves_review_access=preserves_review_access,
        preserves_guardian_identity=preserves_guardian_identity,
        immutable_transition_log=immutable_transition_log,
    )

    return SuccessorPolicyAudit(
        profile_id=profile.profile_id,
        successor_present=successor_present,
        successor_predeclared=successor_predeclared,
        preserves_required_guardians=preserves_required_guardians,
        preserves_review_access=preserves_review_access,
        preserves_guardian_identity=preserves_guardian_identity,
        immutable_transition_log=immutable_transition_log,
        classification=classification,
        required_next=_required_next(classification),
        interpretation=_interpretation(profile, classification),
    )


def run_t178_analysis() -> T178Result:
    audits = tuple(
        audit_successor_policy_profile(profile)
        for profile in successor_policy_profiles()
    )
    live = tuple(
        audit.profile_id
        for audit in audits
        if audit.classification
        in {
            "live_frozen_without_successor",
            "live_predeclared_preserved_rights_successor",
        }
    )
    nulls = tuple(
        audit.profile_id
        for audit in audits
        if audit.classification
        not in {
            "live_frozen_without_successor",
            "live_predeclared_preserved_rights_successor",
        }
    )

    expected_live = (
        "fully_frozen_no_successor_policy",
        "predeclared_preserved_rights_legal_hold_successor",
    )
    if live != expected_live:
        raise AssertionError("unexpected surviving successor-policy profiles")
    if "undeclared_break_glass_successor" not in nulls:
        raise AssertionError("undeclared break-glass successor must remain null")
    if "predeclared_release_pause_pending_governance_clearance" not in nulls:
        raise AssertionError("rights-reducing successor must remain null")

    return T178Result(
        audits=audits,
        live_profiles=live,
        null_profiles=nulls,
        strongest_claim=(
            "T176's freeze burden admits at most one narrow exception. A "
            "challenge-window successor policy can still count for Q1B only if "
            "it is frozen pre-data, trigger-bounded, preserves the same "
            "mandatory archive, escrow, and trust guardians on every critical "
            "action, preserves already-granted full row-review access, "
            "preserves guardian identity, and emits immutable transition logs."
        ),
        improved=(
            "T178 makes the T176 boundary more realistic without reopening the "
            "governance loophole. The repo can now distinguish a preserved-"
            "rights successor policy from generic post-data override stories."
        ),
        weakened=(
            "This weakens Q1B's last practical exceptions. Predeclared legal, "
            "safety, or emergency procedures do not help unless they preserve "
            "the same review rights and guardian structure throughout the "
            "challenge window."
        ),
        falsification_condition=(
            "T178 fails if a successor policy should still count for Q1B even "
            "though it is undeclared, reduces review access, changes guardian "
            "identity, bypasses archive/escrow/trust on a critical action, or "
            "lacks immutable transition logs."
        ),
        q1b_update=(
            "Q1B remains externally blocked. The T176 freeze burden can be "
            "relaxed only by a T178-valid preserved-rights successor policy; "
            "generic emergency, legal, or safety override stories remain null."
        ),
        claim_ledger_update=(
            "Add T178 to Q1B: a predeclared challenge-window successor policy "
            "counts only when it preserves the same mandatory guardians, full "
            "row-review access, guardian identity, and immutable transition "
            "logging throughout the review window."
        ),
        open_blocker=(
            "No named detector workflow in the repo currently exposes either a "
            "fully frozen challenge-window policy or a predeclared preserved-"
            "rights successor policy package that can be audited pre-data."
        ),
        recommended_next=(
            "Update the Q1B handoff so emergency, legal, or safety exceptions "
            "must either be absent or arrive as a predeclared T178-valid "
            "preserved-rights successor policy with trigger conditions and "
            "transition logs fixed before data collection."
        ),
    )


def t178_result_to_dict(result: T178Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "profile_id": audit.profile_id,
                "successor_present": audit.successor_present,
                "successor_predeclared": audit.successor_predeclared,
                "preserves_required_guardians": audit.preserves_required_guardians,
                "preserves_review_access": audit.preserves_review_access,
                "preserves_guardian_identity": audit.preserves_guardian_identity,
                "immutable_transition_log": audit.immutable_transition_log,
                "classification": audit.classification,
                "required_next": audit.required_next,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "live_profiles": list(result.live_profiles),
        "null_profiles": list(result.null_profiles),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1b_update": result.q1b_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _classification(
    *,
    profile: SuccessorPolicyProfile,
    successor_present: bool,
    successor_predeclared: bool,
    preserves_required_guardians: bool,
    preserves_review_access: bool,
    preserves_guardian_identity: bool,
    immutable_transition_log: bool,
) -> str:
    if not profile.base_t175_valid or not profile.base_t176_frozen:
        return "null_base_policy_invalid"
    if not successor_present:
        return "live_frozen_without_successor"
    if not successor_predeclared or not immutable_transition_log:
        return "null_unpredeclared_or_unlogged_successor"
    if not preserves_review_access:
        return "null_successor_reduces_review_rights"
    if not preserves_required_guardians or not preserves_guardian_identity:
        return "null_successor_changes_required_guardians"
    return "live_predeclared_preserved_rights_successor"


def _required_next(classification: str) -> str:
    if classification == "null_base_policy_invalid":
        return "Repair the base T175/T176 policy before auditing successor paths."
    if classification == "null_unpredeclared_or_unlogged_successor":
        return (
            "Freeze the successor trigger and transition log pre-data or remove "
            "the successor path entirely."
        )
    if classification == "null_successor_reduces_review_rights":
        return (
            "Rewrite the successor policy so full row-review access remains live "
            "throughout the challenge window."
        )
    if classification == "null_successor_changes_required_guardians":
        return (
            "Rewrite the successor policy so archive, escrow, and trust remain "
            "mandatory guardians and named identities do not change."
        )
    if classification == "live_predeclared_preserved_rights_successor":
        return (
            "Publish the successor trigger conditions and immutable transition "
            "log format pre-data."
        )
    return "Publish the fully frozen challenge-window policy pre-data."


def _interpretation(profile: SuccessorPolicyProfile, classification: str) -> str:
    if classification == "live_frozen_without_successor":
        return (
            f"{profile.profile_id} remains live because no post-data successor "
            "path exists."
        )
    if classification == "live_predeclared_preserved_rights_successor":
        return (
            f"{profile.profile_id} remains live because its successor path is "
            "predeclared and preserves guardians, access, identity, and logs."
        )
    if classification == "null_base_policy_invalid":
        return (
            f"{profile.profile_id} is null because its base T175/T176 policy "
            "already fails before successor questions matter."
        )
    effects = ", ".join(transition.effect for transition in profile.transitions)
    return f"{profile.profile_id} is null because its successor path yields: {effects}."


if __name__ == "__main__":
    import json

    print(json.dumps(t178_result_to_dict(run_t178_analysis()), indent=2))
