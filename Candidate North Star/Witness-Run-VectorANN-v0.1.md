# Witness Run: Vector/ANN Retrieval — v0.1

## Status

First real execution of the v0.4 audit protocol.
Target witness: approximate nearest-neighbor (ANN) retrieval.
Source: identified in the Database Absorption Test report as "the clearest surviving residue."
This file does not advance a claim. It runs the instrument and records what it finds.

---

## Part 1: Reviewer Checklist Declarations

### Formal Object Declarations

**Y declared?** Yes.

Y is the full vector retrieval system state:
- the set of stored embedding vectors (the corpus);
- the metric space structure (distance function, e.g. cosine or L2);
- the index family and construction parameters (e.g. HNSW with ef_construction, M; or IVFFlat with nlist, nprobe);
- the search-time parameters (ef_search, nprobe at query time);
- any pre-filter or post-filter predicate definitions;
- the hardware/resource budget (memory, FLOPS, latency ceiling);
- the recall target or approximation tolerance (e.g. recall@10 >= 0.95).

This is the full operational state of an ANN retrieval system, not just the stored vectors.

**X declared?** Yes.

X is the observer-visible projection: the stored embedding vectors as readable objects, plus any user-visible metadata fields (document IDs, scalar filter fields). Specifically: what a user of the vector store can directly read or enumerate without knowledge of the index structure, graph connectivity (HNSW layers), inverted file cell assignments (IVFFlat), or hardware configuration.

In concrete terms: X = the vector corpus (embeddings) as a readable table of (id, vector, metadata) tuples.

**pi declared?** Yes.

pi: Y -> X is the projection that reads out the stored vectors and metadata, discarding:
- the index graph or cell-assignment structure;
- the construction and search parameters (ef_construction, M, nlist, nprobe, ef_search);
- the approximation tolerance regime;
- the hardware/resource budget;
- the filter execution policy.

**visible equivalence ~=_X declared?** Yes.

Two full system states y1, y2 satisfy pi(y1) ~=_X pi(y2) when their stored vector corpora are identical: same set of (id, vector, metadata) tuples, byte-for-byte. This is equality of the observable data surface. The underlying index structure, parameter regime, and resource budget may differ.

**K typed?** Yes.

K is an approximate retrieval envelope: for a given query vector q and parameters (k, recall_target r, latency ceiling L, filter predicate f), the capability object is the set of top-k neighbor sets that are reachable by some admissible query execution within the declared budget.

More precisely: K is the set-valued map

    K(y, q, k, r, L, f) = { S subset corpus : |S| = k, S is a valid top-k result achievable with recall >= r within latency L under filter f given index state y }

For fixed q, k, r, L, f this is a subset of the power set of the corpus. Two capability objects are equivalent (~=_K, see below) when they contain the same achievable result sets.

The v0.4 document lists "approximate retrieval envelope" as a named K candidate under the Databases domain calibration. This is not a novel type; it is the explicitly listed one.

**Cap declared before the witness?** Yes.

Cap: Y -> K is declared above. It maps full system state y to the approximate retrieval envelope for a fixed (q, k, r, L, f) tuple. This is fixed before any witness pair is named.

**capability equivalence ~=_K declared?** Yes.

~=_K is equality of achievable result sets: Cap(y1) ~=_K Cap(y2) iff the set of valid top-k result sets achievable within (r, L, f) is the same under y1 and y2. This is a genuine equivalence relation (reflexive, symmetric, transitive). It is domain-natural for retrieval evaluation: two systems are capability-equivalent if they produce the same range of valid approximate answers for the declared task.

**observer/task/horizon/boundary fixed?** Yes.

