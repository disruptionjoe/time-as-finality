# T465: Abramsky-Brandenburger Contextuality Kappa Absorber

## Route

Kappa / CSP-PO1 typed-loss transport line.

## Target Claims

- [T224: Typed-Loss Transport Test](T224-typed-loss-transport-test.md)
- [T21: Bell/CHSH contextuality finality](T21-bell-contextuality-finality.md)
- [Typed-Loss Transport Test](../open-problems/typed-loss-transport-test.md)

## Question

Does Abramsky-Brandenburger style contextuality supply an independent target-side
prediction for kappa, or does it absorb the stronger prediction-language because
its native invariant is already a support/global-section H1 obstruction?

## Motivation

The kappa line has a useful finite catalogue: T224, T229, T234, T239, and T244
show that multiple obstruction domains can be faithfully re-expressed as the
same finite signed-cover rank. The integrator objection is that this does not
yet earn "prediction" or a genre-agnostic theorem, especially when the target
domain is sheaf contextuality itself. In AB contextuality, the native object is
already a local-support/no-global-section obstruction.

T465 makes that objection executable. It treats AB contextuality as the hostile
absorber and checks whether kappa adds an independent target-side witness or
only re-reads the same support table.

## Setup

The model constructs finite AB-style support tables from disjoint CHSH-shaped
blocks:

- contextual blocks with parity pattern `+ + + -`;
- balanced controls with parity pattern `+ + + +`.

For each model it computes:

- native AB contextuality rank by local-section/global-section search, without
  calling `compute_kappa`;
- kappa on the neighbor-visible same/different signed cover derived from the
  same support table;
- a paired-fixture audit where the claimed source kappa equals the native AB
  rank;
- a mismatch control where the claimed source kappa is deliberately wrong.

## Success Criteria

T465 succeeds if it:

- verifies that native AB rank and kappa agree on paired fixtures because both
  read the same support/global-section data;
- verifies that balanced controls have rank 0;
- includes a mismatch control that fails when the claimed source kappa differs
  from the native AB rank;
- labels the result as re-encoding rather than prediction;
- blocks T224 promotion, genre-agnostic theorem language, physics/quantum
  prediction language, public-posture movement, and claim-ledger movement.

## Failure Criteria

T465 fails if it:

- treats AB contextuality as an independent kappa prediction;
- promotes T224, CSP-PO1, Q1/Q1D, T21, T58, or any kappa claim;
- claims Abramsky-Brandenburger novelty;
- claims a new contextuality theorem, physics result, quantum prediction, or
  genre-agnostic theorem;
- edits claim status, roadmap posture, North Star, README, hard policy, or
  cross-repo truth.

## Result

Status: implemented.

Expected verdict:

```text
AB_CONTEXTUALITY_KAPPA_ABSORBER_BUILT_REENCODING_NOT_PREDICTION
```

## Claim Impact

No claim-ledger movement. T465 preserves the finite kappa re-encoding catalogue
but blocks prediction-language for AB contextuality unless a future target
supplies a non-identity native witness.

## Reproduction

```bash
python -m pytest tests/test_ab_contextuality_kappa_absorber.py -q
python -m models.ab_contextuality_kappa_absorber --write-results
```
