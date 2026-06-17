# Governance Review Packet: Autonomous Research Advancement System

## Lifecycle stage: Solution Shaping (Stage 0)

**This is a design-space exploration, not an implementation plan.** No architecture is selected. No code is proposed. The deliverable is the material a human epistemic governor needs to make the *next* narrowing decision — and per the system's own philosophy, that narrowing decision is escalated to you, not made here.

Domain-agnostic by construction: nothing below depends on Time as Finality specifically. TaF is used only as the worked reference instance where an example helps.

Reading order: Part 5 (recommendation) and Part 6 (open governance questions) are the action surface. Parts 1–4 are the support.

---

## Part 0: Restating the invariants (so they can be checked against every architecture)

The source philosophy reduces to seven invariants. Every candidate architecture in Part 1 is scored against these in Part 2. Naming them first prevents the architectures from quietly redefining the goal.

- **I1 Advance, don't conclude.** Agents advance; humans conclude anything that narrows the space. Closure is a human-gated act.
- **I2 No silent pruning.** Every de-prioritization, closure, ontology choice, canonicalization, or branch collapse must emit a visible, reviewable artifact. Attention starvation is a failure even when no decision was made.
- **I3 Literature is evidence, not authority.** Orthodoxy informs; it does not bound.
- **I4 Local-minimum skepticism.** Apparent dead ends get multi-lens adversarial challenge before escalation. The goal is *robust* closure recommendations, not *no* closure.
- **I5 Portfolio, not scalar.** Multiple lanes (Core / Clarification / Frontier); Frontier is never starved by optimization pressure from the others.
- **I6 Append-first.** New artifacts by default; canon modified cautiously and provably.
- **I7 Protect human attention.** The system's success metric is *making it easier to tell what deserves human judgment*, not maximizing throughput. Maintenance must not consume scarce review.

A useful framing for the whole packet: **this is a search-process design problem, and the invariants are all variance-preservation constraints.** Standard optimization collapses variance (that is what "converge" means). This system is deliberately engineered to *resist premature variance collapse* while still making progress. That tension is the entire design challenge, and it is why naive queue/throughput designs fail it.

---

## Part 1: Candidate architectures

Seven architectures, chosen for genuine structural divergence (different *control loci* and different *primitives*), not parameter variations. Each: primitive, control loop, how it handles closure, where it fails.

### A. Queue-and-Packet Pipeline
- **Primitive:** the work packet. A single prioritized queue of typed packets (research / contradiction / literature / opportunity / assumption-audit / governance); agents pull, execute, emit new packets; humans drain a separate review queue.
- **Control loop:** priority score per packet → agents work top-of-queue → outputs append → human review queue surfaces the high-leverage subset.
- **Closure handling:** closure is just another packet type ("closure-recommendation") that lands in the human queue. Nothing closes without a human draining that packet.
- **Fails at:** I5 and I4. A single priority function is exactly the scalar optimizer the philosophy forbids — Frontier work has low immediate legibility and will sort to the bottom forever (silent pruning by ranking, the subtlest I2 violation). This is the "obvious" design and it is the one the philosophy is most directly warning against.

### B. Portfolio-Allocation System
- **Primitive:** the lane budget. Three (or more) lanes each hold a protected fraction of agent compute/attention; allocation is set by policy, not by a global score. Within a lane, any sub-mechanism (even a queue) runs.
- **Control loop:** fixed floor allocations (e.g., Frontier ≥ 20% non-negotiable) → each lane advances independently → cross-lane reconciliation surfaces contradictions → humans adjust *allocations* (a strategic lever) rather than individual items.
- **Closure handling:** a pathway can be de-prioritized *within* a lane but cannot be removed from the portfolio without a governance packet; Frontier's floor guarantees no idea is starved to death.
- **Fails at:** efficiency and coordination. Protected budgets mean known-dead work can still consume Frontier's floor; lanes can drift into incoherence without strong reconciliation. Mitigable but real. Directly satisfies I5 by construction — the floor *is* the anti-starvation mechanism.

