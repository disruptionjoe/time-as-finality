# T175: Detector Threshold-Root Quorum Screen

## Route

Quantum measurement / classical records, detector evidence infrastructure only.

## Target Claims

- [Q1B: Detector Provenance Admissibility](../claims/Q1B-detector-provenance-admissibility.md)
- [T161: Detector Control-Root Independence](T161-detector-control-root-independence.md)
- [T171: Detector Row-Review Substitution Screen](T171-detector-row-review-substitution-screen.md)
- [T173: Detector Claim-Review Authority Bound](T173-detector-claim-review-authority-bound.md)

## Question

Do threshold keys or multisig-controlled detector roots rescue the surviving
T171/T173 claim-review route, or do they remain null whenever some authorized
coalition can bypass archive custody, escrow, or trust audit on challenge-window
actions?

## Motivation

T161 rejects shared critical roots, but a realistic collaboration can respond
that it uses quorum-controlled release rather than one shared HSM. That is a
real loophole if the repo never checks whether escrow and trust are mandatory
guardians or merely optional signers.

T175 turns that loophole into a finite screen.

## Setup

Audit threshold-root policies for three critical action families:

- challenge-window row release;
- challenge-window revocation; and
- audit attestation.

For the surviving T171/T173 claim-review route, require:

- every authorized row-release quorum includes both `archive_custodian` and
  `escrow_custodian`;
- every authorized revocation quorum includes both `trust_auditor` and
  `escrow_custodian`; and
- every authorized audit quorum includes `trust_auditor`.

Include positive and negative fixtures:

1. `mandatory_archive_and_escrow_release`
2. `optional_escrow_two_of_three_release`
3. `optional_archive_three_of_four_release`
4. `optional_trust_two_of_three_revocation`
5. `global_three_of_five_multisig`

## Success Criteria

- Exactly one fixture survives: the one where archive custody, escrow, and
  trust are mandatory guardians in every authorized critical quorum.
- Optional-escrow and optional-trust quorum stories are null.
- A generic multisig can still fail if its authorized coalitions bypass the
  required guardians.
- The result stays at detector governance/admissibility level, not detector
  physics or Q1 empirical support.

## Failure Criteria

- Threshold or multisig control counts merely because escrow or trust appears
  somewhere in the signer set.
- A release or revocation coalition can bypass the claimed guardian domains and
  still be called Q1B-admissible.
- The screen is described as detector evidence rather than a governance burden.

## Claim Impact

Q1B remains `externally_blocked`.

Add this sharpening:

```text
Threshold-key or multisig control is null for Q1B unless escrow is a mandatory
signer in every authorized challenge-window release and revocation quorum,
archive custody is mandatory in every release quorum, and trust audit is
mandatory in every revocation or audit quorum.
```

## Reproduction

```bash
python -m unittest tests.test_detector_threshold_root_quorum_screen -v
python -m models.run_t175
```
