# M1: Coupling-Profile Reconstruction

## Claim

An observer's reconstructed temporal relation can depend on its coupling
profile: the channels through which records can affect it. Different coupling
profiles can yield different, noncontradictory reconstructed relations from
the same causal record graph. In a readout-bearing setting, coupling profile
can also change observer-facing readout without changing the stored graph.

## Class

Conjecture.

## Status

Toy supported by T12 and preserved in T14/T15.

## What This Does Not Claim

- Coupling profile explains conscious temporal experience.
- Semantic importance causes physical events.
- Geometry is derived from mattering.
- A channel model has been dynamically derived.

## Evidence

[T12](../tests/T12-coupling-profile-reconstruction.md) implements one causal
record graph with four observer profiles. The observers reconstruct different
relations, but no relation inverts the all-channel relation and observer
pairs agree on shared reconstructible content.

[T14](../tests/T14-integrated-observer-context-finality.md) shows the same
coupling principle inside the integrated pipeline: a core observer and a
gravity-only observer see different finality profiles and readouts from the
same stored graph without producing a causal contradiction.

[T15](../tests/T15-generated-integrated-finality-stress.md) makes this
systematic under its generated observer profiles: coupling divergence appears
in every generated case.

## Failure Conditions

- Coupling filters produce causal inversions.
- Different profiles do not change any reconstructed relation.
- Hardness collapses into simple channel count.
- A dynamical implementation cannot generate stable channel-specific records.

## Contribution Needed

Generate coupling profiles inside a local dynamical model rather than
assigning them by hand.
