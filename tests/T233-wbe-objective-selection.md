# T233: WBE Objective-Selection Principle — the sharp MTI continuum blocker

## Verdict: conditional

The WBE objective-selection principle T227 named has **two acceptance gates**,
and the natural domain-native principle — *minimize total network dissipation*
— **passes Gate 2 but fails Gate 1**, so it does NOT promote MTI on its own.
Concretely (executable, robust across n and grid):

- **Gate 1 (recover the 3/4 calibration) FAILS for dissipation minimization.**
  The constrained Poiseuille-impedance optimum (minimize impedance at fixed
  tube volume) is the **area-INCREASING** radius ratio `beta_r = n^{-1/3}`,
  which yields metabolic exponent **a = 1**, not 3/4. The area-PRESERVING
  ratio `n^{-1/2}` that gives exactly 3/4 is strictly *fatter* than the
  dissipation optimum and is **not selected by dissipation minimization**.
  3/4 requires the area-preserving impedance-matching condition as a
  **separate physical input** (the large-vessel/pulsatile regime), not as an
  output of the optimization.

- **Gate 2 (load every branch) PASSES for the objective dissipation min
  induces.** Total network dissipation = `sum_i flow_i * latency_i` = the West
  **total-cost** objective, whose optimum loads every branch on both Alpha and
  Beta, so the metric label survives and the T227 separation survives.

So the two gates are each satisfiable, but **not jointly by the dissipation
principle**: the principle that picks the branch-loading objective is exactly
the principle that fails the 3/4 calibration. MTI **stays
PARTIALLY_SUPPORTED**. The verdict is *conditional* (not *fail*) because a named
conditional regime — a hard coverage/service floor — makes even the minimax
objective separate and load every branch, which is the constructive next step.

Tags: `finite_witness` (the dissipation optimum and separation are checked on a
finite branching tree and the finite Alpha/Beta fixtures; no continuum theorem
is asserted) + `poly_decider` (bounded grid scans / closed-form exponent
algebra; NO hidden search, NO hardness or scale claim).

## What Was Derived From Sources

- From **T227** (`tests/T227-mti-wbe-continuum-derivation.md`,
  `models/mti_wbe_continuum.py`): the blocker is a *selection*, not a
  computation. Total-cost preserves the beta separation (loads the slow branch,
  Beta p1 flow 0.16 vs Alpha 0.09); minimax/equal-load annihilates it (zero
  flow on the slow branch, identical optimum 2.9718). Reused the Alpha/Beta
  fixtures (`alpha_network`, `beta_network`) and the `solve_total_cost` /
  `solve_minimax` screens verbatim — no new physics, no re-tuned fixtures.
- From the **MTI claim** (`claims/MTI-metabolic-temporal-irreducibility.md`):
  the sole open promotion blocker is "exact WBE continuum derivation from first
  principles"; T196 already `killed` the imported continuum bridge for lack of
  a *derived* scaling family. T233 supplies the missing derivation step and
  reports its honest outcome.
- The only physics used: canonical Poiseuille tube impedance
  `Z = 8 mu l / (pi r^4)` and tube volume `V = pi r^2 l` over a self-similar
  space-filling tree (`gamma = n^{-1/3}`), plus the M/M/1 congestion delay
  already in `models/mti_cflow_solver.py`. No GR/QFT/spacetime/curvature, no
  new law.

## Strongest Positive Result

**An explicit, executable WBE dissipation functional whose optimum is computed,
not asserted — and the clean negative result it produces.** Minimizing the
constrained dissipation `J = Z * V^2` (impedance at fixed material budget) over
the radius ratio, at the space-filling length ratio `gamma = n^{-1/3}`,
recovers the area-increasing ratio `n^{-1/3}` to grid precision for every
tested `n`:

```
n      dissip-argmin beta_r   area-incr n^-1/3   area-pres n^-1/2   a@dissip-opt
4          0.6299                0.6300             0.5000             0.9999
8          0.5000                0.5000             0.3536             1.0000
16         0.3968                0.3969             0.2500             1.0000
27         0.3333                0.3333             0.1925             0.9999
```

The closed-form check confirms the area-preserving ratios `(n^{-1/2}, n^{-1/3})`
give **exactly** `a = 3/4` for every `n` — so 3/4 is real and the algebra is
right; it is just **not the dissipation minimum**. This is the first *derived*
(not imported) statement in the repo of *which* WBE regime the dissipation
principle actually selects, closing the T196 "no scaling family, imported not
derived" gap for the selection question with a definite answer.

