# Ideas-To-Explore Backlog

Status: ongoing backlog of speculative intuitions, candidate mathematical objects, conjectures, framing devices, and research directions. Nothing here is a claim of correctness. Items are preserved as submitted (with nuance intact), then annotated against the existing repo and known prior art in the Annotations section at the end. Promotion to `claims/` requires the normal claim-file structure and ledger entry.

Location note: this file lives in `explorations/` deliberately — backlog items use renderer/consensus vocabulary that the 2026-06-10 audit recommends keeping out of core surfaces until formalized.

---

## Active Queue From 2026-06-20 All-Persona Review

Source: [all-persona-last-24h-review-2026-06-20](all-persona-last-24h-review-2026-06-20.md).

These are review-derived work cards, not claims:

1. LossKernel separation/collapse test: determine whether typed attribution
   survives same endpoints, same composite/endpoint behavior, and same naive
   loss set, or collapses into ordinary provenance/effect annotation.
2. T90 weak-measurement platform instantiation: name an independent
   branch/provenance/reversal-cost observable before modeling, or demote T12.
3. T87 detector feasibility audit: map raw-log requirements to actual exported
   instrument files and decide whether the detector route is empirically
   feasible.
4. H7 entropy-accounting hard case: test whether bounded reversible local
   memory can be D1-monotone without exported history, erasure, or hidden sinks.
5. T19/T58 gap restriction maps: test whether the proposition-domain
   accessible-witness gap has a T57-style closure property. Goal:
   [Accessible Witness Gap Restriction Theorem](../open-problems/accessible-witness-gap-restriction-theorem.md).
6. Iterated Loss Dynamics: test whether repeated `LossKernel(T^n)` behavior
   adds information beyond one-step T69/T73 loss composition. Goal:
   [Iterated Loss Dynamics](../open-problems/iterated-loss-dynamics.md).
7. Obstruction Relocation / Reconstruction Debt: test whether projection can
   eliminate an object-level obstruction only by moving a reconstruction
   obligation into provenance, loss, admissibility, or gap data. Goal:
   [Obstruction Relocation And Reconstruction Debt](../open-problems/obstruction-relocation-reconstruction-debt.md).

## Active Queue From North Star v0.8 Physics Persona Review

Source: [north-star-v08-20-persona-physics-goal-backlog](north-star-v08-20-persona-physics-goal-backlog.md).

These are North Star geometry-probe work cards, not claims. They are meant to
stress, clarify, or demote physics-facing parts of the v0.8 vision while
leaving Time as Finality and Capability Projection as the main proof discipline.

1. North Star Physics Kill Matrix: list the absorber, falsifier, residue label,
   and next artifact for every physics sentence in v0.8.
2. Physics Claim Inventory And Known-Theory Cap Audit: rewrite each physics
   claim in the No-Free-Physics template before any promotion.
3. Gauge-Invariance Hard Gate For Shadow Claims: reject physics distinctions
   that change under gauge, relabeling, coordinate, basis, or representation
   convention.
4. Finite-To-Smooth Bridge Gate: state which finite TaF witnesses can safely
   support smooth geometry language, and which cannot.
5. Cross-Domain Shadow-Protection Theorem Hunt: attempt a bounded theorem
   skeleton for when observer shadows preserve capability.
6. Domain probes: run one bounded math-first probe for quantum records,
   thermodynamic arrow, causal access/horizons, spin/gauge/matter, and
   experimental discriminator ladders only after the relevant gates exist.

## Active Queue From Temporal Issuance Bridge

Source: [temporal-issuance-bridge-v0.1](temporal-issuance-bridge-v0.1.md).

These are bridge work cards, not claim promotions:

1. Completed by [T172](../tests/T172-issuance-to-finality-bridge.md):
   issuance-to-finality bridge model with source realization DAG, observer
   cadence/access rules, projection into TaF readout, and controls for same
   issuance/different cadence, same records/different hidden issuance, same
   issuance/different `mu`, nonmonotone access loss, and gluing failure.
2. H7 source/readout recast: stop treating finality alone as a physical-arrow
   generator. Test whether finality can be a sound observer-readable
   certificate or projection of a source-side realization order after absorber
   variables are matched.
