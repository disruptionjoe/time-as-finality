---
document_type: persona_meta_synthesis_reverse
cluster: D-simulation-dynamics
pass: meta-synthesis-reverse-2026-07-02
primary_reader: agents
authority: exploratory
status: exploratory
created: 2026-07-02
personas: [16, 17, 18, 20, 21, 57, 58, 59, 60, 61, 62, 63]
structure: [meta-synthesis, hegelian, steelman]
note: "Method not evidence. Single-process ceiling applies. Nothing here moves a claim or edits a ledger."
---

# Cluster D — Simulation / Dynamics / MMO / Game-Mechanism Meta-Synthesis (REVERSE)

Core charge: does this cluster supply the **missing mechanism** — *why observers
are bounded* — by reading finality as a bandwidth / rendering / rollback
phenomenon, and the four modes (E0/E1/E2/E3) as four reasons a state becomes
un-rolled-back-able?

---

## 57. Game-Mechanism Designer

**Meta-synthesis.** The whole program is a theory of the *commit rule*: when does
a tentative state change become un-takeback-able. The four modes are exactly the
four ways a game makes a move stick. **E0** = declared/ruled-final ("the referee
called it," the datum to reverse exists but the rulebook forbids querying it).
**E1** = the undo buffer is finite and the move scrolled off the end (limit
erasure). **E2** = reversing is legal but too expensive to compute in-session
(hardness gate). **E3** = the move is symmetry-locked — no legal inverse move
exists in the ruleset. What we're missing: TaF has been hunting *one* physics of
the arrow (is it E1, E2, or E3?) when the game-design answer is that **finality is
polymorphic** — every persistent world runs all four commit-rules simultaneously
on different records, and the "arrow of time" is just the union of their
commit-fronts.

**Hegelian.** *Antithesis:* "four ways to make a move stick" is a designer's
taxonomy, not a structural claim — it renames E0–E3 as UI states. Against the
honest negatives: single-mode arrow claims got pre-empted, and this doesn't add a
mechanism, it adds a metaphor. *Synthesis:* what survives is not the metaphor but
the **polymorphism claim** — the testable assertion that no single forcing mode
carries the arrow, that a closed system's irreversibility decomposes into a
*profile* over {E0,E1,E2,E3}, and that this profile is an invariant of the
record, not of the observer.

**Steelman.** Concrete claim: define, per committed record, a **finality type** =
the minimal resource whose removal would re-open the record (information / energy
/ computation / symmetry). The arrow of time is then a *typed* commit-front, and
the open TaF question ("E1 or E2 or E3?") is ill-posed — the correct object is the
distribution of finality-types across the record set. The one move that makes it
real: exhibit a single closed model where two records provably carry *different*
finality-types, forcing the decomposition to be non-trivial.

---

## 58. MMO Network Architect

**Meta-synthesis.** Read finality as **authoritative-commit vs rollback**, and the
program snaps into focus. A client shows *apparent* finality (client-side
prediction) that the authoritative server can still roll back until confirmation;
after confirmation it is un-rolled-back-able. E0/E1/E2/E3 are four reasons the
server *cannot* roll a state back: **E0** it was declared authoritative by fiat;
**E1** the reconciliation window (buffer) is finite and the divergence is now
past it; **E2** recomputing the authoritative trajectory to the fork point is
too costly; **E3** a conserved invariant forbids the inverse transition. The thing
we're missing: **observer-boundedness is the client/server split itself.** An
observer is bounded because it is a *predicting client* on a bandwidth-limited
link to the authoritative state — finality is what the link has already
acknowledged and can no longer NAK.

**Hegelian.** *Antithesis:* MMO architecture presupposes a privileged
authoritative server; physics has no such server, so this smuggles in an absolute
frame TaF explicitly denies (observer-*relative* sections). *Synthesis:* drop the
single server. What survives is **peer-authoritative rollback**: every observer is
both client and a shard of the authority; finality is the *acknowledged
intersection* of what no peer can still NAK. That is observer-relative and still
mechanistic — it gives the North Star a commit protocol without a God-frame.

**Steelman.** Concrete claim: finality = the **stable prefix** of an
eventually-consistent, peer-authoritative replicated log, and observer-boundedness
= the ack-latency horizon (a peer cannot distinguish "not yet acked" from "will
never be acked" within its bandwidth). This is the mechanism TaF lacks: observers
are bounded *because acknowledgement is rate-limited*, so each carves a section at
its own confirmation horizon. The move that makes it real: show the ack-horizon
reproduces the E0–E3 forcing trichotomy as *reasons a NAK is impossible*.

---

## 59. Distributed-Simulation Engineer

**Meta-synthesis.** This is Time-Warp optimistic synchronization. Every observer
runs its local simulation optimistically and commits speculatively; **Global
Virtual Time (GVT)** is the frontier below which no rollback (anti-message) can
ever arrive — i.e. GVT *is* finality. The missing reframe: TaF's "increasing
finality within observer-accessible sections" is literally **GVT advancing**, and
the four modes are four reasons an anti-message cannot be sent for an event:
**E0** committed by declaration (fossil-collected); **E1** past the anti-message
horizon (limit); **E2** the rollback is computable but exceeds the cost budget;
**E3** an invariant blocks the anti-message. What we're missing at the meta layer:
finality is not a property of the *state* but of the **anti-message reachability**
of the event — a purely relational, observer-graph quantity.

**Hegelian.** *Antithesis:* GVT requires a global min-reduction over all
LPs — again a global operation the closed-system / no-local-witness constraint
should forbid; and the honest negative on E2 (computational arrow came back
REDESIGN/pre-empted) says the cost-budget story is weak. *Synthesis:* keep GVT as
a *cohomological* object, not a computed minimum. It survives as: **finality =
the global section (GVT frontier) with no local representative** — which is
exactly the H^1 gluing-obstruction residue (item 10). The cluster's independent
route lands on the same "global property, no local witness" object as the
governance/legitimacy cluster.

**Steelman.** Concrete claim: model the observer set as a set of logical processes
with a causality DAG; define the **finality frontier** as the largest antichain
below which anti-messages are unreachable. Claim it is an H^1-type invariant of
the DAG (present in the whole, in no proper subset). The move that makes it real:
prove the frontier is *not* a min over local clocks but a genuine gluing
obstruction — a case where every LP locally believes an event is reversible yet
the global DAG makes it final.

---

## 60. Virtual-Economy Designer

**Meta-synthesis.** Finality = **settlement**. A transaction is provisional (can be
clawed back) until settled, then irreversible. Sinks and faucets are the
irreversibility pumps: value records become final when the counterfactual that
would reverse them has been *destroyed* (sunk), not merely unqueried. The reframe
TaF is missing: the forcing trichotomy is the **three settlement guarantees** — a
record settles because reversing it would (E1) require energy already dissipated
into a sink, (E2) require recomputing a ledger history too deep to unwind, or (E3)
violate a conservation law (double-spend / value-conservation invariant). E0 =
settled by decree (central clearing). Finality is *value that survives clawback
under bounded trust and partial information*.

**Hegelian.** *Antithesis:* "settlement" is just consensus finality wearing an
economics hat — pre-empted by the distributed-systems and Avalanche personas
already on the panel; adds branding, not structure. *Synthesis:* the survivor is
the **sink as physical irreversibility**: settlement is final specifically when
the reversing information has been thermodynamically erased into a sink, tying E1
(Landauer/energy) to E0 (declared) via *cost of un-erasure*. That is a real bridge
— it says "declared" and "energy-forced" are endpoints of one axis (single-
instance vs infinity-or-a-bet, item 2), instantiated as clawback-cost.

**Steelman.** Concrete claim: define finality of a value record as the **clawback
cost** — resources to reconstruct-and-reverse the reversing counterfactual. E0 =
zero physical cost but forbidden by rule; E1 = cost diverges (sunk); E2 = cost
super-polynomial; E3 = cost infinite (no inverse exists). One monotone, four
regimes. The move that makes it real: show clawback-cost is a resource monotone
that recovers the E0–E3 partition as its regime diagram — unifying the trichotomy
under a single measured quantity.

---

## 61. Interest-Management Specialist

**Meta-synthesis.** **This is the missing mechanism for observer-boundedness.**
Observers are bounded not by accident but by *necessity*: no observer can subscribe
to the whole world's state on a finite link, so every observer runs an
area-of-interest (AoI) filter and receives only a bandwidth-bounded relevance
slice. TaF's "observer-accessible section" *is* an AoI subscription. Finality =
what survives the relevance filter and gets persisted into the observer's replica.
The larger story: **boundedness is not a limitation bolted onto observers — it is
the definition of an observer.** An unbounded observer has no AoI, no filter, no
distinct section, hence no arrow. The arrow of time is a side effect of interest
management: relevance filtering is lossy and non-invertible, so past states outside
current AoI cannot be reconstructed — that irrecoverability *is* the past.

**Hegelian.** *Antithesis:* this explains boundedness by *positing* a finite link —
it assumes exactly the resource limit (E1) it claims to explain, so it's
circular; and "relevance filter = arrow" is the poet's move the panel exists to
catch (persona 42). *Synthesis:* de-circularize by making the link-bound
*derived*, not assumed — couple it to persona 63's transport law. What survives:
observer-boundedness = **finite mutual information between a section and its
complement**, and the AoI filter is the channel realizing that bound. Boundedness
becomes a channel-capacity claim, not a decree.

**Steelman.** Concrete structural claim: an observer is a **finite-capacity
subscription** to a state manifold; its section = the AoI it can hold; finality =
records whose removal from the section cannot be detected across the filter (they
have become part of the irreversible substrate rather than the live view). The
move that makes it real: derive the capacity bound from a transport/energy law
(hand to 63) so boundedness is *forced*, not assumed — turning TaF's central gap
("why are agents bounded?") into "because subscription to a branching state
network is capacity-limited by joint energy-time optimization."

---

## 62. Bandwidth-Bounded-World Architect

**Meta-synthesis.** Level-of-detail (LOD) and detail-on-demand are the whole
picture. A world too big to render at full fidelity is stored at multiscale LOD;
near the observer it is high-fidelity and mutable, far away it is coarsened and
*baked* (committed, no longer re-simulated). Finality = **baking**: the moment a
region drops below the fidelity budget it is flattened to a static record and can
no longer be edited. The reframe TaF misses: the arrow of time is a **temporal
LOD gradient** — recent state is high-fidelity/reversible (still in the mutable
near-field), old state is baked/irreversible (coarsened into the far-field
substrate). E0–E3 are four baking triggers: declared-baked, budget-exceeded
(E1), too-costly-to-re-sim (E2), symmetry-collapsed (E3).

**Hegelian.** *Antithesis:* LOD/baking is a re-description of coarse-graining —
Kadanoff renormalization (already E1's established home, item 3); nothing new, and
it inherits the pre-emption of the thermodynamic-arrow route. *Synthesis:* the
novelty isn't the coarse-graining, it's the **budget as the forcing agent**:
baking happens *because a shared finite budget is reallocated toward the
near-field*, so finality-here is paid for by fidelity-loss-there. That is a
**conservation-of-fidelity** claim absent from plain renormalization — irreversible
commitment is not free coarse-graining, it is a *transfer* of a conserved
rendering resource from past to present.

**Steelman.** Concrete claim: posit a conserved fidelity/description budget across
a state manifold; finality of a region = fidelity debited below the re-editability
threshold; the arrow = monotone reallocation of budget from far/old to near/new.
The move that makes it real: identify the conserved budget with a physical
quantity (action? free energy? bits?) and show the reallocation monotone *is*
entropy production — making "baking" a derived thermodynamic law rather than an
engineering choice.

---

## 63. Metabolic Scaling Theorist (Maya Osei)

**Meta-synthesis.** The whole program is a **transport-and-scaling law**, and this
is the mechanism the other personas keep gesturing at. West-Brown-Enquist: a
hierarchical branching network under *joint energy-time optimization* forces
sublinear scaling (B ∝ M^{3/4}) and a space-filling, capacity-limited terminal
unit. Map: the observer is a **terminal unit** of a branching supply network
delivering state/information; it is bounded *because* joint energy-time
optimization of the whole network forces finite terminal capacity — you physically
cannot build a network that supplies every unit unbounded throughput. **This
supplies the missing "why bounded": boundedness is the geometric price of a
branching transport network optimized for energy AND time simultaneously.**
Finality = what has been irreversibly *delivered and metabolized* — records that
have left the reversible circulating pool and been committed to structure. The
arrow = the direction of net transport from source (high free energy) to sink
(committed structure).

**Hegelian.** *Antithesis:* metabolic scaling's derivation assumes a specific
geometry (space-filling fractal, invariant terminal units, dominant viscous/energy
loss). TaF's "state manifold" has no shown branching-transport geometry, so
applying B ∝ M^{3/4} is out-of-domain — the honest-negative pattern (results valid
only inside their geometric assumptions, item on substrate-independence). Also risk
that μ (the source measure) is absorbed by ordinary entropy/counting.
*Synthesis:* keep only the **structural conditional**: *IF* the observer-network
has branching-transport topology, *THEN* boundedness and sublinear finality-
issuance are forced. The contribution is turning "why bounded?" from a posit into a
**theorem with a checkable geometric hypothesis** — which is exactly what TaF's
central gap needs.

**Steelman.** Concrete claim: model information/state delivery to observers as a
hierarchical branching network; impose joint energy-time optimization; derive
(a) finite terminal capacity = observer bandwidth bound, and (b) a sublinear
scaling law for the rate of finality-issuance vs system size. The one move that
makes it real: exhibit a genuinely **sublinear, non-additive** source measure μ
for finality-issuance that standard entropy does *not* reproduce — this would both
(i) give observer-boundedness a forced mechanism and (ii) clear the persona's own
falsification bar (μ not absorbed by counting).

---

## 16. Dynamical Systems Expert (Elena Voss)

**Meta-synthesis.** Strip the game metaphors: finality is **non-injective
dynamics**. A map that is not one-to-one merges distinct pasts into one present;
once merged, the past is unrecoverable — that merging *is* irreversibility, and the
arrow is the accumulation of merges. The reframe TaF is missing: the four modes are
four *sources of non-injectivity*. **E0** the map is invertible but the inverse
branch is not queried (declared); **E1** injectivity fails only in a limit (basins
merge as t→∞, contraction onto an attractor); **E2** the inverse exists but is
computationally intractable (sensitive dependence — reconstructing the preimage
needs unbounded precision); **E3** a symmetry quotients the phase space so distinct
points are identified (structural non-injectivity). Finality = collapse onto an
attractor; observer-boundedness = finite Lyapunov-resolution.

**Hegelian.** *Antithesis:* "irreversibility = non-injectivity" is textbook (dissipative
systems, attractors); no novelty, and E1 again reduces to the pre-empted
thermodynamic route. *Synthesis:* the novel move is **unifying E0–E3 as one
partition of the ways injectivity fails** — declared (unqueried branch),
asymptotic (limit merge), computational (intractable preimage), symmetric
(quotient). That single partition of injectivity-failure is not textbook; it is the
cluster's cleanest candidate for the "one object" the four modes are shadows of.

**Steelman.** Concrete claim: define finality via the **preimage structure** of the
evolution map. A record is final iff its preimage is (E0) not queried, (E1)
non-unique only in the t→∞ limit, (E2) unique but not efficiently invertible, or
(E3) collapsed by symmetry. The arrow = monotone loss of preimage-injectivity
(topological entropy production). The move that makes it real: show these four are
*exhaustive and mutually exclusive* modes of injectivity-failure for a broad map
class — turning the E0–E3 taxonomy into a theorem about non-invertible dynamics.

---

## 17. Symbolic Dynamics Expert (Rafael Cortez)

**Meta-synthesis.** Encode the world as a shift space of symbol sequences.
Irreversibility = the shift is **non-invertible** (a one-sided, not two-sided,
shift): the future determines less of the past than the past determines of the
future. Ordinal/permutation-entropy quantifies exactly the *lost past-
determinacy*. The reframe: **the arrow of time is the failure of the shift to be a
homeomorphism**, and the four modes are four reasons the pre-shift is undefined —
declared (E0: the symbol is present but not read), limit (E1: past symbols fall off
the observable window), computational (E2: the sliding-block inverse code is
intractable), symmetry (E3: a factor map identifies distinct pasts). Finality = a
symbol that can no longer be un-emitted because its preimage word is unreadable.

**Hegelian.** *Antithesis:* one-sided shifts and their non-invertibility are
standard; permutation entropy is a known irreversibility statistic. Where's the
program-level novelty? Risk of just relabeling. *Synthesis:* the survivor is a
**measurement**: permutation-entropy asymmetry gives an *empirical finality
statistic* — a way to read, from a record's symbol stream, how much past-
determinacy has been lost and (potentially) *which mode* dominated. This is the
cluster's one route that hands the Experimentalist (persona 54) a concrete estimator
rather than a metaphor.

**Steelman.** Concrete claim: define finality of a section as the **past-
determinacy deficit** — the conditional entropy of the past given the observable
future window — estimated via ordinal patterns. The arrow = monotone growth of this
deficit. The move that makes it real: show the deficit's *decomposition* tracks the
E0–E3 profile (persona 57's polymorphism), giving a measurable, model-free arrow-of-
time diagnostic with a mode-attribution.

---

## 18. Multiscale Statistics Expert (Lena Kowalski)

**Meta-synthesis.** The four modes live at **different scales**, and the program's
error is treating them as competitors for the *one* arrow rather than as a
**scale hierarchy**. Wavelet/multiresolution view: E0 (declared) is the finest
scale — a single instance, no aggregation; E1 (limit) is the coarsest — the
asymptotic/infinite-scale behavior; E2 (computational) and E3 (symmetry) sit
between. "Physical vs declared" collapsing to "single-instance vs
infinity-or-a-bet" (item 2) is *literally a statement about scale*: fine scale =
declared, coarse/infinite scale = forced. The missing story: **finality is
scale-covariant** — the same record is E0 at one resolution and E1/E3 at another,
and the arrow is the cross-scale reconciliation (cointegration) that must hold for
the record to persist.

**Hegelian.** *Antithesis:* "different modes at different scales" risks being a
filing system, not a mechanism; and multiscale reconciliation doesn't itself force
an arrow. *Synthesis:* the real content is the **admissibility hinge as a scale
choice** (item 7): whether a boundary reads E0 or E3 depends on the observable
algebra, and *the observable algebra is a choice of resolution*. So the E0/E3
ambiguity (and the T421 disanalogy, item 8) is a **scale-dependence**, not a
contradiction — two "E3"s that pull opposite ways are E3 at different resolutions.

**Steelman.** Concrete claim: finality-type is a function of resolution; define a
**finality renormalization-group flow** over scale, with E0 as UV fixed point and
E1 as IR fixed point, E2/E3 as crossover regimes. The move that makes it real:
show the T421 E3-disanalogy is resolved as a UV/IR distinction — operational-forced
(IR/coarse) vs metric-forced (UV/fine) are the two ends of one flow — turning a
contradiction into a scaling relation.

---

## 20. Physics-Informed ML Researcher (Aisha Rahman)

**Meta-synthesis.** Frame the observer as a **reservoir/neural operator** predicting
its world under a finite state budget. Irreversibility appears when the learned
forward operator is **not invertible on the accessible representation** — the
observer's compressed latent cannot reconstruct inputs it has coarse-listened
away. The reframe: the four modes are four reasons the inverse operator fails to
exist *on the observer's representation* — declared (weight not read), limit
(numerically underflowed), computational (inverse ill-conditioned / NP-hard),
symmetry (the encoder quotients a symmetry). TaF's boundedness = **finite latent
capacity of the predicting operator**, and finality = what has been written to
non-trainable (frozen) memory.

**Hegelian.** *Antithesis:* this is just "lossy autoencoders lose information" — an
engineering truism, and it presupposes the capacity bound (E1) it wants to explain,
same circularity as persona 61. *Synthesis:* the durable piece is the
**physics-informed constraint**: a PINN embeds conservation laws (E3) *as hard
constraints* while capacity limits (E1) and conditioning (E2) are soft. That
separation is exactly the forcing trichotomy — symmetry (hard/structural) vs energy
(budget) vs computation (conditioning) — realized as constraint *types* in one
learning objective. The trichotomy is a statement about *how a constraint enters an
optimizer*.

**Steelman.** Concrete claim: model finality as the frozen (non-differentiable)
substrate of a constrained predictive operator; E3 = hard equality constraints, E1
= capacity/regularization bound, E2 = optimization-hardness, E0 = a masked (unread)
input. The move that makes it real: show these constraint-classes are *not
interchangeable* — that you cannot trade an E3 hard constraint for E1 capacity —
giving the trichotomy an operational irreducibility (which the T421 disanalogy
already hints is true for E3).

---

## 21. Complex Systems Scientist

**Meta-synthesis.** Finality is an **emergent global property with no local
witness** — and this cluster's whole job is to say *by what mechanism* emergence
happens: **bandwidth-bounded local interactions on a network**. Self-organization
produces order (finality) that no single node holds; the arrow is the ratchet of
self-organization (order accretes, disorder is exported). The reframe assembling
everything: the program is describing **the same "global section, no local
representative" object three times** — as legitimacy (Aumann-Shapley, item 9), as
cohomology (H^1 residue, item 10), and here as *emergence*. What we're missing:
these are not analogies, they are the **one object** — a conserved global quantity
that is un-rolled-back-able precisely because it lives in the whole and no
bandwidth-bounded local observer can edit it.

**Hegelian.** *Antithesis:* "emergence" is the least falsifiable word in science;
saying finality is emergent risks explaining nothing (persona 50 territory). And
"three descriptions of one object" is a pattern-match unless the identity is
*proven* — item 6 explicitly flags the tri-repo identity as **untested**, and item
8 shows one cross-repo identification (E3) already **failed** to type-check.
*Synthesis:* demote from "they are one object" to "they are candidates for one
object, and the test is whether the same H^1 obstruction computes all three." The
honest negative (identity untested / one E3 identification abandoned) is not fatal
but disciplining: the meta-synthesis is a **conjecture with a decidable type-check**,
not a claim.

**Steelman.** Concrete claim: there is a single global invariant — an H^1-type
gluing obstruction on the observer-interaction network — that instantiates as
legitimacy (governance), finality (TaF), and generation-count residue (GU), and is
un-rolled-back-able because bandwidth-bounded local dynamics cannot reach it. The
move that makes it real: **compute the obstruction in one concrete closed model and
show it is non-zero and local-witness-free** — converting "emergence" into a named
cohomology class, and giving the cross-repo residue its first actual type-check.

---

## Cluster Meta-Synthesis

This cluster's distinctive contribution is that it is the **only cluster positioned
to supply TaF's missing mechanism — *why observers are bounded*** — rather than
merely re-describing finality. Three nominations, strongest first.

**1 — #63 Metabolic Scaling (Osei): boundedness as the forced geometric price of a
branching transport network under joint energy-time optimization.** This is the
cluster's single most important candidate because it converts TaF's central gap
from a *posit* ("assume observers are bounded") into a *theorem with a checkable
hypothesis* ("if the observer-supply network has branching-transport topology, finite
terminal capacity is forced"). Every other boundedness story in the cluster (#61,
#20, #58) is circular — it assumes a finite link to explain the finite link. Osei is
the only one that could make the bound *derived*. Backed by #61 (interest-management
gives the same capacity bound its channel realization) and #62 (fidelity-budget
conservation gives it a substrate). **Real-structure-vs-rhyme:** likely *real
structure* but gated on one hard hypothesis — that the state-delivery network
actually has WBE branching geometry; if it doesn't, it's rhyme. Decidable, not
decided.

**2 — #59 Distributed-Sim GVT ≡ finality-as-anti-message-unreachability, landing
independently on the H^1 "global section, no local witness" object (#21).** The
strongest structural convergence: an optimistic-synchronization engineer, reasoning
purely from Time-Warp rollback, arrives at the *same* cohomological residue that the
governance/legitimacy cluster reached from Aumann-Shapley. Two disciplines, one
object — that raises the object above single-persona rhyme. Backed by #21 (emergence
as the third face) and #57 (polymorphic commit-fronts). **Real-structure-vs-rhyme:**
*real structure at risk* — the convergence is genuine, but item 6 marks the
underlying identity **untested** and item 8 shows one such cross-repo identification
already failed to type-check; so this is a *conjecture with a decidable test* (compute
the obstruction in one model), not a result. Its honesty is its strength.

**3 — #16 Voss / #57 Designer: the E0–E3 taxonomy as one exhaustive partition of the
ways injectivity/commit fails — "finality is polymorphic," not one arrow.** The
cleanest reframe of the program's open question: TaF has been asking "is the arrow
E1, E2, or E3?" and this pair answers "malformed question — it's a *profile* over all
four, one partition of non-injectivity (Voss) / commit-rules (Designer)." This
directly dissolves item 5's open question and reframes the T421 E3-disanalogy (item 8)
as two entries in one partition rather than a contradiction. **Real-structure-vs-
rhyme:** *real structure, most tractable* — proving E0–E3 exhaustive-and-exclusive for
non-injective maps is an actual theorem, and #17 (Cortez) even supplies a measurable
estimator (permutation-entropy past-determinacy deficit with mode-attribution) to test
the profile empirically. Lowest ceiling of novelty, highest chance of being provably
right.

Honest cross-cutting note: #60/#58's settlement/consensus framings are largely
**pre-empted** (distributed-systems and Avalanche personas already own them) and read
more as rebranding than new structure; #62's baking reduces to Kadanoff coarse-graining
unless the fidelity-conservation claim is made physical. The live novelty concentrates
in the three above — and specifically in whichever of {Osei's forced bound, the H^1
type-check, the injectivity partition} first survives a concrete closed-model
computation.
