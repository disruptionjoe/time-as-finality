# T175 Results: Detector Threshold-Root Quorum Screen

## Policy audits

| Policy | Classification | Release bypass | Revocation bypass | Audit bypass | Required next |
| --- | --- | --- | --- | --- | --- |
| `mandatory_archive_and_escrow_release` | `live_threshold_claim_review_policy` | `none` | `none` | `none` | Publish the quorum map pre-data and obtain a named collaboration willing to sign it. |
| `optional_escrow_two_of_three_release` | `null_release_quorum_bypasses_required_guardian` | `archive_custodian`, `escrow_custodian` | `none` | `none` | Rewrite the release quorum so every authorized challenge-window row-release coalition includes both archive custody and escrow. |
| `optional_archive_three_of_four_release` | `null_release_quorum_bypasses_required_guardian` | `archive_custodian` | `none` | `none` | Rewrite the release quorum so every authorized challenge-window row-release coalition includes both archive custody and escrow. |
| `optional_trust_two_of_three_revocation` | `null_revocation_or_audit_quorum_bypasses_required_guardian` | `none` | `trust_auditor` | `none` | Rewrite the revocation and audit quorums so trust audit and escrow cannot be bypassed on critical challenge-window actions. |
| `global_three_of_five_multisig` | `null_release_quorum_bypasses_required_guardian` | `archive_custodian`, `escrow_custodian` | `trust_auditor` | `trust_auditor` | Rewrite the release quorum so every authorized challenge-window row-release coalition includes both archive custody and escrow. |

## Strongest claim

Threshold or multisig root control does not rescue Q1B merely by naming escrow or trust audit as possible signers. For the surviving T171/T173 claim-review route, every authorized challenge-window row-release quorum must include both archive custody and escrow, and every authorized revocation quorum must include both trust audit and escrow.

## What this improved

T175 removes a realistic governance loophole from T161/T173. The repo can now evaluate threshold-key or multisig stories without collapsing them either into naive shared-root failure or into unexamined 'distributed control' optimism.

## What this weakened

This weakens Q1B again. A collaboration does not clear the claim-review route by putting escrow or trust on one branch of a quorum tree. If any authorized release or revocation coalition can bypass those guardians, independent challenge rights are only rhetorical.

## Falsification condition

T175 fails if a threshold-controlled row-release or revocation policy should still count for Q1B even though some authorized coalition omits archive custody, escrow, or trust audit from the critical challenge-window actions they are meant to guard.

## Q1B update

Q1B remains externally blocked. A threshold-key or multisig workflow is admissible only when escrow is a mandatory signer in every authorized challenge-window release and revocation quorum, archive custody is mandatory in every release quorum, and trust audit is mandatory in every revocation or audit quorum.

## Claim ledger update

Add T175 to Q1B: threshold or multisig control is null whenever challenge-window release or revocation can be authorized by a coalition that bypasses archive custody, escrow, or trust audit. Those guardians must be mandatory members of every authorized critical quorum, not optional signers.

## Open blocker

No named detector workflow in the repo currently publishes the critical release and revocation quorum map needed to show that escrow and trust are mandatory rather than optional guardians.

## Recommended next

Update the Q1B handoff to require a pre-data quorum map for challenge-window row release, audit attestation, and revocation. If a realistic collaboration can only offer optional-escrow or optional-trust multisig, demote Q1B below the active frontier.