- Observer: a user with read access to stored vectors and the ability to issue vector similarity queries; no access to index internals, HNSW layer graph, IVFFlat cell assignments, or hardware profiling.
- Task: approximate top-k nearest-neighbor retrieval for a fixed query vector q, with recall target r >= 0.95, latency ceiling L (e.g. 10ms at p99), and optional scalar filter f.
- Horizon: a single query execution (one request-response round trip).
- Resource boundary: the deployed hardware budget (fixed CPU/GPU, RAM, I/O) as part of the system state y. The observer does not change the hardware between queries.

**projection meaningful?** Yes. The projection pi is operationally natural: it is what a vector database user can see by reading the stored data. It is not artificially impoverished; it is the standard read interface.

**same-visible-state context fixed?** Yes. Two states are same-visible when their vector corpora are identical. Schema (vector dimensionality), corpus, and metadata are fixed. What differs is the index and parameter regime, which pi discards.

**projection underdescribed?** This is the key question the audit must answer. See Part 4.

**Cap domain-natural?** Yes. Approximate retrieval capability (achievable top-k sets under recall/latency constraints) is the standard metric by which ANN systems are evaluated in the information retrieval and systems literature. It is not invented for this audit.

**Cap non-gerrymandered?** Yes. The definition follows directly from how ANN benchmarks (ANN-Benchmarks, BigANN) are defined. Recall@k and latency are the standard axes.

**positive preservation control supplied?** Yes. See Part 2.

**negative non-factorization fixture supplied?** Yes. See Part 2.

**fiber spread singleton or non-singleton?** Non-singleton. See Part 2.

**minimal capability-preserving quotient identified?** Partially. See Part 5.

**trivial/native enrichment tested?** Yes. See Parts 4 and 5.

**state-enrichment absorption tested?** Yes. See Part 4.

**native-theory absorption tested?** Yes. See Part 4.

**residue label honest?** Yes. See Part 6.

---

## Part 2: The Witness Pair

### Setup

Fix a corpus C = {v_1, ..., v_n} of n embedding vectors in R^d.
Fix a query vector q in R^d.
Fix parameters: k=10, recall_target r=0.95, latency ceiling L=10ms, no filter.

Define the two system states:

**y1:** Corpus C, metric = cosine similarity, index = HNSW with M=16, ef_construction=200, ef_search=100, hardware = single CPU server, 16GB RAM.

**y2:** Corpus C, metric = cosine similarity, index = IVFFlat with nlist=1024, nprobe=64, hardware = same CPU server, 16GB RAM.

**pi(y1) = pi(y2):** Both expose the same vector corpus C as (id, vector) tuples. The projection is identical: same n vectors, same dimensionality, same metadata. By definition pi(y1) ~=_X pi(y2).

### Cap(y1) vs Cap(y2)

Under HNSW (y1), the graph structure navigates the corpus via a hierarchical proximity graph. At ef_search=100, it explores a candidate set of size 100 and returns the 10 best. The traversal path is graph-dependent: it may miss some true nearest neighbors and include some approximate ones. The achievable result sets are those reachable by the HNSW greedy search algorithm from entry points in the graph, subject to the graph's connectivity determined by M=16, ef_construction=200. The recall@10 is determined by this structure.

Under IVFFlat (y2), the corpus is partitioned into 1024 Voronoi cells. At nprobe=64, queries examine 64 cells. The reachable top-k sets are those found within the union of those 64 cells. If a true neighbor falls in a cell not visited by nprobe=64, it is not retrievable by this system under these parameters.

The achievable result sets differ structurally:
- y1 can retrieve neighbors that are connected via the HNSW graph but may be in distant IVFFlat cells.
- y2 can retrieve all vectors in the 64 nearest cells but misses those in unvisited cells.
- There exist query vectors q where the top-10 set achievable by y1 (within latency L at recall r) differs from the top-10 set achievable by y2.

Therefore: Cap(y1) not ~=_K Cap(y2).

This is a non-factorization witness: pi(y1) ~=_X pi(y2) but Cap(y1) not ~=_K Cap(y2).

### Positive Preservation Control

