# Candidate North Star v0.5: Projection Sufficiency For Typed Capability

**Draft author: Claude Sonnet 4.6 — June 20, 2026**
**This is one of two independent v0.5 drafts for synthesis. Do not treat as
canon until synthesis is complete.**

---

## Status

This is a Candidate North Star working draft.

It is not canon, does not replace `NORTH-STAR.md`, and is not a claim update,
roadmap commitment, paper-ready theorem, or evidence for a physics thesis.

This version patches v0.4 at five points (quotient-equality default, domain
calibration framing, approximate equivalence in checklist, appendix map as
burden table, per-witness falsifiability) and records the first two witness
runs.

## Executive Posture

The bare idea:

```text
observable equivalence is not necessarily capability equivalence
```

is old.

Many mature fields already study when projections, statistics, abstractions,
views, local states, summaries, measurements, or quotients lose
future-relevant distinctions.

The useful Candidate North Star is therefore not:

```text
projections can lose future capability
```

It is:

```text
a disciplined audit surface for typing capability objects, testing projection
sufficiency, recording prior-art absorption, and identifying any canonical
residue that survives.
```

## Governing Sentence

For fixed observer, task, horizon, and resource boundary:

```text
future capability need not factor through observer-visible state
```

Read this as:

```text
a projection-sufficiency question
```

not as:

```text
a metaphysical discovery
```

## Formal Core

Let:

```text
pi_{O,Sigma,r,U} : Y -> X_{O,Sigma,r}(U)
```

where:

- `Y` is the source state space or source structure;
- `X` is the observer-visible shadow;
- `O` is the observer or access profile;
- `Sigma` is the observational schema/interface;
- `r` is resolution, fidelity, or coarse-graining;
- `U` is the local domain, patch, scope, or access region.

Let:

```text
Cap_{O,T,h,B} : Y -> K_{O,T,h,B}
```

where:

- `T` is the task family;
- `h` is the horizon;
- `B` is the budget, boundary, or resource condition;
- `K` is the typed capability object.

Also declare:

```text
~=_X  visible-state equivalence
~=_K  capability equivalence
```

`~=_K` must be an equivalence relation for quotient language to apply. If the
native comparison is a preorder, tolerance, metric, or probabilistic criterion,
the audit must declare the induced equivalence used for quotienting.

The default equality relation is not "same payload" or "same current value."
Equality must be declared by the audit context.

## Capability Sufficiency

A projection:

```text
pi : Y -> X
```

is capability-sufficient for:

```text
Cap : Y -> K
```

when there exists:

```text
Cbar : X / ~=_X -> K
```

such that for every admissible `y`:

```text
Cap(y) ~=_K Cbar([pi(y)]_{~=_X}).
```

In plain language:

```text
the observer-visible state determines the declared capability object up to
the declared capability equivalence
```

The projection is capability-insufficient when there exist admissible `y1,y2`
such that:

```text
pi(y1) ~=_X pi(y2)
```

but:

```text
Cap(y1) not ~=_K Cap(y2).
```

Preferred terms:

- `capability-sufficient projection`;
- `capability-insufficient projection`;
- `projection-sufficiency failure`.

Avoid:

```text
capability-nonfaithful
```

unless a real functorial faithfulness condition is being used.

## Fiber-Constancy Lemma

Lemma:

```text
Cap factors through pi up to ~=_K iff Cap is ~=_K-constant on every pi-fiber.
```

Proof sketch:

If:

```text
Cap(y) ~=_K Cbar([pi(y)]_{~=_X})
```

then any `y1,y2` with `pi(y1) ~=_X pi(y2)` have equivalent `Cap` values
through the same visible equivalence class.

Conversely, if `Cap` is constant on each visible equivalence class, define
`Cbar([x]_{~=_X})` as the common `~=_K`-class of `Cap(y)` for any `y` with
`pi(y) ~=_X x`. Equivalence-class constancy makes this well-defined.

This lemma is not novelty evidence. It is the bookkeeping that prevents the
candidate from becoming vague.

## Minimal Capability-Preserving Quotient

Define:

```text
y1 ~_Cap y2 iff Cap(y1) ~=_K Cap(y2).
```

Then:

```text
Y / ~_Cap
```

is the coarsest quotient of `Y` that preserves the declared capability object.

A projection is capability-sufficient exactly when it does not identify source
states from distinct capability classes:

```text
if pi(y1) ~=_X pi(y2), then Cap(y1) ~=_K Cap(y2).
```

The strongest formal target is not another counterexample pair. It is a
domain-natural minimal capability-preserving quotient, or a useful family of
canonical enrichments that approximates one.

## Capability Spread

For a visible state `x`, define:

```text
Spread_Cap([x]_{~=_X}) =
  { Cap(y) | pi(y) ~=_X x } / ~=_K.
```

