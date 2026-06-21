# Prior Art And Physics Grounding For Capability Projection

## Executive summary

This memo takes the uploaded North Star brief as the governing scope: it treats the note as a speculative research program, not as a theorem, and asks which existing traditions already formalize cases where the same visible readout fails to determine future action, control, convertibility, intervention response, or global reconstruction. fileciteturn0file0

The short verdict is that the core pattern is **not naïve**. It is already native to at least eight mature traditions. In POMDPs, an observation does not determine optimal action; the sufficient object is the **belief state** or history-compression, not the raw observation. In decision theory and statistics, a projection can be **insufficient** for the relevant decision problem, while Blackwell’s comparison of experiments formalizes when one information structure is strictly more decision-useful than another. In control theory, non-observable latent distinctions can matter for future control and estimation. In bisimulation and state abstraction, quotienting states is valid only when future behavior is preserved; otherwise the abstraction collapses dynamics that matter. In resource theories, the key issue is not visible sameness but **convertibility under allowed operations**. In sheaf-theoretic settings, local compatibility does not guarantee global extension. In causal inference, observational equivalence does not entail interventional equivalence. In Koopman/operator theory, what one can infer depends on the chosen observable algebra, and finite observable families can miss relevant latent dynamics. citeturn21search1turn35search4turn26search8turn19search6turn23academia0turn0academia0turn24search8turn25academia2

The cleanest technically literate way to state the North Star is therefore not “capability-nonfaithful.” In category theory, **faithful** already has a precise meaning: injective on hom-sets. That is not the same as “observer-visible state fails to determine capability.” The safer prose replacement is **capability-nondetermining projection** or **capability-insufficient projection**. The formally strongest compact sentence is still the one already in the brief: for fixed observer/access profile \(O\), task family \(T\), and horizon \(h\), **\(C_{O,T,h}\) does not factor through \(\pi\)**. citeturn33search3turn33search0turn33search4

On mathematical structure, the least overcommitted but still useful choice for `Cap` is **an indexed preorder**, optionally accompanied by a viability-filtered reachable set. In plain English: from each rich state \(y\), define which future operations or transformations are admissible, and order them by convertibility, dominance, or reachability. That choice is expressive enough to connect to resource theories, opportunity sets, viability kernels, and control/reachability, while avoiding the premature burden of committing to full categorical composition laws. If the project matures, the next upgrade is an **indexed category** or **resource theory** over \((O,T,h)\), but starting there now would look overfitted. citeturn23academia0turn23academia3turn17search4turn17academia3

The physics sections can be kept, but only if they are aggressively quarantined as **analogies**. General relativity genuinely provides a language of causal accessibility, light cones, causal futures \(J^+(p)\), horizons, and global hyperbolicity. That is enough to justify language like “geometry constrains future accessibility.” It is **not** enough to say gravity *is* capability. Dark matter is a good analogy for projection insufficiency because visible baryonic structure does not determine all gravitationally relevant structure. Dark energy is a decent analogy for separating local visible content from global accessibility geometry, but its microphysics remains unsettled as of mid-2026. Black holes are especially useful because horizons are observer-indexed causal boundaries and naturally raise questions about which signals, reconstructions, or verifications remain possible for which observer. Electrons, charge, spin, and selection rules justify a weaker claim still: physical structure constrains allowed interactions. Time should be handled most carefully; the safe statement is that your proposed “future-operation observable” tracks something **along physical time**, not instead of time. Emergence is best grounded using viability, affordances, niche construction, major transitions, and constructor-theoretic talk about possible and impossible transformations. citeturn10academia0turn10academia1turn11search4turn34academia2turn7academia1turn5academia1turn27academia0turn31news0turn28search6turn29academia1turn9academia0turn16search5turn14search5turn16search7turn36academia1turn17search4turn37academia4turn18academia3turn37search0turn17academia3

