# Candidate North Star v0.6: Projection Sufficiency For Typed Capability

## Status

This is a Candidate North Star working draft.

It is not canon, does not replace `NORTH-STAR.md`, and is not a claim update,
roadmap commitment, paper-ready theorem, or evidence for a physics thesis.

This version synthesizes the two v0.5 drafts and the two v0.5 research
critiques. It keeps the locked posture:

```text
Capability Projection is a typed projection-sufficiency audit language.
It is not, by itself, a novelty claim that projection loses information.
It is not a replacement physics program.
It is not allowed to derive known physics from Cap.
```

The main note should stay compact. Prior-art inventories, citation maps,
witness expansions, and physics depth belong in companion reports unless they
repair a correctness gap or prevent a predictable expert misunderstanding.

## Reader Pushback Targets

If reviewing this draft, do not judge the slogan in isolation. Push on the
audit discipline:

- Is the formal typing correct?
- Is the capability object domain-native, or is it gerrymandered?
- Are visible equality and capability comparison declared sharply enough?
- Has the neighboring field been granted its legitimate state, operations,
  equivalences, access structures, and absorber theorems?
- Does any residue remain useful after honest demotion?
- Does any physics sentence reverse the required direction from known physics
  to induced `Cap`?

## North Star Statement

The bare idea:

```text
observable equivalence is not necessarily capability equivalence
```

is old.

The useful Candidate North Star is:

```text
a disciplined audit surface for typing capability objects, testing projection
sufficiency, recording prior-art absorption, and identifying any formal or
canonical residue that survives.
```

For fixed observer, task family, horizon, admissible state set, and resource
boundary:

```text
future capability need not factor through observer-visible state
```

Read this as a projection-sufficiency question for typed capability objects,
not as a metaphysical discovery, physics derivation, or claim that
non-factorization is new.

## Formal Core

Fix an audit context:

```text
O      observer or access profile
Sigma  observational schema or interface
r      resolution, fidelity, or coarse-graining
U      local domain, patch, scope, or access region
T      task family
h      horizon
B      budget, boundary, or resource condition
A      admissible source states, with A subset Y
```

Declare:

```text
pi_{O,Sigma,r,U} : A -> X_{O,Sigma,r}(U)
Cap_{O,T,h,B}   : A -> K_{O,T,h,B}
```

Also declare:

```text
~=_X  visible-state equivalence
R_K   native capability comparison
```

In the equivalence-valued case, `R_K` is `~=_K`.

The default visible-state equality relation is not "same payload," "same
current value," "same local marginal," or "same current measurement record."
Equality must be declared by the audit context.

## Capability Sufficiency

In the equivalence-valued case, a projection `pi : A -> X` is
capability-sufficient for `Cap : A -> K` when there exists:

```text
Cbar : im(A -> X / ~=_X) -> K / ~=_K
```

such that for every admissible `y`:

```text
Cbar([pi(y)]_{~=_X}) = [Cap(y)]_{~=_K}.
```

Equivalently:

```text
for all admissible y1,y2 in A:

pi(y1) ~=_X pi(y2)  =>  Cap(y1) ~=_K Cap(y2).
```

In plain language:

```text
the observer-visible state determines the declared capability object up to
the declared capability equivalence
```

The projection is capability-insufficient when two admissible states have the
same visible class but different capability classes.

Preferred terms:

- `capability-sufficient projection`;
- `capability-insufficient projection`;
- `projection-sufficiency failure`.

Avoid categorical-faithfulness vocabulary unless a real faithful-functor
condition is being used.

## Fiber Constancy, Kernel, And Spread

Fiber-constancy lemma:

```text
Cap factors through pi up to ~=_K iff Cap is ~=_K-constant over every
visible-equivalence fiber in A.
```

This is not novelty evidence. It is the bookkeeping that prevents the
candidate from becoming vague.

In the equivalence-valued case, define:

```text
y1 ~_Cap y2 iff Cap(y1) ~=_K Cap(y2).
```

Then `A / ~_Cap` is the capability-kernel quotient: the coarsest set quotient
of admissible states that preserves the declared capability class. This may be
glossed as the minimal capability-preserving quotient only after the allowed
morphisms and equivalences are named.

For a visible state class, define:

```text
Spread_Cap([x]_{~=_X}) =
  { Cap(y) | y in A and pi(y) ~=_X x } / ~=_K.
```

