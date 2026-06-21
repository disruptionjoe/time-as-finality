# Candidate North Star v0.3: Capability Projection As Audit Surface

## Status

This is a Candidate North Star working draft.

It is not canon.
It does not replace `NORTH-STAR.md`.
It is not a claim update.
It is not a roadmap commitment.
It is not paper-ready.
It is not a theorem.
It is not evidence for a physics thesis.

This version integrates:

- `Candidate North Star v0.2.md`;
- `Capability Projection Schema v0.1.md`;
- `Database Expert Lens Review v0.1.md`;
- `Database Absorption Test for Capability Projection-deep-research-report.md`;
- `Prior-Art Audit of Capability Projection-deep-research-report.md`;
- `Strongman for physics sections.md`;
- `Fresh-Eyes Review Needed Updates v0.1.md`;
- `Candidate North Star v0.3 Synthesis Plan.md`.

## Executive Posture

The bare slogan:

```text
observable equivalence is not necessarily capability equivalence
```

is not novel as a mathematical idea.

Many mature fields already know that projections, observations, abstractions,
views, local states, or summaries can lose future-relevant distinctions.

The live question is narrower and more useful:

```text
Can one indexed audit surface compare when projections preserve or destroy
future capability across decision theory, process semantics, abstract
interpretation, databases, control, resource theories, causal inference,
physics-facing accessibility, and repo-native record/provenance work?
```

The Candidate North Star survives only as:

```text
a disciplined cross-domain audit language
```

unless a witness survives mature prior-art absorption using a domain-natural
capability object.

## Governing Sentence

For fixed observer, task, horizon, and resource boundary:

```text
future capability need not factor through observer-visible state
```

Equivalent compact form:

```text
observable equivalence is not necessarily capability equivalence
```

But the guardrail is now stronger:

```text
a non-factorization verdict is a projection-sufficiency failure,
not a metaphysical discovery
```

and:

```text
projection-sufficiency failure is old;
the possible contribution is disciplined comparison, typing, absorption, and
canonical residue testing
```

## Formal Core

Let:

```text
pi_{O,Sigma,r,U} : Y -> X_{O,Sigma,r}(U)
```

where:

- `Y` is a richer source structure;
- `X_{O,Sigma,r}(U)` is the observer-visible shadow over domain `U`;
- `O` is the observer or access profile;
- `Sigma` is the observational schema or interface;
- `r` is resolution, fidelity, or coarse-graining;
- `U` is the local domain, patch, or scope.

Let:

```text
Cap_{O,T,h,B} : Y -> K_{O,T,h,B}
```

where:

- `T` is the task family;
- `h` is the horizon;
- `B` is the budget, boundary, or resource condition;
- `K` is the typed capability structure.

The audit question is:

```text
Does Cap factor through pi up to the declared capability equivalence on K?
```

That is, does there exist:

```text
Cbar : X_{O,Sigma,r}(U) -> K_{O,T,h,B}
```

such that:

```text
Cap_{O,T,h,B}(y) ~=_K Cbar(pi_{O,Sigma,r,U}(y))
```

for every admissible source state `y`?

Finite pair witness:

```text
pi(y1) = pi(y2)
```

but:

```text
Cap(y1) not ~=_K Cap(y2)
```

Fiber-constancy form:

```text
Cap factors through pi up to equivalence iff Cap is equivalent-constant on
every pi-fiber.
```

This is the minimal mathematical skeleton. It is also why the idea is easy to
absorb: many fields already study when a projection, view, statistic,
abstraction, observation, or quotient is sufficient for a downstream property.

## Capability Type Gate

No witness should be considered until `K` is declared.

Possible `K` types include:

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

Capability equivalence must be:

```text
domain-native
task-natural
declared before witness construction
```

Examples of equivalence:

- exact equality;
- mutual reachability;
- order equivalence;
- policy/value equivalence;
- Blackwell equivalence or deficiency tolerance;
- bisimulation or testing equivalence;
- complete-abstraction equivalence;
- resource interconvertibility;
- same provenance object up to isomorphism;
- same viable/reachable set;
- same top-k up to ranking tolerance;
- recall@k within epsilon;
- latency/recall envelope equivalence.

