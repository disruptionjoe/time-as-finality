# T178 Results: Detector Preserved-Rights Successor Policy Screen

## Profile audits

| Profile | Classification | Predeclared | Guardians preserved | Review access preserved | Guardian identity preserved | Transition log immutable | Required next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fully_frozen_no_successor_policy` | `live_frozen_without_successor` | `True` | `True` | `True` | `True` | `True` | Publish the fully frozen challenge-window policy pre-data. |
| `predeclared_preserved_rights_legal_hold_successor` | `live_predeclared_preserved_rights_successor` | `True` | `True` | `True` | `True` | `True` | Publish the successor trigger conditions and immutable transition log format pre-data. |
| `undeclared_break_glass_successor` | `null_unpredeclared_or_unlogged_successor` | `False` | `False` | `False` | `False` | `False` | Freeze the successor trigger and transition log pre-data or remove the successor path entirely. |
| `predeclared_release_pause_pending_governance_clearance` | `null_successor_reduces_review_rights` | `True` | `True` | `False` | `True` | `True` | Rewrite the successor policy so full row-review access remains live throughout the challenge window. |
| `predeclared_escrow_rotation_successor` | `null_successor_changes_required_guardians` | `True` | `False` | `True` | `False` | `True` | Rewrite the successor policy so archive, escrow, and trust remain mandatory guardians and named identities do not change. |
| `predeclared_revocation_override_successor` | `null_successor_changes_required_guardians` | `True` | `False` | `True` | `True` | `True` | Rewrite the successor policy so archive, escrow, and trust remain mandatory guardians and named identities do not change. |

## Strongest claim

T176's freeze burden admits at most one narrow exception. A challenge-window successor policy can still count for Q1B only if it is frozen pre-data, trigger-bounded, preserves the same mandatory archive, escrow, and trust guardians on every critical action, preserves already-granted full row-review access, preserves guardian identity, and emits immutable transition logs.

## What this improved

T178 makes the T176 boundary more realistic without reopening the governance loophole. The repo can now distinguish a preserved-rights successor policy from generic post-data override stories.

## What this weakened

This weakens Q1B's last practical exceptions. Predeclared legal, safety, or emergency procedures do not help unless they preserve the same review rights and guardian structure throughout the challenge window.

## Falsification condition

T178 fails if a successor policy should still count for Q1B even though it is undeclared, reduces review access, changes guardian identity, bypasses archive/escrow/trust on a critical action, or lacks immutable transition logs.

## Q1B update

Q1B remains externally blocked. The T176 freeze burden can be relaxed only by a T178-valid preserved-rights successor policy; generic emergency, legal, or safety override stories remain null.

## Claim ledger update

Add T178 to Q1B: a predeclared challenge-window successor policy counts only when it preserves the same mandatory guardians, full row-review access, guardian identity, and immutable transition logging throughout the review window.

## Open blocker

No named detector workflow in the repo currently exposes either a fully frozen challenge-window policy or a predeclared preserved-rights successor policy package that can be audited pre-data.

## Recommended next

Update the Q1B handoff so emergency, legal, or safety exceptions must either be absent or arrive as a predeclared T178-valid preserved-rights successor policy with trigger conditions and transition logs fixed before data collection.
