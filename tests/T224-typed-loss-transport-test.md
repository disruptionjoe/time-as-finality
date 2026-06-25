# T224: Typed-Loss Transport Test (kappa cross-domain prediction) -- THE breakout kill-switch

## Verdict: conditional

The kill-switch fired and **did not kill** the central bet. kappa, defined ONCE
domain-neutrally, transported from domain A (T39 CSP-PO1 signed-graph frustration)
to an a-priori-unrelated repo domain B (T21 Bell/CHSH contextuality H1) and
**correctly predicted B's native obstruction value before B was measured**, with
**no shared derivation**. The prediction did not miss, and kappa did not have to
be re-tuned per domain -- so the "recurrence is a projected template" deflation
verdict is **not** confirmed this cycle.

But the PASS is **conditional**, not promotable, for two structural reasons stated
up front (both are honest limits, not hedges):

1. **One absorber, not two.** The open problem's bar for the full cross-domain
   classification theorem is a passing prediction on **>= 2** unrelated absorbers.
   This cycle cleared exactly one (T21). Two-absorber confirmation remains.
2. **Only the rank-{0,1} fragment of kappa was load-bearing.** The CHSH cover has
   a single independent cycle, so the cross-domain step exercised only kappa in
   {0, 1} (obstruction present / absent). A genuine cross-domain **rank**
   classification (kappa = 2 predicting two independent native obstructions in B)
   was not testable against T21 and is not yet earned.

So: the bet survives the kill-switch and is **conditionally** alive, pending a
second absorber and a rank >= 2 discriminator. This is non-vacuous in both
directions -- it converts "rigor equals deflation" into a falsifiable experiment
that this cycle passed at the entry gate.

## What was derived from the sources

- **open-problems/typed-loss-transport-test.md** supplied the protocol (compute
  kappa_A, build a structure-preserving A->B map with no shared derivation,
  predict B before measuring, measure B, compare) and the falsifiers (kappa needs
  a per-domain choice -> demote; every A->B map fails to preserve neighbor-visible
  structure or trivially shares a derivation -> demote).
- **T220** supplied the *definition* of kappa: the canonical witness obligation
  factors as `obligation = psi . nu` through the neighbor-visible map nu, and the
  T220-canonical quantity is the content unrecoverable from nu -- the set of global
  sections nu cannot distinguish. kappa is exactly the rank of that set.
- **T39** supplied domain A: the binary {-1,+1} same/different signed-graph CSP,
  globally satisfiable iff the signed graph has no frustrated (negative-product)
  cycle, with the minimum-direct (2-cycle), minimum-transitive (T26 odd 3-cycle),
  tree, and all-same witnesses.

## kappa: defined ONCE, domain-neutrally (not re-specifiable per domain)

For any system whose neighbor-visible data nu is a binary {-1,+1} same/different
cover (the package every signed-graph / sheaf-H1 / CAP absorber reads; +1 =
"same", -1 = "different"), define

```text
kappa(nu) = dim_{Z/2} H^1(signed graph of nu)
          = rank of the Z/2 cycle space whose sign-product is -1
          = number of independent frustrated parity cycles
          = (non-forest edges that disagree with a consistent spanning-forest
             potential phi : V -> Z/2).
```

This is the rank of the set of global sections nu cannot distinguish: a global
section is a Z/2-coloring consistent with every signed edge; kappa = 0 iff the
cover glues (a section exists, nu fixes it up to one free bit per component);
kappa = k >= 1 iff there are k independent frustrated cycles, no global section
exists, and nu cannot pick any. It is computed by ONE function
(`compute_kappa(variables, signed_edges)`, union-find spanning forest + BFS
potential) -- a `poly_decider`, not a search. A domain that needed a different
formula to make the prediction land would be a per-domain re-tuning (a FAIL); none
did.

## Strongest positive result

kappa transported A->B and predicted B exactly, across the full witness panel,
with the prediction made before B was measured natively:

| domain-A instance (T39) | kappa_A | predicted kappa_B | native B rank (T21 parity witness) | nu-side kappa_B | match |
|---|---|---|---|---|---|
| min_transitive_conflict (odd 3-cycle) | 1 | 1 | 1 (parity_product = -1) | 1 | yes |
| min_direct_conflict (2-cycle) | 1 | 1 | 1 (parity_product = -1) | 1 | yes |
| satisfiable_all_same | 0 | 0 | 0 (parity_product = +1) | 0 | yes |
| tree_structured | 0 | 0 | 0 (parity_product = +1) | 0 | yes |

The transport map is explicit: it is the identity on the signed-graph isomorphism
type of the neighbor-visible cover. A's odd 3-cycle (a CSP gluing conflict) and
B's odd 4-cycle (a quantum contextuality witness) present the *same*
neighbor-visible invariant -- one independent frustrated cycle -- though their
domain semantics share no derivation. The control sends balanced A-covers to a
balanced CHSH cover (all parities +1) and predicts rank 0; it does.

