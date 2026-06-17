# Open Problem: Finality Under Non-Static Boundaries

## Question

How should [D1](../claims/D1-physical-finality-definition.md) characterize records formed near a finality-domain boundary that moves? Most finality-domain reasoning assumes a boundary that is fixed for the duration of record formation. A periodically moving boundary breaks that assumption.

## Why This Matters

The heliosphere is a concrete case. It expands and contracts with the roughly 11-year solar cycle, so the heliopause is not static. Records formed near the moving boundary may carry signatures of the boundary's transit: an event that was inside the heliosphere during one phase of the cycle may be near or outside it during another. If D1 finality is substrate-relative, and the substrate boundary sweeps back and forth across a region, then the finality status of records in that region is itself time-varying in a way the static-boundary picture does not capture.

See [Heliosphere As A Finality Domain](../explorations/heliosphere-as-finality-domain.md) for the originating context.

## Required Work

- Define what it means for a finality-domain boundary to move, in D1 terms, without circularly invoking time-ordering (the framework derives experienced time from finality).
- Define the record class whose stabilization time is comparable to the boundary's period of motion. Records with stabilization times much shorter or much longer than the cycle are the easy limits; the hard case is the comparable-timescale regime.
- State what observable signature a record formed in the sweep region would carry.
- State a failure condition: what would show that a moving boundary adds nothing beyond the static-boundary treatment.

## Local Consistency Constraint

A moving-boundary model must remain compatible with the no-global-commit-order constraint in [R1](../claims/R1-relativity-no-global-commit-order.md). The boundary's motion is a local substrate change, not a global clock.

## Relation To Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [B1: Black Holes As Finality-Domain Boundaries](../claims/B1-black-holes-finality-boundaries.md)
- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)
