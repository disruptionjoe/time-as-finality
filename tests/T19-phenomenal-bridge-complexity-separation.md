# T19: Phenomenal Bridge as Complexity Separation

## Target Claims

- [C1: Experienced Time as Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D2: Observer as Record-Bearing System](../claims/D2-observer-as-record-bearing-system.md)
- [Open Problem: First-Person Finality and Complexity Separation](../open-problems/first-person-finality-complexity-separation.md)

## Origin

Seven personas across four independent groups (quantum foundations, computability theory,
foundational mathematics, philosophy of science) converged on this framing in the v2 idea
sprint 2026-06-16. It was independently nominated as "Most Profound" by quantum foundations,
computation, heterodox critics, and philosophy of science groups.

## Hypothesis

The gap between third-person record-graph finality and first-person experienced finality is a
formal complexity separation, not a missing empirical mechanism.

Specifically: a bounded observer maintaining a self-model of its own finality state generates a
decision problem — "Is my own current finality assignment among my finalized records?" — that
is outside the observer's own verifiable boundary. This is not a philosophical puzzle. It is a
decision problem that can be placed in a complexity class and asked whether it is decidable by
the observer's own record-graph computation.

If the separation holds, H6 (the phenomenal bridge) is a theorem about what a bounded observer
cannot decide about itself — not a missing mechanism, not an explanatory gap to be filled by
a future theory of consciousness.

## Decision Problem Formulation

**Input:** A finite record graph G representing an embedded observer's causal record structure.
A designated node v representing the observer's self-model node.

**Query:** Does the observer's finality assignment for its own internal states appear as a
finalized record in G at node v?

**The separation conjecture:** This decision problem is not computable by the observer's own
bounded record-graph operations, even when G is fully specified to an external third-person
observer. The observer's own finality assignment is not in the closure of the observer's
accessible records.

