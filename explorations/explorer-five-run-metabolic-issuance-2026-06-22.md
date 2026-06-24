# Five-Run Metabolic Scaling and Issuance Rate Analysis

**Date:** 2026-06-22
**Evaluating:** Two explorations — metabolic scaling energy-time co-equality and optimal issuance rate curve lambda*(s)
**Method:** Sequential persona passes, each building on previous findings
**Open problem addressed:** `temporal-issuance-source-object-spec.md` — can these explorations supply a nonabsorbed source primitive for mu?

---

## Run 1: Maya Osei — Metabolic Scaling Theorist (#63)

**What previous runs missed:** N/A — first run, chosen because the metabolic scaling explorer is explicitly her domain.

### Understanding

The metabolic scaling explorer applies the West-Brown-Enquist-Moses framework to TaF. The central formal claim is that B ∝ M^{3/4} arises from joint energy-time optimization, not energy alone, and that this applies substrate-independently to biological, electronic, and distributed systems. The exploration proposes mu_M(r) = c · |r|^{3/4} as a candidate source measure and asks whether it survives the same-neighbor-data freeze. The issuance rate explorer then asks whether lambda*(s) = argmax[N - C - K] is the dynamics equation for Ext_S.

### Strongest Insight

The sublinear non-additivity claim for mu_M is genuinely discriminating. Standard absorbers (entropy, counting, Shannon information) are either additive or sub-additive in ways that do not produce superefficiency at scale. A metabolically-scaled measure where mu_M(r1 union r2) < mu_M(r1) + mu_M(r2) AND mu_M(r)/|r| decreases with |r| is a different object from any of the current absorber candidates. The key property is not just sublinearity; it is that the sublinearity arises from the hierarchical branching architecture itself, not from saturation or interference effects that entropy production also captures.

This is potentially the first candidate mu that is structurally motivated rather than just formally distinct.

### Strongest Critique

The exploration conflates two different claims: (a) time is co-equal with energy in the Moses optimization, and (b) this grounds TaF's claim that time is constitutive of events being real. Claim (a) is correct — the 3/4 exponent requires joint optimization. Claim (b) is not licensed by (a). The Moses framework establishes that temporal delivery constraints matter for optimal transport network architecture. It does not establish that time has fundamental ontological status independent of physical substrates. A temporal delivery constraint in a biological organism is a physical delay in ATP diffusion or oxygen transport — this is fully causal, fully physical, and fully compatible with time being an emergent label on causal processes rather than a constitutive primitive.

Stronger: the "time as co-equal optimization constraint" framing may actually undercut TaF. If time is merely an optimization parameter that must be minimized alongside energy, it is precisely the kind of secondary/derived quantity TaF claims to oppose. The optimization constraint IS the energy-time tradeoff — time enters as a cost, not as a constitutive ground.

### Heterodox Next Step

Test whether mu_M produces different same-neighbor-data results from a pure capacity measure. Specifically: hold fixed the causal structure, event count, entropy production, and information state of two systems — one with hierarchical branching topology and one without — and check whether mu_M differs. If mu_M is a function of topology alone (which it is, since 3/4 comes from the branching architecture), it may already be absorbed by the D1RestrictionSystem's transport graph structure, which encodes topology. The topology IS the same-neighbor data when the restriction system structure is matched.

### Theorem/Claim Candidate

**Branching-topology superefficiency theorem (candidate):** For two D1RestrictionSystems with matching causal order, event count, and entropy production but different branching topology, the metabolically-scaled source measure mu_M assigns different values. If and only if the branching topology is not itself absorbed by the restriction system's gluing data G, this constitutes a nonabsorbed mu candidate.

The conditional structure matters: it may turn out that G exactly encodes the branching topology, in which case mu_M is a function of G and is absorbed.

---

## Run 2: Elena Voss — Dynamical Systems Expert (#16)

**What Run 1 missed:** Maya Osei checked whether mu_M is the right formal object. She did not address whether lambda*(s) as a dynamics equation has the right mathematical structure. Run 1 also did not examine whether the toy model dS/dt = a*lambda - b*lambda^2 - c*S has the right dynamical behavior — specifically whether the interior optimum is stable, how the system behaves near the optimum, and what happens at the boundaries of the state space.

### Understanding

