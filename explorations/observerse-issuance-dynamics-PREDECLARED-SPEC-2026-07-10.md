# PREDECLARED SPEC: observerse issuance dynamics -- are goals, holonomy, and deflation load-bearing?

2026-07-10, predeclared BEFORE building/running (committed alone; results separate). Screen grade.
Tests Joe's reframe of records-as-rows: goal-driven observers with memory issue new structure to keep
the observerse (Y14) from collapsing into a finite game; multi-observer holonomy supplies coherence
(space); issuance is consistent-but-deflationary for a positive-sum infinite game. Instantiates the
repo's optimal-issuance-rate curve `lambda*(s) = argmax_lambda [N - C - K]`
(`explorations/explorer-optimal-issuance-rate-curve-2026-06-22.md`) with the FULL structure -- goals +
holonomy + deflation -- rather than the single-causet reduction. Holography (Y14->X4) and chirality are
sequenced as the follow-on, NOT dropped.

## The four sharp, falsifiable predictions (fixed)

- **P1 -- interior optimum.** A finite issuance rate `lambda*` sustains coherent novelty strictly better
  than both `lambda -> 0` (freeze: closed rearrangement, the chain) and `lambda -> large` (fragment:
  incoherent branching). FALSIFIED if sustained coherent-novelty is monotone in lambda (no interior peak).
- **P2 -- holonomy necessity.** Holonomy-coupled observers converge to ONE coherent shared structure
  (bounded inter-observer coherence cost C); independent observers FRAGMENT into disjoint structures
  (C grows / no shared geometry). FALSIFIED if independent observers are just as coherent.
- **P3 -- goal necessity.** Goal-directed issuance sustains more coherent novelty than random-direction
  issuance at equal rate. FALSIFIED if random does as well (goals are decoration).
- **P4 -- deflationary.** Diminishing-but-persistent (deflationary) issuance sustains longer / keeps C
  bounded compared to a constant rate that collapses earlier. FALSIFIED if constant sustains as long.

## The model (fixed)

- Observerse `R^D`, `D=12`. `K=6` observers. Each observer `k`: a unit goal `g_k in R^D`, a frame
  `O_k in O(D)` (its gauge; starts near identity), and a frontier (its latest issued point).
- **Issuance** (per tick `t`, per observer, step scale `lambda`): new point
  `x = frontier_k + lambda * (alpha * g_k  +  beta_t * fresh)`, where `fresh` is a unit direction
  ORTHOGONAL to the current structure span (genuine novelty), `alpha` the goal pull. Deflationary:
  `beta_t = beta0 / (1 + t/tau)` (diminishing, never zero). Constant-rate arm: `beta_t = beta0`.
  Random-goal arm: `g_k` re-randomized each tick (no persistent goal).
- **Holonomy reconciliation** (coupled arm): each tick, observers rotate frames toward the running
  consensus frame on overlapping structure (Karcher-style step on O(D)); inter-observer coherence cost
  `C = sum_{k<j} ||O_k - O_j||_F`. The holonomy is `O_k O_j^T`; loop holonomy != I is curvature.
  Independent arm: frames evolve without reconciliation.
- **Metrics per tick:** `N(t)` = novel coherent structure added (magnitude of the fresh-orthogonal
  component that is reconcilable across observers); `C(t)` = inter-observer coherence cost; a **shared
  structure** `G(t)` = elements agreed across observers in the consensus frame.
- **Collapse indicators:** freeze = `N(t) -> 0` (finite game); fragment = `C(t)` unbounded.

## The grid + arms (fixed)

- `lambda in {0.05, 0.15, 0.4, 1.0, 2.5}` (rate sweep for P1).
- Factorial for P2-P4: holonomy in {coupled, independent} x goals in {directed, random} x
  rate in {deflationary, constant}.
- `T = 150` ticks; 8 seeds/cell; report seed-means.

## Success / falsification criteria (fixed)

- **Sustained coherent novelty** `SCN` = mean `N(t)` over the last third of `T`, among reconciled
  structure only. The primary quantity (MTI-aware: NOT a dimension estimate).
- **P1 holds** iff `argmax_lambda SCN` is interior (not the smallest or largest lambda) AND the peak
  `SCN` exceeds both endpoints by >= 25%.
- **P2 holds** iff coupled `C` stays bounded (final `C <= 2x` initial) while independent `C` grows
  (final `C >= 2x` initial) at `lambda*`.
- **P3 holds** iff directed `SCN` >= 1.25x random `SCN` at `lambda*` (coupled, deflationary).
- **P4 holds** iff deflationary sustains `N(t) > 0` over the last third while constant collapses
  (`N -> 0` or `C` unbounded) earlier, at `lambda*`.
- **Overall verdict:** how many of P1-P4 hold names which of Joe's ingredients are load-bearing vs
  decoration. All four = full model validated; a subset = an honest map of what matters.

## Honest caveats (fixed)

- This is a screen-grade DYNAMICAL model of the lambda*-curve, not a derivation of spacetime, a metric,
  or GU. A multi-agent sim can be tuned; the discipline is the predeclared falsifiable P1-P4 with nulls
  (independent / random / constant arms), and honest reporting of which FAIL.
- Diagnostics are novelty/coherence (N, C), not MM-dimension (MTI: dimension is blind to this structure).
- Holography (Y14->X4 boundary reconstruction) and chirality (edge modes) are the sequenced follow-on;
  preserved as nuance, not tested here.

## Discipline

Predictions, model, grid, and criteria FROZEN by this commit. Experiment
(`models/observerse_issuance_dynamics.py`) + results committed separately; verdict is whatever P1-P4
return.