The most important hostile conclusion is this: if all cases you care about reduce cleanly to existing machinery such as belief-state sufficiency, observability, reachability, Blackwell order, resource convertibility, causal identifiability, or provenance, then the North Star adds no mathematical structure and survives only as branding. The note becomes worth keeping only if `Cap` is typed tightly enough that failure of factorization through \(\pi\) becomes a non-vacuous, testable property rather than an almost tautological restatement of “hidden things matter.” That is the central open problem. citeturn21search1turn26search8turn35search4turn23academia0turn24search8turn17search4

## Methodology And Assumptions

This memo follows the user’s uploaded brief on scope, tone, and deliverables. It therefore prioritizes primary papers, standard references, major reviews, and authoritative scientific summaries from roughly the last decade while keeping older seminal work where it is load-bearing to the argument. The brief also explicitly asks that the physics sections be grounded rather than removed, and that the result distinguish analogy from overclaim. fileciteturn0file0

A practical limitation is that some canonical older sources are more readily available on the public web through abstracts, authoritative review summaries, or reference pages than through fully accessible scans of the original journal article. Where that happened, this memo relies on the best accessible combination of original-paper abstracts, standard review papers, and recognized reference-text summaries. This is acceptable for a research memo aimed at technical literacy, but it does mean some citations point to abstracts or standard reference summaries rather than page-scanned originals. citeturn10academia0turn23academia0turn25academia2turn29academia1

The core assumption throughout is that your intended object \(C_{O,T,h}(y)\) is **observer-indexed, task-indexed, and horizon-indexed**. That indexing matters. Without it, “capability” becomes so broad that almost every latent distinction becomes relevant, and the project collapses into an unhelpful truism. With the indexing fixed, the question becomes sharper: does the visible readout \(x=\pi(y)\) determine the admissible or dominant future operations for that observer, task family, and horizon? In many established formalisms, the answer is already “not always.” citeturn21search1turn35search4turn26search8turn24search8

```mermaid
flowchart LR
    Y1[rich state y1 in Y] --> PI[projection π]
    Y2[rich state y2 in Y] --> PI
    PI --> X[visible state x in X]
    Y1 --> L1[belief / latent dynamics / convertibility]
    Y2 --> L2[belief / latent dynamics / convertibility]
    L1 --> C1[C_O,T,h(y1)]
    L2 --> C2[C_O,T,h(y2)]
    X -. may fail to determine .-> C1
    X -. may fail to determine .-> C2
```

The diagram above is only a conceptual summary, but it matches how multiple existing traditions separate visible state from decision-relevant, control-relevant, or intervention-relevant latent structure. citeturn21search1turn26search8turn35search4turn24search8turn25academia2

## Prior Art Map For The Core Mathematical Pattern

The table below compresses the strongest technical neighbors. The important pattern is not merely “hidden state exists.” It is stronger: **a coarse readout can fail to determine the future-relevant object** for action, convertibility, control, or reconstruction.