3. Completed by
   [N13](../literature/N13-temporal-issuance-absorber-map.md): absorber map
   comparing Temporal Issuance against causal set theory, block-universe causal
   order, stochastic thermodynamics, information theory, instrumentation, and
   TaF record reconstruction. The bridge is translation residue unless a
   non-circular same-neighbor-data split survives those absorbers.

---

## Entry 2026-06-10: Distributed Records, Rendering, and Observer-Relative Reality

> Submitted by Joe, 2026-06-10. Preserved as written. See Annotations below for already-considered status.

### Core intuition

Reality may be better understood as a distributed system of records than as a single globally rendered state.

Observers do not directly access "the world as it is." Each observer renders a local reality from available records, inherited constraints, causal histories, and probabilities propagated forward from the past.

The past is what has become difficult to undo.

Matter may correspond to what has become sufficiently finalized, sufficiently constrained, and sufficiently invariant across many admissible renderings.

A useful framing:

> Reality is not what is observed.
> Reality is what remains invariant across admissible reconstructions from distributed records.

Time may therefore emerge from increasing finality rather than existing as a primitive background parameter.

### Important correction: not a blockchain model

Do not model this as: a single ledger, a single blockchain, a single state machine, a single consensus process, a single global observer.

Instead think: graphs of graphs, overlapping observer networks, overlapping systems of record, local consensus processes, recursive finality, hierarchical stabilization, checkpointing between scales, merge finality between systems.

Relevant mathematical inspirations (inspirations, not commitments): Avalanche, Snowball, probabilistic consensus, percolation theory, causal graphs, Bayesian inference, hierarchical Bayesian systems, information geometry, sheaf theory, category theory, renormalization, holographic compression, statistical mechanics.

### Observers as record keepers and renderers

Each observer is a local record keeper possessing: local records, limited causal access, limited rendering capability, probabilistic expectations, inherited records from other systems.

The observer does not necessarily create reality. Instead:

> The observer reconstructs reality from available constraints.

A useful formulation:

> Every observer maintains a set of admissible world reconstructions.

As records accumulate and stabilize, the space of admissible reconstructions shrinks.

### Matter as invariant structure

Avoid: "Matter is consensus."

Prefer: "Matter is invariant structure under distributed reconstruction." Or: "Matter is what remains stable across many independent reconstructions."

Consensus does not create reality. Consensus constrains possible renderings. Matter may emerge as a low-entropy region in the space of admissible renderings.

### Example: the distant star

Observers cannot render every atom, photon interaction, magnetic fluctuation, or microstate of a distant star. Yet observers can render: "There is a star there."

The star becomes a coarse invariant. As more records become available, resolution increases, uncertainty decreases, rendering becomes richer. Nearby objects render with greater detail because more constraints are locally available. Distant objects render as coarse but stable invariants.

Reality may therefore possess observer-relative rendering resolution.

### Recursive finality

> Finality may be compositional.

Examples: individual observations → memories → testimony → documents → institutions → civilizations.

At every level: lower-level records are compressed; higher-level systems inherit finality; not every underlying observation is preserved.

Research question:

> Can finality itself be recursively aggregated?

This may be one of the strongest candidate mathematical questions in the entire program.

### Consensus compression

Millions of observations may be compressed into a smaller canonical representation: scientific papers, textbooks, legal systems, institutions, history. The higher-level system inherits the finality of the lower-level observations.

Possible analogies (without claiming equivalence): holography, compression, sufficient statistics, renormalization.

### Accessibility versus stabilization

Global stabilization and local accessibility may be different quantities.

> What fraction of globally stabilized information is accessible to a local observer?

Possible quantity: A_i = accessible stabilized structure for observer i / total stabilized structure.

Bridge candidates: locality, observability, rendering, information horizons, hidden structure.

### Rendering as distributed Bayesian inference

Observers maintain probability distributions over possible world states. Records constrain those distributions; shared records further; highly replicated records further still.

Matter may correspond to structures that remain invariant across almost all admissible posterior reconstructions. This may be mathematically cleaner than direct consensus language.

