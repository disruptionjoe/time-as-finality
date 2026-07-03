# T422: Representability Span of the Forcing Modes (E1/E2/E3)

> T422 is a recorded-tier exploratory big-swing. `TESTS.md` and
> `CLAIM-LEDGER.md` are UNTOUCHED (the numbering automation normalizes any
> collision later; the T-number lives only in this header and the results note).
> Recorded-tier, NO claim promotion; ledger actions pause for Joe. Cross-domain
> material (Cech cohomology, computational complexity, CRT / quadratic
> residuosity) is the OBJECT OF STUDY, never evidence for physics or a sibling
> repo. One-way rule holds (GU adjacency only).

## Provenance

- Claim source: `explorations/meta-synthesis-reverse-pass-2026-07-02/SYNTHESIS.md`
  (the representability-span headline; ranked next move).
- Taxonomy home: `technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`
  (E0/E1/E2/E3).
- E2 toys: `results/T417-computational-finality-boundary-v0.1-results.md`,
  `results/T419-computational-arrow-of-time-v0.1-results.md`.
- E3-flavored index candidate: `results/T412-separator-refactorization-gate-v0.1-results.md`
  (the Z/2 parity separator).
- Two-index disanalogy (retro-predicted): `results/T421-e3-admissibility-adapter-v0.1-results.md`.

## The predeclared claim (representability span)

Physical forcing modes do NOT form a hierarchy or an interconvertible lattice.
**E1** (asymptotic-limit forcing) and **E3** (structural-symmetry forcing) each
admit a COMMON local-to-global representative — an index / H^1 obstruction class
(a "global section with no local witness"). **E2** (computational-hardness
forcing) admits NO such functorial / homotopy-invariant representative, because
computational hardness is PRESENTATION-DEPENDENT. Therefore the three forcings
are NON-INTERCONVERTIBLE, with E2 the categorical obstruction to unification.

## Construction (the shared engine)

ONE coefficient-generic Cech engine computes H^0/H^1 of the nerve of a
triangulated circle C_n (n arcs U_0..U_{n-1}, cyclic overlaps, no triple
overlaps). H^1(C_n; A) = A via the loop-sum (winding) map. E1 and E3 call the
IDENTICAL function, differing ONLY in the coefficient group A:

- **E1 (asymptotic-limit forcing)**: A = Z. Transition 1-cochain with loop sum
  w = 1. The Z winding index.
- **E3 (structural-symmetry forcing)**: A = Z/2. Sign-local-system transition
  cochain with monodromy = 1. The Z/2 twist index.

This literal same-function / different-coefficient realization retro-predicts
T421's logged Z-vs-Z/2 bifurcation as "same functor, different coefficient
object".

**E2 (computational-hardness forcing)**: object = units mod N=77=7*11 with the
QR / non-QR 2-coloring; datum points x_A=58 (QR), x_B=24 (non-QR, Jacobi +1).
Two presentations related by the CANONICAL CRT ring iso
phi: (Z/77)* -> (Z/7)* x (Z/11)*.

## Predeclared SUCCESS legs

- **S1 COMMON INVARIANT (criterion 1).** The engine computes a nonzero H^1 class
  for BOTH e1_winding (Z, w=1) and e3_twist (Z/2, monodromy=1) via the IDENTICAL
  function differing only in coefficient group; each class is genuinely global
  (every proper subcover trivializes it -> no-local-witness) and refinement-stable
  (n->2n invariant); the e3 class matches T412's measured parity fact (max
  proper-subset trace distance 0.0, full joint separates 1.0).
- **S2 E2 NON-REPRESENTABILITY, EXHIBITED (criterion 2).** phi is verified as a
  genuine ring isomorphism preserving QR-ness; the STEP-1 positive control
  confirms EQUAL Cech invariants (H^0=2, H^1=0) under both presentations (the
  object is not pathological); yet the forcing verdict FLIPS FORCED (N-coords,
  Jacobi +1 for both) -> DECLARED (CRT-coords, per-factor Legendre separates)
  across that iso, so forcing is not an isomorphism-invariant and is represented
  by no Cech class.
- **S3 NON-INTERCONVERTIBILITY MONOTONE (criterion 3).** delta(E1)=delta(E3)=0 <
  delta(E2)=1 from the shared refinement+iso battery; delta is preserved by the
  free operations (cover refinement, object isomorphism), so no free operation
  converts an E1/E3 (delta=0) boundary into an E2 (delta=1) boundary or vice
  versa — E2 is the categorical obstruction. The matched-battery positive control
  returns delta=0 on E1/E3 (T412 48/48), proving the test is not rigged to eject
  E2.
- **S4 FALSIFIER STATED AND DOES NOT TRIGGER (criterion 4).** The candidate
  geometric-hardness measures are each either phi/refinement-invariant-but-
  hardness-blind or hardness-tracking-but-phi-discontinuous; none is
  simultaneously a Cech-representable invariant AND a tracker of the QRA hardness
  gap, so no functorial invariant reproduces the FORCED != DECLARED gap.

## Predeclared KILL / DEMOTION legs

- **K1 FUNCTIONAL INVARIANT FOR E2 CONSTRUCTED -> ABANDON.** Some quantity from
  (x,N) is BOTH CRT/refinement-invariant AND tracks the QRA hardness gap. Span
  collapses.
- **K2 E1/E3 INDEX ENGINEERED OR TRIVIAL -> REDESIGN.** A proper subcover
  witnesses the e1/e3 class, OR the class is not refinement-stable, OR the T412
  cross-check fails.
- **K3 E2 FLIP BUILT BY FIAT -> REDESIGN/ABANDON.** The STEP-1 positive control
  FAILS (the two presentations return different Cech invariants), or phi is not a
  verified ring iso preserving QR-ness.
- **K4 INTERCONVERTIBILITY EXISTS -> ABANDON.** A free operation carries a
  delta=0 boundary to a delta=1 boundary or the reverse.
- **K5 PRIOR-ART PRE-EMPTION -> CITE + DEMOTE TO SYNTHESIS.** A published source
  already states complexity/circuit-size is not a homotopy/functorial invariant
  (Immerman-Vardi order-dependence; Goldwasser-Micali indistinguishability). Cite
  it; only the cross-application to FINALITY / forcing-modes survives as
  synthesis-tier.

## Honest ceiling (binding)

Finite witnesses + a colimit/Fredholm-invariance argument + a stated falsifier —
NOT a universal theorem. Proving "no functorial invariant exists for E2 in
general" is a deep claim and is NOT attempted. E1's true forcing is ASYMPTOTIC;
the finite winding is an explicit PROXY for its no-local-witness STRUCTURE
(refinement-stability is the finite E1-flavor signature), not the divergence. The
separation lives in the cost-blind category (isomorphisms / refinements); a
reviewer insisting on the poly-time-reduction category declines the claim's
category rather than refuting it, and there the E1/E3 indices are not preserved
either. K5 prior art conceded up front; novelty confined to the finality /
forcing-mode cross-application (synthesis-tier).
