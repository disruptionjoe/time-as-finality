# Spacetime as Colimit of Finality Domains

## Problem

Can classical spacetime be derived as the colimit of a diagram of observer-local finality domains, rather than being assumed as the arena in which finality events occur?

This is the most structurally ambitious open problem in the project. Five independent disciplinary formalisms arrived at the same hypothesis from different starting points during the 2026-06-16 idea sprint:

- **Higher/Derived Geometry:** S1 has a precise statement as a colimit in a suitable higher topos of finality domains.
- **Operator Algebra/NCG:** Classical spacetime is the commutative C*-algebra limit of a noncommutative finality algebra recovered when all observer preorders are compatible.
- **QFT:** Path integral restricted to finalized field configurations gives a UV-finite sum; spacetime emerges from summing only over classically recordable histories.
- **Stochastic Geometry:** Smooth spacetime is the large-N limit of a stochastic differential geometry whose metric is the fluctuation spectrum of local finality measures as recorder density grows.
- **Wolfram Physics:** The physical universe is the branch of the multiway graph that has achieved maximal causal invariance; smooth spacetime is the fixed-point of branch-merge convergence.

That five unrelated formalisms converge on the same structural claim is the strongest cross-disciplinary signal from the idea sprint.

## Working Claim

Classical spacetime is not the ground floor on which finality events happen. It is the output of finality aggregation — the stable interface that emerges when many bounded observer-systems' locally consistent finality preorders are stitched together up to a compatibility condition.

## Why It Might Help

Current TaF holds S1 (spacetime as consensus envelope) as a speculative extension and explicitly warns against making it load-bearing. This open problem asks whether S1 can be promoted — not by handwaving but by constructing an explicit map from a diagram of finality domains to a classical spacetime object.

If the construction works, TaF is not a description of what happens in spacetime. It is a derivation of spacetime itself.

## How It Could Mislead

- Colimit language suggests spacetime is built from parts, which may conflict with diffeomorphism invariance if the construction is not covariant.
- The large-N or commutative limit must be taken carefully — limits of quantum algebras do not automatically produce the correct classical geometry.
- "Emerges from" cannot be a metaphor here; the construction must be explicit.

## Formal Entry Points

Each formalism offers a concrete first step:

1. **Topos approach:** Define a site of causal diamonds with finality sheaves as structure sheaves. Ask whether the classifying topos has a geometric morphism to Sh(Lorentzian manifold).
2. **NCG approach:** Define a spectral triple for each observer's finality C*-algebra. Check whether the direct limit of spectral triples converges to a commutative spectral triple (a Riemannian manifold).
3. **Path integral approach:** Restrict the Euclidean path integral to histories satisfying D1's finality threshold. Check whether the restricted partition function is UV-finite and reproduces the correct low-energy effective action.
4. **Stochastic approach:** Define a Langevin equation for finality measure diffusion on a random graph. Compute the large-N stationary distribution. Check whether the induced metric is a Lorentzian signature manifold.

## Connection to Existing Tests

- [T7: Overlapping Causal Domains](../tests/T7-overlapping-causal-domains.md)
- [T15: Causal Record Graph as Causal Set](../tests/T15-causal-record-graph-as-causal-set.md)
- [T13: Finality Sheaf Cohomology](../tests/T13-finality-sheaf-cohomology.md)
- [T16: Spacetime Aggregation Toy Model](../tests/T16-spacetime-aggregation.md)

## T16 Result

T16 implements the minimum finite version of this open problem: local
finality domains are partial orders, overlap restrictions must agree, and the
union must remain acyclic. Successful aggregation returns a global partial
order. Failure returns either an overlap-disagreement witness or a global
cycle witness.

The result is intentionally weak: it defines the first gluing target but does
not derive a manifold, metric, or physical spacetime.

## Contribution Needed

Choose one entry point and make it precise. The minimum deliverable is a formal definition of the colimit/limit object and a check that it is well-defined (not just that it "should be" classical spacetime by hand-waving). The maximum deliverable is a proof that the construction reproduces a known result in GR or QFT as a limiting case.
