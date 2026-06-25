# T222: Finite-to-Infinite Boundary Theorem

**Status:** implemented — per-result verdicts with two-sided witnesses; pytest
green (`24 passed`)
**Builds on:** [T59](T59-finite-to-infinite-boundary-audit.md) (audit frame and
Mobius template), [T39](T39-csp-satisfiability-reframing.md),
[T40](T40-holarchy-lab.md), [T41](T41-typed-transport-category.md)
**Precondition for:** honest external publication language about which
proto_independent results have infinite/continuous reach

---

## Target Claims

- CSP-PO1 (signed-graph 2-colorability gluing obstruction)
- D1Cat (typed transport category laws — associativity / identity)
- PO1 Non-Functor Theorem (endpoint admissibility is not a Boolean functor)
- HEF (holonic emergence / cross-level parity obstruction)

These are the four load-bearing rows that the MATHEMATICAL-INDEPENDENCE-AUDIT and
CLAIM-LEDGER carry as `proto_independent`. T59 opened the boundary audit and
resolved one edge (the Mobius continuum probe for CSP-PO1) but left the remaining
results at a Step-1 classification table without two-sided executable witnesses.
T222 closes that gap: it issues a verdict per result with a surviving
generalization on one side and an explicit obstruction at infinity on the other.

## What Is Being Determined

For each result: does it survive to an infinite or continuous analogue, or is it
strictly finite? The deliverable is a **verdict** — `survives`,
`strictly_finite`, or `conditional` — with a witness on each side of the line:
either a surviving generalization (the proof restated without finiteness and
checked on a finitely-represented infinite instance), or an explicit
counterexample / obstruction at infinity.

The line must be drawn explicitly: *which* finite restriction is load-bearing,
and *where* the boundary actually sits (countability vs. continuum vs. structure
level).

## Setup

A single executable signed-graph parity engine (`signed_graph_satisfiable`)
backs the three obstruction-flavored results, exactly as in T39/T40/T59. Each
result has a dedicated verdict function that constructs both sides:

| Result | Survival witness | Other-side witness |
| --- | --- | --- |
| CSP-PO1 | Compactness over countable graphs: growing prefixes of an all-same infinite path stay satisfiable; a planted finite negative triangle is detected in every prefix. de Bruijn–Erdős lifts the finite verdict. | Continuum: T59 coefficient-blind Mobius encoding (same + same) reports a **false global section** despite monodromy −1. |
| D1Cat | Category laws on a countably-infinite (index-shift) site map: associativity and unit laws hold at every coordinate; `preserved_dims` intersection is exhaustively associative/identity in the fixed 4-element universe. | Colimit of a transfinite strictly-descending chain: `preserved_dims` intersection empties; the colimit morphism preserves no dimension — outside the profile axioms every finite D1 object satisfies. |
| PO1 Non-Functor | Existential monotonicity: the finite `(False, False, True)` functor-failure triple embeds unchanged into any infinite-site ambient because PO1 is endpoint-pair-local. | Scope guard (passing note): only the **negative** result persists; a repaired lax/indexed functor at infinity is a separate open question. |
| HEF | Compactness over depth (König): the planted cross-level negative triangle stays obstructed at depths 0…500; unbounded acyclic levels never dissolve it. | False-dissolution guard: the only way depth "dissolves" the obstruction is by dropping the −1 cross-level sign — the same coefficient-blind move T59 flags. |

## The Mobius Template (Honesty Guard)

T59's Mobius result is the template for testing continuum survival without
self-deception: a **coefficient-blind scalar encoding** can give a false global
section. T222 reuses that exact witness for CSP-PO1 and re-applies its discipline
to HEF (the "infinite-path limit dissolves the obstruction" intuition is shown to
be the same false-section move, not a real limit effect). No result is allowed to
"survive to the continuum" by forgetting transition/coefficient data.

## Success Criteria

1. Every survival witness holds: the surviving-generalization proof is checked on
   a finitely-represented infinite instance and confirmed.
2. Every other-side witness holds: the continuum / colimit / scope obstruction is
   exhibited explicitly, not asserted.
3. The verdict distribution is exactly: D1Cat `survives`, PO1 Non-Functor
   `survives`, HEF `survives`, CSP-PO1 `conditional` (0 `strictly_finite`).
4. The boundary line is stated as the **continuum coefficient layer**, with
   countability explicitly identified as *not* the obstruction.
5. The most load-bearing finite restriction is identified (CSP-PO1 at the
   continuum), since it is the shared engine under the holonic results.

## Failure Criteria

- Any survival witness fails: the result does not in fact carry without
  finiteness, and its verdict must be downgraded.
- A continuum survival is claimed without carrying coefficient/transition data
  (the T59 false-section trap).
- A general Čech / sheaf-cohomology theorem is stated from a finite toy witness
  (explicit ROADMAP language guardrail).
- The D1Cat colimit obstruction is hidden inside a blanket "category survives"
  claim, over-reading the three axioms as cocompleteness.
- The PO1 non-functor "survival" is inverted to assert a positive functor at
  infinity.

## Known Physics Constraints

None directly. T222 is a pure mathematical jurisdiction result. It does **not**
promote S1, Q1, H7, or HEF to physics claims; it states the formal conditions
under which each proto_independent result could be borrowed by a substrate that
is not finite. Per COMPLEXITY-LEDGER.md, no hardness/scale language is used: the
parity engine is a `poly_decider` over the declared binary fragment (T39 row);
the compactness lifts are existence arguments, not complexity claims.

## Verdict

| Result | Verdict | Boundary |
| --- | --- | --- |
| CSP-PO1 | **conditional** | Survives countable scale unconditionally (compactness). Continuum: conditional on carrying transition data; coefficient-blind reuse is strictly finite and produces false global sections. |
| D1Cat (category laws) | **survives** | Boundary-free at the category level; the separate colimit-closure at transfinite depth is an explicit open obstruction (intersection empties). |
| PO1 Non-Functor | **survives** | No boundary on the negative result; monotone under category extension. Positive functor at infinity remains open. |
| HEF | **survives** | Survives infinite nesting depth under compactness; inherits the CSP-PO1 continuum condition only if the holarchy becomes genuinely continuous. |

The single boundary line: **the continuum coefficient layer of the shared
signed-graph parity engine. Countability is never the obstruction.**

## Contribution Needed

- Build the coefficient-aware sheaf-H1 replacement for continuous orientation
  data (the recommended-next from T59) and compare its verdict against PO1
  admissibility metadata.
- Construct a D1Cat colimit (or prove none of the desired form exists) so the
  transfinite-chain edge moves from `conditional` to a verdict.
- Decide the positive direction for PO1 at infinity: does a repaired lax /
  indexed functor exist for infinite-system morphisms?
