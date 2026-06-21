# Candidate North Star Next Version Update Queue v0.3

## Status

This is a pending-update queue for the next Candidate North Star version.

Do not treat this as the next version.
Do not promote these updates to canon.
Do not edit `Candidate North Star v0.2.md` from this file alone.

Purpose:

```text
Collect required changes discovered from Database Expert Lens Review v0.1 and
the follow-up absolute adjustments, plus later inputs, so they can be
integrated into the next Candidate North Star version.
```

Current drafting gate:

```text
The final pending deep research report has arrived.
Update and synthesize this queue before drafting Candidate North Star v0.3.
Use a fresh-eyes review before finalizing the draft.
```

Additional inputs now included:

- `Strongman for physics sections.md`;
- `Database Absorption Test for Capability Projection-deep-research-report.md`.
- `Prior-Art Audit of Capability Projection-deep-research-report.md`.

## Executive Summary

The next version must lower the novelty posture around database examples.

The final prior-art audit requires an even broader novelty downgrade:

```text
The core sentence is not novel as a mathematical idea.
Capability Projection is currently best understood as a translation surface
over several mature theories, not as a new North Star theorem.
```

Primary absorbers now include:

- statistical decision theory, Blackwell comparison of experiments, and Le Cam
  deficiency;
- concurrency/process semantics, testing equivalences, bisimulation, and
  observational-power spectra;
- abstract interpretation, Galois abstraction, completeness of abstractions,
  and quotient adequacy;
- POMDP belief-state sufficiency;
- resource-theory convertibility;
- causal inference and observational/interventional equivalence;
- control observability, controllability, and reachability;
- database view/query determinacy and related database-state theories.

The next version should therefore treat the governing sentence as:

```text
a useful cross-domain audit question
```

not:

```text
a new theorem or newly discovered mathematical phenomenon
```

Database systems do not falsify the Candidate North Star, but they absorb much
of its current shape. In database language, the core factorization question is
very close to:

```text
view/query determinacy
```

or:

```text
does a declared query, workload, recovery operation, audit right, update right,
retrieval behavior, or policy-evaluable object factor through a declared view,
projection, materialized snapshot, index, API surface, or visible state?
```

Therefore, database examples should be used primarily as:

- finite witnesses;
- preservation controls;
- audit-template discipline;
- translation residue;
- heuristic residue.

They should not be presented as evidence of formal novelty unless they survive
same-neighbor-data testing after database-native state is fully admitted.

At the same time, the next version must not make the physics sections timid.
The current v0.2 physics posture is rigorous in a defensive audit sense, but
not yet rigorous in the physics-forward strongman sense. The next version
should keep the guardrails while upgrading each physics-facing section into a
typed instantiation of the schema:

```text
Y
X
pi
Cap
K
equivalence on K
non-factorization question
known absorber
what would count as support
what would kill it
```

The intended posture is:

```text
be bold, but not incorrect
refine, but do not soften
physics as steelman, not just safety label
```

## Required Updates

## 0. Close The No-Redraft Gate And Require Final Integration

Replace the previous no-redraft gate with:

```text
The final prior-art deep research report is now in.
Candidate North Star v0.3 may be drafted only after this queue is synthesized
and the fresh-eyes review is reconciled.
```

Rationale:

The queue has functioned as the integration buffer. It now needs to become the
source of truth for the next draft.

## 0A. Downgrade The Core Novelty Claim Across The Whole Draft

The final prior-art audit says the central slogan is already absorbed by
mature traditions.

Required stance:

```text
Observable equivalence is not necessarily capability equivalence is not novel
as a mathematical idea. The live question is whether the project can build a
useful indexed translation surface and audit discipline across mature
formalisms.
```

The next version should avoid any implication that projection losing
future-relevant information is a new phenomenon.

Replace novelty-leaning language with:

```text
Capability Projection is a candidate cross-domain comparison framework.
It may become valuable if it aligns sufficiency, testing/bisimulation,
belief-state reduction, resource convertibility, causal/interventional
distinguishability, database determinacy, and physics-facing accessibility
under one disciplined indexed audit.
```

## 0B. Add The New Primary Prior-Art Triad

Add these as top-tier absorbers before or alongside database theory.

### Statistical Decision Theory

Required concepts:

- Blackwell comparison of experiments;
- Blackwell-Sherman-Stein theorem;
- garbling;
- Le Cam deficiency;
- task-relative sufficiency versus all-decision-problem sufficiency.