If y3 = y1 but with ef_search=100 replaced by exact search (brute-force scan), and y4 = y2 but with nprobe=nlist (all cells scanned, i.e. exact search), then both y3 and y4 compute exact nearest neighbors. For exact search, Cap factors through the vector corpus: any system with the same corpus and exact search returns the same top-k. So Cap(y3) ~=_K Cap(y4). The projection is capability-sufficient for exact-search retrieval. The non-factorization is specific to the approximate regime with constrained search parameters.

### Non-Factorization Fixture

Confirmed above: HNSW-y1 vs IVFFlat-y2 with same corpus, different achievable result sets for the same query under the same latency constraint.

### Fiber Spread

The pi-fiber of the identical corpus C contains many system states: exact-search systems, HNSW with various M and ef parameters, IVFFlat with various nlist/nprobe, SCANN, NSG, DiskANN, random projection LSH, and others. These span a wide range of (recall, latency) frontiers. The fiber spread of Cap values is non-singleton. Spread_Cap(C) contains multiple distinct capability envelopes.

---

## Part 3: Formal Structure Check

### Fiber-Constancy Lemma

Cap is not ~=_K-constant on the pi-fiber of C. As shown above, HNSW and IVFFlat with the same corpus achieve different result sets for some queries. Therefore the lemma confirms: Cap does not factor through pi.

The factorization fails because pi discards the index structure and parameters that determine which result sets are achievable.

### Capability Spread

Spread_Cap([C]_{~=_X}) is non-singleton. It contains at least:
- the exact-search capability envelope (all true k-NN);
- the HNSW-at-ef100 envelope;
- the IVFFlat-at-nprobe64 envelope;
- LSH-based envelopes with different hash families.

ambiguity_Cap(C) >= 3 for natural parameter choices. The spread is not trivially large (it is bounded by the corpus and k), but it is clearly non-singleton.

---

## Part 4: Absorption Protocol

### State-Enrichment Absorption

**Question:** Does enriching the visible state with the index and parameter regime restore factorization?

**Answer: Yes, immediately and completely.**

Define the enriched projection:

    pi'(y) = (pi(y), index_family(y), construction_params(y), search_params(y), approx_tolerance(y), hardware_budget(y))
           = (corpus C, HNSW/IVFFlat/..., M/nlist/..., ef_search/nprobe/..., r, L)

Then Cap factors through pi'. Given the enriched visible state, the achievable result sets are determined (up to randomized tie-breaking, which is negligible for recall purposes). Two systems with identical enriched states produce identical capability envelopes.

The Database Absorption Test report states this explicitly:

> "Approximate retrieval capability typically does not factor through stored vectors alone; it depends on index and approximation regime."

and

> "It factors, at best, through vectors + metric + index family + search parameters + filters + hardware/budget envelope."

This is state-enrichment absorption: the neighboring field (information retrieval / ANN systems) already treats index family and parameters as part of the system description. The original projection pi was underdescribed relative to domain practice.

**Failure label triggered:** `projection_underdescribed`

The projection pi omits native state data (index structure, search parameters) that the ANN domain standardly treats as relevant for retrieval capability. This is not a self-inflicted construction; it is what any ANN practitioner would say when asked "why do these two systems perform differently on the same corpus?" They would immediately point to the index and parameters.

### Native-Theory Absorption

**Question:** Does information retrieval theory or approximate query processing already own the non-factorization result?

**Answer: Yes.**

The ANN literature has studied the recall-latency-accuracy tradeoff as a first-class design object since at least the mid-1990s (LSH, HNSW, IVFFlat, ScaNN, DiskANN). The standard evaluation framework (ANN-Benchmarks, Babenko et al., Malkov-Yashunin HNSW paper) explicitly parameterizes retrieval capability by (index family, construction params, search params, recall target, latency). This is not a gap the literature ignores; it is the central design variable.

