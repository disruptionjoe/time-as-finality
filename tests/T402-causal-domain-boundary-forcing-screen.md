# T402: Causal-Domain Boundary Forcing Screen

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- T399 boundary-crossing intervention statistics screen
- T400 boundary-forced task gate
- T401 finality-boundary reconciliation screen
- T151/T153 causal-access and Lorentzian absorber screens

## Setup

Use a finite 1+1 causal-domain record substrate:

```text
R input:                  t=0, x=-1
B input:                  t=0, x= 1
common-future verdict:    t=1, x= 0
c = 1
```

The bounded region `R` holds only the left input event. The boundary side `B`
holds the right input event. The verdict event lies in the common future and in
the future domain of dependence of the joint interval `[-1, 1]`, but not of the
`R`-only or `B`-only initial data.

Compare the same source distributions used by the T401 finality screen:

```text
aligned      = 00 with probability 1/2, 11 with probability 1/2
anti_aligned = 01 with probability 1/2, 10 with probability 1/2
```

Both distributions have the same `R` marginal, the same `B` marginal, and the
same statistics after each declared `R`-supported map/readout:

```text
identity, flip, erase_to_0, erase_to_1
```

The predeclared task is:

```text
issue a common-future final verdict from the same/different relation of the
incoming R and B records
```

## Success Criteria

- `R` and `B` are spacelike.
- The verdict event is in their common future.
- The joint `R:B` initial-data interval contains the verdict event.
- The `R`-only and `B`-only domains do not contain the verdict event.
- Region-local and boundary-local statistics are identical.
- The finite `R` intervention/readout menu has max difference `0.0`.
- Region-only and boundary-local binary success remain `0.5`.
- The common-future verdict relation separates aligned from anti-aligned with
  binary success `1.0`.
- Optional joint labels, hidden datum in `R`, closure-key shortcuts, and
  class-marker shortcuts all fail.
- The result says no claim-ledger movement is earned.

## Failure Criteria

The artifact fails if:

- any `R`-supported statistic separates the pair;
- boundary-local statistics separate the pair;
- the verdict event is already determined by the `R`-only domain;
- boundary access is merely optional rather than forced by the common-future
  task setup;
- a hidden datum, closure key, or class marker does the separating work;
- causal-domain completion is ignored as the absorber;
- the result is framed as new physics, public posture change, or claim update.

## Known Physics Constraints

This is a finite causal-domain screen only. It uses a minimal 1+1
Minkowski-style causal relation as an absorber, not as a new physics claim.

The conservative result is that the physical-substrate task shape clears the
T400/T401 gate, but the separator is absorbed by ordinary causal-domain
completion and joint input access. It is not a claim-ledger update.

## Contribution Needed

A future upgrade needs a same-causal-domain-data capability split that is not
expressible as causal reachability, domain of dependence, or ordinary joint
input completion.
