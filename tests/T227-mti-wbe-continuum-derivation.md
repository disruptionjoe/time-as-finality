# T227: MTI Exact WBE-Continuum Derivation Screen

## Target Claims

- MTI (`claims/MTI-metabolic-temporal-irreducibility.md`) -- the sole open
  blocker is the exact West-Brown-Enquist-Moses (WBE) continuum derivation.
- Provenance of T186 (CV proxy) and T187 (harmonic-mean proxy) beta separation.

## Known Physics Constraints

This is a physical-substrate claim, so physics is in scope, but bounded:
no GR/QFT/spacetime/curvature promotion. The only physics used is the
canonical transport-network delivery-time cost (M/M/1-style congestion delay
`delay(load) = tau / (1 - load/capacity)`, already in
`models/mti_cflow_solver.py`). The claim under test is strictly: *the branching
exponent beta carries source-ordering (metric-temporal) information beyond
causal order in WBE-Moses systems.* No new object or law is introduced.

## Verdict: conditional

The metric-vs-causal beta separation **survives one WBE-faithful continuum
optimization and is destroyed by another.** It survives the West *total-cost*
delivery objective and vanishes under the *minimax/equal-load* objective --
which is the single premise (T201) under which the T187 harmonic mean appears.
The separation is therefore **objective-dependent**, not a finite-fixture
artifact and not an unconditional continuum theorem. MTI **stays
PARTIALLY_SUPPORTED**: the continuum obstruction is now named and is a *choice
of objective*, not a missing computation.

Tag: `finite_witness` + `poly_decider` (full grid enumeration over the unit
flow simplex; a finite classifier, not a hidden search and not a hardness or
scale claim).

## What Was Derived From Sources

The prior MTI beta-separation evidence rests on two **post-hoc functional
forms**, neither derived from a WBE optimization:

- T186: `beta = 0.75 * (1 - CV(T))` (chosen efficiency proxy; see
  `models/run_t186.py`, the `efficiency = 1 - CV(T)` block).
- T187: `beta = 1 - log(HM(T))/log(n)`, harmonic mean of *free* path times.
  T200 **killed** the claim that this harmonic mean is the KKT optimum of the
  stated linear program. T201 found the harmonic mean is the optimum of *only*
  the minimax/equal-load objective `min_w max_i w_i t_i`, a premise that itself
  needs physical justification.

T227 supplies that physical optimization concretely, reusing the existing
congestion model (no new physics), and asks whether the separation is real once
the chosen functional form is replaced by an actual optimized delivery time.

## Strongest Positive Result

Re-express Alpha and Beta as three edge-disjoint delivery paths with free
times `{4,2,1}` (Alpha, slow secondary branch) and `{3,2,1}` (Beta, fast
secondary branch) -- identical causal order, identical topology, the only
difference being the metric label on the secondary branch (matches T188:
G encodes topology not timing). Minimize the **West total delivery cost**
`min_w sum_i w_i * latency_i(w)` over the unit flow simplex under the physical
congestion delay. Result (robust across grid steps 0.011 -> 0.0033):

```
total_cost(Alpha) = 2.6945     total_cost(Beta) = 2.5530   (Beta faster)
beta_TOTAL(Alpha) = 0.3841     beta_TOTAL(Beta) = 0.4176   (Beta higher)
```

via the same `beta = 1 - log(T*)/log(n=5)` scaling T187 used, now applied to
the *optimized* `T*` rather than a chosen summary. This is the **first**
metric-vs-causal beta separation produced by an actual physical optimization
rather than a hand-picked functional form. The mechanism is the one T186
predicted: at the optimum, Beta routes strictly more flow through its faster
secondary branch (p1 flow 0.162 vs Alpha 0.089), so the metric label enters
the objective. The sign matches both proxies (CV and HM put Beta above Alpha).

## First Exact Obstruction / Missing Object

Under the **minimax/equal-load** objective `min_w max_i latency_i(w)` -- the
*only* objective (T201) whose optimum is the inverse-time / harmonic-mean
allocation that T187 leaned on -- the separation **disappears**:

```
minimax(Alpha) = 2.9718        minimax(Beta) = 2.9718      (IDENTICAL)
optimal flows  = (0.000, 0.327, 0.663) for BOTH systems
```

The optimizer puts **zero flow on the slow secondary branch** (p1) in both
systems and equalizes the two fast paths (p2, p3). The metric difference
between Alpha and Beta lives entirely on the abandoned p1 branch, so the
binding (equalized) latency is **metric-blind** to it. Consequently the T187
harmonic mean is *not* the value of the minimax optimum -- it is the harmonic
mean of all free times *including the branch the equal-load optimization
discards*. The exact obstruction is therefore:

> **The continuum WBE derivation does not by itself fix a unique objective.
> The beta separation is a property of the West total-cost objective and is
> annihilated by the minimax/equal-load objective. The "exact WBE continuum
> derivation" cannot be completed until a domain-native principle SELECTS one
> objective over the other -- and the harmonic-mean objective that previously
> carried the MTI proxy is exactly the one that kills the separation.**

This also closes a latent inconsistency: T201 endorsed the equal-load premise
as the harmonic mean's only honest home, but that same premise is metric-blind
on these fixtures. The proxies separated Alpha/Beta only because they read the
full free-time multiset, not the optimized delivery time.

## Constructive Next Object

A single declared object resolves the conditional: a **WBE objective-selection
principle** with two acceptance gates:
1. it must reproduce the West-Brown-Enquist 3/4 calibration in the
   uniform/space-filling continuum limit (so it is genuinely WBE, not chosen
   for convenience), AND
2. its optimum must place nonzero flow on every delivery branch (so the metric
   label cannot be optimized away).

The total-cost objective satisfies gate (2) on these fixtures; the open task is
gate (1): derive (or cite) the continuum limit in which West total dissipation
minimization yields the 3/4 exponent *and* show its optimum keeps all branches
loaded. If such a principle exists and selects total-cost, MTI promotes. If the
domain-native WBE principle is the equal-load/minimax form, MTI's metric-temporal
content is **demoted to a chosen-objective artifact** on these fixtures and the
separation must be re-sought in a regime where the slow branch is mandatory
(e.g. a hard service/coverage constraint forcing nonzero flow on every leaf).

## Meaning For The Claim

- MTI stays **PARTIALLY_SUPPORTED**. The continuum derivation is **not** an open
  *computation* (T227 ran it); it is an open *selection*: which WBE objective is
  canonical. This is a sharper, smaller blocker than "exact WBE continuum
  derivation" stated abstractly.
- The metric-vs-causal separation is **real and physically optimized** under
  the West total-cost objective (upgrades the evidence from proxy-only to one
  genuine optimization), but **not objective-invariant**, so no promotion past
  partially_supported is earned.
- No physics/geometry promotion: the result is a finite typed-machinery audit
  of a congestion-flow optimization. The COMPLEXITY-LEDGER tags `finite_witness`
  and `poly_decider` bound it; no hardness, scale, or continuum theorem is
  claimed from this finite witness.
- Absorber named: the **minimax/equal-load convex optimization** (T201) absorbs
  and nullifies the separation; the **West total-cost convex optimization**
  preserves it. The residue that survives both is *nothing yet* -- which is
  precisely why the verdict is conditional rather than closed.

## Failure / Falsification Conditions

- **Promote MTI** only if a WBE-native principle selects a branch-loading
  objective (passes both gates above) AND the beta separation survives its
  optimum in the continuum (uniform-density) limit.
- **Demote MTI's metric-temporal content** if the domain-native WBE objective
  is shown to be the equal-load/minimax form (or any objective whose optimum
  abandons the differentiating branch), since then beta is determined by the
  retained (fast) paths alone and carries no information beyond what causal
  order plus retained-path topology already fix.
- **Invalidate T227** if a coding error makes total-cost and minimax agree, or
  if a finer grid flips either direction. (Checked: directions are stable
  across steps 0.02 -> 0.0033; see `tests/test_mti_wbe_continuum.py`.)

## Artifacts

- `models/mti_wbe_continuum.py` -- WBE-faithful screen: total-cost, minimax,
  and mean-free objectives on the Alpha/Beta congestion networks; beta read-outs
  for both proxies and both optimizations.
- `tests/test_mti_wbe_continuum.py` -- five real checks (not placeholders):
  proxies agree direction; total-cost preserves separation; total-cost loads
  the secondary branch (Beta > Alpha); minimax destroys separation (zero flow
  on slow branch, identical optimum); separation is objective-dependent.
- Reuses `models/mti_cflow_solver.py` congestion model and minimax solver.

## Next Proof / Computation Step

1. State the West-Brown-Enquist continuum dissipation functional explicitly
   (impedance-weighted flow over a space-filling branching tree) and take its
   uniform-density limit; verify the optimum recovers the 3/4 calibration.
2. Check, in that limit, whether the optimal flow keeps every terminal branch
   loaded (gate 2). If yes, total-cost is the canonical objective and the
   separation promotes; if the limit equalizes loads and abandons slow branches,
   MTI's metric content demotes on the current fixtures.
3. If demoted on these fixtures, re-pose the separation under a hard service /
   coverage constraint (mandatory nonzero flow on every leaf) and re-run the
   minimax screen there; this is the regime where equal-load and metric content
   can coexist.

## Registered Status

T227 RUN as of 2026-06-24. Implementation and checks committed under the
worker's slug namespace (`models/mti_wbe_continuum.py`,
`tests/test_mti_wbe_continuum.py`). Does not edit S1, sheaf-H1, kappa, functor,
or colimit files.
