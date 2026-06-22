"""T171: row-review substitution screen for the surviving Q1B route.

T169 left one narrow live deployment class: a pre-data claim-review federation
with distinct critical control roots and a commitment to later reviewable
event-level rows. This module tests the remaining ambiguity inside that
survivor: can summaries, proofs, delayed release, sampled rows, or private
escrow substitute for reviewable full rows without losing the future
operations that claim review requires?

This is still detector evidence infrastructure only. It does not score D1,
upgrade Q1B, or assert that any real lab currently meets the surviving route.
"""

from __future__ import annotations

from dataclasses import dataclass


CLAIM_REVIEW_OPERATIONS = frozenset(
    {
        "verify_lineage",
        "reconstruct_event",
        "challenge_packet",
        "certify_packet",
        "audit_authority",
        "use_for_detector_claim_review",
    }
)


@dataclass(frozen=True)
class RowReviewSubstitute:
    substitute_id: str
    full_event_coverage: bool
    event_rows_reviewable: bool
    reconstruction_replay_possible: bool
    external_challenge_rights: bool
    release_before_challenge_deadline: bool
    independent_escrow: bool
    proof_or_summary_only: bool
    purpose: str


@dataclass(frozen=True)
class RowReviewAudit:
    substitute_id: str
    preserved_operations: frozenset[str]
    operations_missing_vs_claim_review: frozenset[str]
    classification: str
    required_next: str
    interpretation: str


@dataclass(frozen=True)
class T171Result:
    audits: tuple[RowReviewAudit, ...]
    scaffold_only_substitutes: tuple[str, ...]
    live_row_review_substitutes: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1b_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def row_review_substitutes() -> tuple[RowReviewSubstitute, ...]:
    return (
        RowReviewSubstitute(
            substitute_id="aggregate_summary_only",
            full_event_coverage=False,
            event_rows_reviewable=False,
            reconstruction_replay_possible=False,
            external_challenge_rights=False,
            release_before_challenge_deadline=False,
            independent_escrow=False,
            proof_or_summary_only=True,
            purpose="Only dashboard or aggregate summary metrics are released.",
        ),
        RowReviewSubstitute(
            substitute_id="signed_proof_certificate_only",
            full_event_coverage=False,
            event_rows_reviewable=False,
            reconstruction_replay_possible=False,
            external_challenge_rights=False,
            release_before_challenge_deadline=True,
            independent_escrow=True,
            proof_or_summary_only=True,
            purpose=(
                "An auditor or cryptographic proof certifies a verdict, but "
                "outside reviewers never see event-level rows."
            ),
        ),
        RowReviewSubstitute(
            substitute_id="private_escrow_with_auditor_statement",
            full_event_coverage=True,
            event_rows_reviewable=False,
            reconstruction_replay_possible=False,
            external_challenge_rights=False,
            release_before_challenge_deadline=True,
            independent_escrow=True,
            proof_or_summary_only=False,
            purpose=(
                "Full rows exist in private escrow and an auditor issues a "
                "statement, but outside review cannot inspect or challenge rows."
            ),
        ),
        RowReviewSubstitute(
            substitute_id="sampled_public_rows",
            full_event_coverage=False,
            event_rows_reviewable=True,
            reconstruction_replay_possible=False,
            external_challenge_rights=True,
            release_before_challenge_deadline=True,
            independent_escrow=True,
            proof_or_summary_only=False,
            purpose=(
                "A public sample of rows is reviewable, but not the full "
                "event-level packet needed to replay the run."
            ),
        ),
        RowReviewSubstitute(
            substitute_id="delayed_full_rows_after_challenge_window",
            full_event_coverage=True,
            event_rows_reviewable=True,
            reconstruction_replay_possible=True,
            external_challenge_rights=False,
            release_before_challenge_deadline=False,
            independent_escrow=True,
            proof_or_summary_only=False,
            purpose=(
                "Full rows are eventually released, but only after the live "
                "challenge or revocation window has closed."
            ),
        ),
        RowReviewSubstitute(
            substitute_id="reviewable_full_rows_with_independent_escrow",
            full_event_coverage=True,
            event_rows_reviewable=True,
            reconstruction_replay_possible=True,
            external_challenge_rights=True,
            release_before_challenge_deadline=True,
            independent_escrow=True,
            proof_or_summary_only=False,
            purpose=(
                "The full bound packet is reviewable at event level during the "
                "challenge window and independently escrowed."
            ),
        ),
    )


def audit_row_review_substitute(substitute: RowReviewSubstitute) -> RowReviewAudit:
    preserved = _preserved_operations(substitute)
    classification = _classification(substitute, preserved)
    missing = CLAIM_REVIEW_OPERATIONS - preserved
    return RowReviewAudit(
        substitute_id=substitute.substitute_id,
        preserved_operations=preserved,
        operations_missing_vs_claim_review=missing,
        classification=classification,
        required_next=_required_next(classification),
        interpretation=_interpretation(substitute, classification, missing),
    )