I am looking at the optimal issuance rate curve explorer as a dynamics problem. The proposed toy model is a first-order ODE in S with lambda as a control. The claim is that there exists a nonzero finite interior optimum lambda*(s) that maximizes coherent structure formation. Route A (dynamical systems) is my home terrain.

### Strongest Insight

The toy model dS/dt = a*lambda - b*lambda^2 - c*S is a linear controlled ODE with quadratic cost in lambda. This is a standard LQR (Linear-Quadratic Regulator) problem in one state variable. The static optimum lambda* = a/(2b) is not state-dependent — it is a constant. The exploration correctly notes this is the "static special case." The interesting dynamics appear only when K (collapse risk) is state-dependent and nonlinear.

The key dynamical insight the exploration misses: there may be multiple fixed points in the (S, lambda) phase portrait. At low lambda, S declines (insufficient structure formation). At the static optimum, S reaches a steady state S* = a*lambda*/c = a^2/(2bc). At high lambda, S also reaches a steady state but with high coherence cost — unless K grows faster than N-C, in which case the system can have an UNSTABLE high-lambda fixed point that looks like a viable optimum but produces catastrophic collapse under perturbation. This is the canonical pitchfork bifurcation scenario.

**The bifurcation structure is load-bearing.** The claim that there is a "nonzero finite interior optimum" needs to distinguish between: (a) a stable interior fixed point — genuinely optimal, (b) a saddle point — locally optimal but globally unstable, and (c) a maximum on a monotone curve — the apparent optimum is a boundary. Only (a) supports the Optimal Issuance Rate Curve Hypothesis as stated.

### Strongest Critique

The exploration lists three possible outcomes (1: no lambda*(s), 2: lambda*(s) exists but monotone, 3: interior optimum exists). But it does not ask whether the interior optimum, if it exists, is a stable fixed point of the dynamics or merely the argmax of a snapshot functional. These are different questions. A dynamical system can have an interior argmax of N-C-K that is not a fixed point — the system passes through it and does not stay there. The hypothesis as stated conflates the optimization landscape with the dynamics.

More seriously: if S itself appears in N and C (which it must if the system has feedback), the optimization is not static — it is a Hamiltonian boundary-value problem (Pontryagin). The toy model suppresses this by treating lambda as purely external. Once K is state-dependent (K = K(lambda, S)), the first-order condition d/d(lambda)[N-C-K] = 0 becomes an implicit equation in (lambda, S) that may have zero, one, or multiple solutions depending on the current state. The claim of a unique interior optimum requires assumptions about convexity of C and K in lambda that are not stated.

### Heterodox Next Step

Derive the bifurcation diagram for the (S, lambda) system with K = k * S * lambda^n for n > 1 (collapse risk grows superlinearly in both state and rate). Identify where the system undergoes a saddle-node bifurcation and whether there is a parameter window in which the interior optimum is the unique stable attractor. Map this parameter window to TaF structural constraints: what properties of Ext_S correspond to being in the stable window versus the collapse window?

### Theorem/Claim Candidate

**Issuance rate bifurcation theorem (candidate):** The dynamical system dS/dt = N(lambda, S) - C(lambda, S) - K(lambda, S) undergoes a saddle-node bifurcation at a critical issuance rate lambda_c(s) where the interior fixed point and the collapse fixed point merge. For lambda < lambda_c(s), a stable structure-formation attractor exists. For lambda > lambda_c(s), the only attractor is the zero-structure state. lambda*(s) corresponds to the lambda that maximizes the basin of attraction of the stable attractor, not the argmax of the instantaneous net functional.

This is a strictly stronger and more falsifiable version of the Optimal Issuance Rate Curve Hypothesis.

---

## Run 3: Category Theorist (#2)

**What previous runs missed:** Run 1 (Maya Osei) checked the absorber status of mu_M and found it may be topology-absorbed. Run 2 (Elena Voss) found that the dynamics claim needs a stability analysis and the bifurcation structure is load-bearing. Neither run addressed the Route B investigation from the issuance explorer: whether the extension category for Ext_S naturally induces an issuance rate, and whether extension density can be optimized. This is a categorification question and requires a category-theoretic lens.

### Understanding

Both explorations connect to the D1RestrictionSystem and Ext_S. I am examining whether the proposed formal objects (lambda*(s), mu_M, the Ext_S extension category) have the right categorical structure, whether they are natural transformations or mere functions, and whether the proposed connections between them are functorial or ad hoc.

