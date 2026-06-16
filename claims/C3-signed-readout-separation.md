# C3: Signed Readout Separation

## Claim

Record evidence, finality profile, temporal reconstruction, and signed readout
are distinct typed stages. A phase-blind observer-indexed finality profile
does not determine Born-style readout, even when evidence and finality grow
monotonically.

## Class

Core claim.

## Status

Supported in the finite T13 model and preserved by the integrated T14 stress
test.

## What This Does Not Claim

- The model derives quantum mechanics.
- The model derives the Born rule.
- The model describes a physical interference experiment.
- No monotone state summary can determine readout.
- Finality is irrelevant to readout.

## Evidence

[T13](../tests/T13-signed-interfering-readout.md) supplies two finite
witnesses:

- W1: identical finality profiles `(2,2,2,2)` with readouts `4.0` and `0.0`;
- W2: monotonically growing profiles with readout `1.0, 0.0, 1.0`.

The same test suite confirms that linear signed readout factors through two
monotone counters and that phase-class counters recover the Born-style
readout. The separation is therefore specifically from the D1 finality
profile, not from all possible bookkeeping.

[T14](../tests/T14-integrated-observer-context-finality.md) verifies the same
separation inside a larger observer-context pipeline. Two integrated core
graphs have the same finality profile `(3,3,1,3)` but readouts `1.0` and
`9.0`.

## Failure Conditions

- The D1 finality profile is enriched with phase information, making C3 a
  statement about the old profile only.
- The readout map changes so that W1 no longer separates profile from readout.
- A physics-grounded model shows that phase data is always part of the
  relevant finality profile.

## Contribution Needed

Test whether the separation survives generated families of larger graphs,
mixed T12 channels, and T9-style dynamically generated records.