Then:

```text
Cap factors through pi iff Spread_Cap([x]_{~=_X}) is a singleton for every
visible equivalence class in im(pi).
```

The source fiber is not itself the capability. The audit object is the spread
of capability values across that visible-equivalence fiber.

Choose spread summaries native to `K`: cardinality for finite `K`, diameter or
Hausdorff distance for metric objects, order width for preorders, regret or
value gap for decision objects, deficiency distance for experiments, and
certification loss for audit objects.

## Native Capability Comparison

Quotient language is cleanest when `R_K` is an equivalence relation. Many
important capability objects are not naturally equality-valued.

The exact formal core above is the equivalence-valued case. The rows below are
audit regimes: each must supply its own native comparison, preservation
notion, thresholds, morphisms, or reflections before a witness can be judged.

| Native `K` structure | Audit comparison |
| --- | --- |
| Equivalence-valued | Factor through `K / ~=_K`. |
| Metric or tolerance-valued | Bounded fiber diameter, value gap, regret, or native error envelope. |
| Preorder or resource preorder | Mutual convertibility equivalence, or monotone factorization through a posetal reflection. |
| Decision or risk object | Value gap, Bayes risk gap, regret, Blackwell/Le Cam deficiency, or a declared decision-native criterion. |
| Stochastic object | Equality in distribution, total variation, Wasserstein distance, coupling criterion, or risk equivalence. |
| Category-valued object | Quotient category, reflection, fibration, functorial semantics, isomorphism, equivalence, or natural equivalence. |

The exact, approximate, probabilistic, top-k, recall, latency/recall, and
workload regimes must be declared before a witness is promoted.

## Operational Capability Gate

No witness should be considered until `K`, `Cap`, and `R_K` are typed.

Every witness must pass this gate:

```text
1. Cap is native or operationally forced in the domain.
2. Cap is declared before selecting the witness pair or fixture.
3. A native test, measurement, decision procedure, evaluation protocol, or
   operational semantics is named.
4. Visible comparison and capability comparison are declared.
5. Positive preservation controls and negative non-factorization fixtures are
   included.
6. Cap does not merely restate the hidden difference between y1 and y2.
7. The observer/access profile, task, horizon, and resource boundary are fixed.
```

Common `K` types include answer sets, admissible-operation sets, decision or
risk objects, statistical experiment objects, policy classes, provenance
objects, behavioral equivalence classes, resource convertibility structures,
reachable or viable sets, database workload objects, approximate retrieval
envelopes, proof obligations, safety invariants, and physics-facing
accessibility or convertibility structures.

Rule:

```text
Capability comparison must be domain-native, task-natural, operationally
legible, and fixed before witness construction.
```

## Absorption Protocol

Non-factorization is not novelty evidence. It triggers an absorption audit.

Same-neighbor-data condition:

```text
Before assigning residue, grant the neighboring theory all state variables,
operations, equivalences, access structures, comparison criteria, and absorber
theorems it normally treats as legitimate under the same observer, task,
horizon, and resource boundary.
```

This blocks the cheap version of the claim: choosing an impoverished projection
and then treating the resulting failure as residue.

### Native State Completion

The neighboring field's legitimate state distinguishes the cases, restores
factorization, or shows that the original projection was underdescribed.

Examples: belief state, information state, provenance graph, transaction log,
version vector, causal graph, resource monotone, purifier or environment
access, index family, index parameters, build state, materialization state,
detector calibration, apparatus state, or audit log.

State completion is not cheating when the neighboring theory normally includes
that state.

### Native Theorem Absorption

The neighboring field already has the theorem, schema, equivalence hierarchy,
or completeness criterion that explains the non-factorization.

Examples: sufficient statistics, Blackwell comparison, Le Cam deficiency,
POMDP belief states, process semantics, abstract interpretation, database view
determinacy, provenance, causal identifiability, resource theories, gauge
theory, causal structure, RG/EFT, and local observable algebras.

### Repair And Threshold Absorption

A proposed witness is absorbed when the alleged failure disappears after:

- correcting `~=_X`, `R_K`, the admissible domain, or the access profile;
- applying the native tolerance, risk, recall, uncertainty, latency/recall
  envelope, certification threshold, or error budget;