| Tradition | Canonical anchors | Technical concept | How it matches \(\pi(y_1)=\pi(y_2)\) but \(C(y_1)\neq C(y_2)\) | What it absorbs | Residue and safe wording |
|---|---|---|---|---|---|
| Partial observability | Åström’s incomplete-state control framework and the modern POMDP formulation; belief states are sufficient, raw observations are not. citeturn21search1turn21search4 | Belief-state sufficiency | Same observation can correspond to multiple latent states with different optimal actions or values; the policy depends on the belief/history, not the observation alone. citeturn21search1turn21academia0 | A large chunk of “same visible state, different future affordance” in agent settings | Safe wording: “The visible readout can be insufficient for sequential decision; future-relevant capability may depend on latent belief state.” citeturn21search1turn21academia0 |
| Sufficient statistics and Blackwell order | Sufficiency and Rao–Blackwellization; Blackwell informativeness and the BSS tradition. citeturn22search1turn35search7turn35search4turn35academia2 | Statistic sufficiency; comparison of experiments | A projection can preserve some information while losing decision-relevant distinctions; one experiment/readout can dominate another for all decision problems. citeturn35search4turn22search1 | Static decision-theoretic versions of the note | Residue: your notion is horizon-indexed and dynamic. Safe wording: “\(\pi\) can be insufficient for the decision problem at hand; more informative readouts need not change appearance while changing action quality.” citeturn35search4turn22search1 |
| Control and observability | Kalman observability; Kalman decomposition; nonlinear observability via Hermann–Krener. citeturn26search8turn26search5turn26search4 | Output does not always determine internal state | Two latent states can produce identical outputs while differing in future controllability, estimability, or reachable behavior. citeturn26search8turn26search5turn26search6 | Dynamical and control-relevant instances of projection loss | Safe wording: “Observer-visible output can fail to determine the control-relevant latent state.” citeturn26search8turn26search6 |
| Bisimulation and state abstraction | Standard bisimulation, modern RL abstraction, causal bisimulation. citeturn19search6turn19academia1turn19academia0 | Quotienting that preserves future behavior | If an abstraction merges states that are not bisimilar, it destroys reward/dynamics structure that matters for the future. citeturn19search6turn19academia1 | A direct formal neighbor to “capability-preserving quotient” | Safe wording: “Only some projections preserve future behavior; bad abstractions merge states with divergent future options.” citeturn19academia1turn19academia3 |
| Resource theories | Quantum resource theories; convertibility under restricted operations. citeturn23academia0turn23academia3turn23academia1 | Free operations and convertibility preorder | Two states that look similar under a coarse descriptor need not be interconvertible under allowed operations; the key object is not appearance but transformation under constraints. citeturn23academia0turn23academia1 | The strongest home for “capability as allowed transformation” | Residue: your indexing by observer/task/horizon is broader than standard quantum resource settings. Safe wording: “Capability is often best treated as constrained convertibility rather than as visible state.” citeturn23academia0turn23academia3 |
| Sheaf theory and local-to-global obstruction | Abramsky–Brandenburger and later cohomological work. citeturn0academia0turn0academia1 | Compatible local sections without global section | Local consistency on observed overlaps does not imply existence of a single global assignment. citeturn0academia0turn0academia1 | The best “global capability may fail to glue from local visibility” analogy | Residue: unless your note has explicit covering/gluing structure, keep this as a mathematical neighbor, not a claimed reduction. Safe wording: “Local agreement of observables can fail to determine globally realizable structure.” citeturn0academia0 |
| Koopman and operator-theoretic dynamics | Modern Koopman review; time-delay observables. citeturn25academia2turn25academia0 | Dynamics in observable-function space | What you can reconstruct depends on the chosen observable family; finite observable sets can miss the coordinates needed for faithful dynamical representation. citeturn25academia2turn25academia0 | Measurement-choice versions of projection loss | Safe wording: “Observable coordinates may fail to capture the latent dynamics needed for prediction or control.” citeturn25academia2 |
| Causal inference and SCMs | Pearl’s SCM framework, do-calculus, ancestral graphs with latent confounding. citeturn24search8turn19search7turn24search9 | Observational vs interventional equivalence | The same observational distribution can arise from structures with different answers to intervention queries, especially under latent confounding or Markov equivalence. citeturn24search8turn19search7turn24search9 | The cleanest analogy for “appearance does not determine manipulability” | Safe wording: “Observed regularities need not determine intervention-relevant structure.” citeturn24search8turn24academia3 |

The pattern across these traditions is consistent: the note’s core claim is most defensible when it is framed as a statement about **failure of sufficiency** under a specific projection. Once stated that way, the point is no longer exotic. The real question becomes which notion of sufficiency or preservation is intended: decision sufficiency, control sufficiency, bisimulation sufficiency, convertibility sufficiency, gluing sufficiency, or intervention sufficiency. citeturn22search1turn21search1turn26search8turn19academia1turn23academia0turn0academia0turn24search8

That is why the most technically literate summary sentence is not a physics sentence at all. It is this: **for fixed \((O,T,h)\), the relevant capability object need not be a function of the observer-visible readout alone**. Or, more compactly, **\(C_{O,T,h}\) need not factor through \(\pi\)**. citeturn21search1turn35search4turn24search8turn33search3

## Naming And Best Candidate Structures For Cap

