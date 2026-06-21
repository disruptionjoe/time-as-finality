## A. Executive Summary

**Verdict:** promote v0.5 into v0.6 as a **North Star plus audit protocol**, not as a novelty theorem. The strongest defensible version is already close to what the draft says: “Capability Projection” is **projection sufficiency for typed capability objects**. Its value is not the slogan “observable equivalence is not capability equivalence,” which the draft correctly says is old; its value is the disciplined requirement that every claim declare `Y`, `X`, `pi`, `~=_X`, `K`, `Cap`, `~=_K`, observer/access profile, task, horizon, resource boundary, controls, native absorbers, and residue level.

**Mathematical status:** mostly sound with repairs. The set/equivalence case is basically correct, but v0.6 should change the default target from `Cbar : X / ~=_X -> K` to `Cbar : X / ~=_X -> K / ~=_K`, or explicitly say `Cbar` chooses representatives in `K`. The fiber-constancy lemma is right in spirit, but should be stated over **visible-equivalence fibers** and admissible domains, not only literal fibers. Approximate, preorder, stochastic, metric, and category-valued capability objects need a separate “native comparison” appendix, not a forced quotient treatment.

**Prior-art status:** most first-pass witnesses will be absorbed by sufficient statistics, Blackwell/Le Cam comparison, observability/reachability, POMDP belief states, abstract interpretation, process semantics, database view determinacy/provenance, resource theories, and sheaf/local-global frameworks. That is not a failure. It means the candidate should explicitly be an **absorption-aware audit framework**. The draft already names many of these absorbers and correctly sets the default expectation at translation or heuristic residue, not canonical residue.

**Physics status:** keep physics, but only under the draft’s no-free-physics rule: known physics induces `Cap`; `Cap` does not induce physics. QRT, GR causal accessibility, thermodynamic resource theory, EFT/RG, detector provenance, and topological response are worth keeping as typed anchors. Dark matter and dark energy should stay out of the main text except as one-line “typed model required” reminders.

**Witness status:** both recorded witnesses are correctly demoted to **Translation Residue**. The vector/ANN witness is underdescribed without index family/parameters/materialization state. The QRT witness is absorbed by adding the full bipartite state and by native QRT convertibility theory. The next real progress requires a minimality theorem, canonical enrichment family, executable witness suite, or cross-domain transfer result.

---

## B. Mathematical Verdict — Mostly Sound With Repairs

### 1. Projection sufficiency

The definition is right in the ordinary set/equivalence case:

[  
\pi : Y \to X,\quad Cap : Y \to K  
]

and `pi` is capability-sufficient when `Cap` factors through the visible quotient. The draft’s formulation captures the right idea: same visible class should determine the declared capability object up to declared capability equivalence.

**Repair:** write the default factorization as:

[  
\bar{Cap}: X/{\sim_X} \to K/{\sim_K}  
]

with

[  
\bar{Cap}([\pi(y)]_{\sim_X}) = [Cap(y)]_{\sim_K}.  
]

The current type,

[  
Cbar : X/{\sim_X} \to K,  
]

is acceptable only if `Cbar` is understood to choose representatives in `K` and the equality condition is checked modulo `~=_K`. That is mathematically workable, but `K / ~=_K` is the cleaner default.

### 2. Fiber-constancy lemma

The lemma is correct after one wording fix. It should not say only “every `pi`-fiber” unless `~=_X` is literal equality. It should say:

[  
Cap \text{ factors through } \pi \text{ up to } {\sim_K}  
]

iff

[  
\forall y_1,y_2 \in A,\quad \pi(y_1)\sim_X \pi(y_2) \Rightarrow Cap(y_1)\sim_K Cap(y_2),  
]

where `A ⊆ Y` is the admissible domain.

This handles partial maps, filtered witnesses, physical admissibility constraints, and finite-budget states. The draft’s proof sketch already uses visible equivalence classes rather than only literal fibers, so the proof idea is sound; the statement just needs to match the proof.

### 3. Approximate, preorder, probabilistic, and categorical cases

The draft correctly notices that `~=_K` must be an equivalence relation for quotient language to apply, and that preorder, tolerance, metric, or probabilistic comparisons need an induced equivalence if quotienting is used. But v0.6 should be sharper:

|Native `K` structure|Better default than forced quotient|
|---|---|
|Metric / tolerance|Require bounded fiber diameter: `diam(Cap(F_[x])) ≤ ε`. Do not quotient by `d≤ε` unless transitivity is proven or an equivalence closure is intended.|
|Preorder / resource preorder|Use mutual convertibility equivalence `a ~ b iff a ≤ b and b ≤ a`, or require monotone factorization through a posetal reflection.|
|Decision/risk object|Use value gap, regret, Bayes risk difference, or Blackwell/Le Cam deficiency rather than equality.|
|Stochastic object|Use equality in distribution, total variation, Wasserstein distance, coupling criterion, or risk-equivalence.|
|Category-valued object|Factor through a quotient category, reflection, fibration, or functorial semantics; fiber-constancy becomes isomorphism/equivalence/natural equivalence in the target category.|

### 4. Minimal capability-preserving quotient

Under equivalence assumptions,

[  
y_1 \sim_{Cap} y_2 \iff Cap(y_1)\sim_K Cap(y_2)  
]

does define the coarsest set quotient preserving the declared capability class. The language is mostly right.

**Repair:** call it the **capability-kernel quotient** or **Cap-kernel quotient** by default. “Minimal capability-preserving quotient” is understandable but overloaded. In automata and process semantics, the analogous objects are Nerode-style quotients, behavioral equivalences, bisimulations, or testing-equivalence quotients; in abstract interpretation they are complete abstractions or quotient/refinement constructions; in statistics they resemble sufficient or minimal sufficient summaries.

