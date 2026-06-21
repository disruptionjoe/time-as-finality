# Database Expert Lens Review v0.1

## Status

Review artifact for:

```text
Candidate North Star v0.2.md
```

This is not canon.
It is not a claim update.
It is not a replacement draft.

Purpose:

```text
Use ten database-system lenses to ask whether the Candidate North Star is
obviously wrong, already absorbed, or easy to sharpen with finite proofs.
```

The two review voices are treated as:

- `Sam`: database/systems skeptic;
- `H`: formal hostile reviewer asking whether a problem is wrong, fixable, or
  simply absorbed by existing theory.

## Executive Judgment

No database lens finds the core sentence obviously false:

```text
For fixed observer, task, horizon, and resource boundary,
future capability need not factor through observer-visible state.
```

But the database lenses strongly demote the novelty of the sentence.

In database terms, the core schema is close to:

```text
view/query determinacy
```

or:

```text
does a query/workload Q over source state Y factor through a view V?
```

The finite-pair test:

```text
pi(y1) = pi(y2)
but
Cap(y1) != Cap(y2)
```

is exactly the standard witness shape for:

```text
a view does not determine a query
```

So the Candidate North Star is not obviously incorrect. The danger is that
database theory absorbs a large fraction of it.

The fix is not to defend novelty. The fix is to explicitly add database
absorption as a primary prior-art gate.

## Sam/H Summary

### Sam: Is Anything Obviously Incorrect?

Not fatally.

The main incorrectness risk is not the factorization claim. The risk is
calling database-native cases "North Star residue" when they are already normal
database phenomena:

- projection loses information;
- views fail to determine queries;
- logs carry future recovery operations;
- indexes preserve some queries but not others;
- privileges and policies change admissible actions;
- transaction snapshots hide versions;
- lineage/provenance changes audit rights;
- embeddings preserve similarity neighborhoods imperfectly.

If `Cap` is a query, workload, permission set, recovery plan, or admissible
operation set over database state, then the right database question is:

```text
is Cap determined by the visible view?
```

That is mature territory.

### H: Is It Fixable?

Yes.

Add a database-theory clause:

```text
When Y is database state, pi is a view, and Cap is a query, workload,
permission set, recovery operation, or policy-evaluable object, the candidate
must first be tested as query/view determinacy under the declared constraints.
```

Then the Candidate North Star can survive as:

1. a translation layer across view determinacy, provenance, indexing, temporal
   state, access control, and approximate retrieval;
2. a workflow for discovering which state a database system must expose;
3. possible formal residue only if a typed `Cap` distinction survives after
   database-native state, constraints, lineage, policy, and transaction context
   are included.

### H: Or Is It Not Fixable Because Something Is Actually Wrong?

One part may be too strong:

```text
formal residue after same-neighbor-data
```

For database examples, this may often be impossible by construction. Once the
database neighbor is allowed to include schema, constraints, transaction time,
lineage, policy, indexes, logs, and workload, it will usually distinguish any
operation-relevant difference.

That does not make the Candidate North Star false. It means database cases are
likely:

```text
translation residue
```

or:

```text
heuristic residue only
```

not formal residue.

## Ten Database Lenses

## 1. Relational SQL / View Determinacy

Database object:

```text
source database instance I
view V(I)
query/workload Q(I)
```

Translation:

```text
Y   = legal database instances
pi  = view, projection, aggregation, or public schema
Cap = query/workload answer, update capability, or allowed transaction family
```

Review:

Relational theory already asks whether a view determines a query:

```text
V(I) = V(J) implies Q(I) = Q(J)
```

That is structurally identical to the candidate's factorization test.

Obvious incorrectness:

None, but novelty is heavily absorbed.

Fix:

Name this absorption directly. Use "view determinacy" as the canonical database
translation of factorization.

Easy proof target:

For finite fixtures, prove:

```text
Cap factors through pi iff Cap is constant on every pi-fiber.
```

Database version:

```text
Q is determined by V iff all legal instances with equal V have equal Q.
```

## 2. Temporal / Bitemporal / MVCC Databases

Database object:

```text
valid time
transaction time
snapshot isolation
version history
```

Translation:

```text
visible state = current snapshot
hidden source = versioned history plus transaction context
Cap = rollback, audit, correction, replay, or time-travel query capability
```

