# Records, Finality, and Readout: A Separation Result on Finite Causal Record Graphs

**Readiness caveat:** hostile review readiness is not external readiness. The
distinguishing-predictions ledger still has `[OPEN]` neighbors, so this paper
should not be used as an external-readiness certificate.

**Author:** Joe [surname / affiliation to be added] · **Draft v0.1, 2026-06-11** · **Status: ready for hostile review, not yet submitted**

*Code and machine-checked witnesses: `time-as-finality` repository (T1, T11–T13 laboratories). All numbered claims below are verified by unit test; reproduction commands in Appendix B.*

---

## Abstract

In informal reasoning about measurement, evidence, and classical fact-formation, four notions are habitually treated as one: the accumulation of records, the settledness ("finality") of what they support, an observer's access to them, and the value an observer reads out. We exhibit a minimal formal setting — finite causal record graphs with no global time order — in which these four are provably distinct mathematical objects. The central result is a separation theorem proven by finite witness: there exist record states with identical observer-indexed finality profiles and different readouts, and causal trajectories along which every finality dimension grows monotonically while readout fully cancels and returns. The readout measure responsible sits exactly at level 2 of Sorkin's interference hierarchy (pairwise interference present, triple sum rule satisfied), so the gap between finality and readout has the same formal signature as the gap between classical and quantum measures — while the record and finality layers remain entirely classical. We prove a characterization pair delimiting the result: readout fails to factor through *any* weight-blind summary whenever two distinct weights exist (with a measure-zero caveat we state exactly), yet factors through finitely many monotone counters whenever the weight alphabet is finite. We claim no derivation of quantum mechanics; the contribution is the conflation diagnosis made refutable-by-exhibit, in a substrate-neutral setting.

## 1. Introduction

The intuition that "the past is what has become hard to undo" suggests a research program: model facts as records propagating through a causal structure, define how settled a fact is for a bounded observer, and ask what follows. A natural background assumption in such a program — and, we suggest, in much informal reasoning about evidence generally — is that what an observer *measures* is some increasing function of how *settled* the underlying records are. More evidence, stronger signal.

This paper shows that assumption is false in the cleanest setting we could construct, and false in a structured way. We work with finite causal record graphs: directed acyclic graphs of events carrying record tokens, with bounded observers, an observer-indexed finality profile (support, redundancy, branch robustness, reversal cost — all functions of *which* records exist and are accessible, never of any annotation on them), and a readout map computed from complex weights attached to records. The finality layer is weight-blind by construction; that design choice is the formal content of the phrase "settledness measures the records, not the message."

Three results follow. First, a **separation theorem** (§4): readout is not a function of the finality profile — witnessed by two states with profile-identical records and readouts 4 and 0 — and not monotonically related to it even along single causal trajectories, witnessed by a chain whose finality strictly grows while readout passes through exact cancellation. Second, a **characterization pair** (§5) delimiting what the separation does and does not show: any weight alphabet with two distinct values defeats every weight-blind summary (Proposition A, with an exactly-stated measure-zero caveat), while any *finite* alphabet is recovered by per-class monotone counters (Proposition B) — so the separation is from the finality layer specifically, not from monotone bookkeeping in general. Third, a **hierarchy placement** (§6): the readout measure exhibits nonzero pairwise interference while identically satisfying Sorkin's triple sum rule, placing it at level 2 of the interference hierarchy — the level occupied by quantum mechanics — though nothing quantum was put in.

We are explicit about what is not claimed (§8). The result derives no physics. Its value, if any, is diagnostic: arguments that pass between "well-recorded," "settled," "accessible," and "measured" as if these were one notion can now be tested against a two-record counterexample.

## 2. Related Work

Four bodies of work own the territory this paper borders; we state our relation to each.

**Sorkin's quantum measure theory** [1] formalizes the interference hierarchy we use: classical (Kolmogorov) measures satisfy pairwise additivity (level 1); quantum mechanics violates it but satisfies the next sum rule (level 2, I₃ = 0). We borrow the hierarchy and its terminology outright. Our delta is the host structure: Sorkin's measures live on history spaces of physical theories; we show a level-2 measure coexisting with a monotone, observer-indexed, entirely classical finality layer on a record graph with no global time, and prove the two layers cannot be identified.