Required safe wording:

```text
If the governing sentence is read as "a projection may fail to preserve all
downstream decision value," then statistical decision theory already absorbs
the core idea. The Candidate North Star must therefore state whether it is
working task-relatively, universally over a task family, or only as translation
language.
```

### Concurrency And Process Semantics

Required concepts:

- van Glabbeek linear-time/branching-time spectrum;
- De Nicola-Hennessy testing equivalences;
- Park/Milner bisimulation;
- Hennessy-Milner logic;
- may/must testing;
- trace, failures, readiness, ready-trace, branching bisimulation;
- distinguishing tests and formulas.

Required safe wording:

```text
Observation-indexed behavioral equivalence is a mature field. The finite pair
test becomes a distinguishing test or formula showing that two states collapse
under one observation regime but separate under a finer semantics.
```

The final prior-art audit identifies van Glabbeek's spectrum as the single most
damaging missing citation.

### Abstract Interpretation And Complete Abstractions

Required concepts:

- Cousot and Cousot abstract interpretation;
- concrete and abstract domains;
- abstraction/concretization;
- Galois connections;
- soundness versus completeness;
- complete abstract domains;
- adequate quotients.

Required safe wording:

```text
The factorization diagram is standard abstraction machinery. The live question
is whether the chosen projection is complete for the declared capability
property or transformer.
```

## 0B.1 Add The Full Global Absorber List

The prior-art section should be reordered around global absorbers first,
database as an especially executable special case second, and physics
strongman sections third.

Primary absorbers to name:

- Blackwell comparison of experiments;
- Blackwell-Sherman-Stein theorem;
- Le Cam deficiency;
- statistical sufficiency and decision theory;
- van Glabbeek linear-time/branching-time spectrum;
- De Nicola-Hennessy testing equivalences;
- Park/Milner bisimulation;
- Hennessy-Milner logic;
- abstract interpretation;
- complete abstractions;
- Galois connections;
- POMDP belief-state sufficiency;
- resource convertibility and monotones;
- causal observational/interventional equivalence;
- control observability and reachability;
- database view/query determinacy and provenance;
- minimal sufficient statistics;
- fully abstract semantics;
- Myhill-Nerode / Nerode congruence;
- minimal predictive causal states and predictive state representations.

Required placement:

```text
These appear before witness examples, so examples are read as tests of an
absorption-aware schema rather than as proof of novelty.
```

## 0C. Add A Canonicity / Interestingness Criterion Requirement

The final prior-art audit says pre-registering `Cap` is not enough.

Problem:

```text
One can pre-register a pathological Cap that simply reads latent state.
```

The next version must add an interestingness criterion:

```text
A witness matters only if the projection, capability family, and equivalence
are operationally natural, canonical for the neighbor, minimal/adequate for a
declared task family, or forced by an observer/resource/budget regime.
```

Compare against:

- minimal sufficient statistics;
- coarsest adequate congruence;
- fully abstract semantics;
- Nerode congruence;
- quotient by bisimulation;
- minimal predictive causal states;
- predictive state representations;
- complete abstract domains.

Add a new verdict label:

```text
gerrymandered_cap
```

or:

```text
non_canonical_witness
```

Use it when `Cap` is typed but not operationally natural.

Also add a positive target:

```text
canonical_residue
```

Use it only when:

- the witness survives same-neighbor-data testing;
- `Cap` is domain-native, task-natural, or operationally forced;
- the projection is not merely an obviously impoverished state description;
- the neighbor does not already contain the native theorem/schema explaining
  the non-factorization.

## 0D. Reframe The Finite Pair Test As Necessary But Weak

Add:

```text
A finite pair witness is necessary for non-factorization in finite cases, but
it is weak evidence by itself. It shows only that the chosen projection lost
something the chosen downstream capability wanted. The nontrivial question is
why that projection and capability family are canonical or unavoidable.
```

This should temper the current witness priority language.

## 0E. Demote Flagship Self-Inflicted Projection Losses

The final prior-art audit says Git and dark matter examples are useful but not
flagship novelty evidence.

Required treatment:

```text
Git endpoint-tree examples are heuristic illustrations of an intentionally
coarse projection that discards commit DAG, provenance, branch structure,
reflog, and merge history. They should teach the audit, not prove novelty.
```

