# T3: Spacelike Events And No Global Commit Order

## Target Claims

- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)
- [G2: Not A Replacement Theory](../guardrails/G2-not-a-replacement-theory.md)

## Setup

Model two spacelike-separated events `A` and `B`, two observers in relative motion, and a later common causal future where records can be compared.

## Success Criteria

- The model preserves the relativity of simultaneity.
- No hidden universal present is introduced.
- Proper time remains the invariant clock measure along each observer's worldline.
- Finality language tracks record access, not replacement geometry.

## Failure Criteria

- The model imposes a global event order not present in relativity.
- It treats Lorentz transformations as mere ledger translations.
- It confuses causal order with metric interval.

## Contribution Needed

Provide a relativity sanity check with diagrams or equations showing exactly where finality language is safe and where it stops.

## Status Addendum: T3 Sanity Packet v0.1

`models/t3_spacelike_commit_order_sanity.py` supplies a finite 1+1 Minkowski
sanity check. Events `A` and `B` are spacelike-separated, so their order changes
between inertial frames; event `C` lies in the common causal future of both, so
record reconciliation at `C` is causal.

Safe reading: finality language may track when records become comparable at a
common future event, but it must not add a hidden universal present, global
commit order, or replacement geometry for spacelike-separated events.

Result packet: `results/T3-spacelike-commit-order-sanity-v0.1-results.md`.
