# Research Direction Evaluation: Layer Separation, Signed Readout, Cross-Observer Finality Selection

## Status

Exploration / evaluation, 2026-06-11. Response to the Research Direction Note (TaF × GU). This is an evaluation, not an implementation: verdicts, novelty checks, smallest claims, and an incorporation plan. Grounded in: GU's signed-readout test spec (`gu-formalization/explorations/time-as-finality-crosswalk/signed-readout-record-graph-test.md`), the t11 lab results (T9–T12), and the existing audits.

## Verdict In One Paragraph

The direction is productive, and it is the *most* productive direction currently on the table — primarily because the repos have already paid empirical down-payments on it without naming it. T11's typed pipeline result (evidence joins cleanly; finality profiles don't inherit the join; access and decision transform both) **is** the four-layer separation thesis with data. T12's result (reconstruction ≠ binding; coupling determines content) separates accessibility from finality executably. The note's meta-insight — *record propagation, finality, observer accessibility, and physical readout are distinct mathematical objects that have been historically conflated* — is therefore not a speculation to evaluate but a pattern the labs keep finding. The risks are two: a shallowness trap in the signed-readout claim (the Jordan-decomposition objection, below) and a major prior-art collision for the selection reframing (quantum Darwinism's predictability sieve). Both are survivable with the narrowing specified here.

## 1. The Four-Layer Separation: Adopt

Propagation / finality / accessibility / readout as separate formal objects. Evidence already in hand:

- **T11:** evidence state has a join-semilattice; the observer-facing finality profile provably does not inherit it (51.11% LUB agreement). Two layers, two algebras.
- **T12:** observers with identical access to holders and different coupling profiles reconstruct different orders; an observer can reconstruct a record without being bound by it. Accessibility ≠ finality ≠ constraint.
- **T10:** proof verification improves forgery resistance but cannot reject valid conflicting records — certification and truth split.

What's missing is the fourth layer: **readout** — a decoded scalar/semantic value distinct from record stability. That is exactly the GU signed-readout spec's four-relation table (evidence order / causal order / finality relation / readout order). Adopting the separation as the program's spine is justified by the repos' own results.

## 2. The Signed-Readout Wedge: Adopt, But Sharpened — The Shallowness Trap

The candidate claim — monotone evidence + monotone finality + signed cancellation-bearing readout + no global time + observer consistency — is constructible **almost trivially**, and that is the problem.

**The Jordan-decomposition objection (the wedge's first antithesis, stated now so it can't ambush the paper):** any signed readout decomposes as R = P − N where P and N are each monotone accumulators (positive and negative support). "Non-monotone readout from monotone accumulation" is then mere bookkeeping — a difference of two counters — and a referee will say so in one line. GU's own `signed-calm-jordan` exploration suggests this is known there. An existence-by-construction theorem at this level is publishable nowhere.

**The sharpened claim that survives:** the interesting separation is not signed readout but **interference-bearing readout** — readout that is not *any* function of the monotone accumulators, because cross-terms carry it (|Σ amplitudes|² ≠ f(P, N) for any f computed from the counters alone). The precise, literature-anchored form:

> **Wedge theorem (target form):** there exists a finite causal record-graph model, with no global time order and observer-consistent temporal reconstruction (the T1/T12 substrate), in which evidence accumulation and observer-indexed finality are monotone while the readout measure sits at level 2 of Sorkin's measure hierarchy (pairwise-interfering, non-Kolmogorov) — and the readout provably does not factor through any enrichment of the finality profile by finitely many monotone counters.

This is small, provable-or-refutable, and has a clean failure condition: if every level-2 readout on such graphs *can* be re-expressed through finitely many monotone counters, the separation collapses and the direction is closed. Either outcome is informative (the WC-23 property again).

**Novelty check on signed-readout separation (the note's question 5):** the underlying physics distinction — additive classical records vs interfering amplitudes, with classicality emerging when interference cancels — is owned by **decoherent histories** (the decoherence functional's off-diagonal terms) and **Sorkin's quantum measure theory** (the interference hierarchy), with Wigner-function negativity as a third neighbor. What is plausibly novel: putting that distinction on a *record graph with observer-indexed finality and no global time*, i.e., the four-relation separation as a formal package, with the monotone-finality/level-2-readout coexistence as a theorem rather than an interpretation. Honest scores: physics novelty 2, formal-packaging novelty 4, publishability 4 *if* positioned against Sorkin and Gell-Mann–Hartle explicitly, tractability 4 (extends running code). The literature note must precede the theorem paper.

## 3. Cross-Observer Finality Selection: Adopt As Organizing Question — With Its Owner Named

"Why do some structures become universally stable across many observers?" is a genuinely better compass than "what is time" — it converts the project's most distinctive asset (observer-indexing) into its central question, and T9–T12 are all instances of it.

But the prior-art collision is maximal: this is **quantum Darwinism's question**, and the proposed theorem's required properties — persistence, redundancy, compressibility, observer-invariance, erasure resistance — are close to Zurek's **predictability sieve** and einselection criteria nearly item for item. A "Cross-Observer Finality Selection Theorem" written without that positioning would be the project's worst reinvention exposure yet.

The defensible delta, stated precisely: quantum Darwinism establishes selection-for-redundancy *within quantum mechanics, with the environment as the channel*. COFS generalizes to a **substrate-neutral selection principle** over arbitrary record graphs with (a) coupling/channel indexing (T12), (b) known composition behavior across scales (T11's typed pipeline, including where inheritance fails), and (c) noise/perturbation dynamics (T9's counterfactual traces). The theorem question becomes: *do the QD selection criteria follow from record-graph structure alone, without quantum mechanics?* If yes — QD is a special case of a more general selection principle (big, publishable). If no — the quantumness is load-bearing, which is also a finding. Recommended framing: keep "Time as Finality" as the project name; add COFS as hypothesis **H5** in HYPOTHESES.md (pending Joe's canon approval), with QD named as owner of the quantum instance in the same breath.

## 4. The Particle Program: Hold, Gated, As Specified

The note's own discipline is correct and should be enforced harder: "particle-like invariants" (stable localized noise-robust structures selected by cross-observer finality) before any talk of charge/spin/mass. Prior art to position against before even the invariants step: CA glider/soliton robustness literature, einselection, and noise-robust structures in Wolfram-style systems. The dialectical pressure tests for charge, spin, exclusion, gauge structure, and Lorentz behavior should not be scheduled until the invariants result exists — running them now would generate impressive-sounding documents about underived objects, which is the exact overclaim mode the note fears. Parked as Later with an explicit gate: no SM-feature dialectics before a demonstrated localized-invariant theorem.

## 5. Persona Quick-Pass (ten lenses, one line each)

| Persona | Verdict on the direction |
|---|---|
| Quantum foundations | The wedge is real but must cite decoherent histories or it renames the decoherence functional; the level-2 framing is the honest version. |
| Statistical mechanics | Monotone finality + non-monotone readout is unsurprising (free energy vs entropy); the record-graph/no-global-time setting is what's new. |
| Complexity science | COFS is selection-for-stability; demand an order parameter before "selection" does any explanatory work. |
| Cellular automata | Particle-like invariants = gliders under noise; literature exists; the *cross-observer* selection criterion is the possibly-new filter. |
| Wolfram physics | Multiway + observer-selection is adjacent; differentiate by the finality preorder's formal results (T11), which that program lacks. |
| Distributed systems | The four-layer split mirrors log/commit/read-view/materialized-view — strong intuition pump, cite Lamport lineage, never as proof. |
| Information theory | The non-factorization claim is a data-processing question: can cross-terms survive the counter compression? Provable either way. |
| Mathematical physics | The wedge theorem is well-posed iff "enrichment by finitely many monotone counters" is defined precisely; do that first. |
| Philosophy of science | The conflation-diagnosis paper (four objects historically conflated) is publishable *independent* of any physics result — the safest artifact in the program. |
| Scientific publishing | Two papers, in order: (1) the separation/conflation note with the T11/T12 results; (2) the wedge theorem after the Sorkin positioning. COFS waits. |

## 6. Smallest Claims (the note's questions 3–4)

- **Smallest falsifiable claim:** on the T1/T12 substrate with signed record weights, the readout R = P − N is non-monotone while P, N, and the finality profile are monotone. (Trivially true — useful only as the lab's warm-up case, and as the explicit statement of what is *not* novel.)
- **Smallest publishable theorem:** the non-factorization form — no enrichment of the observer-indexed finality profile by finitely many monotone counters reproduces a level-2 (pairwise-interfering) readout on the same graph, while temporal reconstruction and observer consistency are preserved. With the Sorkin/decoherent-histories positioning, this is a focused, citable result independent of all cosmological claims — exactly the note's "meta-level insight" made theorem-shaped.

## 7. Incorporation Plan (work cards)

**RD-1 (High): T13 lab spec — signed and interfering readout on the coupling graph.** Files: t11 worktree `tests/T13-*.md`, models later. Phase 1: signed weights, R = P − N, demonstrate the trivial case and *label it trivial*. Phase 2: level-2 readout (complex weights or Sorkin measure), attempt the non-factorization witness: two evidence states with ordered finality profiles and inverted/cancelled readout not recoverable from any counter enrichment. Acceptance: witness exists or the collapse is demonstrated; either closes the question.

**RD-2 (High, blocks RD-1's paper): literature note — Sorkin quantum measure hierarchy, decoherent-histories decoherence functional, Wigner negativity, QD predictability sieve.** Four anchors, verified citations, one page each on what they own vs what the record-graph setting adds. Without this note the wedge paper is a reinvention risk; with it, the wedge paper has a related-work section that writes itself.

**RD-3 (Medium): COFS as H5.** Draft hypothesis text for HYPOTHESES.md naming QD as the quantum-instance owner and stating the substrate-neutrality question as the delta. Canon edit — requires Joe's approval per governance policy.

**RD-4 (Later, gated): particle-like invariants.** No work until RD-1 resolves; no SM-feature dialectics until a localized-invariant result exists. Gate written into the card to resist enthusiasm.

## 8. Particle-Invariant Target Registry (added 2026-06-11, from Joe's dialectical pass)

Joe ran the seven SM-feature dialectics; each output is a *proof target*, not a claim — consistent with the RD-4 gate. Filed here as a conditional registry. None is active work until its gate clears.

| Feature | Narrowed target (Joe's synthesis) | Prior-art owner to position against | Dependency / gate | Strength now |
|---|---|---|---|---|
| Quantum phase | Monotone provenance + non-monotone, cancellation-bearing readout as theorem | Sorkin quantum measure; decoherent histories | None — this IS RD-1/T13 | **Keystone** |
| Charge | Signed, conserved, observer-invariant labels from record-exchange consistency | CA conservation laws | After T13 | Strong toy target |
| Spin | Cross-observer reconstruction forces representation-like labels | **Wigner classification** (labels-from-group is his; the work is deriving the *group*); SU(2)-vs-SO(3) needs phase | Phase first | Deep, gated |
| Gauge | Local reconciliation over record graphs induces connection-like structure | **Lattice gauge theory** (Wilson parallel transport is this); delta = deriving the group | Positioning note first | Mostly owned |
| Lorentz | Which substrates yield large-scale Lorentz-like causal cones | **Causal set theory** (Poisson sprinkling Lorentz-invariance results) | Positioning note first | Occupied lane |
| Exclusion | Non-duplicable identity records require antisymmetric composition | **Spin-statistics theorem** (exclusion = spin + Lorentz) | Phase → spin → Lorentz → this | Last in chain |
| Mass | Inertia as resistance-to-update of finalized invariants | Landauer / WC-23 reversal cost; Higgs explicitly not addressed | Dynamical labs (T9 line) must mature | Weakest near-term |

Structural finding: the seven form a dependency tree rooted at phase — independently confirming RD-1/T13 as the wedge. One theorem unlocks the tree; running any other branch first inverts the dependencies.

**RD-5 (cheap, anytime): the conflation-diagnosis short paper.** "Record formation, finality, accessibility, and readout are distinct mathematical objects" argued from the T10–T12 results alone, no quantum claims. Lowest-risk publishable artifact in the program; also the best public explanation of what the project is.

## Relation To Repos

- TaF: t11 `TECHNICAL-REPORT-*` (T9–T11), `results/t12-coupling-v0.1-results.md`, [meta-layer analysis](meta-layer-taf-gu-formalization.md), [post-session reassessment](../audits/2026-06-10-post-session-reassessment.md)
- GU: `explorations/time-as-finality-crosswalk/signed-readout-record-graph-test.md`, `explorations/signed-calm-jordan/`, CANON claims 1–2
- Refusals from the meta-layer analysis apply unchanged: method flows freely; physics claims don't; no mutual credibility manufacture.