The collision with category theory is real. A **faithful functor** is, by definition, injective on hom-sets. That usage is standard and entrenched. Calling a projection “capability-nonfaithful” therefore invites a technical reader to ask the wrong question immediately: “faithful with respect to which category and which morphisms?” If your actual intended claim is that visible state does not determine the capability object, then **capability-nondetermining projection** is the cleanest prose label, with **capability-insufficient projection** as a strong alternative when you want a statistical or decision-theoretic flavor. citeturn33search3turn33search0turn33search4

The next issue is the type of `Cap`. Here the note should be more disciplined than ambitious.

| Candidate structure for `Cap` | What it means | Natural notion of capability equivalence | Strengths | Main risk |
|---|---|---|---|---|
| Set of admissible operations | Plain opportunity set | Equality of sets | Minimal commitment; easy to explain | Too extensional; misses dominance, cost, composition, constraints |
| Preorder of admissible transformations | Operations ordered by reachability, dominance, or convertibility | Mutual reachability or equivalence in the preorder | Best early-stage fit; aligns with resource theory and opportunity-set language | Still weak on composition and multi-step structure |
| Viability-filtered reachable set | States/actions reachable while respecting constraints | Equality of viability kernels or reachable sets | Strong link to control, viability, and horizon dependence | Geometric and task-specific; less compositional |
| Category of operations | Objects are states/resources; morphisms are admissible transformations | Isomorphism or equivalence in the category | Captures composition explicitly | Overcommitted too early; category choices will look arbitrary |
| Enriched category | Adds costs, probabilities, metrics, or orders to morphisms | Enriched isomorphism / equivalence | Powerful once metrics or graded access matter | Too heavy for a North Star note unless there is real data or formal development |
| Indexed/fibered structure over \((O,T,h)\) | `Cap` varies systematically with observer, task, horizon | Fiberwise equivalence, possibly with reindexing maps | Best reflection of the brief’s observer/task/horizon indexing | Requires more notation, but the gain is real |
| POMDP or belief-state object | Capability represented by policies and value over beliefs | Policy/value equivalence under the belief MDP | Excellent for agentic and sequential settings | Too narrow if the note aims beyond planning under uncertainty |

The least overcommitted mathematically useful recommendation is therefore:

**Use `Cap` first as an indexed preorder, optionally paired with a viability-filtered reachable set.**
This choice absorbs the resource-theory intuition of convertibility, the control-theory intuition of reachable futures, and the opportunity-set intuition of admissible actions, while still letting you say something sharp about equivalence and projection loss. citeturn23academia0turn17search4turn26search5

If you want one sentence to put into the note, use this:

> For fixed observer/access profile \(O\), task family \(T\), and horizon \(h\), let \(Cap_{O,T,h}(y)\) be an indexed preorder of admissible future operations, optionally realized as a viability-filtered reachable set. The central question is whether this preorder factors through the observer-visible projection \(\pi:Y\to X\). citeturn23academia0turn17search4turn21search1

The **central open problem** is also now clearer:

> The central open problem is not whether capability can be named, but which mathematical structure on `Cap` makes capability equivalence, projection loss, and absorption by existing theories testable rather than rhetorical.

That framing is strong because it admits failure. If `Cap` ends up reducing to a plain belief state, a resource preorder, a viability kernel, or a causal intervention class, then the North Star should concede that and stop pretending it discovered a new ontology. citeturn21search1turn23academia0turn17search4turn24search8

## Citation Backed Physics Grounding

The safe way to keep the physics material is to mark each section as **analogy only**, then be precise about what the underlying physics actually says.

**Gravity.** In general relativity, light cones define causal accessibility, \(J^+(p)\) is the causal future of an event, and globally hyperbolic spacetimes admit Cauchy surfaces and smooth time functions; this is exactly why causal structure is the right vocabulary for “which futures can be reached or influenced.” Causal structure is also conformally robust in the standard Lorentzian sense. citeturn28search4turn11search4turn28search8turn10academia0turn10academia1
**Safe analogy:** geometry constrains future accessibility and possible trajectories; if capability includes reachable future operations, gravity constrains capability.
**Overclaim boundary:** do **not** say gravity *is* capability, or that causal futures are identical to your \(Cap\) object. GR concerns causal structure and geodesic/field evolution, not an observer-indexed operational preorder in your sense. citeturn28search4turn10academia0