Failure label:

```text
gerrymandered_capability
```

Use it when `Cap` is technically predeclared but not operationally natural,
canonical, or native to the domain.

## Prior Art First

The Candidate North Star is surrounded by strong absorbers.

### Statistical Decision Theory

Blackwell comparison of experiments, the Blackwell-Sherman-Stein theorem,
garbling, sufficiency, and Le Cam deficiency already formalize when one
information structure is as useful as another for decision problems.

If the claim means:

```text
a projection may fail to preserve downstream decision value
```

then the core is already absorbed.

Candidate residue would require a useful translation between decision
sufficiency and other capability notions, not a rediscovery of insufficiency.

### Concurrency And Process Semantics

Process semantics already studies observational equivalence by discrimination
power:

- trace equivalence;
- failures semantics;
- readiness and ready-trace semantics;
- may/must testing;
- branching bisimulation;
- Hennessy-Milner-style modal logics;
- van Glabbeek's linear-time/branching-time spectrum.

In this setting, a finite pair witness is a distinguishing test or formula.

This is a major absorber for any claim about:

```text
same observation
different future-discriminating power
```

### Abstract Interpretation And Complete Abstractions

The factorization diagram is standard abstraction machinery.

Abstract interpretation asks whether an abstraction is sound and when it is
complete for a property or transformer. Incompleteness is exactly the failure
of an abstract view to preserve relevant concrete behavior.

Candidate residue would require a new useful capability abstraction or a
cross-domain translation result, not merely a failed abstraction.

### POMDPs And Belief-State Sufficiency

POMDPs already show:

```text
raw observation is generally not sufficient for future control
belief state may be sufficient
```

So partial-observation examples are absorbed unless the candidate contributes
new cross-domain alignment or a nonstandard capability object.

### Resource Theory

If capability means:

```text
what can be converted into what under allowed operations
```

then resource theory is the strongest native home. Convertibility preorders
and monotones already give a capability-like structure.

### Causal Inference And Control

Causal inference distinguishes observational from interventional equivalence.
Control theory distinguishes output equality from observability,
controllability, reachability, and estimation.

These fields already own many instances of:

```text
same visible behavior
different intervention or reachability capability
```

### Databases

Database systems give the cleanest finite executable absorber.

Let:

```text
Y = full database state
pi = view, projection, materialized snapshot, index, API surface, or visible result
Cap = query, workload, recovery operation, audit right, update right,
      retrieval behavior, or policy-evaluable object
```

Then:

```text
Cap factors through pi
```

means:

```text
the visible database surface determines the declared capability under the
declared constraints and workload
```

This is absorbed in many cases by:

- view/query determinacy;
- monotone determinacy and rewritability;
- dependencies and lossless decomposition;
- incomplete information and certain answers;
- provenance and lineage;
- temporal databases and MVCC;
- access control;
- materialized views and indexes;
- OLAP cubes and continuous aggregates;
- graph/RDF semantics;
- distributed consistency metadata;
- vector/ANN retrieval envelopes.

Database examples are excellent witnesses and controls. They are not novelty
evidence by default.

## Two Forms Of Absorption

Prior art can absorb a witness in two ways.

### 1. State-Enrichment Absorption

The neighbor's legitimate state distinguishes the cases, restores
factorization, or shows that the original projection was underdescribed.

Examples:

- POMDP belief state;
- provenance graph;
- commit DAG;
- transaction log;
- version vector;
- causal graph;
- purifier/global access profile;
- resource monotones;
- index/materialization state.

### 2. Native-Theory Absorption

The neighbor already has the theorem, schema, equivalence hierarchy, or
completeness criterion that explains the non-factorization.

Examples:

- Blackwell/Le Cam for decision sufficiency;
- process semantics for observational equivalence and distinguishing tests;
- abstract interpretation for incomplete abstractions;
- resource theory for convertibility;
- database view determinacy;
- causal inference for observational versus interventional equivalence.

Formal residue requires surviving both.

## Finite Pair Test: Necessary But Weak

