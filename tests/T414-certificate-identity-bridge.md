# T414 — Certificate-Identity Bridge (spec, frozen)

**Status:** exploratory bridge probe (bridge obligation #1 of the
governance-Shapley-finality homology note, 2026-07-02). Registered as T414 after
normalizing the committed provisional numbering. No claim promotion; no CLAIM-LEDGER
entry; ledger actions pause for Joe. Cross-domain material is the **object of
study**, never evidence. Spec frozen before the model file exists.

## Purpose

Discharge (or fail) bridge obligation #1: *show the T413 game's
efficiency-forced `final-relative-to-R` separator is the **same typed certificate
object** as T411's `final-relative-to-R+`, in a shared typed signature — not
merely the same verdict word.* Built to be **falsifiable and non-circular**: the
signature must (a) be instantiated by both domains from their own machinery, (b)
derive the verdict from shared fields by an identical rule, (c) **reject** cases
that should not bridge, and (d) report T411's invariance-witness **honestly**,
including where it is only partial.

Certificate primitive chosen by the 10-lens game-theory steelman (chat,
2026-07-02): **not** the Shapley value (that is the object, and defining the
certificate as "satisfies the Shapley axioms" is circular). The certificate is a
**stability / no-deviation** predicate (core-relative-to-R ≈ strategyproof ≈
ESS-uninvadable) plus an **invariance axiom** (symmetry / Arrow-IIA) as the
relabel-proofing.

## The shared signature (fixed)

```
Certificate = ⟨ region R,
                menu M,
                verdict ∈ {final-relative-to-R, revisable-at-R},
                stability_witness   : no M-supported operation in R overturns the verdict,
                invariance_witness  : verdict unchanged under admissible relabelings
                                      of structure OUTSIDE R (irrelevant-alternative class,
                                      and — separately — the FULL admissible class),
                datum_locus ∈ {proper-subset, whole} ⟩
```

Shared **verdict rule** (identical for both domains):

```
final-relative-to-R  ⇔  stability_witness ∧ (region cannot reconstruct the datum)
relabel-proof        ⇔  invariance_witness.complete   (full admissible class, not just one sub-class)
```

## Instantiations under test

- **Game (T413, fully computed).** R = `{0,1,2}`; M = dividend reallocations on
  subsets of R. Stability = no in-R dividend change moves the A-vs-C separation
  (which lives in `d(N)`). Invariance = irrelevant-relabel class (boundary
  permutations; dividends on coalitions disjoint from the focus) **and** full
  admissible class (any localizing re-weighting breaks the **symmetry** axiom —
  T413 Leg 5). datum_locus = whole (Pair 2) / proper-subset (Pair 1).
- **T411/T412 adapter (recorded fields, cited - NOT re-derived).** R = declared `R+`;
  M = all CPTP channels on R + unlimited work. Stability = all-channel
  phi-independence certificate (recorded). Invariance = Lieb-Robinson/product class
  **survives** (recorded); arbitrary entangling refactorization localizes the
  datum unless excluded by a factorization/coupling admissibility rule (T412).
  datum_locus = whole (recorded: beta=0 datum in no proper subset).

## Predeclared legs (verdicts fixed before running)

1. **Signature instantiation.** Both domains instantiate the exact field set with
   matching types; verdict derived by the shared rule = `final-relative-to-R(+)`
   in both.
2. **Stability match.** Both `stability_witness.no_in_R_overturn = True`
   (different evidence, same role).
3. **Datum-locus match (Pair 2).** Game Pair 2 and T411 both `datum_locus = whole`.
4. **Invariance divergence (the honest asymmetry).** Game invariance
   `complete = True` (irrelevant class invariant **and** full class axiom-forced);
   T411/T412 invariance `complete = False` (LR/product class True, arbitrary
   entangling refactorization fails unless excluded). This is the one divergent
   field.
5. **Bridge verdict = PARTIAL HOMOLOGY / SHARED SIGNATURE.** 4 of 5 fields
   structurally identical; the divergent field is exactly `invariance_witness.
   complete`, where the game is **strictly stronger** (proven) than T411/T412
   (factorization-guarded). Current payload: the game supplies the **proof
   template** (an IIA/symmetry-type invariance axiom) for the admissibility rule
   T412 showed the quantum separator needs.
6. **Falsifiability teeth.** Game **Pair 1** (boundary dividend) has
   `datum_locus = proper-subset`; therefore `bridge(Pair1, T411) = REJECT`. The
   signature discriminates — it does not pass everything.
7. **Executable invariance sweep (game).** The A-vs-C separation `Δφ_0 = 1` is
   invariant under: permuting boundary players; adding any dividend on a
   coalition disjoint from the focus; adding any in-R dividend to both games.
   The localizing boundary-blind re-weighting changes `φ_0` but breaks symmetry.

## Success / honesty criteria

Succeeds as exploration if the shared signature is genuinely instantiated by both
and the comparison is honest - including reporting the invariance field as
**partial** for T411/T412 rather than forcing a match, and **rejecting** Pair 1.
A result of "PARTIAL HOMOLOGY, factorization guardrail required" is the current
honest outcome after T412: it would **promote the analogy toward a homology on
4/5 fields** while naming the exact remaining debt. No physics claim, no
governance claim, no cross-repo import, no promotion. Pauses for Joe.