Then:

```text
Cap factors through pi iff Spread_Cap([x]_{~=_X}) is a singleton for every
visible equivalence class.
```

The source fiber:

```text
{ y | pi(y) ~=_X x }
```

is not itself the capability. The audit object is the spread of capability
values across that fiber.

Possible finite summaries:

```text
ambiguity_Cap(x) = |Spread_Cap(x)|
diameter_Cap(x) = diameter(Spread_Cap(x))
```

when `K` has suitable finite, metric, or order structure.

## Capability Type Gate

No witness should be considered until `K` is typed.

Common `K` types:

- set of answers;
- set of admissible operations;
- preorder of admissible future operations;
- decision-value, risk, or loss object;
- provenance or lineage object;
- behavioral equivalence class;
- testing capability or distinguishing formula class;
- resource convertibility structure;
- reachable or viable set;
- causal intervention query class;
- database workload or rewritability object;
- approximate retrieval envelope;
- physics-facing accessibility structure.

Rule:

```text
Capability equivalence must be domain-native, task-natural, and fixed before
witness construction.
```

## Absorption Protocol

Prior art can absorb a witness in two ways.

### State-Enrichment Absorption

The neighboring field's legitimate state distinguishes the cases, restores
factorization, or shows that the original projection was underdescribed.

Examples:

- belief state;
- provenance graph;
- commit DAG;
- transaction log;
- version vector;
- causal graph;
- resource monotone;
- purifier or environment access;
- index/materialization state.

### Native-Theory Absorption

The neighboring field already has the theorem, schema, equivalence hierarchy,
or completeness criterion that explains the non-factorization.

Examples:

- Blackwell/Le Cam for decision sufficiency;
- process semantics for observational equivalence and distinguishing tests;
- abstract interpretation for incomplete abstractions;
- resource theory for convertibility;
- database view determinacy;
- causal inference for observational versus interventional equivalence;
- control theory for observability and reachability.

Formal or canonical residue must survive both forms.

## Trivial Enrichment Theorem

For any:

```text
pi : Y -> X
Cap : Y -> K
```

define:

```text
pi'(y) = (pi(y), Cap(y)) : Y -> X x K.
```

Then `Cap` factors through `pi'`.

Consequence:

```text
Every projection-sufficiency failure can be repaired by enriching visible
state with the capability object itself.
```

Therefore, the research question is not whether enrichment can restore
factorization. It is whether the enrichment is:

- domain-natural;
- minimal;
- canonical;
- operationally available;
- already standard in the neighboring theory.

## Failure Labels

Use these labels during review.

```text
under_typed
```

`K`, `Cap`, `~=_K`, or required indices are not fixed.

```text
same_visible_state_underspecified
```

The equality of visible states lacks the observer/schema/resolution/domain,
snapshot, access, or equivalence context needed to evaluate the witness.

```text
projection_underdescribed
```

The projection is defined, but it omits native state data that the domain
standardly treats as relevant for the task.

```text
gerrymandered_capability
```

`Cap` is technically predeclared but not operationally natural, canonical, or
native to the domain.

Physics-specific labels:

```text
no_free_physics_violation
access_profile_underdeclared
gauge_variant_capability
local_capability_smuggling
physics_direction_reversal
typed_model_missing
```

## Residue Ladder

A proposed witness fails projection-sufficiency if a mature absorber supplies
a natural sufficient enrichment or quotient under the declared audit context.

### 1. Canonical Residue

The strongest target.

Use only when:

- the witness survives state-enrichment absorption;
- the witness survives native-theory absorption;
- `Cap` is domain-natural or operationally forced;
- the relevant quotient or enrichment is minimal or canonical in the native
  field;
- the projection is not obviously impoverished;
- the result reveals an unavoidable tradeoff across observer, task, horizon,
  and resource boundary.

### 2. Formal Residue

A typed distinction survives tested prior-art absorption as a clean formal
object, lemma, quotient, metric, or audit criterion, but canonicity is not
yet established.

### 3. Translation Residue

No new formal phenomenon survives, but the audit surface aligns mature
theories usefully.

### 4. Heuristic Residue

The language helps find missing state, access, provenance, policy, resource,
or observer data.

### 5. Redundant Or Demoted

The vocabulary duplicates prior art or adds confusion without improving
comparison, reviewability, or witness triage.

Default expectation:

```text
translation residue or heuristic residue
```

not:

```text
canonical residue
```

## Witness Record

Both witnesses run to date returned Translation Residue.

