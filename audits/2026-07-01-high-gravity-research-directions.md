# High-Gravity Research Directions — 2026-07-01

Scope: a steelmanned map of the three directions with the highest potential gravity — meaning the capacity, if the work is done and the claims survive, to produce field-defining results that get decided by experiment rather than argument. Each direction is presented as a ladder: the ordered sequence of artifacts and engagements that gets from the repo's current state to an experimentally decided result.

Method: each ladder assumes the strongest survivable version of the relevant claims (steelman posture). This is not a prediction that the claims survive. Every ladder is gated by the same first rung, and each names the kill condition that closes it. Nothing here overrides CLAIM-LEDGER status or the guardrails; this document ranks directions, it does not promote claims.

---

## 0. The Shared Gate

All three directions pass through the same chokepoint, already identified in the 2026-06-10 audit (Path 1 / WC-1–WC-3):

1. **Type D1.** The finality preorder becomes a formal object: four axes (distinct-holder redundancy, accessibility, robustness, reversal cost) with explicit types, not prose.
2. **Run T1.** The finite causal record graph exists as code with a worked example. Until it runs, C1, D1, and D2 have no failure exposure.
3. **Execute T5 as a genuine kill-test.** Does D1-finality reduce to entropy + decoherence + Landauer? Framed as a test that can demote D1, not as support.

T5's outcome is the router for everything below. Residue survives → Direction B opens. Full reduction → Direction B closes and effort consolidates on Direction A, whose mathematics is independent of the reduction question. Direction C is live either way.

What does not pass the gate: further North Star versions, persona panels, or GU cross-references. Per the independence audit, these dilute the serious surface. One typed definition and one number an experimentalist can test outranks every essay in the repo.

---

## Direction A — An Inequality for Temporal Order

**Ranked first overall.**

### The gravity

There is a proven template for how a foundations question becomes an experimentally decided one: compress the metaphysical question into an inequality, and experimental groups will test it for decades (Bell → CHSH → Aspect → loophole-free tests). No one has written the corresponding inequality for *temporal order*. Process-matrix work (Oreshkov–Costa–Brukner) tests causal structure, but there is no device-independent criterion separating "temporal order derived from stabilized records" from "background time." T49's Anti-Scalar result — no total preorder can replicate a partial order with incomparable elements — points directly at that hole.

### The ladder

1. **Generalize the Anti-Scalar result.** From the 3-event witness to arbitrary finite event structures: the Finality Reconstruction Theorem. This is the first post-gate artifact and is within the repo's demonstrated mathematical range (finite partial orders).
2. **Translate into process-matrix formalism.** Map the finality preorder onto the language the indefinite-causal-order community already uses. This step is the CHSH move and the single creative hinge of the entire direction: derive a quantitative bound on correlations achievable when temporal order among k events is record-fixed, violated when it is not.
3. **Publish in the field's native language.** arXiv (quant-ph), written in process-matrix / causal-reference-frame vocabulary, not repo vocabulary. Success criterion: one engaged theorist in the indefinite-causal-order community (IQOQI Vienna, Perimeter, Oxford).
4. **Co-author an experimental proposal.** Photonic quantum-switch experiments already run; the labs actively want new inequalities to test. A new criterion is exactly the artifact that converts theoretical work into an experimental program.
5. **First experiments.** If temporal order behaves as record-derived (partial, observer-indexed) in regimes where background-time models predict otherwise, that is a discovery, not an interpretation.
6. **Replication and absorption.** Loophole-closing iterations; the inequality becomes the standard operationalization of "is temporal order primitive?"

### Why first

The mathematics required is what the repo can actually produce today, and the receiving experimental community already exists and is actively testing adjacent claims. Probability of reaching an experimentally decided result is the highest of the three directions.

### Kill condition

If step 2 fails — the preorder produces no bound distinguishable from existing causal-nonseparability witnesses — the direction reduces to commentary on existing work and should be demoted honestly.

---

## Direction B — A Physical Criterion for Measurement Irreversibility

**Highest ceiling; conditional on T5.**

### The gravity

The quantum measurement problem is the largest named open problem the framework touches. Quantum Darwinism is the incomplete incumbent: it explains how record redundancy spreads but not *when a record becomes final*. H2's distinct claim is that finality — reversal cost plus distinct-holder redundancy plus access — is the true order parameter for when a measurement has happened, and that this threshold is observer-indexed. If that claim survives T5, it is a candidate completion of the decoherence program, and it is testable now: measurement reversal is established experimental fact (weak-measurement un-collapse in circuit QED, Katz et al. 2008 lineage — verify before entering literature/, per the no-fake-citations rule).

