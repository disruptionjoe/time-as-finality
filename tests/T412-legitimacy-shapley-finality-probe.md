# T412 — Legitimacy-as-Shapley Finality Probe (spec, frozen)

**Status:** exploratory big-swing fixture spec. Provisional T-number (next free
after T411; **TESTS.md NOT edited** — noted here only). No claim promotion; no
CLAIM-LEDGER entry; ledger actions pause for Joe. Cross-domain (cooperative game
theory / governance) is the **object of study**, never evidence for physics or
for any sibling repo. This spec is frozen before the model file exists.

## Purpose

Test the candidate **governance-layering ↔ finality** homology surfaced in
`explorations/physical-boundary-hegelian-persona-pass-2026-07-02.md` and Joe's
Nash/Shapley intuition (chat, 2026-07-02), by porting the T411 discriminator
structure into a **classical finite cooperative game** and running the same
four-absorber gauntlet. The question is not "is governance true"; it is: *does
the finality wound (M1: finite closed ⇒ boundary is declarable/absorbable) and
the R1/R2 repair reproduce in a completely different, classical model class — and
does the Shapley/efficiency axiom CONSTRUCT the R1 object the pass said should
exist?*

## The mapping under test

- **Region R** = a proper player subset `S_R`; "R-supported statistics" = the
  restricted game on `2^{S_R}` (values and marginals of sub-coalitions inside R).
- **Capability / legitimate claim** of an in-R player = its **Shapley value**
  `φ_i` in the full game — a boundary-crossing functional.
- **Declared vs physical boundary** = arbitrary imputation vs the axiom-forced
  Shapley value (symmetry = automorphism-invariance; efficiency = the whole
  constrains every part).
- **Nash at finite scale vs Shapley at the infinite layers** (Joe's hint) =
  finite imputation/equilibrium **multiplicity** vs axiom-forced **uniqueness**,
  becoming unconditional only in the non-atomic (Aumann–Shapley) limit.

## Fixture (fixed constants, predeclared)

Players `N = {0,1,2,3,4}`; reach `S_R = {0,1,2}`; boundary `= {3,4}`; focus
player `i = 0`. Games specified by Harsanyi unanimity **dividends** `d(S)`;
`φ_i(v) = Σ_{S ∋ i} d(S)/|S|`; `v(T) = Σ_{S ⊆ T} d(S)`. Exact rational
arithmetic (`fractions.Fraction`).

- **Base** `v_A`: `d({0,1,2}) = 6`. Predeclared `φ_A = (2,2,2,0,0)`, `v_A(N)=6`.
- **Pair 1 — boundary-dividend** `v_B = v_A + [d({0,3}) = 2]`. Predeclared
  `φ_B = (3,2,2,1,0)`, `v_B(N)=8`; `φ_0` shift `Δ = 2/|{0,3}| = 1`.
- **Pair 2 — efficiency-only** `v_C = v_A + [d({0,1,2,3,4}) = 5]`. Predeclared
  `φ_C = (3,3,3,1,1)`, `v_C(N)=11`; `φ_0` shift `Δ = 5/5 = 1`.

## Predeclared legs (verdicts fixed before running)

1. **Shapley cross-check.** Dividend formula and the 120-permutation marginal
   average agree exactly for `v_A,v_B,v_C`; efficiency `Σφ_i = v(N)` exact.
2. **Within-R equality (both pairs).** `v_A(T)=v_B(T)=v_C(T)` for every
   `T ⊆ S_R`; and all R-supported marginal-contribution statistics identical.
3. **Shapley separation (both pairs).** `φ_0` differs by exactly `Δ = 1` in each
   pair; the separating functional is boundary-crossing (Pair 1) / global
   (Pair 2).
4. **Absorber 1 — joint-record completion (the T401 move). Predeclared SPLIT:**
   - *Pair 1 → ABSORBED.* A single co-present **proper-subset** coalition query
     `{0,3}` separates (`v_A=0` vs `v_B=2`). Homolog of T411's single retained-Z
     measurement. Minimal separating coalition size predeclared `= 2`.
   - *Pair 2 → SURVIVES proper-subset completion (R1 satisfied).* Every proper
     subset `S ⊊ N` gives identical restricted games (`v_A|_{2^S}=v_C|_{2^S}`);
     the datum lives only in the grand coalition `v(N)` = the **whole**, not any
     proper subset. Enumerated over all `2^5 − 1` proper subsets.
5. **Absorber 2 — relabel / declared re-weighting.** A "boundary-blind"
   random-order value (orderings with a boundary player before `0` down-weighted)
   changes `φ_0` **but violates the axioms**: predeclared to break **efficiency**
   (`Σ ≠ v(N)`) and/or **symmetry** (unequal shares to interchangeable players in
   `u_N`). Shapley is the unique value satisfying efficiency+symmetry+null+
   additivity (axioms verified numerically). → the localizing relabel is
   **illegitimate**; Pair 2's global datum is relabel-proof *relative to the
   axioms (the constitution)*.
6. **Absorber 3 — "physical vs declared" honesty leg (R2).** `v(N)` (Pair 2's
   datum) and `d({0,3})` (Pair 1's) are **declared numbers**. R1 is satisfied by
   Pair 2; **R2 (physical forcing) is NOT** — physicality is handed to the
   non-atomic / infinite-layer limit. Predeclared to FIRE the analog of
   `boundary_physicality_reduces_to_declaration`: the classical game reproduces
   the wound exactly.
7. **Absorber 4 — Nash-multiplicity vs Shapley-uniqueness (the Joe bridge).** The
   imputation set of `v_C` (efficient, individually rational allocations) is a
   positive-dimensional polytope (many **declared** legitimate-looking splits);
   the four axioms single out **one** point. Predeclared: imputation set
   dimension `= |N|−1 = 4 > 0`; Shapley unique. Finite-N sensitivity of `φ_0` to
   a fixed grand-coalition dividend computed for `N=3,4,5` as an
   Aumann–Shapley-flavored **trend** (gesture, not proof; non-atomic limit is
   out of finite-witness house style).
8. **Quantum-residue negative (the sharp boundary on the homology).** Prove
   executably that in a finite game **any** Shapley difference implies a
   coalition-value difference (Shapley is linear in `v`), so a separator with
   *all coalition values equal* is impossible — the T411 quantum residue
   (information in **no** marginal, a genuinely non-classical global correlation)
   has **no classical Shapley analog**. Pair 2's R1 object is the *weaker*
   whole-coalition kind (datum in `v(N)`), not the no-marginal kind.

## Success / honesty criteria

This is a homology **probe**, not a discriminator claim. It "succeeds" as
exploration if it faithfully reproduces the finality wound and cleanly locates
what does and does not port. Predeclared honest outcome: **the homology is real
at the level of the wound (M1), the R1/R2 split, and the two escape hatches
(axiomatic legitimacy; infinite-limit forcing), but the specific T411 surviving
object is quantum and does not port** (Leg 8). No physics claim, no governance
claim, no cross-repo import. All promotion pauses for Joe.
