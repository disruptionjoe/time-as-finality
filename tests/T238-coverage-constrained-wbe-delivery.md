# T238: Coverage-constrained WBE-native delivery model — is the metric-temporal separation objective-INVARIANT?

## Verdict: conditional

The metric-vs-causal beta separation is **objective-INVARIANT** under a
**defensibly WBE-native** delivery constraint: *every terminal must be reachable
within a finite delivery-time bound D*. Under that physical constraint the
separation holds for **both** the total-cost objective **and** the
minimax/equal-load objective, **across the entire feasible D-window**, with the
operative floor **derived from the network (not hand-picked)**. This resolves
T233 sub-object (2) in the **positive direction**: the metric-temporal content
MTI carries is **no longer objective-dependent** — it is not a total-cost
artifact, because the very objective (minimax) that annihilated it in T227 now
preserves it once the network is required to actually service every leaf it
fills.

This is `conditional`, **not** `closed`, for two explicitly named reasons:
1. **Honesty guard (the binding hypothesis):** the WBE-nativeness rests on
   reading the WBE network as a *space-filling **service** hierarchy* whose
   reason to exist is perfusing every terminal — so "no un-perfused leaf" is a
   definitional constraint, not a tuned floor. That reading is defensible and
   argued independently of the separation, but it is an interpretive premise,
   not a theorem. If a reviewer rejects "every terminal must be reached" as
   WBE-native, the result demotes per T233's falsification clause.
2. **It does NOT promote MTI alone.** This lane closes only the *delivery-
   objective* half of the T233 split. The **other** named sub-object — a
   domain-native justification for the area-preserving `n^{-1/2}` condition that
   singles out the 3/4 exponent — **stays open**. MTI promotes past
   PARTIALLY_SUPPORTED only when **both** halves hold.

Recommendation to integrator: move MTI's metric-temporal content from
*objective-dependent* (T227/T233 horn) to **objective-invariant under a
WBE-native delivery constraint**, i.e. a partial -> stronger-partial move; do
**not** promote MTI itself (3/4 sub-object still open). Ratification is the
integrator's, not this lane's.

Tags: `finite_witness` (finite Alpha/Beta fixtures + finite D-sweep; NO
continuum theorem) + `poly_decider` (finite floored-simplex grid scan +
closed-form bound->ceiling map; NO hidden search, NO hardness/scale claim).

## What Was Derived From Sources (IMPORT ONLY)

- From **T227** (`models/mti_wbe_continuum.py`): the `alpha_network` /
  `beta_network` fixtures (three edge-disjoint delivery terminals, free times
  `{4,2,1}` vs `{3,2,1}`, the only difference the metric label on the slow
  terminal), `solve_total_cost`, and the M/M/1 delay `tau/(1 - load/cap)`.
  Imported verbatim; no fixture re-tuned, no new physics.
- From **T233** (`models/wbe_objective_selection.py`):
  `check_coverage_constrained_minimax` (the bare-NUMERIC-floor baseline) and
  `total_dissipation_of_flow` (= the West total-cost objective). Imported to
  *link* the derived floor to T233's Part C and to reuse the total-cost
  functional; **not** modified.
- From **T233's split**: this lane attacks sub-object (2) only. T233 showed a
  hard numeric floor makes even minimax separate; the open question it flagged
  is whether that floor is WBE-native or a convenience floor. T238 answers it.

The only physics used is the canonical M/M/1 congestion delay already in
`models/mti_cflow_solver.py`. No Poiseuille re-derivation, no exponent claim, no
GR/QFT/spacetime/curvature/new-law language.

## Strongest Positive Result

**A delivery constraint stated as physics — not a number — under which the
separation is objective-invariant, with a decisive falsification control.**

The constraint: a terminal is *reachable within D* iff it carries positive
served flow (a zero-flow leaf has delivery time `+inf` — the physical reading of
an un-perfused leaf / SLA violation) **and** its congested delivery time is
`<= D`. Required of **every** terminal. The operative floor is therefore the
prohibition of un-perfused leaves, with magnitude derived from the network
(`q = demand / K^2`, network-fixed), and the bound `D` anchored to the
network-fixed feasibility threshold `D_min = max free time`.

Under this constraint (run captured in `results/wbe-coverage/T238-run.txt`):

```
   D  feas    TC_a    TC_b TCsep    MM_a    MM_b MMsep
 4.50 True  2.6986  2.5533  True  4.4944  3.3708  True
 5.00 True  2.6986  2.5533  True  4.4944  3.3708  True
 6.00 True  2.6986  2.5533  True  4.4944  3.3708  True
 8.00 True  2.6986  2.5533  True  4.4944  3.3708  True
12.00 True  2.6986  2.5533  True  4.4944  3.3708  True
OBJECTIVE-INVARIANT = True
```

