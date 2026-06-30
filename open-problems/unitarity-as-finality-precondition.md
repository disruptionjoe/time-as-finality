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