```text
Dark matter is a disciplined analogy for projection insufficiency. It should
not be a flagship witness because the luminous projection intentionally omits
gravitationally relevant source structure.
```

Route both as:

```text
heuristic illustration
```

unless a stronger same-neighbor-data witness is produced.

## 0F. State The Surviving Contribution More Narrowly

The next version should define the possible residue as one of three demanding
projects.

### Cross-Disciplinary Comparison Theorem

```text
Define a task-indexed capability object and prove systematic translations to
Blackwell sufficiency, belief-state sufficiency, testing/bisimulation
equivalence, resource convertibility, causal/interventional equivalence,
database determinacy, and abstraction completeness.
```

### Non-Self-Inflicted Witnesses

```text
Specify a legitimate state schema accepted by the neighboring field, fix a
non-gerrymandered task family, allow obvious enrichments, and still show
failure of factoring.
```

### Canonicity Criterion

```text
Prove when a projection-loss witness marks a bad projection versus an
unavoidable tradeoff across an observer/task/budget regime.
```

These should replace broader informal claims about formal residue.

## 0G. Clarify Two Forms Of Prior-Art Absorption

The next version must clarify that absorption is broader than "neighbor
distinguishes the two cases."

Absorption can occur in two ways:

### State-Enrichment Absorption

```text
The neighbor's legitimate state distinguishes the cases, restoring
factorization or showing that the original projection was underdescribed.
```

Examples:

- POMDP belief state;
- provenance graph;
- commit DAG;
- transaction log;
- purifier/global access profile;
- causal graph/intervention model;
- index/materialization state.

### Native-Theory Absorption

```text
The neighbor already has the theorem, schema, equivalence hierarchy, or
completeness criterion that explains the non-factorization itself.
```

Examples:

- Blackwell/Le Cam for decision sufficiency;
- process semantics for observational equivalence and distinguishing tests;
- abstract interpretation for incomplete abstractions;
- resource theory for convertibility;
- database view determinacy;
- causal inference for observational vs interventional equivalence.

Required wording:

```text
Formal residue requires surviving both forms of absorption.
```

## 0H. Promote Capability Type Discipline Before Witnesses

Before listing examples, the next version should require:

```text
Declare K before any witness:
set of answers;
preorder of admissible operations;
decision-value/risk object;
provenance object;
behavioral equivalence class;
resource convertibility structure;
reachable/viable set;
causal intervention query class;
database workload;
approximate retrieval envelope.
```

Add:

```text
Capability equivalence must be domain-native, task-natural, and fixed before
witness construction.
```

This should come before Git, detector, database, quantum, or physics examples.

## 1. Add Database Theory As A Primary Absorber

Add database theory to the `Prior Art First` section as a major absorber,
alongside POMDPs, control theory, resource theory, provenance/access control,
and sheaf obstruction.

Required wording target:

```text
Database systems provide a direct operational translation of the factorization
question. Let Y be source database state, pi be a view, projection, materialized
snapshot, index, or public API surface, and Cap be a query, workload, recovery
operation, audit right, update right, retrieval behavior, or policy-evaluable
object. Then Cap factors through pi exactly when the visible database surface
determines that capability under the declared constraints and workload. This is
absorbed in many cases by view/query determinacy, provenance, temporal
databases, access control, indexing theory, and distributed consistency
metadata.
```

Rationale:

Database view/query determinacy has nearly the same shape as the core
factorization test:

```text
V(I) = V(J) implies Q(I) = Q(J)
```

This is the database-native version of:

```text
pi(y1) = pi(y2) implies Cap(y1) ~=_K Cap(y2)
```

Add the database deep-research refinement:

```text
For a fixed observer, task, horizon, workload, approximation regime, and
resource boundary, future database capability often fails to factor through
payload-visible state alone. Whether it factors through an observer-visible
projection depends on what the projection preserves: schema and constraints,
view definitions, transaction snapshot/isolation, lineage/provenance, access
policy, materialization/index state, consistency model, approximation
parameters, workload, and budget.
```

## 2. Reframe Database Examples As Finite Witnesses, Not Novelty Evidence

Add an explicit statement that database examples are excellent teaching and
testing fixtures, but usually do not support formal residue.

Examples to name:

- event logs;
- provenance/lineage;
- MVCC and bitemporal state;
- indexes and materialized views;
- access policies;
- distributed consistency metadata;
- vector stores and approximate retrieval systems.

Required stance:

```text
These examples are valuable because they make factorization and
non-factorization finite and executable. They usually become translation
residue or heuristic residue, not formal residue, unless a witness survives
after database-native state, constraints, lineage, policy, index state,
transaction context, and workload are admitted.
```

## 3. Define "Same Visible State" Much More Strictly

Patch the equality discipline around visible state.

Current risk:

```text
same payload
same current value
same top-k result
same aggregate
```

can be mistaken for:

```text
same visible state
```

Required warning:

```text
same payload is not same database-visible state unless schema, wrapper, policy,
transaction context, lineage, index/materialization state, visibility context,
and workload are fixed or explicitly excluded.
```

When relevant, visible-state equality must declare:

- schema;
- constraints;
- view definition;
- query/view language;
- transaction time;
- valid time;
- snapshot timestamp;
- isolation level;
- lineage/provenance availability;
- index state;
- materialization state;
- retention policy;
- access policy;
- consistency model;
- embedding model;
- distance metric;
- chunking strategy;
- metadata filters;
- workload or query distribution.

## 4. Patch The Audit Template With Database-Specific Fields

Add a database-specific block to the audit template.

Suggested fields:

```text
Database family:
Database schema:
Constraints:
View/projection definition:
Query/view language:
Transaction timestamp:
Valid-time context:
Isolation level:
Lineage/provenance context:
Index/materialization context:
Retention/aggregation policy:
Access policy:
Consistency model:
Causal metadata:
Embedding model:
Distance metric:
Chunking strategy:
Metadata filters:
Approximation tolerance:
Declared workload:
```

Purpose:

Prevent sloppy examples where a payload, snapshot, or result value is treated
as the whole state while the actual database capability depends on omitted
schema, policy, lineage, transaction, index, or retrieval context.

## 5. Make Approximate Capability Equivalence First-Class

Vector, search, time-series, and approximate query systems show that exact
equality is often the wrong equivalence criterion.

Add examples of allowed `~=_K` relations:

```text
epsilon equivalence
probabilistic equivalence
top-k equivalence
recall@k within epsilon
precision/recall envelope equivalence
latency/recall tradeoff equivalence
ranking equivalence up to tolerance
same anomaly decisions under declared thresholds
same workload-level behavior within declared error bounds
```

Required conceptual patch:

```text
Capability equivalence may be exact, order-theoretic, probabilistic,
metric/tolerance-based, or workload-relative, but it must be declared before
the witness verdict.
```

## 6. Add Database Preservation Controls

Add database examples where `Cap` should factor through `pi`.

Preservation controls to include:

- full table projection determines full-table queries;
- materialized sum determines a declared sum workload;
- OLAP rollup determines the exact aggregate workload it was built for;
- sufficient index determines lookup capability for its declared key workload;
- full event log determines replay/recovery capability;
- full provenance graph determines declared provenance audit workload;
- full detector packet with wrapper/schema/policy determines declared
  admissibility checks;
- full vector index state determines declared ANN search behavior under its
  declared tolerance model.

Why this matters:

```text
If the schema cannot recognize database cases where projection is sufficient,
it is not falsifiable.
```

## 7. Adjust The Novelty Claim Downward

The next version should say directly:

```text
Database systems do not falsify the Candidate North Star, but they absorb a
large fraction of it.
```

The likely surviving value is:

```text
cross-domain audit language
```

unless a database or database-adjacent witness survives same-neighbor-data
testing.

Replace any novelty-leaning phrasing with:

```text
The database lens suggests translation residue by default, formal residue only
after hostile absorption fails.
```

## 8. Add Database-Specific Same-Neighbor-Data Conditions

Extend same-neighbor-data with a database row or subsection.

Database systems must be allowed to use:

- schema;
- constraints;
- views;
- query language;
- transaction and valid time;
- isolation semantics;
- version history;
- provenance/lineage;
- logs;
- indexes;
- materialized views;
- access policies;
- consistency metadata;
- causal metadata;
- embedding model;
- distance metric;
- retrieval index state;
- workload distribution;
- approximation tolerances.

If those distinguish the cases, the result is:

```text
absorbed by database-native state
```

not:

```text
North Star formal residue
```

## 9. Add Database Witness Priority Examples

Add database fixtures to the finite witness queue.

Suggested examples:

### Event-Log Non-Factorization

```text
Y = event log
pi(log) = materialized final account balance
Cap(log) = legally valid compensation/replay/audit operations
```