- recognizing pure gauge, coordinate convention, basis choice, phase
  convention, labeling convention, interface convention, or representational
  redundancy.

Physics witnesses must be invariant under gauge, relabeling, coordinate,
phase-convention, basis, or representation redundancy unless the physical
access profile fixes the choice.

## Trivial Enrichment Theorem

For any `pi : A -> X` and `Cap : A -> K`, define:

```text
pi'(y) = (pi(y), Cap(y)) : A -> X x K.
```

Then `Cap` factors through `pi'`.

Every projection-sufficiency failure can be repaired by enriching visible
state with the capability object itself. The real question is whether the
enrichment is domain-natural, minimal for the declared morphism class,
canonical, operationally available, accessible to the declared observer, and
already standard in an absorber field.

## Residue Ladder

A proposed witness fails promotion if a mature absorber supplies a natural
sufficient enrichment, quotient, comparison, or theorem under the declared
audit context.

1. **Canonical Residue**: survives native state completion, native theorem
   absorption, equivalence repair, approximation-threshold absorption, and
   gauge/representation absorption; `Cap` is domain-natural or operationally
   forced; the quotient or enrichment is minimal or canonical; same-neighbor
   data testing has been done.
2. **Formal Audit Residue**: a typed distinction survives tested prior-art
   absorption as a clean formal object, lemma, quotient, metric, executable
   fixture, or audit criterion, but canonicity is not yet established.
3. **Typed Toy-Model Residue**: a known-physics or domain-native toy model
   cleanly instantiates the audit, without becoming evidence for new physics.
4. **Translation Residue**: no new formal phenomenon survives, but the audit
   surface aligns mature theories usefully.
5. **Heuristic Residue**: the language helps find missing state, access,
   provenance, policy, resource, or observer data.
6. **Redundant Or Demoted**: the vocabulary duplicates prior art or adds
   confusion without improving comparison, reviewability, or witness triage.

Default expectation:

```text
translation residue or heuristic residue
```

not:

```text
canonical residue
```

## Witness Ledger

Witnesses run to date returned Translation Residue.

```text
Vector/ANN retrieval, HNSW vs IVFFlat with same corpus:
  Failure label: projection_underdescribed.
  Absorbed by: native state completion and ANN/vector-search practice.
  Native state includes index family, parameters, build procedure,
  materialization state, query-time settings, workload, selectivity, and
  recall/latency/error envelope.
```

```text
Quantum resource theory, same local rho_A with different global resource:
  Absorbed by: native state completion and native theorem absorption.
  If the observer has only subsystem A, the local state is the available
  state. If the observer has AB, the full bipartite state restores the
  distinction. If Cap is convertibility under LOCC or free operations, QRT
  already supplies the convertibility preorder, monotones, and access-profile
  discipline.
```

These are not failed witnesses. They are successful audit tests: the
instrument identified underdescription and native absorption rather than
inflating a counterexample pair into novelty.

## Witness Template

Use this compact template before promoting any new witness:

```text
Domain:
Neighboring absorber:
Observer/task/horizon/boundary:
A subset Y:
pi:
X:
~=_X:
Cap:
K:
R_K:
Positive preservation control:
Negative non-factorization fixture:
Native state completion tested:
Native theorem absorption tested:
Repair/threshold/gauge absorption tested:
Capability spread:
Residue label:
Demotion condition:
```

## Reviewer Checklist

Before promoting any witness, ask:

```text
A subset Y declared?
admissibility conditions declared?
X declared?
pi declared?
visible equivalence ~=_X declared?
K typed?
Cap declared before the witness?
native capability comparison R_K declared?
if quotienting: ~=_K declared as an equivalence?
if approximate: epsilon/probabilistic/top-k/recall@k/latency-recall/workload
  equivalence or error envelope declared?
observer/access profile fixed?
task family fixed?
horizon fixed?
resource boundary fixed?
projection meaningful?
same-visible-state context fixed?
projection underdescribed?
Cap domain-native or operationally forced?
Cap non-gerrymandered?
native test or evaluation protocol named?
positive preservation control supplied?
negative non-factorization fixture supplied?
capability spread singleton, bounded, or non-singleton under native comparison?
capability-kernel quotient or native minimal object identified?
trivial enrichment tested?
native state completion tested?
native theorem absorption tested?
equivalence repair tested?
approximation-threshold absorption tested?
gauge/representation absorption tested?
residue label honest?
```