On the delivery side (Gate 2), the dissipation-induced **total-cost** objective
loads every branch on both systems and the beta separation survives it
(`separation_survives_selected = True`); the rival minimax objective zeroes the
slow branch on both (reproducing T227 exactly).

## First Exact Obstruction / Missing Object

> **The WBE dissipation-minimization principle does not pass both gates.** It
> induces the branch-loading (total-cost) delivery objective (Gate 2 PASS) but
> its space-filling optimum is the area-increasing regime with metabolic
> exponent `a = 1`, **not** the area-preserving `a = 3/4` (Gate 1 FAIL). The
> 3/4 exponent is recovered **only** by *adding* the area-preserving
> impedance-matching condition, which is a separate physical assumption (the
> large-vessel pulsatile regime), not a consequence of dissipation
> minimization. Pure dissipation minimization at fixed volume selects the
> small-vessel/diffusive regime.

Equivalently: bare impedance is monotone-decreasing in radius (verified —
fatter is always less dissipative, no interior optimum), so the *only* thing
that fixes the branching exponent is the trade-off term, and at fixed volume
that trade-off lands on `n^{-1/3}` (a=1), never on `n^{-1/2}` (a=3/4). The
missing object is therefore a **domain-native justification for the
area-preserving condition** — an impedance-matching / minimal-reflection
principle for pulsatile flow — that (a) singles out `n^{-1/2}` and (b) is shown
to *also* induce a branch-loading delivery objective. Until that object exists,
the WBE 3/4 regime and the branch-loading delivery objective are selected by
*two different* principles, and MTI cannot ride a single one to promotion.

## Constructive Next Object

The conditional escape T227 named, now demonstrated executable: **re-pose the
separation under a hard coverage/service constraint** (mandatory nonzero flow on
every leaf) and re-run the equal-load/minimax screen there. With a floor on
every branch the minimax objective can no longer discard the slow branch, so
the metric label enters the binding latency and the separation **re-appears
even under minimax**:

```
floor   minimax(Alpha)   minimax(Beta)   separates   all_loaded
0.05       4.2105           3.1579          yes          yes
0.10       4.4444           3.3333          yes          yes
0.20       5.0000           3.7500          yes          yes
```

This is the regime where **equal-load fairness and metric-temporal content
coexist**: the separation is no longer an artifact of choosing total-cost over
minimax, because *both* objectives separate once a coverage floor is imposed.
The next object to build is therefore the **coverage-constrained WBE delivery
model**: state the service/coverage requirement physically (every terminal
must be reachable within a delivery-time bound — the genuine biological/
distributed-system constraint WBE networks satisfy), and show it is the
domain-native constraint, not a convenience floor. If that constraint is
WBE-native, the metric-temporal separation is objective-INVARIANT under it and
MTI promotes; the 3/4 calibration then attaches via the (separately justified)
area-preserving condition rather than via the delivery-objective selection.

## Meaning For The Claim

- **MTI stays PARTIALLY_SUPPORTED.** The continuum blocker is now sharper than
  T227 left it: it is not "which delivery objective is canonical" (the
  dissipation principle answers that — total-cost), it is "the principle that
  selects the branch-loading objective is *not* the principle that fixes the
  3/4 exponent." The 3/4 law and the metric-temporal delivery separation are
  carried by **different** WBE inputs (area-preserving geometry vs.
  total-dissipation flow allocation).
- The metric-vs-causal separation is **real and survives the dissipation-
  selected (total-cost) objective**, and additionally survives minimax once a
  coverage floor is imposed — so the separation is *more* robust than T227
  showed (it is not solely a total-cost artifact). But promotion still requires
  a single domain-native principle clearing BOTH gates, which dissipation
  minimization does not.
- **Absorbers named.** The minimax/equal-load convex optimization (T201) still
  absorbs the unconstrained separation; the West total-cost / dissipation
  objective preserves it; and the *coverage-constrained* minimax neither
  absorbs nor is absorbed — it is the residue that survives both objectives,
  which is exactly why the verdict is conditional rather than fail.