### The ladder

1. **Pass the gate with residue.** T5 must leave a component of D1 that does not reduce to entropy + decoherence + Landauer. Steelman assumption: the reversal-cost and distinct-holder axes carry the residue.
2. **Derive the discriminating number.** Predicted measurement-reversal probability as a function of record redundancy N and access structure, quantitatively different from decoherence-only predictions. Without a curve that differs from the incumbent's, there is no experiment.
3. **Publish the discrimination.** A paper whose entire content is: here are two curves, decoherence-only vs. finality, and here is the parameter regime where they separate.
4. **Lab collaboration.** Superconducting-qubit groups can prepare records with controlled redundancy across independent holders and measure reversal-cost scaling. The experiment is a discrimination test between two stated predictions — the strongest possible framing.
5. **If finality's curve wins:** first experimental discrimination *within* the measurement problem. Re-analyze existing quantum-Darwinism experiments (photonic environments) under the finality framework.
6. **Absorption:** the framework becomes a standard account of the quantum–classical transition.

### Why conditional

Lowest survival odds of the three: T5 plausibly reduces, and the incumbent (Zurek's program) owns the territory. But the residue, if it exists, is the single most valuable object the repo could produce. This is exactly why T5 must be run as a kill-test and not as support — either outcome is decisive, and the current framing (audit §: "T5 framed as support") is the direction's biggest internal risk.

### Kill condition

T5 reduces cleanly. Direction closes; record the demotion in CLAIM-LEDGER and consolidate on A.

---

## Direction C — A Thermodynamic Bound on Record Consensus

**Highest survival probability; feeds A and B.**

### The gravity

Landauer's principle went from theoretical bound to experimental verification to anchor of a field. Distributed systems knows that consensus has a cost (Lamport, FLP impossibility); physics knows that erasure has a cost (Landauer); no one has fused them into a single physical bound. That fusion is precisely this repo's Lamport round-trip — identified in the independence audit as the project's best story and the author's home-field credibility — made quantitative.

### The ladder

1. **Derive the positive complement of T110.** T110 blocks a strict scalar finality monotone in finite closed reversible systems. The positive result lives where T110 points: in open, coarse-grained systems, establishing k-observer record agreement requires minimum dissipation ≥ f(k, redundancy, reversal cost) · kT ln 2. Name the bound.
2. **Publish as a self-contained theorem.** Target register: PRL/PRX Quantum. "Thermodynamic cost of temporal consensus." A referee can check it without accepting any of the framework's larger claims — the same property that makes the typed-forgetting paper viable.
3. **Experimental test on Landauer-verification platforms.** Single-electron boxes and trapped ions measured Landauer's bound; a new fundamental bound in the same family is a clean, fundable experiment for the same labs.
4. **Engineering absorption.** Fault-tolerance overhead in quantum error correction *is* record-finality maintenance. If the bound is real, it becomes load-bearing in QEC resource accounting, which gives it independent industrial gravity.
5. **Compounding.** The bound makes reversal cost — currently D1's most hand-waved axis — an experimentally measured quantity, which directly strengthens Directions A and B.

### Why third but always-on

Nearly every rung is publishable regardless of the endgame, it survives both T5 outcomes, and it is the credibility engine: peer-reviewed rungs here are what make the field take Direction A's inequality seriously.

### Kill condition

f(k, ...) collapses to k independent Landauer erasures with no consensus-structure term — i.e., the bound is additive bookkeeping, not a new law. Demote to a pedagogical note.

---

## Focus Allocation

Near-term effort: roughly 70% on the shared gate (D1 typed → T1 run → T5 executed), because it is the router for everything else. Direction C runs in parallel at low intensity from the start, since its first rung (positive complement of T110) does not wait on T5. Direction A's step 1 (Anti-Scalar generalization) can also begin immediately. Direction B consumes no effort until T5 reports.

## Structural Requirements (all directions)

1. **Translation, not evangelism.** Every externally facing artifact must be written in the receiving field's native formalism — process matrices, Lindblad dynamics, stochastic thermodynamics — with repo vocabulary confined to internal documents.
2. **An established co-author per direction** before any experimental proposal. The repo is the workshop; it is not the vehicle.
3. **Kill conditions are commitments.** Each direction above names its closure condition. Closing a direction and recording it in CLAIM-LEDGER is a success of the method, not a failure of the project.
