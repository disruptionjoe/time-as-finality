# Unitarity as a Finality Precondition

Open-problem stub, opened 2026-06-30 from an external-paper calibration pass (Stelle 1977, *Renormalization
of higher derivative quantum gravity*, Phys. Rev. D 16, 953). Exploration-grade. **Projection != finality**
held throughout: this is a structural analogy to interrogate, not a claim that a GR/QFT result *is* a finality
result.

## Problem

Stelle's higher-derivative gravity is renormalizable but propagates a negative-norm (ghost) spin-2 mode, so
it is **non-unitary**: probabilities are not conserved. Unitarity is norm/probability conservation -- the
consistency that lets a system carry a well-defined, conserved ledger over time. TaF defines finality as the
stabilization of records across causally bounded systems. Question: **is a unitarity-like conservation a
precondition for record-finality to be well-defined at all?** In a sector where the underlying dynamics is
non-unitary (negative-norm states, non-conserved "probability"), is there anything for an observer to
finalize -- or does finality presuppose exactly the conserved structure that a ghost sector destroys?

## Working Claim (to attack)

Record-finality presupposes a conserved, positive ledger on the substrate it records. A ghost / non-unitary
sector is structurally a place where finality is *undefined* rather than merely hard: there is no consistent
conserved quantity for a bounded observer's records to stabilize against. If true, "unitarity-like
conservation" becomes a named admissibility condition on substrates that can support finality at all --
parallel to how T10/T29 filter admissible configurations.

## Why It Might Help

- Gives a candidate *necessary condition* on substrates that support finality, sharper than the current
  bracketing of the substrate (see [rendered-interface-assumptions](rendered-interface-assumptions.md)).
- Connects to the repo's wanted **native tradeoff/impossibility** results: Stelle is a clean mainstream
  example of two desiderata (renormalizability, unitarity) that cannot be jointly satisfied with local
  higher-derivative terms -- a calibration target for what a TaF-native "two finality properties you cannot
  jointly have" theorem should look like (cf. T17's no-joint-maximization).

## How It Could Mislead

- A ghost is a Hilbert-space pathology; a record-reconstruction failure is an information-stabilization fact.
  Equating them is the projection error in its purest form. The honest transferable content is only the
  abstract role "conserved positive ledger," not the QFT mechanism.
- "Probability conservation" must not be smuggled in as a TaF primitive; TaF brackets probability. The
  condition, if it survives, must be stated in record/ledger language, then *noted* as analogous to unitarity.
- Do not let this become a back-door for importing QFT axioms into TaF.

## Connection to Existing Claims and Tests

- [T10: Finality Superselection Rule](../tests/T10-finality-superselection-rule.md) -- admissibility filters.
- [T17: Consensus-Finality Crosswalk](../tests/T17-consensus-finality-crosswalk.md) -- no-joint-maximization,
  the latent tradeoff structure.
- [rendered-interface-assumptions](rendered-interface-assumptions.md) -- substrate preconditions.

## Contribution Needed

State a minimal finite model with a "non-conserved ledger" sector and ask whether D1 finality is well-defined
on it. If finality degenerates exactly when the conserved positive ledger is removed, that is the
constructive version of the precondition. Keep the result in record/ledger language; reference unitarity only
as the external analogue.

## Update (2026-06-30): Turok-Bateman Krein-space resolution reframes the precondition

The reading set's capstone (Turok, *A Route to Quantum Gravity (Without Strings)*, Theories of Everything
podcast, 2026; Turok-Bateman quadratic-gravity papers) sharpens this open problem in a useful and partly
adversarial way. Turok-Bateman argue that **norm-positivity is NOT required** for sensible probabilities.
Working in a **Krein space** (pseudo-Hilbert, with positive, null, and negative-norm states), they claim that
*provided the theory has a discrete "ghost-parity" symmetry* (an operator giving +1 on positive-norm and -1 on
negative-norm states), probabilities can be defined via **projection operators and a trace over all states
(including ghosts)** -- a modified Born rule that never normalizes a state -- and the results are positive and
sum to one. Negative-norm states are unobservable labels; what is observable (transition probabilities) stays
positive.

Consequence for this open problem: the candidate precondition is probably **not** "a positive ledger." It is
the weaker, more structural condition: *a discrete symmetry plus a projection/trace construction that makes a
conserved positive probability well-defined.* That is strikingly parallel to TaF's own machinery -- finality
as projection/superselection ([T10](../tests/T10-finality-superselection-rule.md),
[T29](../tests/T29-projection-obstruction-schema.md)). The revised question to attack: **is the precondition
for record-finality the existence of a ghost-parity-like discrete symmetry and a projection structure, rather
than positivity of the underlying ledger?** A finite model with negative-"norm" record weights but a
ghost-parity symmetry should still support well-defined finality; one without the symmetry should not.

Caveat (carry it): Turok's program is explicitly "halfway there" by his own statement -- an external
provocation, not a result. Projection != finality still holds; the Krein/ghost-parity structure is the
analogue to interrogate, not evidence.

## Update (2026-07-07): T507-T509 price the ghost-parity route as review-only

T507, T508, and T509 convert the ghost-parity/finality provocation into
repo-local finite admission gates. T507 records the default reading as
redundancy under positivity-preserving operations and full-Born leakage, with
hidden-record review material only in the full-Krein plus self-normalized
corner. T508 adds the BRST/exactness gate: exact mirrors route to redundancy,
and nontrivial mirror cohomology is only reviewable. T509 adds the observable
compatibility gate: recovery operations must descend through the BRST quotient
and readouts must be exact-invariant; the tested full-Krein recovery and W+
representative leakage are blocked, while direct cohomology readout remains
review-only.

The open problem is therefore narrower than the June formulation. A future
positive packet must supply a real constraint/gauge structure, a
quotient-compatible operation algebra, an exact-invariant observable/readout,
and physics-side support before this can become a finality precondition rather
than a guarded analogy. No claim, public posture, source-action, mass-gap, or
cross-repo truth is earned by the current finite gates.
