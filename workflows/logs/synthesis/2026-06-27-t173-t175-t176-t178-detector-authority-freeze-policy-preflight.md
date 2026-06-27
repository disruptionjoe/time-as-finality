---
document_type: synthesis_preflight
batch_item: sixth_15_task_3
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T173-T175-T176-T178 Detector Authority Freeze Policy Preflight

## Status

Preflight only. This note consolidates four detector-governance gates for a
future Q1B manifest, without changing Q1B's externally blocked status.

## Sources read

- `tests/T173-detector-claim-review-authority-bound.md`
- `tests/T175-detector-threshold-root-quorum-screen.md`
- `tests/T176-detector-challenge-window-freeze-screen.md`
- `tests/T178-detector-preserved-rights-successor-policy-screen.md`
- `workflows/logs/synthesis/2026-06-27-q1b-federated-detector-manifest-preflight.md`

## Plain-English finding

Q1B cannot be rescued by saying "we have escrow" or "we use multisig." The
repo needs escrow, archive custody, trust audit, and challenge-window rights to
remain operationally unavoidable after data exists.

## Technical conclusion

The current combined burden is:

- `T173`: the surviving claim-review route needs five effective authority
  domains, because independent escrow cannot be merged into the older four-domain
  detector packet.
- `T175`: threshold keys or multisig count only if archive, escrow, and trust
  are mandatory guardians on the relevant critical actions.
- `T176`: a good initial quorum map is scaffold-only if guardian identity or
  critical challenge-window rights can change after collection starts.
- `T178`: exception paths are admissible only as predeclared preserved-rights
  successor policies that keep guardians, access, identity, and immutable logs.

This is a governance/admissibility burden, not detector physics.

## Minimum next task

Create one Q1B manifest schema block named `challenge_window_authority_policy`
with required fields for five-domain partition, mandatory guardians, freeze
scope, successor triggers, preserved rights, and immutable transition logs.

## Stop condition

Stop the Q1B route if any authorized release, revocation, audit, exception, or
successor path can bypass archive custody, escrow custody, trust audit, frozen
guardian identity, or already-granted full row-review access.