### C. Governance-First (Escalation-Centric) System
- **Primitive:** the decision. The system is organized around a typed taxonomy of decisions (ontology / canonicalization / closure / prioritization / reward) and their escalation criteria. Research work exists to *feed* decisions.
- **Control loop:** agents continuously classify the repo state into pending decisions → each decision carries an evidence dossier and a "robustness check" status → only decisions passing robustness checks reach humans → humans adjudicate.
- **Closure handling:** the strongest of any architecture — closure is a first-class object with mandatory adversarial dossier (I4 is structurally enforced). I7 is the explicit design target.
- **Fails at:** advancement throughput. A decision-centric system can under-invest in the generative/exploratory work that *creates* things worth deciding about. Risks becoming a beautifully governed repository that doesn't actually advance (I1's "advance" half).

### D. Agent-Swarm / Stigmergic System
- **Primitive:** the trace. Many lightweight agents act locally on the artifact graph, leaving traces (annotations, links, scores) that bias other agents — ant-colony / stigmergy. No central queue; coordination is emergent through the shared artifact medium.
- **Control loop:** agents wander the artifact graph → reinforce promising traces, decay stale ones → structure self-organizes → humans read emergent heat-maps.
- **Closure handling:** weak and dangerous. Trace decay *is* silent pruning (direct I2 violation) — paths die by pheromone evaporation with no review. Would need an explicit "decay event emits an artifact" patch, which fights the paradigm.
- **Fails at:** I2 catastrophically, and legibility. Included because its *failure* is instructive: it is the natural-systems metaphor (the repo loves these) that the governance philosophy most directly forbids. Stigmergy is how silent pruning looks when you build it on purpose.

### E. Hypothesis-Market / Prediction-Market System
- **Primitive:** the position. Each research pathway is an instrument; agents (and humans) take positions on "will this formalize / falsify / publish"; a scoring rule (e.g., logarithmic market scoring) aggregates beliefs and allocates attention to where information value (not consensus) is highest.
- **Control loop:** agents price pathways → attention flows to high-information-value (high-disagreement or high-leverage) positions → resolution events update scores → humans read the order book for surprise.
- **Closure handling:** closure = a market resolving; but markets are pricing mechanisms and can *manufacture* consensus (everyone copies the leader) — an I3 orthodoxy-capture risk in disguise. Needs a subsidy for contrarian positions (a literal Frontier subsidy) to satisfy I5.
- **Fails at:** I3 if naive — markets converge, and convergence is exactly what we're resisting. *But* the information-value framing (subsidize disagreement) is the sharpest available mechanism for "low-effort high-information task discovery," and it operationalizes I7 well (price = what deserves attention). Strong idea, dangerous default.

### F. Evolutionary / Variation-Selection System
- **Primitive:** the population of hypotheses/pathways under variation, retention, and selection — with *explicitly tunable selection pressure*. Low pressure = exploration; high = exploitation; the dial is a governance lever.
- **Control loop:** generate variants (mutation = persona reframes, frame-shifts, randomization) → retain in append-only archive → apply *weak, governed* selection → humans set the pressure dial and protect a "neutral drift" reserve.
- **Closure handling:** nothing is deleted (append-only archive = I6 by construction); "closure" means selection pressure drops a pathway below active threshold but it stays revivable — which is exactly the local-minimum-vs-dead-end distinction (I4) the philosophy cares about most. Maps cleanly onto the repo's own evolutionary-finality lens.
- **Fails at:** archive bloat and selection-metric capture (if the fitness function is literature-fit, you get orthodoxy capture — I3). The fitness function is the single point of failure and must be plural.