### Dark matter-adjacent speculation

Speculative; not a primary claim.

Potential analogy: ordinary matter = high finality + high accessibility; hidden structure = high finality + low accessibility.

> Can a distributed record model naturally produce a large gap between globally stabilized structure and locally renderable structure?

This is a much safer question than "Dark matter is hidden consensus records." Avoid the stronger claim.

### Candidate mathematical problem

> Explore mathematical frameworks in which observers maintain partial records of a shared causal history, and reality corresponds not to a single globally accessible state but to the set of invariants that remain stable across admissible reconstructions from distributed records.

Alternative: Given a graph-of-graphs of observer-record systems, where subgraphs can stabilize, checkpoint, compress, merge, and become inputs to higher-level systems, define natural notions of finality, accessibility, and rendering resolution.

Alternative: How does the space of admissible world reconstructions shrink as records accumulate, propagate, and become difficult to reverse?

### Candidate conjectures (submitter's own ratings: novelty / profundity / publishability)

1. Reality can be modeled as a distributed system of records rather than a globally rendered state. (4/5/3)
2. The past is best understood as what has become difficult to undo. (3/5/4)
3. Matter corresponds to invariant structure across admissible reconstructions. (5/5/4)
4. Consensus does not create reality; it constrains the space of admissible renderings. (4/4/5)
5. Observers are renderers operating over partial records rather than direct perceivers of a global state. (3/4/5)
6. Reality possesses observer-relative rendering resolution. (4/4/4)
7. Finality is compositional: finalized subgraphs can become stable objects for higher-level systems. (5/5/5)
8. Objects, institutions, histories, and civilizations may all be manifestations of recursive finality at different scales. (5/5/3)
9. Globally stabilized information may be substantially larger than locally renderable information. (4/4/5)
10. Matter-like objects emerge as low-entropy regions within the space of admissible reconstructions. (5/5/4)
11. The correct mathematical object is not consensus itself but invariance under distributed reconstruction. (5/5/5)
12. There may exist a mathematically meaningful distinction between stabilized structure and accessible structure. (4/4/5)
13. A graph-of-graphs model of observers and record systems is more fundamental than a single consensus network. (5/4/5)
14. Dark matter may be a useful analogy for hidden stabilized structure, even if not literally explained by it. (3/3/2)

Submitter's priority ranking: 1. recursive/compositional finality; 2. invariance under distributed reconstruction; 3. graph-of-graphs consensus structures; 4. accessibility vs stabilization; 5. rendering resolution; 6. distributed Bayesian reconstruction; 7. consensus compression; 8. dark matter analogy.

---

## Entry 2026-06-11: Mattering-First (M1) — relevance as the fundamental layer

> From discussion, 2026-06-11. Joe's claim, preserved: "settled" mis-frames the system — there is no eventual global consensus, only many levels of consensus intertwined and overlapping (now supported by the T11 local-to-global gluing failure and T1's preserved incomparability). Deeper: observers' record sets of what crossed the rendering threshold — experienced time and 3D space — are not the fundamental thing; they arise from *what matters to the observer, the record holder*.

**Vocabulary rule adopted:** finality is a three-place relation — final(record, domain, channel) — never an unindexed property. "Settled" without an index is banned alongside unqualified "consensus."

**De-psychologized core (the bridge):** mattering = affectability = coupling. D2's condition 1 ("can be affected") already encodes it. An observer's "mattering structure" is its coupling/channel profile; records form only where couplings exist. Neighbors to position against (verify before citing): von Uexküll's umwelt, Zurek's interaction-Hamiltonian pointer selection, Hoffman fitness-relevance (N2), Friston Markov blankets.

**The fork (must be chosen before promotion):**
- **M1-weak:** experienced time/space — the rendered interface — arise from the observer's coupling profile. Repo-compatible (C1 + D2 + WC-29). Testable now: extend the T1 model so record formation is conditional on a coupling profile; show two observers with different profiles reconstruct different temporal orders from one underlying graph. (Candidate next lab: T12.)
- **M1-strong:** causal structure/geometry themselves arise from mattering. Stated failure condition: the coupling circularity — what can matter is defined by couplings, which are defined by physics in spacetime. The claim is unpurchased until the loop is either broken (non-physical mattering primitive: exits science) or shown to close as a consistent fixed point (Wheeler participatory territory; requires the rendered-interface source map).

