# T176 Results: Detector Challenge-Window Freeze Screen

## Profile audits

| Profile | Classification | Mutable targets | Mutable effects | Mutable authorities | Required next |
| --- | --- | --- | --- | --- | --- |
| `fully_frozen_challenge_window_policy` | `live_frozen_challenge_window_policy` | `none` | `none` | `none` | Publish the signed challenge-window freeze policy pre-data. |
| `governance_break_glass_release_override` | `null_mutable_challenge_window_rights` | `release_quorums` | `temporary_override_bypassing_archive_and_escrow` | `analysis_governor`, `control_designer` | Freeze guardian identity and critical release, revocation, and audit policies until challenge-window expiry. |
| `midwindow_escrow_replacement` | `null_mutable_challenge_window_rights` | `guardian_roster` | `replace_escrow_before_row_review` | `analysis_governor`, `trust_auditor` | Freeze guardian identity and critical release, revocation, and audit policies until challenge-window expiry. |
| `trust_suspension_before_revocation` | `null_mutable_challenge_window_rights` | `revocation_quorums` | `temporary_trust_suspension` | `analysis_governor`, `archive_custodian` | Freeze guardian identity and critical release, revocation, and audit policies until challenge-window expiry. |
| `postdispute_guardian_addition` | `null_mutable_challenge_window_rights` | `audit_quorums` | `add_substitute_guardian_postdispute` | `analysis_governor`, `archive_custodian` | Freeze guardian identity and critical release, revocation, and audit policies until challenge-window expiry. |

## Strongest claim

A T175-valid static quorum map is still insufficient for Q1B if challenge-window rights can be changed after data collection. The surviving T171/T173/T175 route stays live only when the guardian roster and critical release, revocation, and audit policies are frozen until challenge-window expiry.

## What this improved

T176 removes a policy-layer loophole from Q1B. The repo can now distinguish a genuinely precommitted claim-review process from one that merely starts with good guardians and then rewrites them under pressure.

## What this weakened

This weakens Q1B again. A detector workflow does not clear the current frontier just by publishing an admissible initial quorum map. Break-glass overrides, mid-window guardian replacement, or temporary suspension of trust or escrow make the challenge rights contingent rather than fixed.

## Falsification condition

T176 fails if a detector workflow should still count for Q1B even though it can change guardian identity or critical release, revocation, or audit rules during the challenge window after data collection begins.

## Q1B update

Q1B remains externally blocked. A T175-valid quorum map counts only if the guardian roster and critical challenge-window action policies are frozen until the review window closes.

## Claim ledger update

Add T176 to Q1B: static guardian quorums are scaffold-only if release, revocation, audit, or guardian-identity rules can be rewritten during the challenge window. The surviving route now requires a pre-data challenge-window freeze.

## Open blocker

No named detector workflow in the repo currently exposes a pre-data freeze policy proving that challenge-window guardians and critical rights cannot be changed after data collection.

## Recommended next

Update the Q1B handoff to require a signed challenge-window freeze policy in addition to the T175 quorum map. If a realistic group needs break-glass override or mid-window guardian rotation, demote Q1B below the active frontier.