### G. Dialectical / Adversarial-Ensemble System
- **Primitive:** the structured disagreement. Every artifact above a significance threshold gets thesis / antithesis / synthesis treatment by divergent + adversarial persona ensembles before it can change status; persistent unresolved disagreement is *preserved*, not averaged away.
- **Control loop:** artifact reaches significance → mandatory multi-persona pass → synthesis attempt → unresolved tensions become first-class "open-tension" artifacts → humans adjudicate genuine forks.
- **Closure handling:** the strongest on I4 — closure literally cannot happen without surviving adversarial challenge. The repo already has the persona machinery for this (personas/INDEX.md).
- **Fails at:** cost and decision-paralysis. Running full dialectic on everything is expensive and can prevent convergence even where convergence is warranted (over-correcting I1 into never-conclude). Needs a significance gate so it doesn't dialectic every typo.

---

## Part 2: Comparative analysis

Scored against the seven invariants. ✓✓ = structurally enforced, ✓ = supported, ~ = possible but not native, ✗ = works against it.

| | A Queue | B Portfolio | C Governance | D Swarm | E Market | F Evolutionary | G Dialectical |
|---|---|---|---|---|---|---|---|
| I1 Advance not conclude | ✓ | ✓ | ~ (under-advances) | ✓ | ✓ | ✓✓ | ~ (over-deliberates) |
| I2 No silent pruning | ✗ (rank-starve) | ✓ | ✓✓ | ✗✗ (decay) | ~ (convergence) | ✓✓ (archive) | ✓ |
| I3 Lit as evidence | ~ | ✓ | ✓ | ~ | ✗ (converges) | ~ (fitness risk) | ✓✓ |
| I4 Local-min skepticism | ✗ | ~ | ✓✓ | ✗ | ✓ (info-value) | ✓✓ (revivable) | ✓✓ |
| I5 Portfolio/Frontier floor | ✗ | ✓✓ | ~ | ~ | ✓ (w/ subsidy) | ✓ (w/ reserve) | ~ |
| I6 Append-first | ✓ | ✓ | ✓ | ~ | ✓ | ✓✓ | ✓ |
| I7 Protect attention | ✓ | ~ | ✓✓ | ✗ | ✓✓ | ~ | ✗ (expensive) |

**Readings:**
- **No single architecture wins.** The strong performers are complementary, not competing: C (Governance) owns closure-quality and attention-protection; B (Portfolio) owns anti-starvation; F (Evolutionary) owns append-archive and the dead-end/local-min distinction; G (Dialectical) owns robustness-of-closure; E (Market) owns information-value-based attention routing.
- **A and D are anti-patterns for *this* philosophy** — and instructively so. A is the default engineering answer (single priority queue); D is the default natural-systems metaphor (stigmergy). Both violate I2, the system's signature constraint, in opposite ways. Their presence in the design space is a warning, not a recommendation.
- **The market (E) and swarm (D) both converge by default** — and convergence is the enemy here. E is salvageable because disagreement-subsidy inverts its convergence; D is not, because decay *is* the mechanism.
- **The honest conclusion is a layered composite** (see Part 5), with B's portfolio as the allocation skeleton, C's decision-objects as the escalation layer, F's append-archive as the substrate, and G's dialectic as the closure gate — applied *selectively* via a significance threshold so I7 survives.

---

## Part 3: Persona reviews

Each persona gives roses (working) / buds (promising-if-developed) / thorns (problems) / missing / likely failure mode. Personas review *the design space and the emerging composite*, not one architecture.

### Research scientist
- **Roses:** the Frontier-floor (I5) matches how real breakthroughs happen — protected slack, not optimized throughput. Append-archive means negative results survive, which is where most scientific value silently dies in practice.
- **Buds:** "low-effort high-information task discovery" is the most valuable behavior promised and the least specified; if delivered it changes daily research life.
- **Thorns:** agents are bad at judging *significance* — they will flood Frontier with weird-but-worthless. Significance gating is doing enormous unspecified work.
- **Missing:** reproducibility/provenance. Every agent conclusion needs a re-runnable trace or it's not science.
- **Failure mode:** a beautifully legible repository full of confident, unverifiable agent claims.