Minimax — the objective that **annihilated** the separation in T227 (zero flow
on the slow branch, identical optimum 2.9718) — now **separates** Alpha 4.4944
vs Beta 3.3708, because the terminal-reachability constraint forbids it from
zeroing the slow terminal. The metric label re-enters the binding latency.

**Mechanism (exact):** the unconstrained minimax dropped the slow terminal from
the binding set (`max_loaded_path_latency` takes the max only over *loaded*
paths), making the metric label invisible. Requiring the slow terminal to be
*reached* re-admits it; at its served flow its congested delivery time tracks
its free time `tau_p1` (4 for Alpha, 3 for Beta), which is exactly the metric
label — so the binding minimax value separates. This is the same mechanism
under both objectives, hence objective-invariant.

**Robustness / honesty checks (all green, 13/13):**
- *Quantum-magnitude robustness*: the verdict survives shrinking the derived
  quantum via `service_fraction` 1.0 -> 0.05 (q 0.11 -> 0.0055). The floor is
  not doing the work by being large — only the terminal being *reached at all*
  matters.
- *The bound does real physical work*: at `D` near `D_min` the delivery-time
  bound, on its own, forbids dumping all demand on the fast terminal
  (`bound_makes_coverage_binding = True`), and below `D_min` the slow terminal
  is genuinely **unreachable** (`feasible = False`) — the constraint reports
  infeasibility rather than fabricating a number. A real physical bound, not a
  fiat floor.
- *Falsification control (decisive)*: when the slow terminal's metric label is
  made **identical** across both systems, the separation **vanishes**
  (`va = vb`); restoring a metric difference restores it. The constraint
  *reveals* the metric label; it does not manufacture a separation.

## First Exact Obstruction / Missing Object

The result is positive, so the obstruction is the **named boundary of the
conditional**, not a failure inside it:

> **The WBE-nativeness is an interpretive premise, not a theorem.** "A WBE
> network must perfuse every terminal it space-fills" is a defensible reading of
> the West-Brown-Enquist *service hierarchy*, argued here independently of the
> separation. But the repo contains no formal object asserting it as a WBE
> *axiom*. A hostile reviewer who insists the WBE optimization is unconstrained
> dissipation minimization with **optional** coverage can still route to the
> T227 minimax horn and demote. The missing object is a **WBE-axiomatic
> coverage statement** — a citation or derivation that terminal-reachability
> (every leaf perfused within a finite delivery bound) is a *constitutive*
> constraint of the WBE model, not an add-on.

Equivalently: this lane shows the separation is invariant under the coverage
constraint **and** that the constraint does real, falsifiable physical work and
is not a renamed numeric floor — which is everything short of elevating
"every terminal reachable" to a cited WBE axiom.

## Constructive Next Object