**Refinement (2026-06-11, Joe): matter as non-optional constraint.** Physical matter "matters" differently from ideas because its constraints bind unconditionally for any coupled observer — you cannot opt out of the wall, while an idea constrains only through interpretive channels and only conditionally. Candidate formal object: **constraint hardness** of a record = the degree to which its constraint binds independent of the observer's internal state, across the observer population coupled through any channel. Matter-grade record = high finality + universal-channel constraint + non-optional binding; idea-grade record = high (social) finality + interpretive-channel constraint + conditional binding. This gives "matter" a definition *inside* the framework (constraint non-optionality × channel breadth) rather than as a primitive, echoes the ESSAY's wall passage ("your shoulder will get a rapid local proof"), and adds a second observable to the T12 experiment: hardness, alongside reconstructed order. Note the convergence: mattering = coupling (M1) and matter-hood = unconditional constraint through universal channels (this entry) make "what matters" and "what is matter" two points on one coupling-structure spectrum — which is presumably why the words share a root.

Disposition: M1-weak = promote toward a T12 experiment spec (now with two observables: reconstructed order + constraint hardness). M1-strong = hold at exploration, gated by the rendered-interface mechanism challenge.

## Annotations: Already-Considered Status (audit pass, 2026-06-10)

Dispositions: **in repo** (already a claim/guardrail/exploration), **known prior art** (exists in literature; needs positioning, not invention), **new — promote** (genuinely new to the repo and worth a work card), **new — hold** (new but blocked on other work), **closed** (already evaluated and closed this cycle).