Construct two logs with the same final balance but different compensation or
audit rights.

Expected disposition:

```text
excellent witness, absorbed by event sourcing/provenance
```

### MVCC / Bitemporal Non-Factorization

```text
Y = versioned table with transaction-time history
pi = current visible snapshot
Cap = rollback, audit, or time-travel query capability
```

Construct two states with identical current rows but different transaction-time
histories.

Expected disposition:

```text
translation or heuristic residue
```

### OLAP Preservation And Loss Pair

```text
pi = daily revenue rollup
Cap_1 = total daily revenue query
Cap_2 = median transaction value or subgroup attribution query
```

Expected verdicts:

```text
Cap_1 factors through pi
Cap_2 does not factor through pi
```

This gives preservation and non-factorization in one compact fixture.

### Vector Approximate Equivalence Fixture

```text
Y = corpus + embedding model + ANN index state
pi = exposed corpus or sample top-k result
Cap = recall@k / latency / filtered retrieval behavior over future workload
```

Construct two systems with same visible sample result but different future
retrieval envelope.

Expected contribution:

```text
forces approximate capability equivalence to be explicit
```

## 10. Add Easy Proof Targets

The next version or companion schema should queue these proof targets.

### Fiber-Constancy Lemma

```text
For finite Y, pi : Y -> X, and Cap : Y -> K with equality equivalence,
Cap factors through pi iff Cap is constant on every fiber pi^{-1}(x).
```

Purpose:

This is the minimal mathematical skeleton of the candidate.

### View-Determinacy Translation

```text
For database instances satisfying constraints C, query Q is determined by view
V iff for all I,J satisfying C, V(I)=V(J) implies Q(I)=Q(J).
```

Purpose:

Anchor the candidate in mature database theory and block novelty overclaim.

### OLAP Rollup Control

Prove that a declared aggregate workload factors through the rollup built for
that workload, while richer attribution or distributional workloads need not.

Purpose:

Gives clean preservation and non-factorization controls.

### Approximate Equivalence Control

Formalize one fixture where:

```text
exact equality is too strict
```

but:

```text
epsilon / recall@k / workload equivalence is meaningful
```

Purpose:

Make approximate `K` equivalence operational rather than rhetorical.

## 11. Add The Strongest Database Translation Of `Y`, `pi`, `Cap`, And `K`

The database deep-research report gives a sharper formal translation than the
earlier lens review. Add this as a compact database-facing schema.

```text
Y = full database state under a chosen tradition
```

`Y` may include:

- base instance;
- schema;
- integrity constraints;
- null or incomplete-information semantics;
- view definitions;
- transaction snapshot;
- isolation level;
- lineage/provenance annotations;
- security policy;
- indexes/materializations;
- replication metadata;
- approximation knobs;
- budgeted execution regime.

```text
pi : Y -> X
```

Examples of `pi`:

- view instance;
- role-filtered result surface;
- materialized summary;
- snapshot seen by one transaction;
- document projection;
- graph neighborhood;
- vector index query interface.

```text
Cap : Y -> K
```

Examples of `Cap`:

- one query answer;
- family of answerable queries;
- preorder of executable operations;
- provenance object;
- set of reconstructible histories;
- approximate retrieval envelope trading recall against latency.

Recommended `K` guidance:

- use a set only for single exact answer tasks;
- use a preorder by default for "can do at least as much under the same budget";
- use a provenance semiring or witness object when explanation is capability;
- use an approximate envelope for ANN and latency-sensitive systems;
- reserve category/enriched-category language for future work unless a domain
  demands it.

## 12. Add Database Absorption Map Details

The next version should not merely say "databases absorb much of this." It
should name the database traditions that do the absorbing.

Database traditions to list as absorbers or partial absorbers:

- relational view determinacy;
- monotone determinacy and rewritability;
- dependencies, normalization, and lossless decomposition;
- data exchange and incomplete information;
- certain-answer semantics;
- provenance and lineage;
- temporal databases and MVCC;
- event sourcing and append-only logs;
- RBAC, ABAC, and row-level security;
- indexes and materialized views;
- OLAP cubes and continuous aggregates;
- document/JSON databases with validation and indexes;
- graph databases, RDF, SPARQL, entailment, and SHACL;
- time-series retention, compression, downsampling, and rollups;
- distributed stores, CRDTs, consistency, causal metadata, and staleness bounds;
- vector databases, ANN retrieval, HNSW/Faiss/pgvector-style search, filters,
  and latency/recall tradeoffs.