A **WBE-coverage axiom certificate**: locate (in WBE/Banavar-Maritan-Rinaldo
directed-transport-network literature, already cited in the repo's MTI line) the
statement that the space-filling network is a *service* network delivering to
every terminal within a bounded transit time, and encode it as the constraint
this module already implements — turning the interpretive premise into a cited
axiom. With that citation in hand, the `conditional` on this half upgrades to
`closed`, leaving only the area-preserving / 3/4 sub-object between MTI and
promotion.

(Independent, NOT in this lane: the area-preserving `n^{-1/2}` justification —
T233 sub-object (1). MTI promotes only when both land.)

## Meaning For The Claim

- **MTI's metric-temporal content is objective-INVARIANT** under a WBE-native
  delivery constraint. The T227/T233 horn ("the separation is a total-cost
  artifact; minimax kills it") is **closed on the delivery-objective axis**:
  minimax preserves the separation once the network must service every leaf.
  This is strictly stronger than T233 left it (T233 had only a hand-set numeric
  floor; T238 derives the floor from a physical bound and proves invariance
  across the feasible window with a falsification control).
- **MTI stays PARTIALLY_SUPPORTED** — this lane does **not** promote it. The
  area-preserving / 3/4 calibration sub-object (T233 sub-object 1) is untouched
  and remains the second, independent blocker.
- **Absorbers named.** The unconstrained minimax/equal-load convex optimization
  (T201/T227) still absorbs the *unconstrained* separation; the West total-cost
  optimization preserves it; and the **coverage-constrained** problem is
  preserved by **both** — so the residue that survives every objective is now
  *the separation itself*, which is exactly why this half moves from horn to
  invariant. No new mature neighbor owns the coverage-constrained residue: the
  service constraint is the WBE model's own, not an imported scheduling add-on.
- **No physics promotion.** A finite typed audit of a congestion-flow
  optimization under a delivery-time constraint. All quantities (`4.4944`,
  `3.3708`, the `D_min = 4.0` threshold, `q = 0.11`) are finite computed values
  of a specific finite fixture; no continuum theorem, hardness, scale claim, or
  new law (`finite_witness` + `poly_decider`).

## Known Physics Constraints

Physics in scope but bounded: only the canonical M/M/1 congestion delay
`delay(load) = tau/(1 - load/capacity)` already in the repo, plus the
closed-form delivery-bound -> flow-ceiling map `w_max = c*(1 - tau/D)` that is
an algebraic inversion of that same delay (no new physics). The
terminal-reachability constraint is the West-Brown-Enquist *service-hierarchy*
reading, stated physically (every terminal perfused within a finite delivery
bound), not promoted to a universal law. No GR/QFT/spacetime/curvature/gravity
language; no exponent claim is made in this lane (the 3/4 sub-object is
explicitly out of scope here).

## Failure / Falsification Conditions

- **Demote this result to T233's horn** if "every terminal must be reached
  within a delivery bound" is rejected as WBE-native — i.e. if the WBE
  optimization is held to be unconstrained dissipation minimization with
  optional coverage. Then the separation reverts to a total-cost artifact and
  MTI's metric content demotes per T233's falsification clause.
- **Invalidate T238** if (a) the slow-branch flow under quantum=0 fails to track
  the grid step toward zero while separation persists — it does track the step
  (0.01->0.005->0.0025), confirming the separation is carried by the
  reached-terminal's free-time label, not a forced epsilon-load artifact; (b)
  the identical-metric-label control separates (it does NOT: `va = vb`); (c) a
  finer grid flips the Beta < Alpha direction (stable across steps 0.01,
  0.005, 0.0025); or (d) the constraint reports feasible below `D_min` (it
  reports infeasible for `D < 4.0`).
- **Promote MTI** (separate, integrator-only) only when BOTH this delivery-
  invariance result AND the area-preserving 3/4 sub-object hold under
  domain-native inputs.

## Artifacts

- `models/wbe_coverage_constrained.py` — the physical terminal-reachability
  constraint (`congested_delivery_time` with `+inf` for un-perfused leaves,
  `terminal_reachable`, `all_terminals_reachable`), the network-fixed
  floor/bound derivation (`coverage_quantum`, `min_flow_for_delivery_bound`,
  `feasible_bound`), the coverage-constrained optimum under both objectives
  (`coverage_constrained_delivery`, `_solve_coverage_constrained`), the
  objective-invariance verdict over the feasible D-window
  (`decide_objective_invariance`), and the derived-vs-convenience floor
  provenance check (`floor_provenance`). Imports T227/T233 models verbatim;
  touches NO kappa / sheaf-h1 / attribution / d1cat files.
- `tests/test_wbe_coverage_constrained.py` — 13 real checks (green): un-perfused
  terminal has +inf delivery; reachability needs positive flow AND bound;
  feasibility threshold + quantum are network-fixed; bound caps fast-branch
  flow; separation under total-cost AND minimax with the physical constraint;
  objective-invariance across the feasible window; verdict robust to shrinking
  quantum; bound makes coverage binding; infeasible below threshold;
  falsification control (identical metric label -> no separation); constrained
  minimax keeps the slow branch where unconstrained drops it.
- `results/wbe-coverage/T238-run.txt` — recorded run.

## Next Proof / Computation Step

1. Obtain the **WBE-coverage axiom certificate**: a citation/derivation that
   terminal-reachability within a bounded transit time is constitutive of the
   WBE service network (not optional). This upgrades the delivery half from
   `conditional` to `closed`.
2. Independently (T233 sub-object 1, other lane): the area-preserving `n^{-1/2}`
   / 3/4 justification.
3. MTI promotes past PARTIALLY_SUPPORTED only when BOTH (1) and (2) hold under
   domain-native inputs; this lane delivers the delivery-objective half.

## Registered Status

T238 RUN as of 2026-06-25. Implementation, results, and 13 green checks under
the worker's slug namespace (`models/wbe_coverage_constrained.py`,
`tests/test_wbe_coverage_constrained.py`,
`results/wbe-coverage/T238-run.txt`). Imports T227/T233 models verbatim; does
NOT edit kappa, sheaf-H1, attribution, functor, or d1cat-colimit files; does
NOT edit CLAIM-LEDGER.md, ROADMAP.md, or TESTS.md.