### Strongest Insight

The Ext_S category is the category of admissible extensions of source-side constraints — morphisms are extensions, objects are constraint states. The issuance rate lambda controls the "density" of extensions. The key categorical observation: if Ext_S has finite limits and colimits, then there is a natural notion of "extension density" as the cardinality of the hom-set Hom(S, Ext_S) at each state S. The optimal issuance rate lambda*(S) is then the rate that maximizes the cardinality of globally coherent extensions — the extensions that survive the global section condition.

This suggests that lambda*(S) is not a smooth optimization problem at all; it is a discrete combinatorial problem about the size of the category of coherent sections at each state. The argmax is over a cardinality, not a continuous functional. This discreteness is what the issuance rate explorer misses by writing down a smooth N-C-K functional.

**The right categorical object is not lambda*(s) but the functor that assigns to each state S the category of its admissible global sections, and the "issuance rate" is the rate of generation of new objects in this functor's image.**

### Strongest Critique

The mu(r) = N(r) - C(r) candidate from the issuance explorer is not typed. N(r) is "novelty" and C(r) is "coherence cost" — but these are not defined as functors, natural transformations, or even well-typed morphisms in any category. Without typing, mu(r) = N(r) - C(r) is not a candidate for the mu field in Y_TI. The mu field requires: units, domain, comparison rule, additivity or monotonicity, and transformation behavior. None of these are supplied for N-C as defined in the issuance explorer. Specifically:

1. Is N a functor from the category of realizations to a monoidal category? If so, what is the monoidal structure?
2. Is C a co-functor (contravariant) reflecting increasing coherence cost with scale?
3. Does N - C respect the morphisms in Ext_S? Does a morphism f: r1 -> r2 imply mu(r1) >= mu(r2) or the reverse?

Without answers, mu(r) = N(r) - C(r) is an informal candidate, not a typed specification.

### Heterodox Next Step

Construct the "coherent section functor" F: States(Ext_S) -> FinSets that assigns to each state the set of coherent global sections. The issuance rate lambda is then a natural transformation rate in this functor. The optimal lambda* is the rate that maximizes the growth rate of |F(S)| rather than a pointwise optimum of N-C-K. This reframing connects Route B (extension category) to Route A (dynamical systems) via the categorical dynamics of F.

Specifically: if F is right-adjoint to a "restriction functor" that forgets global coherence, the unit of the adjunction gives a natural map from local sections to globally coherent sections, and its failure to be an isomorphism is exactly the gluing obstruction (PO1). The issuance rate problem then becomes: what rate of generating new local sections maximizes the proportion that survive to global sections?

### Theorem/Claim Candidate

**Coherent section density theorem (candidate):** For a D1RestrictionSystem with extension category Ext_S, let F(S) be the set of globally coherent sections at state S. The optimal issuance rate lambda*(S) is the rate that maximizes d|F(S)|/dt, which equals the rate of new objects whose image under the global section functor is nonempty minus the rate of objects that create new gluing obstructions. This is equivalent to the PO1 obstruction rate being less than the global section generation rate — and when the PO1 rate dominates, lambda*(S) = 0 (no new extensions are coherence-increasing).

This theorem candidate connects lambda*(S) to the PO1 claim already in the ledger, making the issuance rate curve a consequence of existing formalism.

---

## Run 4: Resource Theory Researcher (#23)

**What previous runs missed:** Run 1 (Maya Osei) focused on the absorber status of mu_M. Run 2 (Elena Voss) found the bifurcation structure of the dynamics. Run 3 (Category Theorist) found that mu(r) = N(r) - C(r) is untyped and that the right object is a coherent section functor. What none of these runs addressed: the resource-theoretic status of the temporal issuance source object. The source-object spec requires a "task-natural capability Cap_TI." A resource theory perspective asks: what resource is being consumed, what resource is being produced, and does the proposed mu represent a genuine resource monotone?

### Understanding

Resource theories are characterized by: (1) a set of free states and free operations, (2) a resource monotone that does not increase under free operations, and (3) a convertibility order on resource states. The temporal issuance source object proposes mu as a source measure. In resource-theoretic terms, mu should be a resource monotone — a function that does not decrease as the system does "free" operations and decreases (strictly) only when a "resourceful" operation is performed.

### Strongest Insight

The optimal issuance rate curve explorer implicitly defines a resource theory but does not name it. Here is the natural resource theory:

- **Free states**: configurations where no new admissible extensions are being generated (lambda = 0); these are the "equilibrium" states
- **Free operations**: restriction maps within the existing D1RestrictionSystem that do not introduce new source events
- **Resource**: the stock of admissible extensions available in Ext_S — the "extension richness" of the source
- **Monotone**: mu(S) = |coherent sections of Ext_S| — the number of coherent global sections is the resource monotone

Under this framing, lambda*(S) is the rate of resource consumption that maximizes the rate of resource reproduction — it is a "sustainable yield" problem in resource theory language. The Optimal Issuance Rate Curve Hypothesis is then equivalent to: the sustainable yield of the extension resource is maximized at a nonzero interior rate. This is the Maximum Sustainable Yield theorem from renewable resource economics, already well-studied.

**This is either the strongest reframing or the strongest absorption.** The Maximum Sustainable Yield literature has full derivations of when interior optima exist, when they are stable, and what bifurcations occur. If N(lambda, S) - C(lambda, S) - K(lambda, S) maps cleanly onto the MSY functional, the issuance rate claim is absorbed by classical renewable resource theory.

### Strongest Critique

The metabolic scaling explorer proposes mu_M as a candidate source measure but does not check whether mu_M is a resource monotone. For mu_M to be a valid mu field, it must satisfy monotonicity or at least have a declared comparison rule. The exploration states "mu_M is monotone in system size" — but this is monotone in |r|, not in the partial order < on source realizations. For a resource monotone, we need: if r1 < r2 (r2 is a later or more developed realization), then mu_M(r1) [relation] mu_M(r2). The 3/4 scaling law says mu_M grows with system size — but if "later" realizations are also larger, this means mu_M increases under the source order, which would make it a "good" monotone only if we want larger mu = more resources. The direction of the inequality is not specified.

More seriously: the non-additivity of mu_M is proposed as the discriminating property. But non-additivity is a property of the measure relative to a specific composition operation. What composition operation is being used? If realizations are composed by union (r1 union r2), subadditivity is the relevant property. If they are composed by sequential extension (r1 then r2), the relevant property is different. The exploration does not specify which composition operation is intended, making the non-additivity claim formal but undefined.

### Heterodox Next Step

Apply the Maximum Sustainable Yield analysis directly to the N-C-K functional. Specifically: identify the "carrying capacity" K of the extension space, the "growth rate" r of new coherent sections, and the "harvesting rate" lambda of new extensions. The MSY lambda* = r*K/4 (for logistic growth) gives a concrete formula that can be compared to the argmax of N-C-K. If they match, the issuance rate curve is an MSY result. If they don't, the discrepancy reveals what TaF-specific structure adds to the standard MSY framework.

### Theorem/Claim Candidate

**Extension resource monotone theorem (candidate):** Define the extension richness E(S) = |{coherent global sections of Ext_S at state S}|. Then E is a resource monotone for the D1RestrictionSystem resource theory where free operations are restriction maps. The optimal issuance rate lambda*(S) that maximizes the sustainable yield of E satisfies: lambda*(S) = argmax_lambda [dE/dt | lambda] = a specific function of the growth rate of coherent sections and the rate of gluing obstruction creation. This is an interior optimum if and only if the gluing obstruction rate K(lambda) grows superlinearly in lambda (which follows if each new extension creates an independent probability p of obstruction: K = p * lambda * E).

---

## Run 5: Scientific Skeptic (#50)

**What previous runs missed:** Run 1 (Maya Osei) found a discriminating mu candidate. Run 2 (Elena Voss) found the bifurcation structure is load-bearing and the dynamics claim needs stability analysis. Run 3 (Category Theorist) found that mu(r) = N(r) - C(r) is untyped and the right object is a coherent section functor. Run 4 (Resource Theorist) found that the issuance rate curve may be a Maximum Sustainable Yield result, which absorbs it. What none of the previous runs did was step back and ask: are these explorations making progress on the actual reopen burden from the source-object spec, or are they generating interesting new ideas that don't address the specific checklist the spec requires?

### Understanding

The temporal-issuance-source-object-spec.md is extremely clear about what is required to reopen the Temporal Issuance bridge:

1. A non-circular source primitive not reducible to causal order, volume/counting, thermodynamic ledgers, information state, instrumentation, or TaF gluing.
2. Units, invariance behavior, operational comparison, and admissible transformations for that primitive.
3. A task-natural Cap_TI and native comparison R_K_TI declared before the witness pair is selected.
4. A positive preservation control.
5. A hostile same-neighbor-data split where the absorber vector is matched but Cap_TI still differs.
6. A demotion rule.

The question is not whether mu_M and lambda*(s) are interesting — they are. The question is whether they address items 1-6 of the reopen burden.

### Strongest Insight

The metabolic scaling explorer is the first exploration to propose a mu candidate with a genuine non-additivity claim grounded in a physical mechanism (hierarchical branching topology, not just an arbitrary functional form). This is closer to item 1 of the reopen burden than any previous mu candidate. However, it still does not complete the burden because items 2, 3, 5, and 6 are entirely absent. The exploration is a strong candidate source primitive nomination, but it is not a completed source-object contract.

The issuance rate explorer is explicitly not claiming to be a new source primitive — it correctly identifies lambda*(s) as the dynamics of Ext_S, not a definition of it. This is self-aware and honest. But it does introduce mu(r) = N(r) - C(r) as "a candidate" without noting that this candidate fails item 2 completely (no units, no comparison rule, no transformation behavior).

**The most important insight across all five runs:** neither exploration names a Cap_TI (task-natural capability). This is item 3 and it is the hardest item. All proposed mu candidates are source-side specifications — they describe the source measure, but they do not describe what capability a Temporal Issuance system provides that a system without temporal issuance cannot. Without Cap_TI, the mu candidates are candidates for a field in the source object but not for a nonabsorbed source primitive. The discriminating test is not "does mu_M differ numerically from entropy" but "does a system with mu_M as its source measure have a capability that a system with entropy-as-mu does not?"

### Strongest Critique

The metabolic scaling explorer makes a category error in claiming that the Moses framework provides "formal support for time as co-equal." The Moses framework shows that minimizing energy alone gives a different architecture than jointly minimizing energy and time. This is a statement about optimization problems, not about the ontological status of time. The correct conclusion is: "transport network architectures that ignore temporal delivery constraints are suboptimal." This does not support "time is constitutive of what it means for an event to be real" — TaF's actual claim. The explorer conflates "time matters for optimization" (true, well-established, uncontroversial) with "time is fundamental in the sense TaF claims" (much stronger, unproven by this route).

The issuance rate explorer is better-disciplined on scope — it correctly labels its central object as a "hypothesis candidate" and lists kill conditions. But it includes Route D (cosmological analogy) as an investigation route, which opens the door to exactly the kind of overclaiming the Scientific Skeptic is watching for. The Madau-Dickinson curve similarity is being used as evidence that the hump-shaped issuance curve is "robust" — but recurrence of a mathematical shape across different substrates is precisely what generic dynamical systems theory predicts, not TaF-specific evidence.

### Heterodox Next Step

Construct a minimal hostile example. Find two systems that:
- Have identical causal order, entropy production, event count, gluing data, and branching topology (so mu_M gives identical values)
- Differ in some other property that would constitute a genuine same-neighbor-data difference

If such a pair can be constructed, it demonstrates that mu_M is not discriminating even on its own terms — two systems can be identical by mu_M while differing in whatever property TaF is actually tracking. Conversely, if no such pair can be constructed while keeping the absorber vector fixed, that would be strong evidence for mu_M's discriminating power. This is the same-neighbor-data freeze applied directly to mu_M, which the metabolic scaling explorer calls for but does not execute.

### Theorem/Claim Candidate

**Reopen burden gap theorem (claim):** The metabolic scaling and issuance rate explorations collectively advance the source-object specification in one dimension (mu candidate with structural motivation) but leave four of six reopen burden items unaddressed. Specifically: items 2 (units/invariance for mu_M), 3 (task-natural Cap_TI), 5 (hostile same-neighbor-data split), and 6 (demotion rule) are not present in either exploration. No amount of mu candidate refinement constitutes progress on items 3 and 5; a separate Cap_TI-first investigation is required to unlock the hostile split.

This is not a theorem in the mathematical sense but a precise constraint on what work is needed next.

---

## Cross-Run Synthesis

### Convergences (what all five runs agree on)

