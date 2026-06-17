# T13: Finality Sheaf Cohomology

## Target Claims

- [C1: Experienced Time as Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [R1: Relativity No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)

## Origin

Algebraic Topologist and Differential Geometer lenses, idea sprint 2026-06-16.

## Hypothesis

The collection of finality preorders across all observers forms a sheaf over the spacetime manifold. The Cech cohomology of this sheaf detects global inconsistencies — configurations where no local observer can resolve an ordering conflict — that are invisible at the level of any single observer's preorder.

H¹ nonzero would mean observer-indexed preorders cannot always be stitched into a global finality structure. This would make observer-dependence a structural topological feature of TaF rather than a notational choice.

## Setup

1. Define the sheaf: the base space is a finite spacetime (e.g., a Minkowski diamond discretized to a small causal set); the stalk over each spacetime region is the finality preorder for observers within that region; restriction maps are causal inclusion.
2. Verify the sheaf axioms (locality and gluing) hold under causal inclusion.
3. Compute the Cech cohomology groups H⁰, H¹ for a covering by causal diamonds.
4. Construct a minimal configuration with H¹ ≠ 0 — a set of locally consistent finality assignments that cannot be globally extended.
5. Interpret: does the H¹ generator correspond to a physically interpretable obstruction (e.g., a spacelike-separated finalization conflict)?

## Success Criteria

- The finality preorder assignment satisfies sheaf axioms under causal inclusion.
- At least one configuration produces H¹ ≠ 0, supplying a concrete topological obstruction to global finality.
- The obstruction corresponds to a physically interpretable situation (relativity of finality, not merely a formal artifact).

## Failure Criteria

- All cohomology groups are trivial — all locally consistent finality assignments extend globally. This would weaken C1's observer-dependence claim: if global finality is always reconstructible, observer-indexing may be a convenience rather than a necessity.
- The sheaf axioms fail under causal inclusion — the assignment is a presheaf but not a sheaf, requiring a reformulation of the gluing structure.

## Contribution Needed

~~Implement the finality sheaf on a small causal set (T1's 5-node graph is a natural starting point). Compute cohomology by hand or with a symbolic computation package. Identify the minimal total-order-counterexample from T1 as a candidate H¹ generator.~~

The Cech cohomology machinery is now implemented in `models/spacetime_aggregation.py`. Status: implemented.

## Result (2026-06-16)

**Formal objects added:**

- `FinalitySection`: assigns a finality score to each event within a domain, serving as the stalk data over a cover element.
- `RestrictionMap`: an explicit typed morphism between two domain sections on their shared overlap, encoding how finality assignments restrict from one domain to another.

**Cohomology machinery:**

- Cech cochains C⁰ and C¹ are defined over a finite cover of domains.
- `cech_coboundary_0` computes δ⁰: C⁰ → C¹.
- `is_cech_1_cocycle` checks whether δ¹(c) = 0 on all triple overlaps.
- `is_cech_1_coboundary` checks whether a 1-cochain equals δ⁰(f) for some global section f.
- `compute_h1_obstruction` detects nontrivial H¹ elements — cochains that are cocycles but not coboundaries.

**H¹ is now executable:** `h1_obstruction_scenario` is a canonical 3-domain example in which pairwise restriction maps are locally consistent but cannot be assembled into a global finality section. This is the first concrete topological obstruction in the TaF finite model.

**What was NOT done:** This result is confined to the finite combinatorial model. It does not define a Lorentzian metric, derive Einstein equations, handle continuous restriction maps, or establish covariance under diffeomorphisms. The connection to physical spacetime geometry remains an open problem (see `open-problems/spacetime-as-finality-colimit.md`).