Review:

The Git/provenance examples are database-native here. Same current row values
can have different valid-time histories, transaction-time histories, rollback
rights, or audit answers.

Obvious incorrectness:

Saying "same visible state" is dangerous unless the snapshot timestamp,
isolation level, and temporal schema are fixed.

Fix:

Require:

```text
visible snapshot equality under declared isolation and temporal schema
```

Easy proof target:

Construct two bitemporal tables with identical current visible rows but
different transaction-time histories. Show that a time-travel query or rollback
operation does not factor through the current snapshot.

Likely residue:

Heuristic or translation. Temporal databases absorb the phenomenon.

## 3. Event-Sourced / Log-Structured Databases

Database object:

```text
append-only event log
materialized view
replay/rebuild operation
```

Translation:

```text
Y   = event log
pi  = materialized current state
Cap = replay, audit, compensation, migration, or recovery operations
```

Review:

This is one of the cleanest finite witnesses. Two event logs can project to the
same materialized state while supporting different explanations, rollback
paths, audit claims, or compensation operations.

Obvious incorrectness:

No. This is a strong example, but it is absorbed by event sourcing and
provenance.

Fix:

Do not present it as novel residue. Present it as a perfect teaching fixture
for capability-nondetermining projection.

Easy proof target:

Let:

```text
pi(log) = final account balance
Cap(log) = set of legally valid compensating transactions
```

Build two logs with equal final balance and different compensation rights.

## 4. Provenance / Lineage Databases

Database object:

```text
why-provenance
where-provenance
semiring provenance
lineage graph
```

Translation:

```text
visible state = query result
source state = derivation / lineage / dependency graph
Cap = explain, challenge, delete, repair, audit, or certify result
```

Review:

This lens directly attacks many Candidate North Star examples. If provenance is
legitimate state, then same result value with different derivation is not a
residue. It is standard provenance.

Obvious incorrectness:

The draft is safe because it says provenance must receive legitimate state.
But it should name provenance databases explicitly in the prior-art-first
section, not only Git/provenance examples.

Fix:

Add provenance/lineage databases as a major absorber.

Easy proof target:

Two SQL derivations produce the same result tuple with different provenance
polynomials. A deletion, explanation, or repair query distinguishes them.

Likely residue:

Mostly translation.

## 5. Graph Databases / RDF / Knowledge Graphs

Database object:

```text
nodes, edges, paths, graph patterns, ontology entailment
```

Translation:

```text
pi  = local neighborhood, projected subgraph, visible labels, or materialized view
Cap = path queries, reachability, constraint satisfaction, inference, update impact
```

Review:

Graph databases make the candidate concrete: two nodes can have identical local
visible neighborhoods up to radius `r` but different global reachability,
centrality, cycle membership, or ontology entailments.

Obvious incorrectness:

Be careful with "same local section, different gluing capability." Graph and
RDF systems already distinguish local isomorphism from global query
equivalence.

Fix:

State whether equivalence is:

- exact node/edge equality;
- bounded-radius bisimulation;
- graph isomorphism;
- ontology entailment equivalence;
- workload equivalence.

Easy proof target:

Construct two graphs with identical radius-1 neighborhoods around a node but
different existence of a length-3 path to a target. The path-query capability
does not factor through the radius-1 projection.

Likely residue:

Translation or heuristic.

## 6. Time-Series Databases

Database object:

```text
timestamped measurements
downsampling
window aggregates
retention policies
rollups
```

Translation:

```text
Y   = raw time series
pi  = sampled, aggregated, downsampled, or windowed series
Cap = anomaly detection, forecasting, reconstruction, alerting, control action
```

Review:

Time-series systems show that equal aggregates can hide different future
operational consequences. Same hourly average can hide spikes, phase shifts,
volatility, or causal ordering needed for alerting or control.

Obvious incorrectness:

None. But "visible state" must include the sampling/retention policy. Without
that, equality is ill-defined.

Fix:

Add `retention policy` and `aggregation window` as concrete examples of
`Sigma`, `r`, and `h`.

Easy proof target:

Two raw sequences have equal hourly averages but only one crosses an alert
threshold. Alert capability does not factor through the hourly average view.

Likely residue:

Absorbed by signal processing, observability, and time-series database design.