**Honesty guard that makes this non-vacuous (the load-bearing finding):** the map
crosses a real no-shared-derivation boundary. `shared_derivation_audit()`
(executed in code, by source inspection) confirms:

- T21 `bell_contextuality_finality.py` does **not** import `d1_restriction_system`
  -- it is built on its own data types (`MeasurementContext`, parity products). So
  A->T21 preserves only nu, with no shared engine.
- T28 `cap_theorem_bridge.py` **is** literally constructed from
  `d1_restriction_system`, the *same* engine as T39. An A->T28 "transport" would
  trivially share a derivation -- the open problem's explicit demote condition.

So B = T21 is the correct unrelated absorber and T28/CAP is correctly
disqualified. The recurrence here is **not** notational: a structure-preserving
map across genuinely independent code predicted the obstruction.

## First exact obstruction / missing object

The first obstruction to promoting this from `conditional` to a theorem is that
**kappa's rank information above 1 was never the discriminator in the cross-domain
step.** T21's CHSH cover has cycle-space rank exactly 1 (4 settings, 4 contexts ->
|E| - |V| + 1 = 1), so no native B obstruction of rank 2 exists to test the
prediction kappa = 2 against. The cross-domain claim earned is therefore
*obstruction-presence* classification (kappa = 0 vs kappa >= 1), not *rank*
classification (which integer kappa). A pure binary obstructed/not classifier
would clear the four trials above; what kappa adds beyond that -- the integer rank
-- is not yet load-bearing across domains.

The second obstruction is the absorber count: one (T21), the open problem needs
two.

## Constructive next object (named, not built here)

The missing object is a **rank >= 2 unrelated absorber B'**: a domain, with no
shared derivation with T39, whose neighbor-visible cover has cycle-space rank 2
and carries two independent native obstructions, so that kappa = 2 transported
from a two-odd-cycle A-instance can predict *both*. Candidate already in the repo:
two independent CHSH boxes (8 settings, parity product per box), or a
contextuality scenario with two disjoint frustrated cells. A->B' passing would
upgrade the cross-domain claim from presence to rank and, together with T21, clear
the two-absorber bar -- at which point the verdict moves `conditional -> closed`
and a cross-domain classification theorem living in no single absorber (the
independent motivation the 2026-06-24 paper audit found NOT EARNED) would be the
honest claim.

## Meaning for the relevant claim

- This does **not** kill the breakout bet (heterodox/orthodox 62-persona pass): the
  prediction held with no shared derivation, so "the cross-domain recurrence is a
  projected template" is **not** the verdict this cycle. The bet is conditionally
  alive.
- It does **not** promote anything. No physics/geometry/curvature/new-object
  language is used; kappa is a Z/2 graph-homology rank over a finite cover. The
  only claim made is a finite cross-domain *obstruction-presence* classification,
  explicitly held below the theorem bar by the two stated conditions.
- It strengthens T220: T220's `psi . nu` content is shown to be the *same*
  invariant in a second, unrelated absorber -- the first evidence that the
  neighbor-visible map is transportable, not domain-local bookkeeping.
- The kill-switch's own promotion gate (prediction passing on >= 2 unrelated
  absorbers) remains **not cleared**.

## Next proof / computation step

Build A->B' to a rank-2 unrelated absorber (two-box CHSH or a two-cell
contextuality scenario), predict kappa = 2 before measuring, and measure both
native obstructions. If the prediction holds with no shared derivation, the
two-absorber + rank conditions both clear and T224 moves to `closed` with a
cross-domain classification theorem. If kappa = 2 mispredicts (e.g. B' carries
only one native obstruction, or needs a re-tuned formula), the breakout is killed
cleanly and the deflation verdict stands.

## Complexity / language tags

- `finite_witness`: all instances are finite executable fixtures (T39 covers,
  T21 four-context CHSH); no scalable theorem is asserted from them.
- `poly_decider`: kappa is computed by union-find spanning forest + BFS Z/2
  potential -- a finite classifier, not a hidden search and not an NP-hardness
  claim.
- No Cech/sheaf-cohomology *general* theorem is promoted from these finite
  witnesses; "dim H^1" here is the finite Z/2 cycle-space rank of a specific
  finite cover, named as such.

## Known Physics Constraints

None. T224 is a finite typed-machinery audit. The Bell/CHSH side is used only as a
structural contextuality cover (parity equations), as in T21 -- not a quantum
amplitude simulation. No time, observer-metaphysics, curvature, or new-object
language is used.

## Reproduction

```bash
python -m unittest tests.test_typed_loss_transport -v
python -m models.typed_loss_transport   # prints the full protocol JSON
# raw output: results/typed-loss-transport/T224-results.json
```