**Dark matter.** The case for dark matter rests on converging evidence including galactic dynamics, gravitational lensing, and merging-cluster systems such as the Bullet Cluster and MACS J0025.4-1222, where baryonic gas and lensing-inferred mass peaks separate. In the standard cosmological fit, dark matter remains a major matter component. citeturn34academia1turn34academia2turn7academia1turn27academia0
**Safe analogy:** electromagnetically visible structure does not determine all gravitationally relevant structure.
**Overclaim boundary:** do **not** say dark matter is “hidden capability” or that the analogy supports any new ontological claim about agency. It supports only the weaker slogan that visible structure can underdetermine dynamically relevant structure. citeturn34academia1turn34academia2

**Dark energy.** The 1998 supernova result established accelerated cosmic expansion, the standard flat \(\Lambda\)CDM fit still works very well in Planck 2018 cosmology, and recent years have added some tension: DESI analyses in 2025 hinted that dark energy may evolve, while a June 2026 supernova analysis reaffirmed that expansion is still accelerating. Event horizons in accelerating cosmologies are standard causal notions. citeturn5academia1turn27academia0turn27news2turn31news0turn31search13
**Safe analogy:** dark energy motivates separating local visible matter content from the large-scale geometry that governs future accessibility.
**Overclaim boundary:** do **not** suggest that “capability explains dark energy,” or that dark energy has a settled microphysical interpretation. It does not. As of June 2026, acceleration is supported, but the nature and possible evolution of dark energy remain active research questions. citeturn31news0turn27news2turn27academia0

**Black holes.** Event horizons are causal boundaries. Classical black holes are constrained by no-hair results in standard settings; black hole thermodynamics gives Bekenstein–Hawking entropy and Hawking radiation, while the information problem remains unresolved in consensus terms. This is exactly the right place to discuss observer-indexed access: which signals can escape, which correlations are recoverable, and which reconstructions are available from infinity versus behind a horizon. citeturn28search6turn9academia0turn9search6turn30search5turn29academia1
**Safe analogy:** black holes are stress tests for observer-relative future operations and verification possibilities.
**Overclaim boundary:** do **not** imply that the note resolves the information paradox, explains entropy, or licenses complementarity/firewall claims unless you are explicitly reviewing competing proposals. citeturn29academia1turn8search15

**Electrons and physical structure.** Electric charge is a coupling quantum number in the electroweak story, spin is an intrinsic angular-momentum property, and observable behavior is sharply constrained by interaction structure and selection rules. Even simple atomic selection rules show that not every formally imaginable transition is physically allowed. citeturn16search5turn14search5turn16search7
**Safe analogy:** charge, spin, and related structure constrain the repertoire of allowed interactions; in that limited sense they constrain future operation structure.
**Overclaim boundary:** do **not** reduce charge, spin, or mass to “capability.” These are physical properties in established theory, not operational sets in your new notation. citeturn16search5turn14search5

**Time.** In relativity, causal order is built into spacetime structure. In thermodynamics and nonequilibrium physics, the arrow of time is linked to irreversibility and entropy production. Your note can safely add a second bookkeeping layer: along physical time, projected visible state may stand still while future-operation structure changes inside a projection fiber. citeturn10academia1turn28search4turn36academia1turn36academia3
**Safe analogy:** capability can be tracked as an additional observable along time, without replacing physical time.
**Overclaim boundary:** do **not** say observers create time, or that capability is more fundamental than spacetime without a very different and much stronger argument. citeturn10academia1turn36academia1

**Emergence.** Viability theory formalizes persistence under constraints; affordance language formalizes perceived possible actions; niche construction and major transitions in evolution show how structures become platforms for further organization; constructor theory makes “possible versus impossible transformations” a literal explanatory primitive. That makes emergence the best home for your most ambitious but still defendable analogy. citeturn17search4turn37academia4turn18academia3turn37search0turn17academia3turn17academia0
**Safe analogy:** emergent structures can be modeled as structures that preserve, enlarge, or stabilize admissible future transformations.
**Overclaim boundary:** do **not** assert that all emergence is reducible to capability expansion; many emergent descriptions also track scale separation, organization, coarse-graining, or new control parameters. citeturn17search4turn37search0turn17academia3

