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

**Sheaf upgrade (2026-06-16):** The T16/T13 implementation adds `FinalitySection` and `RestrictionMap` as explicit formal objects, lifting overlap comparison from event-label equality to typed morphisms. Cech cohomology is now attached: H¹ obstruction detection is computable on the finite model. The canonical `h1_obstruction_scenario` demonstrates a 3-domain cover where pairwise restrictions are consistent but no global finality section exists — the first concrete topological obstruction in TaF.

The result remains intentionally weak relative to this open problem: it defines a richer gluing target but does not derive a manifold, metric, causal Lorentzian structure, or any spacetime geometry. The gap from this finite combinatorial model to the colimit construction described above is the open problem.

## Contribution Needed

Choose one entry point and make it precise. The minimum deliverable is a formal definition of the colimit/limit object and a check that it is well-defined (not just that it "should be" classical spacetime by hand-waving). The maximum deliverable is a proof that the construction reproduces a known result in GR or QFT as a limiting case.

## Status Addendum (2026-07-06): added-assumption admission gate

T464 turns the post-T223 burden into an executable admission gate:
`results/T464-s1-added-assumption-admission-gate-v0.1-results.md`; spec
`tests/T464-s1-added-assumption-admission-gate.md`; model
`models/s1_added_assumption_admission_gate.py`.

Verdict:
`S1_ADDED_ASSUMPTION_ADMISSION_GATE_BUILT_NO_S1_PROMOTION`. T223 remains the
inherited finite no-go baseline for the uniform finite finality-colimit
ensemble. More finite uniform enumeration, selected survivor positives, screen
drift, post-hoc assumptions, circular or tail-tuned measures, missing finite
audits, single-size positives, missing Lorentzian target constraints,
claim-promotion shortcuts, public-posture shortcuts, and non-GitHub external
action shortcuts are rejected or blocked.

Only a future added-assumption packet is admitted for review: it must declare a
non-uniform measure, selection rule, sprinkling law, or continuum bridge before
scoring; justify naturality through finality-native structure or a neighboring
theory; avoid tuning to the known T223 survivor tail; audit against the existing
T126/T156/T159/T223 pipeline; show multi-size persistence or a real limit
target; preserve the finite guardrail screens; and name the later Lorentzian
causal, metric, covariance, locality, or embedding constraints it must face.
This does not promote S1, reverse T223, derive spacetime, prove
manifoldlikeness, supply a dimension estimate, prove a sprinkling law, establish
a continuum theorem, or move public posture.

## Status Addendum (2026-07-07): nonuniform-measure persistence gate

T490 sharpens T464's nonuniform-measure branch:
`results/T490-s1-nonuniform-measure-persistence-gate-v0.1-results.md`; spec
`tests/T490-s1-nonuniform-measure-persistence-gate.md`; model
`models/s1_nonuniform_measure_persistence_gate.py`.

Verdict:
`S1_NONUNIFORM_MEASURE_PERSISTENCE_GATE_BUILT_SCREEN_CONDITIONING_NOT_ENOUGH`.
The T223 uniform baseline stays closed; putting mass on the known survivors is
tail tuning; normalizing over parent-interval or screen-stack passes is
guardrail conditioning, not an independent natural measure; and a single-size
positive is insufficient. Parent-conditioned survivor mass is recorded only as
a diagnostic trajectory, not as S1 evidence.

Only a future packet with a predeclared independent finality-native or
neighbor-theory generating law, fixed T126/T156/T159/T223 screens, multi-size
or limit persistence, a nonvanishing survivor-mass target, and named later
causal, metric, covariance, locality, embedding, or Lorentzian constraints is
admitted for review. This does not promote S1, reverse T223, derive spacetime,
prove manifoldlikeness, supply a dimension estimate, prove a sprinkling law,
establish a continuum theorem, move public posture, or move the claim ledger.

## Status Addendum (2026-07-07): finite-colimit closure router

T491 closes the current T223-T490 finite S1 colimit route to minor restarts:
`results/T491-post-t490-s1-finite-colimit-closure-router-v0.1-results.md`;
spec `tests/T491-post-t490-s1-finite-colimit-closure-router.md`; model
`models/post_t490_s1_finite_colimit_closure_router.py`.

Verdict:
`POST_T490_S1_FINITE_COLIMIT_ROUTE_CLOSED_NEW_EVIDENCE_ONLY`. T490 admission
is review-only and counts as no S1 evidence. Uniform finite-colimit reruns,
survivor-tail indicators, guardrail-screen conditioning, post-T223 screen
drift, single-size positives, T490-admission overreads, spacetime or Lorentzian
overclaims, claim/public-posture shortcuts, and external-action shortcuts are
rejected or blocked.

Only future packets with a predeclared independent measure law, a finite-to-
continuum bridge, or a separate formal entry point such as topos, NCG,
path-integral, or stochastic geometry are admitted for review, and only as new
evidence targets. This does not promote S1, reverse T223, derive spacetime,
prove manifoldlikeness, supply a dimension estimate, prove a sprinkling law,
establish a continuum theorem, move public posture, or move the claim ledger.

## Status Addendum (2026-07-10): reference-law gap audit

T526 turns the post-T525 blocker into a constructive calibration target:
`results/T526-s1-reference-law-gap-audit-v0.1-results.md`; spec
`tests/T526-s1-reference-law-gap-audit.md`; model
`models/t526_s1_reference_law_gap_audit.py`.

Verdict:
`s1_reference_law_calibrates_suite_but_taf_descent_missing`. The external
seeded 1+1 causal-diamond reference law passes all 32 calibrated repaired-suite
samples, while current finite finality colimits still have zero survivors.
This shows the repaired suite is passable. It does not promote S1, because the
reference law imports Lorentzian u/v coordinates and supplies no
finality-colimit descent.

The next live S1 packet should therefore not merely pass repaired
manifoldlikeness. It should predeclare a finality-native generator, measure
law, or continuum bridge; generate finite causets without u/v coordinates as
primitives; pass the repaired suite; include hostile controls; and name later
Lorentzian causal, metric, covariance, locality, or embedding constraints. The
external reference law is calibration-only, not S1 evidence.