For structured `K`, “minimal” must specify the morphism class. Minimal among set quotients is not the same as minimal among congruences, monotone maps, metric contractions, Markov kernels, resource monotones, or categorical reflections.

### 5. Capability spread

The object is useful:

[  
Spread_{Cap}([x]_{\sim_X})={Cap(y)\mid \pi(y)\sim_X x}/{\sim_K}.  
]

The draft is right that factorization is equivalent to singleton spread in every visible class.

But the name should come with “known aliases”:

- ambiguity set;
    
- image of a fiber;
    
- conditional identified set;
    
- belief support;
    
- reachable-set ambiguity;
    
- abstraction concretization image;
    
- nondeterministic continuation set;
    
- decision-loss envelope;
    
- local-to-global obstruction witness.
    

Cardinality is meaningful only for finite, discrete, or quotient-finite `K`. Diameter is meaningful only with a domain-native metric. Add summaries: entropy over spread when a measure is declared, order width or antichain width for preorders, maximal regret, value gap, policy-value gap, Hausdorff distance for reachable sets, refinement order, deficiency distance, and worst-case certification loss.

### 6. Capability Type Gate

The type gate is necessary but not sufficient. The draft requires `K`, `Cap`, and `~=_K` before witness construction, and says capability equivalence must be domain-native, task-natural, and fixed before witness construction.

v0.6 should strengthen this to an **Operational Capability Gate**:

1. `Cap` must be native or operationally forced in the domain.
    
2. `Cap` must be declared before selecting the witness pair.
    
3. A native test, measurement, decision procedure, or evaluation protocol must be named.
    
4. Positive preservation controls and negative non-factorization fixtures must be included.
    
5. `Cap` must not merely restate the hidden difference between `y1` and `y2`.
    

Add `K` types: Markov kernels, experiment objects, statistical decision problems, policy classes, option/action-mask spaces, certification/admissibility predicates, audit logs, calibrated measurement models, channel capacities, information-theoretic rate regions, proof obligations, safety invariants, controllable subspaces, invariant sets, and error-budget envelopes.

---

## C. Prior-Art Verdict

**Most mature fields absorb the core phenomenon.** What survives is a reusable audit surface, not a new universal theorem.