A finite same-`pi` / different-`Cap` pair proves only:

```text
the chosen projection does not determine the chosen capability
```

It does not prove:

```text
formal novelty
```

or:

```text
deep hidden structure
```

A witness is interesting only if:

- `Cap` is domain-natural;
- the projection is operationally meaningful;
- the task family is not gerrymandered;
- equivalence on `K` is justified by the domain;
- obvious enrichment allowed by the neighbor has been tested;
- the neighbor does not already contain the native theorem explaining the
  failure.

Relevant comparison standards:

- minimal sufficient statistic;
- coarsest adequate quotient;
- fully abstract semantics;
- Nerode congruence;
- quotient by bisimulation;
- minimal predictive causal state;
- complete abstract domain.

## Same-Visible-State Discipline

Equality of visible state must be indexed.

Failure label:

```text
same_visible_state_underspecified
```

Use it when a witness says:

```text
same payload
same current value
same visible result
same top-k result
same local patch
```

without declaring the context needed for equality.

Database cases must declare, when relevant:

- schema;
- constraints;
- view definitions;
- query/view language;
- transaction time;
- valid time;
- isolation level;
- snapshot timestamp;
- provenance/lineage regime;
- index/materialization state;
- refresh or retention policy;
- access policy;
- consistency model;
- causal metadata;
- embedding model;
- distance metric;
- chunking strategy;
- metadata filters;
- workload distribution;
- approximation tolerance;
- resource budget.

Physics cases must declare, when relevant:

- observer/access profile;
- local patch or causal domain;
- measurement interface;
- global versus local state;
- allowed operations;
- horizon;
- resource constraints;
- equivalence on future operations.

## Residue Ladder

### 1. Canonical Residue

Strongest target.

A witness has canonical residue only if:

- it survives same-neighbor-data testing;
- it survives native-theory absorption;
- `Cap` is domain-natural or operationally forced;
- the projection is not an obviously impoverished state description;
- the result reveals an unavoidable tradeoff across observer, task, horizon,
  and resource boundary.

### 2. Formal Residue

A typed distinction survives prior-art absorption, but canonicity is not yet
established.

### 3. Translation Residue

No new formal phenomenon survives, but the schema aligns several mature
theories under one audit surface.

This is the current default expectation.

### 4. Heuristic Residue

The language helps discover missing state, access, provenance, resource,
policy, or observer data, even though the final explanation belongs to known
theory.

### 5. Redundant Or Demoted

The vocabulary adds confusion or duplicates an existing framework without
useful translation value.

## Database Witnesses And Controls

Database examples should be used as finite fixtures.

### Preservation Controls

Examples where `Cap` should factor through `pi`:

- full table projection determines full-table queries;
- materialized sum determines a declared sum workload;
- OLAP rollup determines the aggregate workload it was built for;
- sufficient index determines lookup capability for its declared key workload;
- full event log determines replay/recovery capability;
- full provenance graph determines declared provenance audit workload;
- full vector index state determines declared ANN behavior under declared
  tolerance.

### Non-Factorization Fixtures

Event log:

```text
Y = event log
pi(log) = materialized current state
Cap(log) = replay, audit, compensation, or reconstruction operations
```

MVCC / bitemporal:

```text
Y = versioned table plus transaction-time history
pi = current visible snapshot
Cap = rollback, audit, or time-travel query capability
```

OLAP:

```text
pi = daily revenue rollup
Cap_1 = total daily revenue query
Cap_2 = median transaction value or subgroup attribution query
```

Expected:

```text
Cap_1 factors
Cap_2 may not
```

Vector / ANN:

```text
Y = corpus + embedding model + index state + search parameters + budget
pi = visible corpus or sample top-k result
Cap = recall@k / latency / filtered retrieval envelope over future workload
```

This is one of the least-absorbed database zones because capability is
approximate, workload-bounded, policy-sensitive, consistency-sensitive, and
resource-bound.

## Physics-Forward Strongman

Physics sections are not evidential support.

They are typed strongman instantiations of the schema:

```text
Known physics
Y
X
pi
Cap
K
equivalence
non-factorization question
what would support it
what would kill it
absorber
not claimed
```

