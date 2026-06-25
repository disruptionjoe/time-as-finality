# Typed-Loss Transport Test (kappa cross-domain prediction)

## Problem

Is the typed-loss obstruction that recurs across the repo's mature absorbers
(signed-graph frustration, sheaf H1, CAP/commit obstruction, Arrow/SMD
aggregation impossibility, the Pythagorean comma, POMDP value gaps,
rate-distortion floors, holonomy) a single **transportable** invariant, or is it a
template the analysis projects onto unrelated mathematics that merely rhymes?

This is the breakout target from the 2026-06-24 heterodox-vs-orthodox 62-persona
pass
([`explorations/heterodox-orthodox-62-persona-breakout-pass-2026-06-24.md`](../explorations/heterodox-orthodox-62-persona-breakout-pass-2026-06-24.md)).
It is designed to escape the repo's local minimum, in which every candidate
*object* is absorbed by some mature neighbor (most recently T220 collapsing
LossKernel/TF1 through the neighbor-visible map `psi . nu`), leaving the program
more rigorous and less independently motivated each cycle. The transport test
changes the unit of analysis from the object (always absorbed) to the **map
between absorbers** (which no single absorber can own).

## Why the local minimum is escapable only this way

The absorber discipline is per-domain by construction: each gate certifies that
host H owns a residue. It can neither generate nor refute a claim that ranges
*over* hosts, so it is structurally blind to a transport law between hosts.
"Everything gets absorbed" therefore stops being a defeat and becomes the
experimental apparatus: each absorption event is a measurement of the transport
map, and 200+ absorption events have never once been tested for cross-domain
consistency.

## Definition: the typed-loss comma kappa

For a system with neighbor-visible data map `nu` (the map every mature absorber
reads, and through which T220 showed the canonical witness obligation factors),
define

```text
kappa(nu) = rank / dimension (or an information-theoretic measure) of the set of
            global sections that nu cannot distinguish.
```

This is exactly the quantity T220's obligation factorization made canonical: the
unrecoverable-from-local-views content. kappa must be defined once, domain-neutrally,
not re-specified per domain.

## Protocol (the test)

1. **Compute kappa_A** on a fully specified instance in domain A.
2. **Construct a structure-preserving map** A -> B to an a-priori-unrelated domain
   B (no shared derivation; the map preserves the neighbor-visible structure, not
   the domain semantics).
3. **Predict kappa_B (or B's native obstruction value) before computing it
   natively** in B.
4. **Compute B's obstruction natively and compare.**

## Concrete first instance (uses existing repo objects)

- **Domain A:** CSP-PO1 signed-graph frustration (fully formalized; T39).
- **Domain B (pick one):** the T21 Bell/CHSH contextuality H1 obstruction, or the
  T28 CAP/consensus obstruction.
- Define kappa on A, transport to B, predict B's obstruction value, then measure.

This is a single decision-grade test (T224-class), not a fan-out.

## Verdict conditions

- **Pass:** kappa transported from A predicts B's natively-measured obstruction
  across two or more unrelated absorbers, with no shared derivation. Outcome: a
  real cross-domain classification theorem living in no single absorber. This is
  the independent motivation the 2026-06-24 paper audit found NOT EARNED.
- **Fail:** the prediction misses, or kappa must be re-tuned per domain. Outcome:
  the cross-domain recurrence was a projected template; the deflation verdict
  stands; the North Star's central bet is cleanly killed rather than starved.

Either outcome is non-vacuous, which is the point: it converts "rigor equals
deflation" into a falsifiable experiment.

## Dual orthodox face (predictive absorption functor)

The same machinery, read from the orthodox side, is a functor

```text
(residue + active AC-conditions) -> (absorbing neighbor + canonical collapse-witness)
```

with a falsifiable conjecture: every residue with admissibility signature Sigma
collapses through the `psi . nu`-style factoring into host H. A correct novel
host-prediction on an untested residue is a theorem about the absorbers; a residue
with signature Sigma that refuses its predicted host is the first genuine
separation gate. The transport invariant kappa is the *value* this functor carries;
the host assignment is its *domain*.

## What would falsify or demote this open problem

- kappa cannot be defined domain-neutrally (it always needs a per-domain choice) ->
  demote: there is no transport law, only per-domain bookkeeping.
- Every constructed A -> B map either fails to preserve neighbor-visible structure
  or trivially shares a derivation -> demote: the recurrence is notational.
- The first instance's prediction fails and no structure-preserving map repairs it
  -> the breakout bet is killed; record as a clean no-go.

## Relation to existing claims

- Reuses T220's obligation-factoring (`psi . nu`) as the definition of kappa.
- Reuses CSP-PO1 (T39), T21 (Bell/CHSH H1), and T28 (CAP/consensus) as ready
  domains.
- Does not promote any physics, geometry, curvature, or new-object language. The
  only claim allowed on success is a cross-domain classification/transport theorem,
  and only after the protocol's prediction step passes on at least two unrelated
  absorbers.
