# T16: Spacetime Aggregation Toy Model

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [H5: Spacetime Aggregation Conjecture](../HYPOTHESES.md)
- [R1: Relativity No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)

## Origin

Direction 2 from the 42-persona convergence map: spacetime from finality
aggregation.

## Setup

Represent each observer-local finality domain as a finite partial order over
local events. Domains overlap when they share event labels.

Aggregation succeeds only if:

1. each local domain is internally acyclic;
2. domains agree on the finality order induced on every shared overlap;
3. the union of all local orders remains acyclic.

When those checks pass, the toy model returns a global partial order. This is
the minimal "spacetime-like" object in the test: a shared compatibility
structure, not a metric spacetime.

## Success Criteria

- Compatible overlapping domains glue into a global partial order.
- Disagreement on an overlap is reported as an obstruction.
- Pairwise-small overlaps can still produce a global cycle obstruction.
- Successful aggregation does not force a total order.
- The implementation preserves the guardrail that spacetime has not been
  derived.

## Failure Criteria

- Local disagreement is silently averaged away.
- A cyclic global order is accepted.
- The output requires a universal total order.
- The result is presented as a derivation of GR, metric geometry, or physical
  spacetime.

## Known Physics Constraints

This is a finite order-theoretic toy model. It does not derive Lorentzian
geometry, Einstein equations, quantum field theory, or diffeomorphism
invariance.

## Contribution Needed

Extend the toy from event-label overlap to typed restriction maps between
local causal diamonds. Then test whether nontrivial sheaf/cohomology
obstructions correspond to physically meaningful finality conflicts.