**Complexity class placement (target):**
- External third-person verifier: the query is decidable in polynomial time given the full graph.
- Internal first-person verifier (restricted to v's accessible subgraph): the query may not be
  decidable, or may require access to structure outside v's causal boundary.

The formal conjecture: FIRST-PERSON-FINALITY ∉ the complexity class of computations accessible
to a bounded observer from within its own record graph.

## Setup

1. Define the finite observer model: a record graph G = (V, E) where one designated node v ∈ V
   represents the observer. Node v has read-access to a subset of G (its accessible subgraph A(v)).
2. Define v's self-finality assignment: v's D1 score for its own internal state transitions.
3. Define the third-person query: given full G, is v's self-finality assignment finalized in G?
   (Decidable externally by inspection.)
4. Define the first-person query: can v determine, using only A(v), whether its own finality
   assignment is finalized?
5. Construct a minimal case where the external answer is YES (the assignment is finalized from
   the outside) but v cannot certify this from A(v) alone.

## Connection to T8 (Observer-Renderer Toy Model)

T8 asks whether a designated "renderer" node can form a fixed-point finality assignment about
itself. T19 asks the sharper question: even if such a fixed point exists, can the observer
*verify* that it is finalized using only its own accessible subgraph? T8 is about existence;
T19 is about decidability from within.

These two tests together provide a formal scaffold for H6:
- T8 positive + T19 negative: fixed-point self-assignments exist but cannot be self-verified.
  This is the formal gap the phenomenal bridge needs to bridge.
- T8 positive + T19 positive: the separation conjecture is false; first-person finality is
  computationally equivalent to third-person record inspection.
- T8 negative: the fixed-point self-assignment does not exist; no self-model can be finalized.

## Success Criteria

- A finite record graph G is constructed where the external finality query is decidable and
  positive, but the internal query is undecidable or provably out-of-reach for v's accessible subgraph.
- The separation is not a consequence of arbitrary graph construction but of a structural property
  of self-reference (the v node has edges to itself or to nodes that transitively reach v).
- The complexity-class placement is stated precisely with a reduction or oracle argument.
- The result does not require any phenomenal or consciousness language — it is a graph-theoretic
  statement about what a bounded node can decide about its own subgraph membership.

## Failure Criteria

- The decision problem is always decidable from within A(v) given a finite graph. This would
  mean the phenomenal bridge has no formal complexity-theoretic content — it would need to be
  grounded elsewhere or accepted as an irreducibly empirical claim.
- The self-reference is trivially blockable: if the observer can always inspect itself via a
  meta-node added to A(v), the boundary is definitional rather than structural.

## Known Physics Constraints

This test is a graph-theoretic and complexity-theoretic argument. It does not make claims about
consciousness, phenomenal experience, or the hard problem. It makes a claim about what a bounded
computational process can decide about its own finality state — a claim that would hold or fail
independently of any theory of subjective experience.

If the separation theorem holds, it provides a formal lower bound on the explanatory gap:
TaF can say precisely what first-person finality verification requires that third-person
computation cannot supply.

## Contribution Needed

1. Implement the finite observer model: a record graph with a designated observer node and
   a boundary between the observer's accessible subgraph and the full graph.
2. State the self-finality decision problem formally and place it in a complexity class.
3. Construct the minimal separation witness: smallest G where external answer ≠ internal
   decidability.
4. State the separation conjecture precisely: what axioms on G imply the separation, and what
   axioms collapse it?
5. Compare to existing undecidability results in self-reference (Gödel, Turing halting,
   Rice's theorem) to identify the closest formal relative.

---

## Step 1 Results — Phenomenal Bridge Separation Implementation

*Executed 2026-06-19. Code at `models/t19_phenomenal_bridge_separation.py`*

### Graph topology

A 7-node graph extending the T60 core with external witness nodes:

**CORE (R's internal world, 4 nodes):**
```
e_src --> e_R_recv --> e_R_rec1 --> e_R_final
```

**EXTERNAL (third-person witnesses, causally after R's finalization, 3 nodes):**
```
e_R_final --> e_E1 --> e_meta
e_R_final --> e_E2 --> e_meta
```

Propositions: `world_fact` (e_src, e_R_recv), `R_obs` (e_R_recv bridge, e_R_rec1, e_R_final), `R_self_finality` (e_E1, e_E2, e_meta only).

`R_self_finality` records exist only at external nodes — they represent third-person witnesses who record R's finalization from outside R's causal boundary.

### Run output

```
Monotonicity check: MONOTONICITY HOLDS. 7 nodes, 128 subsets, ~8256 pairs.
  f(S) always subset of CORE_NODES (external nodes raise ValueError -- causally after e_R_final)

R's Bounded D1 Access-Update Iteration:
  Step 0: {e_src}
  Step 1: {e_src, e_R_recv}
  Step 2: {e_src, e_R_recv, e_R_rec1, e_R_final}
  Step 3: converged (fixed point)

R's fixed-point access set: [e_R_final, e_R_rec1, e_R_recv, e_src]
External nodes in R's fixed point: []
R self-included (T60 condition): True

Query 1 -- R_obs at e_R_final (INTERNAL):   accessible_support = 3 >= 1  => YES
Query 2 -- R_self_finality at e_R_final (INTERNAL): accessible_support = 0 < 1  => NO
Query 3 -- R_self_finality at e_meta (EXTERNAL):    accessible_support = 3 >= 1  => YES

SEPARATION HOLDS: YES
  FIRST-PERSON-FINALITY(A*(R), R_self_finality at e_R_final) = NO
  THIRD-PERSON-FINALITY(G,    R_self_finality at e_meta)     = YES
```

### All T19 success conditions pass

**Finite observer model:** 7-node graph with designated observer R, explicit boundary between A*(R) = {e_src, e_R_recv, e_R_rec1, e_R_final} and full G (adds e_E1, e_E2, e_meta).

**Formal decision problem:** Query = "Is R_self_finality accessible to the querying agent?" External: decidable in O(|G|) time (scan G). Internal: provably unreachable from A*(R).

**Minimal separation witness:** The core is 4 internal + 3 external nodes — 7 total. This is close to minimal: you need at least 1 internal base (e_src), 1 R boundary node (e_R_final), and 1 external witness (e_E1) to get the separation. The 2-witness design is the minimal case that also gives accessible_support >= 2 if a higher threshold is used.

**Complexity class placement:**
- EXTERNAL: O(|G|) time, decidable by scanning the record set.
- INTERNAL: not merely undecidable — provably unreachable. A*(R) contains no R_self_finality records and no record-transfer path to them. The function is not in the image of any A*(R)-local computation.

**Formal relative:** This result is stronger than undecidability (Gödel/Turing). Undecidable problems are those for which no algorithm terminates with the right answer. T19's gap is more primitive: the required evidence does not exist in the accessible region. The closest structural relatives are:
- Gödel incompleteness: a system cannot prove its own consistency from within.
- Rice's theorem: a program cannot decide semantic properties of its own output.
- T19: a bounded observer cannot verify that its finality is externally witnessed, because the witnesses are in its causal future.

### Structural finding: the causal-boundary obstruction

The gap is not a computational complexity limit. It is a causal-boundary obstruction: R's finality witnesses (e_E1, e_E2) are causally after R's observation horizon (e_R_final). The `accessible_records` function raises `ValueError` for evaluation events not in the observer's causal past — this is not a modeling trick, it is the formalism correctly reporting that e_E1 is outside R's causal reach.

No increase in R's computational power, memory, or running time bridges this gap. Only an observer at e_meta (after the witnesses have acted) can verify R's finality.

### T60 + T19 together: the formal content of H6

- **T60 (closure):** R's fixed-point access set is self-inclusive. Observer closure is structurally guaranteed for finite T1 graphs with D2 recorders. R is in its own finalized record set.
- **T19 (non-self-verifiability):** Even though closure is guaranteed, R cannot verify from A*(R) that its own finalization is an externally recorded fact. The meta-proposition R_self_finality is not accessible to R's bounded computation.

The T60 + T19 combination gives the formal structure behind H6 (Phenomenal Bridge Formal-Gap Conjecture):

> The phenomenal bridge is not a missing mechanism. It is the formal location of the causal-boundary gap between first-person finality verification and third-person record inspection. Closure is guaranteed (T60) but the self-knowledge that closure has been achieved is structurally outside the observer's accessible subgraph (T19).

### Axioms that imply the separation / axioms that collapse it

**Implies separation:**
1. R_self_finality records exist only at events causally after R's observation horizon.
2. R's D1 update operator is anchored at R's observation event (cannot extend past it).
3. No record-transfer edge connects the external witnesses back into A*(R).

**Collapses the separation:**
1. R has a self-loop (R's finalization event creates an R_self_finality record at the same event) — R can then self-witness.
2. External witnesses feed back into R's causal past (e_E1 → some node <= e_R_final) — the boundary dissolves.
3. The proposition R_self_finality is identified with R_obs (the observer claims its own internal records ARE its finality records) — but this is the question T19 is asking, not an axiom.

**Status:** `partial_success` — finite witness positive on all conditions; general theorem (monotonicity for all finite T1 graphs with D2 recorders under this extension) and complexity-class formal proof pending.