|Neighbor|What it already covers|Legitimate state/data it gets to include|Residue after honest absorption|
|---|---|---|---|
|Sufficient statistics / statistical experiments|When data summaries preserve inference or decision-relevant information.|Sample space, model family, likelihood, parameter, loss, prior where relevant.|Translation residue unless v0.6 proves a reusable “capability spread” abstraction across experiments. Blackwell compares experiments by decision performance; Le Cam treats sufficiency and approximate sufficiency. ([Project Euclid](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-24/issue-2/Equivalent-Comparisons-of-Experiments/10.1214/aoms/1177729032.full?utm_source=chatgpt.com "Equivalent Comparisons of Experiments"))|
|Bayesian decision theory / Blackwell / Le Cam|Decision sufficiency, experiment comparison, risk functions, approximation.|Actions, losses, priors, randomized decision rules, experiment kernels.|Strong absorber. Use as primary statistical prior art. ([Project Euclid](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-24/issue-2/Equivalent-Comparisons-of-Experiments/10.1214/aoms/1177729032.full?utm_source=chatgpt.com "Equivalent Comparisons of Experiments"))|
|Control / observability / reachability|Whether hidden state can be reconstructed; which states can be reached; which constraints can be maintained.|Dynamics, controls, outputs, disturbance sets, horizon, estimator/belief state.|Translation residue. Kalman-style controllability/observability and viability/reachability already own much of this territory. ([University of Toronto Control](https://www.control.utoronto.ca/~broucke/ece557f/kalman.pdf?utm_source=chatgpt.com "On the General Theory of Control Systems"))|
|MDPs / POMDPs|Belief-state sufficiency for planning under partial observability.|Transition model, observation model, reward, policy, belief state.|Strong state-enrichment absorption: belief state is the native sufficient enrichment. Kaelbling, Littman, and Cassandra explicitly frame POMDP planning around belief-state sufficiency. ([MIT CSAIL](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf?utm_source=chatgpt.com "Planning and acting in partially observable stochastic domains"))|
|Abstract interpretation|Sound abstractions, precision loss, completeness, Galois connections.|Concrete semantics, abstract domain, abstraction/concretization maps, fixpoint semantics.|Strong native-theory absorption. Potential formal residue only if v0.6 gives a cross-domain audit theorem. ([Patrick Cousot's Website](https://pcousot.github.io/publications.html?utm_source=chatgpt.com "Patrick Cousot's publications on abstract interpretation"))|
|Process semantics / automata|Future tests, traces, failures, readiness, bisimulation, Nerode quotients.|Labelled transition systems, contexts, test languages, observations, continuations.|Strong absorber for “future distinguishing capability.” Hennessy-Milner logic and process equivalences already formalize indistinguishability by tests; Nerode quotients give canonical automata minimization. ([Computer Science & Statistics School](https://www.scss.tcd.ie/matthew.hennessy/pubs/old/HMjacm85.pdf?utm_source=chatgpt.com "Algebraic Laws for Nondeterminism and Concurrency"))|
|Databases / views / provenance|Query determinacy, view rewriting, provenance, materialized/index state, access control.|Schema, views, workloads, transactions, MVCC logs, provenance semirings, roles/policies, index state.|Strong absorber. Approximate/workload-bounded determinacy is the strongest route to formal residue. View determinacy asks when view answers determine query answers; semiring provenance unifies why-provenance variants. ([Springer](https://link.springer.com/chapter/10.1007/978-3-540-74456-6_9?utm_source=chatgpt.com "Rewriting Conjunctive Queries Determined by Views"))|
|Economics / agency / action|Opportunity sets, affordances, capability approach, options/policies.|Agent, environment, feasible actions, institutions, resources, policy class, preferences.|Mostly conceptual translation residue. Sen’s capability approach and Gibson’s affordances already own much of the “what can be done” language. ([Amartya Sen](https://sen.scholars.harvard.edu/publications/commodities-and-capabilities?utm_source=chatgpt.com "Commodities and Capabilities - Amartya Sen"))|
|Quantum/resource theories|Convertibility, free operations, monotones, LOCC, side information, purification.|Full state/channel, allowed operations, access profile, ancillary systems, catalyst, communication.|Strong absorber. QRT is the best physics anchor, but not novelty evidence. ([APS Links](https://link.aps.org/doi/10.1103/RevModPhys.91.025001?utm_source=chatgpt.com "Quantum resource theories \| Rev. Mod. Phys. - APS Journals"))|
|Sheaf/category/geometry|Local-to-global obstructions, quotient/factorization/reflection, fibrations.|Site/cover, local sections, restriction maps, gluing rules, target category.|Formal language absorber. Abramsky-Brandenburger’s sheaf treatment of contextuality is an example of local data failing to glue to global sections. ([arXiv](https://arxiv.org/abs/1102.0264?utm_source=chatgpt.com "The Sheaf-Theoretic Structure Of Non-Locality and Contextuality"))|

**Absorption protocol repair:** keep the draft’s two categories, but rename them and add three more.

- Rename **State-Enrichment Absorption** to **Native State Completion**.
    
- Rename **Native-Theory Absorption** to **Native Theorem Absorption**.
    
- Add **Equivalence-Repair Absorption**: the alleged failure disappears after correcting `~=_X` or `~=_K`.
    
- Add **Approximation-Threshold Absorption**: the failure is below the native tolerance, risk, recall, or error threshold.
    
- Add **Gauge/Representation Absorption**: the difference is pure gauge, coordinate convention, basis choice, phase convention, or representation redundancy.
    

“Translation residue” is legitimate and should remain. The draft is right that absorption is not failure; it is evidence that the instrument is honest.

---

## D. Physics Verdict

The **No-Free-Physics Rule** is the right firewall: physics-facing claims must run from known physics to induced capability object to projection audit, never from capability language back to new physics. The draft’s access-profile rule is especially important: local observers cannot be credited with global, purifier, environment, horizon-interior/exterior, or asymptotic capabilities unless the physical access profile grants that route.

|Physics-facing domain|Typed version|Verdict|
|---|---|---|
|Quantum Resource Theory|`Y`: states/channels; `X`: local reduced state or operational record; `pi`: partial trace or accessible measurement map; `Cap`: convertibility under free operations/LOCC; `K`: resource preorder/monotones.|**Keep and expand.** Best physics anchor, but QRT will absorb most witnesses. Resource theories and LOCC convertibility already own the native machinery. ([APS Links](https://link.aps.org/doi/10.1103/RevModPhys.91.025001?utm_source=chatgpt.com "Quantum resource theories \| Rev. Mod. Phys. - APS Journals"))|
|GR causal accessibility / horizons|`Y`: spacetime plus observer worldline/region; `X`: accessible causal past/diamond/screen; `Cap`: causal accessibility, domains of dependence, reconstructability; `K`: region poset/accessibility structure.|**Keep.** Strong physics anchor if framed as causal-access structure, not metaphysics. Hawking-Ellis is canonical for causal structure; event horizons are global, not locally detectable objects. ([INSPIRE](https://inspirehep.net/literature/87997?utm_source=chatgpt.com "The Large Scale Structure of Space-Time"))|
|Thermodynamic resource theory|`Y`: state, Hamiltonian, bath, work storage; `X`: macro/coarse variables; `Cap`: work extraction or thermal convertibility; `K`: resource preorder/free-energy family.|**Keep.** Strong typed Cap. Thermodynamic resource theories and stochastic thermodynamics already provide native absorbers. ([APS Links](https://link.aps.org/doi/10.1103/PhysRevLett.111.250404?utm_source=chatgpt.com "Resource Theory of Quantum States Out of Thermal Equilibrium"))|
|Detector / instrumentation provenance|`Y`: raw signals, calibration, environment, logs; `X`: reduced event packet; `Cap`: admissibility, auditability, reconstruction rights; `K`: provenance/certification object.|**Keep as physics-adjacent evidence infrastructure**, not as fundamental physics. Database provenance and metrology absorb much of it.|
|Condensed matter / topological response|`Y`: Hamiltonian/phase/boundary conditions; `X`: coarse bulk measurements; `Cap`: protected edge response or robust operation class; `K`: invariant/response/operation structure.|**Keep typed.** Good witness if “topological response constrains operations,” not “topology is capability.” Quantum Hall/topological-insulator references are appropriate anchors. ([APS Links](https://link.aps.org/doi/10.1103/PhysRevLett.49.405?utm_source=chatgpt.com "Quantized Hall Conductance in a Two-Dimensional Periodic ..."))|
|EFT / RG / coarse-graining|`Y`: microscopic theory; `X`: low-energy effective action/relevant operators; `Cap`: low-energy predictive or response capability; `K`: universality/prediction class.|**Keep as bridge and absorber.** RG/EFT is a mature account of what coarse-graining preserves or discards. ([PhilPapers](https://philpapers.org/rec/WILTRG-3?utm_source=chatgpt.com "The renormalization group and the ϵ expansion"))|
|Standard Model structure|`Y`: fields/states with gauge reps; `X`: measured particle properties; `Cap`: constraints on admissible interactions; `K`: representation/selection-rule structure.|**Hold/narrow.** Charge, spin, chirality, gauge representation, and selection rules constrain transformations; they are not themselves “capability.” Use gauge theory/representation language. ([INSPIRE](https://inspirehep.net/literature/430948?utm_source=chatgpt.com "The quantum theory of fields. Vol. 2: Modern applications"))|
|Black holes|`Y`: spacetime plus quantum/gravitational state; `X`: exterior accessible algebra/observations; `Cap`: causal access/reconstructability.|**Hold as stress test.** Do not claim progress on the information problem. Event horizons and holography are native absorbers. ([Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/archives/win2017/entries/spacetime-singularities/?utm_source=chatgpt.com "Singularities and Black Holes"))|
|Time|`Y`: physical histories; `X`: observer records at time; `Cap`: trajectory `t ↦ K_t`; `K`: time-indexed capability/resource object.|**Hold/narrow.** Say “capability along physical time,” never “replacement time.” Closed reversible systems and stationary stochastic systems do not yield strict scalar finality arrows without openness, coarse-graining, boundary conditions, erasure, or resource accounting.|
|Emergence|`Y`: multiscale dynamics; `X`: macrostate; `Cap`: viable actions, affordances, platform capabilities; `K`: option/viability/action structure.|**Hold.** Good as platform-capability language if linked to causal emergence, niche construction, viability, affordances, and active inference. ([Swarma](https://qiniu.pattern.swarma.org/attachment/%E5%BC%A0%E6%B1%9F%26%E8%A2%81%E5%86%B0-%E6%B6%8C%E7%8E%B0%E3%80%81%E5%9B%A0%E6%9E%9C%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0.pdf?utm_source=chatgpt.com "Emergence, Causality, and Artificial Intelligence"))|
|Dark matter / dark energy|Needs typed gravitational/cosmological audit.|**Demote from main text.** One-line analogy only unless `Y`, `X`, `pi`, `Cap`, `K`, access profile, and absorber are supplied. The draft already says this correctly.|

---

## E. Witness Verdict

### Vector / ANN retrieval witness

**Verdict:** correct demotion to **Translation Residue**.

If `pi` exposes “same corpus” but hides HNSW vs IVFFlat, index parameters, build procedure, materialization state, and query-time settings, then the projection is underdescribed for recall/latency/retrieval capability. The draft’s label `projection_underdescribed` is right.

Prior art absorbs it. ANN-Benchmarks explicitly evaluates quality/performance tradeoffs across algorithms and parameter settings; Faiss is built around efficient similarity search, approximate search, and compressed-domain search; pgvector’s documentation explicitly says approximate indexes trade recall for speed and can return different results after adding an approximate index. ([arXiv](https://arxiv.org/abs/1807.05614?utm_source=chatgpt.com "ANN-Benchmarks: A Benchmarking Tool for Approximate Nearest Neighbor Algorithms"))

**Stronger ANN witness:** define `K` as a workload-indexed recall/latency/error envelope under fixed query distribution and budget. Then attempt a minimal metadata theorem: which parts of index family, parameters, seed/build state, quantizer state, and materialization state are necessary and sufficient to preserve that envelope?

### Quantum Resource Theory witness

**Verdict:** correct demotion to **Translation Residue**.

The singlet-vs-product example with the same local reduced state `rho_A = I/2` is a good audit test, but not a new physics result. If the observer has only subsystem `A`, the local state is all they can use. If the observer has access to `AB`, the full bipartite state restores the distinction. If the capability object is LOCC/resource convertibility, QRT already owns the convertibility preorder, monotones, free operations, and side-information questions.

Nielsen’s LOCC theorem gives a majorization criterion for pure bipartite entanglement transformations, and modern QRT reviews explicitly frame resources through free states, free operations, resource measures, and operational tasks. ([Michael Nielsen](https://michaelnielsen.org/papers/majorization.pdf?utm_source=chatgpt.com "Conditions for a Class of Entanglement Transformations"))

**Stronger QRT witness:** make access profiles the main object. Compare:

[  
O_A,\quad O_{AB},\quad O_{A+B+\text{classical comm}},\quad O_{AB+\text{catalyst}},\quad O_{A+\text{purifier access}}.  
]

Then define `Cap_O` as the resource-convertibility preorder available under each access profile. Formal residue would look like an access-indexed family of resource preorders whose projection losses are classified uniformly across QRT, control, databases, and process semantics.

### Next best witnesses

1. **GR causal accessibility witness:** fixed spacetime plus two observer regions with same local observations but different causal futures/domains of dependence.
    
2. **Thermodynamic resource witness:** same macro-observable but different extractable work or thermal convertibility under declared operations.
    
3. **Database/view determinacy witness:** same view instance, different query/provenance/replay capability; then test view determinacy absorption.
    
4. **Process semantics witness:** same trace projection but different testing/failure capability; expect absorption by testing/failure semantics.
    
5. **QRT second witness:** local reduced state vs global resource preorder under explicit access profiles.
    

---

## F. Citation Plan With Insertion Points

|Reference|Supports|Insert in v0.6|Priority|
|---|---|---|---|
|Blackwell, D. “Equivalent Comparisons of Experiments.” _Annals of Mathematical Statistics_ 24(2), 1953.|Blackwell informativeness, experiment comparison, decision sufficiency. ([Project Euclid](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-24/issue-2/Equivalent-Comparisons-of-Experiments/10.1214/aoms/1177729032.full?utm_source=chatgpt.com "Equivalent Comparisons of Experiments"))|Prior-art absorption: statistical/decision theory.|Essential|
|Le Cam, L. “Sufficiency and Approximate Sufficiency.” _Annals of Mathematical Statistics_ 35(4), 1964.|Approximate sufficiency and comparison of experiments. ([Project Euclid](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-35/issue-4/Sufficiency-and-Approximate-Sufficiency/10.1214/aoms/1177700372.full?utm_source=chatgpt.com "Sufficiency and Approximate Sufficiency"))|Approximate/preorder/metric repair section.|Essential|
|Fisher/Neyman factorization theorem; Lehmann & Casella, _Theory of Point Estimation_.|Sufficient statistics, minimal sufficiency.|Mathematical prior-art paragraph.|Essential|
|Kaelbling, L. P., Littman, M. L., Cassandra, A. R. “Planning and Acting in Partially Observable Stochastic Domains.” _Artificial Intelligence_, 1998.|POMDP belief-state sufficiency. ([MIT CSAIL](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf?utm_source=chatgpt.com "Planning and acting in partially observable stochastic domains"))|Decision/control/POMDP absorber.|Essential|
|Kalman, R. E. “On the General Theory of Control Systems.” IFAC Congress, 1960.|Controllability, observability, state-space theory. ([University of Toronto Control](https://www.control.utoronto.ca/~broucke/ece557f/kalman.pdf?utm_source=chatgpt.com "On the General Theory of Control Systems"))|Control/dynamical systems absorber.|Essential|
|Aubin, J.-P. _Viability Theory_. Birkhäuser, 1991.|Viability kernels, controlled invariant sets. ([ACM Digital Library](https://dl.acm.org/doi/10.5555/120830?utm_source=chatgpt.com "Viability theory: \| Guide books \| ACM Digital Library"))|Control/reachability domain.|Useful|
|Althoff, M. et al. “Set Propagation Techniques for Reachability Analysis.” _Annual Review of Control, Robotics, and Autonomous Systems_, 2021.|Reachable-set computation. ([mediaTUM](https://mediatum.ub.tum.de/doc/1636781/bmxy2i7efrdywu2i4of09wh4w.Althoff-2021-ARCRA_preprint.pdf?utm_source=chatgpt.com "Set Propagation Techniques for Reachability Analysis"))|Capability spread summaries.|Useful|
|Cousot, P., Cousot, R. “Abstract Interpretation: A Unified Lattice Model...” POPL, 1977.|Abstraction, Galois connections, sound overapproximation. ([Patrick Cousot's Website](https://pcousot.github.io/publications.html?utm_source=chatgpt.com "Patrick Cousot's publications on abstract interpretation"))|CS/abstraction absorption.|Essential|
|Hennessy, M., Milner, R. “Algebraic Laws for Nondeterminism and Concurrency.” _JACM_, 1985.|Behavioral equivalence by tests/observations. ([Computer Science & Statistics School](https://www.scss.tcd.ie/matthew.hennessy/pubs/old/HMjacm85.pdf?utm_source=chatgpt.com "Algebraic Laws for Nondeterminism and Concurrency"))|Process semantics absorber.|Essential|
|Brookes, S., Hoare, C. A. R., Roscoe, A. W. CSP semantics.|Trace/failure/divergence semantics. ([Springer](https://link.springer.com/chapter/10.1007/11423348_1?utm_source=chatgpt.com "Retracing the Semantics of CSP \| SpringerLink - Springer Nature"))|Process semantics absorber.|Useful|
|Myhill-Nerode theorem / Nerode congruence.|Minimal automata quotients. ([Wikipedia](https://en.wikipedia.org/wiki/Myhill%E2%80%93Nerode_theorem?utm_source=chatgpt.com "Myhill–Nerode theorem"))|Minimal quotient discussion.|Essential|
|Afrati, F. “Rewriting Conjunctive Queries Determined by Views.” 2007.|View/query determinacy. ([Springer](https://link.springer.com/chapter/10.1007/978-3-540-74456-6_9?utm_source=chatgpt.com "Rewriting Conjunctive Queries Determined by Views"))|Database absorption.|Essential|
|Buneman, P., Khanna, S., Tan, W.-C. “Why and Where: A Characterization of Data Provenance.” ICDT, 2001.|Why/where provenance. ([Springer](https://link.springer.com/chapter/10.1007/3-540-44503-X_20?utm_source=chatgpt.com "Why and Where: A Characterization of Data Provenance"))|Provenance capability section.|Essential|
|Green, T. J., Karvounarakis, G., Tannen, V. “Provenance Semirings.” PODS, 2007.|Semiring provenance unification. ([ACM Digital Library](https://dl.acm.org/doi/10.1145/1265530.1265535?utm_source=chatgpt.com "Provenance semirings \| Proceedings of the twenty-sixth ..."))|Database/provenance absorber.|Essential|
|Sandhu, R. et al. “Role-Based Access Control Models.” _IEEE Computer_, 1996.|Access-policy operation sets. ([NIST Computer Security Resource Center](https://csrc.nist.gov/csrc/media/projects/role-based-access-control/documents/sandhu96.pdf?utm_source=chatgpt.com "Role-Based Access Control Models - NIST CSRC"))|Access control `K` examples.|Useful|
|Malkov, Y. A., Yashunin, D. A. “Efficient and Robust Approximate Nearest Neighbor Search Using HNSW.” 2016.|HNSW witness prior art. ([arXiv](https://arxiv.org/abs/1603.09320?utm_source=chatgpt.com "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs"))|ANN witness report.|Essential|
|Johnson, J., Douze, M., Jégou, H. “Billion-scale similarity search with GPUs.” 2017.|Faiss, approximate similarity search. ([arXiv](https://arxiv.org/abs/1702.08734?utm_source=chatgpt.com "Billion-scale similarity search with GPUs"))|ANN witness report.|Essential|
|Aumüller, Bernhardsson, Faithfull. “ANN-Benchmarks.”|Recall/latency/quality tradeoff benchmarking. ([arXiv](https://arxiv.org/abs/1807.05614?utm_source=chatgpt.com "ANN-Benchmarks: A Benchmarking Tool for Approximate Nearest Neighbor Algorithms"))|ANN absorption verdict.|Essential|
|Chitambar, E., Gour, G. “Quantum Resource Theories.” _Reviews of Modern Physics_, 2019.|QRT framework. ([APS Links](https://link.aps.org/doi/10.1103/RevModPhys.91.025001?utm_source=chatgpt.com "Quantum resource theories \| Rev. Mod. Phys. - APS Journals"))|QRT physics anchor.|Essential|
|Nielsen, M. A. “Conditions for a Class of Entanglement Transformations.” 1999.|LOCC convertibility and majorization. ([Michael Nielsen](https://michaelnielsen.org/papers/majorization.pdf?utm_source=chatgpt.com "Conditions for a Class of Entanglement Transformations"))|QRT witness.|Essential|
|Horodecki, R. et al. “Quantum Entanglement.” _Reviews of Modern Physics_, 2009.|Entanglement, LOCC, monotones. ([APS Links](https://link.aps.org/doi/10.1103/RevModPhys.81.865?utm_source=chatgpt.com "Quantum entanglement \| Rev. Mod. Phys. - APS Journals"))|QRT background.|Essential|
|Wilde, M. _Quantum Information Theory_. Cambridge, 2013.|Channels, reduced states, purifications. ([Cambridge University Press & Assessment](https://www.cambridge.org/core/books/quantum-information-theory/9DC2CA59F45636D4F0F30D971B677623?utm_source=chatgpt.com "Quantum Information Theory"))|Quantum formal appendix.|Useful|
|Hawking, S. W., Ellis, G. F. R. _The Large Scale Structure of Space-Time_. Cambridge, 1973.|GR causal structure. ([INSPIRE](https://inspirehep.net/literature/87997?utm_source=chatgpt.com "The Large Scale Structure of Space-Time"))|GR causal accessibility.|Essential|
|Gibbons, G. W., Hawking, S. W. “Cosmological Event Horizons...” _Physical Review D_, 1977.|Cosmological horizons. ([APS Links](https://link.aps.org/doi/10.1103/PhysRevD.15.2738?utm_source=chatgpt.com "Cosmological event horizons, thermodynamics, and particle ..."))|GR/cosmology anchor.|Useful|
|Bousso, R. “The Holographic Principle.” _Reviews of Modern Physics_, 2002.|Holography/horizon caveats. ([APS Links](https://link.aps.org/doi/10.1103/RevModPhys.74.825?utm_source=chatgpt.com "The holographic principle \| Rev. Mod. Phys. - APS Journals"))|Black holes stress-test section.|Useful|
|Brandão, F. et al. “Resource Theory of Quantum States Out of Thermal Equilibrium.” _Physical Review Letters_, 2013.|Thermodynamic resource theory. ([APS Links](https://link.aps.org/doi/10.1103/PhysRevLett.111.250404?utm_source=chatgpt.com "Resource Theory of Quantum States Out of Thermal Equilibrium"))|Thermodynamic Cap.|Essential|
|Seifert, U. “Stochastic Thermodynamics...” _Reports on Progress in Physics_, 2012.|Work, heat, entropy production on trajectories. ([arXiv](https://arxiv.org/abs/1205.4176?utm_source=chatgpt.com "Stochastic thermodynamics, fluctuation theorems, and ..."))|Time/thermodynamic arrow.|Essential|
|Thouless, Kohmoto, Nightingale, den Nijs. “Quantized Hall Conductance...” _Physical Review Letters_, 1982.|Topological response invariant. ([APS Links](https://link.aps.org/doi/10.1103/PhysRevLett.49.405?utm_source=chatgpt.com "Quantized Hall Conductance in a Two-Dimensional Periodic ..."))|Topological response.|Useful|
|Hasan, M. Z., Kane, C. L. “Colloquium: Topological Insulators.” _Reviews of Modern Physics_, 2010.|Protected edge/surface modes. ([APS Links](https://link.aps.org/doi/10.1103/RevModPhys.82.3045?utm_source=chatgpt.com "Colloquium: Topological insulators \| Rev. Mod. Phys."))|Topological response.|Useful|
|Wilson, K. G., Kogut, J. “The Renormalization Group and the ε Expansion.” _Physics Reports_, 1974.|RG/coarse-graining. ([PhilPapers](https://philpapers.org/rec/WILTRG-3?utm_source=chatgpt.com "The renormalization group and the ϵ expansion"))|EFT/RG absorber.|Essential|
|Polchinski, J. “Effective Field Theory and the Fermi Surface.” 1992.|EFT as preservation of low-energy predictive structure. ([arXiv](https://arxiv.org/abs/hep-th/9210046?utm_source=chatgpt.com "Effective Field Theory and the Fermi Surface"))|EFT/RG bridge.|Useful|
|Nakahara, M. _Geometry, Topology and Physics_.|Fiber bundles/gauge geometry. ([Google Books](https://books.google.com/books/about/Geometry_Topology_and_Physics_Second_Edi.html?id=cH-XQB0Ex5wC&utm_source=chatgpt.com "Geometry, Topology and Physics, Second Edition"))|Gauge invariance / Standard Model caution.|Useful|
|Weinberg, S. _The Quantum Theory of Fields_, Vol. II.|Gauge theory, non-Abelian symmetry, Standard Model structure. ([INSPIRE](https://inspirehep.net/literature/430948?utm_source=chatgpt.com "The quantum theory of fields. Vol. 2: Modern applications"))|Standard Model constraints.|Useful|
|Sen, A. _Commodities and Capabilities_. 1985.|Capability approach. ([Amartya Sen](https://sen.scholars.harvard.edu/publications/commodities-and-capabilities?utm_source=chatgpt.com "Commodities and Capabilities - Amartya Sen"))|Economics/agency absorber.|Useful|
|Gibson, J. J. _The Ecological Approach to Visual Perception_. 1979.|Affordances. ([Taylor & Francis](https://www.taylorfrancis.com/books/mono/10.4324/9781315740218/ecological-approach-visual-perception-james-gibson?utm_source=chatgpt.com "The Ecological Approach to Visual Perception \| Classic Edition"))|Affordance/capability language.|Useful|
|Friston, K. “The Free-Energy Principle.” _Nature Reviews Neuroscience_, 2010.|Active inference / free-energy principle. ([Nature](https://www.nature.com/articles/nrn2787?utm_source=chatgpt.com "The free-energy principle: a unified brain theory?"))|Emergence/agency section.|Optional|
|Sutton, R. S., Barto, A. G. _Reinforcement Learning_, 2nd ed. 2018.|Policies, value, options/action spaces. ([MIT Press](https://mitpress.mit.edu/9780262039246/reinforcement-learning/?utm_source=chatgpt.com "Reinforcement Learning"))|RL policy-space `K`.|Useful|
|Abramsky, S., Brandenburger, A. “The Sheaf-Theoretic Structure of Non-Locality and Contextuality.” 2011.|Local-to-global obstruction. ([arXiv](https://arxiv.org/abs/1102.0264?utm_source=chatgpt.com "The Sheaf-Theoretic Structure Of Non-Locality and Contextuality"))|Sheaf/category appendix.|Essential|
|Pearl, J. _Causality_. Cambridge, 2000/2009.|Observational vs interventional equivalence. ([ILLC Archive](https://archive.illc.uva.nl/cil/uploaded_files/inlineitem/Pearl_2009_Causality.pdf?utm_source=chatgpt.com "Causality : models, reasoning, and inference"))|Causal inference absorber.|Essential|
|Odling-Smee, Laland, Feldman. _Niche Construction_. Princeton, 2003.|Niche construction / platform capability. ([University of St Andrews Research Portal](https://research-portal.st-andrews.ac.uk/en/publications/niche-construction-the-neglected-process-in-evolution/?utm_source=chatgpt.com "Niche construction: the neglected process in evolution"))|Emergence section.|Useful|
|Hoel, E. “When the Map Is Better Than the Territory.” _Entropy_, 2017.|Causal emergence. ([Swarma](https://qiniu.pattern.swarma.org/attachment/%E5%BC%A0%E6%B1%9F%26%E8%A2%81%E5%86%B0-%E6%B6%8C%E7%8E%B0%E3%80%81%E5%9B%A0%E6%9E%9C%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0.pdf?utm_source=chatgpt.com "Emergence, Causality, and Artificial Intelligence"))|Emergence section.|Optional|

---

## G. Red Flags

Do **not** let these phrasings into v0.6:

1. “Projection insufficiency is new.”
    
2. “Capability Projection proves a physics thesis.”
    
3. “Capability explains physics.”
    
4. “Same local reduced state means same physical state.”
    
5. “A strictly local observer has access to global entanglement capability.”
    
6. “Dark matter is projection insufficiency.”
    
7. “Dark energy is capability loss.”
    
8. “Time is capability” without “along physical time.”
    
9. “Capability spread cardinality measures severity” in continuous, metric, preorder, or stochastic cases.
    
10. “Minimal quotient” without specifying the allowed morphisms/equivalences.
    
11. “State enrichment is cheating.” It is not cheating when the neighboring theory legitimately includes that state.
    
12. “Cap can be any future-relevant object.” It must be typed, native, operationally meaningful, and fixed before witness construction.
    
13. “Nonfaithful” unless a categorical faithful-functor condition is actually present.
    
14. “Gauge-dependent capability” unless the gauge choice is physically fixed by the access profile.
    

---

## H. Safe Strong Wording

These are bold but defensible:

- “Capability Projection is projection sufficiency for typed capability objects.”
    
- “Non-factorization is not the discovery; the audit discipline is the proposed research instrument.”
    
- “A projection is capability-sufficient exactly when the declared capability object is constant over visible-equivalence fibers.”
    
- “Every witness must earn its type signature.”
    
- “Absorption is an outcome, not an embarrassment.”
    
- “The default expectation is translation or heuristic residue, with canonical residue reserved for rare cases that survive native state completion and native theorem absorption.”
    
- “Physics enters only through known physics inducing a typed capability object under declared access and allowed operations.”
    
- “The strongest next target is not another pair of states, but a minimality theorem, canonical enrichment family, or cross-domain transfer theorem.”
    

---

## Terminology Decisions

|Term|Decision|
|---|---|
|capability-sufficient projection|Keep.|
|capability-insufficient projection|Keep.|
|projection-sufficiency failure|Keep; define as non-factorization after declared equivalence.|
|capability spread|Keep, but define as “fiber image of `Cap` modulo native comparison.”|
|minimal capability-preserving quotient|Rename default to **capability-kernel quotient**; keep old phrase as gloss.|
|state-enrichment absorption|Rename to **native state completion**.|
|native-theory absorption|Rename to **native theorem absorption**.|
|translation residue|Keep; maybe rename to **translation/schema residue** if more precision is desired.|
|heuristic residue|Keep.|
|formal residue|Rename to **formal audit residue**.|
|canonical residue|Keep, but make rare/high-bar.|
|no-free-physics rule|Keep. It is one of the strongest parts of v0.5.|
|same-neighbor-data condition|Keep, but define sharply: the neighboring theory must be granted all state variables, operations, equivalences, and access structures it normally treats as legitimate.|

---

## I. Proposed v0.6 Outline

1. **Status and Non-Claim Boundary**
    
    - Not canon, not paper-ready, not physics evidence.
        
    - “Observable equivalence is not capability equivalence” is old.
        
2. **North Star Statement**
    
    - Projection sufficiency for typed capability objects.
        
    - Strongest governing sentence.
        
3. **Formal Core: Equivalence-Valued Case**
    
    - `A ⊆ Y`, `pi`, `Cap`, `~=_X`, `~=_K`.
        
    - Default target `K / ~=_K`.
        
    - Fiber-constancy lemma over visible-equivalence fibers.
        
    - Capability-kernel quotient.
        
4. **Native Comparison Appendix**
    
    - Preorders, metrics, tolerances, stochastic objects, category-valued objects.
        
5. **Capability Spread**
    
    - Definition.
        
    - Singleton criterion.
        
    - Domain-native summaries.
        
6. **Operational Capability Gate**
    
    - `K`, `Cap`, native test, equivalence, controls, non-gerrymandering.
        
7. **Absorption Protocol**
    
    - Native state completion.
        
    - Native theorem absorption.
        
    - Equivalence repair.
        
    - Approximation-threshold absorption.
        
    - Gauge/representation absorption.
        
8. **Residue Ladder**
    
    - Canonical, formal audit, typed toy-model, translation/schema, heuristic, demoted.
        
9. **Witness Ledger**
    
    - Vector/ANN.
        
    - QRT.
        
    - Next witness queue.
        
10. **Physics Grounding**
    

- No-Free-Physics Rule.
    
- Main anchors: QRT, GR causal accessibility, thermodynamic resource theory.
    
- Secondary anchors: detector provenance, topological response, EFT/RG.
    
- Held/narrowed: Standard Model, black holes, time, emergence.
    
- Demoted: dark matter/dark energy.
    

11. **Citation Map**
    

- Canonical prior art with insertion points.
    

12. **Collapse Condition**
    

- If absorbed everywhere, record translation/heuristic residue or demotion.
    

---

## J. Proposed v0.6 Core Text

> **Capability Projection is projection sufficiency for typed capability objects.**  
> Fix an observer or access profile `O`, observational schema `Sigma`, resolution `r`, domain `U`, task family `T`, horizon `h`, and resource boundary `B`. Let `A ⊆ Y` be the admissible source states. Let
> 
> ```text
> pi : A -> X
> Cap : A -> K
> ```
> 
> and declare visible comparison `~=_X` and native capability comparison `R_K`.
> 
> In the equivalence-valued case, where `R_K` is `~=_K`, the projection is capability-sufficient iff there exists
> 
> ```text
> Cbar : im(A -> X / ~=_X) -> K / ~=_K
> ```
> 
> such that
> 
> ```text
> Cbar([pi(y)]_{~=_X}) = [Cap(y)]_{~=_K}
> ```
> 
> for every admissible `y`.
> 
> Equivalently:
> 
> ```text
> pi(y1) ~=_X pi(y2)  =>  Cap(y1) ~=_K Cap(y2)
> ```
> 
> for all admissible `y1,y2`.
> 
> For metric, preorder, stochastic, approximate, or category-valued capability objects, replace quotient equality with the native comparison: bounded fiber diameter, mutual convertibility, risk/deficiency bound, coupling/distance criterion, or categorical equivalence.
> 
> Non-factorization is not novelty evidence. It triggers an absorption audit. First grant neighboring theories their legitimate state variables and native theorems. A witness earns formal or canonical residue only if it survives native state completion, native theorem absorption, equivalence repair, approximation-threshold absorption, and gauge/representation absorption.
> 
> Physics enters only by deriving `Y`, `X`, `pi`, allowed operations, access profile, and `Cap` from known physics, then auditing projection sufficiency. Capability language does not derive physics.
> 
> If all important witnesses are absorbed by mature neighboring frameworks and no minimality, canonical enrichment, executable audit suite, or transfer theorem remains, record translation residue, heuristic residue, redundancy, or demotion. The purpose is discovery, not defense.

---

## K. Concrete Next Research Actions

1. **Patch the formal core first.** Change the default target to `K / ~=_K`; add admissible subset `A`; rewrite the fiber lemma over visible-equivalence fibers.
    
2. **Write the native-comparison appendix.** Include separate treatments for equivalence, preorder, metric/tolerance, probabilistic, decision-theoretic, resource-theoretic, and categorical `K`.
    
3. **Upgrade the Capability Type Gate into an Operational Capability Gate.** Require native test, controls, non-gerrymandering check, and predeclared equivalence.
    
4. **Run QRT Witness 2.** Same local reduced state, different global resource capability, with access profiles `O_A`, `O_AB`, LOCC, catalyst, purifier/environment access. Expected result: translation residue, but a strong access-profile template.
    
5. **Run GR causal accessibility witness.** Use simple models first: Minkowski causal diamonds, Rindler horizon, Schwarzschild exterior, de Sitter horizon. Define `Cap` as causal accessibility or reconstructability.
    
6. **Run thermodynamic resource witness.** Same coarse macrostate, different work-extraction or thermal convertibility capability. Expect absorption by thermodynamic resource theory; useful typed physics anchor.
    
7. **Run database minimality theorem attempt.** For a workload `W`, view set `V`, provenance/log/index state `E`, ask whether `(V,E)` is minimal for preserving query/provenance/replay capability.
    
8. **Run process semantics absorption comparison.** Instantiate `Cap` as future tests passed. Expect absorption by testing equivalence, failure semantics, bisimulation, or Nerode quotient.
    
9. **Build a small executable witness suite.** Include one positive preservation control and one negative non-factorization fixture for ANN, database views, POMDP belief states, QRT, and process semantics.
    
10. **Attempt the cross-domain transfer theorem.** Candidate theorem: “For any typed capability object with declared native comparison, projection sufficiency is equivalent to singleton or bounded capability spread over visible-equivalence fibers.” This is mathematically simple, but valuable if it produces a reusable audit template across statistics, databases, process semantics, QRT, and control.
    
11. **Move dark matter and dark energy out of the main text.** Keep one appendix line: “May be revisited only as typed gravitational/cosmological accessibility audits.”
    
12. **Make the citation layer part of the repo contract.** Every promoted witness should include: native absorber citations, state-enrichment test, native theorem test, control cases, residue label, and falsification/demotion condition.