Suggested verdict language:

```text
Relational determinacy, incomplete information, provenance, temporal semantics,
and access control mostly absorb the exact-state form of the schema.

Event logs, materializations, OLAP, document stores, and time-series stores
partially absorb it: non-factorization appears when history, freshness, policy,
physical design, or retained raw data are omitted.

Distributed metadata and vector/ANN retrieval are the best database-facing
places to look for surviving residue because capability is approximate,
workload-bounded, policy-sensitive, consistency-sensitive, and resource-bound.
```

## 13. Treat Approximate / Workload-Bounded DB Cases As The Best Residue Zone

The database deep-research report narrows the strongest surviving database
residue to:

- approximate nearest-neighbor retrieval;
- latency/recall tradeoffs;
- workload-sensitive indexing;
- probabilistic freshness in distributed stores;
- policy-sensitive access surfaces;
- consistency-sensitive future operations;
- resource/budget bounded execution.

Required stance:

```text
The least-absorbed database zone is approximate, workload-bounded,
policy-sensitive, consistency-sensitive operational capability. Equal visible
data can support different future operation sets unless index family and
parameters, approximation tolerance, workload, resource budget, policy, and
consistency guarantees are fixed.
```

This should be added as a nuance to the blanket "database absorbs much of it"
posture.

## 14. Add Same-Visible-State Discipline As A Named Failure Mode

Add a verdict or warning label:

```text
same_visible_state_underspecified
```

Use it when a witness does not freeze the relevant database context.

Suggested language:

```text
If schema, constraints, null/incomplete-data semantics, view definitions,
security/access policy, transaction boundaries and isolation, snapshot
timestamp or log position, provenance/lineage regime, materialization and
refresh policy, index family and parameters, consistency model, approximation
tolerance, workload, and resource budget are not fixed when relevant, the
same-visible-state discipline is violated.
```

This should sit near `under_typed`.

## 15. Upgrade Physics Sections From Safety Labels To Strongman Instantiations

The Strongman note says v0.2 is rigorous as defensive audit, but too thin as a
physics-forward steelman. The next version should keep the quarantine but add
mathematical instantiation.

Replace the thin pattern:

```text
Known physics
Safe bridge
Not claimed
Likely absorber
```

with:

```text
Known physics
Candidate Y
Candidate X
Candidate pi
Candidate Cap
Candidate K
Capability equivalence
Steelman non-factorization question
What would count as support
What would kill it
Known absorber
Not claimed
```

Required posture:

```text
Do not strip the physics sections.
For each physics-facing section, instantiate the core schema.
Use known physics as the anchor.
Make the strongest non-laughable mathematical case.
Keep all claims non-canonical and non-promotional.
```

## 16. Add Physics-Forward Steelman Targets

For each physics domain, the next version should include a compact typed
instantiation.

### Gravity

```text
Y = spacetime plus metric, stress-energy, and global causal structure
X = local observer-visible measurement data over patch U
pi = restriction to local observables
Cap = future-directed causal curves, communication possibilities, measurement
      trajectories, and reachable domains
```

Steelman:

```text
Two locally similar visible patches may sit inside globally different causal
structures, so their future accessible domains differ. Gravity is a domain
where capability is naturally encoded by causal geometry, not merely local
visible state.
```

Not claimed:

```text
capability explains gravity
```

### Quantum Theory

```text
Y = global quantum state plus purification/environment/resource structure
X = reduced local state available to observer O
pi = partial trace or restricted measurement interface
Cap = operations available under allowed quantum channels, LOCC, access to
      purifier, side information, or resource conversion
```

Steelman:

```text
Same reduced state can hide different global resources. For a strictly local
observer those differences may be unavailable; for a broader observer with side
access, they can change future operations.
```

Mandatory caveat remains:

```text
same reduced state does not imply different strictly local operational
capability
```

### Standard Model / Particle Structure

```text
Y = field, representation, gauge, phase, and internal quantum-number structure
X = observed particle event or local detector signature
pi = readout/coarse-graining to observed event
Cap = allowed interactions, couplings, transformations, scattering channels,
      conserved quantities, and selection rules
```

Steelman:

```text
Same spacetime localization is not enough. Internal fiber/representation data
changes which interactions are possible.
```

Not claimed:

```text
charge, spin, or mass are capability
```