The point is:

```text
be bold, but not incorrect
```

### Gravity

Known physics:

General relativity ties causal accessibility to spacetime geometry.

Candidate instantiation:

```text
Y = spacetime plus metric, stress-energy, and global causal structure
X = local observer-visible measurement data over patch U
pi = restriction to local observables
Cap = future-directed causal curves, communication possibilities,
      measurement trajectories, and reachable domains
K = causal-accessibility / reachability structure
equivalence = same observer-indexed reachable causal futures under declared
              horizon and resource constraints
```

Steelman:

Two locally similar visible patches may sit inside globally different causal
structures, so their future accessible domains differ. Gravity is a domain
where future capability is naturally encoded by causal geometry.

Support would be a typed pair or theorem where local observational equivalence
does not determine the relevant causal-accessibility structure.

Killed or absorbed by standard GR causal structure if the point is only:

```text
geometry constrains causal futures
```

Not claimed:

```text
capability explains gravity
```

### Quantum Theory

Known physics:

Local reduced states can hide purification, entanglement, and resource
structure, but access determines operational availability.

Candidate instantiation:

```text
Y = global quantum state plus purification/environment/resource structure
X = reduced local state available to observer O
pi = partial trace or restricted measurement interface
Cap = operations available under allowed channels, LOCC, side access,
      purifier access, or resource conversion
K = operational/resource-theoretic convertibility structure
equivalence = same convertibility or same achievable protocol class under
              declared allowed operations
```

Steelman:

Same reduced state can hide different global resources. For a strictly local
observer those differences may be unavailable; for an observer with side
access, purifier access, or joint operations, they can change future
operations.

Not claimed:

```text
same reduced density matrix always implies different strictly local capability
```

Likely absorber:

Quantum information and quantum resource theory.

### Standard Model / Particle Structure

Known physics:

Charge, spin, mass, chirality, phase, gauge representation, and selection
rules constrain possible interactions.

Candidate instantiation:

```text
Y = field, representation, gauge, phase, and internal quantum-number structure
X = observed particle event or local detector signature
pi = readout/coarse-graining to observed event
Cap = allowed interactions, couplings, transformations, scattering channels,
      conserved quantities, and selection rules
K = admissible-interaction / transformation structure
equivalence = same allowed interaction class under declared theory and energy
              regime
```

Steelman:

Same spacetime localization is not enough. Internal representation data changes
which interactions are possible.

Not claimed:

```text
charge, spin, or mass are capability
```

Likely absorber:

Standard Model representation and gauge theory.

### Black Holes

Known physics:

Horizons are causal boundaries that make observer location and access profile
mathematically unavoidable.

Candidate instantiation:

```text
Y = global spacetime including horizon structure and interior/exterior causal
    relations
X = exterior observer-accessible data
pi = restriction to exterior causal domain
Cap = reconstruction, communication, intervention, retrieval, and
      verification operations available to an observer
K = observer-indexed operation availability across a horizon
equivalence = same recoverable/signallable/verifiable operation set under
              declared observer and horizon
```

Steelman:

A horizon is a precise boundary in future operation availability. It separates
global structure from what a given observer can signal, reconstruct, verify, or
act upon.

Not claimed:

```text
capability solves the information problem
```

Likely absorber:

Standard horizon, causal-access, and reconstruction language.

### Cosmology And Dark Energy

Known physics:

Expansion history and accelerated expansion affect large-scale causal
accessibility and event horizons.

Candidate instantiation:

```text
Y = global cosmological spacetime with expansion history
X = observer-visible cosmological data within a horizon
pi = restriction to causal past/future accessible region
Cap = future causal contact, observation, communication, and
      structure-formation possibilities
K = long-horizon causal-contact / reachability structure
equivalence = same future accessible domains under declared cosmology and
              observer location
```

Steelman:

Expansion changes which future regions remain causally accessible. Accelerated
expansion can shrink long-run interaction capability even as spatial scale
grows.

Not claimed:

```text
capability explains dark energy
```

Likely absorber:

Cosmological horizon and causal-access theory.

