# T47 Results: PO1 DAG Theorem

**Date:** 2026-06-18
**Model:** `models/po1_dag_theorem.py`
**Runner:** `models/run_t47.py`
**Output:** `results/po1-dag-theorem-v0.1.json`

---

## Systems

| System | Sites | Obstructed | Layer |
|--------|-------|------------|-------|
| U1_pre_finality | 3 | False | pre_finality |
| U2_pre_finality | 2 | False | pre_finality |
| O1_post_finality | 3 | True | post_finality |
| O2_post_finality | 2 | True | post_finality |
| O3_post_finality | 3 | True | post_finality |

U1 has globally satisfiable coherence patches (same-same-same triangle).
U2 has no patches (trivially unobstructed).
O1, O3 have parity-conflict patches (same-same-different triangle).
O2 has contradictory patches (same + different, same variables).

---

## Edge Results

**Pairs tested:** 20 (all ordered non-self pairs among 5 systems)
**PO1-admissible edges:** 6

| Source | Target | PO1 | Primary failure |
|--------|--------|-----|-----------------|
| U1_pre_finality | O1_post_finality | True | none |
| U1_pre_finality | O2_post_finality | True | none |
| U1_pre_finality | O3_post_finality | True | none |
| U2_pre_finality | O1_post_finality | True | none |
| U2_pre_finality | O2_post_finality | True | none |
| U2_pre_finality | O3_post_finality | True | none |
| U→U (2 pairs) | — | False | AC6 (target not obstructed) |
| O→U (6 pairs) | — | False | AC6 (target not obstructed; AC7 also fails) |
| O→O (6 pairs) | — | False | AC5 (profiles identical; AC7 also fails) |

**Note on primary-failure column:** The column shows the first failing condition
in AC1-AC7 order, not the structural cause of failure. For all 12 O-source pairs,
AC7=False (source obstructed) is the structural cause. AC5 or AC6 happen to appear
earlier in the collection order, so they are listed as primary. The theorem depends
on AC7=False for all O-source pairs, which holds in all 12 cases.

---

## DAG Analysis

| Property | Value |
|----------|-------|
| Is DAG | True |
| Max path depth | 1 |
| Is bipartite | True |
| Pre-finality nodes | U1, U2 |
| Post-finality nodes | O1, O2, O3 |
| Topological sort | U1, U2, O1, O2, O3 |

The admitted edge graph is a complete bipartite graph K_{2,3}: every pair
(Uᵢ, Oⱼ) admits a PO1-admissible morphism. All 6 edges go from pre-finality
to post-finality. No edge exists within either layer or in the reverse direction.

---

## Theorem

**PO1 DAG Theorem (T47):**
The directed graph of PO1-admissible D1RestrictionMorphisms in D1Cat is
acyclic. No directed cycle of PO1-admissible morphisms can exist.

**Proof:**
Suppose f₁, ..., fₙ form a PO1-admissible cycle A₁ -> A₂ -> ... -> Aₙ -> A₁.
For f₁: A₁ -> A₂ to be PO1-admissible, AC7 requires A₁ to be unobstructed.
For fₙ: Aₙ -> A₁ to be PO1-admissible, AC6 requires A₁ to be obstructed.
A₁ cannot be simultaneously obstructed and unobstructed. Contradiction.
Therefore no PO1-admissible directed cycle exists.

The proof depends only on AC6 and AC7, not on the specific systems or morphism
construction. It applies to any D1RestrictionSystems and any D1RestrictionMorphisms
in D1Cat. The finite witness here confirms the pattern: all AC7 failures occur
precisely when the source is obstructed.

---

## Corollaries

**Corollary 1 (Depth Bound):**
No PO1-admissible chain has length greater than one.
If f: A -> B is PO1-admissible, then B is obstructed (AC6 of f). Any morphism
g: B -> C would require AC7: B unobstructed. Contradiction. Therefore all
PO1-admissible paths have length at most one.
Verified: max_depth = 1 in this model.

