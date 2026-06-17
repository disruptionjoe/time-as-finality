# N6: Prior-Art Anchors For Signed/Interfering Readout (RD-2)

## Purpose

The signed-readout wedge (RD-1/T13) claims that monotone record accumulation and monotone observer-indexed finality can coexist with non-monotone, cancellation-bearing readout. Before that becomes a paper, four bodies of work that already own pieces of the territory must be positioned against. This note does that. Citation status: the four primary anchors below were verified against journal/arXiv records on 2026-06-11; secondary references are standard but should get a DOI check before external use.

## Anchor 1: Sorkin's Quantum Measure Theory

**R.D. Sorkin, "Quantum Mechanics as Quantum Measure Theory," Mod. Phys. Lett. A 9 (1994) 3119–3127 (arXiv: gr-qc/9401003).** [verified]

What it owns: the interference hierarchy. Classical probability satisfies the Kolmogorov sum rule (level 1: pairwise additive). Quantum mechanics violates it — interference — but satisfies the next sum rule in the hierarchy (level 2: the triple-sum interference term I₃ vanishes while the pairwise term I₂ does not). This is the precise, standard formalization of "readout that is signed/cancellation-bearing yet lawful."

What the record-graph setting adds, if anything: Sorkin's measures live on history spaces with standard physics underneath. T13 asks whether a level-2 measure can coexist with a *monotone observer-indexed finality layer* on a finite causal record graph *with no global time order* — i.e., the four-relation separation (evidence/causal/finality/readout) as an explicit theorem. The hierarchy itself is borrowed, with attribution; the layered coexistence result is the candidate delta.

Kill condition for novelty: if Sorkin or successors (Dowker, Gudder's quantum measure and integration program) already prove a finality-layer separation result on causal sets, T13 reduces to a worked example and should say so.

## Anchor 2: Decoherent / Consistent Histories

**M. Gell-Mann and J.B. Hartle, "Quantum Mechanics in the Light of Quantum Cosmology," in *Complexity, Entropy and the Physics of Information* (1990); R.B. Griffiths, J. Stat. Phys. 36, 219 (1984); R. Omnès.** [standard; DOI check before external use]

What it owns: the decoherence functional D(α, β), whose off-diagonal terms carry interference; classical, additive, record-bearing histories emerge exactly when those terms vanish. Also the IGUS observer concept (the D2 collision already logged in the 2026-06-10 audit, WC-5). This is the physics-complete account of "classical records emerge when interference cancels."

What the record-graph setting adds: decoherent histories runs inside quantum mechanics; the consistency condition is dynamical. T13's separation is *structural and substrate-neutral*: it asks whether the finality/readout split is expressible without any Hilbert space, as a property of weighted record graphs. If yes, decoherent histories becomes the quantum instance of a more general layering — the same delta-shape as COFS vs quantum Darwinism.

Kill condition: if the separation cannot be stated without importing the decoherence functional's machinery, the wedge is a renaming and fails per H-failure-7.

## Anchor 3: Wigner Negativity

**E. Wigner, Phys. Rev. 40, 749 (1932); R.L. Hudson (1974) on non-negative Wigner functions; R.W. Spekkens, negativity–contextuality equivalence (2008).** [standard; DOI check before external use]

What it owns: the canonical demonstration that quantum states resist description by classical (non-negative, additive) probability — negativity of the quasi-probability distribution as the marker of nonclassicality, with Hudson's theorem delimiting exactly which pure states escape it and Spekkens connecting negativity to contextuality.

What the record-graph setting adds: Wigner negativity is phase-space-specific. T13's "readout not recoverable from phase-blind monotone summaries" is the graph-native analogue of "no non-negative distribution reproduces the statistics." The analogy should be stated once, precisely, and not leaned on.

Kill condition: none direct — this anchor is context, not competition. Misuse risk: claiming T13's witness "explains" negativity. It doesn't; it parallels it.

## Anchor 4: Quantum Darwinism And The Predictability Sieve

**W.H. Zurek, S. Habib, J.P. Paz, "Coherent states via decoherence," Phys. Rev. Lett. 70, 1187 (1993)** [verified]; **H. Ollivier, D. Poulin, W.H. Zurek, "Objective properties from subjective quantum states: environment as a witness," Phys. Rev. Lett. 93, 220401 (2004)** [verified]; **W.H. Zurek, "Quantum Darwinism," Nature Physics 5, 181–188 (2009)** [verified].

What it owns: selection-for-stability. The predictability sieve selects pointer states by minimal entropy production (persistence); OPZ defines objectivity operationally — simultaneously accessible to many observers, without prior knowledge, with consensus and no prior agreement — which is nearly the Cross-Observer Finality Selection criterion list item for item; quantum Darwinism establishes redundant environmental imprinting as the mechanism of classical objectivity, including a route to Born's rule.

What the record-graph setting adds: substrate-neutrality plus the formal results QD lacks at the graph level — channel/coupling indexing (T12), composition behavior including its failures (T11), and now the finality/readout separation (T13). The open question that defines COFS's worth: do the sieve's selection criteria follow from record-graph structure alone, without quantum mechanics? Either answer is a finding.

Kill condition: a COFS theorem whose premises secretly require quantum mechanics is the predictability sieve restated; the substrate-neutrality of every premise must be checked explicitly.

## Net Position For The T13 Paper

Borrowed with attribution: the interference hierarchy (Sorkin), the records-from-decoherence physics (Gell-Mann–Hartle), the nonclassicality framing (Wigner), the selection criteria (Zurek/OPZ). Candidate original contribution: the four-layer separation — evidence order, causal order, observer-indexed finality, readout — proven distinct by finite witness on a causal record graph with no global time, with the finality layer provably unable to carry a level-2 readout. Small, bounded, citable independently of every cosmological or particle claim in either repo.

## Relation To Repo

- [RD evaluation](../explorations/research-direction-evaluation-signed-readout-cofs.md) (RD-1, RD-2, target registry)
- [Q1](../claims/Q1-quantum-under-finalization.md), [T2 spec](../tests/T2-quantum-measurement-record-finality.md) — this note also discharges part of Q1's requested comparison
- GU: `explorations/time-as-finality-crosswalk/signed-readout-record-graph-test.md` (exploration link only)
