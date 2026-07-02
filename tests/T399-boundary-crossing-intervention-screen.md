# T399: Boundary-Crossing Intervention Statistics Screen

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- T397 region-indexed capability no-go
- T398 resource-profile absorber

## Setup

Use a two-qubit finite fixture with a bounded region `R` and a boundary system
`B`.

Main pair:

```text
phi_plus = (|00> + |11>) / sqrt(2)
psi_plus = (|01> + |10>) / sqrt(2)
```

Both states have the same `R` marginal and the same `B` marginal. Therefore
every `R`-supported channel followed by every `R`-supported statistic has the
same output on the pair. The executable artifact also checks a concrete
finite menu of `R` unitaries and `Z/X/Y` readouts.

The boundary-crossing menu admits joint `RB` parity readout and Bell-basis
readout.

## Success Criteria

- Region trace distance is exactly zero.
- Boundary-local trace distance is exactly zero.
- All finite `R` intervention/readout statistics agree.
- The generic all-`R`-supported statistic bound is zero.
- The joint boundary-crossing menu separates the pair perfectly.
- A region-visible control proves the statistics menu has teeth.
- A phase-correlation control proves parity alone is not the whole
  boundary-crossing menu.
- The absorber verdict records ordinary enlarged-state / boundary-access
  absorption, with no claim promotion.

## Failure Criteria

The screen fails if:

- the main pair is distinguishable by any `R`-supported statistic;
- the boundary-crossing menu does not separate the pair;
- the result cannot be explained by ordinary enlarged-state access;
- the artifact upgrades the finite fixture into a physics, public-posture, or
  claim-ledger result.

## Known Physics Constraints

This is a finite correlation/access screen only. It makes no hardware,
spacetime, no-signalling, resource-theory novelty, or physical-agent claim.

## Contribution Needed

For stronger Direction-A work, find a nontrivial task where the
boundary-crossing menu is physically forced by the declared setup rather than
merely admitted as the ordinary enlarged-state completion.
