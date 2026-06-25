# T222 Results: Finite-to-Infinite Boundary Theorem

## Verdict Summary

Four load-bearing proto_independent results classified against the finite/infinite boundary. D1Cat category laws and the PO1 non-functor theorem survive unconditionally (algebraic / existential-monotone). HEF survives to infinite nesting depth under compactness. CSP-PO1 is conditional: it survives countable scale unconditionally but is strictly finite at the continuum unless coefficient and transition data are carried. The single boundary line is the continuum coefficient layer of the signed-graph parity engine; countability is never the obstruction.

Counts: survives = 3, conditional = 1, strictly_finite = 0. All witnesses hold = True.

## Per-Result Verdict Table

| Result | Source tests | Verdict | Boundary line |
| --- | --- | --- | --- |
| CSP-PO1 (Signed-graph 2-colorability gluing obstruction (PO1-as-CSP)) | T39, T59 | **conditional** | Boundary sits at the continuum coefficient layer, not at countability. Countable: survives. Continuous: conditional on carrying transition data; the obstruction object is sheaf H1 with the correct coefficient group, not blind same/different CSP. |
| D1Cat (Typed transport category laws (associativity / identity)) | T41, T34 | **survives** | The category itself is boundary-free. The boundary lies one level up: completeness/cocompleteness (limits/colimits) of D1Cat at transfinite depth is not established and the obvious limit object is degenerate. |
| PO1-NonFunctor (PO1 admissibility is not a Boolean functor on D1Cat) | T41, T34 | **survives** | No boundary on the negative result: non-functoriality is monotone under category extension. The open frontier is the positive direction (repaired lax/indexed functor) for infinite systems. |
| HEF (Holonic emergence / cross-level parity obstruction) | T40, T59 | **survives** | No depth boundary for the obstruction phenomenon: finite-cycle obstructions are compactness-stable. The boundary that does exist is the same continuum-coefficient boundary as CSP-PO1, inherited via the shared signed-graph parity engine. |

## Witnesses

### CSP-PO1 — conditional

Survival hypothesis: Survives to countably infinite constraint graphs unconditionally (compactness). At the continuum it survives only after the coefficient object and transition signs are reduced to a signed finite (transition-aware Z2) problem; the coefficient-blind scalar reuse is strictly finite and produces false global sections.

- **infinite_survival** [holds]: Countably infinite signed CSP: satisfiability decided by finite sub-graphs via propositional compactness (de Bruijn-Erdos).
  - Growing prefixes of an all-same infinite path stay satisfiable (windows n=3,5,8,20 -> [True, True, True, True]); a planted finite negative triangle is detected in every prefix containing it (unsat windows -> [False, False, False, False]). Compactness lifts the finite verdict to the countable limit.
- **continuum_obstruction** [holds]: Continuous orientation data (Mobius): coefficient-blind scalar encoding reports a false global section; parity is not a generic continuum detector.
  - Transition-aware Z2 encoding (same + different) is a direct parity conflict -> obstruction detected (True). Coefficient-blind scalar encoding (same + same) is satisfiable (True) despite monodromy -1: a false global section. Cylinder control satisfiable in both (True). Inherited from T59.

Guardrail: No general Cech/sheaf-cohomology theorem is claimed from the finite Mobius witness. The continuum statement is a counterexample plus a stated replacement target (coefficient-aware H1).

### D1Cat — survives

Survival hypothesis: Category laws (associativity, left/right identity) survive to arbitrary (countably infinite) site sets unconditionally; the proof is algebraic in functions and in the fixed 4-element dimension universe. The SEPARATE colimit-closure question (transfinite chains, T34 extension) is conditional: it needs a colimit construction that does not yet exist, and the natural intersection limit empties.

- **infinite_survival** [holds]: Category laws hold for countably infinite site sets: site_map composition is function composition (associative); preserved_dims is intersection in the fixed 4-element D1_DIMENSIONS universe.
  - Index-shift site maps on N: associativity True, left unit True, right unit True over 1000 coordinates. preserved_dims intersection over all 16 subsets of the fixed universe: associative True, identity True. Site cardinality never enters the proof.