### Mathematician
- **Roses:** treating closure as requiring adversarial survival (G/I4) is just proof-vs-refutation discipline; correct.
- **Buds:** the dead-end-vs-local-minimum distinction is formalizable as "no path found yet" vs "proven no path" — the system should *track which kind of dead end* each closure is.
- **Thorns:** "robustness of a closure recommendation" is undefined. How many persona passes = robust? Without a stopping rule, G never halts (I1 violation) or halts arbitrarily.
- **Missing:** a notion of *independence* among the challenge lenses. Ten correlated personas are one persona. Divergence must be measured, not assumed.
- **Failure mode:** theater of rigor — many persona passes that are secretly one viewpoint, producing false confidence in closures.

### Philosopher of science
- **Roses:** I3 (literature as evidence not authority) is exactly right and rare; most "research AI" silently does the opposite.
- **Buds:** orthodoxy capture is measurable — track the ratio of citations-as-constraint vs citations-as-evidence over time.
- **Thorns:** the system could mistake *contrarianism* for *frontier*. Resisting orthodoxy is not the same as being right; a system rewarded for weirdness manufactures weirdness (the inverse of orthodoxy capture, equally bad).
- **Missing:** a theory of *when convergence is correct*. The philosophy is so anti-closure it risks never accepting a genuinely settled result.
- **Failure mode:** permanent revolution — nothing is ever allowed to be known, every settled fact re-litigated forever.