More specifically:
- The HNSW paper (Malkov and Yashunin, 2020) proves that the navigable small-world graph structure determines the reachable neighbor sets during greedy search, and shows analytically that different ef_search values yield different recall-latency curves.
- The Faiss paper (Johnson et al., 2019) explicitly characterizes the IVFFlat recall-speed tradeoff as a function of nprobe/nlist.
- ANN-Benchmarks (Aumuller et al.) treats (index algorithm, params) as the classification variable for comparing systems.

In short, the information retrieval field has the theorem: "same corpus, different index/params => different retrieval capability." This is the subject of the field, not a gap. There is no residue here that IR theory does not own.

The closest native-theory absorber is the recall-latency Pareto frontier: for a fixed corpus, different index families and parameters trace different (recall, latency) tradeoff curves, and these curves are studied as the primary theoretical and empirical object of the ANN literature. The non-factorization through corpus-only projection is the motivation for the entire field, not a new observation.

---

## Part 5: Trivial Enrichment Theorem

The v0.4 Trivial Enrichment Theorem says: define pi'(y) = (pi(y), Cap(y)). Then Cap factors through pi'.

Applied here: if we enrich the visible state to include the capability envelope itself (the achievable result sets per query), factorization is trivially restored. This is vacuous and uninteresting.

The relevant question is whether the natural enrichment is:
- domain-natural: Yes. Adding (index family, construction params, search params, approx tolerance, hardware budget) to the visible state is exactly what ANN system documentation, benchmarks, and papers do. It is not exotic.
- minimal: Approximately yes. You need at least the index family and the search-time parameters to determine the capability envelope. You cannot do with less and still determine which result sets are achievable.
- canonical: Effectively yes. The ANN field has converged on (corpus, metric, index, params) as the canonical description of a retrieval system. There is no controversy about this.
- operationally available: Yes. Any ANN system operator knows their index family and parameters. This is not hidden information.
- already standard in the neighboring theory: Yes. The IR/ANN literature treats (index family, params) as the independent variable in all comparative evaluations.

**Conclusion:** The natural enrichment (adding index and parameter regime to the visible state) is domain-natural, minimal, canonical, operationally available, and already standard. This is not a discovery; it is what the field already does. The enrichment fully restores factorization.

### Minimal Capability-Preserving Quotient

Define ~_Cap on Y as: y1 ~_Cap y2 iff Cap(y1) ~=_K Cap(y2) for all q, k, r, L, f in the task family.

The minimal capability-preserving quotient Y / ~_Cap identifies systems that produce the same achievable result sets across all queries in the task family. In the ANN setting, this quotient is studied under the name "equivalence of retrieval systems" or "same recall-latency curve." It is not a new object; it is implicit in how ANN benchmarks aggregate results across query sets.

The quotient is determined by the (corpus, index algorithm, construction params, search params, hardware budget) tuple, up to implementation-level noise. Systems in the same equivalence class are interchangeable for the declared task.

---

## Part 6: Residue Label and Verdict

### Residue Label: Translation Residue

By the v0.4 residue ladder:

- **Canonical Residue** requires surviving both state-enrichment absorption and native-theory absorption. This witness fails both. The index and parameter regime is the missing state (state-enrichment absorbs it), and the ANN literature owns the non-factorization result as its foundational subject matter (native-theory absorbs it).

- **Formal Residue** requires a typed distinction that survives immediate prior-art absorption as a clean formal object. Nothing new survives here. The typed distinction (capability envelope indexed by index/params) already exists in the ANN literature.

- **Translation Residue** applies when no new formal phenomenon survives, but the audit surface aligns mature theories usefully. This is the correct label. The v0.4 framework provides a clean vocabulary (Y, X, pi, K, Cap, ~=_K, fiber spread, capability-preserving quotient) that could organize a presentation of ANN system comparison, but it does not add formal content that the ANN field lacks.

- **Heuristic Residue** applies when the language helps find missing state. This is partially true: the projection-underdescribed label correctly identifies that "same corpus" is not a sufficient same-visible-state description. But ANN practitioners already know this without the v0.4 vocabulary.