| # | Conjecture (short) | Status | Nearest repo item | Nearest prior art (verify before citing) | Disposition |
|---|---|---|---|---|---|
| 1 | Distributed records, not global state | In repo | R1, A1, S1 | Lamport 1978; relational QM (Rovelli 1996) | Covered; adds nothing beyond R1+A1 |
| 2 | Past = hard to undo | In repo | C1 — this is the repo's tagline verbatim | Reichenbach 1956; Albert 2000 | Covered |
| 3 | Matter = invariant structure across admissible reconstructions | Known prior art + partially new | D1 (objectivity side), G1 | **Nozick, *Invariances* (2001)**: objectivity = invariance under admissible transformations; structural realism (Worrall, Ladyman); Born 1953 on reality as invariants; quantum Darwinism's objectivity-as-redundancy | The *position* is established philosophy; the *operationalization* ("admissible reconstructions from distributed records") is new. Merge with #11. |
| 4 | Consensus constrains, doesn't create | In repo | G1's "Safer Phrasing" section says this almost verbatim | — | Covered |
| 5 | Observers as Bayesian renderers over partial records | Known prior art | D2, consciousness-as-record-renderer open problem, T8 | Predictive processing / generative world models (Friston); POMDPs; Bayesian epistemology | Covered + flagged: audit QC-3 deferred this layer; WC-7 quarantines the vocabulary |
| 6 | Observer-relative rendering resolution | Partially new | T7's remote-observation vs direct-participation distinction is the binary version | Coarse-graining; rate-distortion theory; sufficient statistics | New as a *graded* quantity. Safe if framed as "constraint density determines reconstruction resolution" — drop "rendering." Fold into #12's formalization. |
| 7 | **Recursive / compositional finality** | **New — promote** | No repo item. Closest: social-finality layer (exploration) gestures at scales without composition | Renormalization-group coarse-graining; sheaf-theoretic local-to-global; hierarchical aggregation; CRDT/checkpoint composition in distributed systems — but no known treatment of *finality* as a compositional operator | **Strongest new item.** Becomes WC-19. Question is crisp: do D1's four dimensions survive aggregation? (Does redundancy-of-redundancies behave like redundancy? Is the finality preorder monoidal?) Directly extends audit Path 1. |
| 8 | Objects→civilizations as recursive finality | In repo (weaker form) | Cognitive-social layer-split exploration, Layer 2 | Searle social ontology; institutional facts | Covered as intuition; the *new* content is #7's composition operator, not the examples. Hold behind #7. |
| 9 | Globally stabilized ≫ locally accessible | Partially new | D1 already separates accessibility from the other three dimensions; this asks for the *ratio* | **Holevo bound** (information present vs information accessible is a deeply studied gap in quantum info); horizon thermodynamics | New as a repo quantity; well-trodden as a general phenomenon. Formalizable: define A_i on the T1 graph in one page. Fold into WC-20 with #12. |
| 10 | Matter = low-entropy regions in reconstruction space | Known prior art | Overlaps #3 | Quantum Darwinism again: high redundancy = low conditional entropy of the consensus observable across fragments | Merge into #3/#11; not a separate conjecture |
| 11 | Invariance, not consensus, is the right object | New — promote (as a correction) | Audit WC-2 reached the adjacent conclusion (preorder, not score) independently | Nozick 2001 (same caveat as #3) | **Adopt as a framing correction now**: it strengthens G1, cleans S1's vocabulary problem, and costs nothing. Becomes part of WC-2's D1 v0.1 wording. |
| 12 | Stabilized vs accessible as distinct quantities | Partially in repo | D1's dimension separation; GLOSSARY's causal accessibility entry | Holevo; accessible information | Agree it is the easiest to formalize. WC-20: define stabilization(p) and access_i(p) as separate functions on the T1 graph; A_i ratio falls out. |
| 13 | Graph-of-graphs more fundamental than one network | Partially new (methodological) | T7 has multiple observers; no nesting anywhere | Multilayer/multiplex network theory; hypergraphs | Defensible as a *modeling commitment*, not a conjecture. Adopt as T1 v2 architecture once flat T1 works. Hold. |
| 14 | Dark matter analogy | **Closed** (this cycle) | No repo item; parent claim fenced by G1 + ESSAY §9 ("mass is finality density" explicitly refused) | Verlinde 2016 (informational lane occupied); MOND (no-hidden-stuff lane occupied) | Closed per 2026-06-10 discussion: human-scale significance fails on CMB-era timing; D2-scale records make it either standard dark matter restated or empirically backwards (dark matter is the *least* record-forming stuff — collisionless, EM-dark — yet gravitates most). Submitter's own downgrade to analogy-only is correct. Failure condition on record: the collapse-or-violate fork. |

### Ratings calibration note

Submitted novelty ratings run high where named prior art exists: #3, #10, #11 rate novelty 5/5 but sit adjacent to Nozick's invariance account of objectivity and quantum Darwinism's redundancy account — the novelty is in the synthesis and operationalization, not the position. #2 (the repo's existing core claim) and #4, #5 (repo guardrail + predictive processing) are not new at all. #7 is the one item where a 5/5 novelty rating may survive a literature check: a compositional/monoidal treatment of finality has no obvious named owner.

### Re-submission note (2026-06-10, second pass)

The "Distributed Records, Rendering, and Observer-Relative Reality" intuition was submitted a second time the same day with minor additions: an explicit "matter = low-entropy regions in admissible-rendering space" phrasing and a "holography in a broad information-theoretic sense" framing for consensus compression. Both are already captured — the low-entropy phrasing is conjecture 10 above (merged into 3/11), and holographic/boundary compression is covered in the consensus-compression section and in the ten-persona crosswalk's compositional-finality work (WC-24). No new disposition needed; logged for completeness.

### New work cards generated by this entry

**WC-19: Compositional finality (from #7) — High priority**
- Files: this backlog, claims/D1 (after WC-2), new open-problems/compositional-finality.md
- Problem: the repo treats finality at a single scale; whether finality aggregates (records-of-records, checkpoint inheritance) is unasked, and it is the backlog's most fertile new question.
- Change: write the open problem with the crisp version: given the D1 preorder on a record graph, define a quotient/aggregation operation (subgraph → node) and determine which of the four dimensions are preserved, strengthened, or broken by aggregation. State failure condition: if aggregation is just coarse-graining with no finality-specific structure, the question reduces to renormalization vocabulary.
- Why: extends audit Path 1 with a question nobody appears to own; matches the strongest available math toolkits (sheaves, RG, CRDT composition) without depending on any of them.
- Acceptance: open-problem file exists with the aggregation operation defined relative to WC-2's preorder; sequenced after WC-2/WC-3.

**WC-19 plain-language anchor (added 2026-06-10, Joe-approved framing):** the fact-ladder. A fact climbs: seen → remembered → told → written → textbook → "what everyone knows." Detail is discarded at every rung, yet settledness carries upward. The formal question is whether that carry follows rules (does combining two settled things reliably yield a settled bigger thing, the way 2+3 reliably yields 5?) or whether it can break. Use this as the motivating paragraph in the eventual open-problems/compositional-finality.md.

**WC-27: Observer-indexing as the stated guiding principle — proposal for canon (requires Joe approval before README edit)**
- Files: README.md, HYPOTHESES.md
- Problem: the ten-persona crosswalk located the project's entire novelty budget in one term — observer-indexing. The repo nowhere states this as its aim.
- Change: add a short principle near the top of README, draft wording: "Established physics studies irreversibility as a property of systems. This project studies it as indexed to bounded observers — what is settled, for whom, given which causally accessible records. Work that does not engage the observer index is almost certainly already owned by another field and should be cited, not reinvented."
- Why: converts the targeting finding into a standing filter for every future contribution and backlog dump.
- Acceptance: principle present in README; referenced as a triage criterion in CONTRIBUTING.

**WC-28: Computational cost asymmetry via cryptography (extends WC-23 / MC-2)**
- Files: open-problems/proof-carrying-record-finality.md, models/ (later)
- Problem: WC-23 needs a definition of computational reversal cost. Cryptography is the existence proof that cost asymmetry can be computational rather than thermodynamic: one-way functions are cheap forward / conjecturally intractable backward; ZK verification is cheap while the underlying computation is expensive; attack can cost vastly more than defense.
- Change: define candidate computational reversal-cost measures on the record graph drawing on one-way-function structure; mark honestly that crypto hardness is conjectural (one-way functions unproven, P≠NP-adjacent) and that quantum algorithms break specific asymmetries (Shor), so "computationally hard to undo" must be stated relative to an adversary model.
- Why: gives MC-2 (a second, non-thermodynamic source of finality) its mathematical substrate, and ties the repo's strongest author-expertise domain to its most decisive experiment.
- Acceptance: at least one formal candidate definition of computational reversal cost, with adversary model stated, usable in the WC-23 benchmark.

**WC-20: Stabilization vs accessibility as separate functions (from #9, #12, #6) — Medium priority**
- Files: tests/T1, GLOSSARY.md, this backlog
- Problem: D1 bundles accessibility with three stabilization-flavored dimensions; the backlog correctly notes the gap between them is itself a quantity (A_i), and resolution (#6) is the graded version.
- Change: in the T1 model, compute stabilization(p) (observer-independent: redundancy, robustness, reversal cost over the whole graph) and access_i(p) (observer-indexed reachability) separately; report A_i. Position against the Holevo accessible-information gap in the eventual literature note.
- Why: cheapest new formal content available; gives the dark-matter intuition its only safe descendant (a hidden-structure *ratio* in a toy graph, no cosmology attached).
- Acceptance: T1 output includes both functions and the ratio for at least two observers with different access.

**WC-21: Adopt invariance framing in D1 v0.1 (from #11, #3) — fold into WC-2**
- Change: word D1 v0.1 so that observer-network objectivity is defined as invariance of p's reconstruction across admissible observers/subgraphs, replacing residual "consensus" wording; cite Nozick and quantum Darwinism as the two flanking prior positions in the eventual literature note.
- Acceptance: the word "consensus" appears in D1 only inside the analogy-marked section.

**WC-30: Iterated Loss Dynamics - medium-high priority, gated**
- Files: [Iterated Loss Dynamics](../open-problems/iterated-loss-dynamics.md),
  [Persona Future Run Goals](persona-future-run-goals-2026-06-20.md),
  [Iterated Loss Dynamics Backlog Review](iterated-loss-dynamics-backlog-review-v0.1.md).
- Problem: T69 and T73 study one-step or path-level loss. The repo has not
  asked whether repeated traversal `T, T^2, ..., T^n` exposes recurrence,
  saturation, failure-type degradation, or hidden periodicity.
- Change: preserve the idea as a bounded executable target, not a main-line
  promotion. Add persona queue items for iterated dynamics, GU-generated finite
  loop witnesses, latent signatures, orbit space, and deferred recurrence
  classification.
- Why: this may become a legitimate LossKernel algebra extension, but the null
  explanation is strong: finite label-union saturation may explain everything.
- Acceptance: a first T101-style audit classifies at least fixed, saturating,
  period-2, and cycle-destroying trajectories, and states whether any behavior
  is not already explained by T73 union accumulation.

**WC-31: Obstruction Relocation / Reconstruction Debt - high priority, gated**
- Files: [Obstruction Relocation And Reconstruction Debt](../open-problems/obstruction-relocation-reconstruction-debt.md),
  [Persona Future Run Goals](persona-future-run-goals-2026-06-20.md),
  [Obstruction Relocation Backlog Review](obstruction-relocation-backlog-review-v0.1.md).
- Problem: several repo branches show a similar move: a visible obstruction is
  not solved but displaced into provenance, LossKernel, admissibility, gap, or
  protocol obligations. Calling this "conservation" would overclaim; calling it
  relocation or reconstruction debt may be testable.
- Change: add bounded persona goals for obstruction relocation, reconstruction
  debt quantification, and obstruction-degree flow. Keep degree-flow theorem
  language blocked until T69-style hypotheses are generalized.
- Why: Version 1 connects directly to T39, T63/T65, T68/T72/T74, T73, and the
  Pati-Salam witness. Version 2 may produce a neutral math-paper observable.
  Version 3 is theorem-shaped but currently too broad.
- Acceptance: a first T102-style audit classifies at least four existing tests
  by where the obstruction moves, and includes a counterexample where a
  projected obstruction genuinely vanishes because the source obligation was
  irrelevant or non-admissible.

**WC-32: Research Constellation persona-goal routing - high priority, exploratory**
- Files: [Research Constellation Orchestrator](research-constellation-orchestrator-2026-06-20.md),
  [Persona Future Run Goals](persona-future-run-goals-2026-06-20.md),
  this backlog.
- Problem: the 2026-06-20 constellation run surfaced sharper candidate goals
  than the existing broad persona queue, especially around reconstruction debt,
  obstruction relocation, operation rights, detector admissibility protocols,
  and aggregation/compositional finality.
- Change: route the themes as candidate persona goals only. Do not treat them
  as roadmap items, claim evidence, workflow triggers, or canonical research
  lines.
- Why: the strongest constellation signals are cross-room and easy to lose if
  they remain only inside the report. They need bounded exploratory runs with
  negative controls and prior-art pressure before any promotion decision.
- Already covered by existing queue entries:
  P24 constructor-theoretic finality; P33/P61 salience and relevance filtering;
  P34 Git semantic-merge witness; P35/P52 prior-art deletion pressure; P36
  access-control authority; P38 correlated tail regimes; P55 signed ancestry;
  P71 aggregation/coarse-graining; P78-P80 obstruction relocation and
  reconstruction debt.
- New focused persona goals added:
  P81 operation-right LossKernel; P82 negative-control search; P83 prior-art
  boundary matrix; P84 detector admissibility protocol; P85 detector threat
  model; P86 challenge-event provenance; P87 authority/trust-boundary
  admissibility; P88 correlated tail false-upgrade analysis; P89 reconstruction
  entropy; P90 accessibility ratio; P91 aggregation survival tests; P92 scale
  transition finality; P93 witness obligations; P94 typed access boundaries;
  P95 motif compression from constellation signals.
- Acceptance: each run remains bounded and exploratory; at least one run in the
  LossKernel/reconstruction-debt cluster must include a negative control where
  loss occurs but no meaningful reconstruction debt remains.
