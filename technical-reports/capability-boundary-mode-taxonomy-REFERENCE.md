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
  recorded as T419 REDESIGN, so any remaining novelty is a redesign/abandon
  question (`open-problems/computational-finality-arrow.md`).
- **E3** ≈ **GU** structural-symmetry no-go (antilinear index-nullity / Krein
  grading) — one-way adjacency, never cited as support.
- **E0** is the mode every absorbed TaF attempt used (stipulated gaps through
  co-present registers).

## Novelty note (honest, verified)

The *packaging* (four modes for capability boundaries + the crypto crosswalk + the
tri-repo alignment) was not found verbatim, but **every component and the framing
have established homes** (verified by arXiv fetch, 2026-07-02). So this taxonomy is
a **useful internal map and at most a synthesis/perspective**, not a novel result.
Its value is organizing the program: it explains the kill history, tells any new
boundary attempt which mode it lives in, and localizes where genuine novelty could
still be (E2 computational finality; the E3=GU adapter).

## How to use it

For any capability/finality boundary attempt, ask: is the separating datum
recoverable by an admissible enlargement (**E0**, declared — stop)? If not, is the
forcing a limit/family effect (**E1**), a hardness assumption (**E2**), or an exact
symmetry no-go (**E3**)? Name the admissible class `A`; state the regime (C)/(Q).
A single-instance non-declared classical boundary is impossible (use E1/E2); a
single-instance quantum one must be E3.

No North Star, canon, public-posture, cross-repo, or ledger movement. GU/TI remain
stress-test input only. Promotion of any mode to a claim pauses for Joe.