- **No physics promotion.** This is a finite typed-machinery audit of a
  congestion-flow optimization and a self-similar impedance tree. `a = 1`,
  `a = 3/4`, and the area-(in)creasing ratios are finite computed quantities of
  a specific finite tree; no continuum theorem, hardness, scale claim, or new
  law is asserted (`finite_witness` + `poly_decider`).

## Known Physics Constraints

Physics is in scope but bounded: only canonical Poiseuille impedance
`Z = 8 mu l / (pi r^4)`, tube volume `V = pi r^2 l`, the space-filling length
ratio `gamma = n^{-1/3}`, and the M/M/1 congestion delay
`delay(load) = tau / (1 - load/capacity)` already in the repo. The 3/4 exponent
is a *computed* property of the WBE optimal ratios, not promoted to a universal
law; it is shown NOT to follow from dissipation minimization alone. No
GR/QFT/spacetime/curvature/gravity language; "exponent" = a finite log-ratio of
geometric growth rates of a specific finite tree.

## Failure / Falsification Conditions

- **Promote MTI** only if a single WBE-native principle (i) recovers 3/4 in the
  space-filling limit AND (ii) induces a delivery objective whose optimum loads
  every branch — *or* if the coverage/service constraint of Part C is shown to
  be WBE-native, making the separation objective-invariant under it.
- **Demote MTI's metric-temporal content** if the coverage constraint is shown
  to be a convenience floor with no domain justification, since then the
  separation reduces to a choice of total-cost over minimax on the unconstrained
  fixtures (the T227 horn).
- **Invalidate T233** if a coding error makes the dissipation optimum land on
  `n^{-1/2}` (it lands on `n^{-1/3}` to grid precision for n=4,8,16,27), or if
  bare impedance shows an interior optimum (it is strictly monotone in radius —
  checked), or if a finer grid flips Part C's separation directions (Beta < Alpha
  is stable across floors 0.05–0.20).

## Artifacts

- `models/wbe_objective_selection.py` — the WBE dissipation functional
  (`BranchingTree.total_impedance` / `.total_volume` / `.constrained_dissipation`
  / `.metabolic_exponent`), the Gate-1 optimum classifier
  (`check_dissipation_optimum`), the Gate-2 branch-loading check
  (`check_branch_loading`), the coverage-constrained re-pose
  (`check_coverage_constrained_minimax`), and the combined
  `run_selection_principle`.
- `tests/test_wbe_objective_selection.py` — 22 real checks (green): dissipation
  optimum is area-increasing not area-preserving (n=4,8,16,27); optimum gives
  a=1 not 3/4; area-preserving ratios give exactly 3/4 (n up to 64); bare
  impedance has no interior optimum; total-cost loads all branches; minimax
  abandons the slow branch (reproduces T227); coverage-floored minimax separates
  and loads all branches; two gates not jointly satisfied by one principle.
- `results/wbe-selection/T233-wbe-selection-v0.1-run.txt` — recorded run.
- Reuses `models/mti_wbe_continuum.py` and `models/mti_cflow_solver.py`; does
  NOT touch kappa / sheaf-h1 / functor / d1cat-colimit files.

## Next Proof / Computation Step

1. Build the **coverage-constrained WBE delivery model**: state the
   service/coverage requirement physically (terminal-reachability within a
   delivery-time bound) and argue it is WBE-native, not a convenience floor.
   Re-run the separation screen under it for both total-cost and minimax; if
   the separation is objective-invariant under the native constraint, MTI's
   metric-temporal content is no longer objective-dependent.
2. Independently, supply (or cite) a **domain-native justification for the
   area-preserving condition** (impedance matching / minimal pulse reflection)
   that singles out `n^{-1/2}` and hence the 3/4 exponent, decoupling the 3/4
   calibration from the delivery-objective selection.
3. Only if BOTH the delivery separation (step 1) and the 3/4 calibration
   (step 2) hold under domain-native inputs does MTI promote past
   PARTIALLY_SUPPORTED; otherwise it stays partial with the blocker now split
   into these two named, independent sub-objects.

## Registered Status

T233 RUN as of 2026-06-25. Implementation, results, and 22 green checks under
the worker's slug namespace (`models/wbe_objective_selection.py`,
`tests/test_wbe_objective_selection.py`,
`results/wbe-selection/T233-wbe-selection-v0.1-run.txt`). Does not edit kappa,
sheaf-H1, functor, or d1cat-colimit files; does not edit CLAIM-LEDGER.md,
ROADMAP.md, or TESTS.md.