## Suggested Revised Wording For The Physics Sections

Below are paste-ready paragraphs that preserve the intuition while keeping the claims bounded.

**Gravity**

> In general relativity, spacetime geometry constrains causal accessibility: light cones, causal futures, geodesics, and horizons determine which events can influence which others and which trajectories remain available from a given event. In that limited and explicitly analogical sense, if a capability concept is meant to track reachable future operations, gravity constrains capability by constraining causal accessibility. This is not a claim that gravity is capability, only that general relativity supplies a rigorous language for future accessibility under geometric constraints. citeturn28search4turn28search8turn10academia0turn10academia1

**Dark matter**

> Dark matter provides a disciplined analogy for projection insufficiency. Electromagnetically visible structure does not determine all gravitationally relevant structure: lensing maps and merging-cluster systems show that baryonic matter distributions can fail to recover the full mass distribution governing dynamics. The point of the analogy is only that visible organization can underdetermine future-relevant structure; it is not that dark matter should be reinterpreted as hidden capability. citeturn34academia1turn34academia2turn7academia1

**Dark energy**

> Dark energy motivates a related separation between local visible content and large-scale accessibility geometry. Accelerated expansion changes which regions are in causal contact and, in standard accelerating cosmologies, introduces cosmic event horizons. The analogy is therefore about future accessibility under large-scale geometry, not about explaining dark energy in operational terms. Since the microphysical nature of dark energy remains unsettled, this section should remain explicitly analogical. citeturn5academia1turn27academia0turn31search13turn31news0

**Black holes**

> Black holes are useful as stress tests for observer-indexed future operations. Horizons are causal boundaries, so the relevant question is not merely what state exists “inside,” but which observers can still signal, verify, reconstruct, or influence what. In this sense black holes are natural examples of observer-relative operational boundaries. This framing does not solve the information problem; it only marks black holes as situations where observer-indexed accessibility becomes mathematically unavoidable. citeturn28search6turn29academia1turn9academia0

**Electrons and physical structure**

> Physical properties such as charge and spin do not reduce to capability, but they do constrain allowed interactions. Charge fixes how a particle couples to gauge fields, spin constrains representation-theoretic behavior and measurable response, and selection rules show that not every imaginable transition is admissible. In that limited sense, physical structure constrains the space of available future operations. citeturn16search5turn14search5turn16search7

**Time**

> A projected visible-state trajectory can miss operationally relevant change occurring within a projection fiber. One can therefore track, alongside ordinary time evolution, changes in an observer/task/horizon-indexed future-operation structure. This supplements rather than replaces physical time: relativity and thermodynamics remain the physical frameworks governing temporal order and irreversibility. citeturn10academia1turn36academia1turn36academia3

**Emergence**

> Emergent structures can often be described as structures that preserve, stabilize, or enlarge admissible future transformations. Viability theory formalizes persistence under constraints, affordance theory highlights action possibilities, and major-transition frameworks describe how new organizational levels become platforms for further organization. The proposal here is not that emergence equals capability expansion, but that capability language may offer one useful operational description of some emergent transitions. citeturn17search4turn37academia4turn18academia3turn37search0turn17academia3

## Negative Test And Recommendations

The note **fails** if it cannot survive the following hostile tests.

First, if every example you care about already reduces without residue to existing formalisms such as belief-state sufficiency in POMDPs, state estimation in control, Blackwell comparison of experiments, bisimulation-preserving abstraction, resource convertibility, viability kernels, or causal identifiability, then the North Star adds vocabulary rather than structure. In that case the note should explicitly reframe itself as a unifying lens, not as a novel mathematical primitive. citeturn21search1turn26search8turn35search4turn19academia1turn23academia0turn17search4turn24search8

