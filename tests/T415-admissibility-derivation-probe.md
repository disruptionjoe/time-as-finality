# T415 — Admissibility-Derivation Probe (spec, frozen)

**Status:** exploratory swing on bridge obligation #2 of the
governance–Shapley–finality homology
(`explorations/governance-shapley-finality-homology-note-2026-07-02.md`),
building on the registered **T412** separator refactorization gate and the
**T414** certificate-identity bridge. Provisional T-number (**TESTS.md NOT
edited**; noted here only; registration pauses for Joe / the numbering
automation). No claim promotion; no CLAIM-LEDGER entry. Cross-domain material is
the **object of study**, never evidence. Spec frozen before the model file.

## The question

T412 proved the β=0 separator survives product-structure-preserving relabels but
is localized by an entangling parity fan-in, and concluded the R1 anti-relabel
property **needs an explicit admissibility rule** — flagging that if that rule is
a free **declaration**, the separator demotes to a coordinate-dependent exhibit.

The T414 bridge showed the game side (T413) has an admissibility rule that is
**derived**, not declared: the game's **symmetry / Arrow-IIA axiom**. Bridge
obligation #2 asks: does that derivation **port** to the quantum side, discharging
T412's "must be declared" worry?

Two candidate ports are tested and **distinguished**:

- **(P1) Equality-preservation.** Admissible ⇔ the relabel preserves the
  discriminator's defining equality (all proper-subset marginals of the two
  states stay equal). This is the naive reading of "IIA = don't change the
  irrelevant statistics."
- **(P2) Operational automorphism group.** Admissible ⇔ the relabel is an
  automorphism of the operational structure (the tensor product / coupling
  graph) — the correct analog of the game's symmetry axiom (automorphisms of the
  game = player permutations).

## Method (reuses T412 machinery; does not redo it)

Enumerate the full group of **reversible linear refactorizations** of the
3-qubit reach = invertible 3×3 matrices over F₂ (`GL(3,2)`, 168 elements), as
basis-permutation unitaries. Classify each by three **independently defined**
predicates and compare the induced partitions on the T412 parity separator:

- `product_preserving`: the matrix is a qubit permutation (product structure
  intact). [local bit-flips are affine and product-preserving too; handled as in
  T412]
- `global_parity_preserving`: `1ᵀA = 1ᵀ` over F₂ (the global parity functional is
  fixed).
- `equality_preserving`: computed — max proper-subset trace distance between the
  two relabeled states is 0 (via T412's `subset_trace_distances`).

## Predeclared legs (verdicts fixed before running)

1. **Baseline reproduces T412.** Parity pair: max proper-subset TD = 0.0, full-
   joint TD = 1.0.
2. **`equality_preserving ⇔ global_parity_preserving`** (computed set identity
   over all 168), matching the closed-form reason: a linear `A` maps the parity
   constraint to `⟨c, y⟩` with `c = A⁻ᵀ1`; a proper subset distinguishes iff it
   contains `support(c)`, impossible for a proper subset **iff** `c = 1` (weight
   3) **iff** `1ᵀA = 1ᵀ`.
3. **Counts:** `|GL(3,2)| = 168`; `equality_preserving = 24` (the stabilizer of
   the parity functional, `168/7`); `product_preserving (permutations) = 6`.
4. **THE TEETH — equality-preservation is strictly broader than product-
   preservation:** `entangling_equality_preserving = 24 − 6 = 18 > 0`. Exhibit
   one explicitly: `A = CNOT(2→0)·CNOT(2→1)` (`y0=x0⊕x2, y1=x1⊕x2, y2=x2`) is
   entangling (non-permutation), preserves global parity, and **preserves the
   equality** (max proper-subset TD = 0.0) while the fan-in `y0=x0⊕x1⊕x2`
   **breaks it** (factor-0 TD = 1.0).
5. **Circularity verdict on (P1).** Because a relabel is unitary, the full-joint
   TD is invariant (= 1.0) under **every** element of `GL(3,2)`; "equality-
   preserving" therefore means only "keeps proper-subset TD = 0," i.e. "keeps the
   separator a separator" — **tautological**, and it admits entangling maps an
   operationally local agent may not possess. (P1) cannot independently justify
   the admissibility rule.
6. **(P2) is the correct port.** The principled admissible class = the operational
   automorphism group (product/coupling-preserving = T412's class), the exact
   analog of the game's symmetry axiom. The separator survives it (T412). It is
   an **operational commitment** (which couplings the agent has), **not a free
   declaration** — but its **physicality is R2**: is the coupling graph /
   factorization physically forced or stipulated?

## Success / honesty criteria

Succeeds as exploration if it cleanly distinguishes (P1) from (P2), exposes (P1)
as circular via the 18 entangling equality-preservers, and states the honest net:
bridge obligation #2 is **structurally bridged** (game symmetry axiom ↔ quantum
operational-automorphism admissibility) but **not discharged to physicality** —
it bottoms out at R2, unchanged. Predeclared honest outcome: the naive "the
admissibility rule derives for free" hope is **refuted** (P1 circular); the
principled rule ports but remains R2-conditional. No physics/governance claim; no
promotion; pauses for Joe.