- **infinite_obstruction** [holds]: Colimit of a transfinite strictly-descending chain: preserved_dims intersection empties; the colimit morphism preserves no dimension, outside the profile axioms every finite D1 object satisfies.
  - Descending preserved_dims chain reaches the empty intersection (True). The accumulated forgotten_structure colimit remains a well-defined set union (True), so the failure is specifically the empty-preservation limit object, not the loss annotation. No D1Cat colimit construction exists yet.

Guardrail: Do not over-read 'category survives' as 'D1Cat is complete at infinity'. Only the three category axioms are shown finiteness-independent; colimit closure is an explicit open obstruction.

### PO1-NonFunctor — survives

Survival hypothesis: The non-functor theorem is existential and survives unconditionally: a finite counterexample to Boolean-and functoriality embeds into any infinite-site ambient with its verdict intact, since PO1 is an endpoint-pair-local predicate. Only the negative result is asserted at infinity; no positive functor is claimed.

- **infinite_survival** [holds]: Existential non-functoriality survives: the finite (False, False, True) counterexample embeds unchanged into any infinite-site ambient, because PO1 is endpoint-pair-local.
  - Finite triple (f,g,fg PO1) = (False, False, True); functor violated True. Embedding into ambients of 10 / 100 / 10000 sites leaves the endpoint-local verdict invariant -> still violated True. An existing counterexample cannot be un-witnessed by enlarging the ambient.
- **infinite_survival** [holds]: Scope guard: persistence of the NEGATIVE result only. Whether some repaired (lax/indexed) functor exists for infinite-system morphisms is a separate open question, not decided here.
  - T222 confirms the obstruction to Boolean-and functoriality carries to infinity; it does not certify any positive functor at infinity. If obstruction detection is later redefined via sheaf H1 for infinite systems, the positive functor question resets (T59).

Guardrail: Survival here means 'the obstruction persists', not 'the functor exists'. Do not invert the polarity.

### HEF — survives

Survival hypothesis: Holonic emergence survives to infinite nesting depth under compactness (Konig's lemma): the obstruction is a finite negative cycle in the combined signed graph and cannot be removed by adding acyclic levels. Apparent dissolution at the infinite-path limit is a coefficient-blind artifact (dropping the cross-level sign), guarded against by the T59 discipline.

- **infinite_survival** [holds]: Holonic emergence survives infinite nesting depth: the cross-level parity obstruction is a finite negative cycle, lifted by compactness (Konig's lemma) -- adding unbounded acyclic depth never dissolves it.
  - Planted cross-level triangle stays obstructed at depths (0, 1, 5, 50, 500) -> [True, True, True, True, True]. The same holarchy without the planted -1 stays satisfiable at all depths -> [True, True, True, True, True]. Obstruction localizes to L0/L1/L2; deeper acyclic levels are irrelevant to it.
- **infinite_obstruction** [holds]: False-dissolution guard: the only way infinite depth 'dissolves' the obstruction is by forgetting the -1 cross-level sign -- the same false-section move T59 flags. With the sign kept, depth is inert.
  - Replacing the planted L0!=L2 (-1) with a same (+1) edge makes the depth-500 holarchy satisfiable (True); keeping the sign keeps it obstructed. Dissolution is an artifact of dropping coefficient/transition data, not a real limit effect.

Guardrail: Survival is for the discrete (countable) cross-level CSP. A genuinely continuous holarchy inherits the CSP-PO1 continuum condition; no sheaf-cohomology emergence theorem is claimed.

## Most Load-Bearing Finite Restriction

CSP-PO1 at the continuum. The signed-graph parity obstruction is the shared engine under HEF and the holonic results, and its continuum restriction is the one place a coefficient-blind reuse silently produces a false global section. Any external paper that states a continuous-domain obstruction must carry the coefficient/transition object (transition-aware Z2 / coefficient-aware H1); the D1Cat colimit gap is a secondary, contained, structure-level open item.
