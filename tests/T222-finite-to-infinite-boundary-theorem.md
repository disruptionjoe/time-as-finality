# T222: Finite-to-Infinite Boundary Theorem

**Status:** implemented — per-result verdicts with two-sided witnesses; pytest
green (`24 passed`)
**Earned corrections:** T226 replaces the single-overlap parity interpretation
with a genuine annular coefficient-aware Čech-H1 object; T228 closes the named
D1Cat descending-chain edge with a legal content-free colimit.
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
| CSP-PO1 | Compactness over countable graphs: growing prefixes of an all-same infinite path stay satisfiable; a planted finite negative triangle is detected in every prefix. de Bruijn–Erdős lifts the finite verdict. | Continuum boundary: T222's T59 two-open signed-CSP control changes verdict when coefficient data are forgotten, but T226 proves the aware single-overlap conflict is not a genuine H1 class and supplies the annular cyclic-nerve correction. |
| D1Cat | Category laws on a countably-infinite (index-shift) site map: associativity and unit laws hold at every coordinate; `preserved_dims` intersection is exhaustively associative/identity in the fixed 4-element universe. | T228 correction: descent reaches empty preservation after at most four finite drops; empty preservation is legal, the chain has a content-free colimit, and only the desired content-bearing form is absent. |
| PO1 Non-Functor | Existential monotonicity: the finite `(False, False, True)` functor-failure triple embeds unchanged into any infinite-site ambient because PO1 is endpoint-pair-local. | Scope guard (passing note): only the **negative** result persists; a repaired lax/indexed functor at infinity is a separate open question. |
| HEF | Compactness over depth (König): the planted cross-level negative triangle stays obstructed at depths 0…500; unbounded acyclic levels never dissolve it. | False-dissolution guard: the only way depth "dissolves" the obstruction is by dropping the −1 cross-level sign — the same coefficient-blind move T59 flags. |

## The Mobius Template (Honesty Guard)

T59's Mobius result is the template for testing continuum survival without
self-deception: a **coefficient-blind scalar encoding** can report a section
after the transition sign is forgotten. T222 reuses that finite signed-CSP
control and re-applies its discipline to HEF. T226 later proves that the
two-open aware conflict is not itself a Čech-H1 class: a genuine H1 obstruction
requires a cyclic nerve. No result is allowed to "survive to the continuum" by
forgetting transition/coefficient data or by relabeling a direct CSP conflict
as cohomology.

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
- The legal content-free D1Cat colimit is mistaken for an absent colimit, or
  the one closed descending-chain case is over-read as general cocompleteness.
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
| CSP-PO1 | **conditional** | Survives countable scale unconditionally (compactness). Continuum: conditional on a genuine coefficient-aware H1 object and refinement/derived bridge; the T222 two-open control is only a finite signed-CSP discriminator. |
| D1Cat (category laws) | **survives** | Boundary-free at the category-law level. T228 closes the named descending-chain edge with a legal content-free colimit and rules out the desired content-bearing form; general cocompleteness remains open. |
| PO1 Non-Functor | **survives** | No boundary on the negative result; monotone under category extension. Positive functor at infinity remains open. |
| HEF | **survives** | Survives infinite nesting depth under compactness; inherits the CSP-PO1 continuum condition only if the holarchy becomes genuinely continuous. |

The single boundary line: **the continuum coefficient layer of the shared
signed-graph parity engine. Countability is never the obstruction.**

## Contribution Status

- **Advanced by T226/T231/T236/T241/T246:** the coefficient-aware H1 object,
  refinement stability, bounded cofinality, and declared annular-tower bridge
  now exist; the all-open-cover continuum statement remains bounded by those
  later artifacts.
- **Closed by T228:** the named D1Cat descending-chain colimit exists in
  content-free form; the desired content-bearing form does not.
- Decide the positive direction for PO1 at infinity: does a repaired lax /
  indexed functor exist for infinite-system morphisms?