**Decoherent histories** [2, 3] provides the physics-complete account of how classical, additive, record-bearing histories emerge when the decoherence functional's off-diagonal interference terms vanish. Our separation is the structural skeleton of that picture, extracted from quantum mechanics: no Hilbert space, no dynamics, no consistency condition — just the demonstration that record-stability and interference-bearing readout are independently axiomatizable layers. If the skeleton could not be extracted, the layered picture would be quantum-mechanical rather than structural; that it can be is the point.

**Wigner quasi-probability and its negativity** [4, 5] is the canonical demonstration that quantum statistics resist non-negative additive description. Proposition A is a graph-native analogue — no weight-blind (hence "classical-summary") description reproduces the readout — but we use this only as orientation; we do not claim our witnesses explain or model phase-space negativity.

**Quantum Darwinism and the predictability sieve** [6, 7, 8] account for classical objectivity via redundant environmental records, and define objectivity operationally through multi-observer accessibility and consensus. Our finality profile's redundancy dimension is a deliberately simplified cousin of that machinery, and the wider research program this paper belongs to asks a question quantum Darwinism does not: whether its selection criteria follow from record-graph structure alone. This paper does not answer that question; it builds the layer separation any such answer would need.

The record/causal-order substrate descends from Lamport's happened-before order [9], which was itself constructed on the analogy with special relativity; we note the lineage to mark the analogy as inherited rather than asserted.

## 3. The Model

We summarize the formal contract (full version: FORMALISM v0.1 in the repository; the model is deliberately finite and substrate-neutral).

**Primitives.** A finite set of events E; a strict causal partial order <c induced by a DAG; record-bearing systems (holders); record tokens r = (id, proposition, value, formation event, holder, erasure-cost proxy); observers O = (observation event, bounded set of accessible holders); a reconstruction threshold. **Not primitive:** timestamps, a global clock, a universal present, a total order over spacelike events, experienced temporal order.

**Finality profile.** For proposition-value pair x, observer O, evaluation event e in O's causal past:

F_{O,e}(x) = (A, R, B, C) — accessible support, holder redundancy, causal antichain width of supporting formation events, and graph reversal count (records that must be erased to drop x below threshold). The componentwise preorder on profiles is the finality relation. Every component is a function of the *set* of accessible active supporting records. Temporal reconstruction (stabilization frontiers and their precedence) is likewise weight-blind; prior work in the repository established that it reconstructs causal precedence while preserving spacelike incomparability, distinguishes access loss from erasure, and is invariant under topological traversal choice.