Physics addendum:

```text
known physics induces Cap?
physical access profile declared?
allowed operations declared?
gauge/relabeling invariance respected?
strictly local controls included where relevant?
no global, purifier, environment, horizon, or asymptotic access smuggled in?
not-claimed boundary explicit?
```

## Domain Calibration

Domain sections are calibration gates, not novelty evidence.

| Domain | Native absorber | Likely residue |
| --- | --- | --- |
| Statistics / decision / control / causal inference | Sufficient statistics, Blackwell/Le Cam, belief states, observability, reachability, viability, interventional identifiability. | Translation unless a cross-domain transfer theorem or minimal-enrichment result appears. |
| Databases / retrieval / information systems | View/query determinacy, rewritability, provenance, temporal semantics, access control, index/materialization state, consistency, approximate retrieval, workload equivalence. | Translation or heuristic; approximate/workload-bounded minimality is the strongest near-term formal route. |
| Process semantics / computation / abstraction | Testing equivalence, bisimulation, trace/failure/readiness semantics, Nerode quotients, abstract interpretation, complete abstractions, Galois connections. | Translation or formal audit residue if capability spread transfers across semantics families. |
| Resource and physics-facing domains | Resource theory, causal structure, thermodynamics, gauge theory, local observable algebras, EFT/RG, topological response, detector metrology. | Translation, typed toy-model residue, or formal audit residue; physics-bearing canonical residue is long-horizon. |

## No-Free-Physics Rule

Physics sections remain strong, but every physics-facing claim must derive
`Cap` from known physics.

Required direction:

```text
known physics -> induced Cap -> projection-sufficiency audit
```

Forbidden direction:

```text
Cap -> known physics
```

unless future theorems justify it.

Use this template:

```text
Known theory:
Y:
A subset Y:
X:
pi:
Cap:
K:
Native comparison on K:
Allowed operations:
Observer/access profile:
Horizon/resource boundary:
Gauge/relabeling invariance:
Factorization question:
Native absorber:
Residue status:
Not claimed:
```

Strictly local observers cannot be credited with global, purifier,
environment, horizon-exterior/interior, or asymptotic capability unless the
access profile grants a physical route to that structure.

## Physics Witness Posture

Promote as strong physics-facing anchors:

- quantum resource theory under explicit access profiles;
- GR causal accessibility, domains of dependence, and horizons;
- thermodynamic resource theory and stochastic thermodynamics;
- detector, instrumentation, calibration, and provenance infrastructure;
- condensed matter and topological response;
- EFT/RG as preservation control, bridge, and absorber.

Hold or narrow:

- Standard Model structure as constraints on admissible transformations, not
  capability by itself;
- black holes as observer-indexed access stress tests, not progress on the
  information problem;
- time as capability trajectories along physical time, not replacement time;
- emergence as platform capability or neighboring motivation, not evidence
  for a new universal law.

Demote from the main text unless typed models exist:

- dark matter;
- dark energy.

Dark matter may be revisited only as a typed gravitational-dynamics audit.
Dark energy may be revisited only as a typed cosmological-accessibility audit.

## Relationship To TaF

Capability Projection remains adjacent to the existing TaF North Star.

TaF may motivate why projection, irreversibility, records, and
observer-relative capability matter. Candidate North Star should still stand
or fall as a typed sufficiency audit.

It can help organize records, finality, observer-accessible sections,
reconstruction debt, detector packets, LossKernel, typed forgetting, future
operation availability, maintenance viability, and capability trajectories
along physical time.

It should not replace the current North Star unless later work shows formal or
canonical residue that survives mature absorption.

## Success, Failure, And Collapse

Success would be one or more of:

- a canonical-residue witness;
- a formal audit residue result that survives hostile absorption;
- a cross-domain transfer theorem across at least two mature fields;
- a domain-natural capability-kernel quotient or minimal enrichment theorem;
- an executable suite with preservation controls and non-factorization
  fixtures;
- an audit template that reliably catches false witness claims;
- a physics-facing typed toy model deriving `Cap` from known physics.

The candidate weakens or dissolves if every domain-natural witness is absorbed
by legitimate state completion or native theorem absorption, no `Cap` object
remains domain-native after comparison is declared, finite pair tests remain
self-inflicted projection loss, physics remains analogy rather than typed
known-physics audit, no useful transfer appears, or the vocabulary duplicates
existing frameworks without improving comparison and triage.