**C1: mu_M is the strongest mu candidate so far.** The hierarchical branching topology grounding and the structural non-additivity make mu_M more physically motivated than entropy production, event counting, or Shannon information as a mu candidate. Maya Osei (Run 1) identified this. The Resource Theorist (Run 4) found that the non-additivity needs a composition operation specified. The Scientific Skeptic (Run 5) found that discriminating power requires a hostile split, not just formal distinction.

**C2: lambda*(s) is correctly placed as a dynamics constraint on Ext_S, not a source primitive.** Both the issuance rate explorer and all five runs agree on this. The Category Theorist (Run 3) gave the sharpest formulation: lambda*(S) is the rate of new objects in the coherent section functor's image, not an argmax of a smooth functional.

**C3: The hardest unaddressed item in the reopen burden is Cap_TI.** No exploration names what capability a Temporal Issuance system provides that could not be provided by a system using standard absorbers (causal order plus entropy). Without Cap_TI, the mu candidates are formally interesting but not source-primitive candidates.

**C4: The "time as co-equal" claim in the metabolic explorer is weaker than TaF needs.** Runs 1, 2, and 5 all noted this from different angles. Time entering an optimization as a cost to be minimized is not the same as time being constitutive of event reality. The Moses framework establishes that temporal delivery constraints are non-derivable from energy alone — this supports "time is not reducible to energy in transport systems," which is a useful but narrower claim.

### Divergences (what runs disagreed on)

**D1: Is the interior optimum of lambda*(s) stable?** Run 2 (Elena Voss) found this is not guaranteed — the dynamics may exhibit a pitchfork bifurcation where the interior optimum is a saddle rather than an attractor. Run 3 (Category Theorist) reframed the question categorically and found that stability corresponds to the global section functor F having a growing image. These are compatible but emphasize different aspects.

**D2: Is lambda*(s) absorbed by Maximum Sustainable Yield theory?** Run 4 (Resource Theorist) raised this as a serious absorption risk. No other run explicitly addressed it. This is unresolved: if N-C-K maps cleanly onto the MSY functional, lambda*(s) is standard resource management, not a TaF-specific result.

**D3: Is mu_M absorbed by the transport graph structure G?** Run 1 (Maya Osei) raised this as a kill condition: if mu_M is a function of the branching topology and the D1RestrictionSystem encodes branching topology in its gluing data G, then mu_M is absorbed by G. The Category Theorist (Run 3) implicitly assumed this could be avoided by the right functorial structure. This remains open and is the most important formal question for the metabolic scaling line.

### Most Important Finding

The most important finding is negative but constructive: the two explorations together constitute a strong mu candidate nomination (mu_M with structural non-additivity) and a correct dynamics reframing (lambda*(s) as Ext_S growth rate), but they do not constitute a nonabsorbed source primitive until Cap_TI is named. The explorations advance the source-object field specification from "all fields absorbed by default" to "one field (mu) has a structurally motivated candidate that may survive the freeze" — but the freeze itself has not been executed, and the capability object that would make the freeze worth executing is not yet defined.

**The correct next research move is Cap_TI-first:** define what unique capability a system with mu_M as its source measure has, then construct the hostile same-neighbor-data split that tests whether that capability depends on mu_M or reduces to its absorbers.

### Recommended Next Actions

1. **Cap_TI investigation**: Before executing the same-neighbor-data freeze for mu_M, name a task-natural capability. Candidates: source-order certification at scale (beyond what causal order plus counting provides), reconstruction reliability under access loss with branching-topology dependence, or observer-reconciliation bound that depends on the branching exponent.

2. **Composition operation specification for mu_M**: The non-additivity claim requires a specific composition operation for realizations. Is it set union? Sequential extension? The choice determines the type of non-additivity and which absorbers are relevant.

3. **Stability analysis for lambda*(s)**: Execute the bifurcation diagram for the N-C-K dynamical system with state-dependent K to determine whether the interior optimum is a stable attractor or a saddle. This is Route A formalized.

4. **G-absorption test for mu_M**: Construct a D1RestrictionSystem whose gluing data G fully encodes the branching topology. Check whether mu_M is then determined by G. If yes, mu_M is absorbed by TaF's own existing formalism and the metabolic scaling line closes.

5. **MSY comparison for lambda*(s)**: Map N(lambda, S) - C(lambda, S) - K(lambda, S) to the Maximum Sustainable Yield functional and check whether the interior optimum formula matches. If yes, lambda*(s) is absorbed by classical resource management theory; if no, the discrepancy specifies what TaF structure adds.