## 7. Columnar OLAP / Data Warehouses

Database object:

```text
fact tables
dimensions
materialized cubes
rollups
star schemas
```

Translation:

```text
pi  = cube rollup or aggregate table
Cap = drill-down, segmentation, attribution, reaggregation, anomaly isolation
```

Review:

OLAP is projection sufficiency made practical. A rollup preserves some
questions and destroys others. Same aggregate can hide different segment-level
facts and therefore different drill-down or attribution capability.

Obvious incorrectness:

No, but the candidate should not imply this is surprising. It is the design
tradeoff of OLAP.

Fix:

Use OLAP as a preservation-control source:

```text
some rollups preserve declared aggregate workloads exactly
```

Easy proof target:

Show that a sum rollup determines total revenue queries but not median,
variance, or subgroup attribution queries.

Likely residue:

Excellent preservation-control material.

## 8. Document / JSON Databases

Database object:

```text
nested documents
schema-on-read
partial indexes
validation rules
```

Translation:

```text
pi  = public JSON projection, flattened view, selected fields
Cap = validation, migration, patching, query routing, schema evolution
```

Review:

Document databases expose an important issue: capability can depend on schema
discipline that is not visible in the payload. Same apparent JSON document can
have different validation context, index support, migration path, or patch
semantics.

Obvious incorrectness:

The draft should avoid treating raw payload as the whole visible state unless
schema, collection, index, and validation context are declared.

Fix:

For detector-packet examples, explicitly distinguish:

```text
payload equality
```

from:

```text
document-with-wrapper/schema/policy equality
```

Easy proof target:

Two identical JSON payloads in different collections with different validation
rules or indexes support different permitted updates or query plans.

Likely residue:

Heuristic residue for schema/context discovery.

## 9. Key-Value / Cache / CRDT / Distributed Stores

Database object:

```text
key-value state
replicas
consistency level
conflict resolution
causal metadata
```

Translation:

```text
visible state = current key/value read
source state = replica vector clocks, causal context, tombstones, merge policy
Cap = merge, resolve conflict, read-your-writes, rollback, converge
```

Review:

Distributed stores are a strong systems version of the candidate. Same visible
value can hide different causal metadata and therefore different future merge
or conflict behavior.

Obvious incorrectness:

None, but if causal metadata is legitimate state, the neighbor absorbs the
witness.

Fix:

Add consistency model and causal metadata to the same-neighbor-data condition.

Easy proof target:

Two replicas expose the same key value but different vector clocks/tombstones.
They behave differently under a future concurrent write or merge.

Likely residue:

Translation; very useful finite witness.

## 10. Search Index / Vector Database / Approximate Retrieval

Database object:

```text
inverted index
embedding vectors
ANN graph/index
distance metric
chunking strategy
metadata filters
```

Translation:

```text
Y   = documents, embeddings, index structure, metadata, metric, refresh state
pi  = visible result list, embedding vector, top-k result, or exposed document text
Cap = retrieval, nearest-neighbor recall, filtering, reranking, update/delete behavior
```

Review:

Vector databases make two subtleties unavoidable.

First, same visible text or same top-k result does not determine future
retrieval capability. Chunking, metadata filters, embedding model, ANN index
state, distance metric, and refresh lag matter.

Second, approximate retrieval means factorization may need to be probabilistic
or tolerance-based:

```text
Cap(y1) ~= Cap(y2)
```

may mean equal within recall, latency, or ranking tolerance, not exact equality.

Obvious incorrectness:

The draft currently treats capability equivalence as generic enough, so it is
not wrong. But it should explicitly admit approximate/probabilistic capability
equivalence for vector and search systems.

Fix:

Add examples of `~=_K` such as:

```text
same top-k up to ranking tolerance
same recall@k within epsilon
same latency/recall tradeoff envelope
same filtered retrieval rights
```

Easy proof target:

Two vector indexes expose the same corpus and same sample query result but have
different ANN graph structure or refresh state, producing different recall for
a future query distribution.

Likely residue:

Potentially useful because approximate equivalence forces the candidate to
handle non-exact `K` equivalence.

## Cross-Lens Findings

## Finding 1: Database Theory Gives The Cleanest Formal Core

The candidate should add:

