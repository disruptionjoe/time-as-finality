# T171 Results: Detector Row-Review Substitution Screen

## Substitute audits

| Substitute | Classification | Missing claim-review operations | Required next |
| --- | --- | --- | --- |
| `aggregate_summary_only` | `scaffold_only_summary_or_proof_substitute` | `certify_packet`, `challenge_packet`, `reconstruct_event`, `use_for_detector_claim_review`, `verify_lineage` | Release full event-level rows instead of summaries or proof certificates. |
| `signed_proof_certificate_only` | `scaffold_only_summary_or_proof_substitute` | `certify_packet`, `challenge_packet`, `reconstruct_event`, `use_for_detector_claim_review`, `verify_lineage` | Release full event-level rows instead of summaries or proof certificates. |
| `private_escrow_with_auditor_statement` | `scaffold_only_private_escrow_without_review` | `certify_packet`, `challenge_packet`, `reconstruct_event`, `use_for_detector_claim_review`, `verify_lineage` | Grant outside review rights over the escrowed full rows during the challenge window. |
| `sampled_public_rows` | `scaffold_only_partial_row_visibility` | `certify_packet`, `reconstruct_event`, `use_for_detector_claim_review` | Expose the full bound event-row packet, not a sample or subset. |
| `delayed_full_rows_after_challenge_window` | `scaffold_only_late_review_window` | `certify_packet`, `challenge_packet`, `use_for_detector_claim_review` | Release the full reviewable row packet before challenge or revocation rights expire. |
| `reviewable_full_rows_with_independent_escrow` | `live_reviewable_row_path` | `none` | Find a named collaboration willing to sign and populate this exact route. |

## Strongest claim

Within the lone T169 survivor, reviewable full event rows are not replaceable by summaries, proofs, sampled publication, private escrow, or delayed release. Claim-review operations survive only when the full bound row packet is reviewable during the challenge window and independently escrowed.

## What this improved

T171 turns the phrase 'reviewable rows' into a concrete capability requirement. Q1B can now say exactly why proof-only, escrow-only, sampled-row, and delayed-release workflows remain scaffold rather than live evidence routes.

## What this weakened

This weakens the practical Q1B frontier again. Several plausible compromise workflows that sound rigorous at first pass still lose reconstruction or challenge operations and therefore do not clear claim review.

## Falsification condition

T171 fails if any proof-only, summary-only, sampled-row, escrow-only, or delayed-release workflow preserves the same claim-review operations as full reviewable rows under the same pre-data manifest and control-root assumptions.

## Q1B update

Q1B remains externally blocked. T171 sharpens T169: the row commitment must mean full event-level rows reviewable during the challenge window, not merely summaries, proofs, samples, delayed release, or private escrow.

## Claim ledger update

Add T171 to Q1B: within the surviving T169 federation class, proof-only, escrow-only, sampled-row, and delayed-release substitutes are scaffold-only because they drop reconstruction or challenge rights. Only full reviewable rows with independent escrow remain live.

## Open blocker

No named detector workflow in the repo currently accepts the full T171 burden: reviewable full rows before challenge expiry plus independent escrow under a pre-data claim-review manifest.

## Recommended next

Map one named collaboration onto the T169/T171 live route and ask whether it can expose full event rows during the challenge window. If not, demote Q1B below the active frontier.
