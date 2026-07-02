# Computational Finality / A Computational Arrow of Time (frozen problem statement)

## Status

**Open problem — frozen problem statement (D2). No build yet; the swing pauses for
Joe's go.** This scopes the one direction the divergent persona pass (2026-07-02,
`papers/drafts/prior-art-verification-and-divergent-direction-pass-2026-07-02.md`)
flagged as the least-covered and most-plausibly-novel angle in the E2 mode of the
adopted taxonomy (`technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`).
Spec-before-build discipline: the novelty bar and kill criteria below are fixed
*before* any fixture is written. No claim promotion; ledger untouched.

## The question

Can a **finality / capability boundary** be forced by **computational hardness under
a standard cryptographic assumption** — such that the record is *information-
theoretically fully present and reversible in principle*, yet *computationally
locked* for any feasible agent — and is this a **distinct** kind of arrow from the
thermodynamic and complexity-growth arrows?

Slogan: **a cryptographic arrow of time** — finality that is real *relative to a
one-way-hardness assumption*, not to entropy growth or to complexity growth.

## Lineage (E2 mode)

- **T417** (`results/T417-computational-finality-boundary-v0.1-results.md`) already
  built the static object: a Goldwasser–Micali datum co-present in `(x,N)` but
  feasibly-hard to recover without the trapdoor; boundary physical conditional on
  QRA/factoring, family-level. D2 asks whether this yields a **temporal** statement
  — an *arrow* (past/future asymmetry of feasible recoverability), not just a
  static boundary.

## Prior art already checked (2026-07-02 pre-check) — the novelty bar

The broad "complexity and the arrow of time" space is **crowded**; D2 must
differentiate from all of these or it is not novel:

- **Brown–Susskind, "Second Law of Quantum Complexity" (arXiv:1701.01107).**
  Complexity grows — but *symmetrically* (toward past and future). D2 is **not** a
  complexity-growth statement; it is a *one-way feasible-recoverability asymmetry*.
- **Lesovik et al., reversal on IBM Q (arXiv:1712.10057).** Spontaneous reversal is
  exponentially *improbable* — a statistical/thermodynamic framing. D2 is **not**
  about probability of spontaneous reversal; it is about *conditional computational
  hardness under a named assumption*, with the information fully present.
- **Crutchfield–Ellison, "Time's Barbed Arrow" / crypticity.** Information hidden in
  a process's causal states (computational mechanics / ε-machines). D2 is **not**
  crypticity; it is *cryptographic* hardness (one-way functions), a different notion
  of "hidden."
- **Wolpert, stochastic thermodynamics of computation; Bennett.** Thermodynamic
  *cost* of computation — that is the **E1/thermodynamic** mode, not E2.

**Novelty survives only if** the claim is specifically: *an
information-theoretically-recoverable-but-computationally-locked finality/arrow,
conditional on a cryptographic hardness assumption, provably distinct from the
thermodynamic (E1) and complexity-growth (Brown–Susskind) arrows.* Anything broader
is already taken.

## Success criteria (a swing succeeds only if)

1. A finite/finite-family fixture where a record's forward direction is feasibly
   computable but its recovery ≡ inverting a one-way function / a standard hardness
   assumption (built on T417), **exhibiting a temporal asymmetry** (an arrow), not
   just a static boundary.
2. An explicit separation showing the boundary is **information-theoretically
   trivial** (the datum is present; reversal exists in principle) yet
   **computationally forced** — i.e. it is E2, not E1 and not E0.
3. A stated argument that this arrow is **distinct** from Brown–Susskind complexity
   growth (asymmetric feasible-recovery, not symmetric complexity) and from the
   thermodynamic arrow (no entropy/erasure needed).

## Kill / demotion criteria

- The construction reduces to a thermodynamic cost (E1) or to Landauer erasure →
  not a new arrow, just E1.
- The asymmetry is actually symmetric complexity growth (Brown–Susskind) → absorbed.
- The "hardness" is stipulated rather than a reduction to a standard assumption →
  E0 (declared) in disguise.
- The temporal content is only the static T417 boundary relabeled "past/future"
  with no dynamical asymmetry → no arrow, demote to T417.
- Prior art turns up a clean statement of exactly this (a cryptographic arrow of
  time with these properties) → cite and demote to synthesis.

## What a swing would build (NOT now)

A finite dynamical fixture: a forward-easy / backward-hard record evolution keyed on
a one-way construction, with the three success separations above computed, run
against the taxonomy's E0/E1 absorbers. Provisional next T-number after the current
highest. **Do not build until Joe greenlights D2.**

No North Star, canon, public-posture, cross-repo, or ledger movement. GU/TI remain
stress-test input only.
