# T47: PO1 DAG Theorem

## Target Claims

- [PO1: Projection-Obstruction Schema](../claims/PO1-projection-obstruction-schema.md)
- [H7: Finality-Induced Direction](../HYPOTHESES.md)
- [T41: Typed Transport Category](T41-typed-transport-category.md)
- [T45: Measurement PO1 Asymmetry](T45-measurement-po1-asymmetry.md)

## Central Question

Do PO1-admissible morphisms in D1Cat form a directed acyclic graph (DAG)?
And does this DAG have a specific structural shape — bipartite between
unobstructed (pre-finality) and obstructed (post-finality) systems, with
all paths of length at most one?

## Theorem (Candidate)

**PO1 DAG Theorem:** The directed graph of PO1-admissible D1RestrictionMorphisms
in D1Cat is acyclic. No directed cycle of PO1-admissible morphisms can exist.

**Proof:**
Suppose f₁, ..., fₙ form a directed PO1-admissible cycle A₁ -> A₂ -> ... -> Aₙ -> A₁.
For f₁: A₁ -> A₂ to be PO1-admissible, AC7 requires A₁ to be unobstructed.
For fₙ: Aₙ -> A₁ to be PO1-admissible, AC6 requires A₁ to be obstructed.
A₁ cannot be simultaneously obstructed and unobstructed. Contradiction.
Therefore no PO1-admissible directed cycle exists.

**Corollary 1 (Depth Bound):** No PO1-admissible chain has length greater than
one. Proof: If f: A -> B is PO1-admissible, then B is obstructed (AC6 of f).
For any g: B -> C to be PO1-admissible, AC7 requires B to be unobstructed.
Contradiction. Therefore no PO1-admissible morphism can start from B.

**Corollary 2 (Bipartite Structure):** The PO1-admissible sub-graph of D1Cat
is bipartite between unobstructed systems (pre-finality layer) and obstructed
systems (post-finality layer), with all edges directed from pre- to post-.

**Corollary 3 (Finality Boundary):** PO1-admissible morphisms cannot cross the
finality boundary in the reverse direction. The boundary is the obstruction
status of the system. Unobstructed systems are categorically prior to obstructed
systems in the PO1-induced order.

## Setup

Five D1RestrictionSystems are constructed:

**Pre-finality layer (unobstructed):**
- U1: three sites, globally satisfiable patches
- U2: two sites, no patches (trivially unobstructed)

**Post-finality layer (obstructed):**
- O1: three sites, parity-conflict patches (same-same-different triangle)
- O2: two sites, contradictory-constraint patches (same + different, same variables)
- O3: three sites, different parity-conflict patches

All 20 ordered pairs (A, B) with A != B are tested with a canonical morphism.

For each pair, the canonical morphism:
- Has a total site map (many-to-one if source has more sites than target)
- Declares preserved_dimensions = ("reversal_cost",)
- Declares forgotten_structure = ("pre_finality_structure",)
- Does not require trust-path or obstruction preservation

The AC1-AC7 verdict is recorded for each pair.

## Hypotheses Evaluated

- H_DAG: The PO1-admissible sub-graph of D1Cat is a DAG (no directed cycles).
- H_DEPTH1: No PO1-admissible chain has length greater than one.
- H_BIPARTITE: The PO1-admissible sub-graph is bipartite between unobstructed
  and obstructed systems.
- H_BORDER: PO1 induces a categorical finality boundary: all PO1-admissible
  morphisms cross from pre-finality to post-finality, never the reverse.

## Success Criteria

1. At least one forward morphism (U -> O) is fully PO1-admissible.
2. No backward morphism (O -> anything) is PO1-admissible; all fail AC7.
3. No same-layer morphism (U -> U) is PO1-admissible; all fail AC6.
4. The DAG property is verified by cycle-detection algorithm.
5. The depth bound is verified: no admitted path has length > 1.
6. The bipartite structure is confirmed: all admitted edges go from U-nodes to O-nodes.
7. A topological sort of the admitted graph is produced.
8. The proof sketch is confirmed by the failure pattern of cycle attempts.

## Failure Criteria

1. Any O -> anything morphism is fully PO1-admissible.
   (Would refute the theorem — AC7 should always fail when source is obstructed.)

2. Any U -> U morphism is fully PO1-admissible.
   (Would mean the same system can be both source and target in a non-trivial
   PO1 structure without an obstruction at the target.)

3. A PO1-admissible chain A -> B -> C of length 2 is constructed.
   (Would refute Corollary 1 — B would be obstructed by the first morphism
   and must be unobstructed for the second.)

4. A cycle is detected in the admitted-edge graph.
   (Would directly refute the theorem.)

5. The proof sketch is invalid: a case exists where A₁ is both obstructed
   and unobstructed simultaneously. (Definitionally impossible but should be
   confirmed by the model that no such case exists.)

## Known Constraints

- This tests five specific systems. The theorem is structural and applies to
  any D1RestrictionSystems; the five systems are a finite witness, not a
  complete enumeration.
- The canonical morphism is one morphism per pair. Other morphisms might have
  different admissibility if site maps or preserved dimensions differ. The
  failure cases (O -> anything) fail AC7 regardless of morphism construction,
  making the failure independent of morphism choice.
- This does not claim that D1Cat has no cycles in general -- only that the
  PO1-admissible sub-graph does not. D1Cat (all D1RestrictionMorphisms, not
  just PO1-admissible ones) is a proper category and can have identity
  morphisms and composable cycles not subject to PO1 constraints.

## Contribution Needed

- If the bipartite structure holds, state it as a named structural fact about
  D1Cat and connect it to H7 (finality-induced direction).
- If the depth bound holds, note that PO1 does not compose in the sense of
  T34 -- the chained admissibility of T34 refers to a different question
  (endpoint admissibility of a composed morphism) than the PO1 chain here.
- Test more systems with varied obstruction patterns to confirm the bipartite
  structure is not an artifact of the specific five systems chosen.