Second, if `Cap` is left so plastic that it can be retrofitted to any case after the fact, then the project becomes unfalsifiable. A serious version of the note must say what counts as capability equivalence, what data can witness inequivalence, and when \(\pi\) *does* preserve the relevant structure. Those preservation cases matter at least as much as the failures. citeturn22search1turn19academia1turn23academia1

Third, the physics sections should be kept only if they do argumentative work that the formal sections cannot. If they merely repeat “hidden things matter,” they should be moved to an intuition appendix. Their best role is not evidentiary but orienting: they show that modern physics already has hard, non-naïve languages for accessibility, observation loss, horizon-limited reconstruction, and constrained transformation. citeturn28search4turn34academia2turn29academia1turn17academia3

The practical recommendations are straightforward. Use **capability-nondetermining projection** in prose and **\(C_{O,T,h}\) does not factor through \(\pi\)** for formal statements. Model `Cap` first as an **indexed preorder**, optionally realized via **viability-filtered reachable sets**. Open the note with the prior-art trinity that is hardest to dismiss—**POMDPs, observability/control, and resource convertibility**—before touching physics. Then mark every physics section with a visible label such as **Analogy only; not a physics claim**. That sequence makes the note technically literate without pretending it has already earned a new ontology. citeturn33search3turn23academia0turn17search4turn21search1turn26search8

## References

### Primary Sources And Seminal Anchors

| Area | Key sources |
|---|---|
| Sequential decision and partial observability | Åström on incomplete-state control and the POMDP lineage; modern POMDP belief-state formulation. citeturn21search4turn21search1 |
| Statistics and decision theory | Sufficiency, Rao–Blackwellization, and Blackwell informativeness/BSS-style comparison of experiments. citeturn22search1turn35search7turn35search4turn35academia2 |
| Control and observability | Kalman observability, Kalman decomposition, Hermann–Krener nonlinear observability. citeturn26search8turn26search5turn26search4 |
| State abstraction | Classical bisimulation plus modern causal/state abstraction work in RL. citeturn19search6turn19academia1 |
| Resource theories | Horodecki–Oppenheim; Gour–Spekkens; modern convertibility results. citeturn23academia0turn23academia3turn23academia1 |
| Sheaf obstruction | Abramsky–Brandenburger and follow-on cohomological obstruction work. citeturn0academia0turn0academia1 |
| Causal inference | Pearl/SCM/do-calculus tradition and ancestral graph work with latent variables. citeturn24search8turn19search7turn24search9 |
| Gravity and causal structure | Bernal–Sánchez on Cauchy surfaces and smooth splitting; standard causal-structure references. citeturn10academia0turn10academia1turn28search8 |
| Cosmology | Riess et al. on acceleration; Planck 2018 cosmological parameters. citeturn5academia1turn27academia0 |
| Black holes | No-hair review, Hawking radiation, black hole thermodynamics, information-loss review. citeturn9academia0turn30search5turn9search6turn29academia1 |

### Reviews And High Value Expository Sources

| Area | Key sources |
|---|---|
| Koopman/operator dynamics | Modern Koopman review and time-delay observable review. citeturn25academia2turn25academia0 |
| Viability, affordances, emergence | Viability-theory overview, RL/affordance reinterpretation, niche-construction and major-transition framing, constructor theory. citeturn17search4turn37academia4turn18academia3turn37search0turn17academia3 |
| Dark matter evidence | Bertone–Hooper–Silk review and Bullet-cluster analyses. citeturn34academia1turn34academia2turn7academia1 |
| Dark energy current status | Planck baseline plus 2025 DESI hints and June 2026 reaffirmation of acceleration. citeturn27academia0turn27news2turn31news0 |
| Black hole information problem | Unruh–Wald review and quantitative review of information recovery directions. citeturn29academia1turn29academia0 |
| Category-theory terminology | Standard summaries of faithful/full/forgetful functors and why “faithful” is overloaded here. citeturn33search3turn33search0turn33search4 |
| Prompt provenance | Uploaded brief defining the task, physics-grounding requirement, and requested output structure. fileciteturn0file0 |