**Readout layer (this paper's addition).** Each record carries a weight w(r) ∈ ℂ. For accessible active supporting records with weights w₁…wₙ: the **linear readout** is Σwᵢ (used only for the trivial case below) and the **Born-style readout** is R = |Σwᵢ|². The associated set function μ(S) = |Σ_{r∈S} w(r)|² is the readout measure.

## 4. The Separation Theorem

**Theorem 1 (layer separation).** On finite causal record graphs as above:

**(i) Non-factorization.** There exist record states with identical finality profiles and different readouts. *Witness W1:* two graphs, identical topology, holders, and records, weights (1, 1) and (1, −1) respectively. Both profiles are (2, 2, 2, 2); Born readouts are 4 and 0. Hence no function — monotone or otherwise — from finality profiles to readouts exists. □

**(ii) No monotone relation per trajectory.** There exists a causal chain along which accessible evidence and every profile dimension grow monotonically while readout passes through exact cancellation. *Witness W2:* records weighted +1, −1, +1 at successive chain events; evidence counts 1→2→3; profiles (1,1,1,1)→(2,2,1,2)→(3,3,1,3) (componentwise strictly growing); Born readout 1→0→1. Hence no monotone map relates profile growth to readout even along a single observer's history. □

**(iii) Conservativity.** The reconstruction layer is weight-blind: every reconstruction and profile result of the underlying model holds identically with weights attached (verified by running the full prior test suite unchanged alongside the new one).

**(iv) Observer consistency.** Observers with different holder access have individually monotone profiles, and readouts agree wherever access agrees; readout divergence between observers is attributable to access alone.

The proof of (i) and (ii) is the witnesses; they are two and three records respectively, and are machine-checked. We regard the smallness of the witnesses as a feature: the conflation being diagnosed fails at the first opportunity, not in some elaborate corner.

**The trivial case, conceded in advance.** With real signed weights and *linear* readout, R = P − N for monotone counters P, N (positive and negative support): the Jordan decomposition. Non-monotone linear readout from monotone accumulation is therefore mere bookkeeping, and nothing in Theorem 1 rests on it; the witnesses use the quadratic (Born-style) readout, whose cross-terms are what no profile dimension carries. This concession is itself a passing test in the repository.

## 5. Characterization: What Exactly Fails To Factor

**Proposition A (weight-blind insufficiency).** Let the weight alphabet contain distinct values u ≠ v. Among the three two-record states with weights (u,u), (u,v), (v,v) — which share every weight-blind summary, the finality profile included — at least two have different Born readouts.

*Proof.* Suppose |2u| = |u+v| = |2v|. The outer equality gives |u| = |v|. Then |u+v| = 2|u| = |u| + |v| forces equality in the triangle inequality, so u and v lie on the same ray; with |u| = |v| this gives u = v, a contradiction. □

*Caveat, stated exactly.* The naive two-state form — "(u,u) and (u,v) always differ" — is false: for each u, the v satisfying |u+v| = 2|u| form a circle (e.g. u = 1, v = 2e^{iθ} with cos θ = −¼), so isolated pairs of states can collide. The three-state form is the correct proposition, and the collision set is measure-zero, so generic pairs witness directly. (This error was caught during formalization by the symbolic proof contradicting an over-strong claim the numerical tests had "confirmed" — random draws avoid a measure-zero set almost surely. We record the episode as a methodological caution and keep both the exact proposition and the explicit exception witness in the test suite.)

**Proposition B (finite-alphabet sufficiency — the honesty clause).** If the weight alphabet Φ is finite, the per-class counts n_φ (records with weight φ) are monotone counters that determine the readout exactly: R = |Σ_φ n_φ φ|².

*Proof.* Immediate; the counts determine the amplitude sum. □

Together: the separation is from the **finality layer specifically** — and from weight-blind summaries generally — not from monotone bookkeeping as such. Tracking phase classes recovers everything, because phase classes specify the state. What Theorem 1 and Proposition A rule out is precisely the historically tempting middle ground: that some notion of *settledness*, computed from which records exist, how redundant, how robust, how costly to reverse — but blind to a phase-like annotation — could carry the measured value. It cannot, and two records suffice to show it.

**Open characterization question.** For infinite weight alphabets, which families of monotone counters suffice? We conjecture no finite family does for dense phase sets, but have not proven it; this is the paper's natural successor problem.

## 6. Hierarchy Placement: The Gap Is Level-2, Not Lawless

For disjoint record sets A, B, C with amplitude sums a, b, c, define I₂(A,B) = μ(A∪B) − μ(A) − μ(B) and the corresponding triple expression I₃(A,B,C).

**Proposition C.** I₂ = 2 Re(a·b̄), which is nonzero in general (e.g. ±2 for unit weights), while I₃ ≡ 0 identically.

*Proof.* Appendix A; the cancellation is a four-line expansion. Numerically verified over 200 random complex configurations. □

So the readout measure violates pairwise additivity but satisfies the next sum rule: level 2 of Sorkin's hierarchy [1] — the level quantum mechanics occupies. The finality-readout gap is therefore not arbitrary non-additivity; it is *lawful* interference, formally of the same grade as the classical/quantum gap, arising here in a model containing no quantum mechanics. We resist drawing more than the structural conclusion: the model shows where a level-2 readout *fits* relative to classical record-keeping, namely as a separate layer that monotone finality provably cannot host.

## 7. Supporting Separations From The Wider Laboratory

Two prior machine-checked results in the same repository separate the remaining pairs of layers, and we state them for completeness of the four-object diagnosis. **Composition:** compatible evidence states merge as a join-semilattice, but the observer-facing finality profile does not inherit that algebra (merged profiles equal the componentwise least upper bound in only 51% of an exhaustive four-source sweep; conflict can destroy locally settled decisions; locally consistent finality assignments need not glue globally). **Access and binding:** observers with identical record access and different coupling profiles reconstruct different temporal orders from one graph, without contradiction on shared content; and an observer can reconstruct a record's content without being constrained by it. Records, finality, access, readout: each adjacent identification now has a counterexample.

## 8. What This Does And Does Not Show

It does not derive quantum mechanics, the Born rule, or any interference phenomenon; the Born-style readout is an imported form, not a derived one. It does not show that physical finality escapes thermodynamic reduction (a separate open question in the program). It does not establish that any physical system instantiates the model. It shows that a cluster of notions routinely treated as interchangeable — recorded, settled, accessible, measured — are mathematically independent at the first nontrivial opportunity, in a setting with no quantum machinery to blame; and that the independence has the precise formal grade (level-2) where quantum phenomenology lives. Conversely, any framework or argument that *identifies* readout with a weight-blind settledness measure is refuted by a two-record exhibit.

## 9. Open Questions

The infinite-alphabet characterization (§5). Robustness of the witnesses under dynamically generated records rather than hand-authored ones. Whether the level-2 placement survives when readout is derived from a dynamical rule rather than imposed. Whether the selection criteria of quantum Darwinism follow from record-graph structure alone — the program's larger question, to which this paper contributes only the layer discipline.

---

## Appendix A: Symbolic Proof That I₃ ≡ 0

For complex x, y: |x+y|² = |x|² + |y|² + 2Re(x·ȳ). With disjoint sets carrying amplitude sums a, b, c:

μ(A∪B∪C) = |a|²+|b|²+|c|² + 2Re(ab̄ + ac̄ + bc̄)
μ(A∪B) = |a|²+|b|² + 2Re(ab̄), and cyclically.

I₃ = μ(A∪B∪C) − μ(A∪B) − μ(A∪C) − μ(B∪C) + μ(A) + μ(B) + μ(C).

Coefficient of |a|²: 1 − 1 − 1 + 1 = 0 (likewise |b|², |c|²). Coefficient of 2Re(ab̄): 1 − 1 = 0 (likewise the other cross-terms). Hence I₃ = 0 identically. ∎ (I₂(A,B) = 2Re(ab̄) survives, and is the interference.)

## Appendix B: Reproducibility

All claims are machine-checked. From the repository working copy:

```bash
python -m unittest discover -s tests -p "test_*.py"   # full suite: 66 tests
python -m unittest tests.test_t13_signed_readout -v    # Theorem 1, Prop C numerics
python -m unittest tests.test_t13_characterization -v  # Propositions A, B + exception circle
python -m models.run_t13                                # witness values as JSON
```

Relevant modules: `models/t1_record_graph.py` (substrate), `models/t13_signed_readout.py` (readout layer), `results/t13-signed-readout-v0.1.json` (witness output). Python ≥ 3.10, no dependencies beyond the standard library.

## References

*Primary anchors verified against journal/arXiv records 2026-06-11; [2]–[5], [9] are standard and were not re-verified in this pass — confirm DOIs before submission.*

[1] R. D. Sorkin, "Quantum Mechanics as Quantum Measure Theory," *Mod. Phys. Lett. A* **9** (1994) 3119–3127. arXiv:gr-qc/9401003.

[2] M. Gell-Mann and J. B. Hartle, "Quantum Mechanics in the Light of Quantum Cosmology," in *Complexity, Entropy and the Physics of Information*, ed. W. H. Zurek (Addison-Wesley, 1990).

[3] R. B. Griffiths, "Consistent histories and the interpretation of quantum mechanics," *J. Stat. Phys.* **36** (1984) 219–272.

[4] E. Wigner, "On the Quantum Correction For Thermodynamic Equilibrium," *Phys. Rev.* **40** (1932) 749.

[5] R. L. Hudson, "When is the Wigner quasi-probability density non-negative?," *Rep. Math. Phys.* **6** (1974) 249–252.

[6] W. H. Zurek, S. Habib, and J. P. Paz, "Coherent states via decoherence," *Phys. Rev. Lett.* **70** (1993) 1187.

[7] H. Ollivier, D. Poulin, and W. H. Zurek, "Objective properties from subjective quantum states: environment as a witness," *Phys. Rev. Lett.* **93** (2004) 220401.

[8] W. H. Zurek, "Quantum Darwinism," *Nature Physics* **5** (2009) 181–188.

[9] L. Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System," *Commun. ACM* **21** (1978) 558–565.