### Systems engineer
- **Roses:** append-first (I6) is operationally sound — immutable log, derived views. Standard, robust, auditable.
- **Buds:** typed packets/decisions give a clean schema spine; the whole thing can be an event-sourced system with projections.
- **Thorns:** append-only grows without bound; you need compaction/indexing, and *compaction is a pruning act* that must itself obey I2. Recursion problem: the maintenance of the anti-pruning system can silently prune.
- **Missing:** failure/rollback semantics for agent actions; rate limits; cost ceilings. Autonomous agents on an append log can generate infinite low-value artifacts.
- **Failure mode:** unbounded artifact growth drowns the legibility it was meant to create. (Note: this is the system doing to itself what dark-matter "stabilized but inaccessible structure" describes — finalized artifacts no observer can render. The repo's own concept predicts its operational failure mode.)

### Complexity theorist
- **Roses:** portfolio + weak selection + variation is a correctly specified exploration/exploitation system; the Frontier floor is a temperature parameter keeping it off the greedy attractor.
- **Buds:** selection pressure as a governance dial is genuinely good — it's an annealing schedule under human control.
- **Thorns:** any fixed fitness function self-organizes toward its own blind spots; you get criticality only with *plural, shifting* selection. Single-metric reward → guaranteed local minimum, the exact failure the system exists to prevent.
- **Missing:** diversity *measurement*. You can't protect variance you don't measure.
- **Failure mode:** the system optimizes its own proxy metric and converges precisely while reporting that it is exploring.

### Knowledge-management expert
- **Roses:** indexes, glossaries, dependency maps, discoverability as first-class agent work — this is the legibility win and it's real and deliverable.
- **Buds:** "make it easier to tell what deserves human judgment" (I7) is the right north star and is measurable (time-to-triage).
- **Thorns:** ontology choices are escalated to humans, but the system needs a *working* ontology to function in the meantime — who owns the provisional one, and how is provisional-vs-canonical marked everywhere?
- **Missing:** versioning of the ontology itself; migration when humans do choose.
- **Failure mode:** ontology limbo — everything provisional forever because canonicalization is a scarce human act that never gets scheduled.

### Governance designer
- **Roses:** decisions as typed first-class objects with dossiers (C) is exactly how you make governance tractable and auditable.
- **Buds:** an escalation taxonomy with explicit criteria prevents both over- and under-escalation.
- **Thorns:** the review queue prioritization is itself a narrowing decision made by agents — *who governs the thing that decides what humans see?* If agents rank the human queue, agents control human attention, inverting the authority model (I7/I1).
- **Missing:** an audit path for *non-escalation* — the dog that didn't bark. You must be able to ask "what did the system decide NOT to show me, and why."
- **Failure mode:** capture-by-queue — agents quietly set the human agenda by ordering the review surface.

### Open-source maintainer
- **Roses:** append-first + work packets = low-friction contribution surface; contributor ledgers and rubrics are real community infrastructure.
- **Buds:** ready-to-run research packets are an excellent onboarding ramp — a newcomer can grab a packet and contribute meaningfully day one.
- **Thorns:** provisional reward/recognition signals generated by agents will be gamed the instant they carry any weight; and contested reward is the fastest way to fracture a research community.
- **Missing:** spam/sybil resistance; a human in the reward loop before anything is durable.
- **Failure mode:** incentive gaming turns the contribution ledger into the thing people optimize, displacing the research.

### Adversarial reviewer
- **Roses:** the system at least *names* its failure modes, which is more than most.
- **Buds:** none worth flattering.
- **Thorns:** every protective mechanism is itself an attack surface. "No silent pruning" → flood the system so nothing can be reviewed (pruning by denial-of-service). "Frontier floor" → farm the floor with garbage. "Adversarial challenge before closure" → never close anything by always mounting a token challenge. The philosophy's strengths are exploitable as written.
- **Missing:** adversarial *cost*. Every challenge, escalation, and revival must cost something or they become griefing vectors.
- **Failure mode:** the system is trivially DOS-able into permanent indecision by anyone (including a dumb agent loop) who exploits the anti-closure bias.

### Incentive designer
- **Roses:** separating "advance" rewards (cheap, abundant) from "conclude" authority (scarce, human) is the right cut.
- **Buds:** information-value pricing (E) is the best available signal for what to reward — pay for reducing uncertainty, not for producing artifacts.
- **Thorns:** rewarding artifact *production* (the append-first default) directly incentivizes volume over value. The metric and the philosophy point opposite directions.
- **Missing:** a cost side to the ledger. Only rewarding production with no cost for noise guarantees noise.
- **Failure mode:** Goodhart — "advance understanding" proxied as "artifacts created," and the system floods.

### Organizational architect
- **Roses:** agents-operate / humans-govern is a clean, real org model (it's a research lab with a strong PI layer).
- **Buds:** the lane structure maps to real research-org functions (core teams, internal tools, skunkworks).
- **Thorns:** the human governors become the bottleneck the instant agents are productive — the whole system's throughput is capped by scarce human adjudication, and the design adds *more* things demanding human judgment (escalations, ontology, reward, closure).
- **Missing:** a model of human *attention budget* as the actual scarce resource, with explicit backpressure when it's exceeded.
- **Failure mode:** the governors drown; either they rubber-stamp (governance theater, I1/I4 lost) or they become the blocker (advancement stalls).

---

## Part 4: Cross-persona synthesis

Five themes recur across independent personas — these are the load-bearing findings:

1. **The meta-pruning problem (engineer, governance, KM, adversarial).** Every mechanism that protects against silent pruning is itself capable of silent pruning: queue-ordering, compaction, escalation-filtering, fitness functions, ontology-limbo. *The system that prevents pruning must be audited for the pruning it does.* This is the single most important finding and no source-document mechanism addresses it. **Required primitive: a "non-escalation audit" / negative-space log — the system must record what it chose not to surface and why, and that record must itself be reviewable.**

2. **Diversity must be measured, not assumed (mathematician, complexity, philosopher).** Adversarial ensembles, persona passes, and Frontier lanes all assume divergence they don't verify. Correlated lenses give false robustness; rewarded weirdness gives manufactured frontier. **Required primitive: a divergence/independence metric over lenses and lanes, tracked over time as an orthodoxy-capture *and* a contrarianism-capture indicator.**

3. **Human attention is the true scarce resource and the true bottleneck (org architect, governance, incentive).** The system adds demand for human judgment while promising to protect it. These can't both win unless attention is modeled as a hard budget with backpressure. **Required primitive: an explicit human-attention budget with backpressure — when the escalation queue exceeds capacity, the system must *raise* its escalation bar (and log that it did), not silently drop items.**

4. **Everything reward-or-rank-bearing gets gamed (incentive, OSS, adversarial).** Production rewards → volume. Queue ranking → agenda capture. Frontier floor → garbage farming. **Required primitive: a cost side to every action — challenges, escalations, revivals, and artifact creation all spend a budget — so the anti-closure bias can't be weaponized into denial-of-service.**

5. **The system must know when convergence is *correct* (philosopher, mathematician, research scientist).** Anti-closure taken to the limit is permanent revolution — nothing is ever known. The philosophy needs a dual: not just "don't close prematurely" but "do accept robustly-supported closure." **Required primitive: a closure-acceptance criterion (a stopping rule), not only a closure-resistance mechanism.**

**The synthesis verdict:** the source philosophy is sound but *incomplete in a specific, patchable way* — it specifies resistance (don't prune, don't close, don't starve) far more thoroughly than it specifies the duals (when to compact, when to accept closure, how to bound the resistance so it can't be gamed or drown the humans). The composite architecture must add the five duals above or the philosophy's own strengths become its failure modes.

---

## Part 5: Recommended direction

**Recommendation: a layered composite, adopted as a *target* not a build order, with the five Part-4 duals as non-negotiable additions.** Explicitly NOT selecting a single architecture (per the constraint), and explicitly flagging that this recommendation is itself a narrowing decision requiring your approval (I1).

The composite, by layer:

- **Substrate: F (Evolutionary append-archive).** Immutable event log of artifacts; nothing deleted; pathways have activation levels, not life/death. This gives I6 and the revivable dead-end/local-min distinction (I4) for free.
- **Allocation: B (Portfolio with Frontier floor).** Lanes with protected budgets; Frontier floor non-negotiable; selection *pressure* (from F) is a per-lane governance dial. This gives I5.
- **Routing: E (information-value pricing), de-converged.** Attention within lanes flows to highest information-value (disagreement × leverage), with an explicit subsidy for contrarian positions so the market doesn't converge. This operationalizes "low-effort high-information discovery" and I7.
- **Closure gate: G (dialectical), significance-gated.** Only artifacts above a significance threshold trigger full adversarial/Hegelian treatment; the threshold protects I7. This gives robust I4.
- **Escalation + human interface: C (decisions as typed objects).** Closure/ontology/canonicalization/reward are first-class dossiers; humans adjudicate; *non-escalation is logged* (Part-4 dual 1). This gives I1, I2, I7.
- **NOT used as paradigms: A and D.** A single global queue and stigmergic decay are explicitly rejected — they violate I2/I5 at the paradigm level.

**Plus the five duals, restated as build requirements:** non-escalation/negative-space log; lens-divergence metric; human-attention budget with logged backpressure; cost-side on every action; closure-acceptance stopping rule.

**Why this and not the simplest thing (A):** the single-queue pipeline is what you'd build if you forgot the philosophy. Its failure (Frontier rank-starvation) is silent, gradual, and exactly Failure Mode 2. The composite costs more but is the minimum structure that doesn't betray the stated invariants. If budget forces simplification, simplify *within* this structure (fewer lanes, cheaper dialectic), never back to A.

---

## Part 6: Open questions requiring governance decisions

These are yours to answer; the system cannot and should not self-resolve them (each is an I1 narrowing decision).

1. **Significance threshold for dialectic.** What makes an artifact "significant enough" to warrant the expensive adversarial pass? Set too low → humans drown (I7). Too high → things close without challenge (I4). This single number trades off the system's two core protections. *Needs a human-set, revisable policy.*
2. **Human-attention budget.** How many escalations/week is the governance layer actually willing to process? Everything downstream (escalation bar, backpressure behavior) calibrates to this number, and it must be honest, not aspirational.
3. **The closure-acceptance stopping rule.** When IS the system permitted to treat something as settled? How many independent surviving challenges? The philosophy is silent here and it is a genuine value choice — how anti-closure do you actually want to be, given permanent-revolution is a real failure?
4. **Plural fitness / what counts as "advance."** The reward and selection signals must be plural to avoid Goodhart, but plural-how? Who defines the basket, and how often is it rotated? This is the orthodoxy-capture lever.
5. **Provisional ontology ownership.** The system needs a working ontology while canonical choices await you. Who/what owns the provisional one, how is provisional-vs-canonical marked, and what triggers a canonicalization escalation? (KM persona's limbo risk.)
6. **Cost currency.** Part-4 dual 4 requires a cost on actions. What's the budget unit — compute, a synthetic credit, human-attention shadow-price? This determines gaming-resistance.
7. **Scope of autonomy on canon.** I6 says modify canon cautiously. Where exactly is the line between an agent appending an exploration (fine) and an agent editing a claim file or the ledger (escalate)? The TaF instance already enforces this manually (Joe-notes, claim-class promotion); the general system needs the rule explicit.
8. **Domain-agnostic vs instance-tuned.** Is the immediate target the reusable general system, or the TaF instance with the general system as a later extraction? The two imply different first builds. (Recommendation leans: prototype on TaF, extract the domain-agnostic core once the duals are validated — but this is your call.)

---

## Part 7: Suggested phased implementation path (for later — not authorization to build)

Offered only so the governance decision has a sense of consequence. Each phase gated by your approval; no phase begins without the prior phase's invariants demonstrated.

- **Phase 0 (now):** this packet. Governance reviews Parts 5–6, answers enough of Part 6 to define a first scope. No build.
- **Phase 1 — Substrate + legibility, lowest risk:** append-only artifact log + typed packets + indexes/glossary/dependency-map agents. Delivers the I6 substrate and the legibility win (the Design Test's "improved legibility" / "low-risk work completed") with near-zero closure risk. Validates the cost-side (dual 4) cheaply before anything can be gamed.
- **Phase 2 — Portfolio + escalation, the governance spine:** lane allocation with Frontier floor (B) + decisions-as-objects with the non-escalation log (C + dual 1) + human-attention budget with backpressure (dual 3). This is where the philosophy first actually bites; build it before any closure machinery exists.
- **Phase 3 — Closure discipline:** significance-gated dialectic (G) + lens-divergence metric (dual 2) + closure-acceptance stopping rule (dual 5). Only now can the system recommend closures, and only with all four I4-protections live.
- **Phase 4 — Information-value routing + incentives, highest gaming risk, last:** de-converged market pricing (E) + contributor ledger/reward. Deliberately last because it's the most gameable and the least reversible socially; everything else should be stable before reward signals carry weight.
- **Continuous:** orthodoxy-capture and contrarianism-capture metrics tracked from Phase 1 onward, surfaced to governance, never auto-actioned.

**Meta-point on the path:** it is deliberately *capability-conservative* — legibility before allocation before closure before incentives — because each phase adds a power the previous phase's safeguards must already be containing. Building closure (Phase 3) before escalation-audit (Phase 2) would be the system committing its own Failure Mode 2 during its own construction.

---

## Constraint compliance

Design space explored (7 divergent architectures, not variations). No architecture selected (composite recommended as a target, flagged as requiring your approval). Design space not collapsed (A–G and their trade-offs preserved; rejected ones kept with reasons). No implementation. Returned for governance review before any build. The recommendation explicitly identifies itself as a narrowing decision escalated to you — which is the system's own first principle applied to its own design.

## Relation to repo

- Operating philosophy aligns with existing repo discipline: append-first ≈ explorations/ vs claims/ separation; closure-as-human-act ≈ claim-class promotion + Joe-notes; adversarial-before-closure ≈ [personas/INDEX.md](../personas/INDEX.md).
- The TaF instance is the natural Phase-1 proving ground; the audit's work cards (WC-1…WC-26) are already a packet backlog in everything but name.
- Filed under governance/ as Stage-0 exploratory material, not canon, per the no-edit-canon constraint.