```text
Vector/ANN retrieval (HNSW vs IVFFlat, same corpus): translation residue.
  Failure label: projection_underdescribed.
  Absorbed by: state-enrichment (add index family + params) and native theory
  (ANN-Benchmarks / Faiss treat recall-latency-accuracy as the primary object).
  Companion: Witness-Run-VectorANN-v0.1.md

Quantum resource theory (singlet vs product state, same rho_A = I/2): translation
  residue.
  Absorbed by: state-enrichment (add full bipartite state rho_AB) and native
  theory (QRT owns all convertibility theorems).
  No-free-physics template fills without strain. QRT as strongest physics-anchor
  domain is confirmed, but at translation residue only.
  Companion: Physics-Witness-QRT-v0.1.md
```

The audit instrument works: it correctly identifies and labels absorption. The
path to formal or canonical residue requires a cross-domain transfer theorem
or a minimality result that is not yet in hand.

## Success Criteria

Success would be one or more of:

- a canonical-residue witness;
- a transfer theorem or reusable audit pattern across at least two mature
  fields;
- a finite executable suite with preservation controls and non-factorization
  fixtures;
- an audit template that catches false witness claims;
- a physics-facing typed toy model deriving `Cap` from known physics;
- a small canonical enrichment family that restores factorization across
  domains.

Success is not another easy same-`pi` / different-`Cap` pair.
Translation Residue is an honest outcome, not a failure of the instrument.

## Failure Criteria

The candidate weakens or dissolves if:

- every domain-natural witness is absorbed by legitimate state enrichment or
  native theory;
- no `Cap` object remains domain-natural after equivalence is declared;
- finite pair tests remain self-inflicted projection loss;
- physics sections remain analogy rather than typed known-physics audits;
- no useful transfer appears across mature fields;
- the vocabulary duplicates existing frameworks without improving comparison,
  reviewability, or witness triage.

Failure is acceptable. Record it as translation residue, heuristic residue,
redundancy, or demotion.

## Reviewer Checklist

Before promoting any witness, ask:

```text
Y declared?
X declared?
pi declared?
visible equivalence ~=_X declared?
K typed?
Cap declared before the witness?
capability equivalence ~=_K declared?
observer/task/horizon/boundary fixed?
projection meaningful?
same-visible-state context fixed?
projection underdescribed?
Cap domain-natural?
Cap non-gerrymandered?
positive preservation control supplied?
negative non-factorization fixture supplied?
fiber spread singleton or non-singleton?
minimal capability-preserving quotient identified?
trivial/native enrichment tested?
state-enrichment absorption tested?
native-theory absorption tested?
residue label honest?
if approximate: epsilon/top-k/recall/workload equivalence declared?
```

Physics addendum:

```text
known physics induces Cap?
physical access profile declared?
allowed operations declared?
gauge/relabeling invariance respected?
strictly local controls included where relevant?
not-claimed boundary explicit?
```

## Domain Calibration

Domain sections are calibration gates. Strong absorption in a domain is
expected; the question is whether any formal or canonical residue survives
after absorption.

Pattern:

```text
Domain:
Native absorber:
Canonical K candidate:
Preservation control:
Non-factorization fixture:
Likely residue:
```

### Databases

Native absorber:

```text
view/query determinacy, provenance, temporal semantics, access control,
index/materialization state, distributed consistency, approximate retrieval
```

Canonical `K` candidates:

- query/workload answer object;
- provenance object;
- recovery/replay capability;
- access-policy operation set;
- latency/recall envelope.

Likely residue:

```text
translation or heuristic; approximate/workload-bounded cases are strongest
```

Witness run: vector/ANN returned translation residue (projection_underdescribed).
Path to formal residue: minimality theorem across ANN algorithm families.

### Decision / Control / Causal Inference

Native absorber:

```text
Blackwell sufficiency, belief-state sufficiency, observability,
reachability, interventional identifiability
```

Canonical `K` candidates:

- value/risk object;
- reachable set;
- intervention query class;
- policy capability.

Likely residue:

```text
translation unless a cross-domain transfer theorem appears
```

### Process Semantics / Computation

Native absorber:

```text
testing equivalence, bisimulation, trace/failure/readiness semantics,
Nerode-style quotients
```

Canonical `K` candidates:

- future tests passed;
- behavioral equivalence class;
- continuation-distinguishability structure.

Likely residue:

```text
translation or formal residue only if a new audit transfer is proven
```

### Resource And Physics-Facing Domains

Native absorber:

```text
resource theory, causal structure, thermodynamics, gauge theory, EFT/RG,
topological response, detector metrology
```

Canonical `K` candidates:

- convertibility preorder;
- causal accessibility structure;
- thermodynamic work/resource envelope;
- detector audit/reconstruction rights;
- topological response operation structure.

Likely residue:

```text
translation or typed toy-model residue; physics-bearing residue is long-horizon
```

Witness run: QRT returned translation residue. No-free-physics template
confirmed fillable. GR causal accessibility is the next-strongest physics
candidate.

## No-Free-Physics Rule

Physics sections remain strong, but every physics-facing claim must derive
`Cap` from known physics.

Use this template:

```text
Known theory:
Y:
X:
pi:
Cap:
K:
Equivalence on K:
Allowed operations:
Observer/access profile:
Horizon/resource boundary:
Factorization question:
Native absorber:
Not claimed:
```

Required direction:

```text
known physics -> induced Cap -> projection sufficiency audit
```

Forbidden direction:

```text
Cap -> known physics
```

unless future theorems justify it.

Physics access profiles must specify physical access: local measurements,
detector readout, environment/purifier access, joint operations, asymptotic
data, exterior-domain access, causal-past access, finite-energy operations,
finite-time operations, apparatus resolution, communication, or allowed
intervention class.

Strictly local observers cannot be credited with global, purifier,
environment, horizon-exterior/interior, or asymptotic capability unless the
access profile grants a physical route to that structure.

Gauge/relabeling invariance:

```text
Cap(g.y) ~=_K Cap(y)
```

for pure gauge, coordinate, phase-convention, basis, or representational
redundancy transformations `g`.

## Physics Witness Posture

Promote as strong physics-facing anchors:

- quantum resource theory under explicit access profiles;
- GR causal accessibility and horizons;
- detector/instrumentation provenance;
- thermodynamic resource convertibility;
- condensed matter/topological response;
- simulation restart/reconstruction/provenance;
- EFT/RG preservation controls.

Hold or narrow:

- Standard Model / particle properties as constraints on admissible
  interactions;
- black holes as observer-indexed access stress tests;
- time as capability trajectories along physical time, not replacement time;
- emergence as platform capability with losses and tradeoffs, not universal
  expansion.

Demote unless typed models exist:

- dark matter;
- dark energy.

Dark matter is a heuristic projection-insufficiency analogy unless written as
a typed gravitational-dynamics audit. Dark energy is a future-causal-access
analogy unless written as a typed cosmological accessibility audit.

## Relationship To TaF

Capability Projection remains adjacent to the existing TaF North Star.

It can help organize:

- records;
- finality;
- observer-accessible sections;
- reconstruction debt;
- detector packets;
- LossKernel;
- typed forgetting;
- future operation availability;
- maintenance viability.

It should not replace the current North Star unless later work shows
canonical residue that survives mature absorption.

## Collapse Condition

If every important witness is absorbed by state enrichment or by a native
prior-art theorem/schema, record:

- translation residue;
- heuristic residue;
- redundancy;
- demotion.

The purpose is discovery, not defense.

## Appendix Map

| Companion report | Burden it carries |
|---|---|
| `Capability Projection Schema v0.1.md` | Full formal schema with extended type definitions |
| `Database Absorption Test for Capability Projection-deep-research-report.md` | Database-domain absorption: view determinacy, provenance, MVCC, approx retrieval |
| `Prior-Art Audit of Capability Projection-deep-research-report.md` | Cross-domain prior art: Blackwell, process semantics, abstract interpretation, resource theory, causal inference |
| `Candidate North Star Mathematical Strengthening Suggestions v0.1.md` | Open mathematical questions and hardening suggestions |
| `Candidate North Star 20 Mathematics Perspectives Report v0.1.md` | 20 mathematics-domain perspective reviews |
| `Candidate North Star 20 Physics Perspectives Report v0.1.md` | 20 physics-domain perspective reviews (written against v0.2; check physics-direction claims against v0.4 no-free-physics rule) |
| `Candidate North Star Low-Hanging Dispatch Synthesis v0.1.md` | Synthesis of low-hanging patch pass that shaped v0.4 |
| `Witness-Run-VectorANN-v0.1.md` | First complete witness run: vector/ANN retrieval, translation residue |
| `Physics-Witness-QRT-v0.1.md` | First physics witness run: quantum resource theory, translation residue |

The main note stays compact enough to function as a reviewable audit
specification. Domain depth, witness banks, prior-art inventories, and physics
expansions live in companion reports.

## Current Best Formulation

The strongest v0.5 formulation is:

> Capability Projection is projection sufficiency for typed capability
> objects. A projection is sufficient exactly when the declared capability
> object factors through it, equivalently when capability is constant over
> visible-state fibers. Non-factorization is old. The useful work is typing
> `Cap`, declaring equivalence, checking fiber-constancy, identifying minimal
> capability-preserving quotients, testing enrichments and absorbers, and
> recording whether formal or canonical residue remains.
>
> The audit instrument has now been run. Two witnesses — vector/ANN retrieval
> and quantum resource theory — both returned Translation Residue after honest
> absorption testing. The instrument correctly labels absorption. The path to
> formal or canonical residue requires a cross-domain transfer theorem or a
> minimality result not yet in hand.
>
> Physics enters only by deriving capability objects from known physics and
> then auditing observer-facing projections. It does not derive physics from
> capability. The no-free-physics template is confirmed fillable.
