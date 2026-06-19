# T58: Bell-Test-to-H¹ Mapping

**Status:** open_formal_target
**Prerequisite tests:** T13 (finality sheaf cohomology), T21 (CHSH contextuality)
**Touches claims:** Q1, D1, R1

---

## What Is Being Tested

T21 gives the T13 H¹ obstruction a finite contextuality model: four CHSH-style
local contexts each admit valid finality sections, but no global assignment
satisfies all four simultaneously. The parity product witness matches the CHSH
contradiction structurally.

T21 is a finite combinatorial certificate. It does not establish that the H¹
obstruction in T13's sheaf language is the correct algebraic invariant for Bell
inequality violation in general — only that one specific finite model has the
right parity structure.

This test asks the stronger question: does the H¹ sheaf cohomology obstruction
over the finality presheaf map, in a well-defined and non-circular way, onto the
algebraic condition that generates Bell inequality violation in quantum mechanics?

If it does, phantom incomparability — currently a finite-model result about
bounded record access — becomes a structural physics prediction: any physical
system exhibiting Bell violation instantiates a finality presheaf with nontrivial
H¹ over its measurement context cover.

That would upgrade T13/T21 from "consistent with Bell" to "structurally explains Bell."

---

## Existing Machinery

**From T13:** The finality presheaf assigns a `FinalitySection` to each observer
domain. Restriction maps encode causal inclusion. Cech coboundaries
δ⁰: C⁰ → C¹ and the `compute_h1_obstruction` function are implemented in
`models/spacetime_aggregation.py`. The canonical obstruction scenario is a
3-domain cover where pairwise restrictions are consistent but no global section
exists.

**From T21:** Four CHSH-style measurement contexts each have local finality
sections. No global assignment satisfies all four. The parity product witness
gives the same -1/+1 contradiction as CHSH. A probability-bearing extension
computes classical (2), Tsirelson (2√2), and PR-box (4) CHSH scores.

**From T56:** Phantom incomparability in the T51/T52 models lives at H⁰ of the
gap presheaf G = A/F, not at H¹ of F over a sparse cover — H¹ was zero
vacuously because pairwise overlaps had trivial order data. The Bell mapping
targets a different cover structure: the measurement context cover, where the
T21 parity constraint does generate a nontrivial 1-cocycle candidate.

---

## Formal Target

**Theorem candidate (to prove or refute):** Let X be the measurement context
space for a CHSH experiment — the cover {A0B0, A0B1, A1B0, A1B1} of the
four-setting Bell scenario. Define a finality presheaf F over X whose stalk F(U)
at each context U is the set of finality assignments consistent with the local
measurement constraint. Define restriction maps as the natural constraint
projections on shared measurement settings.

Then:

1. F satisfies the presheaf axioms over the context cover X.
2. The CHSH parity constraint defines a Cech 1-cocycle in C¹(X, F).
3. This 1-cocycle is not a coboundary — the parity constraint has no global
   solution — and therefore represents a nontrivial class in H¹(X, F).
4. The Tsirelson bound 2√2 appears as the maximal CHSH score compatible with a
   no-signalling finality assignment, and the classical bound 2 as the score
   achievable by a global section of F.

Two coefficient variants must be tried: (a) Boolean-valued sections with Z/2
coefficients, matching T26's binary encoding; (b) real-valued CHSH correlators
with ℝ coefficients, matching T21's probability-bearing extension.

Success requires at least one variant satisfying all four conditions. Partial
success is conditions 1–3 without the Tsirelson bound recovery in condition 4.

---

## Success Conditions

- Precise presheaf definition over the measurement context cover with sheaf axioms
  verified.
- An explicit Cech 1-cocycle computed from the parity constraint, shown to be a
  cocycle and not a coboundary.
- A statement of the form: "Bell violation iff H¹(X, F) ≠ 0 for this presheaf
  over this cover."
- If the Tsirelson bound falls out, it appears as a bound on the H¹ class norm —
  not as an additional assumption.
- The result is stated without importing quantum amplitudes, Hilbert space
  structure, or Born rule. The H¹ class is defined entirely in finality-presheaf
  terms.

This is the threshold for "physics prediction": the obstruction is not a
post-hoc labeling of a known quantum result, but a derivation of the Bell
violation condition from presheaf structure.

---

## Failure Conditions

**Weakenings** — do not kill the goal but require retreating to a narrower claim:

- The parity constraint is a cocycle but a coboundary over a finer cover.
  Obstruction is cover-dependent, not intrinsic.
- H¹ is nontrivial but the Tsirelson bound does not emerge. The mapping is
  incomplete — does not characterize the quantum/super-quantum boundary.
- Presheaf satisfies conditions 1–3 only for one coefficient group, making the
  result encoding-sensitive.

**Killers** — end this line:

- Sheaf axioms fail for the measurement context cover. The object is not
  well-defined and the H¹ approach collapses.
- A global section of F exists consistent with CHSH violation. H¹ = 0. The T21
  parity certificate remains valid as a finite combinatorial certificate but the
  H¹ claim is false.
- Making H¹ nontrivial requires importing quantum-mechanical structure into the
  presheaf definition. The obstruction is not definable in purely finality terms.

---

## Constraints

- No quantum amplitudes or Hilbert space structure may appear in the presheaf
  definition.
- Nontrivial H¹ is not a hidden variable. Consistent with Q1's non-restoration
  of local hidden variables.
- No construction step may assume a global commit order on measurement events
  (consistent with R1).
- T56's lesson applies: confirm dim(C¹) > 0 before assuming the T21 parity
  structure lifts to H¹. Sparse covers can produce dim(C¹) = 0 vacuously.

---

## First Concrete Step

Compute dim(C¹) explicitly for the CHSH context cover {A0B0, A0B1, A1B0, A1B1}.

The pairwise overlaps are four single-setting intersections:
A0B0 ∩ A0B1 = {A0}, A0B0 ∩ A1B0 = {B0}, A1B0 ∩ A1B1 = {A1}, A0B1 ∩ A1B1 = {B1}.
The remaining two pairwise overlaps (A0B0 ∩ A1B1 and A0B1 ∩ A1B0) share no
measurement setting.

For each non-empty overlap, state what F assigns to the stalk. Write the parity
constraint as an element of C¹ and check whether it is a cocycle under δ¹: C¹ → C²
on triple overlaps.

If dim(C¹) > 0 and the parity constraint is a non-coboundary cocycle, the H¹
approach is viable. If dim(C¹) = 0 — the T56 failure mode — the cover is too
sparse and a denser topology must be tried before proceeding.

This step is a hand calculation over the T21 context structure and the T13 Cech
machinery. No new code required.

---

## Relation to Open Problems

A positive result (conditions 1–4) is the first concrete instance of the
spacetime-as-finality-colimit program's basic physics question: does the finality
presheaf structure have independently checkable physical consequences? Bell
violation would be the first such consequence at the cohomological level.

A negative result constrains which physical phenomena can be addressed through
H¹ and redirects to the H⁰(G) gap-presheaf structure from T56 and T57.