def run_t171_analysis() -> T171Result:
    audits = tuple(
        audit_row_review_substitute(substitute)
        for substitute in row_review_substitutes()
    )
    scaffold_only = tuple(
        audit.substitute_id
        for audit in audits
        if audit.classification.startswith("scaffold_only_")
    )
    live = tuple(
        audit.substitute_id
        for audit in audits
        if audit.classification == "live_reviewable_row_path"
    )

    if live != ("reviewable_full_rows_with_independent_escrow",):
        raise AssertionError("exactly one reviewable-row substitute should remain live")
    if "private_escrow_with_auditor_statement" not in scaffold_only:
        raise AssertionError("private escrow alone must remain scaffold-only")
    if "signed_proof_certificate_only" not in scaffold_only:
        raise AssertionError("proof-only release must remain scaffold-only")
    if "delayed_full_rows_after_challenge_window" not in scaffold_only:
        raise AssertionError("late row release must remain scaffold-only")

    return T171Result(
        audits=audits,
        scaffold_only_substitutes=scaffold_only,
        live_row_review_substitutes=live,
        strongest_claim=(
            "Within the lone T169 survivor, reviewable full event rows are not "
            "replaceable by summaries, proofs, sampled publication, private "
            "escrow, or delayed release. Claim-review operations survive only "
            "when the full bound row packet is reviewable during the challenge "
            "window and independently escrowed."
        ),
        improved=(
            "T171 turns the phrase 'reviewable rows' into a concrete "
            "capability requirement. Q1B can now say exactly why proof-only, "
            "escrow-only, sampled-row, and delayed-release workflows remain "
            "scaffold rather than live evidence routes."
        ),
        weakened=(
            "This weakens the practical Q1B frontier again. Several plausible "
            "compromise workflows that sound rigorous at first pass still lose "
            "reconstruction or challenge operations and therefore do not clear "
            "claim review."
        ),
        falsification_condition=(
            "T171 fails if any proof-only, summary-only, sampled-row, "
            "escrow-only, or delayed-release workflow preserves the same "
            "claim-review operations as full reviewable rows under the same "
            "pre-data manifest and control-root assumptions."
        ),
        q1b_update=(
            "Q1B remains externally blocked. T171 sharpens T169: the row "
            "commitment must mean full event-level rows reviewable during the "
            "challenge window, not merely summaries, proofs, samples, delayed "
            "release, or private escrow."
        ),
        claim_ledger_update=(
            "Add T171 to Q1B: within the surviving T169 federation class, "
            "proof-only, escrow-only, sampled-row, and delayed-release "
            "substitutes are scaffold-only because they drop reconstruction or "
            "challenge rights. Only full reviewable rows with independent "
            "escrow remain live."
        ),
        open_blocker=(
            "No named detector workflow in the repo currently accepts the full "
            "T171 burden: reviewable full rows before challenge expiry plus "
            "independent escrow under a pre-data claim-review manifest."
        ),
        recommended_next=(
            "Map one named collaboration onto the T169/T171 live route and ask "
            "whether it can expose full event rows during the challenge window. "
            "If not, demote Q1B below the active frontier."
        ),
    )


def t171_result_to_dict(result: T171Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "substitute_id": audit.substitute_id,
                "preserved_operations": sorted(audit.preserved_operations),
                "operations_missing_vs_claim_review": sorted(
                    audit.operations_missing_vs_claim_review
                ),
                "classification": audit.classification,
                "required_next": audit.required_next,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "scaffold_only_substitutes": list(result.scaffold_only_substitutes),
        "live_row_review_substitutes": list(result.live_row_review_substitutes),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1b_update": result.q1b_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _preserved_operations(substitute: RowReviewSubstitute) -> frozenset[str]:
    operations = {"audit_authority"}
    if substitute.event_rows_reviewable:
        operations.add("verify_lineage")
    if substitute.full_event_coverage and substitute.reconstruction_replay_possible:
        operations.add("reconstruct_event")
    if substitute.event_rows_reviewable and substitute.external_challenge_rights:
        operations.add("challenge_packet")
    if (
        substitute.full_event_coverage
        and substitute.event_rows_reviewable
        and substitute.reconstruction_replay_possible
        and substitute.external_challenge_rights
        and substitute.release_before_challenge_deadline
    ):
        operations.add("certify_packet")
        operations.add("use_for_detector_claim_review")
    return frozenset(operations)


def _classification(
    substitute: RowReviewSubstitute,
    preserved: frozenset[str],
) -> str:
    if preserved == CLAIM_REVIEW_OPERATIONS and substitute.independent_escrow:
        return "live_reviewable_row_path"
    if substitute.proof_or_summary_only:
        return "scaffold_only_summary_or_proof_substitute"
    if not substitute.full_event_coverage:
        return "scaffold_only_partial_row_visibility"
    if not substitute.event_rows_reviewable:
        return "scaffold_only_private_escrow_without_review"
    if not substitute.release_before_challenge_deadline:
        return "scaffold_only_late_review_window"
    return "scaffold_only_missing_claim_review_rights"


def _required_next(classification: str) -> str:
    if classification == "scaffold_only_summary_or_proof_substitute":
        return "Release full event-level rows instead of summaries or proof certificates."
    if classification == "scaffold_only_partial_row_visibility":
        return "Expose the full bound event-row packet, not a sample or subset."
    if classification == "scaffold_only_private_escrow_without_review":
        return "Grant outside review rights over the escrowed full rows during the challenge window."
    if classification == "scaffold_only_late_review_window":
        return "Release the full reviewable row packet before challenge or revocation rights expire."
    if classification == "scaffold_only_missing_claim_review_rights":
        return "Restore the missing reconstruction and challenge rights required for claim review."
    return "Find a named collaboration willing to sign and populate this exact route."


def _interpretation(
    substitute: RowReviewSubstitute,
    classification: str,
    missing: frozenset[str],
) -> str:
    if classification == "live_reviewable_row_path":
        return (
            f"{substitute.substitute_id} preserves the full claim-review "
            "operation set and is the only live T171 route."
        )
    return (
        f"{substitute.substitute_id} is scaffold-only because it drops "
        f"{', '.join(sorted(missing)) or 'required claim-review operations'}."
    )


if __name__ == "__main__":
    import json

    print(json.dumps(t171_result_to_dict(run_t171_analysis()), indent=2))