**Corollary 2 (Bipartite Structure):**
The PO1-admissible sub-graph of D1Cat is bipartite between unobstructed systems
(pre-finality layer) and obstructed systems (post-finality layer), with all
edges directed from pre- to post-finality.
Verified: admitted edges = {U1, U2} x {O1, O2, O3}.

**Corollary 3 (Finality Border):**
PO1-admissible morphisms mark the finality boundary in D1Cat as a categorical
one-way gate. Every PO1-admissible morphism crosses from pre-finality to
post-finality. No PO1-admissible morphism crosses in the reverse direction.

---

## Connections to Prior Results

**T41 (D1Cat is a proper category):** D1Cat admits all D1RestrictionMorphisms,
including identity morphisms (A -> A) and arbitrary compositions. D1Cat can have
cycles. T47 does not contradict T41: T47 restricts to the PO1-admissible
subgraph of D1Cat, which is a sub-structure, not the full category. D1Cat itself
remains a proper category with all its structure intact.

**T45 (Measurement Asymmetry):** T45 showed that the specific measurement
morphism f: Y -> X is PO1-admissible and that no PO1-admissible inverse exists.
T47 generalizes: it is not just this specific pair that lacks a reverse morphism —
no PO1-admissible morphism can ever originate from any obstructed system.
T45 is a special case of T47.

**T34 (PO1 Chain Theorem):** T34 showed that endpoint admissibility of a composed
morphism is independent of the admissibility of intermediate morphisms. T47 shows
that PO1-admissible morphisms cannot be chained at all (depth <= 1). These results
do not conflict: T34 asks about the admissibility of a COMPOSED morphism f;g given
f and g; T47 asks whether a sequence of individually PO1-admissible morphisms can
form a chain. The answer to T47's question is no: if f is PO1-admissible, then
the target of f is obstructed, making any subsequent PO1-admissible g impossible.

**H7 (Finality-Induced Direction):** T18 showed that D1-monotone admissibility
induces an acyclic finality direction. T47 provides the categorical witness: the
PO1-admissible sub-graph of D1Cat IS an acyclic directed graph, and it is
bipartite between pre- and post-finality systems. The finality direction is not
just acyclic in the abstract — it has a specific two-tier structure.

**H1 (Record Reconstruction):** The PO1 partial order (A -> B means there exists
a PO1-admissible morphism from A to B) is a candidate causal partial order:
sources are pre-finality systems (no obstruction), targets are post-finality
systems (obstruction). Any topological sort of the PO1 sub-graph is a valid
temporal ordering consistent with the finality boundary.

---

## Hypothesis Verdicts

| Hypothesis | Claim | Status |
|------------|-------|--------|
| H_DAG | PO1 sub-graph of D1Cat is acyclic | **supported** |
| H_DEPTH1 | No PO1-admissible chain has length > 1 | **supported** |
| H_BIPARTITE | PO1 sub-graph is bipartite (pre vs post finality) | **supported** |
| H_BORDER | All PO1-admissible morphisms cross pre- to post-finality | **supported** |

**Best supported:** H_DAG, H_DEPTH1, H_BIPARTITE, H_BORDER (all four hold)

---

## Boundary

- Five systems are tested. The proof sketch is general; the finite witness
  confirms the pattern but does not cover infinite or continuous D1RestrictionSystems.

- The canonical morphism (many-to-one site map, preserved_dimensions=reversal_cost)
  is one morphism per pair. For the rejected pairs, the failure at AC7 is
  morphism-independent — no morphism from an obstructed source can pass AC7.
  For the admitted pairs, other morphisms with different preserved_dimensions or
  forgotten_structure might fail AC5 even if this canonical one passes.

- The bipartite structure (K_{2,3} complete bipartite graph) is a property of
  this specific five-system model. In a general D1Cat, not every unobstructed
  system need admit a PO1-admissible morphism to every obstructed system — site
  map constraints or profile constraints might prevent AC3 or AC5. The theorem
  (no cycles, depth <= 1) holds in general; the complete bipartite shape is a
  feature of this particular model.