**Assigned label: Translation Residue** (with partial Heuristic Residue for the projection-underdescribed diagnosis as a useful triage tool).

### Verdict

**Is this a legitimate non-self-inflicted witness?**

Partially. The witness pair (HNSW-y1 vs IVFFlat-y2, same corpus) is not self-inflicted in the sense that the projection pi (corpus-only) is operationally meaningful and used in practice (e.g., a user who can read stored vectors but has no access to index internals). The capability difference is real and not manufactured by an artificial equivalence.

However, the witness is non-self-inflicted only at the level of the initial naive projection. Once the same-visible-state discipline is applied properly (the database absorption report's audit template asks: "Index family and parameters — why it matters: they change latency and approximate retrieval capability"), the projection is immediately seen as underdescribed, and state-enrichment absorption applies.

So: the witness demonstrates that a corpus-only projection is capability-insufficient for ANN retrieval. This is true, domain-natural, and not manufactured. But it is also trivially known to anyone in the ANN field. It does not survive absorption as a novel formal result.

**Residue level:** Translation Residue.

The v0.4 framework is a useful vocabulary for stating clearly what the ANN field already knows: capability does not factor through stored vectors alone; it factors through (vectors, metric, index, params, budget). This is a correct and clean restatement, not a new theorem.

**What would be needed for Formal or Canonical Residue in this domain:**

To escape translation residue in the ANN setting, the v0.4 framework would need to produce something the ANN field does not already have. Candidates:
1. A proof that no projection strictly between "corpus only" and "corpus + full system description" is capability-sufficient for all ANN algorithms simultaneously — i.e., a minimality theorem about what must be in the visible state.
2. A transfer theorem connecting ANN recall-latency tradeoffs to capability projection failures in another mature field (e.g., quantum resource theory, Blackwell sufficiency), with a formal mapping that is non-trivial.
3. A canonical enrichment family that characterizes the minimal visible state across multiple approximate query processing paradigms (ANN, approximate joins, approximate aggregation) as instances of a single projection-sufficiency structure.

None of these exist in v0.4. They are speculative directions, not achievements.

---

## Part 7: Domain Calibration Block

Following the v0.4 compact domain calibration pattern:

```
Domain: Vector/ANN retrieval (approximate nearest-neighbor search)
Native absorber: ANN-Benchmarks evaluation framework, HNSW/IVFFlat theory,
                  recall-latency Pareto frontier analysis, pgvector/Faiss/MongoDB documentation
Canonical K candidate: approximate retrieval envelope (achievable top-k sets at declared recall/latency)
Preservation control: exact-search systems (y3, y4) with same corpus achieve same capability; Cap factors
Non-factorization fixture: HNSW-y1 vs IVFFlat-y2 with same corpus C; achievable result sets differ
Likely residue: Translation residue (confirmed by this run)
```

---

## Part 8: Summary for v0.5 Implications

This witness run confirms the database absorption report's conclusion: vector/ANN retrieval is the clearest surviving residue in the database domain not because it escapes absorption, but because the missing state is harder to see at first glance (index internals, graph connectivity) than in relational cases (view definitions, schema).

Once the same-visible-state discipline is applied, the witness is absorbed by:
1. State enrichment: add (index family, params, budget) to X and Cap factors.
2. Native theory: the ANN literature owns the recall-latency-accuracy tradeoff as its core subject.

The witness is legitimate (non-self-inflicted at the naive projection level), domain-natural in both its K type and its Cap definition, and honest about its fate: **Translation Residue**.

For v0.5 to claim stronger residue from the ANN domain, it would need to produce one of the formal targets listed in Part 6. The current v0.4 framework, correctly applied, does not.

---

*Run date: 2026-06-20*
*Protocol: Candidate North Star v0.4 Reviewer Checklist*
*Auditor: Claude Sonnet 4.6 (automated witness run)*