```text
Database translation:
Y = source database instances
pi = view/projection/materialization/index/exposed snapshot
Cap = query, workload, policy, recovery, audit, retrieval, or update capability
```

Then:

```text
Cap factors through pi
```

means:

```text
the visible view determines the declared capability object
```

This is likely the easiest rigorous formalization of the Candidate North Star.

## Finding 2: "Same Visible State" Must Include Context

Across database systems, visible equality is meaningless unless the following
are declared when relevant:

- schema;
- constraints;
- view definition;
- transaction timestamp;
- isolation level;
- retention policy;
- index state;
- access policy;
- provenance/lineage availability;
- consistency model;
- embedding model and metric;
- workload/query language.

This should be added to the audit template as database-specific fields.

## Finding 3: Many Examples Are Absorbed By Legitimate State

Database systems are built around exactly the difference between:

```text
stored/source state
```

and:

```text
visible/materialized/queryable state
```

So most database cases will not produce formal residue.

They are still useful because they give finite, executable witnesses.

## Finding 4: Preservation Controls Are Easy In Databases

Database systems give clean examples where factorization should hold:

- full table projection determines all full-table queries;
- a materialized sum determines a sum workload;
- a sufficient index determines lookup capability for its key workload;
- a complete provenance graph determines a provenance audit workload;
- a full event log determines replay/recovery capability;
- a full vector index state determines declared ANN search behavior.

These should be used to keep the schema falsifiable.

## Finding 5: Approximate Equivalence Needs A First-Class Slot

Vector/search/time-series systems show that exact equality is often the wrong
equivalence.

The candidate should support:

```text
epsilon equivalence
probabilistic equivalence
top-k equivalence
latency/recall envelope equivalence
workload equivalence
```

This is a real sharpening opportunity.

## Suggested Patch To Candidate North Star v0.2

Add a database absorption paragraph under `Prior Art First`:

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

Add database fields to the audit template:

```text
database schema:
constraints:
view/query language:
transaction/isolation context:
lineage/provenance context:
index/materialization context:
access policy:
consistency model:
approximation tolerance:
workload:
```

Add a warning:

```text
same payload is not same database state unless schema, wrapper, policy,
transaction context, lineage, and index/visibility context are fixed or
explicitly excluded.
```

## Easy Proofs To Dig Into Next

## Proof 1: Fiber-Constancy Lemma

Statement:

```text
For finite Y, pi : Y -> X, and Cap : Y -> K with equality equivalence,
Cap factors through pi iff Cap is constant on every fiber pi^{-1}(x).
```

Why it matters:

This is the cleanest mathematical skeleton of the candidate.

## Proof 2: View Determinacy Translation

Statement:

```text
For database instances satisfying constraints C, query Q is determined by view
V iff for all I,J satisfying C, V(I)=V(J) implies Q(I)=Q(J).
```

Why it matters:

This anchors the candidate in mature database theory and prevents novelty
overclaim.

## Proof 3: Event-Log Non-Factorization Fixture

Construct:

```text
two event logs with same materialized state
different compensation/replay/audit capability
```

Why it matters:

This is probably the simplest finite executable witness.

## Proof 4: OLAP Preservation Control

Construct:

```text
rollup pi = total revenue by day
Cap = total-revenue workload
```

Show:

```text
Cap factors through pi
```

Then change:

```text
Cap = median or subgroup attribution workload
```

Show:

```text
Cap does not factor through pi
```

Why it matters:

One fixture gives both preservation and loss.

## Proof 5: Vector Approximate Equivalence Fixture

Construct:

```text
same corpus projection
two ANN indexes
same sample top-k
different recall@k over future query distribution
```

Why it matters:

This forces `~=_K` to handle approximate capability equivalence.

## Bottom Line

Sam's answer:

```text
Nothing central is obviously false, but database theory absorbs much more than
the draft currently admits.
```

H's answer:

```text
It is fixable by adding database view/query determinacy as a primary absorber
and by treating database examples mostly as finite witnesses, preservation
controls, and translation residue rather than formal novelty.
```

Best next move:

```text
write a tiny database factorization note:
Y = database instances
pi = view/materialization/index/snapshot
Cap = workload/recovery/audit/retrieval capability
factorization = view determinacy under constraints
```

This would be easy to prove further and would make the Candidate North Star
more technically disciplined.
