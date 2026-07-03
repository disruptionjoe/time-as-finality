# Capability-Boundary Mode Taxonomy — adopted internal reference

## Status

**Adopted internal organizing map (a frame, not a promoted claim).** Ratified as
the program's working classification of capability/finality boundaries (Joe, chat
2026-07-02). This is *not* a CLAIM-LEDGER entry, a theorem, or new physics — it is
the lens the program uses to classify any boundary attempt, and every mode has an
**established literature home** (see novelty note). Provenance:
`open-problems/finite-closed-capability-boundary-scope-theorem.md` (the derivation
and its withdrawn universal-theorem framing), the adversarial review
(`literature/Adversarial Referee Report ...`), and the prior-art verification
(`papers/drafts/prior-art-verification-and-divergent-direction-pass-2026-07-02.md`).

## The map

A **capability boundary** separates two configurations that are identical to a
bounded region `R` (agree on the observable algebra `⟨M_R⟩`) yet differ in an
enactable/recoverable transformation. By the algebraic Declarability Lemma the
separating datum is always present in the global algebra — so a boundary is either
**informationally declared** or **physically forced**, and forcing comes in three
modes. Four modes total, always stated relative to a declared class `A` of
admissible enlargements (A0 own-region ⊂ A1 ancilla/region ⊂ A2 resource/reference-
frame ⊂ A_all):

| Mode | What forces the boundary | Regime | Established home |
| --- | --- | --- | --- |
| **E0 — declared** | recoverable by some admissible enlargement (e.g. admit the co-present registers); a stipulated trace / fiat restriction. Collapses (joint-record completion). | both | access-restriction; Koashi–Imoto read-only/inaccessible split |
| **E1 — asymptotic / limit gap** | recovery cost or non-locality diverges only in a *family/limit*; a limit-invariant, not single-instance | both (family-level) | **Kadanoff extended-singularity theorem**; Butterfield; Landsman |
| **E2 — forcing assumption (hardness)** | no *feasible* admissible procedure recovers it across the family, conditional on a hardness hypothesis | both (family-level) | computational indistinguishability (Goldwasser–Micali; Yao) |
| **E3 — structural symmetry / conservation-law no-go** | an exact, single-instance impossibility on physical states under a symmetry/superselection rule, regardless of resources | (Q) quantum | **Wigner–Araki–Yanase**; resource theory of asymmetry (Marvian–Spekkens) |

- **Model-class split.** In the **classical finite-state** regime (C) the closure
  argument holds, E3 is empty, and E0/E1/E2 are exhaustive — no single-instance
  physical boundary. In the **finite-dimensional quantum** regime (Q) E3 is
  nonempty — exact single-instance physically-forced boundaries exist.
- **Overarching framing.** "Capabilities = which transformations are
  possible/impossible" is **constructor theory** (Deutsch–Marletto). This taxonomy
  is a classification of *why* a task is impossible (the four modes), read through
  the capability-measure program.

## Tri-repo alignment

- **E1** ≈ TaF game / Aumann–Shapley non-atomic limit (T413).
- **E2** ≈ TaF computational finality (T417); the computational-arrow swing is
  recorded as T419 REDESIGN, and T420 hardens the finite-cycle anti-relabel gate,
  so any remaining novelty is a family-level period-hardness redesign/abandon
  question (`open-problems/computational-finality-arrow.md`).
- **E3** ≈ **GU** structural-symmetry no-go (antilinear index-nullity / Krein
  grading) — one-way adjacency, never cited as support. T421 refutes the first
  GU-adjacent admissibility-adapter candidate as a functor and records it as a
  logged disanalogy, not a claim move.
- **E0** is the mode every absorbed TaF attempt used (stipulated gaps through
  co-present registers).

## Novelty note (honest, verified)

The *packaging* (four modes for capability boundaries + the crypto crosswalk + the
tri-repo alignment) was not found verbatim, but **every component and the framing
have established homes** (verified by arXiv fetch, 2026-07-02). So this taxonomy is
a **useful internal map and at most a synthesis/perspective**, not a novel result.
Its value is organizing the program: it explains the kill history, tells any new
boundary attempt which mode it lives in, and localizes where genuine novelty could
still be (E2 computational finality; any future E3 adapter must start from the
T421 disanalogy rather than restating the refused functor).

## How to use it

For any capability/finality boundary attempt, ask: is the separating datum
recoverable by an admissible enlargement (**E0**, declared — stop)? If not, is the
forcing a limit/family effect (**E1**), a hardness assumption (**E2**), or an exact
symmetry no-go (**E3**)? Name the admissible class `A`; state the regime (C)/(Q).
A single-instance non-declared classical boundary is impossible (use E1/E2); a
single-instance quantum one must be E3.

No North Star, canon, public-posture, cross-repo, or ledger movement. GU/TI remain
stress-test input only. Promotion of any mode to a claim pauses for Joe.

## Internal support update (2026-07-03): classical C-fragment executable gate

T432 (`results/T432-classical-finite-boundary-declarability-gate-v0.1-results.md`)
turns the classical finite-state fragment into a recorded-tier executable check.
With `A0` as declared region observables and `A1` as the full co-present finite
classical code, every tested single-instance separator outside `A0` is recovered
by `A1`. The full-support parity guard has no proper coordinate support and is
still `A1`-declared. The exhaustive `n in {1,2,3}` Boolean sweep found zero
single-instance physical candidates.

T433 (`results/T433-classical-declarability-proof-certificate-v0.1-results.md`)
adds the constructive proof certificate for that same classical C-fragment:
for a finite classical product code `Omega`, region projection `pi_R`, and total
datum `d : Omega -> V`, `A1` contains `id_Omega`, so `d = L o id_Omega` by finite
lookup. A0 insufficiency is therefore E0-declared relative to A1, not a
single-instance physical boundary.

This is support for using the taxonomy internally, not a promoted theorem. It
does not touch the quantum E3 route or the T421 logged disanalogy.

## Internal support update (2026-07-03): quantum E3 A-class gate

T435 (`results/T435-quantum-e3-admissible-menu-gate-v0.1-results.md`) supplies a
recorded-tier finite A-class control for the taxonomy's quantum E3 hinge. In a
two-sector parity/superselection toy with `P=diag(1,-1)`, the states `|+><+|` and
`|-><-|` share the same A1 symmetry-respecting sector-population shadow, while
the relative-phase observable `X` separates them and does not commute with `P`.

Verdict: `QUANTUM_E3_A_CLASS_GATE_BUILT_NO_CLAIM_PROMOTION`. Relative to A1
without a reference/asymmetry resource, the phase datum is recorded as
`E3_STRUCTURAL_SYMMETRY_RELATIVE_TO_A1_NO_REFERENCE`. The same pair becomes
`E0_DECLARED_RELATIVE_TO_A2_REFERENCE_RESOURCE` once A2 admits the reference
resource. Visible A1 controls, classical finite-code controls, post-hoc symmetry
selectors, missing-symmetry packets, and hidden-label oracles do not pass.

This is a taxonomy/admission gate only. It is not a WAY theorem, not a quantum
physics claim, not a GU/TaF adapter, not cross-repo evidence, and not a claim
promotion. T421's logged disanalogy remains closed as stated.