### Black Holes

```text
Y = global spacetime including horizon structure and interior/exterior causal
    relations
X = exterior observer-accessible data
pi = restriction to exterior causal domain
Cap = reconstruction, communication, intervention, retrieval, and verification
      operations available to an observer
```

Steelman:

```text
A horizon is a mathematically precise boundary in future operation
availability. It separates global structure from what a given observer can
signal, reconstruct, or act upon.
```

Not claimed:

```text
capability solves the information problem
```

### Cosmology And Dark Energy

```text
Y = global cosmological spacetime with expansion history
X = observer-visible cosmological data within a horizon
pi = restriction to causal past/future accessible region
Cap = future causal contact, observation, communication, and
      structure-formation possibilities
```

Steelman:

```text
Expansion changes which future regions remain causally accessible.
Accelerated expansion can shrink long-run interaction capability even as
spatial scale grows.
```

Not claimed:

```text
capability explains dark energy
```

### Dark Matter

```text
Y = full gravitational source structure
X = luminous/electromagnetic visible matter distribution
pi = projection to visible matter
Cap = gravitationally allowed trajectories, binding, lensing, rotation
      behavior, and structure formation
```

Steelman:

```text
Dark matter shows that visible luminous state is not a sufficient invariant for
gravitational futures. The hidden structure is not capability, but it changes
future dynamical possibilities.
```

Not claimed:

```text
dark matter is hidden capability
```

### Time And Emergence

For time, require every directional capability claim to instantiate:

```text
Y, X, pi, Cap, K, equivalence, openness/resource/erasure/coarse-graining or
boundary condition
```

For emergence, require:

```text
structure -> preserved capability -> further structure
```

but also compare against:

- viability;
- affordances;
- niche construction;
- major transitions;
- constructor theory;
- resource theory.

## 17. Preserve Ambition While Keeping The Collapse Gate

Add a balancing paragraph:

```text
The physics sections should not be reduced to one-line analogies. They should
make the strongest mathematically typed case that known physics already
contains projection/fiber/capability structures. The sections remain
non-canonical and non-promotional, but they should be steelman arguments, not
only safety labels.
```

Also preserve:

```text
If the typed physics instantiation is fully absorbed by known physics with no
useful residue, record that absorption honestly.
```

## Suggested Placement In The Next Draft

### Status / Posture

Add:

```text
Database systems are treated as primary absorbers and finite-test sources, not
as evidence of novelty.
```

Add:

```text
The physics-facing sections are steelman instantiations of the schema, not
evidential support and not mere safety labels.
```

### Prior Art First

Add database theory as a named primary prior-art family.

### Same-Neighbor-Data Condition

Add database-native state and context as a row/subsection.

### Capability Equivalence

Add approximate/probabilistic/workload equivalence examples.

### Physics Analogy Discipline

Retain the quarantine, but upgrade each physics section to include:

```text
Y / X / pi / Cap / K / equivalence / non-factorization question / support /
falsifier / absorber / not claimed
```

### Preservation Controls

Add OLAP, materialized view, index, full log, and full provenance controls.

### Non-Factorization Witnesses

Add event-log, MVCC, graph-locality, time-series aggregation, distributed
metadata, and vector-index fixtures.

### Collapse Condition

Add:

```text
If database-native state absorbs a witness, record translation or heuristic
residue rather than formal residue.
```

## Do Not Do Yet

Do not draft the next Candidate North Star version until the final pending deep
research report is integrated.

Until that report is in:

```text
only update this queue file
do not redraft v0.2
do not create v0.3
```

Do not promote database examples to formal residue merely because they are
clear.

Do not use "same payload" or "same current value" as sufficient equality
without declaring the database context.

Do not make exact equality the only capability equivalence model.

Do not let database absorption make the whole candidate timid.

Do not let physics sections remain only:

```text
known physics / safe bridge / not claimed
```

They must become typed strongman sections before the next draft is considered
complete.

## Bottom Line

The next version should preserve the Candidate North Star, but make the
database absorption sharper:

```text
Database theory gives the cleanest finite form of the factorization question,
and therefore also absorbs many apparent examples.
```

The productive stance is:

```text
use databases to make the schema executable, falsifiable, and less novel than
it might otherwise sound.
```

The complementary physics stance is:

```text
use physics to make the schema ambitious, domain-instantiated, and
mathematically non-laughable without treating analogy as evidence.
```
