# T401: Finality-Boundary Reconciliation Screen

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- T407 region-indexed capability no-go
- T398 resource-profile absorber
- T399 boundary-crossing intervention statistics screen
- T400 boundary-forced task gate

## Setup

Use a finite two-holder record system:

```text
R = bounded-region holder of one event record bit
B = boundary holder of one event record bit
```

Compare two source distributions:

```text
aligned      = 00 with probability 1/2, 11 with probability 1/2
anti_aligned = 01 with probability 1/2, 10 with probability 1/2
```

Both distributions have the same `R` marginal, the same `B` marginal, and the
same statistics after each declared `R`-supported map/readout:

```text
identity, flip, erase_to_0, erase_to_1
```

The predeclared finality-native task is:

```text
issue a merged/final record verdict only after checking whether the bounded-
region record and boundary-holder record attest the same event value
```

The separating menu is the `R:B` reconciliation relation:

```text
same versus different
```

## Success Criteria

- Region-local and boundary-local statistics are identical.
- The finite `R` intervention/readout menu has max difference `0.0`.
- Region-only and boundary-local binary success remain `0.5`.
- The joint reconciliation relation separates aligned from anti-aligned with
  binary success `1.0`.
- The finality record-reconciliation task passes the forced-task gate.
- Optional joint state labels, hidden datum in `R`, closure-key shortcuts, and
  class-marker shortcuts all fail.
- The result says no claim-ledger movement is earned.

## Failure Criteria

The artifact fails if:

- any `R`-supported statistic separates the pair;
- boundary-local statistics separate the pair;
- the reconciliation task does not require both record holders;
- a hidden datum, closure key, or class marker does the separating work;
- ordinary joint-record access is ignored as the absorber;
- the result is framed as new physics, public posture change, or claim update.

## Known Physics Constraints

This is a finite finality/reconciliation screen only. It does not supply a
physics-native boundary task and does not promote the region-indexed capability
discriminator into the claim ledger.

## Contribution Needed

Use the forced-task audit on a stronger physical setup where boundary crossing
is forced by the substrate, not merely by ordinary joint-record reconciliation.