### Dark Matter

Known physics:

Electromagnetically visible matter does not determine all gravitationally
relevant source structure.

Candidate instantiation:

```text
Y = full gravitational source structure
X = luminous/electromagnetic visible matter distribution
pi = projection to visible matter
Cap = gravitationally allowed trajectories, binding, lensing, rotation
      behavior, and structure formation
K = gravitational-dynamical consequence structure
equivalence = same dynamical/lensing/structure-formation consequences under
              declared model
```

Steelman:

Dark matter shows that visible luminous state is not a sufficient invariant for
gravitational futures. The hidden structure is not capability, but it changes
future dynamical possibilities.

Not claimed:

```text
dark matter is hidden capability
capability explains dark matter
```

Disposition:

Heuristic analogy unless a much stronger typed result is produced.

### Time

Known physics:

Relativity and thermodynamics already govern temporal order and physical
arrows.

Candidate instantiation:

```text
Y = physical system plus records, resources, boundary conditions, and dynamics
X = observer-visible present records or coarse state
pi = projection to current observer-visible state
Cap = future admissible operations, reversibility, reconstruction, erasure,
      maintenance, and intervention possibilities
K = resource-indexed future-operation structure
equivalence = same future operation structure under declared openness,
              coarse-graining, and resource accounting
```

Steelman:

Projected visible state may remain fixed while future-operation structure
changes inside the projection fiber. A capability theory of time must name the
openness, resource, erasure, boundary, coarse-graining, or nonstationarity that
makes directionality appear.

Not claimed:

```text
observers create time
capability replaces physical time
closed reversible systems generate strict finality arrows
```

### Emergence

Known neighbors:

Viability theory, affordance theory, niche construction, major transitions,
constructor theory, and resource theory.

Candidate instantiation:

```text
Y = multiscale system with structures, constraints, maintenance costs, and
    environmental couplings
X = observer-visible coarse structure
pi = coarse-graining to present structure
Cap = future structures, transformations, maintenance, reproduction,
      reconstruction, and platform operations made available
K = viability/resource/affordance/platform structure
equivalence = same preserved or expanded future-operation class under declared
              environment and budget
```

Steelman:

Emergent structures can become platforms that preserve, expand, restrict, or
redirect future capability.

Not claimed:

```text
all emergence is capability expansion
```

Likely disposition:

Potentially strong translation layer, novelty uncertain.

## Relationship To TaF

The existing TaF North Star protects an intuition about records,
stabilization, observer-accessible sections, finality, and possible relations
between time and recursively nested record structures.

Capability Projection is adjacent. It asks when an observer-facing record,
shadow, view, or projection preserves future admissible operations.

It can help organize:

- reconstruction debt;
- observer access;
- provenance and authority;
- future operation availability;
- typed forgetting;
- LossKernel attribution;
- detector packets;
- maintenance viability.

It should not replace the current North Star unless later work shows canonical
residue that is not already absorbed by the mature neighbors above.

## Collapse Condition

The candidate weakens or dissolves if:

```text
every important witness is absorbed by state enrichment or by a native
prior-art theorem/schema
```

In that case, record the result as:

- translation residue;
- heuristic residue;
- redundant vocabulary;
- demoted material.

That outcome is acceptable.

The purpose is discovery, not defense.

## Current Best Formulation

The strongest v0.3 formulation is:

> For fixed observer, task, horizon, and resource boundary, future capability
> need not factor through observer-visible state.
>
> This failure of factorization is not novel by itself. It is already native to
> decision theory, process semantics, abstraction theory, control, resource
> theory, causal inference, databases, and quantum information.
>
> The useful project is to type `Cap`, declare capability equivalence, test
> factorization, grant each neighbor its legitimate state and native theory,
> and record whether any canonical residue remains.
>
> Physics-facing sections should instantiate the same schema boldly but
> non-promotionally: known physics first, typed `Y/X/pi/Cap/K` second,
> absorber and falsifier third.

Operational form:

```text
type Cap
declare equivalence
test fiber constancy
check canonicity
grant prior art legitimate state
check native-theory absorption
record the residue honestly
```