If every important witness is absorbed and no minimality theorem, canonical
enrichment family, executable audit suite, typed toy model, or transfer theorem
remains, record translation residue, heuristic residue, redundancy, or
demotion.

The purpose is discovery, not defense.

## Next Research Actions

The next useful work is:

1. Write a native-comparison appendix for equivalence, preorder, metric,
   tolerance, probabilistic, decision-theoretic, resource-theoretic, and
   category-valued `K`.
2. Run QRT Witness 2 with explicit access profiles.
3. Run a GR causal-accessibility witness using simple models first.
4. Run a thermodynamic resource witness with finite-time or catalytic
   constraints.
5. Run a database/ANN minimality attempt over fixed embeddings, workload,
   selectivity, index family, parameters, build state, materialization state,
   and recall/latency/error envelope.
6. Run a process-semantics absorption comparison using future tests, trace
   projection, testing equivalence, failure semantics, bisimulation, or a
   Nerode-style quotient.
7. Build a small executable witness suite with one positive preservation
   control and one negative non-factorization fixture for each candidate
   domain.
8. Attempt a cross-domain transfer theorem: projection sufficiency is
   equivalent to singleton or bounded capability spread over
   visible-equivalence fibers, with singleton or bounded interpreted through
   the native structure of `K`.

## Appendix Map

Use companion reports for detail:

| Companion report | Burden carried |
| --- | --- |
| `Candidate North Star v0.5 - Claude Draft.md` | v0.5 witness ledger, domain calibration texture, and physics witness posture used in this synthesis. |
| `Candidate North Star v0.5 Codex.md` | v0.5 compact formal spine, equality guardrails, domain-calibration framing, and appendix-navigation posture used in this synthesis. |
| `Candidate North Star v0.5 research critiques.md` | v0.6 mathematical repairs, operational capability gate, absorption expansions, terminology decisions, red flags, and next research actions. |
| `Deep Research Review of Candidate North Star v0.5-deep-research-report.md` | v0.6 research synthesis, prior-art absorption assessment, physics grounding, witness review, and citation insertion plan. |
| `Capability Projection Schema v0.1.md` | Full audit schema, non-arbitrariness conditions, same-neighbor-data condition, positive and negative controls. |
| `Database Absorption Test for Capability Projection-deep-research-report.md` | Database absorption map and equality fields. |
| `Prior-Art Audit of Capability Projection-deep-research-report.md` | Broad absorption posture across mature fields. |
| `Candidate North Star Mathematical Strengthening Suggestions v0.1.md` | Mathematical strengthening suggestions and physics-safe formalization. |
| `Candidate North Star 20 Mathematics Perspectives Report v0.1.md` | Twenty mathematics lenses and hardening moves. |
| `Candidate North Star 20 Physics Perspectives Report v0.1.md` | Twenty physics lenses and no-free-physics requirements. |
| `Witness-Run-VectorANN-v0.1.md` | First complete witness run: vector/ANN retrieval, translation residue. |
| `Physics-Witness-QRT-v0.1.md` | First physics witness run: quantum resource theory, translation residue. |

Every promoted witness should include native absorber citations, native state
completion tests, native theorem tests, control cases, residue label, and
falsification or demotion condition.

## Current Best Formulation

Capability Projection is projection sufficiency for typed capability objects.
For fixed observer, access profile, task family, horizon, admissible state set,
and resource boundary, a visible projection is sufficient exactly when the
declared capability object is determined by visible-state class, equivalently
when capability is constant over visible-equivalence fibers under the native
comparison on `K`.

Non-factorization is old. The proposed value is the audit discipline: type
`Cap`, declare visible and capability comparison, test capability spread,
identify capability-kernel quotients or native minimal objects, grant
neighboring theories their legitimate state and theorems, and record the
residue honestly.

Physics enters only through known physics inducing a typed capability object
under declared access and allowed operations. Capability language does not
derive physics.

The strongest next target is not another pair of states, but a minimality
theorem, canonical enrichment family, executable witness suite, typed
known-physics toy model, or cross-domain transfer theorem.

A witness should be demoted whenever a mature absorber supplies the relevant
state completion, theorem, comparison repair, threshold account, or
representation/gauge correction under the same declared audit context.
